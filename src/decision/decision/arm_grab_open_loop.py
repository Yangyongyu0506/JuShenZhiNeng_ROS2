import rclpy
from rclpy.node import Node
from my_interfaces.srv import Allservos
import time

class ArmGrabOpenLoopNode(Node):
    def __init__(self):
        super().__init__('arm_grab_open_loop_node')
        self._cli = self.create_client(Allservos, 'set_all_servos')

        while not self._cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f'{self._cli.srv_name} not available, waiting...')

        # 动作列表（状态机序列）
        self._actions = [
            [90, 90, 90, 90, 180],
            [90, 180, 120, 60, 180],
            [90, 180, 120, 60, 90],
            [90, 90, 120, 45, 90],
            [0, 180, 120, 45, 90],
            [0, 180, 150, 45, 180],
            [90, 90, 90, 90, 180]
        ]
        self._current_index = 0

        # 启动任务
        self.get_logger().info('Starting open-loop grab sequence...')
        self.execute_next_action()

    def execute_next_action(self):
        if self._current_index >= len(self._actions):
            self.get_logger().info('All actions completed.')
            self.destroy_node()
            rclpy.shutdown()
            return

        args = self._actions[self._current_index]
        self._current_index += 1
        req = Allservos.Request()
        req.angles = args
        self.get_logger().info(f'Executing action {self._current_index}: {args}')
        future = self._cli.call_async(req)
        future.add_done_callback(self._callback_next)

    def _callback_next(self, future):
        try:
            result = future.result()
            if result is not None:
                self.get_logger().info('Action completed successfully.')
            else:
                self.get_logger().warn('Service returned None!')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

        # 稍作延时再执行下一步
        time.sleep(5)
        self.execute_next_action()
def main():
    rclpy.init()
    node = ArmGrabOpenLoopNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
