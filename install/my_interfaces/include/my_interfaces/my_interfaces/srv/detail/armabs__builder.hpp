// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:srv/Armabs.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ARMABS__BUILDER_HPP_
#define MY_INTERFACES__SRV__DETAIL__ARMABS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/srv/detail/armabs__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Armabs_Request_angle4
{
public:
  explicit Init_Armabs_Request_angle4(::my_interfaces::srv::Armabs_Request & msg)
  : msg_(msg)
  {}
  ::my_interfaces::srv::Armabs_Request angle4(::my_interfaces::srv::Armabs_Request::_angle4_type arg)
  {
    msg_.angle4 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Armabs_Request msg_;
};

class Init_Armabs_Request_angle3
{
public:
  explicit Init_Armabs_Request_angle3(::my_interfaces::srv::Armabs_Request & msg)
  : msg_(msg)
  {}
  Init_Armabs_Request_angle4 angle3(::my_interfaces::srv::Armabs_Request::_angle3_type arg)
  {
    msg_.angle3 = std::move(arg);
    return Init_Armabs_Request_angle4(msg_);
  }

private:
  ::my_interfaces::srv::Armabs_Request msg_;
};

class Init_Armabs_Request_angle2
{
public:
  explicit Init_Armabs_Request_angle2(::my_interfaces::srv::Armabs_Request & msg)
  : msg_(msg)
  {}
  Init_Armabs_Request_angle3 angle2(::my_interfaces::srv::Armabs_Request::_angle2_type arg)
  {
    msg_.angle2 = std::move(arg);
    return Init_Armabs_Request_angle3(msg_);
  }

private:
  ::my_interfaces::srv::Armabs_Request msg_;
};

class Init_Armabs_Request_angle1
{
public:
  Init_Armabs_Request_angle1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Armabs_Request_angle2 angle1(::my_interfaces::srv::Armabs_Request::_angle1_type arg)
  {
    msg_.angle1 = std::move(arg);
    return Init_Armabs_Request_angle2(msg_);
  }

private:
  ::my_interfaces::srv::Armabs_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Armabs_Request>()
{
  return my_interfaces::srv::builder::Init_Armabs_Request_angle1();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Armabs_Response_acknowledged
{
public:
  Init_Armabs_Response_acknowledged()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::srv::Armabs_Response acknowledged(::my_interfaces::srv::Armabs_Response::_acknowledged_type arg)
  {
    msg_.acknowledged = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Armabs_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Armabs_Response>()
{
  return my_interfaces::srv::builder::Init_Armabs_Response_acknowledged();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__ARMABS__BUILDER_HPP_
