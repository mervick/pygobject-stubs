# encoding: utf-8
# module gi.repository.GstApp
# from /usr/lib64/girepository-1.0/GstApp-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


# Variables with simple values

_namespace = 'GstApp'

_version = '1.0'

__weakref__ = None

# functions

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class AppSink(__gi_repository_GstBase.BaseSink, __gi_repository_Gst.URIHandler):
    """
    :Constructors:
    
    ::
    
        AppSink(**properties)
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

    def do_activate_pull(self, *args, **kwargs): # real signature unknown
        """ activate_pull(self, active:bool) -> bool """
        pass

    def do_change_state(self, *args, **kwargs): # real signature unknown
        """ change_state(self, transition:Gst.StateChange) -> Gst.StateChangeReturn """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_eos(self, *args, **kwargs): # real signature unknown
        """ eos(self) """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gst.Event) -> bool """
        pass

    def do_fixate(self, *args, **kwargs): # real signature unknown
        """ fixate(self, caps:Gst.Caps) -> Gst.Caps """
        pass

    def do_get_caps(self, *args, **kwargs): # real signature unknown
        """ get_caps(self, filter:Gst.Caps) -> Gst.Caps """
        pass

    def do_get_state(self, *args, **kwargs): # real signature unknown
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def do_get_times(self, *args, **kwargs): # real signature unknown
        """ get_times(self, buffer:Gst.Buffer, start:int, end:int) """
        pass

    def do_new_preroll(self, *args, **kwargs): # real signature unknown
        """ new_preroll(self) -> Gst.FlowReturn """
        pass

    def do_new_sample(self, *args, **kwargs): # real signature unknown
        """ new_sample(self) -> Gst.FlowReturn """
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

    def do_prepare(self, *args, **kwargs): # real signature unknown
        """ prepare(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def do_prepare_list(self, *args, **kwargs): # real signature unknown
        """ prepare_list(self, buffer_list:Gst.BufferList) -> Gst.FlowReturn """
        pass

    def do_preroll(self, *args, **kwargs): # real signature unknown
        """ preroll(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def do_propose_allocation(self, *args, **kwargs): # real signature unknown
        """ propose_allocation(self, query:Gst.Query) -> bool """
        pass

    def do_provide_clock(self, *args, **kwargs): # real signature unknown
        """ provide_clock(self) -> Gst.Clock or None """
        pass

    def do_pull_preroll(self, *args, **kwargs): # real signature unknown
        """ pull_preroll(self) -> Gst.Sample """
        pass

    def do_pull_sample(self, *args, **kwargs): # real signature unknown
        """ pull_sample(self) -> Gst.Sample """
        pass

    def do_query(self, *args, **kwargs): # real signature unknown
        """ query(self, query:Gst.Query) -> bool """
        pass

    def do_release_pad(self, *args, **kwargs): # real signature unknown
        """ release_pad(self, pad:Gst.Pad) """
        pass

    def do_render(self, *args, **kwargs): # real signature unknown
        """ render(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def do_render_list(self, *args, **kwargs): # real signature unknown
        """ render_list(self, buffer_list:Gst.BufferList) -> Gst.FlowReturn """
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

    def do_try_pull_preroll(self, *args, **kwargs): # real signature unknown
        """ try_pull_preroll(self, timeout:int) -> Gst.Sample """
        pass

    def do_try_pull_sample(self, *args, **kwargs): # real signature unknown
        """ try_pull_sample(self, timeout:int) -> Gst.Sample """
        pass

    def do_unlock(self, *args, **kwargs): # real signature unknown
        """ unlock(self) -> bool """
        pass

    def do_unlock_stop(self, *args, **kwargs): # real signature unknown
        """ unlock_stop(self) -> bool """
        pass

    def do_wait_event(self, *args, **kwargs): # real signature unknown
        """ wait_event(self, event:Gst.Event) -> Gst.FlowReturn """
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

    def get_base_time(self): # real signature unknown; restored from __doc__
        """ get_base_time(self) -> int """
        return 0

    def get_blocksize(self): # real signature unknown; restored from __doc__
        """ get_blocksize(self) -> int """
        return 0

    def get_buffer_list_support(self): # real signature unknown; restored from __doc__
        """ get_buffer_list_support(self) -> bool """
        return False

    def get_bus(self): # real signature unknown; restored from __doc__
        """ get_bus(self) -> Gst.Bus or None """
        pass

    def get_caps(self): # real signature unknown; restored from __doc__
        """ get_caps(self) -> Gst.Caps """
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

    def get_drop(self): # real signature unknown; restored from __doc__
        """ get_drop(self) -> bool """
        return False

    def get_drop_out_of_segment(self): # real signature unknown; restored from __doc__
        """ get_drop_out_of_segment(self) -> bool """
        return False

    def get_emit_signals(self): # real signature unknown; restored from __doc__
        """ get_emit_signals(self) -> bool """
        return False

    def get_factory(self): # real signature unknown; restored from __doc__
        """ get_factory(self) -> Gst.ElementFactory or None """
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_last_sample(self): # real signature unknown; restored from __doc__
        """ get_last_sample(self) -> Gst.Sample or None """
        pass

    def get_latency(self): # real signature unknown; restored from __doc__
        """ get_latency(self) -> int """
        return 0

    def get_max_bitrate(self): # real signature unknown; restored from __doc__
        """ get_max_bitrate(self) -> int """
        return 0

    def get_max_buffers(self): # real signature unknown; restored from __doc__
        """ get_max_buffers(self) -> int """
        return 0

    def get_max_lateness(self): # real signature unknown; restored from __doc__
        """ get_max_lateness(self) -> int """
        return 0

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

    def get_processing_deadline(self): # real signature unknown; restored from __doc__
        """ get_processing_deadline(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocols(self): # real signature unknown; restored from __doc__
        """ get_protocols(self) -> list or None """
        return []

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_render_delay(self): # real signature unknown; restored from __doc__
        """ get_render_delay(self) -> int """
        return 0

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

    def get_sync(self): # real signature unknown; restored from __doc__
        """ get_sync(self) -> bool """
        return False

    def get_throttle_time(self): # real signature unknown; restored from __doc__
        """ get_throttle_time(self) -> int """
        return 0

    def get_ts_offset(self): # real signature unknown; restored from __doc__
        """ get_ts_offset(self) -> int """
        return 0

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str or None """
        return ""

    def get_uri_type(self): # real signature unknown; restored from __doc__
        """ get_uri_type(self) -> Gst.URIType """
        pass

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
        pass

    def get_wait_on_eos(self): # real signature unknown; restored from __doc__
        """ get_wait_on_eos(self) -> bool """
        return False

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

    def is_async_enabled(self): # real signature unknown; restored from __doc__
        """ is_async_enabled(self) -> bool """
        return False

    def is_eos(self): # real signature unknown; restored from __doc__
        """ is_eos(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_last_sample_enabled(self): # real signature unknown; restored from __doc__
        """ is_last_sample_enabled(self) -> bool """
        return False

    def is_locked_state(self): # real signature unknown; restored from __doc__
        """ is_locked_state(self) -> bool """
        return False

    def is_qos_enabled(self): # real signature unknown; restored from __doc__
        """ is_qos_enabled(self) -> bool """
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

    def pull_preroll(self): # real signature unknown; restored from __doc__
        """ pull_preroll(self) -> Gst.Sample """
        pass

    def pull_sample(self): # real signature unknown; restored from __doc__
        """ pull_sample(self) -> Gst.Sample """
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
        """ query_latency(self) -> bool, live:bool, upstream_live:bool, min_latency:int, max_latency:int """
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

    def set_async_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_async_enabled(self, enabled:bool) """
        pass

    def set_base_time(self, time): # real signature unknown; restored from __doc__
        """ set_base_time(self, time:int) """
        pass

    def set_blocksize(self, blocksize): # real signature unknown; restored from __doc__
        """ set_blocksize(self, blocksize:int) """
        pass

    def set_buffer_list_support(self, enable_lists): # real signature unknown; restored from __doc__
        """ set_buffer_list_support(self, enable_lists:bool) """
        pass

    def set_bus(self, bus=None): # real signature unknown; restored from __doc__
        """ set_bus(self, bus:Gst.Bus=None) """
        pass

    def set_caps(self, caps): # real signature unknown; restored from __doc__
        """ set_caps(self, caps:Gst.Caps) """
        pass

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

    def set_drop(self, drop): # real signature unknown; restored from __doc__
        """ set_drop(self, drop:bool) """
        pass

    def set_drop_out_of_segment(self, drop_out_of_segment): # real signature unknown; restored from __doc__
        """ set_drop_out_of_segment(self, drop_out_of_segment:bool) """
        pass

    def set_emit_signals(self, emit): # real signature unknown; restored from __doc__
        """ set_emit_signals(self, emit:bool) """
        pass

    def set_last_sample_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_last_sample_enabled(self, enabled:bool) """
        pass

    def set_locked_state(self, locked_state): # real signature unknown; restored from __doc__
        """ set_locked_state(self, locked_state:bool) -> bool """
        return False

    def set_max_bitrate(self, max_bitrate): # real signature unknown; restored from __doc__
        """ set_max_bitrate(self, max_bitrate:int) """
        pass

    def set_max_buffers(self, max): # real signature unknown; restored from __doc__
        """ set_max_buffers(self, max:int) """
        pass

    def set_max_lateness(self, max_lateness): # real signature unknown; restored from __doc__
        """ set_max_lateness(self, max_lateness:int) """
        pass

    def set_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_processing_deadline(self, processing_deadline): # real signature unknown; restored from __doc__
        """ set_processing_deadline(self, processing_deadline:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_qos_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_qos_enabled(self, enabled:bool) """
        pass

    def set_render_delay(self, delay): # real signature unknown; restored from __doc__
        """ set_render_delay(self, delay:int) """
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

    def set_sync(self, sync): # real signature unknown; restored from __doc__
        """ set_sync(self, sync:bool) """
        pass

    def set_throttle_time(self, throttle): # real signature unknown; restored from __doc__
        """ set_throttle_time(self, throttle:int) """
        pass

    def set_ts_offset(self, offset): # real signature unknown; restored from __doc__
        """ set_ts_offset(self, offset:int) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) -> bool """
        return False

    def set_wait_on_eos(self, wait): # real signature unknown; restored from __doc__
        """ set_wait_on_eos(self, wait:bool) """
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

    def try_pull_preroll(self, timeout): # real signature unknown; restored from __doc__
        """ try_pull_preroll(self, timeout:int) -> Gst.Sample """
        pass

    def try_pull_sample(self, timeout): # real signature unknown; restored from __doc__
        """ try_pull_sample(self, timeout:int) -> Gst.Sample """
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

    def wait(self, time): # real signature unknown; restored from __doc__
        """ wait(self, time:int) -> Gst.FlowReturn, jitter:int """
        pass

    def wait_clock(self, time): # real signature unknown; restored from __doc__
        """ wait_clock(self, time:int) -> Gst.ClockReturn, jitter:int """
        pass

    def wait_preroll(self): # real signature unknown; restored from __doc__
        """ wait_preroll(self) -> Gst.FlowReturn """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    basesink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_activate_pull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_activate_push = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flushing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    have_newsegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    have_preroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_return = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_lateness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_preroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsrcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    playing_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preroll_cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    preroll_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sinkpad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f47a136b940>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(AppSink), '__module__': 'gi.repository.GstApp', '__gtype__': <GType GstAppSink (94575106321088)>, '__doc__': None, '__gsignals__': {}, 'get_buffer_list_support': gi.FunctionInfo(get_buffer_list_support), 'get_caps': gi.FunctionInfo(get_caps), 'get_drop': gi.FunctionInfo(get_drop), 'get_emit_signals': gi.FunctionInfo(get_emit_signals), 'get_max_buffers': gi.FunctionInfo(get_max_buffers), 'get_wait_on_eos': gi.FunctionInfo(get_wait_on_eos), 'is_eos': gi.FunctionInfo(is_eos), 'pull_preroll': gi.FunctionInfo(pull_preroll), 'pull_sample': gi.FunctionInfo(pull_sample), 'set_buffer_list_support': gi.FunctionInfo(set_buffer_list_support), 'set_caps': gi.FunctionInfo(set_caps), 'set_drop': gi.FunctionInfo(set_drop), 'set_emit_signals': gi.FunctionInfo(set_emit_signals), 'set_max_buffers': gi.FunctionInfo(set_max_buffers), 'set_wait_on_eos': gi.FunctionInfo(set_wait_on_eos), 'try_pull_preroll': gi.FunctionInfo(try_pull_preroll), 'try_pull_sample': gi.FunctionInfo(try_pull_sample), 'do_eos': gi.VFuncInfo(eos), 'do_new_preroll': gi.VFuncInfo(new_preroll), 'do_new_sample': gi.VFuncInfo(new_sample), 'do_pull_preroll': gi.VFuncInfo(pull_preroll), 'do_pull_sample': gi.VFuncInfo(pull_sample), 'do_try_pull_preroll': gi.VFuncInfo(try_pull_preroll), 'do_try_pull_sample': gi.VFuncInfo(try_pull_sample), 'basesink': <property object at 0x7f47a1366bd0>, 'priv': <property object at 0x7f47a1366cc0>, '_gst_reserved': <property object at 0x7f47a1366db0>})"
    __gdoc__ = 'Object GstAppSink\n\nSignals from GstAppSink:\n  eos ()\n  new-preroll () -> GstFlowReturn\n  new-sample () -> GstFlowReturn\n\nProperties from GstAppSink:\n  eos -> gboolean: EOS\n    Check if the sink is EOS or not started\n  emit-signals -> gboolean: Emit signals\n    Emit new-preroll and new-sample signals\n  max-buffers -> guint: Max Buffers\n    The maximum number of buffers to queue internally (0 = unlimited)\n  drop -> gboolean: Drop\n    Drop old buffers when the buffer queue is filled\n  wait-on-eos -> gboolean: Wait on EOS\n    Wait for all buffers to be processed after receiving an EOS\n  buffer-list -> gboolean: Buffer List\n    Use buffer lists\n\nProperties from GstBaseSink:\n  sync -> gboolean: Sync\n    Sync on the clock\n  max-lateness -> gint64: Max Lateness\n    Maximum number of nanoseconds that a buffer can be late before it is dropped (-1 unlimited)\n  qos -> gboolean: Qos\n    Generate Quality-of-Service events upstream\n  async -> gboolean: Async\n    Go asynchronously to PAUSED\n  ts-offset -> gint64: TS Offset\n    Timestamp offset in nanoseconds\n  enable-last-sample -> gboolean: Enable Last Buffer\n    Enable the last-sample property\n  blocksize -> guint: Block size\n    Size in bytes to pull per buffer (0 = default)\n  render-delay -> guint64: Render Delay\n    Additional render delay of the sink in nanoseconds\n  throttle-time -> guint64: Throttle time\n    The time to keep between rendered buffers (0 = disabled)\n  max-bitrate -> guint64: Max Bitrate\n    The maximum bits per second to render (0 = disabled)\n  processing-deadline -> guint64: Processing deadline\n    Maximum processing deadline in nanoseconds\n\nSignals from GstElement:\n  pad-added (GstPad)\n  pad-removed (GstPad)\n  no-more-pads ()\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstAppSink (94575106321088)>'
    __info__ = ObjectInfo(AppSink)


class AppSinkClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AppSinkClass()
    """
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

    basesink_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_preroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_sample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pull_preroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pull_sample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    try_pull_preroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    try_pull_sample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AppSinkClass), '__module__': 'gi.repository.GstApp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AppSinkClass' objects>, '__weakref__': <attribute '__weakref__' of 'AppSinkClass' objects>, '__doc__': None, 'basesink_class': <property object at 0x7f47a1366f40>, 'eos': <property object at 0x7f47a1369090>, 'new_preroll': <property object at 0x7f47a1369180>, 'new_sample': <property object at 0x7f47a1369270>, 'pull_preroll': <property object at 0x7f47a1369360>, 'pull_sample': <property object at 0x7f47a1369450>, 'try_pull_preroll': <property object at 0x7f47a1369590>, 'try_pull_sample': <property object at 0x7f47a1369630>, '_gst_reserved': <property object at 0x7f47a1369720>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AppSinkClass)


class AppSinkPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AppSinkPrivate), '__module__': 'gi.repository.GstApp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AppSinkPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'AppSinkPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AppSinkPrivate)


class AppSrc(__gi_repository_GstBase.BaseSrc, __gi_repository_Gst.URIHandler):
    """
    :Constructors:
    
    ::
    
        AppSrc(**properties)
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

    def do_end_of_stream(self, *args, **kwargs): # real signature unknown
        """ end_of_stream(self) -> Gst.FlowReturn """
        pass

    def do_enough_data(self, *args, **kwargs): # real signature unknown
        """ enough_data(self) """
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

    def do_need_data(self, *args, **kwargs): # real signature unknown
        """ need_data(self, length:int) """
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

    def do_push_buffer(self, *args, **kwargs): # real signature unknown
        """ push_buffer(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def do_push_buffer_list(self, *args, **kwargs): # real signature unknown
        """ push_buffer_list(self, buffer_list:Gst.BufferList) -> Gst.FlowReturn """
        pass

    def do_push_sample(self, *args, **kwargs): # real signature unknown
        """ push_sample(self, sample:Gst.Sample) -> Gst.FlowReturn """
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

    def do_seek_data(self, *args, **kwargs): # real signature unknown
        """ seek_data(self, offset:int) -> bool """
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

    def end_of_stream(self): # real signature unknown; restored from __doc__
        """ end_of_stream(self) -> Gst.FlowReturn """
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

    def get_caps(self): # real signature unknown; restored from __doc__
        """ get_caps(self) -> Gst.Caps """
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

    def get_current_level_bytes(self): # real signature unknown; restored from __doc__
        """ get_current_level_bytes(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_do_timestamp(self): # real signature unknown; restored from __doc__
        """ get_do_timestamp(self) -> bool """
        return False

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> int """
        return 0

    def get_emit_signals(self): # real signature unknown; restored from __doc__
        """ get_emit_signals(self) -> bool """
        return False

    def get_factory(self): # real signature unknown; restored from __doc__
        """ get_factory(self) -> Gst.ElementFactory or None """
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_latency(self): # real signature unknown; restored from __doc__
        """ get_latency(self) -> min:int, max:int """
        pass

    def get_max_bytes(self): # real signature unknown; restored from __doc__
        """ get_max_bytes(self) -> int """
        return 0

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

    def get_protocols(self): # real signature unknown; restored from __doc__
        """ get_protocols(self) -> list or None """
        return []

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_request_pad(self, name): # real signature unknown; restored from __doc__
        """ get_request_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_start_time(self): # real signature unknown; restored from __doc__
        """ get_start_time(self) -> int """
        return 0

    def get_state(self, timeout): # real signature unknown; restored from __doc__
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def get_static_pad(self, name): # real signature unknown; restored from __doc__
        """ get_static_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_stream_type(self): # real signature unknown; restored from __doc__
        """ get_stream_type(self) -> GstApp.AppStreamType """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str or None """
        return ""

    def get_uri_type(self): # real signature unknown; restored from __doc__
        """ get_uri_type(self) -> Gst.URIType """
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

    def push_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ push_buffer(self, buffer:Gst.Buffer) -> Gst.FlowReturn """
        pass

    def push_buffer_list(self, buffer_list): # real signature unknown; restored from __doc__
        """ push_buffer_list(self, buffer_list:Gst.BufferList) -> Gst.FlowReturn """
        pass

    def push_sample(self, sample): # real signature unknown; restored from __doc__
        """ push_sample(self, sample:Gst.Sample) -> Gst.FlowReturn """
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
        """ set_caps(self, caps:Gst.Caps) """
        pass

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

    def set_duration(self, duration): # real signature unknown; restored from __doc__
        """ set_duration(self, duration:int) """
        pass

    def set_dynamic_size(self, dynamic): # real signature unknown; restored from __doc__
        """ set_dynamic_size(self, dynamic:bool) """
        pass

    def set_emit_signals(self, emit): # real signature unknown; restored from __doc__
        """ set_emit_signals(self, emit:bool) """
        pass

    def set_format(self, format): # real signature unknown; restored from __doc__
        """ set_format(self, format:Gst.Format) """
        pass

    def set_latency(self, min, max): # real signature unknown; restored from __doc__
        """ set_latency(self, min:int, max:int) """
        pass

    def set_live(self, live): # real signature unknown; restored from __doc__
        """ set_live(self, live:bool) """
        pass

    def set_locked_state(self, locked_state): # real signature unknown; restored from __doc__
        """ set_locked_state(self, locked_state:bool) -> bool """
        return False

    def set_max_bytes(self, max): # real signature unknown; restored from __doc__
        """ set_max_bytes(self, max:int) """
        pass

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

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
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

    def set_stream_type(self, type): # real signature unknown; restored from __doc__
        """ set_stream_type(self, type:GstApp.AppStreamType) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) -> bool """
        return False

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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    basesrc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f47a1110a00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(AppSrc), '__module__': 'gi.repository.GstApp', '__gtype__': <GType GstAppSrc (94575106340608)>, '__doc__': None, '__gsignals__': {}, 'end_of_stream': gi.FunctionInfo(end_of_stream), 'get_caps': gi.FunctionInfo(get_caps), 'get_current_level_bytes': gi.FunctionInfo(get_current_level_bytes), 'get_duration': gi.FunctionInfo(get_duration), 'get_emit_signals': gi.FunctionInfo(get_emit_signals), 'get_latency': gi.FunctionInfo(get_latency), 'get_max_bytes': gi.FunctionInfo(get_max_bytes), 'get_size': gi.FunctionInfo(get_size), 'get_stream_type': gi.FunctionInfo(get_stream_type), 'push_buffer': gi.FunctionInfo(push_buffer), 'push_buffer_list': gi.FunctionInfo(push_buffer_list), 'push_sample': gi.FunctionInfo(push_sample), 'set_caps': gi.FunctionInfo(set_caps), 'set_duration': gi.FunctionInfo(set_duration), 'set_emit_signals': gi.FunctionInfo(set_emit_signals), 'set_latency': gi.FunctionInfo(set_latency), 'set_max_bytes': gi.FunctionInfo(set_max_bytes), 'set_size': gi.FunctionInfo(set_size), 'set_stream_type': gi.FunctionInfo(set_stream_type), 'do_end_of_stream': gi.VFuncInfo(end_of_stream), 'do_enough_data': gi.VFuncInfo(enough_data), 'do_need_data': gi.VFuncInfo(need_data), 'do_push_buffer': gi.VFuncInfo(push_buffer), 'do_push_buffer_list': gi.VFuncInfo(push_buffer_list), 'do_push_sample': gi.VFuncInfo(push_sample), 'do_seek_data': gi.VFuncInfo(seek_data), 'basesrc': <property object at 0x7f47a136e040>, 'priv': <property object at 0x7f47a136e180>, '_gst_reserved': <property object at 0x7f47a136e270>})"
    __gdoc__ = 'Object GstAppSrc\n\nSignals from GstAppSrc:\n  need-data (guint)\n  enough-data ()\n  seek-data (guint64) -> gboolean\n  end-of-stream () -> GstFlowReturn\n\nProperties from GstAppSrc:\n  size -> gint64: Size\n    The size of the data stream in bytes (-1 if unknown)\n  stream-type -> GstAppStreamType: Stream Type\n    the type of the stream\n  max-bytes -> guint64: Max bytes\n    The maximum number of bytes to queue internally (0 = unlimited)\n  format -> GstFormat: Format\n    The format of the segment events and seek\n  block -> gboolean: Block\n    Block push-buffer when max-bytes are queued\n  is-live -> gboolean: Is Live\n    Whether to act as a live source\n  min-latency -> gint64: Min Latency\n    The minimum latency (-1 = default)\n  max-latency -> gint64: Max Latency\n    The maximum latency (-1 = unlimited)\n  emit-signals -> gboolean: Emit signals\n    Emit need-data, enough-data and seek-data signals\n  min-percent -> guint: Min Percent\n    Emit need-data when queued bytes drops below this percent of max-bytes\n  current-level-bytes -> guint64: Current Level Bytes\n    The number of currently queued bytes\n  duration -> guint64: Duration\n    The duration of the data stream in nanoseconds (GST_CLOCK_TIME_NONE if unknown)\n\nProperties from GstBaseSrc:\n  blocksize -> guint: Block size\n    Size in bytes to read per buffer (-1 = default)\n  num-buffers -> gint: num-buffers\n    Number of buffers to output before sending EOS (-1 = unlimited)\n  typefind -> gboolean: Typefind\n    Run typefind before negotiating (deprecated, non-functional)\n  do-timestamp -> gboolean: Do timestamp\n    Apply current stream time to buffers\n\nSignals from GstElement:\n  pad-added (GstPad)\n  pad-removed (GstPad)\n  no-more-pads ()\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstAppSrc (94575106340608)>'
    __info__ = ObjectInfo(AppSrc)


class AppSrcClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AppSrcClass()
    """
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

    basesrc_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_of_stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enough_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    push_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    push_buffer_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    push_sample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seek_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AppSrcClass), '__module__': 'gi.repository.GstApp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AppSrcClass' objects>, '__weakref__': <attribute '__weakref__' of 'AppSrcClass' objects>, '__doc__': None, 'basesrc_class': <property object at 0x7f47a136e400>, 'need_data': <property object at 0x7f47a136e4f0>, 'enough_data': <property object at 0x7f47a136e5e0>, 'seek_data': <property object at 0x7f47a136e6d0>, 'push_buffer': <property object at 0x7f47a136e7c0>, 'end_of_stream': <property object at 0x7f47a136e8b0>, 'push_sample': <property object at 0x7f47a136e9a0>, 'push_buffer_list': <property object at 0x7f47a136eae0>, '_gst_reserved': <property object at 0x7f47a136eb80>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AppSrcClass)


class AppSrcPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AppSrcPrivate), '__module__': 'gi.repository.GstApp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AppSrcPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'AppSrcPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AppSrcPrivate)


class AppStreamType(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    RANDOM_ACCESS = 2
    SEEKABLE = 1
    STREAM = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstApp', '__dict__': <attribute '__dict__' of 'AppStreamType' objects>, '__doc__': None, '__gtype__': <GType GstAppStreamType (94575106476864)>, '__enum_values__': {0: <enum GST_APP_STREAM_TYPE_STREAM of type GstApp.AppStreamType>, 1: <enum GST_APP_STREAM_TYPE_SEEKABLE of type GstApp.AppStreamType>, 2: <enum GST_APP_STREAM_TYPE_RANDOM_ACCESS of type GstApp.AppStreamType>}, '__info__': gi.EnumInfo(AppStreamType), 'STREAM': <enum GST_APP_STREAM_TYPE_STREAM of type GstApp.AppStreamType>, 'SEEKABLE': <enum GST_APP_STREAM_TYPE_SEEKABLE of type GstApp.AppStreamType>, 'RANDOM_ACCESS': <enum GST_APP_STREAM_TYPE_RANDOM_ACCESS of type GstApp.AppStreamType>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType GstAppStreamType (94575106476864)>'
    __info__ = gi.EnumInfo(AppStreamType)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f47a15971f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f47a1597280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f47a1597310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f47a15973a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f47a21d3d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstApp-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstApp', loader=<gi.importer.DynamicImporter object at 0x7f47a21d3d00>)"

