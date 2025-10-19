import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from hiwonder_sdk import Sonar

class UltrasonicNode(Node):
    def __init__(self):
        Node.__init__(self, 'ultrasonic_pub')
        self.pub = self.create_publisher(Range, 'sonar', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.sonar = Sonar.Sonar()
        self.get_logger().info('Sonar Node has been started.')
    
    def timer_callback(self):
        dist = self.sonar.getDistance()
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'ultrasonic_link'
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = math.radians(15)  # Example FOV
        msg.min_range = 0.01  # Minimum range in meters
        msg.max_range = 5.0   # Maximum range in meters
        msg.range = dist / 1000.0  # Convert mm to meters
        self.get_logger().info(f'sonar range: {msg.range} m')
        self.pub.publish(msg)

def main():
    try:
        rclpy.init()
        my_sonar_node = UltrasonicNode()
        rclpy.spin(my_sonar_node)
    finally:
        my_sonar_node.destroy_node()
        rclpy.shutdown()

if 'name' == '__main__':
    main()