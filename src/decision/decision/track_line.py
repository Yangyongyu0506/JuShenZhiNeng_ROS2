import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist
from my_interfaces.srv import Allservos
import yaml
import os
from ament_index_python.packages import get_package_share_directory

class TrackLineNode(Node):
    def __init__(self, track_type: str ='k', Kp=0.05, Kd=0.2, Ki=0.001):
        super().__init__('track_line_node')
        config_path = os.path.join(
            get_package_share_directory('decision'),
            'data',
            'color_config.yaml'
        )
        with open(config_path, 'r') as f:
            lab_config = yaml.safe_load(f)
        match track_type:
            case 'r':
                self.color_lab_threshold = lab_config['red']
                self.get_logger().info('Our mission is to track the red line')
            case 'k':
                self.color_lab_threshold = lab_config['black']
                self.get_logger().info('Our mission is to track the black line')
        self.Kp = Kp
        self.Kd = Kd
        self.Ki = Ki
        self.I = 0
        self.bridge = CvBridge()
        self._sub = self.create_subscription(Image, 'camera', self.image_callback, 10)
        self._vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self._imgdebug_pub = self.create_publisher(Image, 'debug_image', 10)
        self._cli = self.create_client(Allservos, 'set_all_servos')
        while not self._cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Servo service not available, waiting...")
        arm_init_req = Allservos.Request()
        arm_init_req.angles = [85, 60, 180, 0, 180]
        arm_init_future = self._cli.call_async(arm_init_req)
        rclpy.spin_until_future_complete(self, arm_init_future)
        res = arm_init_future.result()
        self.get_logger().info(f'Arm initialized: {res.acknowledged}')
        self.get_logger().info("Track line node has been created")

    def image_callback(self, msg: Image):
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        lab_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2LAB) # Consider only the lower half of the image
        mask = cv2.inRange(lab_img, tuple(self.color_lab_threshold['min']), tuple(self.color_lab_threshold['max']))
        mask = cv2.dilate(mask, kernel := np.ones((5, 5), np.uint8))
        debug_img = self.bridge.cv2_to_imgmsg(mask, encoding="mono8")
        self._imgdebug_pub.publish(debug_img)
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
                twist_msg.linear.x = 0.8
                if not hasattr(self, 'error_x_prev'):
                    omega = -float(error_x) * self.Kp
                else:
                    omega = -error_x * self.Kp - (error_x - self.error_x_prev) * self.Kd
                twist_msg.angular.z = np.clip(omega, -10, 10)
                self.error_x_prev = error_x
                self.I += error_x
                self._vel_pub.publish(twist_msg)
                return
        self._vel_pub.publish(Twist())  # Stop if no line is detected
        self.get_logger().info("No line detected, the robot has stopped.")
        self.destroy_node()
        rclpy.shutdown()

def main():
    rclpy.init()
    track_line_node = TrackLineNode(track_type='k')
    rclpy.spin(track_line_node)
    track_line_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
