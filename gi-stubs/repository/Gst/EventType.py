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


class EventType(__gobject.GEnum):
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

    def get_flags(self, type): # real signature unknown; restored from __doc__
        """ get_flags(type:Gst.EventType) -> Gst.EventTypeFlags """
        pass

    def get_name(self, type): # real signature unknown; restored from __doc__
        """ get_name(type:Gst.EventType) -> str """
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
        """ to_quark(type:Gst.EventType) -> int """
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


    BUFFERSIZE = 23054
    CAPS = 12814
    CUSTOM_BOTH = 79367
    CUSTOM_BOTH_OOB = 81923
    CUSTOM_DOWNSTREAM = 71686
    CUSTOM_DOWNSTREAM_OOB = 74242
    CUSTOM_DOWNSTREAM_STICKY = 76830
    CUSTOM_UPSTREAM = 69121
    EOS = 28174
    FLUSH_START = 2563
    FLUSH_STOP = 5127
    GAP = 40966
    LATENCY = 56321
    NAVIGATION = 53761
    PROTECTION = 33310
    QOS = 48641
    RECONFIGURE = 61441
    SEEK = 51201
    SEGMENT = 17934
    SEGMENT_DONE = 38406
    SELECT_STREAMS = 66561
    SINK_MESSAGE = 25630
    STEP = 58881
    STREAM_COLLECTION = 19230
    STREAM_GROUP_DONE = 26894
    STREAM_START = 10254
    TAG = 20510
    TOC = 30750
    TOC_SELECT = 64001
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gst', '__dict__': <attribute '__dict__' of 'EventType' objects>, '__doc__': None, '__gtype__': <GType GstEventType (94058977663856)>, '__enum_values__': {0: <enum GST_EVENT_UNKNOWN of type Gst.EventType>, 2563: <enum GST_EVENT_FLUSH_START of type Gst.EventType>, 5127: <enum GST_EVENT_FLUSH_STOP of type Gst.EventType>, 10254: <enum GST_EVENT_STREAM_START of type Gst.EventType>, 12814: <enum GST_EVENT_CAPS of type Gst.EventType>, 17934: <enum GST_EVENT_SEGMENT of type Gst.EventType>, 19230: <enum GST_EVENT_STREAM_COLLECTION of type Gst.EventType>, 20510: <enum GST_EVENT_TAG of type Gst.EventType>, 23054: <enum GST_EVENT_BUFFERSIZE of type Gst.EventType>, 25630: <enum GST_EVENT_SINK_MESSAGE of type Gst.EventType>, 26894: <enum GST_EVENT_STREAM_GROUP_DONE of type Gst.EventType>, 28174: <enum GST_EVENT_EOS of type Gst.EventType>, 30750: <enum GST_EVENT_TOC of type Gst.EventType>, 33310: <enum GST_EVENT_PROTECTION of type Gst.EventType>, 38406: <enum GST_EVENT_SEGMENT_DONE of type Gst.EventType>, 40966: <enum GST_EVENT_GAP of type Gst.EventType>, 48641: <enum GST_EVENT_QOS of type Gst.EventType>, 51201: <enum GST_EVENT_SEEK of type Gst.EventType>, 53761: <enum GST_EVENT_NAVIGATION of type Gst.EventType>, 56321: <enum GST_EVENT_LATENCY of type Gst.EventType>, 58881: <enum GST_EVENT_STEP of type Gst.EventType>, 61441: <enum GST_EVENT_RECONFIGURE of type Gst.EventType>, 64001: <enum GST_EVENT_TOC_SELECT of type Gst.EventType>, 66561: <enum GST_EVENT_SELECT_STREAMS of type Gst.EventType>, 69121: <enum GST_EVENT_CUSTOM_UPSTREAM of type Gst.EventType>, 71686: <enum GST_EVENT_CUSTOM_DOWNSTREAM of type Gst.EventType>, 74242: <enum GST_EVENT_CUSTOM_DOWNSTREAM_OOB of type Gst.EventType>, 76830: <enum GST_EVENT_CUSTOM_DOWNSTREAM_STICKY of type Gst.EventType>, 79367: <enum GST_EVENT_CUSTOM_BOTH of type Gst.EventType>, 81923: <enum GST_EVENT_CUSTOM_BOTH_OOB of type Gst.EventType>}, '__info__': gi.EnumInfo(EventType), 'UNKNOWN': <enum GST_EVENT_UNKNOWN of type Gst.EventType>, 'FLUSH_START': <enum GST_EVENT_FLUSH_START of type Gst.EventType>, 'FLUSH_STOP': <enum GST_EVENT_FLUSH_STOP of type Gst.EventType>, 'STREAM_START': <enum GST_EVENT_STREAM_START of type Gst.EventType>, 'CAPS': <enum GST_EVENT_CAPS of type Gst.EventType>, 'SEGMENT': <enum GST_EVENT_SEGMENT of type Gst.EventType>, 'STREAM_COLLECTION': <enum GST_EVENT_STREAM_COLLECTION of type Gst.EventType>, 'TAG': <enum GST_EVENT_TAG of type Gst.EventType>, 'BUFFERSIZE': <enum GST_EVENT_BUFFERSIZE of type Gst.EventType>, 'SINK_MESSAGE': <enum GST_EVENT_SINK_MESSAGE of type Gst.EventType>, 'STREAM_GROUP_DONE': <enum GST_EVENT_STREAM_GROUP_DONE of type Gst.EventType>, 'EOS': <enum GST_EVENT_EOS of type Gst.EventType>, 'TOC': <enum GST_EVENT_TOC of type Gst.EventType>, 'PROTECTION': <enum GST_EVENT_PROTECTION of type Gst.EventType>, 'SEGMENT_DONE': <enum GST_EVENT_SEGMENT_DONE of type Gst.EventType>, 'GAP': <enum GST_EVENT_GAP of type Gst.EventType>, 'QOS': <enum GST_EVENT_QOS of type Gst.EventType>, 'SEEK': <enum GST_EVENT_SEEK of type Gst.EventType>, 'NAVIGATION': <enum GST_EVENT_NAVIGATION of type Gst.EventType>, 'LATENCY': <enum GST_EVENT_LATENCY of type Gst.EventType>, 'STEP': <enum GST_EVENT_STEP of type Gst.EventType>, 'RECONFIGURE': <enum GST_EVENT_RECONFIGURE of type Gst.EventType>, 'TOC_SELECT': <enum GST_EVENT_TOC_SELECT of type Gst.EventType>, 'SELECT_STREAMS': <enum GST_EVENT_SELECT_STREAMS of type Gst.EventType>, 'CUSTOM_UPSTREAM': <enum GST_EVENT_CUSTOM_UPSTREAM of type Gst.EventType>, 'CUSTOM_DOWNSTREAM': <enum GST_EVENT_CUSTOM_DOWNSTREAM of type Gst.EventType>, 'CUSTOM_DOWNSTREAM_OOB': <enum GST_EVENT_CUSTOM_DOWNSTREAM_OOB of type Gst.EventType>, 'CUSTOM_DOWNSTREAM_STICKY': <enum GST_EVENT_CUSTOM_DOWNSTREAM_STICKY of type Gst.EventType>, 'CUSTOM_BOTH': <enum GST_EVENT_CUSTOM_BOTH of type Gst.EventType>, 'CUSTOM_BOTH_OOB': <enum GST_EVENT_CUSTOM_BOTH_OOB of type Gst.EventType>, 'get_flags': gi.FunctionInfo(get_flags), 'get_name': gi.FunctionInfo(get_name), 'to_quark': gi.FunctionInfo(to_quark)})"
    __enum_values__ = {
        0: 0,
        2563: 2563,
        5127: 5127,
        10254: 10254,
        12814: 12814,
        17934: 17934,
        19230: 19230,
        20510: 20510,
        23054: 23054,
        25630: 25630,
        26894: 26894,
        28174: 28174,
        30750: 30750,
        33310: 33310,
        38406: 38406,
        40966: 40966,
        48641: 48641,
        51201: 51201,
        53761: 53761,
        56321: 56321,
        58881: 58881,
        61441: 61441,
        64001: 64001,
        66561: 66561,
        69121: 69121,
        71686: 71686,
        74242: 74242,
        76830: 76830,
        79367: 79367,
        81923: 81923,
    }
    __gtype__ = None # (!) real value is '<GType GstEventType (94058977663856)>'
    __info__ = gi.EnumInfo(EventType)


