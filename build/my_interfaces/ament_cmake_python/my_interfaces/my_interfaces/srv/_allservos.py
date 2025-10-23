# generated from rosidl_generator_py/resource/_idl.py.em
# with input from my_interfaces:srv/Allservos.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

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
        '_angle1',
        '_angle2',
        '_angle3',
        '_angle4',
        '_angle5',
        '_angle6',
    ]

    _fields_and_field_types = {
        'angle1': 'int16',
        'angle2': 'int16',
        'angle3': 'int16',
        'angle4': 'int16',
        'angle5': 'int16',
        'angle6': 'int16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.angle1 = kwargs.get('angle1', int())
        self.angle2 = kwargs.get('angle2', int())
        self.angle3 = kwargs.get('angle3', int())
        self.angle4 = kwargs.get('angle4', int())
        self.angle5 = kwargs.get('angle5', int())
        self.angle6 = kwargs.get('angle6', int())

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
        if self.angle5 != other.angle5:
            return False
        if self.angle6 != other.angle6:
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
            assert value >= -32768 and value < 32768, \
                "The 'angle1' field must be an integer in [-32768, 32767]"
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
            assert value >= -32768 and value < 32768, \
                "The 'angle2' field must be an integer in [-32768, 32767]"
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
            assert value >= -32768 and value < 32768, \
                "The 'angle3' field must be an integer in [-32768, 32767]"
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
            assert value >= -32768 and value < 32768, \
                "The 'angle4' field must be an integer in [-32768, 32767]"
        self._angle4 = value

    @builtins.property
    def angle5(self):
        """Message field 'angle5'."""
        return self._angle5

    @angle5.setter
    def angle5(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'angle5' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'angle5' field must be an integer in [-32768, 32767]"
        self._angle5 = value

    @builtins.property
    def angle6(self):
        """Message field 'angle6'."""
        return self._angle6

    @angle6.setter
    def angle6(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'angle6' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'angle6' field must be an integer in [-32768, 32767]"
        self._angle6 = value


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
