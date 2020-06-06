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


class VideoInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        VideoInfo()
        new() -> GstVideo.VideoInfo
    """
    def align(self, align): # real signature unknown; restored from __doc__
        """ align(self, align:GstVideo.VideoAlignment) -> bool """
        return False

    def convert(self, src_format, src_value, dest_format): # real signature unknown; restored from __doc__
        """ convert(self, src_format:Gst.Format, src_value:int, dest_format:Gst.Format) -> bool, dest_value:int """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstVideo.VideoInfo """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_caps(self, caps): # real signature unknown; restored from __doc__
        """ from_caps(self, caps:Gst.Caps) -> bool """
        return False

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def is_equal(self, other): # real signature unknown; restored from __doc__
        """ is_equal(self, other:GstVideo.VideoInfo) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GstVideo.VideoInfo """
        pass

    def set_format(self, format, width, height): # real signature unknown; restored from __doc__
        """ set_format(self, format:GstVideo.VideoFormat, width:int, height:int) -> bool """
        return False

    def set_interlaced_format(self, format, mode, width, height): # real signature unknown; restored from __doc__
        """ set_interlaced_format(self, format:GstVideo.VideoFormat, mode:GstVideo.VideoInterlaceMode, width:int, height:int) -> bool """
        return False

    def to_caps(self): # real signature unknown; restored from __doc__
        """ to_caps(self) -> Gst.Caps """
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
        """ new() -> GstVideo.VideoInfo """
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

    chroma_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    colorimetry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    finfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fps_d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fps_n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    interlace_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    par_d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    par_n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoInfo), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstVideoInfo (94743669497408)>, '__dict__': <attribute '__dict__' of 'VideoInfo' objects>, '__weakref__': <attribute '__weakref__' of 'VideoInfo' objects>, '__doc__': None, 'finfo': <property object at 0x7f930d28e360>, 'interlace_mode': <property object at 0x7f930d28e400>, 'flags': <property object at 0x7f930d28e4f0>, 'width': <property object at 0x7f930d28e5e0>, 'height': <property object at 0x7f930d28e6d0>, 'size': <property object at 0x7f930d28e7c0>, 'views': <property object at 0x7f930d28e8b0>, 'chroma_site': <property object at 0x7f930d28e9a0>, 'colorimetry': <property object at 0x7f930d28ea90>, 'par_n': <property object at 0x7f930d28eb80>, 'par_d': <property object at 0x7f930d28ec70>, 'fps_n': <property object at 0x7f930d28ed60>, 'fps_d': <property object at 0x7f930d28ee50>, 'offset': <property object at 0x7f930d28ef40>, 'stride': <property object at 0x7f930d28f090>, 'new': gi.FunctionInfo(new), 'align': gi.FunctionInfo(align), 'convert': gi.FunctionInfo(convert), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'from_caps': gi.FunctionInfo(from_caps), 'init': gi.FunctionInfo(init), 'is_equal': gi.FunctionInfo(is_equal), 'set_format': gi.FunctionInfo(set_format), 'set_interlaced_format': gi.FunctionInfo(set_interlaced_format), 'to_caps': gi.FunctionInfo(to_caps), '__new__': <staticmethod object at 0x7f930d284ac0>, '__init__': <function nothing at 0x7f930d82eee0>})"
    __gtype__ = None # (!) real value is '<GType GstVideoInfo (94743669497408)>'
    __info__ = StructInfo(VideoInfo)


