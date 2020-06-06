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


class ParameterKind(__gobject.GEnum):
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


    ACTIONPARAM_PARAMETER = 1
    ALTREP_PARAMETER = 2
    ANY_PARAMETER = 0
    CHARSET_PARAMETER = 3
    CN_PARAMETER = 4
    CUTYPE_PARAMETER = 5
    DELEGATEDFROM_PARAMETER = 6
    DELEGATEDTO_PARAMETER = 7
    DIR_PARAMETER = 8
    ENABLE_PARAMETER = 9
    ENCODING_PARAMETER = 10
    FBTYPE_PARAMETER = 11
    FILENAME_PARAMETER = 42
    FMTTYPE_PARAMETER = 12
    IANA_PARAMETER = 33
    ID_PARAMETER = 13
    LANGUAGE_PARAMETER = 14
    LATENCY_PARAMETER = 15
    LOCALIZE_PARAMETER = 17
    LOCAL_PARAMETER = 16
    MANAGEDID_PARAMETER = 40
    MEMBER_PARAMETER = 18
    MODIFIED_PARAMETER = 44
    NO_PARAMETER = 32
    OPTIONS_PARAMETER = 19
    PARTSTAT_PARAMETER = 20
    PUBLICCOMMENT_PARAMETER = 37
    RANGE_PARAMETER = 21
    REASON_PARAMETER = 43
    RELATED_PARAMETER = 22
    RELTYPE_PARAMETER = 23
    REQUIRED_PARAMETER = 43
    RESPONSE_PARAMETER = 38
    ROLE_PARAMETER = 24
    RSVP_PARAMETER = 25
    SCHEDULEAGENT_PARAMETER = 34
    SCHEDULEFORCESEND_PARAMETER = 35
    SCHEDULESTATUS_PARAMETER = 36
    SENTBY_PARAMETER = 26
    SIZE_PARAMETER = 41
    STAYINFORMED_PARAMETER = 39
    SUBSTATE_PARAMETER = 45
    TZID_PARAMETER = 27
    VALUE_PARAMETER = 28
    XLICCOMPARETYPE_PARAMETER = 30
    XLICERRORTYPE_PARAMETER = 31
    X_PARAMETER = 29
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICalGLib', '__dict__': <attribute '__dict__' of 'ParameterKind' objects>, '__doc__': None, '__gtype__': <GType PyICalGLibParameterKind (94403188315728)>, '__enum_values__': {0: <enum I_CAL_ANY_PARAMETER of type ICalGLib.ParameterKind>, 1: <enum I_CAL_ACTIONPARAM_PARAMETER of type ICalGLib.ParameterKind>, 2: <enum I_CAL_ALTREP_PARAMETER of type ICalGLib.ParameterKind>, 3: <enum I_CAL_CHARSET_PARAMETER of type ICalGLib.ParameterKind>, 4: <enum I_CAL_CN_PARAMETER of type ICalGLib.ParameterKind>, 5: <enum I_CAL_CUTYPE_PARAMETER of type ICalGLib.ParameterKind>, 6: <enum I_CAL_DELEGATEDFROM_PARAMETER of type ICalGLib.ParameterKind>, 7: <enum I_CAL_DELEGATEDTO_PARAMETER of type ICalGLib.ParameterKind>, 8: <enum I_CAL_DIR_PARAMETER of type ICalGLib.ParameterKind>, 9: <enum I_CAL_ENABLE_PARAMETER of type ICalGLib.ParameterKind>, 10: <enum I_CAL_ENCODING_PARAMETER of type ICalGLib.ParameterKind>, 11: <enum I_CAL_FBTYPE_PARAMETER of type ICalGLib.ParameterKind>, 42: <enum I_CAL_FILENAME_PARAMETER of type ICalGLib.ParameterKind>, 12: <enum I_CAL_FMTTYPE_PARAMETER of type ICalGLib.ParameterKind>, 33: <enum I_CAL_IANA_PARAMETER of type ICalGLib.ParameterKind>, 13: <enum I_CAL_ID_PARAMETER of type ICalGLib.ParameterKind>, 14: <enum I_CAL_LANGUAGE_PARAMETER of type ICalGLib.ParameterKind>, 15: <enum I_CAL_LATENCY_PARAMETER of type ICalGLib.ParameterKind>, 16: <enum I_CAL_LOCAL_PARAMETER of type ICalGLib.ParameterKind>, 17: <enum I_CAL_LOCALIZE_PARAMETER of type ICalGLib.ParameterKind>, 40: <enum I_CAL_MANAGEDID_PARAMETER of type ICalGLib.ParameterKind>, 18: <enum I_CAL_MEMBER_PARAMETER of type ICalGLib.ParameterKind>, 44: <enum I_CAL_MODIFIED_PARAMETER of type ICalGLib.ParameterKind>, 19: <enum I_CAL_OPTIONS_PARAMETER of type ICalGLib.ParameterKind>, 20: <enum I_CAL_PARTSTAT_PARAMETER of type ICalGLib.ParameterKind>, 37: <enum I_CAL_PUBLICCOMMENT_PARAMETER of type ICalGLib.ParameterKind>, 21: <enum I_CAL_RANGE_PARAMETER of type ICalGLib.ParameterKind>, 43: <enum I_CAL_REASON_PARAMETER of type ICalGLib.ParameterKind>, 22: <enum I_CAL_RELATED_PARAMETER of type ICalGLib.ParameterKind>, 23: <enum I_CAL_RELTYPE_PARAMETER of type ICalGLib.ParameterKind>, 38: <enum I_CAL_RESPONSE_PARAMETER of type ICalGLib.ParameterKind>, 24: <enum I_CAL_ROLE_PARAMETER of type ICalGLib.ParameterKind>, 25: <enum I_CAL_RSVP_PARAMETER of type ICalGLib.ParameterKind>, 34: <enum I_CAL_SCHEDULEAGENT_PARAMETER of type ICalGLib.ParameterKind>, 35: <enum I_CAL_SCHEDULEFORCESEND_PARAMETER of type ICalGLib.ParameterKind>, 36: <enum I_CAL_SCHEDULESTATUS_PARAMETER of type ICalGLib.ParameterKind>, 26: <enum I_CAL_SENTBY_PARAMETER of type ICalGLib.ParameterKind>, 41: <enum I_CAL_SIZE_PARAMETER of type ICalGLib.ParameterKind>, 39: <enum I_CAL_STAYINFORMED_PARAMETER of type ICalGLib.ParameterKind>, 45: <enum I_CAL_SUBSTATE_PARAMETER of type ICalGLib.ParameterKind>, 27: <enum I_CAL_TZID_PARAMETER of type ICalGLib.ParameterKind>, 28: <enum I_CAL_VALUE_PARAMETER of type ICalGLib.ParameterKind>, 29: <enum I_CAL_X_PARAMETER of type ICalGLib.ParameterKind>, 30: <enum I_CAL_XLICCOMPARETYPE_PARAMETER of type ICalGLib.ParameterKind>, 31: <enum I_CAL_XLICERRORTYPE_PARAMETER of type ICalGLib.ParameterKind>, 32: <enum I_CAL_NO_PARAMETER of type ICalGLib.ParameterKind>}, '__info__': gi.EnumInfo(ParameterKind), 'ANY_PARAMETER': <enum I_CAL_ANY_PARAMETER of type ICalGLib.ParameterKind>, 'ACTIONPARAM_PARAMETER': <enum I_CAL_ACTIONPARAM_PARAMETER of type ICalGLib.ParameterKind>, 'ALTREP_PARAMETER': <enum I_CAL_ALTREP_PARAMETER of type ICalGLib.ParameterKind>, 'CHARSET_PARAMETER': <enum I_CAL_CHARSET_PARAMETER of type ICalGLib.ParameterKind>, 'CN_PARAMETER': <enum I_CAL_CN_PARAMETER of type ICalGLib.ParameterKind>, 'CUTYPE_PARAMETER': <enum I_CAL_CUTYPE_PARAMETER of type ICalGLib.ParameterKind>, 'DELEGATEDFROM_PARAMETER': <enum I_CAL_DELEGATEDFROM_PARAMETER of type ICalGLib.ParameterKind>, 'DELEGATEDTO_PARAMETER': <enum I_CAL_DELEGATEDTO_PARAMETER of type ICalGLib.ParameterKind>, 'DIR_PARAMETER': <enum I_CAL_DIR_PARAMETER of type ICalGLib.ParameterKind>, 'ENABLE_PARAMETER': <enum I_CAL_ENABLE_PARAMETER of type ICalGLib.ParameterKind>, 'ENCODING_PARAMETER': <enum I_CAL_ENCODING_PARAMETER of type ICalGLib.ParameterKind>, 'FBTYPE_PARAMETER': <enum I_CAL_FBTYPE_PARAMETER of type ICalGLib.ParameterKind>, 'FILENAME_PARAMETER': <enum I_CAL_FILENAME_PARAMETER of type ICalGLib.ParameterKind>, 'FMTTYPE_PARAMETER': <enum I_CAL_FMTTYPE_PARAMETER of type ICalGLib.ParameterKind>, 'IANA_PARAMETER': <enum I_CAL_IANA_PARAMETER of type ICalGLib.ParameterKind>, 'ID_PARAMETER': <enum I_CAL_ID_PARAMETER of type ICalGLib.ParameterKind>, 'LANGUAGE_PARAMETER': <enum I_CAL_LANGUAGE_PARAMETER of type ICalGLib.ParameterKind>, 'LATENCY_PARAMETER': <enum I_CAL_LATENCY_PARAMETER of type ICalGLib.ParameterKind>, 'LOCAL_PARAMETER': <enum I_CAL_LOCAL_PARAMETER of type ICalGLib.ParameterKind>, 'LOCALIZE_PARAMETER': <enum I_CAL_LOCALIZE_PARAMETER of type ICalGLib.ParameterKind>, 'MANAGEDID_PARAMETER': <enum I_CAL_MANAGEDID_PARAMETER of type ICalGLib.ParameterKind>, 'MEMBER_PARAMETER': <enum I_CAL_MEMBER_PARAMETER of type ICalGLib.ParameterKind>, 'MODIFIED_PARAMETER': <enum I_CAL_MODIFIED_PARAMETER of type ICalGLib.ParameterKind>, 'OPTIONS_PARAMETER': <enum I_CAL_OPTIONS_PARAMETER of type ICalGLib.ParameterKind>, 'PARTSTAT_PARAMETER': <enum I_CAL_PARTSTAT_PARAMETER of type ICalGLib.ParameterKind>, 'PUBLICCOMMENT_PARAMETER': <enum I_CAL_PUBLICCOMMENT_PARAMETER of type ICalGLib.ParameterKind>, 'RANGE_PARAMETER': <enum I_CAL_RANGE_PARAMETER of type ICalGLib.ParameterKind>, 'REASON_PARAMETER': <enum I_CAL_REASON_PARAMETER of type ICalGLib.ParameterKind>, 'RELATED_PARAMETER': <enum I_CAL_RELATED_PARAMETER of type ICalGLib.ParameterKind>, 'RELTYPE_PARAMETER': <enum I_CAL_RELTYPE_PARAMETER of type ICalGLib.ParameterKind>, 'REQUIRED_PARAMETER': <enum I_CAL_REASON_PARAMETER of type ICalGLib.ParameterKind>, 'RESPONSE_PARAMETER': <enum I_CAL_RESPONSE_PARAMETER of type ICalGLib.ParameterKind>, 'ROLE_PARAMETER': <enum I_CAL_ROLE_PARAMETER of type ICalGLib.ParameterKind>, 'RSVP_PARAMETER': <enum I_CAL_RSVP_PARAMETER of type ICalGLib.ParameterKind>, 'SCHEDULEAGENT_PARAMETER': <enum I_CAL_SCHEDULEAGENT_PARAMETER of type ICalGLib.ParameterKind>, 'SCHEDULEFORCESEND_PARAMETER': <enum I_CAL_SCHEDULEFORCESEND_PARAMETER of type ICalGLib.ParameterKind>, 'SCHEDULESTATUS_PARAMETER': <enum I_CAL_SCHEDULESTATUS_PARAMETER of type ICalGLib.ParameterKind>, 'SENTBY_PARAMETER': <enum I_CAL_SENTBY_PARAMETER of type ICalGLib.ParameterKind>, 'SIZE_PARAMETER': <enum I_CAL_SIZE_PARAMETER of type ICalGLib.ParameterKind>, 'STAYINFORMED_PARAMETER': <enum I_CAL_STAYINFORMED_PARAMETER of type ICalGLib.ParameterKind>, 'SUBSTATE_PARAMETER': <enum I_CAL_SUBSTATE_PARAMETER of type ICalGLib.ParameterKind>, 'TZID_PARAMETER': <enum I_CAL_TZID_PARAMETER of type ICalGLib.ParameterKind>, 'VALUE_PARAMETER': <enum I_CAL_VALUE_PARAMETER of type ICalGLib.ParameterKind>, 'X_PARAMETER': <enum I_CAL_X_PARAMETER of type ICalGLib.ParameterKind>, 'XLICCOMPARETYPE_PARAMETER': <enum I_CAL_XLICCOMPARETYPE_PARAMETER of type ICalGLib.ParameterKind>, 'XLICERRORTYPE_PARAMETER': <enum I_CAL_XLICERRORTYPE_PARAMETER of type ICalGLib.ParameterKind>, 'NO_PARAMETER': <enum I_CAL_NO_PARAMETER of type ICalGLib.ParameterKind>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
    }
    __gtype__ = None # (!) real value is '<GType PyICalGLibParameterKind (94403188315728)>'
    __info__ = gi.EnumInfo(ParameterKind)


