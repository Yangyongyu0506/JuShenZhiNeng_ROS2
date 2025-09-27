from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor',
            executable='ultrasonic',
            name='ultrasonic_node',
            output='screen',
        ),
        Node(
            package='sensor',
            executable='battery',
            name='battery_node',
            output='screen',
        ),
        Node(
            package='sensor',
            executable='camera',
            name='camera_node',
            output='screen',
        )
    ])