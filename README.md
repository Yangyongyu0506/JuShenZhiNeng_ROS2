# 第二届具身智能比赛22组代码
# 1. hiwonder_sdk
  这是一个基于例程重写的python包，主要解决了各种绝对路径依赖的问题，使得我们可以方便地在ROS2架构下开发香橙派驱动hiwonder开发板。
  使用时，在第一个hiwonder_sdk目录下，执行
#### bash
```bash
pip install -e .
```
  -e 选项是为了创建连接，这样如果出现了问题我们可以直接修改香橙派本地源码而不用再次 pip install
  
  我在9月27日的调试中发现，ros2默认使用的python环境是系统python，而香橙派上默认使用conda base虚拟环境。所以我把hiwonder_sdk以及其他相关依赖都pip install进了系统python中（但愿科协的人会去重装系统）。以后如果我们需要用别的库，比如ultralytics等等，我们就要先执行
#### bash
```bash
conda deactivate
```
  退出base虚拟环境。看到命令行前面没有(base)了，就表明我们已经来到了系统python。否则不管pip install多少次，ros2也找不到这个库。
# 2. ros2
  我把我在香橙派上写的基于ROS2框架的代码传上来了。
  上传了5个目录，包括src, log, build, install和launch。我们只需关注src和launch目录。src里面是所有的小车控制代码，launch里面是ros2 launch文件，用于一个命令启动所有节点。
  
