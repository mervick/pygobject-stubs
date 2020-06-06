# encoding: utf-8
# module gi.repository.GWeather
# from /usr/lib64/girepository-1.0/GWeather-3.0.typelib
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


# Variables with simple values

LOCATION_ENTRY_H = 1

TIMEZONE_MENU_H = 1

_namespace = 'GWeather'

_version = '3.0'

__weakref__ = None

# functions

def location_detect_nearest_city_finish(result): # real signature unknown; restored from __doc__
    """ location_detect_nearest_city_finish(result:Gio.AsyncResult) -> GWeather.Location """
    pass

def location_get_world(): # real signature unknown; restored from __doc__
    """ location_get_world() -> GWeather.Location or None """
    pass

def location_level_to_string(level): # real signature unknown; restored from __doc__
    """ location_level_to_string(level:GWeather.LocationLevel) -> str """
    return ""

def sky_to_string(sky): # real signature unknown; restored from __doc__
    """ sky_to_string(sky:GWeather.Sky) -> str """
    return ""

def sky_to_string_full(sky, options): # real signature unknown; restored from __doc__
    """ sky_to_string_full(sky:GWeather.Sky, options:GWeather.FormatOptions) -> str """
    return ""

def temperature_unit_to_real(unit): # real signature unknown; restored from __doc__
    """ temperature_unit_to_real(unit:GWeather.TemperatureUnit) -> GWeather.TemperatureUnit """
    pass

def timezone_get_by_tzid(tzid): # real signature unknown; restored from __doc__
    """ timezone_get_by_tzid(tzid:str) -> GWeather.Timezone """
    pass

def timezone_get_utc(): # real signature unknown; restored from __doc__
    """ timezone_get_utc() -> GWeather.Timezone """
    pass

def wind_direction_to_string(wind): # real signature unknown; restored from __doc__
    """ wind_direction_to_string(wind:GWeather.WindDirection) -> str """
    return ""

def wind_direction_to_string_full(wind, options): # real signature unknown; restored from __doc__
    """ wind_direction_to_string_full(wind:GWeather.WindDirection, options:GWeather.FormatOptions) -> str """
    return ""

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class ConditionPhenomenon(__gobject.GEnum):
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


    DRIZZLE = 1
    DUST = 17
    DUSTSTORM = 20
    DUST_WHIRLS = 23
    FOG = 11
    FUNNEL_CLOUD = 21
    HAIL = 7
    HAZE = 15
    ICE_CRYSTALS = 5
    ICE_PELLETS = 6
    INVALID = -1
    LAST = 24
    MIST = 10
    NONE = 0
    RAIN = 2
    SAND = 14
    SANDSTORM = 19
    SMALL_HAIL = 8
    SMOKE = 12
    SNOW = 3
    SNOW_GRAINS = 4
    SPRAY = 16
    SQUALL = 18
    TORNADO = 22
    UNKNOWN_PRECIPITATION = 9
    VOLCANIC_ASH = 13
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'ConditionPhenomenon' objects>, '__doc__': None, '__gtype__': <GType GWeatherConditionPhenomenon (94766763264688)>, '__enum_values__': {-1: <enum GWEATHER_PHENOMENON_INVALID of type GWeather.ConditionPhenomenon>, 0: <enum GWEATHER_PHENOMENON_NONE of type GWeather.ConditionPhenomenon>, 1: <enum GWEATHER_PHENOMENON_DRIZZLE of type GWeather.ConditionPhenomenon>, 2: <enum GWEATHER_PHENOMENON_RAIN of type GWeather.ConditionPhenomenon>, 3: <enum GWEATHER_PHENOMENON_SNOW of type GWeather.ConditionPhenomenon>, 4: <enum GWEATHER_PHENOMENON_SNOW_GRAINS of type GWeather.ConditionPhenomenon>, 5: <enum GWEATHER_PHENOMENON_ICE_CRYSTALS of type GWeather.ConditionPhenomenon>, 6: <enum GWEATHER_PHENOMENON_ICE_PELLETS of type GWeather.ConditionPhenomenon>, 7: <enum GWEATHER_PHENOMENON_HAIL of type GWeather.ConditionPhenomenon>, 8: <enum GWEATHER_PHENOMENON_SMALL_HAIL of type GWeather.ConditionPhenomenon>, 9: <enum GWEATHER_PHENOMENON_UNKNOWN_PRECIPITATION of type GWeather.ConditionPhenomenon>, 10: <enum GWEATHER_PHENOMENON_MIST of type GWeather.ConditionPhenomenon>, 11: <enum GWEATHER_PHENOMENON_FOG of type GWeather.ConditionPhenomenon>, 12: <enum GWEATHER_PHENOMENON_SMOKE of type GWeather.ConditionPhenomenon>, 13: <enum GWEATHER_PHENOMENON_VOLCANIC_ASH of type GWeather.ConditionPhenomenon>, 14: <enum GWEATHER_PHENOMENON_SAND of type GWeather.ConditionPhenomenon>, 15: <enum GWEATHER_PHENOMENON_HAZE of type GWeather.ConditionPhenomenon>, 16: <enum GWEATHER_PHENOMENON_SPRAY of type GWeather.ConditionPhenomenon>, 17: <enum GWEATHER_PHENOMENON_DUST of type GWeather.ConditionPhenomenon>, 18: <enum GWEATHER_PHENOMENON_SQUALL of type GWeather.ConditionPhenomenon>, 19: <enum GWEATHER_PHENOMENON_SANDSTORM of type GWeather.ConditionPhenomenon>, 20: <enum GWEATHER_PHENOMENON_DUSTSTORM of type GWeather.ConditionPhenomenon>, 21: <enum GWEATHER_PHENOMENON_FUNNEL_CLOUD of type GWeather.ConditionPhenomenon>, 22: <enum GWEATHER_PHENOMENON_TORNADO of type GWeather.ConditionPhenomenon>, 23: <enum GWEATHER_PHENOMENON_DUST_WHIRLS of type GWeather.ConditionPhenomenon>, 24: <enum GWEATHER_PHENOMENON_LAST of type GWeather.ConditionPhenomenon>}, '__info__': gi.EnumInfo(ConditionPhenomenon), 'INVALID': <enum GWEATHER_PHENOMENON_INVALID of type GWeather.ConditionPhenomenon>, 'NONE': <enum GWEATHER_PHENOMENON_NONE of type GWeather.ConditionPhenomenon>, 'DRIZZLE': <enum GWEATHER_PHENOMENON_DRIZZLE of type GWeather.ConditionPhenomenon>, 'RAIN': <enum GWEATHER_PHENOMENON_RAIN of type GWeather.ConditionPhenomenon>, 'SNOW': <enum GWEATHER_PHENOMENON_SNOW of type GWeather.ConditionPhenomenon>, 'SNOW_GRAINS': <enum GWEATHER_PHENOMENON_SNOW_GRAINS of type GWeather.ConditionPhenomenon>, 'ICE_CRYSTALS': <enum GWEATHER_PHENOMENON_ICE_CRYSTALS of type GWeather.ConditionPhenomenon>, 'ICE_PELLETS': <enum GWEATHER_PHENOMENON_ICE_PELLETS of type GWeather.ConditionPhenomenon>, 'HAIL': <enum GWEATHER_PHENOMENON_HAIL of type GWeather.ConditionPhenomenon>, 'SMALL_HAIL': <enum GWEATHER_PHENOMENON_SMALL_HAIL of type GWeather.ConditionPhenomenon>, 'UNKNOWN_PRECIPITATION': <enum GWEATHER_PHENOMENON_UNKNOWN_PRECIPITATION of type GWeather.ConditionPhenomenon>, 'MIST': <enum GWEATHER_PHENOMENON_MIST of type GWeather.ConditionPhenomenon>, 'FOG': <enum GWEATHER_PHENOMENON_FOG of type GWeather.ConditionPhenomenon>, 'SMOKE': <enum GWEATHER_PHENOMENON_SMOKE of type GWeather.ConditionPhenomenon>, 'VOLCANIC_ASH': <enum GWEATHER_PHENOMENON_VOLCANIC_ASH of type GWeather.ConditionPhenomenon>, 'SAND': <enum GWEATHER_PHENOMENON_SAND of type GWeather.ConditionPhenomenon>, 'HAZE': <enum GWEATHER_PHENOMENON_HAZE of type GWeather.ConditionPhenomenon>, 'SPRAY': <enum GWEATHER_PHENOMENON_SPRAY of type GWeather.ConditionPhenomenon>, 'DUST': <enum GWEATHER_PHENOMENON_DUST of type GWeather.ConditionPhenomenon>, 'SQUALL': <enum GWEATHER_PHENOMENON_SQUALL of type GWeather.ConditionPhenomenon>, 'SANDSTORM': <enum GWEATHER_PHENOMENON_SANDSTORM of type GWeather.ConditionPhenomenon>, 'DUSTSTORM': <enum GWEATHER_PHENOMENON_DUSTSTORM of type GWeather.ConditionPhenomenon>, 'FUNNEL_CLOUD': <enum GWEATHER_PHENOMENON_FUNNEL_CLOUD of type GWeather.ConditionPhenomenon>, 'TORNADO': <enum GWEATHER_PHENOMENON_TORNADO of type GWeather.ConditionPhenomenon>, 'DUST_WHIRLS': <enum GWEATHER_PHENOMENON_DUST_WHIRLS of type GWeather.ConditionPhenomenon>, 'LAST': <enum GWEATHER_PHENOMENON_LAST of type GWeather.ConditionPhenomenon>})"
    __enum_values__ = {
        -1: -1,
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
    }
    __gtype__ = None # (!) real value is '<GType GWeatherConditionPhenomenon (94766763264688)>'
    __info__ = gi.EnumInfo(ConditionPhenomenon)


class ConditionQualifier(__gobject.GEnum):
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


    BLOWING = 9
    DRIFTING = 11
    FREEZING = 12
    HEAVY = 4
    INVALID = -1
    LAST = 13
    LIGHT = 2
    MODERATE = 3
    NONE = 0
    PARTIAL = 7
    PATCHES = 6
    SHALLOW = 5
    SHOWERS = 10
    THUNDERSTORM = 8
    VICINITY = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'ConditionQualifier' objects>, '__doc__': None, '__gtype__': <GType GWeatherConditionQualifier (94766763358096)>, '__enum_values__': {-1: <enum GWEATHER_QUALIFIER_INVALID of type GWeather.ConditionQualifier>, 0: <enum GWEATHER_QUALIFIER_NONE of type GWeather.ConditionQualifier>, 1: <enum GWEATHER_QUALIFIER_VICINITY of type GWeather.ConditionQualifier>, 2: <enum GWEATHER_QUALIFIER_LIGHT of type GWeather.ConditionQualifier>, 3: <enum GWEATHER_QUALIFIER_MODERATE of type GWeather.ConditionQualifier>, 4: <enum GWEATHER_QUALIFIER_HEAVY of type GWeather.ConditionQualifier>, 5: <enum GWEATHER_QUALIFIER_SHALLOW of type GWeather.ConditionQualifier>, 6: <enum GWEATHER_QUALIFIER_PATCHES of type GWeather.ConditionQualifier>, 7: <enum GWEATHER_QUALIFIER_PARTIAL of type GWeather.ConditionQualifier>, 8: <enum GWEATHER_QUALIFIER_THUNDERSTORM of type GWeather.ConditionQualifier>, 9: <enum GWEATHER_QUALIFIER_BLOWING of type GWeather.ConditionQualifier>, 10: <enum GWEATHER_QUALIFIER_SHOWERS of type GWeather.ConditionQualifier>, 11: <enum GWEATHER_QUALIFIER_DRIFTING of type GWeather.ConditionQualifier>, 12: <enum GWEATHER_QUALIFIER_FREEZING of type GWeather.ConditionQualifier>, 13: <enum GWEATHER_QUALIFIER_LAST of type GWeather.ConditionQualifier>}, '__info__': gi.EnumInfo(ConditionQualifier), 'INVALID': <enum GWEATHER_QUALIFIER_INVALID of type GWeather.ConditionQualifier>, 'NONE': <enum GWEATHER_QUALIFIER_NONE of type GWeather.ConditionQualifier>, 'VICINITY': <enum GWEATHER_QUALIFIER_VICINITY of type GWeather.ConditionQualifier>, 'LIGHT': <enum GWEATHER_QUALIFIER_LIGHT of type GWeather.ConditionQualifier>, 'MODERATE': <enum GWEATHER_QUALIFIER_MODERATE of type GWeather.ConditionQualifier>, 'HEAVY': <enum GWEATHER_QUALIFIER_HEAVY of type GWeather.ConditionQualifier>, 'SHALLOW': <enum GWEATHER_QUALIFIER_SHALLOW of type GWeather.ConditionQualifier>, 'PATCHES': <enum GWEATHER_QUALIFIER_PATCHES of type GWeather.ConditionQualifier>, 'PARTIAL': <enum GWEATHER_QUALIFIER_PARTIAL of type GWeather.ConditionQualifier>, 'THUNDERSTORM': <enum GWEATHER_QUALIFIER_THUNDERSTORM of type GWeather.ConditionQualifier>, 'BLOWING': <enum GWEATHER_QUALIFIER_BLOWING of type GWeather.ConditionQualifier>, 'SHOWERS': <enum GWEATHER_QUALIFIER_SHOWERS of type GWeather.ConditionQualifier>, 'DRIFTING': <enum GWEATHER_QUALIFIER_DRIFTING of type GWeather.ConditionQualifier>, 'FREEZING': <enum GWEATHER_QUALIFIER_FREEZING of type GWeather.ConditionQualifier>, 'LAST': <enum GWEATHER_QUALIFIER_LAST of type GWeather.ConditionQualifier>})"
    __enum_values__ = {
        -1: -1,
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
    }
    __gtype__ = None # (!) real value is '<GType GWeatherConditionQualifier (94766763358096)>'
    __info__ = gi.EnumInfo(ConditionQualifier)


class Conditions(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Conditions()
    """
    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def to_string_full(self, options): # real signature unknown; restored from __doc__
        """ to_string_full(self, options:GWeather.FormatOptions) -> str """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    phenomenon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qualifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    significant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Conditions), '__module__': 'gi.repository.GWeather', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Conditions' objects>, '__weakref__': <attribute '__weakref__' of 'Conditions' objects>, '__doc__': None, 'significant': <property object at 0x7f73c7c2cef0>, 'phenomenon': <property object at 0x7f73c7c2cf40>, 'qualifier': <property object at 0x7f73c7c2cf90>, 'to_string': gi.FunctionInfo(to_string), 'to_string_full': gi.FunctionInfo(to_string_full)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Conditions)


class DistanceUnit(__gobject.GEnum):
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


    DEFAULT = 1
    INVALID = 0
    KM = 3
    METERS = 2
    MILES = 4
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'DistanceUnit' objects>, '__doc__': None, '__gtype__': <GType GWeatherDistanceUnit (94766763281120)>, '__enum_values__': {0: <enum GWEATHER_DISTANCE_UNIT_INVALID of type GWeather.DistanceUnit>, 1: <enum GWEATHER_DISTANCE_UNIT_DEFAULT of type GWeather.DistanceUnit>, 2: <enum GWEATHER_DISTANCE_UNIT_METERS of type GWeather.DistanceUnit>, 3: <enum GWEATHER_DISTANCE_UNIT_KM of type GWeather.DistanceUnit>, 4: <enum GWEATHER_DISTANCE_UNIT_MILES of type GWeather.DistanceUnit>}, '__info__': gi.EnumInfo(DistanceUnit), 'INVALID': <enum GWEATHER_DISTANCE_UNIT_INVALID of type GWeather.DistanceUnit>, 'DEFAULT': <enum GWEATHER_DISTANCE_UNIT_DEFAULT of type GWeather.DistanceUnit>, 'METERS': <enum GWEATHER_DISTANCE_UNIT_METERS of type GWeather.DistanceUnit>, 'KM': <enum GWEATHER_DISTANCE_UNIT_KM of type GWeather.DistanceUnit>, 'MILES': <enum GWEATHER_DISTANCE_UNIT_MILES of type GWeather.DistanceUnit>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherDistanceUnit (94766763281120)>'
    __info__ = gi.EnumInfo(DistanceUnit)


class FormatOptions(__gobject.GFlags):
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


    DEFAULT = 0
    NO_CAPITALIZATION = 2
    SENTENCE_CAPITALIZATION = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'FormatOptions' objects>, '__doc__': None, '__gtype__': <GType GWeatherFormatOptions (94766763264880)>, '__flags_values__': {0: <flags 0 of type GWeather.FormatOptions>, 1: <flags GWEATHER_FORMAT_OPTION_SENTENCE_CAPITALIZATION of type GWeather.FormatOptions>, 2: <flags GWEATHER_FORMAT_OPTION_NO_CAPITALIZATION of type GWeather.FormatOptions>}, '__info__': gi.EnumInfo(FormatOptions), 'DEFAULT': <flags 0 of type GWeather.FormatOptions>, 'SENTENCE_CAPITALIZATION': <flags GWEATHER_FORMAT_OPTION_SENTENCE_CAPITALIZATION of type GWeather.FormatOptions>, 'NO_CAPITALIZATION': <flags GWEATHER_FORMAT_OPTION_NO_CAPITALIZATION of type GWeather.FormatOptions>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherFormatOptions (94766763264880)>'
    __info__ = gi.EnumInfo(FormatOptions)


class Info(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Info(**properties)
        new(location:GWeather.Location=None) -> GWeather.Info
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_updated(self, *args, **kwargs): # real signature unknown
        """ updated(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_apparent(self): # real signature unknown; restored from __doc__
        """ get_apparent(self) -> str """
        return ""

    def get_attribution(self): # real signature unknown; restored from __doc__
        """ get_attribution(self) -> str """
        return ""

    def get_conditions(self): # real signature unknown; restored from __doc__
        """ get_conditions(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dew(self): # real signature unknown; restored from __doc__
        """ get_dew(self) -> str """
        return ""

    def get_enabled_providers(self): # real signature unknown; restored from __doc__
        """ get_enabled_providers(self) -> GWeather.Provider """
        pass

    def get_forecast_list(self): # real signature unknown; restored from __doc__
        """ get_forecast_list(self) -> list """
        return []

    def get_humidity(self): # real signature unknown; restored from __doc__
        """ get_humidity(self) -> str """
        return ""

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> GWeather.Location """
        pass

    def get_location_name(self): # real signature unknown; restored from __doc__
        """ get_location_name(self) -> str """
        return ""

    def get_pressure(self): # real signature unknown; restored from __doc__
        """ get_pressure(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_radar(self): # real signature unknown; restored from __doc__
        """ get_radar(self) -> GdkPixbuf.PixbufAnimation """
        pass

    def get_sky(self): # real signature unknown; restored from __doc__
        """ get_sky(self) -> str """
        return ""

    def get_sunrise(self): # real signature unknown; restored from __doc__
        """ get_sunrise(self) -> str """
        return ""

    def get_sunset(self): # real signature unknown; restored from __doc__
        """ get_sunset(self) -> str """
        return ""

    def get_symbolic_icon_name(self): # real signature unknown; restored from __doc__
        """ get_symbolic_icon_name(self) -> str """
        return ""

    def get_temp(self): # real signature unknown; restored from __doc__
        """ get_temp(self) -> str """
        return ""

    def get_temp_max(self): # real signature unknown; restored from __doc__
        """ get_temp_max(self) -> str """
        return ""

    def get_temp_min(self): # real signature unknown; restored from __doc__
        """ get_temp_min(self) -> str """
        return ""

    def get_temp_summary(self): # real signature unknown; restored from __doc__
        """ get_temp_summary(self) -> str """
        return ""

    def get_upcoming_moonphases(self): # real signature unknown; restored from __doc__
        """ get_upcoming_moonphases(self) -> bool, phases:list """
        return False

    def get_update(self): # real signature unknown; restored from __doc__
        """ get_update(self) -> str """
        return ""

    def get_value_apparent(self, unit): # real signature unknown; restored from __doc__
        """ get_value_apparent(self, unit:GWeather.TemperatureUnit) -> bool, value:float """
        return False

    def get_value_conditions(self): # real signature unknown; restored from __doc__
        """ get_value_conditions(self) -> bool, phenomenon:GWeather.ConditionPhenomenon, qualifier:GWeather.ConditionQualifier """
        return False

    def get_value_dew(self, unit): # real signature unknown; restored from __doc__
        """ get_value_dew(self, unit:GWeather.TemperatureUnit) -> bool, value:float """
        return False

    def get_value_moonphase(self): # real signature unknown; restored from __doc__
        """ get_value_moonphase(self) -> bool, value:float, lat:float """
        return False

    def get_value_pressure(self, unit): # real signature unknown; restored from __doc__
        """ get_value_pressure(self, unit:GWeather.PressureUnit) -> bool, value:float """
        return False

    def get_value_sky(self): # real signature unknown; restored from __doc__
        """ get_value_sky(self) -> bool, sky:GWeather.Sky """
        return False

    def get_value_sunrise(self): # real signature unknown; restored from __doc__
        """ get_value_sunrise(self) -> bool, value:int """
        return False

    def get_value_sunset(self): # real signature unknown; restored from __doc__
        """ get_value_sunset(self) -> bool, value:int """
        return False

    def get_value_temp(self, unit): # real signature unknown; restored from __doc__
        """ get_value_temp(self, unit:GWeather.TemperatureUnit) -> bool, value:float """
        return False

    def get_value_temp_max(self, unit): # real signature unknown; restored from __doc__
        """ get_value_temp_max(self, unit:GWeather.TemperatureUnit) -> bool, value:float """
        return False

    def get_value_temp_min(self, unit): # real signature unknown; restored from __doc__
        """ get_value_temp_min(self, unit:GWeather.TemperatureUnit) -> bool, value:float """
        return False

    def get_value_update(self): # real signature unknown; restored from __doc__
        """ get_value_update(self) -> bool, value:int """
        return False

    def get_value_visibility(self, unit): # real signature unknown; restored from __doc__
        """ get_value_visibility(self, unit:GWeather.DistanceUnit) -> bool, value:float """
        return False

    def get_value_wind(self, unit): # real signature unknown; restored from __doc__
        """ get_value_wind(self, unit:GWeather.SpeedUnit) -> bool, speed:float, direction:GWeather.WindDirection """
        return False

    def get_visibility(self): # real signature unknown; restored from __doc__
        """ get_visibility(self) -> str """
        return ""

    def get_weather_summary(self): # real signature unknown; restored from __doc__
        """ get_weather_summary(self) -> str """
        return ""

    def get_wind(self): # real signature unknown; restored from __doc__
        """ get_wind(self) -> str """
        return ""

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_daytime(self): # real signature unknown; restored from __doc__
        """ is_daytime(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def network_error(self): # real signature unknown; restored from __doc__
        """ network_error(self) -> bool """
        return False

    def new(self, location=None): # real signature unknown; restored from __doc__
        """ new(location:GWeather.Location=None) -> GWeather.Info """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def next_sun_event(self): # real signature unknown; restored from __doc__
        """ next_sun_event(self) -> int """
        return 0

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_enabled_providers(self, providers): # real signature unknown; restored from __doc__
        """ set_enabled_providers(self, providers:GWeather.Provider) """
        pass

    def set_location(self, location=None): # real signature unknown; restored from __doc__
        """ set_location(self, location:GWeather.Location=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def store_cache(self): # real signature unknown; restored from __doc__
        """ store_cache() """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update(self): # real signature unknown; restored from __doc__
        """ update(self) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, **properties): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f73c7b912e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Info), '__module__': 'gi.repository.GWeather', '__gtype__': <GType GWeatherInfo (94766763289168)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'store_cache': gi.FunctionInfo(store_cache), 'abort': gi.FunctionInfo(abort), 'get_apparent': gi.FunctionInfo(get_apparent), 'get_attribution': gi.FunctionInfo(get_attribution), 'get_conditions': gi.FunctionInfo(get_conditions), 'get_dew': gi.FunctionInfo(get_dew), 'get_enabled_providers': gi.FunctionInfo(get_enabled_providers), 'get_forecast_list': gi.FunctionInfo(get_forecast_list), 'get_humidity': gi.FunctionInfo(get_humidity), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_location': gi.FunctionInfo(get_location), 'get_location_name': gi.FunctionInfo(get_location_name), 'get_pressure': gi.FunctionInfo(get_pressure), 'get_radar': gi.FunctionInfo(get_radar), 'get_sky': gi.FunctionInfo(get_sky), 'get_sunrise': gi.FunctionInfo(get_sunrise), 'get_sunset': gi.FunctionInfo(get_sunset), 'get_symbolic_icon_name': gi.FunctionInfo(get_symbolic_icon_name), 'get_temp': gi.FunctionInfo(get_temp), 'get_temp_max': gi.FunctionInfo(get_temp_max), 'get_temp_min': gi.FunctionInfo(get_temp_min), 'get_temp_summary': gi.FunctionInfo(get_temp_summary), 'get_upcoming_moonphases': gi.FunctionInfo(get_upcoming_moonphases), 'get_update': gi.FunctionInfo(get_update), 'get_value_apparent': gi.FunctionInfo(get_value_apparent), 'get_value_conditions': gi.FunctionInfo(get_value_conditions), 'get_value_dew': gi.FunctionInfo(get_value_dew), 'get_value_moonphase': gi.FunctionInfo(get_value_moonphase), 'get_value_pressure': gi.FunctionInfo(get_value_pressure), 'get_value_sky': gi.FunctionInfo(get_value_sky), 'get_value_sunrise': gi.FunctionInfo(get_value_sunrise), 'get_value_sunset': gi.FunctionInfo(get_value_sunset), 'get_value_temp': gi.FunctionInfo(get_value_temp), 'get_value_temp_max': gi.FunctionInfo(get_value_temp_max), 'get_value_temp_min': gi.FunctionInfo(get_value_temp_min), 'get_value_update': gi.FunctionInfo(get_value_update), 'get_value_visibility': gi.FunctionInfo(get_value_visibility), 'get_value_wind': gi.FunctionInfo(get_value_wind), 'get_visibility': gi.FunctionInfo(get_visibility), 'get_weather_summary': gi.FunctionInfo(get_weather_summary), 'get_wind': gi.FunctionInfo(get_wind), 'is_daytime': gi.FunctionInfo(is_daytime), 'is_valid': gi.FunctionInfo(is_valid), 'network_error': gi.FunctionInfo(network_error), 'next_sun_event': gi.FunctionInfo(next_sun_event), 'set_enabled_providers': gi.FunctionInfo(set_enabled_providers), 'set_location': gi.FunctionInfo(set_location), 'update': gi.FunctionInfo(update), 'do_updated': gi.VFuncInfo(updated), 'parent_instance': <property object at 0x7f73c7b7cbd0>, 'priv': <property object at 0x7f73c7b7ccc0>})"
    __gdoc__ = 'Object GWeatherInfo\n\nSignals from GWeatherInfo:\n  updated ()\n\nProperties from GWeatherInfo:\n  location -> GWeatherLocation: Location\n    The location this info represents\n  enabled-providers -> GWeatherProvider: Enabled providers\n    A bitmask of enabled weather service providers\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GWeatherInfo (94766763289168)>'
    __info__ = ObjectInfo(Info)


class InfoClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        InfoClass()
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    updated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(InfoClass), '__module__': 'gi.repository.GWeather', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'InfoClass' objects>, '__weakref__': <attribute '__weakref__' of 'InfoClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f73c7b7ce50>, 'updated': <property object at 0x7f73c7b7cf40>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(InfoClass)


class InfoPrivate(__gi.Struct):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(InfoPrivate), '__module__': 'gi.repository.GWeather', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'InfoPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'InfoPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(InfoPrivate)


class Location(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_detached(name:str, icao:str=None, latitude:float, longitude:float) -> GWeather.Location
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def deserialize(self, serialized): # real signature unknown; restored from __doc__
        """ deserialize(self, serialized:GLib.Variant) -> GWeather.Location """
        pass

    def detect_nearest_city(self, lat, lon, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ detect_nearest_city(self, lat:float, lon:float, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def detect_nearest_city_finish(self, result): # real signature unknown; restored from __doc__
        """ detect_nearest_city_finish(result:Gio.AsyncResult) -> GWeather.Location """
        pass

    def equal(self, two): # real signature unknown; restored from __doc__
        """ equal(self, two:GWeather.Location) -> bool """
        return False

    def find_by_country_code(self, country_code): # real signature unknown; restored from __doc__
        """ find_by_country_code(self, country_code:str) -> GWeather.Location """
        pass

    def find_by_station_code(self, station_code): # real signature unknown; restored from __doc__
        """ find_by_station_code(self, station_code:str) -> GWeather.Location """
        pass

    def find_nearest_city(self, lat, lon): # real signature unknown; restored from __doc__
        """ find_nearest_city(self, lat:float, lon:float) -> GWeather.Location """
        pass

    def find_nearest_city_full(self, lat, lon, func=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_nearest_city_full(self, lat:float, lon:float, func:GWeather.FilterFunc=None, user_data=None) -> GWeather.Location """
        pass

    def free_timezones(self, zones): # real signature unknown; restored from __doc__
        """ free_timezones(self, zones:GWeather.Timezone) """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_city_name(self): # real signature unknown; restored from __doc__
        """ get_city_name(self) -> str or None """
        return ""

    def get_code(self): # real signature unknown; restored from __doc__
        """ get_code(self) -> str or None """
        return ""

    def get_coords(self): # real signature unknown; restored from __doc__
        """ get_coords(self) -> latitude:float, longitude:float """
        pass

    def get_country(self): # real signature unknown; restored from __doc__
        """ get_country(self) -> str or None """
        return ""

    def get_country_name(self): # real signature unknown; restored from __doc__
        """ get_country_name(self) -> str or None """
        return ""

    def get_distance(self, loc2): # real signature unknown; restored from __doc__
        """ get_distance(self, loc2:GWeather.Location) -> float """
        return 0.0

    def get_english_name(self): # real signature unknown; restored from __doc__
        """ get_english_name(self) -> str """
        return ""

    def get_level(self): # real signature unknown; restored from __doc__
        """ get_level(self) -> GWeather.LocationLevel """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> GWeather.Location or None """
        pass

    def get_sort_name(self): # real signature unknown; restored from __doc__
        """ get_sort_name(self) -> str """
        return ""

    def get_timezone(self): # real signature unknown; restored from __doc__
        """ get_timezone(self) -> GWeather.Timezone or None """
        pass

    def get_timezones(self): # real signature unknown; restored from __doc__
        """ get_timezones(self) -> list """
        return []

    def get_timezone_str(self): # real signature unknown; restored from __doc__
        """ get_timezone_str(self) -> str or None """
        return ""

    def get_world(self): # real signature unknown; restored from __doc__
        """ get_world() -> GWeather.Location or None """
        pass

    def has_coords(self): # real signature unknown; restored from __doc__
        """ has_coords(self) -> bool """
        return False

    def new_detached(self, name, icao=None, latitude, longitude): # real signature unknown; restored from __doc__
        """ new_detached(name:str, icao:str=None, latitude:float, longitude:float) -> GWeather.Location """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GWeather.Location """
        pass

    def serialize(self): # real signature unknown; restored from __doc__
        """ serialize(self) -> GLib.Variant """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Location), '__module__': 'gi.repository.GWeather', '__gtype__': <GType GWeatherLocation (94766763400304)>, '__dict__': <attribute '__dict__' of 'Location' objects>, '__weakref__': <attribute '__weakref__' of 'Location' objects>, '__doc__': None, 'new_detached': gi.FunctionInfo(new_detached), 'deserialize': gi.FunctionInfo(deserialize), 'detect_nearest_city': gi.FunctionInfo(detect_nearest_city), 'equal': gi.FunctionInfo(equal), 'find_by_country_code': gi.FunctionInfo(find_by_country_code), 'find_by_station_code': gi.FunctionInfo(find_by_station_code), 'find_nearest_city': gi.FunctionInfo(find_nearest_city), 'find_nearest_city_full': gi.FunctionInfo(find_nearest_city_full), 'free_timezones': gi.FunctionInfo(free_timezones), 'get_children': gi.FunctionInfo(get_children), 'get_city_name': gi.FunctionInfo(get_city_name), 'get_code': gi.FunctionInfo(get_code), 'get_coords': gi.FunctionInfo(get_coords), 'get_country': gi.FunctionInfo(get_country), 'get_country_name': gi.FunctionInfo(get_country_name), 'get_distance': gi.FunctionInfo(get_distance), 'get_english_name': gi.FunctionInfo(get_english_name), 'get_level': gi.FunctionInfo(get_level), 'get_name': gi.FunctionInfo(get_name), 'get_parent': gi.FunctionInfo(get_parent), 'get_sort_name': gi.FunctionInfo(get_sort_name), 'get_timezone': gi.FunctionInfo(get_timezone), 'get_timezone_str': gi.FunctionInfo(get_timezone_str), 'get_timezones': gi.FunctionInfo(get_timezones), 'has_coords': gi.FunctionInfo(has_coords), 'ref': gi.FunctionInfo(ref), 'serialize': gi.FunctionInfo(serialize), 'unref': gi.FunctionInfo(unref), 'detect_nearest_city_finish': gi.FunctionInfo(detect_nearest_city_finish), 'get_world': gi.FunctionInfo(get_world)})"
    __gtype__ = None # (!) real value is '<GType GWeatherLocation (94766763400304)>'
    __info__ = StructInfo(Location)


class LocationEntry(__gi_repository_Gtk.SearchEntry):
    """
    :Constructors:
    
    ::
    
        LocationEntry(**properties)
        new(top:GWeather.Location) -> Gtk.Widget
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def add_accelerator(self, accel_signal, accel_group, accel_key, accel_mods, accel_flags): # real signature unknown; restored from __doc__
        """ add_accelerator(self, accel_signal:str, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType, accel_flags:Gtk.AccelFlags) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def add_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ add_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def add_events(self, events): # real signature unknown; restored from __doc__
        """ add_events(self, events:int) """
        pass

    def add_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ add_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def add_tick_callback(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_tick_callback(self, callback:Gtk.TickCallback, user_data=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def bind_template_callback_full(self, callback_name, callback_symbol): # real signature unknown; restored from __doc__
        """ bind_template_callback_full(self, callback_name:str, callback_symbol:GObject.Callback) """
        pass

    def bind_template_child_full(self, name, internal_child, struct_offset): # real signature unknown; restored from __doc__
        """ bind_template_child_full(self, name:str, internal_child:bool, struct_offset:int) """
        pass

    def can_activate_accel(self, signal_id): # real signature unknown; restored from __doc__
        """ can_activate_accel(self, signal_id:int) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def child_focus(self, direction): # real signature unknown; restored from __doc__
        """ child_focus(self, direction:Gtk.DirectionType) -> bool """
        return False

    def child_notify(self, child_property): # real signature unknown; restored from __doc__
        """ child_notify(self, child_property:str) """
        pass

    def class_path(self): # real signature unknown; restored from __doc__
        """ class_path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def compute_expand(self, orientation): # real signature unknown; restored from __doc__
        """ compute_expand(self, orientation:Gtk.Orientation) -> bool """
        return False

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def copy_clipboard(self): # real signature unknown; restored from __doc__
        """ copy_clipboard(self) """
        pass

    def create_pango_context(self): # real signature unknown; restored from __doc__
        """ create_pango_context(self) -> Pango.Context """
        pass

    def create_pango_layout(self, text=None): # real signature unknown; restored from __doc__
        """ create_pango_layout(self, text:str=None) -> Pango.Layout """
        pass

    def custom_finished(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_finished(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_end(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_tag_end(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_start(self, builder, child=None, tagname): # real signature unknown; restored from __doc__
        """ custom_tag_start(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str) -> bool, parser:GLib.MarkupParser, data """
        return False

    def cut_clipboard(self): # real signature unknown; restored from __doc__
        """ cut_clipboard(self) """
        pass

    def delete_selection(self): # real signature unknown; restored from __doc__
        """ delete_selection(self) """
        pass

    def delete_text(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ delete_text(self, start_pos:int, end_pos:int) """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def destroyed(self, widget_pointer): # real signature unknown; restored from __doc__
        """ destroyed(self, widget_pointer:Gtk.Widget) -> widget_pointer:Gtk.Widget """
        pass

    def device_is_shadowed(self, device): # real signature unknown; restored from __doc__
        """ device_is_shadowed(self, device:Gdk.Device) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) """
        pass

    def do_adjust_baseline_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_allocation(self, baseline:int) """
        pass

    def do_adjust_baseline_request(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_request(self, minimum_baseline:int, natural_baseline:int) """
        pass

    def do_adjust_size_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_size_allocation(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int, allocated_pos:int, allocated_size:int) """
        pass

    def do_adjust_size_request(self, *args, **kwargs): # real signature unknown
        """ adjust_size_request(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int) """
        pass

    def do_backspace(self, *args, **kwargs): # real signature unknown
        """ backspace(self) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_can_activate_accel(self, *args, **kwargs): # real signature unknown
        """ can_activate_accel(self, signal_id:int) -> bool """
        pass

    def do_child_notify(self, *args, **kwargs): # real signature unknown
        """ child_notify(self, child_property:GObject.ParamSpec) """
        pass

    def do_composited_changed(self, *args, **kwargs): # real signature unknown
        """ composited_changed(self) """
        pass

    def do_compute_expand(self, *args, **kwargs): # real signature unknown
        """ compute_expand(self, hexpand_p:bool, vexpand_p:bool) """
        pass

    def do_configure_event(self, *args, **kwargs): # real signature unknown
        """ configure_event(self, event:Gdk.EventConfigure) -> bool """
        pass

    def do_copy_clipboard(self, *args, **kwargs): # real signature unknown
        """ copy_clipboard(self) """
        pass

    def do_cut_clipboard(self, *args, **kwargs): # real signature unknown
        """ cut_clipboard(self) """
        pass

    def do_damage_event(self, *args, **kwargs): # real signature unknown
        """ damage_event(self, event:Gdk.EventExpose) -> bool """
        pass

    def do_delete_event(self, *args, **kwargs): # real signature unknown
        """ delete_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_delete_from_cursor(self, *args, **kwargs): # real signature unknown
        """ delete_from_cursor(self, type:Gtk.DeleteType, count:int) """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_destroy_event(self, *args, **kwargs): # real signature unknown
        """ destroy_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_direction_changed(self, *args, **kwargs): # real signature unknown
        """ direction_changed(self, previous_direction:Gtk.TextDirection) """
        pass

    def do_dispatch_child_properties_changed(self, *args, **kwargs): # real signature unknown
        """ dispatch_child_properties_changed(self, n_pspecs:int, pspecs:GObject.ParamSpec) """
        pass

    def do_drag_begin(self, *args, **kwargs): # real signature unknown
        """ drag_begin(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_delete(self, *args, **kwargs): # real signature unknown
        """ drag_data_delete(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_get(self, *args, **kwargs): # real signature unknown
        """ drag_data_get(self, context:Gdk.DragContext, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_data_received(self, *args, **kwargs): # real signature unknown
        """ drag_data_received(self, context:Gdk.DragContext, x:int, y:int, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_drop(self, *args, **kwargs): # real signature unknown
        """ drag_drop(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_drag_end(self, *args, **kwargs): # real signature unknown
        """ drag_end(self, context:Gdk.DragContext) """
        pass

    def do_drag_failed(self, *args, **kwargs): # real signature unknown
        """ drag_failed(self, context:Gdk.DragContext, result:Gtk.DragResult) -> bool """
        pass

    def do_drag_leave(self, *args, **kwargs): # real signature unknown
        """ drag_leave(self, context:Gdk.DragContext, time_:int) """
        pass

    def do_drag_motion(self, *args, **kwargs): # real signature unknown
        """ drag_motion(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_draw(self, *args, **kwargs): # real signature unknown
        """ draw(self, cr:cairo.Context) -> bool """
        pass

    def do_enter_notify_event(self, *args, **kwargs): # real signature unknown
        """ enter_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gdk.Event) -> bool """
        pass

    def do_focus(self, *args, **kwargs): # real signature unknown
        """ focus(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_focus_in_event(self, *args, **kwargs): # real signature unknown
        """ focus_in_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_focus_out_event(self, *args, **kwargs): # real signature unknown
        """ focus_out_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_get_accessible(self, *args, **kwargs): # real signature unknown
        """ get_accessible(self) -> Atk.Object """
        pass

    def do_get_frame_size(self, *args, **kwargs): # real signature unknown
        """ get_frame_size(self, x:int, y:int, width:int, height:int) """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_height_and_baseline_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def do_get_preferred_height_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def do_get_preferred_width_for_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def do_get_request_mode(self, *args, **kwargs): # real signature unknown
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def do_get_text_area_size(self, *args, **kwargs): # real signature unknown
        """ get_text_area_size(self, x:int, y:int, width:int, height:int) """
        pass

    def do_grab_broken_event(self, *args, **kwargs): # real signature unknown
        """ grab_broken_event(self, event:Gdk.EventGrabBroken) -> bool """
        pass

    def do_grab_focus(self, *args, **kwargs): # real signature unknown
        """ grab_focus(self) """
        pass

    def do_grab_notify(self, *args, **kwargs): # real signature unknown
        """ grab_notify(self, was_grabbed:bool) """
        pass

    def do_hide(self, *args, **kwargs): # real signature unknown
        """ hide(self) """
        pass

    def do_hierarchy_changed(self, *args, **kwargs): # real signature unknown
        """ hierarchy_changed(self, previous_toplevel:Gtk.Widget) """
        pass

    def do_insert_at_cursor(self, *args, **kwargs): # real signature unknown
        """ insert_at_cursor(self, str:str) """
        pass

    def do_insert_emoji(self, *args, **kwargs): # real signature unknown
        """ insert_emoji(self) """
        pass

    def do_keynav_failed(self, *args, **kwargs): # real signature unknown
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_key_press_event(self, *args, **kwargs): # real signature unknown
        """ key_press_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_key_release_event(self, *args, **kwargs): # real signature unknown
        """ key_release_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_leave_notify_event(self, *args, **kwargs): # real signature unknown
        """ leave_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_map(self, *args, **kwargs): # real signature unknown
        """ map(self) """
        pass

    def do_map_event(self, *args, **kwargs): # real signature unknown
        """ map_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_mnemonic_activate(self, *args, **kwargs): # real signature unknown
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        pass

    def do_motion_notify_event(self, *args, **kwargs): # real signature unknown
        """ motion_notify_event(self, event:Gdk.EventMotion) -> bool """
        pass

    def do_move_cursor(self, *args, **kwargs): # real signature unknown
        """ move_cursor(self, step:Gtk.MovementStep, count:int, extend_selection:bool) """
        pass

    def do_move_focus(self, *args, **kwargs): # real signature unknown
        """ move_focus(self, direction:Gtk.DirectionType) """
        pass

    def do_next_match(self, *args, **kwargs): # real signature unknown
        """ next_match(self) """
        pass

    def do_parent_set(self, *args, **kwargs): # real signature unknown
        """ parent_set(self, previous_parent:Gtk.Widget) """
        pass

    def do_paste_clipboard(self, *args, **kwargs): # real signature unknown
        """ paste_clipboard(self) """
        pass

    def do_populate_popup(self, *args, **kwargs): # real signature unknown
        """ populate_popup(self, popup:Gtk.Widget) """
        pass

    def do_popup_menu(self, *args, **kwargs): # real signature unknown
        """ popup_menu(self) -> bool """
        pass

    def do_previous_match(self, *args, **kwargs): # real signature unknown
        """ previous_match(self) """
        pass

    def do_property_notify_event(self, *args, **kwargs): # real signature unknown
        """ property_notify_event(self, event:Gdk.EventProperty) -> bool """
        pass

    def do_proximity_in_event(self, *args, **kwargs): # real signature unknown
        """ proximity_in_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_proximity_out_event(self, *args, **kwargs): # real signature unknown
        """ proximity_out_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_query_tooltip(self, *args, **kwargs): # real signature unknown
        """ query_tooltip(self, x:int, y:int, keyboard_tooltip:bool, tooltip:Gtk.Tooltip) -> bool """
        pass

    def do_queue_draw_region(self, *args, **kwargs): # real signature unknown
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def do_realize(self, *args, **kwargs): # real signature unknown
        """ realize(self) """
        pass

    def do_screen_changed(self, *args, **kwargs): # real signature unknown
        """ screen_changed(self, previous_screen:Gdk.Screen) """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Gdk.EventScroll) -> bool """
        pass

    def do_search_changed(self, *args, **kwargs): # real signature unknown
        """ search_changed(self) """
        pass

    def do_selection_clear_event(self, *args, **kwargs): # real signature unknown
        """ selection_clear_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_get(self, *args, **kwargs): # real signature unknown
        """ selection_get(self, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_selection_notify_event(self, *args, **kwargs): # real signature unknown
        """ selection_notify_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_received(self, *args, **kwargs): # real signature unknown
        """ selection_received(self, selection_data:Gtk.SelectionData, time_:int) """
        pass

    def do_selection_request_event(self, *args, **kwargs): # real signature unknown
        """ selection_request_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_show(self, *args, **kwargs): # real signature unknown
        """ show(self) """
        pass

    def do_show_all(self, *args, **kwargs): # real signature unknown
        """ show_all(self) """
        pass

    def do_show_help(self, *args, **kwargs): # real signature unknown
        """ show_help(self, help_type:Gtk.WidgetHelpType) -> bool """
        pass

    def do_size_allocate(self, *args, **kwargs): # real signature unknown
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, previous_state:Gtk.StateType) """
        pass

    def do_state_flags_changed(self, *args, **kwargs): # real signature unknown
        """ state_flags_changed(self, previous_state_flags:Gtk.StateFlags) """
        pass

    def do_stop_search(self, *args, **kwargs): # real signature unknown
        """ stop_search(self) """
        pass

    def do_style_set(self, *args, **kwargs): # real signature unknown
        """ style_set(self, previous_style:Gtk.Style) """
        pass

    def do_style_updated(self, *args, **kwargs): # real signature unknown
        """ style_updated(self) """
        pass

    def do_toggle_overwrite(self, *args, **kwargs): # real signature unknown
        """ toggle_overwrite(self) """
        pass

    def do_touch_event(self, *args, **kwargs): # real signature unknown
        """ touch_event(self, event:Gdk.EventTouch) -> bool """
        pass

    def do_unmap(self, *args, **kwargs): # real signature unknown
        """ unmap(self) """
        pass

    def do_unmap_event(self, *args, **kwargs): # real signature unknown
        """ unmap_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_unrealize(self, *args, **kwargs): # real signature unknown
        """ unrealize(self) """
        pass

    def do_visibility_notify_event(self, *args, **kwargs): # real signature unknown
        """ visibility_notify_event(self, event:Gdk.EventVisibility) -> bool """
        pass

    def do_window_state_event(self, *args, **kwargs): # real signature unknown
        """ window_state_event(self, event:Gdk.EventWindowState) -> bool """
        pass

    def drag_begin(self, targets, actions, button, event=None): # real signature unknown; restored from __doc__
        """ drag_begin(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None) -> Gdk.DragContext """
        pass

    def drag_begin_with_coordinates(self, targets, actions, button, event=None, x, y): # real signature unknown; restored from __doc__
        """ drag_begin_with_coordinates(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None, x:int, y:int) -> Gdk.DragContext """
        pass

    def drag_check_threshold(self, start_x, start_y, current_x, current_y): # real signature unknown; restored from __doc__
        """ drag_check_threshold(self, start_x:int, start_y:int, current_x:int, current_y:int) -> bool """
        return False

    def drag_dest_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_image_targets(self) """
        pass

    def drag_dest_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_text_targets(self) """
        pass

    def drag_dest_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_uri_targets(self) """
        pass

    def drag_dest_find_target(self, context, target_list=None): # real signature unknown; restored from __doc__
        """ drag_dest_find_target(self, context:Gdk.DragContext, target_list:Gtk.TargetList=None) -> Gdk.Atom """
        pass

    def drag_dest_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_dest_get_track_motion(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_track_motion(self) -> bool """
        return False

    def drag_dest_set(self, flags, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_dest_set(self, flags:Gtk.DestDefaults, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_dest_set_proxy(self, proxy_window, protocol, use_coordinates): # real signature unknown; restored from __doc__
        """ drag_dest_set_proxy(self, proxy_window:Gdk.Window, protocol:Gdk.DragProtocol, use_coordinates:bool) """
        pass

    def drag_dest_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_dest_set_track_motion(self, track_motion): # real signature unknown; restored from __doc__
        """ drag_dest_set_track_motion(self, track_motion:bool) """
        pass

    def drag_dest_unset(self): # real signature unknown; restored from __doc__
        """ drag_dest_unset(self) """
        pass

    def drag_get_data(self, context, target, time_): # real signature unknown; restored from __doc__
        """ drag_get_data(self, context:Gdk.DragContext, target:Gdk.Atom, time_:int) """
        pass

    def drag_highlight(self): # real signature unknown; restored from __doc__
        """ drag_highlight(self) """
        pass

    def drag_source_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_image_targets(self) """
        pass

    def drag_source_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_text_targets(self) """
        pass

    def drag_source_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_uri_targets(self) """
        pass

    def drag_source_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_source_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_source_set(self, start_button_mask, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_source_set(self, start_button_mask:Gdk.ModifierType, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_source_set_icon_gicon(self, icon): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_gicon(self, icon:Gio.Icon) """
        pass

    def drag_source_set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_name(self, icon_name:str) """
        pass

    def drag_source_set_icon_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def drag_source_set_icon_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_stock(self, stock_id:str) """
        pass

    def drag_source_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_source_unset(self): # real signature unknown; restored from __doc__
        """ drag_source_unset(self) """
        pass

    def drag_unhighlight(self): # real signature unknown; restored from __doc__
        """ drag_unhighlight(self) """
        pass

    def draw(self, cr): # real signature unknown; restored from __doc__
        """ draw(self, cr:cairo.Context) """
        pass

    def editing_done(self): # real signature unknown; restored from __doc__
        """ editing_done(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_style(self): # real signature unknown; restored from __doc__
        """ ensure_style(self) """
        pass

    def error_bell(self): # real signature unknown; restored from __doc__
        """ error_bell(self) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event:Gdk.Event) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_style_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_style_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_child_notify(self): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible(self): # real signature unknown; restored from __doc__
        """ get_accessible(self) -> Atk.Object """
        pass

    def get_action_group(self, prefix): # real signature unknown; restored from __doc__
        """ get_action_group(self, prefix:str) -> Gio.ActionGroup or None """
        pass

    def get_activates_default(self): # real signature unknown; restored from __doc__
        """ get_activates_default(self) -> bool """
        return False

    def get_alignment(self): # real signature unknown; restored from __doc__
        """ get_alignment(self) -> float """
        return 0.0

    def get_allocated_baseline(self): # real signature unknown; restored from __doc__
        """ get_allocated_baseline(self) -> int """
        return 0

    def get_allocated_height(self): # real signature unknown; restored from __doc__
        """ get_allocated_height(self) -> int """
        return 0

    def get_allocated_size(self): # real signature unknown; restored from __doc__
        """ get_allocated_size(self) -> allocation:Gdk.Rectangle, baseline:int """
        pass

    def get_allocated_width(self): # real signature unknown; restored from __doc__
        """ get_allocated_width(self) -> int """
        return 0

    def get_allocation(self): # real signature unknown; restored from __doc__
        """ get_allocation(self) -> allocation:Gdk.Rectangle """
        pass

    def get_ancestor(self, widget_type): # real signature unknown; restored from __doc__
        """ get_ancestor(self, widget_type:GType) -> Gtk.Widget or None """
        pass

    def get_app_paintable(self): # real signature unknown; restored from __doc__
        """ get_app_paintable(self) -> bool """
        return False

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> Pango.AttrList or None """
        pass

    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> Gtk.EntryBuffer """
        pass

    def get_can_default(self): # real signature unknown; restored from __doc__
        """ get_can_default(self) -> bool """
        return False

    def get_can_focus(self): # real signature unknown; restored from __doc__
        """ get_can_focus(self) -> bool """
        return False

    def get_chars(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ get_chars(self, start_pos:int, end_pos:int) -> str """
        return ""

    def get_child_requisition(self): # real signature unknown; restored from __doc__
        """ get_child_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_child_visible(self): # real signature unknown; restored from __doc__
        """ get_child_visible(self) -> bool """
        return False

    def get_clip(self): # real signature unknown; restored from __doc__
        """ get_clip(self) -> clip:Gdk.Rectangle """
        pass

    def get_clipboard(self, selection): # real signature unknown; restored from __doc__
        """ get_clipboard(self, selection:Gdk.Atom) -> Gtk.Clipboard """
        pass

    def get_completion(self): # real signature unknown; restored from __doc__
        """ get_completion(self) -> Gtk.EntryCompletion """
        pass

    def get_composite_name(self): # real signature unknown; restored from __doc__
        """ get_composite_name(self) -> str """
        return ""

    def get_css_name(self): # real signature unknown; restored from __doc__
        """ get_css_name(self) -> str """
        return ""

    def get_current_icon_drag_source(self): # real signature unknown; restored from __doc__
        """ get_current_icon_drag_source(self) -> int """
        return 0

    def get_cursor_hadjustment(self): # real signature unknown; restored from __doc__
        """ get_cursor_hadjustment(self) -> Gtk.Adjustment or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_direction(self): # real signature unknown; restored from __doc__
        """ get_default_direction() -> Gtk.TextDirection """
        pass

    def get_default_style(self): # real signature unknown; restored from __doc__
        """ get_default_style() -> Gtk.Style """
        pass

    def get_device_enabled(self, device): # real signature unknown; restored from __doc__
        """ get_device_enabled(self, device:Gdk.Device) -> bool """
        return False

    def get_device_events(self, device): # real signature unknown; restored from __doc__
        """ get_device_events(self, device:Gdk.Device) -> Gdk.EventMask """
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_double_buffered(self): # real signature unknown; restored from __doc__
        """ get_double_buffered(self) -> bool """
        return False

    def get_editable(self): # real signature unknown; restored from __doc__
        """ get_editable(self) -> bool """
        return False

    def get_events(self): # real signature unknown; restored from __doc__
        """ get_events(self) -> int """
        return 0

    def get_focus_on_click(self): # real signature unknown; restored from __doc__
        """ get_focus_on_click(self) -> bool """
        return False

    def get_font_map(self): # real signature unknown; restored from __doc__
        """ get_font_map(self) -> Pango.FontMap or None """
        pass

    def get_font_options(self): # real signature unknown; restored from __doc__
        """ get_font_options(self) -> cairo.FontOptions or None """
        pass

    def get_frame_clock(self): # real signature unknown; restored from __doc__
        """ get_frame_clock(self) -> Gdk.FrameClock or None """
        pass

    def get_halign(self): # real signature unknown; restored from __doc__
        """ get_halign(self) -> Gtk.Align """
        pass

    def get_has_frame(self): # real signature unknown; restored from __doc__
        """ get_has_frame(self) -> bool """
        return False

    def get_has_tooltip(self): # real signature unknown; restored from __doc__
        """ get_has_tooltip(self) -> bool """
        return False

    def get_has_window(self): # real signature unknown; restored from __doc__
        """ get_has_window(self) -> bool """
        return False

    def get_hexpand(self): # real signature unknown; restored from __doc__
        """ get_hexpand(self) -> bool """
        return False

    def get_hexpand_set(self): # real signature unknown; restored from __doc__
        """ get_hexpand_set(self) -> bool """
        return False

    def get_icon_activatable(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_activatable(self, icon_pos:Gtk.EntryIconPosition) -> bool """
        return False

    def get_icon_area(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_area(self, icon_pos:Gtk.EntryIconPosition) -> icon_area:Gdk.Rectangle """
        pass

    def get_icon_at_pos(self, x, y): # real signature unknown; restored from __doc__
        """ get_icon_at_pos(self, x:int, y:int) -> int """
        return 0

    def get_icon_gicon(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_gicon(self, icon_pos:Gtk.EntryIconPosition) -> Gio.Icon or None """
        pass

    def get_icon_name(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_name(self, icon_pos:Gtk.EntryIconPosition) -> str or None """
        return ""

    def get_icon_pixbuf(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_pixbuf(self, icon_pos:Gtk.EntryIconPosition) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_icon_sensitive(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_sensitive(self, icon_pos:Gtk.EntryIconPosition) -> bool """
        return False

    def get_icon_stock(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_stock(self, icon_pos:Gtk.EntryIconPosition) -> str """
        return ""

    def get_icon_storage_type(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_storage_type(self, icon_pos:Gtk.EntryIconPosition) -> Gtk.ImageType """
        pass

    def get_icon_tooltip_markup(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_tooltip_markup(self, icon_pos:Gtk.EntryIconPosition) -> str or None """
        return ""

    def get_icon_tooltip_text(self, icon_pos): # real signature unknown; restored from __doc__
        """ get_icon_tooltip_text(self, icon_pos:Gtk.EntryIconPosition) -> str or None """
        return ""

    def get_inner_border(self): # real signature unknown; restored from __doc__
        """ get_inner_border(self) -> Gtk.Border or None """
        pass

    def get_input_hints(self): # real signature unknown; restored from __doc__
        """ get_input_hints(self) -> Gtk.InputHints """
        pass

    def get_input_purpose(self): # real signature unknown; restored from __doc__
        """ get_input_purpose(self) -> Gtk.InputPurpose """
        pass

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_invisible_char(self): # real signature unknown; restored from __doc__
        """ get_invisible_char(self) -> str """
        return ""

    def get_layout(self): # real signature unknown; restored from __doc__
        """ get_layout(self) -> Pango.Layout """
        pass

    def get_layout_offsets(self): # real signature unknown; restored from __doc__
        """ get_layout_offsets(self) -> x:int, y:int """
        pass

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> GWeather.Location or None """
        pass

    def get_mapped(self): # real signature unknown; restored from __doc__
        """ get_mapped(self) -> bool """
        return False

    def get_margin_bottom(self): # real signature unknown; restored from __doc__
        """ get_margin_bottom(self) -> int """
        return 0

    def get_margin_end(self): # real signature unknown; restored from __doc__
        """ get_margin_end(self) -> int """
        return 0

    def get_margin_left(self): # real signature unknown; restored from __doc__
        """ get_margin_left(self) -> int """
        return 0

    def get_margin_right(self): # real signature unknown; restored from __doc__
        """ get_margin_right(self) -> int """
        return 0

    def get_margin_start(self): # real signature unknown; restored from __doc__
        """ get_margin_start(self) -> int """
        return 0

    def get_margin_top(self): # real signature unknown; restored from __doc__
        """ get_margin_top(self) -> int """
        return 0

    def get_max_length(self): # real signature unknown; restored from __doc__
        """ get_max_length(self) -> int """
        return 0

    def get_max_width_chars(self): # real signature unknown; restored from __doc__
        """ get_max_width_chars(self) -> int """
        return 0

    def get_modifier_mask(self, intent): # real signature unknown; restored from __doc__
        """ get_modifier_mask(self, intent:Gdk.ModifierIntent) -> Gdk.ModifierType """
        pass

    def get_modifier_style(self): # real signature unknown; restored from __doc__
        """ get_modifier_style(self) -> Gtk.RcStyle """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_no_show_all(self): # real signature unknown; restored from __doc__
        """ get_no_show_all(self) -> bool """
        return False

    def get_opacity(self): # real signature unknown; restored from __doc__
        """ get_opacity(self) -> float """
        return 0.0

    def get_overwrite_mode(self): # real signature unknown; restored from __doc__
        """ get_overwrite_mode(self) -> bool """
        return False

    def get_pango_context(self): # real signature unknown; restored from __doc__
        """ get_pango_context(self) -> Pango.Context """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gtk.Widget or None """
        pass

    def get_parent_window(self): # real signature unknown; restored from __doc__
        """ get_parent_window(self) -> Gdk.Window or None """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.WidgetPath """
        pass

    def get_placeholder_text(self): # real signature unknown; restored from __doc__
        """ get_placeholder_text(self) -> str """
        return ""

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) -> x:int, y:int """
        pass

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> int """
        return 0

    def get_preferred_height(self): # real signature unknown; restored from __doc__
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_height_and_baseline_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def get_preferred_height_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_size(self): # real signature unknown; restored from __doc__
        """ get_preferred_size(self) -> minimum_size:Gtk.Requisition, natural_size:Gtk.Requisition """
        pass

    def get_preferred_width(self): # real signature unknown; restored from __doc__
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def get_preferred_width_for_height(self, height): # real signature unknown; restored from __doc__
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def get_progress_fraction(self): # real signature unknown; restored from __doc__
        """ get_progress_fraction(self) -> float """
        return 0.0

    def get_progress_pulse_step(self): # real signature unknown; restored from __doc__
        """ get_progress_pulse_step(self) -> float """
        return 0.0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_realized(self): # real signature unknown; restored from __doc__
        """ get_realized(self) -> bool """
        return False

    def get_receives_default(self): # real signature unknown; restored from __doc__
        """ get_receives_default(self) -> bool """
        return False

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def get_requisition(self): # real signature unknown; restored from __doc__
        """ get_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_root_window(self): # real signature unknown; restored from __doc__
        """ get_root_window(self) -> Gdk.Window """
        pass

    def get_scale_factor(self): # real signature unknown; restored from __doc__
        """ get_scale_factor(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_selection_bounds(*args, **kwargs): # reliably restored by inspect
        """ get_selection_bounds(self) -> bool, start_pos:int, end_pos:int """
        pass

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_settings(self): # real signature unknown; restored from __doc__
        """ get_settings(self) -> Gtk.Settings """
        pass

    def get_size_request(self): # real signature unknown; restored from __doc__
        """ get_size_request(self) -> width:int, height:int """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateType """
        pass

    def get_state_flags(self): # real signature unknown; restored from __doc__
        """ get_state_flags(self) -> Gtk.StateFlags """
        pass

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> Gtk.Style """
        pass

    def get_style_context(self): # real signature unknown; restored from __doc__
        """ get_style_context(self) -> Gtk.StyleContext """
        pass

    def get_support_multidevice(self): # real signature unknown; restored from __doc__
        """ get_support_multidevice(self) -> bool """
        return False

    def get_tabs(self): # real signature unknown; restored from __doc__
        """ get_tabs(self) -> Pango.TabArray or None """
        pass

    def get_template_child(self, widget_type, name): # real signature unknown; restored from __doc__
        """ get_template_child(self, widget_type:GType, name:str) -> GObject.Object """
        pass

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str """
        return ""

    def get_text_area(self): # real signature unknown; restored from __doc__
        """ get_text_area(self) -> text_area:Gdk.Rectangle """
        pass

    def get_text_length(self): # real signature unknown; restored from __doc__
        """ get_text_length(self) -> int """
        return 0

    def get_tooltip_markup(self): # real signature unknown; restored from __doc__
        """ get_tooltip_markup(self) -> str or None """
        return ""

    def get_tooltip_text(self): # real signature unknown; restored from __doc__
        """ get_tooltip_text(self) -> str or None """
        return ""

    def get_tooltip_window(self): # real signature unknown; restored from __doc__
        """ get_tooltip_window(self) -> Gtk.Window """
        pass

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> Gtk.Widget """
        pass

    def get_valign(self): # real signature unknown; restored from __doc__
        """ get_valign(self) -> Gtk.Align """
        pass

    def get_valign_with_baseline(self): # real signature unknown; restored from __doc__
        """ get_valign_with_baseline(self) -> Gtk.Align """
        pass

    def get_vexpand(self): # real signature unknown; restored from __doc__
        """ get_vexpand(self) -> bool """
        return False

    def get_vexpand_set(self): # real signature unknown; restored from __doc__
        """ get_vexpand_set(self) -> bool """
        return False

    def get_visibility(self): # real signature unknown; restored from __doc__
        """ get_visibility(self) -> bool """
        return False

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_visual(self): # real signature unknown; restored from __doc__
        """ get_visual(self) -> Gdk.Visual """
        pass

    def get_width_chars(self): # real signature unknown; restored from __doc__
        """ get_width_chars(self) -> int """
        return 0

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window or None """
        pass

    def grab_add(self): # real signature unknown; restored from __doc__
        """ grab_add(self) """
        pass

    def grab_default(self): # real signature unknown; restored from __doc__
        """ grab_default(self) """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) """
        pass

    def grab_focus_without_selecting(self): # real signature unknown; restored from __doc__
        """ grab_focus_without_selecting(self) """
        pass

    def grab_remove(self): # real signature unknown; restored from __doc__
        """ grab_remove(self) """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handle_event(self, event): # real signature unknown; restored from __doc__
        """ handle_event(self, event:Gdk.Event) -> bool """
        return False

    def has_custom_text(self): # real signature unknown; restored from __doc__
        """ has_custom_text(self) -> bool """
        return False

    def has_default(self): # real signature unknown; restored from __doc__
        """ has_default(self) -> bool """
        return False

    def has_focus(self): # real signature unknown; restored from __doc__
        """ has_focus(self) -> bool """
        return False

    def has_grab(self): # real signature unknown; restored from __doc__
        """ has_grab(self) -> bool """
        return False

    def has_rc_style(self): # real signature unknown; restored from __doc__
        """ has_rc_style(self) -> bool """
        return False

    def has_screen(self): # real signature unknown; restored from __doc__
        """ has_screen(self) -> bool """
        return False

    def has_visible_focus(self): # real signature unknown; restored from __doc__
        """ has_visible_focus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hide_on_delete(self): # real signature unknown; restored from __doc__
        """ hide_on_delete(self) -> bool """
        return False

    def im_context_filter_keypress(self, event): # real signature unknown; restored from __doc__
        """ im_context_filter_keypress(self, event:Gdk.EventKey) -> bool """
        return False

    def init_template(self): # real signature unknown; restored from __doc__
        """ init_template(self) """
        pass

    def input_shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ input_shape_combine_region(self, region:cairo.Region=None) """
        pass

    def insert_action_group(self, name, group=None): # real signature unknown; restored from __doc__
        """ insert_action_group(self, name:str, group:Gio.ActionGroup=None) """
        pass

    def insert_text(self, text, position): # reliably restored by inspect
        # no doc
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_style_property(self, pspec): # real signature unknown; restored from __doc__
        """ install_style_property(self, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def intersect(self, area): # real signature unknown; restored from __doc__
        """ intersect(self, area:Gdk.Rectangle) -> bool, intersection:Gdk.Rectangle """
        return False

    def in_destruction(self): # real signature unknown; restored from __doc__
        """ in_destruction(self) -> bool """
        return False

    def is_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ is_ancestor(self, ancestor:Gtk.Widget) -> bool """
        return False

    def is_composited(self): # real signature unknown; restored from __doc__
        """ is_composited(self) -> bool """
        return False

    def is_drawable(self): # real signature unknown; restored from __doc__
        """ is_drawable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_focus(self): # real signature unknown; restored from __doc__
        """ is_focus(self) -> bool """
        return False

    def is_sensitive(self): # real signature unknown; restored from __doc__
        """ is_sensitive(self) -> bool """
        return False

    def is_toplevel(self): # real signature unknown; restored from __doc__
        """ is_toplevel(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def keynav_failed(self, direction): # real signature unknown; restored from __doc__
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        return False

    def layout_index_to_text_index(self, layout_index): # real signature unknown; restored from __doc__
        """ layout_index_to_text_index(self, layout_index:int) -> int """
        return 0

    def list_accel_closures(self): # real signature unknown; restored from __doc__
        """ list_accel_closures(self) -> list """
        return []

    def list_action_prefixes(self): # real signature unknown; restored from __doc__
        """ list_action_prefixes(self) -> list """
        return []

    def list_mnemonic_labels(self): # real signature unknown; restored from __doc__
        """ list_mnemonic_labels(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_style_properties(self): # real signature unknown; restored from __doc__
        """ list_style_properties(self) -> list, n_properties:int """
        return []

    def map(self): # real signature unknown; restored from __doc__
        """ map(self) """
        pass

    def mnemonic_activate(self, group_cycling): # real signature unknown; restored from __doc__
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        return False

    def modify_base(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_base(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_bg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_bg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_cursor(self, primary=None, secondary=None): # real signature unknown; restored from __doc__
        """ modify_cursor(self, primary:Gdk.Color=None, secondary:Gdk.Color=None) """
        pass

    def modify_fg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_fg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ modify_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def modify_style(self, style): # real signature unknown; restored from __doc__
        """ modify_style(self, style:Gtk.RcStyle) """
        pass

    def modify_text(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_text(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def new(self, top): # real signature unknown; restored from __doc__
        """ new(top:GWeather.Location) -> Gtk.Widget """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ new_with_buffer(buffer:Gtk.EntryBuffer) -> Gtk.Widget """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_background_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_background_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_cursor(self, cursor=None, secondary_cursor=None): # real signature unknown; restored from __doc__
        """ override_cursor(self, cursor:Gdk.RGBA=None, secondary_cursor:Gdk.RGBA=None) """
        pass

    def override_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ override_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def override_symbolic_color(self, name, color=None): # real signature unknown; restored from __doc__
        """ override_symbolic_color(self, name:str, color:Gdk.RGBA=None) """
        pass

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
        pass

    def paste_clipboard(self): # real signature unknown; restored from __doc__
        """ paste_clipboard(self) """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def pop_composite_child(self): # real signature unknown; restored from __doc__
        """ pop_composite_child() """
        pass

    def progress_pulse(self): # real signature unknown; restored from __doc__
        """ progress_pulse(self) """
        pass

    def push_composite_child(self): # real signature unknown; restored from __doc__
        """ push_composite_child() """
        pass

    def queue_allocate(self): # real signature unknown; restored from __doc__
        """ queue_allocate(self) """
        pass

    def queue_compute_expand(self): # real signature unknown; restored from __doc__
        """ queue_compute_expand(self) """
        pass

    def queue_draw(self): # real signature unknown; restored from __doc__
        """ queue_draw(self) """
        pass

    def queue_draw_area(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ queue_draw_area(self, x:int, y:int, width:int, height:int) """
        pass

    def queue_draw_region(self, region): # real signature unknown; restored from __doc__
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def queue_resize(self): # real signature unknown; restored from __doc__
        """ queue_resize(self) """
        pass

    def queue_resize_no_redraw(self): # real signature unknown; restored from __doc__
        """ queue_resize_no_redraw(self) """
        pass

    def realize(self): # real signature unknown; restored from __doc__
        """ realize(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def region_intersect(self, region): # real signature unknown; restored from __doc__
        """ region_intersect(self, region:cairo.Region) -> cairo.Region """
        pass

    def register_window(self, window): # real signature unknown; restored from __doc__
        """ register_window(self, window:Gdk.Window) """
        pass

    def remove_accelerator(self, accel_group, accel_key, accel_mods): # real signature unknown; restored from __doc__
        """ remove_accelerator(self, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType) -> bool """
        return False

    def remove_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ remove_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def remove_tick_callback(self, id): # real signature unknown; restored from __doc__
        """ remove_tick_callback(self, id:int) """
        pass

    def remove_widget(self): # real signature unknown; restored from __doc__
        """ remove_widget(self) """
        pass

    def render_icon(self, stock_id, size, detail=None): # real signature unknown; restored from __doc__
        """ render_icon(self, stock_id:str, size:int, detail:str=None) -> GdkPixbuf.Pixbuf or None """
        pass

    def render_icon_pixbuf(self, stock_id, size): # real signature unknown; restored from __doc__
        """ render_icon_pixbuf(self, stock_id:str, size:int) -> GdkPixbuf.Pixbuf or None """
        pass

    def reparent(self, new_parent): # real signature unknown; restored from __doc__
        """ reparent(self, new_parent:Gtk.Widget) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_im_context(self): # real signature unknown; restored from __doc__
        """ reset_im_context(self) """
        pass

    def reset_rc_styles(self): # real signature unknown; restored from __doc__
        """ reset_rc_styles(self) """
        pass

    def reset_style(self): # real signature unknown; restored from __doc__
        """ reset_style(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def select_region(self, start_pos, end_pos): # real signature unknown; restored from __doc__
        """ select_region(self, start_pos:int, end_pos:int) """
        pass

    def send_expose(self, event): # real signature unknown; restored from __doc__
        """ send_expose(self, event:Gdk.Event) -> int """
        return 0

    def send_focus_change(self, event): # real signature unknown; restored from __doc__
        """ send_focus_change(self, event:Gdk.Event) -> bool """
        return False

    def set_accel_path(self, accel_path=None, accel_group=None): # real signature unknown; restored from __doc__
        """ set_accel_path(self, accel_path:str=None, accel_group:Gtk.AccelGroup=None) """
        pass

    def set_accessible_role(self, role): # real signature unknown; restored from __doc__
        """ set_accessible_role(self, role:Atk.Role) """
        pass

    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
        pass

    def set_activates_default(self, setting): # real signature unknown; restored from __doc__
        """ set_activates_default(self, setting:bool) """
        pass

    def set_alignment(self, xalign): # real signature unknown; restored from __doc__
        """ set_alignment(self, xalign:float) """
        pass

    def set_allocation(self, allocation): # real signature unknown; restored from __doc__
        """ set_allocation(self, allocation:Gdk.Rectangle) """
        pass

    def set_app_paintable(self, app_paintable): # real signature unknown; restored from __doc__
        """ set_app_paintable(self, app_paintable:bool) """
        pass

    def set_attributes(self, attrs): # real signature unknown; restored from __doc__
        """ set_attributes(self, attrs:Pango.AttrList) """
        pass

    def set_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ set_buffer(self, buffer:Gtk.EntryBuffer) """
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_can_default(self, can_default): # real signature unknown; restored from __doc__
        """ set_can_default(self, can_default:bool) """
        pass

    def set_can_focus(self, can_focus): # real signature unknown; restored from __doc__
        """ set_can_focus(self, can_focus:bool) """
        pass

    def set_child_visible(self, is_visible): # real signature unknown; restored from __doc__
        """ set_child_visible(self, is_visible:bool) """
        pass

    def set_city(self, city_name=None, code): # real signature unknown; restored from __doc__
        """ set_city(self, city_name:str=None, code:str) -> bool """
        return False

    def set_clip(self, clip): # real signature unknown; restored from __doc__
        """ set_clip(self, clip:Gdk.Rectangle) """
        pass

    def set_completion(self, completion=None): # real signature unknown; restored from __doc__
        """ set_completion(self, completion:Gtk.EntryCompletion=None) """
        pass

    def set_composite_name(self, name): # real signature unknown; restored from __doc__
        """ set_composite_name(self, name:str) """
        pass

    def set_connect_func(self, connect_func, connect_data=None): # real signature unknown; restored from __doc__
        """ set_connect_func(self, connect_func:Gtk.BuilderConnectFunc, connect_data=None) """
        pass

    def set_css_name(self, name): # real signature unknown; restored from __doc__
        """ set_css_name(self, name:str) """
        pass

    def set_cursor_hadjustment(self, adjustment=None): # real signature unknown; restored from __doc__
        """ set_cursor_hadjustment(self, adjustment:Gtk.Adjustment=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_default_direction(dir:Gtk.TextDirection) """
        pass

    def set_device_enabled(self, device, enabled): # real signature unknown; restored from __doc__
        """ set_device_enabled(self, device:Gdk.Device, enabled:bool) """
        pass

    def set_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ set_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def set_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_direction(self, dir:Gtk.TextDirection) """
        pass

    def set_double_buffered(self, double_buffered): # real signature unknown; restored from __doc__
        """ set_double_buffered(self, double_buffered:bool) """
        pass

    def set_editable(self, is_editable): # real signature unknown; restored from __doc__
        """ set_editable(self, is_editable:bool) """
        pass

    def set_events(self, events): # real signature unknown; restored from __doc__
        """ set_events(self, events:int) """
        pass

    def set_focus_on_click(self, focus_on_click): # real signature unknown; restored from __doc__
        """ set_focus_on_click(self, focus_on_click:bool) """
        pass

    def set_font_map(self, font_map=None): # real signature unknown; restored from __doc__
        """ set_font_map(self, font_map:Pango.FontMap=None) """
        pass

    def set_font_options(self, options=None): # real signature unknown; restored from __doc__
        """ set_font_options(self, options:cairo.FontOptions=None) """
        pass

    def set_halign(self, align): # real signature unknown; restored from __doc__
        """ set_halign(self, align:Gtk.Align) """
        pass

    def set_has_frame(self, setting): # real signature unknown; restored from __doc__
        """ set_has_frame(self, setting:bool) """
        pass

    def set_has_tooltip(self, has_tooltip): # real signature unknown; restored from __doc__
        """ set_has_tooltip(self, has_tooltip:bool) """
        pass

    def set_has_window(self, has_window): # real signature unknown; restored from __doc__
        """ set_has_window(self, has_window:bool) """
        pass

    def set_hexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_hexpand(self, expand:bool) """
        pass

    def set_hexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_hexpand_set(self, set:bool) """
        pass

    def set_icon_activatable(self, icon_pos, activatable): # real signature unknown; restored from __doc__
        """ set_icon_activatable(self, icon_pos:Gtk.EntryIconPosition, activatable:bool) """
        pass

    def set_icon_drag_source(self, icon_pos, target_list, actions): # real signature unknown; restored from __doc__
        """ set_icon_drag_source(self, icon_pos:Gtk.EntryIconPosition, target_list:Gtk.TargetList, actions:Gdk.DragAction) """
        pass

    def set_icon_from_gicon(self, icon_pos, icon=None): # real signature unknown; restored from __doc__
        """ set_icon_from_gicon(self, icon_pos:Gtk.EntryIconPosition, icon:Gio.Icon=None) """
        pass

    def set_icon_from_icon_name(self, icon_pos, icon_name=None): # real signature unknown; restored from __doc__
        """ set_icon_from_icon_name(self, icon_pos:Gtk.EntryIconPosition, icon_name:str=None) """
        pass

    def set_icon_from_pixbuf(self, icon_pos, pixbuf=None): # real signature unknown; restored from __doc__
        """ set_icon_from_pixbuf(self, icon_pos:Gtk.EntryIconPosition, pixbuf:GdkPixbuf.Pixbuf=None) """
        pass

    def set_icon_from_stock(self, icon_pos, stock_id=None): # real signature unknown; restored from __doc__
        """ set_icon_from_stock(self, icon_pos:Gtk.EntryIconPosition, stock_id:str=None) """
        pass

    def set_icon_sensitive(self, icon_pos, sensitive): # real signature unknown; restored from __doc__
        """ set_icon_sensitive(self, icon_pos:Gtk.EntryIconPosition, sensitive:bool) """
        pass

    def set_icon_tooltip_markup(self, icon_pos, tooltip=None): # real signature unknown; restored from __doc__
        """ set_icon_tooltip_markup(self, icon_pos:Gtk.EntryIconPosition, tooltip:str=None) """
        pass

    def set_icon_tooltip_text(self, icon_pos, tooltip=None): # real signature unknown; restored from __doc__
        """ set_icon_tooltip_text(self, icon_pos:Gtk.EntryIconPosition, tooltip:str=None) """
        pass

    def set_inner_border(self, border=None): # real signature unknown; restored from __doc__
        """ set_inner_border(self, border:Gtk.Border=None) """
        pass

    def set_input_hints(self, hints): # real signature unknown; restored from __doc__
        """ set_input_hints(self, hints:Gtk.InputHints) """
        pass

    def set_input_purpose(self, purpose): # real signature unknown; restored from __doc__
        """ set_input_purpose(self, purpose:Gtk.InputPurpose) """
        pass

    def set_invisible_char(self, ch): # real signature unknown; restored from __doc__
        """ set_invisible_char(self, ch:str) """
        pass

    def set_location(self, loc=None): # real signature unknown; restored from __doc__
        """ set_location(self, loc:GWeather.Location=None) """
        pass

    def set_mapped(self, mapped): # real signature unknown; restored from __doc__
        """ set_mapped(self, mapped:bool) """
        pass

    def set_margin_bottom(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_bottom(self, margin:int) """
        pass

    def set_margin_end(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_end(self, margin:int) """
        pass

    def set_margin_left(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_left(self, margin:int) """
        pass

    def set_margin_right(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_right(self, margin:int) """
        pass

    def set_margin_start(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_start(self, margin:int) """
        pass

    def set_margin_top(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_top(self, margin:int) """
        pass

    def set_max_length(self, max): # real signature unknown; restored from __doc__
        """ set_max_length(self, max:int) """
        pass

    def set_max_width_chars(self, n_chars): # real signature unknown; restored from __doc__
        """ set_max_width_chars(self, n_chars:int) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_no_show_all(self, no_show_all): # real signature unknown; restored from __doc__
        """ set_no_show_all(self, no_show_all:bool) """
        pass

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:float) """
        pass

    def set_overwrite_mode(self, overwrite): # real signature unknown; restored from __doc__
        """ set_overwrite_mode(self, overwrite:bool) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gtk.Widget) """
        pass

    def set_parent_window(self, parent_window): # real signature unknown; restored from __doc__
        """ set_parent_window(self, parent_window:Gdk.Window) """
        pass

    def set_placeholder_text(self, text=None): # real signature unknown; restored from __doc__
        """ set_placeholder_text(self, text:str=None) """
        pass

    def set_position(self, position): # real signature unknown; restored from __doc__
        """ set_position(self, position:int) """
        pass

    def set_progress_fraction(self, fraction): # real signature unknown; restored from __doc__
        """ set_progress_fraction(self, fraction:float) """
        pass

    def set_progress_pulse_step(self, fraction): # real signature unknown; restored from __doc__
        """ set_progress_pulse_step(self, fraction:float) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_realized(self, realized): # real signature unknown; restored from __doc__
        """ set_realized(self, realized:bool) """
        pass

    def set_receives_default(self, receives_default): # real signature unknown; restored from __doc__
        """ set_receives_default(self, receives_default:bool) """
        pass

    def set_redraw_on_allocate(self, redraw_on_allocate): # real signature unknown; restored from __doc__
        """ set_redraw_on_allocate(self, redraw_on_allocate:bool) """
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_size_request(self, width, height): # real signature unknown; restored from __doc__
        """ set_size_request(self, width:int, height:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gtk.StateType) """
        pass

    def set_state_flags(self, flags, clear): # real signature unknown; restored from __doc__
        """ set_state_flags(self, flags:Gtk.StateFlags, clear:bool) """
        pass

    def set_style(self, style=None): # real signature unknown; restored from __doc__
        """ set_style(self, style:Gtk.Style=None) """
        pass

    def set_support_multidevice(self, support_multidevice): # real signature unknown; restored from __doc__
        """ set_support_multidevice(self, support_multidevice:bool) """
        pass

    def set_tabs(self, tabs): # real signature unknown; restored from __doc__
        """ set_tabs(self, tabs:Pango.TabArray) """
        pass

    def set_template(self, template_bytes): # real signature unknown; restored from __doc__
        """ set_template(self, template_bytes:GLib.Bytes) """
        pass

    def set_template_from_resource(self, resource_name): # real signature unknown; restored from __doc__
        """ set_template_from_resource(self, resource_name:str) """
        pass

    def set_text(self, text): # real signature unknown; restored from __doc__
        """ set_text(self, text:str) """
        pass

    def set_tooltip_markup(self, markup=None): # real signature unknown; restored from __doc__
        """ set_tooltip_markup(self, markup:str=None) """
        pass

    def set_tooltip_text(self, text=None): # real signature unknown; restored from __doc__
        """ set_tooltip_text(self, text:str=None) """
        pass

    def set_tooltip_window(self, custom_window=None): # real signature unknown; restored from __doc__
        """ set_tooltip_window(self, custom_window:Gtk.Window=None) """
        pass

    def set_valign(self, align): # real signature unknown; restored from __doc__
        """ set_valign(self, align:Gtk.Align) """
        pass

    def set_vexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_vexpand(self, expand:bool) """
        pass

    def set_vexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_vexpand_set(self, set:bool) """
        pass

    def set_visibility(self, visible): # real signature unknown; restored from __doc__
        """ set_visibility(self, visible:bool) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def set_visual(self, visual=None): # real signature unknown; restored from __doc__
        """ set_visual(self, visual:Gdk.Visual=None) """
        pass

    def set_width_chars(self, n_chars): # real signature unknown; restored from __doc__
        """ set_width_chars(self, n_chars:int) """
        pass

    def set_window(self, window): # real signature unknown; restored from __doc__
        """ set_window(self, window:Gdk.Window) """
        pass

    def shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ shape_combine_region(self, region:cairo.Region=None) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def show_all(self): # real signature unknown; restored from __doc__
        """ show_all(self) """
        pass

    def show_now(self): # real signature unknown; restored from __doc__
        """ show_now(self) """
        pass

    def size_allocate(self, allocation): # real signature unknown; restored from __doc__
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def size_allocate_with_baseline(self, allocation, baseline): # real signature unknown; restored from __doc__
        """ size_allocate_with_baseline(self, allocation:Gdk.Rectangle, baseline:int) """
        pass

    def size_request(self): # real signature unknown; restored from __doc__
        """ size_request(self) -> requisition:Gtk.Requisition """
        pass

    def start_editing(self, event=None): # real signature unknown; restored from __doc__
        """ start_editing(self, event:Gdk.Event=None) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def style_attach(self): # real signature unknown; restored from __doc__
        """ style_attach(self) """
        pass

    def style_get_property(self, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def text_index_to_layout_index(self, text_index): # real signature unknown; restored from __doc__
        """ text_index_to_layout_index(self, text_index:int) -> int """
        return 0

    def thaw_child_notify(self): # real signature unknown; restored from __doc__
        """ thaw_child_notify(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def translate_coordinates(*args, **kwargs): # reliably restored by inspect
        """ translate_coordinates(self, dest_widget:Gtk.Widget, src_x:int, src_y:int) -> bool, dest_x:int, dest_y:int """
        pass

    def trigger_tooltip_query(self): # real signature unknown; restored from __doc__
        """ trigger_tooltip_query(self) """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unrealize(self): # real signature unknown; restored from __doc__
        """ unrealize(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_window(self, window): # real signature unknown; restored from __doc__
        """ unregister_window(self, window:Gdk.Window) """
        pass

    def unset_invisible_char(self): # real signature unknown; restored from __doc__
        """ unset_invisible_char(self) """
        pass

    def unset_state_flags(self, flags): # real signature unknown; restored from __doc__
        """ unset_state_flags(self, flags:Gtk.StateFlags) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, **properties): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f73c7bd20a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(LocationEntry), '__module__': 'gi.repository.GWeather', '__gtype__': <GType GWeatherLocationEntry (94766762990160)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_location': gi.FunctionInfo(get_location), 'has_custom_text': gi.FunctionInfo(has_custom_text), 'set_city': gi.FunctionInfo(set_city), 'set_location': gi.FunctionInfo(set_location), 'parent': <property object at 0x7f73c7b84810>, 'priv': <property object at 0x7f73c7b84950>})"
    __gdoc__ = 'Object GWeatherLocationEntry\n\nProperties from GWeatherLocationEntry:\n  top -> GWeatherLocation: Top Location\n    The GWeatherLocation whose children will be used to fill in the entry\n  show-named-timezones -> gboolean: Show named timezones\n    Whether UTC and other named timezones are shown in the list of locations\n  location -> GWeatherLocation: Location\n    The selected GWeatherLocation\n\nSignals from GtkEditable:\n  changed ()\n  insert-text (gchararray, gint, gpointer)\n  delete-text (gint, gint)\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nSignals from GtkSearchEntry:\n  search-changed ()\n  next-match ()\n  previous-match ()\n  stop-search ()\n\nSignals from GtkEditable:\n  changed ()\n  insert-text (gchararray, gint, gpointer)\n  delete-text (gint, gint)\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nSignals from GtkEntry:\n  activate ()\n  populate-popup (GtkWidget)\n  move-cursor (GtkMovementStep, gint, gboolean)\n  insert-at-cursor (gchararray)\n  delete-from-cursor (GtkDeleteType, gint)\n  backspace ()\n  cut-clipboard ()\n  copy-clipboard ()\n  paste-clipboard ()\n  toggle-overwrite ()\n  icon-press (GtkEntryIconPosition, GdkEvent)\n  icon-release (GtkEntryIconPosition, GdkEvent)\n  preedit-changed (gchararray)\n  insert-emoji ()\n\nProperties from GtkEntry:\n  buffer -> GtkEntryBuffer: Text Buffer\n    Text buffer object which actually stores entry text\n  cursor-position -> gint: Cursor Position\n    The current position of the insertion cursor in chars\n  selection-bound -> gint: Selection Bound\n    The position of the opposite end of the selection from the cursor in chars\n  editable -> gboolean: Editable\n    Whether the entry contents can be edited\n  max-length -> gint: Maximum length\n    Maximum number of characters for this entry. Zero if no maximum\n  visibility -> gboolean: Visibility\n    FALSE displays the "invisible char" instead of the actual text (password mode)\n  has-frame -> gboolean: Has Frame\n    FALSE removes outside bevel from entry\n  inner-border -> GtkBorder: Inner Border\n    Border between text and frame. Overrides the inner-border style property\n  invisible-char -> guint: Invisible character\n    The character to use when masking entry contents (in "password mode")\n  activates-default -> gboolean: Activates default\n    Whether to activate the default widget (such as the default button in a dialog) when Enter is pressed\n  width-chars -> gint: Width in chars\n    Number of characters to leave space for in the entry\n  max-width-chars -> gint: Maximum width in characters\n    The desired maximum width of the entry, in characters\n  scroll-offset -> gint: Scroll offset\n    Number of pixels of the entry scrolled off the screen to the left\n  text -> gchararray: Text\n    The contents of the entry\n  xalign -> gfloat: X align\n    The horizontal alignment, from 0 (left) to 1 (right). Reversed for RTL layouts.\n  truncate-multiline -> gboolean: Truncate multiline\n    Whether to truncate multiline pastes to one line.\n  shadow-type -> GtkShadowType: Shadow type\n    Which kind of shadow to draw around the entry when has-frame is set\n  overwrite-mode -> gboolean: Overwrite mode\n    Whether new text overwrites existing text\n  text-length -> guint: Text length\n    Length of the text currently in the entry\n  invisible-char-set -> gboolean: Invisible character set\n    Whether the invisible character has been set\n  caps-lock-warning -> gboolean: Caps Lock warning\n    Whether password entries will show a warning when Caps Lock is on\n  progress-fraction -> gdouble: Progress Fraction\n    The current fraction of the task that\'s been completed\n  progress-pulse-step -> gdouble: Progress Pulse Step\n    The fraction of total entry width to move the progress bouncing block for each call to gtk_entry_progress_pulse()\n  primary-icon-pixbuf -> GdkPixbuf: Primary pixbuf\n    Primary pixbuf for the entry\n  secondary-icon-pixbuf -> GdkPixbuf: Secondary pixbuf\n    Secondary pixbuf for the entry\n  primary-icon-stock -> gchararray: Primary stock ID\n    Stock ID for primary icon\n  secondary-icon-stock -> gchararray: Secondary stock ID\n    Stock ID for secondary icon\n  primary-icon-name -> gchararray: Primary icon name\n    Icon name for primary icon\n  secondary-icon-name -> gchararray: Secondary icon name\n    Icon name for secondary icon\n  primary-icon-gicon -> GIcon: Primary GIcon\n    GIcon for primary icon\n  secondary-icon-gicon -> GIcon: Secondary GIcon\n    GIcon for secondary icon\n  primary-icon-storage-type -> GtkImageType: Primary storage type\n    The representation being used for primary icon\n  secondary-icon-storage-type -> GtkImageType: Secondary storage type\n    The representation being used for secondary icon\n  primary-icon-activatable -> gboolean: Primary icon activatable\n    Whether the primary icon is activatable\n  secondary-icon-activatable -> gboolean: Secondary icon activatable\n    Whether the secondary icon is activatable\n  primary-icon-sensitive -> gboolean: Primary icon sensitive\n    Whether the primary icon is sensitive\n  secondary-icon-sensitive -> gboolean: Secondary icon sensitive\n    Whether the secondary icon is sensitive\n  primary-icon-tooltip-text -> gchararray: Primary icon tooltip text\n    The contents of the tooltip on the primary icon\n  secondary-icon-tooltip-text -> gchararray: Secondary icon tooltip text\n    The contents of the tooltip on the secondary icon\n  primary-icon-tooltip-markup -> gchararray: Primary icon tooltip markup\n    The contents of the tooltip on the primary icon\n  secondary-icon-tooltip-markup -> gchararray: Secondary icon tooltip markup\n    The contents of the tooltip on the secondary icon\n  im-module -> gchararray: IM module\n    Which IM module should be used\n  placeholder-text -> gchararray: Placeholder text\n    Show text in the entry when it\'s empty and unfocused\n  completion -> GtkEntryCompletion: Completion\n    The auxiliary completion object\n  input-purpose -> GtkInputPurpose: Purpose\n    Purpose of the text field\n  input-hints -> GtkInputHints: hints\n    Hints for the text field behaviour\n  attributes -> PangoAttrList: Attributes\n    A list of style attributes to apply to the text of the label\n  populate-all -> gboolean: Populate all\n    Whether to emit ::populate-popup for touch popups\n  tabs -> PangoTabArray: Tabs\n    A list of tabstop locations to apply to the text of the entry\n  show-emoji-icon -> gboolean: Emoji icon\n    Whether to show an icon for Emoji\n  enable-emoji-completion -> gboolean: Enable Emoji completion\n    Whether to suggest Emoji replacements\n\nSignals from GtkEditable:\n  changed ()\n  insert-text (gchararray, gint, gpointer)\n  delete-text (gint, gint)\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nSignals from GtkWidget:\n  composited-changed ()\n  destroy ()\n  show ()\n  hide ()\n  map ()\n  unmap ()\n  realize ()\n  unrealize ()\n  size-allocate (GdkRectangle)\n  state-changed (GtkStateType)\n  state-flags-changed (GtkStateFlags)\n  parent-set (GtkWidget)\n  hierarchy-changed (GtkWidget)\n  style-set (GtkStyle)\n  style-updated ()\n  direction-changed (GtkTextDirection)\n  grab-notify (gboolean)\n  child-notify (GParam)\n  draw (CairoContext) -> gboolean\n  mnemonic-activate (gboolean) -> gboolean\n  grab-focus ()\n  focus (GtkDirectionType) -> gboolean\n  move-focus (GtkDirectionType)\n  keynav-failed (GtkDirectionType) -> gboolean\n  event (GdkEvent) -> gboolean\n  event-after (GdkEvent)\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  touch-event (GdkEvent) -> gboolean\n  scroll-event (GdkEvent) -> gboolean\n  motion-notify-event (GdkEvent) -> gboolean\n  delete-event (GdkEvent) -> gboolean\n  destroy-event (GdkEvent) -> gboolean\n  key-press-event (GdkEvent) -> gboolean\n  key-release-event (GdkEvent) -> gboolean\n  enter-notify-event (GdkEvent) -> gboolean\n  leave-notify-event (GdkEvent) -> gboolean\n  configure-event (GdkEvent) -> gboolean\n  focus-in-event (GdkEvent) -> gboolean\n  focus-out-event (GdkEvent) -> gboolean\n  map-event (GdkEvent) -> gboolean\n  unmap-event (GdkEvent) -> gboolean\n  property-notify-event (GdkEvent) -> gboolean\n  selection-clear-event (GdkEvent) -> gboolean\n  selection-request-event (GdkEvent) -> gboolean\n  selection-notify-event (GdkEvent) -> gboolean\n  selection-received (GtkSelectionData, guint)\n  selection-get (GtkSelectionData, guint, guint)\n  proximity-in-event (GdkEvent) -> gboolean\n  proximity-out-event (GdkEvent) -> gboolean\n  drag-leave (GdkDragContext, guint)\n  drag-begin (GdkDragContext)\n  drag-end (GdkDragContext)\n  drag-data-delete (GdkDragContext)\n  drag-failed (GdkDragContext, GtkDragResult) -> gboolean\n  drag-motion (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-drop (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)\n  drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)\n  visibility-notify-event (GdkEvent) -> gboolean\n  window-state-event (GdkEvent) -> gboolean\n  damage-event (GdkEvent) -> gboolean\n  grab-broken-event (GdkEvent) -> gboolean\n  query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean\n  popup-menu () -> gboolean\n  show-help (GtkWidgetHelpType) -> gboolean\n  accel-closures-changed ()\n  screen-changed (GdkScreen)\n  can-activate-accel (guint) -> gboolean\n\nProperties from GtkWidget:\n  name -> gchararray: Widget name\n    The name of the widget\n  parent -> GtkContainer: Parent widget\n    The parent widget of this widget. Must be a Container widget\n  width-request -> gint: Width request\n    Override for width request of the widget, or -1 if natural request should be used\n  height-request -> gint: Height request\n    Override for height request of the widget, or -1 if natural request should be used\n  visible -> gboolean: Visible\n    Whether the widget is visible\n  sensitive -> gboolean: Sensitive\n    Whether the widget responds to input\n  app-paintable -> gboolean: Application paintable\n    Whether the application will paint directly on the widget\n  can-focus -> gboolean: Can focus\n    Whether the widget can accept the input focus\n  has-focus -> gboolean: Has focus\n    Whether the widget has the input focus\n  is-focus -> gboolean: Is focus\n    Whether the widget is the focus widget within the toplevel\n  focus-on-click -> gboolean: Focus on click\n    Whether the widget should grab focus when it is clicked with the mouse\n  can-default -> gboolean: Can default\n    Whether the widget can be the default widget\n  has-default -> gboolean: Has default\n    Whether the widget is the default widget\n  receives-default -> gboolean: Receives default\n    If TRUE, the widget will receive the default action when it is focused\n  composite-child -> gboolean: Composite child\n    Whether the widget is part of a composite widget\n  style -> GtkStyle: Style\n    The style of the widget, which contains information about how it will look (colors etc)\n  events -> GdkEventMask: Events\n    The event mask that decides what kind of GdkEvents this widget gets\n  no-show-all -> gboolean: No show all\n    Whether gtk_widget_show_all() should not affect this widget\n  has-tooltip -> gboolean: Has tooltip\n    Whether this widget has a tooltip\n  tooltip-markup -> gchararray: Tooltip markup\n    The contents of the tooltip for this widget\n  tooltip-text -> gchararray: Tooltip Text\n    The contents of the tooltip for this widget\n  window -> GdkWindow: Window\n    The widget\'s window if it is realized\n  opacity -> gdouble: Opacity for Widget\n    The opacity of the widget, from 0 to 1\n  double-buffered -> gboolean: Double Buffered\n    Whether the widget is double buffered\n  halign -> GtkAlign: Horizontal Alignment\n    How to position in extra horizontal space\n  valign -> GtkAlign: Vertical Alignment\n    How to position in extra vertical space\n  margin-left -> gint: Margin on Left\n    Pixels of extra space on the left side\n  margin-right -> gint: Margin on Right\n    Pixels of extra space on the right side\n  margin-start -> gint: Margin on Start\n    Pixels of extra space on the start\n  margin-end -> gint: Margin on End\n    Pixels of extra space on the end\n  margin-top -> gint: Margin on Top\n    Pixels of extra space on the top side\n  margin-bottom -> gint: Margin on Bottom\n    Pixels of extra space on the bottom side\n  margin -> gint: All Margins\n    Pixels of extra space on all four sides\n  hexpand -> gboolean: Horizontal Expand\n    Whether widget wants more horizontal space\n  vexpand -> gboolean: Vertical Expand\n    Whether widget wants more vertical space\n  hexpand-set -> gboolean: Horizontal Expand Set\n    Whether to use the hexpand property\n  vexpand-set -> gboolean: Vertical Expand Set\n    Whether to use the vexpand property\n  expand -> gboolean: Expand Both\n    Whether widget wants to expand in both directions\n  scale-factor -> gint: Scale factor\n    The scaling factor of the window\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GWeatherLocationEntry (94766762990160)>'
    __info__ = ObjectInfo(LocationEntry)


class LocationEntryClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        LocationEntryClass()
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(LocationEntryClass), '__module__': 'gi.repository.GWeather', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'LocationEntryClass' objects>, '__weakref__': <attribute '__weakref__' of 'LocationEntryClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f73c7b84ae0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(LocationEntryClass)


class LocationEntryPrivate(__gi.Struct):
    # no doc
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(LocationEntryPrivate), '__module__': 'gi.repository.GWeather', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'LocationEntryPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'LocationEntryPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(LocationEntryPrivate)


class LocationLevel(__gobject.GEnum):
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

    def to_string(self, level): # real signature unknown; restored from __doc__
        """ to_string(level:GWeather.LocationLevel) -> str """
        return ""

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


    ADM1 = 3
    CITY = 4
    COUNTRY = 2
    DETACHED = 6
    NAMED_TIMEZONE = 7
    REGION = 1
    WEATHER_STATION = 5
    WORLD = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'LocationLevel' objects>, '__doc__': None, '__gtype__': <GType GWeatherLocationLevel (94766763397904)>, '__enum_values__': {0: <enum GWEATHER_LOCATION_WORLD of type GWeather.LocationLevel>, 1: <enum GWEATHER_LOCATION_REGION of type GWeather.LocationLevel>, 2: <enum GWEATHER_LOCATION_COUNTRY of type GWeather.LocationLevel>, 3: <enum GWEATHER_LOCATION_ADM1 of type GWeather.LocationLevel>, 4: <enum GWEATHER_LOCATION_CITY of type GWeather.LocationLevel>, 5: <enum GWEATHER_LOCATION_WEATHER_STATION of type GWeather.LocationLevel>, 6: <enum GWEATHER_LOCATION_DETACHED of type GWeather.LocationLevel>, 7: <enum GWEATHER_LOCATION_NAMED_TIMEZONE of type GWeather.LocationLevel>}, '__info__': gi.EnumInfo(LocationLevel), 'WORLD': <enum GWEATHER_LOCATION_WORLD of type GWeather.LocationLevel>, 'REGION': <enum GWEATHER_LOCATION_REGION of type GWeather.LocationLevel>, 'COUNTRY': <enum GWEATHER_LOCATION_COUNTRY of type GWeather.LocationLevel>, 'ADM1': <enum GWEATHER_LOCATION_ADM1 of type GWeather.LocationLevel>, 'CITY': <enum GWEATHER_LOCATION_CITY of type GWeather.LocationLevel>, 'WEATHER_STATION': <enum GWEATHER_LOCATION_WEATHER_STATION of type GWeather.LocationLevel>, 'DETACHED': <enum GWEATHER_LOCATION_DETACHED of type GWeather.LocationLevel>, 'NAMED_TIMEZONE': <enum GWEATHER_LOCATION_NAMED_TIMEZONE of type GWeather.LocationLevel>, 'to_string': gi.FunctionInfo(to_string)})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherLocationLevel (94766763397904)>'
    __info__ = gi.EnumInfo(LocationLevel)


class PressureUnit(__gobject.GEnum):
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


    ATM = 7
    DEFAULT = 1
    HPA = 3
    INCH_HG = 6
    INVALID = 0
    KPA = 2
    MB = 4
    MM_HG = 5
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'PressureUnit' objects>, '__doc__': None, '__gtype__': <GType GWeatherPressureUnit (94766763280768)>, '__enum_values__': {0: <enum GWEATHER_PRESSURE_UNIT_INVALID of type GWeather.PressureUnit>, 1: <enum GWEATHER_PRESSURE_UNIT_DEFAULT of type GWeather.PressureUnit>, 2: <enum GWEATHER_PRESSURE_UNIT_KPA of type GWeather.PressureUnit>, 3: <enum GWEATHER_PRESSURE_UNIT_HPA of type GWeather.PressureUnit>, 4: <enum GWEATHER_PRESSURE_UNIT_MB of type GWeather.PressureUnit>, 5: <enum GWEATHER_PRESSURE_UNIT_MM_HG of type GWeather.PressureUnit>, 6: <enum GWEATHER_PRESSURE_UNIT_INCH_HG of type GWeather.PressureUnit>, 7: <enum GWEATHER_PRESSURE_UNIT_ATM of type GWeather.PressureUnit>}, '__info__': gi.EnumInfo(PressureUnit), 'INVALID': <enum GWEATHER_PRESSURE_UNIT_INVALID of type GWeather.PressureUnit>, 'DEFAULT': <enum GWEATHER_PRESSURE_UNIT_DEFAULT of type GWeather.PressureUnit>, 'KPA': <enum GWEATHER_PRESSURE_UNIT_KPA of type GWeather.PressureUnit>, 'HPA': <enum GWEATHER_PRESSURE_UNIT_HPA of type GWeather.PressureUnit>, 'MB': <enum GWEATHER_PRESSURE_UNIT_MB of type GWeather.PressureUnit>, 'MM_HG': <enum GWEATHER_PRESSURE_UNIT_MM_HG of type GWeather.PressureUnit>, 'INCH_HG': <enum GWEATHER_PRESSURE_UNIT_INCH_HG of type GWeather.PressureUnit>, 'ATM': <enum GWEATHER_PRESSURE_UNIT_ATM of type GWeather.PressureUnit>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherPressureUnit (94766763280768)>'
    __info__ = gi.EnumInfo(PressureUnit)


class Provider(__gobject.GFlags):
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


    ALL = 31
    IWIN = 4
    METAR = 1
    NONE = 0
    OWM = 32
    YAHOO = 8
    YR_NO = 16
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'Provider' objects>, '__doc__': None, '__gtype__': <GType GWeatherProvider (94766763436384)>, '__flags_values__': {0: <flags 0 of type GWeather.Provider>, 1: <flags GWEATHER_PROVIDER_METAR of type GWeather.Provider>, 4: <flags GWEATHER_PROVIDER_IWIN of type GWeather.Provider>, 8: <flags GWEATHER_PROVIDER_YAHOO of type GWeather.Provider>, 16: <flags GWEATHER_PROVIDER_YR_NO of type GWeather.Provider>, 32: <flags GWEATHER_PROVIDER_OWM of type GWeather.Provider>, 31: <flags GWEATHER_PROVIDER_METAR | GWEATHER_PROVIDER_IWIN | GWEATHER_PROVIDER_YAHOO | GWEATHER_PROVIDER_YR_NO | GWEATHER_PROVIDER_ALL of type GWeather.Provider>}, '__info__': gi.EnumInfo(Provider), 'NONE': <flags 0 of type GWeather.Provider>, 'METAR': <flags GWEATHER_PROVIDER_METAR of type GWeather.Provider>, 'IWIN': <flags GWEATHER_PROVIDER_IWIN of type GWeather.Provider>, 'YAHOO': <flags GWEATHER_PROVIDER_YAHOO of type GWeather.Provider>, 'YR_NO': <flags GWEATHER_PROVIDER_YR_NO of type GWeather.Provider>, 'OWM': <flags GWEATHER_PROVIDER_OWM of type GWeather.Provider>, 'ALL': <flags GWEATHER_PROVIDER_METAR | GWEATHER_PROVIDER_IWIN | GWEATHER_PROVIDER_YAHOO | GWEATHER_PROVIDER_YR_NO | GWEATHER_PROVIDER_ALL of type GWeather.Provider>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        4: 4,
        8: 8,
        16: 16,
        31: 31,
        32: 32,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherProvider (94766763436384)>'
    __info__ = gi.EnumInfo(Provider)


class Sky(__gobject.GEnum):
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

    def to_string(self, sky): # real signature unknown; restored from __doc__
        """ to_string(sky:GWeather.Sky) -> str """
        return ""

    def to_string_full(self, sky, options): # real signature unknown; restored from __doc__
        """ to_string_full(sky:GWeather.Sky, options:GWeather.FormatOptions) -> str """
        return ""

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


    BROKEN = 1
    CLEAR = 0
    FEW = 3
    INVALID = -1
    LAST = 5
    OVERCAST = 4
    SCATTERED = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'Sky' objects>, '__doc__': None, '__gtype__': <GType GWeatherSky (94766763395760)>, '__enum_values__': {-1: <enum GWEATHER_SKY_INVALID of type GWeather.Sky>, 0: <enum GWEATHER_SKY_CLEAR of type GWeather.Sky>, 1: <enum GWEATHER_SKY_BROKEN of type GWeather.Sky>, 2: <enum GWEATHER_SKY_SCATTERED of type GWeather.Sky>, 3: <enum GWEATHER_SKY_FEW of type GWeather.Sky>, 4: <enum GWEATHER_SKY_OVERCAST of type GWeather.Sky>, 5: <enum GWEATHER_SKY_LAST of type GWeather.Sky>}, '__info__': gi.EnumInfo(Sky), 'INVALID': <enum GWEATHER_SKY_INVALID of type GWeather.Sky>, 'CLEAR': <enum GWEATHER_SKY_CLEAR of type GWeather.Sky>, 'BROKEN': <enum GWEATHER_SKY_BROKEN of type GWeather.Sky>, 'SCATTERED': <enum GWEATHER_SKY_SCATTERED of type GWeather.Sky>, 'FEW': <enum GWEATHER_SKY_FEW of type GWeather.Sky>, 'OVERCAST': <enum GWEATHER_SKY_OVERCAST of type GWeather.Sky>, 'LAST': <enum GWEATHER_SKY_LAST of type GWeather.Sky>, 'to_string': gi.FunctionInfo(to_string), 'to_string_full': gi.FunctionInfo(to_string_full)})"
    __enum_values__ = {
        -1: -1,
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherSky (94766763395760)>'
    __info__ = gi.EnumInfo(Sky)


class SpeedUnit(__gobject.GEnum):
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


    BFT = 6
    DEFAULT = 1
    INVALID = 0
    KNOTS = 5
    KPH = 3
    MPH = 4
    MS = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'SpeedUnit' objects>, '__doc__': None, '__gtype__': <GType GWeatherSpeedUnit (94766763395968)>, '__enum_values__': {0: <enum GWEATHER_SPEED_UNIT_INVALID of type GWeather.SpeedUnit>, 1: <enum GWEATHER_SPEED_UNIT_DEFAULT of type GWeather.SpeedUnit>, 2: <enum GWEATHER_SPEED_UNIT_MS of type GWeather.SpeedUnit>, 3: <enum GWEATHER_SPEED_UNIT_KPH of type GWeather.SpeedUnit>, 4: <enum GWEATHER_SPEED_UNIT_MPH of type GWeather.SpeedUnit>, 5: <enum GWEATHER_SPEED_UNIT_KNOTS of type GWeather.SpeedUnit>, 6: <enum GWEATHER_SPEED_UNIT_BFT of type GWeather.SpeedUnit>}, '__info__': gi.EnumInfo(SpeedUnit), 'INVALID': <enum GWEATHER_SPEED_UNIT_INVALID of type GWeather.SpeedUnit>, 'DEFAULT': <enum GWEATHER_SPEED_UNIT_DEFAULT of type GWeather.SpeedUnit>, 'MS': <enum GWEATHER_SPEED_UNIT_MS of type GWeather.SpeedUnit>, 'KPH': <enum GWEATHER_SPEED_UNIT_KPH of type GWeather.SpeedUnit>, 'MPH': <enum GWEATHER_SPEED_UNIT_MPH of type GWeather.SpeedUnit>, 'KNOTS': <enum GWEATHER_SPEED_UNIT_KNOTS of type GWeather.SpeedUnit>, 'BFT': <enum GWEATHER_SPEED_UNIT_BFT of type GWeather.SpeedUnit>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherSpeedUnit (94766763395968)>'
    __info__ = gi.EnumInfo(SpeedUnit)


class TemperatureUnit(__gobject.GEnum):
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

    def to_real(self, unit): # real signature unknown; restored from __doc__
        """ to_real(unit:GWeather.TemperatureUnit) -> GWeather.TemperatureUnit """
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


    CENTIGRADE = 3
    DEFAULT = 1
    FAHRENHEIT = 4
    INVALID = 0
    KELVIN = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'TemperatureUnit' objects>, '__doc__': None, '__gtype__': <GType GWeatherTemperatureUnit (94766763438656)>, '__enum_values__': {0: <enum GWEATHER_TEMP_UNIT_INVALID of type GWeather.TemperatureUnit>, 1: <enum GWEATHER_TEMP_UNIT_DEFAULT of type GWeather.TemperatureUnit>, 2: <enum GWEATHER_TEMP_UNIT_KELVIN of type GWeather.TemperatureUnit>, 3: <enum GWEATHER_TEMP_UNIT_CENTIGRADE of type GWeather.TemperatureUnit>, 4: <enum GWEATHER_TEMP_UNIT_FAHRENHEIT of type GWeather.TemperatureUnit>}, '__info__': gi.EnumInfo(TemperatureUnit), 'INVALID': <enum GWEATHER_TEMP_UNIT_INVALID of type GWeather.TemperatureUnit>, 'DEFAULT': <enum GWEATHER_TEMP_UNIT_DEFAULT of type GWeather.TemperatureUnit>, 'KELVIN': <enum GWEATHER_TEMP_UNIT_KELVIN of type GWeather.TemperatureUnit>, 'CENTIGRADE': <enum GWEATHER_TEMP_UNIT_CENTIGRADE of type GWeather.TemperatureUnit>, 'FAHRENHEIT': <enum GWEATHER_TEMP_UNIT_FAHRENHEIT of type GWeather.TemperatureUnit>, 'to_real': gi.FunctionInfo(to_real)})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is '<GType GWeatherTemperatureUnit (94766763438656)>'
    __info__ = gi.EnumInfo(TemperatureUnit)


class Timezone(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_by_tzid(self, tzid): # real signature unknown; restored from __doc__
        """ get_by_tzid(tzid:str) -> GWeather.Timezone """
        pass

    def get_dst_offset(self): # real signature unknown; restored from __doc__
        """ get_dst_offset(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_offset(self): # real signature unknown; restored from __doc__
        """ get_offset(self) -> int """
        return 0

    def get_tzid(self): # real signature unknown; restored from __doc__
        """ get_tzid(self) -> str """
        return ""

    def get_utc(self): # real signature unknown; restored from __doc__
        """ get_utc() -> GWeather.Timezone """
        pass

    def has_dst(self): # real signature unknown; restored from __doc__
        """ has_dst(self) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GWeather.Timezone """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Timezone), '__module__': 'gi.repository.GWeather', '__gtype__': <GType GWeatherTimezone (94766763410192)>, '__dict__': <attribute '__dict__' of 'Timezone' objects>, '__weakref__': <attribute '__weakref__' of 'Timezone' objects>, '__doc__': None, 'get_dst_offset': gi.FunctionInfo(get_dst_offset), 'get_name': gi.FunctionInfo(get_name), 'get_offset': gi.FunctionInfo(get_offset), 'get_tzid': gi.FunctionInfo(get_tzid), 'has_dst': gi.FunctionInfo(has_dst), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), 'get_by_tzid': gi.FunctionInfo(get_by_tzid), 'get_utc': gi.FunctionInfo(get_utc)})"
    __gtype__ = None # (!) real value is '<GType GWeatherTimezone (94766763410192)>'
    __info__ = StructInfo(Timezone)


class TimezoneMenu(__gi_overrides_Gtk.ComboBox):
    """
    :Constructors:
    
    ::
    
        TimezoneMenu(**properties)
        new(top:GWeather.Location) -> Gtk.Widget
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def add(self, widget): # real signature unknown; restored from __doc__
        """ add(self, widget:Gtk.Widget) """
        pass

    def add_accelerator(self, accel_signal, accel_group, accel_key, accel_mods, accel_flags): # real signature unknown; restored from __doc__
        """ add_accelerator(self, accel_signal:str, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType, accel_flags:Gtk.AccelFlags) """
        pass

    def add_attribute(self, cell, attribute, column): # real signature unknown; restored from __doc__
        """ add_attribute(self, cell:Gtk.CellRenderer, attribute:str, column:int) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def add_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ add_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def add_events(self, events): # real signature unknown; restored from __doc__
        """ add_events(self, events:int) """
        pass

    def add_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ add_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def add_tick_callback(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_tick_callback(self, callback:Gtk.TickCallback, user_data=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def bind_template_callback_full(self, callback_name, callback_symbol): # real signature unknown; restored from __doc__
        """ bind_template_callback_full(self, callback_name:str, callback_symbol:GObject.Callback) """
        pass

    def bind_template_child_full(self, name, internal_child, struct_offset): # real signature unknown; restored from __doc__
        """ bind_template_child_full(self, name:str, internal_child:bool, struct_offset:int) """
        pass

    def can_activate_accel(self, signal_id): # real signature unknown; restored from __doc__
        """ can_activate_accel(self, signal_id:int) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_resize(self): # real signature unknown; restored from __doc__
        """ check_resize(self) """
        pass

    def child_focus(self, direction): # real signature unknown; restored from __doc__
        """ child_focus(self, direction:Gtk.DirectionType) -> bool """
        return False

    def child_get(self, child, *prop_names): # reliably restored by inspect
        """ Returns a list of child property values for the given names. """
        pass

    def child_get_property(self, child, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def child_notify(self, child, child_property): # real signature unknown; restored from __doc__
        """ child_notify(self, child:Gtk.Widget, child_property:str) """
        pass

    def child_notify_by_pspec(self, child, pspec): # real signature unknown; restored from __doc__
        """ child_notify_by_pspec(self, child:Gtk.Widget, pspec:GObject.ParamSpec) """
        pass

    def child_set(self, child, **kwargs): # reliably restored by inspect
        """ Set a child properties on the given child to key/value pairs. """
        pass

    def child_set_property(self, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, child:Gtk.Widget, property_name:str, value:GObject.Value) """
        pass

    def child_type(self): # real signature unknown; restored from __doc__
        """ child_type(self) -> GType """
        pass

    def class_path(self): # real signature unknown; restored from __doc__
        """ class_path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_attributes(self, cell): # real signature unknown; restored from __doc__
        """ clear_attributes(self, cell:Gtk.CellRenderer) """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def compute_expand(self, orientation): # real signature unknown; restored from __doc__
        """ compute_expand(self, orientation:Gtk.Orientation) -> bool """
        return False

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def create_pango_context(self): # real signature unknown; restored from __doc__
        """ create_pango_context(self) -> Pango.Context """
        pass

    def create_pango_layout(self, text=None): # real signature unknown; restored from __doc__
        """ create_pango_layout(self, text:str=None) -> Pango.Layout """
        pass

    def custom_finished(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_finished(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_end(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_tag_end(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_start(self, builder, child=None, tagname): # real signature unknown; restored from __doc__
        """ custom_tag_start(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str) -> bool, parser:GLib.MarkupParser, data """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def destroyed(self, widget_pointer): # real signature unknown; restored from __doc__
        """ destroyed(self, widget_pointer:Gtk.Widget) -> widget_pointer:Gtk.Widget """
        pass

    def device_is_shadowed(self, device): # real signature unknown; restored from __doc__
        """ device_is_shadowed(self, device:Gdk.Device) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add(self, *args, **kwargs): # real signature unknown
        """ add(self, widget:Gtk.Widget) """
        pass

    def do_adjust_baseline_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_allocation(self, baseline:int) """
        pass

    def do_adjust_baseline_request(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_request(self, minimum_baseline:int, natural_baseline:int) """
        pass

    def do_adjust_size_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_size_allocation(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int, allocated_pos:int, allocated_size:int) """
        pass

    def do_adjust_size_request(self, *args, **kwargs): # real signature unknown
        """ adjust_size_request(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_can_activate_accel(self, *args, **kwargs): # real signature unknown
        """ can_activate_accel(self, signal_id:int) -> bool """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_check_resize(self, *args, **kwargs): # real signature unknown
        """ check_resize(self) """
        pass

    def do_child_notify(self, *args, **kwargs): # real signature unknown
        """ child_notify(self, child_property:GObject.ParamSpec) """
        pass

    def do_child_type(self, *args, **kwargs): # real signature unknown
        """ child_type(self) -> GType """
        pass

    def do_composited_changed(self, *args, **kwargs): # real signature unknown
        """ composited_changed(self) """
        pass

    def do_composite_name(self, *args, **kwargs): # real signature unknown
        """ composite_name(self, child:Gtk.Widget) -> str """
        pass

    def do_compute_expand(self, *args, **kwargs): # real signature unknown
        """ compute_expand(self, hexpand_p:bool, vexpand_p:bool) """
        pass

    def do_configure_event(self, *args, **kwargs): # real signature unknown
        """ configure_event(self, event:Gdk.EventConfigure) -> bool """
        pass

    def do_damage_event(self, *args, **kwargs): # real signature unknown
        """ damage_event(self, event:Gdk.EventExpose) -> bool """
        pass

    def do_delete_event(self, *args, **kwargs): # real signature unknown
        """ delete_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_destroy_event(self, *args, **kwargs): # real signature unknown
        """ destroy_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_direction_changed(self, *args, **kwargs): # real signature unknown
        """ direction_changed(self, previous_direction:Gtk.TextDirection) """
        pass

    def do_dispatch_child_properties_changed(self, *args, **kwargs): # real signature unknown
        """ dispatch_child_properties_changed(self, n_pspecs:int, pspecs:GObject.ParamSpec) """
        pass

    def do_drag_begin(self, *args, **kwargs): # real signature unknown
        """ drag_begin(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_delete(self, *args, **kwargs): # real signature unknown
        """ drag_data_delete(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_get(self, *args, **kwargs): # real signature unknown
        """ drag_data_get(self, context:Gdk.DragContext, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_data_received(self, *args, **kwargs): # real signature unknown
        """ drag_data_received(self, context:Gdk.DragContext, x:int, y:int, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_drop(self, *args, **kwargs): # real signature unknown
        """ drag_drop(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_drag_end(self, *args, **kwargs): # real signature unknown
        """ drag_end(self, context:Gdk.DragContext) """
        pass

    def do_drag_failed(self, *args, **kwargs): # real signature unknown
        """ drag_failed(self, context:Gdk.DragContext, result:Gtk.DragResult) -> bool """
        pass

    def do_drag_leave(self, *args, **kwargs): # real signature unknown
        """ drag_leave(self, context:Gdk.DragContext, time_:int) """
        pass

    def do_drag_motion(self, *args, **kwargs): # real signature unknown
        """ drag_motion(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_draw(self, *args, **kwargs): # real signature unknown
        """ draw(self, cr:cairo.Context) -> bool """
        pass

    def do_enter_notify_event(self, *args, **kwargs): # real signature unknown
        """ enter_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gdk.Event) -> bool """
        pass

    def do_focus(self, *args, **kwargs): # real signature unknown
        """ focus(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_focus_in_event(self, *args, **kwargs): # real signature unknown
        """ focus_in_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_focus_out_event(self, *args, **kwargs): # real signature unknown
        """ focus_out_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_forall(self, *args, **kwargs): # real signature unknown
        """ forall(self, include_internals:bool, callback:Gtk.Callback, callback_data=None) """
        pass

    def do_format_entry_text(self, *args, **kwargs): # real signature unknown
        """ format_entry_text(self, path:str) -> str """
        pass

    def do_get_accessible(self, *args, **kwargs): # real signature unknown
        """ get_accessible(self) -> Atk.Object """
        pass

    def do_get_child_property(self, *args, **kwargs): # real signature unknown
        """ get_child_property(self, child:Gtk.Widget, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def do_get_path_for_child(self, *args, **kwargs): # real signature unknown
        """ get_path_for_child(self, child:Gtk.Widget) -> Gtk.WidgetPath """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_height_and_baseline_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def do_get_preferred_height_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def do_get_preferred_width_for_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def do_get_request_mode(self, *args, **kwargs): # real signature unknown
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def do_grab_broken_event(self, *args, **kwargs): # real signature unknown
        """ grab_broken_event(self, event:Gdk.EventGrabBroken) -> bool """
        pass

    def do_grab_focus(self, *args, **kwargs): # real signature unknown
        """ grab_focus(self) """
        pass

    def do_grab_notify(self, *args, **kwargs): # real signature unknown
        """ grab_notify(self, was_grabbed:bool) """
        pass

    def do_hide(self, *args, **kwargs): # real signature unknown
        """ hide(self) """
        pass

    def do_hierarchy_changed(self, *args, **kwargs): # real signature unknown
        """ hierarchy_changed(self, previous_toplevel:Gtk.Widget) """
        pass

    def do_keynav_failed(self, *args, **kwargs): # real signature unknown
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_key_press_event(self, *args, **kwargs): # real signature unknown
        """ key_press_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_key_release_event(self, *args, **kwargs): # real signature unknown
        """ key_release_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_leave_notify_event(self, *args, **kwargs): # real signature unknown
        """ leave_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_map(self, *args, **kwargs): # real signature unknown
        """ map(self) """
        pass

    def do_map_event(self, *args, **kwargs): # real signature unknown
        """ map_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_mnemonic_activate(self, *args, **kwargs): # real signature unknown
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        pass

    def do_motion_notify_event(self, *args, **kwargs): # real signature unknown
        """ motion_notify_event(self, event:Gdk.EventMotion) -> bool """
        pass

    def do_move_focus(self, *args, **kwargs): # real signature unknown
        """ move_focus(self, direction:Gtk.DirectionType) """
        pass

    def do_parent_set(self, *args, **kwargs): # real signature unknown
        """ parent_set(self, previous_parent:Gtk.Widget) """
        pass

    def do_popup_menu(self, *args, **kwargs): # real signature unknown
        """ popup_menu(self) -> bool """
        pass

    def do_property_notify_event(self, *args, **kwargs): # real signature unknown
        """ property_notify_event(self, event:Gdk.EventProperty) -> bool """
        pass

    def do_proximity_in_event(self, *args, **kwargs): # real signature unknown
        """ proximity_in_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_proximity_out_event(self, *args, **kwargs): # real signature unknown
        """ proximity_out_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_query_tooltip(self, *args, **kwargs): # real signature unknown
        """ query_tooltip(self, x:int, y:int, keyboard_tooltip:bool, tooltip:Gtk.Tooltip) -> bool """
        pass

    def do_queue_draw_region(self, *args, **kwargs): # real signature unknown
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def do_realize(self, *args, **kwargs): # real signature unknown
        """ realize(self) """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, widget:Gtk.Widget) """
        pass

    def do_screen_changed(self, *args, **kwargs): # real signature unknown
        """ screen_changed(self, previous_screen:Gdk.Screen) """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Gdk.EventScroll) -> bool """
        pass

    def do_selection_clear_event(self, *args, **kwargs): # real signature unknown
        """ selection_clear_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_get(self, *args, **kwargs): # real signature unknown
        """ selection_get(self, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_selection_notify_event(self, *args, **kwargs): # real signature unknown
        """ selection_notify_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_received(self, *args, **kwargs): # real signature unknown
        """ selection_received(self, selection_data:Gtk.SelectionData, time_:int) """
        pass

    def do_selection_request_event(self, *args, **kwargs): # real signature unknown
        """ selection_request_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_set_child_property(self, *args, **kwargs): # real signature unknown
        """ set_child_property(self, child:Gtk.Widget, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def do_set_focus_child(self, *args, **kwargs): # real signature unknown
        """ set_focus_child(self, child:Gtk.Widget=None) """
        pass

    def do_show(self, *args, **kwargs): # real signature unknown
        """ show(self) """
        pass

    def do_show_all(self, *args, **kwargs): # real signature unknown
        """ show_all(self) """
        pass

    def do_show_help(self, *args, **kwargs): # real signature unknown
        """ show_help(self, help_type:Gtk.WidgetHelpType) -> bool """
        pass

    def do_size_allocate(self, *args, **kwargs): # real signature unknown
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, previous_state:Gtk.StateType) """
        pass

    def do_state_flags_changed(self, *args, **kwargs): # real signature unknown
        """ state_flags_changed(self, previous_state_flags:Gtk.StateFlags) """
        pass

    def do_style_set(self, *args, **kwargs): # real signature unknown
        """ style_set(self, previous_style:Gtk.Style) """
        pass

    def do_style_updated(self, *args, **kwargs): # real signature unknown
        """ style_updated(self) """
        pass

    def do_touch_event(self, *args, **kwargs): # real signature unknown
        """ touch_event(self, event:Gdk.EventTouch) -> bool """
        pass

    def do_unmap(self, *args, **kwargs): # real signature unknown
        """ unmap(self) """
        pass

    def do_unmap_event(self, *args, **kwargs): # real signature unknown
        """ unmap_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_unrealize(self, *args, **kwargs): # real signature unknown
        """ unrealize(self) """
        pass

    def do_visibility_notify_event(self, *args, **kwargs): # real signature unknown
        """ visibility_notify_event(self, event:Gdk.EventVisibility) -> bool """
        pass

    def do_window_state_event(self, *args, **kwargs): # real signature unknown
        """ window_state_event(self, event:Gdk.EventWindowState) -> bool """
        pass

    def drag_begin(self, targets, actions, button, event=None): # real signature unknown; restored from __doc__
        """ drag_begin(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None) -> Gdk.DragContext """
        pass

    def drag_begin_with_coordinates(self, targets, actions, button, event=None, x, y): # real signature unknown; restored from __doc__
        """ drag_begin_with_coordinates(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None, x:int, y:int) -> Gdk.DragContext """
        pass

    def drag_check_threshold(self, start_x, start_y, current_x, current_y): # real signature unknown; restored from __doc__
        """ drag_check_threshold(self, start_x:int, start_y:int, current_x:int, current_y:int) -> bool """
        return False

    def drag_dest_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_image_targets(self) """
        pass

    def drag_dest_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_text_targets(self) """
        pass

    def drag_dest_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_uri_targets(self) """
        pass

    def drag_dest_find_target(self, context, target_list=None): # real signature unknown; restored from __doc__
        """ drag_dest_find_target(self, context:Gdk.DragContext, target_list:Gtk.TargetList=None) -> Gdk.Atom """
        pass

    def drag_dest_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_dest_get_track_motion(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_track_motion(self) -> bool """
        return False

    def drag_dest_set(self, flags, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_dest_set(self, flags:Gtk.DestDefaults, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_dest_set_proxy(self, proxy_window, protocol, use_coordinates): # real signature unknown; restored from __doc__
        """ drag_dest_set_proxy(self, proxy_window:Gdk.Window, protocol:Gdk.DragProtocol, use_coordinates:bool) """
        pass

    def drag_dest_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_dest_set_track_motion(self, track_motion): # real signature unknown; restored from __doc__
        """ drag_dest_set_track_motion(self, track_motion:bool) """
        pass

    def drag_dest_unset(self): # real signature unknown; restored from __doc__
        """ drag_dest_unset(self) """
        pass

    def drag_get_data(self, context, target, time_): # real signature unknown; restored from __doc__
        """ drag_get_data(self, context:Gdk.DragContext, target:Gdk.Atom, time_:int) """
        pass

    def drag_highlight(self): # real signature unknown; restored from __doc__
        """ drag_highlight(self) """
        pass

    def drag_source_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_image_targets(self) """
        pass

    def drag_source_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_text_targets(self) """
        pass

    def drag_source_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_uri_targets(self) """
        pass

    def drag_source_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_source_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_source_set(self, start_button_mask, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_source_set(self, start_button_mask:Gdk.ModifierType, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_source_set_icon_gicon(self, icon): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_gicon(self, icon:Gio.Icon) """
        pass

    def drag_source_set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_name(self, icon_name:str) """
        pass

    def drag_source_set_icon_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def drag_source_set_icon_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_stock(self, stock_id:str) """
        pass

    def drag_source_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_source_unset(self): # real signature unknown; restored from __doc__
        """ drag_source_unset(self) """
        pass

    def drag_unhighlight(self): # real signature unknown; restored from __doc__
        """ drag_unhighlight(self) """
        pass

    def draw(self, cr): # real signature unknown; restored from __doc__
        """ draw(self, cr:cairo.Context) """
        pass

    def editing_done(self): # real signature unknown; restored from __doc__
        """ editing_done(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_style(self): # real signature unknown; restored from __doc__
        """ ensure_style(self) """
        pass

    def error_bell(self): # real signature unknown; restored from __doc__
        """ error_bell(self) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event:Gdk.Event) -> bool """
        return False

    def find_child_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_child_property(self, property_name:str) -> GObject.ParamSpec or None """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_style_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_style_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def forall(self, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ forall(self, callback:Gtk.Callback, callback_data=None) """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, callback:Gtk.Callback, callback_data=None) """
        pass

    def freeze_child_notify(self): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accessible(self): # real signature unknown; restored from __doc__
        """ get_accessible(self) -> Atk.Object """
        pass

    def get_action_group(self, prefix): # real signature unknown; restored from __doc__
        """ get_action_group(self, prefix:str) -> Gio.ActionGroup or None """
        pass

    def get_active(self): # real signature unknown; restored from __doc__
        """ get_active(self) -> int """
        return 0

    def get_active_id(self): # real signature unknown; restored from __doc__
        """ get_active_id(self) -> str or None """
        return ""

    def get_active_iter(*args, **kwargs): # reliably restored by inspect
        """ get_active_iter(self) -> bool, iter:Gtk.TreeIter """
        pass

    def get_add_tearoffs(self): # real signature unknown; restored from __doc__
        """ get_add_tearoffs(self) -> bool """
        return False

    def get_allocated_baseline(self): # real signature unknown; restored from __doc__
        """ get_allocated_baseline(self) -> int """
        return 0

    def get_allocated_height(self): # real signature unknown; restored from __doc__
        """ get_allocated_height(self) -> int """
        return 0

    def get_allocated_size(self): # real signature unknown; restored from __doc__
        """ get_allocated_size(self) -> allocation:Gdk.Rectangle, baseline:int """
        pass

    def get_allocated_width(self): # real signature unknown; restored from __doc__
        """ get_allocated_width(self) -> int """
        return 0

    def get_allocation(self): # real signature unknown; restored from __doc__
        """ get_allocation(self) -> allocation:Gdk.Rectangle """
        pass

    def get_ancestor(self, widget_type): # real signature unknown; restored from __doc__
        """ get_ancestor(self, widget_type:GType) -> Gtk.Widget or None """
        pass

    def get_app_paintable(self): # real signature unknown; restored from __doc__
        """ get_app_paintable(self) -> bool """
        return False

    def get_area(self): # real signature unknown; restored from __doc__
        """ get_area(self) -> Gtk.CellArea or None """
        pass

    def get_border_width(self): # real signature unknown; restored from __doc__
        """ get_border_width(self) -> int """
        return 0

    def get_button_sensitivity(self): # real signature unknown; restored from __doc__
        """ get_button_sensitivity(self) -> Gtk.SensitivityType """
        pass

    def get_can_default(self): # real signature unknown; restored from __doc__
        """ get_can_default(self) -> bool """
        return False

    def get_can_focus(self): # real signature unknown; restored from __doc__
        """ get_can_focus(self) -> bool """
        return False

    def get_cells(self): # real signature unknown; restored from __doc__
        """ get_cells(self) -> list """
        return []

    def get_child(self): # real signature unknown; restored from __doc__
        """ get_child(self) -> Gtk.Widget or None """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_child_requisition(self): # real signature unknown; restored from __doc__
        """ get_child_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_child_visible(self): # real signature unknown; restored from __doc__
        """ get_child_visible(self) -> bool """
        return False

    def get_clip(self): # real signature unknown; restored from __doc__
        """ get_clip(self) -> clip:Gdk.Rectangle """
        pass

    def get_clipboard(self, selection): # real signature unknown; restored from __doc__
        """ get_clipboard(self, selection:Gdk.Atom) -> Gtk.Clipboard """
        pass

    def get_column_span_column(self): # real signature unknown; restored from __doc__
        """ get_column_span_column(self) -> int """
        return 0

    def get_composite_name(self): # real signature unknown; restored from __doc__
        """ get_composite_name(self) -> str """
        return ""

    def get_css_name(self): # real signature unknown; restored from __doc__
        """ get_css_name(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_direction(self): # real signature unknown; restored from __doc__
        """ get_default_direction() -> Gtk.TextDirection """
        pass

    def get_default_style(self): # real signature unknown; restored from __doc__
        """ get_default_style() -> Gtk.Style """
        pass

    def get_device_enabled(self, device): # real signature unknown; restored from __doc__
        """ get_device_enabled(self, device:Gdk.Device) -> bool """
        return False

    def get_device_events(self, device): # real signature unknown; restored from __doc__
        """ get_device_events(self, device:Gdk.Device) -> Gdk.EventMask """
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_double_buffered(self): # real signature unknown; restored from __doc__
        """ get_double_buffered(self) -> bool """
        return False

    def get_entry_text_column(self): # real signature unknown; restored from __doc__
        """ get_entry_text_column(self) -> int """
        return 0

    def get_events(self): # real signature unknown; restored from __doc__
        """ get_events(self) -> int """
        return 0

    def get_focus_chain(*args, **kwargs): # reliably restored by inspect
        """ get_focus_chain(self) -> bool, focusable_widgets:list """
        pass

    def get_focus_child(self): # real signature unknown; restored from __doc__
        """ get_focus_child(self) -> Gtk.Widget or None """
        pass

    def get_focus_hadjustment(self): # real signature unknown; restored from __doc__
        """ get_focus_hadjustment(self) -> Gtk.Adjustment or None """
        pass

    def get_focus_on_click(self): # real signature unknown; restored from __doc__
        """ get_focus_on_click(self) -> bool """
        return False

    def get_focus_vadjustment(self): # real signature unknown; restored from __doc__
        """ get_focus_vadjustment(self) -> Gtk.Adjustment or None """
        pass

    def get_font_map(self): # real signature unknown; restored from __doc__
        """ get_font_map(self) -> Pango.FontMap or None """
        pass

    def get_font_options(self): # real signature unknown; restored from __doc__
        """ get_font_options(self) -> cairo.FontOptions or None """
        pass

    def get_frame_clock(self): # real signature unknown; restored from __doc__
        """ get_frame_clock(self) -> Gdk.FrameClock or None """
        pass

    def get_halign(self): # real signature unknown; restored from __doc__
        """ get_halign(self) -> Gtk.Align """
        pass

    def get_has_entry(self): # real signature unknown; restored from __doc__
        """ get_has_entry(self) -> bool """
        return False

    def get_has_tooltip(self): # real signature unknown; restored from __doc__
        """ get_has_tooltip(self) -> bool """
        return False

    def get_has_window(self): # real signature unknown; restored from __doc__
        """ get_has_window(self) -> bool """
        return False

    def get_hexpand(self): # real signature unknown; restored from __doc__
        """ get_hexpand(self) -> bool """
        return False

    def get_hexpand_set(self): # real signature unknown; restored from __doc__
        """ get_hexpand_set(self) -> bool """
        return False

    def get_id_column(self): # real signature unknown; restored from __doc__
        """ get_id_column(self) -> int """
        return 0

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_mapped(self): # real signature unknown; restored from __doc__
        """ get_mapped(self) -> bool """
        return False

    def get_margin_bottom(self): # real signature unknown; restored from __doc__
        """ get_margin_bottom(self) -> int """
        return 0

    def get_margin_end(self): # real signature unknown; restored from __doc__
        """ get_margin_end(self) -> int """
        return 0

    def get_margin_left(self): # real signature unknown; restored from __doc__
        """ get_margin_left(self) -> int """
        return 0

    def get_margin_right(self): # real signature unknown; restored from __doc__
        """ get_margin_right(self) -> int """
        return 0

    def get_margin_start(self): # real signature unknown; restored from __doc__
        """ get_margin_start(self) -> int """
        return 0

    def get_margin_top(self): # real signature unknown; restored from __doc__
        """ get_margin_top(self) -> int """
        return 0

    def get_model(self): # real signature unknown; restored from __doc__
        """ get_model(self) -> Gtk.TreeModel """
        pass

    def get_modifier_mask(self, intent): # real signature unknown; restored from __doc__
        """ get_modifier_mask(self, intent:Gdk.ModifierIntent) -> Gdk.ModifierType """
        pass

    def get_modifier_style(self): # real signature unknown; restored from __doc__
        """ get_modifier_style(self) -> Gtk.RcStyle """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_no_show_all(self): # real signature unknown; restored from __doc__
        """ get_no_show_all(self) -> bool """
        return False

    def get_opacity(self): # real signature unknown; restored from __doc__
        """ get_opacity(self) -> float """
        return 0.0

    def get_pango_context(self): # real signature unknown; restored from __doc__
        """ get_pango_context(self) -> Pango.Context """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gtk.Widget or None """
        pass

    def get_parent_window(self): # real signature unknown; restored from __doc__
        """ get_parent_window(self) -> Gdk.Window or None """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.WidgetPath """
        pass

    def get_path_for_child(self, child): # real signature unknown; restored from __doc__
        """ get_path_for_child(self, child:Gtk.Widget) -> Gtk.WidgetPath """
        pass

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) -> x:int, y:int """
        pass

    def get_popup_accessible(self): # real signature unknown; restored from __doc__
        """ get_popup_accessible(self) -> Atk.Object """
        pass

    def get_popup_fixed_width(self): # real signature unknown; restored from __doc__
        """ get_popup_fixed_width(self) -> bool """
        return False

    def get_preferred_height(self): # real signature unknown; restored from __doc__
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_height_and_baseline_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def get_preferred_height_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_size(self): # real signature unknown; restored from __doc__
        """ get_preferred_size(self) -> minimum_size:Gtk.Requisition, natural_size:Gtk.Requisition """
        pass

    def get_preferred_width(self): # real signature unknown; restored from __doc__
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def get_preferred_width_for_height(self, height): # real signature unknown; restored from __doc__
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_realized(self): # real signature unknown; restored from __doc__
        """ get_realized(self) -> bool """
        return False

    def get_receives_default(self): # real signature unknown; restored from __doc__
        """ get_receives_default(self) -> bool """
        return False

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def get_requisition(self): # real signature unknown; restored from __doc__
        """ get_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_resize_mode(self): # real signature unknown; restored from __doc__
        """ get_resize_mode(self) -> Gtk.ResizeMode """
        pass

    def get_root_window(self): # real signature unknown; restored from __doc__
        """ get_root_window(self) -> Gdk.Window """
        pass

    def get_row_span_column(self): # real signature unknown; restored from __doc__
        """ get_row_span_column(self) -> int """
        return 0

    def get_scale_factor(self): # real signature unknown; restored from __doc__
        """ get_scale_factor(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_settings(self): # real signature unknown; restored from __doc__
        """ get_settings(self) -> Gtk.Settings """
        pass

    def get_size_request(self): # real signature unknown; restored from __doc__
        """ get_size_request(self) -> width:int, height:int """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateType """
        pass

    def get_state_flags(self): # real signature unknown; restored from __doc__
        """ get_state_flags(self) -> Gtk.StateFlags """
        pass

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> Gtk.Style """
        pass

    def get_style_context(self): # real signature unknown; restored from __doc__
        """ get_style_context(self) -> Gtk.StyleContext """
        pass

    def get_support_multidevice(self): # real signature unknown; restored from __doc__
        """ get_support_multidevice(self) -> bool """
        return False

    def get_template_child(self, widget_type, name): # real signature unknown; restored from __doc__
        """ get_template_child(self, widget_type:GType, name:str) -> GObject.Object """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_tooltip_markup(self): # real signature unknown; restored from __doc__
        """ get_tooltip_markup(self) -> str or None """
        return ""

    def get_tooltip_text(self): # real signature unknown; restored from __doc__
        """ get_tooltip_text(self) -> str or None """
        return ""

    def get_tooltip_window(self): # real signature unknown; restored from __doc__
        """ get_tooltip_window(self) -> Gtk.Window """
        pass

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> Gtk.Widget """
        pass

    def get_tzid(self): # real signature unknown; restored from __doc__
        """ get_tzid(self) -> str or None """
        return ""

    def get_valign(self): # real signature unknown; restored from __doc__
        """ get_valign(self) -> Gtk.Align """
        pass

    def get_valign_with_baseline(self): # real signature unknown; restored from __doc__
        """ get_valign_with_baseline(self) -> Gtk.Align """
        pass

    def get_vexpand(self): # real signature unknown; restored from __doc__
        """ get_vexpand(self) -> bool """
        return False

    def get_vexpand_set(self): # real signature unknown; restored from __doc__
        """ get_vexpand_set(self) -> bool """
        return False

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_visual(self): # real signature unknown; restored from __doc__
        """ get_visual(self) -> Gdk.Visual """
        pass

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window or None """
        pass

    def get_wrap_width(self): # real signature unknown; restored from __doc__
        """ get_wrap_width(self) -> int """
        return 0

    def grab_add(self): # real signature unknown; restored from __doc__
        """ grab_add(self) """
        pass

    def grab_default(self): # real signature unknown; restored from __doc__
        """ grab_default(self) """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) """
        pass

    def grab_remove(self): # real signature unknown; restored from __doc__
        """ grab_remove(self) """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handle_border_width(self): # real signature unknown; restored from __doc__
        """ handle_border_width(self) """
        pass

    def has_default(self): # real signature unknown; restored from __doc__
        """ has_default(self) -> bool """
        return False

    def has_focus(self): # real signature unknown; restored from __doc__
        """ has_focus(self) -> bool """
        return False

    def has_grab(self): # real signature unknown; restored from __doc__
        """ has_grab(self) -> bool """
        return False

    def has_rc_style(self): # real signature unknown; restored from __doc__
        """ has_rc_style(self) -> bool """
        return False

    def has_screen(self): # real signature unknown; restored from __doc__
        """ has_screen(self) -> bool """
        return False

    def has_visible_focus(self): # real signature unknown; restored from __doc__
        """ has_visible_focus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hide_on_delete(self): # real signature unknown; restored from __doc__
        """ hide_on_delete(self) -> bool """
        return False

    def init_template(self): # real signature unknown; restored from __doc__
        """ init_template(self) """
        pass

    def input_shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ input_shape_combine_region(self, region:cairo.Region=None) """
        pass

    def insert_action_group(self, name, group=None): # real signature unknown; restored from __doc__
        """ insert_action_group(self, name:str, group:Gio.ActionGroup=None) """
        pass

    def install_child_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_child_properties(self, pspecs:list) """
        pass

    def install_child_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_child_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_style_property(self, pspec): # real signature unknown; restored from __doc__
        """ install_style_property(self, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def intersect(self, area): # real signature unknown; restored from __doc__
        """ intersect(self, area:Gdk.Rectangle) -> bool, intersection:Gdk.Rectangle """
        return False

    def in_destruction(self): # real signature unknown; restored from __doc__
        """ in_destruction(self) -> bool """
        return False

    def is_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ is_ancestor(self, ancestor:Gtk.Widget) -> bool """
        return False

    def is_composited(self): # real signature unknown; restored from __doc__
        """ is_composited(self) -> bool """
        return False

    def is_drawable(self): # real signature unknown; restored from __doc__
        """ is_drawable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_focus(self): # real signature unknown; restored from __doc__
        """ is_focus(self) -> bool """
        return False

    def is_sensitive(self): # real signature unknown; restored from __doc__
        """ is_sensitive(self) -> bool """
        return False

    def is_toplevel(self): # real signature unknown; restored from __doc__
        """ is_toplevel(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def keynav_failed(self, direction): # real signature unknown; restored from __doc__
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        return False

    def list_accel_closures(self): # real signature unknown; restored from __doc__
        """ list_accel_closures(self) -> list """
        return []

    def list_action_prefixes(self): # real signature unknown; restored from __doc__
        """ list_action_prefixes(self) -> list """
        return []

    def list_child_properties(self): # real signature unknown; restored from __doc__
        """ list_child_properties(self) -> list, n_properties:int """
        return []

    def list_mnemonic_labels(self): # real signature unknown; restored from __doc__
        """ list_mnemonic_labels(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_style_properties(self): # real signature unknown; restored from __doc__
        """ list_style_properties(self) -> list, n_properties:int """
        return []

    def map(self): # real signature unknown; restored from __doc__
        """ map(self) """
        pass

    def mnemonic_activate(self, group_cycling): # real signature unknown; restored from __doc__
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        return False

    def modify_base(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_base(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_bg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_bg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_cursor(self, primary=None, secondary=None): # real signature unknown; restored from __doc__
        """ modify_cursor(self, primary:Gdk.Color=None, secondary:Gdk.Color=None) """
        pass

    def modify_fg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_fg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ modify_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def modify_style(self, style): # real signature unknown; restored from __doc__
        """ modify_style(self, style:Gtk.RcStyle) """
        pass

    def modify_text(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_text(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def new(self, top): # real signature unknown; restored from __doc__
        """ new(top:GWeather.Location) -> Gtk.Widget """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_area(self, area): # real signature unknown; restored from __doc__
        """ new_with_area(area:Gtk.CellArea) -> Gtk.Widget """
        pass

    def new_with_area_and_entry(self, area): # real signature unknown; restored from __doc__
        """ new_with_area_and_entry(area:Gtk.CellArea) -> Gtk.Widget """
        pass

    def new_with_entry(self): # real signature unknown; restored from __doc__
        """ new_with_entry() -> Gtk.Widget """
        pass

    def new_with_model(self, model): # real signature unknown; restored from __doc__
        """ new_with_model(model:Gtk.TreeModel) -> Gtk.Widget """
        pass

    def new_with_model_and_entry(self, model): # real signature unknown; restored from __doc__
        """ new_with_model_and_entry(model:Gtk.TreeModel) -> Gtk.Widget """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_background_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_background_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_cursor(self, cursor=None, secondary_cursor=None): # real signature unknown; restored from __doc__
        """ override_cursor(self, cursor:Gdk.RGBA=None, secondary_cursor:Gdk.RGBA=None) """
        pass

    def override_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ override_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def override_symbolic_color(self, name, color=None): # real signature unknown; restored from __doc__
        """ override_symbolic_color(self, name:str, color:Gdk.RGBA=None) """
        pass

    def pack_end(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_end(self, cell:Gtk.CellRenderer, expand:bool) """
        pass

    def pack_start(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_start(self, cell:Gtk.CellRenderer, expand:bool) """
        pass

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def popdown(self): # real signature unknown; restored from __doc__
        """ popdown(self) """
        pass

    def popup(self): # real signature unknown; restored from __doc__
        """ popup(self) """
        pass

    def popup_for_device(self, device): # real signature unknown; restored from __doc__
        """ popup_for_device(self, device:Gdk.Device) """
        pass

    def pop_composite_child(self): # real signature unknown; restored from __doc__
        """ pop_composite_child() """
        pass

    def propagate_draw(self, child, cr): # real signature unknown; restored from __doc__
        """ propagate_draw(self, child:Gtk.Widget, cr:cairo.Context) """
        pass

    def push_composite_child(self): # real signature unknown; restored from __doc__
        """ push_composite_child() """
        pass

    def queue_allocate(self): # real signature unknown; restored from __doc__
        """ queue_allocate(self) """
        pass

    def queue_compute_expand(self): # real signature unknown; restored from __doc__
        """ queue_compute_expand(self) """
        pass

    def queue_draw(self): # real signature unknown; restored from __doc__
        """ queue_draw(self) """
        pass

    def queue_draw_area(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ queue_draw_area(self, x:int, y:int, width:int, height:int) """
        pass

    def queue_draw_region(self, region): # real signature unknown; restored from __doc__
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def queue_resize(self): # real signature unknown; restored from __doc__
        """ queue_resize(self) """
        pass

    def queue_resize_no_redraw(self): # real signature unknown; restored from __doc__
        """ queue_resize_no_redraw(self) """
        pass

    def realize(self): # real signature unknown; restored from __doc__
        """ realize(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def region_intersect(self, region): # real signature unknown; restored from __doc__
        """ region_intersect(self, region:cairo.Region) -> cairo.Region """
        pass

    def register_window(self, window): # real signature unknown; restored from __doc__
        """ register_window(self, window:Gdk.Window) """
        pass

    def remove(self, widget): # real signature unknown; restored from __doc__
        """ remove(self, widget:Gtk.Widget) """
        pass

    def remove_accelerator(self, accel_group, accel_key, accel_mods): # real signature unknown; restored from __doc__
        """ remove_accelerator(self, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType) -> bool """
        return False

    def remove_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ remove_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def remove_tick_callback(self, id): # real signature unknown; restored from __doc__
        """ remove_tick_callback(self, id:int) """
        pass

    def remove_widget(self): # real signature unknown; restored from __doc__
        """ remove_widget(self) """
        pass

    def render_icon(self, stock_id, size, detail=None): # real signature unknown; restored from __doc__
        """ render_icon(self, stock_id:str, size:int, detail:str=None) -> GdkPixbuf.Pixbuf or None """
        pass

    def render_icon_pixbuf(self, stock_id, size): # real signature unknown; restored from __doc__
        """ render_icon_pixbuf(self, stock_id:str, size:int) -> GdkPixbuf.Pixbuf or None """
        pass

    def reorder(self, cell, position): # real signature unknown; restored from __doc__
        """ reorder(self, cell:Gtk.CellRenderer, position:int) """
        pass

    def reparent(self, new_parent): # real signature unknown; restored from __doc__
        """ reparent(self, new_parent:Gtk.Widget) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_rc_styles(self): # real signature unknown; restored from __doc__
        """ reset_rc_styles(self) """
        pass

    def reset_style(self): # real signature unknown; restored from __doc__
        """ reset_style(self) """
        pass

    def resize_children(self): # real signature unknown; restored from __doc__
        """ resize_children(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_expose(self, event): # real signature unknown; restored from __doc__
        """ send_expose(self, event:Gdk.Event) -> int """
        return 0

    def send_focus_change(self, event): # real signature unknown; restored from __doc__
        """ send_focus_change(self, event:Gdk.Event) -> bool """
        return False

    def set_accel_path(self, accel_path=None, accel_group=None): # real signature unknown; restored from __doc__
        """ set_accel_path(self, accel_path:str=None, accel_group:Gtk.AccelGroup=None) """
        pass

    def set_accessible_role(self, role): # real signature unknown; restored from __doc__
        """ set_accessible_role(self, role:Atk.Role) """
        pass

    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
        pass

    def set_active(self, index_): # real signature unknown; restored from __doc__
        """ set_active(self, index_:int) """
        pass

    def set_active_id(self, active_id=None): # real signature unknown; restored from __doc__
        """ set_active_id(self, active_id:str=None) -> bool """
        return False

    def set_active_iter(self, iter=None): # real signature unknown; restored from __doc__
        """ set_active_iter(self, iter:Gtk.TreeIter=None) """
        pass

    def set_add_tearoffs(self, add_tearoffs): # real signature unknown; restored from __doc__
        """ set_add_tearoffs(self, add_tearoffs:bool) """
        pass

    def set_allocation(self, allocation): # real signature unknown; restored from __doc__
        """ set_allocation(self, allocation:Gdk.Rectangle) """
        pass

    def set_app_paintable(self, app_paintable): # real signature unknown; restored from __doc__
        """ set_app_paintable(self, app_paintable:bool) """
        pass

    def set_border_width(self, border_width): # real signature unknown; restored from __doc__
        """ set_border_width(self, border_width:int) """
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_button_sensitivity(self, sensitivity): # real signature unknown; restored from __doc__
        """ set_button_sensitivity(self, sensitivity:Gtk.SensitivityType) """
        pass

    def set_can_default(self, can_default): # real signature unknown; restored from __doc__
        """ set_can_default(self, can_default:bool) """
        pass

    def set_can_focus(self, can_focus): # real signature unknown; restored from __doc__
        """ set_can_focus(self, can_focus:bool) """
        pass

    def set_cell_data_func(self, cell, func=None, func_data=None): # real signature unknown; restored from __doc__
        """ set_cell_data_func(self, cell:Gtk.CellRenderer, func:Gtk.CellLayoutDataFunc=None, func_data=None) """
        pass

    def set_child_visible(self, is_visible): # real signature unknown; restored from __doc__
        """ set_child_visible(self, is_visible:bool) """
        pass

    def set_clip(self, clip): # real signature unknown; restored from __doc__
        """ set_clip(self, clip:Gdk.Rectangle) """
        pass

    def set_column_span_column(self, column_span): # real signature unknown; restored from __doc__
        """ set_column_span_column(self, column_span:int) """
        pass

    def set_composite_name(self, name): # real signature unknown; restored from __doc__
        """ set_composite_name(self, name:str) """
        pass

    def set_connect_func(self, connect_func, connect_data=None): # real signature unknown; restored from __doc__
        """ set_connect_func(self, connect_func:Gtk.BuilderConnectFunc, connect_data=None) """
        pass

    def set_css_name(self, name): # real signature unknown; restored from __doc__
        """ set_css_name(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_default_direction(dir:Gtk.TextDirection) """
        pass

    def set_device_enabled(self, device, enabled): # real signature unknown; restored from __doc__
        """ set_device_enabled(self, device:Gdk.Device, enabled:bool) """
        pass

    def set_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ set_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def set_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_direction(self, dir:Gtk.TextDirection) """
        pass

    def set_double_buffered(self, double_buffered): # real signature unknown; restored from __doc__
        """ set_double_buffered(self, double_buffered:bool) """
        pass

    def set_entry_text_column(self, text_column): # real signature unknown; restored from __doc__
        """ set_entry_text_column(self, text_column:int) """
        pass

    def set_events(self, events): # real signature unknown; restored from __doc__
        """ set_events(self, events:int) """
        pass

    def set_focus_chain(self, focusable_widgets): # real signature unknown; restored from __doc__
        """ set_focus_chain(self, focusable_widgets:list) """
        pass

    def set_focus_child(self, child=None): # real signature unknown; restored from __doc__
        """ set_focus_child(self, child:Gtk.Widget=None) """
        pass

    def set_focus_hadjustment(self, adjustment): # real signature unknown; restored from __doc__
        """ set_focus_hadjustment(self, adjustment:Gtk.Adjustment) """
        pass

    def set_focus_on_click(self, focus_on_click): # real signature unknown; restored from __doc__
        """ set_focus_on_click(self, focus_on_click:bool) """
        pass

    def set_focus_vadjustment(self, adjustment): # real signature unknown; restored from __doc__
        """ set_focus_vadjustment(self, adjustment:Gtk.Adjustment) """
        pass

    def set_font_map(self, font_map=None): # real signature unknown; restored from __doc__
        """ set_font_map(self, font_map:Pango.FontMap=None) """
        pass

    def set_font_options(self, options=None): # real signature unknown; restored from __doc__
        """ set_font_options(self, options:cairo.FontOptions=None) """
        pass

    def set_halign(self, align): # real signature unknown; restored from __doc__
        """ set_halign(self, align:Gtk.Align) """
        pass

    def set_has_tooltip(self, has_tooltip): # real signature unknown; restored from __doc__
        """ set_has_tooltip(self, has_tooltip:bool) """
        pass

    def set_has_window(self, has_window): # real signature unknown; restored from __doc__
        """ set_has_window(self, has_window:bool) """
        pass

    def set_hexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_hexpand(self, expand:bool) """
        pass

    def set_hexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_hexpand_set(self, set:bool) """
        pass

    def set_id_column(self, id_column): # real signature unknown; restored from __doc__
        """ set_id_column(self, id_column:int) """
        pass

    def set_mapped(self, mapped): # real signature unknown; restored from __doc__
        """ set_mapped(self, mapped:bool) """
        pass

    def set_margin_bottom(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_bottom(self, margin:int) """
        pass

    def set_margin_end(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_end(self, margin:int) """
        pass

    def set_margin_left(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_left(self, margin:int) """
        pass

    def set_margin_right(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_right(self, margin:int) """
        pass

    def set_margin_start(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_start(self, margin:int) """
        pass

    def set_margin_top(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_top(self, margin:int) """
        pass

    def set_model(self, model=None): # real signature unknown; restored from __doc__
        """ set_model(self, model:Gtk.TreeModel=None) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_no_show_all(self, no_show_all): # real signature unknown; restored from __doc__
        """ set_no_show_all(self, no_show_all:bool) """
        pass

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:float) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gtk.Widget) """
        pass

    def set_parent_window(self, parent_window): # real signature unknown; restored from __doc__
        """ set_parent_window(self, parent_window:Gdk.Window) """
        pass

    def set_popup_fixed_width(self, fixed): # real signature unknown; restored from __doc__
        """ set_popup_fixed_width(self, fixed:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_realized(self, realized): # real signature unknown; restored from __doc__
        """ set_realized(self, realized:bool) """
        pass

    def set_reallocate_redraws(self, needs_redraws): # real signature unknown; restored from __doc__
        """ set_reallocate_redraws(self, needs_redraws:bool) """
        pass

    def set_receives_default(self, receives_default): # real signature unknown; restored from __doc__
        """ set_receives_default(self, receives_default:bool) """
        pass

    def set_redraw_on_allocate(self, redraw_on_allocate): # real signature unknown; restored from __doc__
        """ set_redraw_on_allocate(self, redraw_on_allocate:bool) """
        pass

    def set_resize_mode(self, resize_mode): # real signature unknown; restored from __doc__
        """ set_resize_mode(self, resize_mode:Gtk.ResizeMode) """
        pass

    def set_row_separator_func(self, func, data=None): # real signature unknown; restored from __doc__
        """ set_row_separator_func(self, func:Gtk.TreeViewRowSeparatorFunc, data=None) """
        pass

    def set_row_span_column(self, row_span): # real signature unknown; restored from __doc__
        """ set_row_span_column(self, row_span:int) """
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_size_request(self, width, height): # real signature unknown; restored from __doc__
        """ set_size_request(self, width:int, height:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gtk.StateType) """
        pass

    def set_state_flags(self, flags, clear): # real signature unknown; restored from __doc__
        """ set_state_flags(self, flags:Gtk.StateFlags, clear:bool) """
        pass

    def set_style(self, style=None): # real signature unknown; restored from __doc__
        """ set_style(self, style:Gtk.Style=None) """
        pass

    def set_support_multidevice(self, support_multidevice): # real signature unknown; restored from __doc__
        """ set_support_multidevice(self, support_multidevice:bool) """
        pass

    def set_template(self, template_bytes): # real signature unknown; restored from __doc__
        """ set_template(self, template_bytes:GLib.Bytes) """
        pass

    def set_template_from_resource(self, resource_name): # real signature unknown; restored from __doc__
        """ set_template_from_resource(self, resource_name:str) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_tooltip_markup(self, markup=None): # real signature unknown; restored from __doc__
        """ set_tooltip_markup(self, markup:str=None) """
        pass

    def set_tooltip_text(self, text=None): # real signature unknown; restored from __doc__
        """ set_tooltip_text(self, text:str=None) """
        pass

    def set_tooltip_window(self, custom_window=None): # real signature unknown; restored from __doc__
        """ set_tooltip_window(self, custom_window:Gtk.Window=None) """
        pass

    def set_tzid(self, tzid=None): # real signature unknown; restored from __doc__
        """ set_tzid(self, tzid:str=None) """
        pass

    def set_valign(self, align): # real signature unknown; restored from __doc__
        """ set_valign(self, align:Gtk.Align) """
        pass

    def set_vexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_vexpand(self, expand:bool) """
        pass

    def set_vexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_vexpand_set(self, set:bool) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def set_visual(self, visual=None): # real signature unknown; restored from __doc__
        """ set_visual(self, visual:Gdk.Visual=None) """
        pass

    def set_window(self, window): # real signature unknown; restored from __doc__
        """ set_window(self, window:Gdk.Window) """
        pass

    def set_wrap_width(self, width): # real signature unknown; restored from __doc__
        """ set_wrap_width(self, width:int) """
        pass

    def shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ shape_combine_region(self, region:cairo.Region=None) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def show_all(self): # real signature unknown; restored from __doc__
        """ show_all(self) """
        pass

    def show_now(self): # real signature unknown; restored from __doc__
        """ show_now(self) """
        pass

    def size_allocate(self, allocation): # real signature unknown; restored from __doc__
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def size_allocate_with_baseline(self, allocation, baseline): # real signature unknown; restored from __doc__
        """ size_allocate_with_baseline(self, allocation:Gdk.Rectangle, baseline:int) """
        pass

    def size_request(self): # real signature unknown; restored from __doc__
        """ size_request(self) -> requisition:Gtk.Requisition """
        pass

    def start_editing(self, event=None): # real signature unknown; restored from __doc__
        """ start_editing(self, event:Gdk.Event=None) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def style_attach(self): # real signature unknown; restored from __doc__
        """ style_attach(self) """
        pass

    def style_get_property(self, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def thaw_child_notify(self): # real signature unknown; restored from __doc__
        """ thaw_child_notify(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def translate_coordinates(*args, **kwargs): # reliably restored by inspect
        """ translate_coordinates(self, dest_widget:Gtk.Widget, src_x:int, src_y:int) -> bool, dest_x:int, dest_y:int """
        pass

    def trigger_tooltip_query(self): # real signature unknown; restored from __doc__
        """ trigger_tooltip_query(self) """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unrealize(self): # real signature unknown; restored from __doc__
        """ unrealize(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_window(self, window): # real signature unknown; restored from __doc__
        """ unregister_window(self, window:Gdk.Window) """
        pass

    def unset_focus_chain(self): # real signature unknown; restored from __doc__
        """ unset_focus_chain(self) """
        pass

    def unset_state_flags(self, flags): # real signature unknown; restored from __doc__
        """ unset_state_flags(self, flags:Gtk.StateFlags) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __contains__(self, child): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, **properties): # real signature unknown; restored from __doc__
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __nonzero__(self): # reliably restored by inspect
        # no doc
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f73c7431b20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TimezoneMenu), '__module__': 'gi.repository.GWeather', '__gtype__': <GType GWeatherTimezoneMenu (94766763450144)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_tzid': gi.FunctionInfo(get_tzid), 'set_tzid': gi.FunctionInfo(set_tzid), 'parent': <property object at 0x7f73c7b8a0e0>, 'zone': <property object at 0x7f73c7b8a220>})"
    __gdoc__ = "Object GWeatherTimezoneMenu\n\nProperties from GWeatherTimezoneMenu:\n  top -> GWeatherLocation: Top Location\n    The GWeatherLocation whose children will be used to fill in the menu\n  tzid -> gchararray: TZID\n    The selected TZID\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nSignals from GtkComboBox:\n  changed ()\n  move-active (GtkScrollType)\n  popup ()\n  popdown () -> gboolean\n  format-entry-text (gchararray) -> gchararray\n\nProperties from GtkComboBox:\n  model -> GtkTreeModel: ComboBox model\n    The model for the combo box\n  wrap-width -> gint: Wrap width\n    Wrap width for laying out the items in a grid\n  row-span-column -> gint: Row span column\n    TreeModel column containing the row span values\n  column-span-column -> gint: Column span column\n    TreeModel column containing the column span values\n  active -> gint: Active item\n    The item which is currently active\n  add-tearoffs -> gboolean: Add tearoffs to menus\n    Whether dropdowns should have a tearoff menu item\n  tearoff-title -> gchararray: Tearoff Title\n    A title that may be displayed by the window manager when the popup is torn-off\n  has-frame -> gboolean: Has Frame\n    Whether the combo box draws a frame around the child\n  popup-shown -> gboolean: Popup shown\n    Whether the combo's dropdown is shown\n  button-sensitivity -> GtkSensitivityType: Button Sensitivity\n    Whether the dropdown button is sensitive when the model is empty\n  has-entry -> gboolean: Has Entry\n    Whether combo box has an entry\n  entry-text-column -> gint: Entry Text Column\n    The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE\n  popup-fixed-width -> gboolean: Popup Fixed Width\n    Whether the popup's width should be a fixed width matching the allocated width of the combo box\n  id-column -> gint: ID Column\n    The column in the combo box's model that provides string IDs for the values in the model\n  active-id -> gchararray: Active id\n    The value of the id column for the active row\n  cell-area -> GtkCellArea: Cell Area\n    The GtkCellArea used to layout cells\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nSignals from GtkContainer:\n  add (GtkWidget)\n  remove (GtkWidget)\n  check-resize ()\n  set-focus-child (GtkWidget)\n\nProperties from GtkContainer:\n  border-width -> guint: Border width\n    The width of the empty border outside the containers children\n  resize-mode -> GtkResizeMode: Resize mode\n    Specify how resize events are handled\n  child -> GtkWidget: Child\n    Can be used to add a new child to the container\n\nSignals from GtkWidget:\n  composited-changed ()\n  destroy ()\n  show ()\n  hide ()\n  map ()\n  unmap ()\n  realize ()\n  unrealize ()\n  size-allocate (GdkRectangle)\n  state-changed (GtkStateType)\n  state-flags-changed (GtkStateFlags)\n  parent-set (GtkWidget)\n  hierarchy-changed (GtkWidget)\n  style-set (GtkStyle)\n  style-updated ()\n  direction-changed (GtkTextDirection)\n  grab-notify (gboolean)\n  child-notify (GParam)\n  draw (CairoContext) -> gboolean\n  mnemonic-activate (gboolean) -> gboolean\n  grab-focus ()\n  focus (GtkDirectionType) -> gboolean\n  move-focus (GtkDirectionType)\n  keynav-failed (GtkDirectionType) -> gboolean\n  event (GdkEvent) -> gboolean\n  event-after (GdkEvent)\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  touch-event (GdkEvent) -> gboolean\n  scroll-event (GdkEvent) -> gboolean\n  motion-notify-event (GdkEvent) -> gboolean\n  delete-event (GdkEvent) -> gboolean\n  destroy-event (GdkEvent) -> gboolean\n  key-press-event (GdkEvent) -> gboolean\n  key-release-event (GdkEvent) -> gboolean\n  enter-notify-event (GdkEvent) -> gboolean\n  leave-notify-event (GdkEvent) -> gboolean\n  configure-event (GdkEvent) -> gboolean\n  focus-in-event (GdkEvent) -> gboolean\n  focus-out-event (GdkEvent) -> gboolean\n  map-event (GdkEvent) -> gboolean\n  unmap-event (GdkEvent) -> gboolean\n  property-notify-event (GdkEvent) -> gboolean\n  selection-clear-event (GdkEvent) -> gboolean\n  selection-request-event (GdkEvent) -> gboolean\n  selection-notify-event (GdkEvent) -> gboolean\n  selection-received (GtkSelectionData, guint)\n  selection-get (GtkSelectionData, guint, guint)\n  proximity-in-event (GdkEvent) -> gboolean\n  proximity-out-event (GdkEvent) -> gboolean\n  drag-leave (GdkDragContext, guint)\n  drag-begin (GdkDragContext)\n  drag-end (GdkDragContext)\n  drag-data-delete (GdkDragContext)\n  drag-failed (GdkDragContext, GtkDragResult) -> gboolean\n  drag-motion (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-drop (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)\n  drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)\n  visibility-notify-event (GdkEvent) -> gboolean\n  window-state-event (GdkEvent) -> gboolean\n  damage-event (GdkEvent) -> gboolean\n  grab-broken-event (GdkEvent) -> gboolean\n  query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean\n  popup-menu () -> gboolean\n  show-help (GtkWidgetHelpType) -> gboolean\n  accel-closures-changed ()\n  screen-changed (GdkScreen)\n  can-activate-accel (guint) -> gboolean\n\nProperties from GtkWidget:\n  name -> gchararray: Widget name\n    The name of the widget\n  parent -> GtkContainer: Parent widget\n    The parent widget of this widget. Must be a Container widget\n  width-request -> gint: Width request\n    Override for width request of the widget, or -1 if natural request should be used\n  height-request -> gint: Height request\n    Override for height request of the widget, or -1 if natural request should be used\n  visible -> gboolean: Visible\n    Whether the widget is visible\n  sensitive -> gboolean: Sensitive\n    Whether the widget responds to input\n  app-paintable -> gboolean: Application paintable\n    Whether the application will paint directly on the widget\n  can-focus -> gboolean: Can focus\n    Whether the widget can accept the input focus\n  has-focus -> gboolean: Has focus\n    Whether the widget has the input focus\n  is-focus -> gboolean: Is focus\n    Whether the widget is the focus widget within the toplevel\n  focus-on-click -> gboolean: Focus on click\n    Whether the widget should grab focus when it is clicked with the mouse\n  can-default -> gboolean: Can default\n    Whether the widget can be the default widget\n  has-default -> gboolean: Has default\n    Whether the widget is the default widget\n  receives-default -> gboolean: Receives default\n    If TRUE, the widget will receive the default action when it is focused\n  composite-child -> gboolean: Composite child\n    Whether the widget is part of a composite widget\n  style -> GtkStyle: Style\n    The style of the widget, which contains information about how it will look (colors etc)\n  events -> GdkEventMask: Events\n    The event mask that decides what kind of GdkEvents this widget gets\n  no-show-all -> gboolean: No show all\n    Whether gtk_widget_show_all() should not affect this widget\n  has-tooltip -> gboolean: Has tooltip\n    Whether this widget has a tooltip\n  tooltip-markup -> gchararray: Tooltip markup\n    The contents of the tooltip for this widget\n  tooltip-text -> gchararray: Tooltip Text\n    The contents of the tooltip for this widget\n  window -> GdkWindow: Window\n    The widget's window if it is realized\n  opacity -> gdouble: Opacity for Widget\n    The opacity of the widget, from 0 to 1\n  double-buffered -> gboolean: Double Buffered\n    Whether the widget is double buffered\n  halign -> GtkAlign: Horizontal Alignment\n    How to position in extra horizontal space\n  valign -> GtkAlign: Vertical Alignment\n    How to position in extra vertical space\n  margin-left -> gint: Margin on Left\n    Pixels of extra space on the left side\n  margin-right -> gint: Margin on Right\n    Pixels of extra space on the right side\n  margin-start -> gint: Margin on Start\n    Pixels of extra space on the start\n  margin-end -> gint: Margin on End\n    Pixels of extra space on the end\n  margin-top -> gint: Margin on Top\n    Pixels of extra space on the top side\n  margin-bottom -> gint: Margin on Bottom\n    Pixels of extra space on the bottom side\n  margin -> gint: All Margins\n    Pixels of extra space on all four sides\n  hexpand -> gboolean: Horizontal Expand\n    Whether widget wants more horizontal space\n  vexpand -> gboolean: Vertical Expand\n    Whether widget wants more vertical space\n  hexpand-set -> gboolean: Horizontal Expand Set\n    Whether to use the hexpand property\n  vexpand-set -> gboolean: Vertical Expand Set\n    Whether to use the vexpand property\n  expand -> gboolean: Expand Both\n    Whether widget wants to expand in both directions\n  scale-factor -> gint: Scale factor\n    The scaling factor of the window\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GWeatherTimezoneMenu (94766763450144)>'
    __info__ = ObjectInfo(TimezoneMenu)


class TimezoneMenuClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TimezoneMenuClass()
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TimezoneMenuClass), '__module__': 'gi.repository.GWeather', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TimezoneMenuClass' objects>, '__weakref__': <attribute '__weakref__' of 'TimezoneMenuClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f73c7b8a3b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TimezoneMenuClass)


class WindDirection(__gobject.GEnum):
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

    def to_string(self, wind): # real signature unknown; restored from __doc__
        """ to_string(wind:GWeather.WindDirection) -> str """
        return ""

    def to_string_full(self, wind, options): # real signature unknown; restored from __doc__
        """ to_string_full(wind:GWeather.WindDirection, options:GWeather.FormatOptions) -> str """
        return ""

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


    E = 5
    ENE = 4
    ESE = 6
    INVALID = -1
    LAST = 17
    N = 1
    NE = 3
    NNE = 2
    NNW = 16
    NW = 15
    S = 9
    SE = 7
    SSE = 8
    SSW = 10
    SW = 11
    VARIABLE = 0
    W = 13
    WNW = 14
    WSW = 12
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GWeather', '__dict__': <attribute '__dict__' of 'WindDirection' objects>, '__doc__': None, '__gtype__': <GType GWeatherWindDirection (94766763448096)>, '__enum_values__': {-1: <enum GWEATHER_WIND_INVALID of type GWeather.WindDirection>, 0: <enum GWEATHER_WIND_VARIABLE of type GWeather.WindDirection>, 1: <enum GWEATHER_WIND_N of type GWeather.WindDirection>, 2: <enum GWEATHER_WIND_NNE of type GWeather.WindDirection>, 3: <enum GWEATHER_WIND_NE of type GWeather.WindDirection>, 4: <enum GWEATHER_WIND_ENE of type GWeather.WindDirection>, 5: <enum GWEATHER_WIND_E of type GWeather.WindDirection>, 6: <enum GWEATHER_WIND_ESE of type GWeather.WindDirection>, 7: <enum GWEATHER_WIND_SE of type GWeather.WindDirection>, 8: <enum GWEATHER_WIND_SSE of type GWeather.WindDirection>, 9: <enum GWEATHER_WIND_S of type GWeather.WindDirection>, 10: <enum GWEATHER_WIND_SSW of type GWeather.WindDirection>, 11: <enum GWEATHER_WIND_SW of type GWeather.WindDirection>, 12: <enum GWEATHER_WIND_WSW of type GWeather.WindDirection>, 13: <enum GWEATHER_WIND_W of type GWeather.WindDirection>, 14: <enum GWEATHER_WIND_WNW of type GWeather.WindDirection>, 15: <enum GWEATHER_WIND_NW of type GWeather.WindDirection>, 16: <enum GWEATHER_WIND_NNW of type GWeather.WindDirection>, 17: <enum GWEATHER_WIND_LAST of type GWeather.WindDirection>}, '__info__': gi.EnumInfo(WindDirection), 'INVALID': <enum GWEATHER_WIND_INVALID of type GWeather.WindDirection>, 'VARIABLE': <enum GWEATHER_WIND_VARIABLE of type GWeather.WindDirection>, 'N': <enum GWEATHER_WIND_N of type GWeather.WindDirection>, 'NNE': <enum GWEATHER_WIND_NNE of type GWeather.WindDirection>, 'NE': <enum GWEATHER_WIND_NE of type GWeather.WindDirection>, 'ENE': <enum GWEATHER_WIND_ENE of type GWeather.WindDirection>, 'E': <enum GWEATHER_WIND_E of type GWeather.WindDirection>, 'ESE': <enum GWEATHER_WIND_ESE of type GWeather.WindDirection>, 'SE': <enum GWEATHER_WIND_SE of type GWeather.WindDirection>, 'SSE': <enum GWEATHER_WIND_SSE of type GWeather.WindDirection>, 'S': <enum GWEATHER_WIND_S of type GWeather.WindDirection>, 'SSW': <enum GWEATHER_WIND_SSW of type GWeather.WindDirection>, 'SW': <enum GWEATHER_WIND_SW of type GWeather.WindDirection>, 'WSW': <enum GWEATHER_WIND_WSW of type GWeather.WindDirection>, 'W': <enum GWEATHER_WIND_W of type GWeather.WindDirection>, 'WNW': <enum GWEATHER_WIND_WNW of type GWeather.WindDirection>, 'NW': <enum GWEATHER_WIND_NW of type GWeather.WindDirection>, 'NNW': <enum GWEATHER_WIND_NNW of type GWeather.WindDirection>, 'LAST': <enum GWEATHER_WIND_LAST of type GWeather.WindDirection>, 'to_string': gi.FunctionInfo(to_string), 'to_string_full': gi.FunctionInfo(to_string_full)})"
    __enum_values__ = {
        -1: -1,
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
    __gtype__ = None # (!) real value is '<GType GWeatherWindDirection (94766763448096)>'
    __info__ = gi.EnumInfo(WindDirection)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f73c8fb31f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f73c8fb3280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f73c8fb3310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f73c8fb33a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f73c9befd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GWeather-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GWeather', loader=<gi.importer.DynamicImporter object at 0x7f73c9befd00>)"

