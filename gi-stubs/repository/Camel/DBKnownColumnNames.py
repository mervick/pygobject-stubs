# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class DBKnownColumnNames(__gobject.GEnum):
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


    ATTACHMENT = 0
    BDATA = 1
    CINFO = 2
    DELETED = 3
    DELETED_COUNT = 4
    DRECEIVED = 5
    DSENT = 6
    FLAGS = 7
    FOLDER_NAME = 8
    FOLLOWUP_COMPLETED_ON = 9
    FOLLOWUP_DUE_BY = 10
    FOLLOWUP_FLAG = 11
    IMPORTANT = 12
    JND_COUNT = 13
    JUNK = 14
    JUNK_COUNT = 15
    LABELS = 16
    MAIL_CC = 17
    MAIL_FROM = 18
    MAIL_TO = 19
    MLIST = 20
    NEXTUID = 21
    PART = 22
    READ = 23
    REPLIED = 24
    SAVED_COUNT = 25
    SIZE = 26
    SUBJECT = 27
    TIME = 28
    UID = 29
    UNKNOWN = -1
    UNREAD_COUNT = 30
    USERTAGS = 31
    VERSION = 32
    VISIBLE_COUNT = 33
    VUID = 34
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Camel', '__dict__': <attribute '__dict__' of 'DBKnownColumnNames' objects>, '__doc__': None, '__gtype__': <GType PyCamelDBKnownColumnNames (94124523596976)>, '__enum_values__': {-1: <enum CAMEL_DB_COLUMN_UNKNOWN of type Camel.DBKnownColumnNames>, 0: <enum CAMEL_DB_COLUMN_ATTACHMENT of type Camel.DBKnownColumnNames>, 1: <enum CAMEL_DB_COLUMN_BDATA of type Camel.DBKnownColumnNames>, 2: <enum CAMEL_DB_COLUMN_CINFO of type Camel.DBKnownColumnNames>, 3: <enum CAMEL_DB_COLUMN_DELETED of type Camel.DBKnownColumnNames>, 4: <enum CAMEL_DB_COLUMN_DELETED_COUNT of type Camel.DBKnownColumnNames>, 5: <enum CAMEL_DB_COLUMN_DRECEIVED of type Camel.DBKnownColumnNames>, 6: <enum CAMEL_DB_COLUMN_DSENT of type Camel.DBKnownColumnNames>, 7: <enum CAMEL_DB_COLUMN_FLAGS of type Camel.DBKnownColumnNames>, 8: <enum CAMEL_DB_COLUMN_FOLDER_NAME of type Camel.DBKnownColumnNames>, 9: <enum CAMEL_DB_COLUMN_FOLLOWUP_COMPLETED_ON of type Camel.DBKnownColumnNames>, 10: <enum CAMEL_DB_COLUMN_FOLLOWUP_DUE_BY of type Camel.DBKnownColumnNames>, 11: <enum CAMEL_DB_COLUMN_FOLLOWUP_FLAG of type Camel.DBKnownColumnNames>, 12: <enum CAMEL_DB_COLUMN_IMPORTANT of type Camel.DBKnownColumnNames>, 13: <enum CAMEL_DB_COLUMN_JND_COUNT of type Camel.DBKnownColumnNames>, 14: <enum CAMEL_DB_COLUMN_JUNK of type Camel.DBKnownColumnNames>, 15: <enum CAMEL_DB_COLUMN_JUNK_COUNT of type Camel.DBKnownColumnNames>, 16: <enum CAMEL_DB_COLUMN_LABELS of type Camel.DBKnownColumnNames>, 17: <enum CAMEL_DB_COLUMN_MAIL_CC of type Camel.DBKnownColumnNames>, 18: <enum CAMEL_DB_COLUMN_MAIL_FROM of type Camel.DBKnownColumnNames>, 19: <enum CAMEL_DB_COLUMN_MAIL_TO of type Camel.DBKnownColumnNames>, 20: <enum CAMEL_DB_COLUMN_MLIST of type Camel.DBKnownColumnNames>, 21: <enum CAMEL_DB_COLUMN_NEXTUID of type Camel.DBKnownColumnNames>, 22: <enum CAMEL_DB_COLUMN_PART of type Camel.DBKnownColumnNames>, 23: <enum CAMEL_DB_COLUMN_READ of type Camel.DBKnownColumnNames>, 24: <enum CAMEL_DB_COLUMN_REPLIED of type Camel.DBKnownColumnNames>, 25: <enum CAMEL_DB_COLUMN_SAVED_COUNT of type Camel.DBKnownColumnNames>, 26: <enum CAMEL_DB_COLUMN_SIZE of type Camel.DBKnownColumnNames>, 27: <enum CAMEL_DB_COLUMN_SUBJECT of type Camel.DBKnownColumnNames>, 28: <enum CAMEL_DB_COLUMN_TIME of type Camel.DBKnownColumnNames>, 29: <enum CAMEL_DB_COLUMN_UID of type Camel.DBKnownColumnNames>, 30: <enum CAMEL_DB_COLUMN_UNREAD_COUNT of type Camel.DBKnownColumnNames>, 31: <enum CAMEL_DB_COLUMN_USERTAGS of type Camel.DBKnownColumnNames>, 32: <enum CAMEL_DB_COLUMN_VERSION of type Camel.DBKnownColumnNames>, 33: <enum CAMEL_DB_COLUMN_VISIBLE_COUNT of type Camel.DBKnownColumnNames>, 34: <enum CAMEL_DB_COLUMN_VUID of type Camel.DBKnownColumnNames>}, '__info__': gi.EnumInfo(DBKnownColumnNames), 'UNKNOWN': <enum CAMEL_DB_COLUMN_UNKNOWN of type Camel.DBKnownColumnNames>, 'ATTACHMENT': <enum CAMEL_DB_COLUMN_ATTACHMENT of type Camel.DBKnownColumnNames>, 'BDATA': <enum CAMEL_DB_COLUMN_BDATA of type Camel.DBKnownColumnNames>, 'CINFO': <enum CAMEL_DB_COLUMN_CINFO of type Camel.DBKnownColumnNames>, 'DELETED': <enum CAMEL_DB_COLUMN_DELETED of type Camel.DBKnownColumnNames>, 'DELETED_COUNT': <enum CAMEL_DB_COLUMN_DELETED_COUNT of type Camel.DBKnownColumnNames>, 'DRECEIVED': <enum CAMEL_DB_COLUMN_DRECEIVED of type Camel.DBKnownColumnNames>, 'DSENT': <enum CAMEL_DB_COLUMN_DSENT of type Camel.DBKnownColumnNames>, 'FLAGS': <enum CAMEL_DB_COLUMN_FLAGS of type Camel.DBKnownColumnNames>, 'FOLDER_NAME': <enum CAMEL_DB_COLUMN_FOLDER_NAME of type Camel.DBKnownColumnNames>, 'FOLLOWUP_COMPLETED_ON': <enum CAMEL_DB_COLUMN_FOLLOWUP_COMPLETED_ON of type Camel.DBKnownColumnNames>, 'FOLLOWUP_DUE_BY': <enum CAMEL_DB_COLUMN_FOLLOWUP_DUE_BY of type Camel.DBKnownColumnNames>, 'FOLLOWUP_FLAG': <enum CAMEL_DB_COLUMN_FOLLOWUP_FLAG of type Camel.DBKnownColumnNames>, 'IMPORTANT': <enum CAMEL_DB_COLUMN_IMPORTANT of type Camel.DBKnownColumnNames>, 'JND_COUNT': <enum CAMEL_DB_COLUMN_JND_COUNT of type Camel.DBKnownColumnNames>, 'JUNK': <enum CAMEL_DB_COLUMN_JUNK of type Camel.DBKnownColumnNames>, 'JUNK_COUNT': <enum CAMEL_DB_COLUMN_JUNK_COUNT of type Camel.DBKnownColumnNames>, 'LABELS': <enum CAMEL_DB_COLUMN_LABELS of type Camel.DBKnownColumnNames>, 'MAIL_CC': <enum CAMEL_DB_COLUMN_MAIL_CC of type Camel.DBKnownColumnNames>, 'MAIL_FROM': <enum CAMEL_DB_COLUMN_MAIL_FROM of type Camel.DBKnownColumnNames>, 'MAIL_TO': <enum CAMEL_DB_COLUMN_MAIL_TO of type Camel.DBKnownColumnNames>, 'MLIST': <enum CAMEL_DB_COLUMN_MLIST of type Camel.DBKnownColumnNames>, 'NEXTUID': <enum CAMEL_DB_COLUMN_NEXTUID of type Camel.DBKnownColumnNames>, 'PART': <enum CAMEL_DB_COLUMN_PART of type Camel.DBKnownColumnNames>, 'READ': <enum CAMEL_DB_COLUMN_READ of type Camel.DBKnownColumnNames>, 'REPLIED': <enum CAMEL_DB_COLUMN_REPLIED of type Camel.DBKnownColumnNames>, 'SAVED_COUNT': <enum CAMEL_DB_COLUMN_SAVED_COUNT of type Camel.DBKnownColumnNames>, 'SIZE': <enum CAMEL_DB_COLUMN_SIZE of type Camel.DBKnownColumnNames>, 'SUBJECT': <enum CAMEL_DB_COLUMN_SUBJECT of type Camel.DBKnownColumnNames>, 'TIME': <enum CAMEL_DB_COLUMN_TIME of type Camel.DBKnownColumnNames>, 'UID': <enum CAMEL_DB_COLUMN_UID of type Camel.DBKnownColumnNames>, 'UNREAD_COUNT': <enum CAMEL_DB_COLUMN_UNREAD_COUNT of type Camel.DBKnownColumnNames>, 'USERTAGS': <enum CAMEL_DB_COLUMN_USERTAGS of type Camel.DBKnownColumnNames>, 'VERSION': <enum CAMEL_DB_COLUMN_VERSION of type Camel.DBKnownColumnNames>, 'VISIBLE_COUNT': <enum CAMEL_DB_COLUMN_VISIBLE_COUNT of type Camel.DBKnownColumnNames>, 'VUID': <enum CAMEL_DB_COLUMN_VUID of type Camel.DBKnownColumnNames>})"
    __enum_values__ = {
        -1: -1,
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
    }
    __gtype__ = None # (!) real value is '<GType PyCamelDBKnownColumnNames (94124523596976)>'
    __info__ = gi.EnumInfo(DBKnownColumnNames)


