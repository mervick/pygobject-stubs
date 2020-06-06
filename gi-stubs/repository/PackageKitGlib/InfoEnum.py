# encoding: utf-8
# module gi.repository.PackageKitGlib
# from /usr/lib64/girepository-1.0/PackageKitGlib-1.0.typelib
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


class InfoEnum(__gobject.GEnum):
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

    def from_string(self, info): # real signature unknown; restored from __doc__
        """ from_string(info:str) -> PackageKitGlib.InfoEnum """
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

    def to_localised_past(self, info): # real signature unknown; restored from __doc__
        """ to_localised_past(info:PackageKitGlib.InfoEnum) -> str """
        return ""

    def to_localised_present(self, info): # real signature unknown; restored from __doc__
        """ to_localised_present(info:PackageKitGlib.InfoEnum) -> str """
        return ""

    def to_string(self, info): # real signature unknown; restored from __doc__
        """ to_string(info:PackageKitGlib.InfoEnum) -> str """
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


    AVAILABLE = 2
    BLOCKED = 9
    BUGFIX = 6
    CLEANUP = 14
    COLLECTION_AVAILABLE = 17
    COLLECTION_INSTALLED = 16
    DECOMPRESSING = 22
    DOWNGRADING = 20
    DOWNLOADING = 10
    ENHANCEMENT = 4
    FINISHED = 18
    IMPORTANT = 7
    INSTALLED = 1
    INSTALLING = 12
    LAST = 26
    LOW = 3
    NORMAL = 5
    OBSOLETING = 15
    PREPARING = 21
    REINSTALLING = 19
    REMOVING = 13
    SECURITY = 8
    TRUSTED = 24
    UNAVAILABLE = 25
    UNKNOWN = 0
    UNTRUSTED = 23
    UPDATING = 11
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.PackageKitGlib', '__dict__': <attribute '__dict__' of 'InfoEnum' objects>, '__doc__': None, '__gtype__': <GType PkInfoEnum (94016447178000)>, '__enum_values__': {0: <enum PK_INFO_ENUM_UNKNOWN of type PackageKitGlib.InfoEnum>, 1: <enum PK_INFO_ENUM_INSTALLED of type PackageKitGlib.InfoEnum>, 2: <enum PK_INFO_ENUM_AVAILABLE of type PackageKitGlib.InfoEnum>, 3: <enum PK_INFO_ENUM_LOW of type PackageKitGlib.InfoEnum>, 4: <enum PK_INFO_ENUM_ENHANCEMENT of type PackageKitGlib.InfoEnum>, 5: <enum PK_INFO_ENUM_NORMAL of type PackageKitGlib.InfoEnum>, 6: <enum PK_INFO_ENUM_BUGFIX of type PackageKitGlib.InfoEnum>, 7: <enum PK_INFO_ENUM_IMPORTANT of type PackageKitGlib.InfoEnum>, 8: <enum PK_INFO_ENUM_SECURITY of type PackageKitGlib.InfoEnum>, 9: <enum PK_INFO_ENUM_BLOCKED of type PackageKitGlib.InfoEnum>, 10: <enum PK_INFO_ENUM_DOWNLOADING of type PackageKitGlib.InfoEnum>, 11: <enum PK_INFO_ENUM_UPDATING of type PackageKitGlib.InfoEnum>, 12: <enum PK_INFO_ENUM_INSTALLING of type PackageKitGlib.InfoEnum>, 13: <enum PK_INFO_ENUM_REMOVING of type PackageKitGlib.InfoEnum>, 14: <enum PK_INFO_ENUM_CLEANUP of type PackageKitGlib.InfoEnum>, 15: <enum PK_INFO_ENUM_OBSOLETING of type PackageKitGlib.InfoEnum>, 16: <enum PK_INFO_ENUM_COLLECTION_INSTALLED of type PackageKitGlib.InfoEnum>, 17: <enum PK_INFO_ENUM_COLLECTION_AVAILABLE of type PackageKitGlib.InfoEnum>, 18: <enum PK_INFO_ENUM_FINISHED of type PackageKitGlib.InfoEnum>, 19: <enum PK_INFO_ENUM_REINSTALLING of type PackageKitGlib.InfoEnum>, 20: <enum PK_INFO_ENUM_DOWNGRADING of type PackageKitGlib.InfoEnum>, 21: <enum PK_INFO_ENUM_PREPARING of type PackageKitGlib.InfoEnum>, 22: <enum PK_INFO_ENUM_DECOMPRESSING of type PackageKitGlib.InfoEnum>, 23: <enum PK_INFO_ENUM_UNTRUSTED of type PackageKitGlib.InfoEnum>, 24: <enum PK_INFO_ENUM_TRUSTED of type PackageKitGlib.InfoEnum>, 25: <enum PK_INFO_ENUM_UNAVAILABLE of type PackageKitGlib.InfoEnum>, 26: <enum PK_INFO_ENUM_LAST of type PackageKitGlib.InfoEnum>}, '__info__': gi.EnumInfo(InfoEnum), 'UNKNOWN': <enum PK_INFO_ENUM_UNKNOWN of type PackageKitGlib.InfoEnum>, 'INSTALLED': <enum PK_INFO_ENUM_INSTALLED of type PackageKitGlib.InfoEnum>, 'AVAILABLE': <enum PK_INFO_ENUM_AVAILABLE of type PackageKitGlib.InfoEnum>, 'LOW': <enum PK_INFO_ENUM_LOW of type PackageKitGlib.InfoEnum>, 'ENHANCEMENT': <enum PK_INFO_ENUM_ENHANCEMENT of type PackageKitGlib.InfoEnum>, 'NORMAL': <enum PK_INFO_ENUM_NORMAL of type PackageKitGlib.InfoEnum>, 'BUGFIX': <enum PK_INFO_ENUM_BUGFIX of type PackageKitGlib.InfoEnum>, 'IMPORTANT': <enum PK_INFO_ENUM_IMPORTANT of type PackageKitGlib.InfoEnum>, 'SECURITY': <enum PK_INFO_ENUM_SECURITY of type PackageKitGlib.InfoEnum>, 'BLOCKED': <enum PK_INFO_ENUM_BLOCKED of type PackageKitGlib.InfoEnum>, 'DOWNLOADING': <enum PK_INFO_ENUM_DOWNLOADING of type PackageKitGlib.InfoEnum>, 'UPDATING': <enum PK_INFO_ENUM_UPDATING of type PackageKitGlib.InfoEnum>, 'INSTALLING': <enum PK_INFO_ENUM_INSTALLING of type PackageKitGlib.InfoEnum>, 'REMOVING': <enum PK_INFO_ENUM_REMOVING of type PackageKitGlib.InfoEnum>, 'CLEANUP': <enum PK_INFO_ENUM_CLEANUP of type PackageKitGlib.InfoEnum>, 'OBSOLETING': <enum PK_INFO_ENUM_OBSOLETING of type PackageKitGlib.InfoEnum>, 'COLLECTION_INSTALLED': <enum PK_INFO_ENUM_COLLECTION_INSTALLED of type PackageKitGlib.InfoEnum>, 'COLLECTION_AVAILABLE': <enum PK_INFO_ENUM_COLLECTION_AVAILABLE of type PackageKitGlib.InfoEnum>, 'FINISHED': <enum PK_INFO_ENUM_FINISHED of type PackageKitGlib.InfoEnum>, 'REINSTALLING': <enum PK_INFO_ENUM_REINSTALLING of type PackageKitGlib.InfoEnum>, 'DOWNGRADING': <enum PK_INFO_ENUM_DOWNGRADING of type PackageKitGlib.InfoEnum>, 'PREPARING': <enum PK_INFO_ENUM_PREPARING of type PackageKitGlib.InfoEnum>, 'DECOMPRESSING': <enum PK_INFO_ENUM_DECOMPRESSING of type PackageKitGlib.InfoEnum>, 'UNTRUSTED': <enum PK_INFO_ENUM_UNTRUSTED of type PackageKitGlib.InfoEnum>, 'TRUSTED': <enum PK_INFO_ENUM_TRUSTED of type PackageKitGlib.InfoEnum>, 'UNAVAILABLE': <enum PK_INFO_ENUM_UNAVAILABLE of type PackageKitGlib.InfoEnum>, 'LAST': <enum PK_INFO_ENUM_LAST of type PackageKitGlib.InfoEnum>, 'from_string': gi.FunctionInfo(from_string), 'to_localised_past': gi.FunctionInfo(to_localised_past), 'to_localised_present': gi.FunctionInfo(to_localised_present), 'to_string': gi.FunctionInfo(to_string)})"
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
    __gtype__ = None # (!) real value is '<GType PkInfoEnum (94016447178000)>'
    __info__ = gi.EnumInfo(InfoEnum)


