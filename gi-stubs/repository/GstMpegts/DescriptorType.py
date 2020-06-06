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


class DescriptorType(__gobject.GEnum):
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


    AUDIO_STREAM = 3
    AUXILIARY_VIDEO_STREAM = 47
    AVC_TIMING_AND_HRD = 42
    AVC_VIDEO = 40
    CA = 9
    CONTENT_LABELING = 36
    COPYRIGHT = 13
    DATA_STREAM_ALIGNMENT = 6
    DSMCC_ASSOCIATION_TAG = 20
    DSMCC_CAROUSEL_IDENTIFIER = 19
    DSMCC_DEFERRED_ASSOCIATION_TAG = 21
    DSMCC_NPT_ENDPOINT = 24
    DSMCC_NPT_REFERENCE = 23
    DSMCC_STREAM_EVENT = 26
    DSMCC_STREAM_MODE = 25
    EXTERNAL_ES_ID = 32
    FLEX_MUX_TIMING = 44
    FMC = 31
    FMX_BUFFER_SIZE = 34
    HIERARCHY = 4
    IBP = 18
    IOD = 29
    IPMP = 41
    ISO_639_LANGUAGE = 10
    J2K_VIDEO = 50
    MAXIMUM_BITRATE = 14
    METADATA = 38
    METADATA_POINTER = 37
    METADATA_STD = 39
    MPEG2_AAC_AUDIO = 43
    MPEG2_STEREOSCOPIC_VIDEO_FORMAT = 52
    MPEG4_AUDIO = 28
    MPEG4_AUDIO_EXTENSION = 46
    MPEG4_TEXT = 45
    MPEG4_VIDEO = 27
    MULTIPLEX_BUFFER = 35
    MULTIPLEX_BUFFER_UTILISATION = 12
    MUX_CODE = 33
    MVC_EXTENSION = 49
    MVC_OPERATION_POINT = 51
    PRIVATE_DATA_INDICATOR = 15
    REGISTRATION = 5
    RESERVED_00 = 0
    RESERVED_01 = 1
    SL = 30
    SMOOTHING_BUFFER = 16
    STD = 17
    STEREOSCOPIC_PROGRAM_INFO = 53
    STEREOSCOPIC_VIDEO_INFO = 54
    SVC_EXTENSION = 48
    SYSTEM_CLOCK = 11
    TARGET_BACKGROUND_GRID = 7
    VIDEO_STREAM = 2
    VIDEO_WINDOW = 8
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'DescriptorType' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsDescriptorType (94624018625824)>, '__enum_values__': {0: <enum GST_MTS_DESC_RESERVED_00 of type GstMpegts.DescriptorType>, 1: <enum GST_MTS_DESC_RESERVED_01 of type GstMpegts.DescriptorType>, 2: <enum GST_MTS_DESC_VIDEO_STREAM of type GstMpegts.DescriptorType>, 3: <enum GST_MTS_DESC_AUDIO_STREAM of type GstMpegts.DescriptorType>, 4: <enum GST_MTS_DESC_HIERARCHY of type GstMpegts.DescriptorType>, 5: <enum GST_MTS_DESC_REGISTRATION of type GstMpegts.DescriptorType>, 6: <enum GST_MTS_DESC_DATA_STREAM_ALIGNMENT of type GstMpegts.DescriptorType>, 7: <enum GST_MTS_DESC_TARGET_BACKGROUND_GRID of type GstMpegts.DescriptorType>, 8: <enum GST_MTS_DESC_VIDEO_WINDOW of type GstMpegts.DescriptorType>, 9: <enum GST_MTS_DESC_CA of type GstMpegts.DescriptorType>, 10: <enum GST_MTS_DESC_ISO_639_LANGUAGE of type GstMpegts.DescriptorType>, 11: <enum GST_MTS_DESC_SYSTEM_CLOCK of type GstMpegts.DescriptorType>, 12: <enum GST_MTS_DESC_MULTIPLEX_BUFFER_UTILISATION of type GstMpegts.DescriptorType>, 13: <enum GST_MTS_DESC_COPYRIGHT of type GstMpegts.DescriptorType>, 14: <enum GST_MTS_DESC_MAXIMUM_BITRATE of type GstMpegts.DescriptorType>, 15: <enum GST_MTS_DESC_PRIVATE_DATA_INDICATOR of type GstMpegts.DescriptorType>, 16: <enum GST_MTS_DESC_SMOOTHING_BUFFER of type GstMpegts.DescriptorType>, 17: <enum GST_MTS_DESC_STD of type GstMpegts.DescriptorType>, 18: <enum GST_MTS_DESC_IBP of type GstMpegts.DescriptorType>, 19: <enum GST_MTS_DESC_DSMCC_CAROUSEL_IDENTIFIER of type GstMpegts.DescriptorType>, 20: <enum GST_MTS_DESC_DSMCC_ASSOCIATION_TAG of type GstMpegts.DescriptorType>, 21: <enum GST_MTS_DESC_DSMCC_DEFERRED_ASSOCIATION_TAG of type GstMpegts.DescriptorType>, 23: <enum GST_MTS_DESC_DSMCC_NPT_REFERENCE of type GstMpegts.DescriptorType>, 24: <enum GST_MTS_DESC_DSMCC_NPT_ENDPOINT of type GstMpegts.DescriptorType>, 25: <enum GST_MTS_DESC_DSMCC_STREAM_MODE of type GstMpegts.DescriptorType>, 26: <enum GST_MTS_DESC_DSMCC_STREAM_EVENT of type GstMpegts.DescriptorType>, 27: <enum GST_MTS_DESC_MPEG4_VIDEO of type GstMpegts.DescriptorType>, 28: <enum GST_MTS_DESC_MPEG4_AUDIO of type GstMpegts.DescriptorType>, 29: <enum GST_MTS_DESC_IOD of type GstMpegts.DescriptorType>, 30: <enum GST_MTS_DESC_SL of type GstMpegts.DescriptorType>, 31: <enum GST_MTS_DESC_FMC of type GstMpegts.DescriptorType>, 32: <enum GST_MTS_DESC_EXTERNAL_ES_ID of type GstMpegts.DescriptorType>, 33: <enum GST_MTS_DESC_MUX_CODE of type GstMpegts.DescriptorType>, 34: <enum GST_MTS_DESC_FMX_BUFFER_SIZE of type GstMpegts.DescriptorType>, 35: <enum GST_MTS_DESC_MULTIPLEX_BUFFER of type GstMpegts.DescriptorType>, 36: <enum GST_MTS_DESC_CONTENT_LABELING of type GstMpegts.DescriptorType>, 37: <enum GST_MTS_DESC_METADATA_POINTER of type GstMpegts.DescriptorType>, 38: <enum GST_MTS_DESC_METADATA of type GstMpegts.DescriptorType>, 39: <enum GST_MTS_DESC_METADATA_STD of type GstMpegts.DescriptorType>, 40: <enum GST_MTS_DESC_AVC_VIDEO of type GstMpegts.DescriptorType>, 41: <enum GST_MTS_DESC_IPMP of type GstMpegts.DescriptorType>, 42: <enum GST_MTS_DESC_AVC_TIMING_AND_HRD of type GstMpegts.DescriptorType>, 43: <enum GST_MTS_DESC_MPEG2_AAC_AUDIO of type GstMpegts.DescriptorType>, 44: <enum GST_MTS_DESC_FLEX_MUX_TIMING of type GstMpegts.DescriptorType>, 45: <enum GST_MTS_DESC_MPEG4_TEXT of type GstMpegts.DescriptorType>, 46: <enum GST_MTS_DESC_MPEG4_AUDIO_EXTENSION of type GstMpegts.DescriptorType>, 47: <enum GST_MTS_DESC_AUXILIARY_VIDEO_STREAM of type GstMpegts.DescriptorType>, 48: <enum GST_MTS_DESC_SVC_EXTENSION of type GstMpegts.DescriptorType>, 49: <enum GST_MTS_DESC_MVC_EXTENSION of type GstMpegts.DescriptorType>, 50: <enum GST_MTS_DESC_J2K_VIDEO of type GstMpegts.DescriptorType>, 51: <enum GST_MTS_DESC_MVC_OPERATION_POINT of type GstMpegts.DescriptorType>, 52: <enum GST_MTS_DESC_MPEG2_STEREOSCOPIC_VIDEO_FORMAT of type GstMpegts.DescriptorType>, 53: <enum GST_MTS_DESC_STEREOSCOPIC_PROGRAM_INFO of type GstMpegts.DescriptorType>, 54: <enum GST_MTS_DESC_STEREOSCOPIC_VIDEO_INFO of type GstMpegts.DescriptorType>}, '__info__': gi.EnumInfo(DescriptorType), 'RESERVED_00': <enum GST_MTS_DESC_RESERVED_00 of type GstMpegts.DescriptorType>, 'RESERVED_01': <enum GST_MTS_DESC_RESERVED_01 of type GstMpegts.DescriptorType>, 'VIDEO_STREAM': <enum GST_MTS_DESC_VIDEO_STREAM of type GstMpegts.DescriptorType>, 'AUDIO_STREAM': <enum GST_MTS_DESC_AUDIO_STREAM of type GstMpegts.DescriptorType>, 'HIERARCHY': <enum GST_MTS_DESC_HIERARCHY of type GstMpegts.DescriptorType>, 'REGISTRATION': <enum GST_MTS_DESC_REGISTRATION of type GstMpegts.DescriptorType>, 'DATA_STREAM_ALIGNMENT': <enum GST_MTS_DESC_DATA_STREAM_ALIGNMENT of type GstMpegts.DescriptorType>, 'TARGET_BACKGROUND_GRID': <enum GST_MTS_DESC_TARGET_BACKGROUND_GRID of type GstMpegts.DescriptorType>, 'VIDEO_WINDOW': <enum GST_MTS_DESC_VIDEO_WINDOW of type GstMpegts.DescriptorType>, 'CA': <enum GST_MTS_DESC_CA of type GstMpegts.DescriptorType>, 'ISO_639_LANGUAGE': <enum GST_MTS_DESC_ISO_639_LANGUAGE of type GstMpegts.DescriptorType>, 'SYSTEM_CLOCK': <enum GST_MTS_DESC_SYSTEM_CLOCK of type GstMpegts.DescriptorType>, 'MULTIPLEX_BUFFER_UTILISATION': <enum GST_MTS_DESC_MULTIPLEX_BUFFER_UTILISATION of type GstMpegts.DescriptorType>, 'COPYRIGHT': <enum GST_MTS_DESC_COPYRIGHT of type GstMpegts.DescriptorType>, 'MAXIMUM_BITRATE': <enum GST_MTS_DESC_MAXIMUM_BITRATE of type GstMpegts.DescriptorType>, 'PRIVATE_DATA_INDICATOR': <enum GST_MTS_DESC_PRIVATE_DATA_INDICATOR of type GstMpegts.DescriptorType>, 'SMOOTHING_BUFFER': <enum GST_MTS_DESC_SMOOTHING_BUFFER of type GstMpegts.DescriptorType>, 'STD': <enum GST_MTS_DESC_STD of type GstMpegts.DescriptorType>, 'IBP': <enum GST_MTS_DESC_IBP of type GstMpegts.DescriptorType>, 'DSMCC_CAROUSEL_IDENTIFIER': <enum GST_MTS_DESC_DSMCC_CAROUSEL_IDENTIFIER of type GstMpegts.DescriptorType>, 'DSMCC_ASSOCIATION_TAG': <enum GST_MTS_DESC_DSMCC_ASSOCIATION_TAG of type GstMpegts.DescriptorType>, 'DSMCC_DEFERRED_ASSOCIATION_TAG': <enum GST_MTS_DESC_DSMCC_DEFERRED_ASSOCIATION_TAG of type GstMpegts.DescriptorType>, 'DSMCC_NPT_REFERENCE': <enum GST_MTS_DESC_DSMCC_NPT_REFERENCE of type GstMpegts.DescriptorType>, 'DSMCC_NPT_ENDPOINT': <enum GST_MTS_DESC_DSMCC_NPT_ENDPOINT of type GstMpegts.DescriptorType>, 'DSMCC_STREAM_MODE': <enum GST_MTS_DESC_DSMCC_STREAM_MODE of type GstMpegts.DescriptorType>, 'DSMCC_STREAM_EVENT': <enum GST_MTS_DESC_DSMCC_STREAM_EVENT of type GstMpegts.DescriptorType>, 'MPEG4_VIDEO': <enum GST_MTS_DESC_MPEG4_VIDEO of type GstMpegts.DescriptorType>, 'MPEG4_AUDIO': <enum GST_MTS_DESC_MPEG4_AUDIO of type GstMpegts.DescriptorType>, 'IOD': <enum GST_MTS_DESC_IOD of type GstMpegts.DescriptorType>, 'SL': <enum GST_MTS_DESC_SL of type GstMpegts.DescriptorType>, 'FMC': <enum GST_MTS_DESC_FMC of type GstMpegts.DescriptorType>, 'EXTERNAL_ES_ID': <enum GST_MTS_DESC_EXTERNAL_ES_ID of type GstMpegts.DescriptorType>, 'MUX_CODE': <enum GST_MTS_DESC_MUX_CODE of type GstMpegts.DescriptorType>, 'FMX_BUFFER_SIZE': <enum GST_MTS_DESC_FMX_BUFFER_SIZE of type GstMpegts.DescriptorType>, 'MULTIPLEX_BUFFER': <enum GST_MTS_DESC_MULTIPLEX_BUFFER of type GstMpegts.DescriptorType>, 'CONTENT_LABELING': <enum GST_MTS_DESC_CONTENT_LABELING of type GstMpegts.DescriptorType>, 'METADATA_POINTER': <enum GST_MTS_DESC_METADATA_POINTER of type GstMpegts.DescriptorType>, 'METADATA': <enum GST_MTS_DESC_METADATA of type GstMpegts.DescriptorType>, 'METADATA_STD': <enum GST_MTS_DESC_METADATA_STD of type GstMpegts.DescriptorType>, 'AVC_VIDEO': <enum GST_MTS_DESC_AVC_VIDEO of type GstMpegts.DescriptorType>, 'IPMP': <enum GST_MTS_DESC_IPMP of type GstMpegts.DescriptorType>, 'AVC_TIMING_AND_HRD': <enum GST_MTS_DESC_AVC_TIMING_AND_HRD of type GstMpegts.DescriptorType>, 'MPEG2_AAC_AUDIO': <enum GST_MTS_DESC_MPEG2_AAC_AUDIO of type GstMpegts.DescriptorType>, 'FLEX_MUX_TIMING': <enum GST_MTS_DESC_FLEX_MUX_TIMING of type GstMpegts.DescriptorType>, 'MPEG4_TEXT': <enum GST_MTS_DESC_MPEG4_TEXT of type GstMpegts.DescriptorType>, 'MPEG4_AUDIO_EXTENSION': <enum GST_MTS_DESC_MPEG4_AUDIO_EXTENSION of type GstMpegts.DescriptorType>, 'AUXILIARY_VIDEO_STREAM': <enum GST_MTS_DESC_AUXILIARY_VIDEO_STREAM of type GstMpegts.DescriptorType>, 'SVC_EXTENSION': <enum GST_MTS_DESC_SVC_EXTENSION of type GstMpegts.DescriptorType>, 'MVC_EXTENSION': <enum GST_MTS_DESC_MVC_EXTENSION of type GstMpegts.DescriptorType>, 'J2K_VIDEO': <enum GST_MTS_DESC_J2K_VIDEO of type GstMpegts.DescriptorType>, 'MVC_OPERATION_POINT': <enum GST_MTS_DESC_MVC_OPERATION_POINT of type GstMpegts.DescriptorType>, 'MPEG2_STEREOSCOPIC_VIDEO_FORMAT': <enum GST_MTS_DESC_MPEG2_STEREOSCOPIC_VIDEO_FORMAT of type GstMpegts.DescriptorType>, 'STEREOSCOPIC_PROGRAM_INFO': <enum GST_MTS_DESC_STEREOSCOPIC_PROGRAM_INFO of type GstMpegts.DescriptorType>, 'STEREOSCOPIC_VIDEO_INFO': <enum GST_MTS_DESC_STEREOSCOPIC_VIDEO_INFO of type GstMpegts.DescriptorType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsDescriptorType (94624018625824)>'
    __info__ = gi.EnumInfo(DescriptorType)


