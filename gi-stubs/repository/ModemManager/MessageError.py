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


class MessageError(__gobject.GEnum):
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


    INVALIDINDEX = 321
    INVALIDPDUPARAMETER = 304
    INVALIDTEXTPARAMETER = 305
    MEFAILURE = 300
    MEMORYFAILURE = 320
    MEMORYFULL = 322
    NETWORKTIMEOUT = 332
    NOCNMAACKEXPECTED = 340
    NONETWORK = 331
    NOTALLOWED = 302
    NOTSUPPORTED = 303
    PHSIMPIN = 312
    SIMBUSY = 314
    SIMFAILURE = 313
    SIMNOTINSERTED = 310
    SIMPIN = 311
    SIMPIN2 = 317
    SIMPUK = 316
    SIMPUK2 = 318
    SIMWRONG = 315
    SMSCADDRESSUNKNOWN = 330
    SMSSERVICERESERVED = 301
    UNKNOWN = 500
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.ModemManager', '__dict__': <attribute '__dict__' of 'MessageError' objects>, '__doc__': None, '__gtype__': <GType MMMessageError (94631948617536)>, '__enum_values__': {300: <enum MM_MESSAGE_ERROR_ME_FAILURE of type ModemManager.MessageError>, 301: <enum MM_MESSAGE_ERROR_SMS_SERVICE_RESERVED of type ModemManager.MessageError>, 302: <enum MM_MESSAGE_ERROR_NOT_ALLOWED of type ModemManager.MessageError>, 303: <enum MM_MESSAGE_ERROR_NOT_SUPPORTED of type ModemManager.MessageError>, 304: <enum MM_MESSAGE_ERROR_INVALID_PDU_PARAMETER of type ModemManager.MessageError>, 305: <enum MM_MESSAGE_ERROR_INVALID_TEXT_PARAMETER of type ModemManager.MessageError>, 310: <enum MM_MESSAGE_ERROR_SIM_NOT_INSERTED of type ModemManager.MessageError>, 311: <enum MM_MESSAGE_ERROR_SIM_PIN of type ModemManager.MessageError>, 312: <enum MM_MESSAGE_ERROR_PH_SIM_PIN of type ModemManager.MessageError>, 313: <enum MM_MESSAGE_ERROR_SIM_FAILURE of type ModemManager.MessageError>, 314: <enum MM_MESSAGE_ERROR_SIM_BUSY of type ModemManager.MessageError>, 315: <enum MM_MESSAGE_ERROR_SIM_WRONG of type ModemManager.MessageError>, 316: <enum MM_MESSAGE_ERROR_SIM_PUK of type ModemManager.MessageError>, 317: <enum MM_MESSAGE_ERROR_SIM_PIN2 of type ModemManager.MessageError>, 318: <enum MM_MESSAGE_ERROR_SIM_PUK2 of type ModemManager.MessageError>, 320: <enum MM_MESSAGE_ERROR_MEMORY_FAILURE of type ModemManager.MessageError>, 321: <enum MM_MESSAGE_ERROR_INVALID_INDEX of type ModemManager.MessageError>, 322: <enum MM_MESSAGE_ERROR_MEMORY_FULL of type ModemManager.MessageError>, 330: <enum MM_MESSAGE_ERROR_SMSC_ADDRESS_UNKNOWN of type ModemManager.MessageError>, 331: <enum MM_MESSAGE_ERROR_NO_NETWORK of type ModemManager.MessageError>, 332: <enum MM_MESSAGE_ERROR_NETWORK_TIMEOUT of type ModemManager.MessageError>, 340: <enum MM_MESSAGE_ERROR_NO_CNMA_ACK_EXPECTED of type ModemManager.MessageError>, 500: <enum MM_MESSAGE_ERROR_UNKNOWN of type ModemManager.MessageError>}, '__info__': gi.EnumInfo(MessageError), 'MEFAILURE': <enum MM_MESSAGE_ERROR_ME_FAILURE of type ModemManager.MessageError>, 'SMSSERVICERESERVED': <enum MM_MESSAGE_ERROR_SMS_SERVICE_RESERVED of type ModemManager.MessageError>, 'NOTALLOWED': <enum MM_MESSAGE_ERROR_NOT_ALLOWED of type ModemManager.MessageError>, 'NOTSUPPORTED': <enum MM_MESSAGE_ERROR_NOT_SUPPORTED of type ModemManager.MessageError>, 'INVALIDPDUPARAMETER': <enum MM_MESSAGE_ERROR_INVALID_PDU_PARAMETER of type ModemManager.MessageError>, 'INVALIDTEXTPARAMETER': <enum MM_MESSAGE_ERROR_INVALID_TEXT_PARAMETER of type ModemManager.MessageError>, 'SIMNOTINSERTED': <enum MM_MESSAGE_ERROR_SIM_NOT_INSERTED of type ModemManager.MessageError>, 'SIMPIN': <enum MM_MESSAGE_ERROR_SIM_PIN of type ModemManager.MessageError>, 'PHSIMPIN': <enum MM_MESSAGE_ERROR_PH_SIM_PIN of type ModemManager.MessageError>, 'SIMFAILURE': <enum MM_MESSAGE_ERROR_SIM_FAILURE of type ModemManager.MessageError>, 'SIMBUSY': <enum MM_MESSAGE_ERROR_SIM_BUSY of type ModemManager.MessageError>, 'SIMWRONG': <enum MM_MESSAGE_ERROR_SIM_WRONG of type ModemManager.MessageError>, 'SIMPUK': <enum MM_MESSAGE_ERROR_SIM_PUK of type ModemManager.MessageError>, 'SIMPIN2': <enum MM_MESSAGE_ERROR_SIM_PIN2 of type ModemManager.MessageError>, 'SIMPUK2': <enum MM_MESSAGE_ERROR_SIM_PUK2 of type ModemManager.MessageError>, 'MEMORYFAILURE': <enum MM_MESSAGE_ERROR_MEMORY_FAILURE of type ModemManager.MessageError>, 'INVALIDINDEX': <enum MM_MESSAGE_ERROR_INVALID_INDEX of type ModemManager.MessageError>, 'MEMORYFULL': <enum MM_MESSAGE_ERROR_MEMORY_FULL of type ModemManager.MessageError>, 'SMSCADDRESSUNKNOWN': <enum MM_MESSAGE_ERROR_SMSC_ADDRESS_UNKNOWN of type ModemManager.MessageError>, 'NONETWORK': <enum MM_MESSAGE_ERROR_NO_NETWORK of type ModemManager.MessageError>, 'NETWORKTIMEOUT': <enum MM_MESSAGE_ERROR_NETWORK_TIMEOUT of type ModemManager.MessageError>, 'NOCNMAACKEXPECTED': <enum MM_MESSAGE_ERROR_NO_CNMA_ACK_EXPECTED of type ModemManager.MessageError>, 'UNKNOWN': <enum MM_MESSAGE_ERROR_UNKNOWN of type ModemManager.MessageError>, 'quark': gi.FunctionInfo(quark)})"
    __enum_values__ = {
        300: 300,
        301: 301,
        302: 302,
        303: 303,
        304: 304,
        305: 305,
        310: 310,
        311: 311,
        312: 312,
        313: 313,
        314: 314,
        315: 315,
        316: 316,
        317: 317,
        318: 318,
        320: 320,
        321: 321,
        322: 322,
        330: 330,
        331: 331,
        332: 332,
        340: 340,
        500: 500,
    }
    __gtype__ = None # (!) real value is '<GType MMMessageError (94631948617536)>'
    __info__ = gi.EnumInfo(MessageError)


