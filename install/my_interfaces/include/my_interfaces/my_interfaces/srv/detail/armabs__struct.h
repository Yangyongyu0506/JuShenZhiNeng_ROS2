// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_interfaces:srv/Armabs.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ARMABS__STRUCT_H_
#define MY_INTERFACES__SRV__DETAIL__ARMABS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Armabs in the package my_interfaces.
typedef struct my_interfaces__srv__Armabs_Request
{
  int16_t angle1;
  int16_t angle2;
  int16_t angle3;
  int16_t angle4;
} my_interfaces__srv__Armabs_Request;

// Struct for a sequence of my_interfaces__srv__Armabs_Request.
typedef struct my_interfaces__srv__Armabs_Request__Sequence
{
  my_interfaces__srv__Armabs_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Armabs_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Armabs in the package my_interfaces.
typedef struct my_interfaces__srv__Armabs_Response
{
  bool acknowledged;
} my_interfaces__srv__Armabs_Response;

// Struct for a sequence of my_interfaces__srv__Armabs_Response.
typedef struct my_interfaces__srv__Armabs_Response__Sequence
{
  my_interfaces__srv__Armabs_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Armabs_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__SRV__DETAIL__ARMABS__STRUCT_H_
