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


from .BookBackendSync import BookBackendSync

class BookMetaBackend(BookBackendSync):
    """
    :Constructors:
    
    ::
    
        BookMetaBackend(**properties)
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

    def connect_sync(self, credentials=None, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(self, credentials:EDataServer.NamedParameters=None, cancellable:Gio.Cancellable=None) -> bool, out_auth_result:EDataServer.SourceAuthenticationResult, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags """
        return False

    def create_contacts(self, vcards, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ create_contacts(self, vcards:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_contacts:list """
        return False

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

    def disconnect_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ disconnect_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def do_authenticate_sync(self, *args, **kwargs): # real signature unknown
        """ authenticate_sync(self, credentials:EDataServer.NamedParameters, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, cancellable:Gio.Cancellable=None) -> EDataServer.SourceAuthenticationResult """
        pass

    def do_closed(self, *args, **kwargs): # real signature unknown
        """ closed(self, sender:str) """
        pass

    def do_connect_sync(self, *args, **kwargs): # real signature unknown
        """ connect_sync(self, credentials:EDataServer.NamedParameters=None, cancellable:Gio.Cancellable=None) -> bool, out_auth_result:EDataServer.SourceAuthenticationResult, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags """
        pass

    def do_disconnect_sync(self, *args, **kwargs): # real signature unknown
        """ disconnect_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_get_changes_sync(self, *args, **kwargs): # real signature unknown
        """ get_changes_sync(self, last_sync_tag:str=None, is_repeat:bool, cancellable:Gio.Cancellable=None) -> bool, out_new_sync_tag:str, out_repeat:bool, out_created_objects:list, out_modified_objects:list, out_removed_objects:list """
        pass

    def do_get_destination_address(self, *args, **kwargs): # real signature unknown
        """ get_destination_address(self) -> bool, host:str, port:int """
        pass

    def do_get_ssl_error_details(self, *args, **kwargs): # real signature unknown
        """ get_ssl_error_details(self) -> bool, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags """
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

    def do_list_existing_sync(self, *args, **kwargs): # real signature unknown
        """ list_existing_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_new_sync_tag:str, out_existing_objects:list """
        pass

    def do_load_contact_sync(self, *args, **kwargs): # real signature unknown
        """ load_contact_sync(self, uid:str, extra:str=None, cancellable:Gio.Cancellable=None) -> bool, out_contact:EBookContacts.Contact, out_extra:str """
        pass

    def do_open_sync(self, *args, **kwargs): # real signature unknown
        """ open_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_prepare_shutdown(self, *args, **kwargs): # real signature unknown
        """ prepare_shutdown(self) """
        pass

    def do_refresh_sync(self, *args, **kwargs): # real signature unknown
        """ refresh_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remove_contact_sync(self, *args, **kwargs): # real signature unknown
        """ remove_contact_sync(self, conflict_resolution:EDataServer.ConflictResolution, uid:str, extra:str=None, object:str=None, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_requires_reconnect(self, *args, **kwargs): # real signature unknown
        """ requires_reconnect(self) -> bool """
        pass

    def do_save_contact_sync(self, *args, **kwargs): # real signature unknown
        """ save_contact_sync(self, overwrite_existing:bool, conflict_resolution:EDataServer.ConflictResolution, contact:EBookContacts.Contact, extra:str=None, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_new_uid:str, out_new_extra:str """
        pass

    def do_search_sync(self, *args, **kwargs): # real signature unknown
        """ search_sync(self, expr:str=None, meta_contact:bool, cancellable:Gio.Cancellable=None) -> bool, out_contacts:list """
        pass

    def do_search_uids_sync(self, *args, **kwargs): # real signature unknown
        """ search_uids_sync(self, expr:str=None, cancellable:Gio.Cancellable=None) -> bool, out_uids:list """
        pass

    def do_shutdown(self, *args, **kwargs): # real signature unknown
        """ shutdown(self) """
        pass

    def do_source_changed(self, *args, **kwargs): # real signature unknown
        """ source_changed(self) """
        pass

    def dup_cache_dir(self): # real signature unknown; restored from __doc__
        """ dup_cache_dir(self) -> str """
        return ""

    def dup_locale(self): # real signature unknown; restored from __doc__
        """ dup_locale(self) -> str """
        return ""

    def dup_sync_tag(self): # real signature unknown; restored from __doc__
        """ dup_sync_tag(self) -> str or None """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def empty_cache_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ empty_cache_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ensure_connected_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ ensure_connected_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> str """
        return ""

    def get_changes_sync(self, last_sync_tag=None, is_repeat, cancellable=None): # real signature unknown; restored from __doc__
        """ get_changes_sync(self, last_sync_tag:str=None, is_repeat:bool, cancellable:Gio.Cancellable=None) -> bool, out_new_sync_tag:str, out_repeat:bool, out_created_objects:list, out_modified_objects:list, out_removed_objects:list """
        return False

    def get_connected_writable(self): # real signature unknown; restored from __doc__
        """ get_connected_writable(self) -> bool """
        return False

    def get_contact(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact(self, uid:str, cancellable:Gio.Cancellable=None) -> EBookContacts.Contact """
        pass

    def get_contact_finish(self, result): # real signature unknown; restored from __doc__
        """ get_contact_finish(self, result:Gio.AsyncResult) -> EBookContacts.Contact """
        pass

    def get_contact_list(self, query, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact_list(self, query:str, cancellable:Gio.Cancellable=None) -> bool, out_contacts:list """
        return False

    def get_contact_list_finish(self, result, out_contacts): # real signature unknown; restored from __doc__
        """ get_contact_list_finish(self, result:Gio.AsyncResult, out_contacts:GLib.Queue) -> bool """
        return False

    def get_contact_list_sync(self, query, out_contacts, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact_list_sync(self, query:str, out_contacts:GLib.Queue, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_contact_list_uids(self, query, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact_list_uids(self, query:str, cancellable:Gio.Cancellable=None) -> bool, out_uids:list """
        return False

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

    def get_ever_connected(self): # real signature unknown; restored from __doc__
        """ get_ever_connected(self) -> bool """
        return False

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

    def get_ssl_error_details(self): # real signature unknown; restored from __doc__
        """ get_ssl_error_details(self) -> bool, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags """
        return False

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

    def inline_local_photos_sync(self, contact, cancellable=None): # real signature unknown; restored from __doc__
        """ inline_local_photos_sync(self, contact:EBookContacts.Contact, cancellable:Gio.Cancellable=None) -> bool """
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

    def list_existing_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ list_existing_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_new_sync_tag:str, out_existing_objects:list """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_views(self): # real signature unknown; restored from __doc__
        """ list_views(self) -> list """
        return []

    def load_contact_sync(self, uid, extra=None, cancellable=None): # real signature unknown; restored from __doc__
        """ load_contact_sync(self, uid:str, extra:str=None, cancellable:Gio.Cancellable=None) -> bool, out_contact:EBookContacts.Contact, out_extra:str """
        return False

    def modify_contacts(self, vcards, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_contacts(self, vcards:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_contacts:list """
        return False

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

    def open(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def process_changes_sync(self, created_objects=None, modified_objects=None, removed_objects=None, cancellable=None): # real signature unknown; restored from __doc__
        """ process_changes_sync(self, created_objects:list=None, modified_objects:list=None, removed_objects:list=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh(self, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def refresh_finish(self, result): # real signature unknown; restored from __doc__
        """ refresh_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def refresh_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref_cache(self): # real signature unknown; restored from __doc__
        """ ref_cache(self) -> EDataBook.BookCache """
        pass

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

    def remove_contacts(self, uids, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contacts(self, uids:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_removed_uids:list """
        return False

    def remove_contacts_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_contacts_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_contacts_sync(self, uids, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contacts_sync(self, uids:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_contact_sync(self, conflict_resolution, uid, extra=None, p_object=None, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contact_sync(self, conflict_resolution:EDataServer.ConflictResolution, uid:str, extra:str=None, object:str=None, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
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

    def requires_reconnect(self): # real signature unknown; restored from __doc__
        """ requires_reconnect(self) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def save_contact_sync(self, overwrite_existing, conflict_resolution, contact, extra=None, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ save_contact_sync(self, overwrite_existing:bool, conflict_resolution:EDataServer.ConflictResolution, contact:EBookContacts.Contact, extra:str=None, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_new_uid:str, out_new_extra:str """
        return False

    def schedule_authenticate(self, credentials=None): # real signature unknown; restored from __doc__
        """ schedule_authenticate(self, credentials:EDataServer.NamedParameters=None) """
        pass

    def schedule_credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, who_calls=None): # real signature unknown; restored from __doc__
        """ schedule_credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, who_calls:str=None) """
        pass

    def schedule_custom_operation(self, use_cancellable=None, func, user_data=None): # real signature unknown; restored from __doc__
        """ schedule_custom_operation(self, use_cancellable:Gio.Cancellable=None, func:EDataBook.BookBackendCustomOpFunc, user_data=None) """
        pass

    def schedule_refresh(self): # real signature unknown; restored from __doc__
        """ schedule_refresh(self) """
        pass

    def search_sync(self, expr=None, meta_contact, cancellable=None): # real signature unknown; restored from __doc__
        """ search_sync(self, expr:str=None, meta_contact:bool, cancellable:Gio.Cancellable=None) -> bool, out_contacts:list """
        return False

    def search_uids_sync(self, expr=None, cancellable=None): # real signature unknown; restored from __doc__
        """ search_uids_sync(self, expr:str=None, cancellable:Gio.Cancellable=None) -> bool, out_uids:list """
        return False

    def set_cache(self, cache): # real signature unknown; restored from __doc__
        """ set_cache(self, cache:EDataBook.BookCache) """
        pass

    def set_cache_dir(self, cache_dir): # real signature unknown; restored from __doc__
        """ set_cache_dir(self, cache_dir:str) """
        pass

    def set_connectable(self, connectable): # real signature unknown; restored from __doc__
        """ set_connectable(self, connectable:Gio.SocketConnectable) """
        pass

    def set_connected_writable(self, value): # real signature unknown; restored from __doc__
        """ set_connected_writable(self, value:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data_book(self, data_book): # real signature unknown; restored from __doc__
        """ set_data_book(self, data_book:EDataBook.DataBook) """
        pass

    def set_ever_connected(self, value): # real signature unknown; restored from __doc__
        """ set_ever_connected(self, value:bool) """
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

    def split_changes_sync(self, objects, cancellable=None): # real signature unknown; restored from __doc__
        """ split_changes_sync(self, objects:list, cancellable:Gio.Cancellable=None) -> bool, objects:list, out_created_objects:list, out_modified_objects:list, out_removed_objects:list """
        return False

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

    def store_inline_photos_sync(self, contact, cancellable=None): # real signature unknown; restored from __doc__
        """ store_inline_photos_sync(self, contact:EBookContacts.Contact, cancellable:Gio.Cancellable=None) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f09d4187070>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BookMetaBackend), '__module__': 'gi.repository.EDataBook', '__gtype__': <GType EBookMetaBackend (94654337915056)>, '__doc__': None, '__gsignals__': {}, 'connect_sync': gi.FunctionInfo(connect_sync), 'disconnect_sync': gi.FunctionInfo(disconnect_sync), 'dup_sync_tag': gi.FunctionInfo(dup_sync_tag), 'empty_cache_sync': gi.FunctionInfo(empty_cache_sync), 'ensure_connected_sync': gi.FunctionInfo(ensure_connected_sync), 'get_capabilities': gi.FunctionInfo(get_capabilities), 'get_changes_sync': gi.FunctionInfo(get_changes_sync), 'get_connected_writable': gi.FunctionInfo(get_connected_writable), 'get_ever_connected': gi.FunctionInfo(get_ever_connected), 'get_ssl_error_details': gi.FunctionInfo(get_ssl_error_details), 'inline_local_photos_sync': gi.FunctionInfo(inline_local_photos_sync), 'list_existing_sync': gi.FunctionInfo(list_existing_sync), 'load_contact_sync': gi.FunctionInfo(load_contact_sync), 'process_changes_sync': gi.FunctionInfo(process_changes_sync), 'ref_cache': gi.FunctionInfo(ref_cache), 'refresh_sync': gi.FunctionInfo(refresh_sync), 'remove_contact_sync': gi.FunctionInfo(remove_contact_sync), 'requires_reconnect': gi.FunctionInfo(requires_reconnect), 'save_contact_sync': gi.FunctionInfo(save_contact_sync), 'schedule_refresh': gi.FunctionInfo(schedule_refresh), 'search_sync': gi.FunctionInfo(search_sync), 'search_uids_sync': gi.FunctionInfo(search_uids_sync), 'set_cache': gi.FunctionInfo(set_cache), 'set_connected_writable': gi.FunctionInfo(set_connected_writable), 'set_ever_connected': gi.FunctionInfo(set_ever_connected), 'split_changes_sync': gi.FunctionInfo(split_changes_sync), 'store_inline_photos_sync': gi.FunctionInfo(store_inline_photos_sync), 'do_connect_sync': gi.VFuncInfo(connect_sync), 'do_disconnect_sync': gi.VFuncInfo(disconnect_sync), 'do_get_changes_sync': gi.VFuncInfo(get_changes_sync), 'do_get_ssl_error_details': gi.VFuncInfo(get_ssl_error_details), 'do_list_existing_sync': gi.VFuncInfo(list_existing_sync), 'do_load_contact_sync': gi.VFuncInfo(load_contact_sync), 'do_remove_contact_sync': gi.VFuncInfo(remove_contact_sync), 'do_requires_reconnect': gi.VFuncInfo(requires_reconnect), 'do_save_contact_sync': gi.VFuncInfo(save_contact_sync), 'do_search_sync': gi.VFuncInfo(search_sync), 'do_search_uids_sync': gi.VFuncInfo(search_uids_sync), 'do_source_changed': gi.VFuncInfo(source_changed), 'parent': <property object at 0x7f09d41b5a90>, 'priv': <property object at 0x7f09d41b5b80>})"
    __gdoc__ = "Object EBookMetaBackend\n\nSignals from EBookMetaBackend:\n  refresh-completed ()\n  source-changed ()\n\nProperties from EBookMetaBackend:\n  cache -> EBookCache: Cache\n    Book Cache\n\nSignals from EBookBackend:\n  closed (gchararray)\n  shutdown ()\n\nProperties from EBookBackend:\n  cache-dir -> gchararray: Cache Dir\n    The backend's cache directory\n  proxy-resolver -> GProxyResolver: Proxy Resolver\n    The proxy resolver for this backend\n  registry -> ESourceRegistry: Registry\n    Data source registry\n  writable -> gboolean: Writable\n    Whether the backend will accept changes\n\nProperties from EBackend:\n  connectable -> GSocketConnectable: Connectable\n    Socket endpoint of a network service\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  online -> gboolean: Online\n    Whether the backend is online\n  source -> ESource: Source\n    The data source being acted upon\n  user-prompter -> EUserPrompter: User Prompter\n    User prompter instance\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EBookMetaBackend (94654337915056)>'
    __info__ = ObjectInfo(BookMetaBackend)


