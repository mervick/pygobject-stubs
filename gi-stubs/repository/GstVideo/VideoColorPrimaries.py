# encoding: utf-8
# module gi.repository.GstVideo
# from /usr/lib64/girepository-1.0/GstVideo-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class VideoColorPrimaries(__gobject.GEnum):
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

    def get_info(self, primaries): # real signature unknown; restored from __doc__
        """ get_info(primaries:GstVideo.VideoColorPrimaries) -> GstVideo.VideoColorPrimariesInfo """
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


    ADOBERGB = 8
    BT2020 = 7
    BT470BG = 3
    BT470M = 2
    BT709 = 1
    EBU3213 = 12
    FILM = 6
    SMPTE170M = 4
    SMPTE240M = 5
    SMPTEEG432 = 11
    SMPTERP431 = 10
    SMPTEST428 = 9
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstVideo', '__dict__': <attribute '__dict__' of 'VideoColorPrimaries' objects>, '__doc__': None, '__gtype__': <GType GstVideoColorPrimaries (94743669358464)>, '__enum_values__': {0: <enum GST_VIDEO_COLOR_PRIMARIES_UNKNOWN of type GstVideo.VideoColorPrimaries>, 1: <enum GST_VIDEO_COLOR_PRIMARIES_BT709 of type GstVideo.VideoColorPrimaries>, 2: <enum GST_VIDEO_COLOR_PRIMARIES_BT470M of type GstVideo.VideoColorPrimaries>, 3: <enum GST_VIDEO_COLOR_PRIMARIES_BT470BG of type GstVideo.VideoColorPrimaries>, 4: <enum GST_VIDEO_COLOR_PRIMARIES_SMPTE170M of type GstVideo.VideoColorPrimaries>, 5: <enum GST_VIDEO_COLOR_PRIMARIES_SMPTE240M of type GstVideo.VideoColorPrimaries>, 6: <enum GST_VIDEO_COLOR_PRIMARIES_FILM of type GstVideo.VideoColorPrimaries>, 7: <enum GST_VIDEO_COLOR_PRIMARIES_BT2020 of type GstVideo.VideoColorPrimaries>, 8: <enum GST_VIDEO_COLOR_PRIMARIES_ADOBERGB of type GstVideo.VideoColorPrimaries>, 9: <enum GST_VIDEO_COLOR_PRIMARIES_SMPTEST428 of type GstVideo.VideoColorPrimaries>, 10: <enum GST_VIDEO_COLOR_PRIMARIES_SMPTERP431 of type GstVideo.VideoColorPrimaries>, 11: <enum GST_VIDEO_COLOR_PRIMARIES_SMPTEEG432 of type GstVideo.VideoColorPrimaries>, 12: <enum GST_VIDEO_COLOR_PRIMARIES_EBU3213 of type GstVideo.VideoColorPrimaries>}, '__info__': gi.EnumInfo(VideoColorPrimaries), 'UNKNOWN': <enum GST_VIDEO_COLOR_PRIMARIES_UNKNOWN of type GstVideo.VideoColorPrimaries>, 'BT709': <enum GST_VIDEO_COLOR_PRIMARIES_BT709 of type GstVideo.VideoColorPrimaries>, 'BT470M': <enum GST_VIDEO_COLOR_PRIMARIES_BT470M of type GstVideo.VideoColorPrimaries>, 'BT470BG': <enum GST_VIDEO_COLOR_PRIMARIES_BT470BG of type GstVideo.VideoColorPrimaries>, 'SMPTE170M': <enum GST_VIDEO_COLOR_PRIMARIES_SMPTE170M of type GstVideo.VideoColorPrimaries>, 'SMPTE240M': <enum GST_VIDEO_COLOR_PRIMARIES_SMPTE240M of type GstVideo.VideoColorPrimaries>, 'FILM': <enum GST_VIDEO_COLOR_PRIMARIES_FILM of type GstVideo.VideoColorPrimaries>, 'BT2020': <enum GST_VIDEO_COLOR_PRIMARIES_BT2020 of type GstVideo.VideoColorPrimaries>, 'ADOBERGB': <enum GST_VIDEO_COLOR_PRIMARIES_ADOBERGB of type GstVideo.VideoColorPrimaries>, 'SMPTEST428': <enum GST_VIDEO_COLOR_PRIMARIES_SMPTEST428 of type GstVideo.VideoColorPrimaries>, 'SMPTERP431': <enum GST_VIDEO_COLOR_PRIMARIES_SMPTERP431 of type GstVideo.VideoColorPrimaries>, 'SMPTEEG432': <enum GST_VIDEO_COLOR_PRIMARIES_SMPTEEG432 of type GstVideo.VideoColorPrimaries>, 'EBU3213': <enum GST_VIDEO_COLOR_PRIMARIES_EBU3213 of type GstVideo.VideoColorPrimaries>, 'get_info': gi.FunctionInfo(get_info)})"
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
    }
    __gtype__ = None # (!) real value is '<GType GstVideoColorPrimaries (94743669358464)>'
    __info__ = gi.EnumInfo(VideoColorPrimaries)


