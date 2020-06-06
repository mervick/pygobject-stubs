# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class DeviceStateReason(__gobject.GEnum):
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


    AUTOIP_ERROR = 21
    AUTOIP_FAILED = 22
    AUTOIP_START_FAILED = 20
    BR2684_FAILED = 51
    BT_FAILED = 44
    CARRIER = 40
    CONFIG_FAILED = 4
    CONNECTION_ASSUMED = 41
    CONNECTION_REMOVED = 38
    DCB_FCOE_FAILED = 55
    DEPENDENCY_FAILED = 50
    DHCP_ERROR = 16
    DHCP_FAILED = 17
    DHCP_START_FAILED = 15
    FIRMWARE_MISSING = 35
    GSM_APN_FAILED = 29
    GSM_PIN_CHECK_FAILED = 34
    GSM_REGISTRATION_DENIED = 31
    GSM_REGISTRATION_FAILED = 33
    GSM_REGISTRATION_NOT_SEARCHING = 30
    GSM_REGISTRATION_TIMEOUT = 32
    GSM_SIM_NOT_INSERTED = 45
    GSM_SIM_PIN_REQUIRED = 46
    GSM_SIM_PUK_REQUIRED = 47
    GSM_SIM_WRONG = 48
    INFINIBAND_MODE = 49
    IP_ADDRESS_DUPLICATE = 64
    IP_CONFIG_EXPIRED = 6
    IP_CONFIG_UNAVAILABLE = 5
    IP_METHOD_UNSUPPORTED = 65
    MODEM_AVAILABLE = 58
    MODEM_BUSY = 23
    MODEM_DIAL_FAILED = 27
    MODEM_DIAL_TIMEOUT = 26
    MODEM_FAILED = 57
    MODEM_INIT_FAILED = 28
    MODEM_MANAGER_UNAVAILABLE = 52
    MODEM_NOT_FOUND = 43
    MODEM_NO_CARRIER = 25
    MODEM_NO_DIAL_TONE = 24
    NEW_ACTIVATION = 60
    NONE = 0
    NOW_MANAGED = 2
    NOW_UNMANAGED = 3
    NO_SECRETS = 7
    OVSDB_FAILED = 63
    PARENT_CHANGED = 61
    PARENT_MANAGED_CHANGED = 62
    PEER_NOT_FOUND = 67
    PPP_DISCONNECT = 13
    PPP_FAILED = 14
    PPP_START_FAILED = 12
    REMOVED = 36
    SECONDARY_CONNECTION_FAILED = 54
    SHARED_FAILED = 19
    SHARED_START_FAILED = 18
    SIM_PIN_INCORRECT = 59
    SLEEPING = 37
    SRIOV_CONFIGURATION_FAILED = 66
    SSID_NOT_FOUND = 53
    SUPPLICANT_AVAILABLE = 42
    SUPPLICANT_CONFIG_FAILED = 9
    SUPPLICANT_DISCONNECT = 8
    SUPPLICANT_FAILED = 10
    SUPPLICANT_TIMEOUT = 11
    TEAMD_CONTROL_FAILED = 56
    UNKNOWN = 1
    USER_REQUESTED = 39
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.NM', '__dict__': <attribute '__dict__' of 'DeviceStateReason' objects>, '__doc__': None, '__gtype__': <GType NMDeviceStateReason (94741104198640)>, '__enum_values__': {0: <enum NM_DEVICE_STATE_REASON_NONE of type NM.DeviceStateReason>, 1: <enum NM_DEVICE_STATE_REASON_UNKNOWN of type NM.DeviceStateReason>, 2: <enum NM_DEVICE_STATE_REASON_NOW_MANAGED of type NM.DeviceStateReason>, 3: <enum NM_DEVICE_STATE_REASON_NOW_UNMANAGED of type NM.DeviceStateReason>, 4: <enum NM_DEVICE_STATE_REASON_CONFIG_FAILED of type NM.DeviceStateReason>, 5: <enum NM_DEVICE_STATE_REASON_IP_CONFIG_UNAVAILABLE of type NM.DeviceStateReason>, 6: <enum NM_DEVICE_STATE_REASON_IP_CONFIG_EXPIRED of type NM.DeviceStateReason>, 7: <enum NM_DEVICE_STATE_REASON_NO_SECRETS of type NM.DeviceStateReason>, 8: <enum NM_DEVICE_STATE_REASON_SUPPLICANT_DISCONNECT of type NM.DeviceStateReason>, 9: <enum NM_DEVICE_STATE_REASON_SUPPLICANT_CONFIG_FAILED of type NM.DeviceStateReason>, 10: <enum NM_DEVICE_STATE_REASON_SUPPLICANT_FAILED of type NM.DeviceStateReason>, 11: <enum NM_DEVICE_STATE_REASON_SUPPLICANT_TIMEOUT of type NM.DeviceStateReason>, 12: <enum NM_DEVICE_STATE_REASON_PPP_START_FAILED of type NM.DeviceStateReason>, 13: <enum NM_DEVICE_STATE_REASON_PPP_DISCONNECT of type NM.DeviceStateReason>, 14: <enum NM_DEVICE_STATE_REASON_PPP_FAILED of type NM.DeviceStateReason>, 15: <enum NM_DEVICE_STATE_REASON_DHCP_START_FAILED of type NM.DeviceStateReason>, 16: <enum NM_DEVICE_STATE_REASON_DHCP_ERROR of type NM.DeviceStateReason>, 17: <enum NM_DEVICE_STATE_REASON_DHCP_FAILED of type NM.DeviceStateReason>, 18: <enum NM_DEVICE_STATE_REASON_SHARED_START_FAILED of type NM.DeviceStateReason>, 19: <enum NM_DEVICE_STATE_REASON_SHARED_FAILED of type NM.DeviceStateReason>, 20: <enum NM_DEVICE_STATE_REASON_AUTOIP_START_FAILED of type NM.DeviceStateReason>, 21: <enum NM_DEVICE_STATE_REASON_AUTOIP_ERROR of type NM.DeviceStateReason>, 22: <enum NM_DEVICE_STATE_REASON_AUTOIP_FAILED of type NM.DeviceStateReason>, 23: <enum NM_DEVICE_STATE_REASON_MODEM_BUSY of type NM.DeviceStateReason>, 24: <enum NM_DEVICE_STATE_REASON_MODEM_NO_DIAL_TONE of type NM.DeviceStateReason>, 25: <enum NM_DEVICE_STATE_REASON_MODEM_NO_CARRIER of type NM.DeviceStateReason>, 26: <enum NM_DEVICE_STATE_REASON_MODEM_DIAL_TIMEOUT of type NM.DeviceStateReason>, 27: <enum NM_DEVICE_STATE_REASON_MODEM_DIAL_FAILED of type NM.DeviceStateReason>, 28: <enum NM_DEVICE_STATE_REASON_MODEM_INIT_FAILED of type NM.DeviceStateReason>, 29: <enum NM_DEVICE_STATE_REASON_GSM_APN_FAILED of type NM.DeviceStateReason>, 30: <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_NOT_SEARCHING of type NM.DeviceStateReason>, 31: <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_DENIED of type NM.DeviceStateReason>, 32: <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_TIMEOUT of type NM.DeviceStateReason>, 33: <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_FAILED of type NM.DeviceStateReason>, 34: <enum NM_DEVICE_STATE_REASON_GSM_PIN_CHECK_FAILED of type NM.DeviceStateReason>, 35: <enum NM_DEVICE_STATE_REASON_FIRMWARE_MISSING of type NM.DeviceStateReason>, 36: <enum NM_DEVICE_STATE_REASON_REMOVED of type NM.DeviceStateReason>, 37: <enum NM_DEVICE_STATE_REASON_SLEEPING of type NM.DeviceStateReason>, 38: <enum NM_DEVICE_STATE_REASON_CONNECTION_REMOVED of type NM.DeviceStateReason>, 39: <enum NM_DEVICE_STATE_REASON_USER_REQUESTED of type NM.DeviceStateReason>, 40: <enum NM_DEVICE_STATE_REASON_CARRIER of type NM.DeviceStateReason>, 41: <enum NM_DEVICE_STATE_REASON_CONNECTION_ASSUMED of type NM.DeviceStateReason>, 42: <enum NM_DEVICE_STATE_REASON_SUPPLICANT_AVAILABLE of type NM.DeviceStateReason>, 43: <enum NM_DEVICE_STATE_REASON_MODEM_NOT_FOUND of type NM.DeviceStateReason>, 44: <enum NM_DEVICE_STATE_REASON_BT_FAILED of type NM.DeviceStateReason>, 45: <enum NM_DEVICE_STATE_REASON_GSM_SIM_NOT_INSERTED of type NM.DeviceStateReason>, 46: <enum NM_DEVICE_STATE_REASON_GSM_SIM_PIN_REQUIRED of type NM.DeviceStateReason>, 47: <enum NM_DEVICE_STATE_REASON_GSM_SIM_PUK_REQUIRED of type NM.DeviceStateReason>, 48: <enum NM_DEVICE_STATE_REASON_GSM_SIM_WRONG of type NM.DeviceStateReason>, 49: <enum NM_DEVICE_STATE_REASON_INFINIBAND_MODE of type NM.DeviceStateReason>, 50: <enum NM_DEVICE_STATE_REASON_DEPENDENCY_FAILED of type NM.DeviceStateReason>, 51: <enum NM_DEVICE_STATE_REASON_BR2684_FAILED of type NM.DeviceStateReason>, 52: <enum NM_DEVICE_STATE_REASON_MODEM_MANAGER_UNAVAILABLE of type NM.DeviceStateReason>, 53: <enum NM_DEVICE_STATE_REASON_SSID_NOT_FOUND of type NM.DeviceStateReason>, 54: <enum NM_DEVICE_STATE_REASON_SECONDARY_CONNECTION_FAILED of type NM.DeviceStateReason>, 55: <enum NM_DEVICE_STATE_REASON_DCB_FCOE_FAILED of type NM.DeviceStateReason>, 56: <enum NM_DEVICE_STATE_REASON_TEAMD_CONTROL_FAILED of type NM.DeviceStateReason>, 57: <enum NM_DEVICE_STATE_REASON_MODEM_FAILED of type NM.DeviceStateReason>, 58: <enum NM_DEVICE_STATE_REASON_MODEM_AVAILABLE of type NM.DeviceStateReason>, 59: <enum NM_DEVICE_STATE_REASON_SIM_PIN_INCORRECT of type NM.DeviceStateReason>, 60: <enum NM_DEVICE_STATE_REASON_NEW_ACTIVATION of type NM.DeviceStateReason>, 61: <enum NM_DEVICE_STATE_REASON_PARENT_CHANGED of type NM.DeviceStateReason>, 62: <enum NM_DEVICE_STATE_REASON_PARENT_MANAGED_CHANGED of type NM.DeviceStateReason>, 63: <enum NM_DEVICE_STATE_REASON_OVSDB_FAILED of type NM.DeviceStateReason>, 64: <enum NM_DEVICE_STATE_REASON_IP_ADDRESS_DUPLICATE of type NM.DeviceStateReason>, 65: <enum NM_DEVICE_STATE_REASON_IP_METHOD_UNSUPPORTED of type NM.DeviceStateReason>, 66: <enum NM_DEVICE_STATE_REASON_SRIOV_CONFIGURATION_FAILED of type NM.DeviceStateReason>, 67: <enum NM_DEVICE_STATE_REASON_PEER_NOT_FOUND of type NM.DeviceStateReason>}, '__info__': gi.EnumInfo(DeviceStateReason), 'NONE': <enum NM_DEVICE_STATE_REASON_NONE of type NM.DeviceStateReason>, 'UNKNOWN': <enum NM_DEVICE_STATE_REASON_UNKNOWN of type NM.DeviceStateReason>, 'NOW_MANAGED': <enum NM_DEVICE_STATE_REASON_NOW_MANAGED of type NM.DeviceStateReason>, 'NOW_UNMANAGED': <enum NM_DEVICE_STATE_REASON_NOW_UNMANAGED of type NM.DeviceStateReason>, 'CONFIG_FAILED': <enum NM_DEVICE_STATE_REASON_CONFIG_FAILED of type NM.DeviceStateReason>, 'IP_CONFIG_UNAVAILABLE': <enum NM_DEVICE_STATE_REASON_IP_CONFIG_UNAVAILABLE of type NM.DeviceStateReason>, 'IP_CONFIG_EXPIRED': <enum NM_DEVICE_STATE_REASON_IP_CONFIG_EXPIRED of type NM.DeviceStateReason>, 'NO_SECRETS': <enum NM_DEVICE_STATE_REASON_NO_SECRETS of type NM.DeviceStateReason>, 'SUPPLICANT_DISCONNECT': <enum NM_DEVICE_STATE_REASON_SUPPLICANT_DISCONNECT of type NM.DeviceStateReason>, 'SUPPLICANT_CONFIG_FAILED': <enum NM_DEVICE_STATE_REASON_SUPPLICANT_CONFIG_FAILED of type NM.DeviceStateReason>, 'SUPPLICANT_FAILED': <enum NM_DEVICE_STATE_REASON_SUPPLICANT_FAILED of type NM.DeviceStateReason>, 'SUPPLICANT_TIMEOUT': <enum NM_DEVICE_STATE_REASON_SUPPLICANT_TIMEOUT of type NM.DeviceStateReason>, 'PPP_START_FAILED': <enum NM_DEVICE_STATE_REASON_PPP_START_FAILED of type NM.DeviceStateReason>, 'PPP_DISCONNECT': <enum NM_DEVICE_STATE_REASON_PPP_DISCONNECT of type NM.DeviceStateReason>, 'PPP_FAILED': <enum NM_DEVICE_STATE_REASON_PPP_FAILED of type NM.DeviceStateReason>, 'DHCP_START_FAILED': <enum NM_DEVICE_STATE_REASON_DHCP_START_FAILED of type NM.DeviceStateReason>, 'DHCP_ERROR': <enum NM_DEVICE_STATE_REASON_DHCP_ERROR of type NM.DeviceStateReason>, 'DHCP_FAILED': <enum NM_DEVICE_STATE_REASON_DHCP_FAILED of type NM.DeviceStateReason>, 'SHARED_START_FAILED': <enum NM_DEVICE_STATE_REASON_SHARED_START_FAILED of type NM.DeviceStateReason>, 'SHARED_FAILED': <enum NM_DEVICE_STATE_REASON_SHARED_FAILED of type NM.DeviceStateReason>, 'AUTOIP_START_FAILED': <enum NM_DEVICE_STATE_REASON_AUTOIP_START_FAILED of type NM.DeviceStateReason>, 'AUTOIP_ERROR': <enum NM_DEVICE_STATE_REASON_AUTOIP_ERROR of type NM.DeviceStateReason>, 'AUTOIP_FAILED': <enum NM_DEVICE_STATE_REASON_AUTOIP_FAILED of type NM.DeviceStateReason>, 'MODEM_BUSY': <enum NM_DEVICE_STATE_REASON_MODEM_BUSY of type NM.DeviceStateReason>, 'MODEM_NO_DIAL_TONE': <enum NM_DEVICE_STATE_REASON_MODEM_NO_DIAL_TONE of type NM.DeviceStateReason>, 'MODEM_NO_CARRIER': <enum NM_DEVICE_STATE_REASON_MODEM_NO_CARRIER of type NM.DeviceStateReason>, 'MODEM_DIAL_TIMEOUT': <enum NM_DEVICE_STATE_REASON_MODEM_DIAL_TIMEOUT of type NM.DeviceStateReason>, 'MODEM_DIAL_FAILED': <enum NM_DEVICE_STATE_REASON_MODEM_DIAL_FAILED of type NM.DeviceStateReason>, 'MODEM_INIT_FAILED': <enum NM_DEVICE_STATE_REASON_MODEM_INIT_FAILED of type NM.DeviceStateReason>, 'GSM_APN_FAILED': <enum NM_DEVICE_STATE_REASON_GSM_APN_FAILED of type NM.DeviceStateReason>, 'GSM_REGISTRATION_NOT_SEARCHING': <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_NOT_SEARCHING of type NM.DeviceStateReason>, 'GSM_REGISTRATION_DENIED': <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_DENIED of type NM.DeviceStateReason>, 'GSM_REGISTRATION_TIMEOUT': <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_TIMEOUT of type NM.DeviceStateReason>, 'GSM_REGISTRATION_FAILED': <enum NM_DEVICE_STATE_REASON_GSM_REGISTRATION_FAILED of type NM.DeviceStateReason>, 'GSM_PIN_CHECK_FAILED': <enum NM_DEVICE_STATE_REASON_GSM_PIN_CHECK_FAILED of type NM.DeviceStateReason>, 'FIRMWARE_MISSING': <enum NM_DEVICE_STATE_REASON_FIRMWARE_MISSING of type NM.DeviceStateReason>, 'REMOVED': <enum NM_DEVICE_STATE_REASON_REMOVED of type NM.DeviceStateReason>, 'SLEEPING': <enum NM_DEVICE_STATE_REASON_SLEEPING of type NM.DeviceStateReason>, 'CONNECTION_REMOVED': <enum NM_DEVICE_STATE_REASON_CONNECTION_REMOVED of type NM.DeviceStateReason>, 'USER_REQUESTED': <enum NM_DEVICE_STATE_REASON_USER_REQUESTED of type NM.DeviceStateReason>, 'CARRIER': <enum NM_DEVICE_STATE_REASON_CARRIER of type NM.DeviceStateReason>, 'CONNECTION_ASSUMED': <enum NM_DEVICE_STATE_REASON_CONNECTION_ASSUMED of type NM.DeviceStateReason>, 'SUPPLICANT_AVAILABLE': <enum NM_DEVICE_STATE_REASON_SUPPLICANT_AVAILABLE of type NM.DeviceStateReason>, 'MODEM_NOT_FOUND': <enum NM_DEVICE_STATE_REASON_MODEM_NOT_FOUND of type NM.DeviceStateReason>, 'BT_FAILED': <enum NM_DEVICE_STATE_REASON_BT_FAILED of type NM.DeviceStateReason>, 'GSM_SIM_NOT_INSERTED': <enum NM_DEVICE_STATE_REASON_GSM_SIM_NOT_INSERTED of type NM.DeviceStateReason>, 'GSM_SIM_PIN_REQUIRED': <enum NM_DEVICE_STATE_REASON_GSM_SIM_PIN_REQUIRED of type NM.DeviceStateReason>, 'GSM_SIM_PUK_REQUIRED': <enum NM_DEVICE_STATE_REASON_GSM_SIM_PUK_REQUIRED of type NM.DeviceStateReason>, 'GSM_SIM_WRONG': <enum NM_DEVICE_STATE_REASON_GSM_SIM_WRONG of type NM.DeviceStateReason>, 'INFINIBAND_MODE': <enum NM_DEVICE_STATE_REASON_INFINIBAND_MODE of type NM.DeviceStateReason>, 'DEPENDENCY_FAILED': <enum NM_DEVICE_STATE_REASON_DEPENDENCY_FAILED of type NM.DeviceStateReason>, 'BR2684_FAILED': <enum NM_DEVICE_STATE_REASON_BR2684_FAILED of type NM.DeviceStateReason>, 'MODEM_MANAGER_UNAVAILABLE': <enum NM_DEVICE_STATE_REASON_MODEM_MANAGER_UNAVAILABLE of type NM.DeviceStateReason>, 'SSID_NOT_FOUND': <enum NM_DEVICE_STATE_REASON_SSID_NOT_FOUND of type NM.DeviceStateReason>, 'SECONDARY_CONNECTION_FAILED': <enum NM_DEVICE_STATE_REASON_SECONDARY_CONNECTION_FAILED of type NM.DeviceStateReason>, 'DCB_FCOE_FAILED': <enum NM_DEVICE_STATE_REASON_DCB_FCOE_FAILED of type NM.DeviceStateReason>, 'TEAMD_CONTROL_FAILED': <enum NM_DEVICE_STATE_REASON_TEAMD_CONTROL_FAILED of type NM.DeviceStateReason>, 'MODEM_FAILED': <enum NM_DEVICE_STATE_REASON_MODEM_FAILED of type NM.DeviceStateReason>, 'MODEM_AVAILABLE': <enum NM_DEVICE_STATE_REASON_MODEM_AVAILABLE of type NM.DeviceStateReason>, 'SIM_PIN_INCORRECT': <enum NM_DEVICE_STATE_REASON_SIM_PIN_INCORRECT of type NM.DeviceStateReason>, 'NEW_ACTIVATION': <enum NM_DEVICE_STATE_REASON_NEW_ACTIVATION of type NM.DeviceStateReason>, 'PARENT_CHANGED': <enum NM_DEVICE_STATE_REASON_PARENT_CHANGED of type NM.DeviceStateReason>, 'PARENT_MANAGED_CHANGED': <enum NM_DEVICE_STATE_REASON_PARENT_MANAGED_CHANGED of type NM.DeviceStateReason>, 'OVSDB_FAILED': <enum NM_DEVICE_STATE_REASON_OVSDB_FAILED of type NM.DeviceStateReason>, 'IP_ADDRESS_DUPLICATE': <enum NM_DEVICE_STATE_REASON_IP_ADDRESS_DUPLICATE of type NM.DeviceStateReason>, 'IP_METHOD_UNSUPPORTED': <enum NM_DEVICE_STATE_REASON_IP_METHOD_UNSUPPORTED of type NM.DeviceStateReason>, 'SRIOV_CONFIGURATION_FAILED': <enum NM_DEVICE_STATE_REASON_SRIOV_CONFIGURATION_FAILED of type NM.DeviceStateReason>, 'PEER_NOT_FOUND': <enum NM_DEVICE_STATE_REASON_PEER_NOT_FOUND of type NM.DeviceStateReason>})"
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
    }
    __gtype__ = None # (!) real value is '<GType NMDeviceStateReason (94741104198640)>'
    __info__ = gi.EnumInfo(DeviceStateReason)


