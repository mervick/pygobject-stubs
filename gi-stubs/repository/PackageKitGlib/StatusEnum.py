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


class StatusEnum(__gobject.GEnum):
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

    def from_string(self, status): # real signature unknown; restored from __doc__
        """ from_string(status:str) -> PackageKitGlib.StatusEnum """
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

    def to_localised_text(self, status): # real signature unknown; restored from __doc__
        """ to_localised_text(status:PackageKitGlib.StatusEnum) -> str """
        return ""

    def to_string(self, status): # real signature unknown; restored from __doc__
        """ to_string(status:PackageKitGlib.StatusEnum) -> str """
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


    CANCEL = 19
    CHECK_EXECUTABLE_FILES = 33
    CHECK_LIBRARIES = 34
    CLEANUP = 11
    COMMIT = 16
    COPY_FILES = 35
    DEP_RESOLVE = 13
    DOWNLOAD = 8
    DOWNLOAD_CHANGELOG = 23
    DOWNLOAD_FILELIST = 22
    DOWNLOAD_GROUP = 24
    DOWNLOAD_PACKAGELIST = 21
    DOWNLOAD_REPOSITORY = 20
    DOWNLOAD_UPDATEINFO = 25
    FINISHED = 18
    GENERATE_PACKAGE_LIST = 29
    INFO = 5
    INSTALL = 9
    LAST = 37
    LOADING_CACHE = 27
    OBSOLETE = 12
    QUERY = 4
    REFRESH_CACHE = 7
    REMOVE = 6
    REPACKAGING = 26
    REQUEST = 17
    RUNNING = 3
    RUN_HOOK = 36
    SCAN_APPLICATIONS = 28
    SCAN_PROCESS_LIST = 32
    SETUP = 2
    SIG_CHECK = 14
    TEST_COMMIT = 15
    UNKNOWN = 0
    UPDATE = 10
    WAIT = 1
    WAITING_FOR_AUTH = 31
    WAITING_FOR_LOCK = 30
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.PackageKitGlib', '__dict__': <attribute '__dict__' of 'StatusEnum' objects>, '__doc__': None, '__gtype__': <GType PkStatusEnum (94016447474032)>, '__enum_values__': {0: <enum PK_STATUS_ENUM_UNKNOWN of type PackageKitGlib.StatusEnum>, 1: <enum PK_STATUS_ENUM_WAIT of type PackageKitGlib.StatusEnum>, 2: <enum PK_STATUS_ENUM_SETUP of type PackageKitGlib.StatusEnum>, 3: <enum PK_STATUS_ENUM_RUNNING of type PackageKitGlib.StatusEnum>, 4: <enum PK_STATUS_ENUM_QUERY of type PackageKitGlib.StatusEnum>, 5: <enum PK_STATUS_ENUM_INFO of type PackageKitGlib.StatusEnum>, 6: <enum PK_STATUS_ENUM_REMOVE of type PackageKitGlib.StatusEnum>, 7: <enum PK_STATUS_ENUM_REFRESH_CACHE of type PackageKitGlib.StatusEnum>, 8: <enum PK_STATUS_ENUM_DOWNLOAD of type PackageKitGlib.StatusEnum>, 9: <enum PK_STATUS_ENUM_INSTALL of type PackageKitGlib.StatusEnum>, 10: <enum PK_STATUS_ENUM_UPDATE of type PackageKitGlib.StatusEnum>, 11: <enum PK_STATUS_ENUM_CLEANUP of type PackageKitGlib.StatusEnum>, 12: <enum PK_STATUS_ENUM_OBSOLETE of type PackageKitGlib.StatusEnum>, 13: <enum PK_STATUS_ENUM_DEP_RESOLVE of type PackageKitGlib.StatusEnum>, 14: <enum PK_STATUS_ENUM_SIG_CHECK of type PackageKitGlib.StatusEnum>, 15: <enum PK_STATUS_ENUM_TEST_COMMIT of type PackageKitGlib.StatusEnum>, 16: <enum PK_STATUS_ENUM_COMMIT of type PackageKitGlib.StatusEnum>, 17: <enum PK_STATUS_ENUM_REQUEST of type PackageKitGlib.StatusEnum>, 18: <enum PK_STATUS_ENUM_FINISHED of type PackageKitGlib.StatusEnum>, 19: <enum PK_STATUS_ENUM_CANCEL of type PackageKitGlib.StatusEnum>, 20: <enum PK_STATUS_ENUM_DOWNLOAD_REPOSITORY of type PackageKitGlib.StatusEnum>, 21: <enum PK_STATUS_ENUM_DOWNLOAD_PACKAGELIST of type PackageKitGlib.StatusEnum>, 22: <enum PK_STATUS_ENUM_DOWNLOAD_FILELIST of type PackageKitGlib.StatusEnum>, 23: <enum PK_STATUS_ENUM_DOWNLOAD_CHANGELOG of type PackageKitGlib.StatusEnum>, 24: <enum PK_STATUS_ENUM_DOWNLOAD_GROUP of type PackageKitGlib.StatusEnum>, 25: <enum PK_STATUS_ENUM_DOWNLOAD_UPDATEINFO of type PackageKitGlib.StatusEnum>, 26: <enum PK_STATUS_ENUM_REPACKAGING of type PackageKitGlib.StatusEnum>, 27: <enum PK_STATUS_ENUM_LOADING_CACHE of type PackageKitGlib.StatusEnum>, 28: <enum PK_STATUS_ENUM_SCAN_APPLICATIONS of type PackageKitGlib.StatusEnum>, 29: <enum PK_STATUS_ENUM_GENERATE_PACKAGE_LIST of type PackageKitGlib.StatusEnum>, 30: <enum PK_STATUS_ENUM_WAITING_FOR_LOCK of type PackageKitGlib.StatusEnum>, 31: <enum PK_STATUS_ENUM_WAITING_FOR_AUTH of type PackageKitGlib.StatusEnum>, 32: <enum PK_STATUS_ENUM_SCAN_PROCESS_LIST of type PackageKitGlib.StatusEnum>, 33: <enum PK_STATUS_ENUM_CHECK_EXECUTABLE_FILES of type PackageKitGlib.StatusEnum>, 34: <enum PK_STATUS_ENUM_CHECK_LIBRARIES of type PackageKitGlib.StatusEnum>, 35: <enum PK_STATUS_ENUM_COPY_FILES of type PackageKitGlib.StatusEnum>, 36: <enum PK_STATUS_ENUM_RUN_HOOK of type PackageKitGlib.StatusEnum>, 37: <enum PK_STATUS_ENUM_LAST of type PackageKitGlib.StatusEnum>}, '__info__': gi.EnumInfo(StatusEnum), 'UNKNOWN': <enum PK_STATUS_ENUM_UNKNOWN of type PackageKitGlib.StatusEnum>, 'WAIT': <enum PK_STATUS_ENUM_WAIT of type PackageKitGlib.StatusEnum>, 'SETUP': <enum PK_STATUS_ENUM_SETUP of type PackageKitGlib.StatusEnum>, 'RUNNING': <enum PK_STATUS_ENUM_RUNNING of type PackageKitGlib.StatusEnum>, 'QUERY': <enum PK_STATUS_ENUM_QUERY of type PackageKitGlib.StatusEnum>, 'INFO': <enum PK_STATUS_ENUM_INFO of type PackageKitGlib.StatusEnum>, 'REMOVE': <enum PK_STATUS_ENUM_REMOVE of type PackageKitGlib.StatusEnum>, 'REFRESH_CACHE': <enum PK_STATUS_ENUM_REFRESH_CACHE of type PackageKitGlib.StatusEnum>, 'DOWNLOAD': <enum PK_STATUS_ENUM_DOWNLOAD of type PackageKitGlib.StatusEnum>, 'INSTALL': <enum PK_STATUS_ENUM_INSTALL of type PackageKitGlib.StatusEnum>, 'UPDATE': <enum PK_STATUS_ENUM_UPDATE of type PackageKitGlib.StatusEnum>, 'CLEANUP': <enum PK_STATUS_ENUM_CLEANUP of type PackageKitGlib.StatusEnum>, 'OBSOLETE': <enum PK_STATUS_ENUM_OBSOLETE of type PackageKitGlib.StatusEnum>, 'DEP_RESOLVE': <enum PK_STATUS_ENUM_DEP_RESOLVE of type PackageKitGlib.StatusEnum>, 'SIG_CHECK': <enum PK_STATUS_ENUM_SIG_CHECK of type PackageKitGlib.StatusEnum>, 'TEST_COMMIT': <enum PK_STATUS_ENUM_TEST_COMMIT of type PackageKitGlib.StatusEnum>, 'COMMIT': <enum PK_STATUS_ENUM_COMMIT of type PackageKitGlib.StatusEnum>, 'REQUEST': <enum PK_STATUS_ENUM_REQUEST of type PackageKitGlib.StatusEnum>, 'FINISHED': <enum PK_STATUS_ENUM_FINISHED of type PackageKitGlib.StatusEnum>, 'CANCEL': <enum PK_STATUS_ENUM_CANCEL of type PackageKitGlib.StatusEnum>, 'DOWNLOAD_REPOSITORY': <enum PK_STATUS_ENUM_DOWNLOAD_REPOSITORY of type PackageKitGlib.StatusEnum>, 'DOWNLOAD_PACKAGELIST': <enum PK_STATUS_ENUM_DOWNLOAD_PACKAGELIST of type PackageKitGlib.StatusEnum>, 'DOWNLOAD_FILELIST': <enum PK_STATUS_ENUM_DOWNLOAD_FILELIST of type PackageKitGlib.StatusEnum>, 'DOWNLOAD_CHANGELOG': <enum PK_STATUS_ENUM_DOWNLOAD_CHANGELOG of type PackageKitGlib.StatusEnum>, 'DOWNLOAD_GROUP': <enum PK_STATUS_ENUM_DOWNLOAD_GROUP of type PackageKitGlib.StatusEnum>, 'DOWNLOAD_UPDATEINFO': <enum PK_STATUS_ENUM_DOWNLOAD_UPDATEINFO of type PackageKitGlib.StatusEnum>, 'REPACKAGING': <enum PK_STATUS_ENUM_REPACKAGING of type PackageKitGlib.StatusEnum>, 'LOADING_CACHE': <enum PK_STATUS_ENUM_LOADING_CACHE of type PackageKitGlib.StatusEnum>, 'SCAN_APPLICATIONS': <enum PK_STATUS_ENUM_SCAN_APPLICATIONS of type PackageKitGlib.StatusEnum>, 'GENERATE_PACKAGE_LIST': <enum PK_STATUS_ENUM_GENERATE_PACKAGE_LIST of type PackageKitGlib.StatusEnum>, 'WAITING_FOR_LOCK': <enum PK_STATUS_ENUM_WAITING_FOR_LOCK of type PackageKitGlib.StatusEnum>, 'WAITING_FOR_AUTH': <enum PK_STATUS_ENUM_WAITING_FOR_AUTH of type PackageKitGlib.StatusEnum>, 'SCAN_PROCESS_LIST': <enum PK_STATUS_ENUM_SCAN_PROCESS_LIST of type PackageKitGlib.StatusEnum>, 'CHECK_EXECUTABLE_FILES': <enum PK_STATUS_ENUM_CHECK_EXECUTABLE_FILES of type PackageKitGlib.StatusEnum>, 'CHECK_LIBRARIES': <enum PK_STATUS_ENUM_CHECK_LIBRARIES of type PackageKitGlib.StatusEnum>, 'COPY_FILES': <enum PK_STATUS_ENUM_COPY_FILES of type PackageKitGlib.StatusEnum>, 'RUN_HOOK': <enum PK_STATUS_ENUM_RUN_HOOK of type PackageKitGlib.StatusEnum>, 'LAST': <enum PK_STATUS_ENUM_LAST of type PackageKitGlib.StatusEnum>, 'from_string': gi.FunctionInfo(from_string), 'to_localised_text': gi.FunctionInfo(to_localised_text), 'to_string': gi.FunctionInfo(to_string)})"
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
    }
    __gtype__ = None # (!) real value is '<GType PkStatusEnum (94016447474032)>'
    __info__ = gi.EnumInfo(StatusEnum)


