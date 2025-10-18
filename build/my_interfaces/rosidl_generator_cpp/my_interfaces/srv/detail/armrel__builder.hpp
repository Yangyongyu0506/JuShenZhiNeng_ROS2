// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:srv/Armrel.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ARMREL__BUILDER_HPP_
#define MY_INTERFACES__SRV__DETAIL__ARMREL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/srv/detail/armrel__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Armrel_Request_dangle4
{
public:
  explicit Init_Armrel_Request_dangle4(::my_interfaces::srv::Armrel_Request & msg)
  : msg_(msg)
  {}
  ::my_interfaces::srv::Armrel_Request dangle4(::my_interfaces::srv::Armrel_Request::_dangle4_type arg)
  {
    msg_.dangle4 = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Armrel_Request msg_;
};

class Init_Armrel_Request_dangle3
{
public:
  explicit Init_Armrel_Request_dangle3(::my_interfaces::srv::Armrel_Request & msg)
  : msg_(msg)
  {}
  Init_Armrel_Request_dangle4 dangle3(::my_interfaces::srv::Armrel_Request::_dangle3_type arg)
  {
    msg_.dangle3 = std::move(arg);
    return Init_Armrel_Request_dangle4(msg_);
  }

private:
  ::my_interfaces::srv::Armrel_Request msg_;
};

class Init_Armrel_Request_dangle2
{
public:
  explicit Init_Armrel_Request_dangle2(::my_interfaces::srv::Armrel_Request & msg)
  : msg_(msg)
  {}
  Init_Armrel_Request_dangle3 dangle2(::my_interfaces::srv::Armrel_Request::_dangle2_type arg)
  {
    msg_.dangle2 = std::move(arg);
    return Init_Armrel_Request_dangle3(msg_);
  }

private:
  ::my_interfaces::srv::Armrel_Request msg_;
};

class Init_Armrel_Request_dangle1
{
public:
  Init_Armrel_Request_dangle1()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Armrel_Request_dangle2 dangle1(::my_interfaces::srv::Armrel_Request::_dangle1_type arg)
  {
    msg_.dangle1 = std::move(arg);
    return Init_Armrel_Request_dangle2(msg_);
  }

private:
  ::my_interfaces::srv::Armrel_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Armrel_Request>()
{
  return my_interfaces::srv::builder::Init_Armrel_Request_dangle1();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Armrel_Response_acknowledged
{
public:
  Init_Armrel_Response_acknowledged()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::srv::Armrel_Response acknowledged(::my_interfaces::srv::Armrel_Response::_acknowledged_type arg)
  {
    msg_.acknowledged = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Armrel_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Armrel_Response>()
{
  return my_interfaces::srv::builder::Init_Armrel_Response_acknowledged();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__ARMREL__BUILDER_HPP_
