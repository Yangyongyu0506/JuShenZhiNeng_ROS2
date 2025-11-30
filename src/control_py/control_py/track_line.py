import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist
import yaml
import os
from ament_index_python.packages import get_package_share_directory

class TrackLineNode(Node):
    def __init__(self): # 'r' for red line, 'k' for black line
        super().__init__('track_line_node')
        # Init color config
        track_type = self.declare_parameter('track_type', 'k').value
        color_config_path = os.path.join(
            get_package_share_directory('control_py'),
            'config',
            'color_lim_lab.yaml'
        )
        with open(color_config_path) as f:
            lab_config = yaml.safe_load(f)
        match track_type:
            case 'r':
                self.color_lab_threshold = lab_config['red']
                self.get_logger().info('Our mission is to track the red line')
            case 'k':
                self.color_lab_threshold = lab_config['black']
                self.get_logger().info('Our mission is to track the black line')
        # Init PID
        self.Kp = 0.001
        self.Kd = 0.0
        self.Ki = 0.01
        self.I = 0
        # Init CvBridge
        self.bridge = CvBridge()
        # Init ROS2 components
        self.sub_img = self.create_subscription(Image, 'camera', self.sub_image_callback, 10)
        self.pub_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.pub_debugimg = self.create_publisher(Image, 'debug_image', 10)
        # Done
        self.get_logger().info("Track line node has been created")

    def sub_image_callback(self, msg: Image):
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        lab_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2LAB)
        mask = cv2.inRange(lab_img, tuple(self.color_lab_threshold['min']), tuple(self.color_lab_threshold['max']))
        mask = cv2.dilate(mask, kernel := np.ones((8, 8), np.uint8))
        debug_img = self.bridge.cv2_to_imgmsg(mask, encoding="mono8")
        self.pub_debugimg.publish(debug_img)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                error_x = cx - (cv_img.shape[1] // 2)
                twist_msg = Twist()
                # 匹配停车标志
                # epsilon = 0.02 * cv2.arcLength(largest_contour, True)
                # approx = cv2.approxPolyDP(largest_contour, epsilon, True)
                # if len(approx) >= 8 and np.sum(mask[:50, :]) < 5:
                #     self._vel_pub.publish(twist_msg)
                #     self.get_logger().info(f"Stop sign detected {len(approx)}, the robot has stopped.")
                #     self.destroy_node()
                #     rclpy.shutdown()
                #     return
                twist_msg.linear.x = 50 / (error_x ** 2 + 1)
                if not hasattr(self, 'error_x_prev'):
                    omega = -float(error_x) * self.Kp - self.I * self.Ki
                else:
                    omega = -error_x * self.Kp - (error_x - self.error_x_prev) * self.Kd - self.I * self.Ki
                twist_msg.angular.z = np.clip(omega, -2, 2)
                self.error_x_prev = error_x
                self.I += error_x
                self.pub_vel.publish(twist_msg)
                return
        self.pub_vel.publish(Twist())  # Stop if no line is detected
        self.get_logger().info("No line detected, the robot has stopped.")

def main():
    rclpy.init()
    track_line_node = TrackLineNode()
    rclpy.spin(track_line_node)
    # track_line_node.destroy_node()
    rclpy.shutdown()