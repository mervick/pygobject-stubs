# encoding: utf-8
# module gi.repository.GstRtsp
# from /usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
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


class RTSPStatusCode(__gobject.GEnum):
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


    AGGREGATE_OPERATION_NOT_ALLOWED = 459
    BAD_GATEWAY = 502
    BAD_REQUEST = 400
    CONFERENCE_NOT_FOUND = 452
    CONTINUE = 100
    CREATED = 201
    DESTINATION_UNREACHABLE = 462
    FORBIDDEN = 403
    GATEWAY_TIMEOUT = 504
    GONE = 410
    HEADER_FIELD_NOT_VALID_FOR_RESOURCE = 456
    INTERNAL_SERVER_ERROR = 500
    INVALID = 0
    INVALID_RANGE = 457
    KEY_MANAGEMENT_FAILURE = 463
    LENGTH_REQUIRED = 411
    LOW_ON_STORAGE = 250
    METHOD_NOT_ALLOWED = 405
    METHOD_NOT_VALID_IN_THIS_STATE = 455
    MOVED_PERMANENTLY = 301
    MOVE_TEMPORARILY = 302
    MULTIPLE_CHOICES = 300
    NOT_ACCEPTABLE = 406
    NOT_ENOUGH_BANDWIDTH = 453
    NOT_FOUND = 404
    NOT_IMPLEMENTED = 501
    NOT_MODIFIED = 304
    OK = 200
    ONLY_AGGREGATE_OPERATION_ALLOWED = 460
    OPTION_NOT_SUPPORTED = 551
    PARAMETER_IS_READONLY = 458
    PARAMETER_NOT_UNDERSTOOD = 451
    PAYMENT_REQUIRED = 402
    PRECONDITION_FAILED = 412
    PROXY_AUTH_REQUIRED = 407
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_TIMEOUT = 408
    REQUEST_URI_TOO_LARGE = 414
    RTSP_VERSION_NOT_SUPPORTED = 505
    SEE_OTHER = 303
    SERVICE_UNAVAILABLE = 503
    SESSION_NOT_FOUND = 454
    UNAUTHORIZED = 401
    UNSUPPORTED_MEDIA_TYPE = 415
    UNSUPPORTED_TRANSPORT = 461
    USE_PROXY = 305
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstRtsp', '__dict__': <attribute '__dict__' of 'RTSPStatusCode' objects>, '__doc__': None, '__gtype__': <GType GstRTSPStatusCode (93854382837536)>, '__enum_values__': {0: <enum GST_RTSP_STS_INVALID of type GstRtsp.RTSPStatusCode>, 100: <enum GST_RTSP_STS_CONTINUE of type GstRtsp.RTSPStatusCode>, 200: <enum GST_RTSP_STS_OK of type GstRtsp.RTSPStatusCode>, 201: <enum GST_RTSP_STS_CREATED of type GstRtsp.RTSPStatusCode>, 250: <enum GST_RTSP_STS_LOW_ON_STORAGE of type GstRtsp.RTSPStatusCode>, 300: <enum GST_RTSP_STS_MULTIPLE_CHOICES of type GstRtsp.RTSPStatusCode>, 301: <enum GST_RTSP_STS_MOVED_PERMANENTLY of type GstRtsp.RTSPStatusCode>, 302: <enum GST_RTSP_STS_MOVE_TEMPORARILY of type GstRtsp.RTSPStatusCode>, 303: <enum GST_RTSP_STS_SEE_OTHER of type GstRtsp.RTSPStatusCode>, 304: <enum GST_RTSP_STS_NOT_MODIFIED of type GstRtsp.RTSPStatusCode>, 305: <enum GST_RTSP_STS_USE_PROXY of type GstRtsp.RTSPStatusCode>, 400: <enum GST_RTSP_STS_BAD_REQUEST of type GstRtsp.RTSPStatusCode>, 401: <enum GST_RTSP_STS_UNAUTHORIZED of type GstRtsp.RTSPStatusCode>, 402: <enum GST_RTSP_STS_PAYMENT_REQUIRED of type GstRtsp.RTSPStatusCode>, 403: <enum GST_RTSP_STS_FORBIDDEN of type GstRtsp.RTSPStatusCode>, 404: <enum GST_RTSP_STS_NOT_FOUND of type GstRtsp.RTSPStatusCode>, 405: <enum GST_RTSP_STS_METHOD_NOT_ALLOWED of type GstRtsp.RTSPStatusCode>, 406: <enum GST_RTSP_STS_NOT_ACCEPTABLE of type GstRtsp.RTSPStatusCode>, 407: <enum GST_RTSP_STS_PROXY_AUTH_REQUIRED of type GstRtsp.RTSPStatusCode>, 408: <enum GST_RTSP_STS_REQUEST_TIMEOUT of type GstRtsp.RTSPStatusCode>, 410: <enum GST_RTSP_STS_GONE of type GstRtsp.RTSPStatusCode>, 411: <enum GST_RTSP_STS_LENGTH_REQUIRED of type GstRtsp.RTSPStatusCode>, 412: <enum GST_RTSP_STS_PRECONDITION_FAILED of type GstRtsp.RTSPStatusCode>, 413: <enum GST_RTSP_STS_REQUEST_ENTITY_TOO_LARGE of type GstRtsp.RTSPStatusCode>, 414: <enum GST_RTSP_STS_REQUEST_URI_TOO_LARGE of type GstRtsp.RTSPStatusCode>, 415: <enum GST_RTSP_STS_UNSUPPORTED_MEDIA_TYPE of type GstRtsp.RTSPStatusCode>, 451: <enum GST_RTSP_STS_PARAMETER_NOT_UNDERSTOOD of type GstRtsp.RTSPStatusCode>, 452: <enum GST_RTSP_STS_CONFERENCE_NOT_FOUND of type GstRtsp.RTSPStatusCode>, 453: <enum GST_RTSP_STS_NOT_ENOUGH_BANDWIDTH of type GstRtsp.RTSPStatusCode>, 454: <enum GST_RTSP_STS_SESSION_NOT_FOUND of type GstRtsp.RTSPStatusCode>, 455: <enum GST_RTSP_STS_METHOD_NOT_VALID_IN_THIS_STATE of type GstRtsp.RTSPStatusCode>, 456: <enum GST_RTSP_STS_HEADER_FIELD_NOT_VALID_FOR_RESOURCE of type GstRtsp.RTSPStatusCode>, 457: <enum GST_RTSP_STS_INVALID_RANGE of type GstRtsp.RTSPStatusCode>, 458: <enum GST_RTSP_STS_PARAMETER_IS_READONLY of type GstRtsp.RTSPStatusCode>, 459: <enum GST_RTSP_STS_AGGREGATE_OPERATION_NOT_ALLOWED of type GstRtsp.RTSPStatusCode>, 460: <enum GST_RTSP_STS_ONLY_AGGREGATE_OPERATION_ALLOWED of type GstRtsp.RTSPStatusCode>, 461: <enum GST_RTSP_STS_UNSUPPORTED_TRANSPORT of type GstRtsp.RTSPStatusCode>, 462: <enum GST_RTSP_STS_DESTINATION_UNREACHABLE of type GstRtsp.RTSPStatusCode>, 463: <enum GST_RTSP_STS_KEY_MANAGEMENT_FAILURE of type GstRtsp.RTSPStatusCode>, 500: <enum GST_RTSP_STS_INTERNAL_SERVER_ERROR of type GstRtsp.RTSPStatusCode>, 501: <enum GST_RTSP_STS_NOT_IMPLEMENTED of type GstRtsp.RTSPStatusCode>, 502: <enum GST_RTSP_STS_BAD_GATEWAY of type GstRtsp.RTSPStatusCode>, 503: <enum GST_RTSP_STS_SERVICE_UNAVAILABLE of type GstRtsp.RTSPStatusCode>, 504: <enum GST_RTSP_STS_GATEWAY_TIMEOUT of type GstRtsp.RTSPStatusCode>, 505: <enum GST_RTSP_STS_RTSP_VERSION_NOT_SUPPORTED of type GstRtsp.RTSPStatusCode>, 551: <enum GST_RTSP_STS_OPTION_NOT_SUPPORTED of type GstRtsp.RTSPStatusCode>}, '__info__': gi.EnumInfo(RTSPStatusCode), 'INVALID': <enum GST_RTSP_STS_INVALID of type GstRtsp.RTSPStatusCode>, 'CONTINUE': <enum GST_RTSP_STS_CONTINUE of type GstRtsp.RTSPStatusCode>, 'OK': <enum GST_RTSP_STS_OK of type GstRtsp.RTSPStatusCode>, 'CREATED': <enum GST_RTSP_STS_CREATED of type GstRtsp.RTSPStatusCode>, 'LOW_ON_STORAGE': <enum GST_RTSP_STS_LOW_ON_STORAGE of type GstRtsp.RTSPStatusCode>, 'MULTIPLE_CHOICES': <enum GST_RTSP_STS_MULTIPLE_CHOICES of type GstRtsp.RTSPStatusCode>, 'MOVED_PERMANENTLY': <enum GST_RTSP_STS_MOVED_PERMANENTLY of type GstRtsp.RTSPStatusCode>, 'MOVE_TEMPORARILY': <enum GST_RTSP_STS_MOVE_TEMPORARILY of type GstRtsp.RTSPStatusCode>, 'SEE_OTHER': <enum GST_RTSP_STS_SEE_OTHER of type GstRtsp.RTSPStatusCode>, 'NOT_MODIFIED': <enum GST_RTSP_STS_NOT_MODIFIED of type GstRtsp.RTSPStatusCode>, 'USE_PROXY': <enum GST_RTSP_STS_USE_PROXY of type GstRtsp.RTSPStatusCode>, 'BAD_REQUEST': <enum GST_RTSP_STS_BAD_REQUEST of type GstRtsp.RTSPStatusCode>, 'UNAUTHORIZED': <enum GST_RTSP_STS_UNAUTHORIZED of type GstRtsp.RTSPStatusCode>, 'PAYMENT_REQUIRED': <enum GST_RTSP_STS_PAYMENT_REQUIRED of type GstRtsp.RTSPStatusCode>, 'FORBIDDEN': <enum GST_RTSP_STS_FORBIDDEN of type GstRtsp.RTSPStatusCode>, 'NOT_FOUND': <enum GST_RTSP_STS_NOT_FOUND of type GstRtsp.RTSPStatusCode>, 'METHOD_NOT_ALLOWED': <enum GST_RTSP_STS_METHOD_NOT_ALLOWED of type GstRtsp.RTSPStatusCode>, 'NOT_ACCEPTABLE': <enum GST_RTSP_STS_NOT_ACCEPTABLE of type GstRtsp.RTSPStatusCode>, 'PROXY_AUTH_REQUIRED': <enum GST_RTSP_STS_PROXY_AUTH_REQUIRED of type GstRtsp.RTSPStatusCode>, 'REQUEST_TIMEOUT': <enum GST_RTSP_STS_REQUEST_TIMEOUT of type GstRtsp.RTSPStatusCode>, 'GONE': <enum GST_RTSP_STS_GONE of type GstRtsp.RTSPStatusCode>, 'LENGTH_REQUIRED': <enum GST_RTSP_STS_LENGTH_REQUIRED of type GstRtsp.RTSPStatusCode>, 'PRECONDITION_FAILED': <enum GST_RTSP_STS_PRECONDITION_FAILED of type GstRtsp.RTSPStatusCode>, 'REQUEST_ENTITY_TOO_LARGE': <enum GST_RTSP_STS_REQUEST_ENTITY_TOO_LARGE of type GstRtsp.RTSPStatusCode>, 'REQUEST_URI_TOO_LARGE': <enum GST_RTSP_STS_REQUEST_URI_TOO_LARGE of type GstRtsp.RTSPStatusCode>, 'UNSUPPORTED_MEDIA_TYPE': <enum GST_RTSP_STS_UNSUPPORTED_MEDIA_TYPE of type GstRtsp.RTSPStatusCode>, 'PARAMETER_NOT_UNDERSTOOD': <enum GST_RTSP_STS_PARAMETER_NOT_UNDERSTOOD of type GstRtsp.RTSPStatusCode>, 'CONFERENCE_NOT_FOUND': <enum GST_RTSP_STS_CONFERENCE_NOT_FOUND of type GstRtsp.RTSPStatusCode>, 'NOT_ENOUGH_BANDWIDTH': <enum GST_RTSP_STS_NOT_ENOUGH_BANDWIDTH of type GstRtsp.RTSPStatusCode>, 'SESSION_NOT_FOUND': <enum GST_RTSP_STS_SESSION_NOT_FOUND of type GstRtsp.RTSPStatusCode>, 'METHOD_NOT_VALID_IN_THIS_STATE': <enum GST_RTSP_STS_METHOD_NOT_VALID_IN_THIS_STATE of type GstRtsp.RTSPStatusCode>, 'HEADER_FIELD_NOT_VALID_FOR_RESOURCE': <enum GST_RTSP_STS_HEADER_FIELD_NOT_VALID_FOR_RESOURCE of type GstRtsp.RTSPStatusCode>, 'INVALID_RANGE': <enum GST_RTSP_STS_INVALID_RANGE of type GstRtsp.RTSPStatusCode>, 'PARAMETER_IS_READONLY': <enum GST_RTSP_STS_PARAMETER_IS_READONLY of type GstRtsp.RTSPStatusCode>, 'AGGREGATE_OPERATION_NOT_ALLOWED': <enum GST_RTSP_STS_AGGREGATE_OPERATION_NOT_ALLOWED of type GstRtsp.RTSPStatusCode>, 'ONLY_AGGREGATE_OPERATION_ALLOWED': <enum GST_RTSP_STS_ONLY_AGGREGATE_OPERATION_ALLOWED of type GstRtsp.RTSPStatusCode>, 'UNSUPPORTED_TRANSPORT': <enum GST_RTSP_STS_UNSUPPORTED_TRANSPORT of type GstRtsp.RTSPStatusCode>, 'DESTINATION_UNREACHABLE': <enum GST_RTSP_STS_DESTINATION_UNREACHABLE of type GstRtsp.RTSPStatusCode>, 'KEY_MANAGEMENT_FAILURE': <enum GST_RTSP_STS_KEY_MANAGEMENT_FAILURE of type GstRtsp.RTSPStatusCode>, 'INTERNAL_SERVER_ERROR': <enum GST_RTSP_STS_INTERNAL_SERVER_ERROR of type GstRtsp.RTSPStatusCode>, 'NOT_IMPLEMENTED': <enum GST_RTSP_STS_NOT_IMPLEMENTED of type GstRtsp.RTSPStatusCode>, 'BAD_GATEWAY': <enum GST_RTSP_STS_BAD_GATEWAY of type GstRtsp.RTSPStatusCode>, 'SERVICE_UNAVAILABLE': <enum GST_RTSP_STS_SERVICE_UNAVAILABLE of type GstRtsp.RTSPStatusCode>, 'GATEWAY_TIMEOUT': <enum GST_RTSP_STS_GATEWAY_TIMEOUT of type GstRtsp.RTSPStatusCode>, 'RTSP_VERSION_NOT_SUPPORTED': <enum GST_RTSP_STS_RTSP_VERSION_NOT_SUPPORTED of type GstRtsp.RTSPStatusCode>, 'OPTION_NOT_SUPPORTED': <enum GST_RTSP_STS_OPTION_NOT_SUPPORTED of type GstRtsp.RTSPStatusCode>})"
    __enum_values__ = {
        0: 0,
        100: 100,
        200: 200,
        201: 201,
        250: 250,
        300: 300,
        301: 301,
        302: 302,
        303: 303,
        304: 304,
        305: 305,
        400: 400,
        401: 401,
        402: 402,
        403: 403,
        404: 404,
        405: 405,
        406: 406,
        407: 407,
        408: 408,
        410: 410,
        411: 411,
        412: 412,
        413: 413,
        414: 414,
        415: 415,
        451: 451,
        452: 452,
        453: 453,
        454: 454,
        455: 455,
        456: 456,
        457: 457,
        458: 458,
        459: 459,
        460: 460,
        461: 461,
        462: 462,
        463: 463,
        500: 500,
        501: 501,
        502: 502,
        503: 503,
        504: 504,
        505: 505,
        551: 551,
    }
    __gtype__ = None # (!) real value is '<GType GstRTSPStatusCode (93854382837536)>'
    __info__ = gi.EnumInfo(RTSPStatusCode)


