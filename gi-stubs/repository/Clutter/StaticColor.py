# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class StaticColor(__gobject.GEnum):
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


    ALUMINIUM_1 = 38
    ALUMINIUM_2 = 39
    ALUMINIUM_3 = 40
    ALUMINIUM_4 = 41
    ALUMINIUM_5 = 42
    ALUMINIUM_6 = 43
    BLACK = 1
    BLUE = 6
    BUTTER = 17
    BUTTER_DARK = 19
    BUTTER_LIGHT = 18
    CHAMELEON = 26
    CHAMELEON_DARK = 28
    CHAMELEON_LIGHT = 27
    CHOCOLATE = 23
    CHOCOLATE_DARK = 25
    CHOCOLATE_LIGHT = 24
    CYAN = 8
    DARK_BLUE = 7
    DARK_CYAN = 9
    DARK_GRAY = 15
    DARK_GREEN = 5
    DARK_MAGENTA = 11
    DARK_RED = 3
    DARK_YELLOW = 13
    GRAY = 14
    GREEN = 4
    LIGHT_GRAY = 16
    MAGENTA = 10
    ORANGE = 20
    ORANGE_DARK = 22
    ORANGE_LIGHT = 21
    PLUM = 32
    PLUM_DARK = 34
    PLUM_LIGHT = 33
    RED = 2
    SCARLET_RED = 35
    SCARLET_RED_DARK = 37
    SCARLET_RED_LIGHT = 36
    SKY_BLUE = 29
    SKY_BLUE_DARK = 31
    SKY_BLUE_LIGHT = 30
    TRANSPARENT = 44
    WHITE = 0
    YELLOW = 12
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Clutter', '__dict__': <attribute '__dict__' of 'StaticColor' objects>, '__doc__': None, '__gtype__': <GType ClutterStaticColor (94911696359040)>, '__enum_values__': {0: <enum CLUTTER_COLOR_WHITE of type Clutter.StaticColor>, 1: <enum CLUTTER_COLOR_BLACK of type Clutter.StaticColor>, 2: <enum CLUTTER_COLOR_RED of type Clutter.StaticColor>, 3: <enum CLUTTER_COLOR_DARK_RED of type Clutter.StaticColor>, 4: <enum CLUTTER_COLOR_GREEN of type Clutter.StaticColor>, 5: <enum CLUTTER_COLOR_DARK_GREEN of type Clutter.StaticColor>, 6: <enum CLUTTER_COLOR_BLUE of type Clutter.StaticColor>, 7: <enum CLUTTER_COLOR_DARK_BLUE of type Clutter.StaticColor>, 8: <enum CLUTTER_COLOR_CYAN of type Clutter.StaticColor>, 9: <enum CLUTTER_COLOR_DARK_CYAN of type Clutter.StaticColor>, 10: <enum CLUTTER_COLOR_MAGENTA of type Clutter.StaticColor>, 11: <enum CLUTTER_COLOR_DARK_MAGENTA of type Clutter.StaticColor>, 12: <enum CLUTTER_COLOR_YELLOW of type Clutter.StaticColor>, 13: <enum CLUTTER_COLOR_DARK_YELLOW of type Clutter.StaticColor>, 14: <enum CLUTTER_COLOR_GRAY of type Clutter.StaticColor>, 15: <enum CLUTTER_COLOR_DARK_GRAY of type Clutter.StaticColor>, 16: <enum CLUTTER_COLOR_LIGHT_GRAY of type Clutter.StaticColor>, 17: <enum CLUTTER_COLOR_BUTTER of type Clutter.StaticColor>, 18: <enum CLUTTER_COLOR_BUTTER_LIGHT of type Clutter.StaticColor>, 19: <enum CLUTTER_COLOR_BUTTER_DARK of type Clutter.StaticColor>, 20: <enum CLUTTER_COLOR_ORANGE of type Clutter.StaticColor>, 21: <enum CLUTTER_COLOR_ORANGE_LIGHT of type Clutter.StaticColor>, 22: <enum CLUTTER_COLOR_ORANGE_DARK of type Clutter.StaticColor>, 23: <enum CLUTTER_COLOR_CHOCOLATE of type Clutter.StaticColor>, 24: <enum CLUTTER_COLOR_CHOCOLATE_LIGHT of type Clutter.StaticColor>, 25: <enum CLUTTER_COLOR_CHOCOLATE_DARK of type Clutter.StaticColor>, 26: <enum CLUTTER_COLOR_CHAMELEON of type Clutter.StaticColor>, 27: <enum CLUTTER_COLOR_CHAMELEON_LIGHT of type Clutter.StaticColor>, 28: <enum CLUTTER_COLOR_CHAMELEON_DARK of type Clutter.StaticColor>, 29: <enum CLUTTER_COLOR_SKY_BLUE of type Clutter.StaticColor>, 30: <enum CLUTTER_COLOR_SKY_BLUE_LIGHT of type Clutter.StaticColor>, 31: <enum CLUTTER_COLOR_SKY_BLUE_DARK of type Clutter.StaticColor>, 32: <enum CLUTTER_COLOR_PLUM of type Clutter.StaticColor>, 33: <enum CLUTTER_COLOR_PLUM_LIGHT of type Clutter.StaticColor>, 34: <enum CLUTTER_COLOR_PLUM_DARK of type Clutter.StaticColor>, 35: <enum CLUTTER_COLOR_SCARLET_RED of type Clutter.StaticColor>, 36: <enum CLUTTER_COLOR_SCARLET_RED_LIGHT of type Clutter.StaticColor>, 37: <enum CLUTTER_COLOR_SCARLET_RED_DARK of type Clutter.StaticColor>, 38: <enum CLUTTER_COLOR_ALUMINIUM_1 of type Clutter.StaticColor>, 39: <enum CLUTTER_COLOR_ALUMINIUM_2 of type Clutter.StaticColor>, 40: <enum CLUTTER_COLOR_ALUMINIUM_3 of type Clutter.StaticColor>, 41: <enum CLUTTER_COLOR_ALUMINIUM_4 of type Clutter.StaticColor>, 42: <enum CLUTTER_COLOR_ALUMINIUM_5 of type Clutter.StaticColor>, 43: <enum CLUTTER_COLOR_ALUMINIUM_6 of type Clutter.StaticColor>, 44: <enum CLUTTER_COLOR_TRANSPARENT of type Clutter.StaticColor>}, '__info__': gi.EnumInfo(StaticColor), 'WHITE': <enum CLUTTER_COLOR_WHITE of type Clutter.StaticColor>, 'BLACK': <enum CLUTTER_COLOR_BLACK of type Clutter.StaticColor>, 'RED': <enum CLUTTER_COLOR_RED of type Clutter.StaticColor>, 'DARK_RED': <enum CLUTTER_COLOR_DARK_RED of type Clutter.StaticColor>, 'GREEN': <enum CLUTTER_COLOR_GREEN of type Clutter.StaticColor>, 'DARK_GREEN': <enum CLUTTER_COLOR_DARK_GREEN of type Clutter.StaticColor>, 'BLUE': <enum CLUTTER_COLOR_BLUE of type Clutter.StaticColor>, 'DARK_BLUE': <enum CLUTTER_COLOR_DARK_BLUE of type Clutter.StaticColor>, 'CYAN': <enum CLUTTER_COLOR_CYAN of type Clutter.StaticColor>, 'DARK_CYAN': <enum CLUTTER_COLOR_DARK_CYAN of type Clutter.StaticColor>, 'MAGENTA': <enum CLUTTER_COLOR_MAGENTA of type Clutter.StaticColor>, 'DARK_MAGENTA': <enum CLUTTER_COLOR_DARK_MAGENTA of type Clutter.StaticColor>, 'YELLOW': <enum CLUTTER_COLOR_YELLOW of type Clutter.StaticColor>, 'DARK_YELLOW': <enum CLUTTER_COLOR_DARK_YELLOW of type Clutter.StaticColor>, 'GRAY': <enum CLUTTER_COLOR_GRAY of type Clutter.StaticColor>, 'DARK_GRAY': <enum CLUTTER_COLOR_DARK_GRAY of type Clutter.StaticColor>, 'LIGHT_GRAY': <enum CLUTTER_COLOR_LIGHT_GRAY of type Clutter.StaticColor>, 'BUTTER': <enum CLUTTER_COLOR_BUTTER of type Clutter.StaticColor>, 'BUTTER_LIGHT': <enum CLUTTER_COLOR_BUTTER_LIGHT of type Clutter.StaticColor>, 'BUTTER_DARK': <enum CLUTTER_COLOR_BUTTER_DARK of type Clutter.StaticColor>, 'ORANGE': <enum CLUTTER_COLOR_ORANGE of type Clutter.StaticColor>, 'ORANGE_LIGHT': <enum CLUTTER_COLOR_ORANGE_LIGHT of type Clutter.StaticColor>, 'ORANGE_DARK': <enum CLUTTER_COLOR_ORANGE_DARK of type Clutter.StaticColor>, 'CHOCOLATE': <enum CLUTTER_COLOR_CHOCOLATE of type Clutter.StaticColor>, 'CHOCOLATE_LIGHT': <enum CLUTTER_COLOR_CHOCOLATE_LIGHT of type Clutter.StaticColor>, 'CHOCOLATE_DARK': <enum CLUTTER_COLOR_CHOCOLATE_DARK of type Clutter.StaticColor>, 'CHAMELEON': <enum CLUTTER_COLOR_CHAMELEON of type Clutter.StaticColor>, 'CHAMELEON_LIGHT': <enum CLUTTER_COLOR_CHAMELEON_LIGHT of type Clutter.StaticColor>, 'CHAMELEON_DARK': <enum CLUTTER_COLOR_CHAMELEON_DARK of type Clutter.StaticColor>, 'SKY_BLUE': <enum CLUTTER_COLOR_SKY_BLUE of type Clutter.StaticColor>, 'SKY_BLUE_LIGHT': <enum CLUTTER_COLOR_SKY_BLUE_LIGHT of type Clutter.StaticColor>, 'SKY_BLUE_DARK': <enum CLUTTER_COLOR_SKY_BLUE_DARK of type Clutter.StaticColor>, 'PLUM': <enum CLUTTER_COLOR_PLUM of type Clutter.StaticColor>, 'PLUM_LIGHT': <enum CLUTTER_COLOR_PLUM_LIGHT of type Clutter.StaticColor>, 'PLUM_DARK': <enum CLUTTER_COLOR_PLUM_DARK of type Clutter.StaticColor>, 'SCARLET_RED': <enum CLUTTER_COLOR_SCARLET_RED of type Clutter.StaticColor>, 'SCARLET_RED_LIGHT': <enum CLUTTER_COLOR_SCARLET_RED_LIGHT of type Clutter.StaticColor>, 'SCARLET_RED_DARK': <enum CLUTTER_COLOR_SCARLET_RED_DARK of type Clutter.StaticColor>, 'ALUMINIUM_1': <enum CLUTTER_COLOR_ALUMINIUM_1 of type Clutter.StaticColor>, 'ALUMINIUM_2': <enum CLUTTER_COLOR_ALUMINIUM_2 of type Clutter.StaticColor>, 'ALUMINIUM_3': <enum CLUTTER_COLOR_ALUMINIUM_3 of type Clutter.StaticColor>, 'ALUMINIUM_4': <enum CLUTTER_COLOR_ALUMINIUM_4 of type Clutter.StaticColor>, 'ALUMINIUM_5': <enum CLUTTER_COLOR_ALUMINIUM_5 of type Clutter.StaticColor>, 'ALUMINIUM_6': <enum CLUTTER_COLOR_ALUMINIUM_6 of type Clutter.StaticColor>, 'TRANSPARENT': <enum CLUTTER_COLOR_TRANSPARENT of type Clutter.StaticColor>})"
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
    }
    __gtype__ = None # (!) real value is '<GType ClutterStaticColor (94911696359040)>'
    __info__ = gi.EnumInfo(StaticColor)


