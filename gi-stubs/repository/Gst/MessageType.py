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


class MessageType(__gobject.GFlags):
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

    def get_name(self, type): # real signature unknown; restored from __doc__
        """ get_name(type:Gst.MessageType) -> str """
        return ""

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

    def to_quark(self, type): # real signature unknown; restored from __doc__
        """ to_quark(type:Gst.MessageType) -> int """
        return 0

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


    ANY = 4294967295
    APPLICATION = 16384
    ASYNC_DONE = 2097152
    ASYNC_START = 1048576
    BUFFERING = 32
    CLOCK_LOST = 1024
    CLOCK_PROVIDE = 512
    DEVICE_ADDED = 2147483649
    DEVICE_CHANGED = 2147483655
    DEVICE_REMOVED = 2147483650
    DURATION_CHANGED = 262144
    ELEMENT = 32768
    EOS = 1
    ERROR = 2
    EXTENDED = 2147483648
    HAVE_CONTEXT = 1073741824
    INFO = 8
    LATENCY = 524288
    NEED_CONTEXT = 536870912
    NEW_CLOCK = 2048
    PROGRESS = 33554432
    PROPERTY_NOTIFY = 2147483651
    QOS = 16777216
    REDIRECT = 2147483654
    REQUEST_STATE = 4194304
    RESET_TIME = 134217728
    SEGMENT_DONE = 131072
    SEGMENT_START = 65536
    STATE_CHANGED = 64
    STATE_DIRTY = 128
    STEP_DONE = 256
    STEP_START = 8388608
    STREAMS_SELECTED = 2147483653
    STREAM_COLLECTION = 2147483652
    STREAM_START = 268435456
    STREAM_STATUS = 8192
    STRUCTURE_CHANGE = 4096
    TAG = 16
    TOC = 67108864
    UNKNOWN = 0
    WARNING = 4
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gst', '__dict__': <attribute '__dict__' of 'MessageType' objects>, '__doc__': None, '__gtype__': <GType GstMessageType (94058977575040)>, '__flags_values__': {0: <flags 0 of type Gst.MessageType>, 1: <flags GST_MESSAGE_EOS of type Gst.MessageType>, 2: <flags GST_MESSAGE_ERROR of type Gst.MessageType>, 4: <flags GST_MESSAGE_WARNING of type Gst.MessageType>, 8: <flags GST_MESSAGE_INFO of type Gst.MessageType>, 16: <flags GST_MESSAGE_TAG of type Gst.MessageType>, 32: <flags GST_MESSAGE_BUFFERING of type Gst.MessageType>, 64: <flags GST_MESSAGE_STATE_CHANGED of type Gst.MessageType>, 128: <flags GST_MESSAGE_STATE_DIRTY of type Gst.MessageType>, 256: <flags GST_MESSAGE_STEP_DONE of type Gst.MessageType>, 512: <flags GST_MESSAGE_CLOCK_PROVIDE of type Gst.MessageType>, 1024: <flags GST_MESSAGE_CLOCK_LOST of type Gst.MessageType>, 2048: <flags GST_MESSAGE_NEW_CLOCK of type Gst.MessageType>, 4096: <flags GST_MESSAGE_STRUCTURE_CHANGE of type Gst.MessageType>, 8192: <flags GST_MESSAGE_STREAM_STATUS of type Gst.MessageType>, 16384: <flags GST_MESSAGE_APPLICATION of type Gst.MessageType>, 32768: <flags GST_MESSAGE_ELEMENT of type Gst.MessageType>, 65536: <flags GST_MESSAGE_SEGMENT_START of type Gst.MessageType>, 131072: <flags GST_MESSAGE_SEGMENT_DONE of type Gst.MessageType>, 262144: <flags GST_MESSAGE_DURATION_CHANGED of type Gst.MessageType>, 524288: <flags GST_MESSAGE_LATENCY of type Gst.MessageType>, 1048576: <flags GST_MESSAGE_ASYNC_START of type Gst.MessageType>, 2097152: <flags GST_MESSAGE_ASYNC_DONE of type Gst.MessageType>, 4194304: <flags GST_MESSAGE_REQUEST_STATE of type Gst.MessageType>, 8388608: <flags GST_MESSAGE_STEP_START of type Gst.MessageType>, 16777216: <flags GST_MESSAGE_QOS of type Gst.MessageType>, 33554432: <flags GST_MESSAGE_PROGRESS of type Gst.MessageType>, 67108864: <flags GST_MESSAGE_TOC of type Gst.MessageType>, 134217728: <flags GST_MESSAGE_RESET_TIME of type Gst.MessageType>, 268435456: <flags GST_MESSAGE_STREAM_START of type Gst.MessageType>, 536870912: <flags GST_MESSAGE_NEED_CONTEXT of type Gst.MessageType>, 1073741824: <flags GST_MESSAGE_HAVE_CONTEXT of type Gst.MessageType>, 2147483648: <flags GST_MESSAGE_EXTENDED of type Gst.MessageType>, 2147483649: <flags GST_MESSAGE_EOS | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED of type Gst.MessageType>, 2147483650: <flags GST_MESSAGE_ERROR | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_REMOVED of type Gst.MessageType>, 2147483651: <flags GST_MESSAGE_EOS | GST_MESSAGE_ERROR | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_PROPERTY_NOTIFY of type Gst.MessageType>, 2147483652: <flags GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_STREAM_COLLECTION of type Gst.MessageType>, 2147483653: <flags GST_MESSAGE_EOS | GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_STREAMS_SELECTED of type Gst.MessageType>, 2147483654: <flags GST_MESSAGE_ERROR | GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_REDIRECT of type Gst.MessageType>, 2147483655: <flags GST_MESSAGE_EOS | GST_MESSAGE_ERROR | GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_PROPERTY_NOTIFY | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_STREAMS_SELECTED | GST_MESSAGE_REDIRECT | GST_MESSAGE_DEVICE_CHANGED of type Gst.MessageType>, 4294967295: <flags GST_MESSAGE_EOS | GST_MESSAGE_ERROR | GST_MESSAGE_WARNING | GST_MESSAGE_INFO | GST_MESSAGE_TAG | GST_MESSAGE_BUFFERING | GST_MESSAGE_STATE_CHANGED | GST_MESSAGE_STATE_DIRTY | GST_MESSAGE_STEP_DONE | GST_MESSAGE_CLOCK_PROVIDE | GST_MESSAGE_CLOCK_LOST | GST_MESSAGE_NEW_CLOCK | GST_MESSAGE_STRUCTURE_CHANGE | GST_MESSAGE_STREAM_STATUS | GST_MESSAGE_APPLICATION | GST_MESSAGE_ELEMENT | GST_MESSAGE_SEGMENT_START | GST_MESSAGE_SEGMENT_DONE | GST_MESSAGE_DURATION_CHANGED | GST_MESSAGE_LATENCY | GST_MESSAGE_ASYNC_START | GST_MESSAGE_ASYNC_DONE | GST_MESSAGE_REQUEST_STATE | GST_MESSAGE_STEP_START | GST_MESSAGE_QOS | GST_MESSAGE_PROGRESS | GST_MESSAGE_TOC | GST_MESSAGE_RESET_TIME | GST_MESSAGE_STREAM_START | GST_MESSAGE_NEED_CONTEXT | GST_MESSAGE_HAVE_CONTEXT | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_PROPERTY_NOTIFY | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_STREAMS_SELECTED | GST_MESSAGE_REDIRECT | GST_MESSAGE_DEVICE_CHANGED | GST_MESSAGE_ANY of type Gst.MessageType>}, '__info__': gi.EnumInfo(MessageType), 'UNKNOWN': <flags 0 of type Gst.MessageType>, 'EOS': <flags GST_MESSAGE_EOS of type Gst.MessageType>, 'ERROR': <flags GST_MESSAGE_ERROR of type Gst.MessageType>, 'WARNING': <flags GST_MESSAGE_WARNING of type Gst.MessageType>, 'INFO': <flags GST_MESSAGE_INFO of type Gst.MessageType>, 'TAG': <flags GST_MESSAGE_TAG of type Gst.MessageType>, 'BUFFERING': <flags GST_MESSAGE_BUFFERING of type Gst.MessageType>, 'STATE_CHANGED': <flags GST_MESSAGE_STATE_CHANGED of type Gst.MessageType>, 'STATE_DIRTY': <flags GST_MESSAGE_STATE_DIRTY of type Gst.MessageType>, 'STEP_DONE': <flags GST_MESSAGE_STEP_DONE of type Gst.MessageType>, 'CLOCK_PROVIDE': <flags GST_MESSAGE_CLOCK_PROVIDE of type Gst.MessageType>, 'CLOCK_LOST': <flags GST_MESSAGE_CLOCK_LOST of type Gst.MessageType>, 'NEW_CLOCK': <flags GST_MESSAGE_NEW_CLOCK of type Gst.MessageType>, 'STRUCTURE_CHANGE': <flags GST_MESSAGE_STRUCTURE_CHANGE of type Gst.MessageType>, 'STREAM_STATUS': <flags GST_MESSAGE_STREAM_STATUS of type Gst.MessageType>, 'APPLICATION': <flags GST_MESSAGE_APPLICATION of type Gst.MessageType>, 'ELEMENT': <flags GST_MESSAGE_ELEMENT of type Gst.MessageType>, 'SEGMENT_START': <flags GST_MESSAGE_SEGMENT_START of type Gst.MessageType>, 'SEGMENT_DONE': <flags GST_MESSAGE_SEGMENT_DONE of type Gst.MessageType>, 'DURATION_CHANGED': <flags GST_MESSAGE_DURATION_CHANGED of type Gst.MessageType>, 'LATENCY': <flags GST_MESSAGE_LATENCY of type Gst.MessageType>, 'ASYNC_START': <flags GST_MESSAGE_ASYNC_START of type Gst.MessageType>, 'ASYNC_DONE': <flags GST_MESSAGE_ASYNC_DONE of type Gst.MessageType>, 'REQUEST_STATE': <flags GST_MESSAGE_REQUEST_STATE of type Gst.MessageType>, 'STEP_START': <flags GST_MESSAGE_STEP_START of type Gst.MessageType>, 'QOS': <flags GST_MESSAGE_QOS of type Gst.MessageType>, 'PROGRESS': <flags GST_MESSAGE_PROGRESS of type Gst.MessageType>, 'TOC': <flags GST_MESSAGE_TOC of type Gst.MessageType>, 'RESET_TIME': <flags GST_MESSAGE_RESET_TIME of type Gst.MessageType>, 'STREAM_START': <flags GST_MESSAGE_STREAM_START of type Gst.MessageType>, 'NEED_CONTEXT': <flags GST_MESSAGE_NEED_CONTEXT of type Gst.MessageType>, 'HAVE_CONTEXT': <flags GST_MESSAGE_HAVE_CONTEXT of type Gst.MessageType>, 'EXTENDED': <flags GST_MESSAGE_EXTENDED of type Gst.MessageType>, 'DEVICE_ADDED': <flags GST_MESSAGE_EOS | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED of type Gst.MessageType>, 'DEVICE_REMOVED': <flags GST_MESSAGE_ERROR | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_REMOVED of type Gst.MessageType>, 'PROPERTY_NOTIFY': <flags GST_MESSAGE_EOS | GST_MESSAGE_ERROR | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_PROPERTY_NOTIFY of type Gst.MessageType>, 'STREAM_COLLECTION': <flags GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_STREAM_COLLECTION of type Gst.MessageType>, 'STREAMS_SELECTED': <flags GST_MESSAGE_EOS | GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_STREAMS_SELECTED of type Gst.MessageType>, 'REDIRECT': <flags GST_MESSAGE_ERROR | GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_REDIRECT of type Gst.MessageType>, 'DEVICE_CHANGED': <flags GST_MESSAGE_EOS | GST_MESSAGE_ERROR | GST_MESSAGE_WARNING | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_PROPERTY_NOTIFY | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_STREAMS_SELECTED | GST_MESSAGE_REDIRECT | GST_MESSAGE_DEVICE_CHANGED of type Gst.MessageType>, 'ANY': <flags GST_MESSAGE_EOS | GST_MESSAGE_ERROR | GST_MESSAGE_WARNING | GST_MESSAGE_INFO | GST_MESSAGE_TAG | GST_MESSAGE_BUFFERING | GST_MESSAGE_STATE_CHANGED | GST_MESSAGE_STATE_DIRTY | GST_MESSAGE_STEP_DONE | GST_MESSAGE_CLOCK_PROVIDE | GST_MESSAGE_CLOCK_LOST | GST_MESSAGE_NEW_CLOCK | GST_MESSAGE_STRUCTURE_CHANGE | GST_MESSAGE_STREAM_STATUS | GST_MESSAGE_APPLICATION | GST_MESSAGE_ELEMENT | GST_MESSAGE_SEGMENT_START | GST_MESSAGE_SEGMENT_DONE | GST_MESSAGE_DURATION_CHANGED | GST_MESSAGE_LATENCY | GST_MESSAGE_ASYNC_START | GST_MESSAGE_ASYNC_DONE | GST_MESSAGE_REQUEST_STATE | GST_MESSAGE_STEP_START | GST_MESSAGE_QOS | GST_MESSAGE_PROGRESS | GST_MESSAGE_TOC | GST_MESSAGE_RESET_TIME | GST_MESSAGE_STREAM_START | GST_MESSAGE_NEED_CONTEXT | GST_MESSAGE_HAVE_CONTEXT | GST_MESSAGE_EXTENDED | GST_MESSAGE_DEVICE_ADDED | GST_MESSAGE_DEVICE_REMOVED | GST_MESSAGE_PROPERTY_NOTIFY | GST_MESSAGE_STREAM_COLLECTION | GST_MESSAGE_STREAMS_SELECTED | GST_MESSAGE_REDIRECT | GST_MESSAGE_DEVICE_CHANGED | GST_MESSAGE_ANY of type Gst.MessageType>, 'get_name': gi.FunctionInfo(get_name), 'to_quark': gi.FunctionInfo(to_quark)})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        128: 128,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        4096: 4096,
        8192: 8192,
        16384: 16384,
        32768: 32768,
        65536: 65536,
        131072: 131072,
        262144: 262144,
        524288: 524288,
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
        2147483649: 2147483649,
        2147483650: 2147483650,
        2147483651: 2147483651,
        2147483652: 2147483652,
        2147483653: 2147483653,
        2147483654: 2147483654,
        2147483655: 2147483655,
        4294967295: 4294967295,
    }
    __gtype__ = None # (!) real value is '<GType GstMessageType (94058977575040)>'
    __info__ = gi.EnumInfo(MessageType)


