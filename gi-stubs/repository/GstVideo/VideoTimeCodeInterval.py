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


class VideoTimeCodeInterval(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        VideoTimeCodeInterval()
        new(hours:int, minutes:int, seconds:int, frames:int) -> GstVideo.VideoTimeCodeInterval
        new_from_string(tc_inter_str:str) -> GstVideo.VideoTimeCodeInterval or None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstVideo.VideoTimeCodeInterval """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self, hours, minutes, seconds, frames): # real signature unknown; restored from __doc__
        """ init(self, hours:int, minutes:int, seconds:int, frames:int) """
        pass

    def new(self, hours, minutes, seconds, frames): # real signature unknown; restored from __doc__
        """ new(hours:int, minutes:int, seconds:int, frames:int) -> GstVideo.VideoTimeCodeInterval """
        pass

    def new_from_string(self, tc_inter_str): # real signature unknown; restored from __doc__
        """ new_from_string(tc_inter_str:str) -> GstVideo.VideoTimeCodeInterval or None """
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

    frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoTimeCodeInterval), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstVideoTimeCodeInterval (94743669606960)>, '__dict__': <attribute '__dict__' of 'VideoTimeCodeInterval' objects>, '__weakref__': <attribute '__weakref__' of 'VideoTimeCodeInterval' objects>, '__doc__': None, 'hours': <property object at 0x7f930d2ac220>, 'minutes': <property object at 0x7f930d2ac310>, 'seconds': <property object at 0x7f930d2ac400>, 'frames': <property object at 0x7f930d2ac4f0>, 'new': gi.FunctionInfo(new), 'new_from_string': gi.FunctionInfo(new_from_string), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init)})"
    __gtype__ = None # (!) real value is '<GType GstVideoTimeCodeInterval (94743669606960)>'
    __info__ = StructInfo(VideoTimeCodeInterval)


