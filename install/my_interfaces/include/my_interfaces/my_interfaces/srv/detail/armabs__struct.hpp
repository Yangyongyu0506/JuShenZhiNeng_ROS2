// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_interfaces:srv/Armabs.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ARMABS__STRUCT_HPP_
#define MY_INTERFACES__SRV__DETAIL__ARMABS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Armabs_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Armabs_Request __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Armabs_Request_
{
  using Type = Armabs_Request_<ContainerAllocator>;

  explicit Armabs_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->angle1 = 0;
      this->angle2 = 0;
      this->angle3 = 0;
      this->angle4 = 0;
    }
  }

  explicit Armabs_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->angle1 = 0;
      this->angle2 = 0;
      this->angle3 = 0;
      this->angle4 = 0;
    }
  }

  // field types and members
  using _angle1_type =
    int16_t;
  _angle1_type angle1;
  using _angle2_type =
    int16_t;
  _angle2_type angle2;
  using _angle3_type =
    int16_t;
  _angle3_type angle3;
  using _angle4_type =
    int16_t;
  _angle4_type angle4;

  // setters for named parameter idiom
  Type & set__angle1(
    const int16_t & _arg)
  {
    this->angle1 = _arg;
    return *this;
  }
  Type & set__angle2(
    const int16_t & _arg)
  {
    this->angle2 = _arg;
    return *this;
  }
  Type & set__angle3(
    const int16_t & _arg)
  {
    this->angle3 = _arg;
    return *this;
  }
  Type & set__angle4(
    const int16_t & _arg)
  {
    this->angle4 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::srv::Armabs_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Armabs_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armabs_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armabs_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Armabs_Request
    std::shared_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Armabs_Request
    std::shared_ptr<my_interfaces::srv::Armabs_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Armabs_Request_ & other) const
  {
    if (this->angle1 != other.angle1) {
      return false;
    }
    if (this->angle2 != other.angle2) {
      return false;
    }
    if (this->angle3 != other.angle3) {
      return false;
    }
    if (this->angle4 != other.angle4) {
      return false;
    }
    return true;
  }
  bool operator!=(const Armabs_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Armabs_Request_

// alias to use template instance with default allocator
using Armabs_Request =
  my_interfaces::srv::Armabs_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Armabs_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Armabs_Response __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Armabs_Response_
{
  using Type = Armabs_Response_<ContainerAllocator>;

  explicit Armabs_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->acknowledged = false;
    }
  }

  explicit Armabs_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    my_interfaces::srv::Armabs_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Armabs_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armabs_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armabs_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Armabs_Response
    std::shared_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Armabs_Response
    std::shared_ptr<my_interfaces::srv::Armabs_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Armabs_Response_ & other) const
  {
    if (this->acknowledged != other.acknowledged) {
      return false;
    }
    return true;
  }
  bool operator!=(const Armabs_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Armabs_Response_

// alias to use template instance with default allocator
using Armabs_Response =
  my_interfaces::srv::Armabs_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces

namespace my_interfaces
{

namespace srv
{

struct Armabs
{
  using Request = my_interfaces::srv::Armabs_Request;
  using Response = my_interfaces::srv::Armabs_Response;
};

}  // namespace srv

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__ARMABS__STRUCT_HPP_
