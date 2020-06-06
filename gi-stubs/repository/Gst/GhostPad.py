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


from .ProxyPad import ProxyPad

class GhostPad(ProxyPad):
    """
    :Constructors:
    
    ::
    
        GhostPad(**properties)
        new(name:str=None, target:Gst.Pad) -> Gst.Pad or None
        new_from_template(name:str=None, target:Gst.Pad, templ:Gst.PadTemplate) -> Gst.Pad or None
        new_no_target(name:str=None, dir:Gst.PadDirection) -> Gst.Pad or None
        new_no_target_from_template(name:str=None, templ:Gst.PadTemplate) -> Gst.Pad or None
    """
    def activate_mode(self, mode, active): # real signature unknown; restored from __doc__
        """ activate_mode(self, mode:Gst.PadMode, active:bool) -> bool """
        return False

    def activate_mode_default(self, pad, parent=None, mode, active): # real signature unknown; restored from __doc__
        """ activate_mode_default(pad:Gst.Pad, parent:Gst.Object=None, mode:Gst.PadMode, active:bool) -> bool """
        return False

    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_probe(self, mask, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_probe(self, mask:Gst.PadProbeType, callback:Gst.PadProbeCallback, user_data=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_link(self, sinkpad): # real signature unknown; restored from __doc__
        """ can_link(self, sinkpad:Gst.Pad) -> bool """
        return False

    def chain(self, buffer): # real signature unknown; restored from __doc__
        """ chain(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def chain_default(self, pad, parent=None, buffer): # real signature unknown; restored from __doc__
        """ chain_default(pad:Gst.Pad, parent:Gst.Object=None, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def chain_list(self, p_list): # real signature unknown; restored from __doc__
        """ chain_list(self, list:Gst.BufferList) -> Gst.FlowReturn """
        pass

    def chain_list_default(self, pad, parent=None, p_list): # real signature unknown; restored from __doc__
        """ chain_list_default(pad:Gst.Pad, parent:Gst.Object=None, list:Gst.BufferList) -> Gst.FlowReturn """
        pass

    def check_reconfigure(self): # real signature unknown; restored from __doc__
        """ check_reconfigure(self) -> bool """
        return False

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

    def construct(self): # real signature unknown; restored from __doc__
        """ construct(self) -> bool """
        return False

    def create_stream_id(self, parent, stream_id=None): # real signature unknown; restored from __doc__
        """ create_stream_id(self, parent:Gst.Element, stream_id:str=None) -> str """
        return ""

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

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_linked(self, *args, **kwargs): # real signature unknown
        """ linked(self, peer:Gst.Pad) """
        pass

    def do_unlinked(self, *args, **kwargs): # real signature unknown
        """ unlinked(self, peer:Gst.Pad) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def event_default(self, parent=None, event): # real signature unknown; restored from __doc__
        """ event_default(self, parent:Gst.Object=None, event:Gst.Event) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def forward(self, forward, user_data=None): # real signature unknown; restored from __doc__
        """ forward(self, forward:Gst.PadForwardFunction, user_data=None) -> bool """
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

    def getrange_default(self, pad, parent, offset, size): # real signature unknown; restored from __doc__
        """ getrange_default(pad:Gst.Pad, parent:Gst.Object, offset:int, size:int) -> Gst.FlowReturn, buffer:Gst.Buffer """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_allowed_caps(self): # real signature unknown; restored from __doc__
        """ get_allowed_caps(self) -> Gst.Caps or None """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_current_caps(self): # real signature unknown; restored from __doc__
        """ get_current_caps(self) -> Gst.Caps or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gst.PadDirection """
        pass

    def get_element_private(self): # real signature unknown; restored from __doc__
        """ get_element_private(self) """
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_internal(self): # real signature unknown; restored from __doc__
        """ get_internal(self) -> Gst.ProxyPad or None """
        pass

    def get_last_flow_return(self): # real signature unknown; restored from __doc__
        """ get_last_flow_return(self) -> Gst.FlowReturn """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_offset(self): # real signature unknown; restored from __doc__
        """ get_offset(self) -> int """
        return 0

    def get_pad_template(self): # real signature unknown; restored from __doc__
        """ get_pad_template(self) -> Gst.PadTemplate or None """
        pass

    def get_pad_template_caps(self): # real signature unknown; restored from __doc__
        """ get_pad_template_caps(self) -> Gst.Caps """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_parent_element(self): # real signature unknown; restored from __doc__
        """ get_parent_element(self) -> Gst.Element or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_peer(self): # real signature unknown; restored from __doc__
        """ get_peer(self) -> Gst.Pad or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_range(self, offset, size): # real signature unknown; restored from __doc__
        """ get_range(self, offset:int, size:int) -> Gst.FlowReturn, buffer:Gst.Buffer """
        pass

    def get_sticky_event(self, event_type, idx): # real signature unknown; restored from __doc__
        """ get_sticky_event(self, event_type:Gst.EventType, idx:int) -> Gst.Event or None """
        pass

    def get_stream(self): # real signature unknown; restored from __doc__
        """ get_stream(self) -> Gst.Stream or None """
        pass

    def get_stream_id(self): # real signature unknown; restored from __doc__
        """ get_stream_id(self) -> str or None """
        return ""

    def get_target(self): # real signature unknown; restored from __doc__
        """ get_target(self) -> Gst.Pad or None """
        pass

    def get_task_state(self): # real signature unknown; restored from __doc__
        """ get_task_state(self) -> Gst.TaskState """
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

    def has_current_caps(self): # real signature unknown; restored from __doc__
        """ has_current_caps(self) -> bool """
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

    def internal_activate_mode_default(self, pad, parent=None, mode, active): # real signature unknown; restored from __doc__
        """ internal_activate_mode_default(pad:Gst.Pad, parent:Gst.Object=None, mode:Gst.PadMode, active:bool) -> bool """
        return False

    def is_active(self): # real signature unknown; restored from __doc__
        """ is_active(self) -> bool """
        return False

    def is_blocked(self): # real signature unknown; restored from __doc__
        """ is_blocked(self) -> bool """
        return False

    def is_blocking(self): # real signature unknown; restored from __doc__
        """ is_blocking(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_linked(self): # real signature unknown; restored from __doc__
        """ is_linked(self) -> bool """
        return False

    def iterate_internal_links(self): # real signature unknown; restored from __doc__
        """ iterate_internal_links(self) -> Gst.Iterator or None """
        pass

    def iterate_internal_links_default(self, pad, parent=None): # real signature unknown; restored from __doc__
        """ iterate_internal_links_default(pad:Gst.Pad, parent:Gst.Object=None) -> Gst.Iterator or None """
        pass

    def link(self, sinkpad): # real signature unknown; restored from __doc__
        """ link(self, sinkpad:Gst.Pad) -> Gst.PadLinkReturn """
        pass

    def link_full(self, sinkpad, flags): # real signature unknown; restored from __doc__
        """ link_full(self, sinkpad:Gst.Pad, flags:Gst.PadLinkCheck) -> Gst.PadLinkReturn """
        pass

    def link_get_name(self, ret): # real signature unknown; restored from __doc__
        """ link_get_name(ret:Gst.PadLinkReturn) -> str """
        return ""

    def link_maybe_ghosting(self, sink): # real signature unknown; restored from __doc__
        """ link_maybe_ghosting(self, sink:Gst.Pad) -> bool """
        return False

    def link_maybe_ghosting_full(self, sink, flags): # real signature unknown; restored from __doc__
        """ link_maybe_ghosting_full(self, sink:Gst.Pad, flags:Gst.PadLinkCheck) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def mark_reconfigure(self): # real signature unknown; restored from __doc__
        """ mark_reconfigure(self) """
        pass

    def needs_reconfigure(self): # real signature unknown; restored from __doc__
        """ needs_reconfigure(self) -> bool """
        return False

    def new(self, name=None, target): # real signature unknown; restored from __doc__
        """ new(name:str=None, target:Gst.Pad) -> Gst.Pad or None """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_static_template(self, templ, name): # real signature unknown; restored from __doc__
        """ new_from_static_template(templ:Gst.StaticPadTemplate, name:str) -> Gst.Pad """
        pass

    def new_from_template(self, name=None, target, templ): # real signature unknown; restored from __doc__
        """ new_from_template(name:str=None, target:Gst.Pad, templ:Gst.PadTemplate) -> Gst.Pad or None """
        pass

    def new_no_target(self, name=None, dir): # real signature unknown; restored from __doc__
        """ new_no_target(name:str=None, dir:Gst.PadDirection) -> Gst.Pad or None """
        pass

    def new_no_target_from_template(self, name=None, templ): # real signature unknown; restored from __doc__
        """ new_no_target_from_template(name:str=None, templ:Gst.PadTemplate) -> Gst.Pad or None """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def pause_task(self): # real signature unknown; restored from __doc__
        """ pause_task(self) -> bool """
        return False

    def peer_query(self, query): # real signature unknown; restored from __doc__
        """ peer_query(self, query:Gst.Query) -> bool """
        return False

    def peer_query_accept_caps(self, caps): # real signature unknown; restored from __doc__
        """ peer_query_accept_caps(self, caps:Gst.Caps) -> bool """
        return False

    def peer_query_caps(self, filter=None): # real signature unknown; restored from __doc__
        """ peer_query_caps(self, filter:Gst.Caps=None) -> Gst.Caps """
        pass

    def peer_query_convert(self, src_format, src_val, dest_format): # real signature unknown; restored from __doc__
        """ peer_query_convert(self, src_format:Gst.Format, src_val:int, dest_format:Gst.Format) -> bool, dest_val:int """
        return False

    def peer_query_duration(self, format): # real signature unknown; restored from __doc__
        """ peer_query_duration(self, format:Gst.Format) -> bool, duration:int """
        return False

    def peer_query_position(self, format): # real signature unknown; restored from __doc__
        """ peer_query_position(self, format:Gst.Format) -> bool, cur:int """
        return False

    def proxy_query_accept_caps(self, query): # real signature unknown; restored from __doc__
        """ proxy_query_accept_caps(self, query:Gst.Query) -> bool """
        return False

    def proxy_query_caps(self, query): # real signature unknown; restored from __doc__
        """ proxy_query_caps(self, query:Gst.Query) -> bool """
        return False

    def pull_range(self, offset, size): # real signature unknown; restored from __doc__
        """ pull_range(self, offset:int, size:int) -> Gst.FlowReturn, buffer:Gst.Buffer """
        pass

    def push(self, buffer): # real signature unknown; restored from __doc__
        """ push(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def push_event(self, event): # real signature unknown; restored from __doc__
        """ push_event(self, event:Gst.Event) -> bool """
        return False

    def push_list(self, p_list): # real signature unknown; restored from __doc__
        """ push_list(self, list:Gst.BufferList) -> Gst.FlowReturn """
        pass

    def query(self, query): # real signature unknown; restored from __doc__
        """ query(self, query:Gst.Query) -> bool """
        return False

    def query_accept_caps(self, caps): # real signature unknown; restored from __doc__
        """ query_accept_caps(self, caps:Gst.Caps) -> bool """
        return False

    def query_caps(self, filter=None): # real signature unknown; restored from __doc__
        """ query_caps(self, filter:Gst.Caps=None) -> Gst.Caps """
        pass

    def query_convert(self, src_format, src_val, dest_format): # real signature unknown; restored from __doc__
        """ query_convert(self, src_format:Gst.Format, src_val:int, dest_format:Gst.Format) -> bool, dest_val:int """
        return False

    def query_default(self, parent=None, query): # real signature unknown; restored from __doc__
        """ query_default(self, parent:Gst.Object=None, query:Gst.Query) -> bool """
        return False

    def query_duration(self, format): # real signature unknown; restored from __doc__
        """ query_duration(self, format:Gst.Format) -> bool, duration:int """
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

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def remove_probe(self, id): # real signature unknown; restored from __doc__
        """ remove_probe(self, id:int) """
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

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_event(self, event): # real signature unknown; restored from __doc__
        """ send_event(self, event:Gst.Event) -> bool """
        return False

    def set_activatemode_function_full(self, activatemode, user_data=None): # real signature unknown; restored from __doc__
        """ set_activatemode_function_full(self, activatemode:Gst.PadActivateModeFunction, user_data=None) """
        pass

    def set_activate_function_full(self, activate, user_data=None): # real signature unknown; restored from __doc__
        """ set_activate_function_full(self, activate:Gst.PadActivateFunction, user_data=None) """
        pass

    def set_active(self, active): # real signature unknown; restored from __doc__
        """ set_active(self, active:bool) -> bool """
        return False

    def set_chain_function_full(self, chain, user_data=None): # real signature unknown; restored from __doc__
        """ set_chain_function_full(self, chain:Gst.PadChainFunction, user_data=None) """
        pass

    def set_chain_list_function_full(self, chainlist, user_data=None): # real signature unknown; restored from __doc__
        """ set_chain_list_function_full(self, chainlist:Gst.PadChainListFunction, user_data=None) """
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

    def set_element_private(self, priv=None): # real signature unknown; restored from __doc__
        """ set_element_private(self, priv=None) """
        pass

    def set_event_full_function_full(self, event, user_data=None): # real signature unknown; restored from __doc__
        """ set_event_full_function_full(self, event:Gst.PadEventFullFunction, user_data=None) """
        pass

    def set_event_function_full(self, event, user_data=None): # real signature unknown; restored from __doc__
        """ set_event_function_full(self, event:Gst.PadEventFunction, user_data=None) """
        pass

    def set_getrange_function_full(self, get, user_data=None): # real signature unknown; restored from __doc__
        """ set_getrange_function_full(self, get:Gst.PadGetRangeFunction, user_data=None) """
        pass

    def set_iterate_internal_links_function_full(self, iterintlink, user_data=None): # real signature unknown; restored from __doc__
        """ set_iterate_internal_links_function_full(self, iterintlink:Gst.PadIterIntLinkFunction, user_data=None) """
        pass

    def set_link_function_full(self, link, user_data=None): # real signature unknown; restored from __doc__
        """ set_link_function_full(self, link:Gst.PadLinkFunction, user_data=None) """
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_offset(self, offset): # real signature unknown; restored from __doc__
        """ set_offset(self, offset:int) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_query_function_full(self, query, user_data=None): # real signature unknown; restored from __doc__
        """ set_query_function_full(self, query:Gst.PadQueryFunction, user_data=None) """
        pass

    def set_target(self, newtarget=None): # real signature unknown; restored from __doc__
        """ set_target(self, newtarget:Gst.Pad=None) -> bool """
        return False

    def set_unlink_function_full(self, unlink, user_data=None): # real signature unknown; restored from __doc__
        """ set_unlink_function_full(self, unlink:Gst.PadUnlinkFunction, user_data=None) """
        pass

    def start_task(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ start_task(self, func:Gst.TaskFunction, user_data=None) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def sticky_events_foreach(self, foreach_func, user_data=None): # real signature unknown; restored from __doc__
        """ sticky_events_foreach(self, foreach_func:Gst.PadStickyEventsForeachFunction, user_data=None) """
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def stop_task(self): # real signature unknown; restored from __doc__
        """ stop_task(self) -> bool """
        return False

    def store_sticky_event(self, event): # real signature unknown; restored from __doc__
        """ store_sticky_event(self, event:Gst.Event) -> Gst.FlowReturn """
        pass

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlink(self, sinkpad): # real signature unknown; restored from __doc__
        """ unlink(self, sinkpad:Gst.Pad) -> bool """
        return False

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def use_fixed_caps(self): # real signature unknown; restored from __doc__
        """ use_fixed_caps(self) """
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

    activatedata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    activatefunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    activatemodedata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    activatemodefunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    activatemodenotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    activatenotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    block_cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chaindata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chainfunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chainlistdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chainlistfunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chainlistnotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chainnotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    element_private = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eventdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eventfunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eventnotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    getrangedata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    getrangefunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    getrangenotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterintlinkdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterintlinkfunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterintlinknotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linkdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linkfunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    linknotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_blocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_probes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padtemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    peer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    probes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    querydata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queryfunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    querynotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stream_rec_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    task = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unlinkdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unlinkfunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unlinknotify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f426048ebe0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(GhostPad), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstGhostPad (94058977693424)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_template': gi.FunctionInfo(new_from_template), 'new_no_target': gi.FunctionInfo(new_no_target), 'new_no_target_from_template': gi.FunctionInfo(new_no_target_from_template), 'activate_mode_default': gi.FunctionInfo(activate_mode_default), 'internal_activate_mode_default': gi.FunctionInfo(internal_activate_mode_default), 'construct': gi.FunctionInfo(construct), 'get_target': gi.FunctionInfo(get_target), 'set_target': gi.FunctionInfo(set_target), 'pad': <property object at 0x7f426055ee50>, 'priv': <property object at 0x7f426055ef40>})"
    __gdoc__ = 'Object GstGhostPad\n\nSignals from GstPad:\n  linked (GstPad)\n  unlinked (GstPad)\n\nProperties from GstPad:\n  direction -> GstPadDirection: Direction\n    The direction of the pad\n  template -> GstPadTemplate: Template\n    The GstPadTemplate of this pad\n  offset -> gint64: Offset\n    The running time offset of the pad\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstGhostPad (94058977693424)>'
    __info__ = ObjectInfo(GhostPad)


