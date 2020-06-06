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


class DeviceType(__gobject.GEnum):
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


    6LOWPAN = 28
    ADSL = 12
    BOND = 10
    BRIDGE = 13
    BT = 5
    DUMMY = 22
    ETHERNET = 1
    GENERIC = 14
    INFINIBAND = 9
    IP_TUNNEL = 17
    MACSEC = 21
    MACVLAN = 18
    MODEM = 8
    OLPC_MESH = 6
    OVS_BRIDGE = 26
    OVS_INTERFACE = 24
    OVS_PORT = 25
    PPP = 23
    TEAM = 15
    TUN = 16
    UNKNOWN = 0
    UNUSED1 = 3
    UNUSED2 = 4
    VETH = 20
    VLAN = 11
    VXLAN = 19
    WIFI = 2
    WIFI_P2P = 30
    WIMAX = 7
    WIREGUARD = 29
    WPAN = 27
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.NM', '__dict__': <attribute '__dict__' of 'DeviceType' objects>, '__doc__': None, '__gtype__': <GType NMDeviceType (94741104205792)>, '__enum_values__': {0: <enum NM_DEVICE_TYPE_UNKNOWN of type NM.DeviceType>, 1: <enum NM_DEVICE_TYPE_ETHERNET of type NM.DeviceType>, 2: <enum NM_DEVICE_TYPE_WIFI of type NM.DeviceType>, 3: <enum NM_DEVICE_TYPE_UNUSED1 of type NM.DeviceType>, 4: <enum NM_DEVICE_TYPE_UNUSED2 of type NM.DeviceType>, 5: <enum NM_DEVICE_TYPE_BT of type NM.DeviceType>, 6: <enum NM_DEVICE_TYPE_OLPC_MESH of type NM.DeviceType>, 7: <enum NM_DEVICE_TYPE_WIMAX of type NM.DeviceType>, 8: <enum NM_DEVICE_TYPE_MODEM of type NM.DeviceType>, 9: <enum NM_DEVICE_TYPE_INFINIBAND of type NM.DeviceType>, 10: <enum NM_DEVICE_TYPE_BOND of type NM.DeviceType>, 11: <enum NM_DEVICE_TYPE_VLAN of type NM.DeviceType>, 12: <enum NM_DEVICE_TYPE_ADSL of type NM.DeviceType>, 13: <enum NM_DEVICE_TYPE_BRIDGE of type NM.DeviceType>, 14: <enum NM_DEVICE_TYPE_GENERIC of type NM.DeviceType>, 15: <enum NM_DEVICE_TYPE_TEAM of type NM.DeviceType>, 16: <enum NM_DEVICE_TYPE_TUN of type NM.DeviceType>, 17: <enum NM_DEVICE_TYPE_IP_TUNNEL of type NM.DeviceType>, 18: <enum NM_DEVICE_TYPE_MACVLAN of type NM.DeviceType>, 19: <enum NM_DEVICE_TYPE_VXLAN of type NM.DeviceType>, 20: <enum NM_DEVICE_TYPE_VETH of type NM.DeviceType>, 21: <enum NM_DEVICE_TYPE_MACSEC of type NM.DeviceType>, 22: <enum NM_DEVICE_TYPE_DUMMY of type NM.DeviceType>, 23: <enum NM_DEVICE_TYPE_PPP of type NM.DeviceType>, 24: <enum NM_DEVICE_TYPE_OVS_INTERFACE of type NM.DeviceType>, 25: <enum NM_DEVICE_TYPE_OVS_PORT of type NM.DeviceType>, 26: <enum NM_DEVICE_TYPE_OVS_BRIDGE of type NM.DeviceType>, 27: <enum NM_DEVICE_TYPE_WPAN of type NM.DeviceType>, 28: <enum NM_DEVICE_TYPE_6LOWPAN of type NM.DeviceType>, 29: <enum NM_DEVICE_TYPE_WIREGUARD of type NM.DeviceType>, 30: <enum NM_DEVICE_TYPE_WIFI_P2P of type NM.DeviceType>}, '__info__': gi.EnumInfo(DeviceType), 'UNKNOWN': <enum NM_DEVICE_TYPE_UNKNOWN of type NM.DeviceType>, 'ETHERNET': <enum NM_DEVICE_TYPE_ETHERNET of type NM.DeviceType>, 'WIFI': <enum NM_DEVICE_TYPE_WIFI of type NM.DeviceType>, 'UNUSED1': <enum NM_DEVICE_TYPE_UNUSED1 of type NM.DeviceType>, 'UNUSED2': <enum NM_DEVICE_TYPE_UNUSED2 of type NM.DeviceType>, 'BT': <enum NM_DEVICE_TYPE_BT of type NM.DeviceType>, 'OLPC_MESH': <enum NM_DEVICE_TYPE_OLPC_MESH of type NM.DeviceType>, 'WIMAX': <enum NM_DEVICE_TYPE_WIMAX of type NM.DeviceType>, 'MODEM': <enum NM_DEVICE_TYPE_MODEM of type NM.DeviceType>, 'INFINIBAND': <enum NM_DEVICE_TYPE_INFINIBAND of type NM.DeviceType>, 'BOND': <enum NM_DEVICE_TYPE_BOND of type NM.DeviceType>, 'VLAN': <enum NM_DEVICE_TYPE_VLAN of type NM.DeviceType>, 'ADSL': <enum NM_DEVICE_TYPE_ADSL of type NM.DeviceType>, 'BRIDGE': <enum NM_DEVICE_TYPE_BRIDGE of type NM.DeviceType>, 'GENERIC': <enum NM_DEVICE_TYPE_GENERIC of type NM.DeviceType>, 'TEAM': <enum NM_DEVICE_TYPE_TEAM of type NM.DeviceType>, 'TUN': <enum NM_DEVICE_TYPE_TUN of type NM.DeviceType>, 'IP_TUNNEL': <enum NM_DEVICE_TYPE_IP_TUNNEL of type NM.DeviceType>, 'MACVLAN': <enum NM_DEVICE_TYPE_MACVLAN of type NM.DeviceType>, 'VXLAN': <enum NM_DEVICE_TYPE_VXLAN of type NM.DeviceType>, 'VETH': <enum NM_DEVICE_TYPE_VETH of type NM.DeviceType>, 'MACSEC': <enum NM_DEVICE_TYPE_MACSEC of type NM.DeviceType>, 'DUMMY': <enum NM_DEVICE_TYPE_DUMMY of type NM.DeviceType>, 'PPP': <enum NM_DEVICE_TYPE_PPP of type NM.DeviceType>, 'OVS_INTERFACE': <enum NM_DEVICE_TYPE_OVS_INTERFACE of type NM.DeviceType>, 'OVS_PORT': <enum NM_DEVICE_TYPE_OVS_PORT of type NM.DeviceType>, 'OVS_BRIDGE': <enum NM_DEVICE_TYPE_OVS_BRIDGE of type NM.DeviceType>, 'WPAN': <enum NM_DEVICE_TYPE_WPAN of type NM.DeviceType>, '6LOWPAN': <enum NM_DEVICE_TYPE_6LOWPAN of type NM.DeviceType>, 'WIREGUARD': <enum NM_DEVICE_TYPE_WIREGUARD of type NM.DeviceType>, 'WIFI_P2P': <enum NM_DEVICE_TYPE_WIFI_P2P of type NM.DeviceType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType NMDeviceType (94741104205792)>'
    __info__ = gi.EnumInfo(DeviceType)


