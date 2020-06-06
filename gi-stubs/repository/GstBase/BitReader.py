# encoding: utf-8
# module gi.repository.GstBase
# from /usr/lib64/girepository-1.0/GstBase-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gobject as __gobject


class BitReader(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BitReader()
    """
    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_bits_uint16(self, nbits): # real signature unknown; restored from __doc__
        """ get_bits_uint16(self, nbits:int) -> bool, val:int """
        return False

    def get_bits_uint32(self, nbits): # real signature unknown; restored from __doc__
        """ get_bits_uint32(self, nbits:int) -> bool, val:int """
        return False

    def get_bits_uint64(self, nbits): # real signature unknown; restored from __doc__
        """ get_bits_uint64(self, nbits:int) -> bool, val:int """
        return False

    def get_bits_uint8(self, nbits): # real signature unknown; restored from __doc__
        """ get_bits_uint8(self, nbits:int) -> bool, val:int """
        return False

    def get_pos(self): # real signature unknown; restored from __doc__
        """ get_pos(self) -> int """
        return 0

    def get_remaining(self): # real signature unknown; restored from __doc__
        """ get_remaining(self) -> int """
        return 0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def init(self, data): # real signature unknown; restored from __doc__
        """ init(self, data:list) """
        pass

    def peek_bits_uint16(self, nbits): # real signature unknown; restored from __doc__
        """ peek_bits_uint16(self, nbits:int) -> bool, val:int """
        return False

    def peek_bits_uint32(self, nbits): # real signature unknown; restored from __doc__
        """ peek_bits_uint32(self, nbits:int) -> bool, val:int """
        return False

    def peek_bits_uint64(self, nbits): # real signature unknown; restored from __doc__
        """ peek_bits_uint64(self, nbits:int) -> bool, val:int """
        return False

    def peek_bits_uint8(self, nbits): # real signature unknown; restored from __doc__
        """ peek_bits_uint8(self, nbits:int) -> bool, val:int """
        return False

    def set_pos(self, pos): # real signature unknown; restored from __doc__
        """ set_pos(self, pos:int) -> bool """
        return False

    def skip(self, nbits): # real signature unknown; restored from __doc__
        """ skip(self, nbits:int) -> bool """
        return False

    def skip_to_byte(self): # real signature unknown; restored from __doc__
        """ skip_to_byte(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    bit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    byte = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BitReader), '__module__': 'gi.repository.GstBase', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BitReader' objects>, '__weakref__': <attribute '__weakref__' of 'BitReader' objects>, '__doc__': None, 'data': <property object at 0x7f9fb7bcae00>, 'size': <property object at 0x7f9fb7bcaef0>, 'byte': <property object at 0x7f9fb7bcb040>, 'bit': <property object at 0x7f9fb7bcb130>, '_gst_reserved': <property object at 0x7f9fb7bcb220>, 'free': gi.FunctionInfo(free), 'get_bits_uint16': gi.FunctionInfo(get_bits_uint16), 'get_bits_uint32': gi.FunctionInfo(get_bits_uint32), 'get_bits_uint64': gi.FunctionInfo(get_bits_uint64), 'get_bits_uint8': gi.FunctionInfo(get_bits_uint8), 'get_pos': gi.FunctionInfo(get_pos), 'get_remaining': gi.FunctionInfo(get_remaining), 'get_size': gi.FunctionInfo(get_size), 'init': gi.FunctionInfo(init), 'peek_bits_uint16': gi.FunctionInfo(peek_bits_uint16), 'peek_bits_uint32': gi.FunctionInfo(peek_bits_uint32), 'peek_bits_uint64': gi.FunctionInfo(peek_bits_uint64), 'peek_bits_uint8': gi.FunctionInfo(peek_bits_uint8), 'set_pos': gi.FunctionInfo(set_pos), 'skip': gi.FunctionInfo(skip), 'skip_to_byte': gi.FunctionInfo(skip_to_byte)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BitReader)


