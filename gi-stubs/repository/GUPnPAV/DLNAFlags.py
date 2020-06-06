# encoding: utf-8
# module gi.repository.GUPnPAV
# from /usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib
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


class DLNAFlags(__gobject.GFlags):
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
        """ Helper for pickle. """
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

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BACKGROUND_TRANSFER_MODE = 4194304
    BYTE_BASED_SEEK = 536870912
    CLEARTEXT_BYTESEEK_FULL = 32768
    CONNECTION_STALL = 2097152
    DLNA_V15 = 1048576
    INTERACTIVE_TRANSFER_MODE = 8388608
    LINK_PROTECTED_CONTENT = 65536
    LOP_CLEARTEXT_BYTESEEK = 16384
    NONE = 0
    PLAY_CONTAINER = 268435456
    RTSP_PAUSE = 33554432
    S0_INCREASE = 134217728
    SENDER_PACED = 2147483648
    SN_INCREASE = 67108864
    STREAMING_TRANSFER_MODE = 16777216
    TIME_BASED_SEEK = 1073741824
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GUPnPAV', '__dict__': <attribute '__dict__' of 'DLNAFlags' objects>, '__doc__': None, '__gtype__': <GType GUPnPDLNAFlags (94653147608928)>, '__flags_values__': {0: <flags 0 of type GUPnPAV.DLNAFlags>, 2147483648: <flags GUPNP_DLNA_FLAGS_SENDER_PACED of type GUPnPAV.DLNAFlags>, 1073741824: <flags GUPNP_DLNA_FLAGS_TIME_BASED_SEEK of type GUPnPAV.DLNAFlags>, 536870912: <flags GUPNP_DLNA_FLAGS_BYTE_BASED_SEEK of type GUPnPAV.DLNAFlags>, 268435456: <flags GUPNP_DLNA_FLAGS_PLAY_CONTAINER of type GUPnPAV.DLNAFlags>, 134217728: <flags GUPNP_DLNA_FLAGS_S0_INCREASE of type GUPnPAV.DLNAFlags>, 67108864: <flags GUPNP_DLNA_FLAGS_SN_INCREASE of type GUPnPAV.DLNAFlags>, 33554432: <flags GUPNP_DLNA_FLAGS_RTSP_PAUSE of type GUPnPAV.DLNAFlags>, 16777216: <flags GUPNP_DLNA_FLAGS_STREAMING_TRANSFER_MODE of type GUPnPAV.DLNAFlags>, 8388608: <flags GUPNP_DLNA_FLAGS_INTERACTIVE_TRANSFER_MODE of type GUPnPAV.DLNAFlags>, 4194304: <flags GUPNP_DLNA_FLAGS_BACKGROUND_TRANSFER_MODE of type GUPnPAV.DLNAFlags>, 2097152: <flags GUPNP_DLNA_FLAGS_CONNECTION_STALL of type GUPnPAV.DLNAFlags>, 1048576: <flags GUPNP_DLNA_FLAGS_DLNA_V15 of type GUPnPAV.DLNAFlags>, 65536: <flags GUPNP_DLNA_FLAGS_LINK_PROTECTED_CONTENT of type GUPnPAV.DLNAFlags>, 32768: <flags GUPNP_DLNA_FLAGS_CLEAR_TEXT_BYTE_SEEK_FULL of type GUPnPAV.DLNAFlags>, 16384: <flags GUPNP_DLNA_FLAGS_LOP_CLEAR_TEXT_BYTE_SEEK of type GUPnPAV.DLNAFlags>}, '__info__': gi.EnumInfo(DLNAFlags), 'NONE': <flags 0 of type GUPnPAV.DLNAFlags>, 'SENDER_PACED': <flags GUPNP_DLNA_FLAGS_SENDER_PACED of type GUPnPAV.DLNAFlags>, 'TIME_BASED_SEEK': <flags GUPNP_DLNA_FLAGS_TIME_BASED_SEEK of type GUPnPAV.DLNAFlags>, 'BYTE_BASED_SEEK': <flags GUPNP_DLNA_FLAGS_BYTE_BASED_SEEK of type GUPnPAV.DLNAFlags>, 'PLAY_CONTAINER': <flags GUPNP_DLNA_FLAGS_PLAY_CONTAINER of type GUPnPAV.DLNAFlags>, 'S0_INCREASE': <flags GUPNP_DLNA_FLAGS_S0_INCREASE of type GUPnPAV.DLNAFlags>, 'SN_INCREASE': <flags GUPNP_DLNA_FLAGS_SN_INCREASE of type GUPnPAV.DLNAFlags>, 'RTSP_PAUSE': <flags GUPNP_DLNA_FLAGS_RTSP_PAUSE of type GUPnPAV.DLNAFlags>, 'STREAMING_TRANSFER_MODE': <flags GUPNP_DLNA_FLAGS_STREAMING_TRANSFER_MODE of type GUPnPAV.DLNAFlags>, 'INTERACTIVE_TRANSFER_MODE': <flags GUPNP_DLNA_FLAGS_INTERACTIVE_TRANSFER_MODE of type GUPnPAV.DLNAFlags>, 'BACKGROUND_TRANSFER_MODE': <flags GUPNP_DLNA_FLAGS_BACKGROUND_TRANSFER_MODE of type GUPnPAV.DLNAFlags>, 'CONNECTION_STALL': <flags GUPNP_DLNA_FLAGS_CONNECTION_STALL of type GUPnPAV.DLNAFlags>, 'DLNA_V15': <flags GUPNP_DLNA_FLAGS_DLNA_V15 of type GUPnPAV.DLNAFlags>, 'LINK_PROTECTED_CONTENT': <flags GUPNP_DLNA_FLAGS_LINK_PROTECTED_CONTENT of type GUPnPAV.DLNAFlags>, 'CLEARTEXT_BYTESEEK_FULL': <flags GUPNP_DLNA_FLAGS_CLEAR_TEXT_BYTE_SEEK_FULL of type GUPnPAV.DLNAFlags>, 'LOP_CLEARTEXT_BYTESEEK': <flags GUPNP_DLNA_FLAGS_LOP_CLEAR_TEXT_BYTE_SEEK of type GUPnPAV.DLNAFlags>})"
    __flags_values__ = {
        0: 0,
        16384: 16384,
        32768: 32768,
        65536: 65536,
        1048576: 1048576,
        2097152: 2097152,
        4194304: 4194304,
        8388608: 8388608,
        16777216: 16777216,
        33554432: 33554432,
        67108864: 67108864,
        134217728: 134217728,
        268435456: 268435456,
        536870912: 536870912,
        1073741824: 1073741824,
        2147483648: 2147483648,
    }
    __gtype__ = None # (!) real value is '<GType GUPnPDLNAFlags (94653147608928)>'
    __info__ = gi.EnumInfo(DLNAFlags)


