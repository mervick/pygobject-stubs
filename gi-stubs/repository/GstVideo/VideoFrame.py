# encoding: utf-8
# module gi.repository.GstVideo
# from /usr/lib64/girepository-1.0/GstVideo-1.0.typelib
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
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class VideoFrame(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VideoFrame()
    """
    def copy(self, src): # real signature unknown; restored from __doc__
        """ copy(self, src:GstVideo.VideoFrame) -> bool """
        return False

    def copy_plane(self, src, plane): # real signature unknown; restored from __doc__
        """ copy_plane(self, src:GstVideo.VideoFrame, plane:int) -> bool """
        return False

    def map(self, info, buffer, flags): # real signature unknown; restored from __doc__
        """ map(self, info:GstVideo.VideoInfo, buffer:Gst.Buffer, flags:Gst.MapFlags) -> bool """
        return False

    def map_id(self, info, buffer, id, flags): # real signature unknown; restored from __doc__
        """ map_id(self, info:GstVideo.VideoInfo, buffer:Gst.Buffer, id:int, flags:Gst.MapFlags) -> bool """
        return False

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
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

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoFrame), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VideoFrame' objects>, '__weakref__': <attribute '__weakref__' of 'VideoFrame' objects>, '__doc__': None, 'info': <property object at 0x7f930d28a220>, 'flags': <property object at 0x7f930d28a310>, 'buffer': <property object at 0x7f930d28a400>, 'meta': <property object at 0x7f930d28a4f0>, 'id': <property object at 0x7f930d28a5e0>, 'data': <property object at 0x7f930d28a6d0>, 'map': gi.FunctionInfo(map), '_gst_reserved': <property object at 0x7f930d28a8b0>, 'copy': gi.FunctionInfo(copy), 'copy_plane': gi.FunctionInfo(copy_plane), 'map_id': gi.FunctionInfo(map_id), 'unmap': gi.FunctionInfo(unmap)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VideoFrame)


