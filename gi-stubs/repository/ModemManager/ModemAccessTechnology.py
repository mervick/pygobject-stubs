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


class ModemAccessTechnology(__gobject.GFlags):
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

    def build_string_from_mask(self, mask): # real signature unknown; restored from __doc__
        """ build_string_from_mask(mask:ModemManager.ModemAccessTechnology) -> str """
        return ""

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


    1XRTT = 1024
    ANY = 4294967295
    EDGE = 16
    EVDO0 = 2048
    EVDOA = 4096
    EVDOB = 8192
    GPRS = 8
    GSM = 2
    GSM_COMPACT = 4
    HSDPA = 64
    HSPA = 256
    HSPA_PLUS = 512
    HSUPA = 128
    LTE = 16384
    POTS = 1
    UMTS = 32
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ModemManager', '__dict__': <attribute '__dict__' of 'ModemAccessTechnology' objects>, '__doc__': None, '__gtype__': <GType MMModemAccessTechnology (94631948705728)>, '__flags_values__': {0: <flags 0 of type ModemManager.ModemAccessTechnology>, 1: <flags MM_MODEM_ACCESS_TECHNOLOGY_POTS of type ModemManager.ModemAccessTechnology>, 2: <flags MM_MODEM_ACCESS_TECHNOLOGY_GSM of type ModemManager.ModemAccessTechnology>, 4: <flags MM_MODEM_ACCESS_TECHNOLOGY_GSM_COMPACT of type ModemManager.ModemAccessTechnology>, 8: <flags MM_MODEM_ACCESS_TECHNOLOGY_GPRS of type ModemManager.ModemAccessTechnology>, 16: <flags MM_MODEM_ACCESS_TECHNOLOGY_EDGE of type ModemManager.ModemAccessTechnology>, 32: <flags MM_MODEM_ACCESS_TECHNOLOGY_UMTS of type ModemManager.ModemAccessTechnology>, 64: <flags MM_MODEM_ACCESS_TECHNOLOGY_HSDPA of type ModemManager.ModemAccessTechnology>, 128: <flags MM_MODEM_ACCESS_TECHNOLOGY_HSUPA of type ModemManager.ModemAccessTechnology>, 256: <flags MM_MODEM_ACCESS_TECHNOLOGY_HSPA of type ModemManager.ModemAccessTechnology>, 512: <flags MM_MODEM_ACCESS_TECHNOLOGY_HSPA_PLUS of type ModemManager.ModemAccessTechnology>, 1024: <flags MM_MODEM_ACCESS_TECHNOLOGY_1XRTT of type ModemManager.ModemAccessTechnology>, 2048: <flags MM_MODEM_ACCESS_TECHNOLOGY_EVDO0 of type ModemManager.ModemAccessTechnology>, 4096: <flags MM_MODEM_ACCESS_TECHNOLOGY_EVDOA of type ModemManager.ModemAccessTechnology>, 8192: <flags MM_MODEM_ACCESS_TECHNOLOGY_EVDOB of type ModemManager.ModemAccessTechnology>, 16384: <flags MM_MODEM_ACCESS_TECHNOLOGY_LTE of type ModemManager.ModemAccessTechnology>, 4294967295: <flags MM_MODEM_ACCESS_TECHNOLOGY_POTS | MM_MODEM_ACCESS_TECHNOLOGY_GSM | MM_MODEM_ACCESS_TECHNOLOGY_GSM_COMPACT | MM_MODEM_ACCESS_TECHNOLOGY_GPRS | MM_MODEM_ACCESS_TECHNOLOGY_EDGE | MM_MODEM_ACCESS_TECHNOLOGY_UMTS | MM_MODEM_ACCESS_TECHNOLOGY_HSDPA | MM_MODEM_ACCESS_TECHNOLOGY_HSUPA | MM_MODEM_ACCESS_TECHNOLOGY_HSPA | MM_MODEM_ACCESS_TECHNOLOGY_HSPA_PLUS | MM_MODEM_ACCESS_TECHNOLOGY_1XRTT | MM_MODEM_ACCESS_TECHNOLOGY_EVDO0 | MM_MODEM_ACCESS_TECHNOLOGY_EVDOA | MM_MODEM_ACCESS_TECHNOLOGY_EVDOB | MM_MODEM_ACCESS_TECHNOLOGY_LTE | MM_MODEM_ACCESS_TECHNOLOGY_ANY of type ModemManager.ModemAccessTechnology>}, '__info__': gi.EnumInfo(ModemAccessTechnology), 'UNKNOWN': <flags 0 of type ModemManager.ModemAccessTechnology>, 'POTS': <flags MM_MODEM_ACCESS_TECHNOLOGY_POTS of type ModemManager.ModemAccessTechnology>, 'GSM': <flags MM_MODEM_ACCESS_TECHNOLOGY_GSM of type ModemManager.ModemAccessTechnology>, 'GSM_COMPACT': <flags MM_MODEM_ACCESS_TECHNOLOGY_GSM_COMPACT of type ModemManager.ModemAccessTechnology>, 'GPRS': <flags MM_MODEM_ACCESS_TECHNOLOGY_GPRS of type ModemManager.ModemAccessTechnology>, 'EDGE': <flags MM_MODEM_ACCESS_TECHNOLOGY_EDGE of type ModemManager.ModemAccessTechnology>, 'UMTS': <flags MM_MODEM_ACCESS_TECHNOLOGY_UMTS of type ModemManager.ModemAccessTechnology>, 'HSDPA': <flags MM_MODEM_ACCESS_TECHNOLOGY_HSDPA of type ModemManager.ModemAccessTechnology>, 'HSUPA': <flags MM_MODEM_ACCESS_TECHNOLOGY_HSUPA of type ModemManager.ModemAccessTechnology>, 'HSPA': <flags MM_MODEM_ACCESS_TECHNOLOGY_HSPA of type ModemManager.ModemAccessTechnology>, 'HSPA_PLUS': <flags MM_MODEM_ACCESS_TECHNOLOGY_HSPA_PLUS of type ModemManager.ModemAccessTechnology>, '1XRTT': <flags MM_MODEM_ACCESS_TECHNOLOGY_1XRTT of type ModemManager.ModemAccessTechnology>, 'EVDO0': <flags MM_MODEM_ACCESS_TECHNOLOGY_EVDO0 of type ModemManager.ModemAccessTechnology>, 'EVDOA': <flags MM_MODEM_ACCESS_TECHNOLOGY_EVDOA of type ModemManager.ModemAccessTechnology>, 'EVDOB': <flags MM_MODEM_ACCESS_TECHNOLOGY_EVDOB of type ModemManager.ModemAccessTechnology>, 'LTE': <flags MM_MODEM_ACCESS_TECHNOLOGY_LTE of type ModemManager.ModemAccessTechnology>, 'ANY': <flags MM_MODEM_ACCESS_TECHNOLOGY_POTS | MM_MODEM_ACCESS_TECHNOLOGY_GSM | MM_MODEM_ACCESS_TECHNOLOGY_GSM_COMPACT | MM_MODEM_ACCESS_TECHNOLOGY_GPRS | MM_MODEM_ACCESS_TECHNOLOGY_EDGE | MM_MODEM_ACCESS_TECHNOLOGY_UMTS | MM_MODEM_ACCESS_TECHNOLOGY_HSDPA | MM_MODEM_ACCESS_TECHNOLOGY_HSUPA | MM_MODEM_ACCESS_TECHNOLOGY_HSPA | MM_MODEM_ACCESS_TECHNOLOGY_HSPA_PLUS | MM_MODEM_ACCESS_TECHNOLOGY_1XRTT | MM_MODEM_ACCESS_TECHNOLOGY_EVDO0 | MM_MODEM_ACCESS_TECHNOLOGY_EVDOA | MM_MODEM_ACCESS_TECHNOLOGY_EVDOB | MM_MODEM_ACCESS_TECHNOLOGY_LTE | MM_MODEM_ACCESS_TECHNOLOGY_ANY of type ModemManager.ModemAccessTechnology>, 'build_string_from_mask': gi.FunctionInfo(build_string_from_mask)})"
    __flags_values__ = {
        0: 0,
        1: 1,
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
        4294967295: 4294967295,
    }
    __gtype__ = None # (!) real value is '<GType MMModemAccessTechnology (94631948705728)>'
    __info__ = gi.EnumInfo(ModemAccessTechnology)


