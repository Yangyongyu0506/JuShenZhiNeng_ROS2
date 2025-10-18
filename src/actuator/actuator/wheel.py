import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from hiwonder_sdk import mecanum

class MecanumWheelNode(Node):
    def __init__(self):
        super().__init__('mecanum_wheel_node')
        self.sub = self.create_subscription(Twist, 'turtle1/cmd_vel', self.cmd_vel_callback, 10)
        self.get_logger().info('Mecanum Wheel Node has been started.')
        self.chassis = mecanum.MecanumChassis()

    def cmd_vel_callback(self, msg):
        self.get_logger().info(f'Get velocity command: x: {msg.linear.x}, y: {msg.linear.y}, omega: {msg.angular.z}')
        v, d = self.chassis.translation(-msg.linear.y * 1000, msg.linear.x * 1000, fake=True)
        self.chassis.set_velocity(v, d, -msg.angular.z)
def main():
    try:
        rclpy.init()
        mynode = MecanumWheelNode()
        rclpy.spin(mynode)
    finally:
        mynode.chassis.reset_motors()
        mynode.get_logger().info('Mecanum Wheel Node has been killed.')
        mynode.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()