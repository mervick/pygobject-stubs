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


class Query(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Query()
        new_accept_caps(caps:Gst.Caps) -> Gst.Query
        new_allocation(caps:Gst.Caps, need_pool:bool) -> Gst.Query
        new_bitrate() -> Gst.Query
        new_buffering(format:Gst.Format) -> Gst.Query
        new_caps(filter:Gst.Caps) -> Gst.Query
        new_context(context_type:str) -> Gst.Query
        new_convert(src_format:Gst.Format, value:int, dest_format:Gst.Format) -> Gst.Query
        new_custom(type:Gst.QueryType, structure:Gst.Structure=None) -> Gst.Query or None
        new_drain() -> Gst.Query
        new_duration(format:Gst.Format) -> Gst.Query
        new_formats() -> Gst.Query
        new_latency() -> Gst.Query
        new_position(format:Gst.Format) -> Gst.Query
        new_scheduling() -> Gst.Query
        new_seeking(format:Gst.Format) -> Gst.Query
        new_segment(format:Gst.Format) -> Gst.Query
        new_uri() -> Gst.Query
    """
    def add_allocation_meta(self, api, params=None): # real signature unknown; restored from __doc__
        """ add_allocation_meta(self, api:GType, params:Gst.Structure=None) """
        pass

    def add_allocation_param(self, allocator=None, params=None): # real signature unknown; restored from __doc__
        """ add_allocation_param(self, allocator:Gst.Allocator=None, params:Gst.AllocationParams=None) """
        pass

    def add_allocation_pool(self, pool=None, size, min_buffers, max_buffers): # real signature unknown; restored from __doc__
        """ add_allocation_pool(self, pool:Gst.BufferPool=None, size:int, min_buffers:int, max_buffers:int) """
        pass

    def add_buffering_range(self, start, stop): # real signature unknown; restored from __doc__
        """ add_buffering_range(self, start:int, stop:int) -> bool """
        return False

    def add_scheduling_mode(self, mode): # real signature unknown; restored from __doc__
        """ add_scheduling_mode(self, mode:Gst.PadMode) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def find_allocation_meta(self, api): # real signature unknown; restored from __doc__
        """ find_allocation_meta(self, api:GType) -> bool, index:int """
        return False

    def get_n_allocation_metas(self): # real signature unknown; restored from __doc__
        """ get_n_allocation_metas(self) -> int """
        return 0

    def get_n_allocation_params(self): # real signature unknown; restored from __doc__
        """ get_n_allocation_params(self) -> int """
        return 0

    def get_n_allocation_pools(self): # real signature unknown; restored from __doc__
        """ get_n_allocation_pools(self) -> int """
        return 0

    def get_n_buffering_ranges(self): # real signature unknown; restored from __doc__
        """ get_n_buffering_ranges(self) -> int """
        return 0

    def get_n_scheduling_modes(self): # real signature unknown; restored from __doc__
        """ get_n_scheduling_modes(self) -> int """
        return 0

    def get_structure(self): # real signature unknown; restored from __doc__
        """ get_structure(self) -> Gst.Structure or None """
        pass

    def has_scheduling_mode(self, mode): # real signature unknown; restored from __doc__
        """ has_scheduling_mode(self, mode:Gst.PadMode) -> bool """
        return False

    def has_scheduling_mode_with_flags(self, mode, flags): # real signature unknown; restored from __doc__
        """ has_scheduling_mode_with_flags(self, mode:Gst.PadMode, flags:Gst.SchedulingFlags) -> bool """
        return False

    def new_accept_caps(self, caps): # real signature unknown; restored from __doc__
        """ new_accept_caps(caps:Gst.Caps) -> Gst.Query """
        pass

    def new_allocation(self, caps, need_pool): # real signature unknown; restored from __doc__
        """ new_allocation(caps:Gst.Caps, need_pool:bool) -> Gst.Query """
        pass

    def new_bitrate(self): # real signature unknown; restored from __doc__
        """ new_bitrate() -> Gst.Query """
        pass

    def new_buffering(self, format): # real signature unknown; restored from __doc__
        """ new_buffering(format:Gst.Format) -> Gst.Query """
        pass

    def new_caps(self, filter): # real signature unknown; restored from __doc__
        """ new_caps(filter:Gst.Caps) -> Gst.Query """
        pass

    def new_context(self, context_type): # real signature unknown; restored from __doc__
        """ new_context(context_type:str) -> Gst.Query """
        pass

    def new_convert(self, src_format, value, dest_format): # real signature unknown; restored from __doc__
        """ new_convert(src_format:Gst.Format, value:int, dest_format:Gst.Format) -> Gst.Query """
        pass

    def new_custom(self, type, structure=None): # real signature unknown; restored from __doc__
        """ new_custom(type:Gst.QueryType, structure:Gst.Structure=None) -> Gst.Query or None """
        pass

    def new_drain(self): # real signature unknown; restored from __doc__
        """ new_drain() -> Gst.Query """
        pass

    def new_duration(self, format): # real signature unknown; restored from __doc__
        """ new_duration(format:Gst.Format) -> Gst.Query """
        pass

    def new_formats(self): # real signature unknown; restored from __doc__
        """ new_formats() -> Gst.Query """
        pass

    def new_latency(self): # real signature unknown; restored from __doc__
        """ new_latency() -> Gst.Query """
        pass

    def new_position(self, format): # real signature unknown; restored from __doc__
        """ new_position(format:Gst.Format) -> Gst.Query """
        pass

    def new_scheduling(self): # real signature unknown; restored from __doc__
        """ new_scheduling() -> Gst.Query """
        pass

    def new_seeking(self, format): # real signature unknown; restored from __doc__
        """ new_seeking(format:Gst.Format) -> Gst.Query """
        pass

    def new_segment(self, format): # real signature unknown; restored from __doc__
        """ new_segment(format:Gst.Format) -> Gst.Query """
        pass

    def new_uri(self): # real signature unknown; restored from __doc__
        """ new_uri() -> Gst.Query """
        pass

    def parse_accept_caps(self): # real signature unknown; restored from __doc__
        """ parse_accept_caps(self) -> caps:Gst.Caps """
        pass

    def parse_accept_caps_result(self): # real signature unknown; restored from __doc__
        """ parse_accept_caps_result(self) -> result:bool """
        pass

    def parse_allocation(self): # real signature unknown; restored from __doc__
        """ parse_allocation(self) -> caps:Gst.Caps, need_pool:bool """
        pass

    def parse_bitrate(self): # real signature unknown; restored from __doc__
        """ parse_bitrate(self) -> nominal_bitrate:int """
        pass

    def parse_buffering_percent(self): # real signature unknown; restored from __doc__
        """ parse_buffering_percent(self) -> busy:bool, percent:int """
        pass

    def parse_buffering_range(self): # real signature unknown; restored from __doc__
        """ parse_buffering_range(self) -> format:Gst.Format, start:int, stop:int, estimated_total:int """
        pass

    def parse_buffering_stats(self): # real signature unknown; restored from __doc__
        """ parse_buffering_stats(self) -> mode:Gst.BufferingMode, avg_in:int, avg_out:int, buffering_left:int """
        pass

    def parse_caps(self): # real signature unknown; restored from __doc__
        """ parse_caps(self) -> filter:Gst.Caps """
        return filter(*(), **{})

    def parse_caps_result(self): # real signature unknown; restored from __doc__
        """ parse_caps_result(self) -> caps:Gst.Caps """
        pass

    def parse_context(self): # real signature unknown; restored from __doc__
        """ parse_context(self) -> context:Gst.Context """
        pass

    def parse_context_type(self): # real signature unknown; restored from __doc__
        """ parse_context_type(self) -> bool, context_type:str """
        return False

    def parse_convert(self): # real signature unknown; restored from __doc__
        """ parse_convert(self) -> src_format:Gst.Format, src_value:int, dest_format:Gst.Format, dest_value:int """
        pass

    def parse_duration(self): # real signature unknown; restored from __doc__
        """ parse_duration(self) -> format:Gst.Format, duration:int """
        pass

    def parse_latency(self): # real signature unknown; restored from __doc__
        """ parse_latency(self) -> live:bool, min_latency:int, max_latency:int """
        pass

    def parse_nth_allocation_meta(self, index): # real signature unknown; restored from __doc__
        """ parse_nth_allocation_meta(self, index:int) -> GType, params:Gst.Structure """
        pass

    def parse_nth_allocation_param(self, index): # real signature unknown; restored from __doc__
        """ parse_nth_allocation_param(self, index:int) -> allocator:Gst.Allocator, params:Gst.AllocationParams """
        pass

    def parse_nth_allocation_pool(self, index): # real signature unknown; restored from __doc__
        """ parse_nth_allocation_pool(self, index:int) -> pool:Gst.BufferPool, size:int, min_buffers:int, max_buffers:int """
        pass

    def parse_nth_buffering_range(self, index): # real signature unknown; restored from __doc__
        """ parse_nth_buffering_range(self, index:int) -> bool, start:int, stop:int """
        return False

    def parse_nth_format(self, nth): # real signature unknown; restored from __doc__
        """ parse_nth_format(self, nth:int) -> format:Gst.Format """
        pass

    def parse_nth_scheduling_mode(self, index): # real signature unknown; restored from __doc__
        """ parse_nth_scheduling_mode(self, index:int) -> Gst.PadMode """
        pass

    def parse_n_formats(self): # real signature unknown; restored from __doc__
        """ parse_n_formats(self) -> n_formats:int """
        pass

    def parse_position(self): # real signature unknown; restored from __doc__
        """ parse_position(self) -> format:Gst.Format, cur:int """
        pass

    def parse_scheduling(self): # real signature unknown; restored from __doc__
        """ parse_scheduling(self) -> flags:Gst.SchedulingFlags, minsize:int, maxsize:int, align:int """
        pass

    def parse_seeking(self): # real signature unknown; restored from __doc__
        """ parse_seeking(self) -> format:Gst.Format, seekable:bool, segment_start:int, segment_end:int """
        pass

    def parse_segment(self): # real signature unknown; restored from __doc__
        """ parse_segment(self) -> rate:float, format:Gst.Format, start_value:int, stop_value:int """
        pass

    def parse_uri(self): # real signature unknown; restored from __doc__
        """ parse_uri(self) -> uri:str """
        pass

    def parse_uri_redirection(self): # real signature unknown; restored from __doc__
        """ parse_uri_redirection(self) -> uri:str """
        pass

    def parse_uri_redirection_permanent(self): # real signature unknown; restored from __doc__
        """ parse_uri_redirection_permanent(self) -> permanent:bool """
        pass

    def remove_nth_allocation_meta(self, index): # real signature unknown; restored from __doc__
        """ remove_nth_allocation_meta(self, index:int) """
        pass

    def remove_nth_allocation_param(self, index): # real signature unknown; restored from __doc__
        """ remove_nth_allocation_param(self, index:int) """
        pass

    def remove_nth_allocation_pool(self, index): # real signature unknown; restored from __doc__
        """ remove_nth_allocation_pool(self, index:int) """
        pass

    def set_accept_caps_result(self, result): # real signature unknown; restored from __doc__
        """ set_accept_caps_result(self, result:bool) """
        pass

    def set_bitrate(self, nominal_bitrate): # real signature unknown; restored from __doc__
        """ set_bitrate(self, nominal_bitrate:int) """
        pass

    def set_buffering_percent(self, busy, percent): # real signature unknown; restored from __doc__
        """ set_buffering_percent(self, busy:bool, percent:int) """
        pass

    def set_buffering_range(self, format, start, stop, estimated_total): # real signature unknown; restored from __doc__
        """ set_buffering_range(self, format:Gst.Format, start:int, stop:int, estimated_total:int) """
        pass

    def set_buffering_stats(self, mode, avg_in, avg_out, buffering_left): # real signature unknown; restored from __doc__
        """ set_buffering_stats(self, mode:Gst.BufferingMode, avg_in:int, avg_out:int, buffering_left:int) """
        pass

    def set_caps_result(self, caps): # real signature unknown; restored from __doc__
        """ set_caps_result(self, caps:Gst.Caps) """
        pass

    def set_context(self, context): # real signature unknown; restored from __doc__
        """ set_context(self, context:Gst.Context) """
        pass

    def set_convert(self, src_format, src_value, dest_format, dest_value): # real signature unknown; restored from __doc__
        """ set_convert(self, src_format:Gst.Format, src_value:int, dest_format:Gst.Format, dest_value:int) """
        pass

    def set_duration(self, format, duration): # real signature unknown; restored from __doc__
        """ set_duration(self, format:Gst.Format, duration:int) """
        pass

    def set_formatsv(self, formats): # real signature unknown; restored from __doc__
        """ set_formatsv(self, formats:list) """
        pass

    def set_latency(self, live, min_latency, max_latency): # real signature unknown; restored from __doc__
        """ set_latency(self, live:bool, min_latency:int, max_latency:int) """
        pass

    def set_nth_allocation_param(self, index, allocator=None, params=None): # real signature unknown; restored from __doc__
        """ set_nth_allocation_param(self, index:int, allocator:Gst.Allocator=None, params:Gst.AllocationParams=None) """
        pass

    def set_nth_allocation_pool(self, index, pool=None, size, min_buffers, max_buffers): # real signature unknown; restored from __doc__
        """ set_nth_allocation_pool(self, index:int, pool:Gst.BufferPool=None, size:int, min_buffers:int, max_buffers:int) """
        pass

    def set_position(self, format, cur): # real signature unknown; restored from __doc__
        """ set_position(self, format:Gst.Format, cur:int) """
        pass

    def set_scheduling(self, flags, minsize, maxsize, align): # real signature unknown; restored from __doc__
        """ set_scheduling(self, flags:Gst.SchedulingFlags, minsize:int, maxsize:int, align:int) """
        pass

    def set_seeking(self, format, seekable, segment_start, segment_end): # real signature unknown; restored from __doc__
        """ set_seeking(self, format:Gst.Format, seekable:bool, segment_start:int, segment_end:int) """
        pass

    def set_segment(self, rate, format, start_value, stop_value): # real signature unknown; restored from __doc__
        """ set_segment(self, rate:float, format:Gst.Format, start_value:int, stop_value:int) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) """
        pass

    def set_uri_redirection(self, uri): # real signature unknown; restored from __doc__
        """ set_uri_redirection(self, uri:str) """
        pass

    def set_uri_redirection_permanent(self, permanent): # real signature unknown; restored from __doc__
        """ set_uri_redirection_permanent(self, permanent:bool) """
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

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Query), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstQuery (94058977895936)>, '__dict__': <attribute '__dict__' of 'Query' objects>, '__weakref__': <attribute '__weakref__' of 'Query' objects>, '__doc__': None, 'mini_object': <property object at 0x7f4260549900>, 'type': <property object at 0x7f426050f0e0>, 'new_accept_caps': gi.FunctionInfo(new_accept_caps), 'new_allocation': gi.FunctionInfo(new_allocation), 'new_bitrate': gi.FunctionInfo(new_bitrate), 'new_buffering': gi.FunctionInfo(new_buffering), 'new_caps': gi.FunctionInfo(new_caps), 'new_context': gi.FunctionInfo(new_context), 'new_convert': gi.FunctionInfo(new_convert), 'new_custom': gi.FunctionInfo(new_custom), 'new_drain': gi.FunctionInfo(new_drain), 'new_duration': gi.FunctionInfo(new_duration), 'new_formats': gi.FunctionInfo(new_formats), 'new_latency': gi.FunctionInfo(new_latency), 'new_position': gi.FunctionInfo(new_position), 'new_scheduling': gi.FunctionInfo(new_scheduling), 'new_seeking': gi.FunctionInfo(new_seeking), 'new_segment': gi.FunctionInfo(new_segment), 'new_uri': gi.FunctionInfo(new_uri), 'add_allocation_meta': gi.FunctionInfo(add_allocation_meta), 'add_allocation_param': gi.FunctionInfo(add_allocation_param), 'add_allocation_pool': gi.FunctionInfo(add_allocation_pool), 'add_buffering_range': gi.FunctionInfo(add_buffering_range), 'add_scheduling_mode': gi.FunctionInfo(add_scheduling_mode), 'find_allocation_meta': gi.FunctionInfo(find_allocation_meta), 'get_n_allocation_metas': gi.FunctionInfo(get_n_allocation_metas), 'get_n_allocation_params': gi.FunctionInfo(get_n_allocation_params), 'get_n_allocation_pools': gi.FunctionInfo(get_n_allocation_pools), 'get_n_buffering_ranges': gi.FunctionInfo(get_n_buffering_ranges), 'get_n_scheduling_modes': gi.FunctionInfo(get_n_scheduling_modes), 'get_structure': gi.FunctionInfo(get_structure), 'has_scheduling_mode': gi.FunctionInfo(has_scheduling_mode), 'has_scheduling_mode_with_flags': gi.FunctionInfo(has_scheduling_mode_with_flags), 'parse_accept_caps': gi.FunctionInfo(parse_accept_caps), 'parse_accept_caps_result': gi.FunctionInfo(parse_accept_caps_result), 'parse_allocation': gi.FunctionInfo(parse_allocation), 'parse_bitrate': gi.FunctionInfo(parse_bitrate), 'parse_buffering_percent': gi.FunctionInfo(parse_buffering_percent), 'parse_buffering_range': gi.FunctionInfo(parse_buffering_range), 'parse_buffering_stats': gi.FunctionInfo(parse_buffering_stats), 'parse_caps': gi.FunctionInfo(parse_caps), 'parse_caps_result': gi.FunctionInfo(parse_caps_result), 'parse_context': gi.FunctionInfo(parse_context), 'parse_context_type': gi.FunctionInfo(parse_context_type), 'parse_convert': gi.FunctionInfo(parse_convert), 'parse_duration': gi.FunctionInfo(parse_duration), 'parse_latency': gi.FunctionInfo(parse_latency), 'parse_n_formats': gi.FunctionInfo(parse_n_formats), 'parse_nth_allocation_meta': gi.FunctionInfo(parse_nth_allocation_meta), 'parse_nth_allocation_param': gi.FunctionInfo(parse_nth_allocation_param), 'parse_nth_allocation_pool': gi.FunctionInfo(parse_nth_allocation_pool), 'parse_nth_buffering_range': gi.FunctionInfo(parse_nth_buffering_range), 'parse_nth_format': gi.FunctionInfo(parse_nth_format), 'parse_nth_scheduling_mode': gi.FunctionInfo(parse_nth_scheduling_mode), 'parse_position': gi.FunctionInfo(parse_position), 'parse_scheduling': gi.FunctionInfo(parse_scheduling), 'parse_seeking': gi.FunctionInfo(parse_seeking), 'parse_segment': gi.FunctionInfo(parse_segment), 'parse_uri': gi.FunctionInfo(parse_uri), 'parse_uri_redirection': gi.FunctionInfo(parse_uri_redirection), 'parse_uri_redirection_permanent': gi.FunctionInfo(parse_uri_redirection_permanent), 'remove_nth_allocation_meta': gi.FunctionInfo(remove_nth_allocation_meta), 'remove_nth_allocation_param': gi.FunctionInfo(remove_nth_allocation_param), 'remove_nth_allocation_pool': gi.FunctionInfo(remove_nth_allocation_pool), 'set_accept_caps_result': gi.FunctionInfo(set_accept_caps_result), 'set_bitrate': gi.FunctionInfo(set_bitrate), 'set_buffering_percent': gi.FunctionInfo(set_buffering_percent), 'set_buffering_range': gi.FunctionInfo(set_buffering_range), 'set_buffering_stats': gi.FunctionInfo(set_buffering_stats), 'set_caps_result': gi.FunctionInfo(set_caps_result), 'set_context': gi.FunctionInfo(set_context), 'set_convert': gi.FunctionInfo(set_convert), 'set_duration': gi.FunctionInfo(set_duration), 'set_formatsv': gi.FunctionInfo(set_formatsv), 'set_latency': gi.FunctionInfo(set_latency), 'set_nth_allocation_param': gi.FunctionInfo(set_nth_allocation_param), 'set_nth_allocation_pool': gi.FunctionInfo(set_nth_allocation_pool), 'set_position': gi.FunctionInfo(set_position), 'set_scheduling': gi.FunctionInfo(set_scheduling), 'set_seeking': gi.FunctionInfo(set_seeking), 'set_segment': gi.FunctionInfo(set_segment), 'set_uri': gi.FunctionInfo(set_uri), 'set_uri_redirection': gi.FunctionInfo(set_uri_redirection), 'set_uri_redirection_permanent': gi.FunctionInfo(set_uri_redirection_permanent), 'writable_structure': gi.FunctionInfo(writable_structure)})"
    __gtype__ = None # (!) real value is '<GType GstQuery (94058977895936)>'
    __info__ = StructInfo(Query)


