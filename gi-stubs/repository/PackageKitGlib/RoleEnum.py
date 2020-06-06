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


class RoleEnum(__gobject.GEnum):
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

    def from_string(self, role): # real signature unknown; restored from __doc__
        """ from_string(role:str) -> PackageKitGlib.RoleEnum """
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

    def to_localised_present(self, role): # real signature unknown; restored from __doc__
        """ to_localised_present(role:PackageKitGlib.RoleEnum) -> str """
        return ""

    def to_string(self, role): # real signature unknown; restored from __doc__
        """ to_string(role:PackageKitGlib.RoleEnum) -> str """
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


    ACCEPT_EULA = 24
    CANCEL = 1
    DEPENDS_ON = 2
    DOWNLOAD_PACKAGES = 25
    GET_CATEGORIES = 27
    GET_DETAILS = 3
    GET_DETAILS_LOCAL = 30
    GET_DISTRO_UPGRADES = 26
    GET_FILES = 4
    GET_FILES_LOCAL = 31
    GET_OLD_TRANSACTIONS = 28
    GET_PACKAGES = 5
    GET_REPO_LIST = 6
    GET_UPDATES = 9
    GET_UPDATE_DETAIL = 8
    INSTALL_FILES = 10
    INSTALL_PACKAGES = 11
    INSTALL_SIGNATURE = 12
    LAST = 34
    REFRESH_CACHE = 13
    REMOVE_PACKAGES = 14
    REPAIR_SYSTEM = 29
    REPO_ENABLE = 15
    REPO_REMOVE = 32
    REPO_SET_DATA = 16
    REQUIRED_BY = 7
    RESOLVE = 17
    SEARCH_DETAILS = 18
    SEARCH_FILE = 19
    SEARCH_GROUP = 20
    SEARCH_NAME = 21
    UNKNOWN = 0
    UPDATE_PACKAGES = 22
    UPGRADE_SYSTEM = 33
    WHAT_PROVIDES = 23
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.PackageKitGlib', '__dict__': <attribute '__dict__' of 'RoleEnum' objects>, '__doc__': None, '__gtype__': <GType PkRoleEnum (94016447470144)>, '__enum_values__': {0: <enum PK_ROLE_ENUM_UNKNOWN of type PackageKitGlib.RoleEnum>, 1: <enum PK_ROLE_ENUM_CANCEL of type PackageKitGlib.RoleEnum>, 2: <enum PK_ROLE_ENUM_DEPENDS_ON of type PackageKitGlib.RoleEnum>, 3: <enum PK_ROLE_ENUM_GET_DETAILS of type PackageKitGlib.RoleEnum>, 4: <enum PK_ROLE_ENUM_GET_FILES of type PackageKitGlib.RoleEnum>, 5: <enum PK_ROLE_ENUM_GET_PACKAGES of type PackageKitGlib.RoleEnum>, 6: <enum PK_ROLE_ENUM_GET_REPO_LIST of type PackageKitGlib.RoleEnum>, 7: <enum PK_ROLE_ENUM_REQUIRED_BY of type PackageKitGlib.RoleEnum>, 8: <enum PK_ROLE_ENUM_GET_UPDATE_DETAIL of type PackageKitGlib.RoleEnum>, 9: <enum PK_ROLE_ENUM_GET_UPDATES of type PackageKitGlib.RoleEnum>, 10: <enum PK_ROLE_ENUM_INSTALL_FILES of type PackageKitGlib.RoleEnum>, 11: <enum PK_ROLE_ENUM_INSTALL_PACKAGES of type PackageKitGlib.RoleEnum>, 12: <enum PK_ROLE_ENUM_INSTALL_SIGNATURE of type PackageKitGlib.RoleEnum>, 13: <enum PK_ROLE_ENUM_REFRESH_CACHE of type PackageKitGlib.RoleEnum>, 14: <enum PK_ROLE_ENUM_REMOVE_PACKAGES of type PackageKitGlib.RoleEnum>, 15: <enum PK_ROLE_ENUM_REPO_ENABLE of type PackageKitGlib.RoleEnum>, 16: <enum PK_ROLE_ENUM_REPO_SET_DATA of type PackageKitGlib.RoleEnum>, 17: <enum PK_ROLE_ENUM_RESOLVE of type PackageKitGlib.RoleEnum>, 18: <enum PK_ROLE_ENUM_SEARCH_DETAILS of type PackageKitGlib.RoleEnum>, 19: <enum PK_ROLE_ENUM_SEARCH_FILE of type PackageKitGlib.RoleEnum>, 20: <enum PK_ROLE_ENUM_SEARCH_GROUP of type PackageKitGlib.RoleEnum>, 21: <enum PK_ROLE_ENUM_SEARCH_NAME of type PackageKitGlib.RoleEnum>, 22: <enum PK_ROLE_ENUM_UPDATE_PACKAGES of type PackageKitGlib.RoleEnum>, 23: <enum PK_ROLE_ENUM_WHAT_PROVIDES of type PackageKitGlib.RoleEnum>, 24: <enum PK_ROLE_ENUM_ACCEPT_EULA of type PackageKitGlib.RoleEnum>, 25: <enum PK_ROLE_ENUM_DOWNLOAD_PACKAGES of type PackageKitGlib.RoleEnum>, 26: <enum PK_ROLE_ENUM_GET_DISTRO_UPGRADES of type PackageKitGlib.RoleEnum>, 27: <enum PK_ROLE_ENUM_GET_CATEGORIES of type PackageKitGlib.RoleEnum>, 28: <enum PK_ROLE_ENUM_GET_OLD_TRANSACTIONS of type PackageKitGlib.RoleEnum>, 29: <enum PK_ROLE_ENUM_REPAIR_SYSTEM of type PackageKitGlib.RoleEnum>, 30: <enum PK_ROLE_ENUM_GET_DETAILS_LOCAL of type PackageKitGlib.RoleEnum>, 31: <enum PK_ROLE_ENUM_GET_FILES_LOCAL of type PackageKitGlib.RoleEnum>, 32: <enum PK_ROLE_ENUM_REPO_REMOVE of type PackageKitGlib.RoleEnum>, 33: <enum PK_ROLE_ENUM_UPGRADE_SYSTEM of type PackageKitGlib.RoleEnum>, 34: <enum PK_ROLE_ENUM_LAST of type PackageKitGlib.RoleEnum>}, '__info__': gi.EnumInfo(RoleEnum), 'UNKNOWN': <enum PK_ROLE_ENUM_UNKNOWN of type PackageKitGlib.RoleEnum>, 'CANCEL': <enum PK_ROLE_ENUM_CANCEL of type PackageKitGlib.RoleEnum>, 'DEPENDS_ON': <enum PK_ROLE_ENUM_DEPENDS_ON of type PackageKitGlib.RoleEnum>, 'GET_DETAILS': <enum PK_ROLE_ENUM_GET_DETAILS of type PackageKitGlib.RoleEnum>, 'GET_FILES': <enum PK_ROLE_ENUM_GET_FILES of type PackageKitGlib.RoleEnum>, 'GET_PACKAGES': <enum PK_ROLE_ENUM_GET_PACKAGES of type PackageKitGlib.RoleEnum>, 'GET_REPO_LIST': <enum PK_ROLE_ENUM_GET_REPO_LIST of type PackageKitGlib.RoleEnum>, 'REQUIRED_BY': <enum PK_ROLE_ENUM_REQUIRED_BY of type PackageKitGlib.RoleEnum>, 'GET_UPDATE_DETAIL': <enum PK_ROLE_ENUM_GET_UPDATE_DETAIL of type PackageKitGlib.RoleEnum>, 'GET_UPDATES': <enum PK_ROLE_ENUM_GET_UPDATES of type PackageKitGlib.RoleEnum>, 'INSTALL_FILES': <enum PK_ROLE_ENUM_INSTALL_FILES of type PackageKitGlib.RoleEnum>, 'INSTALL_PACKAGES': <enum PK_ROLE_ENUM_INSTALL_PACKAGES of type PackageKitGlib.RoleEnum>, 'INSTALL_SIGNATURE': <enum PK_ROLE_ENUM_INSTALL_SIGNATURE of type PackageKitGlib.RoleEnum>, 'REFRESH_CACHE': <enum PK_ROLE_ENUM_REFRESH_CACHE of type PackageKitGlib.RoleEnum>, 'REMOVE_PACKAGES': <enum PK_ROLE_ENUM_REMOVE_PACKAGES of type PackageKitGlib.RoleEnum>, 'REPO_ENABLE': <enum PK_ROLE_ENUM_REPO_ENABLE of type PackageKitGlib.RoleEnum>, 'REPO_SET_DATA': <enum PK_ROLE_ENUM_REPO_SET_DATA of type PackageKitGlib.RoleEnum>, 'RESOLVE': <enum PK_ROLE_ENUM_RESOLVE of type PackageKitGlib.RoleEnum>, 'SEARCH_DETAILS': <enum PK_ROLE_ENUM_SEARCH_DETAILS of type PackageKitGlib.RoleEnum>, 'SEARCH_FILE': <enum PK_ROLE_ENUM_SEARCH_FILE of type PackageKitGlib.RoleEnum>, 'SEARCH_GROUP': <enum PK_ROLE_ENUM_SEARCH_GROUP of type PackageKitGlib.RoleEnum>, 'SEARCH_NAME': <enum PK_ROLE_ENUM_SEARCH_NAME of type PackageKitGlib.RoleEnum>, 'UPDATE_PACKAGES': <enum PK_ROLE_ENUM_UPDATE_PACKAGES of type PackageKitGlib.RoleEnum>, 'WHAT_PROVIDES': <enum PK_ROLE_ENUM_WHAT_PROVIDES of type PackageKitGlib.RoleEnum>, 'ACCEPT_EULA': <enum PK_ROLE_ENUM_ACCEPT_EULA of type PackageKitGlib.RoleEnum>, 'DOWNLOAD_PACKAGES': <enum PK_ROLE_ENUM_DOWNLOAD_PACKAGES of type PackageKitGlib.RoleEnum>, 'GET_DISTRO_UPGRADES': <enum PK_ROLE_ENUM_GET_DISTRO_UPGRADES of type PackageKitGlib.RoleEnum>, 'GET_CATEGORIES': <enum PK_ROLE_ENUM_GET_CATEGORIES of type PackageKitGlib.RoleEnum>, 'GET_OLD_TRANSACTIONS': <enum PK_ROLE_ENUM_GET_OLD_TRANSACTIONS of type PackageKitGlib.RoleEnum>, 'REPAIR_SYSTEM': <enum PK_ROLE_ENUM_REPAIR_SYSTEM of type PackageKitGlib.RoleEnum>, 'GET_DETAILS_LOCAL': <enum PK_ROLE_ENUM_GET_DETAILS_LOCAL of type PackageKitGlib.RoleEnum>, 'GET_FILES_LOCAL': <enum PK_ROLE_ENUM_GET_FILES_LOCAL of type PackageKitGlib.RoleEnum>, 'REPO_REMOVE': <enum PK_ROLE_ENUM_REPO_REMOVE of type PackageKitGlib.RoleEnum>, 'UPGRADE_SYSTEM': <enum PK_ROLE_ENUM_UPGRADE_SYSTEM of type PackageKitGlib.RoleEnum>, 'LAST': <enum PK_ROLE_ENUM_LAST of type PackageKitGlib.RoleEnum>, 'from_string': gi.FunctionInfo(from_string), 'to_localised_present': gi.FunctionInfo(to_localised_present), 'to_string': gi.FunctionInfo(to_string)})"
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
    }
    __gtype__ = None # (!) real value is '<GType PkRoleEnum (94016447470144)>'
    __info__ = gi.EnumInfo(RoleEnum)


