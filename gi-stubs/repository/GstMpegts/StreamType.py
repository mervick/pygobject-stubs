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


class StreamType(__gobject.GEnum):
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


    AUDIO_AAC_ADTS = 15
    AUDIO_AAC_CLEAN = 28
    AUDIO_AAC_LATM = 17
    AUDIO_MPEG1 = 3
    AUDIO_MPEG2 = 4
    AUXILIARY = 14
    DSMCC_A = 10
    DSMCC_B = 11
    DSMCC_C = 12
    DSMCC_D = 13
    DSM_CC = 8
    H_222_1 = 9
    IPMP_STREAM = 127
    METADATA_DATA_CAROUSEL = 23
    METADATA_OBJECT_CAROUSEL = 24
    METADATA_PES_PACKETS = 21
    METADATA_SECTIONS = 22
    METADATA_SYNCHRONIZED_DOWNLOAD = 25
    MHEG = 7
    MPEG2_IPMP = 26
    MPEG4_TIMED_TEXT = 29
    PRIVATE_PES_PACKETS = 6
    PRIVATE_SECTIONS = 5
    RESERVED_00 = 0
    SL_FLEXMUX_PES_PACKETS = 18
    SL_FLEXMUX_SECTIONS = 19
    SYNCHRONIZED_DOWNLOAD = 20
    VIDEO_H264 = 27
    VIDEO_H264_MVC_SUB_BITSTREAM = 32
    VIDEO_H264_STEREO_ADDITIONAL_VIEW = 35
    VIDEO_H264_SVC_SUB_BITSTREAM = 31
    VIDEO_HEVC = 36
    VIDEO_JP2K = 33
    VIDEO_MPEG1 = 1
    VIDEO_MPEG2 = 2
    VIDEO_MPEG2_STEREO_ADDITIONAL_VIEW = 34
    VIDEO_MPEG4 = 16
    VIDEO_RVC = 30
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'StreamType' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsStreamType (94624018751024)>, '__enum_values__': {0: <enum GST_MPEGTS_STREAM_TYPE_RESERVED_00 of type GstMpegts.StreamType>, 1: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG1 of type GstMpegts.StreamType>, 2: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG2 of type GstMpegts.StreamType>, 3: <enum GST_MPEGTS_STREAM_TYPE_AUDIO_MPEG1 of type GstMpegts.StreamType>, 4: <enum GST_MPEGTS_STREAM_TYPE_AUDIO_MPEG2 of type GstMpegts.StreamType>, 5: <enum GST_MPEGTS_STREAM_TYPE_PRIVATE_SECTIONS of type GstMpegts.StreamType>, 6: <enum GST_MPEGTS_STREAM_TYPE_PRIVATE_PES_PACKETS of type GstMpegts.StreamType>, 7: <enum GST_MPEGTS_STREAM_TYPE_MHEG of type GstMpegts.StreamType>, 8: <enum GST_MPEGTS_STREAM_TYPE_DSM_CC of type GstMpegts.StreamType>, 9: <enum GST_MPEGTS_STREAM_TYPE_H_222_1 of type GstMpegts.StreamType>, 10: <enum GST_MPEGTS_STREAM_TYPE_DSMCC_A of type GstMpegts.StreamType>, 11: <enum GST_MPEGTS_STREAM_TYPE_DSMCC_B of type GstMpegts.StreamType>, 12: <enum GST_MPEGTS_STREAM_TYPE_DSMCC_C of type GstMpegts.StreamType>, 13: <enum GST_MPEGTS_STREAM_TYPE_DSMCC_D of type GstMpegts.StreamType>, 14: <enum GST_MPEGTS_STREAM_TYPE_AUXILIARY of type GstMpegts.StreamType>, 15: <enum GST_MPEGTS_STREAM_TYPE_AUDIO_AAC_ADTS of type GstMpegts.StreamType>, 16: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG4 of type GstMpegts.StreamType>, 17: <enum GST_MPEGTS_STREAM_TYPE_AUDIO_AAC_LATM of type GstMpegts.StreamType>, 18: <enum GST_MPEGTS_STREAM_TYPE_SL_FLEXMUX_PES_PACKETS of type GstMpegts.StreamType>, 19: <enum GST_MPEGTS_STREAM_TYPE_SL_FLEXMUX_SECTIONS of type GstMpegts.StreamType>, 20: <enum GST_MPEGTS_STREAM_TYPE_SYNCHRONIZED_DOWNLOAD of type GstMpegts.StreamType>, 21: <enum GST_MPEGTS_STREAM_TYPE_METADATA_PES_PACKETS of type GstMpegts.StreamType>, 22: <enum GST_MPEGTS_STREAM_TYPE_METADATA_SECTIONS of type GstMpegts.StreamType>, 23: <enum GST_MPEGTS_STREAM_TYPE_METADATA_DATA_CAROUSEL of type GstMpegts.StreamType>, 24: <enum GST_MPEGTS_STREAM_TYPE_METADATA_OBJECT_CAROUSEL of type GstMpegts.StreamType>, 25: <enum GST_MPEGTS_STREAM_TYPE_METADATA_SYNCHRONIZED_DOWNLOAD of type GstMpegts.StreamType>, 26: <enum GST_MPEGTS_STREAM_TYPE_MPEG2_IPMP of type GstMpegts.StreamType>, 27: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264 of type GstMpegts.StreamType>, 28: <enum GST_MPEGTS_STREAM_TYPE_AUDIO_AAC_CLEAN of type GstMpegts.StreamType>, 29: <enum GST_MPEGTS_STREAM_TYPE_MPEG4_TIMED_TEXT of type GstMpegts.StreamType>, 30: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_RVC of type GstMpegts.StreamType>, 31: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264_SVC_SUB_BITSTREAM of type GstMpegts.StreamType>, 32: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264_MVC_SUB_BITSTREAM of type GstMpegts.StreamType>, 33: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_JP2K of type GstMpegts.StreamType>, 34: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG2_STEREO_ADDITIONAL_VIEW of type GstMpegts.StreamType>, 35: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264_STEREO_ADDITIONAL_VIEW of type GstMpegts.StreamType>, 36: <enum GST_MPEGTS_STREAM_TYPE_VIDEO_HEVC of type GstMpegts.StreamType>, 127: <enum GST_MPEGTS_STREAM_TYPE_IPMP_STREAM of type GstMpegts.StreamType>}, '__info__': gi.EnumInfo(StreamType), 'RESERVED_00': <enum GST_MPEGTS_STREAM_TYPE_RESERVED_00 of type GstMpegts.StreamType>, 'VIDEO_MPEG1': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG1 of type GstMpegts.StreamType>, 'VIDEO_MPEG2': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG2 of type GstMpegts.StreamType>, 'AUDIO_MPEG1': <enum GST_MPEGTS_STREAM_TYPE_AUDIO_MPEG1 of type GstMpegts.StreamType>, 'AUDIO_MPEG2': <enum GST_MPEGTS_STREAM_TYPE_AUDIO_MPEG2 of type GstMpegts.StreamType>, 'PRIVATE_SECTIONS': <enum GST_MPEGTS_STREAM_TYPE_PRIVATE_SECTIONS of type GstMpegts.StreamType>, 'PRIVATE_PES_PACKETS': <enum GST_MPEGTS_STREAM_TYPE_PRIVATE_PES_PACKETS of type GstMpegts.StreamType>, 'MHEG': <enum GST_MPEGTS_STREAM_TYPE_MHEG of type GstMpegts.StreamType>, 'DSM_CC': <enum GST_MPEGTS_STREAM_TYPE_DSM_CC of type GstMpegts.StreamType>, 'H_222_1': <enum GST_MPEGTS_STREAM_TYPE_H_222_1 of type GstMpegts.StreamType>, 'DSMCC_A': <enum GST_MPEGTS_STREAM_TYPE_DSMCC_A of type GstMpegts.StreamType>, 'DSMCC_B': <enum GST_MPEGTS_STREAM_TYPE_DSMCC_B of type GstMpegts.StreamType>, 'DSMCC_C': <enum GST_MPEGTS_STREAM_TYPE_DSMCC_C of type GstMpegts.StreamType>, 'DSMCC_D': <enum GST_MPEGTS_STREAM_TYPE_DSMCC_D of type GstMpegts.StreamType>, 'AUXILIARY': <enum GST_MPEGTS_STREAM_TYPE_AUXILIARY of type GstMpegts.StreamType>, 'AUDIO_AAC_ADTS': <enum GST_MPEGTS_STREAM_TYPE_AUDIO_AAC_ADTS of type GstMpegts.StreamType>, 'VIDEO_MPEG4': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG4 of type GstMpegts.StreamType>, 'AUDIO_AAC_LATM': <enum GST_MPEGTS_STREAM_TYPE_AUDIO_AAC_LATM of type GstMpegts.StreamType>, 'SL_FLEXMUX_PES_PACKETS': <enum GST_MPEGTS_STREAM_TYPE_SL_FLEXMUX_PES_PACKETS of type GstMpegts.StreamType>, 'SL_FLEXMUX_SECTIONS': <enum GST_MPEGTS_STREAM_TYPE_SL_FLEXMUX_SECTIONS of type GstMpegts.StreamType>, 'SYNCHRONIZED_DOWNLOAD': <enum GST_MPEGTS_STREAM_TYPE_SYNCHRONIZED_DOWNLOAD of type GstMpegts.StreamType>, 'METADATA_PES_PACKETS': <enum GST_MPEGTS_STREAM_TYPE_METADATA_PES_PACKETS of type GstMpegts.StreamType>, 'METADATA_SECTIONS': <enum GST_MPEGTS_STREAM_TYPE_METADATA_SECTIONS of type GstMpegts.StreamType>, 'METADATA_DATA_CAROUSEL': <enum GST_MPEGTS_STREAM_TYPE_METADATA_DATA_CAROUSEL of type GstMpegts.StreamType>, 'METADATA_OBJECT_CAROUSEL': <enum GST_MPEGTS_STREAM_TYPE_METADATA_OBJECT_CAROUSEL of type GstMpegts.StreamType>, 'METADATA_SYNCHRONIZED_DOWNLOAD': <enum GST_MPEGTS_STREAM_TYPE_METADATA_SYNCHRONIZED_DOWNLOAD of type GstMpegts.StreamType>, 'MPEG2_IPMP': <enum GST_MPEGTS_STREAM_TYPE_MPEG2_IPMP of type GstMpegts.StreamType>, 'VIDEO_H264': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264 of type GstMpegts.StreamType>, 'AUDIO_AAC_CLEAN': <enum GST_MPEGTS_STREAM_TYPE_AUDIO_AAC_CLEAN of type GstMpegts.StreamType>, 'MPEG4_TIMED_TEXT': <enum GST_MPEGTS_STREAM_TYPE_MPEG4_TIMED_TEXT of type GstMpegts.StreamType>, 'VIDEO_RVC': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_RVC of type GstMpegts.StreamType>, 'VIDEO_H264_SVC_SUB_BITSTREAM': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264_SVC_SUB_BITSTREAM of type GstMpegts.StreamType>, 'VIDEO_H264_MVC_SUB_BITSTREAM': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264_MVC_SUB_BITSTREAM of type GstMpegts.StreamType>, 'VIDEO_JP2K': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_JP2K of type GstMpegts.StreamType>, 'VIDEO_MPEG2_STEREO_ADDITIONAL_VIEW': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_MPEG2_STEREO_ADDITIONAL_VIEW of type GstMpegts.StreamType>, 'VIDEO_H264_STEREO_ADDITIONAL_VIEW': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_H264_STEREO_ADDITIONAL_VIEW of type GstMpegts.StreamType>, 'VIDEO_HEVC': <enum GST_MPEGTS_STREAM_TYPE_VIDEO_HEVC of type GstMpegts.StreamType>, 'IPMP_STREAM': <enum GST_MPEGTS_STREAM_TYPE_IPMP_STREAM of type GstMpegts.StreamType>})"
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
        127: 127,
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsStreamType (94624018751024)>'
    __info__ = gi.EnumInfo(StreamType)


