# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class KnownStatusCode(__gobject.GEnum):
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


    ACCEPTED = 202
    BAD_GATEWAY = 502
    BAD_REQUEST = 400
    CANCELLED = 1
    CANT_CONNECT = 4
    CANT_CONNECT_PROXY = 5
    CANT_RESOLVE = 2
    CANT_RESOLVE_PROXY = 3
    CONFLICT = 409
    CONTINUE = 100
    CREATED = 201
    EXPECTATION_FAILED = 417
    FAILED_DEPENDENCY = 424
    FORBIDDEN = 403
    FOUND = 302
    GATEWAY_TIMEOUT = 504
    GONE = 410
    HTTP_VERSION_NOT_SUPPORTED = 505
    INSUFFICIENT_STORAGE = 507
    INTERNAL_SERVER_ERROR = 500
    INVALID_RANGE = 416
    IO_ERROR = 7
    LENGTH_REQUIRED = 411
    LOCKED = 423
    MALFORMED = 8
    METHOD_NOT_ALLOWED = 405
    MOVED_PERMANENTLY = 301
    MOVED_TEMPORARILY = 302
    MULTIPLE_CHOICES = 300
    MULTI_STATUS = 207
    NONE = 0
    NON_AUTHORITATIVE = 203
    NOT_ACCEPTABLE = 406
    NOT_APPEARING_IN_THIS_PROTOCOL = 306
    NOT_EXTENDED = 510
    NOT_FOUND = 404
    NOT_IMPLEMENTED = 501
    NOT_MODIFIED = 304
    NO_CONTENT = 204
    OK = 200
    PARTIAL_CONTENT = 206
    PAYMENT_REQUIRED = 402
    PRECONDITION_FAILED = 412
    PROCESSING = 102
    PROXY_AUTHENTICATION_REQUIRED = 407
    PROXY_UNAUTHORIZED = 407
    REQUESTED_RANGE_NOT_SATISFIABLE = 416
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_TIMEOUT = 408
    REQUEST_URI_TOO_LONG = 414
    RESET_CONTENT = 205
    SEE_OTHER = 303
    SERVICE_UNAVAILABLE = 503
    SSL_FAILED = 6
    SWITCHING_PROTOCOLS = 101
    TEMPORARY_REDIRECT = 307
    TLS_FAILED = 11
    TOO_MANY_REDIRECTS = 10
    TRY_AGAIN = 9
    UNAUTHORIZED = 401
    UNPROCESSABLE_ENTITY = 422
    UNSUPPORTED_MEDIA_TYPE = 415
    USE_PROXY = 305
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Soup', '__dict__': <attribute '__dict__' of 'KnownStatusCode' objects>, '__doc__': None, '__gtype__': <GType SoupKnownStatusCode (94750594780416)>, '__enum_values__': {0: <enum SOUP_KNOWN_STATUS_CODE_NONE of type Soup.KnownStatusCode>, 1: <enum SOUP_KNOWN_STATUS_CODE_CANCELLED of type Soup.KnownStatusCode>, 2: <enum SOUP_KNOWN_STATUS_CODE_CANT_RESOLVE of type Soup.KnownStatusCode>, 3: <enum SOUP_KNOWN_STATUS_CODE_CANT_RESOLVE_PROXY of type Soup.KnownStatusCode>, 4: <enum SOUP_KNOWN_STATUS_CODE_CANT_CONNECT of type Soup.KnownStatusCode>, 5: <enum SOUP_KNOWN_STATUS_CODE_CANT_CONNECT_PROXY of type Soup.KnownStatusCode>, 6: <enum SOUP_KNOWN_STATUS_CODE_SSL_FAILED of type Soup.KnownStatusCode>, 7: <enum SOUP_KNOWN_STATUS_CODE_IO_ERROR of type Soup.KnownStatusCode>, 8: <enum SOUP_KNOWN_STATUS_CODE_MALFORMED of type Soup.KnownStatusCode>, 9: <enum SOUP_KNOWN_STATUS_CODE_TRY_AGAIN of type Soup.KnownStatusCode>, 10: <enum SOUP_KNOWN_STATUS_CODE_TOO_MANY_REDIRECTS of type Soup.KnownStatusCode>, 11: <enum SOUP_KNOWN_STATUS_CODE_TLS_FAILED of type Soup.KnownStatusCode>, 100: <enum SOUP_KNOWN_STATUS_CODE_CONTINUE of type Soup.KnownStatusCode>, 101: <enum SOUP_KNOWN_STATUS_CODE_SWITCHING_PROTOCOLS of type Soup.KnownStatusCode>, 102: <enum SOUP_KNOWN_STATUS_CODE_PROCESSING of type Soup.KnownStatusCode>, 200: <enum SOUP_KNOWN_STATUS_CODE_OK of type Soup.KnownStatusCode>, 201: <enum SOUP_KNOWN_STATUS_CODE_CREATED of type Soup.KnownStatusCode>, 202: <enum SOUP_KNOWN_STATUS_CODE_ACCEPTED of type Soup.KnownStatusCode>, 203: <enum SOUP_KNOWN_STATUS_CODE_NON_AUTHORITATIVE of type Soup.KnownStatusCode>, 204: <enum SOUP_KNOWN_STATUS_CODE_NO_CONTENT of type Soup.KnownStatusCode>, 205: <enum SOUP_KNOWN_STATUS_CODE_RESET_CONTENT of type Soup.KnownStatusCode>, 206: <enum SOUP_KNOWN_STATUS_CODE_PARTIAL_CONTENT of type Soup.KnownStatusCode>, 207: <enum SOUP_KNOWN_STATUS_CODE_MULTI_STATUS of type Soup.KnownStatusCode>, 300: <enum SOUP_KNOWN_STATUS_CODE_MULTIPLE_CHOICES of type Soup.KnownStatusCode>, 301: <enum SOUP_KNOWN_STATUS_CODE_MOVED_PERMANENTLY of type Soup.KnownStatusCode>, 302: <enum SOUP_KNOWN_STATUS_CODE_FOUND of type Soup.KnownStatusCode>, 303: <enum SOUP_KNOWN_STATUS_CODE_SEE_OTHER of type Soup.KnownStatusCode>, 304: <enum SOUP_KNOWN_STATUS_CODE_NOT_MODIFIED of type Soup.KnownStatusCode>, 305: <enum SOUP_KNOWN_STATUS_CODE_USE_PROXY of type Soup.KnownStatusCode>, 306: <enum SOUP_KNOWN_STATUS_CODE_NOT_APPEARING_IN_THIS_PROTOCOL of type Soup.KnownStatusCode>, 307: <enum SOUP_KNOWN_STATUS_CODE_TEMPORARY_REDIRECT of type Soup.KnownStatusCode>, 400: <enum SOUP_KNOWN_STATUS_CODE_BAD_REQUEST of type Soup.KnownStatusCode>, 401: <enum SOUP_KNOWN_STATUS_CODE_UNAUTHORIZED of type Soup.KnownStatusCode>, 402: <enum SOUP_KNOWN_STATUS_CODE_PAYMENT_REQUIRED of type Soup.KnownStatusCode>, 403: <enum SOUP_KNOWN_STATUS_CODE_FORBIDDEN of type Soup.KnownStatusCode>, 404: <enum SOUP_KNOWN_STATUS_CODE_NOT_FOUND of type Soup.KnownStatusCode>, 405: <enum SOUP_KNOWN_STATUS_CODE_METHOD_NOT_ALLOWED of type Soup.KnownStatusCode>, 406: <enum SOUP_KNOWN_STATUS_CODE_NOT_ACCEPTABLE of type Soup.KnownStatusCode>, 407: <enum SOUP_KNOWN_STATUS_CODE_PROXY_AUTHENTICATION_REQUIRED of type Soup.KnownStatusCode>, 408: <enum SOUP_KNOWN_STATUS_CODE_REQUEST_TIMEOUT of type Soup.KnownStatusCode>, 409: <enum SOUP_KNOWN_STATUS_CODE_CONFLICT of type Soup.KnownStatusCode>, 410: <enum SOUP_KNOWN_STATUS_CODE_GONE of type Soup.KnownStatusCode>, 411: <enum SOUP_KNOWN_STATUS_CODE_LENGTH_REQUIRED of type Soup.KnownStatusCode>, 412: <enum SOUP_KNOWN_STATUS_CODE_PRECONDITION_FAILED of type Soup.KnownStatusCode>, 413: <enum SOUP_KNOWN_STATUS_CODE_REQUEST_ENTITY_TOO_LARGE of type Soup.KnownStatusCode>, 414: <enum SOUP_KNOWN_STATUS_CODE_REQUEST_URI_TOO_LONG of type Soup.KnownStatusCode>, 415: <enum SOUP_KNOWN_STATUS_CODE_UNSUPPORTED_MEDIA_TYPE of type Soup.KnownStatusCode>, 416: <enum SOUP_KNOWN_STATUS_CODE_REQUESTED_RANGE_NOT_SATISFIABLE of type Soup.KnownStatusCode>, 417: <enum SOUP_KNOWN_STATUS_CODE_EXPECTATION_FAILED of type Soup.KnownStatusCode>, 422: <enum SOUP_KNOWN_STATUS_CODE_UNPROCESSABLE_ENTITY of type Soup.KnownStatusCode>, 423: <enum SOUP_KNOWN_STATUS_CODE_LOCKED of type Soup.KnownStatusCode>, 424: <enum SOUP_KNOWN_STATUS_CODE_FAILED_DEPENDENCY of type Soup.KnownStatusCode>, 500: <enum SOUP_KNOWN_STATUS_CODE_INTERNAL_SERVER_ERROR of type Soup.KnownStatusCode>, 501: <enum SOUP_KNOWN_STATUS_CODE_NOT_IMPLEMENTED of type Soup.KnownStatusCode>, 502: <enum SOUP_KNOWN_STATUS_CODE_BAD_GATEWAY of type Soup.KnownStatusCode>, 503: <enum SOUP_KNOWN_STATUS_CODE_SERVICE_UNAVAILABLE of type Soup.KnownStatusCode>, 504: <enum SOUP_KNOWN_STATUS_CODE_GATEWAY_TIMEOUT of type Soup.KnownStatusCode>, 505: <enum SOUP_KNOWN_STATUS_CODE_HTTP_VERSION_NOT_SUPPORTED of type Soup.KnownStatusCode>, 507: <enum SOUP_KNOWN_STATUS_CODE_INSUFFICIENT_STORAGE of type Soup.KnownStatusCode>, 510: <enum SOUP_KNOWN_STATUS_CODE_NOT_EXTENDED of type Soup.KnownStatusCode>}, '__info__': gi.EnumInfo(KnownStatusCode), 'NONE': <enum SOUP_KNOWN_STATUS_CODE_NONE of type Soup.KnownStatusCode>, 'CANCELLED': <enum SOUP_KNOWN_STATUS_CODE_CANCELLED of type Soup.KnownStatusCode>, 'CANT_RESOLVE': <enum SOUP_KNOWN_STATUS_CODE_CANT_RESOLVE of type Soup.KnownStatusCode>, 'CANT_RESOLVE_PROXY': <enum SOUP_KNOWN_STATUS_CODE_CANT_RESOLVE_PROXY of type Soup.KnownStatusCode>, 'CANT_CONNECT': <enum SOUP_KNOWN_STATUS_CODE_CANT_CONNECT of type Soup.KnownStatusCode>, 'CANT_CONNECT_PROXY': <enum SOUP_KNOWN_STATUS_CODE_CANT_CONNECT_PROXY of type Soup.KnownStatusCode>, 'SSL_FAILED': <enum SOUP_KNOWN_STATUS_CODE_SSL_FAILED of type Soup.KnownStatusCode>, 'IO_ERROR': <enum SOUP_KNOWN_STATUS_CODE_IO_ERROR of type Soup.KnownStatusCode>, 'MALFORMED': <enum SOUP_KNOWN_STATUS_CODE_MALFORMED of type Soup.KnownStatusCode>, 'TRY_AGAIN': <enum SOUP_KNOWN_STATUS_CODE_TRY_AGAIN of type Soup.KnownStatusCode>, 'TOO_MANY_REDIRECTS': <enum SOUP_KNOWN_STATUS_CODE_TOO_MANY_REDIRECTS of type Soup.KnownStatusCode>, 'TLS_FAILED': <enum SOUP_KNOWN_STATUS_CODE_TLS_FAILED of type Soup.KnownStatusCode>, 'CONTINUE': <enum SOUP_KNOWN_STATUS_CODE_CONTINUE of type Soup.KnownStatusCode>, 'SWITCHING_PROTOCOLS': <enum SOUP_KNOWN_STATUS_CODE_SWITCHING_PROTOCOLS of type Soup.KnownStatusCode>, 'PROCESSING': <enum SOUP_KNOWN_STATUS_CODE_PROCESSING of type Soup.KnownStatusCode>, 'OK': <enum SOUP_KNOWN_STATUS_CODE_OK of type Soup.KnownStatusCode>, 'CREATED': <enum SOUP_KNOWN_STATUS_CODE_CREATED of type Soup.KnownStatusCode>, 'ACCEPTED': <enum SOUP_KNOWN_STATUS_CODE_ACCEPTED of type Soup.KnownStatusCode>, 'NON_AUTHORITATIVE': <enum SOUP_KNOWN_STATUS_CODE_NON_AUTHORITATIVE of type Soup.KnownStatusCode>, 'NO_CONTENT': <enum SOUP_KNOWN_STATUS_CODE_NO_CONTENT of type Soup.KnownStatusCode>, 'RESET_CONTENT': <enum SOUP_KNOWN_STATUS_CODE_RESET_CONTENT of type Soup.KnownStatusCode>, 'PARTIAL_CONTENT': <enum SOUP_KNOWN_STATUS_CODE_PARTIAL_CONTENT of type Soup.KnownStatusCode>, 'MULTI_STATUS': <enum SOUP_KNOWN_STATUS_CODE_MULTI_STATUS of type Soup.KnownStatusCode>, 'MULTIPLE_CHOICES': <enum SOUP_KNOWN_STATUS_CODE_MULTIPLE_CHOICES of type Soup.KnownStatusCode>, 'MOVED_PERMANENTLY': <enum SOUP_KNOWN_STATUS_CODE_MOVED_PERMANENTLY of type Soup.KnownStatusCode>, 'FOUND': <enum SOUP_KNOWN_STATUS_CODE_FOUND of type Soup.KnownStatusCode>, 'MOVED_TEMPORARILY': <enum SOUP_KNOWN_STATUS_CODE_FOUND of type Soup.KnownStatusCode>, 'SEE_OTHER': <enum SOUP_KNOWN_STATUS_CODE_SEE_OTHER of type Soup.KnownStatusCode>, 'NOT_MODIFIED': <enum SOUP_KNOWN_STATUS_CODE_NOT_MODIFIED of type Soup.KnownStatusCode>, 'USE_PROXY': <enum SOUP_KNOWN_STATUS_CODE_USE_PROXY of type Soup.KnownStatusCode>, 'NOT_APPEARING_IN_THIS_PROTOCOL': <enum SOUP_KNOWN_STATUS_CODE_NOT_APPEARING_IN_THIS_PROTOCOL of type Soup.KnownStatusCode>, 'TEMPORARY_REDIRECT': <enum SOUP_KNOWN_STATUS_CODE_TEMPORARY_REDIRECT of type Soup.KnownStatusCode>, 'BAD_REQUEST': <enum SOUP_KNOWN_STATUS_CODE_BAD_REQUEST of type Soup.KnownStatusCode>, 'UNAUTHORIZED': <enum SOUP_KNOWN_STATUS_CODE_UNAUTHORIZED of type Soup.KnownStatusCode>, 'PAYMENT_REQUIRED': <enum SOUP_KNOWN_STATUS_CODE_PAYMENT_REQUIRED of type Soup.KnownStatusCode>, 'FORBIDDEN': <enum SOUP_KNOWN_STATUS_CODE_FORBIDDEN of type Soup.KnownStatusCode>, 'NOT_FOUND': <enum SOUP_KNOWN_STATUS_CODE_NOT_FOUND of type Soup.KnownStatusCode>, 'METHOD_NOT_ALLOWED': <enum SOUP_KNOWN_STATUS_CODE_METHOD_NOT_ALLOWED of type Soup.KnownStatusCode>, 'NOT_ACCEPTABLE': <enum SOUP_KNOWN_STATUS_CODE_NOT_ACCEPTABLE of type Soup.KnownStatusCode>, 'PROXY_AUTHENTICATION_REQUIRED': <enum SOUP_KNOWN_STATUS_CODE_PROXY_AUTHENTICATION_REQUIRED of type Soup.KnownStatusCode>, 'PROXY_UNAUTHORIZED': <enum SOUP_KNOWN_STATUS_CODE_PROXY_AUTHENTICATION_REQUIRED of type Soup.KnownStatusCode>, 'REQUEST_TIMEOUT': <enum SOUP_KNOWN_STATUS_CODE_REQUEST_TIMEOUT of type Soup.KnownStatusCode>, 'CONFLICT': <enum SOUP_KNOWN_STATUS_CODE_CONFLICT of type Soup.KnownStatusCode>, 'GONE': <enum SOUP_KNOWN_STATUS_CODE_GONE of type Soup.KnownStatusCode>, 'LENGTH_REQUIRED': <enum SOUP_KNOWN_STATUS_CODE_LENGTH_REQUIRED of type Soup.KnownStatusCode>, 'PRECONDITION_FAILED': <enum SOUP_KNOWN_STATUS_CODE_PRECONDITION_FAILED of type Soup.KnownStatusCode>, 'REQUEST_ENTITY_TOO_LARGE': <enum SOUP_KNOWN_STATUS_CODE_REQUEST_ENTITY_TOO_LARGE of type Soup.KnownStatusCode>, 'REQUEST_URI_TOO_LONG': <enum SOUP_KNOWN_STATUS_CODE_REQUEST_URI_TOO_LONG of type Soup.KnownStatusCode>, 'UNSUPPORTED_MEDIA_TYPE': <enum SOUP_KNOWN_STATUS_CODE_UNSUPPORTED_MEDIA_TYPE of type Soup.KnownStatusCode>, 'REQUESTED_RANGE_NOT_SATISFIABLE': <enum SOUP_KNOWN_STATUS_CODE_REQUESTED_RANGE_NOT_SATISFIABLE of type Soup.KnownStatusCode>, 'INVALID_RANGE': <enum SOUP_KNOWN_STATUS_CODE_REQUESTED_RANGE_NOT_SATISFIABLE of type Soup.KnownStatusCode>, 'EXPECTATION_FAILED': <enum SOUP_KNOWN_STATUS_CODE_EXPECTATION_FAILED of type Soup.KnownStatusCode>, 'UNPROCESSABLE_ENTITY': <enum SOUP_KNOWN_STATUS_CODE_UNPROCESSABLE_ENTITY of type Soup.KnownStatusCode>, 'LOCKED': <enum SOUP_KNOWN_STATUS_CODE_LOCKED of type Soup.KnownStatusCode>, 'FAILED_DEPENDENCY': <enum SOUP_KNOWN_STATUS_CODE_FAILED_DEPENDENCY of type Soup.KnownStatusCode>, 'INTERNAL_SERVER_ERROR': <enum SOUP_KNOWN_STATUS_CODE_INTERNAL_SERVER_ERROR of type Soup.KnownStatusCode>, 'NOT_IMPLEMENTED': <enum SOUP_KNOWN_STATUS_CODE_NOT_IMPLEMENTED of type Soup.KnownStatusCode>, 'BAD_GATEWAY': <enum SOUP_KNOWN_STATUS_CODE_BAD_GATEWAY of type Soup.KnownStatusCode>, 'SERVICE_UNAVAILABLE': <enum SOUP_KNOWN_STATUS_CODE_SERVICE_UNAVAILABLE of type Soup.KnownStatusCode>, 'GATEWAY_TIMEOUT': <enum SOUP_KNOWN_STATUS_CODE_GATEWAY_TIMEOUT of type Soup.KnownStatusCode>, 'HTTP_VERSION_NOT_SUPPORTED': <enum SOUP_KNOWN_STATUS_CODE_HTTP_VERSION_NOT_SUPPORTED of type Soup.KnownStatusCode>, 'INSUFFICIENT_STORAGE': <enum SOUP_KNOWN_STATUS_CODE_INSUFFICIENT_STORAGE of type Soup.KnownStatusCode>, 'NOT_EXTENDED': <enum SOUP_KNOWN_STATUS_CODE_NOT_EXTENDED of type Soup.KnownStatusCode>})"
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
        100: 100,
        101: 101,
        102: 102,
        200: 200,
        201: 201,
        202: 202,
        203: 203,
        204: 204,
        205: 205,
        206: 206,
        207: 207,
        300: 300,
        301: 301,
        302: 302,
        303: 303,
        304: 304,
        305: 305,
        306: 306,
        307: 307,
        400: 400,
        401: 401,
        402: 402,
        403: 403,
        404: 404,
        405: 405,
        406: 406,
        407: 407,
        408: 408,
        409: 409,
        410: 410,
        411: 411,
        412: 412,
        413: 413,
        414: 414,
        415: 415,
        416: 416,
        417: 417,
        422: 422,
        423: 423,
        424: 424,
        500: 500,
        501: 501,
        502: 502,
        503: 503,
        504: 504,
        505: 505,
        507: 507,
        510: 510,
    }
    __gtype__ = None # (!) real value is '<GType SoupKnownStatusCode (94750594780416)>'
    __info__ = gi.EnumInfo(KnownStatusCode)


