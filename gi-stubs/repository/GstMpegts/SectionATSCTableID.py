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


class SectionATSCTableID(__gobject.GEnum):
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


    AGGREGATE_DATA_EVENT = 217
    AGGREGATE_EVENT_INFORMATION = 214
    AGGREGATE_EXTENDED_TEXT = 215
    CABLE_VIRTUAL_CHANNEL = 201
    CHANNEL_OR_EVENT_EXTENDED_TEXT = 204
    DATA_EVENT = 206
    DATA_SERVICE = 207
    DIRECTED_CHANNEL_CHANGE = 211
    DIRECTED_CHANNEL_CHANGE_SECTION_CODE = 212
    EVENT_INFORMATION = 203
    LONG_TERM_SERVICE = 210
    MASTER_GUIDE = 199
    NETWORK_RESOURCE = 209
    RATING_REGION = 202
    SATELLITE_VIRTUAL_CHANNEL = 218
    SYSTEM_TIME = 205
    TERRESTRIAL_VIRTUAL_CHANNEL = 200
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstMpegts', '__dict__': <attribute '__dict__' of 'SectionATSCTableID' objects>, '__doc__': None, '__gtype__': <GType PyGstMpegtsSectionATSCTableID (94624018722928)>, '__enum_values__': {199: <enum GST_MTS_TABLE_ID_ATSC_MASTER_GUIDE of type GstMpegts.SectionATSCTableID>, 200: <enum GST_MTS_TABLE_ID_ATSC_TERRESTRIAL_VIRTUAL_CHANNEL of type GstMpegts.SectionATSCTableID>, 201: <enum GST_MTS_TABLE_ID_ATSC_CABLE_VIRTUAL_CHANNEL of type GstMpegts.SectionATSCTableID>, 202: <enum GST_MTS_TABLE_ID_ATSC_RATING_REGION of type GstMpegts.SectionATSCTableID>, 203: <enum GST_MTS_TABLE_ID_ATSC_EVENT_INFORMATION of type GstMpegts.SectionATSCTableID>, 204: <enum GST_MTS_TABLE_ID_ATSC_CHANNEL_OR_EVENT_EXTENDED_TEXT of type GstMpegts.SectionATSCTableID>, 205: <enum GST_MTS_TABLE_ID_ATSC_SYSTEM_TIME of type GstMpegts.SectionATSCTableID>, 206: <enum GST_MTS_TABLE_ID_ATSC_DATA_EVENT of type GstMpegts.SectionATSCTableID>, 207: <enum GST_MTS_TABLE_ID_ATSC_DATA_SERVICE of type GstMpegts.SectionATSCTableID>, 209: <enum GST_MTS_TABLE_ID_ATSC_NETWORK_RESOURCE of type GstMpegts.SectionATSCTableID>, 210: <enum GST_MTS_TABLE_ID_ATSC_LONG_TERM_SERVICE of type GstMpegts.SectionATSCTableID>, 211: <enum GST_MTS_TABLE_ID_ATSC_DIRECTED_CHANNEL_CHANGE of type GstMpegts.SectionATSCTableID>, 212: <enum GST_MTS_TABLE_ID_ATSC_DIRECTED_CHANNEL_CHANGE_SECTION_CODE of type GstMpegts.SectionATSCTableID>, 214: <enum GST_MTS_TABLE_ID_ATSC_AGGREGATE_EVENT_INFORMATION of type GstMpegts.SectionATSCTableID>, 215: <enum GST_MTS_TABLE_ID_ATSC_AGGREGATE_EXTENDED_TEXT of type GstMpegts.SectionATSCTableID>, 217: <enum GST_MTS_TABLE_ID_ATSC_AGGREGATE_DATA_EVENT of type GstMpegts.SectionATSCTableID>, 218: <enum GST_MTS_TABLE_ID_ATSC_SATELLITE_VIRTUAL_CHANNEL of type GstMpegts.SectionATSCTableID>}, '__info__': gi.EnumInfo(SectionATSCTableID), 'MASTER_GUIDE': <enum GST_MTS_TABLE_ID_ATSC_MASTER_GUIDE of type GstMpegts.SectionATSCTableID>, 'TERRESTRIAL_VIRTUAL_CHANNEL': <enum GST_MTS_TABLE_ID_ATSC_TERRESTRIAL_VIRTUAL_CHANNEL of type GstMpegts.SectionATSCTableID>, 'CABLE_VIRTUAL_CHANNEL': <enum GST_MTS_TABLE_ID_ATSC_CABLE_VIRTUAL_CHANNEL of type GstMpegts.SectionATSCTableID>, 'RATING_REGION': <enum GST_MTS_TABLE_ID_ATSC_RATING_REGION of type GstMpegts.SectionATSCTableID>, 'EVENT_INFORMATION': <enum GST_MTS_TABLE_ID_ATSC_EVENT_INFORMATION of type GstMpegts.SectionATSCTableID>, 'CHANNEL_OR_EVENT_EXTENDED_TEXT': <enum GST_MTS_TABLE_ID_ATSC_CHANNEL_OR_EVENT_EXTENDED_TEXT of type GstMpegts.SectionATSCTableID>, 'SYSTEM_TIME': <enum GST_MTS_TABLE_ID_ATSC_SYSTEM_TIME of type GstMpegts.SectionATSCTableID>, 'DATA_EVENT': <enum GST_MTS_TABLE_ID_ATSC_DATA_EVENT of type GstMpegts.SectionATSCTableID>, 'DATA_SERVICE': <enum GST_MTS_TABLE_ID_ATSC_DATA_SERVICE of type GstMpegts.SectionATSCTableID>, 'NETWORK_RESOURCE': <enum GST_MTS_TABLE_ID_ATSC_NETWORK_RESOURCE of type GstMpegts.SectionATSCTableID>, 'LONG_TERM_SERVICE': <enum GST_MTS_TABLE_ID_ATSC_LONG_TERM_SERVICE of type GstMpegts.SectionATSCTableID>, 'DIRECTED_CHANNEL_CHANGE': <enum GST_MTS_TABLE_ID_ATSC_DIRECTED_CHANNEL_CHANGE of type GstMpegts.SectionATSCTableID>, 'DIRECTED_CHANNEL_CHANGE_SECTION_CODE': <enum GST_MTS_TABLE_ID_ATSC_DIRECTED_CHANNEL_CHANGE_SECTION_CODE of type GstMpegts.SectionATSCTableID>, 'AGGREGATE_EVENT_INFORMATION': <enum GST_MTS_TABLE_ID_ATSC_AGGREGATE_EVENT_INFORMATION of type GstMpegts.SectionATSCTableID>, 'AGGREGATE_EXTENDED_TEXT': <enum GST_MTS_TABLE_ID_ATSC_AGGREGATE_EXTENDED_TEXT of type GstMpegts.SectionATSCTableID>, 'AGGREGATE_DATA_EVENT': <enum GST_MTS_TABLE_ID_ATSC_AGGREGATE_DATA_EVENT of type GstMpegts.SectionATSCTableID>, 'SATELLITE_VIRTUAL_CHANNEL': <enum GST_MTS_TABLE_ID_ATSC_SATELLITE_VIRTUAL_CHANNEL of type GstMpegts.SectionATSCTableID>})"
    __enum_values__ = {
        199: 199,
        200: 200,
        201: 201,
        202: 202,
        203: 203,
        204: 204,
        205: 205,
        206: 206,
        207: 207,
        209: 209,
        210: 210,
        211: 211,
        212: 212,
        214: 214,
        215: 215,
        217: 217,
        218: 218,
    }
    __gtype__ = None # (!) real value is '<GType PyGstMpegtsSectionATSCTableID (94624018722928)>'
    __info__ = gi.EnumInfo(SectionATSCTableID)


