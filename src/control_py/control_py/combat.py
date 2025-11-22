#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Twist
import time

def main():
    # 初始化 ROS2
    rclpy.init()

    # 创建匿名节点，不用继承类
    node = Node('dance_demo')

    pub_arm = node.create_publisher(JointTrajectory, 'arm/joint_trajectory', 10)
    pub_led = node.create_publisher(ColorRGBA, 'ultrasonic/color', 10)
    pub_vel = node.create_publisher(Twist, 'cmd_vel', 10)
    # 秒开战斗脸
    msg = ColorRGBA()
    msg.r = 1.0
    pub_led.publish(msg)
    # 定义舞蹈动作序列
    dance_moves = [
        [1.57, 1.57, 1.57, 1.57, 3.14],
        [1.57, 1.57, 3.14, 0.0, 1.57]
    ]
    # 定义速度序列
    vel_cmds = [
        [0.0, -0.3],
        [0.0, 0.0]
    ]

    node.get_logger().info('开始跳舞！')

    for i, pos in enumerate(dance_moves):
        msg = JointTrajectory()
        msg.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5']
        point = JointTrajectoryPoint()
        point.positions = pos
        point.time_from_start.sec = 0
        msg.points.append(point)
        vel_msg = Twist()
        vel_msg.linear.x = vel_cmds[i][0]
        vel_msg.angular.z = vel_cmds[i][1]
        # 发布
        pub_arm.publish(msg)
        pub_vel.publish(vel_msg)
        # 稍等一下让消息发送出去
        time.sleep(2.0)

    # 舞蹈结束，关闭战斗脸
    pub_led.publish(ColorRGBA())

    node.get_logger().info('舞蹈完成，程序退出')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
