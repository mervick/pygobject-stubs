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


class VideoOverlayRectangle(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_raw(pixels:Gst.Buffer, render_x:int, render_y:int, render_width:int, render_height:int, flags:GstVideo.VideoOverlayFormatFlags) -> GstVideo.VideoOverlayRectangle
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstVideo.VideoOverlayRectangle """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> GstVideo.VideoOverlayFormatFlags """
        pass

    def get_global_alpha(self): # real signature unknown; restored from __doc__
        """ get_global_alpha(self) -> float """
        return 0.0

    def get_pixels_argb(self, flags): # real signature unknown; restored from __doc__
        """ get_pixels_argb(self, flags:GstVideo.VideoOverlayFormatFlags) -> Gst.Buffer """
        pass

    def get_pixels_ayuv(self, flags): # real signature unknown; restored from __doc__
        """ get_pixels_ayuv(self, flags:GstVideo.VideoOverlayFormatFlags) -> Gst.Buffer """
        pass

    def get_pixels_raw(self, flags): # real signature unknown; restored from __doc__
        """ get_pixels_raw(self, flags:GstVideo.VideoOverlayFormatFlags) -> Gst.Buffer """
        pass

    def get_pixels_unscaled_argb(self, flags): # real signature unknown; restored from __doc__
        """ get_pixels_unscaled_argb(self, flags:GstVideo.VideoOverlayFormatFlags) -> Gst.Buffer """
        pass

    def get_pixels_unscaled_ayuv(self, flags): # real signature unknown; restored from __doc__
        """ get_pixels_unscaled_ayuv(self, flags:GstVideo.VideoOverlayFormatFlags) -> Gst.Buffer """
        pass

    def get_pixels_unscaled_raw(self, flags): # real signature unknown; restored from __doc__
        """ get_pixels_unscaled_raw(self, flags:GstVideo.VideoOverlayFormatFlags) -> Gst.Buffer """
        pass

    def get_render_rectangle(self): # real signature unknown; restored from __doc__
        """ get_render_rectangle(self) -> bool, render_x:int, render_y:int, render_width:int, render_height:int """
        return False

    def get_seqnum(self): # real signature unknown; restored from __doc__
        """ get_seqnum(self) -> int """
        return 0

    def new_raw(self, pixels, render_x, render_y, render_width, render_height, flags): # real signature unknown; restored from __doc__
        """ new_raw(pixels:Gst.Buffer, render_x:int, render_y:int, render_width:int, render_height:int, flags:GstVideo.VideoOverlayFormatFlags) -> GstVideo.VideoOverlayRectangle """
        pass

    def set_global_alpha(self, global_alpha): # real signature unknown; restored from __doc__
        """ set_global_alpha(self, global_alpha:float) """
        pass

    def set_render_rectangle(self, render_x, render_y, render_width, render_height): # real signature unknown; restored from __doc__
        """ set_render_rectangle(self, render_x:int, render_y:int, render_width:int, render_height:int) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoOverlayRectangle), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstVideoOverlayRectangle (94743669546016)>, '__dict__': <attribute '__dict__' of 'VideoOverlayRectangle' objects>, '__weakref__': <attribute '__weakref__' of 'VideoOverlayRectangle' objects>, '__doc__': None, 'new_raw': gi.FunctionInfo(new_raw), 'copy': gi.FunctionInfo(copy), 'get_flags': gi.FunctionInfo(get_flags), 'get_global_alpha': gi.FunctionInfo(get_global_alpha), 'get_pixels_argb': gi.FunctionInfo(get_pixels_argb), 'get_pixels_ayuv': gi.FunctionInfo(get_pixels_ayuv), 'get_pixels_raw': gi.FunctionInfo(get_pixels_raw), 'get_pixels_unscaled_argb': gi.FunctionInfo(get_pixels_unscaled_argb), 'get_pixels_unscaled_ayuv': gi.FunctionInfo(get_pixels_unscaled_ayuv), 'get_pixels_unscaled_raw': gi.FunctionInfo(get_pixels_unscaled_raw), 'get_render_rectangle': gi.FunctionInfo(get_render_rectangle), 'get_seqnum': gi.FunctionInfo(get_seqnum), 'set_global_alpha': gi.FunctionInfo(set_global_alpha), 'set_render_rectangle': gi.FunctionInfo(set_render_rectangle)})"
    __gtype__ = None # (!) real value is '<GType GstVideoOverlayRectangle (94743669546016)>'
    __info__ = StructInfo(VideoOverlayRectangle)


