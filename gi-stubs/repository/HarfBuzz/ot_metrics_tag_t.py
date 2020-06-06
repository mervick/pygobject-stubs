# encoding: utf-8
# module gi.repository.HarfBuzz
# from /usr/lib64/girepository-1.0/HarfBuzz-0.0.typelib
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


class ot_metrics_tag_t(__gobject.GEnum):
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


    CAP_HEIGHT = 1668311156
    HORIZONTAL_ASCENDER = 1751216995
    HORIZONTAL_CARET_OFFSET = 1751347046
    HORIZONTAL_CARET_RISE = 1751347827
    HORIZONTAL_CARET_RUN = 1751347822
    HORIZONTAL_CLIPPING_ASCENT = 1751346273
    HORIZONTAL_CLIPPING_DESCENT = 1751346276
    HORIZONTAL_DESCENDER = 1751413603
    HORIZONTAL_LINE_GAP = 1751934832
    STRIKEOUT_OFFSET = 1937011311
    STRIKEOUT_SIZE = 1937011315
    SUBSCRIPT_EM_X_OFFSET = 1935833199
    SUBSCRIPT_EM_X_SIZE = 1935833203
    SUBSCRIPT_EM_Y_OFFSET = 1935833455
    SUBSCRIPT_EM_Y_SIZE = 1935833459
    SUPERSCRIPT_EM_X_OFFSET = 1936750703
    SUPERSCRIPT_EM_X_SIZE = 1936750707
    SUPERSCRIPT_EM_Y_OFFSET = 1936750959
    SUPERSCRIPT_EM_Y_SIZE = 1936750963
    UNDERLINE_OFFSET = 1970168943
    UNDERLINE_SIZE = 1970168947
    VERTICAL_ASCENDER = 1986098019
    VERTICAL_CARET_OFFSET = 1986228070
    VERTICAL_CARET_RISE = 1986228851
    VERTICAL_CARET_RUN = 1986228846
    VERTICAL_DESCENDER = 1986294627
    VERTICAL_LINE_GAP = 1986815856
    X_HEIGHT = 2020108148
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.HarfBuzz', '__dict__': <attribute '__dict__' of 'ot_metrics_tag_t' objects>, '__doc__': None, '__gtype__': <GType hb_ot_metrics_tag_t (94618627285888)>, '__enum_values__': {1751216995: <enum HB_OT_METRICS_TAG_HORIZONTAL_ASCENDER of type HarfBuzz.ot_metrics_tag_t>, 1751413603: <enum HB_OT_METRICS_TAG_HORIZONTAL_DESCENDER of type HarfBuzz.ot_metrics_tag_t>, 1751934832: <enum HB_OT_METRICS_TAG_HORIZONTAL_LINE_GAP of type HarfBuzz.ot_metrics_tag_t>, 1751346273: <enum HB_OT_METRICS_TAG_HORIZONTAL_CLIPPING_ASCENT of type HarfBuzz.ot_metrics_tag_t>, 1751346276: <enum HB_OT_METRICS_TAG_HORIZONTAL_CLIPPING_DESCENT of type HarfBuzz.ot_metrics_tag_t>, 1986098019: <enum HB_OT_METRICS_TAG_VERTICAL_ASCENDER of type HarfBuzz.ot_metrics_tag_t>, 1986294627: <enum HB_OT_METRICS_TAG_VERTICAL_DESCENDER of type HarfBuzz.ot_metrics_tag_t>, 1986815856: <enum HB_OT_METRICS_TAG_VERTICAL_LINE_GAP of type HarfBuzz.ot_metrics_tag_t>, 1751347827: <enum HB_OT_METRICS_TAG_HORIZONTAL_CARET_RISE of type HarfBuzz.ot_metrics_tag_t>, 1751347822: <enum HB_OT_METRICS_TAG_HORIZONTAL_CARET_RUN of type HarfBuzz.ot_metrics_tag_t>, 1751347046: <enum HB_OT_METRICS_TAG_HORIZONTAL_CARET_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 1986228851: <enum HB_OT_METRICS_TAG_VERTICAL_CARET_RISE of type HarfBuzz.ot_metrics_tag_t>, 1986228846: <enum HB_OT_METRICS_TAG_VERTICAL_CARET_RUN of type HarfBuzz.ot_metrics_tag_t>, 1986228070: <enum HB_OT_METRICS_TAG_VERTICAL_CARET_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 2020108148: <enum HB_OT_METRICS_TAG_X_HEIGHT of type HarfBuzz.ot_metrics_tag_t>, 1668311156: <enum HB_OT_METRICS_TAG_CAP_HEIGHT of type HarfBuzz.ot_metrics_tag_t>, 1935833203: <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_X_SIZE of type HarfBuzz.ot_metrics_tag_t>, 1935833459: <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_Y_SIZE of type HarfBuzz.ot_metrics_tag_t>, 1935833199: <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_X_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 1935833455: <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_Y_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 1936750707: <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_X_SIZE of type HarfBuzz.ot_metrics_tag_t>, 1936750963: <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_SIZE of type HarfBuzz.ot_metrics_tag_t>, 1936750703: <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_X_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 1936750959: <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 1937011315: <enum HB_OT_METRICS_TAG_STRIKEOUT_SIZE of type HarfBuzz.ot_metrics_tag_t>, 1937011311: <enum HB_OT_METRICS_TAG_STRIKEOUT_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 1970168947: <enum HB_OT_METRICS_TAG_UNDERLINE_SIZE of type HarfBuzz.ot_metrics_tag_t>, 1970168943: <enum HB_OT_METRICS_TAG_UNDERLINE_OFFSET of type HarfBuzz.ot_metrics_tag_t>}, '__info__': gi.EnumInfo(ot_metrics_tag_t), 'HORIZONTAL_ASCENDER': <enum HB_OT_METRICS_TAG_HORIZONTAL_ASCENDER of type HarfBuzz.ot_metrics_tag_t>, 'HORIZONTAL_DESCENDER': <enum HB_OT_METRICS_TAG_HORIZONTAL_DESCENDER of type HarfBuzz.ot_metrics_tag_t>, 'HORIZONTAL_LINE_GAP': <enum HB_OT_METRICS_TAG_HORIZONTAL_LINE_GAP of type HarfBuzz.ot_metrics_tag_t>, 'HORIZONTAL_CLIPPING_ASCENT': <enum HB_OT_METRICS_TAG_HORIZONTAL_CLIPPING_ASCENT of type HarfBuzz.ot_metrics_tag_t>, 'HORIZONTAL_CLIPPING_DESCENT': <enum HB_OT_METRICS_TAG_HORIZONTAL_CLIPPING_DESCENT of type HarfBuzz.ot_metrics_tag_t>, 'VERTICAL_ASCENDER': <enum HB_OT_METRICS_TAG_VERTICAL_ASCENDER of type HarfBuzz.ot_metrics_tag_t>, 'VERTICAL_DESCENDER': <enum HB_OT_METRICS_TAG_VERTICAL_DESCENDER of type HarfBuzz.ot_metrics_tag_t>, 'VERTICAL_LINE_GAP': <enum HB_OT_METRICS_TAG_VERTICAL_LINE_GAP of type HarfBuzz.ot_metrics_tag_t>, 'HORIZONTAL_CARET_RISE': <enum HB_OT_METRICS_TAG_HORIZONTAL_CARET_RISE of type HarfBuzz.ot_metrics_tag_t>, 'HORIZONTAL_CARET_RUN': <enum HB_OT_METRICS_TAG_HORIZONTAL_CARET_RUN of type HarfBuzz.ot_metrics_tag_t>, 'HORIZONTAL_CARET_OFFSET': <enum HB_OT_METRICS_TAG_HORIZONTAL_CARET_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 'VERTICAL_CARET_RISE': <enum HB_OT_METRICS_TAG_VERTICAL_CARET_RISE of type HarfBuzz.ot_metrics_tag_t>, 'VERTICAL_CARET_RUN': <enum HB_OT_METRICS_TAG_VERTICAL_CARET_RUN of type HarfBuzz.ot_metrics_tag_t>, 'VERTICAL_CARET_OFFSET': <enum HB_OT_METRICS_TAG_VERTICAL_CARET_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 'X_HEIGHT': <enum HB_OT_METRICS_TAG_X_HEIGHT of type HarfBuzz.ot_metrics_tag_t>, 'CAP_HEIGHT': <enum HB_OT_METRICS_TAG_CAP_HEIGHT of type HarfBuzz.ot_metrics_tag_t>, 'SUBSCRIPT_EM_X_SIZE': <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_X_SIZE of type HarfBuzz.ot_metrics_tag_t>, 'SUBSCRIPT_EM_Y_SIZE': <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_Y_SIZE of type HarfBuzz.ot_metrics_tag_t>, 'SUBSCRIPT_EM_X_OFFSET': <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_X_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 'SUBSCRIPT_EM_Y_OFFSET': <enum HB_OT_METRICS_TAG_SUBSCRIPT_EM_Y_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 'SUPERSCRIPT_EM_X_SIZE': <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_X_SIZE of type HarfBuzz.ot_metrics_tag_t>, 'SUPERSCRIPT_EM_Y_SIZE': <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_SIZE of type HarfBuzz.ot_metrics_tag_t>, 'SUPERSCRIPT_EM_X_OFFSET': <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_X_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 'SUPERSCRIPT_EM_Y_OFFSET': <enum HB_OT_METRICS_TAG_SUPERSCRIPT_EM_Y_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 'STRIKEOUT_SIZE': <enum HB_OT_METRICS_TAG_STRIKEOUT_SIZE of type HarfBuzz.ot_metrics_tag_t>, 'STRIKEOUT_OFFSET': <enum HB_OT_METRICS_TAG_STRIKEOUT_OFFSET of type HarfBuzz.ot_metrics_tag_t>, 'UNDERLINE_SIZE': <enum HB_OT_METRICS_TAG_UNDERLINE_SIZE of type HarfBuzz.ot_metrics_tag_t>, 'UNDERLINE_OFFSET': <enum HB_OT_METRICS_TAG_UNDERLINE_OFFSET of type HarfBuzz.ot_metrics_tag_t>})"
    __enum_values__ = {
        1668311156: 1668311156,
        1751216995: 1751216995,
        1751346273: 1751346273,
        1751346276: 1751346276,
        1751347046: 1751347046,
        1751347822: 1751347822,
        1751347827: 1751347827,
        1751413603: 1751413603,
        1751934832: 1751934832,
        1935833199: 1935833199,
        1935833203: 1935833203,
        1935833455: 1935833455,
        1935833459: 1935833459,
        1936750703: 1936750703,
        1936750707: 1936750707,
        1936750959: 1936750959,
        1936750963: 1936750963,
        1937011311: 1937011311,
        1937011315: 1937011315,
        1970168943: 1970168943,
        1970168947: 1970168947,
        1986098019: 1986098019,
        1986228070: 1986228070,
        1986228846: 1986228846,
        1986228851: 1986228851,
        1986294627: 1986294627,
        1986815856: 1986815856,
        2020108148: 2020108148,
    }
    __gtype__ = None # (!) real value is '<GType hb_ot_metrics_tag_t (94618627285888)>'
    __info__ = gi.EnumInfo(ot_metrics_tag_t)


