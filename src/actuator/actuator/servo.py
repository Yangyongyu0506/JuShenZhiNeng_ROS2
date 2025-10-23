import rclpy
from rclpy.node import Node
from my_interfaces.srv import Allservos
from smbus2 import SMBus, i2c_msg
from threading import Lock
import numpy as np

class ServoControlNode(Node):
    """
    真是被坑惨了。驱动舵机千万不要用setPWMServoAngle这种弱智函数，一定要直接操作pwm!!!
    SB hiwonder凸T皿T凸
    """
    def __init__(self):
        super().__init__('servo_control_node')
        self._bus = SMBus(7)  # Assuming bus 7 for I2C
        self._lock = Lock()
        self.sequence = [6, 5, 4, 3, 1]  # Servo IDs
        self.declare_parameter('action_delay_ms', 1000)
        self._action_delay_ms = self.get_parameter('action_delay_ms').get_parameter_value().integer_value
        self.setAllServos(np.array([90, 60, 180, 0, 180], dtype=np.int16))  # Initial positions
        self._srv = self.create_service(Allservos, 'set_all_servos', self.set_all_servos_callback)
        self.get_logger().info('Servo Control Node has been started, waiting for clients...')

    def setAllServos(self, angles: np.ndarray):
        # convert angles from degrees to pwm widths
        angles = np.clip(angles, 0, 180)  # Clamp angles to valid range
        pwms = ((angles / 180.0) * 2000 + 500) # Convert to PWM width
        buf = [40, 5] + list(self._action_delay_ms.to_bytes(2, 'little'))
        data = zip(self.sequence, pwms)
        for (seq, pwm) in data:
            buf.append(seq)
            buf += list(int(pwm).to_bytes(2, 'little'))
        with self._lock:
            try:
                msg = i2c_msg.write(0x7A, buf)
                self._bus.i2c_rdwr(msg)
            except Exception as e:
                self.get_logger().error(f"Failed to set servo positions: {e}")

    def set_all_servos_callback(self, request, response):
        angles = np.array(request.angles, dtype=np.int16)
        self.setAllServos(angles)
        response.acknowledged = True
        self.get_logger().info(f'Set servos to angles: {angles.tolist()}')
        return response

def main():
    rclpy.init()
    servo_control_node = ServoControlNode()
    rclpy.spin(servo_control_node)
    servo_control_node.destroy_node()
    rclpy.shutdown()