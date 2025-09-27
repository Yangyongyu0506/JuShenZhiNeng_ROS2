import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class CameraNode(Node):
    def __init__(self, cam_index = 0):
        Node.__init__(self, 'camera_pub')
        self.pub = self.create_publisher(Image, 'camera/image_raw', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.cap = cv2.VideoCapture(cam_index, cv2.CAP_V4L2)
        self.bridge = CvBridge()

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
        self.get_logger().info('Image captured')

def main(args=None):
    rclpy.init()
    my_cam_node = CameraNode()
    rclpy.spin(my_cam_node)
    my_cam_node.cap.release()
    my_cam_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()