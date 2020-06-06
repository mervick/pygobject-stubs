# encoding: utf-8
# module gi.repository.Gladeui
# from /usr/lib64/girepository-1.0/Gladeui-2.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class Stock(__gobject.GEnum):
    # no doc
    def append_prefix(self, prefix): # real signature unknown; restored from __doc__
        """ append_prefix(prefix:str) """
        pass

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

    def spec(self): # real signature unknown; restored from __doc__
        """ spec() -> GObject.ParamSpec """
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


    DUMMY = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Gladeui', '__dict__': <attribute '__dict__' of 'Stock' objects>, '__doc__': None, '__gtype__': <GType GladeStock (94653531291344)>, '__enum_values__': {0: <enum _About of type Gladeui.Stock>, 1: <enum _Add of type Gladeui.Stock>, 2: <enum _Apply of type Gladeui.Stock>, 80: <enum _Ascending of type Gladeui.Stock>, 26: <enum _Back of type Gladeui.Stock>, 91: <enum Best _Fit of type Gladeui.Stock>, 3: <enum _Bold of type Gladeui.Stock>, 30: <enum _Bottom of type Gladeui.Stock>, 4: <enum _Cancel of type Gladeui.Stock>, 5: <enum _CD-ROM of type Gladeui.Stock>, 42: <enum _Center of type Gladeui.Stock>, 6: <enum _Clear of type Gladeui.Stock>, 7: <enum _Close of type Gladeui.Stock>, 78: <enum _Color of type Gladeui.Stock>, 8: <enum C_onnect of type Gladeui.Stock>, 9: <enum _Convert of type Gladeui.Stock>, 10: <enum _Copy of type Gladeui.Stock>, 11: <enum Cu_t of type Gladeui.Stock>, 88: <enum Decrease Indent of type Gladeui.Stock>, 12: <enum _Delete of type Gladeui.Stock>, 81: <enum _Descending of type Gladeui.Stock>, 17: <enum _Discard of type Gladeui.Stock>, 18: <enum _Disconnect of type Gladeui.Stock>, 27: <enum _Down of type Gladeui.Stock>, 19: <enum _Edit of type Gladeui.Stock>, 13: <enum Error of type Gladeui.Stock>, 20: <enum _Execute of type Gladeui.Stock>, 21: <enum _File of type Gladeui.Stock>, 43: <enum _Fill of type Gladeui.Stock>, 22: <enum _Find of type Gladeui.Stock>, 23: <enum Find and _Replace of type Gladeui.Stock>, 31: <enum _First of type Gladeui.Stock>, 24: <enum _Floppy of type Gladeui.Stock>, 79: <enum _Font of type Gladeui.Stock>, 47: <enum _Forward of type Gladeui.Stock>, 28: <enum _Forward of type Gladeui.Stock>, 25: <enum _Fullscreen of type Gladeui.Stock>, 34: <enum _Hard Disk of type Gladeui.Stock>, 35: <enum _Help of type Gladeui.Stock>, 36: <enum _Home of type Gladeui.Stock>, 37: <enum Increase Indent of type Gladeui.Stock>, 38: <enum _Index of type Gladeui.Stock>, 39: <enum _Information of type Gladeui.Stock>, 14: <enum Information of type Gladeui.Stock>, 40: <enum _Italic of type Gladeui.Stock>, 41: <enum _Jump to of type Gladeui.Stock>, 60: <enum Landscape of type Gladeui.Stock>, 32: <enum _Last of type Gladeui.Stock>, 46: <enum _Leave Fullscreen of type Gladeui.Stock>, 44: <enum _Left of type Gladeui.Stock>, 55: <enum _Network of type Gladeui.Stock>, 56: <enum _New of type Gladeui.Stock>, 48: <enum _Next of type Gladeui.Stock>, 57: <enum _No of type Gladeui.Stock>, 90: <enum _Normal Size of type Gladeui.Stock>, 58: <enum _OK of type Gladeui.Stock>, 59: <enum _Open of type Gladeui.Stock>, 64: <enum Page Set_up of type Gladeui.Stock>, 65: <enum _Paste of type Gladeui.Stock>, 49: <enum P_ause of type Gladeui.Stock>, 50: <enum _Play of type Gladeui.Stock>, 61: <enum Portrait of type Gladeui.Stock>, 66: <enum _Preferences of type Gladeui.Stock>, 51: <enum Pre_vious of type Gladeui.Stock>, 67: <enum _Print of type Gladeui.Stock>, 68: <enum Print Pre_view of type Gladeui.Stock>, 69: <enum _Properties of type Gladeui.Stock>, 15: <enum Question of type Gladeui.Stock>, 70: <enum _Quit of type Gladeui.Stock>, 52: <enum _Record of type Gladeui.Stock>, 71: <enum _Redo of type Gladeui.Stock>, 72: <enum _Refresh of type Gladeui.Stock>, 73: <enum _Remove of type Gladeui.Stock>, 62: <enum Reverse landscape of type Gladeui.Stock>, 63: <enum Reverse portrait of type Gladeui.Stock>, 74: <enum _Revert of type Gladeui.Stock>, 53: <enum R_ewind of type Gladeui.Stock>, 45: <enum _Right of type Gladeui.Stock>, 75: <enum _Save of type Gladeui.Stock>, 76: <enum Save _As of type Gladeui.Stock>, 77: <enum Select _All of type Gladeui.Stock>, 82: <enum _Spell Check of type Gladeui.Stock>, 83: <enum _Stop of type Gladeui.Stock>, 54: <enum _Stop of type Gladeui.Stock>, 84: <enum _Strikethrough of type Gladeui.Stock>, 33: <enum _Top of type Gladeui.Stock>, 85: <enum _Undelete of type Gladeui.Stock>, 86: <enum _Underline of type Gladeui.Stock>, 87: <enum _Undo of type Gladeui.Stock>, 29: <enum _Up of type Gladeui.Stock>, 16: <enum Warning of type Gladeui.Stock>, 89: <enum _Yes of type Gladeui.Stock>, 92: <enum Zoom _In of type Gladeui.Stock>, 93: <enum Zoom _Out of type Gladeui.Stock>}, '__info__': gi.EnumInfo(Stock), 'DUMMY': <enum _About of type Gladeui.Stock>, 'append_prefix': gi.FunctionInfo(append_prefix), 'spec': gi.FunctionInfo(spec)})"
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
        90: 90,
        91: 91,
        92: 92,
        93: 93,
    }
    __gtype__ = None # (!) real value is '<GType GladeStock (94653531291344)>'
    __info__ = gi.EnumInfo(Stock)


