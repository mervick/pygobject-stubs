# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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


class MobileEquipmentError(__gobject.GEnum):
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


    CORPPIN = 46
    CORPPUK = 47
    DIALSTRINGINVALID = 27
    DIALSTRINGTOOLONG = 26
    EAPMETHODNOTSUPPORTED = 49
    GPRSACTIVATIONREJECTEDBYGGSNORGW = 130
    GPRSACTIVATIONREJECTEDUNSPECIFIED = 131
    GPRSANDNONGPRSSERVICESNOTALLOWED = 108
    GPRSCONDITIONALIEERROR = 175
    GPRSCONGESTION = 122
    GPRSFEATURENOTSUPPORTED = 140
    GPRSIENOTIMPLEMENTED = 174
    GPRSILLEGALME = 106
    GPRSILLEGALMS = 103
    GPRSIMSIUNKNOWNINHLR = 102
    GPRSIMSIUNKNOWNINVLR = 104
    GPRSINSUFFICIENTRESOURCES = 126
    GPRSINVALIDMOBILECLASS = 150
    GPRSLASTPDNDISCONNECTIONNOTALLOWED = 171
    GPRSLASTPDNDISCONNECTIONNOTALLOWEDLEGACY = 151
    GPRSLOCATIONNOTALLOWED = 112
    GPRSMANDATORYIEERROR = 173
    GPRSMAXIMUMNUMBEROFPDPCONTEXTSREACHED = 178
    GPRSMISSINGORUNKNOWNAPN = 127
    GPRSNETWORKFAILURE = 117
    GPRSNOCELLSINLOCATIONAREA = 115
    GPRSOPERATORDETERMINEDBARRING = 177
    GPRSPDPAUTHFAILURE = 149
    GPRSPDPCONTEXTWITHOUTTFTALREADYACTIVATED = 146
    GPRSPLMNNOTALLOWED = 111
    GPRSREQUESTEDAPNNOTSUPPORTED = 179
    GPRSREQUESTREJECTEDBCMVIOLATION = 180
    GPRSROMAINGNOTALLOWED = 113
    GPRSSEMANTICALLYINCORRECTMESSAGE = 172
    GPRSSEMANTICERRORINTFTOPERATION = 141
    GPRSSEMANTICERRORSINPACKETFILTER = 144
    GPRSSERVICENOTALLOWED = 107
    GPRSSERVICEOPTIONNOTSUBSCRIBED = 133
    GPRSSERVICEOPTIONNOTSUPPORTED = 132
    GPRSSERVICEOPTIONOUTOFORDER = 134
    GPRSSYNTACTICALERRORINTFTOPERATION = 142
    GPRSSYNTACTICALERRORSINPACKETFILTER = 145
    GPRSUNKNOWN = 148
    GPRSUNKNOWNPDPADDRESSORTYPE = 128
    GPRSUNKNOWNPDPCONTEXT = 143
    GPRSUNSPECIFIEDPROTOCOLERROR = 176
    GPRSUSERAUTHENTICATIONFAILED = 129
    HIDDENKEYREQUIRED = 48
    INCORRECTPARAMETERS = 50
    INCORRECTPASSWORD = 16
    INVALIDCHARS = 25
    INVALIDINDEX = 21
    LINKRESERVED = 2
    MEMORYFAILURE = 23
    MEMORYFULL = 20
    NETWORKNOTALLOWED = 32
    NETWORKPIN = 40
    NETWORKPUK = 41
    NETWORKSUBSETPIN = 42
    NETWORKSUBSETPUK = 43
    NETWORKTIMEOUT = 31
    NOCONNECTION = 1
    NONETWORK = 30
    NOTALLOWED = 3
    NOTAUTHORIZEDFORCSG = 125
    NOTFOUND = 22
    NOTSUPPORTED = 4
    PHFSIMPIN = 6
    PHFSIMPUK = 7
    PHONEFAILURE = 0
    PHSIMPIN = 5
    SERVICEPIN = 44
    SERVICEPUK = 45
    SIMBUSY = 14
    SIMFAILURE = 13
    SIMNOTINSERTED = 10
    SIMPIN = 11
    SIMPIN2 = 17
    SIMPUK = 12
    SIMPUK2 = 18
    SIMWRONG = 15
    TEXTTOOLONG = 24
    UNKNOWN = 100
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ModemManager', '__dict__': <attribute '__dict__' of 'MobileEquipmentError' objects>, '__doc__': None, '__gtype__': <GType MMMobileEquipmentError (94631948615504)>, '__enum_values__': {0: <enum MM_MOBILE_EQUIPMENT_ERROR_PHONE_FAILURE of type ModemManager.MobileEquipmentError>, 1: <enum MM_MOBILE_EQUIPMENT_ERROR_NO_CONNECTION of type ModemManager.MobileEquipmentError>, 2: <enum MM_MOBILE_EQUIPMENT_ERROR_LINK_RESERVED of type ModemManager.MobileEquipmentError>, 3: <enum MM_MOBILE_EQUIPMENT_ERROR_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 4: <enum MM_MOBILE_EQUIPMENT_ERROR_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 5: <enum MM_MOBILE_EQUIPMENT_ERROR_PH_SIM_PIN of type ModemManager.MobileEquipmentError>, 6: <enum MM_MOBILE_EQUIPMENT_ERROR_PH_FSIM_PIN of type ModemManager.MobileEquipmentError>, 7: <enum MM_MOBILE_EQUIPMENT_ERROR_PH_FSIM_PUK of type ModemManager.MobileEquipmentError>, 10: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_NOT_INSERTED of type ModemManager.MobileEquipmentError>, 11: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PIN of type ModemManager.MobileEquipmentError>, 12: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PUK of type ModemManager.MobileEquipmentError>, 13: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_FAILURE of type ModemManager.MobileEquipmentError>, 14: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_BUSY of type ModemManager.MobileEquipmentError>, 15: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_WRONG of type ModemManager.MobileEquipmentError>, 16: <enum MM_MOBILE_EQUIPMENT_ERROR_INCORRECT_PASSWORD of type ModemManager.MobileEquipmentError>, 17: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PIN2 of type ModemManager.MobileEquipmentError>, 18: <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PUK2 of type ModemManager.MobileEquipmentError>, 20: <enum MM_MOBILE_EQUIPMENT_ERROR_MEMORY_FULL of type ModemManager.MobileEquipmentError>, 21: <enum MM_MOBILE_EQUIPMENT_ERROR_INVALID_INDEX of type ModemManager.MobileEquipmentError>, 22: <enum MM_MOBILE_EQUIPMENT_ERROR_NOT_FOUND of type ModemManager.MobileEquipmentError>, 23: <enum MM_MOBILE_EQUIPMENT_ERROR_MEMORY_FAILURE of type ModemManager.MobileEquipmentError>, 24: <enum MM_MOBILE_EQUIPMENT_ERROR_TEXT_TOO_LONG of type ModemManager.MobileEquipmentError>, 25: <enum MM_MOBILE_EQUIPMENT_ERROR_INVALID_CHARS of type ModemManager.MobileEquipmentError>, 26: <enum MM_MOBILE_EQUIPMENT_ERROR_DIAL_STRING_TOO_LONG of type ModemManager.MobileEquipmentError>, 27: <enum MM_MOBILE_EQUIPMENT_ERROR_DIAL_STRING_INVALID of type ModemManager.MobileEquipmentError>, 30: <enum MM_MOBILE_EQUIPMENT_ERROR_NO_NETWORK of type ModemManager.MobileEquipmentError>, 31: <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_TIMEOUT of type ModemManager.MobileEquipmentError>, 32: <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 40: <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_PIN of type ModemManager.MobileEquipmentError>, 41: <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_PUK of type ModemManager.MobileEquipmentError>, 42: <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_SUBSET_PIN of type ModemManager.MobileEquipmentError>, 43: <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_SUBSET_PUK of type ModemManager.MobileEquipmentError>, 44: <enum MM_MOBILE_EQUIPMENT_ERROR_SERVICE_PIN of type ModemManager.MobileEquipmentError>, 45: <enum MM_MOBILE_EQUIPMENT_ERROR_SERVICE_PUK of type ModemManager.MobileEquipmentError>, 46: <enum MM_MOBILE_EQUIPMENT_ERROR_CORP_PIN of type ModemManager.MobileEquipmentError>, 47: <enum MM_MOBILE_EQUIPMENT_ERROR_CORP_PUK of type ModemManager.MobileEquipmentError>, 48: <enum MM_MOBILE_EQUIPMENT_ERROR_HIDDEN_KEY_REQUIRED of type ModemManager.MobileEquipmentError>, 49: <enum MM_MOBILE_EQUIPMENT_ERROR_EAP_METHOD_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 50: <enum MM_MOBILE_EQUIPMENT_ERROR_INCORRECT_PARAMETERS of type ModemManager.MobileEquipmentError>, 100: <enum MM_MOBILE_EQUIPMENT_ERROR_UNKNOWN of type ModemManager.MobileEquipmentError>, 102: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_IMSI_UNKNOWN_IN_HLR of type ModemManager.MobileEquipmentError>, 103: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ILLEGAL_MS of type ModemManager.MobileEquipmentError>, 104: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_IMSI_UNKNOWN_IN_VLR of type ModemManager.MobileEquipmentError>, 106: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ILLEGAL_ME of type ModemManager.MobileEquipmentError>, 107: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 108: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_AND_NON_GPRS_SERVICES_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 111: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_PLMN_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 112: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_LOCATION_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 113: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ROAMING_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 115: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_NO_CELLS_IN_LOCATION_AREA of type ModemManager.MobileEquipmentError>, 117: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_NETWORK_FAILURE of type ModemManager.MobileEquipmentError>, 122: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_CONGESTION of type ModemManager.MobileEquipmentError>, 125: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_NOT_AUTHORIZED_FOR_CSG of type ModemManager.MobileEquipmentError>, 126: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_INSUFFICIENT_RESOURCES of type ModemManager.MobileEquipmentError>, 127: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_MISSING_OR_UNKNOWN_APN of type ModemManager.MobileEquipmentError>, 128: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNKNOWN_PDP_ADDRESS_OR_TYPE of type ModemManager.MobileEquipmentError>, 129: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_USER_AUTHENTICATION_FAILED of type ModemManager.MobileEquipmentError>, 130: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ACTIVATION_REJECTED_BY_GGSN_OR_GW of type ModemManager.MobileEquipmentError>, 131: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ACTIVATION_REJECTED_UNSPECIFIED of type ModemManager.MobileEquipmentError>, 132: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 133: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_NOT_SUBSCRIBED of type ModemManager.MobileEquipmentError>, 134: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_OUT_OF_ORDER of type ModemManager.MobileEquipmentError>, 140: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_FEATURE_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 141: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SEMANTIC_ERROR_IN_TFT_OPERATION of type ModemManager.MobileEquipmentError>, 142: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SYNTACTICAL_ERROR_IN_TFT_OPERATION of type ModemManager.MobileEquipmentError>, 143: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNKNOWN_PDP_CONTEXT of type ModemManager.MobileEquipmentError>, 144: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SEMANTIC_ERRORS_IN_PACKET_FILTER of type ModemManager.MobileEquipmentError>, 145: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SYNTACTICAL_ERROR_IN_PACKET_FILTER of type ModemManager.MobileEquipmentError>, 146: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_PDP_CONTEXT_WITHOUT_TFT_ALREADY_ACTIVATED of type ModemManager.MobileEquipmentError>, 148: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNKNOWN of type ModemManager.MobileEquipmentError>, 149: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_PDP_AUTH_FAILURE of type ModemManager.MobileEquipmentError>, 150: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_INVALID_MOBILE_CLASS of type ModemManager.MobileEquipmentError>, 151: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_LAST_PDN_DISCONNECTION_NOT_ALLOWED_LEGACY of type ModemManager.MobileEquipmentError>, 171: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_LAST_PDN_DISCONNECTION_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 172: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SEMANTICALLY_INCORRECT_MESSAGE of type ModemManager.MobileEquipmentError>, 173: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_MANDATORY_IE_ERROR of type ModemManager.MobileEquipmentError>, 174: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_IE_NOT_IMPLEMENTED of type ModemManager.MobileEquipmentError>, 175: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_CONDITIONAL_IE_ERROR of type ModemManager.MobileEquipmentError>, 176: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNSPECIFIED_PROTOCOL_ERROR of type ModemManager.MobileEquipmentError>, 177: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_OPERATOR_DETERMINED_BARRING of type ModemManager.MobileEquipmentError>, 178: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_MAXIMUM_NUMBER_OF_PDP_CONTEXTS_REACHED of type ModemManager.MobileEquipmentError>, 179: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_REQUESTED_APN_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 180: <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_REQUEST_REJECTED_BCM_VIOLATION of type ModemManager.MobileEquipmentError>}, '__info__': gi.EnumInfo(MobileEquipmentError), 'PHONEFAILURE': <enum MM_MOBILE_EQUIPMENT_ERROR_PHONE_FAILURE of type ModemManager.MobileEquipmentError>, 'NOCONNECTION': <enum MM_MOBILE_EQUIPMENT_ERROR_NO_CONNECTION of type ModemManager.MobileEquipmentError>, 'LINKRESERVED': <enum MM_MOBILE_EQUIPMENT_ERROR_LINK_RESERVED of type ModemManager.MobileEquipmentError>, 'NOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'NOTSUPPORTED': <enum MM_MOBILE_EQUIPMENT_ERROR_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 'PHSIMPIN': <enum MM_MOBILE_EQUIPMENT_ERROR_PH_SIM_PIN of type ModemManager.MobileEquipmentError>, 'PHFSIMPIN': <enum MM_MOBILE_EQUIPMENT_ERROR_PH_FSIM_PIN of type ModemManager.MobileEquipmentError>, 'PHFSIMPUK': <enum MM_MOBILE_EQUIPMENT_ERROR_PH_FSIM_PUK of type ModemManager.MobileEquipmentError>, 'SIMNOTINSERTED': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_NOT_INSERTED of type ModemManager.MobileEquipmentError>, 'SIMPIN': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PIN of type ModemManager.MobileEquipmentError>, 'SIMPUK': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PUK of type ModemManager.MobileEquipmentError>, 'SIMFAILURE': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_FAILURE of type ModemManager.MobileEquipmentError>, 'SIMBUSY': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_BUSY of type ModemManager.MobileEquipmentError>, 'SIMWRONG': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_WRONG of type ModemManager.MobileEquipmentError>, 'INCORRECTPASSWORD': <enum MM_MOBILE_EQUIPMENT_ERROR_INCORRECT_PASSWORD of type ModemManager.MobileEquipmentError>, 'SIMPIN2': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PIN2 of type ModemManager.MobileEquipmentError>, 'SIMPUK2': <enum MM_MOBILE_EQUIPMENT_ERROR_SIM_PUK2 of type ModemManager.MobileEquipmentError>, 'MEMORYFULL': <enum MM_MOBILE_EQUIPMENT_ERROR_MEMORY_FULL of type ModemManager.MobileEquipmentError>, 'INVALIDINDEX': <enum MM_MOBILE_EQUIPMENT_ERROR_INVALID_INDEX of type ModemManager.MobileEquipmentError>, 'NOTFOUND': <enum MM_MOBILE_EQUIPMENT_ERROR_NOT_FOUND of type ModemManager.MobileEquipmentError>, 'MEMORYFAILURE': <enum MM_MOBILE_EQUIPMENT_ERROR_MEMORY_FAILURE of type ModemManager.MobileEquipmentError>, 'TEXTTOOLONG': <enum MM_MOBILE_EQUIPMENT_ERROR_TEXT_TOO_LONG of type ModemManager.MobileEquipmentError>, 'INVALIDCHARS': <enum MM_MOBILE_EQUIPMENT_ERROR_INVALID_CHARS of type ModemManager.MobileEquipmentError>, 'DIALSTRINGTOOLONG': <enum MM_MOBILE_EQUIPMENT_ERROR_DIAL_STRING_TOO_LONG of type ModemManager.MobileEquipmentError>, 'DIALSTRINGINVALID': <enum MM_MOBILE_EQUIPMENT_ERROR_DIAL_STRING_INVALID of type ModemManager.MobileEquipmentError>, 'NONETWORK': <enum MM_MOBILE_EQUIPMENT_ERROR_NO_NETWORK of type ModemManager.MobileEquipmentError>, 'NETWORKTIMEOUT': <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_TIMEOUT of type ModemManager.MobileEquipmentError>, 'NETWORKNOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'NETWORKPIN': <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_PIN of type ModemManager.MobileEquipmentError>, 'NETWORKPUK': <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_PUK of type ModemManager.MobileEquipmentError>, 'NETWORKSUBSETPIN': <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_SUBSET_PIN of type ModemManager.MobileEquipmentError>, 'NETWORKSUBSETPUK': <enum MM_MOBILE_EQUIPMENT_ERROR_NETWORK_SUBSET_PUK of type ModemManager.MobileEquipmentError>, 'SERVICEPIN': <enum MM_MOBILE_EQUIPMENT_ERROR_SERVICE_PIN of type ModemManager.MobileEquipmentError>, 'SERVICEPUK': <enum MM_MOBILE_EQUIPMENT_ERROR_SERVICE_PUK of type ModemManager.MobileEquipmentError>, 'CORPPIN': <enum MM_MOBILE_EQUIPMENT_ERROR_CORP_PIN of type ModemManager.MobileEquipmentError>, 'CORPPUK': <enum MM_MOBILE_EQUIPMENT_ERROR_CORP_PUK of type ModemManager.MobileEquipmentError>, 'HIDDENKEYREQUIRED': <enum MM_MOBILE_EQUIPMENT_ERROR_HIDDEN_KEY_REQUIRED of type ModemManager.MobileEquipmentError>, 'EAPMETHODNOTSUPPORTED': <enum MM_MOBILE_EQUIPMENT_ERROR_EAP_METHOD_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 'INCORRECTPARAMETERS': <enum MM_MOBILE_EQUIPMENT_ERROR_INCORRECT_PARAMETERS of type ModemManager.MobileEquipmentError>, 'UNKNOWN': <enum MM_MOBILE_EQUIPMENT_ERROR_UNKNOWN of type ModemManager.MobileEquipmentError>, 'GPRSIMSIUNKNOWNINHLR': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_IMSI_UNKNOWN_IN_HLR of type ModemManager.MobileEquipmentError>, 'GPRSILLEGALMS': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ILLEGAL_MS of type ModemManager.MobileEquipmentError>, 'GPRSIMSIUNKNOWNINVLR': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_IMSI_UNKNOWN_IN_VLR of type ModemManager.MobileEquipmentError>, 'GPRSILLEGALME': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ILLEGAL_ME of type ModemManager.MobileEquipmentError>, 'GPRSSERVICENOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'GPRSANDNONGPRSSERVICESNOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_AND_NON_GPRS_SERVICES_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'GPRSPLMNNOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_PLMN_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'GPRSLOCATIONNOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_LOCATION_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'GPRSROMAINGNOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ROAMING_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'GPRSNOCELLSINLOCATIONAREA': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_NO_CELLS_IN_LOCATION_AREA of type ModemManager.MobileEquipmentError>, 'GPRSNETWORKFAILURE': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_NETWORK_FAILURE of type ModemManager.MobileEquipmentError>, 'GPRSCONGESTION': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_CONGESTION of type ModemManager.MobileEquipmentError>, 'NOTAUTHORIZEDFORCSG': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_NOT_AUTHORIZED_FOR_CSG of type ModemManager.MobileEquipmentError>, 'GPRSINSUFFICIENTRESOURCES': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_INSUFFICIENT_RESOURCES of type ModemManager.MobileEquipmentError>, 'GPRSMISSINGORUNKNOWNAPN': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_MISSING_OR_UNKNOWN_APN of type ModemManager.MobileEquipmentError>, 'GPRSUNKNOWNPDPADDRESSORTYPE': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNKNOWN_PDP_ADDRESS_OR_TYPE of type ModemManager.MobileEquipmentError>, 'GPRSUSERAUTHENTICATIONFAILED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_USER_AUTHENTICATION_FAILED of type ModemManager.MobileEquipmentError>, 'GPRSACTIVATIONREJECTEDBYGGSNORGW': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ACTIVATION_REJECTED_BY_GGSN_OR_GW of type ModemManager.MobileEquipmentError>, 'GPRSACTIVATIONREJECTEDUNSPECIFIED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_ACTIVATION_REJECTED_UNSPECIFIED of type ModemManager.MobileEquipmentError>, 'GPRSSERVICEOPTIONNOTSUPPORTED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 'GPRSSERVICEOPTIONNOTSUBSCRIBED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_NOT_SUBSCRIBED of type ModemManager.MobileEquipmentError>, 'GPRSSERVICEOPTIONOUTOFORDER': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_OUT_OF_ORDER of type ModemManager.MobileEquipmentError>, 'GPRSFEATURENOTSUPPORTED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_FEATURE_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 'GPRSSEMANTICERRORINTFTOPERATION': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SEMANTIC_ERROR_IN_TFT_OPERATION of type ModemManager.MobileEquipmentError>, 'GPRSSYNTACTICALERRORINTFTOPERATION': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SYNTACTICAL_ERROR_IN_TFT_OPERATION of type ModemManager.MobileEquipmentError>, 'GPRSUNKNOWNPDPCONTEXT': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNKNOWN_PDP_CONTEXT of type ModemManager.MobileEquipmentError>, 'GPRSSEMANTICERRORSINPACKETFILTER': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SEMANTIC_ERRORS_IN_PACKET_FILTER of type ModemManager.MobileEquipmentError>, 'GPRSSYNTACTICALERRORSINPACKETFILTER': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SYNTACTICAL_ERROR_IN_PACKET_FILTER of type ModemManager.MobileEquipmentError>, 'GPRSPDPCONTEXTWITHOUTTFTALREADYACTIVATED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_PDP_CONTEXT_WITHOUT_TFT_ALREADY_ACTIVATED of type ModemManager.MobileEquipmentError>, 'GPRSUNKNOWN': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNKNOWN of type ModemManager.MobileEquipmentError>, 'GPRSPDPAUTHFAILURE': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_PDP_AUTH_FAILURE of type ModemManager.MobileEquipmentError>, 'GPRSINVALIDMOBILECLASS': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_INVALID_MOBILE_CLASS of type ModemManager.MobileEquipmentError>, 'GPRSLASTPDNDISCONNECTIONNOTALLOWEDLEGACY': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_LAST_PDN_DISCONNECTION_NOT_ALLOWED_LEGACY of type ModemManager.MobileEquipmentError>, 'GPRSLASTPDNDISCONNECTIONNOTALLOWED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_LAST_PDN_DISCONNECTION_NOT_ALLOWED of type ModemManager.MobileEquipmentError>, 'GPRSSEMANTICALLYINCORRECTMESSAGE': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_SEMANTICALLY_INCORRECT_MESSAGE of type ModemManager.MobileEquipmentError>, 'GPRSMANDATORYIEERROR': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_MANDATORY_IE_ERROR of type ModemManager.MobileEquipmentError>, 'GPRSIENOTIMPLEMENTED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_IE_NOT_IMPLEMENTED of type ModemManager.MobileEquipmentError>, 'GPRSCONDITIONALIEERROR': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_CONDITIONAL_IE_ERROR of type ModemManager.MobileEquipmentError>, 'GPRSUNSPECIFIEDPROTOCOLERROR': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNSPECIFIED_PROTOCOL_ERROR of type ModemManager.MobileEquipmentError>, 'GPRSOPERATORDETERMINEDBARRING': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_OPERATOR_DETERMINED_BARRING of type ModemManager.MobileEquipmentError>, 'GPRSMAXIMUMNUMBEROFPDPCONTEXTSREACHED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_MAXIMUM_NUMBER_OF_PDP_CONTEXTS_REACHED of type ModemManager.MobileEquipmentError>, 'GPRSREQUESTEDAPNNOTSUPPORTED': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_REQUESTED_APN_NOT_SUPPORTED of type ModemManager.MobileEquipmentError>, 'GPRSREQUESTREJECTEDBCMVIOLATION': <enum MM_MOBILE_EQUIPMENT_ERROR_GPRS_REQUEST_REJECTED_BCM_VIOLATION of type ModemManager.MobileEquipmentError>, 'quark': gi.FunctionInfo(quark)})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        30: 30,
        31: 31,
        32: 32,
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
        100: 100,
        102: 102,
        103: 103,
        104: 104,
        106: 106,
        107: 107,
        108: 108,
        111: 111,
        112: 112,
        113: 113,
        115: 115,
        117: 117,
        122: 122,
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
        140: 140,
        141: 141,
        142: 142,
        143: 143,
        144: 144,
        145: 145,
        146: 146,
        148: 148,
        149: 149,
        150: 150,
        151: 151,
        171: 171,
        172: 172,
        173: 173,
        174: 174,
        175: 175,
        176: 176,
        177: 177,
        178: 178,
        179: 179,
        180: 180,
    }
    __gtype__ = None # (!) real value is '<GType MMMobileEquipmentError (94631948615504)>'
    __info__ = gi.EnumInfo(MobileEquipmentError)


