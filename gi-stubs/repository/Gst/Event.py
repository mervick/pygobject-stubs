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


class Event(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Event()
        new_buffer_size(format:Gst.Format, minsize:int, maxsize:int, async:bool) -> Gst.Event
        new_caps(caps:Gst.Caps) -> Gst.Event or None
        new_custom(type:Gst.EventType, structure:Gst.Structure) -> Gst.Event or None
        new_eos() -> Gst.Event
        new_flush_start() -> Gst.Event
        new_flush_stop(reset_time:bool) -> Gst.Event
        new_gap(timestamp:int, duration:int) -> Gst.Event
        new_latency(latency:int) -> Gst.Event
        new_navigation(structure:Gst.Structure) -> Gst.Event
        new_protection(system_id:str, data:Gst.Buffer, origin:str) -> Gst.Event
        new_qos(type:Gst.QOSType, proportion:float, diff:int, timestamp:int) -> Gst.Event or None
        new_reconfigure() -> Gst.Event
        new_seek(rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int) -> Gst.Event or None
        new_segment(segment:Gst.Segment) -> Gst.Event or None
        new_segment_done(format:Gst.Format, position:int) -> Gst.Event
        new_select_streams(streams:list) -> Gst.Event
        new_sink_message(name:str, msg:Gst.Message) -> Gst.Event
        new_step(format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool) -> Gst.Event or None
        new_stream_collection(collection:Gst.StreamCollection) -> Gst.Event
        new_stream_group_done(group_id:int) -> Gst.Event
        new_stream_start(stream_id:str) -> Gst.Event
        new_tag(taglist:Gst.TagList) -> Gst.Event
        new_toc(toc:Gst.Toc, updated:bool) -> Gst.Event
        new_toc_select(uid:str) -> Gst.Event
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copy_segment(self, segment): # real signature unknown; restored from __doc__
        """ copy_segment(self, segment:Gst.Segment) """
        pass

    def get_running_time_offset(self): # real signature unknown; restored from __doc__
        """ get_running_time_offset(self) -> int """
        return 0

    def get_seqnum(self): # real signature unknown; restored from __doc__
        """ get_seqnum(self) -> int """
        return 0

    def get_structure(self): # real signature unknown; restored from __doc__
        """ get_structure(self) -> Gst.Structure or None """
        pass

    def has_name(self, name): # real signature unknown; restored from __doc__
        """ has_name(self, name:str) -> bool """
        return False

    def new_buffer_size(self, format, minsize, maxsize, async_): # real signature unknown; restored from __doc__
        """ new_buffer_size(format:Gst.Format, minsize:int, maxsize:int, async:bool) -> Gst.Event """
        pass

    def new_caps(self, caps): # real signature unknown; restored from __doc__
        """ new_caps(caps:Gst.Caps) -> Gst.Event or None """
        pass

    def new_custom(self, type, structure): # real signature unknown; restored from __doc__
        """ new_custom(type:Gst.EventType, structure:Gst.Structure) -> Gst.Event or None """
        pass

    def new_eos(self): # real signature unknown; restored from __doc__
        """ new_eos() -> Gst.Event """
        pass

    def new_flush_start(self): # real signature unknown; restored from __doc__
        """ new_flush_start() -> Gst.Event """
        pass

    def new_flush_stop(self, reset_time): # real signature unknown; restored from __doc__
        """ new_flush_stop(reset_time:bool) -> Gst.Event """
        pass

    def new_gap(self, timestamp, duration): # real signature unknown; restored from __doc__
        """ new_gap(timestamp:int, duration:int) -> Gst.Event """
        pass

    def new_latency(self, latency): # real signature unknown; restored from __doc__
        """ new_latency(latency:int) -> Gst.Event """
        pass

    def new_navigation(self, structure): # real signature unknown; restored from __doc__
        """ new_navigation(structure:Gst.Structure) -> Gst.Event """
        pass

    def new_protection(self, system_id, data, origin): # real signature unknown; restored from __doc__
        """ new_protection(system_id:str, data:Gst.Buffer, origin:str) -> Gst.Event """
        pass

    def new_qos(self, type, proportion, diff, timestamp): # real signature unknown; restored from __doc__
        """ new_qos(type:Gst.QOSType, proportion:float, diff:int, timestamp:int) -> Gst.Event or None """
        pass

    def new_reconfigure(self): # real signature unknown; restored from __doc__
        """ new_reconfigure() -> Gst.Event """
        pass

    def new_seek(self, rate, format, flags, start_type, start, stop_type, stop): # real signature unknown; restored from __doc__
        """ new_seek(rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int) -> Gst.Event or None """
        pass

    def new_segment(self, segment): # real signature unknown; restored from __doc__
        """ new_segment(segment:Gst.Segment) -> Gst.Event or None """
        pass

    def new_segment_done(self, format, position): # real signature unknown; restored from __doc__
        """ new_segment_done(format:Gst.Format, position:int) -> Gst.Event """
        pass

    def new_select_streams(self, streams): # real signature unknown; restored from __doc__
        """ new_select_streams(streams:list) -> Gst.Event """
        pass

    def new_sink_message(self, name, msg): # real signature unknown; restored from __doc__
        """ new_sink_message(name:str, msg:Gst.Message) -> Gst.Event """
        pass

    def new_step(self, format, amount, rate, flush, intermediate): # real signature unknown; restored from __doc__
        """ new_step(format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool) -> Gst.Event or None """
        pass

    def new_stream_collection(self, collection): # real signature unknown; restored from __doc__
        """ new_stream_collection(collection:Gst.StreamCollection) -> Gst.Event """
        pass

    def new_stream_group_done(self, group_id): # real signature unknown; restored from __doc__
        """ new_stream_group_done(group_id:int) -> Gst.Event """
        pass

    def new_stream_start(self, stream_id): # real signature unknown; restored from __doc__
        """ new_stream_start(stream_id:str) -> Gst.Event """
        pass

    def new_tag(self, taglist): # real signature unknown; restored from __doc__
        """ new_tag(taglist:Gst.TagList) -> Gst.Event """
        pass

    def new_toc(self, toc, updated): # real signature unknown; restored from __doc__
        """ new_toc(toc:Gst.Toc, updated:bool) -> Gst.Event """
        pass

    def new_toc_select(self, uid): # real signature unknown; restored from __doc__
        """ new_toc_select(uid:str) -> Gst.Event """
        pass

    def parse_buffer_size(self): # real signature unknown; restored from __doc__
        """ parse_buffer_size(self) -> format:Gst.Format, minsize:int, maxsize:int, async:bool """
        pass

    def parse_caps(self): # real signature unknown; restored from __doc__
        """ parse_caps(self) -> caps:Gst.Caps """
        pass

    def parse_flush_stop(self): # real signature unknown; restored from __doc__
        """ parse_flush_stop(self) -> reset_time:bool """
        pass

    def parse_gap(self): # real signature unknown; restored from __doc__
        """ parse_gap(self) -> timestamp:int, duration:int """
        pass

    def parse_group_id(self): # real signature unknown; restored from __doc__
        """ parse_group_id(self) -> bool, group_id:int """
        return False

    def parse_latency(self): # real signature unknown; restored from __doc__
        """ parse_latency(self) -> latency:int """
        pass

    def parse_protection(self): # real signature unknown; restored from __doc__
        """ parse_protection(self) -> system_id:str, data:Gst.Buffer, origin:str """
        pass

    def parse_qos(self): # real signature unknown; restored from __doc__
        """ parse_qos(self) -> type:Gst.QOSType, proportion:float, diff:int, timestamp:int """
        return type(*(), **{})

    def parse_seek(self): # real signature unknown; restored from __doc__
        """ parse_seek(self) -> rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int """
        pass

    def parse_seek_trickmode_interval(self): # real signature unknown; restored from __doc__
        """ parse_seek_trickmode_interval(self) -> interval:int """
        pass

    def parse_segment(self): # real signature unknown; restored from __doc__
        """ parse_segment(self) -> segment:Gst.Segment """
        pass

    def parse_segment_done(self): # real signature unknown; restored from __doc__
        """ parse_segment_done(self) -> format:Gst.Format, position:int """
        pass

    def parse_select_streams(self): # real signature unknown; restored from __doc__
        """ parse_select_streams(self) -> streams:list """
        pass

    def parse_sink_message(self): # real signature unknown; restored from __doc__
        """ parse_sink_message(self) -> msg:Gst.Message """
        pass

    def parse_step(self): # real signature unknown; restored from __doc__
        """ parse_step(self) -> format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool """
        pass

    def parse_stream(self): # real signature unknown; restored from __doc__
        """ parse_stream(self) -> stream:Gst.Stream """
        pass

    def parse_stream_collection(self): # real signature unknown; restored from __doc__
        """ parse_stream_collection(self) -> collection:Gst.StreamCollection """
        pass

    def parse_stream_flags(self): # real signature unknown; restored from __doc__
        """ parse_stream_flags(self) -> flags:Gst.StreamFlags """
        pass

    def parse_stream_group_done(self): # real signature unknown; restored from __doc__
        """ parse_stream_group_done(self) -> group_id:int """
        pass

    def parse_stream_start(self): # real signature unknown; restored from __doc__
        """ parse_stream_start(self) -> stream_id:str """
        pass

    def parse_tag(self): # real signature unknown; restored from __doc__
        """ parse_tag(self) -> taglist:Gst.TagList """
        pass

    def parse_toc(self): # real signature unknown; restored from __doc__
        """ parse_toc(self) -> toc:Gst.Toc, updated:bool """
        pass

    def parse_toc_select(self): # real signature unknown; restored from __doc__
        """ parse_toc_select(self) -> uid:str """
        pass

    def set_group_id(self, group_id): # real signature unknown; restored from __doc__
        """ set_group_id(self, group_id:int) """
        pass

    def set_running_time_offset(self, offset): # real signature unknown; restored from __doc__
        """ set_running_time_offset(self, offset:int) """
        pass

    def set_seek_trickmode_interval(self, interval): # real signature unknown; restored from __doc__
        """ set_seek_trickmode_interval(self, interval:int) """
        pass

    def set_seqnum(self, seqnum): # real signature unknown; restored from __doc__
        """ set_seqnum(self, seqnum:int) """
        pass

    def set_stream(self, stream): # real signature unknown; restored from __doc__
        """ set_stream(self, stream:Gst.Stream) """
        pass

    def set_stream_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_stream_flags(self, flags:Gst.StreamFlags) """
        pass

    def writable_structure(self): # real signature unknown; restored from __doc__
        """ writable_structure(self) -> Gst.Structure """
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

    mini_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seqnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Event), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstEvent (94058977651536)>, '__dict__': <attribute '__dict__' of 'Event' objects>, '__weakref__': <attribute '__weakref__' of 'Event' objects>, '__doc__': None, 'mini_object': <property object at 0x7f4260550cc0>, 'type': <property object at 0x7f4260550db0>, 'timestamp': <property object at 0x7f4260550ea0>, 'seqnum': <property object at 0x7f4260550f90>, 'new_buffer_size': gi.FunctionInfo(new_buffer_size), 'new_caps': gi.FunctionInfo(new_caps), 'new_custom': gi.FunctionInfo(new_custom), 'new_eos': gi.FunctionInfo(new_eos), 'new_flush_start': gi.FunctionInfo(new_flush_start), 'new_flush_stop': gi.FunctionInfo(new_flush_stop), 'new_gap': gi.FunctionInfo(new_gap), 'new_latency': gi.FunctionInfo(new_latency), 'new_navigation': gi.FunctionInfo(new_navigation), 'new_protection': gi.FunctionInfo(new_protection), 'new_qos': gi.FunctionInfo(new_qos), 'new_reconfigure': gi.FunctionInfo(new_reconfigure), 'new_seek': gi.FunctionInfo(new_seek), 'new_segment': gi.FunctionInfo(new_segment), 'new_segment_done': gi.FunctionInfo(new_segment_done), 'new_select_streams': gi.FunctionInfo(new_select_streams), 'new_sink_message': gi.FunctionInfo(new_sink_message), 'new_step': gi.FunctionInfo(new_step), 'new_stream_collection': gi.FunctionInfo(new_stream_collection), 'new_stream_group_done': gi.FunctionInfo(new_stream_group_done), 'new_stream_start': gi.FunctionInfo(new_stream_start), 'new_tag': gi.FunctionInfo(new_tag), 'new_toc': gi.FunctionInfo(new_toc), 'new_toc_select': gi.FunctionInfo(new_toc_select), 'copy_segment': gi.FunctionInfo(copy_segment), 'get_running_time_offset': gi.FunctionInfo(get_running_time_offset), 'get_seqnum': gi.FunctionInfo(get_seqnum), 'get_structure': gi.FunctionInfo(get_structure), 'has_name': gi.FunctionInfo(has_name), 'parse_buffer_size': gi.FunctionInfo(parse_buffer_size), 'parse_caps': gi.FunctionInfo(parse_caps), 'parse_flush_stop': gi.FunctionInfo(parse_flush_stop), 'parse_gap': gi.FunctionInfo(parse_gap), 'parse_group_id': gi.FunctionInfo(parse_group_id), 'parse_latency': gi.FunctionInfo(parse_latency), 'parse_protection': gi.FunctionInfo(parse_protection), 'parse_qos': gi.FunctionInfo(parse_qos), 'parse_seek': gi.FunctionInfo(parse_seek), 'parse_seek_trickmode_interval': gi.FunctionInfo(parse_seek_trickmode_interval), 'parse_segment': gi.FunctionInfo(parse_segment), 'parse_segment_done': gi.FunctionInfo(parse_segment_done), 'parse_select_streams': gi.FunctionInfo(parse_select_streams), 'parse_sink_message': gi.FunctionInfo(parse_sink_message), 'parse_step': gi.FunctionInfo(parse_step), 'parse_stream': gi.FunctionInfo(parse_stream), 'parse_stream_collection': gi.FunctionInfo(parse_stream_collection), 'parse_stream_flags': gi.FunctionInfo(parse_stream_flags), 'parse_stream_group_done': gi.FunctionInfo(parse_stream_group_done), 'parse_stream_start': gi.FunctionInfo(parse_stream_start), 'parse_tag': gi.FunctionInfo(parse_tag), 'parse_toc': gi.FunctionInfo(parse_toc), 'parse_toc_select': gi.FunctionInfo(parse_toc_select), 'set_group_id': gi.FunctionInfo(set_group_id), 'set_running_time_offset': gi.FunctionInfo(set_running_time_offset), 'set_seek_trickmode_interval': gi.FunctionInfo(set_seek_trickmode_interval), 'set_seqnum': gi.FunctionInfo(set_seqnum), 'set_stream': gi.FunctionInfo(set_stream), 'set_stream_flags': gi.FunctionInfo(set_stream_flags), 'writable_structure': gi.FunctionInfo(writable_structure)})"
    __gtype__ = None # (!) real value is '<GType GstEvent (94058977651536)>'
    __info__ = StructInfo(Event)


