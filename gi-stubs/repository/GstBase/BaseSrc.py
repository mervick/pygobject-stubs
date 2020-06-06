# encoding: utf-8
# module gi.repository.GstBase
# from /usr/lib64/girepository-1.0/GstBase-1.0.typelib
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
import gobject as __gobject


class BaseSrc(__gi_repository_Gst.Element):
    """
    :Constructors:
    
    ::
    
        BaseSrc(**properties)
    """
    def abort_state(self): # real signature unknown; restored from __doc__
        """ abort_state(self) """
        pass

    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_metadata(self, key:str, value:str) """
        pass

    def add_pad(self, pad): # real signature unknown; restored from __doc__
        """ add_pad(self, pad:Gst.Pad) -> bool """
        return False

    def add_pad_template(self, templ): # real signature unknown; restored from __doc__
        """ add_pad_template(self, templ:Gst.PadTemplate) """
        pass

    def add_property_deep_notify_watch(self, property_name=None, include_value): # real signature unknown; restored from __doc__
        """ add_property_deep_notify_watch(self, property_name:str=None, include_value:bool) -> int """
        return 0

    def add_property_notify_watch(self, property_name=None, include_value): # real signature unknown; restored from __doc__
        """ add_property_notify_watch(self, property_name:str=None, include_value:bool) -> int """
        return 0

    def add_static_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_static_metadata(self, key:str, value:str) """
        pass

    def add_static_pad_template(self, static_templ): # real signature unknown; restored from __doc__
        """ add_static_pad_template(self, static_templ:Gst.StaticPadTemplate) """
        pass

    def add_static_pad_template_with_gtype(self, static_templ, pad_type): # real signature unknown; restored from __doc__
        """ add_static_pad_template_with_gtype(self, static_templ:Gst.StaticPadTemplate, pad_type:GType) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def call_async(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ call_async(self, func:Gst.ElementCallAsyncFunc, user_data=None) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_state(self, transition): # real signature unknown; restored from __doc__
        """ change_state(self, transition:Gst.StateChange) -> Gst.StateChangeReturn """
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def continue_state(self, ret): # real signature unknown; restored from __doc__
        """ continue_state(self, ret:Gst.StateChangeReturn) -> Gst.StateChangeReturn """
        pass

    def create_all_pads(self): # real signature unknown; restored from __doc__
        """ create_all_pads(self) """
        pass

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_alloc(self, *args, **kwargs): # real signature unknown
        """ alloc(self, offset:int, size:int, buf:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def do_change_state(self, *args, **kwargs): # real signature unknown
        """ change_state(self, transition:Gst.StateChange) -> Gst.StateChangeReturn """
        pass

    def do_create(self, *args, **kwargs): # real signature unknown
        """ create(self, offset:int, size:int) -> Gst.FlowReturn, buf:Gst.Buffer """
        pass

    def do_decide_allocation(self, *args, **kwargs): # real signature unknown
        """ decide_allocation(self, query:Gst.Query) -> bool """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_do_seek(self, *args, **kwargs): # real signature unknown
        """ do_seek(self, segment:Gst.Segment) -> bool """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gst.Event) -> bool """
        pass

    def do_fill(self, *args, **kwargs): # real signature unknown
        """ fill(self, offset:int, size:int, buf:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def do_fixate(self, *args, **kwargs): # real signature unknown
        """ fixate(self, caps:Gst.Caps) -> Gst.Caps """
        pass

    def do_get_caps(self, *args, **kwargs): # real signature unknown
        """ get_caps(self, filter:Gst.Caps) -> Gst.Caps """
        pass

    def do_get_size(self, *args, **kwargs): # real signature unknown
        """ get_size(self, size:int) -> bool """
        pass

    def do_get_state(self, *args, **kwargs): # real signature unknown
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def do_get_times(self, *args, **kwargs): # real signature unknown
        """ get_times(self, buffer:Gst.Buffer) -> start:int, end:int """
        pass

    def do_is_seekable(self, *args, **kwargs): # real signature unknown
        """ is_seekable(self) -> bool """
        pass

    def do_negotiate(self, *args, **kwargs): # real signature unknown
        """ negotiate(self) -> bool """
        pass

    def do_no_more_pads(self, *args, **kwargs): # real signature unknown
        """ no_more_pads(self) """
        pass

    def do_pad_added(self, *args, **kwargs): # real signature unknown
        """ pad_added(self, pad:Gst.Pad) """
        pass

    def do_pad_removed(self, *args, **kwargs): # real signature unknown
        """ pad_removed(self, pad:Gst.Pad) """
        pass

    def do_post_message(self, *args, **kwargs): # real signature unknown
        """ post_message(self, message:Gst.Message) -> bool """
        pass

    def do_prepare_seek_segment(self, *args, **kwargs): # real signature unknown
        """ prepare_seek_segment(self, seek:Gst.Event, segment:Gst.Segment) -> bool """
        pass

    def do_provide_clock(self, *args, **kwargs): # real signature unknown
        """ provide_clock(self) -> Gst.Clock or None """
        pass

    def do_query(self, *args, **kwargs): # real signature unknown
        """ query(self, query:Gst.Query) -> bool """
        pass

    def do_release_pad(self, *args, **kwargs): # real signature unknown
        """ release_pad(self, pad:Gst.Pad) """
        pass

    def do_request_new_pad(self, *args, **kwargs): # real signature unknown
        """ request_new_pad(self, templ:Gst.PadTemplate, name:str=None, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def do_send_event(self, *args, **kwargs): # real signature unknown
        """ send_event(self, event:Gst.Event) -> bool """
        pass

    def do_set_bus(self, *args, **kwargs): # real signature unknown
        """ set_bus(self, bus:Gst.Bus=None) """
        pass

    def do_set_caps(self, *args, **kwargs): # real signature unknown
        """ set_caps(self, caps:Gst.Caps) -> bool """
        pass

    def do_set_clock(self, *args, **kwargs): # real signature unknown
        """ set_clock(self, clock:Gst.Clock=None) -> bool """
        pass

    def do_set_context(self, *args, **kwargs): # real signature unknown
        """ set_context(self, context:Gst.Context) """
        pass

    def do_set_state(self, *args, **kwargs): # real signature unknown
        """ set_state(self, state:Gst.State) -> Gst.StateChangeReturn """
        pass

    def do_start(self, *args, **kwargs): # real signature unknown
        """ start(self) -> bool """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, oldstate:Gst.State, newstate:Gst.State, pending:Gst.State) """
        pass

    def do_stop(self, *args, **kwargs): # real signature unknown
        """ stop(self) -> bool """
        pass

    def do_unlock(self, *args, **kwargs): # real signature unknown
        """ unlock(self) -> bool """
        pass

    def do_unlock_stop(self, *args, **kwargs): # real signature unknown
        """ unlock_stop(self) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
        return False

    def foreach_sink_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_sink_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
        return False

    def foreach_src_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_src_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
        return False

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_allocator(self): # real signature unknown; restored from __doc__
        """ get_allocator(self) -> allocator:Gst.Allocator, params:Gst.AllocationParams """
        pass

    def get_base_time(self): # real signature unknown; restored from __doc__
        """ get_base_time(self) -> int """
        return 0

    def get_blocksize(self): # real signature unknown; restored from __doc__
        """ get_blocksize(self) -> int """
        return 0

    def get_buffer_pool(self): # real signature unknown; restored from __doc__
        """ get_buffer_pool(self) -> Gst.BufferPool """
        pass

    def get_bus(self): # real signature unknown; restored from __doc__
        """ get_bus(self) -> Gst.Bus or None """
        pass

    def get_clock(self): # real signature unknown; restored from __doc__
        """ get_clock(self) -> Gst.Clock or None """
        pass

    def get_compatible_pad(self, pad, caps=None): # real signature unknown; restored from __doc__
        """ get_compatible_pad(self, pad:Gst.Pad, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def get_compatible_pad_template(self, compattempl): # real signature unknown; restored from __doc__
        """ get_compatible_pad_template(self, compattempl:Gst.PadTemplate) -> Gst.PadTemplate or None """
        pass

    def get_context(self, context_type): # real signature unknown; restored from __doc__
        """ get_context(self, context_type:str) -> Gst.Context """
        pass

    def get_contexts(self): # real signature unknown; restored from __doc__
        """ get_contexts(self) -> list """
        return []

    def get_context_unlocked(self, context_type): # real signature unknown; restored from __doc__
        """ get_context_unlocked(self, context_type:str) -> Gst.Context or None """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_do_timestamp(self): # real signature unknown; restored from __doc__
        """ get_do_timestamp(self) -> bool """
        return False

    def get_factory(self): # real signature unknown; restored from __doc__
        """ get_factory(self) -> Gst.ElementFactory or None """
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_metadata(self, key): # real signature unknown; restored from __doc__
        """ get_metadata(self, key:str) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_pad_template(self, name): # real signature unknown; restored from __doc__
        """ get_pad_template(self, name:str) -> Gst.PadTemplate or None """
        pass

    def get_pad_template_list(self): # real signature unknown; restored from __doc__
        """ get_pad_template_list(self) -> list """
        return []

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_request_pad(self, name): # real signature unknown; restored from __doc__
        """ get_request_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_start_time(self): # real signature unknown; restored from __doc__
        """ get_start_time(self) -> int """
        return 0

    def get_state(self, timeout): # real signature unknown; restored from __doc__
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def get_static_pad(self, name): # real signature unknown; restored from __doc__
        """ get_static_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
        return False

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_async(self): # real signature unknown; restored from __doc__
        """ is_async(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_locked_state(self): # real signature unknown; restored from __doc__
        """ is_locked_state(self) -> bool """
        return False

    def iterate_pads(self): # real signature unknown; restored from __doc__
        """ iterate_pads(self) -> Gst.Iterator """
        pass

    def iterate_sink_pads(self): # real signature unknown; restored from __doc__
        """ iterate_sink_pads(self) -> Gst.Iterator """
        pass

    def iterate_src_pads(self): # real signature unknown; restored from __doc__
        """ iterate_src_pads(self) -> Gst.Iterator """
        pass

    def link(self, dest): # real signature unknown; restored from __doc__
        """ link(self, dest:Gst.Element) -> bool """
        return False

    def link_filtered(self, dest, filter=None): # real signature unknown; restored from __doc__
        """ link_filtered(self, dest:Gst.Element, filter:Gst.Caps=None) -> bool """
        return False

    def link_pads(self, srcpadname=None, dest, destpadname=None): # real signature unknown; restored from __doc__
        """ link_pads(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None) -> bool """
        return False

    def link_pads_filtered(self, srcpadname=None, dest, destpadname=None, filter=None): # real signature unknown; restored from __doc__
        """ link_pads_filtered(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None, filter:Gst.Caps=None) -> bool """
        return False

    def link_pads_full(self, srcpadname=None, dest, destpadname=None, flags): # real signature unknown; restored from __doc__
        """ link_pads_full(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None, flags:Gst.PadLinkCheck) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lost_state(self): # real signature unknown; restored from __doc__
        """ lost_state(self) """
        pass

    def make_from_uri(self, type, uri, elementname=None): # real signature unknown; restored from __doc__
        """ make_from_uri(type:Gst.URIType, uri:str, elementname:str=None) -> Gst.Element or None """
        pass

    def message_full(self, type, domain, code, text=None, debug=None, file, function, line): # real signature unknown; restored from __doc__
        """ message_full(self, type:Gst.MessageType, domain:int, code:int, text:str=None, debug:str=None, file:str, function:str, line:int) """
        pass

    def message_full_with_details(self, type, domain, code, text=None, debug=None, file, function, line, structure): # real signature unknown; restored from __doc__
        """ message_full_with_details(self, type:Gst.MessageType, domain:int, code:int, text:str=None, debug:str=None, file:str, function:str, line:int, structure:Gst.Structure) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_seamless_segment(self, start, stop, time): # real signature unknown; restored from __doc__
        """ new_seamless_segment(self, start:int, stop:int, time:int) -> bool """
        return False

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def no_more_pads(self): # real signature unknown; restored from __doc__
        """ no_more_pads(self) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def post_message(self, message): # real signature unknown; restored from __doc__
        """ post_message(self, message:Gst.Message) -> bool """
        return False

    def provide_clock(self): # real signature unknown; restored from __doc__
        """ provide_clock(self) -> Gst.Clock or None """
        pass

    def query(self, query): # real signature unknown; restored from __doc__
        """ query(self, query:Gst.Query) -> bool """
        return False

    def query_convert(self, src_format, src_val, dest_format): # real signature unknown; restored from __doc__
        """ query_convert(self, src_format:Gst.Format, src_val:int, dest_format:Gst.Format) -> bool, dest_val:int """
        return False

    def query_duration(self, format): # real signature unknown; restored from __doc__
        """ query_duration(self, format:Gst.Format) -> bool, duration:int """
        return False

    def query_latency(self): # real signature unknown; restored from __doc__
        """ query_latency(self) -> bool, live:bool, min_latency:int, max_latency:int """
        return False

    def query_position(self, format): # real signature unknown; restored from __doc__
        """ query_position(self, format:Gst.Format) -> bool, cur:int """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self, plugin=None, name, rank, type): # real signature unknown; restored from __doc__
        """ register(plugin:Gst.Plugin=None, name:str, rank:int, type:GType) -> bool """
        return False

    def release_request_pad(self, pad): # real signature unknown; restored from __doc__
        """ release_request_pad(self, pad:Gst.Pad) """
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def remove_pad(self, pad): # real signature unknown; restored from __doc__
        """ remove_pad(self, pad:Gst.Pad) -> bool """
        return False

    def remove_property_notify_watch(self, watch_id): # real signature unknown; restored from __doc__
        """ remove_property_notify_watch(self, watch_id:int) """
        pass

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def request_pad(self, templ, name=None, caps=None): # real signature unknown; restored from __doc__
        """ request_pad(self, templ:Gst.PadTemplate, name:str=None, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def seek(self, rate, format, flags, start_type, start, stop_type, stop): # real signature unknown; restored from __doc__
        """ seek(self, rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int) -> bool """
        return False

    def seek_simple(self, format, seek_flags, seek_pos): # real signature unknown; restored from __doc__
        """ seek_simple(self, format:Gst.Format, seek_flags:Gst.SeekFlags, seek_pos:int) -> bool """
        return False

    def send_event(self, event): # real signature unknown; restored from __doc__
        """ send_event(self, event:Gst.Event) -> bool """
        return False

    def set_async(self, async_): # real signature unknown; restored from __doc__
        """ set_async(self, async:bool) """
        pass

    def set_automatic_eos(self, automatic_eos): # real signature unknown; restored from __doc__
        """ set_automatic_eos(self, automatic_eos:bool) """
        pass

    def set_base_time(self, time): # real signature unknown; restored from __doc__
        """ set_base_time(self, time:int) """
        pass

    def set_blocksize(self, blocksize): # real signature unknown; restored from __doc__
        """ set_blocksize(self, blocksize:int) """
        pass

    def set_bus(self, bus=None): # real signature unknown; restored from __doc__
        """ set_bus(self, bus:Gst.Bus=None) """
        pass

    def set_caps(self, caps): # real signature unknown; restored from __doc__
        """ set_caps(self, caps:Gst.Caps) -> bool """
        return False

    def set_clock(self, clock=None): # real signature unknown; restored from __doc__
        """ set_clock(self, clock:Gst.Clock=None) -> bool """
        return False

    def set_context(self, context): # real signature unknown; restored from __doc__
        """ set_context(self, context:Gst.Context) """
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_do_timestamp(self, timestamp): # real signature unknown; restored from __doc__
        """ set_do_timestamp(self, timestamp:bool) """
        pass

    def set_dynamic_size(self, dynamic): # real signature unknown; restored from __doc__
        """ set_dynamic_size(self, dynamic:bool) """
        pass

    def set_format(self, format): # real signature unknown; restored from __doc__
        """ set_format(self, format:Gst.Format) """
        pass

    def set_live(self, live): # real signature unknown; restored from __doc__
        """ set_live(self, live:bool) """
        pass

    def set_locked_state(self, locked_state): # real signature unknown; restored from __doc__
        """ set_locked_state(self, locked_state:bool) -> bool """
        return False

    def set_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_start_time(self, time): # real signature unknown; restored from __doc__
        """ set_start_time(self, time:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gst.State) -> Gst.StateChangeReturn """
        pass

    def set_static_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_static_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def start_complete(self, ret): # real signature unknown; restored from __doc__
        """ start_complete(self, ret:Gst.FlowReturn) """
        pass

    def start_wait(self): # real signature unknown; restored from __doc__
        """ start_wait(self) -> Gst.FlowReturn """
        pass

    def state_change_return_get_name(self, state_ret): # real signature unknown; restored from __doc__
        """ state_change_return_get_name(state_ret:Gst.StateChangeReturn) -> str """
        return ""

    def state_get_name(self, state): # real signature unknown; restored from __doc__
        """ state_get_name(state:Gst.State) -> str """
        return ""

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def submit_buffer_list(self, buffer_list): # real signature unknown; restored from __doc__
        """ submit_buffer_list(self, buffer_list:Gst.BufferList) """
        pass

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_state_with_parent(self): # real signature unknown; restored from __doc__
        """ sync_state_with_parent(self) -> bool """
        return False

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlink(self, dest): # real signature unknown; restored from __doc__
        """ unlink(self, dest:Gst.Element) """
        pass

    def unlink_pads(self, srcpadname, dest, destpadname): # real signature unknown; restored from __doc__
        """ unlink_pads(self, srcpadname:str, dest:Gst.Element, destpadname:str) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait_playing(self): # real signature unknown; restored from __doc__
        """ wait_playing(self) -> Gst.FlowReturn """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    base_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blocksize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_activate_push = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_live = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_return = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    live_cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    live_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    live_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_newsegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsrcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_buffers_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending_seek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    random_access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srcpad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typefind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9fb7c040d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BaseSrc), '__module__': 'gi.repository.GstBase', '__gtype__': <GType GstBaseSrc (94858291701600)>, '__doc__': None, '__gsignals__': {}, 'get_allocator': gi.FunctionInfo(get_allocator), 'get_blocksize': gi.FunctionInfo(get_blocksize), 'get_buffer_pool': gi.FunctionInfo(get_buffer_pool), 'get_do_timestamp': gi.FunctionInfo(get_do_timestamp), 'is_async': gi.FunctionInfo(is_async), 'is_live': <property object at 0x7f9fb7bc0ea0>, 'new_seamless_segment': gi.FunctionInfo(new_seamless_segment), 'query_latency': gi.FunctionInfo(query_latency), 'set_async': gi.FunctionInfo(set_async), 'set_automatic_eos': gi.FunctionInfo(set_automatic_eos), 'set_blocksize': gi.FunctionInfo(set_blocksize), 'set_caps': gi.FunctionInfo(set_caps), 'set_do_timestamp': gi.FunctionInfo(set_do_timestamp), 'set_dynamic_size': gi.FunctionInfo(set_dynamic_size), 'set_format': gi.FunctionInfo(set_format), 'set_live': gi.FunctionInfo(set_live), 'start_complete': gi.FunctionInfo(start_complete), 'start_wait': gi.FunctionInfo(start_wait), 'submit_buffer_list': gi.FunctionInfo(submit_buffer_list), 'wait_playing': gi.FunctionInfo(wait_playing), 'do_alloc': gi.VFuncInfo(alloc), 'do_create': gi.VFuncInfo(create), 'do_decide_allocation': gi.VFuncInfo(decide_allocation), 'do_do_seek': gi.VFuncInfo(do_seek), 'do_event': gi.VFuncInfo(event), 'do_fill': gi.VFuncInfo(fill), 'do_fixate': gi.VFuncInfo(fixate), 'do_get_caps': gi.VFuncInfo(get_caps), 'do_get_size': gi.VFuncInfo(get_size), 'do_get_times': gi.VFuncInfo(get_times), 'do_is_seekable': gi.VFuncInfo(is_seekable), 'do_negotiate': gi.VFuncInfo(negotiate), 'do_prepare_seek_segment': gi.VFuncInfo(prepare_seek_segment), 'do_query': gi.VFuncInfo(query), 'do_set_caps': gi.VFuncInfo(set_caps), 'do_start': gi.VFuncInfo(start), 'do_stop': gi.VFuncInfo(stop), 'do_unlock': gi.VFuncInfo(unlock), 'do_unlock_stop': gi.VFuncInfo(unlock_stop), 'element': <property object at 0x7f9fb7bc0ae0>, 'srcpad': <property object at 0x7f9fb7bc0bd0>, 'live_lock': <property object at 0x7f9fb7bc0cc0>, 'live_cond': <property object at 0x7f9fb7bc0db0>, 'live_running': <property object at 0x7f9fb7bc0f90>, 'blocksize': <property object at 0x7f9fb7bc20e0>, 'can_activate_push': <property object at 0x7f9fb7bc2220>, 'random_access': <property object at 0x7f9fb7bc22c0>, 'clock_id': <property object at 0x7f9fb7bc23b0>, 'segment': <property object at 0x7f9fb7bc24a0>, 'need_newsegment': <property object at 0x7f9fb7bc2590>, 'num_buffers': <property object at 0x7f9fb7bc2680>, 'num_buffers_left': <property object at 0x7f9fb7bc27c0>, 'typefind': <property object at 0x7f9fb7bc28b0>, 'running': <property object at 0x7f9fb7bc29a0>, 'pending_seek': <property object at 0x7f9fb7bc2a90>, 'priv': <property object at 0x7f9fb7bc2b80>, '_gst_reserved': <property object at 0x7f9fb7bc2c70>})"
    __gdoc__ = 'Object GstBaseSrc\n\nProperties from GstBaseSrc:\n  blocksize -> guint: Block size\n    Size in bytes to read per buffer (-1 = default)\n  num-buffers -> gint: num-buffers\n    Number of buffers to output before sending EOS (-1 = unlimited)\n  typefind -> gboolean: Typefind\n    Run typefind before negotiating (deprecated, non-functional)\n  do-timestamp -> gboolean: Do timestamp\n    Apply current stream time to buffers\n\nSignals from GstElement:\n  pad-added (GstPad)\n  pad-removed (GstPad)\n  no-more-pads ()\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstBaseSrc (94858291701600)>'
    __info__ = ObjectInfo(BaseSrc)


