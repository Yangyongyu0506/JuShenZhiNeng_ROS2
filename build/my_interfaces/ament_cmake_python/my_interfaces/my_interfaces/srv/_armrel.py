# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_interfaces:srv/Armrel.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Armrel_Request(type):
    """Metaclass of message 'Armrel_Request'."""

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
                'my_interfaces.srv.Armrel_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__armrel__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__armrel__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__armrel__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__armrel__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__armrel__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Armrel_Request(metaclass=Metaclass_Armrel_Request):
    """Message class 'Armrel_Request'."""

    __slots__ = [
        '_dangle1',
        '_dangle2',
        '_dangle3',
        '_dangle4',
    ]

    _fields_and_field_types = {
        'dangle1': 'int8',
        'dangle2': 'int8',
        'dangle3': 'int8',
        'dangle4': 'int8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.dangle1 = kwargs.get('dangle1', int())
        self.dangle2 = kwargs.get('dangle2', int())
        self.dangle3 = kwargs.get('dangle3', int())
        self.dangle4 = kwargs.get('dangle4', int())

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
        if self.dangle1 != other.dangle1:
            return False
        if self.dangle2 != other.dangle2:
            return False
        if self.dangle3 != other.dangle3:
            return False
        if self.dangle4 != other.dangle4:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def dangle1(self):
        """Message field 'dangle1'."""
        return self._dangle1

    @dangle1.setter
    def dangle1(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dangle1' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'dangle1' field must be an integer in [-128, 127]"
        self._dangle1 = value

    @builtins.property
    def dangle2(self):
        """Message field 'dangle2'."""
        return self._dangle2

    @dangle2.setter
    def dangle2(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dangle2' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'dangle2' field must be an integer in [-128, 127]"
        self._dangle2 = value

    @builtins.property
    def dangle3(self):
        """Message field 'dangle3'."""
        return self._dangle3

    @dangle3.setter
    def dangle3(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dangle3' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'dangle3' field must be an integer in [-128, 127]"
        self._dangle3 = value

    @builtins.property
    def dangle4(self):
        """Message field 'dangle4'."""
        return self._dangle4

    @dangle4.setter
    def dangle4(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dangle4' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'dangle4' field must be an integer in [-128, 127]"
        self._dangle4 = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Armrel_Response(type):
    """Metaclass of message 'Armrel_Response'."""

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
                'my_interfaces.srv.Armrel_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__armrel__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__armrel__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__armrel__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__armrel__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__armrel__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Armrel_Response(metaclass=Metaclass_Armrel_Response):
    """Message class 'Armrel_Response'."""

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


class Metaclass_Armrel(type):
    """Metaclass of service 'Armrel'."""

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
                'my_interfaces.srv.Armrel')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__armrel

            from my_interfaces.srv import _armrel
            if _armrel.Metaclass_Armrel_Request._TYPE_SUPPORT is None:
                _armrel.Metaclass_Armrel_Request.__import_type_support__()
            if _armrel.Metaclass_Armrel_Response._TYPE_SUPPORT is None:
                _armrel.Metaclass_Armrel_Response.__import_type_support__()


class Armrel(metaclass=Metaclass_Armrel):
    from my_interfaces.srv._armrel import Armrel_Request as Request
    from my_interfaces.srv._armrel import Armrel_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
