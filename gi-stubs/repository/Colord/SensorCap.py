# encoding: utf-8
# module gi.repository.Colord
# from /usr/lib64/girepository-1.0/Colord-1.0.typelib
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


class SensorCap(__gobject.GEnum):
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


    AMBIENT = 6
    CALIBRATION = 7
    CALIBRATION_DARK = 16
    CALIBRATION_IRRADIANCE = 17
    CRT = 2
    LCD = 1
    LCD_CCFL = 10
    LCD_RGB_LED = 11
    LCD_WHITE_LED = 12
    LED = 8
    PLASMA = 9
    PRINTER = 3
    PROJECTOR = 5
    SPECTRAL = 15
    SPOT = 4
    UNKNOWN = 0
    WIDE_GAMUT_LCD_CCFL = 13
    WIDE_GAMUT_LCD_RGB_LED = 14
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colord', '__dict__': <attribute '__dict__' of 'SensorCap' objects>, '__doc__': None, '__gtype__': <GType PyColordSensorCap (94892598974960)>, '__enum_values__': {0: <enum CD_SENSOR_CAP_UNKNOWN of type Colord.SensorCap>, 1: <enum CD_SENSOR_CAP_LCD of type Colord.SensorCap>, 2: <enum CD_SENSOR_CAP_CRT of type Colord.SensorCap>, 3: <enum CD_SENSOR_CAP_PRINTER of type Colord.SensorCap>, 4: <enum CD_SENSOR_CAP_SPOT of type Colord.SensorCap>, 5: <enum CD_SENSOR_CAP_PROJECTOR of type Colord.SensorCap>, 6: <enum CD_SENSOR_CAP_AMBIENT of type Colord.SensorCap>, 7: <enum CD_SENSOR_CAP_CALIBRATION of type Colord.SensorCap>, 8: <enum CD_SENSOR_CAP_LED of type Colord.SensorCap>, 9: <enum CD_SENSOR_CAP_PLASMA of type Colord.SensorCap>, 10: <enum CD_SENSOR_CAP_LCD_CCFL of type Colord.SensorCap>, 11: <enum CD_SENSOR_CAP_LCD_RGB_LED of type Colord.SensorCap>, 12: <enum CD_SENSOR_CAP_LCD_WHITE_LED of type Colord.SensorCap>, 13: <enum CD_SENSOR_CAP_WIDE_GAMUT_LCD_CCFL of type Colord.SensorCap>, 14: <enum CD_SENSOR_CAP_WIDE_GAMUT_LCD_RGB_LED of type Colord.SensorCap>, 15: <enum CD_SENSOR_CAP_SPECTRAL of type Colord.SensorCap>, 16: <enum CD_SENSOR_CAP_CALIBRATION_DARK of type Colord.SensorCap>, 17: <enum CD_SENSOR_CAP_CALIBRATION_IRRADIANCE of type Colord.SensorCap>}, '__info__': gi.EnumInfo(SensorCap), 'UNKNOWN': <enum CD_SENSOR_CAP_UNKNOWN of type Colord.SensorCap>, 'LCD': <enum CD_SENSOR_CAP_LCD of type Colord.SensorCap>, 'CRT': <enum CD_SENSOR_CAP_CRT of type Colord.SensorCap>, 'PRINTER': <enum CD_SENSOR_CAP_PRINTER of type Colord.SensorCap>, 'SPOT': <enum CD_SENSOR_CAP_SPOT of type Colord.SensorCap>, 'PROJECTOR': <enum CD_SENSOR_CAP_PROJECTOR of type Colord.SensorCap>, 'AMBIENT': <enum CD_SENSOR_CAP_AMBIENT of type Colord.SensorCap>, 'CALIBRATION': <enum CD_SENSOR_CAP_CALIBRATION of type Colord.SensorCap>, 'LED': <enum CD_SENSOR_CAP_LED of type Colord.SensorCap>, 'PLASMA': <enum CD_SENSOR_CAP_PLASMA of type Colord.SensorCap>, 'LCD_CCFL': <enum CD_SENSOR_CAP_LCD_CCFL of type Colord.SensorCap>, 'LCD_RGB_LED': <enum CD_SENSOR_CAP_LCD_RGB_LED of type Colord.SensorCap>, 'LCD_WHITE_LED': <enum CD_SENSOR_CAP_LCD_WHITE_LED of type Colord.SensorCap>, 'WIDE_GAMUT_LCD_CCFL': <enum CD_SENSOR_CAP_WIDE_GAMUT_LCD_CCFL of type Colord.SensorCap>, 'WIDE_GAMUT_LCD_RGB_LED': <enum CD_SENSOR_CAP_WIDE_GAMUT_LCD_RGB_LED of type Colord.SensorCap>, 'SPECTRAL': <enum CD_SENSOR_CAP_SPECTRAL of type Colord.SensorCap>, 'CALIBRATION_DARK': <enum CD_SENSOR_CAP_CALIBRATION_DARK of type Colord.SensorCap>, 'CALIBRATION_IRRADIANCE': <enum CD_SENSOR_CAP_CALIBRATION_IRRADIANCE of type Colord.SensorCap>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PyColordSensorCap (94892598974960)>'
    __info__ = gi.EnumInfo(SensorCap)


