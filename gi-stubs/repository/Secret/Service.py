# encoding: utf-8
# module gi.repository.Secret
# from /usr/lib64/girepository-1.0/Secret-1.typelib
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
import gobject as __gobject


from .Backend import Backend

class Service(__gi_overrides_Gio.DBusProxy, Backend):
    """
    :Constructors:
    
    ::
    
        Service(**properties)
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

    def clear(self, schema=None, attributes, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ clear(self, schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def clear_finish(self, result): # real signature unknown; restored from __doc__
        """ clear_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def clear_sync(self, schema=None, attributes, cancellable=None): # real signature unknown; restored from __doc__
        """ clear_sync(self, schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None) -> bool """
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

    def create_item_dbus_path_sync(self, collection_path, properties, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ create_item_dbus_path_sync(self, collection_path:str, properties:dict, value:Secret.Value, flags:Secret.ItemCreateFlags, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def decode_dbus_secret(self, value): # real signature unknown; restored from __doc__
        """ decode_dbus_secret(self, value:GLib.Variant) -> Secret.Value """
        pass

    def disconnect(self): # real signature unknown; restored from __doc__
        """ disconnect() """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_get_collection_gtype(self, *args, **kwargs): # real signature unknown
        """ get_collection_gtype(self) -> GType """
        pass

    def do_get_item_gtype(self, *args, **kwargs): # real signature unknown
        """ get_item_gtype(self) -> GType """
        pass

    def do_g_properties_changed(self, *args, **kwargs): # real signature unknown
        """ g_properties_changed(self, changed_properties:GLib.Variant, invalidated_properties:str) """
        pass

    def do_g_signal(self, *args, **kwargs): # real signature unknown
        """ g_signal(self, sender_name:str, signal_name:str, parameters:GLib.Variant) """
        pass

    def do_prompt_async(self, *args, **kwargs): # real signature unknown
        """ prompt_async(self, prompt:Secret.Prompt, return_type:GLib.VariantType, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_prompt_finish(self, *args, **kwargs): # real signature unknown
        """ prompt_finish(self, result:Gio.AsyncResult) -> GLib.Variant """
        pass

    def do_prompt_sync(self, *args, **kwargs): # real signature unknown
        """ prompt_sync(self, prompt:Secret.Prompt, cancellable:Gio.Cancellable=None, return_type:GLib.VariantType) -> GLib.Variant """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def encode_dbus_secret(self, value): # real signature unknown; restored from __doc__
        """ encode_dbus_secret(self, value:Secret.Value) -> GLib.Variant """
        pass

    def ensure_session(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ ensure_session(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def ensure_session_finish(self, result): # real signature unknown; restored from __doc__
        """ ensure_session_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def ensure_session_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ ensure_session_sync(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def get(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get(flags:Secret.ServiceFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def get_collections(self): # real signature unknown; restored from __doc__
        """ get_collections(self) -> list or None """
        return []

    def get_collection_gtype(self): # real signature unknown; restored from __doc__
        """ get_collection_gtype(self) -> GType """
        pass

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_timeout(self): # real signature unknown; restored from __doc__
        """ get_default_timeout(self) -> int """
        return 0

    def get_finish(self, result): # real signature unknown; restored from __doc__
        """ get_finish(result:Gio.AsyncResult) -> Secret.Service """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Secret.ServiceFlags """
        pass

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> Gio.DBusInterfaceInfo """
        pass

    def get_interface_info(self): # real signature unknown; restored from __doc__
        """ get_interface_info(self) -> Gio.DBusInterfaceInfo or None """
        pass

    def get_interface_name(self): # real signature unknown; restored from __doc__
        """ get_interface_name(self) -> str """
        return ""

    def get_item_gtype(self): # real signature unknown; restored from __doc__
        """ get_item_gtype(self) -> GType """
        pass

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

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_session_algorithms(self): # real signature unknown; restored from __doc__
        """ get_session_algorithms(self) -> str or None """
        return ""

    def get_session_dbus_path(self): # real signature unknown; restored from __doc__
        """ get_session_dbus_path(self) -> str or None """
        return ""

    def get_sync(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ get_sync(flags:Secret.ServiceFlags, cancellable:Gio.Cancellable=None) -> Secret.Service """
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

    def load_collections(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_collections(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_collections_finish(self, result): # real signature unknown; restored from __doc__
        """ load_collections_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def load_collections_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_collections_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def lock(self, objects, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lock(self, objects:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lock_finish(self, result): # real signature unknown; restored from __doc__
        """ lock_finish(self, result:Gio.AsyncResult) -> int, locked:list """
        return 0

    def lock_sync(self, objects, cancellable=None): # real signature unknown; restored from __doc__
        """ lock_sync(self, objects:list, cancellable:Gio.Cancellable=None) -> int, locked:list """
        return 0

    def lookup(self, schema=None, attributes, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup(self, schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_finish(self, result:Gio.AsyncResult) -> Secret.Value """
        pass

    def lookup_sync(self, schema=None, attributes, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_sync(self, schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None) -> Secret.Value """
        pass

    def new(self, connection, flags, info=None, name=None, object_path, interface_name, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, info:Gio.DBusInterfaceInfo=None, name:str=None, object_path:str, interface_name:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, res): # real signature unknown; restored from __doc__
        """ new_finish(res:Gio.AsyncResult) -> Gio.DBusProxy """
        pass

    def new_for_bus(self, bus_type, flags, info=None, name, object_path, interface_name, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_for_bus(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, info:Gio.DBusInterfaceInfo=None, name:str, object_path:str, interface_name:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_for_bus_finish(self, res): # real signature unknown; restored from __doc__
        """ new_for_bus_finish(res:Gio.AsyncResult) -> Gio.DBusProxy """
        pass

    def new_for_bus_sync(self, bus_type, flags, info=None, name, object_path, interface_name, cancellable=None): # real signature unknown; restored from __doc__
        """ new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusProxyFlags, info:Gio.DBusInterfaceInfo=None, name:str, object_path:str, interface_name:str, cancellable:Gio.Cancellable=None) -> Gio.DBusProxy """
        pass

    def new_sync(self, connection, flags, info=None, name=None, object_path, interface_name, cancellable=None): # real signature unknown; restored from __doc__
        """ new_sync(connection:Gio.DBusConnection, flags:Gio.DBusProxyFlags, info:Gio.DBusInterfaceInfo=None, name:str=None, object_path:str, interface_name:str, cancellable:Gio.Cancellable=None) -> Gio.DBusProxy """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open(self, service_gtype, service_bus_name=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open(service_gtype:GType, service_bus_name:str=None, flags:Secret.ServiceFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(result:Gio.AsyncResult) -> Secret.Service """
        pass

    def open_sync(self, service_gtype, service_bus_name=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ open_sync(service_gtype:GType, service_bus_name:str=None, flags:Secret.ServiceFlags, cancellable:Gio.Cancellable=None) -> Secret.Service """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def prompt(self, prompt, return_type=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ prompt(self, prompt:Secret.Prompt, return_type:GLib.VariantType=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def prompt_finish(self, result): # real signature unknown; restored from __doc__
        """ prompt_finish(self, result:Gio.AsyncResult) -> GLib.Variant """
        pass

    def prompt_sync(self, prompt, cancellable=None, return_type): # real signature unknown; restored from __doc__
        """ prompt_sync(self, prompt:Secret.Prompt, cancellable:Gio.Cancellable=None, return_type:GLib.VariantType) -> GLib.Variant """
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

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def search(self, schema=None, attributes, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ search(self, schema:Secret.Schema=None, attributes:dict, flags:Secret.SearchFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def search_finish(self, result): # real signature unknown; restored from __doc__
        """ search_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def search_sync(self, schema=None, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ search_sync(self, schema:Secret.Schema=None, attributes:dict, flags:Secret.SearchFlags, cancellable:Gio.Cancellable=None) -> list """
        return []

    def set_alias(self, alias, collection=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_alias(self, alias:str, collection:Secret.Collection=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_alias_finish(self, result): # real signature unknown; restored from __doc__
        """ set_alias_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_alias_sync(self, alias, collection=None, cancellable=None): # real signature unknown; restored from __doc__
        """ set_alias_sync(self, alias:str, collection:Secret.Collection=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_cached_property(self, property_name, value=None): # real signature unknown; restored from __doc__
        """ set_cached_property(self, property_name:str, value:GLib.Variant=None) """
        pass

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

    def store(self, schema=None, attributes, collection=None, label, value, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ store(self, schema:Secret.Schema=None, attributes:dict, collection:str=None, label:str, value:Secret.Value, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def store_finish(self, result): # real signature unknown; restored from __doc__
        """ store_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def store_sync(self, schema=None, attributes, collection=None, label, value, cancellable=None): # real signature unknown; restored from __doc__
        """ store_sync(self, schema:Secret.Schema=None, attributes:dict, collection:str=None, label:str, value:Secret.Value, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlock(self, objects, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unlock(self, objects:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unlock_finish(self, result): # real signature unknown; restored from __doc__
        """ unlock_finish(self, result:Gio.AsyncResult) -> int, unlocked:list """
        return 0

    def unlock_sync(self, objects, cancellable=None): # real signature unknown; restored from __doc__
        """ unlock_sync(self, objects:list, cancellable:Gio.Cancellable=None) -> int, unlocked:list """
        return 0

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

    pv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa0c5986700>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Service), '__module__': 'gi.repository.Secret', '__gtype__': <GType SecretService (93972238583344)>, '__doc__': None, '__gsignals__': {}, 'disconnect': gi.FunctionInfo(disconnect), 'get': gi.FunctionInfo(get), 'get_finish': gi.FunctionInfo(get_finish), 'get_sync': gi.FunctionInfo(get_sync), 'open': gi.FunctionInfo(open), 'open_finish': gi.FunctionInfo(open_finish), 'open_sync': gi.FunctionInfo(open_sync), 'clear': gi.FunctionInfo(clear), 'clear_finish': gi.FunctionInfo(clear_finish), 'clear_sync': gi.FunctionInfo(clear_sync), 'create_item_dbus_path_sync': gi.FunctionInfo(create_item_dbus_path_sync), 'decode_dbus_secret': gi.FunctionInfo(decode_dbus_secret), 'encode_dbus_secret': gi.FunctionInfo(encode_dbus_secret), 'ensure_session': gi.FunctionInfo(ensure_session), 'ensure_session_finish': gi.FunctionInfo(ensure_session_finish), 'ensure_session_sync': gi.FunctionInfo(ensure_session_sync), 'get_collection_gtype': gi.FunctionInfo(get_collection_gtype), 'get_collections': gi.FunctionInfo(get_collections), 'get_flags': gi.FunctionInfo(get_flags), 'get_item_gtype': gi.FunctionInfo(get_item_gtype), 'get_session_algorithms': gi.FunctionInfo(get_session_algorithms), 'get_session_dbus_path': gi.FunctionInfo(get_session_dbus_path), 'load_collections': gi.FunctionInfo(load_collections), 'load_collections_finish': gi.FunctionInfo(load_collections_finish), 'load_collections_sync': gi.FunctionInfo(load_collections_sync), 'lock': gi.FunctionInfo(lock), 'lock_finish': gi.FunctionInfo(lock_finish), 'lock_sync': gi.FunctionInfo(lock_sync), 'lookup': gi.FunctionInfo(lookup), 'lookup_finish': gi.FunctionInfo(lookup_finish), 'lookup_sync': gi.FunctionInfo(lookup_sync), 'prompt': gi.FunctionInfo(prompt), 'prompt_finish': gi.FunctionInfo(prompt_finish), 'prompt_sync': gi.FunctionInfo(prompt_sync), 'search': gi.FunctionInfo(search), 'search_finish': gi.FunctionInfo(search_finish), 'search_sync': gi.FunctionInfo(search_sync), 'set_alias': gi.FunctionInfo(set_alias), 'set_alias_finish': gi.FunctionInfo(set_alias_finish), 'set_alias_sync': gi.FunctionInfo(set_alias_sync), 'store': gi.FunctionInfo(store), 'store_finish': gi.FunctionInfo(store_finish), 'store_sync': gi.FunctionInfo(store_sync), 'unlock': gi.FunctionInfo(unlock), 'unlock_finish': gi.FunctionInfo(unlock_finish), 'unlock_sync': gi.FunctionInfo(unlock_sync), 'do_get_collection_gtype': gi.VFuncInfo(get_collection_gtype), 'do_get_item_gtype': gi.VFuncInfo(get_item_gtype), 'do_prompt_async': gi.VFuncInfo(prompt_async), 'do_prompt_finish': gi.VFuncInfo(prompt_finish), 'do_prompt_sync': gi.VFuncInfo(prompt_sync), 'parent': <property object at 0x7fa0c59816d0>, 'pv': <property object at 0x7fa0c59817c0>})"
    __gdoc__ = 'Object SecretService\n\nProperties from SecretService:\n  collections -> SecretObjectList: Collections\n    Secret Service Collections\n\nSignals from GDBusProxy:\n  g-properties-changed (GVariant, GStrv)\n  g-signal (gchararray, gchararray, GVariant)\n\nProperties from GDBusProxy:\n  g-connection -> GDBusConnection: g-connection\n    The connection the proxy is for\n  g-bus-type -> GBusType: Bus Type\n    The bus to connect to, if any\n  g-name -> gchararray: g-name\n    The well-known or unique name that the proxy is for\n  g-name-owner -> gchararray: g-name-owner\n    The unique name for the owner\n  g-flags -> GDBusProxyFlags: g-flags\n    Flags for the proxy\n  g-object-path -> gchararray: g-object-path\n    The object path the proxy is for\n  g-interface-name -> gchararray: g-interface-name\n    The D-Bus interface name the proxy is for\n  g-default-timeout -> gint: Default Timeout\n    Timeout for remote method invocation\n  g-interface-info -> GDBusInterfaceInfo: Interface Information\n    Interface Information\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SecretService (93972238583344)>'
    __info__ = ObjectInfo(Service)


