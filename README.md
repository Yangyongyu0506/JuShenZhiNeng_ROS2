# 第二届具身智能比赛22组代码
# 1. hiwonder_sdk
  这是一个基于例程重写的python包，主要解决了各种绝对路径依赖的问题，使得我们可以方便地在ROS2架构下开发香橙派驱动hiwonder开发板。
  使用时，在第一个hiwonder_sdk目录下，执行
#### bash
```bash
pip install -e .
```
  -e 选项是为了创建连接，这样如果出现了问题我们可以直接修改香橙派本地源码而不用再次 pip install
