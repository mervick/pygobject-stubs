# encoding: utf-8
# module gi.repository.Unity
# from /usr/lib/girepository-1.0/Unity-7.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Unity as __gi_overrides_Unity
import gi.repository.Dee as __gi_repository_Dee
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class CategoryType(__gobject.GEnum):
    # no doc
    def bit_length(self): # real signature unknown; restored from __doc__
        """
        int.bit_length() -> int
        
        Number of bits necessary to represent self in binary.
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        return 0

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, bytes, byteorder, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        int.from_bytes(bytes, byteorder, *, signed=False) -> int
        
        Return the integer represented by the given array of bytes.
        
        The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
        
        The byteorder argument determines the byte order used to represent the
        integer.  If byteorder is 'big', the most significant byte is at the
        beginning of the byte array.  If byteorder is 'little', the most
        significant byte is at the end of the byte array.  To request the native
        byte order of the host system, use `sys.byteorder' as the byte order value.
        
        The signed keyword-only argument indicates whether two's complement is
        used to represent the integer.
        """
        pass

    def to_bytes(self, length, byteorder, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        int.to_bytes(length, byteorder, *, signed=False) -> bytes
        
        Return an array of bytes representing an integer.
        
        The integer is represented using length bytes.  An OverflowError is
        raised if the integer is not representable with the given number of
        bytes.
        
        The byteorder argument determines the byte order used to represent the
        integer.  If byteorder is 'big', the most significant byte is at the
        beginning of the byte array.  If byteorder is 'little', the most
        significant byte is at the end of the byte array.  To request the native
        byte order of the host system, use `sys.byteorder' as the byte order value.
        
        The signed keyword-only argument determines whether two's complement is
        used to represent the integer.  If signed is False and a negative integer
        is given, an OverflowError is raised.
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

    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        default dir() implementation
        """
        return []

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
        """ helper for pickle """
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
        """ Returns size in memory, in bytes """
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


    APPLICATION = 1
    BABY = 14
    BEAUTY = 22
    BOOK = 2
    CAR = 25
    CHILDREN = 13
    CLOTHES = 15
    COMPUTERS = 7
    DIY = 23
    ELECTRONICS = 6
    GAMES = 5
    GARDEN = 10
    GROCERY = 20
    HEALTH = 21
    HOME = 9
    MOVIE = 4
    MUSIC = 3
    NONE = 0
    N_CATEGORIES = 26
    OFFICE = 8
    OUTDOORS = 19
    PETS = 11
    SHOES = 16
    SPORTS = 18
    TOOLS = 24
    TOYS = 12
    WATCHES = 17
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Unity', '__dict__': <attribute '__dict__' of 'CategoryType' objects>, '__doc__': None, '__gtype__': <GType UnityCategoryType (26512496)>, '__enum_values__': {0: <enum UNITY_CATEGORY_TYPE_NONE of type Unity.CategoryType>, 1: <enum UNITY_CATEGORY_TYPE_APPLICATION of type Unity.CategoryType>, 2: <enum UNITY_CATEGORY_TYPE_BOOK of type Unity.CategoryType>, 3: <enum UNITY_CATEGORY_TYPE_MUSIC of type Unity.CategoryType>, 4: <enum UNITY_CATEGORY_TYPE_MOVIE of type Unity.CategoryType>, 5: <enum UNITY_CATEGORY_TYPE_GAMES of type Unity.CategoryType>, 6: <enum UNITY_CATEGORY_TYPE_ELECTRONICS of type Unity.CategoryType>, 7: <enum UNITY_CATEGORY_TYPE_COMPUTERS of type Unity.CategoryType>, 8: <enum UNITY_CATEGORY_TYPE_OFFICE of type Unity.CategoryType>, 9: <enum UNITY_CATEGORY_TYPE_HOME of type Unity.CategoryType>, 10: <enum UNITY_CATEGORY_TYPE_GARDEN of type Unity.CategoryType>, 11: <enum UNITY_CATEGORY_TYPE_PETS of type Unity.CategoryType>, 12: <enum UNITY_CATEGORY_TYPE_TOYS of type Unity.CategoryType>, 13: <enum UNITY_CATEGORY_TYPE_CHILDREN of type Unity.CategoryType>, 14: <enum UNITY_CATEGORY_TYPE_BABY of type Unity.CategoryType>, 15: <enum UNITY_CATEGORY_TYPE_CLOTHES of type Unity.CategoryType>, 16: <enum UNITY_CATEGORY_TYPE_SHOES of type Unity.CategoryType>, 17: <enum UNITY_CATEGORY_TYPE_WATCHES of type Unity.CategoryType>, 18: <enum UNITY_CATEGORY_TYPE_SPORTS of type Unity.CategoryType>, 19: <enum UNITY_CATEGORY_TYPE_OUTDOORS of type Unity.CategoryType>, 20: <enum UNITY_CATEGORY_TYPE_GROCERY of type Unity.CategoryType>, 21: <enum UNITY_CATEGORY_TYPE_HEALTH of type Unity.CategoryType>, 22: <enum UNITY_CATEGORY_TYPE_BEAUTY of type Unity.CategoryType>, 23: <enum UNITY_CATEGORY_TYPE_DIY of type Unity.CategoryType>, 24: <enum UNITY_CATEGORY_TYPE_TOOLS of type Unity.CategoryType>, 25: <enum UNITY_CATEGORY_TYPE_CAR of type Unity.CategoryType>, 26: <enum UNITY_CATEGORY_TYPE_N_CATEGORIES of type Unity.CategoryType>}, '__info__': gi.EnumInfo(CategoryType), 'NONE': <enum UNITY_CATEGORY_TYPE_NONE of type Unity.CategoryType>, 'APPLICATION': <enum UNITY_CATEGORY_TYPE_APPLICATION of type Unity.CategoryType>, 'BOOK': <enum UNITY_CATEGORY_TYPE_BOOK of type Unity.CategoryType>, 'MUSIC': <enum UNITY_CATEGORY_TYPE_MUSIC of type Unity.CategoryType>, 'MOVIE': <enum UNITY_CATEGORY_TYPE_MOVIE of type Unity.CategoryType>, 'GAMES': <enum UNITY_CATEGORY_TYPE_GAMES of type Unity.CategoryType>, 'ELECTRONICS': <enum UNITY_CATEGORY_TYPE_ELECTRONICS of type Unity.CategoryType>, 'COMPUTERS': <enum UNITY_CATEGORY_TYPE_COMPUTERS of type Unity.CategoryType>, 'OFFICE': <enum UNITY_CATEGORY_TYPE_OFFICE of type Unity.CategoryType>, 'HOME': <enum UNITY_CATEGORY_TYPE_HOME of type Unity.CategoryType>, 'GARDEN': <enum UNITY_CATEGORY_TYPE_GARDEN of type Unity.CategoryType>, 'PETS': <enum UNITY_CATEGORY_TYPE_PETS of type Unity.CategoryType>, 'TOYS': <enum UNITY_CATEGORY_TYPE_TOYS of type Unity.CategoryType>, 'CHILDREN': <enum UNITY_CATEGORY_TYPE_CHILDREN of type Unity.CategoryType>, 'BABY': <enum UNITY_CATEGORY_TYPE_BABY of type Unity.CategoryType>, 'CLOTHES': <enum UNITY_CATEGORY_TYPE_CLOTHES of type Unity.CategoryType>, 'SHOES': <enum UNITY_CATEGORY_TYPE_SHOES of type Unity.CategoryType>, 'WATCHES': <enum UNITY_CATEGORY_TYPE_WATCHES of type Unity.CategoryType>, 'SPORTS': <enum UNITY_CATEGORY_TYPE_SPORTS of type Unity.CategoryType>, 'OUTDOORS': <enum UNITY_CATEGORY_TYPE_OUTDOORS of type Unity.CategoryType>, 'GROCERY': <enum UNITY_CATEGORY_TYPE_GROCERY of type Unity.CategoryType>, 'HEALTH': <enum UNITY_CATEGORY_TYPE_HEALTH of type Unity.CategoryType>, 'BEAUTY': <enum UNITY_CATEGORY_TYPE_BEAUTY of type Unity.CategoryType>, 'DIY': <enum UNITY_CATEGORY_TYPE_DIY of type Unity.CategoryType>, 'TOOLS': <enum UNITY_CATEGORY_TYPE_TOOLS of type Unity.CategoryType>, 'CAR': <enum UNITY_CATEGORY_TYPE_CAR of type Unity.CategoryType>, 'N_CATEGORIES': <enum UNITY_CATEGORY_TYPE_N_CATEGORIES of type Unity.CategoryType>})"
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
    }
    __gtype__ = None # (!) real value is '<GType UnityCategoryType (26512496)>'
    __info__ = gi.EnumInfo(CategoryType)


