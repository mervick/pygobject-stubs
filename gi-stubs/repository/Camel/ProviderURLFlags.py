# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class ProviderURLFlags(__gobject.GFlags):
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
        """ Helper for pickle. """
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

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ALLOW_AUTH = 2
    ALLOW_HOST = 8
    ALLOW_PASSWORD = 4
    ALLOW_PATH = 32
    ALLOW_PORT = 16
    ALLOW_USER = 1
    FRAGMENT_IS_PATH = 1073741824
    HIDDEN_AUTH = 131072
    HIDDEN_HOST = 524288
    HIDDEN_PASSWORD = 262144
    HIDDEN_PATH = 2097152
    HIDDEN_PORT = 1048576
    HIDDEN_USER = 65536
    NEED_AUTH = 512
    NEED_HOST = 2048
    NEED_PASSWORD = 1024
    NEED_PATH = 8192
    NEED_PATH_DIR = 16384
    NEED_PORT = 4096
    NEED_USER = 256
    PATH_IS_ABSOLUTE = 2147483648
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Camel', '__dict__': <attribute '__dict__' of 'ProviderURLFlags' objects>, '__doc__': None, '__gtype__': <GType PyCamelProviderURLFlags (94124524141392)>, '__flags_values__': {1: <flags CAMEL_URL_ALLOW_USER of type Camel.ProviderURLFlags>, 2: <flags CAMEL_URL_ALLOW_AUTH of type Camel.ProviderURLFlags>, 4: <flags CAMEL_URL_ALLOW_PASSWORD of type Camel.ProviderURLFlags>, 8: <flags CAMEL_URL_ALLOW_HOST of type Camel.ProviderURLFlags>, 16: <flags CAMEL_URL_ALLOW_PORT of type Camel.ProviderURLFlags>, 32: <flags CAMEL_URL_ALLOW_PATH of type Camel.ProviderURLFlags>, 256: <flags CAMEL_URL_NEED_USER of type Camel.ProviderURLFlags>, 512: <flags CAMEL_URL_NEED_AUTH of type Camel.ProviderURLFlags>, 1024: <flags CAMEL_URL_NEED_PASSWORD of type Camel.ProviderURLFlags>, 2048: <flags CAMEL_URL_NEED_HOST of type Camel.ProviderURLFlags>, 4096: <flags CAMEL_URL_NEED_PORT of type Camel.ProviderURLFlags>, 8192: <flags CAMEL_URL_NEED_PATH of type Camel.ProviderURLFlags>, 16384: <flags CAMEL_URL_NEED_PATH_DIR of type Camel.ProviderURLFlags>, 65536: <flags CAMEL_URL_HIDDEN_USER of type Camel.ProviderURLFlags>, 131072: <flags CAMEL_URL_HIDDEN_AUTH of type Camel.ProviderURLFlags>, 262144: <flags CAMEL_URL_HIDDEN_PASSWORD of type Camel.ProviderURLFlags>, 524288: <flags CAMEL_URL_HIDDEN_HOST of type Camel.ProviderURLFlags>, 1048576: <flags CAMEL_URL_HIDDEN_PORT of type Camel.ProviderURLFlags>, 2097152: <flags CAMEL_URL_HIDDEN_PATH of type Camel.ProviderURLFlags>, 1073741824: <flags CAMEL_URL_FRAGMENT_IS_PATH of type Camel.ProviderURLFlags>, 2147483648: <flags CAMEL_URL_PATH_IS_ABSOLUTE of type Camel.ProviderURLFlags>}, '__info__': gi.EnumInfo(ProviderURLFlags), 'ALLOW_USER': <flags CAMEL_URL_ALLOW_USER of type Camel.ProviderURLFlags>, 'ALLOW_AUTH': <flags CAMEL_URL_ALLOW_AUTH of type Camel.ProviderURLFlags>, 'ALLOW_PASSWORD': <flags CAMEL_URL_ALLOW_PASSWORD of type Camel.ProviderURLFlags>, 'ALLOW_HOST': <flags CAMEL_URL_ALLOW_HOST of type Camel.ProviderURLFlags>, 'ALLOW_PORT': <flags CAMEL_URL_ALLOW_PORT of type Camel.ProviderURLFlags>, 'ALLOW_PATH': <flags CAMEL_URL_ALLOW_PATH of type Camel.ProviderURLFlags>, 'NEED_USER': <flags CAMEL_URL_NEED_USER of type Camel.ProviderURLFlags>, 'NEED_AUTH': <flags CAMEL_URL_NEED_AUTH of type Camel.ProviderURLFlags>, 'NEED_PASSWORD': <flags CAMEL_URL_NEED_PASSWORD of type Camel.ProviderURLFlags>, 'NEED_HOST': <flags CAMEL_URL_NEED_HOST of type Camel.ProviderURLFlags>, 'NEED_PORT': <flags CAMEL_URL_NEED_PORT of type Camel.ProviderURLFlags>, 'NEED_PATH': <flags CAMEL_URL_NEED_PATH of type Camel.ProviderURLFlags>, 'NEED_PATH_DIR': <flags CAMEL_URL_NEED_PATH_DIR of type Camel.ProviderURLFlags>, 'HIDDEN_USER': <flags CAMEL_URL_HIDDEN_USER of type Camel.ProviderURLFlags>, 'HIDDEN_AUTH': <flags CAMEL_URL_HIDDEN_AUTH of type Camel.ProviderURLFlags>, 'HIDDEN_PASSWORD': <flags CAMEL_URL_HIDDEN_PASSWORD of type Camel.ProviderURLFlags>, 'HIDDEN_HOST': <flags CAMEL_URL_HIDDEN_HOST of type Camel.ProviderURLFlags>, 'HIDDEN_PORT': <flags CAMEL_URL_HIDDEN_PORT of type Camel.ProviderURLFlags>, 'HIDDEN_PATH': <flags CAMEL_URL_HIDDEN_PATH of type Camel.ProviderURLFlags>, 'FRAGMENT_IS_PATH': <flags CAMEL_URL_FRAGMENT_IS_PATH of type Camel.ProviderURLFlags>, 'PATH_IS_ABSOLUTE': <flags CAMEL_URL_PATH_IS_ABSOLUTE of type Camel.ProviderURLFlags>})"
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        4096: 4096,
        8192: 8192,
        16384: 16384,
        65536: 65536,
        131072: 131072,
        262144: 262144,
        524288: 524288,
        1048576: 1048576,
        2097152: 2097152,
        1073741824: 1073741824,
        2147483648: 2147483648,
    }
    __gtype__ = None # (!) real value is '<GType PyCamelProviderURLFlags (94124524141392)>'
    __info__ = gi.EnumInfo(ProviderURLFlags)


