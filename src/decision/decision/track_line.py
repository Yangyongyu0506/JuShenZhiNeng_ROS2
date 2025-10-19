import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist
from my_interfaces.srv import Armabs
import yaml
import os
from ament_index_python.packages import get_package_share_directory

class TrackLineNode(Node):
    def __init__(self, track_type: str ='k'):
        super().__init__('track_line_node')
        self.bridge = CvBridge()
        self._sub = self.create_subscription(Image, 'camera', self.image_callback, 10)
        self._pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self._cli = self.create_client(Armabs, 'arm_abs')
        while not self._cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Arm service not available, waiting...")
        arm_init_req = Armabs.Request()
        arm_init_req.angle1 = 90
        arm_init_req.angle2 = 90
        arm_init_req.angle3 = 180
        arm_init_req.angle4 = 0
        arm_init_future = self._cli.call_async(arm_init_req)
        rclpy.spin_until_future_complete(self, arm_init_future)
        res = arm_init_future.result()
        try:
            assert(res.acknowledged)
            self.get_logger().info('Arm has been initialized')
        except Exception as e:
            self.get_logger().error('Failed to initialize arm {e}')
            try:
                self.destroy_node()
            finally:
                rclpy.shutdown()
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
            case _:
                self.color_lab_threshold = lab_config['black']
                self.get_logger().info('Our mission is to track the black line')
        self.get_logger().info("Track line node has been created")

    def image_callback(self, msg: Image):
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        lab_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2LAB)
        mask = cv2.inRange(lab_img, tuple(self.color_lab_threshold['min']), tuple(self.color_lab_threshold['max']))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                error_x = cx - (cv_img.shape[1] // 2)
                twist_msg = Twist()
                twist_msg.linear.x = 0.8
                twist_msg.angular.z = -float(error_x) / 30.0
                self._pub.publish(twist_msg)
                return
        self._pub.publish(Twist())  # Stop if no line is detected
        self.get_logger().info("No line detected, the robot has stopped.")

def main():
    rclpy.init()
    track_line_node = TrackLineNode(track_type='k')
    try:
        rclpy.spin(track_line_node)
    finally:
        track_line_node._pub.publish(Twist())
    track_line_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()