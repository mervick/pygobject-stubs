# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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


class Error(__gobject.GEnum):
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

    def quark(self): # real signature unknown; restored from __doc__
        """ quark() -> int """
        return 0

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


    ALREADY_CANCELLED = 2
    ALREADY_MOUNTED = 6
    ALREADY_UNMOUNTING = 10
    CANCELLED = 1
    DEVICE_BUSY = 14
    FAILED = 0
    ISCSI_DAEMON_TRANSPORT_FAILED = 15
    ISCSI_HOST_NOT_FOUND = 16
    ISCSI_IDMB = 17
    ISCSI_LOGIN_AUTH_FAILED = 19
    ISCSI_LOGIN_FAILED = 18
    ISCSI_LOGIN_FATAL = 20
    ISCSI_LOGOUT_FAILED = 21
    ISCSI_NOT_CONNECTED = 24
    ISCSI_NO_FIRMWARE = 22
    ISCSI_NO_OBJECTS_FOUND = 23
    ISCSI_TRANSPORT_FAILED = 25
    ISCSI_UNKNOWN_DISCOVERY_TYPE = 26
    MOUNTED_BY_OTHER_USER = 9
    NOT_AUTHORIZED = 3
    NOT_AUTHORIZED_CAN_OBTAIN = 4
    NOT_AUTHORIZED_DISMISSED = 5
    NOT_MOUNTED = 7
    NOT_SUPPORTED = 11
    OPTION_NOT_PERMITTED = 8
    TIMED_OUT = 12
    WOULD_WAKEUP = 13
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.UDisks', '__dict__': <attribute '__dict__' of 'Error' objects>, '__doc__': None, '__gtype__': <GType UDisksError (93969722286416)>, '__enum_values__': {0: <enum UDISKS_ERROR_FAILED of type UDisks.Error>, 1: <enum UDISKS_ERROR_CANCELLED of type UDisks.Error>, 2: <enum UDISKS_ERROR_ALREADY_CANCELLED of type UDisks.Error>, 3: <enum UDISKS_ERROR_NOT_AUTHORIZED of type UDisks.Error>, 4: <enum UDISKS_ERROR_NOT_AUTHORIZED_CAN_OBTAIN of type UDisks.Error>, 5: <enum UDISKS_ERROR_NOT_AUTHORIZED_DISMISSED of type UDisks.Error>, 6: <enum UDISKS_ERROR_ALREADY_MOUNTED of type UDisks.Error>, 7: <enum UDISKS_ERROR_NOT_MOUNTED of type UDisks.Error>, 8: <enum UDISKS_ERROR_OPTION_NOT_PERMITTED of type UDisks.Error>, 9: <enum UDISKS_ERROR_MOUNTED_BY_OTHER_USER of type UDisks.Error>, 10: <enum UDISKS_ERROR_ALREADY_UNMOUNTING of type UDisks.Error>, 11: <enum UDISKS_ERROR_NOT_SUPPORTED of type UDisks.Error>, 12: <enum UDISKS_ERROR_TIMED_OUT of type UDisks.Error>, 13: <enum UDISKS_ERROR_WOULD_WAKEUP of type UDisks.Error>, 14: <enum UDISKS_ERROR_DEVICE_BUSY of type UDisks.Error>, 15: <enum UDISKS_ERROR_ISCSI_DAEMON_TRANSPORT_FAILED of type UDisks.Error>, 16: <enum UDISKS_ERROR_ISCSI_HOST_NOT_FOUND of type UDisks.Error>, 17: <enum UDISKS_ERROR_ISCSI_IDMB of type UDisks.Error>, 18: <enum UDISKS_ERROR_ISCSI_LOGIN_FAILED of type UDisks.Error>, 19: <enum UDISKS_ERROR_ISCSI_LOGIN_AUTH_FAILED of type UDisks.Error>, 20: <enum UDISKS_ERROR_ISCSI_LOGIN_FATAL of type UDisks.Error>, 21: <enum UDISKS_ERROR_ISCSI_LOGOUT_FAILED of type UDisks.Error>, 22: <enum UDISKS_ERROR_ISCSI_NO_FIRMWARE of type UDisks.Error>, 23: <enum UDISKS_ERROR_ISCSI_NO_OBJECTS_FOUND of type UDisks.Error>, 24: <enum UDISKS_ERROR_ISCSI_NOT_CONNECTED of type UDisks.Error>, 25: <enum UDISKS_ERROR_ISCSI_TRANSPORT_FAILED of type UDisks.Error>, 26: <enum UDISKS_ERROR_ISCSI_UNKNOWN_DISCOVERY_TYPE of type UDisks.Error>}, '__info__': gi.EnumInfo(Error), 'FAILED': <enum UDISKS_ERROR_FAILED of type UDisks.Error>, 'CANCELLED': <enum UDISKS_ERROR_CANCELLED of type UDisks.Error>, 'ALREADY_CANCELLED': <enum UDISKS_ERROR_ALREADY_CANCELLED of type UDisks.Error>, 'NOT_AUTHORIZED': <enum UDISKS_ERROR_NOT_AUTHORIZED of type UDisks.Error>, 'NOT_AUTHORIZED_CAN_OBTAIN': <enum UDISKS_ERROR_NOT_AUTHORIZED_CAN_OBTAIN of type UDisks.Error>, 'NOT_AUTHORIZED_DISMISSED': <enum UDISKS_ERROR_NOT_AUTHORIZED_DISMISSED of type UDisks.Error>, 'ALREADY_MOUNTED': <enum UDISKS_ERROR_ALREADY_MOUNTED of type UDisks.Error>, 'NOT_MOUNTED': <enum UDISKS_ERROR_NOT_MOUNTED of type UDisks.Error>, 'OPTION_NOT_PERMITTED': <enum UDISKS_ERROR_OPTION_NOT_PERMITTED of type UDisks.Error>, 'MOUNTED_BY_OTHER_USER': <enum UDISKS_ERROR_MOUNTED_BY_OTHER_USER of type UDisks.Error>, 'ALREADY_UNMOUNTING': <enum UDISKS_ERROR_ALREADY_UNMOUNTING of type UDisks.Error>, 'NOT_SUPPORTED': <enum UDISKS_ERROR_NOT_SUPPORTED of type UDisks.Error>, 'TIMED_OUT': <enum UDISKS_ERROR_TIMED_OUT of type UDisks.Error>, 'WOULD_WAKEUP': <enum UDISKS_ERROR_WOULD_WAKEUP of type UDisks.Error>, 'DEVICE_BUSY': <enum UDISKS_ERROR_DEVICE_BUSY of type UDisks.Error>, 'ISCSI_DAEMON_TRANSPORT_FAILED': <enum UDISKS_ERROR_ISCSI_DAEMON_TRANSPORT_FAILED of type UDisks.Error>, 'ISCSI_HOST_NOT_FOUND': <enum UDISKS_ERROR_ISCSI_HOST_NOT_FOUND of type UDisks.Error>, 'ISCSI_IDMB': <enum UDISKS_ERROR_ISCSI_IDMB of type UDisks.Error>, 'ISCSI_LOGIN_FAILED': <enum UDISKS_ERROR_ISCSI_LOGIN_FAILED of type UDisks.Error>, 'ISCSI_LOGIN_AUTH_FAILED': <enum UDISKS_ERROR_ISCSI_LOGIN_AUTH_FAILED of type UDisks.Error>, 'ISCSI_LOGIN_FATAL': <enum UDISKS_ERROR_ISCSI_LOGIN_FATAL of type UDisks.Error>, 'ISCSI_LOGOUT_FAILED': <enum UDISKS_ERROR_ISCSI_LOGOUT_FAILED of type UDisks.Error>, 'ISCSI_NO_FIRMWARE': <enum UDISKS_ERROR_ISCSI_NO_FIRMWARE of type UDisks.Error>, 'ISCSI_NO_OBJECTS_FOUND': <enum UDISKS_ERROR_ISCSI_NO_OBJECTS_FOUND of type UDisks.Error>, 'ISCSI_NOT_CONNECTED': <enum UDISKS_ERROR_ISCSI_NOT_CONNECTED of type UDisks.Error>, 'ISCSI_TRANSPORT_FAILED': <enum UDISKS_ERROR_ISCSI_TRANSPORT_FAILED of type UDisks.Error>, 'ISCSI_UNKNOWN_DISCOVERY_TYPE': <enum UDISKS_ERROR_ISCSI_UNKNOWN_DISCOVERY_TYPE of type UDisks.Error>, 'quark': gi.FunctionInfo(quark)})"
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
    __gtype__ = None # (!) real value is '<GType UDisksError (93969722286416)>'
    __info__ = gi.EnumInfo(Error)


