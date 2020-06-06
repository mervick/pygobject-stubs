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


class DVBDescriptorType(__gobject.GEnum):
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


    AAC = 124
    AC3 = 106
    ADAPTATION_FIELD_DATA = 112
    ANCILLARY_DATA = 107
    ANNOUNCEMENT_SUPPORT = 110
    APPLICATION_SIGNALLING = 111
    BOUQUET_NAME = 71
    CABLE_DELIVERY_SYSTEM = 68
    CA_IDENTIFIER = 83
    CELL_FREQUENCY_LINK = 109
    CELL_LIST = 108
    COMPONENT = 80
    CONTENT = 84
    CONTENT_IDENTIFIER = 118
    COUNTRY_AVAILABILITY = 73
    DATA_BROADCAST = 100
    DATA_BROADCAST_ID = 102
    DEFAULT_AUTHORITY = 115
    DSNG = 104
    DTS = 123
    ECM_REPETITION_RATE = 120
    ENHANCED_AC3 = 122
    EXTENDED_EVENT = 78
    EXTENSION = 127
    FREQUENCY_LIST = 98
    FTA_CONTENT_MANAGEMENT = 126
    LINKAGE = 74
    LOCAL_TIME_OFFSET = 88
    MOSAIC = 81
    MULTILINGUAL_BOUQUET_NAME = 92
    MULTILINGUAL_COMPONENT = 94
    MULTILINGUAL_NETWORK_NAME = 91
    MULTILINGUAL_SERVICE_NAME = 93
    NETWORK_NAME = 64
    NVOD_REFERENCE = 75
    PARENTAL_RATING = 85
    PARTIAL_TRANSPORT_STREAM = 99
    PDC = 105
    PRIVATE_DATA_SPECIFIER = 95
    RELATED_CONTENT = 116
    S2_SATELLITE_DELIVERY_SYSTEM = 121
    SATELLITE_DELIVERY_SYSTEM = 67
    SCRAMBLING = 101
    SERVICE = 72
    SERVICE_AVAILABILITY = 114
    SERVICE_IDENTIFIER = 113
    SERVICE_LIST = 65
    SERVICE_MOVE = 96
    SHORT_EVENT = 77
    SHORT_SMOOTHING_BUFFER = 97
    STREAM_IDENTIFIER = 82
    STUFFING = 66
    SUBTITLING = 89
    TELEPHONE = 87
    TELETEXT = 86
    TERRESTRIAL_DELIVERY_SYSTEM = 90
    TIMESLICE_FEC_IDENTIFIER = 119
    TIME_SHIFTED_EVENT = 79
    TIME_SHIFTED_SERVICE = 76
    TRANSPORT_STREAM = 103
    TVA_ID = 117
    VBI_DATA = 69
    VBI_TELETEXT = 70
    XAIT_LOCATION = 125
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'DVBDescriptorType' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsDVBDescriptorType (94624018551376)>, '__enum_values__': {64: <enum GST_MTS_DESC_DVB_NETWORK_NAME of type GstMpegts.DVBDescriptorType>, 65: <enum GST_MTS_DESC_DVB_SERVICE_LIST of type GstMpegts.DVBDescriptorType>, 66: <enum GST_MTS_DESC_DVB_STUFFING of type GstMpegts.DVBDescriptorType>, 67: <enum GST_MTS_DESC_DVB_SATELLITE_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 68: <enum GST_MTS_DESC_DVB_CABLE_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 69: <enum GST_MTS_DESC_DVB_VBI_DATA of type GstMpegts.DVBDescriptorType>, 70: <enum GST_MTS_DESC_DVB_VBI_TELETEXT of type GstMpegts.DVBDescriptorType>, 71: <enum GST_MTS_DESC_DVB_BOUQUET_NAME of type GstMpegts.DVBDescriptorType>, 72: <enum GST_MTS_DESC_DVB_SERVICE of type GstMpegts.DVBDescriptorType>, 73: <enum GST_MTS_DESC_DVB_COUNTRY_AVAILABILITY of type GstMpegts.DVBDescriptorType>, 74: <enum GST_MTS_DESC_DVB_LINKAGE of type GstMpegts.DVBDescriptorType>, 75: <enum GST_MTS_DESC_DVB_NVOD_REFERENCE of type GstMpegts.DVBDescriptorType>, 76: <enum GST_MTS_DESC_DVB_TIME_SHIFTED_SERVICE of type GstMpegts.DVBDescriptorType>, 77: <enum GST_MTS_DESC_DVB_SHORT_EVENT of type GstMpegts.DVBDescriptorType>, 78: <enum GST_MTS_DESC_DVB_EXTENDED_EVENT of type GstMpegts.DVBDescriptorType>, 79: <enum GST_MTS_DESC_DVB_TIME_SHIFTED_EVENT of type GstMpegts.DVBDescriptorType>, 80: <enum GST_MTS_DESC_DVB_COMPONENT of type GstMpegts.DVBDescriptorType>, 81: <enum GST_MTS_DESC_DVB_MOSAIC of type GstMpegts.DVBDescriptorType>, 82: <enum GST_MTS_DESC_DVB_STREAM_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 83: <enum GST_MTS_DESC_DVB_CA_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 84: <enum GST_MTS_DESC_DVB_CONTENT of type GstMpegts.DVBDescriptorType>, 85: <enum GST_MTS_DESC_DVB_PARENTAL_RATING of type GstMpegts.DVBDescriptorType>, 86: <enum GST_MTS_DESC_DVB_TELETEXT of type GstMpegts.DVBDescriptorType>, 87: <enum GST_MTS_DESC_DVB_TELEPHONE of type GstMpegts.DVBDescriptorType>, 88: <enum GST_MTS_DESC_DVB_LOCAL_TIME_OFFSET of type GstMpegts.DVBDescriptorType>, 89: <enum GST_MTS_DESC_DVB_SUBTITLING of type GstMpegts.DVBDescriptorType>, 90: <enum GST_MTS_DESC_DVB_TERRESTRIAL_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 91: <enum GST_MTS_DESC_DVB_MULTILINGUAL_NETWORK_NAME of type GstMpegts.DVBDescriptorType>, 92: <enum GST_MTS_DESC_DVB_MULTILINGUAL_BOUQUET_NAME of type GstMpegts.DVBDescriptorType>, 93: <enum GST_MTS_DESC_DVB_MULTILINGUAL_SERVICE_NAME of type GstMpegts.DVBDescriptorType>, 94: <enum GST_MTS_DESC_DVB_MULTILINGUAL_COMPONENT of type GstMpegts.DVBDescriptorType>, 95: <enum GST_MTS_DESC_DVB_PRIVATE_DATA_SPECIFIER of type GstMpegts.DVBDescriptorType>, 96: <enum GST_MTS_DESC_DVB_SERVICE_MOVE of type GstMpegts.DVBDescriptorType>, 97: <enum GST_MTS_DESC_DVB_SHORT_SMOOTHING_BUFFER of type GstMpegts.DVBDescriptorType>, 98: <enum GST_MTS_DESC_DVB_FREQUENCY_LIST of type GstMpegts.DVBDescriptorType>, 99: <enum GST_MTS_DESC_DVB_PARTIAL_TRANSPORT_STREAM of type GstMpegts.DVBDescriptorType>, 100: <enum GST_MTS_DESC_DVB_DATA_BROADCAST of type GstMpegts.DVBDescriptorType>, 101: <enum GST_MTS_DESC_DVB_SCRAMBLING of type GstMpegts.DVBDescriptorType>, 102: <enum GST_MTS_DESC_DVB_DATA_BROADCAST_ID of type GstMpegts.DVBDescriptorType>, 103: <enum GST_MTS_DESC_DVB_TRANSPORT_STREAM of type GstMpegts.DVBDescriptorType>, 104: <enum GST_MTS_DESC_DVB_DSNG of type GstMpegts.DVBDescriptorType>, 105: <enum GST_MTS_DESC_DVB_PDC of type GstMpegts.DVBDescriptorType>, 106: <enum GST_MTS_DESC_DVB_AC3 of type GstMpegts.DVBDescriptorType>, 107: <enum GST_MTS_DESC_DVB_ANCILLARY_DATA of type GstMpegts.DVBDescriptorType>, 108: <enum GST_MTS_DESC_DVB_CELL_LIST of type GstMpegts.DVBDescriptorType>, 109: <enum GST_MTS_DESC_DVB_CELL_FREQUENCY_LINK of type GstMpegts.DVBDescriptorType>, 110: <enum GST_MTS_DESC_DVB_ANNOUNCEMENT_SUPPORT of type GstMpegts.DVBDescriptorType>, 111: <enum GST_MTS_DESC_DVB_APPLICATION_SIGNALLING of type GstMpegts.DVBDescriptorType>, 112: <enum GST_MTS_DESC_DVB_ADAPTATION_FIELD_DATA of type GstMpegts.DVBDescriptorType>, 113: <enum GST_MTS_DESC_DVB_SERVICE_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 114: <enum GST_MTS_DESC_DVB_SERVICE_AVAILABILITY of type GstMpegts.DVBDescriptorType>, 115: <enum GST_MTS_DESC_DVB_DEFAULT_AUTHORITY of type GstMpegts.DVBDescriptorType>, 116: <enum GST_MTS_DESC_DVB_RELATED_CONTENT of type GstMpegts.DVBDescriptorType>, 117: <enum GST_MTS_DESC_DVB_TVA_ID of type GstMpegts.DVBDescriptorType>, 118: <enum GST_MTS_DESC_DVB_CONTENT_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 119: <enum GST_MTS_DESC_DVB_TIMESLICE_FEC_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 120: <enum GST_MTS_DESC_DVB_ECM_REPETITION_RATE of type GstMpegts.DVBDescriptorType>, 121: <enum GST_MTS_DESC_DVB_S2_SATELLITE_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 122: <enum GST_MTS_DESC_DVB_ENHANCED_AC3 of type GstMpegts.DVBDescriptorType>, 123: <enum GST_MTS_DESC_DVB_DTS of type GstMpegts.DVBDescriptorType>, 124: <enum GST_MTS_DESC_DVB_AAC of type GstMpegts.DVBDescriptorType>, 125: <enum GST_MTS_DESC_DVB_XAIT_LOCATION of type GstMpegts.DVBDescriptorType>, 126: <enum GST_MTS_DESC_DVB_FTA_CONTENT_MANAGEMENT of type GstMpegts.DVBDescriptorType>, 127: <enum GST_MTS_DESC_DVB_EXTENSION of type GstMpegts.DVBDescriptorType>}, '__info__': gi.EnumInfo(DVBDescriptorType), 'NETWORK_NAME': <enum GST_MTS_DESC_DVB_NETWORK_NAME of type GstMpegts.DVBDescriptorType>, 'SERVICE_LIST': <enum GST_MTS_DESC_DVB_SERVICE_LIST of type GstMpegts.DVBDescriptorType>, 'STUFFING': <enum GST_MTS_DESC_DVB_STUFFING of type GstMpegts.DVBDescriptorType>, 'SATELLITE_DELIVERY_SYSTEM': <enum GST_MTS_DESC_DVB_SATELLITE_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 'CABLE_DELIVERY_SYSTEM': <enum GST_MTS_DESC_DVB_CABLE_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 'VBI_DATA': <enum GST_MTS_DESC_DVB_VBI_DATA of type GstMpegts.DVBDescriptorType>, 'VBI_TELETEXT': <enum GST_MTS_DESC_DVB_VBI_TELETEXT of type GstMpegts.DVBDescriptorType>, 'BOUQUET_NAME': <enum GST_MTS_DESC_DVB_BOUQUET_NAME of type GstMpegts.DVBDescriptorType>, 'SERVICE': <enum GST_MTS_DESC_DVB_SERVICE of type GstMpegts.DVBDescriptorType>, 'COUNTRY_AVAILABILITY': <enum GST_MTS_DESC_DVB_COUNTRY_AVAILABILITY of type GstMpegts.DVBDescriptorType>, 'LINKAGE': <enum GST_MTS_DESC_DVB_LINKAGE of type GstMpegts.DVBDescriptorType>, 'NVOD_REFERENCE': <enum GST_MTS_DESC_DVB_NVOD_REFERENCE of type GstMpegts.DVBDescriptorType>, 'TIME_SHIFTED_SERVICE': <enum GST_MTS_DESC_DVB_TIME_SHIFTED_SERVICE of type GstMpegts.DVBDescriptorType>, 'SHORT_EVENT': <enum GST_MTS_DESC_DVB_SHORT_EVENT of type GstMpegts.DVBDescriptorType>, 'EXTENDED_EVENT': <enum GST_MTS_DESC_DVB_EXTENDED_EVENT of type GstMpegts.DVBDescriptorType>, 'TIME_SHIFTED_EVENT': <enum GST_MTS_DESC_DVB_TIME_SHIFTED_EVENT of type GstMpegts.DVBDescriptorType>, 'COMPONENT': <enum GST_MTS_DESC_DVB_COMPONENT of type GstMpegts.DVBDescriptorType>, 'MOSAIC': <enum GST_MTS_DESC_DVB_MOSAIC of type GstMpegts.DVBDescriptorType>, 'STREAM_IDENTIFIER': <enum GST_MTS_DESC_DVB_STREAM_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 'CA_IDENTIFIER': <enum GST_MTS_DESC_DVB_CA_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 'CONTENT': <enum GST_MTS_DESC_DVB_CONTENT of type GstMpegts.DVBDescriptorType>, 'PARENTAL_RATING': <enum GST_MTS_DESC_DVB_PARENTAL_RATING of type GstMpegts.DVBDescriptorType>, 'TELETEXT': <enum GST_MTS_DESC_DVB_TELETEXT of type GstMpegts.DVBDescriptorType>, 'TELEPHONE': <enum GST_MTS_DESC_DVB_TELEPHONE of type GstMpegts.DVBDescriptorType>, 'LOCAL_TIME_OFFSET': <enum GST_MTS_DESC_DVB_LOCAL_TIME_OFFSET of type GstMpegts.DVBDescriptorType>, 'SUBTITLING': <enum GST_MTS_DESC_DVB_SUBTITLING of type GstMpegts.DVBDescriptorType>, 'TERRESTRIAL_DELIVERY_SYSTEM': <enum GST_MTS_DESC_DVB_TERRESTRIAL_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 'MULTILINGUAL_NETWORK_NAME': <enum GST_MTS_DESC_DVB_MULTILINGUAL_NETWORK_NAME of type GstMpegts.DVBDescriptorType>, 'MULTILINGUAL_BOUQUET_NAME': <enum GST_MTS_DESC_DVB_MULTILINGUAL_BOUQUET_NAME of type GstMpegts.DVBDescriptorType>, 'MULTILINGUAL_SERVICE_NAME': <enum GST_MTS_DESC_DVB_MULTILINGUAL_SERVICE_NAME of type GstMpegts.DVBDescriptorType>, 'MULTILINGUAL_COMPONENT': <enum GST_MTS_DESC_DVB_MULTILINGUAL_COMPONENT of type GstMpegts.DVBDescriptorType>, 'PRIVATE_DATA_SPECIFIER': <enum GST_MTS_DESC_DVB_PRIVATE_DATA_SPECIFIER of type GstMpegts.DVBDescriptorType>, 'SERVICE_MOVE': <enum GST_MTS_DESC_DVB_SERVICE_MOVE of type GstMpegts.DVBDescriptorType>, 'SHORT_SMOOTHING_BUFFER': <enum GST_MTS_DESC_DVB_SHORT_SMOOTHING_BUFFER of type GstMpegts.DVBDescriptorType>, 'FREQUENCY_LIST': <enum GST_MTS_DESC_DVB_FREQUENCY_LIST of type GstMpegts.DVBDescriptorType>, 'PARTIAL_TRANSPORT_STREAM': <enum GST_MTS_DESC_DVB_PARTIAL_TRANSPORT_STREAM of type GstMpegts.DVBDescriptorType>, 'DATA_BROADCAST': <enum GST_MTS_DESC_DVB_DATA_BROADCAST of type GstMpegts.DVBDescriptorType>, 'SCRAMBLING': <enum GST_MTS_DESC_DVB_SCRAMBLING of type GstMpegts.DVBDescriptorType>, 'DATA_BROADCAST_ID': <enum GST_MTS_DESC_DVB_DATA_BROADCAST_ID of type GstMpegts.DVBDescriptorType>, 'TRANSPORT_STREAM': <enum GST_MTS_DESC_DVB_TRANSPORT_STREAM of type GstMpegts.DVBDescriptorType>, 'DSNG': <enum GST_MTS_DESC_DVB_DSNG of type GstMpegts.DVBDescriptorType>, 'PDC': <enum GST_MTS_DESC_DVB_PDC of type GstMpegts.DVBDescriptorType>, 'AC3': <enum GST_MTS_DESC_DVB_AC3 of type GstMpegts.DVBDescriptorType>, 'ANCILLARY_DATA': <enum GST_MTS_DESC_DVB_ANCILLARY_DATA of type GstMpegts.DVBDescriptorType>, 'CELL_LIST': <enum GST_MTS_DESC_DVB_CELL_LIST of type GstMpegts.DVBDescriptorType>, 'CELL_FREQUENCY_LINK': <enum GST_MTS_DESC_DVB_CELL_FREQUENCY_LINK of type GstMpegts.DVBDescriptorType>, 'ANNOUNCEMENT_SUPPORT': <enum GST_MTS_DESC_DVB_ANNOUNCEMENT_SUPPORT of type GstMpegts.DVBDescriptorType>, 'APPLICATION_SIGNALLING': <enum GST_MTS_DESC_DVB_APPLICATION_SIGNALLING of type GstMpegts.DVBDescriptorType>, 'ADAPTATION_FIELD_DATA': <enum GST_MTS_DESC_DVB_ADAPTATION_FIELD_DATA of type GstMpegts.DVBDescriptorType>, 'SERVICE_IDENTIFIER': <enum GST_MTS_DESC_DVB_SERVICE_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 'SERVICE_AVAILABILITY': <enum GST_MTS_DESC_DVB_SERVICE_AVAILABILITY of type GstMpegts.DVBDescriptorType>, 'DEFAULT_AUTHORITY': <enum GST_MTS_DESC_DVB_DEFAULT_AUTHORITY of type GstMpegts.DVBDescriptorType>, 'RELATED_CONTENT': <enum GST_MTS_DESC_DVB_RELATED_CONTENT of type GstMpegts.DVBDescriptorType>, 'TVA_ID': <enum GST_MTS_DESC_DVB_TVA_ID of type GstMpegts.DVBDescriptorType>, 'CONTENT_IDENTIFIER': <enum GST_MTS_DESC_DVB_CONTENT_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 'TIMESLICE_FEC_IDENTIFIER': <enum GST_MTS_DESC_DVB_TIMESLICE_FEC_IDENTIFIER of type GstMpegts.DVBDescriptorType>, 'ECM_REPETITION_RATE': <enum GST_MTS_DESC_DVB_ECM_REPETITION_RATE of type GstMpegts.DVBDescriptorType>, 'S2_SATELLITE_DELIVERY_SYSTEM': <enum GST_MTS_DESC_DVB_S2_SATELLITE_DELIVERY_SYSTEM of type GstMpegts.DVBDescriptorType>, 'ENHANCED_AC3': <enum GST_MTS_DESC_DVB_ENHANCED_AC3 of type GstMpegts.DVBDescriptorType>, 'DTS': <enum GST_MTS_DESC_DVB_DTS of type GstMpegts.DVBDescriptorType>, 'AAC': <enum GST_MTS_DESC_DVB_AAC of type GstMpegts.DVBDescriptorType>, 'XAIT_LOCATION': <enum GST_MTS_DESC_DVB_XAIT_LOCATION of type GstMpegts.DVBDescriptorType>, 'FTA_CONTENT_MANAGEMENT': <enum GST_MTS_DESC_DVB_FTA_CONTENT_MANAGEMENT of type GstMpegts.DVBDescriptorType>, 'EXTENSION': <enum GST_MTS_DESC_DVB_EXTENSION of type GstMpegts.DVBDescriptorType>})"
    __enum_values__ = {
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
        86: 86,
        87: 87,
        88: 88,
        89: 89,
        90: 90,
        91: 91,
        92: 92,
        93: 93,
        94: 94,
        95: 95,
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        110: 110,
        111: 111,
        112: 112,
        113: 113,
        114: 114,
        115: 115,
        116: 116,
        117: 117,
        118: 118,
        119: 119,
        120: 120,
        121: 121,
        122: 122,
        123: 123,
        124: 124,
        125: 125,
        126: 126,
        127: 127,
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsDVBDescriptorType (94624018551376)>'
    __info__ = gi.EnumInfo(DVBDescriptorType)


