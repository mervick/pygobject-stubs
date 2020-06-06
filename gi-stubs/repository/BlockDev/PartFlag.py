# encoding: utf-8
# module gi.repository.BlockDev
# from /usr/lib64/girepository-1.0/BlockDev-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.BlockDev as __gi_overrides_BlockDev
import gobject as __gobject


class PartFlag(__gobject.GFlags):
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


    APPLE_TV_RECOVERY = 8192
    BIOS_GRUB = 4096
    BOOT = 2
    CPALO = 512
    DIAG = 16384
    ESP = 262144
    GPT_HIDDEN = 134217728
    GPT_NO_AUTOMOUNT = 268435456
    GPT_READ_ONLY = 67108864
    GPT_SYSTEM_PART = 33554432
    HIDDEN = 16
    HPSERVICE = 256
    IRST = 131072
    LBA = 128
    LEGACY_BOOT = 32768
    LVM = 64
    MSFT_DATA = 65536
    MSFT_RESERVED = 2048
    PREP = 1024
    RAID = 32
    ROOT = 4
    SWAP = 8
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.BlockDev', '__dict__': <attribute '__dict__' of 'PartFlag' objects>, '__doc__': None, '__gtype__': <GType PyBlockDevPartFlag (94066389774576)>, '__flags_values__': {2: <flags BD_PART_FLAG_BOOT of type BlockDev.PartFlag>, 4: <flags BD_PART_FLAG_ROOT of type BlockDev.PartFlag>, 8: <flags BD_PART_FLAG_SWAP of type BlockDev.PartFlag>, 16: <flags BD_PART_FLAG_HIDDEN of type BlockDev.PartFlag>, 32: <flags BD_PART_FLAG_RAID of type BlockDev.PartFlag>, 64: <flags BD_PART_FLAG_LVM of type BlockDev.PartFlag>, 128: <flags BD_PART_FLAG_LBA of type BlockDev.PartFlag>, 256: <flags BD_PART_FLAG_HPSERVICE of type BlockDev.PartFlag>, 512: <flags BD_PART_FLAG_CPALO of type BlockDev.PartFlag>, 1024: <flags BD_PART_FLAG_PREP of type BlockDev.PartFlag>, 2048: <flags BD_PART_FLAG_MSFT_RESERVED of type BlockDev.PartFlag>, 4096: <flags BD_PART_FLAG_BIOS_GRUB of type BlockDev.PartFlag>, 8192: <flags BD_PART_FLAG_APPLE_TV_RECOVERY of type BlockDev.PartFlag>, 16384: <flags BD_PART_FLAG_DIAG of type BlockDev.PartFlag>, 32768: <flags BD_PART_FLAG_LEGACY_BOOT of type BlockDev.PartFlag>, 65536: <flags BD_PART_FLAG_MSFT_DATA of type BlockDev.PartFlag>, 131072: <flags BD_PART_FLAG_IRST of type BlockDev.PartFlag>, 262144: <flags BD_PART_FLAG_ESP of type BlockDev.PartFlag>, 33554432: <flags BD_PART_FLAG_GPT_SYSTEM_PART of type BlockDev.PartFlag>, 67108864: <flags BD_PART_FLAG_GPT_READ_ONLY of type BlockDev.PartFlag>, 134217728: <flags BD_PART_FLAG_GPT_HIDDEN of type BlockDev.PartFlag>, 268435456: <flags BD_PART_FLAG_GPT_NO_AUTOMOUNT of type BlockDev.PartFlag>}, '__info__': gi.EnumInfo(PartFlag), 'BOOT': <flags BD_PART_FLAG_BOOT of type BlockDev.PartFlag>, 'ROOT': <flags BD_PART_FLAG_ROOT of type BlockDev.PartFlag>, 'SWAP': <flags BD_PART_FLAG_SWAP of type BlockDev.PartFlag>, 'HIDDEN': <flags BD_PART_FLAG_HIDDEN of type BlockDev.PartFlag>, 'RAID': <flags BD_PART_FLAG_RAID of type BlockDev.PartFlag>, 'LVM': <flags BD_PART_FLAG_LVM of type BlockDev.PartFlag>, 'LBA': <flags BD_PART_FLAG_LBA of type BlockDev.PartFlag>, 'HPSERVICE': <flags BD_PART_FLAG_HPSERVICE of type BlockDev.PartFlag>, 'CPALO': <flags BD_PART_FLAG_CPALO of type BlockDev.PartFlag>, 'PREP': <flags BD_PART_FLAG_PREP of type BlockDev.PartFlag>, 'MSFT_RESERVED': <flags BD_PART_FLAG_MSFT_RESERVED of type BlockDev.PartFlag>, 'BIOS_GRUB': <flags BD_PART_FLAG_BIOS_GRUB of type BlockDev.PartFlag>, 'APPLE_TV_RECOVERY': <flags BD_PART_FLAG_APPLE_TV_RECOVERY of type BlockDev.PartFlag>, 'DIAG': <flags BD_PART_FLAG_DIAG of type BlockDev.PartFlag>, 'LEGACY_BOOT': <flags BD_PART_FLAG_LEGACY_BOOT of type BlockDev.PartFlag>, 'MSFT_DATA': <flags BD_PART_FLAG_MSFT_DATA of type BlockDev.PartFlag>, 'IRST': <flags BD_PART_FLAG_IRST of type BlockDev.PartFlag>, 'ESP': <flags BD_PART_FLAG_ESP of type BlockDev.PartFlag>, 'GPT_SYSTEM_PART': <flags BD_PART_FLAG_GPT_SYSTEM_PART of type BlockDev.PartFlag>, 'GPT_READ_ONLY': <flags BD_PART_FLAG_GPT_READ_ONLY of type BlockDev.PartFlag>, 'GPT_HIDDEN': <flags BD_PART_FLAG_GPT_HIDDEN of type BlockDev.PartFlag>, 'GPT_NO_AUTOMOUNT': <flags BD_PART_FLAG_GPT_NO_AUTOMOUNT of type BlockDev.PartFlag>})"
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
        33554432: 33554432,
        67108864: 67108864,
        134217728: 134217728,
        268435456: 268435456,
    }
    __gtype__ = None # (!) real value is '<GType PyBlockDevPartFlag (94066389774576)>'
    __info__ = gi.EnumInfo(PartFlag)


