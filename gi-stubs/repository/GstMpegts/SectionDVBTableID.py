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


class SectionDVBTableID(__gobject.GEnum):
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


    APPLICATION_INFORMATION_TABLE = 116
    BOUQUET_ASSOCIATION = 74
    CA_MESSAGE_ECM_0 = 128
    CA_MESSAGE_ECM_1 = 129
    CA_MESSAGE_SYSTEM_PRIVATE_1 = 130
    CA_MESSAGE_SYSTEM_PRIVATE_N = 143
    CMT = 164
    CONTAINER = 117
    CONTENT_IDENTIFIER = 119
    DISCONTINUITY_INFORMATION = 126
    EVENT_INFORMATION_ACTUAL_TS_PRESENT = 78
    EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_1 = 80
    EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_N = 95
    EVENT_INFORMATION_OTHER_TS_PRESENT = 79
    EVENT_INFORMATION_OTHER_TS_SCHEDULE_1 = 96
    EVENT_INFORMATION_OTHER_TS_SCHEDULE_N = 111
    FCT = 161
    LL_FEC_PARITY_DATA_TABLE = 177
    MPE_FEC = 120
    MPE_IFEC = 122
    NETWORK_INFORMATION_ACTUAL_NETWORK = 64
    NETWORK_INFORMATION_OTHER_NETWORK = 65
    PCR_PACKET_PAYLOAD = 166
    RELATED_CONTENT = 118
    RESOLUTION_NOTIFICATION = 121
    RUNNING_STATUS = 113
    SCT = 160
    SELECTION_INFORMATION = 127
    SERVICE_DESCRIPTION_ACTUAL_TS = 66
    SERVICE_DESCRIPTION_OTHER_TS = 70
    SPT = 163
    STUFFING = 114
    TBTP = 165
    TCT = 162
    TIM = 176
    TIME_DATE = 112
    TIME_OFFSET = 115
    TRANSMISSION_MODE_SUPPORT_PAYLOAD = 170
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'SectionDVBTableID' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsSectionDVBTableID (94624018730304)>, '__enum_values__': {64: <enum GST_MTS_TABLE_ID_NETWORK_INFORMATION_ACTUAL_NETWORK of type GstMpegts.SectionDVBTableID>, 65: <enum GST_MTS_TABLE_ID_NETWORK_INFORMATION_OTHER_NETWORK of type GstMpegts.SectionDVBTableID>, 66: <enum GST_MTS_TABLE_ID_SERVICE_DESCRIPTION_ACTUAL_TS of type GstMpegts.SectionDVBTableID>, 70: <enum GST_MTS_TABLE_ID_SERVICE_DESCRIPTION_OTHER_TS of type GstMpegts.SectionDVBTableID>, 74: <enum GST_MTS_TABLE_ID_BOUQUET_ASSOCIATION of type GstMpegts.SectionDVBTableID>, 78: <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_ACTUAL_TS_PRESENT of type GstMpegts.SectionDVBTableID>, 79: <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_OTHER_TS_PRESENT of type GstMpegts.SectionDVBTableID>, 80: <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_1 of type GstMpegts.SectionDVBTableID>, 95: <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_N of type GstMpegts.SectionDVBTableID>, 96: <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_OTHER_TS_SCHEDULE_1 of type GstMpegts.SectionDVBTableID>, 111: <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_OTHER_TS_SCHEDULE_N of type GstMpegts.SectionDVBTableID>, 112: <enum GST_MTS_TABLE_ID_TIME_DATE of type GstMpegts.SectionDVBTableID>, 113: <enum GST_MTS_TABLE_ID_RUNNING_STATUS of type GstMpegts.SectionDVBTableID>, 114: <enum GST_MTS_TABLE_ID_STUFFING of type GstMpegts.SectionDVBTableID>, 115: <enum GST_MTS_TABLE_ID_TIME_OFFSET of type GstMpegts.SectionDVBTableID>, 116: <enum GST_MTS_TABLE_ID_APPLICATION_INFORMATION_TABLE of type GstMpegts.SectionDVBTableID>, 117: <enum GST_MTS_TABLE_ID_CONTAINER of type GstMpegts.SectionDVBTableID>, 118: <enum GST_MTS_TABLE_ID_RELATED_CONTENT of type GstMpegts.SectionDVBTableID>, 119: <enum GST_MTS_TABLE_ID_CONTENT_IDENTIFIER of type GstMpegts.SectionDVBTableID>, 120: <enum GST_MTS_TABLE_ID_MPE_FEC of type GstMpegts.SectionDVBTableID>, 121: <enum GST_MTS_TABLE_ID_RESOLUTION_NOTIFICATION of type GstMpegts.SectionDVBTableID>, 122: <enum GST_MTS_TABLE_ID_MPE_IFEC of type GstMpegts.SectionDVBTableID>, 126: <enum GST_MTS_TABLE_ID_DISCONTINUITY_INFORMATION of type GstMpegts.SectionDVBTableID>, 127: <enum GST_MTS_TABLE_ID_SELECTION_INFORMATION of type GstMpegts.SectionDVBTableID>, 128: <enum GST_MTS_TABLE_ID_CA_MESSAGE_ECM_0 of type GstMpegts.SectionDVBTableID>, 129: <enum GST_MTS_TABLE_ID_CA_MESSAGE_ECM_1 of type GstMpegts.SectionDVBTableID>, 130: <enum GST_MTS_TABLE_ID_CA_MESSAGE_SYSTEM_PRIVATE_1 of type GstMpegts.SectionDVBTableID>, 143: <enum GST_MTS_TABLE_ID_CA_MESSAGE_SYSTEM_PRIVATE_N of type GstMpegts.SectionDVBTableID>, 160: <enum GST_MTS_TABLE_ID_SCT of type GstMpegts.SectionDVBTableID>, 161: <enum GST_MTS_TABLE_ID_FCT of type GstMpegts.SectionDVBTableID>, 162: <enum GST_MTS_TABLE_ID_TCT of type GstMpegts.SectionDVBTableID>, 163: <enum GST_MTS_TABLE_ID_SPT of type GstMpegts.SectionDVBTableID>, 164: <enum GST_MTS_TABLE_ID_CMT of type GstMpegts.SectionDVBTableID>, 165: <enum GST_MTS_TABLE_ID_TBTP of type GstMpegts.SectionDVBTableID>, 166: <enum GST_MTS_TABLE_ID_PCR_PACKET_PAYLOAD of type GstMpegts.SectionDVBTableID>, 170: <enum GST_MTS_TABLE_ID_TRANSMISSION_MODE_SUPPORT_PAYLOAD of type GstMpegts.SectionDVBTableID>, 176: <enum GST_MTS_TABLE_ID_TIM of type GstMpegts.SectionDVBTableID>, 177: <enum GST_MTS_TABLE_ID_LL_FEC_PARITY_DATA_TABLE of type GstMpegts.SectionDVBTableID>}, '__info__': gi.EnumInfo(SectionDVBTableID), 'NETWORK_INFORMATION_ACTUAL_NETWORK': <enum GST_MTS_TABLE_ID_NETWORK_INFORMATION_ACTUAL_NETWORK of type GstMpegts.SectionDVBTableID>, 'NETWORK_INFORMATION_OTHER_NETWORK': <enum GST_MTS_TABLE_ID_NETWORK_INFORMATION_OTHER_NETWORK of type GstMpegts.SectionDVBTableID>, 'SERVICE_DESCRIPTION_ACTUAL_TS': <enum GST_MTS_TABLE_ID_SERVICE_DESCRIPTION_ACTUAL_TS of type GstMpegts.SectionDVBTableID>, 'SERVICE_DESCRIPTION_OTHER_TS': <enum GST_MTS_TABLE_ID_SERVICE_DESCRIPTION_OTHER_TS of type GstMpegts.SectionDVBTableID>, 'BOUQUET_ASSOCIATION': <enum GST_MTS_TABLE_ID_BOUQUET_ASSOCIATION of type GstMpegts.SectionDVBTableID>, 'EVENT_INFORMATION_ACTUAL_TS_PRESENT': <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_ACTUAL_TS_PRESENT of type GstMpegts.SectionDVBTableID>, 'EVENT_INFORMATION_OTHER_TS_PRESENT': <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_OTHER_TS_PRESENT of type GstMpegts.SectionDVBTableID>, 'EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_1': <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_1 of type GstMpegts.SectionDVBTableID>, 'EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_N': <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_N of type GstMpegts.SectionDVBTableID>, 'EVENT_INFORMATION_OTHER_TS_SCHEDULE_1': <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_OTHER_TS_SCHEDULE_1 of type GstMpegts.SectionDVBTableID>, 'EVENT_INFORMATION_OTHER_TS_SCHEDULE_N': <enum GST_MTS_TABLE_ID_EVENT_INFORMATION_OTHER_TS_SCHEDULE_N of type GstMpegts.SectionDVBTableID>, 'TIME_DATE': <enum GST_MTS_TABLE_ID_TIME_DATE of type GstMpegts.SectionDVBTableID>, 'RUNNING_STATUS': <enum GST_MTS_TABLE_ID_RUNNING_STATUS of type GstMpegts.SectionDVBTableID>, 'STUFFING': <enum GST_MTS_TABLE_ID_STUFFING of type GstMpegts.SectionDVBTableID>, 'TIME_OFFSET': <enum GST_MTS_TABLE_ID_TIME_OFFSET of type GstMpegts.SectionDVBTableID>, 'APPLICATION_INFORMATION_TABLE': <enum GST_MTS_TABLE_ID_APPLICATION_INFORMATION_TABLE of type GstMpegts.SectionDVBTableID>, 'CONTAINER': <enum GST_MTS_TABLE_ID_CONTAINER of type GstMpegts.SectionDVBTableID>, 'RELATED_CONTENT': <enum GST_MTS_TABLE_ID_RELATED_CONTENT of type GstMpegts.SectionDVBTableID>, 'CONTENT_IDENTIFIER': <enum GST_MTS_TABLE_ID_CONTENT_IDENTIFIER of type GstMpegts.SectionDVBTableID>, 'MPE_FEC': <enum GST_MTS_TABLE_ID_MPE_FEC of type GstMpegts.SectionDVBTableID>, 'RESOLUTION_NOTIFICATION': <enum GST_MTS_TABLE_ID_RESOLUTION_NOTIFICATION of type GstMpegts.SectionDVBTableID>, 'MPE_IFEC': <enum GST_MTS_TABLE_ID_MPE_IFEC of type GstMpegts.SectionDVBTableID>, 'DISCONTINUITY_INFORMATION': <enum GST_MTS_TABLE_ID_DISCONTINUITY_INFORMATION of type GstMpegts.SectionDVBTableID>, 'SELECTION_INFORMATION': <enum GST_MTS_TABLE_ID_SELECTION_INFORMATION of type GstMpegts.SectionDVBTableID>, 'CA_MESSAGE_ECM_0': <enum GST_MTS_TABLE_ID_CA_MESSAGE_ECM_0 of type GstMpegts.SectionDVBTableID>, 'CA_MESSAGE_ECM_1': <enum GST_MTS_TABLE_ID_CA_MESSAGE_ECM_1 of type GstMpegts.SectionDVBTableID>, 'CA_MESSAGE_SYSTEM_PRIVATE_1': <enum GST_MTS_TABLE_ID_CA_MESSAGE_SYSTEM_PRIVATE_1 of type GstMpegts.SectionDVBTableID>, 'CA_MESSAGE_SYSTEM_PRIVATE_N': <enum GST_MTS_TABLE_ID_CA_MESSAGE_SYSTEM_PRIVATE_N of type GstMpegts.SectionDVBTableID>, 'SCT': <enum GST_MTS_TABLE_ID_SCT of type GstMpegts.SectionDVBTableID>, 'FCT': <enum GST_MTS_TABLE_ID_FCT of type GstMpegts.SectionDVBTableID>, 'TCT': <enum GST_MTS_TABLE_ID_TCT of type GstMpegts.SectionDVBTableID>, 'SPT': <enum GST_MTS_TABLE_ID_SPT of type GstMpegts.SectionDVBTableID>, 'CMT': <enum GST_MTS_TABLE_ID_CMT of type GstMpegts.SectionDVBTableID>, 'TBTP': <enum GST_MTS_TABLE_ID_TBTP of type GstMpegts.SectionDVBTableID>, 'PCR_PACKET_PAYLOAD': <enum GST_MTS_TABLE_ID_PCR_PACKET_PAYLOAD of type GstMpegts.SectionDVBTableID>, 'TRANSMISSION_MODE_SUPPORT_PAYLOAD': <enum GST_MTS_TABLE_ID_TRANSMISSION_MODE_SUPPORT_PAYLOAD of type GstMpegts.SectionDVBTableID>, 'TIM': <enum GST_MTS_TABLE_ID_TIM of type GstMpegts.SectionDVBTableID>, 'LL_FEC_PARITY_DATA_TABLE': <enum GST_MTS_TABLE_ID_LL_FEC_PARITY_DATA_TABLE of type GstMpegts.SectionDVBTableID>})"
    __enum_values__ = {
        64: 64,
        65: 65,
        66: 66,
        70: 70,
        74: 74,
        78: 78,
        79: 79,
        80: 80,
        95: 95,
        96: 96,
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
        126: 126,
        127: 127,
        128: 128,
        129: 129,
        130: 130,
        143: 143,
        160: 160,
        161: 161,
        162: 162,
        163: 163,
        164: 164,
        165: 165,
        166: 166,
        170: 170,
        176: 176,
        177: 177,
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsSectionDVBTableID (94624018730304)>'
    __info__ = gi.EnumInfo(SectionDVBTableID)


