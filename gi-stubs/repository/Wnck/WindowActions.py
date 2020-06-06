# encoding: utf-8
# module gi.repository.Wnck
# from /usr/lib64/girepository-1.0/Wnck-3.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class WindowActions(__gobject.GFlags):
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


    ABOVE = 131072
    BELOW = 262144
    CHANGE_WORKSPACE = 64
    CLOSE = 128
    FULLSCREEN = 65536
    MAXIMIZE = 16384
    MAXIMIZE_HORIZONTALLY = 16
    MAXIMIZE_VERTICALLY = 32
    MINIMIZE = 4096
    MOVE = 1
    RESIZE = 2
    SHADE = 4
    STICK = 8
    UNMAXIMIZE = 32768
    UNMAXIMIZE_HORIZONTALLY = 256
    UNMAXIMIZE_VERTICALLY = 512
    UNMINIMIZE = 8192
    UNSHADE = 1024
    UNSTICK = 2048
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Wnck', '__dict__': <attribute '__dict__' of 'WindowActions' objects>, '__doc__': None, '__gtype__': <GType WnckWindowActions (94401669338896)>, '__flags_values__': {1: <flags WNCK_WINDOW_ACTION_MOVE of type Wnck.WindowActions>, 2: <flags WNCK_WINDOW_ACTION_RESIZE of type Wnck.WindowActions>, 4: <flags WNCK_WINDOW_ACTION_SHADE of type Wnck.WindowActions>, 8: <flags WNCK_WINDOW_ACTION_STICK of type Wnck.WindowActions>, 16: <flags WNCK_WINDOW_ACTION_MAXIMIZE_HORIZONTALLY of type Wnck.WindowActions>, 32: <flags WNCK_WINDOW_ACTION_MAXIMIZE_VERTICALLY of type Wnck.WindowActions>, 64: <flags WNCK_WINDOW_ACTION_CHANGE_WORKSPACE of type Wnck.WindowActions>, 128: <flags WNCK_WINDOW_ACTION_CLOSE of type Wnck.WindowActions>, 256: <flags WNCK_WINDOW_ACTION_UNMAXIMIZE_HORIZONTALLY of type Wnck.WindowActions>, 512: <flags WNCK_WINDOW_ACTION_UNMAXIMIZE_VERTICALLY of type Wnck.WindowActions>, 1024: <flags WNCK_WINDOW_ACTION_UNSHADE of type Wnck.WindowActions>, 2048: <flags WNCK_WINDOW_ACTION_UNSTICK of type Wnck.WindowActions>, 4096: <flags WNCK_WINDOW_ACTION_MINIMIZE of type Wnck.WindowActions>, 8192: <flags WNCK_WINDOW_ACTION_UNMINIMIZE of type Wnck.WindowActions>, 16384: <flags WNCK_WINDOW_ACTION_MAXIMIZE of type Wnck.WindowActions>, 32768: <flags WNCK_WINDOW_ACTION_UNMAXIMIZE of type Wnck.WindowActions>, 65536: <flags WNCK_WINDOW_ACTION_FULLSCREEN of type Wnck.WindowActions>, 131072: <flags WNCK_WINDOW_ACTION_ABOVE of type Wnck.WindowActions>, 262144: <flags WNCK_WINDOW_ACTION_BELOW of type Wnck.WindowActions>}, '__info__': gi.EnumInfo(WindowActions), 'MOVE': <flags WNCK_WINDOW_ACTION_MOVE of type Wnck.WindowActions>, 'RESIZE': <flags WNCK_WINDOW_ACTION_RESIZE of type Wnck.WindowActions>, 'SHADE': <flags WNCK_WINDOW_ACTION_SHADE of type Wnck.WindowActions>, 'STICK': <flags WNCK_WINDOW_ACTION_STICK of type Wnck.WindowActions>, 'MAXIMIZE_HORIZONTALLY': <flags WNCK_WINDOW_ACTION_MAXIMIZE_HORIZONTALLY of type Wnck.WindowActions>, 'MAXIMIZE_VERTICALLY': <flags WNCK_WINDOW_ACTION_MAXIMIZE_VERTICALLY of type Wnck.WindowActions>, 'CHANGE_WORKSPACE': <flags WNCK_WINDOW_ACTION_CHANGE_WORKSPACE of type Wnck.WindowActions>, 'CLOSE': <flags WNCK_WINDOW_ACTION_CLOSE of type Wnck.WindowActions>, 'UNMAXIMIZE_HORIZONTALLY': <flags WNCK_WINDOW_ACTION_UNMAXIMIZE_HORIZONTALLY of type Wnck.WindowActions>, 'UNMAXIMIZE_VERTICALLY': <flags WNCK_WINDOW_ACTION_UNMAXIMIZE_VERTICALLY of type Wnck.WindowActions>, 'UNSHADE': <flags WNCK_WINDOW_ACTION_UNSHADE of type Wnck.WindowActions>, 'UNSTICK': <flags WNCK_WINDOW_ACTION_UNSTICK of type Wnck.WindowActions>, 'MINIMIZE': <flags WNCK_WINDOW_ACTION_MINIMIZE of type Wnck.WindowActions>, 'UNMINIMIZE': <flags WNCK_WINDOW_ACTION_UNMINIMIZE of type Wnck.WindowActions>, 'MAXIMIZE': <flags WNCK_WINDOW_ACTION_MAXIMIZE of type Wnck.WindowActions>, 'UNMAXIMIZE': <flags WNCK_WINDOW_ACTION_UNMAXIMIZE of type Wnck.WindowActions>, 'FULLSCREEN': <flags WNCK_WINDOW_ACTION_FULLSCREEN of type Wnck.WindowActions>, 'ABOVE': <flags WNCK_WINDOW_ACTION_ABOVE of type Wnck.WindowActions>, 'BELOW': <flags WNCK_WINDOW_ACTION_BELOW of type Wnck.WindowActions>})"
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        128: 128,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        4096: 4096,
        8192: 8192,
        16384: 16384,
        32768: 32768,
        65536: 65536,
        131072: 131072,
        262144: 262144,
    }
    __gtype__ = None # (!) real value is '<GType WnckWindowActions (94401669338896)>'
    __info__ = gi.EnumInfo(WindowActions)


