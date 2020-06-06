# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .GdbusModem3gppProxy import GdbusModem3gppProxy

class Modem3gpp(GdbusModem3gppProxy):
    """
    :Constructors:
    
    ::
    
        Modem3gpp(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def call(self, method_name, parameters=None, flags, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call(self, method_name:str, parameters:GLib.Variant=None, flags:Gio.DBusCallFlags, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_finish(self, res): # real signature unknown; restored from __doc__
        """ call_finish(self, res:Gio.AsyncResult) -> GLib.Variant """
        pass

    def call_register(self, arg_operator_id, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_register(self, arg_operator_id:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_register_finish(self, res): # real signature unknown; restored from __doc__
        """ call_register_finish(self, res:Gio.AsyncResult) """
        pass

    def call_register_sync(self, arg_operator_id, cancellable=None): # real signature unknown; restored from __doc__
        """ call_register_sync(self, arg_operator_id:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_scan(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_scan(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_scan_finish(self, res): # real signature unknown; restored from __doc__
        """ call_scan_finish(self, res:Gio.AsyncResult) -> out_results:GLib.Variant """
        pass

    def call_scan_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_scan_sync(self, cancellable:Gio.Cancellable=None) -> out_results:GLib.Variant """
        pass

    def call_set_eps_ue_mode_operation(self, arg_mode, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_eps_ue_mode_operation(self, arg_mode:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_eps_ue_mode_operation_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_eps_ue_mode_operation_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_eps_ue_mode_operation_sync(self, arg_mode, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_eps_ue_mode_operation_sync(self, arg_mode:int, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_initial_eps_bearer_settings(self, arg_settings, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_initial_eps_bearer_settings(self, arg_settings:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_initial_eps_bearer_settings_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_initial_eps_bearer_settings_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_initial_eps_bearer_settings_sync(self, arg_settings, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_initial_eps_bearer_settings_sync(self, arg_settings:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_sync(self, method_name, parameters=None, flags, timeout_msec, cancellable=None): # real signature unknown; restored from __doc__
        """ call_sync(self, method_name:str, parameters:GLib.Variant=None, flags:Gio.DBusCallFlags, timeout_msec:int, cancellable:Gio.Cancellable=None) -> GLib.Variant """
        pass

    def call_with_unix_fd_list(self, method_name, parameters=None, flags, timeout_msec, fd_list=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_with_unix_fd_list(self, method_name:str, parameters:GLib.Variant=None, flags:Gio.DBusCallFlags, timeout_msec:int, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_with_unix_fd_list_finish(self, res): # real signature unknown; restored from __doc__
        """ call_with_unix_fd_list_finish(self, res:Gio.AsyncResult) -> GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_with_unix_fd_list_sync(self, method_name, parameters=None, flags, timeout_msec, fd_list=None, cancellable=None): # real signature unknown; restored from __doc__
        """ call_with_unix_fd_list_sync(self, method_name:str, parameters:GLib.Variant=None, flags:Gio.DBusCallFlags, timeout_msec:int, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None) -> GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def complete_register(self, invocation): # real signature unknown; restored from __doc__
        """ complete_register(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_scan(self, invocation, results): # real signature unknown; restored from __doc__
        """ complete_scan(self, invocation:Gio.DBusMethodInvocation, results:GLib.Variant) """
        pass

    def complete_set_eps_ue_mode_operation(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_eps_ue_mode_operation(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_initial_eps_bearer_settings(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_initial_eps_bearer_settings(self, invocation:Gio.DBusMethodInvocation) """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_g_properties_changed(self, *args, **kwargs): # real signature unknown
        """ g_properties_changed(self, changed_properties:GLib.Variant, invalidated_properties:str) """
        pass

    def do_g_signal(self, *args, **kwargs): # real signature unknown
        """ g_signal(self, sender_name:str, signal_name:str, parameters:GLib.Variant) """
        pass

    def dup_imei(self): # real signature unknown; restored from __doc__
        """ dup_imei(self) -> str """
        return ""

    def dup_initial_eps_bearer_path(self): # real signature unknown; restored from __doc__
        """ dup_initial_eps_bearer_path(self) -> str """
        return ""

    def dup_operator_code(self): # real signature unknown; restored from __doc__
        """ dup_operator_code(self) -> str """
        return ""

    def dup_operator_name(self): # real signature unknown; restored from __doc__
        """ dup_operator_name(self) -> str """
        return ""

    def dup_path(self): # real signature unknown; restored from __doc__
        """ dup_path(self) -> str """
        return ""

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

    def get_cached_property(self, property_name): # real signature unknown; restored from __doc__
        """ get_cached_property(self, property_name:str) -> GLib.Variant or None """
        pass

    def get_cached_property_names(self): # real signature unknown; restored from __doc__
        """ get_cached_property_names(self) -> list or None """
        return []

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_timeout(self): # real signature unknown; restored from __doc__
        """ get_default_timeout(self) -> int """
        return 0

    def get_enabled_facility_locks(self): # real signature unknown; restored from __doc__
        """ get_enabled_facility_locks(self) -> ModemManager.Modem3gppFacility """
        pass

    def get_eps_ue_mode_operation(self): # real signature unknown; restored from __doc__
        """ get_eps_ue_mode_operation(self) -> ModemManager.Modem3gppEpsUeModeOperation """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.DBusProxyFlags """
        pass

    def get_imei(self): # real signature unknown; restored from __doc__
        """ get_imei(self) -> str """
        return ""

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> Gio.DBusInterfaceInfo """
        pass

    def get_initial_eps_bearer(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_initial_eps_bearer(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_initial_eps_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ get_initial_eps_bearer_finish(self, res:Gio.AsyncResult) -> ModemManager.Bearer """
        pass

    def get_initial_eps_bearer_settings(self): # real signature unknown; restored from __doc__
        """ get_initial_eps_bearer_settings(self) -> ModemManager.BearerProperties """
        pass

    def get_initial_eps_bearer_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_initial_eps_bearer_sync(self, cancellable:Gio.Cancellable=None) -> ModemManager.Bearer """
        pass

    def get_interface_info(self): # real signature unknown; restored from __doc__
        """ get_interface_info(self) -> Gio.DBusInterfaceInfo or None """
        pass

    def get_interface_name(self): # real signature unknown; restored from __doc__
        """ get_interface_name(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_name_owner(self): # real signature unknown; restored from __doc__
        """ get_name_owner(self) -> str or None """
        return ""

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> Gio.DBusObject """
        pass

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_operator_code(self): # real signature unknown; restored from __doc__
        """ get_operator_code(self) -> str """
        return ""

    def get_operator_name(self): # real signature unknown; restored from __doc__
        """ get_operator_name(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_pco(self): # real signature unknown; restored from __doc__
        """ get_pco(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_registration_state(self): # real signature unknown; restored from __doc__
        """ get_registration_state(self) -> ModemManager.Modem3gppRegistrationState """
        pass

    def get_subscription_state(self): # real signature unknown; restored from __doc__
        """ get_subscription_state(self) -> ModemManager.Modem3gppSubscriptionState """
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

    def interface_info(self): # real signature unknown; restored from __doc__
        """ interface_info() -> Gio.DBusInterfaceInfo """
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

    def new(self, connection, flags, name=None, object_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, res): # real signature unknown; restored from __doc__
        """ new_finish(res:Gio.AsyncResult) -> ModemManager.GdbusModem3gppProxy """
        pass

    def new_for_bus(self, bus_type, flags, name, object_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_for_bus(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_for_bus_finish(self, res): # real signature unknown; restored from __doc__
        """ new_for_bus_finish(res:Gio.AsyncResult) -> ModemManager.GdbusModem3gppProxy """
        pass

    def new_for_bus_sync(self, bus_type, flags, name, object_path, cancellable=None): # real signature unknown; restored from __doc__
        """ new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> ModemManager.GdbusModem3gppProxy """
        pass

    def new_sync(self, connection, flags, name=None, object_path, cancellable=None): # real signature unknown; restored from __doc__
        """ new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> ModemManager.GdbusModem3gppProxy """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_properties(self, klass, property_id_begin): # real signature unknown; restored from __doc__
        """ override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
        return 0

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_initial_eps_bearer_settings(self): # real signature unknown; restored from __doc__
        """ peek_initial_eps_bearer_settings(self) -> ModemManager.BearerProperties """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self, network_id, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ register(self, network_id:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def register_finish(self, res): # real signature unknown; restored from __doc__
        """ register_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def register_sync(self, network_id, cancellable=None): # real signature unknown; restored from __doc__
        """ register_sync(self, network_id:str, cancellable:Gio.Cancellable=None) -> bool """
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

    def scan(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ scan(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def scan_finish(self, res): # real signature unknown; restored from __doc__
        """ scan_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def scan_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ scan_sync(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def set_cached_property(self, property_name, value=None): # real signature unknown; restored from __doc__
        """ set_cached_property(self, property_name:str, value:GLib.Variant=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_timeout(self, timeout_msec): # real signature unknown; restored from __doc__
        """ set_default_timeout(self, timeout_msec:int) """
        pass

    def set_eps_ue_mode_operation(self, mode, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_eps_ue_mode_operation(self, mode:ModemManager.Modem3gppEpsUeModeOperation, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_eps_ue_mode_operation_finish(self, res): # real signature unknown; restored from __doc__
        """ set_eps_ue_mode_operation_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_eps_ue_mode_operation_sync(self, mode, cancellable=None): # real signature unknown; restored from __doc__
        """ set_eps_ue_mode_operation_sync(self, mode:ModemManager.Modem3gppEpsUeModeOperation, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_initial_eps_bearer_settings(self, config, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_initial_eps_bearer_settings(self, config:ModemManager.BearerProperties, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_initial_eps_bearer_settings_finish(self, res): # real signature unknown; restored from __doc__
        """ set_initial_eps_bearer_settings_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_initial_eps_bearer_settings_sync(self, config, cancellable=None): # real signature unknown; restored from __doc__
        """ set_initial_eps_bearer_settings_sync(self, config:ModemManager.BearerProperties, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_interface_info(self, info=None): # real signature unknown; restored from __doc__
        """ set_interface_info(self, info:Gio.DBusInterfaceInfo=None) """
        pass

    def set_object(self, p_object=None): # real signature unknown; restored from __doc__
        """ set_object(self, object:Gio.DBusObject=None) """
        pass

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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f6943588430>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Modem3gpp), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MMModem3gpp (94631948655632)>, '__doc__': None, '__gsignals__': {}, 'dup_imei': gi.FunctionInfo(dup_imei), 'dup_initial_eps_bearer_path': gi.FunctionInfo(dup_initial_eps_bearer_path), 'dup_operator_code': gi.FunctionInfo(dup_operator_code), 'dup_operator_name': gi.FunctionInfo(dup_operator_name), 'dup_path': gi.FunctionInfo(dup_path), 'get_enabled_facility_locks': gi.FunctionInfo(get_enabled_facility_locks), 'get_eps_ue_mode_operation': gi.FunctionInfo(get_eps_ue_mode_operation), 'get_imei': gi.FunctionInfo(get_imei), 'get_initial_eps_bearer': gi.FunctionInfo(get_initial_eps_bearer), 'get_initial_eps_bearer_finish': gi.FunctionInfo(get_initial_eps_bearer_finish), 'get_initial_eps_bearer_settings': gi.FunctionInfo(get_initial_eps_bearer_settings), 'get_initial_eps_bearer_sync': gi.FunctionInfo(get_initial_eps_bearer_sync), 'get_operator_code': gi.FunctionInfo(get_operator_code), 'get_operator_name': gi.FunctionInfo(get_operator_name), 'get_path': gi.FunctionInfo(get_path), 'get_pco': gi.FunctionInfo(get_pco), 'get_registration_state': gi.FunctionInfo(get_registration_state), 'get_subscription_state': gi.FunctionInfo(get_subscription_state), 'peek_initial_eps_bearer_settings': gi.FunctionInfo(peek_initial_eps_bearer_settings), 'register': gi.FunctionInfo(register), 'register_finish': gi.FunctionInfo(register_finish), 'register_sync': gi.FunctionInfo(register_sync), 'scan': gi.FunctionInfo(scan), 'scan_finish': gi.FunctionInfo(scan_finish), 'scan_sync': gi.FunctionInfo(scan_sync), 'set_eps_ue_mode_operation': gi.FunctionInfo(set_eps_ue_mode_operation), 'set_eps_ue_mode_operation_finish': gi.FunctionInfo(set_eps_ue_mode_operation_finish), 'set_eps_ue_mode_operation_sync': gi.FunctionInfo(set_eps_ue_mode_operation_sync), 'set_initial_eps_bearer_settings': gi.FunctionInfo(set_initial_eps_bearer_settings), 'set_initial_eps_bearer_settings_finish': gi.FunctionInfo(set_initial_eps_bearer_settings_finish), 'set_initial_eps_bearer_settings_sync': gi.FunctionInfo(set_initial_eps_bearer_settings_sync), 'parent': <property object at 0x7f69438ab680>, 'priv': <property object at 0x7f69438ab770>})"
    __gdoc__ = 'Object MMModem3gpp\n\nSignals from MmGdbusModem3gpp:\n  handle-register (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-scan (GDBusMethodInvocation) -> gboolean\n  handle-set-eps-ue-mode-operation (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-initial-eps-bearer-settings (GDBusMethodInvocation, GVariant) -> gboolean\n\nSignals from MmGdbusModem3gpp:\n  handle-register (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-scan (GDBusMethodInvocation) -> gboolean\n  handle-set-eps-ue-mode-operation (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-initial-eps-bearer-settings (GDBusMethodInvocation, GVariant) -> gboolean\n\nSignals from GDBusProxy:\n  g-properties-changed (GVariant, GStrv)\n  g-signal (gchararray, gchararray, GVariant)\n\nProperties from GDBusProxy:\n  g-connection -> GDBusConnection: g-connection\n    The connection the proxy is for\n  g-bus-type -> GBusType: Bus Type\n    The bus to connect to, if any\n  g-name -> gchararray: g-name\n    The well-known or unique name that the proxy is for\n  g-name-owner -> gchararray: g-name-owner\n    The unique name for the owner\n  g-flags -> GDBusProxyFlags: g-flags\n    Flags for the proxy\n  g-object-path -> gchararray: g-object-path\n    The object path the proxy is for\n  g-interface-name -> gchararray: g-interface-name\n    The D-Bus interface name the proxy is for\n  g-default-timeout -> gint: Default Timeout\n    Timeout for remote method invocation\n  g-interface-info -> GDBusInterfaceInfo: Interface Information\n    Interface Information\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MMModem3gpp (94631948655632)>'
    __info__ = ObjectInfo(Modem3gpp)


