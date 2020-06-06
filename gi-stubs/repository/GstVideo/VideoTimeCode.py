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


class VideoTimeCode(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        VideoTimeCode()
        new(fps_n:int, fps_d:int, latest_daily_jam:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, hours:int, minutes:int, seconds:int, frames:int, field_count:int) -> GstVideo.VideoTimeCode
        new_empty() -> GstVideo.VideoTimeCode
        new_from_date_time(fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) -> GstVideo.VideoTimeCode
        new_from_date_time_full(fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) -> GstVideo.VideoTimeCode
        new_from_string(tc_str:str) -> GstVideo.VideoTimeCode or None
    """
    def add_frames(self, frames): # real signature unknown; restored from __doc__
        """ add_frames(self, frames:int) """
        pass

    def add_interval(self, tc_inter): # real signature unknown; restored from __doc__
        """ add_interval(self, tc_inter:GstVideo.VideoTimeCodeInterval) -> GstVideo.VideoTimeCode or None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def compare(self, tc2): # real signature unknown; restored from __doc__
        """ compare(self, tc2:GstVideo.VideoTimeCode) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstVideo.VideoTimeCode """
        pass

    def frames_since_daily_jam(self): # real signature unknown; restored from __doc__
        """ frames_since_daily_jam(self) -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def increment_frame(self): # real signature unknown; restored from __doc__
        """ increment_frame(self) """
        pass

    def init(self, fps_n, fps_d, latest_daily_jam, flags, hours, minutes, seconds, frames, field_count): # real signature unknown; restored from __doc__
        """ init(self, fps_n:int, fps_d:int, latest_daily_jam:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, hours:int, minutes:int, seconds:int, frames:int, field_count:int) """
        pass

    def init_from_date_time(self, fps_n, fps_d, dt, flags, field_count): # real signature unknown; restored from __doc__
        """ init_from_date_time(self, fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) """
        pass

    def init_from_date_time_full(self, fps_n, fps_d, dt, flags, field_count): # real signature unknown; restored from __doc__
        """ init_from_date_time_full(self, fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def new(self, fps_n, fps_d, latest_daily_jam, flags, hours, minutes, seconds, frames, field_count): # real signature unknown; restored from __doc__
        """ new(fps_n:int, fps_d:int, latest_daily_jam:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, hours:int, minutes:int, seconds:int, frames:int, field_count:int) -> GstVideo.VideoTimeCode """
        pass

    def new_empty(self): # real signature unknown; restored from __doc__
        """ new_empty() -> GstVideo.VideoTimeCode """
        pass

    def new_from_date_time(self, fps_n, fps_d, dt, flags, field_count): # real signature unknown; restored from __doc__
        """ new_from_date_time(fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) -> GstVideo.VideoTimeCode """
        pass

    def new_from_date_time_full(self, fps_n, fps_d, dt, flags, field_count): # real signature unknown; restored from __doc__
        """ new_from_date_time_full(fps_n:int, fps_d:int, dt:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, field_count:int) -> GstVideo.VideoTimeCode """
        pass

    def new_from_string(self, tc_str): # real signature unknown; restored from __doc__
        """ new_from_string(tc_str:str) -> GstVideo.VideoTimeCode or None """
        pass

    def nsec_since_daily_jam(self): # real signature unknown; restored from __doc__
        """ nsec_since_daily_jam(self) -> int """
        return 0

    def to_date_time(self): # real signature unknown; restored from __doc__
        """ to_date_time(self) -> GLib.DateTime or None """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    field_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minutes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoTimeCode), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstVideoTimeCode (94743669598016)>, '__dict__': <attribute '__dict__' of 'VideoTimeCode' objects>, '__weakref__': <attribute '__weakref__' of 'VideoTimeCode' objects>, '__doc__': None, 'config': <property object at 0x7f930d2ab0e0>, 'hours': <property object at 0x7f930d2ab1d0>, 'minutes': <property object at 0x7f930d2ab2c0>, 'seconds': <property object at 0x7f930d2ab3b0>, 'frames': <property object at 0x7f930d2ab4a0>, 'field_count': <property object at 0x7f930d2ab590>, 'new': gi.FunctionInfo(new), 'new_empty': gi.FunctionInfo(new_empty), 'new_from_date_time': gi.FunctionInfo(new_from_date_time), 'new_from_date_time_full': gi.FunctionInfo(new_from_date_time_full), 'new_from_string': gi.FunctionInfo(new_from_string), 'add_frames': gi.FunctionInfo(add_frames), 'add_interval': gi.FunctionInfo(add_interval), 'clear': gi.FunctionInfo(clear), 'compare': gi.FunctionInfo(compare), 'copy': gi.FunctionInfo(copy), 'frames_since_daily_jam': gi.FunctionInfo(frames_since_daily_jam), 'free': gi.FunctionInfo(free), 'increment_frame': gi.FunctionInfo(increment_frame), 'init': gi.FunctionInfo(init), 'init_from_date_time': gi.FunctionInfo(init_from_date_time), 'init_from_date_time_full': gi.FunctionInfo(init_from_date_time_full), 'is_valid': gi.FunctionInfo(is_valid), 'nsec_since_daily_jam': gi.FunctionInfo(nsec_since_daily_jam), 'to_date_time': gi.FunctionInfo(to_date_time), 'to_string': gi.FunctionInfo(to_string)})"
    __gtype__ = None # (!) real value is '<GType GstVideoTimeCode (94743669598016)>'
    __info__ = StructInfo(VideoTimeCode)


