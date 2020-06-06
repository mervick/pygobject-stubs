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


class SensorKind(__gobject.GEnum):
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


    COLORHUG = 14
    COLORHUG2 = 24
    COLORHUG_PLUS = 17
    COLORIMTRE_HCFR = 12
    COLOR_MUNKI_PHOTO = 3
    COLOR_MUNKI_SMILE = 23
    DTP20 = 5
    DTP22 = 6
    DTP41 = 7
    DTP51 = 8
    DTP92 = 20
    DTP94 = 9
    DUMMY = 1
    HUEY = 2
    I1_DISPLAY1 = 18
    I1_DISPLAY2 = 19
    I1_DISPLAY3 = 13
    I1_MONITOR = 21
    I1_PRO = 11
    SPARK = 26
    SPECTRO_SCAN = 10
    SPYDER = 4
    SPYDER2 = 15
    SPYDER3 = 16
    SPYDER4 = 22
    SPYDER5 = 25
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Colord', '__dict__': <attribute '__dict__' of 'SensorKind' objects>, '__doc__': None, '__gtype__': <GType PyColordSensorKind (94892598987712)>, '__enum_values__': {0: <enum CD_SENSOR_KIND_UNKNOWN of type Colord.SensorKind>, 1: <enum CD_SENSOR_KIND_DUMMY of type Colord.SensorKind>, 2: <enum CD_SENSOR_KIND_HUEY of type Colord.SensorKind>, 3: <enum CD_SENSOR_KIND_COLOR_MUNKI_PHOTO of type Colord.SensorKind>, 4: <enum CD_SENSOR_KIND_SPYDER of type Colord.SensorKind>, 5: <enum CD_SENSOR_KIND_DTP20 of type Colord.SensorKind>, 6: <enum CD_SENSOR_KIND_DTP22 of type Colord.SensorKind>, 7: <enum CD_SENSOR_KIND_DTP41 of type Colord.SensorKind>, 8: <enum CD_SENSOR_KIND_DTP51 of type Colord.SensorKind>, 9: <enum CD_SENSOR_KIND_DTP94 of type Colord.SensorKind>, 10: <enum CD_SENSOR_KIND_SPECTRO_SCAN of type Colord.SensorKind>, 11: <enum CD_SENSOR_KIND_I1_PRO of type Colord.SensorKind>, 12: <enum CD_SENSOR_KIND_COLORIMTRE_HCFR of type Colord.SensorKind>, 13: <enum CD_SENSOR_KIND_I1_DISPLAY3 of type Colord.SensorKind>, 14: <enum CD_SENSOR_KIND_COLORHUG of type Colord.SensorKind>, 15: <enum CD_SENSOR_KIND_SPYDER2 of type Colord.SensorKind>, 16: <enum CD_SENSOR_KIND_SPYDER3 of type Colord.SensorKind>, 17: <enum CD_SENSOR_KIND_COLORHUG_PLUS of type Colord.SensorKind>, 18: <enum CD_SENSOR_KIND_I1_DISPLAY1 of type Colord.SensorKind>, 19: <enum CD_SENSOR_KIND_I1_DISPLAY2 of type Colord.SensorKind>, 20: <enum CD_SENSOR_KIND_DTP92 of type Colord.SensorKind>, 21: <enum CD_SENSOR_KIND_I1_MONITOR of type Colord.SensorKind>, 22: <enum CD_SENSOR_KIND_SPYDER4 of type Colord.SensorKind>, 23: <enum CD_SENSOR_KIND_COLOR_MUNKI_SMILE of type Colord.SensorKind>, 24: <enum CD_SENSOR_KIND_COLORHUG2 of type Colord.SensorKind>, 25: <enum CD_SENSOR_KIND_SPYDER5 of type Colord.SensorKind>, 26: <enum CD_SENSOR_KIND_SPARK of type Colord.SensorKind>}, '__info__': gi.EnumInfo(SensorKind), 'UNKNOWN': <enum CD_SENSOR_KIND_UNKNOWN of type Colord.SensorKind>, 'DUMMY': <enum CD_SENSOR_KIND_DUMMY of type Colord.SensorKind>, 'HUEY': <enum CD_SENSOR_KIND_HUEY of type Colord.SensorKind>, 'COLOR_MUNKI_PHOTO': <enum CD_SENSOR_KIND_COLOR_MUNKI_PHOTO of type Colord.SensorKind>, 'SPYDER': <enum CD_SENSOR_KIND_SPYDER of type Colord.SensorKind>, 'DTP20': <enum CD_SENSOR_KIND_DTP20 of type Colord.SensorKind>, 'DTP22': <enum CD_SENSOR_KIND_DTP22 of type Colord.SensorKind>, 'DTP41': <enum CD_SENSOR_KIND_DTP41 of type Colord.SensorKind>, 'DTP51': <enum CD_SENSOR_KIND_DTP51 of type Colord.SensorKind>, 'DTP94': <enum CD_SENSOR_KIND_DTP94 of type Colord.SensorKind>, 'SPECTRO_SCAN': <enum CD_SENSOR_KIND_SPECTRO_SCAN of type Colord.SensorKind>, 'I1_PRO': <enum CD_SENSOR_KIND_I1_PRO of type Colord.SensorKind>, 'COLORIMTRE_HCFR': <enum CD_SENSOR_KIND_COLORIMTRE_HCFR of type Colord.SensorKind>, 'I1_DISPLAY3': <enum CD_SENSOR_KIND_I1_DISPLAY3 of type Colord.SensorKind>, 'COLORHUG': <enum CD_SENSOR_KIND_COLORHUG of type Colord.SensorKind>, 'SPYDER2': <enum CD_SENSOR_KIND_SPYDER2 of type Colord.SensorKind>, 'SPYDER3': <enum CD_SENSOR_KIND_SPYDER3 of type Colord.SensorKind>, 'COLORHUG_PLUS': <enum CD_SENSOR_KIND_COLORHUG_PLUS of type Colord.SensorKind>, 'I1_DISPLAY1': <enum CD_SENSOR_KIND_I1_DISPLAY1 of type Colord.SensorKind>, 'I1_DISPLAY2': <enum CD_SENSOR_KIND_I1_DISPLAY2 of type Colord.SensorKind>, 'DTP92': <enum CD_SENSOR_KIND_DTP92 of type Colord.SensorKind>, 'I1_MONITOR': <enum CD_SENSOR_KIND_I1_MONITOR of type Colord.SensorKind>, 'SPYDER4': <enum CD_SENSOR_KIND_SPYDER4 of type Colord.SensorKind>, 'COLOR_MUNKI_SMILE': <enum CD_SENSOR_KIND_COLOR_MUNKI_SMILE of type Colord.SensorKind>, 'COLORHUG2': <enum CD_SENSOR_KIND_COLORHUG2 of type Colord.SensorKind>, 'SPYDER5': <enum CD_SENSOR_KIND_SPYDER5 of type Colord.SensorKind>, 'SPARK': <enum CD_SENSOR_KIND_SPARK of type Colord.SensorKind>})"
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
    }
    __gtype__ = None # (!) real value is '<GType PyColordSensorKind (94892598987712)>'
    __info__ = gi.EnumInfo(SensorKind)


