# encoding: utf-8
# module gi.repository.PackageKitGlib
# from /usr/lib64/girepository-1.0/PackageKitGlib-1.0.typelib
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
import gobject as __gobject


from .Client import Client

class Task(Client):
    """
    :Constructors:
    
    ::
    
        Task(**properties)
        new() -> PackageKitGlib.Task
    """
    def accept_eula(self, eula_id, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ accept_eula(self, eula_id:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def accept_eula_async(self, eula_id, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ accept_eula_async(self, eula_id:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def adopt(self, transaction_id, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ adopt(self, transaction_id:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def adopt_async(self, transaction_id, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ adopt_async(self, transaction_id:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def create_helper_argv_envp(self, argv, envp_out): # real signature unknown; restored from __doc__
        """ create_helper_argv_envp(argv:str, envp_out:str) -> bool """
        return False

    def depends_on(self, filters, package_ids, recursive, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ depends_on(self, filters:int, package_ids:list, recursive:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def depends_on_async(self, filters, package_ids, recursive, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ depends_on_async(self, filters:int, package_ids:list, recursive:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def depends_on_sync(self, filters, package_ids, recursive, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ depends_on_sync(self, filters:int, package_ids:list, recursive:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def download_packages(self, package_ids, directory, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ download_packages(self, package_ids:list, directory:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def download_packages_async(self, package_ids, directory, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ download_packages_async(self, package_ids:list, directory:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def download_packages_sync(self, package_ids, directory, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ download_packages_sync(self, package_ids:list, directory:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_eula_question(self, *args, **kwargs): # real signature unknown
        """ eula_question(self, request:int, results:PackageKitGlib.Results) """
        pass

    def do_key_question(self, *args, **kwargs): # real signature unknown
        """ key_question(self, request:int, results:PackageKitGlib.Results) """
        pass

    def do_media_change_question(self, *args, **kwargs): # real signature unknown
        """ media_change_question(self, request:int, results:PackageKitGlib.Results) """
        pass

    def do_repair_question(self, *args, **kwargs): # real signature unknown
        """ repair_question(self, request:int, results:PackageKitGlib.Results) """
        pass

    def do_simulate_question(self, *args, **kwargs): # real signature unknown
        """ simulate_question(self, request:int, results:PackageKitGlib.Results) """
        pass

    def do_untrusted_question(self, *args, **kwargs): # real signature unknown
        """ untrusted_question(self, request:int, results:PackageKitGlib.Results) """
        pass

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

    def generic_finish(self, res): # real signature unknown; restored from __doc__
        """ generic_finish(self, res:Gio.AsyncResult) -> PackageKitGlib.Results """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_allow_downgrade(self): # real signature unknown; restored from __doc__
        """ get_allow_downgrade(self) -> bool """
        return False

    def get_allow_reinstall(self): # real signature unknown; restored from __doc__
        """ get_allow_reinstall(self) -> bool """
        return False

    def get_background(self): # real signature unknown; restored from __doc__
        """ get_background(self) -> bool """
        return False

    def get_cache_age(self): # real signature unknown; restored from __doc__
        """ get_cache_age(self) -> int """
        return 0

    def get_categories(self, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_categories(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_categories_async(self, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_categories_async(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_categories_sync(self, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_categories_sync(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_details(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_details(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_details_async(self, package_ids, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_details_async(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_details_local(self, files, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_details_local(self, files:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_details_local_async(self, files, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_details_local_async(self, files:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_details_sync(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_details_sync(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_distro_upgrades(self, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_distro_upgrades(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_distro_upgrades_async(self, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_distro_upgrades_async(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_files(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_files(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_files_async(self, package_ids, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_files_async(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_files_local(self, files, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_files_local(self, files:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_files_local_async(self, files, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_files_local_async(self, files:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_files_sync(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_files_sync(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_idle(self): # real signature unknown; restored from __doc__
        """ get_idle(self) -> bool """
        return False

    def get_interactive(self): # real signature unknown; restored from __doc__
        """ get_interactive(self) -> bool """
        return False

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str """
        return ""

    def get_old_transactions(self, number, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_old_transactions(self, number:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_old_transactions_async(self, number, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_old_transactions_async(self, number:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_only_download(self): # real signature unknown; restored from __doc__
        """ get_only_download(self) -> bool """
        return False

    def get_only_trusted(self): # real signature unknown; restored from __doc__
        """ get_only_trusted(self) -> bool """
        return False

    def get_packages(self, filters, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_packages(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_packages_async(self, filters, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_packages_async(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_packages_sync(self, filters, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_packages_sync(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_progress(self, transaction_id, cancellable=None): # real signature unknown; restored from __doc__
        """ get_progress(self, transaction_id:str, cancellable:Gio.Cancellable=None) -> PackageKitGlib.Progress """
        pass

    def get_progress_async(self, transaction_id, cancellable=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_progress_async(self, transaction_id:str, cancellable:Gio.Cancellable=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_progress_finish(self, res): # real signature unknown; restored from __doc__
        """ get_progress_finish(self, res:Gio.AsyncResult) -> PackageKitGlib.Progress """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_repo_list(self, filters, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_repo_list(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_repo_list_async(self, filters, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_repo_list_async(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_repo_list_sync(self, filters, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_repo_list_sync(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_simulate(self): # real signature unknown; restored from __doc__
        """ get_simulate(self) -> bool """
        return False

    def get_updates(self, filters, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_updates(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_updates_async(self, filters, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_updates_async(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_updates_sync(self, filters, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_updates_sync(self, filters:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_update_detail(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_update_detail(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def get_update_detail_async(self, package_ids, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_update_detail_async(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_update_detail_sync(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ get_update_detail_sync(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
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

    def install_files(self, transaction_flags, files, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ install_files(self, transaction_flags:int, files:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def install_files_async(self, files, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ install_files_async(self, files:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def install_files_sync(self, files, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ install_files_sync(self, files:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def install_packages(self, transaction_flags, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ install_packages(self, transaction_flags:int, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def install_packages_async(self, package_ids, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ install_packages_async(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def install_packages_sync(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ install_packages_sync(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_signature(self, type, key_id, package_id, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ install_signature(self, type:PackageKitGlib.SigTypeEnum, key_id:str, package_id:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def install_signature_async(self, type, key_id, package_id, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ install_signature_async(self, type:PackageKitGlib.SigTypeEnum, key_id:str, package_id:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> PackageKitGlib.Task """
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

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh_cache(self, force, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ refresh_cache(self, force:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def refresh_cache_async(self, force, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ refresh_cache_async(self, force:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def refresh_cache_sync(self, force, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ refresh_cache_sync(self, force:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_packages(self, transaction_flags, package_ids, allow_deps, autoremove, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ remove_packages(self, transaction_flags:int, package_ids:list, allow_deps:bool, autoremove:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def remove_packages_async(self, package_ids, allow_deps, autoremove, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_packages_async(self, package_ids:list, allow_deps:bool, autoremove:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_packages_sync(self, package_ids, allow_deps, autoremove, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ remove_packages_sync(self, package_ids:list, allow_deps:bool, autoremove:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def repair_system(self, transaction_flags, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ repair_system(self, transaction_flags:int, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def repair_system_async(self, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ repair_system_async(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def repair_system_sync(self, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ repair_system_sync(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def repo_enable(self, repo_id, enabled, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ repo_enable(self, repo_id:str, enabled:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def repo_enable_async(self, repo_id, enabled, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ repo_enable_async(self, repo_id:str, enabled:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def repo_enable_sync(self, repo_id, enabled, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ repo_enable_sync(self, repo_id:str, enabled:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def repo_remove(self, transaction_flags, repo_id, autoremove, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ repo_remove(self, transaction_flags:int, repo_id:str, autoremove:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def repo_remove_async(self, transaction_flags, repo_id, autoremove, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ repo_remove_async(self, transaction_flags:int, repo_id:str, autoremove:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def repo_set_data(self, repo_id, parameter, value, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ repo_set_data(self, repo_id:str, parameter:str, value:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def repo_set_data_async(self, repo_id, parameter, value, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ repo_set_data_async(self, repo_id:str, parameter:str, value:str, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def required_by(self, filters, package_ids, recursive, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ required_by(self, filters:int, package_ids:list, recursive:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def required_by_async(self, filters, package_ids, recursive, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ required_by_async(self, filters:int, package_ids:list, recursive:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def required_by_sync(self, filters, package_ids, recursive, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ required_by_sync(self, filters:int, package_ids:list, recursive:bool, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def resolve(self, filters, packages, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ resolve(self, filters:int, packages:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def resolve_async(self, filters, packages, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ resolve_async(self, filters:int, packages:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def resolve_sync(self, filters, packages, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ resolve_sync(self, filters:int, packages:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def search_details(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_details(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def search_details_async(self, filters, values, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ search_details_async(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def search_details_sync(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_details_sync(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def search_files(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_files(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def search_files_async(self, filters, values, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ search_files_async(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def search_files_sync(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_files_sync(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def search_groups(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_groups(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def search_groups_async(self, filters, values, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ search_groups_async(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def search_groups_sync(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_groups_sync(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def search_names(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_names(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def search_names_async(self, filters, values, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ search_names_async(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def search_names_sync(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ search_names_sync(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def set_allow_downgrade(self, allow_downgrade): # real signature unknown; restored from __doc__
        """ set_allow_downgrade(self, allow_downgrade:bool) """
        pass

    def set_allow_reinstall(self, allow_reinstall): # real signature unknown; restored from __doc__
        """ set_allow_reinstall(self, allow_reinstall:bool) """
        pass

    def set_background(self, background): # real signature unknown; restored from __doc__
        """ set_background(self, background:bool) """
        pass

    def set_cache_age(self, cache_age): # real signature unknown; restored from __doc__
        """ set_cache_age(self, cache_age:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_interactive(self, interactive): # real signature unknown; restored from __doc__
        """ set_interactive(self, interactive:bool) """
        pass

    def set_locale(self, locale): # real signature unknown; restored from __doc__
        """ set_locale(self, locale:str) """
        pass

    def set_only_download(self, only_download): # real signature unknown; restored from __doc__
        """ set_only_download(self, only_download:bool) """
        pass

    def set_only_trusted(self, only_trusted): # real signature unknown; restored from __doc__
        """ set_only_trusted(self, only_trusted:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_simulate(self, simulate): # real signature unknown; restored from __doc__
        """ set_simulate(self, simulate:bool) """
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

    def update_packages(self, transaction_flags, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ update_packages(self, transaction_flags:int, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def update_packages_async(self, package_ids, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ update_packages_async(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def update_packages_sync(self, package_ids, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ update_packages_sync(self, package_ids:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def upgrade_system(self, transaction_flags, distro_id, upgrade_kind, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ upgrade_system(self, transaction_flags:int, distro_id:str, upgrade_kind:PackageKitGlib.UpgradeKindEnum, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def upgrade_system_async(self, distro_id, upgrade_kind, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ upgrade_system_async(self, distro_id:str, upgrade_kind:PackageKitGlib.UpgradeKindEnum, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def upgrade_system_sync(self, distro_id, upgrade_kind, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ upgrade_system_sync(self, distro_id:str, upgrade_kind:PackageKitGlib.UpgradeKindEnum, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def user_accepted(self, request): # real signature unknown; restored from __doc__
        """ user_accepted(self, request:int) -> bool """
        return False

    def user_declined(self, request): # real signature unknown; restored from __doc__
        """ user_declined(self, request:int) -> bool """
        return False

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def what_provides(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ what_provides(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
        pass

    def what_provides_async(self, filters, values, cancellable=None, progress_callback, progress_user_data=None, callback_ready=None, user_data=None): # real signature unknown; restored from __doc__
        """ what_provides_async(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback_ready:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def what_provides_sync(self, filters, values, cancellable=None, progress_callback, progress_user_data=None): # real signature unknown; restored from __doc__
        """ what_provides_sync(self, filters:int, values:list, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None) -> PackageKitGlib.Results """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f121f817610>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Task), '__module__': 'gi.repository.PackageKitGlib', '__gtype__': <GType PkTask (94016447474256)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'depends_on_async': gi.FunctionInfo(depends_on_async), 'depends_on_sync': gi.FunctionInfo(depends_on_sync), 'download_packages_async': gi.FunctionInfo(download_packages_async), 'download_packages_sync': gi.FunctionInfo(download_packages_sync), 'generic_finish': gi.FunctionInfo(generic_finish), 'get_allow_downgrade': gi.FunctionInfo(get_allow_downgrade), 'get_allow_reinstall': gi.FunctionInfo(get_allow_reinstall), 'get_categories_async': gi.FunctionInfo(get_categories_async), 'get_categories_sync': gi.FunctionInfo(get_categories_sync), 'get_details_async': gi.FunctionInfo(get_details_async), 'get_details_sync': gi.FunctionInfo(get_details_sync), 'get_files_async': gi.FunctionInfo(get_files_async), 'get_files_sync': gi.FunctionInfo(get_files_sync), 'get_only_download': gi.FunctionInfo(get_only_download), 'get_only_trusted': gi.FunctionInfo(get_only_trusted), 'get_packages_async': gi.FunctionInfo(get_packages_async), 'get_packages_sync': gi.FunctionInfo(get_packages_sync), 'get_repo_list_async': gi.FunctionInfo(get_repo_list_async), 'get_repo_list_sync': gi.FunctionInfo(get_repo_list_sync), 'get_simulate': gi.FunctionInfo(get_simulate), 'get_update_detail_async': gi.FunctionInfo(get_update_detail_async), 'get_update_detail_sync': gi.FunctionInfo(get_update_detail_sync), 'get_updates_async': gi.FunctionInfo(get_updates_async), 'get_updates_sync': gi.FunctionInfo(get_updates_sync), 'install_files_async': gi.FunctionInfo(install_files_async), 'install_files_sync': gi.FunctionInfo(install_files_sync), 'install_packages_async': gi.FunctionInfo(install_packages_async), 'install_packages_sync': gi.FunctionInfo(install_packages_sync), 'refresh_cache_async': gi.FunctionInfo(refresh_cache_async), 'refresh_cache_sync': gi.FunctionInfo(refresh_cache_sync), 'remove_packages_async': gi.FunctionInfo(remove_packages_async), 'remove_packages_sync': gi.FunctionInfo(remove_packages_sync), 'repair_system_async': gi.FunctionInfo(repair_system_async), 'repair_system_sync': gi.FunctionInfo(repair_system_sync), 'repo_enable_async': gi.FunctionInfo(repo_enable_async), 'repo_enable_sync': gi.FunctionInfo(repo_enable_sync), 'required_by_async': gi.FunctionInfo(required_by_async), 'required_by_sync': gi.FunctionInfo(required_by_sync), 'resolve_async': gi.FunctionInfo(resolve_async), 'resolve_sync': gi.FunctionInfo(resolve_sync), 'search_details_async': gi.FunctionInfo(search_details_async), 'search_details_sync': gi.FunctionInfo(search_details_sync), 'search_files_async': gi.FunctionInfo(search_files_async), 'search_files_sync': gi.FunctionInfo(search_files_sync), 'search_groups_async': gi.FunctionInfo(search_groups_async), 'search_groups_sync': gi.FunctionInfo(search_groups_sync), 'search_names_async': gi.FunctionInfo(search_names_async), 'search_names_sync': gi.FunctionInfo(search_names_sync), 'set_allow_downgrade': gi.FunctionInfo(set_allow_downgrade), 'set_allow_reinstall': gi.FunctionInfo(set_allow_reinstall), 'set_only_download': gi.FunctionInfo(set_only_download), 'set_only_trusted': gi.FunctionInfo(set_only_trusted), 'set_simulate': gi.FunctionInfo(set_simulate), 'update_packages_async': gi.FunctionInfo(update_packages_async), 'update_packages_sync': gi.FunctionInfo(update_packages_sync), 'upgrade_system_async': gi.FunctionInfo(upgrade_system_async), 'upgrade_system_sync': gi.FunctionInfo(upgrade_system_sync), 'user_accepted': gi.FunctionInfo(user_accepted), 'user_declined': gi.FunctionInfo(user_declined), 'what_provides_async': gi.FunctionInfo(what_provides_async), 'what_provides_sync': gi.FunctionInfo(what_provides_sync), 'do_eula_question': gi.VFuncInfo(eula_question), 'do_key_question': gi.VFuncInfo(key_question), 'do_media_change_question': gi.VFuncInfo(media_change_question), 'do_repair_question': gi.VFuncInfo(repair_question), 'do_simulate_question': gi.VFuncInfo(simulate_question), 'do_untrusted_question': gi.VFuncInfo(untrusted_question), 'parent': <property object at 0x7f121f9056d0>, 'priv': <property object at 0x7f121f905860>})"
    __gdoc__ = 'Object PkTask\n\nProperties from PkTask:\n  simulate -> gboolean: simulate\n  only-download -> gboolean: only-download\n  only-trusted -> gboolean: only-trusted\n  allow-reinstall -> gboolean: allow-reinstall\n  allow-downgrade -> gboolean: allow-downgrade\n\nProperties from PkClient:\n  locale -> gchararray: locale\n  background -> gboolean: background\n  interactive -> gboolean: interactive\n  idle -> gboolean: idle\n    if there are no transactions in progress on this client\n  cache-age -> guint: cache-age\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PkTask (94016447474256)>'
    __info__ = ObjectInfo(Task)


