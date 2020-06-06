# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


from .Folder import Folder

class VeeFolder(Folder):
    """
    :Constructors:
    
    ::
    
        VeeFolder(**properties)
        new(parent_store:Camel.Store, full:str, flags:int) -> Camel.Folder
    """
    def add_folder(self, subfolder, cancellable=None): # real signature unknown; restored from __doc__
        """ add_folder(self, subfolder:Camel.Folder, cancellable:Gio.Cancellable=None) """
        pass

    def add_vuid(self, mi_data=None, changes=None): # real signature unknown; restored from __doc__
        """ add_vuid(self, mi_data=None, changes:Camel.FolderChangeInfo=None) """
        pass

    def append_message(self, message, info, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ append_message(self, message:Camel.MimeMessage, info:Camel.MessageInfo, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def append_message_finish(self, result, appended_uid): # real signature unknown; restored from __doc__
        """ append_message_finish(self, result:Gio.AsyncResult, appended_uid:str) -> bool """
        return False

    def append_message_sync(self, message, info, appended_uid, cancellable=None): # real signature unknown; restored from __doc__
        """ append_message_sync(self, message:Camel.MimeMessage, info:Camel.MessageInfo, appended_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, changes): # real signature unknown; restored from __doc__
        """ changed(self, changes:Camel.FolderChangeInfo) """
        pass

    def cmp_uids(self, uid1, uid2): # real signature unknown; restored from __doc__
        """ cmp_uids(self, uid1:str, uid2:str) -> int """
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

    def construct(self, flags): # real signature unknown; restored from __doc__
        """ construct(self, flags:int) """
        pass

    def count_by_expression(self, expression, cancellable=None): # real signature unknown; restored from __doc__
        """ count_by_expression(self, expression:str, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add_folder(self, *args, **kwargs): # real signature unknown
        """ add_folder(self, subfolder:Camel.Folder, cancellable:Gio.Cancellable=None) """
        pass

    def do_append_message_sync(self, *args, **kwargs): # real signature unknown
        """ append_message_sync(self, message:Camel.MimeMessage, info:Camel.MessageInfo, appended_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self, changes:Camel.FolderChangeInfo) """
        pass

    def do_cmp_uids(self, *args, **kwargs): # real signature unknown
        """ cmp_uids(self, uid1:str, uid2:str) -> int """
        pass

    def do_count_by_expression(self, *args, **kwargs): # real signature unknown
        """ count_by_expression(self, expression:str, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_deleted(self, *args, **kwargs): # real signature unknown
        """ deleted(self) """
        pass

    def do_delete_(self, *args, **kwargs): # real signature unknown
        """ delete_(self) """
        pass

    def do_expunge_sync(self, *args, **kwargs): # real signature unknown
        """ expunge_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_folder_changed(self, *args, **kwargs): # real signature unknown
        """ folder_changed(self, subfolder:Camel.Folder, changes:Camel.FolderChangeInfo) """
        pass

    def do_freeze(self, *args, **kwargs): # real signature unknown
        """ freeze(self) """
        pass

    def do_free_summary(self, *args, **kwargs): # real signature unknown
        """ free_summary(self, array:list) """
        pass

    def do_free_uids(self, *args, **kwargs): # real signature unknown
        """ free_uids(self, array:list) """
        pass

    def do_get_filename(self, *args, **kwargs): # real signature unknown
        """ get_filename(self, uid:str) -> str """
        pass

    def do_get_message_cached(self, *args, **kwargs): # real signature unknown
        """ get_message_cached(self, message_uid:str, cancellable:Gio.Cancellable=None) -> Camel.MimeMessage or None """
        pass

    def do_get_message_count(self, *args, **kwargs): # real signature unknown
        """ get_message_count(self) -> int """
        pass

    def do_get_message_flags(self, *args, **kwargs): # real signature unknown
        """ get_message_flags(self, uid:str) -> int """
        pass

    def do_get_message_info(self, *args, **kwargs): # real signature unknown
        """ get_message_info(self, uid:str) -> Camel.MessageInfo """
        pass

    def do_get_message_sync(self, *args, **kwargs): # real signature unknown
        """ get_message_sync(self, message_uid:str, cancellable:Gio.Cancellable=None) -> Camel.MimeMessage """
        pass

    def do_get_message_user_flag(self, *args, **kwargs): # real signature unknown
        """ get_message_user_flag(self, uid:str, name:str) -> bool """
        pass

    def do_get_message_user_tag(self, *args, **kwargs): # real signature unknown
        """ get_message_user_tag(self, uid:str, name:str) -> str """
        pass

    def do_get_permanent_flags(self, *args, **kwargs): # real signature unknown
        """ get_permanent_flags(self) -> int """
        pass

    def do_get_quota_info_sync(self, *args, **kwargs): # real signature unknown
        """ get_quota_info_sync(self, cancellable:Gio.Cancellable=None) -> Camel.FolderQuotaInfo """
        pass

    def do_get_summary(self, *args, **kwargs): # real signature unknown
        """ get_summary(self) -> list """
        pass

    def do_get_uids(self, *args, **kwargs): # real signature unknown
        """ get_uids(self) -> list """
        pass

    def do_get_uncached_uids(self, *args, **kwargs): # real signature unknown
        """ get_uncached_uids(self, uids:list) -> list """
        pass

    def do_has_search_capability(self, *args, **kwargs): # real signature unknown
        """ has_search_capability(self) -> bool """
        pass

    def do_is_frozen(self, *args, **kwargs): # real signature unknown
        """ is_frozen(self) -> bool """
        pass

    def do_prepare_content_refresh(self, *args, **kwargs): # real signature unknown
        """ prepare_content_refresh(self) """
        pass

    def do_purge_message_cache_sync(self, *args, **kwargs): # real signature unknown
        """ purge_message_cache_sync(self, start_uid:str, end_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_rebuild_folder(self, *args, **kwargs): # real signature unknown
        """ rebuild_folder(self, subfolder:Camel.Folder, cancellable:Gio.Cancellable=None) """
        pass

    def do_refresh_info_sync(self, *args, **kwargs): # real signature unknown
        """ refresh_info_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remove_folder(self, *args, **kwargs): # real signature unknown
        """ remove_folder(self, subfolder:Camel.Folder, cancellable:Gio.Cancellable=None) """
        pass

    def do_rename(self, *args, **kwargs): # real signature unknown
        """ rename(self, new_name:str) """
        pass

    def do_renamed(self, *args, **kwargs): # real signature unknown
        """ renamed(self, old_name:str) """
        pass

    def do_search_by_expression(self, *args, **kwargs): # real signature unknown
        """ search_by_expression(self, expression:str, cancellable:Gio.Cancellable=None) -> list """
        pass

    def do_search_by_uids(self, *args, **kwargs): # real signature unknown
        """ search_by_uids(self, expression:str, uids:list, cancellable:Gio.Cancellable=None) -> list """
        pass

    def do_search_free(self, *args, **kwargs): # real signature unknown
        """ search_free(self, result:list) """
        pass

    def do_set_expression(self, *args, **kwargs): # real signature unknown
        """ set_expression(self, expression:str) """
        pass

    def do_set_message_flags(self, *args, **kwargs): # real signature unknown
        """ set_message_flags(self, uid:str, mask:int, set:int) -> bool """
        pass

    def do_set_message_user_flag(self, *args, **kwargs): # real signature unknown
        """ set_message_user_flag(self, uid:str, name:str, value:bool) """
        pass

    def do_set_message_user_tag(self, *args, **kwargs): # real signature unknown
        """ set_message_user_tag(self, uid:str, name:str, value:str) """
        pass

    def do_sort_uids(self, *args, **kwargs): # real signature unknown
        """ sort_uids(self, uids:list) """
        pass

    def do_state_read(self, *args, **kwargs): # real signature unknown
        """ state_read(self, fp=None) -> int """
        pass

    def do_state_write(self, *args, **kwargs): # real signature unknown
        """ state_write(self, fp=None) -> int """
        pass

    def do_synchronize_message_sync(self, *args, **kwargs): # real signature unknown
        """ synchronize_message_sync(self, message_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_synchronize_sync(self, *args, **kwargs): # real signature unknown
        """ synchronize_sync(self, expunge:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_thaw(self, *args, **kwargs): # real signature unknown
        """ thaw(self) """
        pass

    def do_transfer_messages_to_sync(self, *args, **kwargs): # real signature unknown
        """ transfer_messages_to_sync(self, message_uids:list, destination:Camel.Folder, delete_originals:bool, cancellable:Gio.Cancellable=None) -> bool, transferred_uids:list """
        pass

    def dup_description(self): # real signature unknown; restored from __doc__
        """ dup_description(self) -> str """
        return ""

    def dup_display_name(self): # real signature unknown; restored from __doc__
        """ dup_display_name(self) -> str """
        return ""

    def dup_full_name(self): # real signature unknown; restored from __doc__
        """ dup_full_name(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def expunge(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ expunge(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def expunge_finish(self, result): # real signature unknown; restored from __doc__
        """ expunge_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def expunge_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ expunge_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze(self): # real signature unknown; restored from __doc__
        """ freeze(self) """
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

    def free_deep(self, array): # real signature unknown; restored from __doc__
        """ free_deep(self, array:list) """
        pass

    def free_shallow(self, array): # real signature unknown; restored from __doc__
        """ free_shallow(self, array:list) """
        pass

    def free_summary(self, array): # real signature unknown; restored from __doc__
        """ free_summary(self, array:list) """
        pass

    def free_uids(self, array): # real signature unknown; restored from __doc__
        """ free_uids(self, array:list) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_auto_update(self): # real signature unknown; restored from __doc__
        """ get_auto_update(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_deleted_message_count(self): # real signature unknown; restored from __doc__
        """ get_deleted_message_count(self) -> int """
        return 0

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_expression(self): # real signature unknown; restored from __doc__
        """ get_expression(self) -> str """
        return ""

    def get_filename(self, uid): # real signature unknown; restored from __doc__
        """ get_filename(self, uid:str) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_folder_summary(self): # real signature unknown; restored from __doc__
        """ get_folder_summary(self) -> Camel.FolderSummary """
        pass

    def get_frozen_count(self): # real signature unknown; restored from __doc__
        """ get_frozen_count(self) -> int """
        return 0

    def get_full_name(self): # real signature unknown; restored from __doc__
        """ get_full_name(self) -> str """
        return ""

    def get_location(self, vinfo): # real signature unknown; restored from __doc__
        """ get_location(self, vinfo:Camel.VeeMessageInfo) -> Camel.Folder, realuid:str """
        pass

    def get_mark_seen(self): # real signature unknown; restored from __doc__
        """ get_mark_seen(self) -> Camel.ThreeState """
        pass

    def get_mark_seen_timeout(self): # real signature unknown; restored from __doc__
        """ get_mark_seen_timeout(self) -> int """
        return 0

    def get_message(self, message_uid, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_message(self, message_uid:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_message_cached(self, message_uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_message_cached(self, message_uid:str, cancellable:Gio.Cancellable=None) -> Camel.MimeMessage or None """
        pass

    def get_message_count(self): # real signature unknown; restored from __doc__
        """ get_message_count(self) -> int """
        return 0

    def get_message_finish(self, result): # real signature unknown; restored from __doc__
        """ get_message_finish(self, result:Gio.AsyncResult) -> Camel.MimeMessage """
        pass

    def get_message_flags(self, uid): # real signature unknown; restored from __doc__
        """ get_message_flags(self, uid:str) -> int """
        return 0

    def get_message_info(self, uid): # real signature unknown; restored from __doc__
        """ get_message_info(self, uid:str) -> Camel.MessageInfo """
        pass

    def get_message_sync(self, message_uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_message_sync(self, message_uid:str, cancellable:Gio.Cancellable=None) -> Camel.MimeMessage """
        pass

    def get_message_user_flag(self, uid, name): # real signature unknown; restored from __doc__
        """ get_message_user_flag(self, uid:str, name:str) -> bool """
        return False

    def get_message_user_tag(self, uid, name): # real signature unknown; restored from __doc__
        """ get_message_user_tag(self, uid:str, name:str) -> str """
        return ""

    def get_parent_store(self): # real signature unknown; restored from __doc__
        """ get_parent_store(self) """
        pass

    def get_permanent_flags(self): # real signature unknown; restored from __doc__
        """ get_permanent_flags(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_quota_info(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_quota_info(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_quota_info_finish(self, result): # real signature unknown; restored from __doc__
        """ get_quota_info_finish(self, result:Gio.AsyncResult) -> Camel.FolderQuotaInfo """
        pass

    def get_quota_info_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_quota_info_sync(self, cancellable:Gio.Cancellable=None) -> Camel.FolderQuotaInfo """
        pass

    def get_state_filename(self): # real signature unknown; restored from __doc__
        """ get_state_filename(self) -> str """
        return ""

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> list """
        return []

    def get_uids(self): # real signature unknown; restored from __doc__
        """ get_uids(self) -> list """
        return []

    def get_uncached_uids(self, uids): # real signature unknown; restored from __doc__
        """ get_uncached_uids(self, uids:list) -> list """
        return []

    def get_unread_message_count(self): # real signature unknown; restored from __doc__
        """ get_unread_message_count(self) -> int """
        return 0

    def get_vee_uid_folder(self, vee_message_uid): # real signature unknown; restored from __doc__
        """ get_vee_uid_folder(self, vee_message_uid:str) -> Camel.Folder or None """
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

    def has_summary_capability(self): # real signature unknown; restored from __doc__
        """ has_summary_capability(self) -> bool """
        return False

    def ignore_next_changed_event(self, subfolder): # real signature unknown; restored from __doc__
        """ ignore_next_changed_event(self, subfolder:Camel.Folder) """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_frozen(self): # real signature unknown; restored from __doc__
        """ is_frozen(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) """
        pass

    def new(self, parent_store, full, flags): # real signature unknown; restored from __doc__
        """ new(parent_store:Camel.Store, full:str, flags:int) -> Camel.Folder """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
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

    def prepare_content_refresh(self): # real signature unknown; restored from __doc__
        """ prepare_content_refresh(self) """
        pass

    def purge_message_cache(self, start_uid, end_uid, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ purge_message_cache(self, start_uid:str, end_uid:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def purge_message_cache_finish(self, result): # real signature unknown; restored from __doc__
        """ purge_message_cache_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def purge_message_cache_sync(self, start_uid, end_uid, cancellable=None): # real signature unknown; restored from __doc__
        """ purge_message_cache_sync(self, start_uid:str, end_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def rebuild_folder(self, subfolder, cancellable=None): # real signature unknown; restored from __doc__
        """ rebuild_folder(self, subfolder:Camel.Folder, cancellable:Gio.Cancellable=None) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh_info(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ refresh_info(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def refresh_info_finish(self, result): # real signature unknown; restored from __doc__
        """ refresh_info_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def refresh_info_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_info_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref_folders(self): # real signature unknown; restored from __doc__
        """ ref_folders(self) -> list """
        return []

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_folder(self, subfolder, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_folder(self, subfolder:Camel.Folder, cancellable:Gio.Cancellable=None) """
        pass

    def remove_from_ignore_changed_event(self, subfolder): # real signature unknown; restored from __doc__
        """ remove_from_ignore_changed_event(self, subfolder:Camel.Folder) """
        pass

    def remove_vuid(self, mi_data=None, changes=None): # real signature unknown; restored from __doc__
        """ remove_vuid(self, mi_data=None, changes:Camel.FolderChangeInfo=None) """
        pass

    def rename(self, new_name): # real signature unknown; restored from __doc__
        """ rename(self, new_name:str) """
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

    def search_by_expression(self, expression, cancellable=None): # real signature unknown; restored from __doc__
        """ search_by_expression(self, expression:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def search_by_uids(self, expression, uids, cancellable=None): # real signature unknown; restored from __doc__
        """ search_by_uids(self, expression:str, uids:list, cancellable:Gio.Cancellable=None) -> list """
        return []

    def search_free(self, result): # real signature unknown; restored from __doc__
        """ search_free(self, result:list) """
        pass

    def set_auto_update(self, auto_update): # real signature unknown; restored from __doc__
        """ set_auto_update(self, auto_update:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_display_name(self, display_name): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str) """
        pass

    def set_expression(self, expression): # real signature unknown; restored from __doc__
        """ set_expression(self, expression:str) """
        pass

    def set_flags(self, folder_flags): # real signature unknown; restored from __doc__
        """ set_flags(self, folder_flags:int) """
        pass

    def set_folders(self, folders, cancellable=None): # real signature unknown; restored from __doc__
        """ set_folders(self, folders:list, cancellable:Gio.Cancellable=None) """
        pass

    def set_full_name(self, full_name): # real signature unknown; restored from __doc__
        """ set_full_name(self, full_name:str) """
        pass

    def set_lock_async(self, skip_folder_lock): # real signature unknown; restored from __doc__
        """ set_lock_async(self, skip_folder_lock:bool) """
        pass

    def set_mark_seen(self, mark_seen): # real signature unknown; restored from __doc__
        """ set_mark_seen(self, mark_seen:Camel.ThreeState) """
        pass

    def set_mark_seen_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_mark_seen_timeout(self, timeout:int) """
        pass

    def set_message_flags(self, uid, mask, set): # real signature unknown; restored from __doc__
        """ set_message_flags(self, uid:str, mask:int, set:int) -> bool """
        return False

    def set_message_user_flag(self, uid, name, value): # real signature unknown; restored from __doc__
        """ set_message_user_flag(self, uid:str, name:str, value:bool) """
        pass

    def set_message_user_tag(self, uid, name, value): # real signature unknown; restored from __doc__
        """ set_message_user_tag(self, uid:str, name:str, value:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_state_filename(self, state_filename): # real signature unknown; restored from __doc__
        """ set_state_filename(self, state_filename:str) """
        pass

    def sort_uids(self, uids): # real signature unknown; restored from __doc__
        """ sort_uids(self, uids:list) """
        pass

    def state_read(self): # real signature unknown; restored from __doc__
        """ state_read(self) -> int """
        return 0

    def state_write(self): # real signature unknown; restored from __doc__
        """ state_write(self) -> int """
        return 0

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

    def synchronize(self, expunge, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ synchronize(self, expunge:bool, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def synchronize_finish(self, result): # real signature unknown; restored from __doc__
        """ synchronize_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def synchronize_message(self, message_uid, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ synchronize_message(self, message_uid:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def synchronize_message_finish(self, result): # real signature unknown; restored from __doc__
        """ synchronize_message_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def synchronize_message_sync(self, message_uid, cancellable=None): # real signature unknown; restored from __doc__
        """ synchronize_message_sync(self, message_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def synchronize_sync(self, expunge, cancellable=None): # real signature unknown; restored from __doc__
        """ synchronize_sync(self, expunge:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def take_folder_summary(self, summary): # real signature unknown; restored from __doc__
        """ take_folder_summary(self, summary:Camel.FolderSummary) """
        pass

    def thaw(self): # real signature unknown; restored from __doc__
        """ thaw(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def threaded_messages_dump(self, c): # real signature unknown; restored from __doc__
        """ threaded_messages_dump(c:Camel.FolderThreadNode) -> int """
        return 0

    def transfer_messages_to(self, message_uids, destination, delete_originals, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ transfer_messages_to(self, message_uids:list, destination:Camel.Folder, delete_originals:bool, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def transfer_messages_to_finish(self, result): # real signature unknown; restored from __doc__
        """ transfer_messages_to_finish(self, result:Gio.AsyncResult) -> bool, transferred_uids:list """
        return False

    def transfer_messages_to_sync(self, message_uids, destination, delete_originals, cancellable=None): # real signature unknown; restored from __doc__
        """ transfer_messages_to_sync(self, message_uids:list, destination:Camel.Folder, delete_originals:bool, cancellable:Gio.Cancellable=None) -> bool, transferred_uids:list """
        return False

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7b348cddf0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(VeeFolder), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelVeeFolder (94124524416272)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_folder': gi.FunctionInfo(add_folder), 'add_vuid': gi.FunctionInfo(add_vuid), 'construct': gi.FunctionInfo(construct), 'get_auto_update': gi.FunctionInfo(get_auto_update), 'get_expression': gi.FunctionInfo(get_expression), 'get_flags': gi.FunctionInfo(get_flags), 'get_location': gi.FunctionInfo(get_location), 'get_vee_uid_folder': gi.FunctionInfo(get_vee_uid_folder), 'ignore_next_changed_event': gi.FunctionInfo(ignore_next_changed_event), 'rebuild_folder': gi.FunctionInfo(rebuild_folder), 'ref_folders': gi.FunctionInfo(ref_folders), 'remove_folder': gi.FunctionInfo(remove_folder), 'remove_from_ignore_changed_event': gi.FunctionInfo(remove_from_ignore_changed_event), 'remove_vuid': gi.FunctionInfo(remove_vuid), 'set_auto_update': gi.FunctionInfo(set_auto_update), 'set_expression': gi.FunctionInfo(set_expression), 'set_folders': gi.FunctionInfo(set_folders), 'do_add_folder': gi.VFuncInfo(add_folder), 'do_folder_changed': gi.VFuncInfo(folder_changed), 'do_rebuild_folder': gi.VFuncInfo(rebuild_folder), 'do_remove_folder': gi.VFuncInfo(remove_folder), 'do_set_expression': gi.VFuncInfo(set_expression), 'parent': <property object at 0x7f7b34efa040>, 'priv': <property object at 0x7f7b34efa130>})"
    __gdoc__ = "Object CamelVeeFolder\n\nProperties from CamelVeeFolder:\n  auto-update -> gboolean: Auto Update\n    Automatically _update on change in source folders\n\nSignals from CamelFolder:\n  changed (CamelFolderChangeInfo)\n  deleted ()\n  renamed (gchararray)\n\nProperties from CamelFolder:\n  description -> gchararray: Description\n    The folder's description\n  display-name -> gchararray: Display Name\n    The folder's display name\n  full-name -> gchararray: Full Name\n    The folder's fully qualified name\n  parent-store -> CamelStore: Parent Store\n    The store to which the folder belongs\n  mark-seen -> CamelThreeState: Mark Seen\n    Mark messages as read after N seconds\n  mark-seen-timeout -> gint: Mark Seen Timeout\n    Mark seen timeout\n\nProperties from CamelObject:\n  state-filename -> gchararray: State Filename\n    File containing persistent property values\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelVeeFolder (94124524416272)>'
    __info__ = ObjectInfo(VeeFolder)


