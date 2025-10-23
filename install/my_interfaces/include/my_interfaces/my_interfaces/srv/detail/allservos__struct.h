// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_interfaces:srv/Allservos.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ALLSERVOS__STRUCT_H_
#define MY_INTERFACES__SRV__DETAIL__ALLSERVOS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Allservos in the package my_interfaces.
typedef struct my_interfaces__srv__Allservos_Request
{
  int16_t angles[5];
} my_interfaces__srv__Allservos_Request;

// Struct for a sequence of my_interfaces__srv__Allservos_Request.
typedef struct my_interfaces__srv__Allservos_Request__Sequence
{
  my_interfaces__srv__Allservos_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Allservos_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Allservos in the package my_interfaces.
typedef struct my_interfaces__srv__Allservos_Response
{
  bool acknowledged;
} my_interfaces__srv__Allservos_Response;

// Struct for a sequence of my_interfaces__srv__Allservos_Response.
typedef struct my_interfaces__srv__Allservos_Response__Sequence
{
  my_interfaces__srv__Allservos_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Allservos_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__SRV__DETAIL__ALLSERVOS__STRUCT_H_
