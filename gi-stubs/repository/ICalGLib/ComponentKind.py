# encoding: utf-8
# module gi.repository.ICalGLib
# from /usr/lib64/girepository-1.0/ICalGLib-3.0.typelib
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


class ComponentKind(__gobject.GEnum):
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


    ANY_COMPONENT = 1
    NO_COMPONENT = 0
    VAGENDA_COMPONENT = 8
    VALARM_COMPONENT = 10
    VAVAILABILITY_COMPONENT = 26
    VCALENDAR_COMPONENT = 7
    VCAR_COMPONENT = 22
    VCOMMAND_COMPONENT = 23
    VEVENT_COMPONENT = 4
    VFREEBUSY_COMPONENT = 9
    VJOURNAL_COMPONENT = 6
    VPOLL_COMPONENT = 28
    VQUERY_COMPONENT = 20
    VREPLY_COMPONENT = 21
    VSCHEDULE_COMPONENT = 19
    VTIMEZONE_COMPONENT = 15
    VTODO_COMPONENT = 5
    VVOTER_COMPONENT = 29
    XATTACH_COMPONENT = 3
    XAUDIOALARM_COMPONENT = 11
    XAVAILABLE_COMPONENT = 27
    XDAYLIGHT_COMPONENT = 17
    XDISPLAYALARM_COMPONENT = 12
    XEMAILALARM_COMPONENT = 13
    XLICINVALID_COMPONENT = 24
    XLICMIMEPART_COMPONENT = 25
    XPROCEDUREALARM_COMPONENT = 14
    XROOT_COMPONENT = 2
    XSTANDARD_COMPONENT = 16
    XVOTE_COMPONENT = 30
    X_COMPONENT = 18
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICalGLib', '__dict__': <attribute '__dict__' of 'ComponentKind' objects>, '__doc__': None, '__gtype__': <GType PyICalGLibComponentKind (94403187644208)>, '__enum_values__': {0: <enum I_CAL_NO_COMPONENT of type ICalGLib.ComponentKind>, 1: <enum I_CAL_ANY_COMPONENT of type ICalGLib.ComponentKind>, 2: <enum I_CAL_XROOT_COMPONENT of type ICalGLib.ComponentKind>, 3: <enum I_CAL_XATTACH_COMPONENT of type ICalGLib.ComponentKind>, 4: <enum I_CAL_VEVENT_COMPONENT of type ICalGLib.ComponentKind>, 5: <enum I_CAL_VTODO_COMPONENT of type ICalGLib.ComponentKind>, 6: <enum I_CAL_VJOURNAL_COMPONENT of type ICalGLib.ComponentKind>, 7: <enum I_CAL_VCALENDAR_COMPONENT of type ICalGLib.ComponentKind>, 8: <enum I_CAL_VAGENDA_COMPONENT of type ICalGLib.ComponentKind>, 9: <enum I_CAL_VFREEBUSY_COMPONENT of type ICalGLib.ComponentKind>, 10: <enum I_CAL_VALARM_COMPONENT of type ICalGLib.ComponentKind>, 11: <enum I_CAL_XAUDIOALARM_COMPONENT of type ICalGLib.ComponentKind>, 12: <enum I_CAL_XDISPLAYALARM_COMPONENT of type ICalGLib.ComponentKind>, 13: <enum I_CAL_XEMAILALARM_COMPONENT of type ICalGLib.ComponentKind>, 14: <enum I_CAL_XPROCEDUREALARM_COMPONENT of type ICalGLib.ComponentKind>, 15: <enum I_CAL_VTIMEZONE_COMPONENT of type ICalGLib.ComponentKind>, 16: <enum I_CAL_XSTANDARD_COMPONENT of type ICalGLib.ComponentKind>, 17: <enum I_CAL_XDAYLIGHT_COMPONENT of type ICalGLib.ComponentKind>, 18: <enum I_CAL_X_COMPONENT of type ICalGLib.ComponentKind>, 19: <enum I_CAL_VSCHEDULE_COMPONENT of type ICalGLib.ComponentKind>, 20: <enum I_CAL_VQUERY_COMPONENT of type ICalGLib.ComponentKind>, 21: <enum I_CAL_VREPLY_COMPONENT of type ICalGLib.ComponentKind>, 22: <enum I_CAL_VCAR_COMPONENT of type ICalGLib.ComponentKind>, 23: <enum I_CAL_VCOMMAND_COMPONENT of type ICalGLib.ComponentKind>, 24: <enum I_CAL_XLICINVALID_COMPONENT of type ICalGLib.ComponentKind>, 25: <enum I_CAL_XLICMIMEPART_COMPONENT of type ICalGLib.ComponentKind>, 26: <enum I_CAL_VAVAILABILITY_COMPONENT of type ICalGLib.ComponentKind>, 27: <enum I_CAL_XAVAILABLE_COMPONENT of type ICalGLib.ComponentKind>, 28: <enum I_CAL_VPOLL_COMPONENT of type ICalGLib.ComponentKind>, 29: <enum I_CAL_VVOTER_COMPONENT of type ICalGLib.ComponentKind>, 30: <enum I_CAL_XVOTE_COMPONENT of type ICalGLib.ComponentKind>}, '__info__': gi.EnumInfo(ComponentKind), 'NO_COMPONENT': <enum I_CAL_NO_COMPONENT of type ICalGLib.ComponentKind>, 'ANY_COMPONENT': <enum I_CAL_ANY_COMPONENT of type ICalGLib.ComponentKind>, 'XROOT_COMPONENT': <enum I_CAL_XROOT_COMPONENT of type ICalGLib.ComponentKind>, 'XATTACH_COMPONENT': <enum I_CAL_XATTACH_COMPONENT of type ICalGLib.ComponentKind>, 'VEVENT_COMPONENT': <enum I_CAL_VEVENT_COMPONENT of type ICalGLib.ComponentKind>, 'VTODO_COMPONENT': <enum I_CAL_VTODO_COMPONENT of type ICalGLib.ComponentKind>, 'VJOURNAL_COMPONENT': <enum I_CAL_VJOURNAL_COMPONENT of type ICalGLib.ComponentKind>, 'VCALENDAR_COMPONENT': <enum I_CAL_VCALENDAR_COMPONENT of type ICalGLib.ComponentKind>, 'VAGENDA_COMPONENT': <enum I_CAL_VAGENDA_COMPONENT of type ICalGLib.ComponentKind>, 'VFREEBUSY_COMPONENT': <enum I_CAL_VFREEBUSY_COMPONENT of type ICalGLib.ComponentKind>, 'VALARM_COMPONENT': <enum I_CAL_VALARM_COMPONENT of type ICalGLib.ComponentKind>, 'XAUDIOALARM_COMPONENT': <enum I_CAL_XAUDIOALARM_COMPONENT of type ICalGLib.ComponentKind>, 'XDISPLAYALARM_COMPONENT': <enum I_CAL_XDISPLAYALARM_COMPONENT of type ICalGLib.ComponentKind>, 'XEMAILALARM_COMPONENT': <enum I_CAL_XEMAILALARM_COMPONENT of type ICalGLib.ComponentKind>, 'XPROCEDUREALARM_COMPONENT': <enum I_CAL_XPROCEDUREALARM_COMPONENT of type ICalGLib.ComponentKind>, 'VTIMEZONE_COMPONENT': <enum I_CAL_VTIMEZONE_COMPONENT of type ICalGLib.ComponentKind>, 'XSTANDARD_COMPONENT': <enum I_CAL_XSTANDARD_COMPONENT of type ICalGLib.ComponentKind>, 'XDAYLIGHT_COMPONENT': <enum I_CAL_XDAYLIGHT_COMPONENT of type ICalGLib.ComponentKind>, 'X_COMPONENT': <enum I_CAL_X_COMPONENT of type ICalGLib.ComponentKind>, 'VSCHEDULE_COMPONENT': <enum I_CAL_VSCHEDULE_COMPONENT of type ICalGLib.ComponentKind>, 'VQUERY_COMPONENT': <enum I_CAL_VQUERY_COMPONENT of type ICalGLib.ComponentKind>, 'VREPLY_COMPONENT': <enum I_CAL_VREPLY_COMPONENT of type ICalGLib.ComponentKind>, 'VCAR_COMPONENT': <enum I_CAL_VCAR_COMPONENT of type ICalGLib.ComponentKind>, 'VCOMMAND_COMPONENT': <enum I_CAL_VCOMMAND_COMPONENT of type ICalGLib.ComponentKind>, 'XLICINVALID_COMPONENT': <enum I_CAL_XLICINVALID_COMPONENT of type ICalGLib.ComponentKind>, 'XLICMIMEPART_COMPONENT': <enum I_CAL_XLICMIMEPART_COMPONENT of type ICalGLib.ComponentKind>, 'VAVAILABILITY_COMPONENT': <enum I_CAL_VAVAILABILITY_COMPONENT of type ICalGLib.ComponentKind>, 'XAVAILABLE_COMPONENT': <enum I_CAL_XAVAILABLE_COMPONENT of type ICalGLib.ComponentKind>, 'VPOLL_COMPONENT': <enum I_CAL_VPOLL_COMPONENT of type ICalGLib.ComponentKind>, 'VVOTER_COMPONENT': <enum I_CAL_VVOTER_COMPONENT of type ICalGLib.ComponentKind>, 'XVOTE_COMPONENT': <enum I_CAL_XVOTE_COMPONENT of type ICalGLib.ComponentKind>})"
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
    __gtype__ = None # (!) real value is '<GType PyICalGLibComponentKind (94403187644208)>'
    __info__ = gi.EnumInfo(ComponentKind)


