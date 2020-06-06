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


class PropertyKind(__gobject.GEnum):
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


    ACCEPTRESPONSE_PROPERTY = 102
    ACKNOWLEDGED_PROPERTY = 1
    ACTION_PROPERTY = 2
    ALLOWCONFLICT_PROPERTY = 3
    ANY_PROPERTY = 0
    ATTACH_PROPERTY = 4
    ATTENDEE_PROPERTY = 5
    BUSYTYPE_PROPERTY = 101
    CALID_PROPERTY = 6
    CALMASTER_PROPERTY = 7
    CALSCALE_PROPERTY = 8
    CAPVERSION_PROPERTY = 9
    CARID_PROPERTY = 11
    CARLEVEL_PROPERTY = 10
    CATEGORIES_PROPERTY = 12
    CLASS_PROPERTY = 13
    CMD_PROPERTY = 14
    COLOR_PROPERTY = 118
    COMMENT_PROPERTY = 15
    COMPLETED_PROPERTY = 16
    COMPONENTS_PROPERTY = 17
    CONTACT_PROPERTY = 18
    CREATED_PROPERTY = 19
    CSID_PROPERTY = 20
    DATEMAX_PROPERTY = 21
    DATEMIN_PROPERTY = 22
    DECREED_PROPERTY = 23
    DEFAULTCHARSET_PROPERTY = 24
    DEFAULTLOCALE_PROPERTY = 25
    DEFAULTTZID_PROPERTY = 26
    DEFAULTVCARS_PROPERTY = 27
    DENY_PROPERTY = 28
    DESCRIPTION_PROPERTY = 29
    DTEND_PROPERTY = 30
    DTSTAMP_PROPERTY = 31
    DTSTART_PROPERTY = 32
    DUE_PROPERTY = 33
    DURATION_PROPERTY = 34
    ESTIMATEDDURATION_PROPERTY = 113
    EXDATE_PROPERTY = 35
    EXPAND_PROPERTY = 36
    EXRULE_PROPERTY = 37
    FREEBUSY_PROPERTY = 38
    GEO_PROPERTY = 39
    GRANT_PROPERTY = 40
    ITIPVERSION_PROPERTY = 41
    LASTMODIFIED_PROPERTY = 42
    LOCATION_PROPERTY = 43
    MAXCOMPONENTSIZE_PROPERTY = 44
    MAXDATE_PROPERTY = 45
    MAXRESULTSSIZE_PROPERTY = 47
    MAXRESULTS_PROPERTY = 46
    METHOD_PROPERTY = 48
    MINDATE_PROPERTY = 49
    MULTIPART_PROPERTY = 50
    NAME_PROPERTY = 115
    NO_PROPERTY = 100
    ORGANIZER_PROPERTY = 52
    OWNER_PROPERTY = 53
    PERCENTCOMPLETE_PROPERTY = 54
    PERMISSION_PROPERTY = 55
    POLLCOMPLETION_PROPERTY = 110
    POLLITEMID_PROPERTY = 103
    POLLMODE_PROPERTY = 104
    POLLPROPERTIES_PROPERTY = 105
    POLLWINNER_PROPERTY = 106
    PRIORITY_PROPERTY = 56
    PRODID_PROPERTY = 57
    QUERYID_PROPERTY = 60
    QUERYLEVEL_PROPERTY = 59
    QUERYNAME_PROPERTY = 61
    QUERY_PROPERTY = 58
    RDATE_PROPERTY = 62
    RECURACCEPTED_PROPERTY = 63
    RECUREXPAND_PROPERTY = 64
    RECURLIMIT_PROPERTY = 65
    RECURRENCEID_PROPERTY = 66
    RELATEDTO_PROPERTY = 67
    RELCALID_PROPERTY = 68
    REPEAT_PROPERTY = 69
    REPLYURL_PROPERTY = 111
    REQUESTSTATUS_PROPERTY = 70
    RESOURCES_PROPERTY = 71
    RESPONSE_PROPERTY = 112
    RESTRICTION_PROPERTY = 72
    RRULE_PROPERTY = 73
    SCOPE_PROPERTY = 74
    SEQUENCE_PROPERTY = 75
    STATUS_PROPERTY = 76
    STORESEXPANDED_PROPERTY = 77
    SUMMARY_PROPERTY = 78
    TARGET_PROPERTY = 79
    TASKMODE_PROPERTY = 114
    TRANSP_PROPERTY = 80
    TRIGGER_PROPERTY = 81
    TZIDALIASOF_PROPERTY = 108
    TZID_PROPERTY = 82
    TZNAME_PROPERTY = 83
    TZOFFSETFROM_PROPERTY = 84
    TZOFFSETTO_PROPERTY = 85
    TZUNTIL_PROPERTY = 109
    TZURL_PROPERTY = 86
    UID_PROPERTY = 87
    URL_PROPERTY = 88
    VERSION_PROPERTY = 89
    VOTER_PROPERTY = 107
    XLICCLASS_PROPERTY = 91
    XLICCLUSTERCOUNT_PROPERTY = 92
    XLICERROR_PROPERTY = 93
    XLICMIMECHARSET_PROPERTY = 94
    XLICMIMECID_PROPERTY = 95
    XLICMIMECONTENTTYPE_PROPERTY = 96
    XLICMIMEENCODING_PROPERTY = 97
    XLICMIMEFILENAME_PROPERTY = 98
    XLICMIMEOPTINFO_PROPERTY = 99
    X_PROPERTY = 90
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICalGLib', '__dict__': <attribute '__dict__' of 'PropertyKind' objects>, '__doc__': None, '__gtype__': <GType PyICalGLibPropertyKind (94403188461360)>, '__enum_values__': {0: <enum I_CAL_ANY_PROPERTY of type ICalGLib.PropertyKind>, 102: <enum I_CAL_ACCEPTRESPONSE_PROPERTY of type ICalGLib.PropertyKind>, 1: <enum I_CAL_ACKNOWLEDGED_PROPERTY of type ICalGLib.PropertyKind>, 2: <enum I_CAL_ACTION_PROPERTY of type ICalGLib.PropertyKind>, 3: <enum I_CAL_ALLOWCONFLICT_PROPERTY of type ICalGLib.PropertyKind>, 4: <enum I_CAL_ATTACH_PROPERTY of type ICalGLib.PropertyKind>, 5: <enum I_CAL_ATTENDEE_PROPERTY of type ICalGLib.PropertyKind>, 101: <enum I_CAL_BUSYTYPE_PROPERTY of type ICalGLib.PropertyKind>, 6: <enum I_CAL_CALID_PROPERTY of type ICalGLib.PropertyKind>, 7: <enum I_CAL_CALMASTER_PROPERTY of type ICalGLib.PropertyKind>, 8: <enum I_CAL_CALSCALE_PROPERTY of type ICalGLib.PropertyKind>, 9: <enum I_CAL_CAPVERSION_PROPERTY of type ICalGLib.PropertyKind>, 10: <enum I_CAL_CARLEVEL_PROPERTY of type ICalGLib.PropertyKind>, 11: <enum I_CAL_CARID_PROPERTY of type ICalGLib.PropertyKind>, 12: <enum I_CAL_CATEGORIES_PROPERTY of type ICalGLib.PropertyKind>, 13: <enum I_CAL_CLASS_PROPERTY of type ICalGLib.PropertyKind>, 14: <enum I_CAL_CMD_PROPERTY of type ICalGLib.PropertyKind>, 118: <enum I_CAL_COLOR_PROPERTY of type ICalGLib.PropertyKind>, 15: <enum I_CAL_COMMENT_PROPERTY of type ICalGLib.PropertyKind>, 16: <enum I_CAL_COMPLETED_PROPERTY of type ICalGLib.PropertyKind>, 17: <enum I_CAL_COMPONENTS_PROPERTY of type ICalGLib.PropertyKind>, 18: <enum I_CAL_CONTACT_PROPERTY of type ICalGLib.PropertyKind>, 19: <enum I_CAL_CREATED_PROPERTY of type ICalGLib.PropertyKind>, 20: <enum I_CAL_CSID_PROPERTY of type ICalGLib.PropertyKind>, 21: <enum I_CAL_DATEMAX_PROPERTY of type ICalGLib.PropertyKind>, 22: <enum I_CAL_DATEMIN_PROPERTY of type ICalGLib.PropertyKind>, 23: <enum I_CAL_DECREED_PROPERTY of type ICalGLib.PropertyKind>, 24: <enum I_CAL_DEFAULTCHARSET_PROPERTY of type ICalGLib.PropertyKind>, 25: <enum I_CAL_DEFAULTLOCALE_PROPERTY of type ICalGLib.PropertyKind>, 26: <enum I_CAL_DEFAULTTZID_PROPERTY of type ICalGLib.PropertyKind>, 27: <enum I_CAL_DEFAULTVCARS_PROPERTY of type ICalGLib.PropertyKind>, 28: <enum I_CAL_DENY_PROPERTY of type ICalGLib.PropertyKind>, 29: <enum I_CAL_DESCRIPTION_PROPERTY of type ICalGLib.PropertyKind>, 30: <enum I_CAL_DTEND_PROPERTY of type ICalGLib.PropertyKind>, 31: <enum I_CAL_DTSTAMP_PROPERTY of type ICalGLib.PropertyKind>, 32: <enum I_CAL_DTSTART_PROPERTY of type ICalGLib.PropertyKind>, 33: <enum I_CAL_DUE_PROPERTY of type ICalGLib.PropertyKind>, 34: <enum I_CAL_DURATION_PROPERTY of type ICalGLib.PropertyKind>, 113: <enum I_CAL_ESTIMATEDDURATION_PROPERTY of type ICalGLib.PropertyKind>, 35: <enum I_CAL_EXDATE_PROPERTY of type ICalGLib.PropertyKind>, 36: <enum I_CAL_EXPAND_PROPERTY of type ICalGLib.PropertyKind>, 37: <enum I_CAL_EXRULE_PROPERTY of type ICalGLib.PropertyKind>, 38: <enum I_CAL_FREEBUSY_PROPERTY of type ICalGLib.PropertyKind>, 39: <enum I_CAL_GEO_PROPERTY of type ICalGLib.PropertyKind>, 40: <enum I_CAL_GRANT_PROPERTY of type ICalGLib.PropertyKind>, 41: <enum I_CAL_ITIPVERSION_PROPERTY of type ICalGLib.PropertyKind>, 42: <enum I_CAL_LASTMODIFIED_PROPERTY of type ICalGLib.PropertyKind>, 43: <enum I_CAL_LOCATION_PROPERTY of type ICalGLib.PropertyKind>, 44: <enum I_CAL_MAXCOMPONENTSIZE_PROPERTY of type ICalGLib.PropertyKind>, 45: <enum I_CAL_MAXDATE_PROPERTY of type ICalGLib.PropertyKind>, 46: <enum I_CAL_MAXRESULTS_PROPERTY of type ICalGLib.PropertyKind>, 47: <enum I_CAL_MAXRESULTSSIZE_PROPERTY of type ICalGLib.PropertyKind>, 48: <enum I_CAL_METHOD_PROPERTY of type ICalGLib.PropertyKind>, 49: <enum I_CAL_MINDATE_PROPERTY of type ICalGLib.PropertyKind>, 50: <enum I_CAL_MULTIPART_PROPERTY of type ICalGLib.PropertyKind>, 115: <enum I_CAL_NAME_PROPERTY of type ICalGLib.PropertyKind>, 52: <enum I_CAL_ORGANIZER_PROPERTY of type ICalGLib.PropertyKind>, 53: <enum I_CAL_OWNER_PROPERTY of type ICalGLib.PropertyKind>, 54: <enum I_CAL_PERCENTCOMPLETE_PROPERTY of type ICalGLib.PropertyKind>, 55: <enum I_CAL_PERMISSION_PROPERTY of type ICalGLib.PropertyKind>, 110: <enum I_CAL_POLLCOMPLETION_PROPERTY of type ICalGLib.PropertyKind>, 103: <enum I_CAL_POLLITEMID_PROPERTY of type ICalGLib.PropertyKind>, 104: <enum I_CAL_POLLMODE_PROPERTY of type ICalGLib.PropertyKind>, 105: <enum I_CAL_POLLPROPERTIES_PROPERTY of type ICalGLib.PropertyKind>, 106: <enum I_CAL_POLLWINNER_PROPERTY of type ICalGLib.PropertyKind>, 56: <enum I_CAL_PRIORITY_PROPERTY of type ICalGLib.PropertyKind>, 57: <enum I_CAL_PRODID_PROPERTY of type ICalGLib.PropertyKind>, 58: <enum I_CAL_QUERY_PROPERTY of type ICalGLib.PropertyKind>, 59: <enum I_CAL_QUERYLEVEL_PROPERTY of type ICalGLib.PropertyKind>, 60: <enum I_CAL_QUERYID_PROPERTY of type ICalGLib.PropertyKind>, 61: <enum I_CAL_QUERYNAME_PROPERTY of type ICalGLib.PropertyKind>, 62: <enum I_CAL_RDATE_PROPERTY of type ICalGLib.PropertyKind>, 63: <enum I_CAL_RECURACCEPTED_PROPERTY of type ICalGLib.PropertyKind>, 64: <enum I_CAL_RECUREXPAND_PROPERTY of type ICalGLib.PropertyKind>, 65: <enum I_CAL_RECURLIMIT_PROPERTY of type ICalGLib.PropertyKind>, 66: <enum I_CAL_RECURRENCEID_PROPERTY of type ICalGLib.PropertyKind>, 67: <enum I_CAL_RELATEDTO_PROPERTY of type ICalGLib.PropertyKind>, 68: <enum I_CAL_RELCALID_PROPERTY of type ICalGLib.PropertyKind>, 69: <enum I_CAL_REPEAT_PROPERTY of type ICalGLib.PropertyKind>, 111: <enum I_CAL_REPLYURL_PROPERTY of type ICalGLib.PropertyKind>, 70: <enum I_CAL_REQUESTSTATUS_PROPERTY of type ICalGLib.PropertyKind>, 71: <enum I_CAL_RESOURCES_PROPERTY of type ICalGLib.PropertyKind>, 112: <enum I_CAL_RESPONSE_PROPERTY of type ICalGLib.PropertyKind>, 72: <enum I_CAL_RESTRICTION_PROPERTY of type ICalGLib.PropertyKind>, 73: <enum I_CAL_RRULE_PROPERTY of type ICalGLib.PropertyKind>, 74: <enum I_CAL_SCOPE_PROPERTY of type ICalGLib.PropertyKind>, 75: <enum I_CAL_SEQUENCE_PROPERTY of type ICalGLib.PropertyKind>, 76: <enum I_CAL_STATUS_PROPERTY of type ICalGLib.PropertyKind>, 77: <enum I_CAL_STORESEXPANDED_PROPERTY of type ICalGLib.PropertyKind>, 78: <enum I_CAL_SUMMARY_PROPERTY of type ICalGLib.PropertyKind>, 79: <enum I_CAL_TARGET_PROPERTY of type ICalGLib.PropertyKind>, 114: <enum I_CAL_TASKMODE_PROPERTY of type ICalGLib.PropertyKind>, 80: <enum I_CAL_TRANSP_PROPERTY of type ICalGLib.PropertyKind>, 81: <enum I_CAL_TRIGGER_PROPERTY of type ICalGLib.PropertyKind>, 82: <enum I_CAL_TZID_PROPERTY of type ICalGLib.PropertyKind>, 108: <enum I_CAL_TZIDALIASOF_PROPERTY of type ICalGLib.PropertyKind>, 83: <enum I_CAL_TZNAME_PROPERTY of type ICalGLib.PropertyKind>, 84: <enum I_CAL_TZOFFSETFROM_PROPERTY of type ICalGLib.PropertyKind>, 85: <enum I_CAL_TZOFFSETTO_PROPERTY of type ICalGLib.PropertyKind>, 109: <enum I_CAL_TZUNTIL_PROPERTY of type ICalGLib.PropertyKind>, 86: <enum I_CAL_TZURL_PROPERTY of type ICalGLib.PropertyKind>, 87: <enum I_CAL_UID_PROPERTY of type ICalGLib.PropertyKind>, 88: <enum I_CAL_URL_PROPERTY of type ICalGLib.PropertyKind>, 89: <enum I_CAL_VERSION_PROPERTY of type ICalGLib.PropertyKind>, 107: <enum I_CAL_VOTER_PROPERTY of type ICalGLib.PropertyKind>, 90: <enum I_CAL_X_PROPERTY of type ICalGLib.PropertyKind>, 91: <enum I_CAL_XLICCLASS_PROPERTY of type ICalGLib.PropertyKind>, 92: <enum I_CAL_XLICCLUSTERCOUNT_PROPERTY of type ICalGLib.PropertyKind>, 93: <enum I_CAL_XLICERROR_PROPERTY of type ICalGLib.PropertyKind>, 94: <enum I_CAL_XLICMIMECHARSET_PROPERTY of type ICalGLib.PropertyKind>, 95: <enum I_CAL_XLICMIMECID_PROPERTY of type ICalGLib.PropertyKind>, 96: <enum I_CAL_XLICMIMECONTENTTYPE_PROPERTY of type ICalGLib.PropertyKind>, 97: <enum I_CAL_XLICMIMEENCODING_PROPERTY of type ICalGLib.PropertyKind>, 98: <enum I_CAL_XLICMIMEFILENAME_PROPERTY of type ICalGLib.PropertyKind>, 99: <enum I_CAL_XLICMIMEOPTINFO_PROPERTY of type ICalGLib.PropertyKind>, 100: <enum I_CAL_NO_PROPERTY of type ICalGLib.PropertyKind>}, '__info__': gi.EnumInfo(PropertyKind), 'ANY_PROPERTY': <enum I_CAL_ANY_PROPERTY of type ICalGLib.PropertyKind>, 'ACCEPTRESPONSE_PROPERTY': <enum I_CAL_ACCEPTRESPONSE_PROPERTY of type ICalGLib.PropertyKind>, 'ACKNOWLEDGED_PROPERTY': <enum I_CAL_ACKNOWLEDGED_PROPERTY of type ICalGLib.PropertyKind>, 'ACTION_PROPERTY': <enum I_CAL_ACTION_PROPERTY of type ICalGLib.PropertyKind>, 'ALLOWCONFLICT_PROPERTY': <enum I_CAL_ALLOWCONFLICT_PROPERTY of type ICalGLib.PropertyKind>, 'ATTACH_PROPERTY': <enum I_CAL_ATTACH_PROPERTY of type ICalGLib.PropertyKind>, 'ATTENDEE_PROPERTY': <enum I_CAL_ATTENDEE_PROPERTY of type ICalGLib.PropertyKind>, 'BUSYTYPE_PROPERTY': <enum I_CAL_BUSYTYPE_PROPERTY of type ICalGLib.PropertyKind>, 'CALID_PROPERTY': <enum I_CAL_CALID_PROPERTY of type ICalGLib.PropertyKind>, 'CALMASTER_PROPERTY': <enum I_CAL_CALMASTER_PROPERTY of type ICalGLib.PropertyKind>, 'CALSCALE_PROPERTY': <enum I_CAL_CALSCALE_PROPERTY of type ICalGLib.PropertyKind>, 'CAPVERSION_PROPERTY': <enum I_CAL_CAPVERSION_PROPERTY of type ICalGLib.PropertyKind>, 'CARLEVEL_PROPERTY': <enum I_CAL_CARLEVEL_PROPERTY of type ICalGLib.PropertyKind>, 'CARID_PROPERTY': <enum I_CAL_CARID_PROPERTY of type ICalGLib.PropertyKind>, 'CATEGORIES_PROPERTY': <enum I_CAL_CATEGORIES_PROPERTY of type ICalGLib.PropertyKind>, 'CLASS_PROPERTY': <enum I_CAL_CLASS_PROPERTY of type ICalGLib.PropertyKind>, 'CMD_PROPERTY': <enum I_CAL_CMD_PROPERTY of type ICalGLib.PropertyKind>, 'COLOR_PROPERTY': <enum I_CAL_COLOR_PROPERTY of type ICalGLib.PropertyKind>, 'COMMENT_PROPERTY': <enum I_CAL_COMMENT_PROPERTY of type ICalGLib.PropertyKind>, 'COMPLETED_PROPERTY': <enum I_CAL_COMPLETED_PROPERTY of type ICalGLib.PropertyKind>, 'COMPONENTS_PROPERTY': <enum I_CAL_COMPONENTS_PROPERTY of type ICalGLib.PropertyKind>, 'CONTACT_PROPERTY': <enum I_CAL_CONTACT_PROPERTY of type ICalGLib.PropertyKind>, 'CREATED_PROPERTY': <enum I_CAL_CREATED_PROPERTY of type ICalGLib.PropertyKind>, 'CSID_PROPERTY': <enum I_CAL_CSID_PROPERTY of type ICalGLib.PropertyKind>, 'DATEMAX_PROPERTY': <enum I_CAL_DATEMAX_PROPERTY of type ICalGLib.PropertyKind>, 'DATEMIN_PROPERTY': <enum I_CAL_DATEMIN_PROPERTY of type ICalGLib.PropertyKind>, 'DECREED_PROPERTY': <enum I_CAL_DECREED_PROPERTY of type ICalGLib.PropertyKind>, 'DEFAULTCHARSET_PROPERTY': <enum I_CAL_DEFAULTCHARSET_PROPERTY of type ICalGLib.PropertyKind>, 'DEFAULTLOCALE_PROPERTY': <enum I_CAL_DEFAULTLOCALE_PROPERTY of type ICalGLib.PropertyKind>, 'DEFAULTTZID_PROPERTY': <enum I_CAL_DEFAULTTZID_PROPERTY of type ICalGLib.PropertyKind>, 'DEFAULTVCARS_PROPERTY': <enum I_CAL_DEFAULTVCARS_PROPERTY of type ICalGLib.PropertyKind>, 'DENY_PROPERTY': <enum I_CAL_DENY_PROPERTY of type ICalGLib.PropertyKind>, 'DESCRIPTION_PROPERTY': <enum I_CAL_DESCRIPTION_PROPERTY of type ICalGLib.PropertyKind>, 'DTEND_PROPERTY': <enum I_CAL_DTEND_PROPERTY of type ICalGLib.PropertyKind>, 'DTSTAMP_PROPERTY': <enum I_CAL_DTSTAMP_PROPERTY of type ICalGLib.PropertyKind>, 'DTSTART_PROPERTY': <enum I_CAL_DTSTART_PROPERTY of type ICalGLib.PropertyKind>, 'DUE_PROPERTY': <enum I_CAL_DUE_PROPERTY of type ICalGLib.PropertyKind>, 'DURATION_PROPERTY': <enum I_CAL_DURATION_PROPERTY of type ICalGLib.PropertyKind>, 'ESTIMATEDDURATION_PROPERTY': <enum I_CAL_ESTIMATEDDURATION_PROPERTY of type ICalGLib.PropertyKind>, 'EXDATE_PROPERTY': <enum I_CAL_EXDATE_PROPERTY of type ICalGLib.PropertyKind>, 'EXPAND_PROPERTY': <enum I_CAL_EXPAND_PROPERTY of type ICalGLib.PropertyKind>, 'EXRULE_PROPERTY': <enum I_CAL_EXRULE_PROPERTY of type ICalGLib.PropertyKind>, 'FREEBUSY_PROPERTY': <enum I_CAL_FREEBUSY_PROPERTY of type ICalGLib.PropertyKind>, 'GEO_PROPERTY': <enum I_CAL_GEO_PROPERTY of type ICalGLib.PropertyKind>, 'GRANT_PROPERTY': <enum I_CAL_GRANT_PROPERTY of type ICalGLib.PropertyKind>, 'ITIPVERSION_PROPERTY': <enum I_CAL_ITIPVERSION_PROPERTY of type ICalGLib.PropertyKind>, 'LASTMODIFIED_PROPERTY': <enum I_CAL_LASTMODIFIED_PROPERTY of type ICalGLib.PropertyKind>, 'LOCATION_PROPERTY': <enum I_CAL_LOCATION_PROPERTY of type ICalGLib.PropertyKind>, 'MAXCOMPONENTSIZE_PROPERTY': <enum I_CAL_MAXCOMPONENTSIZE_PROPERTY of type ICalGLib.PropertyKind>, 'MAXDATE_PROPERTY': <enum I_CAL_MAXDATE_PROPERTY of type ICalGLib.PropertyKind>, 'MAXRESULTS_PROPERTY': <enum I_CAL_MAXRESULTS_PROPERTY of type ICalGLib.PropertyKind>, 'MAXRESULTSSIZE_PROPERTY': <enum I_CAL_MAXRESULTSSIZE_PROPERTY of type ICalGLib.PropertyKind>, 'METHOD_PROPERTY': <enum I_CAL_METHOD_PROPERTY of type ICalGLib.PropertyKind>, 'MINDATE_PROPERTY': <enum I_CAL_MINDATE_PROPERTY of type ICalGLib.PropertyKind>, 'MULTIPART_PROPERTY': <enum I_CAL_MULTIPART_PROPERTY of type ICalGLib.PropertyKind>, 'NAME_PROPERTY': <enum I_CAL_NAME_PROPERTY of type ICalGLib.PropertyKind>, 'ORGANIZER_PROPERTY': <enum I_CAL_ORGANIZER_PROPERTY of type ICalGLib.PropertyKind>, 'OWNER_PROPERTY': <enum I_CAL_OWNER_PROPERTY of type ICalGLib.PropertyKind>, 'PERCENTCOMPLETE_PROPERTY': <enum I_CAL_PERCENTCOMPLETE_PROPERTY of type ICalGLib.PropertyKind>, 'PERMISSION_PROPERTY': <enum I_CAL_PERMISSION_PROPERTY of type ICalGLib.PropertyKind>, 'POLLCOMPLETION_PROPERTY': <enum I_CAL_POLLCOMPLETION_PROPERTY of type ICalGLib.PropertyKind>, 'POLLITEMID_PROPERTY': <enum I_CAL_POLLITEMID_PROPERTY of type ICalGLib.PropertyKind>, 'POLLMODE_PROPERTY': <enum I_CAL_POLLMODE_PROPERTY of type ICalGLib.PropertyKind>, 'POLLPROPERTIES_PROPERTY': <enum I_CAL_POLLPROPERTIES_PROPERTY of type ICalGLib.PropertyKind>, 'POLLWINNER_PROPERTY': <enum I_CAL_POLLWINNER_PROPERTY of type ICalGLib.PropertyKind>, 'PRIORITY_PROPERTY': <enum I_CAL_PRIORITY_PROPERTY of type ICalGLib.PropertyKind>, 'PRODID_PROPERTY': <enum I_CAL_PRODID_PROPERTY of type ICalGLib.PropertyKind>, 'QUERY_PROPERTY': <enum I_CAL_QUERY_PROPERTY of type ICalGLib.PropertyKind>, 'QUERYLEVEL_PROPERTY': <enum I_CAL_QUERYLEVEL_PROPERTY of type ICalGLib.PropertyKind>, 'QUERYID_PROPERTY': <enum I_CAL_QUERYID_PROPERTY of type ICalGLib.PropertyKind>, 'QUERYNAME_PROPERTY': <enum I_CAL_QUERYNAME_PROPERTY of type ICalGLib.PropertyKind>, 'RDATE_PROPERTY': <enum I_CAL_RDATE_PROPERTY of type ICalGLib.PropertyKind>, 'RECURACCEPTED_PROPERTY': <enum I_CAL_RECURACCEPTED_PROPERTY of type ICalGLib.PropertyKind>, 'RECUREXPAND_PROPERTY': <enum I_CAL_RECUREXPAND_PROPERTY of type ICalGLib.PropertyKind>, 'RECURLIMIT_PROPERTY': <enum I_CAL_RECURLIMIT_PROPERTY of type ICalGLib.PropertyKind>, 'RECURRENCEID_PROPERTY': <enum I_CAL_RECURRENCEID_PROPERTY of type ICalGLib.PropertyKind>, 'RELATEDTO_PROPERTY': <enum I_CAL_RELATEDTO_PROPERTY of type ICalGLib.PropertyKind>, 'RELCALID_PROPERTY': <enum I_CAL_RELCALID_PROPERTY of type ICalGLib.PropertyKind>, 'REPEAT_PROPERTY': <enum I_CAL_REPEAT_PROPERTY of type ICalGLib.PropertyKind>, 'REPLYURL_PROPERTY': <enum I_CAL_REPLYURL_PROPERTY of type ICalGLib.PropertyKind>, 'REQUESTSTATUS_PROPERTY': <enum I_CAL_REQUESTSTATUS_PROPERTY of type ICalGLib.PropertyKind>, 'RESOURCES_PROPERTY': <enum I_CAL_RESOURCES_PROPERTY of type ICalGLib.PropertyKind>, 'RESPONSE_PROPERTY': <enum I_CAL_RESPONSE_PROPERTY of type ICalGLib.PropertyKind>, 'RESTRICTION_PROPERTY': <enum I_CAL_RESTRICTION_PROPERTY of type ICalGLib.PropertyKind>, 'RRULE_PROPERTY': <enum I_CAL_RRULE_PROPERTY of type ICalGLib.PropertyKind>, 'SCOPE_PROPERTY': <enum I_CAL_SCOPE_PROPERTY of type ICalGLib.PropertyKind>, 'SEQUENCE_PROPERTY': <enum I_CAL_SEQUENCE_PROPERTY of type ICalGLib.PropertyKind>, 'STATUS_PROPERTY': <enum I_CAL_STATUS_PROPERTY of type ICalGLib.PropertyKind>, 'STORESEXPANDED_PROPERTY': <enum I_CAL_STORESEXPANDED_PROPERTY of type ICalGLib.PropertyKind>, 'SUMMARY_PROPERTY': <enum I_CAL_SUMMARY_PROPERTY of type ICalGLib.PropertyKind>, 'TARGET_PROPERTY': <enum I_CAL_TARGET_PROPERTY of type ICalGLib.PropertyKind>, 'TASKMODE_PROPERTY': <enum I_CAL_TASKMODE_PROPERTY of type ICalGLib.PropertyKind>, 'TRANSP_PROPERTY': <enum I_CAL_TRANSP_PROPERTY of type ICalGLib.PropertyKind>, 'TRIGGER_PROPERTY': <enum I_CAL_TRIGGER_PROPERTY of type ICalGLib.PropertyKind>, 'TZID_PROPERTY': <enum I_CAL_TZID_PROPERTY of type ICalGLib.PropertyKind>, 'TZIDALIASOF_PROPERTY': <enum I_CAL_TZIDALIASOF_PROPERTY of type ICalGLib.PropertyKind>, 'TZNAME_PROPERTY': <enum I_CAL_TZNAME_PROPERTY of type ICalGLib.PropertyKind>, 'TZOFFSETFROM_PROPERTY': <enum I_CAL_TZOFFSETFROM_PROPERTY of type ICalGLib.PropertyKind>, 'TZOFFSETTO_PROPERTY': <enum I_CAL_TZOFFSETTO_PROPERTY of type ICalGLib.PropertyKind>, 'TZUNTIL_PROPERTY': <enum I_CAL_TZUNTIL_PROPERTY of type ICalGLib.PropertyKind>, 'TZURL_PROPERTY': <enum I_CAL_TZURL_PROPERTY of type ICalGLib.PropertyKind>, 'UID_PROPERTY': <enum I_CAL_UID_PROPERTY of type ICalGLib.PropertyKind>, 'URL_PROPERTY': <enum I_CAL_URL_PROPERTY of type ICalGLib.PropertyKind>, 'VERSION_PROPERTY': <enum I_CAL_VERSION_PROPERTY of type ICalGLib.PropertyKind>, 'VOTER_PROPERTY': <enum I_CAL_VOTER_PROPERTY of type ICalGLib.PropertyKind>, 'X_PROPERTY': <enum I_CAL_X_PROPERTY of type ICalGLib.PropertyKind>, 'XLICCLASS_PROPERTY': <enum I_CAL_XLICCLASS_PROPERTY of type ICalGLib.PropertyKind>, 'XLICCLUSTERCOUNT_PROPERTY': <enum I_CAL_XLICCLUSTERCOUNT_PROPERTY of type ICalGLib.PropertyKind>, 'XLICERROR_PROPERTY': <enum I_CAL_XLICERROR_PROPERTY of type ICalGLib.PropertyKind>, 'XLICMIMECHARSET_PROPERTY': <enum I_CAL_XLICMIMECHARSET_PROPERTY of type ICalGLib.PropertyKind>, 'XLICMIMECID_PROPERTY': <enum I_CAL_XLICMIMECID_PROPERTY of type ICalGLib.PropertyKind>, 'XLICMIMECONTENTTYPE_PROPERTY': <enum I_CAL_XLICMIMECONTENTTYPE_PROPERTY of type ICalGLib.PropertyKind>, 'XLICMIMEENCODING_PROPERTY': <enum I_CAL_XLICMIMEENCODING_PROPERTY of type ICalGLib.PropertyKind>, 'XLICMIMEFILENAME_PROPERTY': <enum I_CAL_XLICMIMEFILENAME_PROPERTY of type ICalGLib.PropertyKind>, 'XLICMIMEOPTINFO_PROPERTY': <enum I_CAL_XLICMIMEOPTINFO_PROPERTY of type ICalGLib.PropertyKind>, 'NO_PROPERTY': <enum I_CAL_NO_PROPERTY of type ICalGLib.PropertyKind>})"
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
        70: 70,
        71: 71,
        72: 72,
        73: 73,
        74: 74,
        75: 75,
        76: 76,
        77: 77,
        78: 78,
        79: 79,
        80: 80,
        81: 81,
        82: 82,
        83: 83,
        84: 84,
        85: 85,
        86: 86,
        87: 87,
        88: 88,
        89: 89,
        90: 90,
        91: 91,
        92: 92,
        93: 93,
        94: 94,
        95: 95,
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        110: 110,
        111: 111,
        112: 112,
        113: 113,
        114: 114,
        115: 115,
        118: 118,
    }
    __gtype__ = None # (!) real value is '<GType PyICalGLibPropertyKind (94403188461360)>'
    __info__ = gi.EnumInfo(PropertyKind)


