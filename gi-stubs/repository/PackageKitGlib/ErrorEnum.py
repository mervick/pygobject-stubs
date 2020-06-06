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


class ErrorEnum(__gobject.GEnum):
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

    def from_string(self, code): # real signature unknown; restored from __doc__
        """ from_string(code:str) -> PackageKitGlib.ErrorEnum """
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

    def to_string(self, code): # real signature unknown; restored from __doc__
        """ to_string(code:PackageKitGlib.ErrorEnum) -> str """
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


    ALL_PACKAGES_ALREADY_INSTALLED = 41
    BAD_GPG_SIGNATURE = 30
    CANCELLED_PRIORITY = 65
    CANNOT_CANCEL = 25
    CANNOT_DISABLE_REPOSITORY = 54
    CANNOT_FETCH_SOURCES = 64
    CANNOT_GET_FILELIST = 52
    CANNOT_GET_LOCK = 26
    CANNOT_GET_REQUIRES = 53
    CANNOT_INSTALL_REPO_UNSIGNED = 50
    CANNOT_INSTALL_SOURCE_PACKAGE = 32
    CANNOT_REMOVE_SYSTEM_PACKAGE = 20
    CANNOT_UPDATE_REPO_UNSIGNED = 51
    CANNOT_WRITE_REPO_CONFIG = 28
    CREATE_THREAD_FAILED = 15
    DEP_RESOLUTION_FAILED = 13
    FAILED_CONFIG_PARSING = 24
    FAILED_FINALISE = 23
    FAILED_INITIALIZATION = 22
    FILE_CONFLICTS = 35
    FILE_NOT_FOUND = 42
    FILTER_INVALID = 14
    GPG_FAILURE = 5
    GROUP_LIST_INVALID = 12
    GROUP_NOT_FOUND = 11
    INCOMPATIBLE_ARCHITECTURE = 45
    INSTALL_ROOT_INVALID = 63
    INTERNAL_ERROR = 4
    INVALID_PACKAGE_FILE = 38
    LAST = 69
    LOCAL_INSTALL_FAILED = 29
    LOCK_REQUIRED = 67
    MEDIA_CHANGE_REQUIRED = 47
    MISSING_GPG_SIGNATURE = 31
    NOT_AUTHORIZED = 48
    NOT_SUPPORTED = 3
    NO_CACHE = 18
    NO_DISTRO_UPGRADE_DATA = 44
    NO_LICENSE_AGREEMENT = 34
    NO_MORE_MIRRORS_TO_TRY = 43
    NO_NETWORK = 2
    NO_PACKAGES_TO_UPDATE = 27
    NO_SPACE_ON_DEVICE = 46
    OOM = 1
    PACKAGE_ALREADY_INSTALLED = 9
    PACKAGE_CONFLICTS = 36
    PACKAGE_CORRUPT = 40
    PACKAGE_DATABASE_CHANGED = 61
    PACKAGE_DOWNLOAD_FAILED = 10
    PACKAGE_FAILED_TO_BUILD = 57
    PACKAGE_FAILED_TO_CONFIGURE = 56
    PACKAGE_FAILED_TO_INSTALL = 58
    PACKAGE_FAILED_TO_REMOVE = 59
    PACKAGE_ID_INVALID = 6
    PACKAGE_INSTALL_BLOCKED = 39
    PACKAGE_NOT_FOUND = 8
    PACKAGE_NOT_INSTALLED = 7
    PROCESS_KILL = 21
    PROVIDE_TYPE_NOT_SUPPORTED = 62
    REPO_ALREADY_SET = 68
    REPO_CONFIGURATION_ERROR = 33
    REPO_NOT_AVAILABLE = 37
    REPO_NOT_FOUND = 19
    RESTRICTED_DOWNLOAD = 55
    TRANSACTION_CANCELLED = 17
    TRANSACTION_ERROR = 16
    UNFINISHED_TRANSACTION = 66
    UNKNOWN = 0
    UPDATE_FAILED_DUE_TO_RUNNING_PROCESS = 60
    UPDATE_NOT_FOUND = 49
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.PackageKitGlib', '__dict__': <attribute '__dict__' of 'ErrorEnum' objects>, '__doc__': None, '__gtype__': <GType PkErrorEnum (94016447057232)>, '__enum_values__': {0: <enum PK_ERROR_ENUM_UNKNOWN of type PackageKitGlib.ErrorEnum>, 1: <enum PK_ERROR_ENUM_OOM of type PackageKitGlib.ErrorEnum>, 2: <enum PK_ERROR_ENUM_NO_NETWORK of type PackageKitGlib.ErrorEnum>, 3: <enum PK_ERROR_ENUM_NOT_SUPPORTED of type PackageKitGlib.ErrorEnum>, 4: <enum PK_ERROR_ENUM_INTERNAL_ERROR of type PackageKitGlib.ErrorEnum>, 5: <enum PK_ERROR_ENUM_GPG_FAILURE of type PackageKitGlib.ErrorEnum>, 6: <enum PK_ERROR_ENUM_PACKAGE_ID_INVALID of type PackageKitGlib.ErrorEnum>, 7: <enum PK_ERROR_ENUM_PACKAGE_NOT_INSTALLED of type PackageKitGlib.ErrorEnum>, 8: <enum PK_ERROR_ENUM_PACKAGE_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 9: <enum PK_ERROR_ENUM_PACKAGE_ALREADY_INSTALLED of type PackageKitGlib.ErrorEnum>, 10: <enum PK_ERROR_ENUM_PACKAGE_DOWNLOAD_FAILED of type PackageKitGlib.ErrorEnum>, 11: <enum PK_ERROR_ENUM_GROUP_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 12: <enum PK_ERROR_ENUM_GROUP_LIST_INVALID of type PackageKitGlib.ErrorEnum>, 13: <enum PK_ERROR_ENUM_DEP_RESOLUTION_FAILED of type PackageKitGlib.ErrorEnum>, 14: <enum PK_ERROR_ENUM_FILTER_INVALID of type PackageKitGlib.ErrorEnum>, 15: <enum PK_ERROR_ENUM_CREATE_THREAD_FAILED of type PackageKitGlib.ErrorEnum>, 16: <enum PK_ERROR_ENUM_TRANSACTION_ERROR of type PackageKitGlib.ErrorEnum>, 17: <enum PK_ERROR_ENUM_TRANSACTION_CANCELLED of type PackageKitGlib.ErrorEnum>, 18: <enum PK_ERROR_ENUM_NO_CACHE of type PackageKitGlib.ErrorEnum>, 19: <enum PK_ERROR_ENUM_REPO_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 20: <enum PK_ERROR_ENUM_CANNOT_REMOVE_SYSTEM_PACKAGE of type PackageKitGlib.ErrorEnum>, 21: <enum PK_ERROR_ENUM_PROCESS_KILL of type PackageKitGlib.ErrorEnum>, 22: <enum PK_ERROR_ENUM_FAILED_INITIALIZATION of type PackageKitGlib.ErrorEnum>, 23: <enum PK_ERROR_ENUM_FAILED_FINALISE of type PackageKitGlib.ErrorEnum>, 24: <enum PK_ERROR_ENUM_FAILED_CONFIG_PARSING of type PackageKitGlib.ErrorEnum>, 25: <enum PK_ERROR_ENUM_CANNOT_CANCEL of type PackageKitGlib.ErrorEnum>, 26: <enum PK_ERROR_ENUM_CANNOT_GET_LOCK of type PackageKitGlib.ErrorEnum>, 27: <enum PK_ERROR_ENUM_NO_PACKAGES_TO_UPDATE of type PackageKitGlib.ErrorEnum>, 28: <enum PK_ERROR_ENUM_CANNOT_WRITE_REPO_CONFIG of type PackageKitGlib.ErrorEnum>, 29: <enum PK_ERROR_ENUM_LOCAL_INSTALL_FAILED of type PackageKitGlib.ErrorEnum>, 30: <enum PK_ERROR_ENUM_BAD_GPG_SIGNATURE of type PackageKitGlib.ErrorEnum>, 31: <enum PK_ERROR_ENUM_MISSING_GPG_SIGNATURE of type PackageKitGlib.ErrorEnum>, 32: <enum PK_ERROR_ENUM_CANNOT_INSTALL_SOURCE_PACKAGE of type PackageKitGlib.ErrorEnum>, 33: <enum PK_ERROR_ENUM_REPO_CONFIGURATION_ERROR of type PackageKitGlib.ErrorEnum>, 34: <enum PK_ERROR_ENUM_NO_LICENSE_AGREEMENT of type PackageKitGlib.ErrorEnum>, 35: <enum PK_ERROR_ENUM_FILE_CONFLICTS of type PackageKitGlib.ErrorEnum>, 36: <enum PK_ERROR_ENUM_PACKAGE_CONFLICTS of type PackageKitGlib.ErrorEnum>, 37: <enum PK_ERROR_ENUM_REPO_NOT_AVAILABLE of type PackageKitGlib.ErrorEnum>, 38: <enum PK_ERROR_ENUM_INVALID_PACKAGE_FILE of type PackageKitGlib.ErrorEnum>, 39: <enum PK_ERROR_ENUM_PACKAGE_INSTALL_BLOCKED of type PackageKitGlib.ErrorEnum>, 40: <enum PK_ERROR_ENUM_PACKAGE_CORRUPT of type PackageKitGlib.ErrorEnum>, 41: <enum PK_ERROR_ENUM_ALL_PACKAGES_ALREADY_INSTALLED of type PackageKitGlib.ErrorEnum>, 42: <enum PK_ERROR_ENUM_FILE_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 43: <enum PK_ERROR_ENUM_NO_MORE_MIRRORS_TO_TRY of type PackageKitGlib.ErrorEnum>, 44: <enum PK_ERROR_ENUM_NO_DISTRO_UPGRADE_DATA of type PackageKitGlib.ErrorEnum>, 45: <enum PK_ERROR_ENUM_INCOMPATIBLE_ARCHITECTURE of type PackageKitGlib.ErrorEnum>, 46: <enum PK_ERROR_ENUM_NO_SPACE_ON_DEVICE of type PackageKitGlib.ErrorEnum>, 47: <enum PK_ERROR_ENUM_MEDIA_CHANGE_REQUIRED of type PackageKitGlib.ErrorEnum>, 48: <enum PK_ERROR_ENUM_NOT_AUTHORIZED of type PackageKitGlib.ErrorEnum>, 49: <enum PK_ERROR_ENUM_UPDATE_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 50: <enum PK_ERROR_ENUM_CANNOT_INSTALL_REPO_UNSIGNED of type PackageKitGlib.ErrorEnum>, 51: <enum PK_ERROR_ENUM_CANNOT_UPDATE_REPO_UNSIGNED of type PackageKitGlib.ErrorEnum>, 52: <enum PK_ERROR_ENUM_CANNOT_GET_FILELIST of type PackageKitGlib.ErrorEnum>, 53: <enum PK_ERROR_ENUM_CANNOT_GET_REQUIRES of type PackageKitGlib.ErrorEnum>, 54: <enum PK_ERROR_ENUM_CANNOT_DISABLE_REPOSITORY of type PackageKitGlib.ErrorEnum>, 55: <enum PK_ERROR_ENUM_RESTRICTED_DOWNLOAD of type PackageKitGlib.ErrorEnum>, 56: <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_CONFIGURE of type PackageKitGlib.ErrorEnum>, 57: <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_BUILD of type PackageKitGlib.ErrorEnum>, 58: <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_INSTALL of type PackageKitGlib.ErrorEnum>, 59: <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_REMOVE of type PackageKitGlib.ErrorEnum>, 60: <enum PK_ERROR_ENUM_UPDATE_FAILED_DUE_TO_RUNNING_PROCESS of type PackageKitGlib.ErrorEnum>, 61: <enum PK_ERROR_ENUM_PACKAGE_DATABASE_CHANGED of type PackageKitGlib.ErrorEnum>, 62: <enum PK_ERROR_ENUM_PROVIDE_TYPE_NOT_SUPPORTED of type PackageKitGlib.ErrorEnum>, 63: <enum PK_ERROR_ENUM_INSTALL_ROOT_INVALID of type PackageKitGlib.ErrorEnum>, 64: <enum PK_ERROR_ENUM_CANNOT_FETCH_SOURCES of type PackageKitGlib.ErrorEnum>, 65: <enum PK_ERROR_ENUM_CANCELLED_PRIORITY of type PackageKitGlib.ErrorEnum>, 66: <enum PK_ERROR_ENUM_UNFINISHED_TRANSACTION of type PackageKitGlib.ErrorEnum>, 67: <enum PK_ERROR_ENUM_LOCK_REQUIRED of type PackageKitGlib.ErrorEnum>, 68: <enum PK_ERROR_ENUM_REPO_ALREADY_SET of type PackageKitGlib.ErrorEnum>, 69: <enum PK_ERROR_ENUM_LAST of type PackageKitGlib.ErrorEnum>}, '__info__': gi.EnumInfo(ErrorEnum), 'UNKNOWN': <enum PK_ERROR_ENUM_UNKNOWN of type PackageKitGlib.ErrorEnum>, 'OOM': <enum PK_ERROR_ENUM_OOM of type PackageKitGlib.ErrorEnum>, 'NO_NETWORK': <enum PK_ERROR_ENUM_NO_NETWORK of type PackageKitGlib.ErrorEnum>, 'NOT_SUPPORTED': <enum PK_ERROR_ENUM_NOT_SUPPORTED of type PackageKitGlib.ErrorEnum>, 'INTERNAL_ERROR': <enum PK_ERROR_ENUM_INTERNAL_ERROR of type PackageKitGlib.ErrorEnum>, 'GPG_FAILURE': <enum PK_ERROR_ENUM_GPG_FAILURE of type PackageKitGlib.ErrorEnum>, 'PACKAGE_ID_INVALID': <enum PK_ERROR_ENUM_PACKAGE_ID_INVALID of type PackageKitGlib.ErrorEnum>, 'PACKAGE_NOT_INSTALLED': <enum PK_ERROR_ENUM_PACKAGE_NOT_INSTALLED of type PackageKitGlib.ErrorEnum>, 'PACKAGE_NOT_FOUND': <enum PK_ERROR_ENUM_PACKAGE_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 'PACKAGE_ALREADY_INSTALLED': <enum PK_ERROR_ENUM_PACKAGE_ALREADY_INSTALLED of type PackageKitGlib.ErrorEnum>, 'PACKAGE_DOWNLOAD_FAILED': <enum PK_ERROR_ENUM_PACKAGE_DOWNLOAD_FAILED of type PackageKitGlib.ErrorEnum>, 'GROUP_NOT_FOUND': <enum PK_ERROR_ENUM_GROUP_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 'GROUP_LIST_INVALID': <enum PK_ERROR_ENUM_GROUP_LIST_INVALID of type PackageKitGlib.ErrorEnum>, 'DEP_RESOLUTION_FAILED': <enum PK_ERROR_ENUM_DEP_RESOLUTION_FAILED of type PackageKitGlib.ErrorEnum>, 'FILTER_INVALID': <enum PK_ERROR_ENUM_FILTER_INVALID of type PackageKitGlib.ErrorEnum>, 'CREATE_THREAD_FAILED': <enum PK_ERROR_ENUM_CREATE_THREAD_FAILED of type PackageKitGlib.ErrorEnum>, 'TRANSACTION_ERROR': <enum PK_ERROR_ENUM_TRANSACTION_ERROR of type PackageKitGlib.ErrorEnum>, 'TRANSACTION_CANCELLED': <enum PK_ERROR_ENUM_TRANSACTION_CANCELLED of type PackageKitGlib.ErrorEnum>, 'NO_CACHE': <enum PK_ERROR_ENUM_NO_CACHE of type PackageKitGlib.ErrorEnum>, 'REPO_NOT_FOUND': <enum PK_ERROR_ENUM_REPO_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 'CANNOT_REMOVE_SYSTEM_PACKAGE': <enum PK_ERROR_ENUM_CANNOT_REMOVE_SYSTEM_PACKAGE of type PackageKitGlib.ErrorEnum>, 'PROCESS_KILL': <enum PK_ERROR_ENUM_PROCESS_KILL of type PackageKitGlib.ErrorEnum>, 'FAILED_INITIALIZATION': <enum PK_ERROR_ENUM_FAILED_INITIALIZATION of type PackageKitGlib.ErrorEnum>, 'FAILED_FINALISE': <enum PK_ERROR_ENUM_FAILED_FINALISE of type PackageKitGlib.ErrorEnum>, 'FAILED_CONFIG_PARSING': <enum PK_ERROR_ENUM_FAILED_CONFIG_PARSING of type PackageKitGlib.ErrorEnum>, 'CANNOT_CANCEL': <enum PK_ERROR_ENUM_CANNOT_CANCEL of type PackageKitGlib.ErrorEnum>, 'CANNOT_GET_LOCK': <enum PK_ERROR_ENUM_CANNOT_GET_LOCK of type PackageKitGlib.ErrorEnum>, 'NO_PACKAGES_TO_UPDATE': <enum PK_ERROR_ENUM_NO_PACKAGES_TO_UPDATE of type PackageKitGlib.ErrorEnum>, 'CANNOT_WRITE_REPO_CONFIG': <enum PK_ERROR_ENUM_CANNOT_WRITE_REPO_CONFIG of type PackageKitGlib.ErrorEnum>, 'LOCAL_INSTALL_FAILED': <enum PK_ERROR_ENUM_LOCAL_INSTALL_FAILED of type PackageKitGlib.ErrorEnum>, 'BAD_GPG_SIGNATURE': <enum PK_ERROR_ENUM_BAD_GPG_SIGNATURE of type PackageKitGlib.ErrorEnum>, 'MISSING_GPG_SIGNATURE': <enum PK_ERROR_ENUM_MISSING_GPG_SIGNATURE of type PackageKitGlib.ErrorEnum>, 'CANNOT_INSTALL_SOURCE_PACKAGE': <enum PK_ERROR_ENUM_CANNOT_INSTALL_SOURCE_PACKAGE of type PackageKitGlib.ErrorEnum>, 'REPO_CONFIGURATION_ERROR': <enum PK_ERROR_ENUM_REPO_CONFIGURATION_ERROR of type PackageKitGlib.ErrorEnum>, 'NO_LICENSE_AGREEMENT': <enum PK_ERROR_ENUM_NO_LICENSE_AGREEMENT of type PackageKitGlib.ErrorEnum>, 'FILE_CONFLICTS': <enum PK_ERROR_ENUM_FILE_CONFLICTS of type PackageKitGlib.ErrorEnum>, 'PACKAGE_CONFLICTS': <enum PK_ERROR_ENUM_PACKAGE_CONFLICTS of type PackageKitGlib.ErrorEnum>, 'REPO_NOT_AVAILABLE': <enum PK_ERROR_ENUM_REPO_NOT_AVAILABLE of type PackageKitGlib.ErrorEnum>, 'INVALID_PACKAGE_FILE': <enum PK_ERROR_ENUM_INVALID_PACKAGE_FILE of type PackageKitGlib.ErrorEnum>, 'PACKAGE_INSTALL_BLOCKED': <enum PK_ERROR_ENUM_PACKAGE_INSTALL_BLOCKED of type PackageKitGlib.ErrorEnum>, 'PACKAGE_CORRUPT': <enum PK_ERROR_ENUM_PACKAGE_CORRUPT of type PackageKitGlib.ErrorEnum>, 'ALL_PACKAGES_ALREADY_INSTALLED': <enum PK_ERROR_ENUM_ALL_PACKAGES_ALREADY_INSTALLED of type PackageKitGlib.ErrorEnum>, 'FILE_NOT_FOUND': <enum PK_ERROR_ENUM_FILE_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 'NO_MORE_MIRRORS_TO_TRY': <enum PK_ERROR_ENUM_NO_MORE_MIRRORS_TO_TRY of type PackageKitGlib.ErrorEnum>, 'NO_DISTRO_UPGRADE_DATA': <enum PK_ERROR_ENUM_NO_DISTRO_UPGRADE_DATA of type PackageKitGlib.ErrorEnum>, 'INCOMPATIBLE_ARCHITECTURE': <enum PK_ERROR_ENUM_INCOMPATIBLE_ARCHITECTURE of type PackageKitGlib.ErrorEnum>, 'NO_SPACE_ON_DEVICE': <enum PK_ERROR_ENUM_NO_SPACE_ON_DEVICE of type PackageKitGlib.ErrorEnum>, 'MEDIA_CHANGE_REQUIRED': <enum PK_ERROR_ENUM_MEDIA_CHANGE_REQUIRED of type PackageKitGlib.ErrorEnum>, 'NOT_AUTHORIZED': <enum PK_ERROR_ENUM_NOT_AUTHORIZED of type PackageKitGlib.ErrorEnum>, 'UPDATE_NOT_FOUND': <enum PK_ERROR_ENUM_UPDATE_NOT_FOUND of type PackageKitGlib.ErrorEnum>, 'CANNOT_INSTALL_REPO_UNSIGNED': <enum PK_ERROR_ENUM_CANNOT_INSTALL_REPO_UNSIGNED of type PackageKitGlib.ErrorEnum>, 'CANNOT_UPDATE_REPO_UNSIGNED': <enum PK_ERROR_ENUM_CANNOT_UPDATE_REPO_UNSIGNED of type PackageKitGlib.ErrorEnum>, 'CANNOT_GET_FILELIST': <enum PK_ERROR_ENUM_CANNOT_GET_FILELIST of type PackageKitGlib.ErrorEnum>, 'CANNOT_GET_REQUIRES': <enum PK_ERROR_ENUM_CANNOT_GET_REQUIRES of type PackageKitGlib.ErrorEnum>, 'CANNOT_DISABLE_REPOSITORY': <enum PK_ERROR_ENUM_CANNOT_DISABLE_REPOSITORY of type PackageKitGlib.ErrorEnum>, 'RESTRICTED_DOWNLOAD': <enum PK_ERROR_ENUM_RESTRICTED_DOWNLOAD of type PackageKitGlib.ErrorEnum>, 'PACKAGE_FAILED_TO_CONFIGURE': <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_CONFIGURE of type PackageKitGlib.ErrorEnum>, 'PACKAGE_FAILED_TO_BUILD': <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_BUILD of type PackageKitGlib.ErrorEnum>, 'PACKAGE_FAILED_TO_INSTALL': <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_INSTALL of type PackageKitGlib.ErrorEnum>, 'PACKAGE_FAILED_TO_REMOVE': <enum PK_ERROR_ENUM_PACKAGE_FAILED_TO_REMOVE of type PackageKitGlib.ErrorEnum>, 'UPDATE_FAILED_DUE_TO_RUNNING_PROCESS': <enum PK_ERROR_ENUM_UPDATE_FAILED_DUE_TO_RUNNING_PROCESS of type PackageKitGlib.ErrorEnum>, 'PACKAGE_DATABASE_CHANGED': <enum PK_ERROR_ENUM_PACKAGE_DATABASE_CHANGED of type PackageKitGlib.ErrorEnum>, 'PROVIDE_TYPE_NOT_SUPPORTED': <enum PK_ERROR_ENUM_PROVIDE_TYPE_NOT_SUPPORTED of type PackageKitGlib.ErrorEnum>, 'INSTALL_ROOT_INVALID': <enum PK_ERROR_ENUM_INSTALL_ROOT_INVALID of type PackageKitGlib.ErrorEnum>, 'CANNOT_FETCH_SOURCES': <enum PK_ERROR_ENUM_CANNOT_FETCH_SOURCES of type PackageKitGlib.ErrorEnum>, 'CANCELLED_PRIORITY': <enum PK_ERROR_ENUM_CANCELLED_PRIORITY of type PackageKitGlib.ErrorEnum>, 'UNFINISHED_TRANSACTION': <enum PK_ERROR_ENUM_UNFINISHED_TRANSACTION of type PackageKitGlib.ErrorEnum>, 'LOCK_REQUIRED': <enum PK_ERROR_ENUM_LOCK_REQUIRED of type PackageKitGlib.ErrorEnum>, 'REPO_ALREADY_SET': <enum PK_ERROR_ENUM_REPO_ALREADY_SET of type PackageKitGlib.ErrorEnum>, 'LAST': <enum PK_ERROR_ENUM_LAST of type PackageKitGlib.ErrorEnum>, 'from_string': gi.FunctionInfo(from_string), 'to_string': gi.FunctionInfo(to_string)})"
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
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        44: 44,
        45: 45,
        46: 46,
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
    }
    __gtype__ = None # (!) real value is '<GType PkErrorEnum (94016447057232)>'
    __info__ = gi.EnumInfo(ErrorEnum)


