# encoding: utf-8
# module gi.repository.Grl
# from /usr/lib64/girepository-1.0/Grl-0.3.typelib
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
import gobject as __gobject


class CoreError(__gobject.GEnum):
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


    AUTHENTICATION_TOKEN = 19
    BROWSE_FAILED = 1
    CONFIG_FAILED = 12
    CONFIG_LOAD_FAILED = 11
    LOAD_PLUGIN_FAILED = 14
    MEDIA_FROM_URI_FAILED = 10
    MEDIA_NOT_FOUND = 6
    NOTIFY_CHANGED_FAILED = 17
    OPERATION_CANCELLED = 18
    QUERY_FAILED = 4
    REGISTER_METADATA_KEY_FAILED = 16
    REMOVE_FAILED = 9
    RESOLVE_FAILED = 5
    SEARCH_FAILED = 2
    SEARCH_NULL_UNSUPPORTED = 3
    STORE_FAILED = 7
    STORE_METADATA_FAILED = 8
    UNLOAD_PLUGIN_FAILED = 15
    UNREGISTER_SOURCE_FAILED = 13
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Grl', '__dict__': <attribute '__dict__' of 'CoreError' objects>, '__doc__': None, '__gtype__': <GType PyGrlCoreError (94188897453280)>, '__enum_values__': {1: <enum GRL_CORE_ERROR_BROWSE_FAILED of type Grl.CoreError>, 2: <enum GRL_CORE_ERROR_SEARCH_FAILED of type Grl.CoreError>, 3: <enum GRL_CORE_ERROR_SEARCH_NULL_UNSUPPORTED of type Grl.CoreError>, 4: <enum GRL_CORE_ERROR_QUERY_FAILED of type Grl.CoreError>, 5: <enum GRL_CORE_ERROR_RESOLVE_FAILED of type Grl.CoreError>, 6: <enum GRL_CORE_ERROR_MEDIA_NOT_FOUND of type Grl.CoreError>, 7: <enum GRL_CORE_ERROR_STORE_FAILED of type Grl.CoreError>, 8: <enum GRL_CORE_ERROR_STORE_METADATA_FAILED of type Grl.CoreError>, 9: <enum GRL_CORE_ERROR_REMOVE_FAILED of type Grl.CoreError>, 10: <enum GRL_CORE_ERROR_MEDIA_FROM_URI_FAILED of type Grl.CoreError>, 11: <enum GRL_CORE_ERROR_CONFIG_LOAD_FAILED of type Grl.CoreError>, 12: <enum GRL_CORE_ERROR_CONFIG_FAILED of type Grl.CoreError>, 13: <enum GRL_CORE_ERROR_UNREGISTER_SOURCE_FAILED of type Grl.CoreError>, 14: <enum GRL_CORE_ERROR_LOAD_PLUGIN_FAILED of type Grl.CoreError>, 15: <enum GRL_CORE_ERROR_UNLOAD_PLUGIN_FAILED of type Grl.CoreError>, 16: <enum GRL_CORE_ERROR_REGISTER_METADATA_KEY_FAILED of type Grl.CoreError>, 17: <enum GRL_CORE_ERROR_NOTIFY_CHANGED_FAILED of type Grl.CoreError>, 18: <enum GRL_CORE_ERROR_OPERATION_CANCELLED of type Grl.CoreError>, 19: <enum GRL_CORE_ERROR_AUTHENTICATION_TOKEN of type Grl.CoreError>}, '__info__': gi.EnumInfo(CoreError), 'BROWSE_FAILED': <enum GRL_CORE_ERROR_BROWSE_FAILED of type Grl.CoreError>, 'SEARCH_FAILED': <enum GRL_CORE_ERROR_SEARCH_FAILED of type Grl.CoreError>, 'SEARCH_NULL_UNSUPPORTED': <enum GRL_CORE_ERROR_SEARCH_NULL_UNSUPPORTED of type Grl.CoreError>, 'QUERY_FAILED': <enum GRL_CORE_ERROR_QUERY_FAILED of type Grl.CoreError>, 'RESOLVE_FAILED': <enum GRL_CORE_ERROR_RESOLVE_FAILED of type Grl.CoreError>, 'MEDIA_NOT_FOUND': <enum GRL_CORE_ERROR_MEDIA_NOT_FOUND of type Grl.CoreError>, 'STORE_FAILED': <enum GRL_CORE_ERROR_STORE_FAILED of type Grl.CoreError>, 'STORE_METADATA_FAILED': <enum GRL_CORE_ERROR_STORE_METADATA_FAILED of type Grl.CoreError>, 'REMOVE_FAILED': <enum GRL_CORE_ERROR_REMOVE_FAILED of type Grl.CoreError>, 'MEDIA_FROM_URI_FAILED': <enum GRL_CORE_ERROR_MEDIA_FROM_URI_FAILED of type Grl.CoreError>, 'CONFIG_LOAD_FAILED': <enum GRL_CORE_ERROR_CONFIG_LOAD_FAILED of type Grl.CoreError>, 'CONFIG_FAILED': <enum GRL_CORE_ERROR_CONFIG_FAILED of type Grl.CoreError>, 'UNREGISTER_SOURCE_FAILED': <enum GRL_CORE_ERROR_UNREGISTER_SOURCE_FAILED of type Grl.CoreError>, 'LOAD_PLUGIN_FAILED': <enum GRL_CORE_ERROR_LOAD_PLUGIN_FAILED of type Grl.CoreError>, 'UNLOAD_PLUGIN_FAILED': <enum GRL_CORE_ERROR_UNLOAD_PLUGIN_FAILED of type Grl.CoreError>, 'REGISTER_METADATA_KEY_FAILED': <enum GRL_CORE_ERROR_REGISTER_METADATA_KEY_FAILED of type Grl.CoreError>, 'NOTIFY_CHANGED_FAILED': <enum GRL_CORE_ERROR_NOTIFY_CHANGED_FAILED of type Grl.CoreError>, 'OPERATION_CANCELLED': <enum GRL_CORE_ERROR_OPERATION_CANCELLED of type Grl.CoreError>, 'AUTHENTICATION_TOKEN': <enum GRL_CORE_ERROR_AUTHENTICATION_TOKEN of type Grl.CoreError>})"
    __enum_values__ = {
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
    }
    __gtype__ = None # (!) real value is '<GType PyGrlCoreError (94188897453280)>'
    __info__ = gi.EnumInfo(CoreError)


