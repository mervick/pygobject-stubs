# encoding: utf-8
# module gi.repository.OSTree
# from /usr/lib64/girepository-1.0/OSTree-1.0.typelib
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


class Repo(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Repo(**properties)
        new(path:Gio.File) -> OSTree.Repo
        new_default() -> OSTree.Repo
        new_for_sysroot_path(repo_path:Gio.File, sysroot_path:Gio.File) -> OSTree.Repo
    """
    def abort_transaction(self, cancellable=None): # real signature unknown; restored from __doc__
        """ abort_transaction(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def add_gpg_signature_summary(self, key_id, homedir=None, cancellable=None): # real signature unknown; restored from __doc__
        """ add_gpg_signature_summary(self, key_id:list, homedir:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def append_gpg_signature(self, commit_checksum, signature_bytes, cancellable=None): # real signature unknown; restored from __doc__
        """ append_gpg_signature(self, commit_checksum:str, signature_bytes:GLib.Bytes, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def checkout_at(self, options=None, destination_dfd, destination_path, commit, cancellable=None): # real signature unknown; restored from __doc__
        """ checkout_at(self, options:OSTree.RepoCheckoutAtOptions=None, destination_dfd:int, destination_path:str, commit:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def checkout_gc(self, cancellable=None): # real signature unknown; restored from __doc__
        """ checkout_gc(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def checkout_tree(self, mode, overwrite_mode, destination, source, source_info, cancellable=None): # real signature unknown; restored from __doc__
        """ checkout_tree(self, mode:OSTree.RepoCheckoutMode, overwrite_mode:OSTree.RepoCheckoutOverwriteMode, destination:Gio.File, source:OSTree.RepoFile, source_info:Gio.FileInfo, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def commit_transaction(self, cancellable=None): # real signature unknown; restored from __doc__
        """ commit_transaction(self, cancellable:Gio.Cancellable=None) -> bool, out_stats:OSTree.RepoTransactionStats """
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

    def copy_config(self): # real signature unknown; restored from __doc__
        """ copy_config(self) -> GLib.KeyFile """
        pass

    def create(self, mode, cancellable=None): # real signature unknown; restored from __doc__
        """ create(self, mode:OSTree.RepoMode, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def create_at(self, dfd, path, mode, options, cancellable=None): # real signature unknown; restored from __doc__
        """ create_at(dfd:int, path:str, mode:OSTree.RepoMode, options:GLib.Variant, cancellable:Gio.Cancellable=None) -> OSTree.Repo """
        pass

    def delete_object(self, objtype, sha256, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_object(self, objtype:OSTree.ObjectType, sha256:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:OSTree.Repo) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_remotes_async(self, refs, options=None, finders, progress=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_remotes_async(self, refs:list, options:GLib.Variant=None, finders:list, progress:OSTree.AsyncProgress=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_remotes_finish(self, result): # real signature unknown; restored from __doc__
        """ find_remotes_finish(self, result:Gio.AsyncResult) -> list """
        return []

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

    def fsck_object(self, objtype, sha256, cancellable=None): # real signature unknown; restored from __doc__
        """ fsck_object(self, objtype:OSTree.ObjectType, sha256:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_bootloader(self): # real signature unknown; restored from __doc__
        """ get_bootloader(self) -> str """
        return ""

    def get_collection_id(self): # real signature unknown; restored from __doc__
        """ get_collection_id(self) -> str or None """
        return ""

    def get_config(self): # real signature unknown; restored from __doc__
        """ get_config(self) -> GLib.KeyFile """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_repo_finders(self): # real signature unknown; restored from __doc__
        """ get_default_repo_finders(self) -> list """
        return []

    def get_dfd(self): # real signature unknown; restored from __doc__
        """ get_dfd(self) -> int """
        return 0

    def get_disable_fsync(self): # real signature unknown; restored from __doc__
        """ get_disable_fsync(self) -> bool """
        return False

    def get_min_free_space_bytes(self): # real signature unknown; restored from __doc__
        """ get_min_free_space_bytes(self) -> bool, out_reserved_bytes:int """
        return False

    def get_mode(self): # real signature unknown; restored from __doc__
        """ get_mode(self) -> OSTree.RepoMode """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> OSTree.Repo """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gio.File """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_boolean_option(self, remote_name, option_name, default_value): # real signature unknown; restored from __doc__
        """ get_remote_boolean_option(self, remote_name:str, option_name:str, default_value:bool) -> bool, out_value:bool """
        return False

    def get_remote_list_option(self, remote_name, option_name): # real signature unknown; restored from __doc__
        """ get_remote_list_option(self, remote_name:str, option_name:str) -> bool, out_value:list """
        return False

    def get_remote_option(self, remote_name, option_name, default_value=None): # real signature unknown; restored from __doc__
        """ get_remote_option(self, remote_name:str, option_name:str, default_value:str=None) -> bool, out_value:str """
        return False

    def gpg_verify_data(self, remote_name=None, data, signatures, keyringdir=None, extra_keyring=None, cancellable=None): # real signature unknown; restored from __doc__
        """ gpg_verify_data(self, remote_name:str=None, data:GLib.Bytes, signatures:GLib.Bytes, keyringdir:Gio.File=None, extra_keyring:Gio.File=None, cancellable:Gio.Cancellable=None) -> OSTree.GpgVerifyResult """
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

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def has_object(self, objtype, checksum, cancellable=None): # real signature unknown; restored from __doc__
        """ has_object(self, objtype:OSTree.ObjectType, checksum:str, cancellable:Gio.Cancellable=None) -> bool, out_have_object:bool """
        return False

    def import_object_from(self, source, objtype, checksum, cancellable=None): # real signature unknown; restored from __doc__
        """ import_object_from(self, source:OSTree.Repo, objtype:OSTree.ObjectType, checksum:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def import_object_from_with_trust(self, source, objtype, checksum, trusted, cancellable=None): # real signature unknown; restored from __doc__
        """ import_object_from_with_trust(self, source:OSTree.Repo, objtype:OSTree.ObjectType, checksum:str, trusted:bool, cancellable:Gio.Cancellable=None) -> bool """
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

    def is_system(self): # real signature unknown; restored from __doc__
        """ is_system(self) -> bool """
        return False

    def is_writable(self): # real signature unknown; restored from __doc__
        """ is_writable(self) -> bool """
        return False

    def list_collection_refs(self, match_collection_id=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ list_collection_refs(self, match_collection_id:str=None, flags:OSTree.RepoListRefsExtFlags, cancellable:Gio.Cancellable=None) -> bool, out_all_refs:dict """
        return False

    def list_commit_objects_starting_with(self, start, cancellable=None): # real signature unknown; restored from __doc__
        """ list_commit_objects_starting_with(self, start:str, cancellable:Gio.Cancellable=None) -> bool, out_commits:dict """
        return False

    def list_objects(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ list_objects(self, flags:OSTree.RepoListObjectsFlags, cancellable:Gio.Cancellable=None) -> bool, out_objects:dict """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_refs(self, refspec_prefix=None, cancellable=None): # real signature unknown; restored from __doc__
        """ list_refs(self, refspec_prefix:str=None, cancellable:Gio.Cancellable=None) -> bool, out_all_refs:dict """
        return False

    def list_refs_ext(self, refspec_prefix=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ list_refs_ext(self, refspec_prefix:str=None, flags:OSTree.RepoListRefsExtFlags, cancellable:Gio.Cancellable=None) -> bool, out_all_refs:dict """
        return False

    def list_static_delta_names(self, cancellable=None): # real signature unknown; restored from __doc__
        """ list_static_delta_names(self, cancellable:Gio.Cancellable=None) -> bool, out_deltas:list """
        return False

    def load_commit(self, checksum): # real signature unknown; restored from __doc__
        """ load_commit(self, checksum:str) -> bool, out_commit:GLib.Variant, out_state:OSTree.RepoCommitState """
        return False

    def load_file(self, checksum, cancellable=None): # real signature unknown; restored from __doc__
        """ load_file(self, checksum:str, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream, out_file_info:Gio.FileInfo, out_xattrs:GLib.Variant """
        return False

    def load_object_stream(self, objtype, checksum, cancellable=None): # real signature unknown; restored from __doc__
        """ load_object_stream(self, objtype:OSTree.ObjectType, checksum:str, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream, out_size:int """
        return False

    def load_variant(self, objtype, sha256): # real signature unknown; restored from __doc__
        """ load_variant(self, objtype:OSTree.ObjectType, sha256:str) -> bool, out_variant:GLib.Variant """
        return False

    def load_variant_if_exists(self, objtype, sha256): # real signature unknown; restored from __doc__
        """ load_variant_if_exists(self, objtype:OSTree.ObjectType, sha256:str) -> bool, out_variant:GLib.Variant """
        return False

    def mark_commit_partial(self, checksum, is_partial): # real signature unknown; restored from __doc__
        """ mark_commit_partial(self, checksum:str, is_partial:bool) -> bool """
        return False

    def mark_commit_partial_reason(self, checksum, is_partial, in_state): # real signature unknown; restored from __doc__
        """ mark_commit_partial_reason(self, checksum:str, is_partial:bool, in_state:OSTree.RepoCommitState) -> bool """
        return False

    def mode_from_string(self, mode): # real signature unknown; restored from __doc__
        """ mode_from_string(mode:str) -> bool, out_mode:OSTree.RepoMode """
        return False

    def new(self, path): # real signature unknown; restored from __doc__
        """ new(path:Gio.File) -> OSTree.Repo """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_default(self): # real signature unknown; restored from __doc__
        """ new_default() -> OSTree.Repo """
        pass

    def new_for_sysroot_path(self, repo_path, sysroot_path): # real signature unknown; restored from __doc__
        """ new_for_sysroot_path(repo_path:Gio.File, sysroot_path:Gio.File) -> OSTree.Repo """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def open_at(self, dfd, path, cancellable=None): # real signature unknown; restored from __doc__
        """ open_at(dfd:int, path:str, cancellable:Gio.Cancellable=None) -> OSTree.Repo """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def prepare_transaction(self, cancellable=None): # real signature unknown; restored from __doc__
        """ prepare_transaction(self, cancellable:Gio.Cancellable=None) -> bool, out_transaction_resume:bool """
        return False

    def prune(self, flags, depth, cancellable=None): # real signature unknown; restored from __doc__
        """ prune(self, flags:OSTree.RepoPruneFlags, depth:int, cancellable:Gio.Cancellable=None) -> bool, out_objects_total:int, out_objects_pruned:int, out_pruned_object_size_total:int """
        return False

    def prune_from_reachable(self, options, cancellable=None): # real signature unknown; restored from __doc__
        """ prune_from_reachable(self, options:OSTree.RepoPruneOptions, cancellable:Gio.Cancellable=None) -> bool, out_objects_total:int, out_objects_pruned:int, out_pruned_object_size_total:int """
        return False

    def prune_static_deltas(self, commit=None, cancellable=None): # real signature unknown; restored from __doc__
        """ prune_static_deltas(self, commit:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def pull(self, remote_name, refs_to_fetch=None, flags, progress=None, cancellable=None): # real signature unknown; restored from __doc__
        """ pull(self, remote_name:str, refs_to_fetch:list=None, flags:OSTree.RepoPullFlags, progress:OSTree.AsyncProgress=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def pull_default_console_progress_changed(self, progress, user_data=None): # real signature unknown; restored from __doc__
        """ pull_default_console_progress_changed(progress:OSTree.AsyncProgress, user_data=None) """
        pass

    def pull_from_remotes_async(self, results, options=None, progress=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ pull_from_remotes_async(self, results:list, options:GLib.Variant=None, progress:OSTree.AsyncProgress=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def pull_from_remotes_finish(self, result): # real signature unknown; restored from __doc__
        """ pull_from_remotes_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def pull_one_dir(self, remote_name, dir_to_pull, refs_to_fetch=None, flags, progress=None, cancellable=None): # real signature unknown; restored from __doc__
        """ pull_one_dir(self, remote_name:str, dir_to_pull:str, refs_to_fetch:list=None, flags:OSTree.RepoPullFlags, progress:OSTree.AsyncProgress=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def pull_with_options(self, remote_name_or_baseurl, options, progress=None, cancellable=None): # real signature unknown; restored from __doc__
        """ pull_with_options(self, remote_name_or_baseurl:str, options:GLib.Variant, progress:OSTree.AsyncProgress=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def query_object_storage_size(self, objtype, sha256, cancellable=None): # real signature unknown; restored from __doc__
        """ query_object_storage_size(self, objtype:OSTree.ObjectType, sha256:str, cancellable:Gio.Cancellable=None) -> bool, out_size:int """
        return False

    def read_commit(self, ref, cancellable=None): # real signature unknown; restored from __doc__
        """ read_commit(self, ref:str, cancellable:Gio.Cancellable=None) -> bool, out_root:Gio.File, out_commit:str """
        return False

    def read_commit_detached_metadata(self, checksum, cancellable=None): # real signature unknown; restored from __doc__
        """ read_commit_detached_metadata(self, checksum:str, cancellable:Gio.Cancellable=None) -> bool, out_metadata:GLib.Variant """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def regenerate_summary(self, additional_metadata=None, cancellable=None): # real signature unknown; restored from __doc__
        """ regenerate_summary(self, additional_metadata:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def reload_config(self, cancellable=None): # real signature unknown; restored from __doc__
        """ reload_config(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remote_add(self, name, url, options=None, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_add(self, name:str, url:str, options:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remote_change(self, sysroot=None, changeop, name, url, options=None, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_change(self, sysroot:Gio.File=None, changeop:OSTree.RepoRemoteChange, name:str, url:str, options:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remote_delete(self, name, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_delete(self, name:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remote_fetch_summary(self, name, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_fetch_summary(self, name:str, cancellable:Gio.Cancellable=None) -> bool, out_summary:GLib.Bytes, out_signatures:GLib.Bytes """
        return False

    def remote_fetch_summary_with_options(self, name, options=None, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_fetch_summary_with_options(self, name:str, options:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool, out_summary:GLib.Bytes, out_signatures:GLib.Bytes """
        return False

    def remote_get_gpg_verify(self, name): # real signature unknown; restored from __doc__
        """ remote_get_gpg_verify(self, name:str) -> bool, out_gpg_verify:bool """
        return False

    def remote_get_gpg_verify_summary(self, name): # real signature unknown; restored from __doc__
        """ remote_get_gpg_verify_summary(self, name:str) -> bool, out_gpg_verify_summary:bool """
        return False

    def remote_get_url(self, name): # real signature unknown; restored from __doc__
        """ remote_get_url(self, name:str) -> bool, out_url:str """
        return False

    def remote_gpg_import(self, name, source_stream=None, key_ids=None, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_gpg_import(self, name:str, source_stream:Gio.InputStream=None, key_ids:list=None, cancellable:Gio.Cancellable=None) -> bool, out_imported:int """
        return False

    def remote_list(self): # real signature unknown; restored from __doc__
        """ remote_list(self) -> list, out_n_remotes:int """
        return []

    def remote_list_collection_refs(self, remote_name, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_list_collection_refs(self, remote_name:str, cancellable:Gio.Cancellable=None) -> bool, out_all_refs:dict """
        return False

    def remote_list_refs(self, remote_name, cancellable=None): # real signature unknown; restored from __doc__
        """ remote_list_refs(self, remote_name:str, cancellable:Gio.Cancellable=None) -> bool, out_all_refs:dict """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def resolve_collection_ref(self, ref, allow_noent, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ resolve_collection_ref(self, ref:OSTree.CollectionRef, allow_noent:bool, flags:OSTree.RepoResolveRevExtFlags, cancellable:Gio.Cancellable=None) -> bool, out_rev:str """
        return False

    def resolve_keyring_for_collection(self, collection_id, cancellable=None): # real signature unknown; restored from __doc__
        """ resolve_keyring_for_collection(self, collection_id:str, cancellable:Gio.Cancellable=None) -> OSTree.Remote """
        pass

    def resolve_rev(self, refspec, allow_noent): # real signature unknown; restored from __doc__
        """ resolve_rev(self, refspec:str, allow_noent:bool) -> bool, out_rev:str """
        return False

    def resolve_rev_ext(self, refspec, allow_noent, flags): # real signature unknown; restored from __doc__
        """ resolve_rev_ext(self, refspec:str, allow_noent:bool, flags:OSTree.RepoResolveRevExtFlags) -> bool, out_rev:str """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scan_hardlinks(self, cancellable=None): # real signature unknown; restored from __doc__
        """ scan_hardlinks(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_alias_ref_immediate(self, remote=None, ref, target=None, cancellable=None): # real signature unknown; restored from __doc__
        """ set_alias_ref_immediate(self, remote:str=None, ref:str, target:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_cache_dir(self, dfd, path, cancellable=None): # real signature unknown; restored from __doc__
        """ set_cache_dir(self, dfd:int, path:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_collection_id(self, collection_id=None): # real signature unknown; restored from __doc__
        """ set_collection_id(self, collection_id:str=None) -> bool """
        return False

    def set_collection_ref_immediate(self, ref, checksum=None, cancellable=None): # real signature unknown; restored from __doc__
        """ set_collection_ref_immediate(self, ref:OSTree.CollectionRef, checksum:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_disable_fsync(self, disable_fsync): # real signature unknown; restored from __doc__
        """ set_disable_fsync(self, disable_fsync:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_ref_immediate(self, remote=None, ref, checksum=None, cancellable=None): # real signature unknown; restored from __doc__
        """ set_ref_immediate(self, remote:str=None, ref:str, checksum:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def sign_commit(self, commit_checksum, key_id, homedir=None, cancellable=None): # real signature unknown; restored from __doc__
        """ sign_commit(self, commit_checksum:str, key_id:str, homedir:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def sign_delta(self, from_commit, to_commit, key_id, homedir, cancellable=None): # real signature unknown; restored from __doc__
        """ sign_delta(self, from_commit:str, to_commit:str, key_id:str, homedir:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def static_delta_execute_offline(self, dir_or_file, skip_validation, cancellable=None): # real signature unknown; restored from __doc__
        """ static_delta_execute_offline(self, dir_or_file:Gio.File, skip_validation:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def static_delta_generate(self, opt, from_, to, metadata=None, params=None, cancellable=None): # real signature unknown; restored from __doc__
        """ static_delta_generate(self, opt:OSTree.StaticDeltaGenerateOpt, from_:str, to:str, metadata:GLib.Variant=None, params:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def transaction_set_collection_ref(self, ref, checksum=None): # real signature unknown; restored from __doc__
        """ transaction_set_collection_ref(self, ref:OSTree.CollectionRef, checksum:str=None) """
        pass

    def transaction_set_ref(self, remote=None, ref, checksum=None): # real signature unknown; restored from __doc__
        """ transaction_set_ref(self, remote:str=None, ref:str, checksum:str=None) """
        pass

    def transaction_set_refspec(self, refspec, checksum=None): # real signature unknown; restored from __doc__
        """ transaction_set_refspec(self, refspec:str, checksum:str=None) """
        pass

    def traverse_commit(self, commit_checksum, maxdepth, cancellable=None): # real signature unknown; restored from __doc__
        """ traverse_commit(self, commit_checksum:str, maxdepth:int, cancellable:Gio.Cancellable=None) -> bool, out_reachable:dict """
        return False

    def traverse_new_parents(self): # real signature unknown; restored from __doc__
        """ traverse_new_parents() -> dict """
        return {}

    def traverse_new_reachable(self): # real signature unknown; restored from __doc__
        """ traverse_new_reachable() -> dict """
        return {}

    def traverse_parents_get_commits(self, parents, p_object): # real signature unknown; restored from __doc__
        """ traverse_parents_get_commits(parents:dict, object:GLib.Variant) -> list """
        return []

    def traverse_reachable_refs(self, depth, reachable, cancellable=None): # real signature unknown; restored from __doc__
        """ traverse_reachable_refs(self, depth:int, reachable:dict, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def verify_commit(self, commit_checksum, keyringdir=None, extra_keyring=None, cancellable=None): # real signature unknown; restored from __doc__
        """ verify_commit(self, commit_checksum:str, keyringdir:Gio.File=None, extra_keyring:Gio.File=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def verify_commit_ext(self, commit_checksum, keyringdir=None, extra_keyring=None, cancellable=None): # real signature unknown; restored from __doc__
        """ verify_commit_ext(self, commit_checksum:str, keyringdir:Gio.File=None, extra_keyring:Gio.File=None, cancellable:Gio.Cancellable=None) -> OSTree.GpgVerifyResult """
        pass

    def verify_commit_for_remote(self, commit_checksum, remote_name, cancellable=None): # real signature unknown; restored from __doc__
        """ verify_commit_for_remote(self, commit_checksum:str, remote_name:str, cancellable:Gio.Cancellable=None) -> OSTree.GpgVerifyResult """
        pass

    def verify_summary(self, remote_name, summary, signatures, cancellable=None): # real signature unknown; restored from __doc__
        """ verify_summary(self, remote_name:str, summary:GLib.Bytes, signatures:GLib.Bytes, cancellable:Gio.Cancellable=None) -> OSTree.GpgVerifyResult """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write_archive_to_mtree(self, archive, mtree, modifier=None, autocreate_parents, cancellable=None): # real signature unknown; restored from __doc__
        """ write_archive_to_mtree(self, archive:Gio.File, mtree:OSTree.MutableTree, modifier:OSTree.RepoCommitModifier=None, autocreate_parents:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_archive_to_mtree_from_fd(self, fd, mtree, modifier=None, autocreate_parents, cancellable=None): # real signature unknown; restored from __doc__
        """ write_archive_to_mtree_from_fd(self, fd:int, mtree:OSTree.MutableTree, modifier:OSTree.RepoCommitModifier=None, autocreate_parents:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_commit(self, parent=None, subject=None, body=None, metadata=None, root, cancellable=None): # real signature unknown; restored from __doc__
        """ write_commit(self, parent:str=None, subject:str=None, body:str=None, metadata:GLib.Variant=None, root:OSTree.RepoFile, cancellable:Gio.Cancellable=None) -> bool, out_commit:str """
        return False

    def write_commit_detached_metadata(self, checksum, metadata=None, cancellable=None): # real signature unknown; restored from __doc__
        """ write_commit_detached_metadata(self, checksum:str, metadata:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_commit_with_time(self, parent=None, subject=None, body=None, metadata=None, root, time, cancellable=None): # real signature unknown; restored from __doc__
        """ write_commit_with_time(self, parent:str=None, subject:str=None, body:str=None, metadata:GLib.Variant=None, root:OSTree.RepoFile, time:int, cancellable:Gio.Cancellable=None) -> bool, out_commit:str """
        return False

    def write_config(self, new_config): # real signature unknown; restored from __doc__
        """ write_config(self, new_config:GLib.KeyFile) -> bool """
        return False

    def write_content(self, expected_checksum=None, object_input, length, cancellable=None): # real signature unknown; restored from __doc__
        """ write_content(self, expected_checksum:str=None, object_input:Gio.InputStream, length:int, cancellable:Gio.Cancellable=None) -> bool, out_csum:list """
        return False

    def write_content_async(self, expected_checksum=None, p_object, length, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write_content_async(self, expected_checksum:str=None, object:Gio.InputStream, length:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_content_finish(self, result): # real signature unknown; restored from __doc__
        """ write_content_finish(self, result:Gio.AsyncResult) -> bool, out_csum:int """
        return False

    def write_content_trusted(self, checksum, object_input, length, cancellable=None): # real signature unknown; restored from __doc__
        """ write_content_trusted(self, checksum:str, object_input:Gio.InputStream, length:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_dfd_to_mtree(self, dfd, path, mtree, modifier=None, cancellable=None): # real signature unknown; restored from __doc__
        """ write_dfd_to_mtree(self, dfd:int, path:str, mtree:OSTree.MutableTree, modifier:OSTree.RepoCommitModifier=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_directory_to_mtree(self, dir, mtree, modifier=None, cancellable=None): # real signature unknown; restored from __doc__
        """ write_directory_to_mtree(self, dir:Gio.File, mtree:OSTree.MutableTree, modifier:OSTree.RepoCommitModifier=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_metadata(self, objtype, expected_checksum=None, p_object, cancellable=None): # real signature unknown; restored from __doc__
        """ write_metadata(self, objtype:OSTree.ObjectType, expected_checksum:str=None, object:GLib.Variant, cancellable:Gio.Cancellable=None) -> bool, out_csum:list """
        return False

    def write_metadata_async(self, objtype, expected_checksum=None, p_object, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write_metadata_async(self, objtype:OSTree.ObjectType, expected_checksum:str=None, object:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_metadata_finish(self, result): # real signature unknown; restored from __doc__
        """ write_metadata_finish(self, result:Gio.AsyncResult) -> bool, out_csum:list """
        return False

    def write_metadata_stream_trusted(self, objtype, checksum, object_input, length, cancellable=None): # real signature unknown; restored from __doc__
        """ write_metadata_stream_trusted(self, objtype:OSTree.ObjectType, checksum:str, object_input:Gio.InputStream, length:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_metadata_trusted(self, objtype, checksum, variant, cancellable=None): # real signature unknown; restored from __doc__
        """ write_metadata_trusted(self, objtype:OSTree.ObjectType, checksum:str, variant:GLib.Variant, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_mtree(self, mtree, cancellable=None): # real signature unknown; restored from __doc__
        """ write_mtree(self, mtree:OSTree.MutableTree, cancellable:Gio.Cancellable=None) -> bool, out_file:Gio.File """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fecec292430>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Repo), '__module__': 'gi.repository.OSTree', '__gtype__': <GType OstreeRepo (94405993275248)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_default': gi.FunctionInfo(new_default), 'new_for_sysroot_path': gi.FunctionInfo(new_for_sysroot_path), 'create_at': gi.FunctionInfo(create_at), 'mode_from_string': gi.FunctionInfo(mode_from_string), 'open_at': gi.FunctionInfo(open_at), 'pull_default_console_progress_changed': gi.FunctionInfo(pull_default_console_progress_changed), 'traverse_new_parents': gi.FunctionInfo(traverse_new_parents), 'traverse_new_reachable': gi.FunctionInfo(traverse_new_reachable), 'traverse_parents_get_commits': gi.FunctionInfo(traverse_parents_get_commits), 'abort_transaction': gi.FunctionInfo(abort_transaction), 'add_gpg_signature_summary': gi.FunctionInfo(add_gpg_signature_summary), 'append_gpg_signature': gi.FunctionInfo(append_gpg_signature), 'checkout_at': gi.FunctionInfo(checkout_at), 'checkout_gc': gi.FunctionInfo(checkout_gc), 'checkout_tree': gi.FunctionInfo(checkout_tree), 'commit_transaction': gi.FunctionInfo(commit_transaction), 'copy_config': gi.FunctionInfo(copy_config), 'create': gi.FunctionInfo(create), 'delete_object': gi.FunctionInfo(delete_object), 'equal': gi.FunctionInfo(equal), 'find_remotes_async': gi.FunctionInfo(find_remotes_async), 'find_remotes_finish': gi.FunctionInfo(find_remotes_finish), 'fsck_object': gi.FunctionInfo(fsck_object), 'get_bootloader': gi.FunctionInfo(get_bootloader), 'get_collection_id': gi.FunctionInfo(get_collection_id), 'get_config': gi.FunctionInfo(get_config), 'get_default_repo_finders': gi.FunctionInfo(get_default_repo_finders), 'get_dfd': gi.FunctionInfo(get_dfd), 'get_disable_fsync': gi.FunctionInfo(get_disable_fsync), 'get_min_free_space_bytes': gi.FunctionInfo(get_min_free_space_bytes), 'get_mode': gi.FunctionInfo(get_mode), 'get_parent': gi.FunctionInfo(get_parent), 'get_path': gi.FunctionInfo(get_path), 'get_remote_boolean_option': gi.FunctionInfo(get_remote_boolean_option), 'get_remote_list_option': gi.FunctionInfo(get_remote_list_option), 'get_remote_option': gi.FunctionInfo(get_remote_option), 'gpg_verify_data': gi.FunctionInfo(gpg_verify_data), 'has_object': gi.FunctionInfo(has_object), 'hash': gi.FunctionInfo(hash), 'import_object_from': gi.FunctionInfo(import_object_from), 'import_object_from_with_trust': gi.FunctionInfo(import_object_from_with_trust), 'is_system': gi.FunctionInfo(is_system), 'is_writable': gi.FunctionInfo(is_writable), 'list_collection_refs': gi.FunctionInfo(list_collection_refs), 'list_commit_objects_starting_with': gi.FunctionInfo(list_commit_objects_starting_with), 'list_objects': gi.FunctionInfo(list_objects), 'list_refs': gi.FunctionInfo(list_refs), 'list_refs_ext': gi.FunctionInfo(list_refs_ext), 'list_static_delta_names': gi.FunctionInfo(list_static_delta_names), 'load_commit': gi.FunctionInfo(load_commit), 'load_file': gi.FunctionInfo(load_file), 'load_object_stream': gi.FunctionInfo(load_object_stream), 'load_variant': gi.FunctionInfo(load_variant), 'load_variant_if_exists': gi.FunctionInfo(load_variant_if_exists), 'mark_commit_partial': gi.FunctionInfo(mark_commit_partial), 'mark_commit_partial_reason': gi.FunctionInfo(mark_commit_partial_reason), 'open': gi.FunctionInfo(open), 'prepare_transaction': gi.FunctionInfo(prepare_transaction), 'prune': gi.FunctionInfo(prune), 'prune_from_reachable': gi.FunctionInfo(prune_from_reachable), 'prune_static_deltas': gi.FunctionInfo(prune_static_deltas), 'pull': gi.FunctionInfo(pull), 'pull_from_remotes_async': gi.FunctionInfo(pull_from_remotes_async), 'pull_from_remotes_finish': gi.FunctionInfo(pull_from_remotes_finish), 'pull_one_dir': gi.FunctionInfo(pull_one_dir), 'pull_with_options': gi.FunctionInfo(pull_with_options), 'query_object_storage_size': gi.FunctionInfo(query_object_storage_size), 'read_commit': gi.FunctionInfo(read_commit), 'read_commit_detached_metadata': gi.FunctionInfo(read_commit_detached_metadata), 'regenerate_summary': gi.FunctionInfo(regenerate_summary), 'reload_config': gi.FunctionInfo(reload_config), 'remote_add': gi.FunctionInfo(remote_add), 'remote_change': gi.FunctionInfo(remote_change), 'remote_delete': gi.FunctionInfo(remote_delete), 'remote_fetch_summary': gi.FunctionInfo(remote_fetch_summary), 'remote_fetch_summary_with_options': gi.FunctionInfo(remote_fetch_summary_with_options), 'remote_get_gpg_verify': gi.FunctionInfo(remote_get_gpg_verify), 'remote_get_gpg_verify_summary': gi.FunctionInfo(remote_get_gpg_verify_summary), 'remote_get_url': gi.FunctionInfo(remote_get_url), 'remote_gpg_import': gi.FunctionInfo(remote_gpg_import), 'remote_list': gi.FunctionInfo(remote_list), 'remote_list_collection_refs': gi.FunctionInfo(remote_list_collection_refs), 'remote_list_refs': gi.FunctionInfo(remote_list_refs), 'resolve_collection_ref': gi.FunctionInfo(resolve_collection_ref), 'resolve_keyring_for_collection': gi.FunctionInfo(resolve_keyring_for_collection), 'resolve_rev': gi.FunctionInfo(resolve_rev), 'resolve_rev_ext': gi.FunctionInfo(resolve_rev_ext), 'scan_hardlinks': gi.FunctionInfo(scan_hardlinks), 'set_alias_ref_immediate': gi.FunctionInfo(set_alias_ref_immediate), 'set_cache_dir': gi.FunctionInfo(set_cache_dir), 'set_collection_id': gi.FunctionInfo(set_collection_id), 'set_collection_ref_immediate': gi.FunctionInfo(set_collection_ref_immediate), 'set_disable_fsync': gi.FunctionInfo(set_disable_fsync), 'set_ref_immediate': gi.FunctionInfo(set_ref_immediate), 'sign_commit': gi.FunctionInfo(sign_commit), 'sign_delta': gi.FunctionInfo(sign_delta), 'static_delta_execute_offline': gi.FunctionInfo(static_delta_execute_offline), 'static_delta_generate': gi.FunctionInfo(static_delta_generate), 'transaction_set_collection_ref': gi.FunctionInfo(transaction_set_collection_ref), 'transaction_set_ref': gi.FunctionInfo(transaction_set_ref), 'transaction_set_refspec': gi.FunctionInfo(transaction_set_refspec), 'traverse_commit': gi.FunctionInfo(traverse_commit), 'traverse_reachable_refs': gi.FunctionInfo(traverse_reachable_refs), 'verify_commit': gi.FunctionInfo(verify_commit), 'verify_commit_ext': gi.FunctionInfo(verify_commit_ext), 'verify_commit_for_remote': gi.FunctionInfo(verify_commit_for_remote), 'verify_summary': gi.FunctionInfo(verify_summary), 'write_archive_to_mtree': gi.FunctionInfo(write_archive_to_mtree), 'write_archive_to_mtree_from_fd': gi.FunctionInfo(write_archive_to_mtree_from_fd), 'write_commit': gi.FunctionInfo(write_commit), 'write_commit_detached_metadata': gi.FunctionInfo(write_commit_detached_metadata), 'write_commit_with_time': gi.FunctionInfo(write_commit_with_time), 'write_config': gi.FunctionInfo(write_config), 'write_content': gi.FunctionInfo(write_content), 'write_content_async': gi.FunctionInfo(write_content_async), 'write_content_finish': gi.FunctionInfo(write_content_finish), 'write_content_trusted': gi.FunctionInfo(write_content_trusted), 'write_dfd_to_mtree': gi.FunctionInfo(write_dfd_to_mtree), 'write_directory_to_mtree': gi.FunctionInfo(write_directory_to_mtree), 'write_metadata': gi.FunctionInfo(write_metadata), 'write_metadata_async': gi.FunctionInfo(write_metadata_async), 'write_metadata_finish': gi.FunctionInfo(write_metadata_finish), 'write_metadata_stream_trusted': gi.FunctionInfo(write_metadata_stream_trusted), 'write_metadata_trusted': gi.FunctionInfo(write_metadata_trusted), 'write_mtree': gi.FunctionInfo(write_mtree)})"
    __gdoc__ = 'Object OstreeRepo\n\nSignals from OstreeRepo:\n  gpg-verify-result (gchararray, OstreeGpgVerifyResult)\n\nProperties from OstreeRepo:\n  path -> GFile: Path\n    Path\n  remotes-config-dir -> gchararray: \n    \n  sysroot-path -> GFile: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OstreeRepo (94405993275248)>'
    __info__ = ObjectInfo(Repo)


