# encoding: utf-8
# module gi.repository.IBus
# from /usr/lib64/girepository-1.0/IBus-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .Object import Object

class Bus(Object):
    """
    :Constructors:
    
    ::
    
        Bus(**properties)
        new() -> IBus.Bus
        new_async() -> IBus.Bus
        new_async_client() -> IBus.Bus
    """
    def add_match(self, rule): # real signature unknown; restored from __doc__
        """ add_match(self, rule:str) -> bool """
        return False

    def add_match_async(self, rule, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_match_async(self, rule:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_match_async_finish(self, res): # real signature unknown; restored from __doc__
        """ add_match_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

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

    def create_input_context(self, client_name): # real signature unknown; restored from __doc__
        """ create_input_context(self, client_name:str) -> IBus.InputContext """
        pass

    def create_input_context_async(self, client_name, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_input_context_async(self, client_name:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_input_context_async_finish(self, res): # real signature unknown; restored from __doc__
        """ create_input_context_async_finish(self, res:Gio.AsyncResult) -> IBus.InputContext """
        pass

    def current_input_context(self): # real signature unknown; restored from __doc__
        """ current_input_context(self) -> str """
        return ""

    def current_input_context_async(self, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ current_input_context_async(self, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def current_input_context_async_finish(self, res): # real signature unknown; restored from __doc__
        """ current_input_context_async_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def exit(self, restart): # real signature unknown; restored from __doc__
        """ exit(self, restart:bool) -> bool """
        return False

    def exit_async(self, restart, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ exit_async(self, restart:bool, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def exit_async_finish(self, res): # real signature unknown; restored from __doc__
        """ exit_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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

    def get_config(self): # real signature unknown; restored from __doc__
        """ get_config(self) -> IBus.Config """
        pass

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_engines_by_names(self, names): # real signature unknown; restored from __doc__
        """ get_engines_by_names(self, names:list) -> list """
        return []

    def get_global_engine(self): # real signature unknown; restored from __doc__
        """ get_global_engine(self) -> IBus.EngineDesc """
        pass

    def get_global_engine_async(self, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_global_engine_async(self, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_global_engine_async_finish(self, res): # real signature unknown; restored from __doc__
        """ get_global_engine_async_finish(self, res:Gio.AsyncResult) -> IBus.EngineDesc """
        pass

    def get_ibus_property(self, property_name): # real signature unknown; restored from __doc__
        """ get_ibus_property(self, property_name:str) -> GLib.Variant """
        pass

    def get_ibus_property_async(self, property_name, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_ibus_property_async(self, property_name:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_ibus_property_async_finish(self, res): # real signature unknown; restored from __doc__
        """ get_ibus_property_async_finish(self, res:Gio.AsyncResult) -> GLib.Variant """
        pass

    def get_name_owner(self, name): # real signature unknown; restored from __doc__
        """ get_name_owner(self, name:str) -> str """
        return ""

    def get_name_owner_async(self, name, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_name_owner_async(self, name:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_name_owner_async_finish(self, res): # real signature unknown; restored from __doc__
        """ get_name_owner_async_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_service_name(self): # real signature unknown; restored from __doc__
        """ get_service_name(self) -> str """
        return ""

    def get_use_global_engine(self): # real signature unknown; restored from __doc__
        """ get_use_global_engine(self) -> bool """
        return False

    def get_use_global_engine_async(self, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_use_global_engine_async(self, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_use_global_engine_async_finish(self, res): # real signature unknown; restored from __doc__
        """ get_use_global_engine_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def get_use_sys_layout(self): # real signature unknown; restored from __doc__
        """ get_use_sys_layout(self) -> bool """
        return False

    def get_use_sys_layout_async(self, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_use_sys_layout_async(self, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_use_sys_layout_async_finish(self, res): # real signature unknown; restored from __doc__
        """ get_use_sys_layout_async_finish(self, res:Gio.AsyncResult) -> bool """
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

    def hello(self): # real signature unknown; restored from __doc__
        """ hello(self) -> str """
        return ""

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

    def is_connected(self): # real signature unknown; restored from __doc__
        """ is_connected(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_global_engine_enabled(self): # real signature unknown; restored from __doc__
        """ is_global_engine_enabled(self) -> bool """
        return False

    def is_global_engine_enabled_async(self, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ is_global_engine_enabled_async(self, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def is_global_engine_enabled_async_finish(self, res): # real signature unknown; restored from __doc__
        """ is_global_engine_enabled_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def list_active_engines(self): # real signature unknown; restored from __doc__
        """ list_active_engines(self) -> list """
        return []

    def list_active_engines_async(self, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ list_active_engines_async(self, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def list_active_engines_async_finish(self, res): # real signature unknown; restored from __doc__
        """ list_active_engines_async_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def list_engines(self): # real signature unknown; restored from __doc__
        """ list_engines(self) -> list """
        return []

    def list_engines_async(self, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ list_engines_async(self, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def list_engines_async_finish(self, res): # real signature unknown; restored from __doc__
        """ list_engines_async_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def list_names(self): # real signature unknown; restored from __doc__
        """ list_names(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_queued_owners(self, name): # real signature unknown; restored from __doc__
        """ list_queued_owners(self, name:str) -> list """
        return []

    def name_has_owner(self, name): # real signature unknown; restored from __doc__
        """ name_has_owner(self, name:str) -> bool """
        return False

    def name_has_owner_async(self, name, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ name_has_owner_async(self, name:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def name_has_owner_async_finish(self, res): # real signature unknown; restored from __doc__
        """ name_has_owner_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> IBus.Bus """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_async(self): # real signature unknown; restored from __doc__
        """ new_async() -> IBus.Bus """
        pass

    def new_async_client(self): # real signature unknown; restored from __doc__
        """ new_async_client() -> IBus.Bus """
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

    def preload_engines(self, names): # real signature unknown; restored from __doc__
        """ preload_engines(self, names:list) -> bool """
        return False

    def preload_engines_async(self, names, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ preload_engines_async(self, names:list, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def preload_engines_async_finish(self, res): # real signature unknown; restored from __doc__
        """ preload_engines_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register_component(self, component): # real signature unknown; restored from __doc__
        """ register_component(self, component:IBus.Component) -> bool """
        return False

    def register_component_async(self, component, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ register_component_async(self, component:IBus.Component, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def register_component_async_finish(self, res): # real signature unknown; restored from __doc__
        """ register_component_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def release_name(self, name): # real signature unknown; restored from __doc__
        """ release_name(self, name:str) -> int """
        return 0

    def release_name_async(self, name, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ release_name_async(self, name:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def release_name_async_finish(self, res): # real signature unknown; restored from __doc__
        """ release_name_async_finish(self, res:Gio.AsyncResult) -> int """
        return 0

    def remove_match(self, rule): # real signature unknown; restored from __doc__
        """ remove_match(self, rule:str) -> bool """
        return False

    def remove_match_async(self, rule, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_match_async(self, rule:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_match_async_finish(self, res): # real signature unknown; restored from __doc__
        """ remove_match_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def request_name(self, name, flags): # real signature unknown; restored from __doc__
        """ request_name(self, name:str, flags:int) -> int """
        return 0

    def request_name_async(self, name, flags, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ request_name_async(self, name:str, flags:int, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def request_name_async_finish(self, res): # real signature unknown; restored from __doc__
        """ request_name_async_finish(self, res:Gio.AsyncResult) -> int """
        return 0

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_global_engine(self, global_engine): # real signature unknown; restored from __doc__
        """ set_global_engine(self, global_engine:str) -> bool """
        return False

    def set_global_engine_async(self, global_engine, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_global_engine_async(self, global_engine:str, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_global_engine_async_finish(self, res): # real signature unknown; restored from __doc__
        """ set_global_engine_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_ibus_property(self, property_name, value): # real signature unknown; restored from __doc__
        """ set_ibus_property(self, property_name:str, value:GLib.Variant) """
        pass

    def set_ibus_property_async(self, property_name, value, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_ibus_property_async(self, property_name:str, value:GLib.Variant, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_ibus_property_async_finish(self, res): # real signature unknown; restored from __doc__
        """ set_ibus_property_async_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_watch_dbus_signal(self, watch): # real signature unknown; restored from __doc__
        """ set_watch_dbus_signal(self, watch:bool) """
        pass

    def set_watch_ibus_signal(self, watch): # real signature unknown; restored from __doc__
        """ set_watch_ibus_signal(self, watch:bool) """
        pass

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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f59b1235ca0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Bus), '__module__': 'gi.repository.IBus', '__gtype__': <GType IBusBus (94061789731344)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_async': gi.FunctionInfo(new_async), 'new_async_client': gi.FunctionInfo(new_async_client), 'add_match': gi.FunctionInfo(add_match), 'add_match_async': gi.FunctionInfo(add_match_async), 'add_match_async_finish': gi.FunctionInfo(add_match_async_finish), 'create_input_context': gi.FunctionInfo(create_input_context), 'create_input_context_async': gi.FunctionInfo(create_input_context_async), 'create_input_context_async_finish': gi.FunctionInfo(create_input_context_async_finish), 'current_input_context': gi.FunctionInfo(current_input_context), 'current_input_context_async': gi.FunctionInfo(current_input_context_async), 'current_input_context_async_finish': gi.FunctionInfo(current_input_context_async_finish), 'exit': gi.FunctionInfo(exit), 'exit_async': gi.FunctionInfo(exit_async), 'exit_async_finish': gi.FunctionInfo(exit_async_finish), 'get_config': gi.FunctionInfo(get_config), 'get_connection': gi.FunctionInfo(get_connection), 'get_engines_by_names': gi.FunctionInfo(get_engines_by_names), 'get_global_engine': gi.FunctionInfo(get_global_engine), 'get_global_engine_async': gi.FunctionInfo(get_global_engine_async), 'get_global_engine_async_finish': gi.FunctionInfo(get_global_engine_async_finish), 'get_ibus_property': gi.FunctionInfo(get_ibus_property), 'get_ibus_property_async': gi.FunctionInfo(get_ibus_property_async), 'get_ibus_property_async_finish': gi.FunctionInfo(get_ibus_property_async_finish), 'get_name_owner': gi.FunctionInfo(get_name_owner), 'get_name_owner_async': gi.FunctionInfo(get_name_owner_async), 'get_name_owner_async_finish': gi.FunctionInfo(get_name_owner_async_finish), 'get_service_name': gi.FunctionInfo(get_service_name), 'get_use_global_engine': gi.FunctionInfo(get_use_global_engine), 'get_use_global_engine_async': gi.FunctionInfo(get_use_global_engine_async), 'get_use_global_engine_async_finish': gi.FunctionInfo(get_use_global_engine_async_finish), 'get_use_sys_layout': gi.FunctionInfo(get_use_sys_layout), 'get_use_sys_layout_async': gi.FunctionInfo(get_use_sys_layout_async), 'get_use_sys_layout_async_finish': gi.FunctionInfo(get_use_sys_layout_async_finish), 'hello': gi.FunctionInfo(hello), 'is_connected': gi.FunctionInfo(is_connected), 'is_global_engine_enabled': gi.FunctionInfo(is_global_engine_enabled), 'is_global_engine_enabled_async': gi.FunctionInfo(is_global_engine_enabled_async), 'is_global_engine_enabled_async_finish': gi.FunctionInfo(is_global_engine_enabled_async_finish), 'list_active_engines': gi.FunctionInfo(list_active_engines), 'list_active_engines_async': gi.FunctionInfo(list_active_engines_async), 'list_active_engines_async_finish': gi.FunctionInfo(list_active_engines_async_finish), 'list_engines': gi.FunctionInfo(list_engines), 'list_engines_async': gi.FunctionInfo(list_engines_async), 'list_engines_async_finish': gi.FunctionInfo(list_engines_async_finish), 'list_names': gi.FunctionInfo(list_names), 'list_queued_owners': gi.FunctionInfo(list_queued_owners), 'name_has_owner': gi.FunctionInfo(name_has_owner), 'name_has_owner_async': gi.FunctionInfo(name_has_owner_async), 'name_has_owner_async_finish': gi.FunctionInfo(name_has_owner_async_finish), 'preload_engines': gi.FunctionInfo(preload_engines), 'preload_engines_async': gi.FunctionInfo(preload_engines_async), 'preload_engines_async_finish': gi.FunctionInfo(preload_engines_async_finish), 'register_component': gi.FunctionInfo(register_component), 'register_component_async': gi.FunctionInfo(register_component_async), 'register_component_async_finish': gi.FunctionInfo(register_component_async_finish), 'release_name': gi.FunctionInfo(release_name), 'release_name_async': gi.FunctionInfo(release_name_async), 'release_name_async_finish': gi.FunctionInfo(release_name_async_finish), 'remove_match': gi.FunctionInfo(remove_match), 'remove_match_async': gi.FunctionInfo(remove_match_async), 'remove_match_async_finish': gi.FunctionInfo(remove_match_async_finish), 'request_name': gi.FunctionInfo(request_name), 'request_name_async': gi.FunctionInfo(request_name_async), 'request_name_async_finish': gi.FunctionInfo(request_name_async_finish), 'set_global_engine': gi.FunctionInfo(set_global_engine), 'set_global_engine_async': gi.FunctionInfo(set_global_engine_async), 'set_global_engine_async_finish': gi.FunctionInfo(set_global_engine_async_finish), 'set_ibus_property': gi.FunctionInfo(set_ibus_property), 'set_ibus_property_async': gi.FunctionInfo(set_ibus_property_async), 'set_ibus_property_async_finish': gi.FunctionInfo(set_ibus_property_async_finish), 'set_watch_dbus_signal': gi.FunctionInfo(set_watch_dbus_signal), 'set_watch_ibus_signal': gi.FunctionInfo(set_watch_ibus_signal), 'parent': <property object at 0x7f59b132f950>, 'priv': <property object at 0x7f59b132fa40>})"
    __gdoc__ = 'Object IBusBus\n\nSignals from IBusBus:\n  connected ()\n  disconnected ()\n  global-engine-changed (gchararray)\n  name-owner-changed (gchararray, gchararray, gchararray)\n\nProperties from IBusBus:\n  connect-async -> gboolean: Connect Async\n    Connect asynchronously to the bus\n  client-only -> gboolean: ClientOnly\n    Client use only\n\nSignals from IBusObject:\n  destroy ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType IBusBus (94061789731344)>'
    __info__ = ObjectInfo(Bus)


