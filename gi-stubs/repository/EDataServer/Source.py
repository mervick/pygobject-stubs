# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


class Source(__gi_overrides_GObject.Object, __gi_repository_Gio.Initable, __gi_repository_Gio.ProxyResolver):
    """
    :Constructors:
    
    ::
    
        Source(**properties)
        new(dbus_object:Gio.DBusObject=None, main_context:GLib.MainContext=None) -> EDataServer.Source
        new_with_uid(uid:str, main_context:GLib.MainContext=None) -> EDataServer.Source
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def camel_configure_service(self, service): # real signature unknown; restored from __doc__
        """ camel_configure_service(self, service:Camel.Service) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) """
        pass

    def compare_by_display_name(self, source2): # real signature unknown; restored from __doc__
        """ compare_by_display_name(self, source2:EDataServer.Source) -> int """
        return 0

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

    def delete_password(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_password(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_password_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_password_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def delete_password_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_password_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authenticate(self, *args, **kwargs): # real signature unknown
        """ authenticate(self, credentials:EDataServer.NamedParameters) """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_credentials_required(self, *args, **kwargs): # real signature unknown
        """ credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error) """
        pass

    def do_get_oauth2_access_token(self, *args, **kwargs): # real signature unknown
        """ get_oauth2_access_token(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_get_oauth2_access_token_finish(self, *args, **kwargs): # real signature unknown
        """ get_oauth2_access_token_finish(self, result:Gio.AsyncResult) -> bool, out_access_token:str, out_expires_in:int """
        pass

    def do_get_oauth2_access_token_sync(self, *args, **kwargs): # real signature unknown
        """ get_oauth2_access_token_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_access_token:str, out_expires_in:int """
        pass

    def do_invoke_authenticate_impl(self, *args, **kwargs): # real signature unknown
        """ invoke_authenticate_impl(self, dbus_source=None, arg_credentials:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_invoke_credentials_required_impl(self, *args, **kwargs): # real signature unknown
        """ invoke_credentials_required_impl(self, dbus_source=None, arg_reason:str, arg_certificate_pem:str, arg_certificate_errors:str, arg_dbus_error_name:str, arg_dbus_error_message:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remote_create(self, *args, **kwargs): # real signature unknown
        """ remote_create(self, scratch_source:EDataServer.Source, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_remote_create_finish(self, *args, **kwargs): # real signature unknown
        """ remote_create_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_remote_create_sync(self, *args, **kwargs): # real signature unknown
        """ remote_create_sync(self, scratch_source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remote_delete(self, *args, **kwargs): # real signature unknown
        """ remote_delete(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_remote_delete_finish(self, *args, **kwargs): # real signature unknown
        """ remote_delete_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_remote_delete_sync(self, *args, **kwargs): # real signature unknown
        """ remote_delete_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_remove_finish(self, *args, **kwargs): # real signature unknown
        """ remove_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_remove_sync(self, *args, **kwargs): # real signature unknown
        """ remove_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_unset_last_credentials_required_arguments_impl(self, *args, **kwargs): # real signature unknown
        """ unset_last_credentials_required_arguments_impl(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_write(self, *args, **kwargs): # real signature unknown
        """ write(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_write_finish(self, *args, **kwargs): # real signature unknown
        """ write_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_write_sync(self, *args, **kwargs): # real signature unknown
        """ write_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def dup_display_name(self): # real signature unknown; restored from __doc__
        """ dup_display_name(self) -> str """
        return ""

    def dup_parent(self): # real signature unknown; restored from __doc__
        """ dup_parent(self) -> str """
        return ""

    def dup_secret_label(self): # real signature unknown; restored from __doc__
        """ dup_secret_label(self) -> str """
        return ""

    def dup_uid(self): # real signature unknown; restored from __doc__
        """ dup_uid(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None): # real signature unknown; restored from __doc__
        """ emit_credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None) """
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equal(self, source2): # real signature unknown; restored from __doc__
        """ equal(self, source2:EDataServer.Source) -> bool """
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

    def get_connection_status(self): # real signature unknown; restored from __doc__
        """ get_connection_status(self) -> EDataServer.SourceConnectionStatus """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gio.ProxyResolver """
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_enabled(self): # real signature unknown; restored from __doc__
        """ get_enabled(self) -> bool """
        return False

    def get_extension(self, extension_name): # real signature unknown; restored from __doc__
        """ get_extension(self, extension_name:str) -> EDataServer.SourceExtension """
        pass

    def get_last_credentials_required_arguments(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_last_credentials_required_arguments(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_last_credentials_required_arguments_finish(self, result): # real signature unknown; restored from __doc__
        """ get_last_credentials_required_arguments_finish(self, result:Gio.AsyncResult) -> bool, out_reason:EDataServer.SourceCredentialsReason, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, out_op_error:error """
        return False

    def get_last_credentials_required_arguments_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_last_credentials_required_arguments_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_reason:EDataServer.SourceCredentialsReason, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, out_op_error:error """
        return False

    def get_oauth2_access_token(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_oauth2_access_token(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_oauth2_access_token_finish(self, result): # real signature unknown; restored from __doc__
        """ get_oauth2_access_token_finish(self, result:Gio.AsyncResult) -> bool, out_access_token:str, out_expires_in:int """
        return False

    def get_oauth2_access_token_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_oauth2_access_token_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_access_token:str, out_expires_in:int """
        return False

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_creatable(self): # real signature unknown; restored from __doc__
        """ get_remote_creatable(self) -> bool """
        return False

    def get_remote_deletable(self): # real signature unknown; restored from __doc__
        """ get_remote_deletable(self) -> bool """
        return False

    def get_removable(self): # real signature unknown; restored from __doc__
        """ get_removable(self) -> bool """
        return False

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def get_writable(self): # real signature unknown; restored from __doc__
        """ get_writable(self) -> bool """
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

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def has_extension(self, extension_name): # real signature unknown; restored from __doc__
        """ has_extension(self, extension_name:str) -> bool """
        return False

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def invoke_authenticate(self, credentials=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ invoke_authenticate(self, credentials:EDataServer.NamedParameters=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def invoke_authenticate_finish(self, result): # real signature unknown; restored from __doc__
        """ invoke_authenticate_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def invoke_authenticate_sync(self, credentials=None, cancellable=None): # real signature unknown; restored from __doc__
        """ invoke_authenticate_sync(self, credentials:EDataServer.NamedParameters=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def invoke_credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ invoke_credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def invoke_credentials_required_finish(self, result): # real signature unknown; restored from __doc__
        """ invoke_credentials_required_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def invoke_credentials_required_sync(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None): # real signature unknown; restored from __doc__
        """ invoke_credentials_required_sync(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_supported(self): # real signature unknown; restored from __doc__
        """ is_supported(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lookup(self, uri, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup(self, uri:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def lookup_async(self, uri, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_async(self, uri:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def lookup_password(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_password(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_password_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_password_finish(self, result:Gio.AsyncResult) -> bool, out_password:str """
        return False

    def lookup_password_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_password_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_password:str """
        return False

    def mail_signature_load(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mail_signature_load(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mail_signature_load_finish(self, result): # real signature unknown; restored from __doc__
        """ mail_signature_load_finish(self, result:Gio.AsyncResult) -> bool, contents:str, length:int """
        return False

    def mail_signature_load_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ mail_signature_load_sync(self, cancellable:Gio.Cancellable=None) -> bool, contents:str, length:int """
        return False

    def mail_signature_replace(self, contents, length, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mail_signature_replace(self, contents:str, length:int, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mail_signature_replace_finish(self, result): # real signature unknown; restored from __doc__
        """ mail_signature_replace_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def mail_signature_replace_sync(self, contents, length, cancellable=None): # real signature unknown; restored from __doc__
        """ mail_signature_replace_sync(self, contents:str, length:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def mail_signature_symlink(self, symlink_target, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mail_signature_symlink(self, symlink_target:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mail_signature_symlink_finish(self, result): # real signature unknown; restored from __doc__
        """ mail_signature_symlink_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def mail_signature_symlink_sync(self, symlink_target, cancellable=None): # real signature unknown; restored from __doc__
        """ mail_signature_symlink_sync(self, symlink_target:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def new(self, dbus_object=None, main_context=None): # real signature unknown; restored from __doc__
        """ new(dbus_object:Gio.DBusObject=None, main_context:GLib.MainContext=None) -> EDataServer.Source """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_uid(self, uid, main_context=None): # real signature unknown; restored from __doc__
        """ new_with_uid(uid:str, main_context:GLib.MainContext=None) -> EDataServer.Source """
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

    def parameter_to_key(self, param_name): # real signature unknown; restored from __doc__
        """ parameter_to_key(param_name:str) -> str """
        return ""

    def proxy_lookup(self, uri, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ proxy_lookup(self, uri:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def proxy_lookup_finish(self, result): # real signature unknown; restored from __doc__
        """ proxy_lookup_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def proxy_lookup_sync(self, uri, cancellable=None): # real signature unknown; restored from __doc__
        """ proxy_lookup_sync(self, uri:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh_add_timeout(self, context=None, callback, user_data=None): # real signature unknown; restored from __doc__
        """ refresh_add_timeout(self, context:GLib.MainContext=None, callback:EDataServer.SourceRefreshFunc, user_data=None) -> int """
        return 0

    def refresh_force_timeout(self): # real signature unknown; restored from __doc__
        """ refresh_force_timeout(self) """
        pass

    def refresh_remove_timeout(self, refresh_timeout_id): # real signature unknown; restored from __doc__
        """ refresh_remove_timeout(self, refresh_timeout_id:int) -> bool """
        return False

    def refresh_remove_timeouts_by_data(self, user_data=None): # real signature unknown; restored from __doc__
        """ refresh_remove_timeouts_by_data(self, user_data=None) -> int """
        return 0

    def ref_dbus_object(self): # real signature unknown; restored from __doc__
        """ ref_dbus_object(self) -> Gio.DBusObject """
        pass

    def ref_main_context(self): # real signature unknown; restored from __doc__
        """ ref_main_context(self) -> GLib.MainContext """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remote_create(self, scratch_source, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remote_create(self, scratch_source:EDataServer.Source, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remote_create_finish(self, result): # real signature unknown; restored from __doc__
        """ remote_create_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remote_create_sync(self, scratch_source, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_create_sync(self, scratch_source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remote_delete(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remote_delete(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remote_delete_finish(self, result): # real signature unknown; restored from __doc__
        """ remote_delete_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remote_delete_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_delete_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_sync(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def set_connection_status(self, connection_status): # real signature unknown; restored from __doc__
        """ set_connection_status(self, connection_status:EDataServer.SourceConnectionStatus) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_display_name(self, display_name): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str) """
        pass

    def set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_enabled(self, enabled:bool) """
        pass

    def set_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:str=None) """
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

    def store_password(self, password, permanently, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ store_password(self, password:str, permanently:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def store_password_finish(self, result): # real signature unknown; restored from __doc__
        """ store_password_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def store_password_sync(self, password, permanently, cancellable=None): # real signature unknown; restored from __doc__
        """ store_password_sync(self, password:str, permanently:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def to_string(self, length=None): # real signature unknown; restored from __doc__
        """ to_string(self, length:int=None) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unset_last_credentials_required_arguments(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unset_last_credentials_required_arguments(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unset_last_credentials_required_arguments_finish(self, result): # real signature unknown; restored from __doc__
        """ unset_last_credentials_required_arguments_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unset_last_credentials_required_arguments_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ unset_last_credentials_required_arguments_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_finish(self, result): # real signature unknown; restored from __doc__
        """ write_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def write_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ write_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f6271ba8520>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Source), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ESource (94877537038912)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_uid': gi.FunctionInfo(new_with_uid), 'parameter_to_key': gi.FunctionInfo(parameter_to_key), 'camel_configure_service': gi.FunctionInfo(camel_configure_service), 'changed': gi.FunctionInfo(changed), 'compare_by_display_name': gi.FunctionInfo(compare_by_display_name), 'delete_password': gi.FunctionInfo(delete_password), 'delete_password_finish': gi.FunctionInfo(delete_password_finish), 'delete_password_sync': gi.FunctionInfo(delete_password_sync), 'dup_display_name': gi.FunctionInfo(dup_display_name), 'dup_parent': gi.FunctionInfo(dup_parent), 'dup_secret_label': gi.FunctionInfo(dup_secret_label), 'dup_uid': gi.FunctionInfo(dup_uid), 'emit_credentials_required': gi.FunctionInfo(emit_credentials_required), 'equal': gi.FunctionInfo(equal), 'get_connection_status': gi.FunctionInfo(get_connection_status), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_enabled': gi.FunctionInfo(get_enabled), 'get_extension': gi.FunctionInfo(get_extension), 'get_last_credentials_required_arguments': gi.FunctionInfo(get_last_credentials_required_arguments), 'get_last_credentials_required_arguments_finish': gi.FunctionInfo(get_last_credentials_required_arguments_finish), 'get_last_credentials_required_arguments_sync': gi.FunctionInfo(get_last_credentials_required_arguments_sync), 'get_oauth2_access_token': gi.FunctionInfo(get_oauth2_access_token), 'get_oauth2_access_token_finish': gi.FunctionInfo(get_oauth2_access_token_finish), 'get_oauth2_access_token_sync': gi.FunctionInfo(get_oauth2_access_token_sync), 'get_parent': gi.FunctionInfo(get_parent), 'get_remote_creatable': gi.FunctionInfo(get_remote_creatable), 'get_remote_deletable': gi.FunctionInfo(get_remote_deletable), 'get_removable': gi.FunctionInfo(get_removable), 'get_uid': gi.FunctionInfo(get_uid), 'get_writable': gi.FunctionInfo(get_writable), 'has_extension': gi.FunctionInfo(has_extension), 'hash': gi.FunctionInfo(hash), 'invoke_authenticate': gi.FunctionInfo(invoke_authenticate), 'invoke_authenticate_finish': gi.FunctionInfo(invoke_authenticate_finish), 'invoke_authenticate_sync': gi.FunctionInfo(invoke_authenticate_sync), 'invoke_credentials_required': gi.FunctionInfo(invoke_credentials_required), 'invoke_credentials_required_finish': gi.FunctionInfo(invoke_credentials_required_finish), 'invoke_credentials_required_sync': gi.FunctionInfo(invoke_credentials_required_sync), 'lookup_password': gi.FunctionInfo(lookup_password), 'lookup_password_finish': gi.FunctionInfo(lookup_password_finish), 'lookup_password_sync': gi.FunctionInfo(lookup_password_sync), 'mail_signature_load': gi.FunctionInfo(mail_signature_load), 'mail_signature_load_finish': gi.FunctionInfo(mail_signature_load_finish), 'mail_signature_load_sync': gi.FunctionInfo(mail_signature_load_sync), 'mail_signature_replace': gi.FunctionInfo(mail_signature_replace), 'mail_signature_replace_finish': gi.FunctionInfo(mail_signature_replace_finish), 'mail_signature_replace_sync': gi.FunctionInfo(mail_signature_replace_sync), 'mail_signature_symlink': gi.FunctionInfo(mail_signature_symlink), 'mail_signature_symlink_finish': gi.FunctionInfo(mail_signature_symlink_finish), 'mail_signature_symlink_sync': gi.FunctionInfo(mail_signature_symlink_sync), 'proxy_lookup': gi.FunctionInfo(proxy_lookup), 'proxy_lookup_finish': gi.FunctionInfo(proxy_lookup_finish), 'proxy_lookup_sync': gi.FunctionInfo(proxy_lookup_sync), 'ref_dbus_object': gi.FunctionInfo(ref_dbus_object), 'ref_main_context': gi.FunctionInfo(ref_main_context), 'refresh_add_timeout': gi.FunctionInfo(refresh_add_timeout), 'refresh_force_timeout': gi.FunctionInfo(refresh_force_timeout), 'refresh_remove_timeout': gi.FunctionInfo(refresh_remove_timeout), 'refresh_remove_timeouts_by_data': gi.FunctionInfo(refresh_remove_timeouts_by_data), 'remote_create': gi.FunctionInfo(remote_create), 'remote_create_finish': gi.FunctionInfo(remote_create_finish), 'remote_create_sync': gi.FunctionInfo(remote_create_sync), 'remote_delete': gi.FunctionInfo(remote_delete), 'remote_delete_finish': gi.FunctionInfo(remote_delete_finish), 'remote_delete_sync': gi.FunctionInfo(remote_delete_sync), 'remove': gi.FunctionInfo(remove), 'remove_finish': gi.FunctionInfo(remove_finish), 'remove_sync': gi.FunctionInfo(remove_sync), 'set_connection_status': gi.FunctionInfo(set_connection_status), 'set_display_name': gi.FunctionInfo(set_display_name), 'set_enabled': gi.FunctionInfo(set_enabled), 'set_parent': gi.FunctionInfo(set_parent), 'store_password': gi.FunctionInfo(store_password), 'store_password_finish': gi.FunctionInfo(store_password_finish), 'store_password_sync': gi.FunctionInfo(store_password_sync), 'to_string': gi.FunctionInfo(to_string), 'unset_last_credentials_required_arguments': gi.FunctionInfo(unset_last_credentials_required_arguments), 'unset_last_credentials_required_arguments_finish': gi.FunctionInfo(unset_last_credentials_required_arguments_finish), 'unset_last_credentials_required_arguments_sync': gi.FunctionInfo(unset_last_credentials_required_arguments_sync), 'write': gi.FunctionInfo(write), 'write_finish': gi.FunctionInfo(write_finish), 'write_sync': gi.FunctionInfo(write_sync), 'do_authenticate': gi.VFuncInfo(authenticate), 'do_changed': gi.VFuncInfo(changed), 'do_credentials_required': gi.VFuncInfo(credentials_required), 'do_get_oauth2_access_token': gi.VFuncInfo(get_oauth2_access_token), 'do_get_oauth2_access_token_finish': gi.VFuncInfo(get_oauth2_access_token_finish), 'do_get_oauth2_access_token_sync': gi.VFuncInfo(get_oauth2_access_token_sync), 'do_invoke_authenticate_impl': gi.VFuncInfo(invoke_authenticate_impl), 'do_invoke_credentials_required_impl': gi.VFuncInfo(invoke_credentials_required_impl), 'do_remote_create': gi.VFuncInfo(remote_create), 'do_remote_create_finish': gi.VFuncInfo(remote_create_finish), 'do_remote_create_sync': gi.VFuncInfo(remote_create_sync), 'do_remote_delete': gi.VFuncInfo(remote_delete), 'do_remote_delete_finish': gi.VFuncInfo(remote_delete_finish), 'do_remote_delete_sync': gi.VFuncInfo(remote_delete_sync), 'do_remove': gi.VFuncInfo(remove), 'do_remove_finish': gi.VFuncInfo(remove_finish), 'do_remove_sync': gi.VFuncInfo(remove_sync), 'do_unset_last_credentials_required_arguments_impl': gi.VFuncInfo(unset_last_credentials_required_arguments_impl), 'do_write': gi.VFuncInfo(write), 'do_write_finish': gi.VFuncInfo(write_finish), 'do_write_sync': gi.VFuncInfo(write_sync), 'parent': <property object at 0x7f6271ca8630>, 'priv': <property object at 0x7f626e916360>})"
    __gdoc__ = 'Object ESource\n\nSignals from ESource:\n  authenticate (ENamedParameters)\n  changed ()\n  credentials-required (ESourceCredentialsReason, gchararray, GTlsCertificateFlags, GError)\n\nProperties from ESource:\n  dbus-object -> EDBusObject: D-Bus Object\n    The D-Bus object for the data source\n  display-name -> gchararray: Display Name\n    The human-readable name of the data source\n  enabled -> gboolean: Enabled\n    Whether the data source is enabled\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  parent -> gchararray: Parent\n    The unique identity of the parent data source\n  remote-creatable -> gboolean: Remote Creatable\n    Whether the data source can create remote resources\n  remote-deletable -> gboolean: Remote Deletable\n    Whether the data source can delete remote resources\n  removable -> gboolean: Removable\n    Whether the data source is removable\n  uid -> gchararray: UID\n    The unique identity of the data source\n  writable -> gboolean: Writable\n    Whether the data source is writable\n  connection-status -> ESourceConnectionStatus: Connection Status\n    Connection status of the source\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ESource (94877537038912)>'
    __info__ = ObjectInfo(Source)


