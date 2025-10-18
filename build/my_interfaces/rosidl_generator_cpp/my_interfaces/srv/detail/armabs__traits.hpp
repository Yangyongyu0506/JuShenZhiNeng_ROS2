// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_interfaces:srv/Armabs.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ARMABS__TRAITS_HPP_
#define MY_INTERFACES__SRV__DETAIL__ARMABS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_interfaces/srv/detail/armabs__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Armabs_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: angle1
  {
    out << "angle1: ";
    rosidl_generator_traits::value_to_yaml(msg.angle1, out);
    out << ", ";
  }

  // member: angle2
  {
    out << "angle2: ";
    rosidl_generator_traits::value_to_yaml(msg.angle2, out);
    out << ", ";
  }

  // member: angle3
  {
    out << "angle3: ";
    rosidl_generator_traits::value_to_yaml(msg.angle3, out);
    out << ", ";
  }

  // member: angle4
  {
    out << "angle4: ";
    rosidl_generator_traits::value_to_yaml(msg.angle4, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Armabs_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: angle1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle1: ";
    rosidl_generator_traits::value_to_yaml(msg.angle1, out);
    out << "\n";
  }

  // member: angle2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle2: ";
    rosidl_generator_traits::value_to_yaml(msg.angle2, out);
    out << "\n";
  }

  // member: angle3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle3: ";
    rosidl_generator_traits::value_to_yaml(msg.angle3, out);
    out << "\n";
  }

  // member: angle4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle4: ";
    rosidl_generator_traits::value_to_yaml(msg.angle4, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Armabs_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use my_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_interfaces::srv::Armabs_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_interfaces::srv::Armabs_Request & msg)
{
  return my_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_interfaces::srv::Armabs_Request>()
{
  return "my_interfaces::srv::Armabs_Request";
}

template<>
inline const char * name<my_interfaces::srv::Armabs_Request>()
{
  return "my_interfaces/srv/Armabs_Request";
}

template<>
struct has_fixed_size<my_interfaces::srv::Armabs_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_interfaces::srv::Armabs_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_interfaces::srv::Armabs_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace my_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Armabs_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: acknowledged
  {
    out << "acknowledged: ";
    rosidl_generator_traits::value_to_yaml(msg.acknowledged, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Armabs_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: acknowledged
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acknowledged: ";
    rosidl_generator_traits::value_to_yaml(msg.acknowledged, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Armabs_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace my_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use my_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_interfaces::srv::Armabs_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_interfaces::srv::Armabs_Response & msg)
{
  return my_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_interfaces::srv::Armabs_Response>()
{
  return "my_interfaces::srv::Armabs_Response";
}

template<>
inline const char * name<my_interfaces::srv::Armabs_Response>()
{
  return "my_interfaces/srv/Armabs_Response";
}

template<>
struct has_fixed_size<my_interfaces::srv::Armabs_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_interfaces::srv::Armabs_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_interfaces::srv::Armabs_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_interfaces::srv::Armabs>()
{
  return "my_interfaces::srv::Armabs";
}

template<>
inline const char * name<my_interfaces::srv::Armabs>()
{
  return "my_interfaces/srv/Armabs";
}

template<>
struct has_fixed_size<my_interfaces::srv::Armabs>
  : std::integral_constant<
    bool,
    has_fixed_size<my_interfaces::srv::Armabs_Request>::value &&
    has_fixed_size<my_interfaces::srv::Armabs_Response>::value
  >
{
};

template<>
struct has_bounded_size<my_interfaces::srv::Armabs>
  : std::integral_constant<
    bool,
    has_bounded_size<my_interfaces::srv::Armabs_Request>::value &&
    has_bounded_size<my_interfaces::srv::Armabs_Response>::value
  >
{
};

template<>
struct is_service<my_interfaces::srv::Armabs>
  : std::true_type
{
};

template<>
struct is_service_request<my_interfaces::srv::Armabs_Request>
  : std::true_type
{
};

template<>
struct is_service_response<my_interfaces::srv::Armabs_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MY_INTERFACES__SRV__DETAIL__ARMABS__TRAITS_HPP_
