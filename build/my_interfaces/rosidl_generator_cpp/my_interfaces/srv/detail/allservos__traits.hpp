// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_interfaces:srv/Allservos.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ALLSERVOS__TRAITS_HPP_
#define MY_INTERFACES__SRV__DETAIL__ALLSERVOS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_interfaces/srv/detail/allservos__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Allservos_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: angles
  {
    if (msg.angles.size() == 0) {
      out << "angles: []";
    } else {
      out << "angles: [";
      size_t pending_items = msg.angles.size();
      for (auto item : msg.angles) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Allservos_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: angles
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.angles.size() == 0) {
      out << "angles: []\n";
    } else {
      out << "angles:\n";
      for (auto item : msg.angles) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Allservos_Request & msg, bool use_flow_style = false)
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
  const my_interfaces::srv::Allservos_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_interfaces::srv::Allservos_Request & msg)
{
  return my_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_interfaces::srv::Allservos_Request>()
{
  return "my_interfaces::srv::Allservos_Request";
}

template<>
inline const char * name<my_interfaces::srv::Allservos_Request>()
{
  return "my_interfaces/srv/Allservos_Request";
}

template<>
struct has_fixed_size<my_interfaces::srv::Allservos_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_interfaces::srv::Allservos_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_interfaces::srv::Allservos_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace my_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Allservos_Response & msg,
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
  const Allservos_Response & msg,
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

inline std::string to_yaml(const Allservos_Response & msg, bool use_flow_style = false)
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
  const my_interfaces::srv::Allservos_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const my_interfaces::srv::Allservos_Response & msg)
{
  return my_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<my_interfaces::srv::Allservos_Response>()
{
  return "my_interfaces::srv::Allservos_Response";
}

template<>
inline const char * name<my_interfaces::srv::Allservos_Response>()
{
  return "my_interfaces/srv/Allservos_Response";
}

template<>
struct has_fixed_size<my_interfaces::srv::Allservos_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<my_interfaces::srv::Allservos_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<my_interfaces::srv::Allservos_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_interfaces::srv::Allservos>()
{
  return "my_interfaces::srv::Allservos";
}

template<>
inline const char * name<my_interfaces::srv::Allservos>()
{
  return "my_interfaces/srv/Allservos";
}

template<>
struct has_fixed_size<my_interfaces::srv::Allservos>
  : std::integral_constant<
    bool,
    has_fixed_size<my_interfaces::srv::Allservos_Request>::value &&
    has_fixed_size<my_interfaces::srv::Allservos_Response>::value
  >
{
};

template<>
struct has_bounded_size<my_interfaces::srv::Allservos>
  : std::integral_constant<
    bool,
    has_bounded_size<my_interfaces::srv::Allservos_Request>::value &&
    has_bounded_size<my_interfaces::srv::Allservos_Response>::value
  >
{
};

template<>
struct is_service<my_interfaces::srv::Allservos>
  : std::true_type
{
};

template<>
struct is_service_request<my_interfaces::srv::Allservos_Request>
  : std::true_type
{
};

template<>
struct is_service_response<my_interfaces::srv::Allservos_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // MY_INTERFACES__SRV__DETAIL__ALLSERVOS__TRAITS_HPP_
