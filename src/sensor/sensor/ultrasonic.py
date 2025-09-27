import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from hiwonder_sdk import Sonar
import threading
from collections import deque
import math
import time 

class UltrasonicNode(Node):
    def __init__(self):
        Node.__init__(self, 'ultrasonic_pub')
        self.pub = self.create_publisher(Range, 'range', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.sonar = Sonar.Sonar()
        self.lock = threading.Lock()
        self.distance_queue = deque(maxlen=2)
        self.sonar_task = threading.Thread(target=self.sonar_loop, daemon=True)
        self.sonar_task.start()
    
    def timer_callback(self):
        with self.lock:
            while self.distance_queue:
                dist = self.distance_queue.popleft()
                msg = Range()
                msg.header.stamp = self.get_clock().now().to_msg()
                msg.header.frame_id = 'ultrasonic_link'
                msg.radiation_type = Range.ULTRASOUND
                msg.field_of_view = math.radians(15)  # Example FOV
                msg.min_range = 0.01  # Minimum range in meters
                msg.max_range = 5.0   # Maximum range in meters
                msg.range = dist / 1000.0  # Convert mm to meters
                self.get_logger.info(f'sonar range: {msg.range} m')
                self.pub.publish(msg)

    def sonar_loop(self):
        with self.lock:
            while True:
                self.distance_queue.append(self.sonar.getDistance())
                time.sleep(0.001)

def main():
    rclpy.init()
    my_sonar_node = UltrasonicNode()
    rclpy.spin(my_sonar_node)
    my_sonar_node.destroy_node()
    rclpy.shutdown()

if 'name' == '__main__':
    main()