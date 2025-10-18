// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:srv/Doclamp.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__DOCLAMP__BUILDER_HPP_
#define MY_INTERFACES__SRV__DETAIL__DOCLAMP__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/srv/detail/doclamp__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Doclamp_Request_angle
{
public:
  Init_Doclamp_Request_angle()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::srv::Doclamp_Request angle(::my_interfaces::srv::Doclamp_Request::_angle_type arg)
  {
    msg_.angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Doclamp_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Doclamp_Request>()
{
  return my_interfaces::srv::builder::Init_Doclamp_Request_angle();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Doclamp_Response_acknowledged
{
public:
  Init_Doclamp_Response_acknowledged()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::srv::Doclamp_Response acknowledged(::my_interfaces::srv::Doclamp_Response::_acknowledged_type arg)
  {
    msg_.acknowledged = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Doclamp_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Doclamp_Response>()
{
  return my_interfaces::srv::builder::Init_Doclamp_Response_acknowledged();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__DOCLAMP__BUILDER_HPP_
