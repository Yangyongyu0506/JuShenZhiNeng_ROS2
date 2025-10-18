// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_interfaces:srv/Armrel.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ARMREL__STRUCT_HPP_
#define MY_INTERFACES__SRV__DETAIL__ARMREL__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Armrel_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Armrel_Request __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Armrel_Request_
{
  using Type = Armrel_Request_<ContainerAllocator>;

  explicit Armrel_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->dangle1 = 0;
      this->dangle2 = 0;
      this->dangle3 = 0;
      this->dangle4 = 0;
    }
  }

  explicit Armrel_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->dangle1 = 0;
      this->dangle2 = 0;
      this->dangle3 = 0;
      this->dangle4 = 0;
    }
  }

  // field types and members
  using _dangle1_type =
    int16_t;
  _dangle1_type dangle1;
  using _dangle2_type =
    int16_t;
  _dangle2_type dangle2;
  using _dangle3_type =
    int16_t;
  _dangle3_type dangle3;
  using _dangle4_type =
    int16_t;
  _dangle4_type dangle4;

  // setters for named parameter idiom
  Type & set__dangle1(
    const int16_t & _arg)
  {
    this->dangle1 = _arg;
    return *this;
  }
  Type & set__dangle2(
    const int16_t & _arg)
  {
    this->dangle2 = _arg;
    return *this;
  }
  Type & set__dangle3(
    const int16_t & _arg)
  {
    this->dangle3 = _arg;
    return *this;
  }
  Type & set__dangle4(
    const int16_t & _arg)
  {
    this->dangle4 = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::srv::Armrel_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Armrel_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armrel_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armrel_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Armrel_Request
    std::shared_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Armrel_Request
    std::shared_ptr<my_interfaces::srv::Armrel_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Armrel_Request_ & other) const
  {
    if (this->dangle1 != other.dangle1) {
      return false;
    }
    if (this->dangle2 != other.dangle2) {
      return false;
    }
    if (this->dangle3 != other.dangle3) {
      return false;
    }
    if (this->dangle4 != other.dangle4) {
      return false;
    }
    return true;
  }
  bool operator!=(const Armrel_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Armrel_Request_

// alias to use template instance with default allocator
using Armrel_Request =
  my_interfaces::srv::Armrel_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Armrel_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Armrel_Response __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Armrel_Response_
{
  using Type = Armrel_Response_<ContainerAllocator>;

  explicit Armrel_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->acknowledged = false;
    }
  }

  explicit Armrel_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    my_interfaces::srv::Armrel_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Armrel_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armrel_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Armrel_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Armrel_Response
    std::shared_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Armrel_Response
    std::shared_ptr<my_interfaces::srv::Armrel_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Armrel_Response_ & other) const
  {
    if (this->acknowledged != other.acknowledged) {
      return false;
    }
    return true;
  }
  bool operator!=(const Armrel_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Armrel_Response_

// alias to use template instance with default allocator
using Armrel_Response =
  my_interfaces::srv::Armrel_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces

namespace my_interfaces
{

namespace srv
{

struct Armrel
{
  using Request = my_interfaces::srv::Armrel_Request;
  using Response = my_interfaces::srv::Armrel_Response;
};

}  // namespace srv

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__ARMREL__STRUCT_HPP_
