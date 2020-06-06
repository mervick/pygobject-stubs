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


class GroupEnum(__gobject.GEnum):
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

    def from_string(self, group): # real signature unknown; restored from __doc__
        """ from_string(group:str) -> PackageKitGlib.GroupEnum """
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

    def to_string(self, group): # real signature unknown; restored from __doc__
        """ to_string(group:PackageKitGlib.GroupEnum) -> str """
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


    ACCESSIBILITY = 1
    ACCESSORIES = 2
    ADMIN_TOOLS = 3
    COLLECTIONS = 32
    COMMUNICATION = 4
    DESKTOP_GNOME = 5
    DESKTOP_KDE = 6
    DESKTOP_OTHER = 7
    DESKTOP_XFCE = 8
    DOCUMENTATION = 30
    EDUCATION = 9
    ELECTRONICS = 31
    FONTS = 10
    GAMES = 11
    GRAPHICS = 12
    INTERNET = 13
    LAST = 35
    LEGACY = 14
    LOCALIZATION = 15
    MAPS = 16
    MULTIMEDIA = 17
    NETWORK = 18
    NEWEST = 34
    OFFICE = 19
    OTHER = 20
    POWER_MANAGEMENT = 21
    PROGRAMMING = 22
    PUBLISHING = 23
    REPOS = 24
    SCIENCE = 29
    SECURITY = 25
    SERVERS = 26
    SYSTEM = 27
    UNKNOWN = 0
    VENDOR = 33
    VIRTUALIZATION = 28
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.PackageKitGlib', '__dict__': <attribute '__dict__' of 'GroupEnum' objects>, '__doc__': None, '__gtype__': <GType PkGroupEnum (94016447161984)>, '__enum_values__': {0: <enum PK_GROUP_ENUM_UNKNOWN of type PackageKitGlib.GroupEnum>, 1: <enum PK_GROUP_ENUM_ACCESSIBILITY of type PackageKitGlib.GroupEnum>, 2: <enum PK_GROUP_ENUM_ACCESSORIES of type PackageKitGlib.GroupEnum>, 3: <enum PK_GROUP_ENUM_ADMIN_TOOLS of type PackageKitGlib.GroupEnum>, 4: <enum PK_GROUP_ENUM_COMMUNICATION of type PackageKitGlib.GroupEnum>, 5: <enum PK_GROUP_ENUM_DESKTOP_GNOME of type PackageKitGlib.GroupEnum>, 6: <enum PK_GROUP_ENUM_DESKTOP_KDE of type PackageKitGlib.GroupEnum>, 7: <enum PK_GROUP_ENUM_DESKTOP_OTHER of type PackageKitGlib.GroupEnum>, 8: <enum PK_GROUP_ENUM_DESKTOP_XFCE of type PackageKitGlib.GroupEnum>, 9: <enum PK_GROUP_ENUM_EDUCATION of type PackageKitGlib.GroupEnum>, 10: <enum PK_GROUP_ENUM_FONTS of type PackageKitGlib.GroupEnum>, 11: <enum PK_GROUP_ENUM_GAMES of type PackageKitGlib.GroupEnum>, 12: <enum PK_GROUP_ENUM_GRAPHICS of type PackageKitGlib.GroupEnum>, 13: <enum PK_GROUP_ENUM_INTERNET of type PackageKitGlib.GroupEnum>, 14: <enum PK_GROUP_ENUM_LEGACY of type PackageKitGlib.GroupEnum>, 15: <enum PK_GROUP_ENUM_LOCALIZATION of type PackageKitGlib.GroupEnum>, 16: <enum PK_GROUP_ENUM_MAPS of type PackageKitGlib.GroupEnum>, 17: <enum PK_GROUP_ENUM_MULTIMEDIA of type PackageKitGlib.GroupEnum>, 18: <enum PK_GROUP_ENUM_NETWORK of type PackageKitGlib.GroupEnum>, 19: <enum PK_GROUP_ENUM_OFFICE of type PackageKitGlib.GroupEnum>, 20: <enum PK_GROUP_ENUM_OTHER of type PackageKitGlib.GroupEnum>, 21: <enum PK_GROUP_ENUM_POWER_MANAGEMENT of type PackageKitGlib.GroupEnum>, 22: <enum PK_GROUP_ENUM_PROGRAMMING of type PackageKitGlib.GroupEnum>, 23: <enum PK_GROUP_ENUM_PUBLISHING of type PackageKitGlib.GroupEnum>, 24: <enum PK_GROUP_ENUM_REPOS of type PackageKitGlib.GroupEnum>, 25: <enum PK_GROUP_ENUM_SECURITY of type PackageKitGlib.GroupEnum>, 26: <enum PK_GROUP_ENUM_SERVERS of type PackageKitGlib.GroupEnum>, 27: <enum PK_GROUP_ENUM_SYSTEM of type PackageKitGlib.GroupEnum>, 28: <enum PK_GROUP_ENUM_VIRTUALIZATION of type PackageKitGlib.GroupEnum>, 29: <enum PK_GROUP_ENUM_SCIENCE of type PackageKitGlib.GroupEnum>, 30: <enum PK_GROUP_ENUM_DOCUMENTATION of type PackageKitGlib.GroupEnum>, 31: <enum PK_GROUP_ENUM_ELECTRONICS of type PackageKitGlib.GroupEnum>, 32: <enum PK_GROUP_ENUM_COLLECTIONS of type PackageKitGlib.GroupEnum>, 33: <enum PK_GROUP_ENUM_VENDOR of type PackageKitGlib.GroupEnum>, 34: <enum PK_GROUP_ENUM_NEWEST of type PackageKitGlib.GroupEnum>, 35: <enum PK_GROUP_ENUM_LAST of type PackageKitGlib.GroupEnum>}, '__info__': gi.EnumInfo(GroupEnum), 'UNKNOWN': <enum PK_GROUP_ENUM_UNKNOWN of type PackageKitGlib.GroupEnum>, 'ACCESSIBILITY': <enum PK_GROUP_ENUM_ACCESSIBILITY of type PackageKitGlib.GroupEnum>, 'ACCESSORIES': <enum PK_GROUP_ENUM_ACCESSORIES of type PackageKitGlib.GroupEnum>, 'ADMIN_TOOLS': <enum PK_GROUP_ENUM_ADMIN_TOOLS of type PackageKitGlib.GroupEnum>, 'COMMUNICATION': <enum PK_GROUP_ENUM_COMMUNICATION of type PackageKitGlib.GroupEnum>, 'DESKTOP_GNOME': <enum PK_GROUP_ENUM_DESKTOP_GNOME of type PackageKitGlib.GroupEnum>, 'DESKTOP_KDE': <enum PK_GROUP_ENUM_DESKTOP_KDE of type PackageKitGlib.GroupEnum>, 'DESKTOP_OTHER': <enum PK_GROUP_ENUM_DESKTOP_OTHER of type PackageKitGlib.GroupEnum>, 'DESKTOP_XFCE': <enum PK_GROUP_ENUM_DESKTOP_XFCE of type PackageKitGlib.GroupEnum>, 'EDUCATION': <enum PK_GROUP_ENUM_EDUCATION of type PackageKitGlib.GroupEnum>, 'FONTS': <enum PK_GROUP_ENUM_FONTS of type PackageKitGlib.GroupEnum>, 'GAMES': <enum PK_GROUP_ENUM_GAMES of type PackageKitGlib.GroupEnum>, 'GRAPHICS': <enum PK_GROUP_ENUM_GRAPHICS of type PackageKitGlib.GroupEnum>, 'INTERNET': <enum PK_GROUP_ENUM_INTERNET of type PackageKitGlib.GroupEnum>, 'LEGACY': <enum PK_GROUP_ENUM_LEGACY of type PackageKitGlib.GroupEnum>, 'LOCALIZATION': <enum PK_GROUP_ENUM_LOCALIZATION of type PackageKitGlib.GroupEnum>, 'MAPS': <enum PK_GROUP_ENUM_MAPS of type PackageKitGlib.GroupEnum>, 'MULTIMEDIA': <enum PK_GROUP_ENUM_MULTIMEDIA of type PackageKitGlib.GroupEnum>, 'NETWORK': <enum PK_GROUP_ENUM_NETWORK of type PackageKitGlib.GroupEnum>, 'OFFICE': <enum PK_GROUP_ENUM_OFFICE of type PackageKitGlib.GroupEnum>, 'OTHER': <enum PK_GROUP_ENUM_OTHER of type PackageKitGlib.GroupEnum>, 'POWER_MANAGEMENT': <enum PK_GROUP_ENUM_POWER_MANAGEMENT of type PackageKitGlib.GroupEnum>, 'PROGRAMMING': <enum PK_GROUP_ENUM_PROGRAMMING of type PackageKitGlib.GroupEnum>, 'PUBLISHING': <enum PK_GROUP_ENUM_PUBLISHING of type PackageKitGlib.GroupEnum>, 'REPOS': <enum PK_GROUP_ENUM_REPOS of type PackageKitGlib.GroupEnum>, 'SECURITY': <enum PK_GROUP_ENUM_SECURITY of type PackageKitGlib.GroupEnum>, 'SERVERS': <enum PK_GROUP_ENUM_SERVERS of type PackageKitGlib.GroupEnum>, 'SYSTEM': <enum PK_GROUP_ENUM_SYSTEM of type PackageKitGlib.GroupEnum>, 'VIRTUALIZATION': <enum PK_GROUP_ENUM_VIRTUALIZATION of type PackageKitGlib.GroupEnum>, 'SCIENCE': <enum PK_GROUP_ENUM_SCIENCE of type PackageKitGlib.GroupEnum>, 'DOCUMENTATION': <enum PK_GROUP_ENUM_DOCUMENTATION of type PackageKitGlib.GroupEnum>, 'ELECTRONICS': <enum PK_GROUP_ENUM_ELECTRONICS of type PackageKitGlib.GroupEnum>, 'COLLECTIONS': <enum PK_GROUP_ENUM_COLLECTIONS of type PackageKitGlib.GroupEnum>, 'VENDOR': <enum PK_GROUP_ENUM_VENDOR of type PackageKitGlib.GroupEnum>, 'NEWEST': <enum PK_GROUP_ENUM_NEWEST of type PackageKitGlib.GroupEnum>, 'LAST': <enum PK_GROUP_ENUM_LAST of type PackageKitGlib.GroupEnum>, 'from_string': gi.FunctionInfo(from_string), 'to_string': gi.FunctionInfo(to_string)})"
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
        32: 32,
        33: 33,
        34: 34,
        35: 35,
    }
    __gtype__ = None # (!) real value is '<GType PkGroupEnum (94016447161984)>'
    __info__ = gi.EnumInfo(GroupEnum)


