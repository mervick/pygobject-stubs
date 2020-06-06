# encoding: utf-8
# module gi.repository.Vips
# from /usr/lib64/girepository-1.0/Vips-8.0.typelib
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


class Interpretation(__gobject.GEnum):
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


    B_W = 1
    CMC = 18
    CMYK = 15
    ERROR = -1
    FOURIER = 24
    GREY16 = 26
    HISTOGRAM = 10
    HSV = 29
    LAB = 13
    LABQ = 16
    LABS = 21
    LAST = 30
    LCH = 19
    MATRIX = 27
    MULTIBAND = 0
    RGB = 17
    RGB16 = 25
    SCRGB = 28
    SRGB = 22
    XYZ = 12
    YXY = 23
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Vips', '__dict__': <attribute '__dict__' of 'Interpretation' objects>, '__doc__': None, '__gtype__': <GType VipsInterpretation (94317410543664)>, '__enum_values__': {-1: <enum VIPS_INTERPRETATION_ERROR of type Vips.Interpretation>, 0: <enum VIPS_INTERPRETATION_MULTIBAND of type Vips.Interpretation>, 1: <enum VIPS_INTERPRETATION_B_W of type Vips.Interpretation>, 10: <enum VIPS_INTERPRETATION_HISTOGRAM of type Vips.Interpretation>, 12: <enum VIPS_INTERPRETATION_XYZ of type Vips.Interpretation>, 13: <enum VIPS_INTERPRETATION_LAB of type Vips.Interpretation>, 15: <enum VIPS_INTERPRETATION_CMYK of type Vips.Interpretation>, 16: <enum VIPS_INTERPRETATION_LABQ of type Vips.Interpretation>, 17: <enum VIPS_INTERPRETATION_RGB of type Vips.Interpretation>, 18: <enum VIPS_INTERPRETATION_CMC of type Vips.Interpretation>, 19: <enum VIPS_INTERPRETATION_LCH of type Vips.Interpretation>, 21: <enum VIPS_INTERPRETATION_LABS of type Vips.Interpretation>, 22: <enum VIPS_INTERPRETATION_sRGB of type Vips.Interpretation>, 23: <enum VIPS_INTERPRETATION_YXY of type Vips.Interpretation>, 24: <enum VIPS_INTERPRETATION_FOURIER of type Vips.Interpretation>, 25: <enum VIPS_INTERPRETATION_RGB16 of type Vips.Interpretation>, 26: <enum VIPS_INTERPRETATION_GREY16 of type Vips.Interpretation>, 27: <enum VIPS_INTERPRETATION_MATRIX of type Vips.Interpretation>, 28: <enum VIPS_INTERPRETATION_scRGB of type Vips.Interpretation>, 29: <enum VIPS_INTERPRETATION_HSV of type Vips.Interpretation>, 30: <enum VIPS_INTERPRETATION_LAST of type Vips.Interpretation>}, '__info__': gi.EnumInfo(Interpretation), 'ERROR': <enum VIPS_INTERPRETATION_ERROR of type Vips.Interpretation>, 'MULTIBAND': <enum VIPS_INTERPRETATION_MULTIBAND of type Vips.Interpretation>, 'B_W': <enum VIPS_INTERPRETATION_B_W of type Vips.Interpretation>, 'HISTOGRAM': <enum VIPS_INTERPRETATION_HISTOGRAM of type Vips.Interpretation>, 'XYZ': <enum VIPS_INTERPRETATION_XYZ of type Vips.Interpretation>, 'LAB': <enum VIPS_INTERPRETATION_LAB of type Vips.Interpretation>, 'CMYK': <enum VIPS_INTERPRETATION_CMYK of type Vips.Interpretation>, 'LABQ': <enum VIPS_INTERPRETATION_LABQ of type Vips.Interpretation>, 'RGB': <enum VIPS_INTERPRETATION_RGB of type Vips.Interpretation>, 'CMC': <enum VIPS_INTERPRETATION_CMC of type Vips.Interpretation>, 'LCH': <enum VIPS_INTERPRETATION_LCH of type Vips.Interpretation>, 'LABS': <enum VIPS_INTERPRETATION_LABS of type Vips.Interpretation>, 'SRGB': <enum VIPS_INTERPRETATION_sRGB of type Vips.Interpretation>, 'YXY': <enum VIPS_INTERPRETATION_YXY of type Vips.Interpretation>, 'FOURIER': <enum VIPS_INTERPRETATION_FOURIER of type Vips.Interpretation>, 'RGB16': <enum VIPS_INTERPRETATION_RGB16 of type Vips.Interpretation>, 'GREY16': <enum VIPS_INTERPRETATION_GREY16 of type Vips.Interpretation>, 'MATRIX': <enum VIPS_INTERPRETATION_MATRIX of type Vips.Interpretation>, 'SCRGB': <enum VIPS_INTERPRETATION_scRGB of type Vips.Interpretation>, 'HSV': <enum VIPS_INTERPRETATION_HSV of type Vips.Interpretation>, 'LAST': <enum VIPS_INTERPRETATION_LAST of type Vips.Interpretation>})"
    __enum_values__ = {
        -1: -1,
        0: 0,
        1: 1,
        10: 10,
        12: 12,
        13: 13,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
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
    }
    __gtype__ = None # (!) real value is '<GType VipsInterpretation (94317410543664)>'
    __info__ = gi.EnumInfo(Interpretation)


