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


class StoreInfoFlags(__gobject.GFlags):
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
        """ Helper for pickle. """
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

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CHILDREN = 4
    FLAGGED = 262144
    NOCHILDREN = 8
    NOINFERIORS = 2
    NOSELECT = 1
    READONLY = 65536
    SHARED_BY_ME = 512
    SHARED_TO_ME = 256
    SUBSCRIBED = 16
    SYSTEM = 64
    TYPE_ALL = 10240
    TYPE_ARCHIVE = 11264
    TYPE_CONTACTS = 6144
    TYPE_DRAFTS = 12288
    TYPE_EVENTS = 7168
    TYPE_INBOX = 1024
    TYPE_JUNK = 4096
    TYPE_MEMOS = 8192
    TYPE_NORMAL = 0
    TYPE_OUTBOX = 2048
    TYPE_SENT = 5120
    TYPE_TASKS = 9216
    TYPE_TRASH = 3072
    VIRTUAL = 32
    VTRASH = 128
    WRITEONLY = 131072
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Camel', '__dict__': <attribute '__dict__' of 'StoreInfoFlags' objects>, '__doc__': None, '__gtype__': <GType CamelStoreInfoFlags (94124523628208)>, '__flags_values__': {1: <flags CAMEL_STORE_INFO_FOLDER_NOSELECT of type Camel.StoreInfoFlags>, 2: <flags CAMEL_STORE_INFO_FOLDER_NOINFERIORS of type Camel.StoreInfoFlags>, 4: <flags CAMEL_STORE_INFO_FOLDER_CHILDREN of type Camel.StoreInfoFlags>, 8: <flags CAMEL_STORE_INFO_FOLDER_NOCHILDREN of type Camel.StoreInfoFlags>, 16: <flags CAMEL_STORE_INFO_FOLDER_SUBSCRIBED of type Camel.StoreInfoFlags>, 32: <flags CAMEL_STORE_INFO_FOLDER_VIRTUAL of type Camel.StoreInfoFlags>, 64: <flags CAMEL_STORE_INFO_FOLDER_SYSTEM of type Camel.StoreInfoFlags>, 128: <flags CAMEL_STORE_INFO_FOLDER_VTRASH of type Camel.StoreInfoFlags>, 256: <flags CAMEL_STORE_INFO_FOLDER_SHARED_TO_ME of type Camel.StoreInfoFlags>, 512: <flags CAMEL_STORE_INFO_FOLDER_SHARED_BY_ME of type Camel.StoreInfoFlags>, 0: <flags 0 of type Camel.StoreInfoFlags>, 1024: <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX of type Camel.StoreInfoFlags>, 2048: <flags CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX of type Camel.StoreInfoFlags>, 3072: <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_TRASH of type Camel.StoreInfoFlags>, 4096: <flags CAMEL_STORE_INFO_FOLDER_TYPE_JUNK of type Camel.StoreInfoFlags>, 5120: <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_SENT of type Camel.StoreInfoFlags>, 6144: <flags CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_CONTACTS of type Camel.StoreInfoFlags>, 7168: <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_TRASH | CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_SENT | CAMEL_STORE_INFO_FOLDER_TYPE_CONTACTS | CAMEL_STORE_INFO_FOLDER_TYPE_EVENTS of type Camel.StoreInfoFlags>, 8192: <flags CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS of type Camel.StoreInfoFlags>, 9216: <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_TASKS of type Camel.StoreInfoFlags>, 10240: <flags CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_ALL of type Camel.StoreInfoFlags>, 11264: <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_TRASH | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_TASKS | CAMEL_STORE_INFO_FOLDER_TYPE_ALL | CAMEL_STORE_INFO_FOLDER_TYPE_ARCHIVE of type Camel.StoreInfoFlags>, 12288: <flags CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_DRAFTS of type Camel.StoreInfoFlags>, 65536: <flags CAMEL_STORE_INFO_FOLDER_READONLY of type Camel.StoreInfoFlags>, 131072: <flags CAMEL_STORE_INFO_FOLDER_WRITEONLY of type Camel.StoreInfoFlags>, 262144: <flags CAMEL_STORE_INFO_FOLDER_FLAGGED of type Camel.StoreInfoFlags>}, '__info__': gi.EnumInfo(StoreInfoFlags), 'NOSELECT': <flags CAMEL_STORE_INFO_FOLDER_NOSELECT of type Camel.StoreInfoFlags>, 'NOINFERIORS': <flags CAMEL_STORE_INFO_FOLDER_NOINFERIORS of type Camel.StoreInfoFlags>, 'CHILDREN': <flags CAMEL_STORE_INFO_FOLDER_CHILDREN of type Camel.StoreInfoFlags>, 'NOCHILDREN': <flags CAMEL_STORE_INFO_FOLDER_NOCHILDREN of type Camel.StoreInfoFlags>, 'SUBSCRIBED': <flags CAMEL_STORE_INFO_FOLDER_SUBSCRIBED of type Camel.StoreInfoFlags>, 'VIRTUAL': <flags CAMEL_STORE_INFO_FOLDER_VIRTUAL of type Camel.StoreInfoFlags>, 'SYSTEM': <flags CAMEL_STORE_INFO_FOLDER_SYSTEM of type Camel.StoreInfoFlags>, 'VTRASH': <flags CAMEL_STORE_INFO_FOLDER_VTRASH of type Camel.StoreInfoFlags>, 'SHARED_TO_ME': <flags CAMEL_STORE_INFO_FOLDER_SHARED_TO_ME of type Camel.StoreInfoFlags>, 'SHARED_BY_ME': <flags CAMEL_STORE_INFO_FOLDER_SHARED_BY_ME of type Camel.StoreInfoFlags>, 'TYPE_NORMAL': <flags 0 of type Camel.StoreInfoFlags>, 'TYPE_INBOX': <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX of type Camel.StoreInfoFlags>, 'TYPE_OUTBOX': <flags CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX of type Camel.StoreInfoFlags>, 'TYPE_TRASH': <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_TRASH of type Camel.StoreInfoFlags>, 'TYPE_JUNK': <flags CAMEL_STORE_INFO_FOLDER_TYPE_JUNK of type Camel.StoreInfoFlags>, 'TYPE_SENT': <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_SENT of type Camel.StoreInfoFlags>, 'TYPE_CONTACTS': <flags CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_CONTACTS of type Camel.StoreInfoFlags>, 'TYPE_EVENTS': <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_TRASH | CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_SENT | CAMEL_STORE_INFO_FOLDER_TYPE_CONTACTS | CAMEL_STORE_INFO_FOLDER_TYPE_EVENTS of type Camel.StoreInfoFlags>, 'TYPE_MEMOS': <flags CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS of type Camel.StoreInfoFlags>, 'TYPE_TASKS': <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_TASKS of type Camel.StoreInfoFlags>, 'TYPE_ALL': <flags CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_ALL of type Camel.StoreInfoFlags>, 'TYPE_ARCHIVE': <flags CAMEL_STORE_INFO_FOLDER_TYPE_INBOX | CAMEL_STORE_INFO_FOLDER_TYPE_OUTBOX | CAMEL_STORE_INFO_FOLDER_TYPE_TRASH | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_TASKS | CAMEL_STORE_INFO_FOLDER_TYPE_ALL | CAMEL_STORE_INFO_FOLDER_TYPE_ARCHIVE of type Camel.StoreInfoFlags>, 'TYPE_DRAFTS': <flags CAMEL_STORE_INFO_FOLDER_TYPE_JUNK | CAMEL_STORE_INFO_FOLDER_TYPE_MEMOS | CAMEL_STORE_INFO_FOLDER_TYPE_DRAFTS of type Camel.StoreInfoFlags>, 'READONLY': <flags CAMEL_STORE_INFO_FOLDER_READONLY of type Camel.StoreInfoFlags>, 'WRITEONLY': <flags CAMEL_STORE_INFO_FOLDER_WRITEONLY of type Camel.StoreInfoFlags>, 'FLAGGED': <flags CAMEL_STORE_INFO_FOLDER_FLAGGED of type Camel.StoreInfoFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        128: 128,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        3072: 3072,
        4096: 4096,
        5120: 5120,
        6144: 6144,
        7168: 7168,
        8192: 8192,
        9216: 9216,
        10240: 10240,
        11264: 11264,
        12288: 12288,
        65536: 65536,
        131072: 131072,
        262144: 262144,
    }
    __gtype__ = None # (!) real value is '<GType CamelStoreInfoFlags (94124523628208)>'
    __info__ = gi.EnumInfo(StoreInfoFlags)


