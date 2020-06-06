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


from .GdbusModemProxy import GdbusModemProxy

class Modem(GdbusModemProxy):
    """
    :Constructors:
    
    ::
    
        Modem(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def call(self, method_name, parameters=None, flags, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call(self, method_name:str, parameters:GLib.Variant=None, flags:Gio.DBusCallFlags, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_command(self, arg_cmd, arg_timeout, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_command(self, arg_cmd:str, arg_timeout:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_command_finish(self, res): # real signature unknown; restored from __doc__
        """ call_command_finish(self, res:Gio.AsyncResult) -> out_response:str """
        pass

    def call_command_sync(self, arg_cmd, arg_timeout, cancellable=None): # real signature unknown; restored from __doc__
        """ call_command_sync(self, arg_cmd:str, arg_timeout:int, cancellable:Gio.Cancellable=None) -> out_response:str """
        pass

    def call_create_bearer(self, arg_properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_create_bearer(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_create_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ call_create_bearer_finish(self, res:Gio.AsyncResult) -> out_path:str """
        pass

    def call_create_bearer_sync(self, arg_properties, cancellable=None): # real signature unknown; restored from __doc__
        """ call_create_bearer_sync(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_path:str """
        pass

    def call_delete_bearer(self, arg_bearer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_delete_bearer(self, arg_bearer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_delete_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ call_delete_bearer_finish(self, res:Gio.AsyncResult) """
        pass

    def call_delete_bearer_sync(self, arg_bearer, cancellable=None): # real signature unknown; restored from __doc__
        """ call_delete_bearer_sync(self, arg_bearer:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_enable(self, arg_enable, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_enable(self, arg_enable:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_enable_finish(self, res): # real signature unknown; restored from __doc__
        """ call_enable_finish(self, res:Gio.AsyncResult) """
        pass

    def call_enable_sync(self, arg_enable, cancellable=None): # real signature unknown; restored from __doc__
        """ call_enable_sync(self, arg_enable:bool, cancellable:Gio.Cancellable=None) """
        pass

    def call_factory_reset(self, arg_code, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_factory_reset(self, arg_code:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_factory_reset_finish(self, res): # real signature unknown; restored from __doc__
        """ call_factory_reset_finish(self, res:Gio.AsyncResult) """
        pass

    def call_factory_reset_sync(self, arg_code, cancellable=None): # real signature unknown; restored from __doc__
        """ call_factory_reset_sync(self, arg_code:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_finish(self, res): # real signature unknown; restored from __doc__
        """ call_finish(self, res:Gio.AsyncResult) -> GLib.Variant """
        pass

    def call_list_bearers(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_list_bearers(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_list_bearers_finish(self, res): # real signature unknown; restored from __doc__
        """ call_list_bearers_finish(self, res:Gio.AsyncResult) -> out_bearers:list """
        pass

    def call_list_bearers_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_list_bearers_sync(self, cancellable:Gio.Cancellable=None) -> out_bearers:list """
        pass

    def call_reset(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_reset(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_reset_finish(self, res): # real signature unknown; restored from __doc__
        """ call_reset_finish(self, res:Gio.AsyncResult) """
        pass

    def call_reset_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_reset_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_bands(self, arg_bands, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_bands(self, arg_bands:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_bands_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_bands_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_bands_sync(self, arg_bands, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_bands_sync(self, arg_bands:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_capabilities(self, arg_capabilities, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities(self, arg_capabilities:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_capabilities_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_capabilities_sync(self, arg_capabilities, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities_sync(self, arg_capabilities:int, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_modes(self, arg_modes, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_modes(self, arg_modes:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_modes_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_modes_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_modes_sync(self, arg_modes, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_modes_sync(self, arg_modes:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_power_state(self, arg_state, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_power_state(self, arg_state:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_power_state_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_power_state_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_power_state_sync(self, arg_state, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_power_state_sync(self, arg_state:int, cancellable:Gio.Cancellable=None) """
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

    def command(self, cmd, timeout, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ command(self, cmd:str, timeout:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def command_finish(self, res): # real signature unknown; restored from __doc__
        """ command_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def command_sync(self, cmd, timeout, cancellable=None): # real signature unknown; restored from __doc__
        """ command_sync(self, cmd:str, timeout:int, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def complete_command(self, invocation, response): # real signature unknown; restored from __doc__
        """ complete_command(self, invocation:Gio.DBusMethodInvocation, response:str) """
        pass

    def complete_create_bearer(self, invocation, path): # real signature unknown; restored from __doc__
        """ complete_create_bearer(self, invocation:Gio.DBusMethodInvocation, path:str) """
        pass

    def complete_delete_bearer(self, invocation): # real signature unknown; restored from __doc__
        """ complete_delete_bearer(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_enable(self, invocation): # real signature unknown; restored from __doc__
        """ complete_enable(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_factory_reset(self, invocation): # real signature unknown; restored from __doc__
        """ complete_factory_reset(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_list_bearers(self, invocation, bearers): # real signature unknown; restored from __doc__
        """ complete_list_bearers(self, invocation:Gio.DBusMethodInvocation, bearers:str) """
        pass

    def complete_reset(self, invocation): # real signature unknown; restored from __doc__
        """ complete_reset(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_bands(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_bands(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_capabilities(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_capabilities(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_modes(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_modes(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_power_state(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_power_state(self, invocation:Gio.DBusMethodInvocation) """
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

    def create_bearer(self, properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_bearer(self, properties:ModemManager.BearerProperties, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ create_bearer_finish(self, res:Gio.AsyncResult) -> ModemManager.Bearer """
        pass

    def create_bearer_sync(self, properties, cancellable=None): # real signature unknown; restored from __doc__
        """ create_bearer_sync(self, properties:ModemManager.BearerProperties, cancellable:Gio.Cancellable=None) -> ModemManager.Bearer """
        pass

    def delete_bearer(self, bearer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_bearer(self, bearer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ delete_bearer_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def delete_bearer_sync(self, bearer, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_bearer_sync(self, bearer:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disable(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ disable(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def disable_finish(self, res): # real signature unknown; restored from __doc__
        """ disable_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def disable_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ disable_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def dup_bearer_paths(self): # real signature unknown; restored from __doc__
        """ dup_bearer_paths(self) -> list """
        return []

    def dup_carrier_configuration(self): # real signature unknown; restored from __doc__
        """ dup_carrier_configuration(self) -> str """
        return ""

    def dup_carrier_configuration_revision(self): # real signature unknown; restored from __doc__
        """ dup_carrier_configuration_revision(self) -> str """
        return ""

    def dup_device(self): # real signature unknown; restored from __doc__
        """ dup_device(self) -> str """
        return ""

    def dup_device_identifier(self): # real signature unknown; restored from __doc__
        """ dup_device_identifier(self) -> str """
        return ""

    def dup_drivers(self): # real signature unknown; restored from __doc__
        """ dup_drivers(self) -> list """
        return []

    def dup_equipment_identifier(self): # real signature unknown; restored from __doc__
        """ dup_equipment_identifier(self) -> str """
        return ""

    def dup_hardware_revision(self): # real signature unknown; restored from __doc__
        """ dup_hardware_revision(self) -> str """
        return ""

    def dup_manufacturer(self): # real signature unknown; restored from __doc__
        """ dup_manufacturer(self) -> str """
        return ""

    def dup_model(self): # real signature unknown; restored from __doc__
        """ dup_model(self) -> str """
        return ""

    def dup_own_numbers(self): # real signature unknown; restored from __doc__
        """ dup_own_numbers(self) -> list """
        return []

    def dup_path(self): # real signature unknown; restored from __doc__
        """ dup_path(self) -> str """
        return ""

    def dup_plugin(self): # real signature unknown; restored from __doc__
        """ dup_plugin(self) -> str """
        return ""

    def dup_primary_port(self): # real signature unknown; restored from __doc__
        """ dup_primary_port(self) -> str """
        return ""

    def dup_revision(self): # real signature unknown; restored from __doc__
        """ dup_revision(self) -> str """
        return ""

    def dup_sim_path(self): # real signature unknown; restored from __doc__
        """ dup_sim_path(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_state_changed(self, arg_old, arg_new, arg_reason): # real signature unknown; restored from __doc__
        """ emit_state_changed(self, arg_old:int, arg_new:int, arg_reason:int) """
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def enable(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ enable(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def enable_finish(self, res): # real signature unknown; restored from __doc__
        """ enable_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def enable_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ enable_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def factory_reset(self, code, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ factory_reset(self, code:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def factory_reset_finish(self, res): # real signature unknown; restored from __doc__
        """ factory_reset_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def factory_reset_sync(self, code, cancellable=None): # real signature unknown; restored from __doc__
        """ factory_reset_sync(self, code:str, cancellable:Gio.Cancellable=None) -> bool """
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

    def get_access_technologies(self): # real signature unknown; restored from __doc__
        """ get_access_technologies(self) -> ModemManager.ModemAccessTechnology """
        pass

    def get_bearer_paths(self): # real signature unknown; restored from __doc__
        """ get_bearer_paths(self) -> list """
        return []

    def get_cached_property(self, property_name): # real signature unknown; restored from __doc__
        """ get_cached_property(self, property_name:str) -> GLib.Variant or None """
        pass

    def get_cached_property_names(self): # real signature unknown; restored from __doc__
        """ get_cached_property_names(self) -> list or None """
        return []

    def get_carrier_configuration(self): # real signature unknown; restored from __doc__
        """ get_carrier_configuration(self) -> str """
        return ""

    def get_carrier_configuration_revision(self): # real signature unknown; restored from __doc__
        """ get_carrier_configuration_revision(self) -> str """
        return ""

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_current_bands(self): # real signature unknown; restored from __doc__
        """ get_current_bands(self) -> bool, bands:list """
        return False

    def get_current_capabilities(self): # real signature unknown; restored from __doc__
        """ get_current_capabilities(self) -> ModemManager.ModemCapability """
        pass

    def get_current_modes(self): # real signature unknown; restored from __doc__
        """ get_current_modes(self) -> bool, allowed:ModemManager.ModemMode, preferred:ModemManager.ModemMode """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_timeout(self): # real signature unknown; restored from __doc__
        """ get_default_timeout(self) -> int """
        return 0

    def get_device(self): # real signature unknown; restored from __doc__
        """ get_device(self) -> str """
        return ""

    def get_device_identifier(self): # real signature unknown; restored from __doc__
        """ get_device_identifier(self) -> str """
        return ""

    def get_drivers(self): # real signature unknown; restored from __doc__
        """ get_drivers(self) -> list """
        return []

    def get_equipment_identifier(self): # real signature unknown; restored from __doc__
        """ get_equipment_identifier(self) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.DBusProxyFlags """
        pass

    def get_hardware_revision(self): # real signature unknown; restored from __doc__
        """ get_hardware_revision(self) -> str """
        return ""

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> Gio.DBusInterfaceInfo """
        pass

    def get_interface_info(self): # real signature unknown; restored from __doc__
        """ get_interface_info(self) -> Gio.DBusInterfaceInfo or None """
        pass

    def get_interface_name(self): # real signature unknown; restored from __doc__
        """ get_interface_name(self) -> str """
        return ""

    def get_manufacturer(self): # real signature unknown; restored from __doc__
        """ get_manufacturer(self) -> str """
        return ""

    def get_max_active_bearers(self): # real signature unknown; restored from __doc__
        """ get_max_active_bearers(self) -> int """
        return 0

    def get_max_bearers(self): # real signature unknown; restored from __doc__
        """ get_max_bearers(self) -> int """
        return 0

    def get_model(self): # real signature unknown; restored from __doc__
        """ get_model(self) -> str """
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

    def get_pending_network_initiated_sessions(self): # real signature unknown; restored from __doc__
        """ get_pending_network_initiated_sessions(self:ModemManager.ModemOma) -> bool, sessions:list """
        return False

    def get_plugin(self): # real signature unknown; restored from __doc__
        """ get_plugin(self) -> str """
        return ""

    def get_ports(self): # real signature unknown; restored from __doc__
        """ get_ports(self) -> bool, ports:list """
        return False

    def get_power_state(self): # real signature unknown; restored from __doc__
        """ get_power_state(self) -> ModemManager.ModemPowerState """
        pass

    def get_primary_port(self): # real signature unknown; restored from __doc__
        """ get_primary_port(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_revision(self): # real signature unknown; restored from __doc__
        """ get_revision(self) -> str """
        return ""

    def get_signal_quality(self): # real signature unknown; restored from __doc__
        """ get_signal_quality(self) -> int, recent:bool """
        return 0

    def get_sim(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_sim(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_sim_finish(self, res): # real signature unknown; restored from __doc__
        """ get_sim_finish(self, res:Gio.AsyncResult) -> ModemManager.Sim """
        pass

    def get_sim_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_sim_sync(self, cancellable:Gio.Cancellable=None) -> ModemManager.Sim """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> ModemManager.ModemState """
        pass

    def get_state_failed_reason(self): # real signature unknown; restored from __doc__
        """ get_state_failed_reason(self) -> ModemManager.ModemStateFailedReason """
        pass

    def get_supported_bands(self): # real signature unknown; restored from __doc__
        """ get_supported_bands(self) -> bool, bands:list """
        return False

    def get_supported_capabilities(self): # real signature unknown; restored from __doc__
        """ get_supported_capabilities(self) -> bool, capabilities:list """
        return False

    def get_supported_ip_families(self): # real signature unknown; restored from __doc__
        """ get_supported_ip_families(self) -> ModemManager.BearerIpFamily """
        pass

    def get_supported_modes(self): # real signature unknown; restored from __doc__
        """ get_supported_modes(self) -> bool, modes:list """
        return False

    def get_unlock_required(self): # real signature unknown; restored from __doc__
        """ get_unlock_required(self) -> ModemManager.ModemLock """
        pass

    def get_unlock_retries(self): # real signature unknown; restored from __doc__
        """ get_unlock_retries(self) -> ModemManager.UnlockRetries """
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

    def list_bearers(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ list_bearers(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def list_bearers_finish(self, res): # real signature unknown; restored from __doc__
        """ list_bearers_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def list_bearers_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ list_bearers_sync(self, cancellable:Gio.Cancellable=None) -> list """
        return []

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
        """ new_finish(res:Gio.AsyncResult) -> ModemManager.GdbusModemProxy """
        pass

    def new_for_bus(self, bus_type, flags, name, object_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_for_bus(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_for_bus_finish(self, res): # real signature unknown; restored from __doc__
        """ new_for_bus_finish(res:Gio.AsyncResult) -> ModemManager.GdbusModemProxy """
        pass

    def new_for_bus_sync(self, bus_type, flags, name, object_path, cancellable=None): # real signature unknown; restored from __doc__
        """ new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> ModemManager.GdbusModemProxy """
        pass

    def new_sync(self, connection, flags, name=None, object_path, cancellable=None): # real signature unknown; restored from __doc__
        """ new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, name:str=None, object_path:str, cancellable:Gio.Cancellable=None) -> ModemManager.GdbusModemProxy """
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

    def peek_current_bands(self): # real signature unknown; restored from __doc__
        """ peek_current_bands(self) -> bool, bands:list """
        return False

    def peek_pending_network_initiated_sessions(self): # real signature unknown; restored from __doc__
        """ peek_pending_network_initiated_sessions(self:ModemManager.ModemOma) -> bool, sessions:list """
        return False

    def peek_ports(self): # real signature unknown; restored from __doc__
        """ peek_ports(self) -> bool, ports:list """
        return False

    def peek_supported_bands(self): # real signature unknown; restored from __doc__
        """ peek_supported_bands(self) -> bool, bands:list """
        return False

    def peek_supported_capabilities(self): # real signature unknown; restored from __doc__
        """ peek_supported_capabilities(self) -> bool, capabilities:list """
        return False

    def peek_supported_modes(self): # real signature unknown; restored from __doc__
        """ peek_supported_modes(self) -> bool, modes:list """
        return False

    def peek_unlock_retries(self): # real signature unknown; restored from __doc__
        """ peek_unlock_retries(self) -> ModemManager.UnlockRetries """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ reset(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def reset_finish(self, res): # real signature unknown; restored from __doc__
        """ reset_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def reset_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ reset_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_cached_property(self, property_name, value=None): # real signature unknown; restored from __doc__
        """ set_cached_property(self, property_name:str, value:GLib.Variant=None) """
        pass

    def set_current_bands(self, bands, n_bands, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_current_bands(self, bands:ModemManager.ModemBand, n_bands:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_current_bands_finish(self, res): # real signature unknown; restored from __doc__
        """ set_current_bands_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_current_bands_sync(self, bands, n_bands, cancellable=None): # real signature unknown; restored from __doc__
        """ set_current_bands_sync(self, bands:ModemManager.ModemBand, n_bands:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_current_capabilities(self, capabilities, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_current_capabilities(self, capabilities:ModemManager.ModemCapability, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_current_capabilities_finish(self, res): # real signature unknown; restored from __doc__
        """ set_current_capabilities_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_current_capabilities_sync(self, capabilities, cancellable=None): # real signature unknown; restored from __doc__
        """ set_current_capabilities_sync(self, capabilities:ModemManager.ModemCapability, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_current_modes(self, modes, preferred, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_current_modes(self, modes:ModemManager.ModemMode, preferred:ModemManager.ModemMode, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_current_modes_finish(self, res): # real signature unknown; restored from __doc__
        """ set_current_modes_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_current_modes_sync(self, modes, preferred, cancellable=None): # real signature unknown; restored from __doc__
        """ set_current_modes_sync(self, modes:ModemManager.ModemMode, preferred:ModemManager.ModemMode, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_timeout(self, timeout_msec): # real signature unknown; restored from __doc__
        """ set_default_timeout(self, timeout_msec:int) """
        pass

    def set_interface_info(self, info=None): # real signature unknown; restored from __doc__
        """ set_interface_info(self, info:Gio.DBusInterfaceInfo=None) """
        pass

    def set_object(self, p_object=None): # real signature unknown; restored from __doc__
        """ set_object(self, object:Gio.DBusObject=None) """
        pass

    def set_power_state(self, state, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_power_state(self, state:ModemManager.ModemPowerState, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_power_state_finish(self, res): # real signature unknown; restored from __doc__
        """ set_power_state_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_power_state_sync(self, state, cancellable=None): # real signature unknown; restored from __doc__
        """ set_power_state_sync(self, state:ModemManager.ModemPowerState, cancellable:Gio.Cancellable=None) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f69436d3190>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Modem), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MMModem (94631948251728)>, '__doc__': None, '__gsignals__': {}, 'get_pending_network_initiated_sessions': gi.FunctionInfo(get_pending_network_initiated_sessions), 'peek_pending_network_initiated_sessions': gi.FunctionInfo(peek_pending_network_initiated_sessions), 'command': gi.FunctionInfo(command), 'command_finish': gi.FunctionInfo(command_finish), 'command_sync': gi.FunctionInfo(command_sync), 'create_bearer': gi.FunctionInfo(create_bearer), 'create_bearer_finish': gi.FunctionInfo(create_bearer_finish), 'create_bearer_sync': gi.FunctionInfo(create_bearer_sync), 'delete_bearer': gi.FunctionInfo(delete_bearer), 'delete_bearer_finish': gi.FunctionInfo(delete_bearer_finish), 'delete_bearer_sync': gi.FunctionInfo(delete_bearer_sync), 'disable': gi.FunctionInfo(disable), 'disable_finish': gi.FunctionInfo(disable_finish), 'disable_sync': gi.FunctionInfo(disable_sync), 'dup_bearer_paths': gi.FunctionInfo(dup_bearer_paths), 'dup_carrier_configuration': gi.FunctionInfo(dup_carrier_configuration), 'dup_carrier_configuration_revision': gi.FunctionInfo(dup_carrier_configuration_revision), 'dup_device': gi.FunctionInfo(dup_device), 'dup_device_identifier': gi.FunctionInfo(dup_device_identifier), 'dup_drivers': gi.FunctionInfo(dup_drivers), 'dup_equipment_identifier': gi.FunctionInfo(dup_equipment_identifier), 'dup_hardware_revision': gi.FunctionInfo(dup_hardware_revision), 'dup_manufacturer': gi.FunctionInfo(dup_manufacturer), 'dup_model': gi.FunctionInfo(dup_model), 'dup_own_numbers': gi.FunctionInfo(dup_own_numbers), 'dup_path': gi.FunctionInfo(dup_path), 'dup_plugin': gi.FunctionInfo(dup_plugin), 'dup_primary_port': gi.FunctionInfo(dup_primary_port), 'dup_revision': gi.FunctionInfo(dup_revision), 'dup_sim_path': gi.FunctionInfo(dup_sim_path), 'enable': gi.FunctionInfo(enable), 'enable_finish': gi.FunctionInfo(enable_finish), 'enable_sync': gi.FunctionInfo(enable_sync), 'factory_reset': gi.FunctionInfo(factory_reset), 'factory_reset_finish': gi.FunctionInfo(factory_reset_finish), 'factory_reset_sync': gi.FunctionInfo(factory_reset_sync), 'get_access_technologies': gi.FunctionInfo(get_access_technologies), 'get_bearer_paths': gi.FunctionInfo(get_bearer_paths), 'get_carrier_configuration': gi.FunctionInfo(get_carrier_configuration), 'get_carrier_configuration_revision': gi.FunctionInfo(get_carrier_configuration_revision), 'get_current_bands': gi.FunctionInfo(get_current_bands), 'get_current_capabilities': gi.FunctionInfo(get_current_capabilities), 'get_current_modes': gi.FunctionInfo(get_current_modes), 'get_device': gi.FunctionInfo(get_device), 'get_device_identifier': gi.FunctionInfo(get_device_identifier), 'get_drivers': gi.FunctionInfo(get_drivers), 'get_equipment_identifier': gi.FunctionInfo(get_equipment_identifier), 'get_hardware_revision': gi.FunctionInfo(get_hardware_revision), 'get_manufacturer': gi.FunctionInfo(get_manufacturer), 'get_max_active_bearers': gi.FunctionInfo(get_max_active_bearers), 'get_max_bearers': gi.FunctionInfo(get_max_bearers), 'get_model': gi.FunctionInfo(get_model), 'get_plugin': gi.FunctionInfo(get_plugin), 'get_ports': gi.FunctionInfo(get_ports), 'get_power_state': gi.FunctionInfo(get_power_state), 'get_primary_port': gi.FunctionInfo(get_primary_port), 'get_revision': gi.FunctionInfo(get_revision), 'get_signal_quality': gi.FunctionInfo(get_signal_quality), 'get_sim': gi.FunctionInfo(get_sim), 'get_sim_finish': gi.FunctionInfo(get_sim_finish), 'get_sim_sync': gi.FunctionInfo(get_sim_sync), 'get_state': gi.FunctionInfo(get_state), 'get_state_failed_reason': gi.FunctionInfo(get_state_failed_reason), 'get_supported_bands': gi.FunctionInfo(get_supported_bands), 'get_supported_capabilities': gi.FunctionInfo(get_supported_capabilities), 'get_supported_ip_families': gi.FunctionInfo(get_supported_ip_families), 'get_supported_modes': gi.FunctionInfo(get_supported_modes), 'get_unlock_required': gi.FunctionInfo(get_unlock_required), 'get_unlock_retries': gi.FunctionInfo(get_unlock_retries), 'list_bearers': gi.FunctionInfo(list_bearers), 'list_bearers_finish': gi.FunctionInfo(list_bearers_finish), 'list_bearers_sync': gi.FunctionInfo(list_bearers_sync), 'peek_current_bands': gi.FunctionInfo(peek_current_bands), 'peek_ports': gi.FunctionInfo(peek_ports), 'peek_supported_bands': gi.FunctionInfo(peek_supported_bands), 'peek_supported_capabilities': gi.FunctionInfo(peek_supported_capabilities), 'peek_supported_modes': gi.FunctionInfo(peek_supported_modes), 'peek_unlock_retries': gi.FunctionInfo(peek_unlock_retries), 'reset': gi.FunctionInfo(reset), 'reset_finish': gi.FunctionInfo(reset_finish), 'reset_sync': gi.FunctionInfo(reset_sync), 'set_current_bands': gi.FunctionInfo(set_current_bands), 'set_current_bands_finish': gi.FunctionInfo(set_current_bands_finish), 'set_current_bands_sync': gi.FunctionInfo(set_current_bands_sync), 'set_current_capabilities': gi.FunctionInfo(set_current_capabilities), 'set_current_capabilities_finish': gi.FunctionInfo(set_current_capabilities_finish), 'set_current_capabilities_sync': gi.FunctionInfo(set_current_capabilities_sync), 'set_current_modes': gi.FunctionInfo(set_current_modes), 'set_current_modes_finish': gi.FunctionInfo(set_current_modes_finish), 'set_current_modes_sync': gi.FunctionInfo(set_current_modes_sync), 'set_power_state': gi.FunctionInfo(set_power_state), 'set_power_state_finish': gi.FunctionInfo(set_power_state_finish), 'set_power_state_sync': gi.FunctionInfo(set_power_state_sync), 'parent': <property object at 0x7f69438ab130>, 'priv': <property object at 0x7f69438ab220>})"
    __gdoc__ = 'Object MMModem\n\nSignals from MmGdbusModem:\n  state-changed (gint, gint, guint)\n  handle-enable (GDBusMethodInvocation, gboolean) -> gboolean\n  handle-list-bearers (GDBusMethodInvocation) -> gboolean\n  handle-create-bearer (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-delete-bearer (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-reset (GDBusMethodInvocation) -> gboolean\n  handle-factory-reset (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-set-power-state (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-current-capabilities (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-current-modes (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-set-current-bands (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-command (GDBusMethodInvocation, gchararray, guint) -> gboolean\n\nSignals from MmGdbusModem:\n  state-changed (gint, gint, guint)\n  handle-enable (GDBusMethodInvocation, gboolean) -> gboolean\n  handle-list-bearers (GDBusMethodInvocation) -> gboolean\n  handle-create-bearer (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-delete-bearer (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-reset (GDBusMethodInvocation) -> gboolean\n  handle-factory-reset (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-set-power-state (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-current-capabilities (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-current-modes (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-set-current-bands (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-command (GDBusMethodInvocation, gchararray, guint) -> gboolean\n\nSignals from GDBusProxy:\n  g-properties-changed (GVariant, GStrv)\n  g-signal (gchararray, gchararray, GVariant)\n\nProperties from GDBusProxy:\n  g-connection -> GDBusConnection: g-connection\n    The connection the proxy is for\n  g-bus-type -> GBusType: Bus Type\n    The bus to connect to, if any\n  g-name -> gchararray: g-name\n    The well-known or unique name that the proxy is for\n  g-name-owner -> gchararray: g-name-owner\n    The unique name for the owner\n  g-flags -> GDBusProxyFlags: g-flags\n    Flags for the proxy\n  g-object-path -> gchararray: g-object-path\n    The object path the proxy is for\n  g-interface-name -> gchararray: g-interface-name\n    The D-Bus interface name the proxy is for\n  g-default-timeout -> gint: Default Timeout\n    Timeout for remote method invocation\n  g-interface-info -> GDBusInterfaceInfo: Interface Information\n    Interface Information\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MMModem (94631948251728)>'
    __info__ = ObjectInfo(Modem)


