# 初赛后开发记录
## 2025.11.20
我优化了节点的布置，取消了感受器-决策-执行器的设计架构，改为按照硬件-决策架构设计。在硬件上，我把所有占用同一硬件资源的发布者、订阅者合并为了一个节点，并使用SingleThreadedExecutor强制它们单线程顺序执行，从根本上消灭了硬件资源竞争的风险，以后传感器不会再莫名其妙地跑着跑着突然报错死掉了。同时，我把大多数参数都声明为了ros2参数，这样可以便捷地在launch文件中管理参数，复用性更高。最重要的是，我再次研读了hiwonder_sdk，把所有的硬件交互函数都重写了一遍，以后我们就不需要hiwonder_sdk库了，这也方便跨车移植代码。

若要进行调试，可以打开xserver然后在mobaxterm中使用rqt->plugins->robot tools->robot steering工具便捷地发布速度指令。

若要使机械臂打到特定角度，可以发布：
```bash
ros2 topic pub /arm/joint_trajectory trajectory_msgs/JointTrajectory "
joint_names: ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5']
points:
- positions: [1.57, 1.57, 1.57, 1.57, 2]
  time_from_start: {sec: 1, nanosec: 0}
" --once
```
## 2025.11.22
我添加了超声波LED颜色设置功能，在进行战斗任务的时候可以把超声波的LED设置为红色，秒开战斗脸
```bash
ros2 topic pub /ultrasonic/color std_msgs/msg/ColorRGBA "{r: 1}" --once
```