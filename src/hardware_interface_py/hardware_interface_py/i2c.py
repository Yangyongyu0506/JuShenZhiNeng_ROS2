import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
from smbus2 import SMBus, i2c_msg
import numpy as np

from trajectory_msgs.msg import JointTrajectory
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

class I2CNode(Node):
    """
    A unified ROS2 I2C driver node that handles:
    1. Ultrasonic range sensor (I2C)
    2. Robot arm servo controller (I2C)
    3. Mecanum wheel motor controller (I2C)

    Subscribes:
        - /arm/joint_trajectory  (JointTrajectory)
        - /cmd_vel               (Twist)

    Publishes:
        - ultrasonic/range       (Range)
    """

    def __init__(self):
        super().__init__('i2c_node')

        # ==============================
        #       Parameter loading
        # ==============================

        # I2C device parameters
        self.declare_parameter('i2c_bus', 7)
        self.declare_parameter('sonar_i2c_addr', 0x77)
        self.declare_parameter('arm_i2c_addr', 0x7A)
        self.declare_parameter('mecanum_i2c_addr', 0x7A)  # (User should update)

        self.sonar_addr = self.get_parameter('sonar_i2c_addr').value
        self.arm_addr = self.get_parameter('arm_i2c_addr').value
        self.mecanum_addr = self.get_parameter('mecanum_i2c_addr').value
        i2c_bus = self.get_parameter('i2c_bus').value

        # Open I2C bus
        self.bus = SMBus(i2c_bus)

        # Topic parameters
        self.declare_parameter('sonar_topic', 'ultrasonic/range')
        self.declare_parameter('cmd_vel_topic', 'cmd_vel')
        self.declare_parameter('joint_trajectory_topic', 'arm/joint_trajectory')

        sonar_topic = self.get_parameter('sonar_topic').value
        joint_trajectory_topic = self.get_parameter('joint_trajectory_topic').value
        cmd_vel_topic = self.get_parameter('cmd_vel_topic').value

        # Arm servo mapping parameters
        # servo_names → logical names from ROS
        # servo_sequence → hardware ID for each servo
        self.declare_parameter('servo_names', ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5'])
        self.declare_parameter('servo_sequence', [6, 2, 4, 3, 1])

        servo_names = self.get_parameter('servo_names').value
        servo_sequence = self.get_parameter('servo_sequence').value

        # Build mapping for name → ID
        self.arm_name2id = {name: seq for name, seq in zip(servo_names, servo_sequence)}

        # Initialize mechanical arm at startup
        self.arm_set([90, 60, 180, 0, 90], servo_sequence, 'deg')

        # =====================================
        #           Timer + Publishers
        # =====================================

        # Sonar publish frequency
        self.declare_parameter('sonar_freq', 20)
        sonar_freq = self.get_parameter('sonar_freq').value

        # Publisher: ultrasonic range
        self.pub_sonar = self.create_publisher(Range, sonar_topic, 10)

        # Timer for sonar reading
        self.timer_sonar = self.create_timer(1.0 / sonar_freq, self.timer_sonar_callback)

        # =====================================
        #           Subscribers
        # =====================================

        # Arm trajectory controller
        self.sub_arm = self.create_subscription(
            JointTrajectory,
            joint_trajectory_topic,
            self.sub_traj_callback,
            10
        )

        # Mecanum wheel velocity controller
        self.sub_vel = self.create_subscription(
            Twist,
            cmd_vel_topic,
            self.sub_vel_callback,
            10
        )

        self.get_logger().info("I2C node has been started successfully.")

    # ==========================================================
    #                   ULTRASONIC SENSOR
    # ==========================================================

    def sonar_get_dist(self):
        """
        Read distance from ultrasonic sensor via I2C.
        The sensor returns 2 bytes representing distance in mm.
        """
        # Trigger measurement
        msg = i2c_msg.write(self.sonar_addr, [0])
        self.bus.i2c_rdwr(msg)

        # Read 2 bytes
        read = i2c_msg.read(self.sonar_addr, 2)
        self.bus.i2c_rdwr(read)

        # Convert mm → meters
        dist_mm = int.from_bytes(bytes(list(read)), 'little')
        return dist_mm / 1000.0

    def sonar_publish(self, timestamp):
        """
        Publish ultrasonic distance to ROS topic.
        """
        msg = Range()
        msg.header.stamp = timestamp
        msg.header.frame_id = 'ultrasonic_link'
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = np.deg2rad(30)
        msg.min_range = 0.01
        msg.max_range = 5.0
        msg.range = self.sonar_get_dist()

        self.pub_sonar.publish(msg)

    def timer_sonar_callback(self):
        """
        Timer callback: periodically read sonar and publish.
        """
        timestamp = self.get_clock().now().to_msg()
        self.sonar_publish(timestamp)

    # ==========================================================
    #                   ROBOT ARM (SERVO CONTROL)
    # ==========================================================

    def arm_map_sequence(self, joint_names):
        """
        Map logical ROS joint names → servo hardware IDs.
        """
        return [self.arm_name2id[name] for name in joint_names if name in self.arm_name2id]

    def arm_set(self, angles, sequence, angle_unit='rad', time_delay_ms=0):
        """
        Send servo PWM command packet via I2C.

        angles: list of angles (rad or deg)
        sequence: servo IDs
        time_delay_ms: execution delay for this command
        """
        # Convert to degrees if needed
        if angle_unit == 'rad':
            angles = np.rad2deg(angles)

        # Clamp to valid servo range
        angles = np.clip(angles, 0, 180)

        # Convert degrees → PWM width
        pwms = (angles / 180.0) * 2000 + 500

        # Command format:
        # [40, 5, delay_low, delay_high, servo_id, pwm_low, pwm_high, ...]
        buf = [40, 5] + list(time_delay_ms.to_bytes(2, 'little'))

        for seq, pwm in zip(sequence, pwms):
            buf.append(seq)
            buf += list(int(pwm).to_bytes(2, 'little'))

        # Send via I2C
        msg = i2c_msg.write(self.arm_addr, buf)
        self.bus.i2c_rdwr(msg)

    def sub_traj_callback(self, msg: JointTrajectory):
        """
        Handle JointTrajectory commands.
        Only the first trajectory point is used (standard for simple arms).
        """
        if len(msg.points) == 0:
            self.get_logger().warn("JointTrajectory contains no points.")
            return

        point = msg.points[0]

        if len(point.positions) != len(msg.joint_names):
            self.get_logger().error("Positions length does not match joint_names length!")
            return

        # Extract angle list + mapping
        angles = point.positions
        seq = self.arm_map_sequence(msg.joint_names)

        # Convert time_from_start (seconds → milliseconds)
        time_delay_ms = point.time_from_start.sec * 1000

        # Send to arm
        self.arm_set(angles, seq, 'rad', time_delay_ms)

    # ==========================================================
    #                 MECANUM WHEEL DRIVE
    # ==========================================================

    def mecanum_set_motor(self, index, speed):
        """
        Send a motor speed command via I2C.
        index: 1~4
        speed: -100 ~ +100 (%)
        """
        # Reverse rotation direction for some motors
        if index not in (2, 4):
            speed = -speed

        index -= 1  # motor index offset

        speed = max(-100, min(100, speed))  # clamp speed

        reg = 31 + index  # motor register base address

        msg = i2c_msg.write(self.mecanum_addr, [reg, speed.to_bytes(1, 'little', signed=True)[0]])
        self.bus.i2c_rdwr(msg)

    def mecanum_set_vel(self, vx_ms, gz_rs):
        """
        Convert Twist command (vx, gz) into mecanum motor speeds.
        vx_ms: forward m/s
        gz_rs: yaw angular speed rad/s
        """
        vx_mms = vx_ms * 1000
        robot_radius_mm = 67 + 59  # Example robot geometry
        vr_mms = gz_rs * robot_radius_mm

        # Basic differential drive model
        self.mecanum_set_motor(1, int(vx_mms - vr_mms))
        self.mecanum_set_motor(2, int(vx_mms + vr_mms))
        self.mecanum_set_motor(3, int(vx_mms - vr_mms))
        self.mecanum_set_motor(4, int(vx_mms + vr_mms))

    def sub_vel_callback(self, msg: Twist):
        """
        Handle incoming /cmd_vel messages.
        """
        self.mecanum_set_vel(msg.linear.x, msg.angular.z)


def main(args=None):
    rclpy.init(args=args)

    i2c_node = I2CNode()
    executor = SingleThreadedExecutor()
    executor.add_node(i2c_node)

    executor.spin()

    i2c_node.destroy_node()
    rclpy.shutdown()
