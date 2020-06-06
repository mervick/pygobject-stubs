# encoding: utf-8
# module gi.repository.GstGL
# from /usr/lib64/girepository-1.0/GstGL-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class GLBaseMemory(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        GLBaseMemory()
    """
    def alloc(self, allocator, params): # real signature unknown; restored from __doc__
        """ alloc(allocator:GstGL.GLBaseMemoryAllocator, params:GstGL.GLAllocationParams) -> GstGL.GLBaseMemory """
        pass

    def alloc_data(self): # real signature unknown; restored from __doc__
        """ alloc_data(self) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def init(self, allocator, parent=None, context, params=None, size, user_data=None, notify=None): # real signature unknown; restored from __doc__
        """ init(self, allocator:Gst.Allocator, parent:Gst.Memory=None, context:GstGL.GLContext, params:Gst.AllocationParams=None, size:int, user_data=None, notify:GLib.DestroyNotify=None) """
        pass

    def init_once(self): # real signature unknown; restored from __doc__
        """ init_once() """
        pass

    def memcpy(self, dest, offset, size): # real signature unknown; restored from __doc__
        """ memcpy(self, dest:GstGL.GLBaseMemory, offset:int, size:int) -> bool """
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

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gl_map_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLBaseMemory), '__module__': 'gi.repository.GstGL', '__gtype__': <GType GstGLBaseMemory (93979012161984)>, '__dict__': <attribute '__dict__' of 'GLBaseMemory' objects>, '__weakref__': <attribute '__weakref__' of 'GLBaseMemory' objects>, '__doc__': None, 'mem': <property object at 0x7f56a3fe19a0>, 'context': <property object at 0x7f56a3fe1a90>, 'lock': <property object at 0x7f56a3fe1b80>, 'map_flags': <property object at 0x7f56a3fe1c70>, 'map_count': <property object at 0x7f56a3fe1d60>, 'gl_map_count': <property object at 0x7f56a3fe1e50>, 'data': <property object at 0x7f56a3fe1f40>, 'query': <property object at 0x7f56a3fe3090>, 'alloc_size': <property object at 0x7f56a3fe3180>, 'alloc_data': gi.FunctionInfo(alloc_data), 'notify': <property object at 0x7f56a3fe3360>, 'user_data': <property object at 0x7f56a3fe3450>, '_padding': <property object at 0x7f56a3fe3540>, 'init': gi.FunctionInfo(init), 'memcpy': gi.FunctionInfo(memcpy), 'alloc': gi.FunctionInfo(alloc), 'init_once': gi.FunctionInfo(init_once)})"
    __gtype__ = None # (!) real value is '<GType GstGLBaseMemory (93979012161984)>'
    __info__ = StructInfo(GLBaseMemory)


