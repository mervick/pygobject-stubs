# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
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


class PixelFormat(__gobject.GEnum):
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


    ABGR_2101010 = 125
    ABGR_2101010_PRE = 253
    ABGR_8888 = 115
    ABGR_8888_PRE = 243
    ANY = 0
    ARGB_2101010 = 93
    ARGB_2101010_PRE = 221
    ARGB_8888 = 83
    ARGB_8888_PRE = 211
    A_8 = 17
    BGRA_1010102 = 61
    BGRA_1010102_PRE = 189
    BGRA_8888 = 51
    BGRA_8888_PRE = 179
    BGR_888 = 34
    DEPTH_16 = 265
    DEPTH_24_STENCIL_8 = 771
    DEPTH_32 = 259
    G_8 = 8
    RGBA_1010102 = 29
    RGBA_1010102_PRE = 157
    RGBA_4444 = 21
    RGBA_4444_PRE = 149
    RGBA_5551 = 22
    RGBA_5551_PRE = 150
    RGBA_8888 = 19
    RGBA_8888_PRE = 147
    RGB_565 = 4
    RGB_888 = 2
    RG_88 = 9
    YUV = 7
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Cogl', '__dict__': <attribute '__dict__' of 'PixelFormat' objects>, '__doc__': None, '__gtype__': <GType CoglPixelFormat (93970932240704)>, '__enum_values__': {0: <enum COGL_PIXEL_FORMAT_ANY of type Cogl.PixelFormat>, 17: <enum COGL_PIXEL_FORMAT_A_8 of type Cogl.PixelFormat>, 4: <enum COGL_PIXEL_FORMAT_RGB_565 of type Cogl.PixelFormat>, 21: <enum COGL_PIXEL_FORMAT_RGBA_4444 of type Cogl.PixelFormat>, 22: <enum COGL_PIXEL_FORMAT_RGBA_5551 of type Cogl.PixelFormat>, 7: <enum COGL_PIXEL_FORMAT_YUV of type Cogl.PixelFormat>, 8: <enum COGL_PIXEL_FORMAT_G_8 of type Cogl.PixelFormat>, 9: <enum COGL_PIXEL_FORMAT_RG_88 of type Cogl.PixelFormat>, 2: <enum COGL_PIXEL_FORMAT_RGB_888 of type Cogl.PixelFormat>, 34: <enum COGL_PIXEL_FORMAT_BGR_888 of type Cogl.PixelFormat>, 19: <enum COGL_PIXEL_FORMAT_RGBA_8888 of type Cogl.PixelFormat>, 51: <enum COGL_PIXEL_FORMAT_BGRA_8888 of type Cogl.PixelFormat>, 83: <enum COGL_PIXEL_FORMAT_ARGB_8888 of type Cogl.PixelFormat>, 115: <enum COGL_PIXEL_FORMAT_ABGR_8888 of type Cogl.PixelFormat>, 29: <enum COGL_PIXEL_FORMAT_RGBA_1010102 of type Cogl.PixelFormat>, 61: <enum COGL_PIXEL_FORMAT_BGRA_1010102 of type Cogl.PixelFormat>, 93: <enum COGL_PIXEL_FORMAT_ARGB_2101010 of type Cogl.PixelFormat>, 125: <enum COGL_PIXEL_FORMAT_ABGR_2101010 of type Cogl.PixelFormat>, 147: <enum COGL_PIXEL_FORMAT_RGBA_8888_PRE of type Cogl.PixelFormat>, 179: <enum COGL_PIXEL_FORMAT_BGRA_8888_PRE of type Cogl.PixelFormat>, 211: <enum COGL_PIXEL_FORMAT_ARGB_8888_PRE of type Cogl.PixelFormat>, 243: <enum COGL_PIXEL_FORMAT_ABGR_8888_PRE of type Cogl.PixelFormat>, 149: <enum COGL_PIXEL_FORMAT_RGBA_4444_PRE of type Cogl.PixelFormat>, 150: <enum COGL_PIXEL_FORMAT_RGBA_5551_PRE of type Cogl.PixelFormat>, 157: <enum COGL_PIXEL_FORMAT_RGBA_1010102_PRE of type Cogl.PixelFormat>, 189: <enum COGL_PIXEL_FORMAT_BGRA_1010102_PRE of type Cogl.PixelFormat>, 221: <enum COGL_PIXEL_FORMAT_ARGB_2101010_PRE of type Cogl.PixelFormat>, 253: <enum COGL_PIXEL_FORMAT_ABGR_2101010_PRE of type Cogl.PixelFormat>, 265: <enum COGL_PIXEL_FORMAT_DEPTH_16 of type Cogl.PixelFormat>, 259: <enum COGL_PIXEL_FORMAT_DEPTH_32 of type Cogl.PixelFormat>, 771: <enum COGL_PIXEL_FORMAT_DEPTH_24_STENCIL_8 of type Cogl.PixelFormat>}, '__info__': gi.EnumInfo(PixelFormat), 'ANY': <enum COGL_PIXEL_FORMAT_ANY of type Cogl.PixelFormat>, 'A_8': <enum COGL_PIXEL_FORMAT_A_8 of type Cogl.PixelFormat>, 'RGB_565': <enum COGL_PIXEL_FORMAT_RGB_565 of type Cogl.PixelFormat>, 'RGBA_4444': <enum COGL_PIXEL_FORMAT_RGBA_4444 of type Cogl.PixelFormat>, 'RGBA_5551': <enum COGL_PIXEL_FORMAT_RGBA_5551 of type Cogl.PixelFormat>, 'YUV': <enum COGL_PIXEL_FORMAT_YUV of type Cogl.PixelFormat>, 'G_8': <enum COGL_PIXEL_FORMAT_G_8 of type Cogl.PixelFormat>, 'RG_88': <enum COGL_PIXEL_FORMAT_RG_88 of type Cogl.PixelFormat>, 'RGB_888': <enum COGL_PIXEL_FORMAT_RGB_888 of type Cogl.PixelFormat>, 'BGR_888': <enum COGL_PIXEL_FORMAT_BGR_888 of type Cogl.PixelFormat>, 'RGBA_8888': <enum COGL_PIXEL_FORMAT_RGBA_8888 of type Cogl.PixelFormat>, 'BGRA_8888': <enum COGL_PIXEL_FORMAT_BGRA_8888 of type Cogl.PixelFormat>, 'ARGB_8888': <enum COGL_PIXEL_FORMAT_ARGB_8888 of type Cogl.PixelFormat>, 'ABGR_8888': <enum COGL_PIXEL_FORMAT_ABGR_8888 of type Cogl.PixelFormat>, 'RGBA_1010102': <enum COGL_PIXEL_FORMAT_RGBA_1010102 of type Cogl.PixelFormat>, 'BGRA_1010102': <enum COGL_PIXEL_FORMAT_BGRA_1010102 of type Cogl.PixelFormat>, 'ARGB_2101010': <enum COGL_PIXEL_FORMAT_ARGB_2101010 of type Cogl.PixelFormat>, 'ABGR_2101010': <enum COGL_PIXEL_FORMAT_ABGR_2101010 of type Cogl.PixelFormat>, 'RGBA_8888_PRE': <enum COGL_PIXEL_FORMAT_RGBA_8888_PRE of type Cogl.PixelFormat>, 'BGRA_8888_PRE': <enum COGL_PIXEL_FORMAT_BGRA_8888_PRE of type Cogl.PixelFormat>, 'ARGB_8888_PRE': <enum COGL_PIXEL_FORMAT_ARGB_8888_PRE of type Cogl.PixelFormat>, 'ABGR_8888_PRE': <enum COGL_PIXEL_FORMAT_ABGR_8888_PRE of type Cogl.PixelFormat>, 'RGBA_4444_PRE': <enum COGL_PIXEL_FORMAT_RGBA_4444_PRE of type Cogl.PixelFormat>, 'RGBA_5551_PRE': <enum COGL_PIXEL_FORMAT_RGBA_5551_PRE of type Cogl.PixelFormat>, 'RGBA_1010102_PRE': <enum COGL_PIXEL_FORMAT_RGBA_1010102_PRE of type Cogl.PixelFormat>, 'BGRA_1010102_PRE': <enum COGL_PIXEL_FORMAT_BGRA_1010102_PRE of type Cogl.PixelFormat>, 'ARGB_2101010_PRE': <enum COGL_PIXEL_FORMAT_ARGB_2101010_PRE of type Cogl.PixelFormat>, 'ABGR_2101010_PRE': <enum COGL_PIXEL_FORMAT_ABGR_2101010_PRE of type Cogl.PixelFormat>, 'DEPTH_16': <enum COGL_PIXEL_FORMAT_DEPTH_16 of type Cogl.PixelFormat>, 'DEPTH_32': <enum COGL_PIXEL_FORMAT_DEPTH_32 of type Cogl.PixelFormat>, 'DEPTH_24_STENCIL_8': <enum COGL_PIXEL_FORMAT_DEPTH_24_STENCIL_8 of type Cogl.PixelFormat>})"
    __enum_values__ = {
        0: 0,
        2: 2,
        4: 4,
        7: 7,
        8: 8,
        9: 9,
        17: 17,
        19: 19,
        21: 21,
        22: 22,
        29: 29,
        34: 34,
        51: 51,
        61: 61,
        83: 83,
        93: 93,
        115: 115,
        125: 125,
        147: 147,
        149: 149,
        150: 150,
        157: 157,
        179: 179,
        189: 189,
        211: 211,
        221: 221,
        243: 243,
        253: 253,
        259: 259,
        265: 265,
        771: 771,
    }
    __gtype__ = None # (!) real value is '<GType CoglPixelFormat (93970932240704)>'
    __info__ = gi.EnumInfo(PixelFormat)


