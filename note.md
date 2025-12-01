colcon build --symlink-install

source install/setup.bash
ros2 run hardware_interface_py i2c

source install/setup.bash
ros2 run control_py combat 

source install/setup.bash
ros2 launch control_py track_line_launch.yaml 

* 检查摄像头序号对应
```
//track_line_launch.yaml
  - node:
      pkg: hardware_interface_py
      exec: usb_camera
      name: usb_camera_node
      output: screen
      param:
        - name: video_id
          value: 0
```