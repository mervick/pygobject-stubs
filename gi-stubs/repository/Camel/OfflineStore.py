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


from .Store import Store

class OfflineStore(Store):
    """
    :Constructors:
    
    ::
    
        OfflineStore(**properties)
    """
    def authenticate(self, mechanism=None, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ authenticate(self, mechanism:str=None, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def authenticate_finish(self, result): # real signature unknown; restored from __doc__
        """ authenticate_finish(self, result:Gio.AsyncResult) -> Camel.AuthenticationResult """
        pass

    def authenticate_sync(self, mechanism=None, cancellable=None): # real signature unknown; restored from __doc__
        """ authenticate_sync(self, mechanism:str=None, cancellable:Gio.Cancellable=None) -> Camel.AuthenticationResult """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_refresh_folder(self, info): # real signature unknown; restored from __doc__
        """ can_refresh_folder(self, info:Camel.FolderInfo) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def connect_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def create_folder(self, parent_name=None, folder_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_folder(self, parent_name:str=None, folder_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ create_folder_finish(self, result:Gio.AsyncResult) -> Camel.FolderInfo or None """
        pass

    def create_folder_sync(self, parent_name=None, folder_name, cancellable=None): # real signature unknown; restored from __doc__
        """ create_folder_sync(self, parent_name:str=None, folder_name:str, cancellable:Gio.Cancellable=None) -> Camel.FolderInfo or None """
        pass

    def delete_cached_folder(self, folder_name): # real signature unknown; restored from __doc__
        """ delete_cached_folder(self, folder_name:str) """
        pass

    def delete_folder(self, folder_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_folder(self, folder_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_folder_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def delete_folder_sync(self, folder_name, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_folder_sync(self, folder_name:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(self, clean, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ disconnect(self, clean:bool, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_finish(self, result): # real signature unknown; restored from __doc__
        """ disconnect_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def disconnect_sync(self, clean, cancellable=None): # real signature unknown; restored from __doc__
        """ disconnect_sync(self, clean:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def do_authenticate_sync(self, *args, **kwargs): # real signature unknown
        """ authenticate_sync(self, mechanism:str=None, cancellable:Gio.Cancellable=None) -> Camel.AuthenticationResult """
        pass

    def do_can_refresh_folder(self, *args, **kwargs): # real signature unknown
        """ can_refresh_folder(self, info:Camel.FolderInfo) -> bool """
        pass

    def do_connect_sync(self, *args, **kwargs): # real signature unknown
        """ connect_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_create_folder_sync(self, *args, **kwargs): # real signature unknown
        """ create_folder_sync(self, parent_name:str=None, folder_name:str, cancellable:Gio.Cancellable=None) -> Camel.FolderInfo or None """
        pass

    def do_delete_folder_sync(self, *args, **kwargs): # real signature unknown
        """ delete_folder_sync(self, folder_name:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_disconnect_sync(self, *args, **kwargs): # real signature unknown
        """ disconnect_sync(self, clean:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_dup_downsync_folders(self, *args, **kwargs): # real signature unknown
        """ dup_downsync_folders(self) -> list """
        pass

    def do_folder_created(self, *args, **kwargs): # real signature unknown
        """ folder_created(self, folder_info:Camel.FolderInfo) """
        pass

    def do_folder_deleted(self, *args, **kwargs): # real signature unknown
        """ folder_deleted(self, folder_info:Camel.FolderInfo) """
        pass

    def do_folder_info_stale(self, *args, **kwargs): # real signature unknown
        """ folder_info_stale(self) """
        pass

    def do_folder_opened(self, *args, **kwargs): # real signature unknown
        """ folder_opened(self, folder:Camel.Folder) """
        pass

    def do_folder_renamed(self, *args, **kwargs): # real signature unknown
        """ folder_renamed(self, old_name:str, folder_info:Camel.FolderInfo) """
        pass

    def do_get_folder_info_sync(self, *args, **kwargs): # real signature unknown
        """ get_folder_info_sync(self, top:str=None, flags:Camel.StoreGetFolderInfoFlags, cancellable:Gio.Cancellable=None) -> Camel.FolderInfo or None """
        pass

    def do_get_folder_sync(self, *args, **kwargs): # real signature unknown
        """ get_folder_sync(self, folder_name:str, flags:Camel.StoreGetFolderFlags, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def do_get_inbox_folder_sync(self, *args, **kwargs): # real signature unknown
        """ get_inbox_folder_sync(self, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def do_get_junk_folder_sync(self, *args, **kwargs): # real signature unknown
        """ get_junk_folder_sync(self, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self, brief:bool) -> str """
        pass

    def do_get_trash_folder_sync(self, *args, **kwargs): # real signature unknown
        """ get_trash_folder_sync(self, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def do_initial_setup_sync(self, *args, **kwargs): # real signature unknown
        """ initial_setup_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_save_setup:dict """
        pass

    def do_query_auth_types_sync(self, *args, **kwargs): # real signature unknown
        """ query_auth_types_sync(self, cancellable:Gio.Cancellable=None) -> list """
        pass

    def do_rename_folder_sync(self, *args, **kwargs): # real signature unknown
        """ rename_folder_sync(self, old_name:str, new_name:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_state_read(self, *args, **kwargs): # real signature unknown
        """ state_read(self, fp=None) -> int """
        pass

    def do_state_write(self, *args, **kwargs): # real signature unknown
        """ state_write(self, fp=None) -> int """
        pass

    def do_synchronize_sync(self, *args, **kwargs): # real signature unknown
        """ synchronize_sync(self, expunge:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def dup_display_name(self): # real signature unknown; restored from __doc__
        """ dup_display_name(self) -> str """
        return ""

    def dup_downsync_folders(self): # real signature unknown; restored from __doc__
        """ dup_downsync_folders(self) -> list """
        return []

    def dup_opened_folders(self): # real signature unknown; restored from __doc__
        """ dup_opened_folders(self) -> list """
        return []

    def dup_password(self): # real signature unknown; restored from __doc__
        """ dup_password(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def folder_created(self, folder_info): # real signature unknown; restored from __doc__
        """ folder_created(self, folder_info:Camel.FolderInfo) """
        pass

    def folder_deleted(self, folder_info): # real signature unknown; restored from __doc__
        """ folder_deleted(self, folder_info:Camel.FolderInfo) """
        pass

    def folder_info_stale(self): # real signature unknown; restored from __doc__
        """ folder_info_stale(self) """
        pass

    def folder_opened(self, folder): # real signature unknown; restored from __doc__
        """ folder_opened(self, folder:Camel.Folder) """
        pass

    def folder_renamed(self, old_name, folder_info): # real signature unknown; restored from __doc__
        """ folder_renamed(self, old_name:str, folder_info:Camel.FolderInfo) """
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
        """ get_connection_status(self) -> Camel.ServiceConnectionStatus """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_db(self): # real signature unknown; restored from __doc__
        """ get_db(self) -> Camel.DB """
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_folder(self, folder_name, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_folder(self, folder_name:str, flags:Camel.StoreGetFolderFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_folders_bag(self): # real signature unknown; restored from __doc__
        """ get_folders_bag(self) -> Camel.ObjectBag """
        pass

    def get_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ get_folder_finish(self, result:Gio.AsyncResult) -> Camel.Folder or None """
        pass

    def get_folder_info(self, top=None, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_folder_info(self, top:str=None, flags:Camel.StoreGetFolderInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_folder_info_finish(self, result): # real signature unknown; restored from __doc__
        """ get_folder_info_finish(self, result:Gio.AsyncResult) -> Camel.FolderInfo or None """
        pass

    def get_folder_info_sync(self, top=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ get_folder_info_sync(self, top:str=None, flags:Camel.StoreGetFolderInfoFlags, cancellable:Gio.Cancellable=None) -> Camel.FolderInfo or None """
        pass

    def get_folder_sync(self, folder_name, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ get_folder_sync(self, folder_name:str, flags:Camel.StoreGetFolderFlags, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def get_inbox_folder(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_inbox_folder(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_inbox_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ get_inbox_folder_finish(self, result:Gio.AsyncResult) -> Camel.Folder or None """
        pass

    def get_inbox_folder_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_inbox_folder_sync(self, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def get_junk_folder(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_junk_folder(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_junk_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ get_junk_folder_finish(self, result:Gio.AsyncResult) -> Camel.Folder or None """
        pass

    def get_junk_folder_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_junk_folder_sync(self, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def get_name(self, brief): # real signature unknown; restored from __doc__
        """ get_name(self, brief:bool) -> str """
        return ""

    def get_online(self): # real signature unknown; restored from __doc__
        """ get_online(self) -> bool """
        return False

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str """
        return ""

    def get_permissions(self): # real signature unknown; restored from __doc__
        """ get_permissions(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_provider(self): # real signature unknown; restored from __doc__
        """ get_provider(self) -> Camel.Provider """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_state_filename(self): # real signature unknown; restored from __doc__
        """ get_state_filename(self) -> str """
        return ""

    def get_trash_folder(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_trash_folder(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_trash_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ get_trash_folder_finish(self, result:Gio.AsyncResult) -> Camel.Folder or None """
        pass

    def get_trash_folder_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_trash_folder_sync(self, cancellable:Gio.Cancellable=None) -> Camel.Folder or None """
        pass

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def get_user_cache_dir(self): # real signature unknown; restored from __doc__
        """ get_user_cache_dir(self) -> str """
        return ""

    def get_user_data_dir(self): # real signature unknown; restored from __doc__
        """ get_user_data_dir(self) -> str """
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

    def initial_setup(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ initial_setup(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def initial_setup_finish(self, result): # real signature unknown; restored from __doc__
        """ initial_setup_finish(self, result:Gio.AsyncResult) -> bool, out_save_setup:dict """
        return False

    def initial_setup_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ initial_setup_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_save_setup:dict """
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

    def maybe_run_db_maintenance(self): # real signature unknown; restored from __doc__
        """ maybe_run_db_maintenance(self) -> bool """
        return False

    def migrate_files(self): # real signature unknown; restored from __doc__
        """ migrate_files(self) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_camel_url(self): # real signature unknown; restored from __doc__
        """ new_camel_url(self) -> Camel.URL """
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

    def prepare_for_offline_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ prepare_for_offline_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def query_auth_types(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_auth_types(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_auth_types_finish(self, result): # real signature unknown; restored from __doc__
        """ query_auth_types_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def query_auth_types_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_auth_types_sync(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def queue_task(self, task, task_func): # real signature unknown; restored from __doc__
        """ queue_task(self, task:Gio.Task, task_func:Gio.TaskThreadFunc) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_proxy_resolver(self): # real signature unknown; restored from __doc__
        """ ref_proxy_resolver(self) -> Gio.ProxyResolver """
        pass

    def ref_session(self): # real signature unknown; restored from __doc__
        """ ref_session(self) -> Camel.Session """
        pass

    def ref_settings(self): # real signature unknown; restored from __doc__
        """ ref_settings(self) -> Camel.Settings """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def rename_folder(self, old_name, new_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ rename_folder(self, old_name:str, new_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def rename_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ rename_folder_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def rename_folder_sync(self, old_name, new_name, cancellable=None): # real signature unknown; restored from __doc__
        """ rename_folder_sync(self, old_name:str, new_name:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def requires_downsync(self): # real signature unknown; restored from __doc__
        """ requires_downsync(self) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_display_name(self, display_name): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:int) """
        pass

    def set_online(self, online, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_online(self, online:bool, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_online_finish(self, result): # real signature unknown; restored from __doc__
        """ set_online_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_online_sync(self, online, cancellable=None): # real signature unknown; restored from __doc__
        """ set_online_sync(self, online:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_password(self, password): # real signature unknown; restored from __doc__
        """ set_password(self, password:str) """
        pass

    def set_permissions(self, permissions): # real signature unknown; restored from __doc__
        """ set_permissions(self, permissions:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_proxy_resolver(self, proxy_resolver): # real signature unknown; restored from __doc__
        """ set_proxy_resolver(self, proxy_resolver:Gio.ProxyResolver) """
        pass

    def set_settings(self, settings): # real signature unknown; restored from __doc__
        """ set_settings(self, settings:Camel.Settings) """
        pass

    def set_state_filename(self, state_filename): # real signature unknown; restored from __doc__
        """ set_state_filename(self, state_filename:str) """
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

    def synchronize_sync(self, expunge, cancellable=None): # real signature unknown; restored from __doc__
        """ synchronize_sync(self, expunge:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7b34a0b2b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(OfflineStore), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelOfflineStore (94124524071504)>, '__doc__': None, '__gsignals__': {}, 'dup_downsync_folders': gi.FunctionInfo(dup_downsync_folders), 'get_online': gi.FunctionInfo(get_online), 'prepare_for_offline_sync': gi.FunctionInfo(prepare_for_offline_sync), 'requires_downsync': gi.FunctionInfo(requires_downsync), 'set_online': gi.FunctionInfo(set_online), 'set_online_finish': gi.FunctionInfo(set_online_finish), 'set_online_sync': gi.FunctionInfo(set_online_sync), 'do_dup_downsync_folders': gi.VFuncInfo(dup_downsync_folders), 'parent': <property object at 0x7f7b34f2de50>, 'priv': <property object at 0x7f7b34f2df90>})"
    __gdoc__ = 'Object CamelOfflineStore\n\nProperties from CamelOfflineStore:\n  online -> gboolean: Online\n    Whether the store is online\n\nSignals from CamelStore:\n  folder-created (CamelFolderInfo)\n  folder-deleted (CamelFolderInfo)\n  folder-info-stale ()\n  folder-opened (CamelFolder)\n  folder-renamed (gchararray, CamelFolderInfo)\n\nProperties from CamelService:\n  connection-status -> CamelServiceConnectionStatus: Connection Status\n    The connection status for the service\n  display-name -> gchararray: Display Name\n    The display name for the service\n  password -> gchararray: Password\n    The password for the service\n  provider -> CamelProvider: Provider\n    The CamelProvider for the service\n  proxy-resolver -> GProxyResolver: Proxy Resolver\n    The proxy resolver for the service\n  session -> CamelSession: Session\n    A CamelSession instance\n  settings -> CamelSettings: Settings\n    A CamelSettings instance\n  uid -> gchararray: UID\n    The unique identity of the service\n\nProperties from CamelObject:\n  state-filename -> gchararray: State Filename\n    File containing persistent property values\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelOfflineStore (94124524071504)>'
    __info__ = ObjectInfo(OfflineStore)


