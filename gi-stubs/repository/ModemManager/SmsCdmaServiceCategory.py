# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class SmsCdmaServiceCategory(__gobject.GEnum):
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

    def get_string(self, val): # real signature unknown; restored from __doc__
        """ get_string(val:ModemManager.SmsCdmaServiceCategory) -> str """
        return ""

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


    ADMINISTRATIVE = 2
    ADVERTISEMENTS = 26
    BUSINESS_NEWS_INTERNATIONAL = 11
    BUSINESS_NEWS_LOCAL = 8
    BUSINESS_NEWS_NATIONAL = 10
    BUSINESS_NEWS_REGIONAL = 9
    CMAS_CHILD_ABDUCTION_EMERGENCY = 4099
    CMAS_EXTREME_THREAT = 4097
    CMAS_PRESIDENTIAL_ALERT = 4096
    CMAS_SEVERE_THREAT = 4098
    CMAS_TEST = 4100
    EMERGENCY_BROADCAST = 1
    EMPLOYMENT = 28
    ENTERTAINMENT_NEWS_INTERNATIONAL = 19
    ENTERTAINMENT_NEWS_LOCAL = 16
    ENTERTAINMENT_NEWS_NATIONAL = 18
    ENTERTAINMENT_NEWS_REGIONAL = 17
    FLIGHT_SCHEDULES = 22
    GENERAL_NEWS_INTERNATIONAL = 7
    GENERAL_NEWS_LOCAL = 4
    GENERAL_NEWS_NATIONAL = 6
    GENERAL_NEWS_REGIONAL = 5
    HOSPITALS = 29
    LOCAL_WEATHER = 20
    LODGINGS = 24
    MAINTENANCE = 3
    MULTICATEGORY = 31
    RESTAURANTS = 23
    RETAIL_DIRECTORY = 25
    SPORTS_NEWS_INTERNATIONAL = 15
    SPORTS_NEWS_LOCAL = 12
    SPORTS_NEWS_NATIONAL = 14
    SPORTS_NEWS_REGIONAL = 13
    STOCK_QUOTES = 27
    TECHNOLOGY_NEWS = 30
    TRAFFIC_REPORT = 21
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ModemManager', '__dict__': <attribute '__dict__' of 'SmsCdmaServiceCategory' objects>, '__doc__': None, '__gtype__': <GType MMSmsCdmaServiceCategory (94631948884848)>, '__enum_values__': {0: <enum MM_SMS_CDMA_SERVICE_CATEGORY_UNKNOWN of type ModemManager.SmsCdmaServiceCategory>, 1: <enum MM_SMS_CDMA_SERVICE_CATEGORY_EMERGENCY_BROADCAST of type ModemManager.SmsCdmaServiceCategory>, 2: <enum MM_SMS_CDMA_SERVICE_CATEGORY_ADMINISTRATIVE of type ModemManager.SmsCdmaServiceCategory>, 3: <enum MM_SMS_CDMA_SERVICE_CATEGORY_MAINTENANCE of type ModemManager.SmsCdmaServiceCategory>, 4: <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 5: <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 6: <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 7: <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 8: <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 9: <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 10: <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 11: <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 12: <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 13: <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 14: <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 15: <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 16: <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 17: <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 18: <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 19: <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 20: <enum MM_SMS_CDMA_SERVICE_CATEGORY_LOCAL_WEATHER of type ModemManager.SmsCdmaServiceCategory>, 21: <enum MM_SMS_CDMA_SERVICE_CATEGORY_TRAFFIC_REPORT of type ModemManager.SmsCdmaServiceCategory>, 22: <enum MM_SMS_CDMA_SERVICE_CATEGORY_FLIGHT_SCHEDULES of type ModemManager.SmsCdmaServiceCategory>, 23: <enum MM_SMS_CDMA_SERVICE_CATEGORY_RESTAURANTS of type ModemManager.SmsCdmaServiceCategory>, 24: <enum MM_SMS_CDMA_SERVICE_CATEGORY_LODGINGS of type ModemManager.SmsCdmaServiceCategory>, 25: <enum MM_SMS_CDMA_SERVICE_CATEGORY_RETAIL_DIRECTORY of type ModemManager.SmsCdmaServiceCategory>, 26: <enum MM_SMS_CDMA_SERVICE_CATEGORY_ADVERTISEMENTS of type ModemManager.SmsCdmaServiceCategory>, 27: <enum MM_SMS_CDMA_SERVICE_CATEGORY_STOCK_QUOTES of type ModemManager.SmsCdmaServiceCategory>, 28: <enum MM_SMS_CDMA_SERVICE_CATEGORY_EMPLOYMENT of type ModemManager.SmsCdmaServiceCategory>, 29: <enum MM_SMS_CDMA_SERVICE_CATEGORY_HOSPITALS of type ModemManager.SmsCdmaServiceCategory>, 30: <enum MM_SMS_CDMA_SERVICE_CATEGORY_TECHNOLOGY_NEWS of type ModemManager.SmsCdmaServiceCategory>, 31: <enum MM_SMS_CDMA_SERVICE_CATEGORY_MULTICATEGORY of type ModemManager.SmsCdmaServiceCategory>, 4096: <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_PRESIDENTIAL_ALERT of type ModemManager.SmsCdmaServiceCategory>, 4097: <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_EXTREME_THREAT of type ModemManager.SmsCdmaServiceCategory>, 4098: <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_SEVERE_THREAT of type ModemManager.SmsCdmaServiceCategory>, 4099: <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_CHILD_ABDUCTION_EMERGENCY of type ModemManager.SmsCdmaServiceCategory>, 4100: <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_TEST of type ModemManager.SmsCdmaServiceCategory>}, '__info__': gi.EnumInfo(SmsCdmaServiceCategory), 'UNKNOWN': <enum MM_SMS_CDMA_SERVICE_CATEGORY_UNKNOWN of type ModemManager.SmsCdmaServiceCategory>, 'EMERGENCY_BROADCAST': <enum MM_SMS_CDMA_SERVICE_CATEGORY_EMERGENCY_BROADCAST of type ModemManager.SmsCdmaServiceCategory>, 'ADMINISTRATIVE': <enum MM_SMS_CDMA_SERVICE_CATEGORY_ADMINISTRATIVE of type ModemManager.SmsCdmaServiceCategory>, 'MAINTENANCE': <enum MM_SMS_CDMA_SERVICE_CATEGORY_MAINTENANCE of type ModemManager.SmsCdmaServiceCategory>, 'GENERAL_NEWS_LOCAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 'GENERAL_NEWS_REGIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 'GENERAL_NEWS_NATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'GENERAL_NEWS_INTERNATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_GENERAL_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'BUSINESS_NEWS_LOCAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 'BUSINESS_NEWS_REGIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 'BUSINESS_NEWS_NATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'BUSINESS_NEWS_INTERNATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_BUSINESS_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'SPORTS_NEWS_LOCAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 'SPORTS_NEWS_REGIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 'SPORTS_NEWS_NATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'SPORTS_NEWS_INTERNATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_SPORTS_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'ENTERTAINMENT_NEWS_LOCAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_LOCAL of type ModemManager.SmsCdmaServiceCategory>, 'ENTERTAINMENT_NEWS_REGIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_REGIONAL of type ModemManager.SmsCdmaServiceCategory>, 'ENTERTAINMENT_NEWS_NATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_NATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'ENTERTAINMENT_NEWS_INTERNATIONAL': <enum MM_SMS_CDMA_SERVICE_CATEGORY_ENTERTAINMENT_NEWS_INTERNATIONAL of type ModemManager.SmsCdmaServiceCategory>, 'LOCAL_WEATHER': <enum MM_SMS_CDMA_SERVICE_CATEGORY_LOCAL_WEATHER of type ModemManager.SmsCdmaServiceCategory>, 'TRAFFIC_REPORT': <enum MM_SMS_CDMA_SERVICE_CATEGORY_TRAFFIC_REPORT of type ModemManager.SmsCdmaServiceCategory>, 'FLIGHT_SCHEDULES': <enum MM_SMS_CDMA_SERVICE_CATEGORY_FLIGHT_SCHEDULES of type ModemManager.SmsCdmaServiceCategory>, 'RESTAURANTS': <enum MM_SMS_CDMA_SERVICE_CATEGORY_RESTAURANTS of type ModemManager.SmsCdmaServiceCategory>, 'LODGINGS': <enum MM_SMS_CDMA_SERVICE_CATEGORY_LODGINGS of type ModemManager.SmsCdmaServiceCategory>, 'RETAIL_DIRECTORY': <enum MM_SMS_CDMA_SERVICE_CATEGORY_RETAIL_DIRECTORY of type ModemManager.SmsCdmaServiceCategory>, 'ADVERTISEMENTS': <enum MM_SMS_CDMA_SERVICE_CATEGORY_ADVERTISEMENTS of type ModemManager.SmsCdmaServiceCategory>, 'STOCK_QUOTES': <enum MM_SMS_CDMA_SERVICE_CATEGORY_STOCK_QUOTES of type ModemManager.SmsCdmaServiceCategory>, 'EMPLOYMENT': <enum MM_SMS_CDMA_SERVICE_CATEGORY_EMPLOYMENT of type ModemManager.SmsCdmaServiceCategory>, 'HOSPITALS': <enum MM_SMS_CDMA_SERVICE_CATEGORY_HOSPITALS of type ModemManager.SmsCdmaServiceCategory>, 'TECHNOLOGY_NEWS': <enum MM_SMS_CDMA_SERVICE_CATEGORY_TECHNOLOGY_NEWS of type ModemManager.SmsCdmaServiceCategory>, 'MULTICATEGORY': <enum MM_SMS_CDMA_SERVICE_CATEGORY_MULTICATEGORY of type ModemManager.SmsCdmaServiceCategory>, 'CMAS_PRESIDENTIAL_ALERT': <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_PRESIDENTIAL_ALERT of type ModemManager.SmsCdmaServiceCategory>, 'CMAS_EXTREME_THREAT': <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_EXTREME_THREAT of type ModemManager.SmsCdmaServiceCategory>, 'CMAS_SEVERE_THREAT': <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_SEVERE_THREAT of type ModemManager.SmsCdmaServiceCategory>, 'CMAS_CHILD_ABDUCTION_EMERGENCY': <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_CHILD_ABDUCTION_EMERGENCY of type ModemManager.SmsCdmaServiceCategory>, 'CMAS_TEST': <enum MM_SMS_CDMA_SERVICE_CATEGORY_CMAS_TEST of type ModemManager.SmsCdmaServiceCategory>, 'get_string': gi.FunctionInfo(get_string)})"
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
        4096: 4096,
        4097: 4097,
        4098: 4098,
        4099: 4099,
        4100: 4100,
    }
    __gtype__ = None # (!) real value is '<GType MMSmsCdmaServiceCategory (94631948884848)>'
    __info__ = gi.EnumInfo(SmsCdmaServiceCategory)


