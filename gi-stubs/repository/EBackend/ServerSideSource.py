# encoding: utf-8
# module gi.repository.EBackend
# from /usr/lib64/girepository-1.0/EBackend-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ServerSideSource(__gi_repository_EDataServer.Source):
    """
    :Constructors:
    
    ::
    
        ServerSideSource(**properties)
        new(server:EBackend.SourceRegistryServer, file:Gio.File) -> EDataServer.Source
        new_memory_only(server:EBackend.SourceRegistryServer, uid:str) -> EDataServer.Source
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

    def get_exported(self): # real signature unknown; restored from __doc__
        """ get_exported(self) -> bool """
        return False

    def get_extension(self, extension_name): # real signature unknown; restored from __doc__
        """ get_extension(self, extension_name:str) -> EDataServer.SourceExtension """
        pass

    def get_file(self): # real signature unknown; restored from __doc__
        """ get_file(self) -> Gio.File or None """
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

    def get_node(self): # real signature unknown; restored from __doc__
        """ get_node(self) -> GLib.Node or None """
        pass

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

    def get_server(self): # real signature unknown; restored from __doc__
        """ get_server(self) -> EBackend.SourceRegistryServer """
        pass

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def get_user_dir(self): # real signature unknown; restored from __doc__
        """ get_user_dir() -> str """
        return ""

    def get_writable(self): # real signature unknown; restored from __doc__
        """ get_writable(self) -> bool """
        return False

    def get_write_directory(self): # real signature unknown; restored from __doc__
        """ get_write_directory(self) -> str """
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

    def load(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def new(self, server, file): # real signature unknown; restored from __doc__
        """ new(server:EBackend.SourceRegistryServer, file:Gio.File) -> EDataServer.Source """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_memory_only(self, server, uid): # real signature unknown; restored from __doc__
        """ new_memory_only(server:EBackend.SourceRegistryServer, uid:str) -> EDataServer.Source """
        pass

    def new_user_file(self, uid): # real signature unknown; restored from __doc__
        """ new_user_file(uid:str) -> Gio.File """
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

    def ref_oauth2_support(self): # real signature unknown; restored from __doc__
        """ ref_oauth2_support(self) -> EBackend.OAuth2Support or None """
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

    def set_oauth2_support(self, oauth2_support): # real signature unknown; restored from __doc__
        """ set_oauth2_support(self, oauth2_support:EBackend.OAuth2Support) """
        pass

    def set_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_remote_creatable(self, remote_creatable): # real signature unknown; restored from __doc__
        """ set_remote_creatable(self, remote_creatable:bool) """
        pass

    def set_remote_deletable(self, remote_deletable): # real signature unknown; restored from __doc__
        """ set_remote_deletable(self, remote_deletable:bool) """
        pass

    def set_removable(self, removable): # real signature unknown; restored from __doc__
        """ set_removable(self, removable:bool) """
        pass

    def set_writable(self, writable): # real signature unknown; restored from __doc__
        """ set_writable(self, writable:bool) """
        pass

    def set_write_directory(self, write_directory): # real signature unknown; restored from __doc__
        """ set_write_directory(self, write_directory:str) """
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

    def uid_from_file(self, file): # real signature unknown; restored from __doc__
        """ uid_from_file(file:Gio.File) -> str """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9dc2d8d430>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ServerSideSource), '__module__': 'gi.repository.EBackend', '__gtype__': <GType EServerSideSource (94170535288352)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_memory_only': gi.FunctionInfo(new_memory_only), 'get_user_dir': gi.FunctionInfo(get_user_dir), 'new_user_file': gi.FunctionInfo(new_user_file), 'uid_from_file': gi.FunctionInfo(uid_from_file), 'get_exported': gi.FunctionInfo(get_exported), 'get_file': gi.FunctionInfo(get_file), 'get_node': gi.FunctionInfo(get_node), 'get_server': gi.FunctionInfo(get_server), 'get_write_directory': gi.FunctionInfo(get_write_directory), 'load': gi.FunctionInfo(load), 'ref_oauth2_support': gi.FunctionInfo(ref_oauth2_support), 'set_oauth2_support': gi.FunctionInfo(set_oauth2_support), 'set_remote_creatable': gi.FunctionInfo(set_remote_creatable), 'set_remote_deletable': gi.FunctionInfo(set_remote_deletable), 'set_removable': gi.FunctionInfo(set_removable), 'set_writable': gi.FunctionInfo(set_writable), 'set_write_directory': gi.FunctionInfo(set_write_directory), 'parent': <property object at 0x7f9dbf894400>, 'priv': <property object at 0x7f9dbf8944f0>})"
    __gdoc__ = 'Object EServerSideSource\n\nProperties from EServerSideSource:\n  exported -> gboolean: Exported\n    Whether the source has been exported over D-Bus\n  file -> GFile: File\n    The key file for the data source\n  oauth2-support -> EOAuth2Support: OAuth2 Support\n    The object providing OAuth 2.0 support\n  remote-creatable -> gboolean: Remote Creatable\n    Whether the data source can create remote resources\n  remote-deletable -> gboolean: Remote Deletable\n    Whether the data source can delete remote resources\n  removable -> gboolean: Removable\n    Whether the data source is removable\n  server -> ESourceRegistryServer: Server\n    The server to which the data source belongs\n  writable -> gboolean: Writable\n    Whether the data source is writable\n  write-directory -> gchararray: Write Directory\n    Directory in which to write changes to disk\n\nSignals from ESource:\n  changed ()\n  credentials-required (ESourceCredentialsReason, gchararray, GTlsCertificateFlags, GError)\n  authenticate (ENamedParameters)\n\nProperties from ESource:\n  dbus-object -> EDBusObject: D-Bus Object\n    The D-Bus object for the data source\n  display-name -> gchararray: Display Name\n    The human-readable name of the data source\n  enabled -> gboolean: Enabled\n    Whether the data source is enabled\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  parent -> gchararray: Parent\n    The unique identity of the parent data source\n  remote-creatable -> gboolean: Remote Creatable\n    Whether the data source can create remote resources\n  remote-deletable -> gboolean: Remote Deletable\n    Whether the data source can delete remote resources\n  removable -> gboolean: Removable\n    Whether the data source is removable\n  uid -> gchararray: UID\n    The unique identity of the data source\n  writable -> gboolean: Writable\n    Whether the data source is writable\n  connection-status -> ESourceConnectionStatus: Connection Status\n    Connection status of the source\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EServerSideSource (94170535288352)>'
    __info__ = ObjectInfo(ServerSideSource)


