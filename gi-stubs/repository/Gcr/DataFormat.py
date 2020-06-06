# encoding: utf-8
# module gi.repository.Gcr
# from /usr/lib64/girepository-1.0/Gcr-3.typelib
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
import gi.repository.Gck as __gi_repository_Gck
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class DataFormat(__gobject.GEnum):
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


    ALL = -1
    BASE64_SPKAC = 456
    DER_CERTIFICATE_X509 = 200
    DER_PKCS10 = 450
    DER_PKCS12 = 500
    DER_PKCS7 = 300
    DER_PKCS8 = 400
    DER_PKCS8_ENCRYPTED = 402
    DER_PKCS8_PLAIN = 401
    DER_PRIVATE_KEY = 100
    DER_PRIVATE_KEY_DSA = 102
    DER_PRIVATE_KEY_EC = 103
    DER_PRIVATE_KEY_RSA = 101
    DER_SPKAC = 455
    DER_SUBJECT_PUBLIC_KEY = 150
    INVALID = 0
    OPENPGP_ARMOR = 701
    OPENPGP_PACKET = 700
    OPENSSH_PUBLIC = 600
    PEM = 1000
    PEM_CERTIFICATE_X509 = 1003
    PEM_PKCS10 = 1009
    PEM_PKCS12 = 1007
    PEM_PKCS7 = 1004
    PEM_PKCS8_ENCRYPTED = 1006
    PEM_PKCS8_PLAIN = 1005
    PEM_PRIVATE_KEY = 1008
    PEM_PRIVATE_KEY_DSA = 1002
    PEM_PRIVATE_KEY_EC = 1010
    PEM_PRIVATE_KEY_RSA = 1001
    PEM_PUBLIC_KEY = 1011
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gcr', '__dict__': <attribute '__dict__' of 'DataFormat' objects>, '__doc__': None, '__gtype__': <GType PyGcrDataFormat (94112497672496)>, '__enum_values__': {-1: <enum GCR_FORMAT_ALL of type Gcr.DataFormat>, 0: <enum GCR_FORMAT_INVALID of type Gcr.DataFormat>, 100: <enum GCR_FORMAT_DER_PRIVATE_KEY of type Gcr.DataFormat>, 101: <enum GCR_FORMAT_DER_PRIVATE_KEY_RSA of type Gcr.DataFormat>, 102: <enum GCR_FORMAT_DER_PRIVATE_KEY_DSA of type Gcr.DataFormat>, 103: <enum GCR_FORMAT_DER_PRIVATE_KEY_EC of type Gcr.DataFormat>, 150: <enum GCR_FORMAT_DER_SUBJECT_PUBLIC_KEY of type Gcr.DataFormat>, 200: <enum GCR_FORMAT_DER_CERTIFICATE_X509 of type Gcr.DataFormat>, 300: <enum GCR_FORMAT_DER_PKCS7 of type Gcr.DataFormat>, 400: <enum GCR_FORMAT_DER_PKCS8 of type Gcr.DataFormat>, 401: <enum GCR_FORMAT_DER_PKCS8_PLAIN of type Gcr.DataFormat>, 402: <enum GCR_FORMAT_DER_PKCS8_ENCRYPTED of type Gcr.DataFormat>, 450: <enum GCR_FORMAT_DER_PKCS10 of type Gcr.DataFormat>, 455: <enum GCR_FORMAT_DER_SPKAC of type Gcr.DataFormat>, 456: <enum GCR_FORMAT_BASE64_SPKAC of type Gcr.DataFormat>, 500: <enum GCR_FORMAT_DER_PKCS12 of type Gcr.DataFormat>, 600: <enum GCR_FORMAT_OPENSSH_PUBLIC of type Gcr.DataFormat>, 700: <enum GCR_FORMAT_OPENPGP_PACKET of type Gcr.DataFormat>, 701: <enum GCR_FORMAT_OPENPGP_ARMOR of type Gcr.DataFormat>, 1000: <enum GCR_FORMAT_PEM of type Gcr.DataFormat>, 1001: <enum GCR_FORMAT_PEM_PRIVATE_KEY_RSA of type Gcr.DataFormat>, 1002: <enum GCR_FORMAT_PEM_PRIVATE_KEY_DSA of type Gcr.DataFormat>, 1003: <enum GCR_FORMAT_PEM_CERTIFICATE_X509 of type Gcr.DataFormat>, 1004: <enum GCR_FORMAT_PEM_PKCS7 of type Gcr.DataFormat>, 1005: <enum GCR_FORMAT_PEM_PKCS8_PLAIN of type Gcr.DataFormat>, 1006: <enum GCR_FORMAT_PEM_PKCS8_ENCRYPTED of type Gcr.DataFormat>, 1007: <enum GCR_FORMAT_PEM_PKCS12 of type Gcr.DataFormat>, 1008: <enum GCR_FORMAT_PEM_PRIVATE_KEY of type Gcr.DataFormat>, 1009: <enum GCR_FORMAT_PEM_PKCS10 of type Gcr.DataFormat>, 1010: <enum GCR_FORMAT_PEM_PRIVATE_KEY_EC of type Gcr.DataFormat>, 1011: <enum GCR_FORMAT_PEM_PUBLIC_KEY of type Gcr.DataFormat>}, '__info__': gi.EnumInfo(DataFormat), 'ALL': <enum GCR_FORMAT_ALL of type Gcr.DataFormat>, 'INVALID': <enum GCR_FORMAT_INVALID of type Gcr.DataFormat>, 'DER_PRIVATE_KEY': <enum GCR_FORMAT_DER_PRIVATE_KEY of type Gcr.DataFormat>, 'DER_PRIVATE_KEY_RSA': <enum GCR_FORMAT_DER_PRIVATE_KEY_RSA of type Gcr.DataFormat>, 'DER_PRIVATE_KEY_DSA': <enum GCR_FORMAT_DER_PRIVATE_KEY_DSA of type Gcr.DataFormat>, 'DER_PRIVATE_KEY_EC': <enum GCR_FORMAT_DER_PRIVATE_KEY_EC of type Gcr.DataFormat>, 'DER_SUBJECT_PUBLIC_KEY': <enum GCR_FORMAT_DER_SUBJECT_PUBLIC_KEY of type Gcr.DataFormat>, 'DER_CERTIFICATE_X509': <enum GCR_FORMAT_DER_CERTIFICATE_X509 of type Gcr.DataFormat>, 'DER_PKCS7': <enum GCR_FORMAT_DER_PKCS7 of type Gcr.DataFormat>, 'DER_PKCS8': <enum GCR_FORMAT_DER_PKCS8 of type Gcr.DataFormat>, 'DER_PKCS8_PLAIN': <enum GCR_FORMAT_DER_PKCS8_PLAIN of type Gcr.DataFormat>, 'DER_PKCS8_ENCRYPTED': <enum GCR_FORMAT_DER_PKCS8_ENCRYPTED of type Gcr.DataFormat>, 'DER_PKCS10': <enum GCR_FORMAT_DER_PKCS10 of type Gcr.DataFormat>, 'DER_SPKAC': <enum GCR_FORMAT_DER_SPKAC of type Gcr.DataFormat>, 'BASE64_SPKAC': <enum GCR_FORMAT_BASE64_SPKAC of type Gcr.DataFormat>, 'DER_PKCS12': <enum GCR_FORMAT_DER_PKCS12 of type Gcr.DataFormat>, 'OPENSSH_PUBLIC': <enum GCR_FORMAT_OPENSSH_PUBLIC of type Gcr.DataFormat>, 'OPENPGP_PACKET': <enum GCR_FORMAT_OPENPGP_PACKET of type Gcr.DataFormat>, 'OPENPGP_ARMOR': <enum GCR_FORMAT_OPENPGP_ARMOR of type Gcr.DataFormat>, 'PEM': <enum GCR_FORMAT_PEM of type Gcr.DataFormat>, 'PEM_PRIVATE_KEY_RSA': <enum GCR_FORMAT_PEM_PRIVATE_KEY_RSA of type Gcr.DataFormat>, 'PEM_PRIVATE_KEY_DSA': <enum GCR_FORMAT_PEM_PRIVATE_KEY_DSA of type Gcr.DataFormat>, 'PEM_CERTIFICATE_X509': <enum GCR_FORMAT_PEM_CERTIFICATE_X509 of type Gcr.DataFormat>, 'PEM_PKCS7': <enum GCR_FORMAT_PEM_PKCS7 of type Gcr.DataFormat>, 'PEM_PKCS8_PLAIN': <enum GCR_FORMAT_PEM_PKCS8_PLAIN of type Gcr.DataFormat>, 'PEM_PKCS8_ENCRYPTED': <enum GCR_FORMAT_PEM_PKCS8_ENCRYPTED of type Gcr.DataFormat>, 'PEM_PKCS12': <enum GCR_FORMAT_PEM_PKCS12 of type Gcr.DataFormat>, 'PEM_PRIVATE_KEY': <enum GCR_FORMAT_PEM_PRIVATE_KEY of type Gcr.DataFormat>, 'PEM_PKCS10': <enum GCR_FORMAT_PEM_PKCS10 of type Gcr.DataFormat>, 'PEM_PRIVATE_KEY_EC': <enum GCR_FORMAT_PEM_PRIVATE_KEY_EC of type Gcr.DataFormat>, 'PEM_PUBLIC_KEY': <enum GCR_FORMAT_PEM_PUBLIC_KEY of type Gcr.DataFormat>})"
    __enum_values__ = {
        -1: -1,
        0: 0,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        150: 150,
        200: 200,
        300: 300,
        400: 400,
        401: 401,
        402: 402,
        450: 450,
        455: 455,
        456: 456,
        500: 500,
        600: 600,
        700: 700,
        701: 701,
        1000: 1000,
        1001: 1001,
        1002: 1002,
        1003: 1003,
        1004: 1004,
        1005: 1005,
        1006: 1006,
        1007: 1007,
        1008: 1008,
        1009: 1009,
        1010: 1010,
        1011: 1011,
    }
    __gtype__ = None # (!) real value is '<GType PyGcrDataFormat (94112497672496)>'
    __info__ = gi.EnumInfo(DataFormat)


