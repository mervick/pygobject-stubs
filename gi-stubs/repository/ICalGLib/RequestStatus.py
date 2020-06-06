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


class RequestStatus(__gobject.GEnum):
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


    2_0_SUCCESS_STATUS = 1
    2_10_ONETODO_STATUS = 11
    2_11_TRUNCRRULE_STATUS = 12
    2_1_FALLBACK_STATUS = 2
    2_2_IGPROP_STATUS = 3
    2_3_IGPARAM_STATUS = 4
    2_4_IGXPROP_STATUS = 5
    2_5_IGXPARAM_STATUS = 6
    2_6_IGCOMP_STATUS = 7
    2_7_FORWARD_STATUS = 8
    2_8_ONEEVENT_STATUS = 9
    2_9_TRUNC_STATUS = 10
    3_0_INVPROPNAME_STATUS = 13
    3_10_TOOBIG_STATUS = 23
    3_11_MISSREQCOMP_STATUS = 24
    3_12_UNKCOMP_STATUS = 25
    3_13_BADCOMP_STATUS = 26
    3_14_NOCAP_STATUS = 27
    3_15_INVCOMMAND = 28
    3_1_INVPROPVAL_STATUS = 14
    3_2_INVPARAM_STATUS = 15
    3_3_INVPARAMVAL_STATUS = 16
    3_4_INVCOMP_STATUS = 17
    3_5_INVTIME_STATUS = 18
    3_6_INVRULE_STATUS = 19
    3_7_INVCU_STATUS = 20
    3_8_NOAUTH_STATUS = 21
    3_9_BADVERSION_STATUS = 22
    4_0_BUSY_STATUS = 29
    4_1_STORE_ACCESS_DENIED = 30
    4_2_STORE_FAILED = 31
    4_3_STORE_NOT_FOUND = 32
    5_0_MAYBE_STATUS = 33
    5_1_UNAVAIL_STATUS = 34
    5_2_NOSERVICE_STATUS = 35
    5_3_NOSCHED_STATUS = 36
    6_1_CONTAINER_NOT_FOUND = 37
    9_0_UNRECOGNIZED_COMMAND = 38
    UNKNOWN_STATUS = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICalGLib', '__dict__': <attribute '__dict__' of 'RequestStatus' objects>, '__doc__': None, '__gtype__': <GType PyICalGLibRequestStatus (94403188547104)>, '__enum_values__': {0: <enum I_CAL_UNKNOWN_STATUS of type ICalGLib.RequestStatus>, 1: <enum I_CAL_2_0_SUCCESS_STATUS of type ICalGLib.RequestStatus>, 2: <enum I_CAL_2_1_FALLBACK_STATUS of type ICalGLib.RequestStatus>, 3: <enum I_CAL_2_2_IGPROP_STATUS of type ICalGLib.RequestStatus>, 4: <enum I_CAL_2_3_IGPARAM_STATUS of type ICalGLib.RequestStatus>, 5: <enum I_CAL_2_4_IGXPROP_STATUS of type ICalGLib.RequestStatus>, 6: <enum I_CAL_2_5_IGXPARAM_STATUS of type ICalGLib.RequestStatus>, 7: <enum I_CAL_2_6_IGCOMP_STATUS of type ICalGLib.RequestStatus>, 8: <enum I_CAL_2_7_FORWARD_STATUS of type ICalGLib.RequestStatus>, 9: <enum I_CAL_2_8_ONEEVENT_STATUS of type ICalGLib.RequestStatus>, 10: <enum I_CAL_2_9_TRUNC_STATUS of type ICalGLib.RequestStatus>, 11: <enum I_CAL_2_10_ONETODO_STATUS of type ICalGLib.RequestStatus>, 12: <enum I_CAL_2_11_TRUNCRRULE_STATUS of type ICalGLib.RequestStatus>, 13: <enum I_CAL_3_0_INVPROPNAME_STATUS of type ICalGLib.RequestStatus>, 14: <enum I_CAL_3_1_INVPROPVAL_STATUS of type ICalGLib.RequestStatus>, 15: <enum I_CAL_3_2_INVPARAM_STATUS of type ICalGLib.RequestStatus>, 16: <enum I_CAL_3_3_INVPARAMVAL_STATUS of type ICalGLib.RequestStatus>, 17: <enum I_CAL_3_4_INVCOMP_STATUS of type ICalGLib.RequestStatus>, 18: <enum I_CAL_3_5_INVTIME_STATUS of type ICalGLib.RequestStatus>, 19: <enum I_CAL_3_6_INVRULE_STATUS of type ICalGLib.RequestStatus>, 20: <enum I_CAL_3_7_INVCU_STATUS of type ICalGLib.RequestStatus>, 21: <enum I_CAL_3_8_NOAUTH_STATUS of type ICalGLib.RequestStatus>, 22: <enum I_CAL_3_9_BADVERSION_STATUS of type ICalGLib.RequestStatus>, 23: <enum I_CAL_3_10_TOOBIG_STATUS of type ICalGLib.RequestStatus>, 24: <enum I_CAL_3_11_MISSREQCOMP_STATUS of type ICalGLib.RequestStatus>, 25: <enum I_CAL_3_12_UNKCOMP_STATUS of type ICalGLib.RequestStatus>, 26: <enum I_CAL_3_13_BADCOMP_STATUS of type ICalGLib.RequestStatus>, 27: <enum I_CAL_3_14_NOCAP_STATUS of type ICalGLib.RequestStatus>, 28: <enum I_CAL_3_15_INVCOMMAND of type ICalGLib.RequestStatus>, 29: <enum I_CAL_4_0_BUSY_STATUS of type ICalGLib.RequestStatus>, 30: <enum I_CAL_4_1_STORE_ACCESS_DENIED of type ICalGLib.RequestStatus>, 31: <enum I_CAL_4_2_STORE_FAILED of type ICalGLib.RequestStatus>, 32: <enum I_CAL_4_3_STORE_NOT_FOUND of type ICalGLib.RequestStatus>, 33: <enum I_CAL_5_0_MAYBE_STATUS of type ICalGLib.RequestStatus>, 34: <enum I_CAL_5_1_UNAVAIL_STATUS of type ICalGLib.RequestStatus>, 35: <enum I_CAL_5_2_NOSERVICE_STATUS of type ICalGLib.RequestStatus>, 36: <enum I_CAL_5_3_NOSCHED_STATUS of type ICalGLib.RequestStatus>, 37: <enum I_CAL_6_1_CONTAINER_NOT_FOUND of type ICalGLib.RequestStatus>, 38: <enum I_CAL_9_0_UNRECOGNIZED_COMMAND of type ICalGLib.RequestStatus>}, '__info__': gi.EnumInfo(RequestStatus), 'UNKNOWN_STATUS': <enum I_CAL_UNKNOWN_STATUS of type ICalGLib.RequestStatus>, '2_0_SUCCESS_STATUS': <enum I_CAL_2_0_SUCCESS_STATUS of type ICalGLib.RequestStatus>, '2_1_FALLBACK_STATUS': <enum I_CAL_2_1_FALLBACK_STATUS of type ICalGLib.RequestStatus>, '2_2_IGPROP_STATUS': <enum I_CAL_2_2_IGPROP_STATUS of type ICalGLib.RequestStatus>, '2_3_IGPARAM_STATUS': <enum I_CAL_2_3_IGPARAM_STATUS of type ICalGLib.RequestStatus>, '2_4_IGXPROP_STATUS': <enum I_CAL_2_4_IGXPROP_STATUS of type ICalGLib.RequestStatus>, '2_5_IGXPARAM_STATUS': <enum I_CAL_2_5_IGXPARAM_STATUS of type ICalGLib.RequestStatus>, '2_6_IGCOMP_STATUS': <enum I_CAL_2_6_IGCOMP_STATUS of type ICalGLib.RequestStatus>, '2_7_FORWARD_STATUS': <enum I_CAL_2_7_FORWARD_STATUS of type ICalGLib.RequestStatus>, '2_8_ONEEVENT_STATUS': <enum I_CAL_2_8_ONEEVENT_STATUS of type ICalGLib.RequestStatus>, '2_9_TRUNC_STATUS': <enum I_CAL_2_9_TRUNC_STATUS of type ICalGLib.RequestStatus>, '2_10_ONETODO_STATUS': <enum I_CAL_2_10_ONETODO_STATUS of type ICalGLib.RequestStatus>, '2_11_TRUNCRRULE_STATUS': <enum I_CAL_2_11_TRUNCRRULE_STATUS of type ICalGLib.RequestStatus>, '3_0_INVPROPNAME_STATUS': <enum I_CAL_3_0_INVPROPNAME_STATUS of type ICalGLib.RequestStatus>, '3_1_INVPROPVAL_STATUS': <enum I_CAL_3_1_INVPROPVAL_STATUS of type ICalGLib.RequestStatus>, '3_2_INVPARAM_STATUS': <enum I_CAL_3_2_INVPARAM_STATUS of type ICalGLib.RequestStatus>, '3_3_INVPARAMVAL_STATUS': <enum I_CAL_3_3_INVPARAMVAL_STATUS of type ICalGLib.RequestStatus>, '3_4_INVCOMP_STATUS': <enum I_CAL_3_4_INVCOMP_STATUS of type ICalGLib.RequestStatus>, '3_5_INVTIME_STATUS': <enum I_CAL_3_5_INVTIME_STATUS of type ICalGLib.RequestStatus>, '3_6_INVRULE_STATUS': <enum I_CAL_3_6_INVRULE_STATUS of type ICalGLib.RequestStatus>, '3_7_INVCU_STATUS': <enum I_CAL_3_7_INVCU_STATUS of type ICalGLib.RequestStatus>, '3_8_NOAUTH_STATUS': <enum I_CAL_3_8_NOAUTH_STATUS of type ICalGLib.RequestStatus>, '3_9_BADVERSION_STATUS': <enum I_CAL_3_9_BADVERSION_STATUS of type ICalGLib.RequestStatus>, '3_10_TOOBIG_STATUS': <enum I_CAL_3_10_TOOBIG_STATUS of type ICalGLib.RequestStatus>, '3_11_MISSREQCOMP_STATUS': <enum I_CAL_3_11_MISSREQCOMP_STATUS of type ICalGLib.RequestStatus>, '3_12_UNKCOMP_STATUS': <enum I_CAL_3_12_UNKCOMP_STATUS of type ICalGLib.RequestStatus>, '3_13_BADCOMP_STATUS': <enum I_CAL_3_13_BADCOMP_STATUS of type ICalGLib.RequestStatus>, '3_14_NOCAP_STATUS': <enum I_CAL_3_14_NOCAP_STATUS of type ICalGLib.RequestStatus>, '3_15_INVCOMMAND': <enum I_CAL_3_15_INVCOMMAND of type ICalGLib.RequestStatus>, '4_0_BUSY_STATUS': <enum I_CAL_4_0_BUSY_STATUS of type ICalGLib.RequestStatus>, '4_1_STORE_ACCESS_DENIED': <enum I_CAL_4_1_STORE_ACCESS_DENIED of type ICalGLib.RequestStatus>, '4_2_STORE_FAILED': <enum I_CAL_4_2_STORE_FAILED of type ICalGLib.RequestStatus>, '4_3_STORE_NOT_FOUND': <enum I_CAL_4_3_STORE_NOT_FOUND of type ICalGLib.RequestStatus>, '5_0_MAYBE_STATUS': <enum I_CAL_5_0_MAYBE_STATUS of type ICalGLib.RequestStatus>, '5_1_UNAVAIL_STATUS': <enum I_CAL_5_1_UNAVAIL_STATUS of type ICalGLib.RequestStatus>, '5_2_NOSERVICE_STATUS': <enum I_CAL_5_2_NOSERVICE_STATUS of type ICalGLib.RequestStatus>, '5_3_NOSCHED_STATUS': <enum I_CAL_5_3_NOSCHED_STATUS of type ICalGLib.RequestStatus>, '6_1_CONTAINER_NOT_FOUND': <enum I_CAL_6_1_CONTAINER_NOT_FOUND of type ICalGLib.RequestStatus>, '9_0_UNRECOGNIZED_COMMAND': <enum I_CAL_9_0_UNRECOGNIZED_COMMAND of type ICalGLib.RequestStatus>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PyICalGLibRequestStatus (94403188547104)>'
    __info__ = gi.EnumInfo(RequestStatus)


