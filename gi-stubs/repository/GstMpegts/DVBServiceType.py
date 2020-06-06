# encoding: utf-8
# module gi.repository.GstMpegts
# from /usr/lib64/girepository-1.0/GstMpegts-1.0.typelib
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


class DVBServiceType(__gobject.GEnum):
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


    ADVANCED_CODEC_DIGITAL_RADIO_SOUND = 10
    ADVANCED_CODEC_HD_DIGITAL_TELEVISION = 25
    ADVANCED_CODEC_HD_NVOD_REFERENCE = 27
    ADVANCED_CODEC_HD_NVOD_TIME_SHIFTED = 26
    ADVANCED_CODEC_MOSAIC = 11
    ADVANCED_CODEC_SD_DIGITAL_TELEVISION = 22
    ADVANCED_CODEC_SD_NVOD_REFERENCE = 24
    ADVANCED_CODEC_SD_NVOD_TIME_SHIFTED = 23
    ADVANCED_CODEC_STEREO_HD_DIGITAL_TELEVISION = 28
    ADVANCED_CODEC_STEREO_HD_NVOD_REFERENCE = 30
    ADVANCED_CODEC_STEREO_HD_NVOD_TIME_SHIFTED = 29
    DATA_BROADCAST = 12
    DIGITAL_RADIO_SOUND = 2
    DIGITAL_TELEVISION = 1
    DVB_MHP = 16
    DVB_SRM = 8
    FM_RADIO = 7
    MOSAIC = 6
    MPEG2_HD_DIGITAL_TELEVISION = 17
    NVOD_REFERENCE = 4
    NVOD_TIME_SHIFTED = 5
    RCS_FLS = 15
    RCS_MAP = 14
    RESERVED_00 = 0
    RESERVED_09 = 9
    RESERVED_0D_COMMON_INTERFACE = 13
    RESERVED_FF = 31
    TELETEXT = 3
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'DVBServiceType' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsDVBServiceType (94624018591088)>, '__enum_values__': {0: <enum GST_DVB_SERVICE_RESERVED_00 of type GstMpegts.DVBServiceType>, 1: <enum GST_DVB_SERVICE_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 2: <enum GST_DVB_SERVICE_DIGITAL_RADIO_SOUND of type GstMpegts.DVBServiceType>, 3: <enum GST_DVB_SERVICE_TELETEXT of type GstMpegts.DVBServiceType>, 4: <enum GST_DVB_SERVICE_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 5: <enum GST_DVB_SERVICE_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 6: <enum GST_DVB_SERVICE_MOSAIC of type GstMpegts.DVBServiceType>, 7: <enum GST_DVB_SERVICE_FM_RADIO of type GstMpegts.DVBServiceType>, 8: <enum GST_DVB_SERVICE_DVB_SRM of type GstMpegts.DVBServiceType>, 9: <enum GST_DVB_SERVICE_RESERVED_09 of type GstMpegts.DVBServiceType>, 10: <enum GST_DVB_SERVICE_ADVANCED_CODEC_DIGITAL_RADIO_SOUND of type GstMpegts.DVBServiceType>, 11: <enum GST_DVB_SERVICE_ADVANCED_CODEC_MOSAIC of type GstMpegts.DVBServiceType>, 12: <enum GST_DVB_SERVICE_DATA_BROADCAST of type GstMpegts.DVBServiceType>, 13: <enum GST_DVB_SERVICE_RESERVED_0D_COMMON_INTERFACE of type GstMpegts.DVBServiceType>, 14: <enum GST_DVB_SERVICE_RCS_MAP of type GstMpegts.DVBServiceType>, 15: <enum GST_DVB_SERVICE_RCS_FLS of type GstMpegts.DVBServiceType>, 16: <enum GST_DVB_SERVICE_DVB_MHP of type GstMpegts.DVBServiceType>, 17: <enum GST_DVB_SERVICE_MPEG2_HD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 22: <enum GST_DVB_SERVICE_ADVANCED_CODEC_SD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 23: <enum GST_DVB_SERVICE_ADVANCED_CODEC_SD_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 24: <enum GST_DVB_SERVICE_ADVANCED_CODEC_SD_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 25: <enum GST_DVB_SERVICE_ADVANCED_CODEC_HD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 26: <enum GST_DVB_SERVICE_ADVANCED_CODEC_HD_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 27: <enum GST_DVB_SERVICE_ADVANCED_CODEC_HD_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 28: <enum GST_DVB_SERVICE_ADVANCED_CODEC_STEREO_HD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 29: <enum GST_DVB_SERVICE_ADVANCED_CODEC_STEREO_HD_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 30: <enum GST_DVB_SERVICE_ADVANCED_CODEC_STEREO_HD_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 31: <enum GST_DVB_SERVICE_RESERVED_FF of type GstMpegts.DVBServiceType>}, '__info__': gi.EnumInfo(DVBServiceType), 'RESERVED_00': <enum GST_DVB_SERVICE_RESERVED_00 of type GstMpegts.DVBServiceType>, 'DIGITAL_TELEVISION': <enum GST_DVB_SERVICE_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 'DIGITAL_RADIO_SOUND': <enum GST_DVB_SERVICE_DIGITAL_RADIO_SOUND of type GstMpegts.DVBServiceType>, 'TELETEXT': <enum GST_DVB_SERVICE_TELETEXT of type GstMpegts.DVBServiceType>, 'NVOD_REFERENCE': <enum GST_DVB_SERVICE_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 'NVOD_TIME_SHIFTED': <enum GST_DVB_SERVICE_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 'MOSAIC': <enum GST_DVB_SERVICE_MOSAIC of type GstMpegts.DVBServiceType>, 'FM_RADIO': <enum GST_DVB_SERVICE_FM_RADIO of type GstMpegts.DVBServiceType>, 'DVB_SRM': <enum GST_DVB_SERVICE_DVB_SRM of type GstMpegts.DVBServiceType>, 'RESERVED_09': <enum GST_DVB_SERVICE_RESERVED_09 of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_DIGITAL_RADIO_SOUND': <enum GST_DVB_SERVICE_ADVANCED_CODEC_DIGITAL_RADIO_SOUND of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_MOSAIC': <enum GST_DVB_SERVICE_ADVANCED_CODEC_MOSAIC of type GstMpegts.DVBServiceType>, 'DATA_BROADCAST': <enum GST_DVB_SERVICE_DATA_BROADCAST of type GstMpegts.DVBServiceType>, 'RESERVED_0D_COMMON_INTERFACE': <enum GST_DVB_SERVICE_RESERVED_0D_COMMON_INTERFACE of type GstMpegts.DVBServiceType>, 'RCS_MAP': <enum GST_DVB_SERVICE_RCS_MAP of type GstMpegts.DVBServiceType>, 'RCS_FLS': <enum GST_DVB_SERVICE_RCS_FLS of type GstMpegts.DVBServiceType>, 'DVB_MHP': <enum GST_DVB_SERVICE_DVB_MHP of type GstMpegts.DVBServiceType>, 'MPEG2_HD_DIGITAL_TELEVISION': <enum GST_DVB_SERVICE_MPEG2_HD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_SD_DIGITAL_TELEVISION': <enum GST_DVB_SERVICE_ADVANCED_CODEC_SD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_SD_NVOD_TIME_SHIFTED': <enum GST_DVB_SERVICE_ADVANCED_CODEC_SD_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_SD_NVOD_REFERENCE': <enum GST_DVB_SERVICE_ADVANCED_CODEC_SD_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_HD_DIGITAL_TELEVISION': <enum GST_DVB_SERVICE_ADVANCED_CODEC_HD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_HD_NVOD_TIME_SHIFTED': <enum GST_DVB_SERVICE_ADVANCED_CODEC_HD_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_HD_NVOD_REFERENCE': <enum GST_DVB_SERVICE_ADVANCED_CODEC_HD_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_STEREO_HD_DIGITAL_TELEVISION': <enum GST_DVB_SERVICE_ADVANCED_CODEC_STEREO_HD_DIGITAL_TELEVISION of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_STEREO_HD_NVOD_TIME_SHIFTED': <enum GST_DVB_SERVICE_ADVANCED_CODEC_STEREO_HD_NVOD_TIME_SHIFTED of type GstMpegts.DVBServiceType>, 'ADVANCED_CODEC_STEREO_HD_NVOD_REFERENCE': <enum GST_DVB_SERVICE_ADVANCED_CODEC_STEREO_HD_NVOD_REFERENCE of type GstMpegts.DVBServiceType>, 'RESERVED_FF': <enum GST_DVB_SERVICE_RESERVED_FF of type GstMpegts.DVBServiceType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsDVBServiceType (94624018591088)>'
    __info__ = gi.EnumInfo(DVBServiceType)


