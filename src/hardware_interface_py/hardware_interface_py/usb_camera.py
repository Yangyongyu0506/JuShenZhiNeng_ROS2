import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class CameraNode(Node):
    def __init__(self):
        Node.__init__(self, 'camera_pub')
        self.declare_parameter('video_id', 1)
        self.declare_parameter('video_freq', 10)
        self.declare_parameter('cam_topic', 'camera')
        cam_index = self.get_parameter('video_id').value
        freq = self.get_parameter('video_freq').value
        topic_name = self.get_parameter('cam_topic').value
        self.pub = self.create_publisher(Image, topic_name, 10)
        self.timer = self.create_timer(1 / freq, self.timer_callback)
        self.cap = cv2.VideoCapture(cam_index, cv2.CAP_V4L2) # Our resolution is 640x480
        self.bridge = CvBridge()
        self.get_logger().info('Camera Node has been started.')

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error('Failed to capture image')
            return
        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        msg.height = frame.shape[0]
        msg.width = frame.shape[1]
        msg.step = frame.strides[0]
        msg.header.stamp = self.get_clock().now().to_msg()
        self.pub.publish(msg)
        self.get_logger().debug('Image captured')

    def destroy_node(self):
        self.cap.release()
        super().destroy_node()

def main(args=None):
    rclpy.init()
    my_cam_node = CameraNode()
    rclpy.spin(my_cam_node)
    my_cam_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()