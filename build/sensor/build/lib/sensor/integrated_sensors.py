import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
from hiwonder_sdk import Sonar
from hiwonder_sdk import Board
from std_msgs.msg import Int16
from sensor_msgs.msg import Range
import math

class IntegratedSensorsNode(Node):
    def __init__(self):
        super().__init__('integral_sensors')
        self._cap = cv2.VideoCapture(0, cv2.CAP_V4L2) # Our resolution is 640x480
        self._sonar = Sonar.Sonar()

        self._timer_cam = self.create_timer(0.1, self.cam_callback)
        self._timer_sonar = self.create_timer(0.1, self.sonar_callback)
        self._timer_bat = self.create_timer(5, self.bat_callback)

        self._cam_pub = self.create_publisher(Image, 'camera', 10)
        self._sonar_pub = self.create_publisher(Range, 'sonar', 10)
        self._bat_pub = self.create_publisher(Int16, 'battery', 10)
        self.get_logger().info('Integrated Senor Node has been started.')

        self.cvbridge = CvBridge()

    def cam_callback(self):
        ret, frame = self._cap.read()
        if not ret:
            self.get_logger().error('Failed to capture image')
            return
        msg = self.cvbridge.cv2_to_imgmsg(cv2.flip(frame, -1), encoding="bgr8")
        msg.height = frame.shape[0]
        msg.width = frame.shape[1]
        msg.step = frame.strides[0]
        msg.header.stamp = self.get_clock().now().to_msg()
        self._cam_pub.publish(msg)
        self.get_logger().info('Image captured')

    def sonar_callback(self):
        dist = self._sonar.getDistance()
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'ultrasonic_link'
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = math.radians(15)  # Example FOV
        msg.min_range = 0.01  # Minimum range in meters
        msg.max_range = 5.0   # Maximum range in meters
        msg.range = dist / 1000.0  # Convert mm to meters
        self._sonar_pub.publish(msg)
        self.get_logger().info(f'sonar range: {msg.range} m')

    def bat_callback(self):
        msg = Int16()
        msg.data = Board.getBattery()
        self._bat_pub.publish(msg)
        self.get_logger().info(f'battery adc: {msg.data}')

def main():
    rclpy.init()
    integrated_sensors_node = IntegratedSensorsNode()
    try:
        rclpy.spin(integrated_sensors_node)
    finally:
        integrated_sensors_node._cap.release()
        integrated_sensors_node.destroy_node()
        rclpy.shutdown()