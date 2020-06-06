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


class SmsDeliveryState(__gobject.GEnum):
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

    def get_string(self, val): # real signature unknown; restored from __doc__
        """ get_string(val:ModemManager.SmsDeliveryState) -> str """
        return ""

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


    COMPLETED_FORWARDED_UNCONFIRMED = 1
    COMPLETED_RECEIVED = 0
    COMPLETED_REPLACED_BY_SC = 2
    ERROR_CONNECTION_REJECTED = 66
    ERROR_DELETED_BY_ORIGINATING_SME = 71
    ERROR_DELETED_BY_SC_ADMINISTRATION = 72
    ERROR_INCOMPATIBLE_DESTINATION = 65
    ERROR_MESSAGE_DOES_NOT_EXIST = 73
    ERROR_NOT_OBTAINABLE = 67
    ERROR_NO_INTERWORKING_AVAILABLE = 69
    ERROR_QOS_NOT_AVAILABLE = 68
    ERROR_REMOTE_PROCEDURE = 64
    ERROR_VALIDITY_PERIOD_EXPIRED = 70
    GENERAL_PROBLEM_ENCODING = 608
    GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER = 614
    GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER = 615
    GENERAL_PROBLEM_OTHER = 619
    GENERAL_PROBLEM_SMS_NOT_SUPPORTED = 612
    GENERAL_PROBLEM_SMS_ORIGINATION_DENIED = 609
    GENERAL_PROBLEM_SMS_TERMINATION_DENIED = 610
    GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED = 611
    GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE = 617
    GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE = 616
    GENERAL_PROBLEM_USER_DATA_SIZE_ERROR = 618
    NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE = 513
    NETWORK_PROBLEM_ADDRESS_VACANT = 512
    NETWORK_PROBLEM_INVALID_TELESERVICE_ID = 516
    NETWORK_PROBLEM_NETWORK_FAILURE = 515
    NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE = 514
    NETWORK_PROBLEM_OTHER = 517
    RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY = 577
    RADIO_INTERFACE_PROBLEM_OTHER = 578
    RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE = 576
    TEMPORARY_ERROR_CONGESTION = 32
    TEMPORARY_ERROR_IN_SME = 37
    TEMPORARY_ERROR_NO_RESPONSE_FROM_SME = 34
    TEMPORARY_ERROR_QOS_NOT_AVAILABLE = 36
    TEMPORARY_ERROR_SERVICE_REJECTED = 35
    TEMPORARY_ERROR_SME_BUSY = 33
    TEMPORARY_FATAL_ERROR_CONGESTION = 96
    TEMPORARY_FATAL_ERROR_IN_SME = 101
    TEMPORARY_FATAL_ERROR_NO_RESPONSE_FROM_SME = 98
    TEMPORARY_FATAL_ERROR_QOS_NOT_AVAILABLE = 100
    TEMPORARY_FATAL_ERROR_SERVICE_REJECTED = 99
    TEMPORARY_FATAL_ERROR_SME_BUSY = 97
    TEMPORARY_GENERAL_PROBLEM_ENCODING = 864
    TEMPORARY_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER = 870
    TEMPORARY_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER = 871
    TEMPORARY_GENERAL_PROBLEM_OTHER = 875
    TEMPORARY_GENERAL_PROBLEM_SMS_NOT_SUPPORTED = 868
    TEMPORARY_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED = 865
    TEMPORARY_GENERAL_PROBLEM_SMS_TERMINATION_DENIED = 866
    TEMPORARY_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED = 867
    TEMPORARY_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE = 873
    TEMPORARY_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE = 872
    TEMPORARY_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR = 874
    TEMPORARY_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE = 769
    TEMPORARY_NETWORK_PROBLEM_ADDRESS_VACANT = 768
    TEMPORARY_NETWORK_PROBLEM_INVALID_TELESERVICE_ID = 772
    TEMPORARY_NETWORK_PROBLEM_NETWORK_FAILURE = 771
    TEMPORARY_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE = 770
    TEMPORARY_NETWORK_PROBLEM_OTHER = 773
    TEMPORARY_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY = 833
    TEMPORARY_RADIO_INTERFACE_PROBLEM_OTHER = 834
    TEMPORARY_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE = 832
    TEMPORARY_TERMINAL_PROBLEM_DESTINATION_BUSY = 801
    TEMPORARY_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS = 806
    TEMPORARY_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE = 805
    TEMPORARY_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE = 803
    TEMPORARY_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT = 802
    TEMPORARY_TERMINAL_PROBLEM_NO_PAGE_RESPONSE = 800
    TEMPORARY_TERMINAL_PROBLEM_OTHER = 807
    TEMPORARY_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED = 804
    TERMINAL_PROBLEM_DESTINATION_BUSY = 545
    TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS = 550
    TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE = 549
    TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE = 547
    TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT = 546
    TERMINAL_PROBLEM_NO_PAGE_RESPONSE = 544
    TERMINAL_PROBLEM_OTHER = 551
    TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED = 548
    UNKNOWN = 256
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ModemManager', '__dict__': <attribute '__dict__' of 'SmsDeliveryState' objects>, '__doc__': None, '__gtype__': <GType MMSmsDeliveryState (94631948900192)>, '__enum_values__': {0: <enum MM_SMS_DELIVERY_STATE_COMPLETED_RECEIVED of type ModemManager.SmsDeliveryState>, 1: <enum MM_SMS_DELIVERY_STATE_COMPLETED_FORWARDED_UNCONFIRMED of type ModemManager.SmsDeliveryState>, 2: <enum MM_SMS_DELIVERY_STATE_COMPLETED_REPLACED_BY_SC of type ModemManager.SmsDeliveryState>, 32: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_CONGESTION of type ModemManager.SmsDeliveryState>, 33: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_SME_BUSY of type ModemManager.SmsDeliveryState>, 34: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_NO_RESPONSE_FROM_SME of type ModemManager.SmsDeliveryState>, 35: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_SERVICE_REJECTED of type ModemManager.SmsDeliveryState>, 36: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_QOS_NOT_AVAILABLE of type ModemManager.SmsDeliveryState>, 37: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_IN_SME of type ModemManager.SmsDeliveryState>, 64: <enum MM_SMS_DELIVERY_STATE_ERROR_REMOTE_PROCEDURE of type ModemManager.SmsDeliveryState>, 65: <enum MM_SMS_DELIVERY_STATE_ERROR_INCOMPATIBLE_DESTINATION of type ModemManager.SmsDeliveryState>, 66: <enum MM_SMS_DELIVERY_STATE_ERROR_CONNECTION_REJECTED of type ModemManager.SmsDeliveryState>, 67: <enum MM_SMS_DELIVERY_STATE_ERROR_NOT_OBTAINABLE of type ModemManager.SmsDeliveryState>, 68: <enum MM_SMS_DELIVERY_STATE_ERROR_QOS_NOT_AVAILABLE of type ModemManager.SmsDeliveryState>, 69: <enum MM_SMS_DELIVERY_STATE_ERROR_NO_INTERWORKING_AVAILABLE of type ModemManager.SmsDeliveryState>, 70: <enum MM_SMS_DELIVERY_STATE_ERROR_VALIDITY_PERIOD_EXPIRED of type ModemManager.SmsDeliveryState>, 71: <enum MM_SMS_DELIVERY_STATE_ERROR_DELETED_BY_ORIGINATING_SME of type ModemManager.SmsDeliveryState>, 72: <enum MM_SMS_DELIVERY_STATE_ERROR_DELETED_BY_SC_ADMINISTRATION of type ModemManager.SmsDeliveryState>, 73: <enum MM_SMS_DELIVERY_STATE_ERROR_MESSAGE_DOES_NOT_EXIST of type ModemManager.SmsDeliveryState>, 96: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_CONGESTION of type ModemManager.SmsDeliveryState>, 97: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_SME_BUSY of type ModemManager.SmsDeliveryState>, 98: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_NO_RESPONSE_FROM_SME of type ModemManager.SmsDeliveryState>, 99: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_SERVICE_REJECTED of type ModemManager.SmsDeliveryState>, 100: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_QOS_NOT_AVAILABLE of type ModemManager.SmsDeliveryState>, 101: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_IN_SME of type ModemManager.SmsDeliveryState>, 256: <enum MM_SMS_DELIVERY_STATE_UNKNOWN of type ModemManager.SmsDeliveryState>, 512: <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_ADDRESS_VACANT of type ModemManager.SmsDeliveryState>, 513: <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE of type ModemManager.SmsDeliveryState>, 514: <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE of type ModemManager.SmsDeliveryState>, 515: <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_NETWORK_FAILURE of type ModemManager.SmsDeliveryState>, 516: <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_INVALID_TELESERVICE_ID of type ModemManager.SmsDeliveryState>, 517: <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 544: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_NO_PAGE_RESPONSE of type ModemManager.SmsDeliveryState>, 545: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_BUSY of type ModemManager.SmsDeliveryState>, 546: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT of type ModemManager.SmsDeliveryState>, 547: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 548: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED of type ModemManager.SmsDeliveryState>, 549: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE of type ModemManager.SmsDeliveryState>, 550: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS of type ModemManager.SmsDeliveryState>, 551: <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 576: <enum MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 577: <enum MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY of type ModemManager.SmsDeliveryState>, 578: <enum MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 608: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_ENCODING of type ModemManager.SmsDeliveryState>, 609: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED of type ModemManager.SmsDeliveryState>, 610: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_TERMINATION_DENIED of type ModemManager.SmsDeliveryState>, 611: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 612: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 614: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER of type ModemManager.SmsDeliveryState>, 615: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER of type ModemManager.SmsDeliveryState>, 616: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 617: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 618: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR of type ModemManager.SmsDeliveryState>, 619: <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 768: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_ADDRESS_VACANT of type ModemManager.SmsDeliveryState>, 769: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE of type ModemManager.SmsDeliveryState>, 770: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE of type ModemManager.SmsDeliveryState>, 771: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_NETWORK_FAILURE of type ModemManager.SmsDeliveryState>, 772: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_INVALID_TELESERVICE_ID of type ModemManager.SmsDeliveryState>, 773: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 800: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_NO_PAGE_RESPONSE of type ModemManager.SmsDeliveryState>, 801: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_BUSY of type ModemManager.SmsDeliveryState>, 802: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT of type ModemManager.SmsDeliveryState>, 803: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 804: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED of type ModemManager.SmsDeliveryState>, 805: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE of type ModemManager.SmsDeliveryState>, 806: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS of type ModemManager.SmsDeliveryState>, 807: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 832: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 833: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY of type ModemManager.SmsDeliveryState>, 834: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 864: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_ENCODING of type ModemManager.SmsDeliveryState>, 865: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED of type ModemManager.SmsDeliveryState>, 866: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_TERMINATION_DENIED of type ModemManager.SmsDeliveryState>, 867: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 868: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 870: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER of type ModemManager.SmsDeliveryState>, 871: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER of type ModemManager.SmsDeliveryState>, 872: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 873: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 874: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR of type ModemManager.SmsDeliveryState>, 875: <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>}, '__info__': gi.EnumInfo(SmsDeliveryState), 'COMPLETED_RECEIVED': <enum MM_SMS_DELIVERY_STATE_COMPLETED_RECEIVED of type ModemManager.SmsDeliveryState>, 'COMPLETED_FORWARDED_UNCONFIRMED': <enum MM_SMS_DELIVERY_STATE_COMPLETED_FORWARDED_UNCONFIRMED of type ModemManager.SmsDeliveryState>, 'COMPLETED_REPLACED_BY_SC': <enum MM_SMS_DELIVERY_STATE_COMPLETED_REPLACED_BY_SC of type ModemManager.SmsDeliveryState>, 'TEMPORARY_ERROR_CONGESTION': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_CONGESTION of type ModemManager.SmsDeliveryState>, 'TEMPORARY_ERROR_SME_BUSY': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_SME_BUSY of type ModemManager.SmsDeliveryState>, 'TEMPORARY_ERROR_NO_RESPONSE_FROM_SME': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_NO_RESPONSE_FROM_SME of type ModemManager.SmsDeliveryState>, 'TEMPORARY_ERROR_SERVICE_REJECTED': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_SERVICE_REJECTED of type ModemManager.SmsDeliveryState>, 'TEMPORARY_ERROR_QOS_NOT_AVAILABLE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_QOS_NOT_AVAILABLE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_ERROR_IN_SME': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_ERROR_IN_SME of type ModemManager.SmsDeliveryState>, 'ERROR_REMOTE_PROCEDURE': <enum MM_SMS_DELIVERY_STATE_ERROR_REMOTE_PROCEDURE of type ModemManager.SmsDeliveryState>, 'ERROR_INCOMPATIBLE_DESTINATION': <enum MM_SMS_DELIVERY_STATE_ERROR_INCOMPATIBLE_DESTINATION of type ModemManager.SmsDeliveryState>, 'ERROR_CONNECTION_REJECTED': <enum MM_SMS_DELIVERY_STATE_ERROR_CONNECTION_REJECTED of type ModemManager.SmsDeliveryState>, 'ERROR_NOT_OBTAINABLE': <enum MM_SMS_DELIVERY_STATE_ERROR_NOT_OBTAINABLE of type ModemManager.SmsDeliveryState>, 'ERROR_QOS_NOT_AVAILABLE': <enum MM_SMS_DELIVERY_STATE_ERROR_QOS_NOT_AVAILABLE of type ModemManager.SmsDeliveryState>, 'ERROR_NO_INTERWORKING_AVAILABLE': <enum MM_SMS_DELIVERY_STATE_ERROR_NO_INTERWORKING_AVAILABLE of type ModemManager.SmsDeliveryState>, 'ERROR_VALIDITY_PERIOD_EXPIRED': <enum MM_SMS_DELIVERY_STATE_ERROR_VALIDITY_PERIOD_EXPIRED of type ModemManager.SmsDeliveryState>, 'ERROR_DELETED_BY_ORIGINATING_SME': <enum MM_SMS_DELIVERY_STATE_ERROR_DELETED_BY_ORIGINATING_SME of type ModemManager.SmsDeliveryState>, 'ERROR_DELETED_BY_SC_ADMINISTRATION': <enum MM_SMS_DELIVERY_STATE_ERROR_DELETED_BY_SC_ADMINISTRATION of type ModemManager.SmsDeliveryState>, 'ERROR_MESSAGE_DOES_NOT_EXIST': <enum MM_SMS_DELIVERY_STATE_ERROR_MESSAGE_DOES_NOT_EXIST of type ModemManager.SmsDeliveryState>, 'TEMPORARY_FATAL_ERROR_CONGESTION': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_CONGESTION of type ModemManager.SmsDeliveryState>, 'TEMPORARY_FATAL_ERROR_SME_BUSY': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_SME_BUSY of type ModemManager.SmsDeliveryState>, 'TEMPORARY_FATAL_ERROR_NO_RESPONSE_FROM_SME': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_NO_RESPONSE_FROM_SME of type ModemManager.SmsDeliveryState>, 'TEMPORARY_FATAL_ERROR_SERVICE_REJECTED': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_SERVICE_REJECTED of type ModemManager.SmsDeliveryState>, 'TEMPORARY_FATAL_ERROR_QOS_NOT_AVAILABLE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_QOS_NOT_AVAILABLE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_FATAL_ERROR_IN_SME': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_FATAL_ERROR_IN_SME of type ModemManager.SmsDeliveryState>, 'UNKNOWN': <enum MM_SMS_DELIVERY_STATE_UNKNOWN of type ModemManager.SmsDeliveryState>, 'NETWORK_PROBLEM_ADDRESS_VACANT': <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_ADDRESS_VACANT of type ModemManager.SmsDeliveryState>, 'NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE': <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE of type ModemManager.SmsDeliveryState>, 'NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE': <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE of type ModemManager.SmsDeliveryState>, 'NETWORK_PROBLEM_NETWORK_FAILURE': <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_NETWORK_FAILURE of type ModemManager.SmsDeliveryState>, 'NETWORK_PROBLEM_INVALID_TELESERVICE_ID': <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_INVALID_TELESERVICE_ID of type ModemManager.SmsDeliveryState>, 'NETWORK_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_NETWORK_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_NO_PAGE_RESPONSE': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_NO_PAGE_RESPONSE of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_DESTINATION_BUSY': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_BUSY of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS of type ModemManager.SmsDeliveryState>, 'TERMINAL_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_TERMINAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE': <enum MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 'RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY': <enum MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY of type ModemManager.SmsDeliveryState>, 'RADIO_INTERFACE_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_RADIO_INTERFACE_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_ENCODING': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_ENCODING of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_SMS_ORIGINATION_DENIED': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_SMS_TERMINATION_DENIED': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_TERMINATION_DENIED of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_SMS_NOT_SUPPORTED': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_SMS_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_USER_DATA_SIZE_ERROR': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR of type ModemManager.SmsDeliveryState>, 'GENERAL_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_GENERAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'TEMPORARY_NETWORK_PROBLEM_ADDRESS_VACANT': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_ADDRESS_VACANT of type ModemManager.SmsDeliveryState>, 'TEMPORARY_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_ADDRESS_TRANSLATION_FAILURE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_NETWORK_RESOURCE_OUTAGE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_NETWORK_PROBLEM_NETWORK_FAILURE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_NETWORK_FAILURE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_NETWORK_PROBLEM_INVALID_TELESERVICE_ID': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_INVALID_TELESERVICE_ID of type ModemManager.SmsDeliveryState>, 'TEMPORARY_NETWORK_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_NETWORK_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_NO_PAGE_RESPONSE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_NO_PAGE_RESPONSE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_DESTINATION_BUSY': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_BUSY of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_NO_ACKNOWLEDGMENT of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_SMS_DELIVERY_POSTPONED of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_OUT_OF_SERVICE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_DESTINATION_NO_LONGER_AT_THIS_ADDRESS of type ModemManager.SmsDeliveryState>, 'TEMPORARY_TERMINAL_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_TERMINAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'TEMPORARY_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_RESOURCE_SHORTAGE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_INCOMPATIBILITY of type ModemManager.SmsDeliveryState>, 'TEMPORARY_RADIO_INTERFACE_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_RADIO_INTERFACE_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_ENCODING': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_ENCODING of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_ORIGINATION_DENIED of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_SMS_TERMINATION_DENIED': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_TERMINATION_DENIED of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SUPPLEMENTARY_SERVICE_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_SMS_NOT_SUPPORTED': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_SMS_NOT_SUPPORTED of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_MISSING_EXPECTED_PARAMETER of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_MISSING_MANDATORY_PARAMETER of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_UNRECOGNIZED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_UNEXPECTED_PARAMETER_VALUE of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_USER_DATA_SIZE_ERROR of type ModemManager.SmsDeliveryState>, 'TEMPORARY_GENERAL_PROBLEM_OTHER': <enum MM_SMS_DELIVERY_STATE_TEMPORARY_GENERAL_PROBLEM_OTHER of type ModemManager.SmsDeliveryState>, 'get_string': gi.FunctionInfo(get_string)})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
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
        96: 96,
        97: 97,
        98: 98,
        99: 99,
        100: 100,
        101: 101,
        256: 256,
        512: 512,
        513: 513,
        514: 514,
        515: 515,
        516: 516,
        517: 517,
        544: 544,
        545: 545,
        546: 546,
        547: 547,
        548: 548,
        549: 549,
        550: 550,
        551: 551,
        576: 576,
        577: 577,
        578: 578,
        608: 608,
        609: 609,
        610: 610,
        611: 611,
        612: 612,
        614: 614,
        615: 615,
        616: 616,
        617: 617,
        618: 618,
        619: 619,
        768: 768,
        769: 769,
        770: 770,
        771: 771,
        772: 772,
        773: 773,
        800: 800,
        801: 801,
        802: 802,
        803: 803,
        804: 804,
        805: 805,
        806: 806,
        807: 807,
        832: 832,
        833: 833,
        834: 834,
        864: 864,
        865: 865,
        866: 866,
        867: 867,
        868: 868,
        870: 870,
        871: 871,
        872: 872,
        873: 873,
        874: 874,
        875: 875,
    }
    __gtype__ = None # (!) real value is '<GType MMSmsDeliveryState (94631948900192)>'
    __info__ = gi.EnumInfo(SmsDeliveryState)


