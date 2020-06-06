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


class property_method(__gobject.GEnum):
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


    ADD = 10504
    CANCEL = 10505
    COUNTER = 10507
    CREATE = 10509
    DECLINECOUNTER = 10508
    DELETE = 10515
    GENERATEUID = 10514
    MODIFY = 10513
    MOVE = 10512
    NONE = 10599
    POLLSTATUS = 10516
    PUBLISH = 10501
    READ = 10510
    REFRESH = 10506
    REPLY = 10503
    REQUEST = 10502
    RESPONSE = 10511
    X = 10500
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICal', '__dict__': <attribute '__dict__' of 'property_method' objects>, '__doc__': None, '__gtype__': <GType PyICalproperty_method (94628528798272)>, '__enum_values__': {10500: <enum ICAL_METHOD_X of type ICal.property_method>, 10501: <enum ICAL_METHOD_PUBLISH of type ICal.property_method>, 10502: <enum ICAL_METHOD_REQUEST of type ICal.property_method>, 10503: <enum ICAL_METHOD_REPLY of type ICal.property_method>, 10504: <enum ICAL_METHOD_ADD of type ICal.property_method>, 10505: <enum ICAL_METHOD_CANCEL of type ICal.property_method>, 10506: <enum ICAL_METHOD_REFRESH of type ICal.property_method>, 10507: <enum ICAL_METHOD_COUNTER of type ICal.property_method>, 10508: <enum ICAL_METHOD_DECLINECOUNTER of type ICal.property_method>, 10509: <enum ICAL_METHOD_CREATE of type ICal.property_method>, 10510: <enum ICAL_METHOD_READ of type ICal.property_method>, 10511: <enum ICAL_METHOD_RESPONSE of type ICal.property_method>, 10512: <enum ICAL_METHOD_MOVE of type ICal.property_method>, 10513: <enum ICAL_METHOD_MODIFY of type ICal.property_method>, 10514: <enum ICAL_METHOD_GENERATEUID of type ICal.property_method>, 10515: <enum ICAL_METHOD_DELETE of type ICal.property_method>, 10516: <enum ICAL_METHOD_POLLSTATUS of type ICal.property_method>, 10599: <enum ICAL_METHOD_NONE of type ICal.property_method>}, '__info__': gi.EnumInfo(property_method), 'X': <enum ICAL_METHOD_X of type ICal.property_method>, 'PUBLISH': <enum ICAL_METHOD_PUBLISH of type ICal.property_method>, 'REQUEST': <enum ICAL_METHOD_REQUEST of type ICal.property_method>, 'REPLY': <enum ICAL_METHOD_REPLY of type ICal.property_method>, 'ADD': <enum ICAL_METHOD_ADD of type ICal.property_method>, 'CANCEL': <enum ICAL_METHOD_CANCEL of type ICal.property_method>, 'REFRESH': <enum ICAL_METHOD_REFRESH of type ICal.property_method>, 'COUNTER': <enum ICAL_METHOD_COUNTER of type ICal.property_method>, 'DECLINECOUNTER': <enum ICAL_METHOD_DECLINECOUNTER of type ICal.property_method>, 'CREATE': <enum ICAL_METHOD_CREATE of type ICal.property_method>, 'READ': <enum ICAL_METHOD_READ of type ICal.property_method>, 'RESPONSE': <enum ICAL_METHOD_RESPONSE of type ICal.property_method>, 'MOVE': <enum ICAL_METHOD_MOVE of type ICal.property_method>, 'MODIFY': <enum ICAL_METHOD_MODIFY of type ICal.property_method>, 'GENERATEUID': <enum ICAL_METHOD_GENERATEUID of type ICal.property_method>, 'DELETE': <enum ICAL_METHOD_DELETE of type ICal.property_method>, 'POLLSTATUS': <enum ICAL_METHOD_POLLSTATUS of type ICal.property_method>, 'NONE': <enum ICAL_METHOD_NONE of type ICal.property_method>})"
    __enum_values__ = {
        10500: 10500,
        10501: 10501,
        10502: 10502,
        10503: 10503,
        10504: 10504,
        10505: 10505,
        10506: 10506,
        10507: 10507,
        10508: 10508,
        10509: 10509,
        10510: 10510,
        10511: 10511,
        10512: 10512,
        10513: 10513,
        10514: 10514,
        10515: 10515,
        10516: 10516,
        10599: 10599,
    }
    __gtype__ = None # (!) real value is '<GType PyICalproperty_method (94628528798272)>'
    __info__ = gi.EnumInfo(property_method)


