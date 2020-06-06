# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class DebugColorFlags(__gobject.GFlags):
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


    BG_BLACK = 0
    BG_BLUE = 64
    BG_CYAN = 96
    BG_GREEN = 32
    BG_MAGENTA = 80
    BG_RED = 16
    BG_WHITE = 112
    BG_YELLOW = 48
    BOLD = 256
    FG_BLACK = 0
    FG_BLUE = 4
    FG_CYAN = 6
    FG_GREEN = 2
    FG_MAGENTA = 5
    FG_RED = 1
    FG_WHITE = 7
    FG_YELLOW = 3
    UNDERLINE = 512
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gst', '__dict__': <attribute '__dict__' of 'DebugColorFlags' objects>, '__doc__': None, '__gtype__': <GType GstDebugColorFlags (94058977584544)>, '__flags_values__': {0: <flags 0 of type Gst.DebugColorFlags>, 1: <flags GST_DEBUG_FG_RED of type Gst.DebugColorFlags>, 2: <flags GST_DEBUG_FG_GREEN of type Gst.DebugColorFlags>, 3: <flags GST_DEBUG_FG_RED | GST_DEBUG_FG_GREEN | GST_DEBUG_FG_YELLOW of type Gst.DebugColorFlags>, 4: <flags GST_DEBUG_FG_BLUE of type Gst.DebugColorFlags>, 5: <flags GST_DEBUG_FG_RED | GST_DEBUG_FG_BLUE | GST_DEBUG_FG_MAGENTA of type Gst.DebugColorFlags>, 6: <flags GST_DEBUG_FG_GREEN | GST_DEBUG_FG_BLUE | GST_DEBUG_FG_CYAN of type Gst.DebugColorFlags>, 7: <flags GST_DEBUG_FG_RED | GST_DEBUG_FG_GREEN | GST_DEBUG_FG_YELLOW | GST_DEBUG_FG_BLUE | GST_DEBUG_FG_MAGENTA | GST_DEBUG_FG_CYAN | GST_DEBUG_FG_WHITE of type Gst.DebugColorFlags>, 16: <flags GST_DEBUG_BG_RED of type Gst.DebugColorFlags>, 32: <flags GST_DEBUG_BG_GREEN of type Gst.DebugColorFlags>, 48: <flags GST_DEBUG_BG_RED | GST_DEBUG_BG_GREEN | GST_DEBUG_BG_YELLOW of type Gst.DebugColorFlags>, 64: <flags GST_DEBUG_BG_BLUE of type Gst.DebugColorFlags>, 80: <flags GST_DEBUG_BG_RED | GST_DEBUG_BG_BLUE | GST_DEBUG_BG_MAGENTA of type Gst.DebugColorFlags>, 96: <flags GST_DEBUG_BG_GREEN | GST_DEBUG_BG_BLUE | GST_DEBUG_BG_CYAN of type Gst.DebugColorFlags>, 112: <flags GST_DEBUG_BG_RED | GST_DEBUG_BG_GREEN | GST_DEBUG_BG_YELLOW | GST_DEBUG_BG_BLUE | GST_DEBUG_BG_MAGENTA | GST_DEBUG_BG_CYAN | GST_DEBUG_BG_WHITE of type Gst.DebugColorFlags>, 256: <flags GST_DEBUG_BOLD of type Gst.DebugColorFlags>, 512: <flags GST_DEBUG_UNDERLINE of type Gst.DebugColorFlags>}, '__info__': gi.EnumInfo(DebugColorFlags), 'FG_BLACK': <flags 0 of type Gst.DebugColorFlags>, 'FG_RED': <flags GST_DEBUG_FG_RED of type Gst.DebugColorFlags>, 'FG_GREEN': <flags GST_DEBUG_FG_GREEN of type Gst.DebugColorFlags>, 'FG_YELLOW': <flags GST_DEBUG_FG_RED | GST_DEBUG_FG_GREEN | GST_DEBUG_FG_YELLOW of type Gst.DebugColorFlags>, 'FG_BLUE': <flags GST_DEBUG_FG_BLUE of type Gst.DebugColorFlags>, 'FG_MAGENTA': <flags GST_DEBUG_FG_RED | GST_DEBUG_FG_BLUE | GST_DEBUG_FG_MAGENTA of type Gst.DebugColorFlags>, 'FG_CYAN': <flags GST_DEBUG_FG_GREEN | GST_DEBUG_FG_BLUE | GST_DEBUG_FG_CYAN of type Gst.DebugColorFlags>, 'FG_WHITE': <flags GST_DEBUG_FG_RED | GST_DEBUG_FG_GREEN | GST_DEBUG_FG_YELLOW | GST_DEBUG_FG_BLUE | GST_DEBUG_FG_MAGENTA | GST_DEBUG_FG_CYAN | GST_DEBUG_FG_WHITE of type Gst.DebugColorFlags>, 'BG_BLACK': <flags 0 of type Gst.DebugColorFlags>, 'BG_RED': <flags GST_DEBUG_BG_RED of type Gst.DebugColorFlags>, 'BG_GREEN': <flags GST_DEBUG_BG_GREEN of type Gst.DebugColorFlags>, 'BG_YELLOW': <flags GST_DEBUG_BG_RED | GST_DEBUG_BG_GREEN | GST_DEBUG_BG_YELLOW of type Gst.DebugColorFlags>, 'BG_BLUE': <flags GST_DEBUG_BG_BLUE of type Gst.DebugColorFlags>, 'BG_MAGENTA': <flags GST_DEBUG_BG_RED | GST_DEBUG_BG_BLUE | GST_DEBUG_BG_MAGENTA of type Gst.DebugColorFlags>, 'BG_CYAN': <flags GST_DEBUG_BG_GREEN | GST_DEBUG_BG_BLUE | GST_DEBUG_BG_CYAN of type Gst.DebugColorFlags>, 'BG_WHITE': <flags GST_DEBUG_BG_RED | GST_DEBUG_BG_GREEN | GST_DEBUG_BG_YELLOW | GST_DEBUG_BG_BLUE | GST_DEBUG_BG_MAGENTA | GST_DEBUG_BG_CYAN | GST_DEBUG_BG_WHITE of type Gst.DebugColorFlags>, 'BOLD': <flags GST_DEBUG_BOLD of type Gst.DebugColorFlags>, 'UNDERLINE': <flags GST_DEBUG_UNDERLINE of type Gst.DebugColorFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        16: 16,
        32: 32,
        48: 48,
        64: 64,
        80: 80,
        96: 96,
        112: 112,
        256: 256,
        512: 512,
    }
    __gtype__ = None # (!) real value is '<GType GstDebugColorFlags (94058977584544)>'
    __info__ = gi.EnumInfo(DebugColorFlags)


