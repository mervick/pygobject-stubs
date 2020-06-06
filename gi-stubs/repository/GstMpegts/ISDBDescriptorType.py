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


class ISDBDescriptorType(__gobject.GEnum):
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


    AUDIO_COMPONENT = 196
    BASIC_LOCAL_EVENT = 208
    BOARD_INFORMATION = 219
    BROADCASTER_NAME = 216
    CA_CONTRACT_INFORMATION = 203
    CA_EMM_TS = 202
    CA_SERVICE = 204
    COMPONENT_GROUP = 217
    CONNECTED_TRANSMISSION = 221
    CONTENT_AVAILABILITY = 222
    DATA_CONTENT = 199
    DIGITAL_COPY_CONTROL = 193
    DOWNLOAD_CONTENT = 201
    EVENT_GROUP = 214
    EXTENDED_BROADCASTER = 206
    HIERARCHICAL_TRANSMISSION = 192
    HYPERLINK = 197
    LDT_LINKAGE = 220
    LOGO_TRANSMISSION = 207
    NETWORK_IDENTIFICATION = 194
    NODE_RELATION = 210
    PARTIAL_TS_TIME = 195
    REFERENCE = 209
    SERIES = 213
    SERVICE_GROUP = 224
    SHORT_NODE_INFORMATION = 211
    SI_PARAMETER = 215
    SI_PRIME_TS = 218
    STC_REFERENCE = 212
    TARGET_REGION = 198
    TS_INFORMATION = 205
    VIDEO_DECODE_CONTROL = 200
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'ISDBDescriptorType' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsISDBDescriptorType (94624018648816)>, '__enum_values__': {192: <enum GST_MTS_DESC_ISDB_HIERARCHICAL_TRANSMISSION of type GstMpegts.ISDBDescriptorType>, 193: <enum GST_MTS_DESC_ISDB_DIGITAL_COPY_CONTROL of type GstMpegts.ISDBDescriptorType>, 194: <enum GST_MTS_DESC_ISDB_NETWORK_IDENTIFICATION of type GstMpegts.ISDBDescriptorType>, 195: <enum GST_MTS_DESC_ISDB_PARTIAL_TS_TIME of type GstMpegts.ISDBDescriptorType>, 196: <enum GST_MTS_DESC_ISDB_AUDIO_COMPONENT of type GstMpegts.ISDBDescriptorType>, 197: <enum GST_MTS_DESC_ISDB_HYPERLINK of type GstMpegts.ISDBDescriptorType>, 198: <enum GST_MTS_DESC_ISDB_TARGET_REGION of type GstMpegts.ISDBDescriptorType>, 199: <enum GST_MTS_DESC_ISDB_DATA_CONTENT of type GstMpegts.ISDBDescriptorType>, 200: <enum GST_MTS_DESC_ISDB_VIDEO_DECODE_CONTROL of type GstMpegts.ISDBDescriptorType>, 201: <enum GST_MTS_DESC_ISDB_DOWNLOAD_CONTENT of type GstMpegts.ISDBDescriptorType>, 202: <enum GST_MTS_DESC_ISDB_CA_EMM_TS of type GstMpegts.ISDBDescriptorType>, 203: <enum GST_MTS_DESC_ISDB_CA_CONTRACT_INFORMATION of type GstMpegts.ISDBDescriptorType>, 204: <enum GST_MTS_DESC_ISDB_CA_SERVICE of type GstMpegts.ISDBDescriptorType>, 205: <enum GST_MTS_DESC_ISDB_TS_INFORMATION of type GstMpegts.ISDBDescriptorType>, 206: <enum GST_MTS_DESC_ISDB_EXTENDED_BROADCASTER of type GstMpegts.ISDBDescriptorType>, 207: <enum GST_MTS_DESC_ISDB_LOGO_TRANSMISSION of type GstMpegts.ISDBDescriptorType>, 208: <enum GST_MTS_DESC_ISDB_BASIC_LOCAL_EVENT of type GstMpegts.ISDBDescriptorType>, 209: <enum GST_MTS_DESC_ISDB_REFERENCE of type GstMpegts.ISDBDescriptorType>, 210: <enum GST_MTS_DESC_ISDB_NODE_RELATION of type GstMpegts.ISDBDescriptorType>, 211: <enum GST_MTS_DESC_ISDB_SHORT_NODE_INFORMATION of type GstMpegts.ISDBDescriptorType>, 212: <enum GST_MTS_DESC_ISDB_STC_REFERENCE of type GstMpegts.ISDBDescriptorType>, 213: <enum GST_MTS_DESC_ISDB_SERIES of type GstMpegts.ISDBDescriptorType>, 214: <enum GST_MTS_DESC_ISDB_EVENT_GROUP of type GstMpegts.ISDBDescriptorType>, 215: <enum GST_MTS_DESC_ISDB_SI_PARAMETER of type GstMpegts.ISDBDescriptorType>, 216: <enum GST_MTS_DESC_ISDB_BROADCASTER_NAME of type GstMpegts.ISDBDescriptorType>, 217: <enum GST_MTS_DESC_ISDB_COMPONENT_GROUP of type GstMpegts.ISDBDescriptorType>, 218: <enum GST_MTS_DESC_ISDB_SI_PRIME_TS of type GstMpegts.ISDBDescriptorType>, 219: <enum GST_MTS_DESC_ISDB_BOARD_INFORMATION of type GstMpegts.ISDBDescriptorType>, 220: <enum GST_MTS_DESC_ISDB_LDT_LINKAGE of type GstMpegts.ISDBDescriptorType>, 221: <enum GST_MTS_DESC_ISDB_CONNECTED_TRANSMISSION of type GstMpegts.ISDBDescriptorType>, 222: <enum GST_MTS_DESC_ISDB_CONTENT_AVAILABILITY of type GstMpegts.ISDBDescriptorType>, 224: <enum GST_MTS_DESC_ISDB_SERVICE_GROUP of type GstMpegts.ISDBDescriptorType>}, '__info__': gi.EnumInfo(ISDBDescriptorType), 'HIERARCHICAL_TRANSMISSION': <enum GST_MTS_DESC_ISDB_HIERARCHICAL_TRANSMISSION of type GstMpegts.ISDBDescriptorType>, 'DIGITAL_COPY_CONTROL': <enum GST_MTS_DESC_ISDB_DIGITAL_COPY_CONTROL of type GstMpegts.ISDBDescriptorType>, 'NETWORK_IDENTIFICATION': <enum GST_MTS_DESC_ISDB_NETWORK_IDENTIFICATION of type GstMpegts.ISDBDescriptorType>, 'PARTIAL_TS_TIME': <enum GST_MTS_DESC_ISDB_PARTIAL_TS_TIME of type GstMpegts.ISDBDescriptorType>, 'AUDIO_COMPONENT': <enum GST_MTS_DESC_ISDB_AUDIO_COMPONENT of type GstMpegts.ISDBDescriptorType>, 'HYPERLINK': <enum GST_MTS_DESC_ISDB_HYPERLINK of type GstMpegts.ISDBDescriptorType>, 'TARGET_REGION': <enum GST_MTS_DESC_ISDB_TARGET_REGION of type GstMpegts.ISDBDescriptorType>, 'DATA_CONTENT': <enum GST_MTS_DESC_ISDB_DATA_CONTENT of type GstMpegts.ISDBDescriptorType>, 'VIDEO_DECODE_CONTROL': <enum GST_MTS_DESC_ISDB_VIDEO_DECODE_CONTROL of type GstMpegts.ISDBDescriptorType>, 'DOWNLOAD_CONTENT': <enum GST_MTS_DESC_ISDB_DOWNLOAD_CONTENT of type GstMpegts.ISDBDescriptorType>, 'CA_EMM_TS': <enum GST_MTS_DESC_ISDB_CA_EMM_TS of type GstMpegts.ISDBDescriptorType>, 'CA_CONTRACT_INFORMATION': <enum GST_MTS_DESC_ISDB_CA_CONTRACT_INFORMATION of type GstMpegts.ISDBDescriptorType>, 'CA_SERVICE': <enum GST_MTS_DESC_ISDB_CA_SERVICE of type GstMpegts.ISDBDescriptorType>, 'TS_INFORMATION': <enum GST_MTS_DESC_ISDB_TS_INFORMATION of type GstMpegts.ISDBDescriptorType>, 'EXTENDED_BROADCASTER': <enum GST_MTS_DESC_ISDB_EXTENDED_BROADCASTER of type GstMpegts.ISDBDescriptorType>, 'LOGO_TRANSMISSION': <enum GST_MTS_DESC_ISDB_LOGO_TRANSMISSION of type GstMpegts.ISDBDescriptorType>, 'BASIC_LOCAL_EVENT': <enum GST_MTS_DESC_ISDB_BASIC_LOCAL_EVENT of type GstMpegts.ISDBDescriptorType>, 'REFERENCE': <enum GST_MTS_DESC_ISDB_REFERENCE of type GstMpegts.ISDBDescriptorType>, 'NODE_RELATION': <enum GST_MTS_DESC_ISDB_NODE_RELATION of type GstMpegts.ISDBDescriptorType>, 'SHORT_NODE_INFORMATION': <enum GST_MTS_DESC_ISDB_SHORT_NODE_INFORMATION of type GstMpegts.ISDBDescriptorType>, 'STC_REFERENCE': <enum GST_MTS_DESC_ISDB_STC_REFERENCE of type GstMpegts.ISDBDescriptorType>, 'SERIES': <enum GST_MTS_DESC_ISDB_SERIES of type GstMpegts.ISDBDescriptorType>, 'EVENT_GROUP': <enum GST_MTS_DESC_ISDB_EVENT_GROUP of type GstMpegts.ISDBDescriptorType>, 'SI_PARAMETER': <enum GST_MTS_DESC_ISDB_SI_PARAMETER of type GstMpegts.ISDBDescriptorType>, 'BROADCASTER_NAME': <enum GST_MTS_DESC_ISDB_BROADCASTER_NAME of type GstMpegts.ISDBDescriptorType>, 'COMPONENT_GROUP': <enum GST_MTS_DESC_ISDB_COMPONENT_GROUP of type GstMpegts.ISDBDescriptorType>, 'SI_PRIME_TS': <enum GST_MTS_DESC_ISDB_SI_PRIME_TS of type GstMpegts.ISDBDescriptorType>, 'BOARD_INFORMATION': <enum GST_MTS_DESC_ISDB_BOARD_INFORMATION of type GstMpegts.ISDBDescriptorType>, 'LDT_LINKAGE': <enum GST_MTS_DESC_ISDB_LDT_LINKAGE of type GstMpegts.ISDBDescriptorType>, 'CONNECTED_TRANSMISSION': <enum GST_MTS_DESC_ISDB_CONNECTED_TRANSMISSION of type GstMpegts.ISDBDescriptorType>, 'CONTENT_AVAILABILITY': <enum GST_MTS_DESC_ISDB_CONTENT_AVAILABILITY of type GstMpegts.ISDBDescriptorType>, 'SERVICE_GROUP': <enum GST_MTS_DESC_ISDB_SERVICE_GROUP of type GstMpegts.ISDBDescriptorType>})"
    __enum_values__ = {
        192: 192,
        193: 193,
        194: 194,
        195: 195,
        196: 196,
        197: 197,
        198: 198,
        199: 199,
        200: 200,
        201: 201,
        202: 202,
        203: 203,
        204: 204,
        205: 205,
        206: 206,
        207: 207,
        208: 208,
        209: 209,
        210: 210,
        211: 211,
        212: 212,
        213: 213,
        214: 214,
        215: 215,
        216: 216,
        217: 217,
        218: 218,
        219: 219,
        220: 220,
        221: 221,
        222: 222,
        224: 224,
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsISDBDescriptorType (94624018648816)>'
    __info__ = gi.EnumInfo(ISDBDescriptorType)


