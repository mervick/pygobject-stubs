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


class ATSCDescriptorType(__gobject.GEnum):
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


    AC3 = 131
    CAPTION_SERVICE = 134
    COMPONENT_NAME = 163
    CONTENT_ADVISORY = 135
    CRC32 = 181
    DATA_SERVICE = 164
    DCC_ARRIVING_REQUEST = 169
    DCC_DEPARTING_REQUEST = 168
    DOWNLOAD_DESCRIPTOR = 166
    EAC3 = 204
    ENHANCED_SIGNALING = 178
    EXTENDED_CHANNEL_NAME = 160
    GENRE = 171
    GROUP_LINK = 184
    MODULE_LINK = 180
    MULTIPROTOCOL_ENCAPSULATION = 167
    PID_COUNT = 165
    PRIVATE_INFORMATION = 173
    REDISTRIBUTION_CONTROL = 170
    SERVICE_LOCATION = 161
    STUFFING = 128
    TIME_SHIFTED_SERVICE = 162
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'ATSCDescriptorType' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsATSCDescriptorType (94624018128976)>, '__enum_values__': {128: <enum GST_MTS_DESC_ATSC_STUFFING of type GstMpegts.ATSCDescriptorType>, 131: <enum GST_MTS_DESC_ATSC_AC3 of type GstMpegts.ATSCDescriptorType>, 134: <enum GST_MTS_DESC_ATSC_CAPTION_SERVICE of type GstMpegts.ATSCDescriptorType>, 135: <enum GST_MTS_DESC_ATSC_CONTENT_ADVISORY of type GstMpegts.ATSCDescriptorType>, 160: <enum GST_MTS_DESC_ATSC_EXTENDED_CHANNEL_NAME of type GstMpegts.ATSCDescriptorType>, 161: <enum GST_MTS_DESC_ATSC_SERVICE_LOCATION of type GstMpegts.ATSCDescriptorType>, 162: <enum GST_MTS_DESC_ATSC_TIME_SHIFTED_SERVICE of type GstMpegts.ATSCDescriptorType>, 163: <enum GST_MTS_DESC_ATSC_COMPONENT_NAME of type GstMpegts.ATSCDescriptorType>, 168: <enum GST_MTS_DESC_ATSC_DCC_DEPARTING_REQUEST of type GstMpegts.ATSCDescriptorType>, 169: <enum GST_MTS_DESC_ATSC_DCC_ARRIVING_REQUEST of type GstMpegts.ATSCDescriptorType>, 170: <enum GST_MTS_DESC_ATSC_REDISTRIBUTION_CONTROL of type GstMpegts.ATSCDescriptorType>, 171: <enum GST_MTS_DESC_ATSC_GENRE of type GstMpegts.ATSCDescriptorType>, 173: <enum GST_MTS_DESC_ATSC_PRIVATE_INFORMATION of type GstMpegts.ATSCDescriptorType>, 204: <enum GST_MTS_DESC_ATSC_EAC3 of type GstMpegts.ATSCDescriptorType>, 178: <enum GST_MTS_DESC_ATSC_ENHANCED_SIGNALING of type GstMpegts.ATSCDescriptorType>, 164: <enum GST_MTS_DESC_ATSC_DATA_SERVICE of type GstMpegts.ATSCDescriptorType>, 165: <enum GST_MTS_DESC_ATSC_PID_COUNT of type GstMpegts.ATSCDescriptorType>, 166: <enum GST_MTS_DESC_ATSC_DOWNLOAD_DESCRIPTOR of type GstMpegts.ATSCDescriptorType>, 167: <enum GST_MTS_DESC_ATSC_MULTIPROTOCOL_ENCAPSULATION of type GstMpegts.ATSCDescriptorType>, 180: <enum GST_MTS_DESC_ATSC_MODULE_LINK of type GstMpegts.ATSCDescriptorType>, 181: <enum GST_MTS_DESC_ATSC_CRC32 of type GstMpegts.ATSCDescriptorType>, 184: <enum GST_MTS_DESC_ATSC_GROUP_LINK of type GstMpegts.ATSCDescriptorType>}, '__info__': gi.EnumInfo(ATSCDescriptorType), 'STUFFING': <enum GST_MTS_DESC_ATSC_STUFFING of type GstMpegts.ATSCDescriptorType>, 'AC3': <enum GST_MTS_DESC_ATSC_AC3 of type GstMpegts.ATSCDescriptorType>, 'CAPTION_SERVICE': <enum GST_MTS_DESC_ATSC_CAPTION_SERVICE of type GstMpegts.ATSCDescriptorType>, 'CONTENT_ADVISORY': <enum GST_MTS_DESC_ATSC_CONTENT_ADVISORY of type GstMpegts.ATSCDescriptorType>, 'EXTENDED_CHANNEL_NAME': <enum GST_MTS_DESC_ATSC_EXTENDED_CHANNEL_NAME of type GstMpegts.ATSCDescriptorType>, 'SERVICE_LOCATION': <enum GST_MTS_DESC_ATSC_SERVICE_LOCATION of type GstMpegts.ATSCDescriptorType>, 'TIME_SHIFTED_SERVICE': <enum GST_MTS_DESC_ATSC_TIME_SHIFTED_SERVICE of type GstMpegts.ATSCDescriptorType>, 'COMPONENT_NAME': <enum GST_MTS_DESC_ATSC_COMPONENT_NAME of type GstMpegts.ATSCDescriptorType>, 'DCC_DEPARTING_REQUEST': <enum GST_MTS_DESC_ATSC_DCC_DEPARTING_REQUEST of type GstMpegts.ATSCDescriptorType>, 'DCC_ARRIVING_REQUEST': <enum GST_MTS_DESC_ATSC_DCC_ARRIVING_REQUEST of type GstMpegts.ATSCDescriptorType>, 'REDISTRIBUTION_CONTROL': <enum GST_MTS_DESC_ATSC_REDISTRIBUTION_CONTROL of type GstMpegts.ATSCDescriptorType>, 'GENRE': <enum GST_MTS_DESC_ATSC_GENRE of type GstMpegts.ATSCDescriptorType>, 'PRIVATE_INFORMATION': <enum GST_MTS_DESC_ATSC_PRIVATE_INFORMATION of type GstMpegts.ATSCDescriptorType>, 'EAC3': <enum GST_MTS_DESC_ATSC_EAC3 of type GstMpegts.ATSCDescriptorType>, 'ENHANCED_SIGNALING': <enum GST_MTS_DESC_ATSC_ENHANCED_SIGNALING of type GstMpegts.ATSCDescriptorType>, 'DATA_SERVICE': <enum GST_MTS_DESC_ATSC_DATA_SERVICE of type GstMpegts.ATSCDescriptorType>, 'PID_COUNT': <enum GST_MTS_DESC_ATSC_PID_COUNT of type GstMpegts.ATSCDescriptorType>, 'DOWNLOAD_DESCRIPTOR': <enum GST_MTS_DESC_ATSC_DOWNLOAD_DESCRIPTOR of type GstMpegts.ATSCDescriptorType>, 'MULTIPROTOCOL_ENCAPSULATION': <enum GST_MTS_DESC_ATSC_MULTIPROTOCOL_ENCAPSULATION of type GstMpegts.ATSCDescriptorType>, 'MODULE_LINK': <enum GST_MTS_DESC_ATSC_MODULE_LINK of type GstMpegts.ATSCDescriptorType>, 'CRC32': <enum GST_MTS_DESC_ATSC_CRC32 of type GstMpegts.ATSCDescriptorType>, 'GROUP_LINK': <enum GST_MTS_DESC_ATSC_GROUP_LINK of type GstMpegts.ATSCDescriptorType>})"
    __enum_values__ = {
        128: 128,
        131: 131,
        134: 134,
        135: 135,
        160: 160,
        161: 161,
        162: 162,
        163: 163,
        164: 164,
        165: 165,
        166: 166,
        167: 167,
        168: 168,
        169: 169,
        170: 170,
        171: 171,
        173: 173,
        178: 178,
        180: 180,
        181: 181,
        184: 184,
        204: 204,
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsATSCDescriptorType (94624018128976)>'
    __info__ = gi.EnumInfo(ATSCDescriptorType)


