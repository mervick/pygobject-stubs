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


class Message(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Message()
        new_application(src:Gst.Object=None, structure:Gst.Structure) -> Gst.Message or None
        new_async_done(src:Gst.Object=None, running_time:int) -> Gst.Message
        new_async_start(src:Gst.Object=None) -> Gst.Message
        new_buffering(src:Gst.Object=None, percent:int) -> Gst.Message or None
        new_clock_lost(src:Gst.Object=None, clock:Gst.Clock) -> Gst.Message
        new_clock_provide(src:Gst.Object=None, clock:Gst.Clock, ready:bool) -> Gst.Message
        new_custom(type:Gst.MessageType, src:Gst.Object=None, structure:Gst.Structure=None) -> Gst.Message or None
        new_device_added(src:Gst.Object, device:Gst.Device) -> Gst.Message
        new_device_changed(src:Gst.Object, device:Gst.Device, changed_device:Gst.Device) -> Gst.Message
        new_device_removed(src:Gst.Object, device:Gst.Device) -> Gst.Message
        new_duration_changed(src:Gst.Object=None) -> Gst.Message
        new_element(src:Gst.Object=None, structure:Gst.Structure) -> Gst.Message or None
        new_eos(src:Gst.Object=None) -> Gst.Message
        new_error(src:Gst.Object=None, error:error, debug:str) -> Gst.Message
        new_error_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message or None
        new_have_context(src:Gst.Object=None, context:Gst.Context) -> Gst.Message
        new_info(src:Gst.Object=None, error:error, debug:str) -> Gst.Message
        new_info_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message or None
        new_latency(src:Gst.Object=None) -> Gst.Message
        new_need_context(src:Gst.Object=None, context_type:str) -> Gst.Message
        new_new_clock(src:Gst.Object=None, clock:Gst.Clock) -> Gst.Message
        new_progress(src:Gst.Object, type:Gst.ProgressType, code:str, text:str) -> Gst.Message or None
        new_property_notify(src:Gst.Object, property_name:str, val:GObject.Value=None) -> Gst.Message
        new_qos(src:Gst.Object, live:bool, running_time:int, stream_time:int, timestamp:int, duration:int) -> Gst.Message
        new_redirect(src:Gst.Object, location:str, tag_list:Gst.TagList=None, entry_struct:Gst.Structure=None) -> Gst.Message
        new_request_state(src:Gst.Object=None, state:Gst.State) -> Gst.Message
        new_reset_time(src:Gst.Object=None, running_time:int) -> Gst.Message
        new_segment_done(src:Gst.Object=None, format:Gst.Format, position:int) -> Gst.Message
        new_segment_start(src:Gst.Object=None, format:Gst.Format, position:int) -> Gst.Message
        new_state_changed(src:Gst.Object=None, oldstate:Gst.State, newstate:Gst.State, pending:Gst.State) -> Gst.Message
        new_state_dirty(src:Gst.Object=None) -> Gst.Message
        new_step_done(src:Gst.Object, format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool, duration:int, eos:bool) -> Gst.Message
        new_step_start(src:Gst.Object, active:bool, format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool) -> Gst.Message
        new_stream_collection(src:Gst.Object, collection:Gst.StreamCollection) -> Gst.Message
        new_stream_start(src:Gst.Object=None) -> Gst.Message
        new_stream_status(src:Gst.Object, type:Gst.StreamStatusType, owner:Gst.Element) -> Gst.Message
        new_streams_selected(src:Gst.Object, collection:Gst.StreamCollection) -> Gst.Message
        new_structure_change(src:Gst.Object=None, type:Gst.StructureChangeType, owner:Gst.Element, busy:bool) -> Gst.Message
        new_tag(src:Gst.Object=None, tag_list:Gst.TagList) -> Gst.Message
        new_toc(src:Gst.Object, toc:Gst.Toc, updated:bool) -> Gst.Message
        new_warning(src:Gst.Object=None, error:error, debug:str) -> Gst.Message
        new_warning_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message or None
    """
    def add_redirect_entry(self, location, tag_list=None, entry_struct=None): # real signature unknown; restored from __doc__
        """ add_redirect_entry(self, location:str, tag_list:Gst.TagList=None, entry_struct:Gst.Structure=None) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_redirect_entries(self): # real signature unknown; restored from __doc__
        """ get_num_redirect_entries(self) -> int """
        return 0

    def get_seqnum(self): # real signature unknown; restored from __doc__
        """ get_seqnum(self) -> int """
        return 0

    def get_stream_status_object(self): # real signature unknown; restored from __doc__
        """ get_stream_status_object(self) -> GObject.Value or None """
        pass

    def get_structure(self): # real signature unknown; restored from __doc__
        """ get_structure(self) -> Gst.Structure or None """
        pass

    def has_name(self, name): # real signature unknown; restored from __doc__
        """ has_name(self, name:str) -> bool """
        return False

    def new_application(self, src=None, structure): # real signature unknown; restored from __doc__
        """ new_application(src:Gst.Object=None, structure:Gst.Structure) -> Gst.Message or None """
        pass

    def new_async_done(self, src=None, running_time): # real signature unknown; restored from __doc__
        """ new_async_done(src:Gst.Object=None, running_time:int) -> Gst.Message """
        pass

    def new_async_start(self, src=None): # real signature unknown; restored from __doc__
        """ new_async_start(src:Gst.Object=None) -> Gst.Message """
        pass

    def new_buffering(self, src=None, percent): # real signature unknown; restored from __doc__
        """ new_buffering(src:Gst.Object=None, percent:int) -> Gst.Message or None """
        pass

    def new_clock_lost(self, src=None, clock): # real signature unknown; restored from __doc__
        """ new_clock_lost(src:Gst.Object=None, clock:Gst.Clock) -> Gst.Message """
        pass

    def new_clock_provide(self, src=None, clock, ready): # real signature unknown; restored from __doc__
        """ new_clock_provide(src:Gst.Object=None, clock:Gst.Clock, ready:bool) -> Gst.Message """
        pass

    def new_custom(self, type, src=None, structure=None): # real signature unknown; restored from __doc__
        """ new_custom(type:Gst.MessageType, src:Gst.Object=None, structure:Gst.Structure=None) -> Gst.Message or None """
        pass

    def new_device_added(self, src, device): # real signature unknown; restored from __doc__
        """ new_device_added(src:Gst.Object, device:Gst.Device) -> Gst.Message """
        pass

    def new_device_changed(self, src, device, changed_device): # real signature unknown; restored from __doc__
        """ new_device_changed(src:Gst.Object, device:Gst.Device, changed_device:Gst.Device) -> Gst.Message """
        pass

    def new_device_removed(self, src, device): # real signature unknown; restored from __doc__
        """ new_device_removed(src:Gst.Object, device:Gst.Device) -> Gst.Message """
        pass

    def new_duration_changed(self, src=None): # real signature unknown; restored from __doc__
        """ new_duration_changed(src:Gst.Object=None) -> Gst.Message """
        pass

    def new_element(self, src=None, structure): # real signature unknown; restored from __doc__
        """ new_element(src:Gst.Object=None, structure:Gst.Structure) -> Gst.Message or None """
        pass

    def new_eos(self, src=None): # real signature unknown; restored from __doc__
        """ new_eos(src:Gst.Object=None) -> Gst.Message """
        pass

    def new_error(self, src=None, error, debug): # real signature unknown; restored from __doc__
        """ new_error(src:Gst.Object=None, error:error, debug:str) -> Gst.Message """
        pass

    def new_error_with_details(self, src=None, error, debug, details=None): # real signature unknown; restored from __doc__
        """ new_error_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message or None """
        pass

    def new_have_context(self, src=None, context): # real signature unknown; restored from __doc__
        """ new_have_context(src:Gst.Object=None, context:Gst.Context) -> Gst.Message """
        pass

    def new_info(self, src=None, error, debug): # real signature unknown; restored from __doc__
        """ new_info(src:Gst.Object=None, error:error, debug:str) -> Gst.Message """
        pass

    def new_info_with_details(self, src=None, error, debug, details=None): # real signature unknown; restored from __doc__
        """ new_info_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message or None """
        pass

    def new_latency(self, src=None): # real signature unknown; restored from __doc__
        """ new_latency(src:Gst.Object=None) -> Gst.Message """
        pass

    def new_need_context(self, src=None, context_type): # real signature unknown; restored from __doc__
        """ new_need_context(src:Gst.Object=None, context_type:str) -> Gst.Message """
        pass

    def new_new_clock(self, src=None, clock): # real signature unknown; restored from __doc__
        """ new_new_clock(src:Gst.Object=None, clock:Gst.Clock) -> Gst.Message """
        pass

    def new_progress(self, src, type, code, text): # real signature unknown; restored from __doc__
        """ new_progress(src:Gst.Object, type:Gst.ProgressType, code:str, text:str) -> Gst.Message or None """
        pass

    def new_property_notify(self, src, property_name, val=None): # real signature unknown; restored from __doc__
        """ new_property_notify(src:Gst.Object, property_name:str, val:GObject.Value=None) -> Gst.Message """
        pass

    def new_qos(self, src, live, running_time, stream_time, timestamp, duration): # real signature unknown; restored from __doc__
        """ new_qos(src:Gst.Object, live:bool, running_time:int, stream_time:int, timestamp:int, duration:int) -> Gst.Message """
        pass

    def new_redirect(self, src, location, tag_list=None, entry_struct=None): # real signature unknown; restored from __doc__
        """ new_redirect(src:Gst.Object, location:str, tag_list:Gst.TagList=None, entry_struct:Gst.Structure=None) -> Gst.Message """
        pass

    def new_request_state(self, src=None, state): # real signature unknown; restored from __doc__
        """ new_request_state(src:Gst.Object=None, state:Gst.State) -> Gst.Message """
        pass

    def new_reset_time(self, src=None, running_time): # real signature unknown; restored from __doc__
        """ new_reset_time(src:Gst.Object=None, running_time:int) -> Gst.Message """
        pass

    def new_segment_done(self, src=None, format, position): # real signature unknown; restored from __doc__
        """ new_segment_done(src:Gst.Object=None, format:Gst.Format, position:int) -> Gst.Message """
        pass

    def new_segment_start(self, src=None, format, position): # real signature unknown; restored from __doc__
        """ new_segment_start(src:Gst.Object=None, format:Gst.Format, position:int) -> Gst.Message """
        pass

    def new_state_changed(self, src=None, oldstate, newstate, pending): # real signature unknown; restored from __doc__
        """ new_state_changed(src:Gst.Object=None, oldstate:Gst.State, newstate:Gst.State, pending:Gst.State) -> Gst.Message """
        pass

    def new_state_dirty(self, src=None): # real signature unknown; restored from __doc__
        """ new_state_dirty(src:Gst.Object=None) -> Gst.Message """
        pass

    def new_step_done(self, src, format, amount, rate, flush, intermediate, duration, eos): # real signature unknown; restored from __doc__
        """ new_step_done(src:Gst.Object, format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool, duration:int, eos:bool) -> Gst.Message """
        pass

    def new_step_start(self, src, active, format, amount, rate, flush, intermediate): # real signature unknown; restored from __doc__
        """ new_step_start(src:Gst.Object, active:bool, format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool) -> Gst.Message """
        pass

    def new_streams_selected(self, src, collection): # real signature unknown; restored from __doc__
        """ new_streams_selected(src:Gst.Object, collection:Gst.StreamCollection) -> Gst.Message """
        pass

    def new_stream_collection(self, src, collection): # real signature unknown; restored from __doc__
        """ new_stream_collection(src:Gst.Object, collection:Gst.StreamCollection) -> Gst.Message """
        pass

    def new_stream_start(self, src=None): # real signature unknown; restored from __doc__
        """ new_stream_start(src:Gst.Object=None) -> Gst.Message """
        pass

    def new_stream_status(self, src, type, owner): # real signature unknown; restored from __doc__
        """ new_stream_status(src:Gst.Object, type:Gst.StreamStatusType, owner:Gst.Element) -> Gst.Message """
        pass

    def new_structure_change(self, src=None, type, owner, busy): # real signature unknown; restored from __doc__
        """ new_structure_change(src:Gst.Object=None, type:Gst.StructureChangeType, owner:Gst.Element, busy:bool) -> Gst.Message """
        pass

    def new_tag(self, src=None, tag_list): # real signature unknown; restored from __doc__
        """ new_tag(src:Gst.Object=None, tag_list:Gst.TagList) -> Gst.Message """
        pass

    def new_toc(self, src, toc, updated): # real signature unknown; restored from __doc__
        """ new_toc(src:Gst.Object, toc:Gst.Toc, updated:bool) -> Gst.Message """
        pass

    def new_warning(self, src=None, error, debug): # real signature unknown; restored from __doc__
        """ new_warning(src:Gst.Object=None, error:error, debug:str) -> Gst.Message """
        pass

    def new_warning_with_details(self, src=None, error, debug, details=None): # real signature unknown; restored from __doc__
        """ new_warning_with_details(src:Gst.Object=None, error:error, debug:str, details:Gst.Structure=None) -> Gst.Message or None """
        pass

    def parse_async_done(self): # real signature unknown; restored from __doc__
        """ parse_async_done(self) -> running_time:int """
        pass

    def parse_buffering(self): # real signature unknown; restored from __doc__
        """ parse_buffering(self) -> percent:int """
        pass

    def parse_buffering_stats(self): # real signature unknown; restored from __doc__
        """ parse_buffering_stats(self) -> mode:Gst.BufferingMode, avg_in:int, avg_out:int, buffering_left:int """
        pass

    def parse_clock_lost(self): # real signature unknown; restored from __doc__
        """ parse_clock_lost(self) -> clock:Gst.Clock """
        pass

    def parse_clock_provide(self): # real signature unknown; restored from __doc__
        """ parse_clock_provide(self) -> clock:Gst.Clock, ready:bool """
        pass

    def parse_context_type(self): # real signature unknown; restored from __doc__
        """ parse_context_type(self) -> bool, context_type:str """
        return False

    def parse_device_added(self): # real signature unknown; restored from __doc__
        """ parse_device_added(self) -> device:Gst.Device """
        pass

    def parse_device_changed(self): # real signature unknown; restored from __doc__
        """ parse_device_changed(self) -> device:Gst.Device, changed_device:Gst.Device """
        pass

    def parse_device_removed(self): # real signature unknown; restored from __doc__
        """ parse_device_removed(self) -> device:Gst.Device """
        pass

    def parse_error(self): # real signature unknown; restored from __doc__
        """ parse_error(self) -> gerror:error, debug:str """
        pass

    def parse_error_details(self): # real signature unknown; restored from __doc__
        """ parse_error_details(self) -> structure:Gst.Structure """
        pass

    def parse_group_id(self): # real signature unknown; restored from __doc__
        """ parse_group_id(self) -> bool, group_id:int """
        return False

    def parse_have_context(self): # real signature unknown; restored from __doc__
        """ parse_have_context(self) -> context:Gst.Context """
        pass

    def parse_info(self): # real signature unknown; restored from __doc__
        """ parse_info(self) -> gerror:error, debug:str """
        pass

    def parse_info_details(self): # real signature unknown; restored from __doc__
        """ parse_info_details(self) -> structure:Gst.Structure """
        pass

    def parse_new_clock(self): # real signature unknown; restored from __doc__
        """ parse_new_clock(self) -> clock:Gst.Clock """
        pass

    def parse_progress(self): # real signature unknown; restored from __doc__
        """ parse_progress(self) -> type:Gst.ProgressType, code:str, text:str """
        return type(*(), **{})

    def parse_property_notify(self): # real signature unknown; restored from __doc__
        """ parse_property_notify(self) -> object:Gst.Object, property_name:str, property_value:GObject.Value """
        return object()

    def parse_qos(self): # real signature unknown; restored from __doc__
        """ parse_qos(self) -> live:bool, running_time:int, stream_time:int, timestamp:int, duration:int """
        pass

    def parse_qos_stats(self): # real signature unknown; restored from __doc__
        """ parse_qos_stats(self) -> format:Gst.Format, processed:int, dropped:int """
        pass

    def parse_qos_values(self): # real signature unknown; restored from __doc__
        """ parse_qos_values(self) -> jitter:int, proportion:float, quality:int """
        pass

    def parse_redirect_entry(self, entry_index): # real signature unknown; restored from __doc__
        """ parse_redirect_entry(self, entry_index:int) -> location:str, tag_list:Gst.TagList, entry_struct:Gst.Structure """
        pass

    def parse_request_state(self): # real signature unknown; restored from __doc__
        """ parse_request_state(self) -> state:Gst.State """
        pass

    def parse_reset_time(self): # real signature unknown; restored from __doc__
        """ parse_reset_time(self) -> running_time:int """
        pass

    def parse_segment_done(self): # real signature unknown; restored from __doc__
        """ parse_segment_done(self) -> format:Gst.Format, position:int """
        pass

    def parse_segment_start(self): # real signature unknown; restored from __doc__
        """ parse_segment_start(self) -> format:Gst.Format, position:int """
        pass

    def parse_state_changed(self): # real signature unknown; restored from __doc__
        """ parse_state_changed(self) -> oldstate:Gst.State, newstate:Gst.State, pending:Gst.State """
        pass

    def parse_step_done(self): # real signature unknown; restored from __doc__
        """ parse_step_done(self) -> format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool, duration:int, eos:bool """
        pass

    def parse_step_start(self): # real signature unknown; restored from __doc__
        """ parse_step_start(self) -> active:bool, format:Gst.Format, amount:int, rate:float, flush:bool, intermediate:bool """
        pass

    def parse_streams_selected(self): # real signature unknown; restored from __doc__
        """ parse_streams_selected(self) -> collection:Gst.StreamCollection """
        pass

    def parse_stream_collection(self): # real signature unknown; restored from __doc__
        """ parse_stream_collection(self) -> collection:Gst.StreamCollection """
        pass

    def parse_stream_status(self): # real signature unknown; restored from __doc__
        """ parse_stream_status(self) -> type:Gst.StreamStatusType, owner:Gst.Element """
        return type(*(), **{})

    def parse_structure_change(self): # real signature unknown; restored from __doc__
        """ parse_structure_change(self) -> type:Gst.StructureChangeType, owner:Gst.Element, busy:bool """
        return type(*(), **{})

    def parse_tag(self): # real signature unknown; restored from __doc__
        """ parse_tag(self) -> tag_list:Gst.TagList """
        pass

    def parse_toc(self): # real signature unknown; restored from __doc__
        """ parse_toc(self) -> toc:Gst.Toc, updated:bool """
        pass

    def parse_warning(self): # real signature unknown; restored from __doc__
        """ parse_warning(self) -> gerror:error, debug:str """
        pass

    def parse_warning_details(self): # real signature unknown; restored from __doc__
        """ parse_warning_details(self) -> structure:Gst.Structure """
        pass

    def set_buffering_stats(self, mode, avg_in, avg_out, buffering_left): # real signature unknown; restored from __doc__
        """ set_buffering_stats(self, mode:Gst.BufferingMode, avg_in:int, avg_out:int, buffering_left:int) """
        pass

    def set_group_id(self, group_id): # real signature unknown; restored from __doc__
        """ set_group_id(self, group_id:int) """
        pass

    def set_qos_stats(self, format, processed, dropped): # real signature unknown; restored from __doc__
        """ set_qos_stats(self, format:Gst.Format, processed:int, dropped:int) """
        pass

    def set_qos_values(self, jitter, proportion, quality): # real signature unknown; restored from __doc__
        """ set_qos_values(self, jitter:int, proportion:float, quality:int) """
        pass

    def set_seqnum(self, seqnum): # real signature unknown; restored from __doc__
        """ set_seqnum(self, seqnum:int) """
        pass

    def set_stream_status_object(self, p_object): # real signature unknown; restored from __doc__
        """ set_stream_status_object(self, object:GObject.Value) """
        pass

    def streams_selected_add(self, stream): # real signature unknown; restored from __doc__
        """ streams_selected_add(self, stream:Gst.Stream) """
        pass

    def streams_selected_get_size(self): # real signature unknown; restored from __doc__
        """ streams_selected_get_size(self) -> int """
        return 0

    def streams_selected_get_stream(self, idx): # real signature unknown; restored from __doc__
        """ streams_selected_get_stream(self, idx:int) -> Gst.Stream or None """
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

    cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mini_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seqnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    src = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Message), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstMessage (94058977341952)>, '__dict__': <attribute '__dict__' of 'Message' objects>, '__weakref__': <attribute '__weakref__' of 'Message' objects>, '__doc__': None, 'mini_object': <property object at 0x7f4260567180>, 'type': <property object at 0x7f4260567270>, 'timestamp': <property object at 0x7f4260567360>, 'src': <property object at 0x7f4260567450>, 'seqnum': <property object at 0x7f4260567540>, 'lock': <property object at 0x7f4260567630>, 'cond': <property object at 0x7f4260567720>, 'new_application': gi.FunctionInfo(new_application), 'new_async_done': gi.FunctionInfo(new_async_done), 'new_async_start': gi.FunctionInfo(new_async_start), 'new_buffering': gi.FunctionInfo(new_buffering), 'new_clock_lost': gi.FunctionInfo(new_clock_lost), 'new_clock_provide': gi.FunctionInfo(new_clock_provide), 'new_custom': gi.FunctionInfo(new_custom), 'new_device_added': gi.FunctionInfo(new_device_added), 'new_device_changed': gi.FunctionInfo(new_device_changed), 'new_device_removed': gi.FunctionInfo(new_device_removed), 'new_duration_changed': gi.FunctionInfo(new_duration_changed), 'new_element': gi.FunctionInfo(new_element), 'new_eos': gi.FunctionInfo(new_eos), 'new_error': gi.FunctionInfo(new_error), 'new_error_with_details': gi.FunctionInfo(new_error_with_details), 'new_have_context': gi.FunctionInfo(new_have_context), 'new_info': gi.FunctionInfo(new_info), 'new_info_with_details': gi.FunctionInfo(new_info_with_details), 'new_latency': gi.FunctionInfo(new_latency), 'new_need_context': gi.FunctionInfo(new_need_context), 'new_new_clock': gi.FunctionInfo(new_new_clock), 'new_progress': gi.FunctionInfo(new_progress), 'new_property_notify': gi.FunctionInfo(new_property_notify), 'new_qos': gi.FunctionInfo(new_qos), 'new_redirect': gi.FunctionInfo(new_redirect), 'new_request_state': gi.FunctionInfo(new_request_state), 'new_reset_time': gi.FunctionInfo(new_reset_time), 'new_segment_done': gi.FunctionInfo(new_segment_done), 'new_segment_start': gi.FunctionInfo(new_segment_start), 'new_state_changed': gi.FunctionInfo(new_state_changed), 'new_state_dirty': gi.FunctionInfo(new_state_dirty), 'new_step_done': gi.FunctionInfo(new_step_done), 'new_step_start': gi.FunctionInfo(new_step_start), 'new_stream_collection': gi.FunctionInfo(new_stream_collection), 'new_stream_start': gi.FunctionInfo(new_stream_start), 'new_stream_status': gi.FunctionInfo(new_stream_status), 'new_streams_selected': gi.FunctionInfo(new_streams_selected), 'new_structure_change': gi.FunctionInfo(new_structure_change), 'new_tag': gi.FunctionInfo(new_tag), 'new_toc': gi.FunctionInfo(new_toc), 'new_warning': gi.FunctionInfo(new_warning), 'new_warning_with_details': gi.FunctionInfo(new_warning_with_details), 'add_redirect_entry': gi.FunctionInfo(add_redirect_entry), 'get_num_redirect_entries': gi.FunctionInfo(get_num_redirect_entries), 'get_seqnum': gi.FunctionInfo(get_seqnum), 'get_stream_status_object': gi.FunctionInfo(get_stream_status_object), 'get_structure': gi.FunctionInfo(get_structure), 'has_name': gi.FunctionInfo(has_name), 'parse_async_done': gi.FunctionInfo(parse_async_done), 'parse_buffering': gi.FunctionInfo(parse_buffering), 'parse_buffering_stats': gi.FunctionInfo(parse_buffering_stats), 'parse_clock_lost': gi.FunctionInfo(parse_clock_lost), 'parse_clock_provide': gi.FunctionInfo(parse_clock_provide), 'parse_context_type': gi.FunctionInfo(parse_context_type), 'parse_device_added': gi.FunctionInfo(parse_device_added), 'parse_device_changed': gi.FunctionInfo(parse_device_changed), 'parse_device_removed': gi.FunctionInfo(parse_device_removed), 'parse_error': gi.FunctionInfo(parse_error), 'parse_error_details': gi.FunctionInfo(parse_error_details), 'parse_group_id': gi.FunctionInfo(parse_group_id), 'parse_have_context': gi.FunctionInfo(parse_have_context), 'parse_info': gi.FunctionInfo(parse_info), 'parse_info_details': gi.FunctionInfo(parse_info_details), 'parse_new_clock': gi.FunctionInfo(parse_new_clock), 'parse_progress': gi.FunctionInfo(parse_progress), 'parse_property_notify': gi.FunctionInfo(parse_property_notify), 'parse_qos': gi.FunctionInfo(parse_qos), 'parse_qos_stats': gi.FunctionInfo(parse_qos_stats), 'parse_qos_values': gi.FunctionInfo(parse_qos_values), 'parse_redirect_entry': gi.FunctionInfo(parse_redirect_entry), 'parse_request_state': gi.FunctionInfo(parse_request_state), 'parse_reset_time': gi.FunctionInfo(parse_reset_time), 'parse_segment_done': gi.FunctionInfo(parse_segment_done), 'parse_segment_start': gi.FunctionInfo(parse_segment_start), 'parse_state_changed': gi.FunctionInfo(parse_state_changed), 'parse_step_done': gi.FunctionInfo(parse_step_done), 'parse_step_start': gi.FunctionInfo(parse_step_start), 'parse_stream_collection': gi.FunctionInfo(parse_stream_collection), 'parse_stream_status': gi.FunctionInfo(parse_stream_status), 'parse_streams_selected': gi.FunctionInfo(parse_streams_selected), 'parse_structure_change': gi.FunctionInfo(parse_structure_change), 'parse_tag': gi.FunctionInfo(parse_tag), 'parse_toc': gi.FunctionInfo(parse_toc), 'parse_warning': gi.FunctionInfo(parse_warning), 'parse_warning_details': gi.FunctionInfo(parse_warning_details), 'set_buffering_stats': gi.FunctionInfo(set_buffering_stats), 'set_group_id': gi.FunctionInfo(set_group_id), 'set_qos_stats': gi.FunctionInfo(set_qos_stats), 'set_qos_values': gi.FunctionInfo(set_qos_values), 'set_seqnum': gi.FunctionInfo(set_seqnum), 'set_stream_status_object': gi.FunctionInfo(set_stream_status_object), 'streams_selected_add': gi.FunctionInfo(streams_selected_add), 'streams_selected_get_size': gi.FunctionInfo(streams_selected_get_size), 'streams_selected_get_stream': gi.FunctionInfo(streams_selected_get_stream), 'writable_structure': gi.FunctionInfo(writable_structure)})"
    __gtype__ = None # (!) real value is '<GType GstMessage (94058977341952)>'
    __info__ = StructInfo(Message)


