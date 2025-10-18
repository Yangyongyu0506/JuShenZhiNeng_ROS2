// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_interfaces:srv/Doclamp.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__DOCLAMP__STRUCT_H_
#define MY_INTERFACES__SRV__DETAIL__DOCLAMP__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Doclamp in the package my_interfaces.
typedef struct my_interfaces__srv__Doclamp_Request
{
  /// Desired angle to set the clamp to
  int16_t angle;
} my_interfaces__srv__Doclamp_Request;

// Struct for a sequence of my_interfaces__srv__Doclamp_Request.
typedef struct my_interfaces__srv__Doclamp_Request__Sequence
{
  my_interfaces__srv__Doclamp_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Doclamp_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Doclamp in the package my_interfaces.
typedef struct my_interfaces__srv__Doclamp_Response
{
  bool acknowledged;
} my_interfaces__srv__Doclamp_Response;

// Struct for a sequence of my_interfaces__srv__Doclamp_Response.
typedef struct my_interfaces__srv__Doclamp_Response__Sequence
{
  my_interfaces__srv__Doclamp_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Doclamp_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__SRV__DETAIL__DOCLAMP__STRUCT_H_
