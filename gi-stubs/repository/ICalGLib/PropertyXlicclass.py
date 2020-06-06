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


class PropertyXlicclass(__gobject.GEnum):
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


    ADDINSTANCE = 11117
    CANCELALL = 11120
    CANCELEVENT = 11118
    CANCELINSTANCE = 11119
    COUNTER = 11122
    DECLINECOUNTER = 11123
    MALFORMED = 11124
    MISSEQUENCED = 11126
    NONE = 11199
    OBSOLETE = 11125
    PUBLISHFREEBUSY = 11103
    PUBLISHNEW = 11101
    PUBLISHUPDATE = 11102
    REFRESH = 11121
    REPLYACCEPT = 11112
    REPLYCRASHERACCEPT = 11115
    REPLYCRASHERDECLINE = 11116
    REPLYDECLINE = 11113
    REPLYDELEGATE = 11114
    REQUESTDELEGATE = 11107
    REQUESTFORWARD = 11109
    REQUESTFREEBUSY = 11111
    REQUESTNEW = 11104
    REQUESTNEWORGANIZER = 11108
    REQUESTRESCHEDULE = 11106
    REQUESTSTATUS = 11110
    REQUESTUPDATE = 11105
    UNKNOWN = 11127
    X = 11100
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICalGLib', '__dict__': <attribute '__dict__' of 'PropertyXlicclass' objects>, '__doc__': None, '__gtype__': <GType PyICalGLibPropertyXlicclass (94403188514160)>, '__enum_values__': {11100: <enum I_CAL_XLICCLASS_X of type ICalGLib.PropertyXlicclass>, 11101: <enum I_CAL_XLICCLASS_PUBLISHNEW of type ICalGLib.PropertyXlicclass>, 11102: <enum I_CAL_XLICCLASS_PUBLISHUPDATE of type ICalGLib.PropertyXlicclass>, 11103: <enum I_CAL_XLICCLASS_PUBLISHFREEBUSY of type ICalGLib.PropertyXlicclass>, 11104: <enum I_CAL_XLICCLASS_REQUESTNEW of type ICalGLib.PropertyXlicclass>, 11105: <enum I_CAL_XLICCLASS_REQUESTUPDATE of type ICalGLib.PropertyXlicclass>, 11106: <enum I_CAL_XLICCLASS_REQUESTRESCHEDULE of type ICalGLib.PropertyXlicclass>, 11107: <enum I_CAL_XLICCLASS_REQUESTDELEGATE of type ICalGLib.PropertyXlicclass>, 11108: <enum I_CAL_XLICCLASS_REQUESTNEWORGANIZER of type ICalGLib.PropertyXlicclass>, 11109: <enum I_CAL_XLICCLASS_REQUESTFORWARD of type ICalGLib.PropertyXlicclass>, 11110: <enum I_CAL_XLICCLASS_REQUESTSTATUS of type ICalGLib.PropertyXlicclass>, 11111: <enum I_CAL_XLICCLASS_REQUESTFREEBUSY of type ICalGLib.PropertyXlicclass>, 11112: <enum I_CAL_XLICCLASS_REPLYACCEPT of type ICalGLib.PropertyXlicclass>, 11113: <enum I_CAL_XLICCLASS_REPLYDECLINE of type ICalGLib.PropertyXlicclass>, 11114: <enum I_CAL_XLICCLASS_REPLYDELEGATE of type ICalGLib.PropertyXlicclass>, 11115: <enum I_CAL_XLICCLASS_REPLYCRASHERACCEPT of type ICalGLib.PropertyXlicclass>, 11116: <enum I_CAL_XLICCLASS_REPLYCRASHERDECLINE of type ICalGLib.PropertyXlicclass>, 11117: <enum I_CAL_XLICCLASS_ADDINSTANCE of type ICalGLib.PropertyXlicclass>, 11118: <enum I_CAL_XLICCLASS_CANCELEVENT of type ICalGLib.PropertyXlicclass>, 11119: <enum I_CAL_XLICCLASS_CANCELINSTANCE of type ICalGLib.PropertyXlicclass>, 11120: <enum I_CAL_XLICCLASS_CANCELALL of type ICalGLib.PropertyXlicclass>, 11121: <enum I_CAL_XLICCLASS_REFRESH of type ICalGLib.PropertyXlicclass>, 11122: <enum I_CAL_XLICCLASS_COUNTER of type ICalGLib.PropertyXlicclass>, 11123: <enum I_CAL_XLICCLASS_DECLINECOUNTER of type ICalGLib.PropertyXlicclass>, 11124: <enum I_CAL_XLICCLASS_MALFORMED of type ICalGLib.PropertyXlicclass>, 11125: <enum I_CAL_XLICCLASS_OBSOLETE of type ICalGLib.PropertyXlicclass>, 11126: <enum I_CAL_XLICCLASS_MISSEQUENCED of type ICalGLib.PropertyXlicclass>, 11127: <enum I_CAL_XLICCLASS_UNKNOWN of type ICalGLib.PropertyXlicclass>, 11199: <enum I_CAL_XLICCLASS_NONE of type ICalGLib.PropertyXlicclass>}, '__info__': gi.EnumInfo(PropertyXlicclass), 'X': <enum I_CAL_XLICCLASS_X of type ICalGLib.PropertyXlicclass>, 'PUBLISHNEW': <enum I_CAL_XLICCLASS_PUBLISHNEW of type ICalGLib.PropertyXlicclass>, 'PUBLISHUPDATE': <enum I_CAL_XLICCLASS_PUBLISHUPDATE of type ICalGLib.PropertyXlicclass>, 'PUBLISHFREEBUSY': <enum I_CAL_XLICCLASS_PUBLISHFREEBUSY of type ICalGLib.PropertyXlicclass>, 'REQUESTNEW': <enum I_CAL_XLICCLASS_REQUESTNEW of type ICalGLib.PropertyXlicclass>, 'REQUESTUPDATE': <enum I_CAL_XLICCLASS_REQUESTUPDATE of type ICalGLib.PropertyXlicclass>, 'REQUESTRESCHEDULE': <enum I_CAL_XLICCLASS_REQUESTRESCHEDULE of type ICalGLib.PropertyXlicclass>, 'REQUESTDELEGATE': <enum I_CAL_XLICCLASS_REQUESTDELEGATE of type ICalGLib.PropertyXlicclass>, 'REQUESTNEWORGANIZER': <enum I_CAL_XLICCLASS_REQUESTNEWORGANIZER of type ICalGLib.PropertyXlicclass>, 'REQUESTFORWARD': <enum I_CAL_XLICCLASS_REQUESTFORWARD of type ICalGLib.PropertyXlicclass>, 'REQUESTSTATUS': <enum I_CAL_XLICCLASS_REQUESTSTATUS of type ICalGLib.PropertyXlicclass>, 'REQUESTFREEBUSY': <enum I_CAL_XLICCLASS_REQUESTFREEBUSY of type ICalGLib.PropertyXlicclass>, 'REPLYACCEPT': <enum I_CAL_XLICCLASS_REPLYACCEPT of type ICalGLib.PropertyXlicclass>, 'REPLYDECLINE': <enum I_CAL_XLICCLASS_REPLYDECLINE of type ICalGLib.PropertyXlicclass>, 'REPLYDELEGATE': <enum I_CAL_XLICCLASS_REPLYDELEGATE of type ICalGLib.PropertyXlicclass>, 'REPLYCRASHERACCEPT': <enum I_CAL_XLICCLASS_REPLYCRASHERACCEPT of type ICalGLib.PropertyXlicclass>, 'REPLYCRASHERDECLINE': <enum I_CAL_XLICCLASS_REPLYCRASHERDECLINE of type ICalGLib.PropertyXlicclass>, 'ADDINSTANCE': <enum I_CAL_XLICCLASS_ADDINSTANCE of type ICalGLib.PropertyXlicclass>, 'CANCELEVENT': <enum I_CAL_XLICCLASS_CANCELEVENT of type ICalGLib.PropertyXlicclass>, 'CANCELINSTANCE': <enum I_CAL_XLICCLASS_CANCELINSTANCE of type ICalGLib.PropertyXlicclass>, 'CANCELALL': <enum I_CAL_XLICCLASS_CANCELALL of type ICalGLib.PropertyXlicclass>, 'REFRESH': <enum I_CAL_XLICCLASS_REFRESH of type ICalGLib.PropertyXlicclass>, 'COUNTER': <enum I_CAL_XLICCLASS_COUNTER of type ICalGLib.PropertyXlicclass>, 'DECLINECOUNTER': <enum I_CAL_XLICCLASS_DECLINECOUNTER of type ICalGLib.PropertyXlicclass>, 'MALFORMED': <enum I_CAL_XLICCLASS_MALFORMED of type ICalGLib.PropertyXlicclass>, 'OBSOLETE': <enum I_CAL_XLICCLASS_OBSOLETE of type ICalGLib.PropertyXlicclass>, 'MISSEQUENCED': <enum I_CAL_XLICCLASS_MISSEQUENCED of type ICalGLib.PropertyXlicclass>, 'UNKNOWN': <enum I_CAL_XLICCLASS_UNKNOWN of type ICalGLib.PropertyXlicclass>, 'NONE': <enum I_CAL_XLICCLASS_NONE of type ICalGLib.PropertyXlicclass>})"
    __enum_values__ = {
        11100: 11100,
        11101: 11101,
        11102: 11102,
        11103: 11103,
        11104: 11104,
        11105: 11105,
        11106: 11106,
        11107: 11107,
        11108: 11108,
        11109: 11109,
        11110: 11110,
        11111: 11111,
        11112: 11112,
        11113: 11113,
        11114: 11114,
        11115: 11115,
        11116: 11116,
        11117: 11117,
        11118: 11118,
        11119: 11119,
        11120: 11120,
        11121: 11121,
        11122: 11122,
        11123: 11123,
        11124: 11124,
        11125: 11125,
        11126: 11126,
        11127: 11127,
        11199: 11199,
    }
    __gtype__ = None # (!) real value is '<GType PyICalGLibPropertyXlicclass (94403188514160)>'
    __info__ = gi.EnumInfo(PropertyXlicclass)


