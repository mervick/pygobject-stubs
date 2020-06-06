# encoding: utf-8
# module gi.repository.Flatpak
# from /usr/lib64/girepository-1.0/Flatpak-1.0.typelib
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


    ABORTED = 4
    ALREADY_INSTALLED = 0
    DIFFERENT_REMOTE = 3
    DOWNGRADE = 9
    EXPORT_FAILED = 14
    INVALID_DATA = 11
    INVALID_NAME = 17
    INVALID_REF = 10
    NEED_NEW_FLATPAK = 6
    NOT_CACHED = 20
    NOT_INSTALLED = 1
    ONLY_PULLED = 2
    OUT_OF_SPACE = 18
    PERMISSION_DENIED = 22
    REF_NOT_FOUND = 21
    REMOTE_NOT_FOUND = 7
    REMOTE_USED = 15
    RUNTIME_NOT_FOUND = 8
    RUNTIME_USED = 16
    SETUP_FAILED = 13
    SKIPPED = 5
    UNTRUSTED = 12
    WRONG_USER = 19
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Flatpak', '__dict__': <attribute '__dict__' of 'Error' objects>, '__doc__': None, '__gtype__': <GType FlatpakError (94781644062304)>, '__enum_values__': {0: <enum FLATPAK_ERROR_ALREADY_INSTALLED of type Flatpak.Error>, 1: <enum FLATPAK_ERROR_NOT_INSTALLED of type Flatpak.Error>, 2: <enum FLATPAK_ERROR_ONLY_PULLED of type Flatpak.Error>, 3: <enum FLATPAK_ERROR_DIFFERENT_REMOTE of type Flatpak.Error>, 4: <enum FLATPAK_ERROR_ABORTED of type Flatpak.Error>, 5: <enum FLATPAK_ERROR_SKIPPED of type Flatpak.Error>, 6: <enum FLATPAK_ERROR_NEED_NEW_FLATPAK of type Flatpak.Error>, 7: <enum FLATPAK_ERROR_REMOTE_NOT_FOUND of type Flatpak.Error>, 8: <enum FLATPAK_ERROR_RUNTIME_NOT_FOUND of type Flatpak.Error>, 9: <enum FLATPAK_ERROR_DOWNGRADE of type Flatpak.Error>, 10: <enum FLATPAK_ERROR_INVALID_REF of type Flatpak.Error>, 11: <enum FLATPAK_ERROR_INVALID_DATA of type Flatpak.Error>, 12: <enum FLATPAK_ERROR_UNTRUSTED of type Flatpak.Error>, 13: <enum FLATPAK_ERROR_SETUP_FAILED of type Flatpak.Error>, 14: <enum FLATPAK_ERROR_EXPORT_FAILED of type Flatpak.Error>, 15: <enum FLATPAK_ERROR_REMOTE_USED of type Flatpak.Error>, 16: <enum FLATPAK_ERROR_RUNTIME_USED of type Flatpak.Error>, 17: <enum FLATPAK_ERROR_INVALID_NAME of type Flatpak.Error>, 18: <enum FLATPAK_ERROR_OUT_OF_SPACE of type Flatpak.Error>, 19: <enum FLATPAK_ERROR_WRONG_USER of type Flatpak.Error>, 20: <enum FLATPAK_ERROR_NOT_CACHED of type Flatpak.Error>, 21: <enum FLATPAK_ERROR_REF_NOT_FOUND of type Flatpak.Error>, 22: <enum FLATPAK_ERROR_PERMISSION_DENIED of type Flatpak.Error>}, '__info__': gi.EnumInfo(Error), 'ALREADY_INSTALLED': <enum FLATPAK_ERROR_ALREADY_INSTALLED of type Flatpak.Error>, 'NOT_INSTALLED': <enum FLATPAK_ERROR_NOT_INSTALLED of type Flatpak.Error>, 'ONLY_PULLED': <enum FLATPAK_ERROR_ONLY_PULLED of type Flatpak.Error>, 'DIFFERENT_REMOTE': <enum FLATPAK_ERROR_DIFFERENT_REMOTE of type Flatpak.Error>, 'ABORTED': <enum FLATPAK_ERROR_ABORTED of type Flatpak.Error>, 'SKIPPED': <enum FLATPAK_ERROR_SKIPPED of type Flatpak.Error>, 'NEED_NEW_FLATPAK': <enum FLATPAK_ERROR_NEED_NEW_FLATPAK of type Flatpak.Error>, 'REMOTE_NOT_FOUND': <enum FLATPAK_ERROR_REMOTE_NOT_FOUND of type Flatpak.Error>, 'RUNTIME_NOT_FOUND': <enum FLATPAK_ERROR_RUNTIME_NOT_FOUND of type Flatpak.Error>, 'DOWNGRADE': <enum FLATPAK_ERROR_DOWNGRADE of type Flatpak.Error>, 'INVALID_REF': <enum FLATPAK_ERROR_INVALID_REF of type Flatpak.Error>, 'INVALID_DATA': <enum FLATPAK_ERROR_INVALID_DATA of type Flatpak.Error>, 'UNTRUSTED': <enum FLATPAK_ERROR_UNTRUSTED of type Flatpak.Error>, 'SETUP_FAILED': <enum FLATPAK_ERROR_SETUP_FAILED of type Flatpak.Error>, 'EXPORT_FAILED': <enum FLATPAK_ERROR_EXPORT_FAILED of type Flatpak.Error>, 'REMOTE_USED': <enum FLATPAK_ERROR_REMOTE_USED of type Flatpak.Error>, 'RUNTIME_USED': <enum FLATPAK_ERROR_RUNTIME_USED of type Flatpak.Error>, 'INVALID_NAME': <enum FLATPAK_ERROR_INVALID_NAME of type Flatpak.Error>, 'OUT_OF_SPACE': <enum FLATPAK_ERROR_OUT_OF_SPACE of type Flatpak.Error>, 'WRONG_USER': <enum FLATPAK_ERROR_WRONG_USER of type Flatpak.Error>, 'NOT_CACHED': <enum FLATPAK_ERROR_NOT_CACHED of type Flatpak.Error>, 'REF_NOT_FOUND': <enum FLATPAK_ERROR_REF_NOT_FOUND of type Flatpak.Error>, 'PERMISSION_DENIED': <enum FLATPAK_ERROR_PERMISSION_DENIED of type Flatpak.Error>, 'quark': gi.FunctionInfo(quark)})"
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
    }
    __gtype__ = None # (!) real value is '<GType FlatpakError (94781644062304)>'
    __info__ = gi.EnumInfo(Error)


