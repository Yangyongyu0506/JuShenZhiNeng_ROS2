import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
from smbus2 import SMBus, i2c_msg
import numpy as np

from trajectory_msgs.msg import JointTrajectory
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from std_msgs.msg import ColorRGBA


class I2CNode(Node):
    """
    一个统一的 ROS2 I2C 驱动节点，支持以下硬件：
    1. 超声波测距模组（I2C）
    2. 机械臂舵机控制器（I2C）
    3. 麦克纳姆轮电机控制器（I2C）
    4. LED 颜色控制（内置于超声波模块）

    订阅：
        - /arm/joint_trajectory (JointTrajectory): 控制机械臂轨迹
        - /cmd_vel (Twist): 控制移动底盘
        - /ultrasonic/color (ColorRGBA): 设置超声波模块的 RGB LED

    发布：
        - ultrasonic/range (Range): 发送超声波距离数据
    """

    def __init__(self):
        super().__init__('i2c_node')

        # ==============================
        #       加载参数
        # ==============================

        # I2C 设备地址与 Bus 号
        self.declare_parameter('i2c_bus', 7)
        self.declare_parameter('sonar_i2c_addr', 0x77)   # 超声波测距模块
        self.declare_parameter('arm_i2c_addr', 0x7A)     # 舵机总线控制器
        self.declare_parameter('mecanum_i2c_addr', 0x7A) # 麦克纳姆轮控制器（用户自定义）

        self.sonar_addr = self.get_parameter('sonar_i2c_addr').value
        self.arm_addr = self.get_parameter('arm_i2c_addr').value
        self.mecanum_addr = self.get_parameter('mecanum_i2c_addr').value
        i2c_bus = self.get_parameter('i2c_bus').value

        # 打开 I2C bus
        self.bus = SMBus(i2c_bus)

        # Topic 名称配置
        self.declare_parameter('sonar_topic', 'ultrasonic/range')
        self.declare_parameter('cmd_vel_topic', 'cmd_vel')
        self.declare_parameter('joint_trajectory_topic', 'arm/joint_trajectory')
        self.declare_parameter('led_topic', 'ultrasonic/color')

        sonar_topic = self.get_parameter('sonar_topic').value
        joint_trajectory_topic = self.get_parameter('joint_trajectory_topic').value
        cmd_vel_topic = self.get_parameter('cmd_vel_topic').value
        led_topic = self.get_parameter('led_topic').value

        # 舵机名称映射配置（ROS 逻辑名称 -> 实际硬件 ID）
        self.declare_parameter('servo_names', ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5'])
        self.declare_parameter('servo_sequence', [6, 2, 4, 3, 1])

        servo_names = self.get_parameter('servo_names').value
        servo_sequence = self.get_parameter('servo_sequence').value

        # 建立名称到ID的映射表
        self.arm_name2id = {name: seq for name, seq in zip(servo_names, servo_sequence)}

        # 机械臂启动初始化位置
        self.arm_set([90, 60, 180, 0, 90], servo_sequence, 'deg')

        # LED初始化
        self.sonar_set_led((0, 0, 0))

        # ==============================
        #          发布与定时器
        # ==============================

        # 设置超声波发布频率
        self.declare_parameter('sonar_freq', 20)
        sonar_freq = self.get_parameter('sonar_freq').value

        # 发布超声波测距数据
        self.pub_sonar = self.create_publisher(Range, sonar_topic, 10)

        # 定时器：周期性读取并发布超声波数据
        self.timer_sonar = self.create_timer(1.0 / sonar_freq, self.timer_sonar_callback)

        # ==============================
        #             订阅者
        # ==============================

        # 机械臂轨迹控制
        self.sub_arm = self.create_subscription(
            JointTrajectory,
            joint_trajectory_topic,
            self.sub_traj_callback,
            10
        )

        # 麦克纳姆底盘速度控制
        self.sub_vel = self.create_subscription(
            Twist,
            cmd_vel_topic,
            self.sub_vel_callback,
            10
        )

        # 超声波 RGB LED 控制
        self.sub_led = self.create_subscription(
            ColorRGBA,
            led_topic,
            self.sub_led_callback,
            10
        )

        self.get_logger().info("I2C node has been started successfully.")

    # ==========================================================
    #                      LED 控制部分
    # ==========================================================

    def sonar_set_led(self, color: tuple):
        """
        设置超声波模块上的 RGB LED（两个 LED 灯同时设置）。
        硬件协议：每个 LED 用 3 个寄存器 (R,G,B) 控制
            地址 = base + 3 * led_index

        color: (r, g, b) in [0.0 ~ 1.0]
        """
        r = int(color[0] * 255)
        g = int(color[1] * 255)
        b = int(color[2] * 255)

        for i in range(1, 3):  # LED index 1~2
            self.bus.write_byte_data(self.sonar_addr, 3 * i, r)
            self.bus.write_byte_data(self.sonar_addr, 3 * i + 1, g)
            self.bus.write_byte_data(self.sonar_addr, 3 * i + 2, b)

    def sub_led_callback(self, msg: ColorRGBA):
        """
        LED 控制 Topic 回调。
        将 ColorRGBA 映射到 RGB LED（忽略 alpha）。
        """
        self.sonar_set_led((msg.r, msg.g, msg.b))

    # ==========================================================
    #                   超声波测距（I2C）
    # ==========================================================

    def sonar_get_dist(self):
        """
        读取超声波测距传感器数据。
        协议：
            1. 发送触发字节 [0]
            2. 模块返回 2 字节整型（小端）单位 mm
        """
        # 触发测量
        msg = i2c_msg.write(self.sonar_addr, [0])
        self.bus.i2c_rdwr(msg)

        # 读取 2 字节
        read = i2c_msg.read(self.sonar_addr, 2)
        self.bus.i2c_rdwr(read)

        dist_mm = int.from_bytes(bytes(list(read)), 'little')
        return dist_mm / 1000.0  # 转换为米

    def sonar_publish(self, timestamp):
        """发布超声波测距数据。"""
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
        """定时器：读取测距并发布。"""
        timestamp = self.get_clock().now().to_msg()
        self.sonar_publish(timestamp)

    # ==========================================================
    #                   机械臂（舵机总线控制）
    # ==========================================================

    def arm_map_sequence(self, joint_names):
        """将 ROS 关节名称映射为硬件ID序列。"""
        return [self.arm_name2id[name] for name in joint_names if name in self.arm_name2id]

    def arm_set(self, angles, sequence, angle_unit='rad', time_delay_ms=0):
        """
        向舵机总线发送角度控制命令。

        angles: 角度列表（deg 或 rad）
        sequence: 舵机硬件ID
        time_delay_ms: 延时执行，控制动作速度（与舵机协议相关）
        """
        # rad → deg
        if angle_unit == 'rad':
            angles = np.rad2deg(angles)

        # 限幅
        angles = np.clip(angles, 0, 180)

        # 角度 → PWM (500–2500us)
        pwms = (angles / 180.0) * 2000 + 500

        # 舵机协议数据包格式：
        # [40, 5, delay_low, delay_high, servo_id, pwm_low, pwm_high, ...]
        buf = [40, 5] + list(time_delay_ms.to_bytes(2, 'little'))

        for seq, pwm in zip(sequence, pwms):
            buf.append(seq)
            buf += list(int(pwm).to_bytes(2, 'little'))

        msg = i2c_msg.write(self.arm_addr, buf)
        self.bus.i2c_rdwr(msg)

    def sub_traj_callback(self, msg: JointTrajectory):
        """
        JointTrajectory 回调。
        支持执行多个 trajectory point。
        """
        if len(msg.points) == 0:
            self.get_logger().warn("JointTrajectory contains no points.")
            return

        for point in msg.points:

            if len(point.positions) != len(msg.joint_names):
                self.get_logger().error("Positions length does not match joint_names length!")
                return

            angles = point.positions
            seq = self.arm_map_sequence(msg.joint_names)

            time_delay_ms = point.time_from_start.sec * 1000

            self.arm_set(angles, seq, 'rad', time_delay_ms)

    # ==========================================================
    #                    麦克纳姆轮（底盘）
    # ==========================================================

    def mecanum_set_motor(self, index, speed):
        """
        发送单个麦克纳姆轮电机速度。
        index: 1~4
        speed: [-100, 100] 百分比
        """
        # 电机正反方向补偿
        if index not in (2, 4):
            speed = -speed

        index -= 1
        speed = max(-100, min(100, speed))

        reg = 31 + index  # 寄存器地址

        msg = i2c_msg.write(self.mecanum_addr, [reg, speed.to_bytes(1, 'little', signed=True)[0]])
        self.bus.i2c_rdwr(msg)

    def mecanum_set_vel(self, vx_ms, gz_rs):
        """
        Twist → 4个轮速控制。
        简化的差速模型。
        """
        vx_mms = vx_ms * 1000
        robot_radius_mm = 67 + 59
        vr_mms = gz_rs * robot_radius_mm

        self.mecanum_set_motor(1, int(vx_mms - vr_mms))
        self.mecanum_set_motor(2, int(vx_mms + vr_mms))
        self.mecanum_set_motor(3, int(vx_mms - vr_mms))
        self.mecanum_set_motor(4, int(vx_mms + vr_mms))

    def sub_vel_callback(self, msg: Twist):
        """cmd_vel 回调。"""
        self.mecanum_set_vel(msg.linear.x, msg.angular.z)


def main(args=None):
    rclpy.init(args=args)

    i2c_node = I2CNode()
    executor = SingleThreadedExecutor()
    executor.add_node(i2c_node)

    executor.spin()

    i2c_node.destroy_node()
    rclpy.shutdown()
