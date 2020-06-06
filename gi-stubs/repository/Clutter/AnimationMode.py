# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class AnimationMode(__gobject.GEnum):
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


    ANIMATION_LAST = 40
    CUBIC_BEZIER = 35
    CUSTOM_MODE = 0
    EASE = 36
    EASE_IN = 37
    EASE_IN_BACK = 26
    EASE_IN_BOUNCE = 29
    EASE_IN_CIRC = 20
    EASE_IN_CUBIC = 5
    EASE_IN_ELASTIC = 23
    EASE_IN_EXPO = 17
    EASE_IN_OUT = 39
    EASE_IN_OUT_BACK = 28
    EASE_IN_OUT_BOUNCE = 31
    EASE_IN_OUT_CIRC = 22
    EASE_IN_OUT_CUBIC = 7
    EASE_IN_OUT_ELASTIC = 25
    EASE_IN_OUT_EXPO = 19
    EASE_IN_OUT_QUAD = 4
    EASE_IN_OUT_QUART = 10
    EASE_IN_OUT_QUINT = 13
    EASE_IN_OUT_SINE = 16
    EASE_IN_QUAD = 2
    EASE_IN_QUART = 8
    EASE_IN_QUINT = 11
    EASE_IN_SINE = 14
    EASE_OUT = 38
    EASE_OUT_BACK = 27
    EASE_OUT_BOUNCE = 30
    EASE_OUT_CIRC = 21
    EASE_OUT_CUBIC = 6
    EASE_OUT_ELASTIC = 24
    EASE_OUT_EXPO = 18
    EASE_OUT_QUAD = 3
    EASE_OUT_QUART = 9
    EASE_OUT_QUINT = 12
    EASE_OUT_SINE = 15
    LINEAR = 1
    STEPS = 32
    STEP_END = 34
    STEP_START = 33
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Clutter', '__dict__': <attribute '__dict__' of 'AnimationMode' objects>, '__doc__': None, '__gtype__': <GType ClutterAnimationMode (94911695939120)>, '__enum_values__': {0: <enum CLUTTER_CUSTOM_MODE of type Clutter.AnimationMode>, 1: <enum CLUTTER_LINEAR of type Clutter.AnimationMode>, 2: <enum CLUTTER_EASE_IN_QUAD of type Clutter.AnimationMode>, 3: <enum CLUTTER_EASE_OUT_QUAD of type Clutter.AnimationMode>, 4: <enum CLUTTER_EASE_IN_OUT_QUAD of type Clutter.AnimationMode>, 5: <enum CLUTTER_EASE_IN_CUBIC of type Clutter.AnimationMode>, 6: <enum CLUTTER_EASE_OUT_CUBIC of type Clutter.AnimationMode>, 7: <enum CLUTTER_EASE_IN_OUT_CUBIC of type Clutter.AnimationMode>, 8: <enum CLUTTER_EASE_IN_QUART of type Clutter.AnimationMode>, 9: <enum CLUTTER_EASE_OUT_QUART of type Clutter.AnimationMode>, 10: <enum CLUTTER_EASE_IN_OUT_QUART of type Clutter.AnimationMode>, 11: <enum CLUTTER_EASE_IN_QUINT of type Clutter.AnimationMode>, 12: <enum CLUTTER_EASE_OUT_QUINT of type Clutter.AnimationMode>, 13: <enum CLUTTER_EASE_IN_OUT_QUINT of type Clutter.AnimationMode>, 14: <enum CLUTTER_EASE_IN_SINE of type Clutter.AnimationMode>, 15: <enum CLUTTER_EASE_OUT_SINE of type Clutter.AnimationMode>, 16: <enum CLUTTER_EASE_IN_OUT_SINE of type Clutter.AnimationMode>, 17: <enum CLUTTER_EASE_IN_EXPO of type Clutter.AnimationMode>, 18: <enum CLUTTER_EASE_OUT_EXPO of type Clutter.AnimationMode>, 19: <enum CLUTTER_EASE_IN_OUT_EXPO of type Clutter.AnimationMode>, 20: <enum CLUTTER_EASE_IN_CIRC of type Clutter.AnimationMode>, 21: <enum CLUTTER_EASE_OUT_CIRC of type Clutter.AnimationMode>, 22: <enum CLUTTER_EASE_IN_OUT_CIRC of type Clutter.AnimationMode>, 23: <enum CLUTTER_EASE_IN_ELASTIC of type Clutter.AnimationMode>, 24: <enum CLUTTER_EASE_OUT_ELASTIC of type Clutter.AnimationMode>, 25: <enum CLUTTER_EASE_IN_OUT_ELASTIC of type Clutter.AnimationMode>, 26: <enum CLUTTER_EASE_IN_BACK of type Clutter.AnimationMode>, 27: <enum CLUTTER_EASE_OUT_BACK of type Clutter.AnimationMode>, 28: <enum CLUTTER_EASE_IN_OUT_BACK of type Clutter.AnimationMode>, 29: <enum CLUTTER_EASE_IN_BOUNCE of type Clutter.AnimationMode>, 30: <enum CLUTTER_EASE_OUT_BOUNCE of type Clutter.AnimationMode>, 31: <enum CLUTTER_EASE_IN_OUT_BOUNCE of type Clutter.AnimationMode>, 32: <enum CLUTTER_STEPS of type Clutter.AnimationMode>, 33: <enum CLUTTER_STEP_START of type Clutter.AnimationMode>, 34: <enum CLUTTER_STEP_END of type Clutter.AnimationMode>, 35: <enum CLUTTER_CUBIC_BEZIER of type Clutter.AnimationMode>, 36: <enum CLUTTER_EASE of type Clutter.AnimationMode>, 37: <enum CLUTTER_EASE_IN of type Clutter.AnimationMode>, 38: <enum CLUTTER_EASE_OUT of type Clutter.AnimationMode>, 39: <enum CLUTTER_EASE_IN_OUT of type Clutter.AnimationMode>, 40: <enum CLUTTER_ANIMATION_LAST of type Clutter.AnimationMode>}, '__info__': gi.EnumInfo(AnimationMode), 'CUSTOM_MODE': <enum CLUTTER_CUSTOM_MODE of type Clutter.AnimationMode>, 'LINEAR': <enum CLUTTER_LINEAR of type Clutter.AnimationMode>, 'EASE_IN_QUAD': <enum CLUTTER_EASE_IN_QUAD of type Clutter.AnimationMode>, 'EASE_OUT_QUAD': <enum CLUTTER_EASE_OUT_QUAD of type Clutter.AnimationMode>, 'EASE_IN_OUT_QUAD': <enum CLUTTER_EASE_IN_OUT_QUAD of type Clutter.AnimationMode>, 'EASE_IN_CUBIC': <enum CLUTTER_EASE_IN_CUBIC of type Clutter.AnimationMode>, 'EASE_OUT_CUBIC': <enum CLUTTER_EASE_OUT_CUBIC of type Clutter.AnimationMode>, 'EASE_IN_OUT_CUBIC': <enum CLUTTER_EASE_IN_OUT_CUBIC of type Clutter.AnimationMode>, 'EASE_IN_QUART': <enum CLUTTER_EASE_IN_QUART of type Clutter.AnimationMode>, 'EASE_OUT_QUART': <enum CLUTTER_EASE_OUT_QUART of type Clutter.AnimationMode>, 'EASE_IN_OUT_QUART': <enum CLUTTER_EASE_IN_OUT_QUART of type Clutter.AnimationMode>, 'EASE_IN_QUINT': <enum CLUTTER_EASE_IN_QUINT of type Clutter.AnimationMode>, 'EASE_OUT_QUINT': <enum CLUTTER_EASE_OUT_QUINT of type Clutter.AnimationMode>, 'EASE_IN_OUT_QUINT': <enum CLUTTER_EASE_IN_OUT_QUINT of type Clutter.AnimationMode>, 'EASE_IN_SINE': <enum CLUTTER_EASE_IN_SINE of type Clutter.AnimationMode>, 'EASE_OUT_SINE': <enum CLUTTER_EASE_OUT_SINE of type Clutter.AnimationMode>, 'EASE_IN_OUT_SINE': <enum CLUTTER_EASE_IN_OUT_SINE of type Clutter.AnimationMode>, 'EASE_IN_EXPO': <enum CLUTTER_EASE_IN_EXPO of type Clutter.AnimationMode>, 'EASE_OUT_EXPO': <enum CLUTTER_EASE_OUT_EXPO of type Clutter.AnimationMode>, 'EASE_IN_OUT_EXPO': <enum CLUTTER_EASE_IN_OUT_EXPO of type Clutter.AnimationMode>, 'EASE_IN_CIRC': <enum CLUTTER_EASE_IN_CIRC of type Clutter.AnimationMode>, 'EASE_OUT_CIRC': <enum CLUTTER_EASE_OUT_CIRC of type Clutter.AnimationMode>, 'EASE_IN_OUT_CIRC': <enum CLUTTER_EASE_IN_OUT_CIRC of type Clutter.AnimationMode>, 'EASE_IN_ELASTIC': <enum CLUTTER_EASE_IN_ELASTIC of type Clutter.AnimationMode>, 'EASE_OUT_ELASTIC': <enum CLUTTER_EASE_OUT_ELASTIC of type Clutter.AnimationMode>, 'EASE_IN_OUT_ELASTIC': <enum CLUTTER_EASE_IN_OUT_ELASTIC of type Clutter.AnimationMode>, 'EASE_IN_BACK': <enum CLUTTER_EASE_IN_BACK of type Clutter.AnimationMode>, 'EASE_OUT_BACK': <enum CLUTTER_EASE_OUT_BACK of type Clutter.AnimationMode>, 'EASE_IN_OUT_BACK': <enum CLUTTER_EASE_IN_OUT_BACK of type Clutter.AnimationMode>, 'EASE_IN_BOUNCE': <enum CLUTTER_EASE_IN_BOUNCE of type Clutter.AnimationMode>, 'EASE_OUT_BOUNCE': <enum CLUTTER_EASE_OUT_BOUNCE of type Clutter.AnimationMode>, 'EASE_IN_OUT_BOUNCE': <enum CLUTTER_EASE_IN_OUT_BOUNCE of type Clutter.AnimationMode>, 'STEPS': <enum CLUTTER_STEPS of type Clutter.AnimationMode>, 'STEP_START': <enum CLUTTER_STEP_START of type Clutter.AnimationMode>, 'STEP_END': <enum CLUTTER_STEP_END of type Clutter.AnimationMode>, 'CUBIC_BEZIER': <enum CLUTTER_CUBIC_BEZIER of type Clutter.AnimationMode>, 'EASE': <enum CLUTTER_EASE of type Clutter.AnimationMode>, 'EASE_IN': <enum CLUTTER_EASE_IN of type Clutter.AnimationMode>, 'EASE_OUT': <enum CLUTTER_EASE_OUT of type Clutter.AnimationMode>, 'EASE_IN_OUT': <enum CLUTTER_EASE_IN_OUT of type Clutter.AnimationMode>, 'ANIMATION_LAST': <enum CLUTTER_ANIMATION_LAST of type Clutter.AnimationMode>})"
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
    }
    __gtype__ = None # (!) real value is '<GType ClutterAnimationMode (94911695939120)>'
    __info__ = gi.EnumInfo(AnimationMode)


