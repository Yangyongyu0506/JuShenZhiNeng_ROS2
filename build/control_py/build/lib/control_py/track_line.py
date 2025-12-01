import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32
import yaml
import os
from ament_index_python.packages import get_package_share_directory

class TrackLineNode(Node):
    def __init__(self):
        super().__init__('track_line_node')
        # Init color config
        track_color = self.declare_parameter('track_color', 'black').value
        track_method = self.declare_parameter('track_method', 'COM').value # Offer an API to select the method
        color_config_path = os.path.join(
            get_package_share_directory('control_py'),
            'config',
            'color_lim_lab.yaml'
        )
        with open(color_config_path) as f:
            lab_config = yaml.safe_load(f)
        self.color_lab_threshold = lab_config[track_color]
        # Init PID
        self.Kp = 0.0001
        self.Kd = 0.0
        self.Ki = 0.0
        self.I = 0
        self.error_x_prev = 0
        # Init CvBridge
        self.bridge = CvBridge()
        # Init ROS2 components
        self.sub_img = self.create_subscription(Image, 'camera', self.sub_image_callback, 10)
        self.pub_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.pub_debugimg = self.create_publisher(Image, 'debug_image', 10)
        self.pub_error_x = self.create_publisher(Int32, 'error_x', 10)
        # Done
        self.get_logger().info("Track line node has been created")

    def sub_image_callback(self, msg: Image):
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        roi = cv_img[:, int(cv_img.shape[1] * 0.1):int(cv_img.shape[1] * 0.9)]
        # roi = cv_img[int(cv_img.shape[0] * 0.6):]
        # roi = cv_img[:int(cv_img.shape[0] * 0.8), int(cv_img.shape[1] * 0.1):int(cv_img.shape[1] * 0.9)]
        # roi = cv_img
        lab_img = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)
        mask = cv2.inRange(lab_img, tuple(self.color_lab_threshold['min']), tuple(self.color_lab_threshold['max']))
        mask = cv2.dilate(mask, kernel := np.ones((8, 8), np.uint8))
        debug_img = self.bridge.cv2_to_imgmsg(mask, encoding="mono8")
        self.pub_debugimg.publish(debug_img)
        
        # # Approach V1: Find the center of mass of the white area
        # contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # if contours:
        #     largest_contour = max(contours, key=cv2.contourArea)
        #     M = cv2.moments(largest_contour)
        #     if M['m00'] != 0:
        #         cx = int(M['m10'] / M['m00'])
        #         error_x = cx - (cv_img.shape[1] // 2)
        #         twist_msg = Twist()
        #         twist_msg.linear.x = 0.05
        #         if not hasattr(self, 'error_x_prev'):
        #             omega = -float(error_x) * self.Kp - self.I * self.Ki
        #         else:
        #             omega = -error_x * self.Kp - (error_x - self.error_x_prev) * self.Kd - self.I * self.Ki
        #         twist_msg.angular.z = np.clip(omega, -10, 10)
        #         self.error_x_prev = error_x
        #         self.I += error_x
        #         self.pub_vel.publish(twist_msg)
        #         return
            
        # # Approach V2: Weighted center of mass
        # H, W = mask.shape
        # center = W // 2

        # xs = np.arange(W)
        # dx = (xs - center)
        # abs_dx = np.abs(dx)

        # weights = mask.astype(np.float32) * dx * abs_dx
        # weighted_sum = weights.sum()
        # count = mask.sum()
        # if count != 0:
        #     error_x = weighted_sum / count
        #     twist_msg = Twist()
        #     if np.abs(error_x) < 60000:
        #         twist_msg.linear.x = 0.05
        #     else:
        #         twist_msg.linear.x = 0.02
        #     if not hasattr(self, 'error_x_prev'):
        #         omega = -float(error_x) * self.Kp - self.I * self.Ki
        #     else:
        #         omega = -error_x * self.Kp - (error_x - self.error_x_prev) * self.Kd - self.I * self.Ki
        #     twist_msg.angular.z = np.clip(omega, -10, 10)
        #     self.error_x_prev = error_x
        #     self.I += error_x
        #     self.pub_vel.publish(twist_msg)
        #     self.pub_error_x.publish(Int32(data=int(error_x)))
        #     return
        # else:
        #     self.pub_vel.publish(Twist())  # Stop if no line is detected
        #     self.get_logger().info("No line detected, the robot has stopped.")

        # Approach V3: Scanline method
        H, W = mask.shape
        centers = []

        # 从底部往上 取 5 条扫描线
        scan_rows = [int(H * r) for r in [0.9, 0.7, 0.5, 0.3, 0.1]]

        for row in scan_rows:
            line = mask[row]
            idx = np.where(line > 0)[0]

            if len(idx) > 10:
                left = idx[0]
                right = idx[-1]
                center = (left + right) // 2
                centers.append(center)

        if len(centers) == 0:
            # 找不到线 → 停车
            self.pub_vel.publish(Twist())
            return

        # 得到最终误差（多行平均比质心稳很多）
        center_avg = int(np.mean(centers))
        error_x = center_avg - W//2

        # ---------- 控制 ----------
        twist = Twist()
        twist.linear.x = 0.02
        twist.angular.z = -error_x * self.Kp - (error_x - self.error_x_prev) * self.Kd  # 参数可调
        self.error_x_prev = error_x
        self.pub_vel.publish(twist)

def main():
    rclpy.init()
    track_line_node = TrackLineNode()
    rclpy.spin(track_line_node)
    # track_line_node.destroy_node()
    rclpy.shutdown()