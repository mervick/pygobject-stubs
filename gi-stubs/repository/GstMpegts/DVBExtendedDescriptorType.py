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


class DVBExtendedDescriptorType(__gobject.GEnum):
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


    C2_DELIVERY_SYSTEM = 13
    CP = 2
    CPCM_DELIVERY_SIGNALLING = 1
    CP_IDENTIFIER = 3
    DTS_HD_AUDIO_STREAM = 14
    DTS_NEUTRAL = 15
    IMAGE_ICON = 0
    MESSAGE = 8
    NETWORK_CHANGE_NOTIFY = 7
    SERVICE_RELOCATED = 11
    SH_DELIVERY_SYSTEM = 5
    SUPPLEMENTARY_AUDIO = 6
    T2MI = 17
    T2_DELIVERY_SYSTEM = 4
    TARGET_REGION = 9
    TARGET_REGION_NAME = 10
    URI_LINKAGE = 19
    VIDEO_DEPTH_RANGE = 16
    XAIT_PID = 12
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'DVBExtendedDescriptorType' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsDVBExtendedDescriptorType (94624018567776)>, '__enum_values__': {0: <enum GST_MTS_DESC_EXT_DVB_IMAGE_ICON of type GstMpegts.DVBExtendedDescriptorType>, 1: <enum GST_MTS_DESC_EXT_DVB_CPCM_DELIVERY_SIGNALLING of type GstMpegts.DVBExtendedDescriptorType>, 2: <enum GST_MTS_DESC_EXT_DVB_CP of type GstMpegts.DVBExtendedDescriptorType>, 3: <enum GST_MTS_DESC_EXT_DVB_CP_IDENTIFIER of type GstMpegts.DVBExtendedDescriptorType>, 4: <enum GST_MTS_DESC_EXT_DVB_T2_DELIVERY_SYSTEM of type GstMpegts.DVBExtendedDescriptorType>, 5: <enum GST_MTS_DESC_EXT_DVB_SH_DELIVERY_SYSTEM of type GstMpegts.DVBExtendedDescriptorType>, 6: <enum GST_MTS_DESC_EXT_DVB_SUPPLEMENTARY_AUDIO of type GstMpegts.DVBExtendedDescriptorType>, 7: <enum GST_MTS_DESC_EXT_DVB_NETWORK_CHANGE_NOTIFY of type GstMpegts.DVBExtendedDescriptorType>, 8: <enum GST_MTS_DESC_EXT_DVB_MESSAGE of type GstMpegts.DVBExtendedDescriptorType>, 9: <enum GST_MTS_DESC_EXT_DVB_TARGET_REGION of type GstMpegts.DVBExtendedDescriptorType>, 10: <enum GST_MTS_DESC_EXT_DVB_TARGET_REGION_NAME of type GstMpegts.DVBExtendedDescriptorType>, 11: <enum GST_MTS_DESC_EXT_DVB_SERVICE_RELOCATED of type GstMpegts.DVBExtendedDescriptorType>, 12: <enum GST_MTS_DESC_EXT_DVB_XAIT_PID of type GstMpegts.DVBExtendedDescriptorType>, 13: <enum GST_MTS_DESC_EXT_DVB_C2_DELIVERY_SYSTEM of type GstMpegts.DVBExtendedDescriptorType>, 14: <enum GST_MTS_DESC_EXT_DVB_DTS_HD_AUDIO_STREAM of type GstMpegts.DVBExtendedDescriptorType>, 15: <enum GST_MTS_DESC_EXT_DVB_DTS_NEUTRAL of type GstMpegts.DVBExtendedDescriptorType>, 16: <enum GST_MTS_DESC_EXT_DVB_VIDEO_DEPTH_RANGE of type GstMpegts.DVBExtendedDescriptorType>, 17: <enum GST_MTS_DESC_EXT_DVB_T2MI of type GstMpegts.DVBExtendedDescriptorType>, 19: <enum GST_MTS_DESC_EXT_DVB_URI_LINKAGE of type GstMpegts.DVBExtendedDescriptorType>}, '__info__': gi.EnumInfo(DVBExtendedDescriptorType), 'IMAGE_ICON': <enum GST_MTS_DESC_EXT_DVB_IMAGE_ICON of type GstMpegts.DVBExtendedDescriptorType>, 'CPCM_DELIVERY_SIGNALLING': <enum GST_MTS_DESC_EXT_DVB_CPCM_DELIVERY_SIGNALLING of type GstMpegts.DVBExtendedDescriptorType>, 'CP': <enum GST_MTS_DESC_EXT_DVB_CP of type GstMpegts.DVBExtendedDescriptorType>, 'CP_IDENTIFIER': <enum GST_MTS_DESC_EXT_DVB_CP_IDENTIFIER of type GstMpegts.DVBExtendedDescriptorType>, 'T2_DELIVERY_SYSTEM': <enum GST_MTS_DESC_EXT_DVB_T2_DELIVERY_SYSTEM of type GstMpegts.DVBExtendedDescriptorType>, 'SH_DELIVERY_SYSTEM': <enum GST_MTS_DESC_EXT_DVB_SH_DELIVERY_SYSTEM of type GstMpegts.DVBExtendedDescriptorType>, 'SUPPLEMENTARY_AUDIO': <enum GST_MTS_DESC_EXT_DVB_SUPPLEMENTARY_AUDIO of type GstMpegts.DVBExtendedDescriptorType>, 'NETWORK_CHANGE_NOTIFY': <enum GST_MTS_DESC_EXT_DVB_NETWORK_CHANGE_NOTIFY of type GstMpegts.DVBExtendedDescriptorType>, 'MESSAGE': <enum GST_MTS_DESC_EXT_DVB_MESSAGE of type GstMpegts.DVBExtendedDescriptorType>, 'TARGET_REGION': <enum GST_MTS_DESC_EXT_DVB_TARGET_REGION of type GstMpegts.DVBExtendedDescriptorType>, 'TARGET_REGION_NAME': <enum GST_MTS_DESC_EXT_DVB_TARGET_REGION_NAME of type GstMpegts.DVBExtendedDescriptorType>, 'SERVICE_RELOCATED': <enum GST_MTS_DESC_EXT_DVB_SERVICE_RELOCATED of type GstMpegts.DVBExtendedDescriptorType>, 'XAIT_PID': <enum GST_MTS_DESC_EXT_DVB_XAIT_PID of type GstMpegts.DVBExtendedDescriptorType>, 'C2_DELIVERY_SYSTEM': <enum GST_MTS_DESC_EXT_DVB_C2_DELIVERY_SYSTEM of type GstMpegts.DVBExtendedDescriptorType>, 'DTS_HD_AUDIO_STREAM': <enum GST_MTS_DESC_EXT_DVB_DTS_HD_AUDIO_STREAM of type GstMpegts.DVBExtendedDescriptorType>, 'DTS_NEUTRAL': <enum GST_MTS_DESC_EXT_DVB_DTS_NEUTRAL of type GstMpegts.DVBExtendedDescriptorType>, 'VIDEO_DEPTH_RANGE': <enum GST_MTS_DESC_EXT_DVB_VIDEO_DEPTH_RANGE of type GstMpegts.DVBExtendedDescriptorType>, 'T2MI': <enum GST_MTS_DESC_EXT_DVB_T2MI of type GstMpegts.DVBExtendedDescriptorType>, 'URI_LINKAGE': <enum GST_MTS_DESC_EXT_DVB_URI_LINKAGE of type GstMpegts.DVBExtendedDescriptorType>})"
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
        19: 19,
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsDVBExtendedDescriptorType (94624018567776)>'
    __info__ = gi.EnumInfo(DVBExtendedDescriptorType)


