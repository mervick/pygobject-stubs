# encoding: utf-8
# module gi.repository.EDataBook
# from /usr/lib64/girepository-1.0/EDataBook-1.2.typelib
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
import gi.repository.EBackend as __gi_repository_EBackend
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class BookBackend(__gi_repository_EBackend.Backend):
    """
    :Constructors:
    
    ::
    
        BookBackend(**properties)
    """
    def add_view(self, view): # real signature unknown; restored from __doc__
        """ add_view(self, view:EDataBook.DataBookView) """
        pass

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

    def configure_direct(self, config): # real signature unknown; restored from __doc__
        """ configure_direct(self, config:str) """
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

    def create_contacts(self, vcards, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_contacts(self, vcards:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_contacts_finish(self, result, out_contacts): # real signature unknown; restored from __doc__
        """ create_contacts_finish(self, result:Gio.AsyncResult, out_contacts:GLib.Queue) -> bool """
        return False

    def create_contacts_sync(self, vcards, opflags, out_contacts, cancellable=None): # real signature unknown; restored from __doc__
        """ create_contacts_sync(self, vcards:str, opflags:int, out_contacts:GLib.Queue, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def create_cursor(self, sort_fields, sort_types, n_fields): # real signature unknown; restored from __doc__
        """ create_cursor(self, sort_fields:EBookContacts.ContactField, sort_types:EBookContacts.BookCursorSortType, n_fields:int) -> EDataBook.DataBookCursor """
        pass

    def credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def credentials_required_finish(self, result): # real signature unknown; restored from __doc__
        """ credentials_required_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def credentials_required_sync(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None): # real signature unknown; restored from __doc__
        """ credentials_required_sync(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_cursor(self, cursor): # real signature unknown; restored from __doc__
        """ delete_cursor(self, cursor:EDataBook.DataBookCursor) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authenticate_sync(self, *args, **kwargs): # real signature unknown
        """ authenticate_sync(self, credentials:EDataServer.NamedParameters, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, cancellable:Gio.Cancellable=None) -> EDataServer.SourceAuthenticationResult """
        pass

    def do_closed(self, *args, **kwargs): # real signature unknown
        """ closed(self, sender:str) """
        pass

    def do_get_destination_address(self, *args, **kwargs): # real signature unknown
        """ get_destination_address(self) -> bool, host:str, port:int """
        pass

    def do_impl_configure_direct(self, *args, **kwargs): # real signature unknown
        """ impl_configure_direct(self, config:str) """
        pass

    def do_impl_create_contacts(self, *args, **kwargs): # real signature unknown
        """ impl_create_contacts(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None, vcards:str, opflags:int) """
        pass

    def do_impl_delete_cursor(self, *args, **kwargs): # real signature unknown
        """ impl_delete_cursor(self, cursor:EDataBook.DataBookCursor) -> bool """
        pass

    def do_impl_dup_locale(self, *args, **kwargs): # real signature unknown
        """ impl_dup_locale(self) -> str """
        pass

    def do_impl_get_backend_property(self, *args, **kwargs): # real signature unknown
        """ impl_get_backend_property(self, prop_name:str) -> str """
        pass

    def do_impl_get_contact(self, *args, **kwargs): # real signature unknown
        """ impl_get_contact(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None, id:str) """
        pass

    def do_impl_get_contact_list(self, *args, **kwargs): # real signature unknown
        """ impl_get_contact_list(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None, query:str) """
        pass

    def do_impl_get_contact_list_uids(self, *args, **kwargs): # real signature unknown
        """ impl_get_contact_list_uids(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None, query:str) """
        pass

    def do_impl_modify_contacts(self, *args, **kwargs): # real signature unknown
        """ impl_modify_contacts(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None, vcards:str, opflags:int) """
        pass

    def do_impl_notify_update(self, *args, **kwargs): # real signature unknown
        """ impl_notify_update(self, contact:EBookContacts.Contact) """
        pass

    def do_impl_open(self, *args, **kwargs): # real signature unknown
        """ impl_open(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None) """
        pass

    def do_impl_refresh(self, *args, **kwargs): # real signature unknown
        """ impl_refresh(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None) """
        pass

    def do_impl_remove_contacts(self, *args, **kwargs): # real signature unknown
        """ impl_remove_contacts(self, book:EDataBook.DataBook, opid:int, cancellable:Gio.Cancellable=None, uids:str, opflags:int) """
        pass

    def do_impl_set_locale(self, *args, **kwargs): # real signature unknown
        """ impl_set_locale(self, locale:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_impl_start_view(self, *args, **kwargs): # real signature unknown
        """ impl_start_view(self, view:EDataBook.DataBookView) """
        pass

    def do_impl_stop_view(self, *args, **kwargs): # real signature unknown
        """ impl_stop_view(self, view:EDataBook.DataBookView) """
        pass

    def do_prepare_shutdown(self, *args, **kwargs): # real signature unknown
        """ prepare_shutdown(self) """
        pass

    def do_shutdown(self, *args, **kwargs): # real signature unknown
        """ shutdown(self) """
        pass

    def dup_cache_dir(self): # real signature unknown; restored from __doc__
        """ dup_cache_dir(self) -> str """
        return ""

    def dup_locale(self): # real signature unknown; restored from __doc__
        """ dup_locale(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_online_state_updated(self, cancellable=None): # real signature unknown; restored from __doc__
        """ ensure_online_state_updated(self, cancellable:Gio.Cancellable=None) """
        pass

    def ensure_source_status_connected(self): # real signature unknown; restored from __doc__
        """ ensure_source_status_connected(self) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach_view(self, func=None, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_view(self, func:EDataBook.BookBackendForeachViewFunc=None, user_data=None) -> bool """
        return False

    def foreach_view_notify_progress(self, only_completed_views, percent, message=None): # real signature unknown; restored from __doc__
        """ foreach_view_notify_progress(self, only_completed_views:bool, percent:int, message:str=None) """
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

    def get_backend_property(self, prop_name): # real signature unknown; restored from __doc__
        """ get_backend_property(self, prop_name:str) -> str """
        return ""

    def get_cache_dir(self): # real signature unknown; restored from __doc__
        """ get_cache_dir(self) -> str """
        return ""

    def get_contact(self, uid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_contact(self, uid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_contact_finish(self, result): # real signature unknown; restored from __doc__
        """ get_contact_finish(self, result:Gio.AsyncResult) -> EBookContacts.Contact """
        pass

    def get_contact_list(self, query, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_contact_list(self, query:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_contact_list_finish(self, result, out_contacts): # real signature unknown; restored from __doc__
        """ get_contact_list_finish(self, result:Gio.AsyncResult, out_contacts:GLib.Queue) -> bool """
        return False

    def get_contact_list_sync(self, query, out_contacts, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact_list_sync(self, query:str, out_contacts:GLib.Queue, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_contact_list_uids(self, query, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_contact_list_uids(self, query:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_contact_list_uids_finish(self, result, out_uids): # real signature unknown; restored from __doc__
        """ get_contact_list_uids_finish(self, result:Gio.AsyncResult, out_uids:GLib.Queue) -> bool """
        return False

    def get_contact_list_uids_sync(self, query, out_uids, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact_list_uids_sync(self, query:str, out_uids:GLib.Queue, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_contact_sync(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact_sync(self, uid:str, cancellable:Gio.Cancellable=None) -> EBookContacts.Contact """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_destination_address(self): # real signature unknown; restored from __doc__
        """ get_destination_address(self) -> bool, host:str, port:int """
        return False

    def get_direct_book(self): # real signature unknown; restored from __doc__
        """ get_direct_book(self) -> EDataBook.DataBookDirect or None """
        pass

    def get_online(self): # real signature unknown; restored from __doc__
        """ get_online(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_registry(self): # real signature unknown; restored from __doc__
        """ get_registry(self) -> EDataServer.SourceRegistry """
        pass

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_user_prompter(self): # real signature unknown; restored from __doc__
        """ get_user_prompter(self) """
        pass

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

    def is_destination_reachable(self, cancellable=None): # real signature unknown; restored from __doc__
        """ is_destination_reachable(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_opened(self): # real signature unknown; restored from __doc__
        """ is_opened(self) -> bool """
        return False

    def is_readonly(self): # real signature unknown; restored from __doc__
        """ is_readonly(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_views(self): # real signature unknown; restored from __doc__
        """ list_views(self) -> list """
        return []

    def modify_contacts(self, vcards, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ modify_contacts(self, vcards:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def modify_contacts_finish(self, result): # real signature unknown; restored from __doc__
        """ modify_contacts_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def modify_contacts_sync(self, vcards, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_contacts_sync(self, vcards:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_complete(self): # real signature unknown; restored from __doc__
        """ notify_complete(self) """
        pass

    def notify_error(self, message): # real signature unknown; restored from __doc__
        """ notify_error(self, message:str) """
        pass

    def notify_property_changed(self, prop_name, prop_value=None): # real signature unknown; restored from __doc__
        """ notify_property_changed(self, prop_name:str, prop_value:str=None) """
        pass

    def notify_remove(self, id): # real signature unknown; restored from __doc__
        """ notify_remove(self, id:str) """
        pass

    def notify_update(self, contact): # real signature unknown; restored from __doc__
        """ notify_update(self, contact:EBookContacts.Contact) """
        pass

    def open(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def open_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def prepare_for_completion(self, opid, result_queue): # real signature unknown; restored from __doc__
        """ prepare_for_completion(self, opid:int, result_queue:GLib.Queue) -> Gio.SimpleAsyncResult """
        pass

    def prepare_shutdown(self): # real signature unknown; restored from __doc__
        """ prepare_shutdown(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ refresh(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def refresh_finish(self, result): # real signature unknown; restored from __doc__
        """ refresh_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def refresh_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref_connectable(self): # real signature unknown; restored from __doc__
        """ ref_connectable(self) -> Gio.SocketConnectable or None """
        pass

    def ref_data_book(self): # real signature unknown; restored from __doc__
        """ ref_data_book(self) -> EDataBook.DataBook or None """
        pass

    def ref_main_context(self): # real signature unknown; restored from __doc__
        """ ref_main_context(self) -> GLib.MainContext """
        pass

    def ref_proxy_resolver(self): # real signature unknown; restored from __doc__
        """ ref_proxy_resolver(self) -> Gio.ProxyResolver or None """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_contacts(self, uids, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_contacts(self, uids:list, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_contacts_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_contacts_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_contacts_sync(self, uids, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contacts_sync(self, uids:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_view(self, view): # real signature unknown; restored from __doc__
        """ remove_view(self, view:EDataBook.DataBookView) """
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

    def schedule_authenticate(self, credentials=None): # real signature unknown; restored from __doc__
        """ schedule_authenticate(self, credentials:EDataServer.NamedParameters=None) """
        pass

    def schedule_credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, who_calls=None): # real signature unknown; restored from __doc__
        """ schedule_credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, who_calls:str=None) """
        pass

    def schedule_custom_operation(self, use_cancellable=None, func, user_data=None): # real signature unknown; restored from __doc__
        """ schedule_custom_operation(self, use_cancellable:Gio.Cancellable=None, func:EDataBook.BookBackendCustomOpFunc, user_data=None) """
        pass

    def set_cache_dir(self, cache_dir): # real signature unknown; restored from __doc__
        """ set_cache_dir(self, cache_dir:str) """
        pass

    def set_connectable(self, connectable): # real signature unknown; restored from __doc__
        """ set_connectable(self, connectable:Gio.SocketConnectable) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data_book(self, data_book): # real signature unknown; restored from __doc__
        """ set_data_book(self, data_book:EDataBook.DataBook) """
        pass

    def set_locale(self, locale, cancellable=None): # real signature unknown; restored from __doc__
        """ set_locale(self, locale:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_online(self, online): # real signature unknown; restored from __doc__
        """ set_online(self, online:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_writable(self, writable): # real signature unknown; restored from __doc__
        """ set_writable(self, writable:bool) """
        pass

    def start_view(self, view): # real signature unknown; restored from __doc__
        """ start_view(self, view:EDataBook.DataBookView) """
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

    def stop_view(self, view): # real signature unknown; restored from __doc__
        """ stop_view(self, view:EDataBook.DataBookView) """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def trust_prompt(self, parameters, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ trust_prompt(self, parameters:EDataServer.NamedParameters, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def trust_prompt_finish(self, result): # real signature unknown; restored from __doc__
        """ trust_prompt_finish(self, result:Gio.AsyncResult) -> EDataServer.TrustPromptResponse """
        pass

    def trust_prompt_sync(self, parameters, cancellable=None): # real signature unknown; restored from __doc__
        """ trust_prompt_sync(self, parameters:EDataServer.NamedParameters, cancellable:Gio.Cancellable=None) -> EDataServer.TrustPromptResponse """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f09d4187670>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BookBackend), '__module__': 'gi.repository.EDataBook', '__gtype__': <GType EBookBackend (94654337843088)>, '__doc__': None, '__gsignals__': {}, 'add_view': gi.FunctionInfo(add_view), 'configure_direct': gi.FunctionInfo(configure_direct), 'create_contacts': gi.FunctionInfo(create_contacts), 'create_contacts_finish': gi.FunctionInfo(create_contacts_finish), 'create_contacts_sync': gi.FunctionInfo(create_contacts_sync), 'create_cursor': gi.FunctionInfo(create_cursor), 'delete_cursor': gi.FunctionInfo(delete_cursor), 'dup_cache_dir': gi.FunctionInfo(dup_cache_dir), 'dup_locale': gi.FunctionInfo(dup_locale), 'foreach_view': gi.FunctionInfo(foreach_view), 'foreach_view_notify_progress': gi.FunctionInfo(foreach_view_notify_progress), 'get_backend_property': gi.FunctionInfo(get_backend_property), 'get_cache_dir': gi.FunctionInfo(get_cache_dir), 'get_contact': gi.FunctionInfo(get_contact), 'get_contact_finish': gi.FunctionInfo(get_contact_finish), 'get_contact_list': gi.FunctionInfo(get_contact_list), 'get_contact_list_finish': gi.FunctionInfo(get_contact_list_finish), 'get_contact_list_sync': gi.FunctionInfo(get_contact_list_sync), 'get_contact_list_uids': gi.FunctionInfo(get_contact_list_uids), 'get_contact_list_uids_finish': gi.FunctionInfo(get_contact_list_uids_finish), 'get_contact_list_uids_sync': gi.FunctionInfo(get_contact_list_uids_sync), 'get_contact_sync': gi.FunctionInfo(get_contact_sync), 'get_direct_book': gi.FunctionInfo(get_direct_book), 'get_registry': gi.FunctionInfo(get_registry), 'get_writable': gi.FunctionInfo(get_writable), 'is_opened': gi.FunctionInfo(is_opened), 'is_readonly': gi.FunctionInfo(is_readonly), 'list_views': gi.FunctionInfo(list_views), 'modify_contacts': gi.FunctionInfo(modify_contacts), 'modify_contacts_finish': gi.FunctionInfo(modify_contacts_finish), 'modify_contacts_sync': gi.FunctionInfo(modify_contacts_sync), 'notify_complete': gi.FunctionInfo(notify_complete), 'notify_error': gi.FunctionInfo(notify_error), 'notify_property_changed': gi.FunctionInfo(notify_property_changed), 'notify_remove': gi.FunctionInfo(notify_remove), 'notify_update': gi.FunctionInfo(notify_update), 'open': gi.FunctionInfo(open), 'open_finish': gi.FunctionInfo(open_finish), 'open_sync': gi.FunctionInfo(open_sync), 'prepare_for_completion': gi.FunctionInfo(prepare_for_completion), 'ref_data_book': gi.FunctionInfo(ref_data_book), 'ref_proxy_resolver': gi.FunctionInfo(ref_proxy_resolver), 'refresh': gi.FunctionInfo(refresh), 'refresh_finish': gi.FunctionInfo(refresh_finish), 'refresh_sync': gi.FunctionInfo(refresh_sync), 'remove_contacts': gi.FunctionInfo(remove_contacts), 'remove_contacts_finish': gi.FunctionInfo(remove_contacts_finish), 'remove_contacts_sync': gi.FunctionInfo(remove_contacts_sync), 'remove_view': gi.FunctionInfo(remove_view), 'schedule_custom_operation': gi.FunctionInfo(schedule_custom_operation), 'set_cache_dir': gi.FunctionInfo(set_cache_dir), 'set_data_book': gi.FunctionInfo(set_data_book), 'set_locale': gi.FunctionInfo(set_locale), 'set_writable': gi.FunctionInfo(set_writable), 'start_view': gi.FunctionInfo(start_view), 'stop_view': gi.FunctionInfo(stop_view), 'sync': gi.FunctionInfo(sync), 'do_closed': gi.VFuncInfo(closed), 'do_impl_configure_direct': gi.VFuncInfo(impl_configure_direct), 'do_impl_create_contacts': gi.VFuncInfo(impl_create_contacts), 'do_impl_delete_cursor': gi.VFuncInfo(impl_delete_cursor), 'do_impl_dup_locale': gi.VFuncInfo(impl_dup_locale), 'do_impl_get_backend_property': gi.VFuncInfo(impl_get_backend_property), 'do_impl_get_contact': gi.VFuncInfo(impl_get_contact), 'do_impl_get_contact_list': gi.VFuncInfo(impl_get_contact_list), 'do_impl_get_contact_list_uids': gi.VFuncInfo(impl_get_contact_list_uids), 'do_impl_modify_contacts': gi.VFuncInfo(impl_modify_contacts), 'do_impl_notify_update': gi.VFuncInfo(impl_notify_update), 'do_impl_open': gi.VFuncInfo(impl_open), 'do_impl_refresh': gi.VFuncInfo(impl_refresh), 'do_impl_remove_contacts': gi.VFuncInfo(impl_remove_contacts), 'do_impl_set_locale': gi.VFuncInfo(impl_set_locale), 'do_impl_start_view': gi.VFuncInfo(impl_start_view), 'do_impl_stop_view': gi.VFuncInfo(impl_stop_view), 'do_shutdown': gi.VFuncInfo(shutdown), 'parent': <property object at 0x7f09d41a7950>, 'priv': <property object at 0x7f09d41a79a0>})"
    __gdoc__ = "Object EBookBackend\n\nSignals from EBookBackend:\n  closed (gchararray)\n  shutdown ()\n\nProperties from EBookBackend:\n  cache-dir -> gchararray: Cache Dir\n    The backend's cache directory\n  proxy-resolver -> GProxyResolver: Proxy Resolver\n    The proxy resolver for this backend\n  registry -> ESourceRegistry: Registry\n    Data source registry\n  writable -> gboolean: Writable\n    Whether the backend will accept changes\n\nProperties from EBackend:\n  connectable -> GSocketConnectable: Connectable\n    Socket endpoint of a network service\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  online -> gboolean: Online\n    Whether the backend is online\n  source -> ESource: Source\n    The data source being acted upon\n  user-prompter -> EUserPrompter: User Prompter\n    User prompter instance\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EBookBackend (94654337843088)>'
    __info__ = ObjectInfo(BookBackend)


