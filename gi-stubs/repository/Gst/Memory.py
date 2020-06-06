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


class Memory(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Memory()
        new_wrapped(flags:Gst.MemoryFlags, data:list, maxsize:int, offset:int, user_data=None, notify:GLib.DestroyNotify=None) -> Gst.Memory or None
    """
    def copy(self, offset, size): # real signature unknown; restored from __doc__
        """ copy(self, offset:int, size:int) -> Gst.Memory """
        pass

    def get_sizes(self): # real signature unknown; restored from __doc__
        """ get_sizes(self) -> int, offset:int, maxsize:int """
        return 0

    def is_span(self, mem2): # real signature unknown; restored from __doc__
        """ is_span(self, mem2:Gst.Memory) -> bool, offset:int """
        return False

    def is_type(self, mem_type): # real signature unknown; restored from __doc__
        """ is_type(self, mem_type:str) -> bool """
        return False

    def make_mapped(self, flags): # real signature unknown; restored from __doc__
        """ make_mapped(self, flags:Gst.MapFlags) -> Gst.Memory or None, info:Gst.MapInfo """
        pass

    def map(self, flags): # real signature unknown; restored from __doc__
        """ map(self, flags:Gst.MapFlags) -> bool, info:Gst.MapInfo """
        return False

    def new_wrapped(self, flags, data, maxsize, offset, user_data=None, notify=None): # real signature unknown; restored from __doc__
        """ new_wrapped(flags:Gst.MemoryFlags, data:list, maxsize:int, offset:int, user_data=None, notify:GLib.DestroyNotify=None) -> Gst.Memory or None """
        pass

    def resize(self, offset, size): # real signature unknown; restored from __doc__
        """ resize(self, offset:int, size:int) """
        pass

    def share(self, offset, size): # real signature unknown; restored from __doc__
        """ share(self, offset:int, size:int) -> Gst.Memory """
        pass

    def unmap(self, info): # real signature unknown; restored from __doc__
        """ unmap(self, info:Gst.MapInfo) """
        pass

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

    align = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    allocator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    maxsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mini_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Memory), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstMemory (94058977741152)>, '__dict__': <attribute '__dict__' of 'Memory' objects>, '__weakref__': <attribute '__weakref__' of 'Memory' objects>, '__doc__': None, 'mini_object': <property object at 0x7f4260565450>, 'allocator': <property object at 0x7f4260565540>, 'parent': <property object at 0x7f4260565630>, 'maxsize': <property object at 0x7f4260565720>, 'align': <property object at 0x7f4260565810>, 'offset': <property object at 0x7f4260565900>, 'size': <property object at 0x7f42605659f0>, 'new_wrapped': gi.FunctionInfo(new_wrapped), 'copy': gi.FunctionInfo(copy), 'get_sizes': gi.FunctionInfo(get_sizes), 'is_span': gi.FunctionInfo(is_span), 'is_type': gi.FunctionInfo(is_type), 'make_mapped': gi.FunctionInfo(make_mapped), 'map': gi.FunctionInfo(map), 'resize': gi.FunctionInfo(resize), 'share': gi.FunctionInfo(share), 'unmap': gi.FunctionInfo(unmap)})"
    __gtype__ = None # (!) real value is '<GType GstMemory (94058977741152)>'
    __info__ = StructInfo(Memory)


