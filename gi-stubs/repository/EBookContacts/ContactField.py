# encoding: utf-8
# module gi.repository.EBookContacts
# from /usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gobject as __gobject


class ContactField(__gobject.GEnum):
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


    ADDRESS = 89
    ADDRESS_HOME = 90
    ADDRESS_LABEL_HOME = 13
    ADDRESS_LABEL_OTHER = 15
    ADDRESS_LABEL_WORK = 14
    ADDRESS_OTHER = 92
    ADDRESS_WORK = 91
    ANNIVERSARY = 108
    ASSISTANT = 41
    BIRTH_DATE = 107
    BLOG_URL = 43
    BOOK_UID = 3
    CALENDAR_URI = 45
    CATEGORIES = 44
    CATEGORY_LIST = 93
    EMAIL = 97
    EMAIL_1 = 8
    EMAIL_2 = 9
    EMAIL_3 = 10
    EMAIL_4 = 11
    FAMILY_NAME = 6
    FIELD_FIRST = 1
    FIELD_LAST = 136
    FILE_AS = 2
    FIRST_ADDRESS_ID = 90
    FIRST_EMAIL_ID = 8
    FIRST_LABEL_ID = 13
    FIRST_PHONE_ID = 16
    FREEBUSY_URL = 46
    FULL_NAME = 4
    GEO = 118
    GIVEN_NAME = 5
    HOMEPAGE_URL = 42
    ICS_CALENDAR = 47
    IM_AIM = 98
    IM_AIM_HOME_1 = 51
    IM_AIM_HOME_2 = 52
    IM_AIM_HOME_3 = 53
    IM_AIM_WORK_1 = 54
    IM_AIM_WORK_2 = 55
    IM_AIM_WORK_3 = 56
    IM_GADUGADU = 117
    IM_GADUGADU_HOME_1 = 111
    IM_GADUGADU_HOME_2 = 112
    IM_GADUGADU_HOME_3 = 113
    IM_GADUGADU_WORK_1 = 114
    IM_GADUGADU_WORK_2 = 115
    IM_GADUGADU_WORK_3 = 116
    IM_GOOGLE_TALK = 134
    IM_GOOGLE_TALK_HOME_1 = 128
    IM_GOOGLE_TALK_HOME_2 = 129
    IM_GOOGLE_TALK_HOME_3 = 130
    IM_GOOGLE_TALK_WORK_1 = 131
    IM_GOOGLE_TALK_WORK_2 = 132
    IM_GOOGLE_TALK_WORK_3 = 133
    IM_GROUPWISE = 99
    IM_GROUPWISE_HOME_1 = 57
    IM_GROUPWISE_HOME_2 = 58
    IM_GROUPWISE_HOME_3 = 59
    IM_GROUPWISE_WORK_1 = 60
    IM_GROUPWISE_WORK_2 = 61
    IM_GROUPWISE_WORK_3 = 62
    IM_ICQ = 103
    IM_ICQ_HOME_1 = 81
    IM_ICQ_HOME_2 = 82
    IM_ICQ_HOME_3 = 83
    IM_ICQ_WORK_1 = 84
    IM_ICQ_WORK_2 = 85
    IM_ICQ_WORK_3 = 86
    IM_JABBER = 100
    IM_JABBER_HOME_1 = 63
    IM_JABBER_HOME_2 = 64
    IM_JABBER_HOME_3 = 65
    IM_JABBER_WORK_1 = 66
    IM_JABBER_WORK_2 = 67
    IM_JABBER_WORK_3 = 68
    IM_MSN = 102
    IM_MSN_HOME_1 = 75
    IM_MSN_HOME_2 = 76
    IM_MSN_HOME_3 = 77
    IM_MSN_WORK_1 = 78
    IM_MSN_WORK_2 = 79
    IM_MSN_WORK_3 = 80
    IM_SKYPE = 126
    IM_SKYPE_HOME_1 = 120
    IM_SKYPE_HOME_2 = 121
    IM_SKYPE_HOME_3 = 122
    IM_SKYPE_WORK_1 = 123
    IM_SKYPE_WORK_2 = 124
    IM_SKYPE_WORK_3 = 125
    IM_TWITTER = 135
    IM_YAHOO = 101
    IM_YAHOO_HOME_1 = 69
    IM_YAHOO_HOME_2 = 70
    IM_YAHOO_HOME_3 = 71
    IM_YAHOO_WORK_1 = 72
    IM_YAHOO_WORK_2 = 73
    IM_YAHOO_WORK_3 = 74
    IS_LIST = 105
    LAST_ADDRESS_ID = 92
    LAST_EMAIL_ID = 11
    LAST_LABEL_ID = 15
    LAST_PHONE_ID = 34
    LAST_SIMPLE_STRING = 88
    LIST_SHOW_ADDRESSES = 106
    LOGO = 95
    MAILER = 12
    MANAGER = 40
    NAME = 96
    NAME_OR_ORG = 88
    NICKNAME = 7
    NOTE = 50
    OFFICE = 37
    ORG = 35
    ORG_UNIT = 36
    PGP_CERT = 110
    PHONE_ASSISTANT = 16
    PHONE_BUSINESS = 17
    PHONE_BUSINESS_2 = 18
    PHONE_BUSINESS_FAX = 19
    PHONE_CALLBACK = 20
    PHONE_CAR = 21
    PHONE_COMPANY = 22
    PHONE_HOME = 23
    PHONE_HOME_2 = 24
    PHONE_HOME_FAX = 25
    PHONE_ISDN = 26
    PHONE_MOBILE = 27
    PHONE_OTHER = 28
    PHONE_OTHER_FAX = 29
    PHONE_PAGER = 30
    PHONE_PRIMARY = 31
    PHONE_RADIO = 32
    PHONE_TELEX = 33
    PHONE_TTYTDD = 34
    PHOTO = 94
    REV = 87
    ROLE = 39
    SIP = 127
    SPOUSE = 49
    TEL = 119
    TITLE = 38
    UID = 1
    VIDEO_URL = 48
    WANTS_HTML = 104
    X509_CERT = 109
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.EBookContacts', '__dict__': <attribute '__dict__' of 'ContactField' objects>, '__doc__': None, '__gtype__': <GType PyEBookContactsContactField (94769385575280)>, '__enum_values__': {1: <enum E_CONTACT_UID of type EBookContacts.ContactField>, 2: <enum E_CONTACT_FILE_AS of type EBookContacts.ContactField>, 3: <enum E_CONTACT_BOOK_UID of type EBookContacts.ContactField>, 4: <enum E_CONTACT_FULL_NAME of type EBookContacts.ContactField>, 5: <enum E_CONTACT_GIVEN_NAME of type EBookContacts.ContactField>, 6: <enum E_CONTACT_FAMILY_NAME of type EBookContacts.ContactField>, 7: <enum E_CONTACT_NICKNAME of type EBookContacts.ContactField>, 8: <enum E_CONTACT_EMAIL_1 of type EBookContacts.ContactField>, 9: <enum E_CONTACT_EMAIL_2 of type EBookContacts.ContactField>, 10: <enum E_CONTACT_EMAIL_3 of type EBookContacts.ContactField>, 11: <enum E_CONTACT_EMAIL_4 of type EBookContacts.ContactField>, 12: <enum E_CONTACT_MAILER of type EBookContacts.ContactField>, 13: <enum E_CONTACT_ADDRESS_LABEL_HOME of type EBookContacts.ContactField>, 14: <enum E_CONTACT_ADDRESS_LABEL_WORK of type EBookContacts.ContactField>, 15: <enum E_CONTACT_ADDRESS_LABEL_OTHER of type EBookContacts.ContactField>, 16: <enum E_CONTACT_PHONE_ASSISTANT of type EBookContacts.ContactField>, 17: <enum E_CONTACT_PHONE_BUSINESS of type EBookContacts.ContactField>, 18: <enum E_CONTACT_PHONE_BUSINESS_2 of type EBookContacts.ContactField>, 19: <enum E_CONTACT_PHONE_BUSINESS_FAX of type EBookContacts.ContactField>, 20: <enum E_CONTACT_PHONE_CALLBACK of type EBookContacts.ContactField>, 21: <enum E_CONTACT_PHONE_CAR of type EBookContacts.ContactField>, 22: <enum E_CONTACT_PHONE_COMPANY of type EBookContacts.ContactField>, 23: <enum E_CONTACT_PHONE_HOME of type EBookContacts.ContactField>, 24: <enum E_CONTACT_PHONE_HOME_2 of type EBookContacts.ContactField>, 25: <enum E_CONTACT_PHONE_HOME_FAX of type EBookContacts.ContactField>, 26: <enum E_CONTACT_PHONE_ISDN of type EBookContacts.ContactField>, 27: <enum E_CONTACT_PHONE_MOBILE of type EBookContacts.ContactField>, 28: <enum E_CONTACT_PHONE_OTHER of type EBookContacts.ContactField>, 29: <enum E_CONTACT_PHONE_OTHER_FAX of type EBookContacts.ContactField>, 30: <enum E_CONTACT_PHONE_PAGER of type EBookContacts.ContactField>, 31: <enum E_CONTACT_PHONE_PRIMARY of type EBookContacts.ContactField>, 32: <enum E_CONTACT_PHONE_RADIO of type EBookContacts.ContactField>, 33: <enum E_CONTACT_PHONE_TELEX of type EBookContacts.ContactField>, 34: <enum E_CONTACT_PHONE_TTYTDD of type EBookContacts.ContactField>, 35: <enum E_CONTACT_ORG of type EBookContacts.ContactField>, 36: <enum E_CONTACT_ORG_UNIT of type EBookContacts.ContactField>, 37: <enum E_CONTACT_OFFICE of type EBookContacts.ContactField>, 38: <enum E_CONTACT_TITLE of type EBookContacts.ContactField>, 39: <enum E_CONTACT_ROLE of type EBookContacts.ContactField>, 40: <enum E_CONTACT_MANAGER of type EBookContacts.ContactField>, 41: <enum E_CONTACT_ASSISTANT of type EBookContacts.ContactField>, 42: <enum E_CONTACT_HOMEPAGE_URL of type EBookContacts.ContactField>, 43: <enum E_CONTACT_BLOG_URL of type EBookContacts.ContactField>, 44: <enum E_CONTACT_CATEGORIES of type EBookContacts.ContactField>, 45: <enum E_CONTACT_CALENDAR_URI of type EBookContacts.ContactField>, 46: <enum E_CONTACT_FREEBUSY_URL of type EBookContacts.ContactField>, 47: <enum E_CONTACT_ICS_CALENDAR of type EBookContacts.ContactField>, 48: <enum E_CONTACT_VIDEO_URL of type EBookContacts.ContactField>, 49: <enum E_CONTACT_SPOUSE of type EBookContacts.ContactField>, 50: <enum E_CONTACT_NOTE of type EBookContacts.ContactField>, 51: <enum E_CONTACT_IM_AIM_HOME_1 of type EBookContacts.ContactField>, 52: <enum E_CONTACT_IM_AIM_HOME_2 of type EBookContacts.ContactField>, 53: <enum E_CONTACT_IM_AIM_HOME_3 of type EBookContacts.ContactField>, 54: <enum E_CONTACT_IM_AIM_WORK_1 of type EBookContacts.ContactField>, 55: <enum E_CONTACT_IM_AIM_WORK_2 of type EBookContacts.ContactField>, 56: <enum E_CONTACT_IM_AIM_WORK_3 of type EBookContacts.ContactField>, 57: <enum E_CONTACT_IM_GROUPWISE_HOME_1 of type EBookContacts.ContactField>, 58: <enum E_CONTACT_IM_GROUPWISE_HOME_2 of type EBookContacts.ContactField>, 59: <enum E_CONTACT_IM_GROUPWISE_HOME_3 of type EBookContacts.ContactField>, 60: <enum E_CONTACT_IM_GROUPWISE_WORK_1 of type EBookContacts.ContactField>, 61: <enum E_CONTACT_IM_GROUPWISE_WORK_2 of type EBookContacts.ContactField>, 62: <enum E_CONTACT_IM_GROUPWISE_WORK_3 of type EBookContacts.ContactField>, 63: <enum E_CONTACT_IM_JABBER_HOME_1 of type EBookContacts.ContactField>, 64: <enum E_CONTACT_IM_JABBER_HOME_2 of type EBookContacts.ContactField>, 65: <enum E_CONTACT_IM_JABBER_HOME_3 of type EBookContacts.ContactField>, 66: <enum E_CONTACT_IM_JABBER_WORK_1 of type EBookContacts.ContactField>, 67: <enum E_CONTACT_IM_JABBER_WORK_2 of type EBookContacts.ContactField>, 68: <enum E_CONTACT_IM_JABBER_WORK_3 of type EBookContacts.ContactField>, 69: <enum E_CONTACT_IM_YAHOO_HOME_1 of type EBookContacts.ContactField>, 70: <enum E_CONTACT_IM_YAHOO_HOME_2 of type EBookContacts.ContactField>, 71: <enum E_CONTACT_IM_YAHOO_HOME_3 of type EBookContacts.ContactField>, 72: <enum E_CONTACT_IM_YAHOO_WORK_1 of type EBookContacts.ContactField>, 73: <enum E_CONTACT_IM_YAHOO_WORK_2 of type EBookContacts.ContactField>, 74: <enum E_CONTACT_IM_YAHOO_WORK_3 of type EBookContacts.ContactField>, 75: <enum E_CONTACT_IM_MSN_HOME_1 of type EBookContacts.ContactField>, 76: <enum E_CONTACT_IM_MSN_HOME_2 of type EBookContacts.ContactField>, 77: <enum E_CONTACT_IM_MSN_HOME_3 of type EBookContacts.ContactField>, 78: <enum E_CONTACT_IM_MSN_WORK_1 of type EBookContacts.ContactField>, 79: <enum E_CONTACT_IM_MSN_WORK_2 of type EBookContacts.ContactField>, 80: <enum E_CONTACT_IM_MSN_WORK_3 of type EBookContacts.ContactField>, 81: <enum E_CONTACT_IM_ICQ_HOME_1 of type EBookContacts.ContactField>, 82: <enum E_CONTACT_IM_ICQ_HOME_2 of type EBookContacts.ContactField>, 83: <enum E_CONTACT_IM_ICQ_HOME_3 of type EBookContacts.ContactField>, 84: <enum E_CONTACT_IM_ICQ_WORK_1 of type EBookContacts.ContactField>, 85: <enum E_CONTACT_IM_ICQ_WORK_2 of type EBookContacts.ContactField>, 86: <enum E_CONTACT_IM_ICQ_WORK_3 of type EBookContacts.ContactField>, 87: <enum E_CONTACT_REV of type EBookContacts.ContactField>, 88: <enum E_CONTACT_NAME_OR_ORG of type EBookContacts.ContactField>, 89: <enum E_CONTACT_ADDRESS of type EBookContacts.ContactField>, 90: <enum E_CONTACT_ADDRESS_HOME of type EBookContacts.ContactField>, 91: <enum E_CONTACT_ADDRESS_WORK of type EBookContacts.ContactField>, 92: <enum E_CONTACT_ADDRESS_OTHER of type EBookContacts.ContactField>, 93: <enum E_CONTACT_CATEGORY_LIST of type EBookContacts.ContactField>, 94: <enum E_CONTACT_PHOTO of type EBookContacts.ContactField>, 95: <enum E_CONTACT_LOGO of type EBookContacts.ContactField>, 96: <enum E_CONTACT_NAME of type EBookContacts.ContactField>, 97: <enum E_CONTACT_EMAIL of type EBookContacts.ContactField>, 98: <enum E_CONTACT_IM_AIM of type EBookContacts.ContactField>, 99: <enum E_CONTACT_IM_GROUPWISE of type EBookContacts.ContactField>, 100: <enum E_CONTACT_IM_JABBER of type EBookContacts.ContactField>, 101: <enum E_CONTACT_IM_YAHOO of type EBookContacts.ContactField>, 102: <enum E_CONTACT_IM_MSN of type EBookContacts.ContactField>, 103: <enum E_CONTACT_IM_ICQ of type EBookContacts.ContactField>, 104: <enum E_CONTACT_WANTS_HTML of type EBookContacts.ContactField>, 105: <enum E_CONTACT_IS_LIST of type EBookContacts.ContactField>, 106: <enum E_CONTACT_LIST_SHOW_ADDRESSES of type EBookContacts.ContactField>, 107: <enum E_CONTACT_BIRTH_DATE of type EBookContacts.ContactField>, 108: <enum E_CONTACT_ANNIVERSARY of type EBookContacts.ContactField>, 109: <enum E_CONTACT_X509_CERT of type EBookContacts.ContactField>, 110: <enum E_CONTACT_PGP_CERT of type EBookContacts.ContactField>, 111: <enum E_CONTACT_IM_GADUGADU_HOME_1 of type EBookContacts.ContactField>, 112: <enum E_CONTACT_IM_GADUGADU_HOME_2 of type EBookContacts.ContactField>, 113: <enum E_CONTACT_IM_GADUGADU_HOME_3 of type EBookContacts.ContactField>, 114: <enum E_CONTACT_IM_GADUGADU_WORK_1 of type EBookContacts.ContactField>, 115: <enum E_CONTACT_IM_GADUGADU_WORK_2 of type EBookContacts.ContactField>, 116: <enum E_CONTACT_IM_GADUGADU_WORK_3 of type EBookContacts.ContactField>, 117: <enum E_CONTACT_IM_GADUGADU of type EBookContacts.ContactField>, 118: <enum E_CONTACT_GEO of type EBookContacts.ContactField>, 119: <enum E_CONTACT_TEL of type EBookContacts.ContactField>, 120: <enum E_CONTACT_IM_SKYPE_HOME_1 of type EBookContacts.ContactField>, 121: <enum E_CONTACT_IM_SKYPE_HOME_2 of type EBookContacts.ContactField>, 122: <enum E_CONTACT_IM_SKYPE_HOME_3 of type EBookContacts.ContactField>, 123: <enum E_CONTACT_IM_SKYPE_WORK_1 of type EBookContacts.ContactField>, 124: <enum E_CONTACT_IM_SKYPE_WORK_2 of type EBookContacts.ContactField>, 125: <enum E_CONTACT_IM_SKYPE_WORK_3 of type EBookContacts.ContactField>, 126: <enum E_CONTACT_IM_SKYPE of type EBookContacts.ContactField>, 127: <enum E_CONTACT_SIP of type EBookContacts.ContactField>, 128: <enum E_CONTACT_IM_GOOGLE_TALK_HOME_1 of type EBookContacts.ContactField>, 129: <enum E_CONTACT_IM_GOOGLE_TALK_HOME_2 of type EBookContacts.ContactField>, 130: <enum E_CONTACT_IM_GOOGLE_TALK_HOME_3 of type EBookContacts.ContactField>, 131: <enum E_CONTACT_IM_GOOGLE_TALK_WORK_1 of type EBookContacts.ContactField>, 132: <enum E_CONTACT_IM_GOOGLE_TALK_WORK_2 of type EBookContacts.ContactField>, 133: <enum E_CONTACT_IM_GOOGLE_TALK_WORK_3 of type EBookContacts.ContactField>, 134: <enum E_CONTACT_IM_GOOGLE_TALK of type EBookContacts.ContactField>, 135: <enum E_CONTACT_IM_TWITTER of type EBookContacts.ContactField>, 136: <enum E_CONTACT_FIELD_LAST of type EBookContacts.ContactField>}, '__info__': gi.EnumInfo(ContactField), 'UID': <enum E_CONTACT_UID of type EBookContacts.ContactField>, 'FILE_AS': <enum E_CONTACT_FILE_AS of type EBookContacts.ContactField>, 'BOOK_UID': <enum E_CONTACT_BOOK_UID of type EBookContacts.ContactField>, 'FULL_NAME': <enum E_CONTACT_FULL_NAME of type EBookContacts.ContactField>, 'GIVEN_NAME': <enum E_CONTACT_GIVEN_NAME of type EBookContacts.ContactField>, 'FAMILY_NAME': <enum E_CONTACT_FAMILY_NAME of type EBookContacts.ContactField>, 'NICKNAME': <enum E_CONTACT_NICKNAME of type EBookContacts.ContactField>, 'EMAIL_1': <enum E_CONTACT_EMAIL_1 of type EBookContacts.ContactField>, 'EMAIL_2': <enum E_CONTACT_EMAIL_2 of type EBookContacts.ContactField>, 'EMAIL_3': <enum E_CONTACT_EMAIL_3 of type EBookContacts.ContactField>, 'EMAIL_4': <enum E_CONTACT_EMAIL_4 of type EBookContacts.ContactField>, 'MAILER': <enum E_CONTACT_MAILER of type EBookContacts.ContactField>, 'ADDRESS_LABEL_HOME': <enum E_CONTACT_ADDRESS_LABEL_HOME of type EBookContacts.ContactField>, 'ADDRESS_LABEL_WORK': <enum E_CONTACT_ADDRESS_LABEL_WORK of type EBookContacts.ContactField>, 'ADDRESS_LABEL_OTHER': <enum E_CONTACT_ADDRESS_LABEL_OTHER of type EBookContacts.ContactField>, 'PHONE_ASSISTANT': <enum E_CONTACT_PHONE_ASSISTANT of type EBookContacts.ContactField>, 'PHONE_BUSINESS': <enum E_CONTACT_PHONE_BUSINESS of type EBookContacts.ContactField>, 'PHONE_BUSINESS_2': <enum E_CONTACT_PHONE_BUSINESS_2 of type EBookContacts.ContactField>, 'PHONE_BUSINESS_FAX': <enum E_CONTACT_PHONE_BUSINESS_FAX of type EBookContacts.ContactField>, 'PHONE_CALLBACK': <enum E_CONTACT_PHONE_CALLBACK of type EBookContacts.ContactField>, 'PHONE_CAR': <enum E_CONTACT_PHONE_CAR of type EBookContacts.ContactField>, 'PHONE_COMPANY': <enum E_CONTACT_PHONE_COMPANY of type EBookContacts.ContactField>, 'PHONE_HOME': <enum E_CONTACT_PHONE_HOME of type EBookContacts.ContactField>, 'PHONE_HOME_2': <enum E_CONTACT_PHONE_HOME_2 of type EBookContacts.ContactField>, 'PHONE_HOME_FAX': <enum E_CONTACT_PHONE_HOME_FAX of type EBookContacts.ContactField>, 'PHONE_ISDN': <enum E_CONTACT_PHONE_ISDN of type EBookContacts.ContactField>, 'PHONE_MOBILE': <enum E_CONTACT_PHONE_MOBILE of type EBookContacts.ContactField>, 'PHONE_OTHER': <enum E_CONTACT_PHONE_OTHER of type EBookContacts.ContactField>, 'PHONE_OTHER_FAX': <enum E_CONTACT_PHONE_OTHER_FAX of type EBookContacts.ContactField>, 'PHONE_PAGER': <enum E_CONTACT_PHONE_PAGER of type EBookContacts.ContactField>, 'PHONE_PRIMARY': <enum E_CONTACT_PHONE_PRIMARY of type EBookContacts.ContactField>, 'PHONE_RADIO': <enum E_CONTACT_PHONE_RADIO of type EBookContacts.ContactField>, 'PHONE_TELEX': <enum E_CONTACT_PHONE_TELEX of type EBookContacts.ContactField>, 'PHONE_TTYTDD': <enum E_CONTACT_PHONE_TTYTDD of type EBookContacts.ContactField>, 'ORG': <enum E_CONTACT_ORG of type EBookContacts.ContactField>, 'ORG_UNIT': <enum E_CONTACT_ORG_UNIT of type EBookContacts.ContactField>, 'OFFICE': <enum E_CONTACT_OFFICE of type EBookContacts.ContactField>, 'TITLE': <enum E_CONTACT_TITLE of type EBookContacts.ContactField>, 'ROLE': <enum E_CONTACT_ROLE of type EBookContacts.ContactField>, 'MANAGER': <enum E_CONTACT_MANAGER of type EBookContacts.ContactField>, 'ASSISTANT': <enum E_CONTACT_ASSISTANT of type EBookContacts.ContactField>, 'HOMEPAGE_URL': <enum E_CONTACT_HOMEPAGE_URL of type EBookContacts.ContactField>, 'BLOG_URL': <enum E_CONTACT_BLOG_URL of type EBookContacts.ContactField>, 'CATEGORIES': <enum E_CONTACT_CATEGORIES of type EBookContacts.ContactField>, 'CALENDAR_URI': <enum E_CONTACT_CALENDAR_URI of type EBookContacts.ContactField>, 'FREEBUSY_URL': <enum E_CONTACT_FREEBUSY_URL of type EBookContacts.ContactField>, 'ICS_CALENDAR': <enum E_CONTACT_ICS_CALENDAR of type EBookContacts.ContactField>, 'VIDEO_URL': <enum E_CONTACT_VIDEO_URL of type EBookContacts.ContactField>, 'SPOUSE': <enum E_CONTACT_SPOUSE of type EBookContacts.ContactField>, 'NOTE': <enum E_CONTACT_NOTE of type EBookContacts.ContactField>, 'IM_AIM_HOME_1': <enum E_CONTACT_IM_AIM_HOME_1 of type EBookContacts.ContactField>, 'IM_AIM_HOME_2': <enum E_CONTACT_IM_AIM_HOME_2 of type EBookContacts.ContactField>, 'IM_AIM_HOME_3': <enum E_CONTACT_IM_AIM_HOME_3 of type EBookContacts.ContactField>, 'IM_AIM_WORK_1': <enum E_CONTACT_IM_AIM_WORK_1 of type EBookContacts.ContactField>, 'IM_AIM_WORK_2': <enum E_CONTACT_IM_AIM_WORK_2 of type EBookContacts.ContactField>, 'IM_AIM_WORK_3': <enum E_CONTACT_IM_AIM_WORK_3 of type EBookContacts.ContactField>, 'IM_GROUPWISE_HOME_1': <enum E_CONTACT_IM_GROUPWISE_HOME_1 of type EBookContacts.ContactField>, 'IM_GROUPWISE_HOME_2': <enum E_CONTACT_IM_GROUPWISE_HOME_2 of type EBookContacts.ContactField>, 'IM_GROUPWISE_HOME_3': <enum E_CONTACT_IM_GROUPWISE_HOME_3 of type EBookContacts.ContactField>, 'IM_GROUPWISE_WORK_1': <enum E_CONTACT_IM_GROUPWISE_WORK_1 of type EBookContacts.ContactField>, 'IM_GROUPWISE_WORK_2': <enum E_CONTACT_IM_GROUPWISE_WORK_2 of type EBookContacts.ContactField>, 'IM_GROUPWISE_WORK_3': <enum E_CONTACT_IM_GROUPWISE_WORK_3 of type EBookContacts.ContactField>, 'IM_JABBER_HOME_1': <enum E_CONTACT_IM_JABBER_HOME_1 of type EBookContacts.ContactField>, 'IM_JABBER_HOME_2': <enum E_CONTACT_IM_JABBER_HOME_2 of type EBookContacts.ContactField>, 'IM_JABBER_HOME_3': <enum E_CONTACT_IM_JABBER_HOME_3 of type EBookContacts.ContactField>, 'IM_JABBER_WORK_1': <enum E_CONTACT_IM_JABBER_WORK_1 of type EBookContacts.ContactField>, 'IM_JABBER_WORK_2': <enum E_CONTACT_IM_JABBER_WORK_2 of type EBookContacts.ContactField>, 'IM_JABBER_WORK_3': <enum E_CONTACT_IM_JABBER_WORK_3 of type EBookContacts.ContactField>, 'IM_YAHOO_HOME_1': <enum E_CONTACT_IM_YAHOO_HOME_1 of type EBookContacts.ContactField>, 'IM_YAHOO_HOME_2': <enum E_CONTACT_IM_YAHOO_HOME_2 of type EBookContacts.ContactField>, 'IM_YAHOO_HOME_3': <enum E_CONTACT_IM_YAHOO_HOME_3 of type EBookContacts.ContactField>, 'IM_YAHOO_WORK_1': <enum E_CONTACT_IM_YAHOO_WORK_1 of type EBookContacts.ContactField>, 'IM_YAHOO_WORK_2': <enum E_CONTACT_IM_YAHOO_WORK_2 of type EBookContacts.ContactField>, 'IM_YAHOO_WORK_3': <enum E_CONTACT_IM_YAHOO_WORK_3 of type EBookContacts.ContactField>, 'IM_MSN_HOME_1': <enum E_CONTACT_IM_MSN_HOME_1 of type EBookContacts.ContactField>, 'IM_MSN_HOME_2': <enum E_CONTACT_IM_MSN_HOME_2 of type EBookContacts.ContactField>, 'IM_MSN_HOME_3': <enum E_CONTACT_IM_MSN_HOME_3 of type EBookContacts.ContactField>, 'IM_MSN_WORK_1': <enum E_CONTACT_IM_MSN_WORK_1 of type EBookContacts.ContactField>, 'IM_MSN_WORK_2': <enum E_CONTACT_IM_MSN_WORK_2 of type EBookContacts.ContactField>, 'IM_MSN_WORK_3': <enum E_CONTACT_IM_MSN_WORK_3 of type EBookContacts.ContactField>, 'IM_ICQ_HOME_1': <enum E_CONTACT_IM_ICQ_HOME_1 of type EBookContacts.ContactField>, 'IM_ICQ_HOME_2': <enum E_CONTACT_IM_ICQ_HOME_2 of type EBookContacts.ContactField>, 'IM_ICQ_HOME_3': <enum E_CONTACT_IM_ICQ_HOME_3 of type EBookContacts.ContactField>, 'IM_ICQ_WORK_1': <enum E_CONTACT_IM_ICQ_WORK_1 of type EBookContacts.ContactField>, 'IM_ICQ_WORK_2': <enum E_CONTACT_IM_ICQ_WORK_2 of type EBookContacts.ContactField>, 'IM_ICQ_WORK_3': <enum E_CONTACT_IM_ICQ_WORK_3 of type EBookContacts.ContactField>, 'REV': <enum E_CONTACT_REV of type EBookContacts.ContactField>, 'NAME_OR_ORG': <enum E_CONTACT_NAME_OR_ORG of type EBookContacts.ContactField>, 'ADDRESS': <enum E_CONTACT_ADDRESS of type EBookContacts.ContactField>, 'ADDRESS_HOME': <enum E_CONTACT_ADDRESS_HOME of type EBookContacts.ContactField>, 'ADDRESS_WORK': <enum E_CONTACT_ADDRESS_WORK of type EBookContacts.ContactField>, 'ADDRESS_OTHER': <enum E_CONTACT_ADDRESS_OTHER of type EBookContacts.ContactField>, 'CATEGORY_LIST': <enum E_CONTACT_CATEGORY_LIST of type EBookContacts.ContactField>, 'PHOTO': <enum E_CONTACT_PHOTO of type EBookContacts.ContactField>, 'LOGO': <enum E_CONTACT_LOGO of type EBookContacts.ContactField>, 'NAME': <enum E_CONTACT_NAME of type EBookContacts.ContactField>, 'EMAIL': <enum E_CONTACT_EMAIL of type EBookContacts.ContactField>, 'IM_AIM': <enum E_CONTACT_IM_AIM of type EBookContacts.ContactField>, 'IM_GROUPWISE': <enum E_CONTACT_IM_GROUPWISE of type EBookContacts.ContactField>, 'IM_JABBER': <enum E_CONTACT_IM_JABBER of type EBookContacts.ContactField>, 'IM_YAHOO': <enum E_CONTACT_IM_YAHOO of type EBookContacts.ContactField>, 'IM_MSN': <enum E_CONTACT_IM_MSN of type EBookContacts.ContactField>, 'IM_ICQ': <enum E_CONTACT_IM_ICQ of type EBookContacts.ContactField>, 'WANTS_HTML': <enum E_CONTACT_WANTS_HTML of type EBookContacts.ContactField>, 'IS_LIST': <enum E_CONTACT_IS_LIST of type EBookContacts.ContactField>, 'LIST_SHOW_ADDRESSES': <enum E_CONTACT_LIST_SHOW_ADDRESSES of type EBookContacts.ContactField>, 'BIRTH_DATE': <enum E_CONTACT_BIRTH_DATE of type EBookContacts.ContactField>, 'ANNIVERSARY': <enum E_CONTACT_ANNIVERSARY of type EBookContacts.ContactField>, 'X509_CERT': <enum E_CONTACT_X509_CERT of type EBookContacts.ContactField>, 'PGP_CERT': <enum E_CONTACT_PGP_CERT of type EBookContacts.ContactField>, 'IM_GADUGADU_HOME_1': <enum E_CONTACT_IM_GADUGADU_HOME_1 of type EBookContacts.ContactField>, 'IM_GADUGADU_HOME_2': <enum E_CONTACT_IM_GADUGADU_HOME_2 of type EBookContacts.ContactField>, 'IM_GADUGADU_HOME_3': <enum E_CONTACT_IM_GADUGADU_HOME_3 of type EBookContacts.ContactField>, 'IM_GADUGADU_WORK_1': <enum E_CONTACT_IM_GADUGADU_WORK_1 of type EBookContacts.ContactField>, 'IM_GADUGADU_WORK_2': <enum E_CONTACT_IM_GADUGADU_WORK_2 of type EBookContacts.ContactField>, 'IM_GADUGADU_WORK_3': <enum E_CONTACT_IM_GADUGADU_WORK_3 of type EBookContacts.ContactField>, 'IM_GADUGADU': <enum E_CONTACT_IM_GADUGADU of type EBookContacts.ContactField>, 'GEO': <enum E_CONTACT_GEO of type EBookContacts.ContactField>, 'TEL': <enum E_CONTACT_TEL of type EBookContacts.ContactField>, 'IM_SKYPE_HOME_1': <enum E_CONTACT_IM_SKYPE_HOME_1 of type EBookContacts.ContactField>, 'IM_SKYPE_HOME_2': <enum E_CONTACT_IM_SKYPE_HOME_2 of type EBookContacts.ContactField>, 'IM_SKYPE_HOME_3': <enum E_CONTACT_IM_SKYPE_HOME_3 of type EBookContacts.ContactField>, 'IM_SKYPE_WORK_1': <enum E_CONTACT_IM_SKYPE_WORK_1 of type EBookContacts.ContactField>, 'IM_SKYPE_WORK_2': <enum E_CONTACT_IM_SKYPE_WORK_2 of type EBookContacts.ContactField>, 'IM_SKYPE_WORK_3': <enum E_CONTACT_IM_SKYPE_WORK_3 of type EBookContacts.ContactField>, 'IM_SKYPE': <enum E_CONTACT_IM_SKYPE of type EBookContacts.ContactField>, 'SIP': <enum E_CONTACT_SIP of type EBookContacts.ContactField>, 'IM_GOOGLE_TALK_HOME_1': <enum E_CONTACT_IM_GOOGLE_TALK_HOME_1 of type EBookContacts.ContactField>, 'IM_GOOGLE_TALK_HOME_2': <enum E_CONTACT_IM_GOOGLE_TALK_HOME_2 of type EBookContacts.ContactField>, 'IM_GOOGLE_TALK_HOME_3': <enum E_CONTACT_IM_GOOGLE_TALK_HOME_3 of type EBookContacts.ContactField>, 'IM_GOOGLE_TALK_WORK_1': <enum E_CONTACT_IM_GOOGLE_TALK_WORK_1 of type EBookContacts.ContactField>, 'IM_GOOGLE_TALK_WORK_2': <enum E_CONTACT_IM_GOOGLE_TALK_WORK_2 of type EBookContacts.ContactField>, 'IM_GOOGLE_TALK_WORK_3': <enum E_CONTACT_IM_GOOGLE_TALK_WORK_3 of type EBookContacts.ContactField>, 'IM_GOOGLE_TALK': <enum E_CONTACT_IM_GOOGLE_TALK of type EBookContacts.ContactField>, 'IM_TWITTER': <enum E_CONTACT_IM_TWITTER of type EBookContacts.ContactField>, 'FIELD_LAST': <enum E_CONTACT_FIELD_LAST of type EBookContacts.ContactField>, 'FIELD_FIRST': <enum E_CONTACT_UID of type EBookContacts.ContactField>, 'LAST_SIMPLE_STRING': <enum E_CONTACT_NAME_OR_ORG of type EBookContacts.ContactField>, 'FIRST_PHONE_ID': <enum E_CONTACT_PHONE_ASSISTANT of type EBookContacts.ContactField>, 'LAST_PHONE_ID': <enum E_CONTACT_PHONE_TTYTDD of type EBookContacts.ContactField>, 'FIRST_EMAIL_ID': <enum E_CONTACT_EMAIL_1 of type EBookContacts.ContactField>, 'LAST_EMAIL_ID': <enum E_CONTACT_EMAIL_4 of type EBookContacts.ContactField>, 'FIRST_ADDRESS_ID': <enum E_CONTACT_ADDRESS_HOME of type EBookContacts.ContactField>, 'LAST_ADDRESS_ID': <enum E_CONTACT_ADDRESS_OTHER of type EBookContacts.ContactField>, 'FIRST_LABEL_ID': <enum E_CONTACT_ADDRESS_LABEL_HOME of type EBookContacts.ContactField>, 'LAST_LABEL_ID': <enum E_CONTACT_ADDRESS_LABEL_OTHER of type EBookContacts.ContactField>})"
    __enum_values__ = {
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
        126: 126,
        127: 127,
        128: 128,
        129: 129,
        130: 130,
        131: 131,
        132: 132,
        133: 133,
        134: 134,
        135: 135,
        136: 136,
    }
    __gtype__ = None # (!) real value is '<GType PyEBookContactsContactField (94769385575280)>'
    __info__ = gi.EnumInfo(ContactField)


