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


class ModemBand(__gobject.GEnum):
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
        """ get_string(val:ModemManager.ModemBand) -> str """
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


    ANY = 256
    CDMA_BC0 = 128
    CDMA_BC1 = 129
    CDMA_BC10 = 139
    CDMA_BC11 = 140
    CDMA_BC12 = 141
    CDMA_BC13 = 142
    CDMA_BC14 = 143
    CDMA_BC15 = 144
    CDMA_BC16 = 145
    CDMA_BC17 = 146
    CDMA_BC18 = 147
    CDMA_BC19 = 148
    CDMA_BC2 = 130
    CDMA_BC3 = 131
    CDMA_BC4 = 132
    CDMA_BC5 = 134
    CDMA_BC6 = 135
    CDMA_BC7 = 136
    CDMA_BC8 = 137
    CDMA_BC9 = 138
    DCS = 2
    EGSM = 1
    EUTRAN_1 = 31
    EUTRAN_10 = 40
    EUTRAN_11 = 41
    EUTRAN_12 = 42
    EUTRAN_13 = 43
    EUTRAN_14 = 44
    EUTRAN_17 = 47
    EUTRAN_18 = 48
    EUTRAN_19 = 49
    EUTRAN_2 = 32
    EUTRAN_20 = 50
    EUTRAN_21 = 51
    EUTRAN_22 = 52
    EUTRAN_23 = 53
    EUTRAN_24 = 54
    EUTRAN_25 = 55
    EUTRAN_26 = 56
    EUTRAN_27 = 57
    EUTRAN_28 = 58
    EUTRAN_29 = 59
    EUTRAN_3 = 33
    EUTRAN_30 = 60
    EUTRAN_31 = 61
    EUTRAN_32 = 62
    EUTRAN_33 = 63
    EUTRAN_34 = 64
    EUTRAN_35 = 65
    EUTRAN_36 = 66
    EUTRAN_37 = 67
    EUTRAN_38 = 68
    EUTRAN_39 = 69
    EUTRAN_4 = 34
    EUTRAN_40 = 70
    EUTRAN_41 = 71
    EUTRAN_42 = 72
    EUTRAN_43 = 73
    EUTRAN_44 = 74
    EUTRAN_45 = 75
    EUTRAN_46 = 76
    EUTRAN_47 = 77
    EUTRAN_48 = 78
    EUTRAN_49 = 79
    EUTRAN_5 = 35
    EUTRAN_50 = 80
    EUTRAN_51 = 81
    EUTRAN_52 = 82
    EUTRAN_53 = 83
    EUTRAN_54 = 84
    EUTRAN_55 = 85
    EUTRAN_56 = 86
    EUTRAN_57 = 87
    EUTRAN_58 = 88
    EUTRAN_59 = 89
    EUTRAN_6 = 36
    EUTRAN_60 = 90
    EUTRAN_61 = 91
    EUTRAN_62 = 92
    EUTRAN_63 = 93
    EUTRAN_64 = 94
    EUTRAN_65 = 95
    EUTRAN_66 = 96
    EUTRAN_67 = 97
    EUTRAN_68 = 98
    EUTRAN_69 = 99
    EUTRAN_7 = 37
    EUTRAN_70 = 100
    EUTRAN_71 = 101
    EUTRAN_8 = 38
    EUTRAN_9 = 39
    G380 = 17
    G410 = 18
    G450 = 14
    G480 = 15
    G710 = 19
    G750 = 16
    G810 = 20
    G850 = 4
    PCS = 3
    UNKNOWN = 0
    UTRAN_1 = 5
    UTRAN_10 = 210
    UTRAN_11 = 211
    UTRAN_12 = 212
    UTRAN_13 = 213
    UTRAN_14 = 214
    UTRAN_19 = 219
    UTRAN_2 = 12
    UTRAN_20 = 220
    UTRAN_21 = 221
    UTRAN_22 = 222
    UTRAN_25 = 225
    UTRAN_26 = 226
    UTRAN_3 = 6
    UTRAN_32 = 232
    UTRAN_4 = 7
    UTRAN_5 = 9
    UTRAN_6 = 8
    UTRAN_7 = 13
    UTRAN_8 = 10
    UTRAN_9 = 11
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ModemManager', '__dict__': <attribute '__dict__' of 'ModemBand' objects>, '__doc__': None, '__gtype__': <GType MMModemBand (94631948708176)>, '__enum_values__': {0: <enum MM_MODEM_BAND_UNKNOWN of type ModemManager.ModemBand>, 1: <enum MM_MODEM_BAND_EGSM of type ModemManager.ModemBand>, 2: <enum MM_MODEM_BAND_DCS of type ModemManager.ModemBand>, 3: <enum MM_MODEM_BAND_PCS of type ModemManager.ModemBand>, 4: <enum MM_MODEM_BAND_G850 of type ModemManager.ModemBand>, 5: <enum MM_MODEM_BAND_UTRAN_1 of type ModemManager.ModemBand>, 6: <enum MM_MODEM_BAND_UTRAN_3 of type ModemManager.ModemBand>, 7: <enum MM_MODEM_BAND_UTRAN_4 of type ModemManager.ModemBand>, 8: <enum MM_MODEM_BAND_UTRAN_6 of type ModemManager.ModemBand>, 9: <enum MM_MODEM_BAND_UTRAN_5 of type ModemManager.ModemBand>, 10: <enum MM_MODEM_BAND_UTRAN_8 of type ModemManager.ModemBand>, 11: <enum MM_MODEM_BAND_UTRAN_9 of type ModemManager.ModemBand>, 12: <enum MM_MODEM_BAND_UTRAN_2 of type ModemManager.ModemBand>, 13: <enum MM_MODEM_BAND_UTRAN_7 of type ModemManager.ModemBand>, 14: <enum MM_MODEM_BAND_G450 of type ModemManager.ModemBand>, 15: <enum MM_MODEM_BAND_G480 of type ModemManager.ModemBand>, 16: <enum MM_MODEM_BAND_G750 of type ModemManager.ModemBand>, 17: <enum MM_MODEM_BAND_G380 of type ModemManager.ModemBand>, 18: <enum MM_MODEM_BAND_G410 of type ModemManager.ModemBand>, 19: <enum MM_MODEM_BAND_G710 of type ModemManager.ModemBand>, 20: <enum MM_MODEM_BAND_G810 of type ModemManager.ModemBand>, 31: <enum MM_MODEM_BAND_EUTRAN_1 of type ModemManager.ModemBand>, 32: <enum MM_MODEM_BAND_EUTRAN_2 of type ModemManager.ModemBand>, 33: <enum MM_MODEM_BAND_EUTRAN_3 of type ModemManager.ModemBand>, 34: <enum MM_MODEM_BAND_EUTRAN_4 of type ModemManager.ModemBand>, 35: <enum MM_MODEM_BAND_EUTRAN_5 of type ModemManager.ModemBand>, 36: <enum MM_MODEM_BAND_EUTRAN_6 of type ModemManager.ModemBand>, 37: <enum MM_MODEM_BAND_EUTRAN_7 of type ModemManager.ModemBand>, 38: <enum MM_MODEM_BAND_EUTRAN_8 of type ModemManager.ModemBand>, 39: <enum MM_MODEM_BAND_EUTRAN_9 of type ModemManager.ModemBand>, 40: <enum MM_MODEM_BAND_EUTRAN_10 of type ModemManager.ModemBand>, 41: <enum MM_MODEM_BAND_EUTRAN_11 of type ModemManager.ModemBand>, 42: <enum MM_MODEM_BAND_EUTRAN_12 of type ModemManager.ModemBand>, 43: <enum MM_MODEM_BAND_EUTRAN_13 of type ModemManager.ModemBand>, 44: <enum MM_MODEM_BAND_EUTRAN_14 of type ModemManager.ModemBand>, 47: <enum MM_MODEM_BAND_EUTRAN_17 of type ModemManager.ModemBand>, 48: <enum MM_MODEM_BAND_EUTRAN_18 of type ModemManager.ModemBand>, 49: <enum MM_MODEM_BAND_EUTRAN_19 of type ModemManager.ModemBand>, 50: <enum MM_MODEM_BAND_EUTRAN_20 of type ModemManager.ModemBand>, 51: <enum MM_MODEM_BAND_EUTRAN_21 of type ModemManager.ModemBand>, 52: <enum MM_MODEM_BAND_EUTRAN_22 of type ModemManager.ModemBand>, 53: <enum MM_MODEM_BAND_EUTRAN_23 of type ModemManager.ModemBand>, 54: <enum MM_MODEM_BAND_EUTRAN_24 of type ModemManager.ModemBand>, 55: <enum MM_MODEM_BAND_EUTRAN_25 of type ModemManager.ModemBand>, 56: <enum MM_MODEM_BAND_EUTRAN_26 of type ModemManager.ModemBand>, 57: <enum MM_MODEM_BAND_EUTRAN_27 of type ModemManager.ModemBand>, 58: <enum MM_MODEM_BAND_EUTRAN_28 of type ModemManager.ModemBand>, 59: <enum MM_MODEM_BAND_EUTRAN_29 of type ModemManager.ModemBand>, 60: <enum MM_MODEM_BAND_EUTRAN_30 of type ModemManager.ModemBand>, 61: <enum MM_MODEM_BAND_EUTRAN_31 of type ModemManager.ModemBand>, 62: <enum MM_MODEM_BAND_EUTRAN_32 of type ModemManager.ModemBand>, 63: <enum MM_MODEM_BAND_EUTRAN_33 of type ModemManager.ModemBand>, 64: <enum MM_MODEM_BAND_EUTRAN_34 of type ModemManager.ModemBand>, 65: <enum MM_MODEM_BAND_EUTRAN_35 of type ModemManager.ModemBand>, 66: <enum MM_MODEM_BAND_EUTRAN_36 of type ModemManager.ModemBand>, 67: <enum MM_MODEM_BAND_EUTRAN_37 of type ModemManager.ModemBand>, 68: <enum MM_MODEM_BAND_EUTRAN_38 of type ModemManager.ModemBand>, 69: <enum MM_MODEM_BAND_EUTRAN_39 of type ModemManager.ModemBand>, 70: <enum MM_MODEM_BAND_EUTRAN_40 of type ModemManager.ModemBand>, 71: <enum MM_MODEM_BAND_EUTRAN_41 of type ModemManager.ModemBand>, 72: <enum MM_MODEM_BAND_EUTRAN_42 of type ModemManager.ModemBand>, 73: <enum MM_MODEM_BAND_EUTRAN_43 of type ModemManager.ModemBand>, 74: <enum MM_MODEM_BAND_EUTRAN_44 of type ModemManager.ModemBand>, 75: <enum MM_MODEM_BAND_EUTRAN_45 of type ModemManager.ModemBand>, 76: <enum MM_MODEM_BAND_EUTRAN_46 of type ModemManager.ModemBand>, 77: <enum MM_MODEM_BAND_EUTRAN_47 of type ModemManager.ModemBand>, 78: <enum MM_MODEM_BAND_EUTRAN_48 of type ModemManager.ModemBand>, 79: <enum MM_MODEM_BAND_EUTRAN_49 of type ModemManager.ModemBand>, 80: <enum MM_MODEM_BAND_EUTRAN_50 of type ModemManager.ModemBand>, 81: <enum MM_MODEM_BAND_EUTRAN_51 of type ModemManager.ModemBand>, 82: <enum MM_MODEM_BAND_EUTRAN_52 of type ModemManager.ModemBand>, 83: <enum MM_MODEM_BAND_EUTRAN_53 of type ModemManager.ModemBand>, 84: <enum MM_MODEM_BAND_EUTRAN_54 of type ModemManager.ModemBand>, 85: <enum MM_MODEM_BAND_EUTRAN_55 of type ModemManager.ModemBand>, 86: <enum MM_MODEM_BAND_EUTRAN_56 of type ModemManager.ModemBand>, 87: <enum MM_MODEM_BAND_EUTRAN_57 of type ModemManager.ModemBand>, 88: <enum MM_MODEM_BAND_EUTRAN_58 of type ModemManager.ModemBand>, 89: <enum MM_MODEM_BAND_EUTRAN_59 of type ModemManager.ModemBand>, 90: <enum MM_MODEM_BAND_EUTRAN_60 of type ModemManager.ModemBand>, 91: <enum MM_MODEM_BAND_EUTRAN_61 of type ModemManager.ModemBand>, 92: <enum MM_MODEM_BAND_EUTRAN_62 of type ModemManager.ModemBand>, 93: <enum MM_MODEM_BAND_EUTRAN_63 of type ModemManager.ModemBand>, 94: <enum MM_MODEM_BAND_EUTRAN_64 of type ModemManager.ModemBand>, 95: <enum MM_MODEM_BAND_EUTRAN_65 of type ModemManager.ModemBand>, 96: <enum MM_MODEM_BAND_EUTRAN_66 of type ModemManager.ModemBand>, 97: <enum MM_MODEM_BAND_EUTRAN_67 of type ModemManager.ModemBand>, 98: <enum MM_MODEM_BAND_EUTRAN_68 of type ModemManager.ModemBand>, 99: <enum MM_MODEM_BAND_EUTRAN_69 of type ModemManager.ModemBand>, 100: <enum MM_MODEM_BAND_EUTRAN_70 of type ModemManager.ModemBand>, 101: <enum MM_MODEM_BAND_EUTRAN_71 of type ModemManager.ModemBand>, 128: <enum MM_MODEM_BAND_CDMA_BC0 of type ModemManager.ModemBand>, 129: <enum MM_MODEM_BAND_CDMA_BC1 of type ModemManager.ModemBand>, 130: <enum MM_MODEM_BAND_CDMA_BC2 of type ModemManager.ModemBand>, 131: <enum MM_MODEM_BAND_CDMA_BC3 of type ModemManager.ModemBand>, 132: <enum MM_MODEM_BAND_CDMA_BC4 of type ModemManager.ModemBand>, 134: <enum MM_MODEM_BAND_CDMA_BC5 of type ModemManager.ModemBand>, 135: <enum MM_MODEM_BAND_CDMA_BC6 of type ModemManager.ModemBand>, 136: <enum MM_MODEM_BAND_CDMA_BC7 of type ModemManager.ModemBand>, 137: <enum MM_MODEM_BAND_CDMA_BC8 of type ModemManager.ModemBand>, 138: <enum MM_MODEM_BAND_CDMA_BC9 of type ModemManager.ModemBand>, 139: <enum MM_MODEM_BAND_CDMA_BC10 of type ModemManager.ModemBand>, 140: <enum MM_MODEM_BAND_CDMA_BC11 of type ModemManager.ModemBand>, 141: <enum MM_MODEM_BAND_CDMA_BC12 of type ModemManager.ModemBand>, 142: <enum MM_MODEM_BAND_CDMA_BC13 of type ModemManager.ModemBand>, 143: <enum MM_MODEM_BAND_CDMA_BC14 of type ModemManager.ModemBand>, 144: <enum MM_MODEM_BAND_CDMA_BC15 of type ModemManager.ModemBand>, 145: <enum MM_MODEM_BAND_CDMA_BC16 of type ModemManager.ModemBand>, 146: <enum MM_MODEM_BAND_CDMA_BC17 of type ModemManager.ModemBand>, 147: <enum MM_MODEM_BAND_CDMA_BC18 of type ModemManager.ModemBand>, 148: <enum MM_MODEM_BAND_CDMA_BC19 of type ModemManager.ModemBand>, 210: <enum MM_MODEM_BAND_UTRAN_10 of type ModemManager.ModemBand>, 211: <enum MM_MODEM_BAND_UTRAN_11 of type ModemManager.ModemBand>, 212: <enum MM_MODEM_BAND_UTRAN_12 of type ModemManager.ModemBand>, 213: <enum MM_MODEM_BAND_UTRAN_13 of type ModemManager.ModemBand>, 214: <enum MM_MODEM_BAND_UTRAN_14 of type ModemManager.ModemBand>, 219: <enum MM_MODEM_BAND_UTRAN_19 of type ModemManager.ModemBand>, 220: <enum MM_MODEM_BAND_UTRAN_20 of type ModemManager.ModemBand>, 221: <enum MM_MODEM_BAND_UTRAN_21 of type ModemManager.ModemBand>, 222: <enum MM_MODEM_BAND_UTRAN_22 of type ModemManager.ModemBand>, 225: <enum MM_MODEM_BAND_UTRAN_25 of type ModemManager.ModemBand>, 226: <enum MM_MODEM_BAND_UTRAN_26 of type ModemManager.ModemBand>, 232: <enum MM_MODEM_BAND_UTRAN_32 of type ModemManager.ModemBand>, 256: <enum MM_MODEM_BAND_ANY of type ModemManager.ModemBand>}, '__info__': gi.EnumInfo(ModemBand), 'UNKNOWN': <enum MM_MODEM_BAND_UNKNOWN of type ModemManager.ModemBand>, 'EGSM': <enum MM_MODEM_BAND_EGSM of type ModemManager.ModemBand>, 'DCS': <enum MM_MODEM_BAND_DCS of type ModemManager.ModemBand>, 'PCS': <enum MM_MODEM_BAND_PCS of type ModemManager.ModemBand>, 'G850': <enum MM_MODEM_BAND_G850 of type ModemManager.ModemBand>, 'UTRAN_1': <enum MM_MODEM_BAND_UTRAN_1 of type ModemManager.ModemBand>, 'UTRAN_3': <enum MM_MODEM_BAND_UTRAN_3 of type ModemManager.ModemBand>, 'UTRAN_4': <enum MM_MODEM_BAND_UTRAN_4 of type ModemManager.ModemBand>, 'UTRAN_6': <enum MM_MODEM_BAND_UTRAN_6 of type ModemManager.ModemBand>, 'UTRAN_5': <enum MM_MODEM_BAND_UTRAN_5 of type ModemManager.ModemBand>, 'UTRAN_8': <enum MM_MODEM_BAND_UTRAN_8 of type ModemManager.ModemBand>, 'UTRAN_9': <enum MM_MODEM_BAND_UTRAN_9 of type ModemManager.ModemBand>, 'UTRAN_2': <enum MM_MODEM_BAND_UTRAN_2 of type ModemManager.ModemBand>, 'UTRAN_7': <enum MM_MODEM_BAND_UTRAN_7 of type ModemManager.ModemBand>, 'G450': <enum MM_MODEM_BAND_G450 of type ModemManager.ModemBand>, 'G480': <enum MM_MODEM_BAND_G480 of type ModemManager.ModemBand>, 'G750': <enum MM_MODEM_BAND_G750 of type ModemManager.ModemBand>, 'G380': <enum MM_MODEM_BAND_G380 of type ModemManager.ModemBand>, 'G410': <enum MM_MODEM_BAND_G410 of type ModemManager.ModemBand>, 'G710': <enum MM_MODEM_BAND_G710 of type ModemManager.ModemBand>, 'G810': <enum MM_MODEM_BAND_G810 of type ModemManager.ModemBand>, 'EUTRAN_1': <enum MM_MODEM_BAND_EUTRAN_1 of type ModemManager.ModemBand>, 'EUTRAN_2': <enum MM_MODEM_BAND_EUTRAN_2 of type ModemManager.ModemBand>, 'EUTRAN_3': <enum MM_MODEM_BAND_EUTRAN_3 of type ModemManager.ModemBand>, 'EUTRAN_4': <enum MM_MODEM_BAND_EUTRAN_4 of type ModemManager.ModemBand>, 'EUTRAN_5': <enum MM_MODEM_BAND_EUTRAN_5 of type ModemManager.ModemBand>, 'EUTRAN_6': <enum MM_MODEM_BAND_EUTRAN_6 of type ModemManager.ModemBand>, 'EUTRAN_7': <enum MM_MODEM_BAND_EUTRAN_7 of type ModemManager.ModemBand>, 'EUTRAN_8': <enum MM_MODEM_BAND_EUTRAN_8 of type ModemManager.ModemBand>, 'EUTRAN_9': <enum MM_MODEM_BAND_EUTRAN_9 of type ModemManager.ModemBand>, 'EUTRAN_10': <enum MM_MODEM_BAND_EUTRAN_10 of type ModemManager.ModemBand>, 'EUTRAN_11': <enum MM_MODEM_BAND_EUTRAN_11 of type ModemManager.ModemBand>, 'EUTRAN_12': <enum MM_MODEM_BAND_EUTRAN_12 of type ModemManager.ModemBand>, 'EUTRAN_13': <enum MM_MODEM_BAND_EUTRAN_13 of type ModemManager.ModemBand>, 'EUTRAN_14': <enum MM_MODEM_BAND_EUTRAN_14 of type ModemManager.ModemBand>, 'EUTRAN_17': <enum MM_MODEM_BAND_EUTRAN_17 of type ModemManager.ModemBand>, 'EUTRAN_18': <enum MM_MODEM_BAND_EUTRAN_18 of type ModemManager.ModemBand>, 'EUTRAN_19': <enum MM_MODEM_BAND_EUTRAN_19 of type ModemManager.ModemBand>, 'EUTRAN_20': <enum MM_MODEM_BAND_EUTRAN_20 of type ModemManager.ModemBand>, 'EUTRAN_21': <enum MM_MODEM_BAND_EUTRAN_21 of type ModemManager.ModemBand>, 'EUTRAN_22': <enum MM_MODEM_BAND_EUTRAN_22 of type ModemManager.ModemBand>, 'EUTRAN_23': <enum MM_MODEM_BAND_EUTRAN_23 of type ModemManager.ModemBand>, 'EUTRAN_24': <enum MM_MODEM_BAND_EUTRAN_24 of type ModemManager.ModemBand>, 'EUTRAN_25': <enum MM_MODEM_BAND_EUTRAN_25 of type ModemManager.ModemBand>, 'EUTRAN_26': <enum MM_MODEM_BAND_EUTRAN_26 of type ModemManager.ModemBand>, 'EUTRAN_27': <enum MM_MODEM_BAND_EUTRAN_27 of type ModemManager.ModemBand>, 'EUTRAN_28': <enum MM_MODEM_BAND_EUTRAN_28 of type ModemManager.ModemBand>, 'EUTRAN_29': <enum MM_MODEM_BAND_EUTRAN_29 of type ModemManager.ModemBand>, 'EUTRAN_30': <enum MM_MODEM_BAND_EUTRAN_30 of type ModemManager.ModemBand>, 'EUTRAN_31': <enum MM_MODEM_BAND_EUTRAN_31 of type ModemManager.ModemBand>, 'EUTRAN_32': <enum MM_MODEM_BAND_EUTRAN_32 of type ModemManager.ModemBand>, 'EUTRAN_33': <enum MM_MODEM_BAND_EUTRAN_33 of type ModemManager.ModemBand>, 'EUTRAN_34': <enum MM_MODEM_BAND_EUTRAN_34 of type ModemManager.ModemBand>, 'EUTRAN_35': <enum MM_MODEM_BAND_EUTRAN_35 of type ModemManager.ModemBand>, 'EUTRAN_36': <enum MM_MODEM_BAND_EUTRAN_36 of type ModemManager.ModemBand>, 'EUTRAN_37': <enum MM_MODEM_BAND_EUTRAN_37 of type ModemManager.ModemBand>, 'EUTRAN_38': <enum MM_MODEM_BAND_EUTRAN_38 of type ModemManager.ModemBand>, 'EUTRAN_39': <enum MM_MODEM_BAND_EUTRAN_39 of type ModemManager.ModemBand>, 'EUTRAN_40': <enum MM_MODEM_BAND_EUTRAN_40 of type ModemManager.ModemBand>, 'EUTRAN_41': <enum MM_MODEM_BAND_EUTRAN_41 of type ModemManager.ModemBand>, 'EUTRAN_42': <enum MM_MODEM_BAND_EUTRAN_42 of type ModemManager.ModemBand>, 'EUTRAN_43': <enum MM_MODEM_BAND_EUTRAN_43 of type ModemManager.ModemBand>, 'EUTRAN_44': <enum MM_MODEM_BAND_EUTRAN_44 of type ModemManager.ModemBand>, 'EUTRAN_45': <enum MM_MODEM_BAND_EUTRAN_45 of type ModemManager.ModemBand>, 'EUTRAN_46': <enum MM_MODEM_BAND_EUTRAN_46 of type ModemManager.ModemBand>, 'EUTRAN_47': <enum MM_MODEM_BAND_EUTRAN_47 of type ModemManager.ModemBand>, 'EUTRAN_48': <enum MM_MODEM_BAND_EUTRAN_48 of type ModemManager.ModemBand>, 'EUTRAN_49': <enum MM_MODEM_BAND_EUTRAN_49 of type ModemManager.ModemBand>, 'EUTRAN_50': <enum MM_MODEM_BAND_EUTRAN_50 of type ModemManager.ModemBand>, 'EUTRAN_51': <enum MM_MODEM_BAND_EUTRAN_51 of type ModemManager.ModemBand>, 'EUTRAN_52': <enum MM_MODEM_BAND_EUTRAN_52 of type ModemManager.ModemBand>, 'EUTRAN_53': <enum MM_MODEM_BAND_EUTRAN_53 of type ModemManager.ModemBand>, 'EUTRAN_54': <enum MM_MODEM_BAND_EUTRAN_54 of type ModemManager.ModemBand>, 'EUTRAN_55': <enum MM_MODEM_BAND_EUTRAN_55 of type ModemManager.ModemBand>, 'EUTRAN_56': <enum MM_MODEM_BAND_EUTRAN_56 of type ModemManager.ModemBand>, 'EUTRAN_57': <enum MM_MODEM_BAND_EUTRAN_57 of type ModemManager.ModemBand>, 'EUTRAN_58': <enum MM_MODEM_BAND_EUTRAN_58 of type ModemManager.ModemBand>, 'EUTRAN_59': <enum MM_MODEM_BAND_EUTRAN_59 of type ModemManager.ModemBand>, 'EUTRAN_60': <enum MM_MODEM_BAND_EUTRAN_60 of type ModemManager.ModemBand>, 'EUTRAN_61': <enum MM_MODEM_BAND_EUTRAN_61 of type ModemManager.ModemBand>, 'EUTRAN_62': <enum MM_MODEM_BAND_EUTRAN_62 of type ModemManager.ModemBand>, 'EUTRAN_63': <enum MM_MODEM_BAND_EUTRAN_63 of type ModemManager.ModemBand>, 'EUTRAN_64': <enum MM_MODEM_BAND_EUTRAN_64 of type ModemManager.ModemBand>, 'EUTRAN_65': <enum MM_MODEM_BAND_EUTRAN_65 of type ModemManager.ModemBand>, 'EUTRAN_66': <enum MM_MODEM_BAND_EUTRAN_66 of type ModemManager.ModemBand>, 'EUTRAN_67': <enum MM_MODEM_BAND_EUTRAN_67 of type ModemManager.ModemBand>, 'EUTRAN_68': <enum MM_MODEM_BAND_EUTRAN_68 of type ModemManager.ModemBand>, 'EUTRAN_69': <enum MM_MODEM_BAND_EUTRAN_69 of type ModemManager.ModemBand>, 'EUTRAN_70': <enum MM_MODEM_BAND_EUTRAN_70 of type ModemManager.ModemBand>, 'EUTRAN_71': <enum MM_MODEM_BAND_EUTRAN_71 of type ModemManager.ModemBand>, 'CDMA_BC0': <enum MM_MODEM_BAND_CDMA_BC0 of type ModemManager.ModemBand>, 'CDMA_BC1': <enum MM_MODEM_BAND_CDMA_BC1 of type ModemManager.ModemBand>, 'CDMA_BC2': <enum MM_MODEM_BAND_CDMA_BC2 of type ModemManager.ModemBand>, 'CDMA_BC3': <enum MM_MODEM_BAND_CDMA_BC3 of type ModemManager.ModemBand>, 'CDMA_BC4': <enum MM_MODEM_BAND_CDMA_BC4 of type ModemManager.ModemBand>, 'CDMA_BC5': <enum MM_MODEM_BAND_CDMA_BC5 of type ModemManager.ModemBand>, 'CDMA_BC6': <enum MM_MODEM_BAND_CDMA_BC6 of type ModemManager.ModemBand>, 'CDMA_BC7': <enum MM_MODEM_BAND_CDMA_BC7 of type ModemManager.ModemBand>, 'CDMA_BC8': <enum MM_MODEM_BAND_CDMA_BC8 of type ModemManager.ModemBand>, 'CDMA_BC9': <enum MM_MODEM_BAND_CDMA_BC9 of type ModemManager.ModemBand>, 'CDMA_BC10': <enum MM_MODEM_BAND_CDMA_BC10 of type ModemManager.ModemBand>, 'CDMA_BC11': <enum MM_MODEM_BAND_CDMA_BC11 of type ModemManager.ModemBand>, 'CDMA_BC12': <enum MM_MODEM_BAND_CDMA_BC12 of type ModemManager.ModemBand>, 'CDMA_BC13': <enum MM_MODEM_BAND_CDMA_BC13 of type ModemManager.ModemBand>, 'CDMA_BC14': <enum MM_MODEM_BAND_CDMA_BC14 of type ModemManager.ModemBand>, 'CDMA_BC15': <enum MM_MODEM_BAND_CDMA_BC15 of type ModemManager.ModemBand>, 'CDMA_BC16': <enum MM_MODEM_BAND_CDMA_BC16 of type ModemManager.ModemBand>, 'CDMA_BC17': <enum MM_MODEM_BAND_CDMA_BC17 of type ModemManager.ModemBand>, 'CDMA_BC18': <enum MM_MODEM_BAND_CDMA_BC18 of type ModemManager.ModemBand>, 'CDMA_BC19': <enum MM_MODEM_BAND_CDMA_BC19 of type ModemManager.ModemBand>, 'UTRAN_10': <enum MM_MODEM_BAND_UTRAN_10 of type ModemManager.ModemBand>, 'UTRAN_11': <enum MM_MODEM_BAND_UTRAN_11 of type ModemManager.ModemBand>, 'UTRAN_12': <enum MM_MODEM_BAND_UTRAN_12 of type ModemManager.ModemBand>, 'UTRAN_13': <enum MM_MODEM_BAND_UTRAN_13 of type ModemManager.ModemBand>, 'UTRAN_14': <enum MM_MODEM_BAND_UTRAN_14 of type ModemManager.ModemBand>, 'UTRAN_19': <enum MM_MODEM_BAND_UTRAN_19 of type ModemManager.ModemBand>, 'UTRAN_20': <enum MM_MODEM_BAND_UTRAN_20 of type ModemManager.ModemBand>, 'UTRAN_21': <enum MM_MODEM_BAND_UTRAN_21 of type ModemManager.ModemBand>, 'UTRAN_22': <enum MM_MODEM_BAND_UTRAN_22 of type ModemManager.ModemBand>, 'UTRAN_25': <enum MM_MODEM_BAND_UTRAN_25 of type ModemManager.ModemBand>, 'UTRAN_26': <enum MM_MODEM_BAND_UTRAN_26 of type ModemManager.ModemBand>, 'UTRAN_32': <enum MM_MODEM_BAND_UTRAN_32 of type ModemManager.ModemBand>, 'ANY': <enum MM_MODEM_BAND_ANY of type ModemManager.ModemBand>, 'get_string': gi.FunctionInfo(get_string)})"
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
        94: 94,
        95: 95,
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        128: 128,
        129: 129,
        130: 130,
        131: 131,
        132: 132,
        134: 134,
        135: 135,
        136: 136,
        137: 137,
        138: 138,
        139: 139,
        140: 140,
        141: 141,
        142: 142,
        143: 143,
        144: 144,
        145: 145,
        146: 146,
        147: 147,
        148: 148,
        210: 210,
        211: 211,
        212: 212,
        213: 213,
        214: 214,
        219: 219,
        220: 220,
        221: 221,
        222: 222,
        225: 225,
        226: 226,
        232: 232,
        256: 256,
    }
    __gtype__ = None # (!) real value is '<GType MMModemBand (94631948708176)>'
    __info__ = gi.EnumInfo(ModemBand)


