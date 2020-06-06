# encoding: utf-8
# module gi.repository.ICal
# from /usr/lib64/girepository-1.0/ICal-3.0.typelib
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
import gobject as __gobject


class property_kind(__gobject.GEnum):
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
    CONFERENCE_PROPERTY = 120
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
    IMAGE_PROPERTY = 119
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
    PATCHDELETE_PROPERTY = 124
    PATCHORDER_PROPERTY = 122
    PATCHPARAMETER_PROPERTY = 125
    PATCHTARGET_PROPERTY = 123
    PATCHVERSION_PROPERTY = 121
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
    REFRESHINTERVAL_PROPERTY = 116
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
    SOURCE_PROPERTY = 117
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ICal', '__dict__': <attribute '__dict__' of 'property_kind' objects>, '__doc__': None, '__gtype__': <GType PyICalproperty_kind (94628528780864)>, '__enum_values__': {0: <enum ICAL_ANY_PROPERTY of type ICal.property_kind>, 102: <enum ICAL_ACCEPTRESPONSE_PROPERTY of type ICal.property_kind>, 1: <enum ICAL_ACKNOWLEDGED_PROPERTY of type ICal.property_kind>, 2: <enum ICAL_ACTION_PROPERTY of type ICal.property_kind>, 3: <enum ICAL_ALLOWCONFLICT_PROPERTY of type ICal.property_kind>, 4: <enum ICAL_ATTACH_PROPERTY of type ICal.property_kind>, 5: <enum ICAL_ATTENDEE_PROPERTY of type ICal.property_kind>, 101: <enum ICAL_BUSYTYPE_PROPERTY of type ICal.property_kind>, 6: <enum ICAL_CALID_PROPERTY of type ICal.property_kind>, 7: <enum ICAL_CALMASTER_PROPERTY of type ICal.property_kind>, 8: <enum ICAL_CALSCALE_PROPERTY of type ICal.property_kind>, 9: <enum ICAL_CAPVERSION_PROPERTY of type ICal.property_kind>, 10: <enum ICAL_CARLEVEL_PROPERTY of type ICal.property_kind>, 11: <enum ICAL_CARID_PROPERTY of type ICal.property_kind>, 12: <enum ICAL_CATEGORIES_PROPERTY of type ICal.property_kind>, 13: <enum ICAL_CLASS_PROPERTY of type ICal.property_kind>, 14: <enum ICAL_CMD_PROPERTY of type ICal.property_kind>, 118: <enum ICAL_COLOR_PROPERTY of type ICal.property_kind>, 15: <enum ICAL_COMMENT_PROPERTY of type ICal.property_kind>, 16: <enum ICAL_COMPLETED_PROPERTY of type ICal.property_kind>, 17: <enum ICAL_COMPONENTS_PROPERTY of type ICal.property_kind>, 120: <enum ICAL_CONFERENCE_PROPERTY of type ICal.property_kind>, 18: <enum ICAL_CONTACT_PROPERTY of type ICal.property_kind>, 19: <enum ICAL_CREATED_PROPERTY of type ICal.property_kind>, 20: <enum ICAL_CSID_PROPERTY of type ICal.property_kind>, 21: <enum ICAL_DATEMAX_PROPERTY of type ICal.property_kind>, 22: <enum ICAL_DATEMIN_PROPERTY of type ICal.property_kind>, 23: <enum ICAL_DECREED_PROPERTY of type ICal.property_kind>, 24: <enum ICAL_DEFAULTCHARSET_PROPERTY of type ICal.property_kind>, 25: <enum ICAL_DEFAULTLOCALE_PROPERTY of type ICal.property_kind>, 26: <enum ICAL_DEFAULTTZID_PROPERTY of type ICal.property_kind>, 27: <enum ICAL_DEFAULTVCARS_PROPERTY of type ICal.property_kind>, 28: <enum ICAL_DENY_PROPERTY of type ICal.property_kind>, 29: <enum ICAL_DESCRIPTION_PROPERTY of type ICal.property_kind>, 30: <enum ICAL_DTEND_PROPERTY of type ICal.property_kind>, 31: <enum ICAL_DTSTAMP_PROPERTY of type ICal.property_kind>, 32: <enum ICAL_DTSTART_PROPERTY of type ICal.property_kind>, 33: <enum ICAL_DUE_PROPERTY of type ICal.property_kind>, 34: <enum ICAL_DURATION_PROPERTY of type ICal.property_kind>, 113: <enum ICAL_ESTIMATEDDURATION_PROPERTY of type ICal.property_kind>, 35: <enum ICAL_EXDATE_PROPERTY of type ICal.property_kind>, 36: <enum ICAL_EXPAND_PROPERTY of type ICal.property_kind>, 37: <enum ICAL_EXRULE_PROPERTY of type ICal.property_kind>, 38: <enum ICAL_FREEBUSY_PROPERTY of type ICal.property_kind>, 39: <enum ICAL_GEO_PROPERTY of type ICal.property_kind>, 40: <enum ICAL_GRANT_PROPERTY of type ICal.property_kind>, 119: <enum ICAL_IMAGE_PROPERTY of type ICal.property_kind>, 41: <enum ICAL_ITIPVERSION_PROPERTY of type ICal.property_kind>, 42: <enum ICAL_LASTMODIFIED_PROPERTY of type ICal.property_kind>, 43: <enum ICAL_LOCATION_PROPERTY of type ICal.property_kind>, 44: <enum ICAL_MAXCOMPONENTSIZE_PROPERTY of type ICal.property_kind>, 45: <enum ICAL_MAXDATE_PROPERTY of type ICal.property_kind>, 46: <enum ICAL_MAXRESULTS_PROPERTY of type ICal.property_kind>, 47: <enum ICAL_MAXRESULTSSIZE_PROPERTY of type ICal.property_kind>, 48: <enum ICAL_METHOD_PROPERTY of type ICal.property_kind>, 49: <enum ICAL_MINDATE_PROPERTY of type ICal.property_kind>, 50: <enum ICAL_MULTIPART_PROPERTY of type ICal.property_kind>, 115: <enum ICAL_NAME_PROPERTY of type ICal.property_kind>, 52: <enum ICAL_ORGANIZER_PROPERTY of type ICal.property_kind>, 53: <enum ICAL_OWNER_PROPERTY of type ICal.property_kind>, 124: <enum ICAL_PATCHDELETE_PROPERTY of type ICal.property_kind>, 122: <enum ICAL_PATCHORDER_PROPERTY of type ICal.property_kind>, 125: <enum ICAL_PATCHPARAMETER_PROPERTY of type ICal.property_kind>, 123: <enum ICAL_PATCHTARGET_PROPERTY of type ICal.property_kind>, 121: <enum ICAL_PATCHVERSION_PROPERTY of type ICal.property_kind>, 54: <enum ICAL_PERCENTCOMPLETE_PROPERTY of type ICal.property_kind>, 55: <enum ICAL_PERMISSION_PROPERTY of type ICal.property_kind>, 110: <enum ICAL_POLLCOMPLETION_PROPERTY of type ICal.property_kind>, 103: <enum ICAL_POLLITEMID_PROPERTY of type ICal.property_kind>, 104: <enum ICAL_POLLMODE_PROPERTY of type ICal.property_kind>, 105: <enum ICAL_POLLPROPERTIES_PROPERTY of type ICal.property_kind>, 106: <enum ICAL_POLLWINNER_PROPERTY of type ICal.property_kind>, 56: <enum ICAL_PRIORITY_PROPERTY of type ICal.property_kind>, 57: <enum ICAL_PRODID_PROPERTY of type ICal.property_kind>, 58: <enum ICAL_QUERY_PROPERTY of type ICal.property_kind>, 59: <enum ICAL_QUERYLEVEL_PROPERTY of type ICal.property_kind>, 60: <enum ICAL_QUERYID_PROPERTY of type ICal.property_kind>, 61: <enum ICAL_QUERYNAME_PROPERTY of type ICal.property_kind>, 62: <enum ICAL_RDATE_PROPERTY of type ICal.property_kind>, 63: <enum ICAL_RECURACCEPTED_PROPERTY of type ICal.property_kind>, 64: <enum ICAL_RECUREXPAND_PROPERTY of type ICal.property_kind>, 65: <enum ICAL_RECURLIMIT_PROPERTY of type ICal.property_kind>, 66: <enum ICAL_RECURRENCEID_PROPERTY of type ICal.property_kind>, 116: <enum ICAL_REFRESHINTERVAL_PROPERTY of type ICal.property_kind>, 67: <enum ICAL_RELATEDTO_PROPERTY of type ICal.property_kind>, 68: <enum ICAL_RELCALID_PROPERTY of type ICal.property_kind>, 69: <enum ICAL_REPEAT_PROPERTY of type ICal.property_kind>, 111: <enum ICAL_REPLYURL_PROPERTY of type ICal.property_kind>, 70: <enum ICAL_REQUESTSTATUS_PROPERTY of type ICal.property_kind>, 71: <enum ICAL_RESOURCES_PROPERTY of type ICal.property_kind>, 112: <enum ICAL_RESPONSE_PROPERTY of type ICal.property_kind>, 72: <enum ICAL_RESTRICTION_PROPERTY of type ICal.property_kind>, 73: <enum ICAL_RRULE_PROPERTY of type ICal.property_kind>, 74: <enum ICAL_SCOPE_PROPERTY of type ICal.property_kind>, 75: <enum ICAL_SEQUENCE_PROPERTY of type ICal.property_kind>, 117: <enum ICAL_SOURCE_PROPERTY of type ICal.property_kind>, 76: <enum ICAL_STATUS_PROPERTY of type ICal.property_kind>, 77: <enum ICAL_STORESEXPANDED_PROPERTY of type ICal.property_kind>, 78: <enum ICAL_SUMMARY_PROPERTY of type ICal.property_kind>, 79: <enum ICAL_TARGET_PROPERTY of type ICal.property_kind>, 114: <enum ICAL_TASKMODE_PROPERTY of type ICal.property_kind>, 80: <enum ICAL_TRANSP_PROPERTY of type ICal.property_kind>, 81: <enum ICAL_TRIGGER_PROPERTY of type ICal.property_kind>, 82: <enum ICAL_TZID_PROPERTY of type ICal.property_kind>, 108: <enum ICAL_TZIDALIASOF_PROPERTY of type ICal.property_kind>, 83: <enum ICAL_TZNAME_PROPERTY of type ICal.property_kind>, 84: <enum ICAL_TZOFFSETFROM_PROPERTY of type ICal.property_kind>, 85: <enum ICAL_TZOFFSETTO_PROPERTY of type ICal.property_kind>, 109: <enum ICAL_TZUNTIL_PROPERTY of type ICal.property_kind>, 86: <enum ICAL_TZURL_PROPERTY of type ICal.property_kind>, 87: <enum ICAL_UID_PROPERTY of type ICal.property_kind>, 88: <enum ICAL_URL_PROPERTY of type ICal.property_kind>, 89: <enum ICAL_VERSION_PROPERTY of type ICal.property_kind>, 107: <enum ICAL_VOTER_PROPERTY of type ICal.property_kind>, 90: <enum ICAL_X_PROPERTY of type ICal.property_kind>, 91: <enum ICAL_XLICCLASS_PROPERTY of type ICal.property_kind>, 92: <enum ICAL_XLICCLUSTERCOUNT_PROPERTY of type ICal.property_kind>, 93: <enum ICAL_XLICERROR_PROPERTY of type ICal.property_kind>, 94: <enum ICAL_XLICMIMECHARSET_PROPERTY of type ICal.property_kind>, 95: <enum ICAL_XLICMIMECID_PROPERTY of type ICal.property_kind>, 96: <enum ICAL_XLICMIMECONTENTTYPE_PROPERTY of type ICal.property_kind>, 97: <enum ICAL_XLICMIMEENCODING_PROPERTY of type ICal.property_kind>, 98: <enum ICAL_XLICMIMEFILENAME_PROPERTY of type ICal.property_kind>, 99: <enum ICAL_XLICMIMEOPTINFO_PROPERTY of type ICal.property_kind>, 100: <enum ICAL_NO_PROPERTY of type ICal.property_kind>}, '__info__': gi.EnumInfo(property_kind), 'ANY_PROPERTY': <enum ICAL_ANY_PROPERTY of type ICal.property_kind>, 'ACCEPTRESPONSE_PROPERTY': <enum ICAL_ACCEPTRESPONSE_PROPERTY of type ICal.property_kind>, 'ACKNOWLEDGED_PROPERTY': <enum ICAL_ACKNOWLEDGED_PROPERTY of type ICal.property_kind>, 'ACTION_PROPERTY': <enum ICAL_ACTION_PROPERTY of type ICal.property_kind>, 'ALLOWCONFLICT_PROPERTY': <enum ICAL_ALLOWCONFLICT_PROPERTY of type ICal.property_kind>, 'ATTACH_PROPERTY': <enum ICAL_ATTACH_PROPERTY of type ICal.property_kind>, 'ATTENDEE_PROPERTY': <enum ICAL_ATTENDEE_PROPERTY of type ICal.property_kind>, 'BUSYTYPE_PROPERTY': <enum ICAL_BUSYTYPE_PROPERTY of type ICal.property_kind>, 'CALID_PROPERTY': <enum ICAL_CALID_PROPERTY of type ICal.property_kind>, 'CALMASTER_PROPERTY': <enum ICAL_CALMASTER_PROPERTY of type ICal.property_kind>, 'CALSCALE_PROPERTY': <enum ICAL_CALSCALE_PROPERTY of type ICal.property_kind>, 'CAPVERSION_PROPERTY': <enum ICAL_CAPVERSION_PROPERTY of type ICal.property_kind>, 'CARLEVEL_PROPERTY': <enum ICAL_CARLEVEL_PROPERTY of type ICal.property_kind>, 'CARID_PROPERTY': <enum ICAL_CARID_PROPERTY of type ICal.property_kind>, 'CATEGORIES_PROPERTY': <enum ICAL_CATEGORIES_PROPERTY of type ICal.property_kind>, 'CLASS_PROPERTY': <enum ICAL_CLASS_PROPERTY of type ICal.property_kind>, 'CMD_PROPERTY': <enum ICAL_CMD_PROPERTY of type ICal.property_kind>, 'COLOR_PROPERTY': <enum ICAL_COLOR_PROPERTY of type ICal.property_kind>, 'COMMENT_PROPERTY': <enum ICAL_COMMENT_PROPERTY of type ICal.property_kind>, 'COMPLETED_PROPERTY': <enum ICAL_COMPLETED_PROPERTY of type ICal.property_kind>, 'COMPONENTS_PROPERTY': <enum ICAL_COMPONENTS_PROPERTY of type ICal.property_kind>, 'CONFERENCE_PROPERTY': <enum ICAL_CONFERENCE_PROPERTY of type ICal.property_kind>, 'CONTACT_PROPERTY': <enum ICAL_CONTACT_PROPERTY of type ICal.property_kind>, 'CREATED_PROPERTY': <enum ICAL_CREATED_PROPERTY of type ICal.property_kind>, 'CSID_PROPERTY': <enum ICAL_CSID_PROPERTY of type ICal.property_kind>, 'DATEMAX_PROPERTY': <enum ICAL_DATEMAX_PROPERTY of type ICal.property_kind>, 'DATEMIN_PROPERTY': <enum ICAL_DATEMIN_PROPERTY of type ICal.property_kind>, 'DECREED_PROPERTY': <enum ICAL_DECREED_PROPERTY of type ICal.property_kind>, 'DEFAULTCHARSET_PROPERTY': <enum ICAL_DEFAULTCHARSET_PROPERTY of type ICal.property_kind>, 'DEFAULTLOCALE_PROPERTY': <enum ICAL_DEFAULTLOCALE_PROPERTY of type ICal.property_kind>, 'DEFAULTTZID_PROPERTY': <enum ICAL_DEFAULTTZID_PROPERTY of type ICal.property_kind>, 'DEFAULTVCARS_PROPERTY': <enum ICAL_DEFAULTVCARS_PROPERTY of type ICal.property_kind>, 'DENY_PROPERTY': <enum ICAL_DENY_PROPERTY of type ICal.property_kind>, 'DESCRIPTION_PROPERTY': <enum ICAL_DESCRIPTION_PROPERTY of type ICal.property_kind>, 'DTEND_PROPERTY': <enum ICAL_DTEND_PROPERTY of type ICal.property_kind>, 'DTSTAMP_PROPERTY': <enum ICAL_DTSTAMP_PROPERTY of type ICal.property_kind>, 'DTSTART_PROPERTY': <enum ICAL_DTSTART_PROPERTY of type ICal.property_kind>, 'DUE_PROPERTY': <enum ICAL_DUE_PROPERTY of type ICal.property_kind>, 'DURATION_PROPERTY': <enum ICAL_DURATION_PROPERTY of type ICal.property_kind>, 'ESTIMATEDDURATION_PROPERTY': <enum ICAL_ESTIMATEDDURATION_PROPERTY of type ICal.property_kind>, 'EXDATE_PROPERTY': <enum ICAL_EXDATE_PROPERTY of type ICal.property_kind>, 'EXPAND_PROPERTY': <enum ICAL_EXPAND_PROPERTY of type ICal.property_kind>, 'EXRULE_PROPERTY': <enum ICAL_EXRULE_PROPERTY of type ICal.property_kind>, 'FREEBUSY_PROPERTY': <enum ICAL_FREEBUSY_PROPERTY of type ICal.property_kind>, 'GEO_PROPERTY': <enum ICAL_GEO_PROPERTY of type ICal.property_kind>, 'GRANT_PROPERTY': <enum ICAL_GRANT_PROPERTY of type ICal.property_kind>, 'IMAGE_PROPERTY': <enum ICAL_IMAGE_PROPERTY of type ICal.property_kind>, 'ITIPVERSION_PROPERTY': <enum ICAL_ITIPVERSION_PROPERTY of type ICal.property_kind>, 'LASTMODIFIED_PROPERTY': <enum ICAL_LASTMODIFIED_PROPERTY of type ICal.property_kind>, 'LOCATION_PROPERTY': <enum ICAL_LOCATION_PROPERTY of type ICal.property_kind>, 'MAXCOMPONENTSIZE_PROPERTY': <enum ICAL_MAXCOMPONENTSIZE_PROPERTY of type ICal.property_kind>, 'MAXDATE_PROPERTY': <enum ICAL_MAXDATE_PROPERTY of type ICal.property_kind>, 'MAXRESULTS_PROPERTY': <enum ICAL_MAXRESULTS_PROPERTY of type ICal.property_kind>, 'MAXRESULTSSIZE_PROPERTY': <enum ICAL_MAXRESULTSSIZE_PROPERTY of type ICal.property_kind>, 'METHOD_PROPERTY': <enum ICAL_METHOD_PROPERTY of type ICal.property_kind>, 'MINDATE_PROPERTY': <enum ICAL_MINDATE_PROPERTY of type ICal.property_kind>, 'MULTIPART_PROPERTY': <enum ICAL_MULTIPART_PROPERTY of type ICal.property_kind>, 'NAME_PROPERTY': <enum ICAL_NAME_PROPERTY of type ICal.property_kind>, 'ORGANIZER_PROPERTY': <enum ICAL_ORGANIZER_PROPERTY of type ICal.property_kind>, 'OWNER_PROPERTY': <enum ICAL_OWNER_PROPERTY of type ICal.property_kind>, 'PATCHDELETE_PROPERTY': <enum ICAL_PATCHDELETE_PROPERTY of type ICal.property_kind>, 'PATCHORDER_PROPERTY': <enum ICAL_PATCHORDER_PROPERTY of type ICal.property_kind>, 'PATCHPARAMETER_PROPERTY': <enum ICAL_PATCHPARAMETER_PROPERTY of type ICal.property_kind>, 'PATCHTARGET_PROPERTY': <enum ICAL_PATCHTARGET_PROPERTY of type ICal.property_kind>, 'PATCHVERSION_PROPERTY': <enum ICAL_PATCHVERSION_PROPERTY of type ICal.property_kind>, 'PERCENTCOMPLETE_PROPERTY': <enum ICAL_PERCENTCOMPLETE_PROPERTY of type ICal.property_kind>, 'PERMISSION_PROPERTY': <enum ICAL_PERMISSION_PROPERTY of type ICal.property_kind>, 'POLLCOMPLETION_PROPERTY': <enum ICAL_POLLCOMPLETION_PROPERTY of type ICal.property_kind>, 'POLLITEMID_PROPERTY': <enum ICAL_POLLITEMID_PROPERTY of type ICal.property_kind>, 'POLLMODE_PROPERTY': <enum ICAL_POLLMODE_PROPERTY of type ICal.property_kind>, 'POLLPROPERTIES_PROPERTY': <enum ICAL_POLLPROPERTIES_PROPERTY of type ICal.property_kind>, 'POLLWINNER_PROPERTY': <enum ICAL_POLLWINNER_PROPERTY of type ICal.property_kind>, 'PRIORITY_PROPERTY': <enum ICAL_PRIORITY_PROPERTY of type ICal.property_kind>, 'PRODID_PROPERTY': <enum ICAL_PRODID_PROPERTY of type ICal.property_kind>, 'QUERY_PROPERTY': <enum ICAL_QUERY_PROPERTY of type ICal.property_kind>, 'QUERYLEVEL_PROPERTY': <enum ICAL_QUERYLEVEL_PROPERTY of type ICal.property_kind>, 'QUERYID_PROPERTY': <enum ICAL_QUERYID_PROPERTY of type ICal.property_kind>, 'QUERYNAME_PROPERTY': <enum ICAL_QUERYNAME_PROPERTY of type ICal.property_kind>, 'RDATE_PROPERTY': <enum ICAL_RDATE_PROPERTY of type ICal.property_kind>, 'RECURACCEPTED_PROPERTY': <enum ICAL_RECURACCEPTED_PROPERTY of type ICal.property_kind>, 'RECUREXPAND_PROPERTY': <enum ICAL_RECUREXPAND_PROPERTY of type ICal.property_kind>, 'RECURLIMIT_PROPERTY': <enum ICAL_RECURLIMIT_PROPERTY of type ICal.property_kind>, 'RECURRENCEID_PROPERTY': <enum ICAL_RECURRENCEID_PROPERTY of type ICal.property_kind>, 'REFRESHINTERVAL_PROPERTY': <enum ICAL_REFRESHINTERVAL_PROPERTY of type ICal.property_kind>, 'RELATEDTO_PROPERTY': <enum ICAL_RELATEDTO_PROPERTY of type ICal.property_kind>, 'RELCALID_PROPERTY': <enum ICAL_RELCALID_PROPERTY of type ICal.property_kind>, 'REPEAT_PROPERTY': <enum ICAL_REPEAT_PROPERTY of type ICal.property_kind>, 'REPLYURL_PROPERTY': <enum ICAL_REPLYURL_PROPERTY of type ICal.property_kind>, 'REQUESTSTATUS_PROPERTY': <enum ICAL_REQUESTSTATUS_PROPERTY of type ICal.property_kind>, 'RESOURCES_PROPERTY': <enum ICAL_RESOURCES_PROPERTY of type ICal.property_kind>, 'RESPONSE_PROPERTY': <enum ICAL_RESPONSE_PROPERTY of type ICal.property_kind>, 'RESTRICTION_PROPERTY': <enum ICAL_RESTRICTION_PROPERTY of type ICal.property_kind>, 'RRULE_PROPERTY': <enum ICAL_RRULE_PROPERTY of type ICal.property_kind>, 'SCOPE_PROPERTY': <enum ICAL_SCOPE_PROPERTY of type ICal.property_kind>, 'SEQUENCE_PROPERTY': <enum ICAL_SEQUENCE_PROPERTY of type ICal.property_kind>, 'SOURCE_PROPERTY': <enum ICAL_SOURCE_PROPERTY of type ICal.property_kind>, 'STATUS_PROPERTY': <enum ICAL_STATUS_PROPERTY of type ICal.property_kind>, 'STORESEXPANDED_PROPERTY': <enum ICAL_STORESEXPANDED_PROPERTY of type ICal.property_kind>, 'SUMMARY_PROPERTY': <enum ICAL_SUMMARY_PROPERTY of type ICal.property_kind>, 'TARGET_PROPERTY': <enum ICAL_TARGET_PROPERTY of type ICal.property_kind>, 'TASKMODE_PROPERTY': <enum ICAL_TASKMODE_PROPERTY of type ICal.property_kind>, 'TRANSP_PROPERTY': <enum ICAL_TRANSP_PROPERTY of type ICal.property_kind>, 'TRIGGER_PROPERTY': <enum ICAL_TRIGGER_PROPERTY of type ICal.property_kind>, 'TZID_PROPERTY': <enum ICAL_TZID_PROPERTY of type ICal.property_kind>, 'TZIDALIASOF_PROPERTY': <enum ICAL_TZIDALIASOF_PROPERTY of type ICal.property_kind>, 'TZNAME_PROPERTY': <enum ICAL_TZNAME_PROPERTY of type ICal.property_kind>, 'TZOFFSETFROM_PROPERTY': <enum ICAL_TZOFFSETFROM_PROPERTY of type ICal.property_kind>, 'TZOFFSETTO_PROPERTY': <enum ICAL_TZOFFSETTO_PROPERTY of type ICal.property_kind>, 'TZUNTIL_PROPERTY': <enum ICAL_TZUNTIL_PROPERTY of type ICal.property_kind>, 'TZURL_PROPERTY': <enum ICAL_TZURL_PROPERTY of type ICal.property_kind>, 'UID_PROPERTY': <enum ICAL_UID_PROPERTY of type ICal.property_kind>, 'URL_PROPERTY': <enum ICAL_URL_PROPERTY of type ICal.property_kind>, 'VERSION_PROPERTY': <enum ICAL_VERSION_PROPERTY of type ICal.property_kind>, 'VOTER_PROPERTY': <enum ICAL_VOTER_PROPERTY of type ICal.property_kind>, 'X_PROPERTY': <enum ICAL_X_PROPERTY of type ICal.property_kind>, 'XLICCLASS_PROPERTY': <enum ICAL_XLICCLASS_PROPERTY of type ICal.property_kind>, 'XLICCLUSTERCOUNT_PROPERTY': <enum ICAL_XLICCLUSTERCOUNT_PROPERTY of type ICal.property_kind>, 'XLICERROR_PROPERTY': <enum ICAL_XLICERROR_PROPERTY of type ICal.property_kind>, 'XLICMIMECHARSET_PROPERTY': <enum ICAL_XLICMIMECHARSET_PROPERTY of type ICal.property_kind>, 'XLICMIMECID_PROPERTY': <enum ICAL_XLICMIMECID_PROPERTY of type ICal.property_kind>, 'XLICMIMECONTENTTYPE_PROPERTY': <enum ICAL_XLICMIMECONTENTTYPE_PROPERTY of type ICal.property_kind>, 'XLICMIMEENCODING_PROPERTY': <enum ICAL_XLICMIMEENCODING_PROPERTY of type ICal.property_kind>, 'XLICMIMEFILENAME_PROPERTY': <enum ICAL_XLICMIMEFILENAME_PROPERTY of type ICal.property_kind>, 'XLICMIMEOPTINFO_PROPERTY': <enum ICAL_XLICMIMEOPTINFO_PROPERTY of type ICal.property_kind>, 'NO_PROPERTY': <enum ICAL_NO_PROPERTY of type ICal.property_kind>})"
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
        116: 116,
        117: 117,
        118: 118,
        119: 119,
        120: 120,
        121: 121,
        122: 122,
        123: 123,
        124: 124,
        125: 125,
    }
    __gtype__ = None # (!) real value is '<GType PyICalproperty_kind (94628528780864)>'
    __info__ = gi.EnumInfo(property_kind)


