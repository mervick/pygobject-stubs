# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Segment(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Segment()
        new() -> Gst.Segment
    """
    def clip(self, format, start, stop): # real signature unknown; restored from __doc__
        """ clip(self, format:Gst.Format, start:int, stop:int) -> bool, clip_start:int, clip_stop:int """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gst.Segment """
        pass

    def copy_into(self, dest): # real signature unknown; restored from __doc__
        """ copy_into(self, dest:Gst.Segment) """
        pass

    def do_seek(self, rate, format, flags, start_type, start, stop_type, stop): # real signature unknown; restored from __doc__
        """ do_seek(self, rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int) -> bool, update:bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self, format): # real signature unknown; restored from __doc__
        """ init(self, format:Gst.Format) """
        pass

    def is_equal(self, s1): # real signature unknown; restored from __doc__
        """ is_equal(self, s1:Gst.Segment) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gst.Segment """
        pass

    def offset_running_time(self, format, offset): # real signature unknown; restored from __doc__
        """ offset_running_time(self, format:Gst.Format, offset:int) -> bool """
        return False

    def position_from_running_time(self, format, running_time): # real signature unknown; restored from __doc__
        """ position_from_running_time(self, format:Gst.Format, running_time:int) -> int """
        return 0

    def position_from_running_time_full(self, format, running_time): # real signature unknown; restored from __doc__
        """ position_from_running_time_full(self, format:Gst.Format, running_time:int) -> int, position:int """
        return 0

    def position_from_stream_time(self, format, stream_time): # real signature unknown; restored from __doc__
        """ position_from_stream_time(self, format:Gst.Format, stream_time:int) -> int """
        return 0

    def position_from_stream_time_full(self, format, stream_time): # real signature unknown; restored from __doc__
        """ position_from_stream_time_full(self, format:Gst.Format, stream_time:int) -> int, position:int """
        return 0

    def set_running_time(self, format, running_time): # real signature unknown; restored from __doc__
        """ set_running_time(self, format:Gst.Format, running_time:int) -> bool """
        return False

    def to_position(self, format, running_time): # real signature unknown; restored from __doc__
        """ to_position(self, format:Gst.Format, running_time:int) -> int """
        return 0

    def to_running_time(self, format, position): # real signature unknown; restored from __doc__
        """ to_running_time(self, format:Gst.Format, position:int) -> int """
        return 0

    def to_running_time_full(self, format, position): # real signature unknown; restored from __doc__
        """ to_running_time_full(self, format:Gst.Format, position:int) -> int, running_time:int """
        return 0

    def to_stream_time(self, format, position): # real signature unknown; restored from __doc__
        """ to_stream_time(self, format:Gst.Format, position:int) -> int """
        return 0

    def to_stream_time_full(self, format, position): # real signature unknown; restored from __doc__
        """ to_stream_time_full(self, format:Gst.Format, position:int) -> int, stream_time:int """
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
        """ new() -> Gst.Segment """
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

    applied_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Segment), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstSegment (94058977930272)>, '__dict__': <attribute '__dict__' of 'Segment' objects>, '__weakref__': <attribute '__weakref__' of 'Segment' objects>, '__doc__': None, 'flags': <property object at 0x7f4260517860>, 'rate': <property object at 0x7f4260517950>, 'applied_rate': <property object at 0x7f4260517a40>, 'format': <property object at 0x7f4260517b30>, 'base': <property object at 0x7f4260517c20>, 'offset': <property object at 0x7f4260517d10>, 'start': <property object at 0x7f4260517e00>, 'stop': <property object at 0x7f4260517ef0>, 'time': <property object at 0x7f4260519040>, 'position': <property object at 0x7f4260519130>, 'duration': <property object at 0x7f4260519220>, '_gst_reserved': <property object at 0x7f4260519310>, 'new': gi.FunctionInfo(new), 'clip': gi.FunctionInfo(clip), 'copy': gi.FunctionInfo(copy), 'copy_into': gi.FunctionInfo(copy_into), 'do_seek': gi.FunctionInfo(do_seek), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init), 'is_equal': gi.FunctionInfo(is_equal), 'offset_running_time': gi.FunctionInfo(offset_running_time), 'position_from_running_time': gi.FunctionInfo(position_from_running_time), 'position_from_running_time_full': gi.FunctionInfo(position_from_running_time_full), 'position_from_stream_time': gi.FunctionInfo(position_from_stream_time), 'position_from_stream_time_full': gi.FunctionInfo(position_from_stream_time_full), 'set_running_time': gi.FunctionInfo(set_running_time), 'to_position': gi.FunctionInfo(to_position), 'to_running_time': gi.FunctionInfo(to_running_time), 'to_running_time_full': gi.FunctionInfo(to_running_time_full), 'to_stream_time': gi.FunctionInfo(to_stream_time), 'to_stream_time_full': gi.FunctionInfo(to_stream_time_full), '__new__': <staticmethod object at 0x7f4260518220>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstSegment (94058977930272)>'
    __info__ = StructInfo(Segment)


