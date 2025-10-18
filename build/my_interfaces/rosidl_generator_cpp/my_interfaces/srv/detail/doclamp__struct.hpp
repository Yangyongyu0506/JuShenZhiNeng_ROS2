// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_interfaces:srv/Doclamp.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__DOCLAMP__STRUCT_HPP_
#define MY_INTERFACES__SRV__DETAIL__DOCLAMP__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Doclamp_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Doclamp_Request __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Doclamp_Request_
{
  using Type = Doclamp_Request_<ContainerAllocator>;

  explicit Doclamp_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->angle = 0;
    }
  }

  explicit Doclamp_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->angle = 0;
    }
  }

  // field types and members
  using _angle_type =
    int16_t;
  _angle_type angle;

  // setters for named parameter idiom
  Type & set__angle(
    const int16_t & _arg)
  {
    this->angle = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::srv::Doclamp_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Doclamp_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Doclamp_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Doclamp_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Doclamp_Request
    std::shared_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Doclamp_Request
    std::shared_ptr<my_interfaces::srv::Doclamp_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Doclamp_Request_ & other) const
  {
    if (this->angle != other.angle) {
      return false;
    }
    return true;
  }
  bool operator!=(const Doclamp_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Doclamp_Request_

// alias to use template instance with default allocator
using Doclamp_Request =
  my_interfaces::srv::Doclamp_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Doclamp_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Doclamp_Response __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Doclamp_Response_
{
  using Type = Doclamp_Response_<ContainerAllocator>;

  explicit Doclamp_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->acknowledged = false;
    }
  }

  explicit Doclamp_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->acknowledged = false;
    }
  }

  // field types and members
  using _acknowledged_type =
    bool;
  _acknowledged_type acknowledged;

  // setters for named parameter idiom
  Type & set__acknowledged(
    const bool & _arg)
  {
    this->acknowledged = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::srv::Doclamp_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Doclamp_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Doclamp_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Doclamp_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Doclamp_Response
    std::shared_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Doclamp_Response
    std::shared_ptr<my_interfaces::srv::Doclamp_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Doclamp_Response_ & other) const
  {
    if (this->acknowledged != other.acknowledged) {
      return false;
    }
    return true;
  }
  bool operator!=(const Doclamp_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Doclamp_Response_

// alias to use template instance with default allocator
using Doclamp_Response =
  my_interfaces::srv::Doclamp_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces

namespace my_interfaces
{

namespace srv
{

struct Doclamp
{
  using Request = my_interfaces::srv::Doclamp_Request;
  using Response = my_interfaces::srv::Doclamp_Response;
};

}  // namespace srv

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__DOCLAMP__STRUCT_HPP_
