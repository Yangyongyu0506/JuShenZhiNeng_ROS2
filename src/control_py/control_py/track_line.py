import rclpy
from rclpy.node import Node
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32, Bool, String
import yaml
import os
from ament_index_python.packages import get_package_share_directory

class TrackLineNode(Node):
    def __init__(self):
        super().__init__('track_line_node')

        # state variable
        self.enabled = False  # 巡线是否启用
        self.emergency_stop = False  # 紧急停止

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
        self.Kp = 0.0005
        self.Kd = 0.0
        self.Ki = 0.0
        self.I = 0
        self.error_x_prev = 0

        # 速度参数
        self.base_speed = self.declare_parameter('base_speed', 0.05).value  # 降低速度便于调试
        self.max_angular_speed = self.declare_parameter('max_angular_speed', 2.0).value

        # Init CvBridge
        self.bridge = CvBridge()

        # Init ROS2 components
        self.sub_img = self.create_subscription(Image, 'camera', self.sub_image_callback, 10)
        self.pub_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.pub_debugimg = self.create_publisher(Image, 'debug_image', 10)
        self.pub_error_x = self.create_publisher(Int32, 'error_x', 10)

        # 新增：订阅控制命令
        self.sub_enable = self.create_subscription(
            Bool,
            'track_line/enable',
            self.enable_callback,
            10
        )
        
        self.sub_command = self.create_subscription(
            String,
            'track_line/command',
            self.command_callback,
            10
        )
        
        # 新增：发布状态信息
        self.pub_status = self.create_publisher(String, 'track_line/status', 10)
        
        # 新增：定时器用于定期发布状态
        self.timer = self.create_timer(1.0, self.publish_status)

        # Done
        self.get_logger().info("Track line node has been created")
        self.get_logger().info("Send 'True' to /track_line/enable to start")
        self.get_logger().info("Send 'stop' to /track_line/command to stop")

    def enable_callback(self, msg: Bool):
        """处理启用/禁用巡线的命令"""
        self.enabled = msg.data
        if self.enabled:
            self.get_logger().info("Track line ENABLED")
            # 重置PID状态
            self.I = 0
            self.error_x_prev = 0
        else:
            self.get_logger().info("Track line DISABLED")
            # 发布停止指令
            self.stop_robot()
    def command_callback(self, msg: String):
        """处理文本命令"""
        command = msg.data.lower()
        
        if command == "start":
            self.enabled = True
            self.emergency_stop = False
            self.get_logger().info("START command received")
        elif command == "stop":
            self.enabled = False
            self.emergency_stop = False
            self.stop_robot()
            self.get_logger().info("STOP command received")
        elif command == "emergency_stop":
            self.enabled = False
            self.emergency_stop = True
            self.stop_robot()
            self.get_logger().warn("EMERGENCY STOP activated!")
        elif command == "reset_pid":
            self.I = 0
            self.error_x_prev = 0
            self.get_logger().info("PID state reset")
        else:
            self.get_logger().warn(f"Unknown command: {command}")
    
    def stop_robot(self):
        """停止机器人"""
        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.angular.z = 0.0
        self.pub_vel.publish(twist_msg)
    
    def publish_status(self):
        """定期发布状态信息"""
        status_msg = String()
        if self.emergency_stop:
            status_msg.data = "EMERGENCY_STOP"
        elif self.enabled:
            status_msg.data = "RUNNING"
        else:
            status_msg.data = "STOPPED"
        self.pub_status.publish(status_msg)
    
    def sub_image_callback(self, msg: Image):
        if self.emergency_stop:
            self.stop_robot()
            return
        
        if not self.enabled:
            # 如果未启用，仍然可以处理图像用于调试，但不控制小车
            self.process_image_for_debug(msg)
            return
        
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # roi = cv_img[:, int(cv_img.shape[1] * 0.1):int(cv_img.shape[1] * 0.9)]
        # roi = cv_img[int(cv_img.shape[0] * 0.6):]
        # roi = cv_img[:int(cv_img.shape[0] * 0.8), int(cv_img.shape[1] * 0.1):int(cv_img.shape[1] * 0.9)]
        # roi = cv_img
        # lab_img = cv2.cvtColor(roi, cv2.COLOR_BGR2LAB)

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
                # 发布误差值
                self.pub_error_x.publish(Int32(data=error_x))
                
                # 计算PID控制量
                P = self.Kp * error_x
                D = self.Kd * (error_x - self.error_x_prev)
                self.I += error_x
                I_term = self.Ki * self.I
                
                # 限制积分项，防止积分饱和
                I_term = np.clip(I_term, -0.5, 0.5)
                
                # 计算角速度
                omega = -(P + D + I_term)
                
                # 限制角速度
                omega = np.clip(omega, -self.max_angular_speed, self.max_angular_speed)
                
                # 创建速度指令
                twist_msg = Twist()
                twist_msg.linear.x = self.base_speed
                twist_msg.angular.z = float(omega)  # 确保是Python float类型
                
                # 发布速度指令
                self.pub_vel.publish(twist_msg)
                
                # 保存当前误差供下次计算D项使用
                self.error_x_prev = error_x
                
                return
                # twist_msg = Twist()
                # # 匹配停车标志
                # # epsilon = 0.02 * cv2.arcLength(largest_contour, True)
                # # approx = cv2.approxPolyDP(largest_contour, epsilon, True)
                # # if len(approx) >= 8 and np.sum(mask[:50, :]) < 5:
                # #     self._vel_pub.publish(twist_msg)
                # #     self.get_logger().info(f"Stop sign detected {len(approx)}, the robot has stopped.")
                # #     self.destroy_node()
                # #     rclpy.shutdown()
                # #     return
                # twist_msg.linear.x = 50 / (error_x ** 2 + 1)
                # if not hasattr(self, 'error_x_prev'):
                #     omega = -float(error_x) * self.Kp - self.I * self.Ki
                # else:
                #     omega = -error_x * self.Kp - (error_x - self.error_x_prev) * self.Kd - self.I * self.Ki
                # twist_msg.angular.z = np.clip(omega, -2, 2)
                # self.error_x_prev = error_x
                # self.I += error_x
                # self.pub_vel.publish(twist_msg)
                # return
            
        self.pub_vel.publish(Twist())  # Stop if no line is detected
        self.get_logger().info("No line detected, the robot has stopped.")

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

        # # Approach V3: Scanline method
        # H, W = mask.shape
        # centers = []

        # # 从底部往上 取 5 条扫描线
        # scan_rows = [int(H * r) for r in [0.9, 0.7, 0.5, 0.3, 0.1]]

        # for row in scan_rows:
        #     line = mask[row]
        #     idx = np.where(line > 0)[0]

        #     if len(idx) > 10:
        #         left = idx[0]
        #         right = idx[-1]
        #         center = (left + right) // 2
        #         centers.append(center)

        # if len(centers) == 0:
        #     # 找不到线 → 停车
        #     self.pub_vel.publish(Twist())
        #     return

        # # 得到最终误差（多行平均比质心稳很多）
        # center_avg = int(np.mean(centers))
        # error_x = center_avg - W//2

        # # ---------- 控制 ----------
        # twist = Twist()
        # twist.linear.x = 0.02
        # twist.angular.z = -error_x * self.Kp - (error_x - self.error_x_prev) * self.Kd  # 参数可调
        # self.error_x_prev = error_x
        # self.pub_vel.publish(twist)

    def process_image_for_debug(self, msg: Image):
        """仅处理图像用于调试，不控制小车"""
        cv_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        lab_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2LAB)
        mask = cv2.inRange(
            lab_img, 
            tuple(self.color_lab_threshold['min']), 
            tuple(self.color_lab_threshold['max'])
        )
        debug_img = self.bridge.cv2_to_imgmsg(mask, encoding="mono8")
        self.pub_debugimg.publish(debug_img)

def main():
    rclpy.init()
    track_line_node = TrackLineNode()

    try:
        rclpy.spin(track_line_node)
    except KeyboardInterrupt:
        track_line_node.get_logger().info("Keyboard interrupt received")
    finally:
        # 确保小车停止
        track_line_node.stop_robot()
        track_line_node.destroy_node()
        rclpy.shutdown()

    # rclpy.spin(track_line_node)
    # track_line_node.destroy_node()
    # rclpy.shutdown()