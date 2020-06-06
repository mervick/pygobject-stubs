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


class GLMemory(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GLMemory()
    """
    def copy_into(self, tex_id, target, tex_format, width, height): # real signature unknown; restored from __doc__
        """ copy_into(self, tex_id:int, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, width:int, height:int) -> bool """
        return False

    def copy_teximage(self, tex_id, out_target, out_tex_format, out_width, out_height): # real signature unknown; restored from __doc__
        """ copy_teximage(self, tex_id:int, out_target:GstGL.GLTextureTarget, out_tex_format:GstGL.GLFormat, out_width:int, out_height:int) -> bool """
        return False

    def get_texture_format(self): # real signature unknown; restored from __doc__
        """ get_texture_format(self) -> GstGL.GLFormat """
        pass

    def get_texture_height(self): # real signature unknown; restored from __doc__
        """ get_texture_height(self) -> int """
        return 0

    def get_texture_id(self): # real signature unknown; restored from __doc__
        """ get_texture_id(self) -> int """
        return 0

    def get_texture_target(self): # real signature unknown; restored from __doc__
        """ get_texture_target(self) -> GstGL.GLTextureTarget """
        pass

    def get_texture_width(self): # real signature unknown; restored from __doc__
        """ get_texture_width(self) -> int """
        return 0

    def init(self, allocator, parent=None, context, target, tex_format, params=None, info, plane, valign=None, user_data=None, notify=None): # real signature unknown; restored from __doc__
        """ init(self, allocator:Gst.Allocator, parent:Gst.Memory=None, context:GstGL.GLContext, target:GstGL.GLTextureTarget, tex_format:GstGL.GLFormat, params:Gst.AllocationParams=None, info:GstVideo.VideoInfo, plane:int, valign:GstVideo.VideoAlignment=None, user_data=None, notify:GLib.DestroyNotify=None) """
        pass

    def init_once(self): # real signature unknown; restored from __doc__
        """ init_once() """
        pass

    def read_pixels(self, read_pointer=None): # real signature unknown; restored from __doc__
        """ read_pixels(self, read_pointer=None) -> bool """
        return False

    def texsubimage(self, read_pointer=None): # real signature unknown; restored from __doc__
        """ texsubimage(self, read_pointer=None) """
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

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    texture_wrapped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_scaling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unpack_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    valign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLMemory), '__module__': 'gi.repository.GstGL', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GLMemory' objects>, '__weakref__': <attribute '__weakref__' of 'GLMemory' objects>, '__doc__': None, 'mem': <property object at 0x7f56a3ffbb80>, 'tex_id': <property object at 0x7f56a3ffbc70>, 'tex_target': <property object at 0x7f56a3ffbd60>, 'tex_format': <property object at 0x7f56a3ffbe50>, 'info': <property object at 0x7f56a3ffbf40>, 'valign': <property object at 0x7f56a4000090>, 'plane': <property object at 0x7f56a4000180>, 'tex_scaling': <property object at 0x7f56a4000270>, 'texture_wrapped': <property object at 0x7f56a4000360>, 'unpack_length': <property object at 0x7f56a4000450>, 'tex_width': <property object at 0x7f56a4000540>, '_padding': <property object at 0x7f56a4000630>, 'copy_into': gi.FunctionInfo(copy_into), 'copy_teximage': gi.FunctionInfo(copy_teximage), 'get_texture_format': gi.FunctionInfo(get_texture_format), 'get_texture_height': gi.FunctionInfo(get_texture_height), 'get_texture_id': gi.FunctionInfo(get_texture_id), 'get_texture_target': gi.FunctionInfo(get_texture_target), 'get_texture_width': gi.FunctionInfo(get_texture_width), 'init': gi.FunctionInfo(init), 'read_pixels': gi.FunctionInfo(read_pixels), 'texsubimage': gi.FunctionInfo(texsubimage), 'init_once': gi.FunctionInfo(init_once)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GLMemory)


