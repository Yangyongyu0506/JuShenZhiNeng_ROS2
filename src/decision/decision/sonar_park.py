import rclpy
from rclpy.node import Node
import time
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

class SonarParkNode(Node):
    def __init__(self, Kp, Kd, Ki):
        super().__init__('sonar_park')
        self._sub = self.create_subscription(Range, 'sonar', self.range_callback, 10)
        self._pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.error = 0.02 # 2cm
        self.goal = 0.2 # 20cm
        self.last_dist = None

        self.Kp = Kp
        self.Kd = Kd
        self.Ki = Ki

    def range_callback(self, msg):
        dist_now = msg.range
        cmd_vel_msg = Twist()
        if self.last_dist is None:
            cmd_vel_msg.linear.x = self.Kp * (dist_now - self.goal)
            self._pub.publish(cmd_vel_msg)
        else:
            cmd_vel_msg.linear.x = self.Kp * (dist_now - self.goal) + self.Kd * (dist_now - self.last_dist) / 0.1
            self._pub.publish(cmd_vel_msg)
        self.last_dist = dist_now
        self.get_logger().info(f"Current Distance: {dist_now:.3f} m, Commanded Velocity: {cmd_vel_msg.linear.x:.3f} m/s")
        if abs(dist_now - self.goal) <= self.error:
            self.get_logger().info("Target distance reached. Stopping the robot.")
            stop_msg = Twist()
            self._pub.publish(stop_msg)
            self.get_logger().info("Press Ctrl+C to exit")
    
def main(args=None):
    rclpy.init(args=args)
    Kp = 1
    Kd = 0.1
    Ki = 0.0
    sonar_park_node = SonarParkNode(Kp, Kd, Ki)
    try:
        rclpy.spin(sonar_park_node)
    finally:
        sonar_park_node.destroy_node()
        rclpy.shutdown()