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


class VideoFormat(__gobject.GEnum):
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

    def from_fourcc(self, fourcc): # real signature unknown; restored from __doc__
        """ from_fourcc(fourcc:int) -> GstVideo.VideoFormat """
        pass

    def from_masks(self, depth, bpp, endianness, red_mask, green_mask, blue_mask, alpha_mask): # real signature unknown; restored from __doc__
        """ from_masks(depth:int, bpp:int, endianness:int, red_mask:int, green_mask:int, blue_mask:int, alpha_mask:int) -> GstVideo.VideoFormat """
        pass

    def from_string(self, format): # real signature unknown; restored from __doc__
        """ from_string(format:str) -> GstVideo.VideoFormat """
        pass

    def get_info(self, format): # real signature unknown; restored from __doc__
        """ get_info(format:GstVideo.VideoFormat) -> GstVideo.VideoFormatInfo """
        pass

    def get_palette(self, format): # real signature unknown; restored from __doc__
        """ get_palette(format:GstVideo.VideoFormat) -> size:int """
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

    def to_fourcc(self, format): # real signature unknown; restored from __doc__
        """ to_fourcc(format:GstVideo.VideoFormat) -> int """
        return 0

    def to_string(self, format): # real signature unknown; restored from __doc__
        """ to_string(format:GstVideo.VideoFormat) -> str """
        return ""

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


    A420 = 34
    A420_10BE = 54
    A420_10LE = 55
    A422_10BE = 56
    A422_10LE = 57
    A444_10BE = 58
    A444_10LE = 59
    ABGR = 14
    ARGB = 13
    ARGB64 = 39
    AYUV = 6
    AYUV64 = 40
    BGR = 16
    BGR10A2_LE = 85
    BGR15 = 32
    BGR16 = 30
    BGRA = 12
    BGRX = 8
    ENCODED = 1
    GBR = 48
    GBRA = 65
    GBRA_10BE = 66
    GBRA_10LE = 67
    GBRA_12BE = 70
    GBRA_12LE = 71
    GBR_10BE = 49
    GBR_10LE = 50
    GBR_12BE = 68
    GBR_12LE = 69
    GRAY10_LE32 = 78
    GRAY16_BE = 26
    GRAY16_LE = 27
    GRAY8 = 25
    I420 = 2
    I420_10BE = 42
    I420_10LE = 43
    I420_12BE = 72
    I420_12LE = 73
    I422_10BE = 44
    I422_10LE = 45
    I422_12BE = 74
    I422_12LE = 75
    IYU1 = 38
    IYU2 = 63
    NV12 = 23
    NV12_10LE32 = 79
    NV12_10LE40 = 81
    NV12_64Z32 = 53
    NV16 = 51
    NV16_10LE32 = 80
    NV21 = 24
    NV24 = 52
    NV61 = 60
    P010_10BE = 61
    P010_10LE = 62
    R210 = 41
    RGB = 15
    RGB15 = 31
    RGB16 = 29
    RGB8P = 35
    RGBA = 11
    RGBX = 7
    UNKNOWN = 0
    UYVP = 33
    UYVY = 5
    V210 = 21
    V216 = 22
    V308 = 28
    VUYA = 84
    VYUY = 64
    XBGR = 10
    XRGB = 9
    Y210 = 82
    Y410 = 83
    Y41B = 17
    Y42B = 18
    Y444 = 20
    Y444_10BE = 46
    Y444_10LE = 47
    Y444_12BE = 76
    Y444_12LE = 77
    YUV9 = 36
    YUY2 = 4
    YV12 = 3
    YVU9 = 37
    YVYU = 19
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstVideo', '__dict__': <attribute '__dict__' of 'VideoFormat' objects>, '__doc__': None, '__gtype__': <GType GstVideoFormat (94743669244608)>, '__enum_values__': {0: <enum GST_VIDEO_FORMAT_UNKNOWN of type GstVideo.VideoFormat>, 1: <enum GST_VIDEO_FORMAT_ENCODED of type GstVideo.VideoFormat>, 2: <enum GST_VIDEO_FORMAT_I420 of type GstVideo.VideoFormat>, 3: <enum GST_VIDEO_FORMAT_YV12 of type GstVideo.VideoFormat>, 4: <enum GST_VIDEO_FORMAT_YUY2 of type GstVideo.VideoFormat>, 5: <enum GST_VIDEO_FORMAT_UYVY of type GstVideo.VideoFormat>, 6: <enum GST_VIDEO_FORMAT_AYUV of type GstVideo.VideoFormat>, 7: <enum GST_VIDEO_FORMAT_RGBx of type GstVideo.VideoFormat>, 8: <enum GST_VIDEO_FORMAT_BGRx of type GstVideo.VideoFormat>, 9: <enum GST_VIDEO_FORMAT_xRGB of type GstVideo.VideoFormat>, 10: <enum GST_VIDEO_FORMAT_xBGR of type GstVideo.VideoFormat>, 11: <enum GST_VIDEO_FORMAT_RGBA of type GstVideo.VideoFormat>, 12: <enum GST_VIDEO_FORMAT_BGRA of type GstVideo.VideoFormat>, 13: <enum GST_VIDEO_FORMAT_ARGB of type GstVideo.VideoFormat>, 14: <enum GST_VIDEO_FORMAT_ABGR of type GstVideo.VideoFormat>, 15: <enum GST_VIDEO_FORMAT_RGB of type GstVideo.VideoFormat>, 16: <enum GST_VIDEO_FORMAT_BGR of type GstVideo.VideoFormat>, 17: <enum GST_VIDEO_FORMAT_Y41B of type GstVideo.VideoFormat>, 18: <enum GST_VIDEO_FORMAT_Y42B of type GstVideo.VideoFormat>, 19: <enum GST_VIDEO_FORMAT_YVYU of type GstVideo.VideoFormat>, 20: <enum GST_VIDEO_FORMAT_Y444 of type GstVideo.VideoFormat>, 21: <enum GST_VIDEO_FORMAT_v210 of type GstVideo.VideoFormat>, 22: <enum GST_VIDEO_FORMAT_v216 of type GstVideo.VideoFormat>, 23: <enum GST_VIDEO_FORMAT_NV12 of type GstVideo.VideoFormat>, 24: <enum GST_VIDEO_FORMAT_NV21 of type GstVideo.VideoFormat>, 25: <enum GST_VIDEO_FORMAT_GRAY8 of type GstVideo.VideoFormat>, 26: <enum GST_VIDEO_FORMAT_GRAY16_BE of type GstVideo.VideoFormat>, 27: <enum GST_VIDEO_FORMAT_GRAY16_LE of type GstVideo.VideoFormat>, 28: <enum GST_VIDEO_FORMAT_v308 of type GstVideo.VideoFormat>, 29: <enum GST_VIDEO_FORMAT_RGB16 of type GstVideo.VideoFormat>, 30: <enum GST_VIDEO_FORMAT_BGR16 of type GstVideo.VideoFormat>, 31: <enum GST_VIDEO_FORMAT_RGB15 of type GstVideo.VideoFormat>, 32: <enum GST_VIDEO_FORMAT_BGR15 of type GstVideo.VideoFormat>, 33: <enum GST_VIDEO_FORMAT_UYVP of type GstVideo.VideoFormat>, 34: <enum GST_VIDEO_FORMAT_A420 of type GstVideo.VideoFormat>, 35: <enum GST_VIDEO_FORMAT_RGB8P of type GstVideo.VideoFormat>, 36: <enum GST_VIDEO_FORMAT_YUV9 of type GstVideo.VideoFormat>, 37: <enum GST_VIDEO_FORMAT_YVU9 of type GstVideo.VideoFormat>, 38: <enum GST_VIDEO_FORMAT_IYU1 of type GstVideo.VideoFormat>, 39: <enum GST_VIDEO_FORMAT_ARGB64 of type GstVideo.VideoFormat>, 40: <enum GST_VIDEO_FORMAT_AYUV64 of type GstVideo.VideoFormat>, 41: <enum GST_VIDEO_FORMAT_r210 of type GstVideo.VideoFormat>, 42: <enum GST_VIDEO_FORMAT_I420_10BE of type GstVideo.VideoFormat>, 43: <enum GST_VIDEO_FORMAT_I420_10LE of type GstVideo.VideoFormat>, 44: <enum GST_VIDEO_FORMAT_I422_10BE of type GstVideo.VideoFormat>, 45: <enum GST_VIDEO_FORMAT_I422_10LE of type GstVideo.VideoFormat>, 46: <enum GST_VIDEO_FORMAT_Y444_10BE of type GstVideo.VideoFormat>, 47: <enum GST_VIDEO_FORMAT_Y444_10LE of type GstVideo.VideoFormat>, 48: <enum GST_VIDEO_FORMAT_GBR of type GstVideo.VideoFormat>, 49: <enum GST_VIDEO_FORMAT_GBR_10BE of type GstVideo.VideoFormat>, 50: <enum GST_VIDEO_FORMAT_GBR_10LE of type GstVideo.VideoFormat>, 51: <enum GST_VIDEO_FORMAT_NV16 of type GstVideo.VideoFormat>, 52: <enum GST_VIDEO_FORMAT_NV24 of type GstVideo.VideoFormat>, 53: <enum GST_VIDEO_FORMAT_NV12_64Z32 of type GstVideo.VideoFormat>, 54: <enum GST_VIDEO_FORMAT_A420_10BE of type GstVideo.VideoFormat>, 55: <enum GST_VIDEO_FORMAT_A420_10LE of type GstVideo.VideoFormat>, 56: <enum GST_VIDEO_FORMAT_A422_10BE of type GstVideo.VideoFormat>, 57: <enum GST_VIDEO_FORMAT_A422_10LE of type GstVideo.VideoFormat>, 58: <enum GST_VIDEO_FORMAT_A444_10BE of type GstVideo.VideoFormat>, 59: <enum GST_VIDEO_FORMAT_A444_10LE of type GstVideo.VideoFormat>, 60: <enum GST_VIDEO_FORMAT_NV61 of type GstVideo.VideoFormat>, 61: <enum GST_VIDEO_FORMAT_P010_10BE of type GstVideo.VideoFormat>, 62: <enum GST_VIDEO_FORMAT_P010_10LE of type GstVideo.VideoFormat>, 63: <enum GST_VIDEO_FORMAT_IYU2 of type GstVideo.VideoFormat>, 64: <enum GST_VIDEO_FORMAT_VYUY of type GstVideo.VideoFormat>, 65: <enum GST_VIDEO_FORMAT_GBRA of type GstVideo.VideoFormat>, 66: <enum GST_VIDEO_FORMAT_GBRA_10BE of type GstVideo.VideoFormat>, 67: <enum GST_VIDEO_FORMAT_GBRA_10LE of type GstVideo.VideoFormat>, 68: <enum GST_VIDEO_FORMAT_GBR_12BE of type GstVideo.VideoFormat>, 69: <enum GST_VIDEO_FORMAT_GBR_12LE of type GstVideo.VideoFormat>, 70: <enum GST_VIDEO_FORMAT_GBRA_12BE of type GstVideo.VideoFormat>, 71: <enum GST_VIDEO_FORMAT_GBRA_12LE of type GstVideo.VideoFormat>, 72: <enum GST_VIDEO_FORMAT_I420_12BE of type GstVideo.VideoFormat>, 73: <enum GST_VIDEO_FORMAT_I420_12LE of type GstVideo.VideoFormat>, 74: <enum GST_VIDEO_FORMAT_I422_12BE of type GstVideo.VideoFormat>, 75: <enum GST_VIDEO_FORMAT_I422_12LE of type GstVideo.VideoFormat>, 76: <enum GST_VIDEO_FORMAT_Y444_12BE of type GstVideo.VideoFormat>, 77: <enum GST_VIDEO_FORMAT_Y444_12LE of type GstVideo.VideoFormat>, 78: <enum GST_VIDEO_FORMAT_GRAY10_LE32 of type GstVideo.VideoFormat>, 79: <enum GST_VIDEO_FORMAT_NV12_10LE32 of type GstVideo.VideoFormat>, 80: <enum GST_VIDEO_FORMAT_NV16_10LE32 of type GstVideo.VideoFormat>, 81: <enum GST_VIDEO_FORMAT_NV12_10LE40 of type GstVideo.VideoFormat>, 82: <enum GST_VIDEO_FORMAT_Y210 of type GstVideo.VideoFormat>, 83: <enum GST_VIDEO_FORMAT_Y410 of type GstVideo.VideoFormat>, 84: <enum GST_VIDEO_FORMAT_VUYA of type GstVideo.VideoFormat>, 85: <enum GST_VIDEO_FORMAT_BGR10A2_LE of type GstVideo.VideoFormat>}, '__info__': gi.EnumInfo(VideoFormat), 'UNKNOWN': <enum GST_VIDEO_FORMAT_UNKNOWN of type GstVideo.VideoFormat>, 'ENCODED': <enum GST_VIDEO_FORMAT_ENCODED of type GstVideo.VideoFormat>, 'I420': <enum GST_VIDEO_FORMAT_I420 of type GstVideo.VideoFormat>, 'YV12': <enum GST_VIDEO_FORMAT_YV12 of type GstVideo.VideoFormat>, 'YUY2': <enum GST_VIDEO_FORMAT_YUY2 of type GstVideo.VideoFormat>, 'UYVY': <enum GST_VIDEO_FORMAT_UYVY of type GstVideo.VideoFormat>, 'AYUV': <enum GST_VIDEO_FORMAT_AYUV of type GstVideo.VideoFormat>, 'RGBX': <enum GST_VIDEO_FORMAT_RGBx of type GstVideo.VideoFormat>, 'BGRX': <enum GST_VIDEO_FORMAT_BGRx of type GstVideo.VideoFormat>, 'XRGB': <enum GST_VIDEO_FORMAT_xRGB of type GstVideo.VideoFormat>, 'XBGR': <enum GST_VIDEO_FORMAT_xBGR of type GstVideo.VideoFormat>, 'RGBA': <enum GST_VIDEO_FORMAT_RGBA of type GstVideo.VideoFormat>, 'BGRA': <enum GST_VIDEO_FORMAT_BGRA of type GstVideo.VideoFormat>, 'ARGB': <enum GST_VIDEO_FORMAT_ARGB of type GstVideo.VideoFormat>, 'ABGR': <enum GST_VIDEO_FORMAT_ABGR of type GstVideo.VideoFormat>, 'RGB': <enum GST_VIDEO_FORMAT_RGB of type GstVideo.VideoFormat>, 'BGR': <enum GST_VIDEO_FORMAT_BGR of type GstVideo.VideoFormat>, 'Y41B': <enum GST_VIDEO_FORMAT_Y41B of type GstVideo.VideoFormat>, 'Y42B': <enum GST_VIDEO_FORMAT_Y42B of type GstVideo.VideoFormat>, 'YVYU': <enum GST_VIDEO_FORMAT_YVYU of type GstVideo.VideoFormat>, 'Y444': <enum GST_VIDEO_FORMAT_Y444 of type GstVideo.VideoFormat>, 'V210': <enum GST_VIDEO_FORMAT_v210 of type GstVideo.VideoFormat>, 'V216': <enum GST_VIDEO_FORMAT_v216 of type GstVideo.VideoFormat>, 'NV12': <enum GST_VIDEO_FORMAT_NV12 of type GstVideo.VideoFormat>, 'NV21': <enum GST_VIDEO_FORMAT_NV21 of type GstVideo.VideoFormat>, 'GRAY8': <enum GST_VIDEO_FORMAT_GRAY8 of type GstVideo.VideoFormat>, 'GRAY16_BE': <enum GST_VIDEO_FORMAT_GRAY16_BE of type GstVideo.VideoFormat>, 'GRAY16_LE': <enum GST_VIDEO_FORMAT_GRAY16_LE of type GstVideo.VideoFormat>, 'V308': <enum GST_VIDEO_FORMAT_v308 of type GstVideo.VideoFormat>, 'RGB16': <enum GST_VIDEO_FORMAT_RGB16 of type GstVideo.VideoFormat>, 'BGR16': <enum GST_VIDEO_FORMAT_BGR16 of type GstVideo.VideoFormat>, 'RGB15': <enum GST_VIDEO_FORMAT_RGB15 of type GstVideo.VideoFormat>, 'BGR15': <enum GST_VIDEO_FORMAT_BGR15 of type GstVideo.VideoFormat>, 'UYVP': <enum GST_VIDEO_FORMAT_UYVP of type GstVideo.VideoFormat>, 'A420': <enum GST_VIDEO_FORMAT_A420 of type GstVideo.VideoFormat>, 'RGB8P': <enum GST_VIDEO_FORMAT_RGB8P of type GstVideo.VideoFormat>, 'YUV9': <enum GST_VIDEO_FORMAT_YUV9 of type GstVideo.VideoFormat>, 'YVU9': <enum GST_VIDEO_FORMAT_YVU9 of type GstVideo.VideoFormat>, 'IYU1': <enum GST_VIDEO_FORMAT_IYU1 of type GstVideo.VideoFormat>, 'ARGB64': <enum GST_VIDEO_FORMAT_ARGB64 of type GstVideo.VideoFormat>, 'AYUV64': <enum GST_VIDEO_FORMAT_AYUV64 of type GstVideo.VideoFormat>, 'R210': <enum GST_VIDEO_FORMAT_r210 of type GstVideo.VideoFormat>, 'I420_10BE': <enum GST_VIDEO_FORMAT_I420_10BE of type GstVideo.VideoFormat>, 'I420_10LE': <enum GST_VIDEO_FORMAT_I420_10LE of type GstVideo.VideoFormat>, 'I422_10BE': <enum GST_VIDEO_FORMAT_I422_10BE of type GstVideo.VideoFormat>, 'I422_10LE': <enum GST_VIDEO_FORMAT_I422_10LE of type GstVideo.VideoFormat>, 'Y444_10BE': <enum GST_VIDEO_FORMAT_Y444_10BE of type GstVideo.VideoFormat>, 'Y444_10LE': <enum GST_VIDEO_FORMAT_Y444_10LE of type GstVideo.VideoFormat>, 'GBR': <enum GST_VIDEO_FORMAT_GBR of type GstVideo.VideoFormat>, 'GBR_10BE': <enum GST_VIDEO_FORMAT_GBR_10BE of type GstVideo.VideoFormat>, 'GBR_10LE': <enum GST_VIDEO_FORMAT_GBR_10LE of type GstVideo.VideoFormat>, 'NV16': <enum GST_VIDEO_FORMAT_NV16 of type GstVideo.VideoFormat>, 'NV24': <enum GST_VIDEO_FORMAT_NV24 of type GstVideo.VideoFormat>, 'NV12_64Z32': <enum GST_VIDEO_FORMAT_NV12_64Z32 of type GstVideo.VideoFormat>, 'A420_10BE': <enum GST_VIDEO_FORMAT_A420_10BE of type GstVideo.VideoFormat>, 'A420_10LE': <enum GST_VIDEO_FORMAT_A420_10LE of type GstVideo.VideoFormat>, 'A422_10BE': <enum GST_VIDEO_FORMAT_A422_10BE of type GstVideo.VideoFormat>, 'A422_10LE': <enum GST_VIDEO_FORMAT_A422_10LE of type GstVideo.VideoFormat>, 'A444_10BE': <enum GST_VIDEO_FORMAT_A444_10BE of type GstVideo.VideoFormat>, 'A444_10LE': <enum GST_VIDEO_FORMAT_A444_10LE of type GstVideo.VideoFormat>, 'NV61': <enum GST_VIDEO_FORMAT_NV61 of type GstVideo.VideoFormat>, 'P010_10BE': <enum GST_VIDEO_FORMAT_P010_10BE of type GstVideo.VideoFormat>, 'P010_10LE': <enum GST_VIDEO_FORMAT_P010_10LE of type GstVideo.VideoFormat>, 'IYU2': <enum GST_VIDEO_FORMAT_IYU2 of type GstVideo.VideoFormat>, 'VYUY': <enum GST_VIDEO_FORMAT_VYUY of type GstVideo.VideoFormat>, 'GBRA': <enum GST_VIDEO_FORMAT_GBRA of type GstVideo.VideoFormat>, 'GBRA_10BE': <enum GST_VIDEO_FORMAT_GBRA_10BE of type GstVideo.VideoFormat>, 'GBRA_10LE': <enum GST_VIDEO_FORMAT_GBRA_10LE of type GstVideo.VideoFormat>, 'GBR_12BE': <enum GST_VIDEO_FORMAT_GBR_12BE of type GstVideo.VideoFormat>, 'GBR_12LE': <enum GST_VIDEO_FORMAT_GBR_12LE of type GstVideo.VideoFormat>, 'GBRA_12BE': <enum GST_VIDEO_FORMAT_GBRA_12BE of type GstVideo.VideoFormat>, 'GBRA_12LE': <enum GST_VIDEO_FORMAT_GBRA_12LE of type GstVideo.VideoFormat>, 'I420_12BE': <enum GST_VIDEO_FORMAT_I420_12BE of type GstVideo.VideoFormat>, 'I420_12LE': <enum GST_VIDEO_FORMAT_I420_12LE of type GstVideo.VideoFormat>, 'I422_12BE': <enum GST_VIDEO_FORMAT_I422_12BE of type GstVideo.VideoFormat>, 'I422_12LE': <enum GST_VIDEO_FORMAT_I422_12LE of type GstVideo.VideoFormat>, 'Y444_12BE': <enum GST_VIDEO_FORMAT_Y444_12BE of type GstVideo.VideoFormat>, 'Y444_12LE': <enum GST_VIDEO_FORMAT_Y444_12LE of type GstVideo.VideoFormat>, 'GRAY10_LE32': <enum GST_VIDEO_FORMAT_GRAY10_LE32 of type GstVideo.VideoFormat>, 'NV12_10LE32': <enum GST_VIDEO_FORMAT_NV12_10LE32 of type GstVideo.VideoFormat>, 'NV16_10LE32': <enum GST_VIDEO_FORMAT_NV16_10LE32 of type GstVideo.VideoFormat>, 'NV12_10LE40': <enum GST_VIDEO_FORMAT_NV12_10LE40 of type GstVideo.VideoFormat>, 'Y210': <enum GST_VIDEO_FORMAT_Y210 of type GstVideo.VideoFormat>, 'Y410': <enum GST_VIDEO_FORMAT_Y410 of type GstVideo.VideoFormat>, 'VUYA': <enum GST_VIDEO_FORMAT_VUYA of type GstVideo.VideoFormat>, 'BGR10A2_LE': <enum GST_VIDEO_FORMAT_BGR10A2_LE of type GstVideo.VideoFormat>, 'from_fourcc': gi.FunctionInfo(from_fourcc), 'from_masks': gi.FunctionInfo(from_masks), 'from_string': gi.FunctionInfo(from_string), 'get_info': gi.FunctionInfo(get_info), 'get_palette': gi.FunctionInfo(get_palette), 'to_fourcc': gi.FunctionInfo(to_fourcc), 'to_string': gi.FunctionInfo(to_string)})"
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
        46: 46,
        47: 47,
        48: 48,
        49: 49,
        50: 50,
        51: 51,
        52: 52,
        53: 53,
        54: 54,
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
        64: 64,
        65: 65,
        66: 66,
        67: 67,
        68: 68,
        69: 69,
        70: 70,
        71: 71,
        72: 72,
        73: 73,
        74: 74,
        75: 75,
        76: 76,
        77: 77,
        78: 78,
        79: 79,
        80: 80,
        81: 81,
        82: 82,
        83: 83,
        84: 84,
        85: 85,
    }
    __gtype__ = None # (!) real value is '<GType GstVideoFormat (94743669244608)>'
    __info__ = gi.EnumInfo(VideoFormat)


