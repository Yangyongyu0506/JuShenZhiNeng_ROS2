import rclpy
from rclpy.node import Node
from hiwonder_sdk import Board
from std_msgs.msg import Int16

class BatteryADCNode(Node):
    def __init__(self):
        Node.__init__(self, 'batteryadc_pub')
        self.pub = self.create_publisher(Int16, 'batteryadc', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int16()
        msg.data = Board.getBattery()
        self.pub.publish(msg)
        self.get_logger().info(f'battery adc: {msg.data}')

def main():
    rclpy.init()
    batteryadc_node = BatteryADCNode()
    rclpy.spin(batteryadc_node)
    batteryadc_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()