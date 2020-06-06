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


class RTSPHeaderField(__gobject.GEnum):
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


    ACCEPT = 1
    ACCEPT_CHARSET = 56
    ACCEPT_ENCODING = 2
    ACCEPT_LANGUAGE = 3
    ACCEPT_RANGES = 86
    ALERT = 45
    ALLOW = 4
    AUTHENTICATION_INFO = 76
    AUTHORIZATION = 5
    BANDWIDTH = 6
    BLOCKSIZE = 7
    CACHE_CONTROL = 8
    CLIENT_CHALLENGE = 40
    CLIENT_ID = 46
    COMPANY_ID = 47
    CONFERENCE = 9
    CONNECTION = 10
    CONTENT_BASE = 11
    CONTENT_ENCODING = 12
    CONTENT_LANGUAGE = 13
    CONTENT_LENGTH = 14
    CONTENT_LOCATION = 15
    CONTENT_TYPE = 16
    CSEQ = 17
    DATE = 18
    ETAG = 54
    EXPIRES = 19
    FRAMES = 87
    FROM = 20
    GUID = 48
    HOST = 77
    IF_MATCH = 55
    IF_MODIFIED_SINCE = 21
    INVALID = 0
    KEYMGMT = 82
    LANGUAGE = 51
    LAST = 89
    LAST_MODIFIED = 22
    LOCATION = 53
    MAX_ASM_WIDTH = 50
    MEDIA_PROPERTIES = 84
    PIPELINED_REQUESTS = 83
    PLAYER_START_TIME = 52
    PRAGMA = 78
    PROXY_AUTHENTICATE = 23
    PROXY_REQUIRE = 24
    PUBLIC = 25
    RANGE = 26
    RATE_CONTROL = 88
    REAL_CHALLENGE1 = 41
    REAL_CHALLENGE2 = 42
    REAL_CHALLENGE3 = 43
    REFERER = 27
    REGION_DATA = 49
    REQUIRE = 28
    RETRY_AFTER = 29
    RTCP_INTERVAL = 81
    RTP_INFO = 30
    SCALE = 31
    SEEK_STYLE = 85
    SERVER = 33
    SESSION = 32
    SPEED = 34
    SUBSCRIBE = 44
    SUPPORTED = 57
    TIMESTAMP = 75
    TRANSPORT = 35
    UNSUPPORTED = 36
    USER_AGENT = 37
    VARY = 58
    VIA = 38
    WWW_AUTHENTICATE = 39
    X_ACCELERATE_STREAMING = 59
    X_ACCEPT_AUTHENT = 60
    X_ACCEPT_PROXY_AUTHENT = 61
    X_BROADCAST_ID = 62
    X_BURST_STREAMING = 63
    X_NOTICE = 64
    X_PLAYER_LAG_TIME = 65
    X_PLAYLIST = 66
    X_PLAYLIST_CHANGE_NOTICE = 67
    X_PLAYLIST_GEN_ID = 68
    X_PLAYLIST_SEEK_ID = 69
    X_PROXY_CLIENT_AGENT = 70
    X_PROXY_CLIENT_VERB = 71
    X_RECEDING_PLAYLISTCHANGE = 72
    X_RTP_INFO = 73
    X_SERVER_IP_ADDRESS = 79
    X_SESSIONCOOKIE = 80
    X_STARTUPPROFILE = 74
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstRtsp', '__dict__': <attribute '__dict__' of 'RTSPHeaderField' objects>, '__doc__': None, '__gtype__': <GType GstRTSPHeaderField (93854382881968)>, '__enum_values__': {0: <enum GST_RTSP_HDR_INVALID of type GstRtsp.RTSPHeaderField>, 1: <enum GST_RTSP_HDR_ACCEPT of type GstRtsp.RTSPHeaderField>, 2: <enum GST_RTSP_HDR_ACCEPT_ENCODING of type GstRtsp.RTSPHeaderField>, 3: <enum GST_RTSP_HDR_ACCEPT_LANGUAGE of type GstRtsp.RTSPHeaderField>, 4: <enum GST_RTSP_HDR_ALLOW of type GstRtsp.RTSPHeaderField>, 5: <enum GST_RTSP_HDR_AUTHORIZATION of type GstRtsp.RTSPHeaderField>, 6: <enum GST_RTSP_HDR_BANDWIDTH of type GstRtsp.RTSPHeaderField>, 7: <enum GST_RTSP_HDR_BLOCKSIZE of type GstRtsp.RTSPHeaderField>, 8: <enum GST_RTSP_HDR_CACHE_CONTROL of type GstRtsp.RTSPHeaderField>, 9: <enum GST_RTSP_HDR_CONFERENCE of type GstRtsp.RTSPHeaderField>, 10: <enum GST_RTSP_HDR_CONNECTION of type GstRtsp.RTSPHeaderField>, 11: <enum GST_RTSP_HDR_CONTENT_BASE of type GstRtsp.RTSPHeaderField>, 12: <enum GST_RTSP_HDR_CONTENT_ENCODING of type GstRtsp.RTSPHeaderField>, 13: <enum GST_RTSP_HDR_CONTENT_LANGUAGE of type GstRtsp.RTSPHeaderField>, 14: <enum GST_RTSP_HDR_CONTENT_LENGTH of type GstRtsp.RTSPHeaderField>, 15: <enum GST_RTSP_HDR_CONTENT_LOCATION of type GstRtsp.RTSPHeaderField>, 16: <enum GST_RTSP_HDR_CONTENT_TYPE of type GstRtsp.RTSPHeaderField>, 17: <enum GST_RTSP_HDR_CSEQ of type GstRtsp.RTSPHeaderField>, 18: <enum GST_RTSP_HDR_DATE of type GstRtsp.RTSPHeaderField>, 19: <enum GST_RTSP_HDR_EXPIRES of type GstRtsp.RTSPHeaderField>, 20: <enum GST_RTSP_HDR_FROM of type GstRtsp.RTSPHeaderField>, 21: <enum GST_RTSP_HDR_IF_MODIFIED_SINCE of type GstRtsp.RTSPHeaderField>, 22: <enum GST_RTSP_HDR_LAST_MODIFIED of type GstRtsp.RTSPHeaderField>, 23: <enum GST_RTSP_HDR_PROXY_AUTHENTICATE of type GstRtsp.RTSPHeaderField>, 24: <enum GST_RTSP_HDR_PROXY_REQUIRE of type GstRtsp.RTSPHeaderField>, 25: <enum GST_RTSP_HDR_PUBLIC of type GstRtsp.RTSPHeaderField>, 26: <enum GST_RTSP_HDR_RANGE of type GstRtsp.RTSPHeaderField>, 27: <enum GST_RTSP_HDR_REFERER of type GstRtsp.RTSPHeaderField>, 28: <enum GST_RTSP_HDR_REQUIRE of type GstRtsp.RTSPHeaderField>, 29: <enum GST_RTSP_HDR_RETRY_AFTER of type GstRtsp.RTSPHeaderField>, 30: <enum GST_RTSP_HDR_RTP_INFO of type GstRtsp.RTSPHeaderField>, 31: <enum GST_RTSP_HDR_SCALE of type GstRtsp.RTSPHeaderField>, 32: <enum GST_RTSP_HDR_SESSION of type GstRtsp.RTSPHeaderField>, 33: <enum GST_RTSP_HDR_SERVER of type GstRtsp.RTSPHeaderField>, 34: <enum GST_RTSP_HDR_SPEED of type GstRtsp.RTSPHeaderField>, 35: <enum GST_RTSP_HDR_TRANSPORT of type GstRtsp.RTSPHeaderField>, 36: <enum GST_RTSP_HDR_UNSUPPORTED of type GstRtsp.RTSPHeaderField>, 37: <enum GST_RTSP_HDR_USER_AGENT of type GstRtsp.RTSPHeaderField>, 38: <enum GST_RTSP_HDR_VIA of type GstRtsp.RTSPHeaderField>, 39: <enum GST_RTSP_HDR_WWW_AUTHENTICATE of type GstRtsp.RTSPHeaderField>, 40: <enum GST_RTSP_HDR_CLIENT_CHALLENGE of type GstRtsp.RTSPHeaderField>, 41: <enum GST_RTSP_HDR_REAL_CHALLENGE1 of type GstRtsp.RTSPHeaderField>, 42: <enum GST_RTSP_HDR_REAL_CHALLENGE2 of type GstRtsp.RTSPHeaderField>, 43: <enum GST_RTSP_HDR_REAL_CHALLENGE3 of type GstRtsp.RTSPHeaderField>, 44: <enum GST_RTSP_HDR_SUBSCRIBE of type GstRtsp.RTSPHeaderField>, 45: <enum GST_RTSP_HDR_ALERT of type GstRtsp.RTSPHeaderField>, 46: <enum GST_RTSP_HDR_CLIENT_ID of type GstRtsp.RTSPHeaderField>, 47: <enum GST_RTSP_HDR_COMPANY_ID of type GstRtsp.RTSPHeaderField>, 48: <enum GST_RTSP_HDR_GUID of type GstRtsp.RTSPHeaderField>, 49: <enum GST_RTSP_HDR_REGION_DATA of type GstRtsp.RTSPHeaderField>, 50: <enum GST_RTSP_HDR_MAX_ASM_WIDTH of type GstRtsp.RTSPHeaderField>, 51: <enum GST_RTSP_HDR_LANGUAGE of type GstRtsp.RTSPHeaderField>, 52: <enum GST_RTSP_HDR_PLAYER_START_TIME of type GstRtsp.RTSPHeaderField>, 53: <enum GST_RTSP_HDR_LOCATION of type GstRtsp.RTSPHeaderField>, 54: <enum GST_RTSP_HDR_ETAG of type GstRtsp.RTSPHeaderField>, 55: <enum GST_RTSP_HDR_IF_MATCH of type GstRtsp.RTSPHeaderField>, 56: <enum GST_RTSP_HDR_ACCEPT_CHARSET of type GstRtsp.RTSPHeaderField>, 57: <enum GST_RTSP_HDR_SUPPORTED of type GstRtsp.RTSPHeaderField>, 58: <enum GST_RTSP_HDR_VARY of type GstRtsp.RTSPHeaderField>, 59: <enum GST_RTSP_HDR_X_ACCELERATE_STREAMING of type GstRtsp.RTSPHeaderField>, 60: <enum GST_RTSP_HDR_X_ACCEPT_AUTHENT of type GstRtsp.RTSPHeaderField>, 61: <enum GST_RTSP_HDR_X_ACCEPT_PROXY_AUTHENT of type GstRtsp.RTSPHeaderField>, 62: <enum GST_RTSP_HDR_X_BROADCAST_ID of type GstRtsp.RTSPHeaderField>, 63: <enum GST_RTSP_HDR_X_BURST_STREAMING of type GstRtsp.RTSPHeaderField>, 64: <enum GST_RTSP_HDR_X_NOTICE of type GstRtsp.RTSPHeaderField>, 65: <enum GST_RTSP_HDR_X_PLAYER_LAG_TIME of type GstRtsp.RTSPHeaderField>, 66: <enum GST_RTSP_HDR_X_PLAYLIST of type GstRtsp.RTSPHeaderField>, 67: <enum GST_RTSP_HDR_X_PLAYLIST_CHANGE_NOTICE of type GstRtsp.RTSPHeaderField>, 68: <enum GST_RTSP_HDR_X_PLAYLIST_GEN_ID of type GstRtsp.RTSPHeaderField>, 69: <enum GST_RTSP_HDR_X_PLAYLIST_SEEK_ID of type GstRtsp.RTSPHeaderField>, 70: <enum GST_RTSP_HDR_X_PROXY_CLIENT_AGENT of type GstRtsp.RTSPHeaderField>, 71: <enum GST_RTSP_HDR_X_PROXY_CLIENT_VERB of type GstRtsp.RTSPHeaderField>, 72: <enum GST_RTSP_HDR_X_RECEDING_PLAYLISTCHANGE of type GstRtsp.RTSPHeaderField>, 73: <enum GST_RTSP_HDR_X_RTP_INFO of type GstRtsp.RTSPHeaderField>, 74: <enum GST_RTSP_HDR_X_STARTUPPROFILE of type GstRtsp.RTSPHeaderField>, 75: <enum GST_RTSP_HDR_TIMESTAMP of type GstRtsp.RTSPHeaderField>, 76: <enum GST_RTSP_HDR_AUTHENTICATION_INFO of type GstRtsp.RTSPHeaderField>, 77: <enum GST_RTSP_HDR_HOST of type GstRtsp.RTSPHeaderField>, 78: <enum GST_RTSP_HDR_PRAGMA of type GstRtsp.RTSPHeaderField>, 79: <enum GST_RTSP_HDR_X_SERVER_IP_ADDRESS of type GstRtsp.RTSPHeaderField>, 80: <enum GST_RTSP_HDR_X_SESSIONCOOKIE of type GstRtsp.RTSPHeaderField>, 81: <enum GST_RTSP_HDR_RTCP_INTERVAL of type GstRtsp.RTSPHeaderField>, 82: <enum GST_RTSP_HDR_KEYMGMT of type GstRtsp.RTSPHeaderField>, 83: <enum GST_RTSP_HDR_PIPELINED_REQUESTS of type GstRtsp.RTSPHeaderField>, 84: <enum GST_RTSP_HDR_MEDIA_PROPERTIES of type GstRtsp.RTSPHeaderField>, 85: <enum GST_RTSP_HDR_SEEK_STYLE of type GstRtsp.RTSPHeaderField>, 86: <enum GST_RTSP_HDR_ACCEPT_RANGES of type GstRtsp.RTSPHeaderField>, 87: <enum GST_RTSP_HDR_FRAMES of type GstRtsp.RTSPHeaderField>, 88: <enum GST_RTSP_HDR_RATE_CONTROL of type GstRtsp.RTSPHeaderField>, 89: <enum GST_RTSP_HDR_LAST of type GstRtsp.RTSPHeaderField>}, '__info__': gi.EnumInfo(RTSPHeaderField), 'INVALID': <enum GST_RTSP_HDR_INVALID of type GstRtsp.RTSPHeaderField>, 'ACCEPT': <enum GST_RTSP_HDR_ACCEPT of type GstRtsp.RTSPHeaderField>, 'ACCEPT_ENCODING': <enum GST_RTSP_HDR_ACCEPT_ENCODING of type GstRtsp.RTSPHeaderField>, 'ACCEPT_LANGUAGE': <enum GST_RTSP_HDR_ACCEPT_LANGUAGE of type GstRtsp.RTSPHeaderField>, 'ALLOW': <enum GST_RTSP_HDR_ALLOW of type GstRtsp.RTSPHeaderField>, 'AUTHORIZATION': <enum GST_RTSP_HDR_AUTHORIZATION of type GstRtsp.RTSPHeaderField>, 'BANDWIDTH': <enum GST_RTSP_HDR_BANDWIDTH of type GstRtsp.RTSPHeaderField>, 'BLOCKSIZE': <enum GST_RTSP_HDR_BLOCKSIZE of type GstRtsp.RTSPHeaderField>, 'CACHE_CONTROL': <enum GST_RTSP_HDR_CACHE_CONTROL of type GstRtsp.RTSPHeaderField>, 'CONFERENCE': <enum GST_RTSP_HDR_CONFERENCE of type GstRtsp.RTSPHeaderField>, 'CONNECTION': <enum GST_RTSP_HDR_CONNECTION of type GstRtsp.RTSPHeaderField>, 'CONTENT_BASE': <enum GST_RTSP_HDR_CONTENT_BASE of type GstRtsp.RTSPHeaderField>, 'CONTENT_ENCODING': <enum GST_RTSP_HDR_CONTENT_ENCODING of type GstRtsp.RTSPHeaderField>, 'CONTENT_LANGUAGE': <enum GST_RTSP_HDR_CONTENT_LANGUAGE of type GstRtsp.RTSPHeaderField>, 'CONTENT_LENGTH': <enum GST_RTSP_HDR_CONTENT_LENGTH of type GstRtsp.RTSPHeaderField>, 'CONTENT_LOCATION': <enum GST_RTSP_HDR_CONTENT_LOCATION of type GstRtsp.RTSPHeaderField>, 'CONTENT_TYPE': <enum GST_RTSP_HDR_CONTENT_TYPE of type GstRtsp.RTSPHeaderField>, 'CSEQ': <enum GST_RTSP_HDR_CSEQ of type GstRtsp.RTSPHeaderField>, 'DATE': <enum GST_RTSP_HDR_DATE of type GstRtsp.RTSPHeaderField>, 'EXPIRES': <enum GST_RTSP_HDR_EXPIRES of type GstRtsp.RTSPHeaderField>, 'FROM': <enum GST_RTSP_HDR_FROM of type GstRtsp.RTSPHeaderField>, 'IF_MODIFIED_SINCE': <enum GST_RTSP_HDR_IF_MODIFIED_SINCE of type GstRtsp.RTSPHeaderField>, 'LAST_MODIFIED': <enum GST_RTSP_HDR_LAST_MODIFIED of type GstRtsp.RTSPHeaderField>, 'PROXY_AUTHENTICATE': <enum GST_RTSP_HDR_PROXY_AUTHENTICATE of type GstRtsp.RTSPHeaderField>, 'PROXY_REQUIRE': <enum GST_RTSP_HDR_PROXY_REQUIRE of type GstRtsp.RTSPHeaderField>, 'PUBLIC': <enum GST_RTSP_HDR_PUBLIC of type GstRtsp.RTSPHeaderField>, 'RANGE': <enum GST_RTSP_HDR_RANGE of type GstRtsp.RTSPHeaderField>, 'REFERER': <enum GST_RTSP_HDR_REFERER of type GstRtsp.RTSPHeaderField>, 'REQUIRE': <enum GST_RTSP_HDR_REQUIRE of type GstRtsp.RTSPHeaderField>, 'RETRY_AFTER': <enum GST_RTSP_HDR_RETRY_AFTER of type GstRtsp.RTSPHeaderField>, 'RTP_INFO': <enum GST_RTSP_HDR_RTP_INFO of type GstRtsp.RTSPHeaderField>, 'SCALE': <enum GST_RTSP_HDR_SCALE of type GstRtsp.RTSPHeaderField>, 'SESSION': <enum GST_RTSP_HDR_SESSION of type GstRtsp.RTSPHeaderField>, 'SERVER': <enum GST_RTSP_HDR_SERVER of type GstRtsp.RTSPHeaderField>, 'SPEED': <enum GST_RTSP_HDR_SPEED of type GstRtsp.RTSPHeaderField>, 'TRANSPORT': <enum GST_RTSP_HDR_TRANSPORT of type GstRtsp.RTSPHeaderField>, 'UNSUPPORTED': <enum GST_RTSP_HDR_UNSUPPORTED of type GstRtsp.RTSPHeaderField>, 'USER_AGENT': <enum GST_RTSP_HDR_USER_AGENT of type GstRtsp.RTSPHeaderField>, 'VIA': <enum GST_RTSP_HDR_VIA of type GstRtsp.RTSPHeaderField>, 'WWW_AUTHENTICATE': <enum GST_RTSP_HDR_WWW_AUTHENTICATE of type GstRtsp.RTSPHeaderField>, 'CLIENT_CHALLENGE': <enum GST_RTSP_HDR_CLIENT_CHALLENGE of type GstRtsp.RTSPHeaderField>, 'REAL_CHALLENGE1': <enum GST_RTSP_HDR_REAL_CHALLENGE1 of type GstRtsp.RTSPHeaderField>, 'REAL_CHALLENGE2': <enum GST_RTSP_HDR_REAL_CHALLENGE2 of type GstRtsp.RTSPHeaderField>, 'REAL_CHALLENGE3': <enum GST_RTSP_HDR_REAL_CHALLENGE3 of type GstRtsp.RTSPHeaderField>, 'SUBSCRIBE': <enum GST_RTSP_HDR_SUBSCRIBE of type GstRtsp.RTSPHeaderField>, 'ALERT': <enum GST_RTSP_HDR_ALERT of type GstRtsp.RTSPHeaderField>, 'CLIENT_ID': <enum GST_RTSP_HDR_CLIENT_ID of type GstRtsp.RTSPHeaderField>, 'COMPANY_ID': <enum GST_RTSP_HDR_COMPANY_ID of type GstRtsp.RTSPHeaderField>, 'GUID': <enum GST_RTSP_HDR_GUID of type GstRtsp.RTSPHeaderField>, 'REGION_DATA': <enum GST_RTSP_HDR_REGION_DATA of type GstRtsp.RTSPHeaderField>, 'MAX_ASM_WIDTH': <enum GST_RTSP_HDR_MAX_ASM_WIDTH of type GstRtsp.RTSPHeaderField>, 'LANGUAGE': <enum GST_RTSP_HDR_LANGUAGE of type GstRtsp.RTSPHeaderField>, 'PLAYER_START_TIME': <enum GST_RTSP_HDR_PLAYER_START_TIME of type GstRtsp.RTSPHeaderField>, 'LOCATION': <enum GST_RTSP_HDR_LOCATION of type GstRtsp.RTSPHeaderField>, 'ETAG': <enum GST_RTSP_HDR_ETAG of type GstRtsp.RTSPHeaderField>, 'IF_MATCH': <enum GST_RTSP_HDR_IF_MATCH of type GstRtsp.RTSPHeaderField>, 'ACCEPT_CHARSET': <enum GST_RTSP_HDR_ACCEPT_CHARSET of type GstRtsp.RTSPHeaderField>, 'SUPPORTED': <enum GST_RTSP_HDR_SUPPORTED of type GstRtsp.RTSPHeaderField>, 'VARY': <enum GST_RTSP_HDR_VARY of type GstRtsp.RTSPHeaderField>, 'X_ACCELERATE_STREAMING': <enum GST_RTSP_HDR_X_ACCELERATE_STREAMING of type GstRtsp.RTSPHeaderField>, 'X_ACCEPT_AUTHENT': <enum GST_RTSP_HDR_X_ACCEPT_AUTHENT of type GstRtsp.RTSPHeaderField>, 'X_ACCEPT_PROXY_AUTHENT': <enum GST_RTSP_HDR_X_ACCEPT_PROXY_AUTHENT of type GstRtsp.RTSPHeaderField>, 'X_BROADCAST_ID': <enum GST_RTSP_HDR_X_BROADCAST_ID of type GstRtsp.RTSPHeaderField>, 'X_BURST_STREAMING': <enum GST_RTSP_HDR_X_BURST_STREAMING of type GstRtsp.RTSPHeaderField>, 'X_NOTICE': <enum GST_RTSP_HDR_X_NOTICE of type GstRtsp.RTSPHeaderField>, 'X_PLAYER_LAG_TIME': <enum GST_RTSP_HDR_X_PLAYER_LAG_TIME of type GstRtsp.RTSPHeaderField>, 'X_PLAYLIST': <enum GST_RTSP_HDR_X_PLAYLIST of type GstRtsp.RTSPHeaderField>, 'X_PLAYLIST_CHANGE_NOTICE': <enum GST_RTSP_HDR_X_PLAYLIST_CHANGE_NOTICE of type GstRtsp.RTSPHeaderField>, 'X_PLAYLIST_GEN_ID': <enum GST_RTSP_HDR_X_PLAYLIST_GEN_ID of type GstRtsp.RTSPHeaderField>, 'X_PLAYLIST_SEEK_ID': <enum GST_RTSP_HDR_X_PLAYLIST_SEEK_ID of type GstRtsp.RTSPHeaderField>, 'X_PROXY_CLIENT_AGENT': <enum GST_RTSP_HDR_X_PROXY_CLIENT_AGENT of type GstRtsp.RTSPHeaderField>, 'X_PROXY_CLIENT_VERB': <enum GST_RTSP_HDR_X_PROXY_CLIENT_VERB of type GstRtsp.RTSPHeaderField>, 'X_RECEDING_PLAYLISTCHANGE': <enum GST_RTSP_HDR_X_RECEDING_PLAYLISTCHANGE of type GstRtsp.RTSPHeaderField>, 'X_RTP_INFO': <enum GST_RTSP_HDR_X_RTP_INFO of type GstRtsp.RTSPHeaderField>, 'X_STARTUPPROFILE': <enum GST_RTSP_HDR_X_STARTUPPROFILE of type GstRtsp.RTSPHeaderField>, 'TIMESTAMP': <enum GST_RTSP_HDR_TIMESTAMP of type GstRtsp.RTSPHeaderField>, 'AUTHENTICATION_INFO': <enum GST_RTSP_HDR_AUTHENTICATION_INFO of type GstRtsp.RTSPHeaderField>, 'HOST': <enum GST_RTSP_HDR_HOST of type GstRtsp.RTSPHeaderField>, 'PRAGMA': <enum GST_RTSP_HDR_PRAGMA of type GstRtsp.RTSPHeaderField>, 'X_SERVER_IP_ADDRESS': <enum GST_RTSP_HDR_X_SERVER_IP_ADDRESS of type GstRtsp.RTSPHeaderField>, 'X_SESSIONCOOKIE': <enum GST_RTSP_HDR_X_SESSIONCOOKIE of type GstRtsp.RTSPHeaderField>, 'RTCP_INTERVAL': <enum GST_RTSP_HDR_RTCP_INTERVAL of type GstRtsp.RTSPHeaderField>, 'KEYMGMT': <enum GST_RTSP_HDR_KEYMGMT of type GstRtsp.RTSPHeaderField>, 'PIPELINED_REQUESTS': <enum GST_RTSP_HDR_PIPELINED_REQUESTS of type GstRtsp.RTSPHeaderField>, 'MEDIA_PROPERTIES': <enum GST_RTSP_HDR_MEDIA_PROPERTIES of type GstRtsp.RTSPHeaderField>, 'SEEK_STYLE': <enum GST_RTSP_HDR_SEEK_STYLE of type GstRtsp.RTSPHeaderField>, 'ACCEPT_RANGES': <enum GST_RTSP_HDR_ACCEPT_RANGES of type GstRtsp.RTSPHeaderField>, 'FRAMES': <enum GST_RTSP_HDR_FRAMES of type GstRtsp.RTSPHeaderField>, 'RATE_CONTROL': <enum GST_RTSP_HDR_RATE_CONTROL of type GstRtsp.RTSPHeaderField>, 'LAST': <enum GST_RTSP_HDR_LAST of type GstRtsp.RTSPHeaderField>})"
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
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
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
    }
    __gtype__ = None # (!) real value is '<GType GstRTSPHeaderField (93854382881968)>'
    __info__ = gi.EnumInfo(RTSPHeaderField)


