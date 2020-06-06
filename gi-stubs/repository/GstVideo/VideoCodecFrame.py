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


class VideoCodecFrame(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        VideoCodecFrame()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_user_data(self): # real signature unknown; restored from __doc__
        """ get_user_data(self) """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GstVideo.VideoCodecFrame """
        pass

    def set_user_data(self, user_data=None, notify): # real signature unknown; restored from __doc__
        """ set_user_data(self, user_data=None, notify:GLib.DestroyNotify) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    deadline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    decode_frame_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    distance_from_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    input_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    output_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    presentation_frame_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    system_frame_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data_destroy_notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoCodecFrame), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstVideoCodecFrame (94743668812240)>, '__dict__': <attribute '__dict__' of 'VideoCodecFrame' objects>, '__weakref__': <attribute '__weakref__' of 'VideoCodecFrame' objects>, '__doc__': None, 'ref_count': <property object at 0x7f930d6112c0>, 'flags': <property object at 0x7f930d6113b0>, 'system_frame_number': <property object at 0x7f930d6114f0>, 'decode_frame_number': <property object at 0x7f930d611630>, 'presentation_frame_number': <property object at 0x7f930d611770>, 'dts': <property object at 0x7f930d611860>, 'pts': <property object at 0x7f930d611950>, 'duration': <property object at 0x7f930d611a40>, 'distance_from_sync': <property object at 0x7f930d611b80>, 'input_buffer': <property object at 0x7f930d611c70>, 'output_buffer': <property object at 0x7f930d611d60>, 'deadline': <property object at 0x7f930d611e50>, 'events': <property object at 0x7f930d611f40>, 'user_data': <property object at 0x7f930d613090>, 'user_data_destroy_notify': <property object at 0x7f930d6131d0>, 'get_user_data': gi.FunctionInfo(get_user_data), 'ref': gi.FunctionInfo(ref), 'set_user_data': gi.FunctionInfo(set_user_data), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GstVideoCodecFrame (94743668812240)>'
    __info__ = StructInfo(VideoCodecFrame)


