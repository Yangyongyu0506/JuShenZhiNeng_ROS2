import rclpy
from rclpy.node import Node
from my_interfaces.srv import Doclamp
from hiwonder_sdk import Board

class ClampServer(Node):
    def __init__(self):
        super().__init__('clamp_server')
        self._srv = self.create_service(Doclamp, 'doclamp', self.srv_callback)
        self.get_logger().info('Clamp service started, waiting for clients')

    def srv_callback(self, request, response):
        Board.setPWMServoAngle(1, request.angle if request.angle >= 90 else 90)
        response.acknowledged = True
        self.get_logger().info(f'Clamp to {request.angle} degs')
        return response

def main():
    rclpy.init()
    clampsrv = ClampServer()
    try:
        rclpy.spin(clampsrv)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()