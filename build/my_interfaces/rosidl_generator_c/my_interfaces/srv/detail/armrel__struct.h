// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_interfaces:srv/Armrel.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__ARMREL__STRUCT_H_
#define MY_INTERFACES__SRV__DETAIL__ARMREL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Armrel in the package my_interfaces.
typedef struct my_interfaces__srv__Armrel_Request
{
  int16_t dangle1;
  int16_t dangle2;
  int16_t dangle3;
  int16_t dangle4;
} my_interfaces__srv__Armrel_Request;

// Struct for a sequence of my_interfaces__srv__Armrel_Request.
typedef struct my_interfaces__srv__Armrel_Request__Sequence
{
  my_interfaces__srv__Armrel_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Armrel_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Armrel in the package my_interfaces.
typedef struct my_interfaces__srv__Armrel_Response
{
  bool acknowledged;
} my_interfaces__srv__Armrel_Response;

// Struct for a sequence of my_interfaces__srv__Armrel_Response.
typedef struct my_interfaces__srv__Armrel_Response__Sequence
{
  my_interfaces__srv__Armrel_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__srv__Armrel_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__SRV__DETAIL__ARMREL__STRUCT_H_
