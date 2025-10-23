// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from my_interfaces:srv/Armabs.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "my_interfaces/srv/detail/armabs__struct.h"
#include "my_interfaces/srv/detail/armabs__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool my_interfaces__srv__armabs__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[41];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("my_interfaces.srv._armabs.Armabs_Request", full_classname_dest, 40) == 0);
  }
  my_interfaces__srv__Armabs_Request * ros_message = _ros_message;
  {  // angle1
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle1");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->angle1 = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // angle2
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle2");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->angle2 = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // angle3
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle3");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->angle3 = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // angle4
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle4");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->angle4 = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * my_interfaces__srv__armabs__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Armabs_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("my_interfaces.srv._armabs");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Armabs_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  my_interfaces__srv__Armabs_Request * ros_message = (my_interfaces__srv__Armabs_Request *)raw_ros_message;
  {  // angle1
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->angle1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle2
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->angle2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle3
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->angle3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle4
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->angle4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "my_interfaces/srv/detail/armabs__struct.h"
// already included above
// #include "my_interfaces/srv/detail/armabs__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool my_interfaces__srv__armabs__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[42];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("my_interfaces.srv._armabs.Armabs_Response", full_classname_dest, 41) == 0);
  }
  my_interfaces__srv__Armabs_Response * ros_message = _ros_message;
  {  // acknowledged
    PyObject * field = PyObject_GetAttrString(_pymsg, "acknowledged");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->acknowledged = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * my_interfaces__srv__armabs__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Armabs_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("my_interfaces.srv._armabs");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Armabs_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  my_interfaces__srv__Armabs_Response * ros_message = (my_interfaces__srv__Armabs_Response *)raw_ros_message;
  {  // acknowledged
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->acknowledged ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acknowledged", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
