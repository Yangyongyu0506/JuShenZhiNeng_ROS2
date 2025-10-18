# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_interfaces:srv/Armabs.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Armabs_Request(type):
    """Metaclass of message 'Armabs_Request'."""

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
                'my_interfaces.srv.Armabs_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__armabs__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__armabs__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__armabs__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__armabs__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__armabs__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Armabs_Request(metaclass=Metaclass_Armabs_Request):
    """Message class 'Armabs_Request'."""

    __slots__ = [
        '_angle1',
        '_angle2',
        '_angle3',
        '_angle4',
    ]

    _fields_and_field_types = {
        'angle1': 'int8',
        'angle2': 'int8',
        'angle3': 'int8',
        'angle4': 'int8',
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
        self.angle1 = kwargs.get('angle1', int())
        self.angle2 = kwargs.get('angle2', int())
        self.angle3 = kwargs.get('angle3', int())
        self.angle4 = kwargs.get('angle4', int())

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
        if self.angle1 != other.angle1:
            return False
        if self.angle2 != other.angle2:
            return False
        if self.angle3 != other.angle3:
            return False
        if self.angle4 != other.angle4:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def angle1(self):
        """Message field 'angle1'."""
        return self._angle1

    @angle1.setter
    def angle1(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'angle1' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'angle1' field must be an integer in [-128, 127]"
        self._angle1 = value

    @builtins.property
    def angle2(self):
        """Message field 'angle2'."""
        return self._angle2

    @angle2.setter
    def angle2(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'angle2' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'angle2' field must be an integer in [-128, 127]"
        self._angle2 = value

    @builtins.property
    def angle3(self):
        """Message field 'angle3'."""
        return self._angle3

    @angle3.setter
    def angle3(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'angle3' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'angle3' field must be an integer in [-128, 127]"
        self._angle3 = value

    @builtins.property
    def angle4(self):
        """Message field 'angle4'."""
        return self._angle4

    @angle4.setter
    def angle4(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'angle4' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'angle4' field must be an integer in [-128, 127]"
        self._angle4 = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Armabs_Response(type):
    """Metaclass of message 'Armabs_Response'."""

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
                'my_interfaces.srv.Armabs_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__armabs__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__armabs__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__armabs__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__armabs__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__armabs__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Armabs_Response(metaclass=Metaclass_Armabs_Response):
    """Message class 'Armabs_Response'."""

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


class Metaclass_Armabs(type):
    """Metaclass of service 'Armabs'."""

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
                'my_interfaces.srv.Armabs')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__armabs

            from my_interfaces.srv import _armabs
            if _armabs.Metaclass_Armabs_Request._TYPE_SUPPORT is None:
                _armabs.Metaclass_Armabs_Request.__import_type_support__()
            if _armabs.Metaclass_Armabs_Response._TYPE_SUPPORT is None:
                _armabs.Metaclass_Armabs_Response.__import_type_support__()


class Armabs(metaclass=Metaclass_Armabs):
    from my_interfaces.srv._armabs import Armabs_Request as Request
    from my_interfaces.srv._armabs import Armabs_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
