# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Client(__gi_overrides_GObject.Object, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        Client(**properties)
        new(cancellable:Gio.Cancellable=None) -> NM.Client
        new_finish(result:Gio.AsyncResult) -> NM.Client
    """
    def activate_connection_async(self, connection=None, device=None, specific_object=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ activate_connection_async(self, connection:NM.Connection=None, device:NM.Device=None, specific_object:str=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def activate_connection_finish(self, result): # real signature unknown; restored from __doc__
        """ activate_connection_finish(self, result:Gio.AsyncResult) -> NM.ActiveConnection """
        pass

    def add_and_activate_connection2(self, partial=None, device, specific_object=None, options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_and_activate_connection2(self, partial:NM.Connection=None, device:NM.Device, specific_object:str=None, options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_and_activate_connection2_finish(self, result, out_result=None): # real signature unknown; restored from __doc__
        """ add_and_activate_connection2_finish(self, result:Gio.AsyncResult, out_result:GLib.Variant=None) -> NM.ActiveConnection """
        pass

    def add_and_activate_connection_async(self, partial=None, device, specific_object=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_and_activate_connection_async(self, partial:NM.Connection=None, device:NM.Device, specific_object:str=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_and_activate_connection_finish(self, result): # real signature unknown; restored from __doc__
        """ add_and_activate_connection_finish(self, result:Gio.AsyncResult) -> NM.ActiveConnection """
        pass

    def add_connection2(self, settings, flags, args=None, ignore_out_result, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_connection2(self, settings:GLib.Variant, flags:NM.SettingsAddConnection2Flags, args:GLib.Variant=None, ignore_out_result:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_connection2_finish(self, result): # real signature unknown; restored from __doc__
        """ add_connection2_finish(self, result:Gio.AsyncResult) -> NM.RemoteConnection, out_result:GLib.Variant """
        pass

    def add_connection_async(self, connection, save_to_disk, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_connection_async(self, connection:NM.Connection, save_to_disk:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_connection_finish(self, result): # real signature unknown; restored from __doc__
        """ add_connection_finish(self, result:Gio.AsyncResult) -> NM.RemoteConnection """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def checkpoint_adjust_rollback_timeout(self, checkpoint_path, add_timeout, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ checkpoint_adjust_rollback_timeout(self, checkpoint_path:str, add_timeout:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def checkpoint_adjust_rollback_timeout_finish(self, result): # real signature unknown; restored from __doc__
        """ checkpoint_adjust_rollback_timeout_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def checkpoint_create(self, devices, rollback_timeout, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ checkpoint_create(self, devices:list, rollback_timeout:int, flags:NM.CheckpointCreateFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def checkpoint_create_finish(self, result): # real signature unknown; restored from __doc__
        """ checkpoint_create_finish(self, result:Gio.AsyncResult) -> NM.Checkpoint """
        pass

    def checkpoint_destroy(self, checkpoint_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ checkpoint_destroy(self, checkpoint_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def checkpoint_destroy_finish(self, result): # real signature unknown; restored from __doc__
        """ checkpoint_destroy_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def checkpoint_rollback(self, checkpoint_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ checkpoint_rollback(self, checkpoint_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def checkpoint_rollback_finish(self, result): # real signature unknown; restored from __doc__
        """ checkpoint_rollback_finish(self, result:Gio.AsyncResult) -> dict """
        return {}

    def check_connectivity(self, cancellable=None): # real signature unknown; restored from __doc__
        """ check_connectivity(self, cancellable:Gio.Cancellable=None) -> NM.ConnectivityState """
        pass

    def check_connectivity_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ check_connectivity_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def check_connectivity_finish(self, result): # real signature unknown; restored from __doc__
        """ check_connectivity_finish(self, result:Gio.AsyncResult) -> NM.ConnectivityState """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connectivity_check_get_available(self): # real signature unknown; restored from __doc__
        """ connectivity_check_get_available(self) -> bool """
        return False

    def connectivity_check_get_enabled(self): # real signature unknown; restored from __doc__
        """ connectivity_check_get_enabled(self) -> bool """
        return False

    def connectivity_check_get_uri(self): # real signature unknown; restored from __doc__
        """ connectivity_check_get_uri(self) -> str """
        return ""

    def connectivity_check_set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ connectivity_check_set_enabled(self, enabled:bool) """
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

    def deactivate_connection(self, active, cancellable=None): # real signature unknown; restored from __doc__
        """ deactivate_connection(self, active:NM.ActiveConnection, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def deactivate_connection_async(self, active, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ deactivate_connection_async(self, active:NM.ActiveConnection, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def deactivate_connection_finish(self, result): # real signature unknown; restored from __doc__
        """ deactivate_connection_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
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

    def get_activating_connection(self): # real signature unknown; restored from __doc__
        """ get_activating_connection(self) -> NM.ActiveConnection """
        pass

    def get_active_connections(self): # real signature unknown; restored from __doc__
        """ get_active_connections(self) -> list """
        return []

    def get_all_devices(self): # real signature unknown; restored from __doc__
        """ get_all_devices(self) -> list """
        return []

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> list, length:int """
        return []

    def get_checkpoints(self): # real signature unknown; restored from __doc__
        """ get_checkpoints(self) -> list """
        return []

    def get_connections(self): # real signature unknown; restored from __doc__
        """ get_connections(self) -> list """
        return []

    def get_connection_by_id(self, id): # real signature unknown; restored from __doc__
        """ get_connection_by_id(self, id:str) -> NM.RemoteConnection """
        pass

    def get_connection_by_path(self, path): # real signature unknown; restored from __doc__
        """ get_connection_by_path(self, path:str) -> NM.RemoteConnection """
        pass

    def get_connection_by_uuid(self, uuid): # real signature unknown; restored from __doc__
        """ get_connection_by_uuid(self, uuid:str) -> NM.RemoteConnection """
        pass

    def get_connectivity(self): # real signature unknown; restored from __doc__
        """ get_connectivity(self) -> NM.ConnectivityState """
        pass

    def get_context_busy_watcher(self): # real signature unknown; restored from __doc__
        """ get_context_busy_watcher(self) -> GObject.Object """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dbus_connection(self): # real signature unknown; restored from __doc__
        """ get_dbus_connection(self) -> Gio.DBusConnection """
        pass

    def get_dbus_name_owner(self): # real signature unknown; restored from __doc__
        """ get_dbus_name_owner(self) -> str """
        return ""

    def get_devices(self): # real signature unknown; restored from __doc__
        """ get_devices(self) -> list """
        return []

    def get_device_by_iface(self, iface): # real signature unknown; restored from __doc__
        """ get_device_by_iface(self, iface:str) -> NM.Device """
        pass

    def get_device_by_path(self, object_path): # real signature unknown; restored from __doc__
        """ get_device_by_path(self, object_path:str) -> NM.Device """
        pass

    def get_dns_configuration(self): # real signature unknown; restored from __doc__
        """ get_dns_configuration(self) -> list """
        return []

    def get_dns_mode(self): # real signature unknown; restored from __doc__
        """ get_dns_mode(self) -> str """
        return ""

    def get_dns_rc_manager(self): # real signature unknown; restored from __doc__
        """ get_dns_rc_manager(self) -> str """
        return ""

    def get_logging(self, level=None, domains=None): # real signature unknown; restored from __doc__
        """ get_logging(self, level:str=None, domains:str=None) -> bool """
        return False

    def get_main_context(self): # real signature unknown; restored from __doc__
        """ get_main_context(self) -> GLib.MainContext """
        pass

    def get_metered(self): # real signature unknown; restored from __doc__
        """ get_metered(self) -> NM.Metered """
        pass

    def get_nm_running(self): # real signature unknown; restored from __doc__
        """ get_nm_running(self) -> bool """
        return False

    def get_permission_result(self, permission): # real signature unknown; restored from __doc__
        """ get_permission_result(self, permission:NM.ClientPermission) -> NM.ClientPermissionResult """
        pass

    def get_primary_connection(self): # real signature unknown; restored from __doc__
        """ get_primary_connection(self) -> NM.ActiveConnection """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_startup(self): # real signature unknown; restored from __doc__
        """ get_startup(self) -> bool """
        return False

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> NM.State """
        pass

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
        return ""

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

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_finish(self, res): # real signature unknown; restored from __doc__
        """ init_finish(self, res:Gio.AsyncResult) -> bool """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load_connections(self, filenames, cancellable=None): # real signature unknown; restored from __doc__
        """ load_connections(self, filenames:list, cancellable:Gio.Cancellable=None) -> bool, failures:str """
        return False

    def load_connections_async(self, filenames, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_connections_async(self, filenames:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_connections_finish(self, result): # real signature unknown; restored from __doc__
        """ load_connections_finish(self, result:Gio.AsyncResult) -> bool, failures:list """
        return False

    def networking_get_enabled(self): # real signature unknown; restored from __doc__
        """ networking_get_enabled(self) -> bool """
        return False

    def networking_set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ networking_set_enabled(self, enabled:bool) -> bool """
        return False

    def new(self, cancellable=None): # real signature unknown; restored from __doc__
        """ new(cancellable:Gio.Cancellable=None) -> NM.Client """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_async(cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, result): # real signature unknown; restored from __doc__
        """ new_finish(result:Gio.AsyncResult) -> NM.Client """
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

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reload(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ reload(self, flags:NM.ManagerReloadFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def reload_connections(self, cancellable=None): # real signature unknown; restored from __doc__
        """ reload_connections(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def reload_connections_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ reload_connections_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def reload_connections_finish(self, result): # real signature unknown; restored from __doc__
        """ reload_connections_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def reload_finish(self, result): # real signature unknown; restored from __doc__
        """ reload_finish(self, result:Gio.AsyncResult) -> bool """
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

    def save_hostname(self, hostname=None, cancellable=None): # real signature unknown; restored from __doc__
        """ save_hostname(self, hostname:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def save_hostname_async(self, hostname=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ save_hostname_async(self, hostname:str=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def save_hostname_finish(self, result): # real signature unknown; restored from __doc__
        """ save_hostname_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_logging(self, level=None, domains=None): # real signature unknown; restored from __doc__
        """ set_logging(self, level:str=None, domains:str=None) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    def wimax_get_enabled(self): # real signature unknown; restored from __doc__
        """ wimax_get_enabled(self) -> bool """
        return False

    def wimax_hardware_get_enabled(self): # real signature unknown; restored from __doc__
        """ wimax_hardware_get_enabled(self) -> bool """
        return False

    def wimax_set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ wimax_set_enabled(self, enabled:bool) """
        pass

    def wireless_get_enabled(self): # real signature unknown; restored from __doc__
        """ wireless_get_enabled(self) -> bool """
        return False

    def wireless_hardware_get_enabled(self): # real signature unknown; restored from __doc__
        """ wireless_hardware_get_enabled(self) -> bool """
        return False

    def wireless_set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ wireless_set_enabled(self, enabled:bool) """
        pass

    def wwan_get_enabled(self): # real signature unknown; restored from __doc__
        """ wwan_get_enabled(self) -> bool """
        return False

    def wwan_hardware_get_enabled(self): # real signature unknown; restored from __doc__
        """ wwan_hardware_get_enabled(self) -> bool """
        return False

    def wwan_set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ wwan_set_enabled(self, enabled:bool) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b8467a60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Client), '__module__': 'gi.repository.NM', '__gtype__': <GType NMClient (94741104160480)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_finish': gi.FunctionInfo(new_finish), 'new_async': gi.FunctionInfo(new_async), 'activate_connection_async': gi.FunctionInfo(activate_connection_async), 'activate_connection_finish': gi.FunctionInfo(activate_connection_finish), 'add_and_activate_connection2': gi.FunctionInfo(add_and_activate_connection2), 'add_and_activate_connection2_finish': gi.FunctionInfo(add_and_activate_connection2_finish), 'add_and_activate_connection_async': gi.FunctionInfo(add_and_activate_connection_async), 'add_and_activate_connection_finish': gi.FunctionInfo(add_and_activate_connection_finish), 'add_connection2': gi.FunctionInfo(add_connection2), 'add_connection2_finish': gi.FunctionInfo(add_connection2_finish), 'add_connection_async': gi.FunctionInfo(add_connection_async), 'add_connection_finish': gi.FunctionInfo(add_connection_finish), 'check_connectivity': gi.FunctionInfo(check_connectivity), 'check_connectivity_async': gi.FunctionInfo(check_connectivity_async), 'check_connectivity_finish': gi.FunctionInfo(check_connectivity_finish), 'checkpoint_adjust_rollback_timeout': gi.FunctionInfo(checkpoint_adjust_rollback_timeout), 'checkpoint_adjust_rollback_timeout_finish': gi.FunctionInfo(checkpoint_adjust_rollback_timeout_finish), 'checkpoint_create': gi.FunctionInfo(checkpoint_create), 'checkpoint_create_finish': gi.FunctionInfo(checkpoint_create_finish), 'checkpoint_destroy': gi.FunctionInfo(checkpoint_destroy), 'checkpoint_destroy_finish': gi.FunctionInfo(checkpoint_destroy_finish), 'checkpoint_rollback': gi.FunctionInfo(checkpoint_rollback), 'checkpoint_rollback_finish': gi.FunctionInfo(checkpoint_rollback_finish), 'connectivity_check_get_available': gi.FunctionInfo(connectivity_check_get_available), 'connectivity_check_get_enabled': gi.FunctionInfo(connectivity_check_get_enabled), 'connectivity_check_get_uri': gi.FunctionInfo(connectivity_check_get_uri), 'connectivity_check_set_enabled': gi.FunctionInfo(connectivity_check_set_enabled), 'deactivate_connection': gi.FunctionInfo(deactivate_connection), 'deactivate_connection_async': gi.FunctionInfo(deactivate_connection_async), 'deactivate_connection_finish': gi.FunctionInfo(deactivate_connection_finish), 'get_activating_connection': gi.FunctionInfo(get_activating_connection), 'get_active_connections': gi.FunctionInfo(get_active_connections), 'get_all_devices': gi.FunctionInfo(get_all_devices), 'get_capabilities': gi.FunctionInfo(get_capabilities), 'get_checkpoints': gi.FunctionInfo(get_checkpoints), 'get_connection_by_id': gi.FunctionInfo(get_connection_by_id), 'get_connection_by_path': gi.FunctionInfo(get_connection_by_path), 'get_connection_by_uuid': gi.FunctionInfo(get_connection_by_uuid), 'get_connections': gi.FunctionInfo(get_connections), 'get_connectivity': gi.FunctionInfo(get_connectivity), 'get_context_busy_watcher': gi.FunctionInfo(get_context_busy_watcher), 'get_dbus_connection': gi.FunctionInfo(get_dbus_connection), 'get_dbus_name_owner': gi.FunctionInfo(get_dbus_name_owner), 'get_device_by_iface': gi.FunctionInfo(get_device_by_iface), 'get_device_by_path': gi.FunctionInfo(get_device_by_path), 'get_devices': gi.FunctionInfo(get_devices), 'get_dns_configuration': gi.FunctionInfo(get_dns_configuration), 'get_dns_mode': gi.FunctionInfo(get_dns_mode), 'get_dns_rc_manager': gi.FunctionInfo(get_dns_rc_manager), 'get_logging': gi.FunctionInfo(get_logging), 'get_main_context': gi.FunctionInfo(get_main_context), 'get_metered': gi.FunctionInfo(get_metered), 'get_nm_running': gi.FunctionInfo(get_nm_running), 'get_permission_result': gi.FunctionInfo(get_permission_result), 'get_primary_connection': gi.FunctionInfo(get_primary_connection), 'get_startup': gi.FunctionInfo(get_startup), 'get_state': gi.FunctionInfo(get_state), 'get_version': gi.FunctionInfo(get_version), 'load_connections': gi.FunctionInfo(load_connections), 'load_connections_async': gi.FunctionInfo(load_connections_async), 'load_connections_finish': gi.FunctionInfo(load_connections_finish), 'networking_get_enabled': gi.FunctionInfo(networking_get_enabled), 'networking_set_enabled': gi.FunctionInfo(networking_set_enabled), 'reload': gi.FunctionInfo(reload), 'reload_connections': gi.FunctionInfo(reload_connections), 'reload_connections_async': gi.FunctionInfo(reload_connections_async), 'reload_connections_finish': gi.FunctionInfo(reload_connections_finish), 'reload_finish': gi.FunctionInfo(reload_finish), 'save_hostname': gi.FunctionInfo(save_hostname), 'save_hostname_async': gi.FunctionInfo(save_hostname_async), 'save_hostname_finish': gi.FunctionInfo(save_hostname_finish), 'set_logging': gi.FunctionInfo(set_logging), 'wimax_get_enabled': gi.FunctionInfo(wimax_get_enabled), 'wimax_hardware_get_enabled': gi.FunctionInfo(wimax_hardware_get_enabled), 'wimax_set_enabled': gi.FunctionInfo(wimax_set_enabled), 'wireless_get_enabled': gi.FunctionInfo(wireless_get_enabled), 'wireless_hardware_get_enabled': gi.FunctionInfo(wireless_hardware_get_enabled), 'wireless_set_enabled': gi.FunctionInfo(wireless_set_enabled), 'wwan_get_enabled': gi.FunctionInfo(wwan_get_enabled), 'wwan_hardware_get_enabled': gi.FunctionInfo(wwan_hardware_get_enabled), 'wwan_set_enabled': gi.FunctionInfo(wwan_set_enabled)})"
    __gdoc__ = 'Object NMClient\n\nSignals from NMClient:\n  device-added (GObject)\n  device-removed (GObject)\n  any-device-added (GObject)\n  any-device-removed (GObject)\n  permission-changed (guint, guint)\n  connection-added (NMRemoteConnection)\n  connection-removed (NMRemoteConnection)\n  active-connection-added (NMActiveConnection)\n  active-connection-removed (NMActiveConnection)\n\nProperties from NMClient:\n  dbus-connection -> GDBusConnection: \n    \n  dbus-name-owner -> gchararray: \n    \n  version -> gchararray: \n    \n  state -> NMState: \n    \n  startup -> gboolean: \n    \n  nm-running -> gboolean: \n    \n  networking-enabled -> gboolean: \n    \n  wireless-enabled -> gboolean: \n    \n  wireless-hardware-enabled -> gboolean: \n    \n  wwan-enabled -> gboolean: \n    \n  wwan-hardware-enabled -> gboolean: \n    \n  wimax-enabled -> gboolean: \n    \n  wimax-hardware-enabled -> gboolean: \n    \n  active-connections -> GPtrArray: \n    \n  connectivity -> NMConnectivityState: \n    \n  connectivity-check-uri -> gchararray: \n    \n  connectivity-check-available -> gboolean: \n    \n  connectivity-check-enabled -> gboolean: \n    \n  primary-connection -> NMActiveConnection: \n    \n  activating-connection -> NMActiveConnection: \n    \n  devices -> GPtrArray: \n    \n  all-devices -> GPtrArray: \n    \n  connections -> GPtrArray: \n    \n  hostname -> gchararray: \n    \n  can-modify -> gboolean: \n    \n  metered -> guint: \n    \n  dns-mode -> gchararray: \n    \n  dns-rc-manager -> gchararray: \n    \n  dns-configuration -> GPtrArray: \n    \n  checkpoints -> GPtrArray: \n    \n  capabilities -> GArray: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMClient (94741104160480)>'
    __info__ = ObjectInfo(Client)


