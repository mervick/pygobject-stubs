# encoding: utf-8
# module gi.repository.GstGL
# from /usr/lib64/girepository-1.0/GstGL-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class GLFormat(__gobject.GEnum):
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

    def from_video_info(self, context, vinfo, plane): # real signature unknown; restored from __doc__
        """ from_video_info(context:GstGL.GLContext, vinfo:GstVideo.VideoInfo, plane:int) -> GstGL.GLFormat """
        pass

    def is_supported(self, context, format): # real signature unknown; restored from __doc__
        """ is_supported(context:GstGL.GLContext, format:GstGL.GLFormat) -> bool """
        return False

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

    def type_from_sized_gl_format(self, format): # real signature unknown; restored from __doc__
        """ type_from_sized_gl_format(format:GstGL.GLFormat) -> unsized_format:GstGL.GLFormat, gl_type:int """
        pass

    def type_n_bytes(self, format, type): # real signature unknown; restored from __doc__
        """ type_n_bytes(format:int, type:int) -> int """
        return 0

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


    ALPHA = 6406
    DEPTH24_STENCIL8 = 35056
    DEPTH_COMPONENT16 = 33189
    LUMINANCE = 6409
    LUMINANCE_ALPHA = 6410
    R8 = 33321
    RED = 6403
    RG = 33319
    RG8 = 33323
    RGB = 6407
    RGB16 = 32852
    RGB565 = 36194
    RGB8 = 32849
    RGBA = 6408
    RGBA16 = 32859
    RGBA8 = 32856
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstGL', '__dict__': <attribute '__dict__' of 'GLFormat' objects>, '__doc__': None, '__gtype__': <GType GstGLFormat (93979012406928)>, '__enum_values__': {6409: <enum GST_GL_LUMINANCE of type GstGL.GLFormat>, 6406: <enum GST_GL_ALPHA of type GstGL.GLFormat>, 6410: <enum GST_GL_LUMINANCE_ALPHA of type GstGL.GLFormat>, 6403: <enum GST_GL_RED of type GstGL.GLFormat>, 33321: <enum GST_GL_R8 of type GstGL.GLFormat>, 33319: <enum GST_GL_RG of type GstGL.GLFormat>, 33323: <enum GST_GL_RG8 of type GstGL.GLFormat>, 6407: <enum GST_GL_RGB of type GstGL.GLFormat>, 32849: <enum GST_GL_RGB8 of type GstGL.GLFormat>, 36194: <enum GST_GL_RGB565 of type GstGL.GLFormat>, 32852: <enum GST_GL_RGB16 of type GstGL.GLFormat>, 6408: <enum GST_GL_RGBA of type GstGL.GLFormat>, 32856: <enum GST_GL_RGBA8 of type GstGL.GLFormat>, 32859: <enum GST_GL_RGBA16 of type GstGL.GLFormat>, 33189: <enum GST_GL_DEPTH_COMPONENT16 of type GstGL.GLFormat>, 35056: <enum GST_GL_DEPTH24_STENCIL8 of type GstGL.GLFormat>}, '__info__': gi.EnumInfo(GLFormat), 'LUMINANCE': <enum GST_GL_LUMINANCE of type GstGL.GLFormat>, 'ALPHA': <enum GST_GL_ALPHA of type GstGL.GLFormat>, 'LUMINANCE_ALPHA': <enum GST_GL_LUMINANCE_ALPHA of type GstGL.GLFormat>, 'RED': <enum GST_GL_RED of type GstGL.GLFormat>, 'R8': <enum GST_GL_R8 of type GstGL.GLFormat>, 'RG': <enum GST_GL_RG of type GstGL.GLFormat>, 'RG8': <enum GST_GL_RG8 of type GstGL.GLFormat>, 'RGB': <enum GST_GL_RGB of type GstGL.GLFormat>, 'RGB8': <enum GST_GL_RGB8 of type GstGL.GLFormat>, 'RGB565': <enum GST_GL_RGB565 of type GstGL.GLFormat>, 'RGB16': <enum GST_GL_RGB16 of type GstGL.GLFormat>, 'RGBA': <enum GST_GL_RGBA of type GstGL.GLFormat>, 'RGBA8': <enum GST_GL_RGBA8 of type GstGL.GLFormat>, 'RGBA16': <enum GST_GL_RGBA16 of type GstGL.GLFormat>, 'DEPTH_COMPONENT16': <enum GST_GL_DEPTH_COMPONENT16 of type GstGL.GLFormat>, 'DEPTH24_STENCIL8': <enum GST_GL_DEPTH24_STENCIL8 of type GstGL.GLFormat>, 'from_video_info': gi.FunctionInfo(from_video_info), 'is_supported': gi.FunctionInfo(is_supported), 'type_from_sized_gl_format': gi.FunctionInfo(type_from_sized_gl_format), 'type_n_bytes': gi.FunctionInfo(type_n_bytes)})"
    __enum_values__ = {
        6403: 6403,
        6406: 6406,
        6407: 6407,
        6408: 6408,
        6409: 6409,
        6410: 6410,
        32849: 32849,
        32852: 32852,
        32856: 32856,
        32859: 32859,
        33189: 33189,
        33319: 33319,
        33321: 33321,
        33323: 33323,
        35056: 35056,
        36194: 36194,
    }
    __gtype__ = None # (!) real value is '<GType GstGLFormat (93979012406928)>'
    __info__ = gi.EnumInfo(GLFormat)


