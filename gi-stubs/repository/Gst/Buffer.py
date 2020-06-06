# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Buffer(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Buffer()
        new() -> Gst.Buffer
        new_allocate(allocator:Gst.Allocator=None, size:int, params:Gst.AllocationParams=None) -> Gst.Buffer or None
        new_wrapped(data:list) -> Gst.Buffer
        new_wrapped_bytes(bytes:GLib.Bytes) -> Gst.Buffer
        new_wrapped_full(flags:Gst.MemoryFlags, data:list, maxsize:int, offset:int, user_data=None, notify:GLib.DestroyNotify=None) -> Gst.Buffer
    """
    def add_meta(self, info, params=None): # real signature unknown; restored from __doc__
        """ add_meta(self, info:Gst.MetaInfo, params=None) -> Gst.Meta or None """
        pass

    def add_parent_buffer_meta(self, ref): # real signature unknown; restored from __doc__
        """ add_parent_buffer_meta(self, ref:Gst.Buffer) -> Gst.ParentBufferMeta or None """
        pass

    def add_protection_meta(self, info): # real signature unknown; restored from __doc__
        """ add_protection_meta(self, info:Gst.Structure) -> Gst.ProtectionMeta """
        pass

    def add_reference_timestamp_meta(self, reference, timestamp, duration): # real signature unknown; restored from __doc__
        """ add_reference_timestamp_meta(self, reference:Gst.Caps, timestamp:int, duration:int) -> Gst.ReferenceTimestampMeta or None """
        pass

    def append(self, buf2): # real signature unknown; restored from __doc__
        """ append(self, buf2:Gst.Buffer) -> Gst.Buffer """
        pass

    def append_memory(self, mem): # real signature unknown; restored from __doc__
        """ append_memory(self, mem:Gst.Memory) """
        pass

    def append_region(self, buf2, offset, size): # real signature unknown; restored from __doc__
        """ append_region(self, buf2:Gst.Buffer, offset:int, size:int) -> Gst.Buffer """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copy_deep(self): # real signature unknown; restored from __doc__
        """ copy_deep(self) -> Gst.Buffer """
        pass

    def copy_into(self, src, flags, offset, size): # real signature unknown; restored from __doc__
        """ copy_into(self, src:Gst.Buffer, flags:Gst.BufferCopyFlags, offset:int, size:int) -> bool """
        return False

    def copy_region(self, flags, offset, size): # real signature unknown; restored from __doc__
        """ copy_region(self, flags:Gst.BufferCopyFlags, offset:int, size:int) -> Gst.Buffer """
        pass

    def extract(self, offset): # real signature unknown; restored from __doc__
        """ extract(self, offset:int) -> int, dest:list """
        return 0

    def extract_dup(self, offset, size): # real signature unknown; restored from __doc__
        """ extract_dup(self, offset:int, size:int) -> dest:list """
        pass

    def fill(self, offset, src): # real signature unknown; restored from __doc__
        """ fill(self, offset:int, src:list) -> int """
        return 0

    def find_memory(self, offset, size): # real signature unknown; restored from __doc__
        """ find_memory(self, offset:int, size:int) -> bool, idx:int, length:int, skip:int """
        return False

    def foreach_meta(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_meta(self, func:Gst.BufferForeachMetaFunc, user_data=None) -> bool """
        return False

    def get_all_memory(self): # real signature unknown; restored from __doc__
        """ get_all_memory(self) -> Gst.Memory or None """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gst.BufferFlags """
        pass

    def get_max_memory(self): # real signature unknown; restored from __doc__
        """ get_max_memory() -> int """
        return 0

    def get_memory(self, idx): # real signature unknown; restored from __doc__
        """ get_memory(self, idx:int) -> Gst.Memory or None """
        pass

    def get_memory_range(self, idx, length): # real signature unknown; restored from __doc__
        """ get_memory_range(self, idx:int, length:int) -> Gst.Memory or None """
        pass

    def get_meta(self, api): # real signature unknown; restored from __doc__
        """ get_meta(self, api:GType) -> Gst.Meta or None """
        pass

    def get_n_meta(self, api_type): # real signature unknown; restored from __doc__
        """ get_n_meta(self, api_type:GType) -> int """
        return 0

    def get_reference_timestamp_meta(self, reference=None): # real signature unknown; restored from __doc__
        """ get_reference_timestamp_meta(self, reference:Gst.Caps=None) -> Gst.ReferenceTimestampMeta or None """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_sizes(self): # real signature unknown; restored from __doc__
        """ get_sizes(self) -> int, offset:int, maxsize:int """
        return 0

    def get_sizes_range(self, idx, length): # real signature unknown; restored from __doc__
        """ get_sizes_range(self, idx:int, length:int) -> int, offset:int, maxsize:int """
        return 0

    def has_flags(self, flags): # real signature unknown; restored from __doc__
        """ has_flags(self, flags:Gst.BufferFlags) -> bool """
        return False

    def insert_memory(self, idx, mem): # real signature unknown; restored from __doc__
        """ insert_memory(self, idx:int, mem:Gst.Memory) """
        pass

    def is_all_memory_writable(self): # real signature unknown; restored from __doc__
        """ is_all_memory_writable(self) -> bool """
        return False

    def is_memory_range_writable(self, idx, length): # real signature unknown; restored from __doc__
        """ is_memory_range_writable(self, idx:int, length:int) -> bool """
        return False

    def map(self, flags): # real signature unknown; restored from __doc__
        """ map(self, flags:Gst.MapFlags) -> bool, info:Gst.MapInfo """
        return False

    def map_range(self, idx, length, flags): # real signature unknown; restored from __doc__
        """ map_range(self, idx:int, length:int, flags:Gst.MapFlags) -> bool, info:Gst.MapInfo """
        return False

    def memcmp(self, offset, mem): # real signature unknown; restored from __doc__
        """ memcmp(self, offset:int, mem:list) -> int """
        return 0

    def memset(self, offset, val, size): # real signature unknown; restored from __doc__
        """ memset(self, offset:int, val:int, size:int) -> int """
        return 0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gst.Buffer """
        pass

    def new_allocate(self, allocator=None, size, params=None): # real signature unknown; restored from __doc__
        """ new_allocate(allocator:Gst.Allocator=None, size:int, params:Gst.AllocationParams=None) -> Gst.Buffer or None """
        pass

    def new_wrapped(self, data): # real signature unknown; restored from __doc__
        """ new_wrapped(data:list) -> Gst.Buffer """
        pass

    def new_wrapped_bytes(self, bytes): # real signature unknown; restored from __doc__
        """ new_wrapped_bytes(bytes:GLib.Bytes) -> Gst.Buffer """
        pass

    def new_wrapped_full(self, flags, data, maxsize, offset, user_data=None, notify=None): # real signature unknown; restored from __doc__
        """ new_wrapped_full(flags:Gst.MemoryFlags, data:list, maxsize:int, offset:int, user_data=None, notify:GLib.DestroyNotify=None) -> Gst.Buffer """
        pass

    def n_memory(self): # real signature unknown; restored from __doc__
        """ n_memory(self) -> int """
        return 0

    def peek_memory(self, idx): # real signature unknown; restored from __doc__
        """ peek_memory(self, idx:int) -> Gst.Memory or None """
        pass

    def prepend_memory(self, mem): # real signature unknown; restored from __doc__
        """ prepend_memory(self, mem:Gst.Memory) """
        pass

    def remove_all_memory(self): # real signature unknown; restored from __doc__
        """ remove_all_memory(self) """
        pass

    def remove_memory(self, idx): # real signature unknown; restored from __doc__
        """ remove_memory(self, idx:int) """
        pass

    def remove_memory_range(self, idx, length): # real signature unknown; restored from __doc__
        """ remove_memory_range(self, idx:int, length:int) """
        pass

    def remove_meta(self, meta): # real signature unknown; restored from __doc__
        """ remove_meta(self, meta:Gst.Meta) -> bool """
        return False

    def replace_all_memory(self, mem): # real signature unknown; restored from __doc__
        """ replace_all_memory(self, mem:Gst.Memory) """
        pass

    def replace_memory(self, idx, mem): # real signature unknown; restored from __doc__
        """ replace_memory(self, idx:int, mem:Gst.Memory) """
        pass

    def replace_memory_range(self, idx, length, mem): # real signature unknown; restored from __doc__
        """ replace_memory_range(self, idx:int, length:int, mem:Gst.Memory) """
        pass

    def resize(self, offset, size): # real signature unknown; restored from __doc__
        """ resize(self, offset:int, size:int) """
        pass

    def resize_range(self, idx, length, offset, size): # real signature unknown; restored from __doc__
        """ resize_range(self, idx:int, length:int, offset:int, size:int) -> bool """
        return False

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Gst.BufferFlags) -> bool """
        return False

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
        pass

    def unmap(self, info): # real signature unknown; restored from __doc__
        """ unmap(self, info:Gst.MapInfo) """
        pass

    def unset_flags(self, flags): # real signature unknown; restored from __doc__
        """ unset_flags(self, flags:Gst.BufferFlags) -> bool """
        return False

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Gst.Buffer """
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

    dts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mini_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Buffer), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstBuffer (94058977204576)>, '__dict__': <attribute '__dict__' of 'Buffer' objects>, '__weakref__': <attribute '__weakref__' of 'Buffer' objects>, '__doc__': None, 'mini_object': <property object at 0x7f4260717360>, 'pool': <property object at 0x7f4260717450>, 'pts': <property object at 0x7f4260717540>, 'dts': <property object at 0x7f4260717630>, 'duration': <property object at 0x7f4260717720>, 'offset': <property object at 0x7f4260717810>, 'offset_end': <property object at 0x7f4260717900>, 'new': gi.FunctionInfo(new), 'new_allocate': gi.FunctionInfo(new_allocate), 'new_wrapped': gi.FunctionInfo(new_wrapped), 'new_wrapped_bytes': gi.FunctionInfo(new_wrapped_bytes), 'new_wrapped_full': gi.FunctionInfo(new_wrapped_full), 'add_meta': gi.FunctionInfo(add_meta), 'add_parent_buffer_meta': gi.FunctionInfo(add_parent_buffer_meta), 'add_protection_meta': gi.FunctionInfo(add_protection_meta), 'add_reference_timestamp_meta': gi.FunctionInfo(add_reference_timestamp_meta), 'append': gi.FunctionInfo(append), 'append_memory': gi.FunctionInfo(append_memory), 'append_region': gi.FunctionInfo(append_region), 'copy_deep': gi.FunctionInfo(copy_deep), 'copy_into': gi.FunctionInfo(copy_into), 'copy_region': gi.FunctionInfo(copy_region), 'extract': gi.FunctionInfo(extract), 'extract_dup': gi.FunctionInfo(extract_dup), 'fill': gi.FunctionInfo(fill), 'find_memory': gi.FunctionInfo(find_memory), 'foreach_meta': gi.FunctionInfo(foreach_meta), 'get_all_memory': gi.FunctionInfo(get_all_memory), 'get_flags': gi.FunctionInfo(get_flags), 'get_memory': gi.FunctionInfo(get_memory), 'get_memory_range': gi.FunctionInfo(get_memory_range), 'get_meta': gi.FunctionInfo(get_meta), 'get_n_meta': gi.FunctionInfo(get_n_meta), 'get_reference_timestamp_meta': gi.FunctionInfo(get_reference_timestamp_meta), 'get_size': gi.FunctionInfo(get_size), 'get_sizes': gi.FunctionInfo(get_sizes), 'get_sizes_range': gi.FunctionInfo(get_sizes_range), 'has_flags': gi.FunctionInfo(has_flags), 'insert_memory': gi.FunctionInfo(insert_memory), 'is_all_memory_writable': gi.FunctionInfo(is_all_memory_writable), 'is_memory_range_writable': gi.FunctionInfo(is_memory_range_writable), 'map': gi.FunctionInfo(map), 'map_range': gi.FunctionInfo(map_range), 'memcmp': gi.FunctionInfo(memcmp), 'memset': gi.FunctionInfo(memset), 'n_memory': gi.FunctionInfo(n_memory), 'peek_memory': gi.FunctionInfo(peek_memory), 'prepend_memory': gi.FunctionInfo(prepend_memory), 'remove_all_memory': gi.FunctionInfo(remove_all_memory), 'remove_memory': gi.FunctionInfo(remove_memory), 'remove_memory_range': gi.FunctionInfo(remove_memory_range), 'remove_meta': gi.FunctionInfo(remove_meta), 'replace_all_memory': gi.FunctionInfo(replace_all_memory), 'replace_memory': gi.FunctionInfo(replace_memory), 'replace_memory_range': gi.FunctionInfo(replace_memory_range), 'resize': gi.FunctionInfo(resize), 'resize_range': gi.FunctionInfo(resize_range), 'set_flags': gi.FunctionInfo(set_flags), 'set_size': gi.FunctionInfo(set_size), 'unmap': gi.FunctionInfo(unmap), 'unset_flags': gi.FunctionInfo(unset_flags), 'get_max_memory': gi.FunctionInfo(get_max_memory), '__new__': <staticmethod object at 0x7f4260714550>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstBuffer (94058977204576)>'
    __info__ = StructInfo(Buffer)


