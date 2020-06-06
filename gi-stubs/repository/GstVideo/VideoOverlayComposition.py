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


class VideoOverlayComposition(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(rectangle:GstVideo.VideoOverlayRectangle) -> GstVideo.VideoOverlayComposition
    """
    def add_rectangle(self, rectangle): # real signature unknown; restored from __doc__
        """ add_rectangle(self, rectangle:GstVideo.VideoOverlayRectangle) """
        pass

    def blend(self, video_buf): # real signature unknown; restored from __doc__
        """ blend(self, video_buf:GstVideo.VideoFrame) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstVideo.VideoOverlayComposition """
        pass

    def get_rectangle(self, n): # real signature unknown; restored from __doc__
        """ get_rectangle(self, n:int) -> GstVideo.VideoOverlayRectangle """
        pass

    def get_seqnum(self): # real signature unknown; restored from __doc__
        """ get_seqnum(self) -> int """
        return 0

    def make_writable(self): # real signature unknown; restored from __doc__
        """ make_writable(self) -> GstVideo.VideoOverlayComposition """
        pass

    def new(self, rectangle): # real signature unknown; restored from __doc__
        """ new(rectangle:GstVideo.VideoOverlayRectangle) -> GstVideo.VideoOverlayComposition """
        pass

    def n_rectangles(self): # real signature unknown; restored from __doc__
        """ n_rectangles(self) -> int """
        return 0

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
        """ new(rectangle:GstVideo.VideoOverlayRectangle) -> GstVideo.VideoOverlayComposition """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoOverlayComposition), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstVideoOverlayComposition (94743669533216)>, '__dict__': <attribute '__dict__' of 'VideoOverlayComposition' objects>, '__weakref__': <attribute '__weakref__' of 'VideoOverlayComposition' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'add_rectangle': gi.FunctionInfo(add_rectangle), 'blend': gi.FunctionInfo(blend), 'copy': gi.FunctionInfo(copy), 'get_rectangle': gi.FunctionInfo(get_rectangle), 'get_seqnum': gi.FunctionInfo(get_seqnum), 'make_writable': gi.FunctionInfo(make_writable), 'n_rectangles': gi.FunctionInfo(n_rectangles), '__new__': <staticmethod object at 0x7f930d293460>, '__init__': <function nothing at 0x7f930d82eee0>})"
    __gtype__ = None # (!) real value is '<GType GstVideoOverlayComposition (94743669533216)>'
    __info__ = StructInfo(VideoOverlayComposition)


