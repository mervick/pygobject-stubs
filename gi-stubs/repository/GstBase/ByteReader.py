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


class ByteReader(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ByteReader()
    """
    def dup_data(self): # real signature unknown; restored from __doc__
        """ dup_data(self) -> bool, val:list """
        return False

    def dup_string_utf16(self): # real signature unknown; restored from __doc__
        """ dup_string_utf16(self) -> bool, str:list """
        return False

    def dup_string_utf32(self): # real signature unknown; restored from __doc__
        """ dup_string_utf32(self) -> bool, str:list """
        return False

    def dup_string_utf8(self): # real signature unknown; restored from __doc__
        """ dup_string_utf8(self) -> bool, str:list """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> bool, val:list """
        return False

    def get_float32_be(self): # real signature unknown; restored from __doc__
        """ get_float32_be(self) -> bool, val:float """
        return False

    def get_float32_le(self): # real signature unknown; restored from __doc__
        """ get_float32_le(self) -> bool, val:float """
        return False

    def get_float64_be(self): # real signature unknown; restored from __doc__
        """ get_float64_be(self) -> bool, val:float """
        return False

    def get_float64_le(self): # real signature unknown; restored from __doc__
        """ get_float64_le(self) -> bool, val:float """
        return False

    def get_int16_be(self): # real signature unknown; restored from __doc__
        """ get_int16_be(self) -> bool, val:int """
        return False

    def get_int16_le(self): # real signature unknown; restored from __doc__
        """ get_int16_le(self) -> bool, val:int """
        return False

    def get_int24_be(self): # real signature unknown; restored from __doc__
        """ get_int24_be(self) -> bool, val:int """
        return False

    def get_int24_le(self): # real signature unknown; restored from __doc__
        """ get_int24_le(self) -> bool, val:int """
        return False

    def get_int32_be(self): # real signature unknown; restored from __doc__
        """ get_int32_be(self) -> bool, val:int """
        return False

    def get_int32_le(self): # real signature unknown; restored from __doc__
        """ get_int32_le(self) -> bool, val:int """
        return False

    def get_int64_be(self): # real signature unknown; restored from __doc__
        """ get_int64_be(self) -> bool, val:int """
        return False

    def get_int64_le(self): # real signature unknown; restored from __doc__
        """ get_int64_le(self) -> bool, val:int """
        return False

    def get_int8(self): # real signature unknown; restored from __doc__
        """ get_int8(self) -> bool, val:int """
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

    def get_string_utf8(self): # real signature unknown; restored from __doc__
        """ get_string_utf8(self) -> bool, str:list """
        return False

    def get_uint16_be(self): # real signature unknown; restored from __doc__
        """ get_uint16_be(self) -> bool, val:int """
        return False

    def get_uint16_le(self): # real signature unknown; restored from __doc__
        """ get_uint16_le(self) -> bool, val:int """
        return False

    def get_uint24_be(self): # real signature unknown; restored from __doc__
        """ get_uint24_be(self) -> bool, val:int """
        return False

    def get_uint24_le(self): # real signature unknown; restored from __doc__
        """ get_uint24_le(self) -> bool, val:int """
        return False

    def get_uint32_be(self): # real signature unknown; restored from __doc__
        """ get_uint32_be(self) -> bool, val:int """
        return False

    def get_uint32_le(self): # real signature unknown; restored from __doc__
        """ get_uint32_le(self) -> bool, val:int """
        return False

    def get_uint64_be(self): # real signature unknown; restored from __doc__
        """ get_uint64_be(self) -> bool, val:int """
        return False

    def get_uint64_le(self): # real signature unknown; restored from __doc__
        """ get_uint64_le(self) -> bool, val:int """
        return False

    def get_uint8(self): # real signature unknown; restored from __doc__
        """ get_uint8(self) -> bool, val:int """
        return False

    def init(self, data): # real signature unknown; restored from __doc__
        """ init(self, data:list) """
        pass

    def masked_scan_uint32(self, mask, pattern, offset, size): # real signature unknown; restored from __doc__
        """ masked_scan_uint32(self, mask:int, pattern:int, offset:int, size:int) -> int """
        return 0

    def masked_scan_uint32_peek(self, mask, pattern, offset, size): # real signature unknown; restored from __doc__
        """ masked_scan_uint32_peek(self, mask:int, pattern:int, offset:int, size:int) -> int, value:int """
        return 0

    def peek_data(self): # real signature unknown; restored from __doc__
        """ peek_data(self) -> bool, val:list """
        return False

    def peek_float32_be(self): # real signature unknown; restored from __doc__
        """ peek_float32_be(self) -> bool, val:float """
        return False

    def peek_float32_le(self): # real signature unknown; restored from __doc__
        """ peek_float32_le(self) -> bool, val:float """
        return False

    def peek_float64_be(self): # real signature unknown; restored from __doc__
        """ peek_float64_be(self) -> bool, val:float """
        return False

    def peek_float64_le(self): # real signature unknown; restored from __doc__
        """ peek_float64_le(self) -> bool, val:float """
        return False

    def peek_int16_be(self): # real signature unknown; restored from __doc__
        """ peek_int16_be(self) -> bool, val:int """
        return False

    def peek_int16_le(self): # real signature unknown; restored from __doc__
        """ peek_int16_le(self) -> bool, val:int """
        return False

    def peek_int24_be(self): # real signature unknown; restored from __doc__
        """ peek_int24_be(self) -> bool, val:int """
        return False

    def peek_int24_le(self): # real signature unknown; restored from __doc__
        """ peek_int24_le(self) -> bool, val:int """
        return False

    def peek_int32_be(self): # real signature unknown; restored from __doc__
        """ peek_int32_be(self) -> bool, val:int """
        return False

    def peek_int32_le(self): # real signature unknown; restored from __doc__
        """ peek_int32_le(self) -> bool, val:int """
        return False

    def peek_int64_be(self): # real signature unknown; restored from __doc__
        """ peek_int64_be(self) -> bool, val:int """
        return False

    def peek_int64_le(self): # real signature unknown; restored from __doc__
        """ peek_int64_le(self) -> bool, val:int """
        return False

    def peek_int8(self): # real signature unknown; restored from __doc__
        """ peek_int8(self) -> bool, val:int """
        return False

    def peek_string_utf8(self): # real signature unknown; restored from __doc__
        """ peek_string_utf8(self) -> bool, str:list """
        return False

    def peek_uint16_be(self): # real signature unknown; restored from __doc__
        """ peek_uint16_be(self) -> bool, val:int """
        return False

    def peek_uint16_le(self): # real signature unknown; restored from __doc__
        """ peek_uint16_le(self) -> bool, val:int """
        return False

    def peek_uint24_be(self): # real signature unknown; restored from __doc__
        """ peek_uint24_be(self) -> bool, val:int """
        return False

    def peek_uint24_le(self): # real signature unknown; restored from __doc__
        """ peek_uint24_le(self) -> bool, val:int """
        return False

    def peek_uint32_be(self): # real signature unknown; restored from __doc__
        """ peek_uint32_be(self) -> bool, val:int """
        return False

    def peek_uint32_le(self): # real signature unknown; restored from __doc__
        """ peek_uint32_le(self) -> bool, val:int """
        return False

    def peek_uint64_be(self): # real signature unknown; restored from __doc__
        """ peek_uint64_be(self) -> bool, val:int """
        return False

    def peek_uint64_le(self): # real signature unknown; restored from __doc__
        """ peek_uint64_le(self) -> bool, val:int """
        return False

    def peek_uint8(self): # real signature unknown; restored from __doc__
        """ peek_uint8(self) -> bool, val:int """
        return False

    def set_pos(self, pos): # real signature unknown; restored from __doc__
        """ set_pos(self, pos:int) -> bool """
        return False

    def skip(self, nbytes): # real signature unknown; restored from __doc__
        """ skip(self, nbytes:int) -> bool """
        return False

    def skip_string_utf16(self): # real signature unknown; restored from __doc__
        """ skip_string_utf16(self) -> bool """
        return False

    def skip_string_utf32(self): # real signature unknown; restored from __doc__
        """ skip_string_utf32(self) -> bool """
        return False

    def skip_string_utf8(self): # real signature unknown; restored from __doc__
        """ skip_string_utf8(self) -> bool """
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

    byte = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ByteReader), '__module__': 'gi.repository.GstBase', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ByteReader' objects>, '__weakref__': <attribute '__weakref__' of 'ByteReader' objects>, '__doc__': None, 'data': <property object at 0x7f9fb7bcbbd0>, 'size': <property object at 0x7f9fb7bcbcc0>, 'byte': <property object at 0x7f9fb7bcbdb0>, '_gst_reserved': <property object at 0x7f9fb7bcbea0>, 'dup_data': gi.FunctionInfo(dup_data), 'dup_string_utf16': gi.FunctionInfo(dup_string_utf16), 'dup_string_utf32': gi.FunctionInfo(dup_string_utf32), 'dup_string_utf8': gi.FunctionInfo(dup_string_utf8), 'free': gi.FunctionInfo(free), 'get_data': gi.FunctionInfo(get_data), 'get_float32_be': gi.FunctionInfo(get_float32_be), 'get_float32_le': gi.FunctionInfo(get_float32_le), 'get_float64_be': gi.FunctionInfo(get_float64_be), 'get_float64_le': gi.FunctionInfo(get_float64_le), 'get_int16_be': gi.FunctionInfo(get_int16_be), 'get_int16_le': gi.FunctionInfo(get_int16_le), 'get_int24_be': gi.FunctionInfo(get_int24_be), 'get_int24_le': gi.FunctionInfo(get_int24_le), 'get_int32_be': gi.FunctionInfo(get_int32_be), 'get_int32_le': gi.FunctionInfo(get_int32_le), 'get_int64_be': gi.FunctionInfo(get_int64_be), 'get_int64_le': gi.FunctionInfo(get_int64_le), 'get_int8': gi.FunctionInfo(get_int8), 'get_pos': gi.FunctionInfo(get_pos), 'get_remaining': gi.FunctionInfo(get_remaining), 'get_size': gi.FunctionInfo(get_size), 'get_string_utf8': gi.FunctionInfo(get_string_utf8), 'get_uint16_be': gi.FunctionInfo(get_uint16_be), 'get_uint16_le': gi.FunctionInfo(get_uint16_le), 'get_uint24_be': gi.FunctionInfo(get_uint24_be), 'get_uint24_le': gi.FunctionInfo(get_uint24_le), 'get_uint32_be': gi.FunctionInfo(get_uint32_be), 'get_uint32_le': gi.FunctionInfo(get_uint32_le), 'get_uint64_be': gi.FunctionInfo(get_uint64_be), 'get_uint64_le': gi.FunctionInfo(get_uint64_le), 'get_uint8': gi.FunctionInfo(get_uint8), 'init': gi.FunctionInfo(init), 'masked_scan_uint32': gi.FunctionInfo(masked_scan_uint32), 'masked_scan_uint32_peek': gi.FunctionInfo(masked_scan_uint32_peek), 'peek_data': gi.FunctionInfo(peek_data), 'peek_float32_be': gi.FunctionInfo(peek_float32_be), 'peek_float32_le': gi.FunctionInfo(peek_float32_le), 'peek_float64_be': gi.FunctionInfo(peek_float64_be), 'peek_float64_le': gi.FunctionInfo(peek_float64_le), 'peek_int16_be': gi.FunctionInfo(peek_int16_be), 'peek_int16_le': gi.FunctionInfo(peek_int16_le), 'peek_int24_be': gi.FunctionInfo(peek_int24_be), 'peek_int24_le': gi.FunctionInfo(peek_int24_le), 'peek_int32_be': gi.FunctionInfo(peek_int32_be), 'peek_int32_le': gi.FunctionInfo(peek_int32_le), 'peek_int64_be': gi.FunctionInfo(peek_int64_be), 'peek_int64_le': gi.FunctionInfo(peek_int64_le), 'peek_int8': gi.FunctionInfo(peek_int8), 'peek_string_utf8': gi.FunctionInfo(peek_string_utf8), 'peek_uint16_be': gi.FunctionInfo(peek_uint16_be), 'peek_uint16_le': gi.FunctionInfo(peek_uint16_le), 'peek_uint24_be': gi.FunctionInfo(peek_uint24_be), 'peek_uint24_le': gi.FunctionInfo(peek_uint24_le), 'peek_uint32_be': gi.FunctionInfo(peek_uint32_be), 'peek_uint32_le': gi.FunctionInfo(peek_uint32_le), 'peek_uint64_be': gi.FunctionInfo(peek_uint64_be), 'peek_uint64_le': gi.FunctionInfo(peek_uint64_le), 'peek_uint8': gi.FunctionInfo(peek_uint8), 'set_pos': gi.FunctionInfo(set_pos), 'skip': gi.FunctionInfo(skip), 'skip_string_utf16': gi.FunctionInfo(skip_string_utf16), 'skip_string_utf32': gi.FunctionInfo(skip_string_utf32), 'skip_string_utf8': gi.FunctionInfo(skip_string_utf8)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ByteReader)


