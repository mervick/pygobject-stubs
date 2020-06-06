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


class GLVideoAllocationParams(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        GLVideoAllocationParams()
        new(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat) -> GstGL.GLVideoAllocationParams
        new_wrapped_data(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, wrapped_data=None, user_data=None, notify:GLib.DestroyNotify=None) -> GstGL.GLVideoAllocationParams
        new_wrapped_gl_handle(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, gl_handle=None, user_data=None, notify:GLib.DestroyNotify=None) -> GstGL.GLVideoAllocationParams
        new_wrapped_texture(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, tex_id:int, user_data=None, notify:GLib.DestroyNotify=None) -> GstGL.GLVideoAllocationParams
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copy_data(self, dest_vid): # real signature unknown; restored from __doc__
        """ copy_data(self, dest_vid:GstGL.GLVideoAllocationParams) """
        pass

    def free_data(self): # real signature unknown; restored from __doc__
        """ free_data(self) """
        pass

    def new(self, context, alloc_params=None, v_info, plane, valign=None, target, tex_format): # real signature unknown; restored from __doc__
        """ new(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat) -> GstGL.GLVideoAllocationParams """
        pass

    def new_wrapped_data(self, context, alloc_params=None, v_info, plane, valign=None, target, tex_format, wrapped_data=None, user_data=None, notify=None): # real signature unknown; restored from __doc__
        """ new_wrapped_data(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, wrapped_data=None, user_data=None, notify:GLib.DestroyNotify=None) -> GstGL.GLVideoAllocationParams """
        pass

    def new_wrapped_gl_handle(self, context, alloc_params=None, v_info, plane, valign=None, target, tex_format, gl_handle=None, user_data=None, notify=None): # real signature unknown; restored from __doc__
        """ new_wrapped_gl_handle(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, gl_handle=None, user_data=None, notify:GLib.DestroyNotify=None) -> GstGL.GLVideoAllocationParams """
        pass

    def new_wrapped_texture(self, context, alloc_params=None, v_info, plane, valign=None, target, tex_format, tex_id, user_data=None, notify=None): # real signature unknown; restored from __doc__
        """ new_wrapped_texture(context:GstGL.GLContext, alloc_params:Gst.AllocationParams=None, v_info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, tex_id:int, user_data=None, notify:GLib.DestroyNotify=None) -> GstGL.GLVideoAllocationParams """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLVideoAllocationParams), '__module__': 'gi.repository.GstGL', '__gtype__': <GType GstGLVideoAllocationParams (93979012512256)>, '__dict__': <attribute '__dict__' of 'GLVideoAllocationParams' objects>, '__weakref__': <attribute '__weakref__' of 'GLVideoAllocationParams' objects>, '__doc__': None, 'parent': <property object at 0x7f56a3a33bd0>, 'v_info': <property object at 0x7f56a3a33cc0>, 'plane': <property object at 0x7f56a3a33db0>, 'valign': <property object at 0x7f56a3a33ea0>, 'target': <property object at 0x7f56a3a33f90>, 'tex_format': <property object at 0x7f56a3a360e0>, '_padding': <property object at 0x7f56a3a361d0>, 'new': gi.FunctionInfo(new), 'new_wrapped_data': gi.FunctionInfo(new_wrapped_data), 'new_wrapped_gl_handle': gi.FunctionInfo(new_wrapped_gl_handle), 'new_wrapped_texture': gi.FunctionInfo(new_wrapped_texture), 'copy_data': gi.FunctionInfo(copy_data), 'free_data': gi.FunctionInfo(free_data)})"
    __gtype__ = None # (!) real value is '<GType GstGLVideoAllocationParams (93979012512256)>'
    __info__ = StructInfo(GLVideoAllocationParams)


