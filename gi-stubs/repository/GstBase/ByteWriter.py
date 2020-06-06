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


class ByteWriter(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ByteWriter()
    """
    def ensure_free_space(self, size): # real signature unknown; restored from __doc__
        """ ensure_free_space(self, size:int) -> bool """
        return False

    def fill(self, value, size): # real signature unknown; restored from __doc__
        """ fill(self, value:int, size:int) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def free_and_get_buffer(self): # real signature unknown; restored from __doc__
        """ free_and_get_buffer(self) -> Gst.Buffer """
        pass

    def free_and_get_data(self): # real signature unknown; restored from __doc__
        """ free_and_get_data(self) -> int """
        return 0

    def get_remaining(self): # real signature unknown; restored from __doc__
        """ get_remaining(self) -> int """
        return 0

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def init_with_data(self, data, initialized): # real signature unknown; restored from __doc__
        """ init_with_data(self, data:list, initialized:bool) """
        pass

    def init_with_size(self, size, fixed): # real signature unknown; restored from __doc__
        """ init_with_size(self, size:int, fixed:bool) """
        pass

    def put_buffer(self, buffer, offset, size): # real signature unknown; restored from __doc__
        """ put_buffer(self, buffer:Gst.Buffer, offset:int, size:int) -> bool """
        return False

    def put_data(self, data): # real signature unknown; restored from __doc__
        """ put_data(self, data:list) -> bool """
        return False

    def put_float32_be(self, val): # real signature unknown; restored from __doc__
        """ put_float32_be(self, val:float) -> bool """
        return False

    def put_float32_le(self, val): # real signature unknown; restored from __doc__
        """ put_float32_le(self, val:float) -> bool """
        return False

    def put_float64_be(self, val): # real signature unknown; restored from __doc__
        """ put_float64_be(self, val:float) -> bool """
        return False

    def put_float64_le(self, val): # real signature unknown; restored from __doc__
        """ put_float64_le(self, val:float) -> bool """
        return False

    def put_int16_be(self, val): # real signature unknown; restored from __doc__
        """ put_int16_be(self, val:int) -> bool """
        return False

    def put_int16_le(self, val): # real signature unknown; restored from __doc__
        """ put_int16_le(self, val:int) -> bool """
        return False

    def put_int24_be(self, val): # real signature unknown; restored from __doc__
        """ put_int24_be(self, val:int) -> bool """
        return False

    def put_int24_le(self, val): # real signature unknown; restored from __doc__
        """ put_int24_le(self, val:int) -> bool """
        return False

    def put_int32_be(self, val): # real signature unknown; restored from __doc__
        """ put_int32_be(self, val:int) -> bool """
        return False

    def put_int32_le(self, val): # real signature unknown; restored from __doc__
        """ put_int32_le(self, val:int) -> bool """
        return False

    def put_int64_be(self, val): # real signature unknown; restored from __doc__
        """ put_int64_be(self, val:int) -> bool """
        return False

    def put_int64_le(self, val): # real signature unknown; restored from __doc__
        """ put_int64_le(self, val:int) -> bool """
        return False

    def put_int8(self, val): # real signature unknown; restored from __doc__
        """ put_int8(self, val:int) -> bool """
        return False

    def put_string_utf16(self, data): # real signature unknown; restored from __doc__
        """ put_string_utf16(self, data:list) -> bool """
        return False

    def put_string_utf32(self, data): # real signature unknown; restored from __doc__
        """ put_string_utf32(self, data:list) -> bool """
        return False

    def put_string_utf8(self, data): # real signature unknown; restored from __doc__
        """ put_string_utf8(self, data:str) -> bool """
        return False

    def put_uint16_be(self, val): # real signature unknown; restored from __doc__
        """ put_uint16_be(self, val:int) -> bool """
        return False

    def put_uint16_le(self, val): # real signature unknown; restored from __doc__
        """ put_uint16_le(self, val:int) -> bool """
        return False

    def put_uint24_be(self, val): # real signature unknown; restored from __doc__
        """ put_uint24_be(self, val:int) -> bool """
        return False

    def put_uint24_le(self, val): # real signature unknown; restored from __doc__
        """ put_uint24_le(self, val:int) -> bool """
        return False

    def put_uint32_be(self, val): # real signature unknown; restored from __doc__
        """ put_uint32_be(self, val:int) -> bool """
        return False

    def put_uint32_le(self, val): # real signature unknown; restored from __doc__
        """ put_uint32_le(self, val:int) -> bool """
        return False

    def put_uint64_be(self, val): # real signature unknown; restored from __doc__
        """ put_uint64_be(self, val:int) -> bool """
        return False

    def put_uint64_le(self, val): # real signature unknown; restored from __doc__
        """ put_uint64_le(self, val:int) -> bool """
        return False

    def put_uint8(self, val): # real signature unknown; restored from __doc__
        """ put_uint8(self, val:int) -> bool """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def reset_and_get_buffer(self): # real signature unknown; restored from __doc__
        """ reset_and_get_buffer(self) -> Gst.Buffer """
        pass

    def reset_and_get_data(self): # real signature unknown; restored from __doc__
        """ reset_and_get_data(self) -> list """
        return []

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

    alloc_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ByteWriter), '__module__': 'gi.repository.GstBase', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ByteWriter' objects>, '__weakref__': <attribute '__weakref__' of 'ByteWriter' objects>, '__doc__': None, 'parent': <property object at 0x7f9fb7bcf270>, 'alloc_size': <property object at 0x7f9fb7bcf360>, 'fixed': <property object at 0x7f9fb7bcf450>, 'owned': <property object at 0x7f9fb7bcf540>, '_gst_reserved': <property object at 0x7f9fb7bcf630>, 'ensure_free_space': gi.FunctionInfo(ensure_free_space), 'fill': gi.FunctionInfo(fill), 'free': gi.FunctionInfo(free), 'free_and_get_buffer': gi.FunctionInfo(free_and_get_buffer), 'free_and_get_data': gi.FunctionInfo(free_and_get_data), 'get_remaining': gi.FunctionInfo(get_remaining), 'init': gi.FunctionInfo(init), 'init_with_data': gi.FunctionInfo(init_with_data), 'init_with_size': gi.FunctionInfo(init_with_size), 'put_buffer': gi.FunctionInfo(put_buffer), 'put_data': gi.FunctionInfo(put_data), 'put_float32_be': gi.FunctionInfo(put_float32_be), 'put_float32_le': gi.FunctionInfo(put_float32_le), 'put_float64_be': gi.FunctionInfo(put_float64_be), 'put_float64_le': gi.FunctionInfo(put_float64_le), 'put_int16_be': gi.FunctionInfo(put_int16_be), 'put_int16_le': gi.FunctionInfo(put_int16_le), 'put_int24_be': gi.FunctionInfo(put_int24_be), 'put_int24_le': gi.FunctionInfo(put_int24_le), 'put_int32_be': gi.FunctionInfo(put_int32_be), 'put_int32_le': gi.FunctionInfo(put_int32_le), 'put_int64_be': gi.FunctionInfo(put_int64_be), 'put_int64_le': gi.FunctionInfo(put_int64_le), 'put_int8': gi.FunctionInfo(put_int8), 'put_string_utf16': gi.FunctionInfo(put_string_utf16), 'put_string_utf32': gi.FunctionInfo(put_string_utf32), 'put_string_utf8': gi.FunctionInfo(put_string_utf8), 'put_uint16_be': gi.FunctionInfo(put_uint16_be), 'put_uint16_le': gi.FunctionInfo(put_uint16_le), 'put_uint24_be': gi.FunctionInfo(put_uint24_be), 'put_uint24_le': gi.FunctionInfo(put_uint24_le), 'put_uint32_be': gi.FunctionInfo(put_uint32_be), 'put_uint32_le': gi.FunctionInfo(put_uint32_le), 'put_uint64_be': gi.FunctionInfo(put_uint64_be), 'put_uint64_le': gi.FunctionInfo(put_uint64_le), 'put_uint8': gi.FunctionInfo(put_uint8), 'reset': gi.FunctionInfo(reset), 'reset_and_get_buffer': gi.FunctionInfo(reset_and_get_buffer), 'reset_and_get_data': gi.FunctionInfo(reset_and_get_data)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ByteWriter)


