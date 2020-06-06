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


from .SoupSession import SoupSession

class WebDAVSession(SoupSession):
    """
    :Constructors:
    
    ::
    
        WebDAVSession(**properties)
        new(source:EDataServer.Source) -> EDataServer.WebDAVSession
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def acl_sync(self, uri=None, xml, cancellable=None): # real signature unknown; restored from __doc__
        """ acl_sync(self, uri:str=None, xml:EDataServer.XmlDocument, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def add_feature(self, feature): # real signature unknown; restored from __doc__
        """ add_feature(self, feature:Soup.SessionFeature) """
        pass

    def add_feature_by_type(self, feature_type): # real signature unknown; restored from __doc__
        """ add_feature_by_type(self, feature_type:GType) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cancel_message(self, msg, status_code): # real signature unknown; restored from __doc__
        """ cancel_message(self, msg:Soup.Message, status_code:int) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_result(self, request, read_bytes=None, bytes_length): # real signature unknown; restored from __doc__
        """ check_result(self, request:Soup.RequestHTTP, read_bytes=None, bytes_length:int) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_async(self, uri, cancellable=None, progress_callback=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect_async(self, uri:Soup.URI, cancellable:Gio.Cancellable=None, progress_callback:Soup.SessionConnectProgressCallback=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def connect_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_finish(self, result:Gio.AsyncResult) -> Gio.IOStream """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def copy_sync(self, source_uri, destination_uri, depth, can_overwrite, cancellable=None): # real signature unknown; restored from __doc__
        """ copy_sync(self, source_uri:str, destination_uri:str, depth:str, can_overwrite:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_sync(self, uri, depth=None, etag=None, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_sync(self, uri:str, depth:str=None, etag:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authenticate(self, *args, **kwargs): # real signature unknown
        """ authenticate(self, msg:Soup.Message, auth:Soup.Auth, retrying:bool) """
        pass

    def do_auth_required(self, *args, **kwargs): # real signature unknown
        """ auth_required(self, msg:Soup.Message, auth:Soup.Auth, retrying:bool) """
        pass

    def do_cancel_message(self, *args, **kwargs): # real signature unknown
        """ cancel_message(self, msg:Soup.Message, status_code:int) """
        pass

    def do_flush_queue(self, *args, **kwargs): # real signature unknown
        """ flush_queue(self) """
        pass

    def do_kick(self, *args, **kwargs): # real signature unknown
        """ kick(self) """
        pass

    def do_queue_message(self, *args, **kwargs): # real signature unknown
        """ queue_message(self, msg:Soup.Message, callback:Soup.SessionCallback=None, user_data=None) """
        pass

    def do_request_started(self, *args, **kwargs): # real signature unknown
        """ request_started(self, msg:Soup.Message, socket:Soup.Socket) """
        pass

    def do_requeue_message(self, *args, **kwargs): # real signature unknown
        """ requeue_message(self, msg:Soup.Message) """
        pass

    def do_send_message(self, *args, **kwargs): # real signature unknown
        """ send_message(self, msg:Soup.Message) -> int """
        pass

    def dup_credentials(self): # real signature unknown; restored from __doc__
        """ dup_credentials(self) -> EDataServer.NamedParameters or None """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_full_uri(self, request_uri=None, href): # real signature unknown; restored from __doc__
        """ ensure_full_uri(self, request_uri:Soup.URI=None, href:str) -> str """
        return ""

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

    def getctag_sync(self, uri=None, cancellable=None): # real signature unknown; restored from __doc__
        """ getctag_sync(self, uri:str=None, cancellable:Gio.Cancellable=None) -> bool, out_ctag:str """
        return False

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_acl_restrictions_sync(self, uri=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_acl_restrictions_sync(self, uri:str=None, cancellable:Gio.Cancellable=None) -> bool, out_restrictions:int, out_principal_kind:EDataServer.WebDAVACEPrincipalKind, out_principal_hrefs:list """
        return False

    def get_acl_sync(self, uri=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_acl_sync(self, uri:str=None, cancellable:Gio.Cancellable=None) -> bool, out_entries:list """
        return False

    def get_async_context(self): # real signature unknown; restored from __doc__
        """ get_async_context(self) -> GLib.MainContext or None """
        pass

    def get_authentication_requires_credentials(self): # real signature unknown; restored from __doc__
        """ get_authentication_requires_credentials(self) -> bool """
        return False

    def get_current_user_privilege_set_sync(self, uri=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_current_user_privilege_set_sync(self, uri:str=None, cancellable:Gio.Cancellable=None) -> bool, out_privileges:list """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_data_sync(self, uri, cancellable=None): # real signature unknown; restored from __doc__
        """ get_data_sync(self, uri:str, cancellable:Gio.Cancellable=None) -> bool, out_href:str, out_etag:str, out_bytes:str, out_length:int """
        return False

    def get_feature(self, feature_type): # real signature unknown; restored from __doc__
        """ get_feature(self, feature_type:GType) -> Soup.SessionFeature or None """
        pass

    def get_features(self, feature_type): # real signature unknown; restored from __doc__
        """ get_features(self, feature_type:GType) -> list """
        return []

    def get_feature_for_message(self, feature_type, msg): # real signature unknown; restored from __doc__
        """ get_feature_for_message(self, feature_type:GType, msg:Soup.Message) -> Soup.SessionFeature or None """
        pass

    def get_last_dav_error_code(self): # real signature unknown; restored from __doc__
        """ get_last_dav_error_code(self) -> str """
        return ""

    def get_last_dav_error_is_permission(self): # real signature unknown; restored from __doc__
        """ get_last_dav_error_is_permission(self) -> bool """
        return False

    def get_log_level(self): # real signature unknown; restored from __doc__
        """ get_log_level(self) -> Soup.LoggerLogLevel """
        pass

    def get_principal_collection_set_sync(self, uri=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_principal_collection_set_sync(self, uri:str=None, cancellable:Gio.Cancellable=None) -> bool, out_principal_hrefs:list """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_ssl_error_details(self): # real signature unknown; restored from __doc__
        """ get_ssl_error_details(self) -> bool, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags """
        return False

    def get_supported_privilege_set_sync(self, uri=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_supported_privilege_set_sync(self, uri:str=None, cancellable:Gio.Cancellable=None) -> bool, out_privileges:GLib.Node """
        return False

    def get_sync(self, uri, cancellable=None): # real signature unknown; restored from __doc__
        """ get_sync(self, uri:str, cancellable:Gio.Cancellable=None) -> bool, out_href:str, out_etag:str, out_stream:Gio.OutputStream """
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

    def has_feature(self, feature_type): # real signature unknown; restored from __doc__
        """ has_feature(self, feature_type:GType) -> bool """
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

    def list_sync(self, uri=None, depth, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ list_sync(self, uri:str=None, depth:str, flags:int, cancellable:Gio.Cancellable=None) -> bool, out_resources:list """
        return False

    def lock_resource_sync(self, uri=None, lock_scope, lock_timeout, owner=None, cancellable=None): # real signature unknown; restored from __doc__
        """ lock_resource_sync(self, uri:str=None, lock_scope:EDataServer.WebDAVLockScope, lock_timeout:int, owner:str=None, cancellable:Gio.Cancellable=None) -> bool, out_lock_token:str """
        return False

    def lock_sync(self, uri=None, depth, lock_timeout, xml, cancellable=None): # real signature unknown; restored from __doc__
        """ lock_sync(self, uri:str=None, depth:str, lock_timeout:int, xml:EDataServer.XmlDocument, cancellable:Gio.Cancellable=None) -> bool, out_lock_token:str, out_xml_response:libxml2.Doc """
        return False

    def mkcalendar_sync(self, uri, display_name=None, description=None, color=None, supports, cancellable=None): # real signature unknown; restored from __doc__
        """ mkcalendar_sync(self, uri:str, display_name:str=None, description:str=None, color:str=None, supports:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def mkcol_addressbook_sync(self, uri, display_name=None, description=None, cancellable=None): # real signature unknown; restored from __doc__
        """ mkcol_addressbook_sync(self, uri:str, display_name:str=None, description:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def mkcol_sync(self, uri, cancellable=None): # real signature unknown; restored from __doc__
        """ mkcol_sync(self, uri:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def move_sync(self, source_uri, destination_uri, can_overwrite, cancellable=None): # real signature unknown; restored from __doc__
        """ move_sync(self, source_uri:str, destination_uri:str, can_overwrite:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def new(self, source): # real signature unknown; restored from __doc__
        """ new(source:EDataServer.Source) -> EDataServer.WebDAVSession """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_request(self, method, uri=None): # real signature unknown; restored from __doc__
        """ new_request(self, method:str, uri:str=None) -> Soup.RequestHTTP """
        pass

    def new_request_uri(self, method, uri): # real signature unknown; restored from __doc__
        """ new_request_uri(self, method:str, uri:Soup.URI) -> Soup.RequestHTTP """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def options_sync(self, uri=None, cancellable=None): # real signature unknown; restored from __doc__
        """ options_sync(self, uri:str=None, cancellable:Gio.Cancellable=None) -> bool, out_capabilities:dict, out_allows:dict """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def pause_message(self, msg): # real signature unknown; restored from __doc__
        """ pause_message(self, msg:Soup.Message) """
        pass

    def post_sync(self, uri=None, data, data_length, out_content_type=None, out_content=None, cancellable=None): # real signature unknown; restored from __doc__
        """ post_sync(self, uri:str=None, data:str, data_length:int, out_content_type:str=None, out_content:list=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def post_with_content_type_sync(self, uri=None, data, data_length, in_content_type=None, out_content_type=None, out_content=None, cancellable=None): # real signature unknown; restored from __doc__
        """ post_with_content_type_sync(self, uri:str=None, data:str, data_length:int, in_content_type:str=None, out_content_type:str=None, out_content:list=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def prefetch_dns(self, hostname, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ prefetch_dns(self, hostname:str, cancellable:Gio.Cancellable=None, callback:Soup.AddressCallback=None, user_data=None) """
        pass

    def prepare_for_uri(self, uri): # real signature unknown; restored from __doc__
        """ prepare_for_uri(self, uri:Soup.URI) """
        pass

    def principal_property_search_sync(self, uri=None, apply_to_principal_collection_set, match_ns_uri=None, match_property, match_value, cancellable=None): # real signature unknown; restored from __doc__
        """ principal_property_search_sync(self, uri:str=None, apply_to_principal_collection_set:bool, match_ns_uri:str=None, match_property:str, match_value:str, cancellable:Gio.Cancellable=None) -> bool, out_principals:list """
        return False

    def proppatch_sync(self, uri=None, xml, cancellable=None): # real signature unknown; restored from __doc__
        """ proppatch_sync(self, uri:str=None, xml:EDataServer.XmlDocument, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_data_sync(self, uri, etag=None, content_type, bytes, length, cancellable=None): # real signature unknown; restored from __doc__
        """ put_data_sync(self, uri:str, etag:str=None, content_type:str, bytes:str, length:int, cancellable:Gio.Cancellable=None) -> bool, out_href:str, out_etag:str """
        return False

    def put_sync(self, uri, etag=None, content_type, stream, cancellable=None): # real signature unknown; restored from __doc__
        """ put_sync(self, uri:str, etag:str=None, content_type:str, stream:Gio.InputStream, cancellable:Gio.Cancellable=None) -> bool, out_href:str, out_etag:str """
        return False

    def queue_message(self, msg, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ queue_message(self, msg:Soup.Message, callback:Soup.SessionCallback=None, user_data=None) """
        pass

    def redirect_message(self, msg): # real signature unknown; restored from __doc__
        """ redirect_message(self, msg:Soup.Message) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh_lock_sync(self, uri=None, lock_token, lock_timeout, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_lock_sync(self, uri:str=None, lock_token:str, lock_timeout:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_feature(self, feature): # real signature unknown; restored from __doc__
        """ remove_feature(self, feature:Soup.SessionFeature) """
        pass

    def remove_feature_by_type(self, feature_type): # real signature unknown; restored from __doc__
        """ remove_feature_by_type(self, feature_type:GType) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_with_detailed_error(self, request, response_data=None, ignore_multistatus, prefix=None): # real signature unknown; restored from __doc__
        """ replace_with_detailed_error(self, request:Soup.RequestHTTP, response_data:list=None, ignore_multistatus:bool, prefix:str=None) -> bool """
        return False

    def request(self, uri_string): # real signature unknown; restored from __doc__
        """ request(self, uri_string:str) -> Soup.Request """
        pass

    def request_http(self, method, uri_string): # real signature unknown; restored from __doc__
        """ request_http(self, method:str, uri_string:str) -> Soup.RequestHTTP """
        pass

    def request_http_uri(self, method, uri): # real signature unknown; restored from __doc__
        """ request_http_uri(self, method:str, uri:Soup.URI) -> Soup.RequestHTTP """
        pass

    def request_uri(self, uri): # real signature unknown; restored from __doc__
        """ request_uri(self, uri:Soup.URI) -> Soup.Request """
        pass

    def requeue_message(self, msg): # real signature unknown; restored from __doc__
        """ requeue_message(self, msg:Soup.Message) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send(self, msg, cancellable=None): # real signature unknown; restored from __doc__
        """ send(self, msg:Soup.Message, cancellable:Gio.Cancellable=None) -> Gio.InputStream """
        pass

    def send_async(self, msg, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ send_async(self, msg:Soup.Message, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def send_finish(self, result): # real signature unknown; restored from __doc__
        """ send_finish(self, result:Gio.AsyncResult) -> Gio.InputStream """
        pass

    def send_message(self, msg): # real signature unknown; restored from __doc__
        """ send_message(self, msg:Soup.Message) -> int """
        return 0

    def send_request_simple_sync(self, request, cancellable=None): # real signature unknown; restored from __doc__
        """ send_request_simple_sync(self, request:Soup.RequestHTTP, cancellable:Gio.Cancellable=None) -> list """
        return []

    def send_request_sync(self, request, cancellable=None): # real signature unknown; restored from __doc__
        """ send_request_sync(self, request:Soup.RequestHTTP, cancellable:Gio.Cancellable=None) -> Gio.InputStream """
        pass

    def setup_logging(self, logging_level=None): # real signature unknown; restored from __doc__
        """ setup_logging(self, logging_level:str=None) """
        pass

    def set_acl_sync(self, uri=None, entries, cancellable=None): # real signature unknown; restored from __doc__
        """ set_acl_sync(self, uri:str=None, entries:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_credentials(self, credentials=None): # real signature unknown; restored from __doc__
        """ set_credentials(self, credentials:EDataServer.NamedParameters=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def steal_connection(self, msg): # real signature unknown; restored from __doc__
        """ steal_connection(self, msg:Soup.Message) -> Gio.IOStream """
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

    def unlock_sync(self, uri=None, lock_token, cancellable=None): # real signature unknown; restored from __doc__
        """ unlock_sync(self, uri:str=None, lock_token:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def unpause_message(self, msg): # real signature unknown; restored from __doc__
        """ unpause_message(self, msg:Soup.Message) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update_properties_sync(self, uri=None, changes, cancellable=None): # real signature unknown; restored from __doc__
        """ update_properties_sync(self, uri:str=None, changes:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def util_free_privileges(self, privileges=None): # real signature unknown; restored from __doc__
        """ util_free_privileges(privileges:GLib.Node=None) """
        pass

    def util_maybe_dequote(self, text=None): # real signature unknown; restored from __doc__
        """ util_maybe_dequote(text:str=None) -> str, text:str """
        return ""

    def util_status_to_string(self, status_code, reason_phrase=None): # real signature unknown; restored from __doc__
        """ util_status_to_string(status_code:int, reason_phrase:str=None) -> str """
        return ""

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def websocket_connect_async(self, msg, origin=None, protocols=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ websocket_connect_async(self, msg:Soup.Message, origin:str=None, protocols:list=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def websocket_connect_finish(self, result): # real signature unknown; restored from __doc__
        """ websocket_connect_finish(self, result:Gio.AsyncResult) -> Soup.WebsocketConnection """
        pass

    def would_redirect(self, msg): # real signature unknown; restored from __doc__
        """ would_redirect(self, msg:Soup.Message) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f626e50b1c0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(WebDAVSession), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType EWebDAVSession (94877537406832)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'util_free_privileges': gi.FunctionInfo(util_free_privileges), 'util_maybe_dequote': gi.FunctionInfo(util_maybe_dequote), 'acl_sync': gi.FunctionInfo(acl_sync), 'copy_sync': gi.FunctionInfo(copy_sync), 'delete_sync': gi.FunctionInfo(delete_sync), 'ensure_full_uri': gi.FunctionInfo(ensure_full_uri), 'get_acl_restrictions_sync': gi.FunctionInfo(get_acl_restrictions_sync), 'get_acl_sync': gi.FunctionInfo(get_acl_sync), 'get_current_user_privilege_set_sync': gi.FunctionInfo(get_current_user_privilege_set_sync), 'get_data_sync': gi.FunctionInfo(get_data_sync), 'get_last_dav_error_code': gi.FunctionInfo(get_last_dav_error_code), 'get_last_dav_error_is_permission': gi.FunctionInfo(get_last_dav_error_is_permission), 'get_principal_collection_set_sync': gi.FunctionInfo(get_principal_collection_set_sync), 'get_supported_privilege_set_sync': gi.FunctionInfo(get_supported_privilege_set_sync), 'get_sync': gi.FunctionInfo(get_sync), 'getctag_sync': gi.FunctionInfo(getctag_sync), 'list_sync': gi.FunctionInfo(list_sync), 'lock_resource_sync': gi.FunctionInfo(lock_resource_sync), 'lock_sync': gi.FunctionInfo(lock_sync), 'mkcalendar_sync': gi.FunctionInfo(mkcalendar_sync), 'mkcol_addressbook_sync': gi.FunctionInfo(mkcol_addressbook_sync), 'mkcol_sync': gi.FunctionInfo(mkcol_sync), 'move_sync': gi.FunctionInfo(move_sync), 'new_request': gi.FunctionInfo(new_request), 'options_sync': gi.FunctionInfo(options_sync), 'post_sync': gi.FunctionInfo(post_sync), 'post_with_content_type_sync': gi.FunctionInfo(post_with_content_type_sync), 'principal_property_search_sync': gi.FunctionInfo(principal_property_search_sync), 'proppatch_sync': gi.FunctionInfo(proppatch_sync), 'put_data_sync': gi.FunctionInfo(put_data_sync), 'put_sync': gi.FunctionInfo(put_sync), 'refresh_lock_sync': gi.FunctionInfo(refresh_lock_sync), 'replace_with_detailed_error': gi.FunctionInfo(replace_with_detailed_error), 'set_acl_sync': gi.FunctionInfo(set_acl_sync), 'unlock_sync': gi.FunctionInfo(unlock_sync), 'update_properties_sync': gi.FunctionInfo(update_properties_sync), 'parent': <property object at 0x7f626e8dd6d0>, 'priv': <property object at 0x7f626e8dd7c0>})"
    __gdoc__ = "Object EWebDAVSession\n\nProperties from ESoupSession:\n  source -> ESource: Source\n  credentials -> ENamedParameters: Credentials\n\nSignals from SoupSession:\n  request-queued (SoupMessage)\n  request-started (SoupMessage, SoupSocket)\n  request-unqueued (SoupMessage)\n  authenticate (SoupMessage, SoupAuth, gboolean)\n  connection-created (GObject)\n  tunneling (GObject)\n\nProperties from SoupSession:\n  proxy-uri -> SoupURI: Proxy URI\n    The HTTP Proxy to use for this session\n  proxy-resolver -> GProxyResolver: Proxy Resolver\n    The GProxyResolver to use for this session\n  max-conns -> gint: Max Connection Count\n    The maximum number of connections that the session can open at once\n  max-conns-per-host -> gint: Max Per-Host Connection Count\n    The maximum number of connections that the session can open at once to a given host\n  use-ntlm -> gboolean: Use NTLM\n    Whether or not to use NTLM authentication\n  ssl-ca-file -> gchararray: SSL CA file\n    File containing SSL CA certificates\n  ssl-use-system-ca-file -> gboolean: Use system CA file\n    Use the system certificate database\n  tls-database -> GTlsDatabase: TLS Database\n    TLS database to use\n  ssl-strict -> gboolean: Strictly validate SSL certificates\n    Whether certificate errors should be considered a connection error\n  async-context -> gpointer: Async GMainContext\n    The GMainContext to dispatch async I/O in\n  use-thread-context -> gboolean: Use thread-default GMainContext\n    Whether to use thread-default main contexts\n  timeout -> guint: Timeout value\n    Value in seconds to timeout a blocking I/O\n  user-agent -> gchararray: User-Agent string\n    User-Agent string\n  accept-language -> gchararray: Accept-Language string\n    Accept-Language string\n  accept-language-auto -> gboolean: Accept-Language automatic mode\n    Accept-Language automatic mode\n  idle-timeout -> guint: Idle Timeout\n    Connection lifetime when idle\n  add-feature -> SoupSessionFeature: Add Feature\n    Add a feature object to the session\n  add-feature-by-type -> GType: Add Feature By Type\n    Add a feature object of the given type to the session\n  remove-feature-by-type -> GType: Remove Feature By Type\n    Remove features of the given type from the session\n  http-aliases -> GStrv: http aliases\n    URI schemes that are considered aliases for 'http'\n  https-aliases -> GStrv: https aliases\n    URI schemes that are considered aliases for 'https'\n  local-address -> SoupAddress: Local address\n    Address of local end of socket\n  tls-interaction -> GTlsInteraction: TLS Interaction\n    TLS interaction to use\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EWebDAVSession (94877537406832)>'
    __info__ = ObjectInfo(WebDAVSession)


