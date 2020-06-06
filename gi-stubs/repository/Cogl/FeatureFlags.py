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


class FeatureFlags(__gobject.GFlags):
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


    DEPTH_RANGE = 16384
    DEPTH_TEXTURE = 16777216
    FOUR_CLIP_PLANES = 512
    MAP_BUFFER_FOR_READ = 2097152
    MAP_BUFFER_FOR_WRITE = 4194304
    OFFSCREEN = 64
    OFFSCREEN_BLIT = 256
    OFFSCREEN_MULTISAMPLE = 128
    ONSCREEN_MULTIPLE = 8388608
    PBOS = 4096
    POINT_SPRITE = 262144
    SHADERS_ARBFP = 1048576
    SHADERS_GLSL = 32
    SHADER_TEXTURE_LOD = 33554432
    STENCIL_BUFFER = 1024
    TEXTURE_3D = 524288
    TEXTURE_NPOT = 4
    TEXTURE_NPOT_BASIC = 32768
    TEXTURE_NPOT_MIPMAP = 65536
    TEXTURE_NPOT_REPEAT = 131072
    TEXTURE_READ_PIXELS = 16
    TEXTURE_RECTANGLE = 2
    TEXTURE_YUV = 8
    UNSIGNED_INT_INDICES = 8192
    VBOS = 2048
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Cogl', '__dict__': <attribute '__dict__' of 'FeatureFlags' objects>, '__doc__': None, '__gtype__': <GType CoglFeatureFlags (93970932092464)>, '__flags_values__': {2: <flags COGL_FEATURE_TEXTURE_RECTANGLE of type Cogl.FeatureFlags>, 4: <flags COGL_FEATURE_TEXTURE_NPOT of type Cogl.FeatureFlags>, 8: <flags COGL_FEATURE_TEXTURE_YUV of type Cogl.FeatureFlags>, 16: <flags COGL_FEATURE_TEXTURE_READ_PIXELS of type Cogl.FeatureFlags>, 32: <flags COGL_FEATURE_SHADERS_GLSL of type Cogl.FeatureFlags>, 64: <flags COGL_FEATURE_OFFSCREEN of type Cogl.FeatureFlags>, 128: <flags COGL_FEATURE_OFFSCREEN_MULTISAMPLE of type Cogl.FeatureFlags>, 256: <flags COGL_FEATURE_OFFSCREEN_BLIT of type Cogl.FeatureFlags>, 512: <flags COGL_FEATURE_FOUR_CLIP_PLANES of type Cogl.FeatureFlags>, 1024: <flags COGL_FEATURE_STENCIL_BUFFER of type Cogl.FeatureFlags>, 2048: <flags COGL_FEATURE_VBOS of type Cogl.FeatureFlags>, 4096: <flags COGL_FEATURE_PBOS of type Cogl.FeatureFlags>, 8192: <flags COGL_FEATURE_UNSIGNED_INT_INDICES of type Cogl.FeatureFlags>, 16384: <flags COGL_FEATURE_DEPTH_RANGE of type Cogl.FeatureFlags>, 32768: <flags COGL_FEATURE_TEXTURE_NPOT_BASIC of type Cogl.FeatureFlags>, 65536: <flags COGL_FEATURE_TEXTURE_NPOT_MIPMAP of type Cogl.FeatureFlags>, 131072: <flags COGL_FEATURE_TEXTURE_NPOT_REPEAT of type Cogl.FeatureFlags>, 262144: <flags COGL_FEATURE_POINT_SPRITE of type Cogl.FeatureFlags>, 524288: <flags COGL_FEATURE_TEXTURE_3D of type Cogl.FeatureFlags>, 1048576: <flags COGL_FEATURE_SHADERS_ARBFP of type Cogl.FeatureFlags>, 2097152: <flags COGL_FEATURE_MAP_BUFFER_FOR_READ of type Cogl.FeatureFlags>, 4194304: <flags COGL_FEATURE_MAP_BUFFER_FOR_WRITE of type Cogl.FeatureFlags>, 8388608: <flags COGL_FEATURE_ONSCREEN_MULTIPLE of type Cogl.FeatureFlags>, 16777216: <flags COGL_FEATURE_DEPTH_TEXTURE of type Cogl.FeatureFlags>, 33554432: <flags COGL_FEATURE_SHADER_TEXTURE_LOD of type Cogl.FeatureFlags>}, '__info__': gi.EnumInfo(FeatureFlags), 'TEXTURE_RECTANGLE': <flags COGL_FEATURE_TEXTURE_RECTANGLE of type Cogl.FeatureFlags>, 'TEXTURE_NPOT': <flags COGL_FEATURE_TEXTURE_NPOT of type Cogl.FeatureFlags>, 'TEXTURE_YUV': <flags COGL_FEATURE_TEXTURE_YUV of type Cogl.FeatureFlags>, 'TEXTURE_READ_PIXELS': <flags COGL_FEATURE_TEXTURE_READ_PIXELS of type Cogl.FeatureFlags>, 'SHADERS_GLSL': <flags COGL_FEATURE_SHADERS_GLSL of type Cogl.FeatureFlags>, 'OFFSCREEN': <flags COGL_FEATURE_OFFSCREEN of type Cogl.FeatureFlags>, 'OFFSCREEN_MULTISAMPLE': <flags COGL_FEATURE_OFFSCREEN_MULTISAMPLE of type Cogl.FeatureFlags>, 'OFFSCREEN_BLIT': <flags COGL_FEATURE_OFFSCREEN_BLIT of type Cogl.FeatureFlags>, 'FOUR_CLIP_PLANES': <flags COGL_FEATURE_FOUR_CLIP_PLANES of type Cogl.FeatureFlags>, 'STENCIL_BUFFER': <flags COGL_FEATURE_STENCIL_BUFFER of type Cogl.FeatureFlags>, 'VBOS': <flags COGL_FEATURE_VBOS of type Cogl.FeatureFlags>, 'PBOS': <flags COGL_FEATURE_PBOS of type Cogl.FeatureFlags>, 'UNSIGNED_INT_INDICES': <flags COGL_FEATURE_UNSIGNED_INT_INDICES of type Cogl.FeatureFlags>, 'DEPTH_RANGE': <flags COGL_FEATURE_DEPTH_RANGE of type Cogl.FeatureFlags>, 'TEXTURE_NPOT_BASIC': <flags COGL_FEATURE_TEXTURE_NPOT_BASIC of type Cogl.FeatureFlags>, 'TEXTURE_NPOT_MIPMAP': <flags COGL_FEATURE_TEXTURE_NPOT_MIPMAP of type Cogl.FeatureFlags>, 'TEXTURE_NPOT_REPEAT': <flags COGL_FEATURE_TEXTURE_NPOT_REPEAT of type Cogl.FeatureFlags>, 'POINT_SPRITE': <flags COGL_FEATURE_POINT_SPRITE of type Cogl.FeatureFlags>, 'TEXTURE_3D': <flags COGL_FEATURE_TEXTURE_3D of type Cogl.FeatureFlags>, 'SHADERS_ARBFP': <flags COGL_FEATURE_SHADERS_ARBFP of type Cogl.FeatureFlags>, 'MAP_BUFFER_FOR_READ': <flags COGL_FEATURE_MAP_BUFFER_FOR_READ of type Cogl.FeatureFlags>, 'MAP_BUFFER_FOR_WRITE': <flags COGL_FEATURE_MAP_BUFFER_FOR_WRITE of type Cogl.FeatureFlags>, 'ONSCREEN_MULTIPLE': <flags COGL_FEATURE_ONSCREEN_MULTIPLE of type Cogl.FeatureFlags>, 'DEPTH_TEXTURE': <flags COGL_FEATURE_DEPTH_TEXTURE of type Cogl.FeatureFlags>, 'SHADER_TEXTURE_LOD': <flags COGL_FEATURE_SHADER_TEXTURE_LOD of type Cogl.FeatureFlags>})"
    __flags_values__ = {
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
        524288: 524288,
        1048576: 1048576,
        2097152: 2097152,
        4194304: 4194304,
        8388608: 8388608,
        16777216: 16777216,
        33554432: 33554432,
    }
    __gtype__ = None # (!) real value is '<GType CoglFeatureFlags (93970932092464)>'
    __info__ = gi.EnumInfo(FeatureFlags)


