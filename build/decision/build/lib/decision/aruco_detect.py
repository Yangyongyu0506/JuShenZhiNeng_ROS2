import rclpy
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ArucoDetectNode(Node):
    def __init__(self):
        super().__init__('aruco_detect_node')
        self.bridge = CvBridge()
        self._sub = self.create_subscription(Image, 'camera', self.image_callback, 10)

        # arUco settings
        aruco_dict_type = cv2.aruco.DICT_6X6_250
        aruco_dict = cv2.aruco.getPredefinedDictionary(aruco_dict_type)
        aruco_params = cv2.aruco.DetectorParameters()
        self.aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

        self.get_logger().info('Aruco Detect Node has been started.')

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        corners, ids, _ = self.aruco_detector.detectMarkers(cv_image)
        if ids is not None:
            self.get_logger().info(f'Detected ArUco markers with IDs: {ids.flatten()}')
        else:
            self.get_logger().info('No ArUco markers detected.')
        
def main(args=None):
    rclpy.init()
    aruco_detect_node = ArucoDetectNode()
    rclpy.spin(aruco_detect_node)
    aruco_detect_node.destroy_node()
    rclpy.shutdown()