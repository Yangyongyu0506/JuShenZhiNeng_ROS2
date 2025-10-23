# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_interfaces:srv/Allservos.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

# Member 'angles'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Allservos_Request(type):
    """Metaclass of message 'Allservos_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_interfaces.srv.Allservos_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__allservos__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__allservos__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__allservos__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__allservos__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__allservos__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Allservos_Request(metaclass=Metaclass_Allservos_Request):
    """Message class 'Allservos_Request'."""

    __slots__ = [
        '_angles',
    ]

    _fields_and_field_types = {
        'angles': 'int16[5]',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('int16'), 5),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        if 'angles' not in kwargs:
            self.angles = numpy.zeros(5, dtype=numpy.int16)
        else:
            self.angles = numpy.array(kwargs.get('angles'), dtype=numpy.int16)
            assert self.angles.shape == (5, )

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if any(self.angles != other.angles):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def angles(self):
        """Message field 'angles'."""
        return self._angles

    @angles.setter
    def angles(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.int16, \
                "The 'angles' numpy.ndarray() must have the dtype of 'numpy.int16'"
            assert value.size == 5, \
                "The 'angles' numpy.ndarray() must have a size of 5"
            self._angles = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 5 and
                 all(isinstance(v, int) for v in value) and
                 all(val >= -32768 and val < 32768 for val in value)), \
                "The 'angles' field must be a set or sequence with length 5 and each value of type 'int' and each integer in [-32768, 32767]"
        self._angles = numpy.array(value, dtype=numpy.int16)


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Allservos_Response(type):
    """Metaclass of message 'Allservos_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_interfaces.srv.Allservos_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__allservos__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__allservos__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__allservos__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__allservos__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__allservos__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Allservos_Response(metaclass=Metaclass_Allservos_Response):
    """Message class 'Allservos_Response'."""

    __slots__ = [
        '_acknowledged',
    ]

    _fields_and_field_types = {
        'acknowledged': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.acknowledged = kwargs.get('acknowledged', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.acknowledged != other.acknowledged:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def acknowledged(self):
        """Message field 'acknowledged'."""
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'acknowledged' field must be of type 'bool'"
        self._acknowledged = value


class Metaclass_Allservos(type):
    """Metaclass of service 'Allservos'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('my_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'my_interfaces.srv.Allservos')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__allservos

            from my_interfaces.srv import _allservos
            if _allservos.Metaclass_Allservos_Request._TYPE_SUPPORT is None:
                _allservos.Metaclass_Allservos_Request.__import_type_support__()
            if _allservos.Metaclass_Allservos_Response._TYPE_SUPPORT is None:
                _allservos.Metaclass_Allservos_Response.__import_type_support__()


class Allservos(metaclass=Metaclass_Allservos):
    from my_interfaces.srv._allservos import Allservos_Request as Request
    from my_interfaces.srv._allservos import Allservos_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
