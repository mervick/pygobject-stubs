# encoding: utf-8
# module gi.repository.ICalGLib
# from /usr/lib64/girepository-1.0/ICalGLib-3.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class ValueKind(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ACTION_VALUE = 5027
    ANY_VALUE = 5000
    ATTACH_VALUE = 5003
    BINARY_VALUE = 5011
    BOOLEAN_VALUE = 5021
    BUSYTYPE_VALUE = 5032
    CALADDRESS_VALUE = 5023
    CARLEVEL_VALUE = 5016
    CLASS_VALUE = 5019
    CMD_VALUE = 5010
    DATETIMEDATE_VALUE = 5036
    DATETIMEPERIOD_VALUE = 5015
    DATETIME_VALUE = 5028
    DATE_VALUE = 5002
    DURATION_VALUE = 5020
    FLOAT_VALUE = 5013
    GEO_VALUE = 5004
    INTEGER_VALUE = 5017
    METHOD_VALUE = 5030
    NO_VALUE = 5031
    PERIOD_VALUE = 5014
    POLLCOMPLETION_VALUE = 5034
    POLLMODE_VALUE = 5033
    QUERYLEVEL_VALUE = 5012
    QUERY_VALUE = 5001
    RECUR_VALUE = 5026
    REQUESTSTATUS_VALUE = 5009
    STATUS_VALUE = 5005
    STRING_VALUE = 5007
    TASKMODE_VALUE = 5035
    TEXT_VALUE = 5008
    TRANSP_VALUE = 5006
    TRIGGER_VALUE = 5024
    URI_VALUE = 5018
    UTCOFFSET_VALUE = 5029
    XLICCLASS_VALUE = 5025
    X_VALUE = 5022
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICalGLib', '__dict__': <attribute '__dict__' of 'ValueKind' objects>, '__doc__': None, '__gtype__': <GType PyICalGLibValueKind (94403188614944)>, '__enum_values__': {5000: <enum I_CAL_ANY_VALUE of type ICalGLib.ValueKind>, 5027: <enum I_CAL_ACTION_VALUE of type ICalGLib.ValueKind>, 5003: <enum I_CAL_ATTACH_VALUE of type ICalGLib.ValueKind>, 5011: <enum I_CAL_BINARY_VALUE of type ICalGLib.ValueKind>, 5021: <enum I_CAL_BOOLEAN_VALUE of type ICalGLib.ValueKind>, 5032: <enum I_CAL_BUSYTYPE_VALUE of type ICalGLib.ValueKind>, 5023: <enum I_CAL_CALADDRESS_VALUE of type ICalGLib.ValueKind>, 5016: <enum I_CAL_CARLEVEL_VALUE of type ICalGLib.ValueKind>, 5019: <enum I_CAL_CLASS_VALUE of type ICalGLib.ValueKind>, 5010: <enum I_CAL_CMD_VALUE of type ICalGLib.ValueKind>, 5002: <enum I_CAL_DATE_VALUE of type ICalGLib.ValueKind>, 5028: <enum I_CAL_DATETIME_VALUE of type ICalGLib.ValueKind>, 5036: <enum I_CAL_DATETIMEDATE_VALUE of type ICalGLib.ValueKind>, 5015: <enum I_CAL_DATETIMEPERIOD_VALUE of type ICalGLib.ValueKind>, 5020: <enum I_CAL_DURATION_VALUE of type ICalGLib.ValueKind>, 5013: <enum I_CAL_FLOAT_VALUE of type ICalGLib.ValueKind>, 5004: <enum I_CAL_GEO_VALUE of type ICalGLib.ValueKind>, 5017: <enum I_CAL_INTEGER_VALUE of type ICalGLib.ValueKind>, 5030: <enum I_CAL_METHOD_VALUE of type ICalGLib.ValueKind>, 5014: <enum I_CAL_PERIOD_VALUE of type ICalGLib.ValueKind>, 5034: <enum I_CAL_POLLCOMPLETION_VALUE of type ICalGLib.ValueKind>, 5033: <enum I_CAL_POLLMODE_VALUE of type ICalGLib.ValueKind>, 5001: <enum I_CAL_QUERY_VALUE of type ICalGLib.ValueKind>, 5012: <enum I_CAL_QUERYLEVEL_VALUE of type ICalGLib.ValueKind>, 5026: <enum I_CAL_RECUR_VALUE of type ICalGLib.ValueKind>, 5009: <enum I_CAL_REQUESTSTATUS_VALUE of type ICalGLib.ValueKind>, 5005: <enum I_CAL_STATUS_VALUE of type ICalGLib.ValueKind>, 5007: <enum I_CAL_STRING_VALUE of type ICalGLib.ValueKind>, 5035: <enum I_CAL_TASKMODE_VALUE of type ICalGLib.ValueKind>, 5008: <enum I_CAL_TEXT_VALUE of type ICalGLib.ValueKind>, 5006: <enum I_CAL_TRANSP_VALUE of type ICalGLib.ValueKind>, 5024: <enum I_CAL_TRIGGER_VALUE of type ICalGLib.ValueKind>, 5018: <enum I_CAL_URI_VALUE of type ICalGLib.ValueKind>, 5029: <enum I_CAL_UTCOFFSET_VALUE of type ICalGLib.ValueKind>, 5022: <enum I_CAL_X_VALUE of type ICalGLib.ValueKind>, 5025: <enum I_CAL_XLICCLASS_VALUE of type ICalGLib.ValueKind>, 5031: <enum I_CAL_NO_VALUE of type ICalGLib.ValueKind>}, '__info__': gi.EnumInfo(ValueKind), 'ANY_VALUE': <enum I_CAL_ANY_VALUE of type ICalGLib.ValueKind>, 'ACTION_VALUE': <enum I_CAL_ACTION_VALUE of type ICalGLib.ValueKind>, 'ATTACH_VALUE': <enum I_CAL_ATTACH_VALUE of type ICalGLib.ValueKind>, 'BINARY_VALUE': <enum I_CAL_BINARY_VALUE of type ICalGLib.ValueKind>, 'BOOLEAN_VALUE': <enum I_CAL_BOOLEAN_VALUE of type ICalGLib.ValueKind>, 'BUSYTYPE_VALUE': <enum I_CAL_BUSYTYPE_VALUE of type ICalGLib.ValueKind>, 'CALADDRESS_VALUE': <enum I_CAL_CALADDRESS_VALUE of type ICalGLib.ValueKind>, 'CARLEVEL_VALUE': <enum I_CAL_CARLEVEL_VALUE of type ICalGLib.ValueKind>, 'CLASS_VALUE': <enum I_CAL_CLASS_VALUE of type ICalGLib.ValueKind>, 'CMD_VALUE': <enum I_CAL_CMD_VALUE of type ICalGLib.ValueKind>, 'DATE_VALUE': <enum I_CAL_DATE_VALUE of type ICalGLib.ValueKind>, 'DATETIME_VALUE': <enum I_CAL_DATETIME_VALUE of type ICalGLib.ValueKind>, 'DATETIMEDATE_VALUE': <enum I_CAL_DATETIMEDATE_VALUE of type ICalGLib.ValueKind>, 'DATETIMEPERIOD_VALUE': <enum I_CAL_DATETIMEPERIOD_VALUE of type ICalGLib.ValueKind>, 'DURATION_VALUE': <enum I_CAL_DURATION_VALUE of type ICalGLib.ValueKind>, 'FLOAT_VALUE': <enum I_CAL_FLOAT_VALUE of type ICalGLib.ValueKind>, 'GEO_VALUE': <enum I_CAL_GEO_VALUE of type ICalGLib.ValueKind>, 'INTEGER_VALUE': <enum I_CAL_INTEGER_VALUE of type ICalGLib.ValueKind>, 'METHOD_VALUE': <enum I_CAL_METHOD_VALUE of type ICalGLib.ValueKind>, 'PERIOD_VALUE': <enum I_CAL_PERIOD_VALUE of type ICalGLib.ValueKind>, 'POLLCOMPLETION_VALUE': <enum I_CAL_POLLCOMPLETION_VALUE of type ICalGLib.ValueKind>, 'POLLMODE_VALUE': <enum I_CAL_POLLMODE_VALUE of type ICalGLib.ValueKind>, 'QUERY_VALUE': <enum I_CAL_QUERY_VALUE of type ICalGLib.ValueKind>, 'QUERYLEVEL_VALUE': <enum I_CAL_QUERYLEVEL_VALUE of type ICalGLib.ValueKind>, 'RECUR_VALUE': <enum I_CAL_RECUR_VALUE of type ICalGLib.ValueKind>, 'REQUESTSTATUS_VALUE': <enum I_CAL_REQUESTSTATUS_VALUE of type ICalGLib.ValueKind>, 'STATUS_VALUE': <enum I_CAL_STATUS_VALUE of type ICalGLib.ValueKind>, 'STRING_VALUE': <enum I_CAL_STRING_VALUE of type ICalGLib.ValueKind>, 'TASKMODE_VALUE': <enum I_CAL_TASKMODE_VALUE of type ICalGLib.ValueKind>, 'TEXT_VALUE': <enum I_CAL_TEXT_VALUE of type ICalGLib.ValueKind>, 'TRANSP_VALUE': <enum I_CAL_TRANSP_VALUE of type ICalGLib.ValueKind>, 'TRIGGER_VALUE': <enum I_CAL_TRIGGER_VALUE of type ICalGLib.ValueKind>, 'URI_VALUE': <enum I_CAL_URI_VALUE of type ICalGLib.ValueKind>, 'UTCOFFSET_VALUE': <enum I_CAL_UTCOFFSET_VALUE of type ICalGLib.ValueKind>, 'X_VALUE': <enum I_CAL_X_VALUE of type ICalGLib.ValueKind>, 'XLICCLASS_VALUE': <enum I_CAL_XLICCLASS_VALUE of type ICalGLib.ValueKind>, 'NO_VALUE': <enum I_CAL_NO_VALUE of type ICalGLib.ValueKind>})"
    __enum_values__ = {
        5000: 5000,
        5001: 5001,
        5002: 5002,
        5003: 5003,
        5004: 5004,
        5005: 5005,
        5006: 5006,
        5007: 5007,
        5008: 5008,
        5009: 5009,
        5010: 5010,
        5011: 5011,
        5012: 5012,
        5013: 5013,
        5014: 5014,
        5015: 5015,
        5016: 5016,
        5017: 5017,
        5018: 5018,
        5019: 5019,
        5020: 5020,
        5021: 5021,
        5022: 5022,
        5023: 5023,
        5024: 5024,
        5025: 5025,
        5026: 5026,
        5027: 5027,
        5028: 5028,
        5029: 5029,
        5030: 5030,
        5031: 5031,
        5032: 5032,
        5033: 5033,
        5034: 5034,
        5035: 5035,
        5036: 5036,
    }
    __gtype__ = None # (!) real value is '<GType PyICalGLibValueKind (94403188614944)>'
    __info__ = gi.EnumInfo(ValueKind)


