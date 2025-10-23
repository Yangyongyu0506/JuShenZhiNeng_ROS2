// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_interfaces:srv/Allservos.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ALLSERVOS__STRUCT_HPP_
#define MY_INTERFACES__SRV__DETAIL__ALLSERVOS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Allservos_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Allservos_Request __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Allservos_Request_
{
  using Type = Allservos_Request_<ContainerAllocator>;

  explicit Allservos_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int16_t, 5>::iterator, int16_t>(this->angles.begin(), this->angles.end(), 0);
    }
  }

  explicit Allservos_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : angles(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int16_t, 5>::iterator, int16_t>(this->angles.begin(), this->angles.end(), 0);
    }
  }

  // field types and members
  using _angles_type =
    std::array<int16_t, 5>;
  _angles_type angles;

  // setters for named parameter idiom
  Type & set__angles(
    const std::array<int16_t, 5> & _arg)
  {
    this->angles = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::srv::Allservos_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Allservos_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Allservos_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Allservos_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Allservos_Request
    std::shared_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Allservos_Request
    std::shared_ptr<my_interfaces::srv::Allservos_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Allservos_Request_ & other) const
  {
    if (this->angles != other.angles) {
      return false;
    }
    return true;
  }
  bool operator!=(const Allservos_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Allservos_Request_

// alias to use template instance with default allocator
using Allservos_Request =
  my_interfaces::srv::Allservos_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Allservos_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Allservos_Response __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Allservos_Response_
{
  using Type = Allservos_Response_<ContainerAllocator>;

  explicit Allservos_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->acknowledged = false;
    }
  }

  explicit Allservos_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    my_interfaces::srv::Allservos_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Allservos_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Allservos_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Allservos_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Allservos_Response
    std::shared_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Allservos_Response
    std::shared_ptr<my_interfaces::srv::Allservos_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Allservos_Response_ & other) const
  {
    if (this->acknowledged != other.acknowledged) {
      return false;
    }
    return true;
  }
  bool operator!=(const Allservos_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Allservos_Response_

// alias to use template instance with default allocator
using Allservos_Response =
  my_interfaces::srv::Allservos_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces

namespace my_interfaces
{

namespace srv
{

struct Allservos
{
  using Request = my_interfaces::srv::Allservos_Request;
  using Response = my_interfaces::srv::Allservos_Response;
};

}  // namespace srv

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__ALLSERVOS__STRUCT_HPP_
