# encoding: utf-8
# module gi.repository.Atspi
# from /usr/lib64/girepository-1.0/Atspi-2.0.typelib
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


class StateType(__gobject.GEnum):
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


    ACTIVE = 1
    ANIMATED = 35
    ARMED = 2
    BUSY = 3
    CHECKABLE = 41
    CHECKED = 4
    COLLAPSED = 5
    DEFUNCT = 6
    EDITABLE = 7
    ENABLED = 8
    EXPANDABLE = 9
    EXPANDED = 10
    FOCUSABLE = 11
    FOCUSED = 12
    HAS_POPUP = 42
    HAS_TOOLTIP = 13
    HORIZONTAL = 14
    ICONIFIED = 15
    INDETERMINATE = 32
    INVALID = 0
    INVALID_ENTRY = 36
    IS_DEFAULT = 39
    LAST_DEFINED = 44
    MANAGES_DESCENDANTS = 31
    MODAL = 16
    MULTISELECTABLE = 18
    MULTI_LINE = 17
    OPAQUE = 19
    PRESSED = 20
    READ_ONLY = 43
    REQUIRED = 33
    RESIZABLE = 21
    SELECTABLE = 22
    SELECTABLE_TEXT = 38
    SELECTED = 23
    SENSITIVE = 24
    SHOWING = 25
    SINGLE_LINE = 26
    STALE = 27
    SUPPORTS_AUTOCOMPLETION = 37
    TRANSIENT = 28
    TRUNCATED = 34
    VERTICAL = 29
    VISIBLE = 30
    VISITED = 40
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Atspi', '__dict__': <attribute '__dict__' of 'StateType' objects>, '__doc__': None, '__gtype__': <GType AtspiStateType (94141573838320)>, '__enum_values__': {0: <enum ATSPI_STATE_INVALID of type Atspi.StateType>, 1: <enum ATSPI_STATE_ACTIVE of type Atspi.StateType>, 2: <enum ATSPI_STATE_ARMED of type Atspi.StateType>, 3: <enum ATSPI_STATE_BUSY of type Atspi.StateType>, 4: <enum ATSPI_STATE_CHECKED of type Atspi.StateType>, 5: <enum ATSPI_STATE_COLLAPSED of type Atspi.StateType>, 6: <enum ATSPI_STATE_DEFUNCT of type Atspi.StateType>, 7: <enum ATSPI_STATE_EDITABLE of type Atspi.StateType>, 8: <enum ATSPI_STATE_ENABLED of type Atspi.StateType>, 9: <enum ATSPI_STATE_EXPANDABLE of type Atspi.StateType>, 10: <enum ATSPI_STATE_EXPANDED of type Atspi.StateType>, 11: <enum ATSPI_STATE_FOCUSABLE of type Atspi.StateType>, 12: <enum ATSPI_STATE_FOCUSED of type Atspi.StateType>, 13: <enum ATSPI_STATE_HAS_TOOLTIP of type Atspi.StateType>, 14: <enum ATSPI_STATE_HORIZONTAL of type Atspi.StateType>, 15: <enum ATSPI_STATE_ICONIFIED of type Atspi.StateType>, 16: <enum ATSPI_STATE_MODAL of type Atspi.StateType>, 17: <enum ATSPI_STATE_MULTI_LINE of type Atspi.StateType>, 18: <enum ATSPI_STATE_MULTISELECTABLE of type Atspi.StateType>, 19: <enum ATSPI_STATE_OPAQUE of type Atspi.StateType>, 20: <enum ATSPI_STATE_PRESSED of type Atspi.StateType>, 21: <enum ATSPI_STATE_RESIZABLE of type Atspi.StateType>, 22: <enum ATSPI_STATE_SELECTABLE of type Atspi.StateType>, 23: <enum ATSPI_STATE_SELECTED of type Atspi.StateType>, 24: <enum ATSPI_STATE_SENSITIVE of type Atspi.StateType>, 25: <enum ATSPI_STATE_SHOWING of type Atspi.StateType>, 26: <enum ATSPI_STATE_SINGLE_LINE of type Atspi.StateType>, 27: <enum ATSPI_STATE_STALE of type Atspi.StateType>, 28: <enum ATSPI_STATE_TRANSIENT of type Atspi.StateType>, 29: <enum ATSPI_STATE_VERTICAL of type Atspi.StateType>, 30: <enum ATSPI_STATE_VISIBLE of type Atspi.StateType>, 31: <enum ATSPI_STATE_MANAGES_DESCENDANTS of type Atspi.StateType>, 32: <enum ATSPI_STATE_INDETERMINATE of type Atspi.StateType>, 33: <enum ATSPI_STATE_REQUIRED of type Atspi.StateType>, 34: <enum ATSPI_STATE_TRUNCATED of type Atspi.StateType>, 35: <enum ATSPI_STATE_ANIMATED of type Atspi.StateType>, 36: <enum ATSPI_STATE_INVALID_ENTRY of type Atspi.StateType>, 37: <enum ATSPI_STATE_SUPPORTS_AUTOCOMPLETION of type Atspi.StateType>, 38: <enum ATSPI_STATE_SELECTABLE_TEXT of type Atspi.StateType>, 39: <enum ATSPI_STATE_IS_DEFAULT of type Atspi.StateType>, 40: <enum ATSPI_STATE_VISITED of type Atspi.StateType>, 41: <enum ATSPI_STATE_CHECKABLE of type Atspi.StateType>, 42: <enum ATSPI_STATE_HAS_POPUP of type Atspi.StateType>, 43: <enum ATSPI_STATE_READ_ONLY of type Atspi.StateType>, 44: <enum ATSPI_STATE_LAST_DEFINED of type Atspi.StateType>}, '__info__': gi.EnumInfo(StateType), 'INVALID': <enum ATSPI_STATE_INVALID of type Atspi.StateType>, 'ACTIVE': <enum ATSPI_STATE_ACTIVE of type Atspi.StateType>, 'ARMED': <enum ATSPI_STATE_ARMED of type Atspi.StateType>, 'BUSY': <enum ATSPI_STATE_BUSY of type Atspi.StateType>, 'CHECKED': <enum ATSPI_STATE_CHECKED of type Atspi.StateType>, 'COLLAPSED': <enum ATSPI_STATE_COLLAPSED of type Atspi.StateType>, 'DEFUNCT': <enum ATSPI_STATE_DEFUNCT of type Atspi.StateType>, 'EDITABLE': <enum ATSPI_STATE_EDITABLE of type Atspi.StateType>, 'ENABLED': <enum ATSPI_STATE_ENABLED of type Atspi.StateType>, 'EXPANDABLE': <enum ATSPI_STATE_EXPANDABLE of type Atspi.StateType>, 'EXPANDED': <enum ATSPI_STATE_EXPANDED of type Atspi.StateType>, 'FOCUSABLE': <enum ATSPI_STATE_FOCUSABLE of type Atspi.StateType>, 'FOCUSED': <enum ATSPI_STATE_FOCUSED of type Atspi.StateType>, 'HAS_TOOLTIP': <enum ATSPI_STATE_HAS_TOOLTIP of type Atspi.StateType>, 'HORIZONTAL': <enum ATSPI_STATE_HORIZONTAL of type Atspi.StateType>, 'ICONIFIED': <enum ATSPI_STATE_ICONIFIED of type Atspi.StateType>, 'MODAL': <enum ATSPI_STATE_MODAL of type Atspi.StateType>, 'MULTI_LINE': <enum ATSPI_STATE_MULTI_LINE of type Atspi.StateType>, 'MULTISELECTABLE': <enum ATSPI_STATE_MULTISELECTABLE of type Atspi.StateType>, 'OPAQUE': <enum ATSPI_STATE_OPAQUE of type Atspi.StateType>, 'PRESSED': <enum ATSPI_STATE_PRESSED of type Atspi.StateType>, 'RESIZABLE': <enum ATSPI_STATE_RESIZABLE of type Atspi.StateType>, 'SELECTABLE': <enum ATSPI_STATE_SELECTABLE of type Atspi.StateType>, 'SELECTED': <enum ATSPI_STATE_SELECTED of type Atspi.StateType>, 'SENSITIVE': <enum ATSPI_STATE_SENSITIVE of type Atspi.StateType>, 'SHOWING': <enum ATSPI_STATE_SHOWING of type Atspi.StateType>, 'SINGLE_LINE': <enum ATSPI_STATE_SINGLE_LINE of type Atspi.StateType>, 'STALE': <enum ATSPI_STATE_STALE of type Atspi.StateType>, 'TRANSIENT': <enum ATSPI_STATE_TRANSIENT of type Atspi.StateType>, 'VERTICAL': <enum ATSPI_STATE_VERTICAL of type Atspi.StateType>, 'VISIBLE': <enum ATSPI_STATE_VISIBLE of type Atspi.StateType>, 'MANAGES_DESCENDANTS': <enum ATSPI_STATE_MANAGES_DESCENDANTS of type Atspi.StateType>, 'INDETERMINATE': <enum ATSPI_STATE_INDETERMINATE of type Atspi.StateType>, 'REQUIRED': <enum ATSPI_STATE_REQUIRED of type Atspi.StateType>, 'TRUNCATED': <enum ATSPI_STATE_TRUNCATED of type Atspi.StateType>, 'ANIMATED': <enum ATSPI_STATE_ANIMATED of type Atspi.StateType>, 'INVALID_ENTRY': <enum ATSPI_STATE_INVALID_ENTRY of type Atspi.StateType>, 'SUPPORTS_AUTOCOMPLETION': <enum ATSPI_STATE_SUPPORTS_AUTOCOMPLETION of type Atspi.StateType>, 'SELECTABLE_TEXT': <enum ATSPI_STATE_SELECTABLE_TEXT of type Atspi.StateType>, 'IS_DEFAULT': <enum ATSPI_STATE_IS_DEFAULT of type Atspi.StateType>, 'VISITED': <enum ATSPI_STATE_VISITED of type Atspi.StateType>, 'CHECKABLE': <enum ATSPI_STATE_CHECKABLE of type Atspi.StateType>, 'HAS_POPUP': <enum ATSPI_STATE_HAS_POPUP of type Atspi.StateType>, 'READ_ONLY': <enum ATSPI_STATE_READ_ONLY of type Atspi.StateType>, 'LAST_DEFINED': <enum ATSPI_STATE_LAST_DEFINED of type Atspi.StateType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType AtspiStateType (94141573838320)>'
    __info__ = gi.EnumInfo(StateType)


