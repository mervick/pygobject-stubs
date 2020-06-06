# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class PadProbeType(__gobject.GFlags):
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


    ALL_BOTH = 1776
    BLOCK = 2
    BLOCKING = 3
    BLOCK_DOWNSTREAM = 114
    BLOCK_UPSTREAM = 130
    BUFFER = 16
    BUFFER_LIST = 32
    DATA_BOTH = 240
    DATA_DOWNSTREAM = 112
    DATA_UPSTREAM = 128
    EVENT_BOTH = 192
    EVENT_DOWNSTREAM = 64
    EVENT_FLUSH = 256
    EVENT_UPSTREAM = 128
    IDLE = 1
    INVALID = 0
    PULL = 8192
    PUSH = 4096
    QUERY_BOTH = 1536
    QUERY_DOWNSTREAM = 512
    QUERY_UPSTREAM = 1024
    SCHEDULING = 12288
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gst', '__dict__': <attribute '__dict__' of 'PadProbeType' objects>, '__doc__': None, '__gtype__': <GType GstPadProbeType (94058977811696)>, '__flags_values__': {0: <flags 0 of type Gst.PadProbeType>, 1: <flags GST_PAD_PROBE_TYPE_IDLE of type Gst.PadProbeType>, 2: <flags GST_PAD_PROBE_TYPE_BLOCK of type Gst.PadProbeType>, 16: <flags GST_PAD_PROBE_TYPE_BUFFER of type Gst.PadProbeType>, 32: <flags GST_PAD_PROBE_TYPE_BUFFER_LIST of type Gst.PadProbeType>, 64: <flags GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM of type Gst.PadProbeType>, 128: <flags GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM of type Gst.PadProbeType>, 256: <flags GST_PAD_PROBE_TYPE_EVENT_FLUSH of type Gst.PadProbeType>, 512: <flags GST_PAD_PROBE_TYPE_QUERY_DOWNSTREAM of type Gst.PadProbeType>, 1024: <flags GST_PAD_PROBE_TYPE_QUERY_UPSTREAM of type Gst.PadProbeType>, 4096: <flags GST_PAD_PROBE_TYPE_PUSH of type Gst.PadProbeType>, 8192: <flags GST_PAD_PROBE_TYPE_PULL of type Gst.PadProbeType>, 3: <flags GST_PAD_PROBE_TYPE_IDLE | GST_PAD_PROBE_TYPE_BLOCK | GST_PAD_PROBE_TYPE_BLOCKING of type Gst.PadProbeType>, 112: <flags GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM of type Gst.PadProbeType>, 240: <flags GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_BOTH | GST_PAD_PROBE_TYPE_EVENT_BOTH of type Gst.PadProbeType>, 114: <flags GST_PAD_PROBE_TYPE_BLOCK | GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM | GST_PAD_PROBE_TYPE_BLOCK_DOWNSTREAM of type Gst.PadProbeType>, 130: <flags GST_PAD_PROBE_TYPE_BLOCK | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_BLOCK_UPSTREAM of type Gst.PadProbeType>, 192: <flags GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_EVENT_BOTH of type Gst.PadProbeType>, 1536: <flags GST_PAD_PROBE_TYPE_QUERY_DOWNSTREAM | GST_PAD_PROBE_TYPE_QUERY_UPSTREAM | GST_PAD_PROBE_TYPE_QUERY_BOTH of type Gst.PadProbeType>, 1776: <flags GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_QUERY_DOWNSTREAM | GST_PAD_PROBE_TYPE_QUERY_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_BOTH | GST_PAD_PROBE_TYPE_EVENT_BOTH | GST_PAD_PROBE_TYPE_QUERY_BOTH | GST_PAD_PROBE_TYPE_ALL_BOTH of type Gst.PadProbeType>, 12288: <flags GST_PAD_PROBE_TYPE_PUSH | GST_PAD_PROBE_TYPE_PULL | GST_PAD_PROBE_TYPE_SCHEDULING of type Gst.PadProbeType>}, '__info__': gi.EnumInfo(PadProbeType), 'INVALID': <flags 0 of type Gst.PadProbeType>, 'IDLE': <flags GST_PAD_PROBE_TYPE_IDLE of type Gst.PadProbeType>, 'BLOCK': <flags GST_PAD_PROBE_TYPE_BLOCK of type Gst.PadProbeType>, 'BUFFER': <flags GST_PAD_PROBE_TYPE_BUFFER of type Gst.PadProbeType>, 'BUFFER_LIST': <flags GST_PAD_PROBE_TYPE_BUFFER_LIST of type Gst.PadProbeType>, 'EVENT_DOWNSTREAM': <flags GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM of type Gst.PadProbeType>, 'EVENT_UPSTREAM': <flags GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM of type Gst.PadProbeType>, 'EVENT_FLUSH': <flags GST_PAD_PROBE_TYPE_EVENT_FLUSH of type Gst.PadProbeType>, 'QUERY_DOWNSTREAM': <flags GST_PAD_PROBE_TYPE_QUERY_DOWNSTREAM of type Gst.PadProbeType>, 'QUERY_UPSTREAM': <flags GST_PAD_PROBE_TYPE_QUERY_UPSTREAM of type Gst.PadProbeType>, 'PUSH': <flags GST_PAD_PROBE_TYPE_PUSH of type Gst.PadProbeType>, 'PULL': <flags GST_PAD_PROBE_TYPE_PULL of type Gst.PadProbeType>, 'BLOCKING': <flags GST_PAD_PROBE_TYPE_IDLE | GST_PAD_PROBE_TYPE_BLOCK | GST_PAD_PROBE_TYPE_BLOCKING of type Gst.PadProbeType>, 'DATA_DOWNSTREAM': <flags GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM of type Gst.PadProbeType>, 'DATA_UPSTREAM': <flags GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM of type Gst.PadProbeType>, 'DATA_BOTH': <flags GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_BOTH | GST_PAD_PROBE_TYPE_EVENT_BOTH of type Gst.PadProbeType>, 'BLOCK_DOWNSTREAM': <flags GST_PAD_PROBE_TYPE_BLOCK | GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM | GST_PAD_PROBE_TYPE_BLOCK_DOWNSTREAM of type Gst.PadProbeType>, 'BLOCK_UPSTREAM': <flags GST_PAD_PROBE_TYPE_BLOCK | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_BLOCK_UPSTREAM of type Gst.PadProbeType>, 'EVENT_BOTH': <flags GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_EVENT_BOTH of type Gst.PadProbeType>, 'QUERY_BOTH': <flags GST_PAD_PROBE_TYPE_QUERY_DOWNSTREAM | GST_PAD_PROBE_TYPE_QUERY_UPSTREAM | GST_PAD_PROBE_TYPE_QUERY_BOTH of type Gst.PadProbeType>, 'ALL_BOTH': <flags GST_PAD_PROBE_TYPE_BUFFER | GST_PAD_PROBE_TYPE_BUFFER_LIST | GST_PAD_PROBE_TYPE_EVENT_DOWNSTREAM | GST_PAD_PROBE_TYPE_EVENT_UPSTREAM | GST_PAD_PROBE_TYPE_QUERY_DOWNSTREAM | GST_PAD_PROBE_TYPE_QUERY_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_DOWNSTREAM | GST_PAD_PROBE_TYPE_DATA_UPSTREAM | GST_PAD_PROBE_TYPE_DATA_BOTH | GST_PAD_PROBE_TYPE_EVENT_BOTH | GST_PAD_PROBE_TYPE_QUERY_BOTH | GST_PAD_PROBE_TYPE_ALL_BOTH of type Gst.PadProbeType>, 'SCHEDULING': <flags GST_PAD_PROBE_TYPE_PUSH | GST_PAD_PROBE_TYPE_PULL | GST_PAD_PROBE_TYPE_SCHEDULING of type Gst.PadProbeType>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        16: 16,
        32: 32,
        64: 64,
        112: 112,
        114: 114,
        128: 128,
        130: 130,
        192: 192,
        240: 240,
        256: 256,
        512: 512,
        1024: 1024,
        1536: 1536,
        1776: 1776,
        4096: 4096,
        8192: 8192,
        12288: 12288,
    }
    __gtype__ = None # (!) real value is '<GType GstPadProbeType (94058977811696)>'
    __info__ = gi.EnumInfo(PadProbeType)


