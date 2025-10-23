import rclpy
from rclpy.node import Node
from my_interfaces.srv import Armabs
from hiwonder_sdk import Board

class ArmServer(Node):
    def __init__(self):
        super().__init__('arm_server')
        self._srv_abs = self.create_service(Armabs, 'arm_abs', self.srv_abs_callback)
        self.get_logger().info('Arm service started, waiting for clients')
        Board.setPWMServoAngle(2, 90) # 原来是2
        Board.setPWMServoAngle(5, 60) # 原来是5
        Board.setPWMServoAngle(4, 180)
        Board.setPWMServoAngle(3, 0)
    
    def srv_abs_callback(self, request, response):
        Board.setPWMServoAngle(2, request.angle1)
        Board.setPWMServoAngle(5, request.angle2)
        Board.setPWMServoAngle(4, request.angle3)
        Board.setPWMServoAngle(3, request.angle4)
        response.acknowledged = True
        self.get_logger().info('Arm command implemented')
        return response

def main():
    rclpy.init()
    armsrv = ArmServer()
    try:
        rclpy.spin(armsrv)
    finally:
        rclpy.shutdown()
    
if __name__ == '__main__':
    main()