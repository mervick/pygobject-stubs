# encoding: utf-8
# module gi.repository.ICal
# from /usr/lib64/girepository-1.0/ICal-3.0.typelib
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
import gobject as __gobject


class value_kind(__gobject.GEnum):
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICal', '__dict__': <attribute '__dict__' of 'value_kind' objects>, '__doc__': None, '__gtype__': <GType PyICalvalue_kind (94628528871792)>, '__enum_values__': {5000: <enum ICAL_ANY_VALUE of type ICal.value_kind>, 5027: <enum ICAL_ACTION_VALUE of type ICal.value_kind>, 5003: <enum ICAL_ATTACH_VALUE of type ICal.value_kind>, 5011: <enum ICAL_BINARY_VALUE of type ICal.value_kind>, 5021: <enum ICAL_BOOLEAN_VALUE of type ICal.value_kind>, 5032: <enum ICAL_BUSYTYPE_VALUE of type ICal.value_kind>, 5023: <enum ICAL_CALADDRESS_VALUE of type ICal.value_kind>, 5016: <enum ICAL_CARLEVEL_VALUE of type ICal.value_kind>, 5019: <enum ICAL_CLASS_VALUE of type ICal.value_kind>, 5010: <enum ICAL_CMD_VALUE of type ICal.value_kind>, 5002: <enum ICAL_DATE_VALUE of type ICal.value_kind>, 5028: <enum ICAL_DATETIME_VALUE of type ICal.value_kind>, 5036: <enum ICAL_DATETIMEDATE_VALUE of type ICal.value_kind>, 5015: <enum ICAL_DATETIMEPERIOD_VALUE of type ICal.value_kind>, 5020: <enum ICAL_DURATION_VALUE of type ICal.value_kind>, 5013: <enum ICAL_FLOAT_VALUE of type ICal.value_kind>, 5004: <enum ICAL_GEO_VALUE of type ICal.value_kind>, 5017: <enum ICAL_INTEGER_VALUE of type ICal.value_kind>, 5030: <enum ICAL_METHOD_VALUE of type ICal.value_kind>, 5014: <enum ICAL_PERIOD_VALUE of type ICal.value_kind>, 5034: <enum ICAL_POLLCOMPLETION_VALUE of type ICal.value_kind>, 5033: <enum ICAL_POLLMODE_VALUE of type ICal.value_kind>, 5001: <enum ICAL_QUERY_VALUE of type ICal.value_kind>, 5012: <enum ICAL_QUERYLEVEL_VALUE of type ICal.value_kind>, 5026: <enum ICAL_RECUR_VALUE of type ICal.value_kind>, 5009: <enum ICAL_REQUESTSTATUS_VALUE of type ICal.value_kind>, 5005: <enum ICAL_STATUS_VALUE of type ICal.value_kind>, 5007: <enum ICAL_STRING_VALUE of type ICal.value_kind>, 5035: <enum ICAL_TASKMODE_VALUE of type ICal.value_kind>, 5008: <enum ICAL_TEXT_VALUE of type ICal.value_kind>, 5006: <enum ICAL_TRANSP_VALUE of type ICal.value_kind>, 5024: <enum ICAL_TRIGGER_VALUE of type ICal.value_kind>, 5018: <enum ICAL_URI_VALUE of type ICal.value_kind>, 5029: <enum ICAL_UTCOFFSET_VALUE of type ICal.value_kind>, 5022: <enum ICAL_X_VALUE of type ICal.value_kind>, 5025: <enum ICAL_XLICCLASS_VALUE of type ICal.value_kind>, 5031: <enum ICAL_NO_VALUE of type ICal.value_kind>}, '__info__': gi.EnumInfo(value_kind), 'ANY_VALUE': <enum ICAL_ANY_VALUE of type ICal.value_kind>, 'ACTION_VALUE': <enum ICAL_ACTION_VALUE of type ICal.value_kind>, 'ATTACH_VALUE': <enum ICAL_ATTACH_VALUE of type ICal.value_kind>, 'BINARY_VALUE': <enum ICAL_BINARY_VALUE of type ICal.value_kind>, 'BOOLEAN_VALUE': <enum ICAL_BOOLEAN_VALUE of type ICal.value_kind>, 'BUSYTYPE_VALUE': <enum ICAL_BUSYTYPE_VALUE of type ICal.value_kind>, 'CALADDRESS_VALUE': <enum ICAL_CALADDRESS_VALUE of type ICal.value_kind>, 'CARLEVEL_VALUE': <enum ICAL_CARLEVEL_VALUE of type ICal.value_kind>, 'CLASS_VALUE': <enum ICAL_CLASS_VALUE of type ICal.value_kind>, 'CMD_VALUE': <enum ICAL_CMD_VALUE of type ICal.value_kind>, 'DATE_VALUE': <enum ICAL_DATE_VALUE of type ICal.value_kind>, 'DATETIME_VALUE': <enum ICAL_DATETIME_VALUE of type ICal.value_kind>, 'DATETIMEDATE_VALUE': <enum ICAL_DATETIMEDATE_VALUE of type ICal.value_kind>, 'DATETIMEPERIOD_VALUE': <enum ICAL_DATETIMEPERIOD_VALUE of type ICal.value_kind>, 'DURATION_VALUE': <enum ICAL_DURATION_VALUE of type ICal.value_kind>, 'FLOAT_VALUE': <enum ICAL_FLOAT_VALUE of type ICal.value_kind>, 'GEO_VALUE': <enum ICAL_GEO_VALUE of type ICal.value_kind>, 'INTEGER_VALUE': <enum ICAL_INTEGER_VALUE of type ICal.value_kind>, 'METHOD_VALUE': <enum ICAL_METHOD_VALUE of type ICal.value_kind>, 'PERIOD_VALUE': <enum ICAL_PERIOD_VALUE of type ICal.value_kind>, 'POLLCOMPLETION_VALUE': <enum ICAL_POLLCOMPLETION_VALUE of type ICal.value_kind>, 'POLLMODE_VALUE': <enum ICAL_POLLMODE_VALUE of type ICal.value_kind>, 'QUERY_VALUE': <enum ICAL_QUERY_VALUE of type ICal.value_kind>, 'QUERYLEVEL_VALUE': <enum ICAL_QUERYLEVEL_VALUE of type ICal.value_kind>, 'RECUR_VALUE': <enum ICAL_RECUR_VALUE of type ICal.value_kind>, 'REQUESTSTATUS_VALUE': <enum ICAL_REQUESTSTATUS_VALUE of type ICal.value_kind>, 'STATUS_VALUE': <enum ICAL_STATUS_VALUE of type ICal.value_kind>, 'STRING_VALUE': <enum ICAL_STRING_VALUE of type ICal.value_kind>, 'TASKMODE_VALUE': <enum ICAL_TASKMODE_VALUE of type ICal.value_kind>, 'TEXT_VALUE': <enum ICAL_TEXT_VALUE of type ICal.value_kind>, 'TRANSP_VALUE': <enum ICAL_TRANSP_VALUE of type ICal.value_kind>, 'TRIGGER_VALUE': <enum ICAL_TRIGGER_VALUE of type ICal.value_kind>, 'URI_VALUE': <enum ICAL_URI_VALUE of type ICal.value_kind>, 'UTCOFFSET_VALUE': <enum ICAL_UTCOFFSET_VALUE of type ICal.value_kind>, 'X_VALUE': <enum ICAL_X_VALUE of type ICal.value_kind>, 'XLICCLASS_VALUE': <enum ICAL_XLICCLASS_VALUE of type ICal.value_kind>, 'NO_VALUE': <enum ICAL_NO_VALUE of type ICal.value_kind>})"
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
    __gtype__ = None # (!) real value is '<GType PyICalvalue_kind (94628528871792)>'
    __info__ = gi.EnumInfo(value_kind)


