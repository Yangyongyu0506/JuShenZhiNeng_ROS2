import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import yaml
import os
from ament_index_python.packages import get_package_share_directory

class ColorDetectNode(Node):
    def __init__(self):
        super().__init__('color_detect_node')
        self.bridge = CvBridge()
        self._sub = self.create_subscription(Image, 'camera', self.image_callback, 10)
        config_path = os.path.join(
            get_package_share_directory('decision'),
            'data',
            'color_config.yaml'
        )
        with open(config_path, 'r') as f:
            self.lab_config = yaml.safe_load(f)
        self.get_logger().info('Color Detect Node has been started.')

    def image_callback(self, msg: Image):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        gb_image = cv2.GaussianBlur(cv_image, (3, 3), 3)
        lab_image = cv2.cvtColor(gb_image, cv2.COLOR_BGR2LAB) # Convert to LAB color space

        for color in ['red', 'green', 'blue']:
            mask = cv2.inRange(
                lab_image,
                (self.lab_config[color]['min'][0],
                self.lab_config[color]['min'][1],
                self.lab_config[color]['min'][2]),
                (self.lab_config[color]['max'][0],
                self.lab_config[color]['max'][1],
                self.lab_config[color]['max'][2])
            )
            opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel := np.ones((5, 5), np.uint8))  # 开运算
            closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)  # 闭运算
            contours = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]  # 找出轮廓
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                if cv2.contourArea(largest_contour) > 2500:
                    self.get_logger().info(f'{color.upper()}')

def main(args=None):
    rclpy.init()
    color_detect_node = ColorDetectNode()
    rclpy.spin(color_detect_node)
    color_detect_node.destroy_node()
    rclpy.shutdown()