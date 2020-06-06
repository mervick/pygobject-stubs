# encoding: utf-8
# module gi.repository.Flatpak
# from /usr/lib64/girepository-1.0/Flatpak-1.0.typelib
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


class Installation(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Installation(**properties)
        new_for_path(path:Gio.File, user:bool, cancellable:Gio.Cancellable=None) -> Flatpak.Installation
        new_system(cancellable:Gio.Cancellable=None) -> Flatpak.Installation
        new_system_with_id(id:str=None, cancellable:Gio.Cancellable=None) -> Flatpak.Installation
        new_user(cancellable:Gio.Cancellable=None) -> Flatpak.Installation
    """
    def add_remote(self, remote, if_needed, cancellable=None): # real signature unknown; restored from __doc__
        """ add_remote(self, remote:Flatpak.Remote, if_needed:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def cleanup_local_refs_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ cleanup_local_refs_sync(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def create_monitor(self, cancellable=None): # real signature unknown; restored from __doc__
        """ create_monitor(self, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def drop_caches(self, cancellable=None): # real signature unknown; restored from __doc__
        """ drop_caches(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def fetch_remote_metadata_sync(self, remote_name, ref, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_remote_metadata_sync(self, remote_name:str, ref:Flatpak.Ref, cancellable:Gio.Cancellable=None) -> GLib.Bytes """
        pass

    def fetch_remote_ref_sync(self, remote_name, kind, name, arch=None, branch=None, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_remote_ref_sync(self, remote_name:str, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, cancellable:Gio.Cancellable=None) -> Flatpak.RemoteRef """
        pass

    def fetch_remote_ref_sync_full(self, remote_name, kind, name, arch=None, branch=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_remote_ref_sync_full(self, remote_name:str, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, flags:Flatpak.QueryFlags, cancellable:Gio.Cancellable=None) -> Flatpak.RemoteRef """
        pass

    def fetch_remote_size_sync(self, remote_name, ref, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_remote_size_sync(self, remote_name:str, ref:Flatpak.Ref, cancellable:Gio.Cancellable=None) -> bool, download_size:int, installed_size:int """
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

    def get_config(self, key, cancellable=None): # real signature unknown; restored from __doc__
        """ get_config(self, key:str, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def get_current_installed_app(self, name, cancellable=None): # real signature unknown; restored from __doc__
        """ get_current_installed_app(self, name:str, cancellable:Gio.Cancellable=None) -> Flatpak.InstalledRef """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_languages(self): # real signature unknown; restored from __doc__
        """ get_default_languages(self) -> list """
        return []

    def get_default_locales(self): # real signature unknown; restored from __doc__
        """ get_default_locales(self) -> list """
        return []

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_installed_ref(self, kind, name, arch=None, branch=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_installed_ref(self, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, cancellable:Gio.Cancellable=None) -> Flatpak.InstalledRef """
        pass

    def get_is_user(self): # real signature unknown; restored from __doc__
        """ get_is_user(self) -> bool """
        return False

    def get_min_free_space_bytes(self): # real signature unknown; restored from __doc__
        """ get_min_free_space_bytes(self) -> bool, out_bytes:int """
        return False

    def get_no_interaction(self): # real signature unknown; restored from __doc__
        """ get_no_interaction(self) -> bool """
        return False

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gio.File """
        pass

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_by_name(self, name, cancellable=None): # real signature unknown; restored from __doc__
        """ get_remote_by_name(self, name:str, cancellable:Gio.Cancellable=None) -> Flatpak.Remote """
        pass

    def get_storage_type(self): # real signature unknown; restored from __doc__
        """ get_storage_type(self) -> Flatpak.StorageType """
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

    def install(self, remote_name, kind, name, arch=None, branch=None, progress=None, progress_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ install(self, remote_name:str, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, progress:Flatpak.ProgressCallback=None, progress_data=None, cancellable:Gio.Cancellable=None) -> Flatpak.InstalledRef """
        pass

    def install_bundle(self, file, progress=None, progress_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ install_bundle(self, file:Gio.File, progress:Flatpak.ProgressCallback=None, progress_data=None, cancellable:Gio.Cancellable=None) -> Flatpak.InstalledRef """
        pass

    def install_full(self, flags, remote_name, kind, name, arch=None, branch=None, subpaths=None, progress=None, progress_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ install_full(self, flags:Flatpak.InstallFlags, remote_name:str, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, subpaths:list=None, progress:Flatpak.ProgressCallback=None, progress_data=None, cancellable:Gio.Cancellable=None) -> Flatpak.InstalledRef """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_ref_file(self, ref_file_data, cancellable=None): # real signature unknown; restored from __doc__
        """ install_ref_file(self, ref_file_data:GLib.Bytes, cancellable:Gio.Cancellable=None) -> Flatpak.RemoteRef """
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

    def launch(self, name, arch=None, branch=None, commit=None, cancellable=None): # real signature unknown; restored from __doc__
        """ launch(self, name:str, arch:str=None, branch:str=None, commit:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def launch_full(self, flags, name, arch=None, branch=None, commit=None, instance_out=None, cancellable=None): # real signature unknown; restored from __doc__
        """ launch_full(self, flags:Flatpak.LaunchFlags, name:str, arch:str=None, branch:str=None, commit:str=None, instance_out:Flatpak.Instance=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def list_installed_refs(self, cancellable=None): # real signature unknown; restored from __doc__
        """ list_installed_refs(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_installed_refs_by_kind(self, kind, cancellable=None): # real signature unknown; restored from __doc__
        """ list_installed_refs_by_kind(self, kind:Flatpak.RefKind, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_installed_refs_for_update(self, cancellable=None): # real signature unknown; restored from __doc__
        """ list_installed_refs_for_update(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_installed_related_refs_sync(self, remote_name, ref, cancellable=None): # real signature unknown; restored from __doc__
        """ list_installed_related_refs_sync(self, remote_name:str, ref:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_remotes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ list_remotes(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_remotes_by_type(self, types, cancellable=None): # real signature unknown; restored from __doc__
        """ list_remotes_by_type(self, types:list, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_remote_refs_sync(self, remote_or_uri, cancellable=None): # real signature unknown; restored from __doc__
        """ list_remote_refs_sync(self, remote_or_uri:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_remote_refs_sync_full(self, remote_or_uri, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ list_remote_refs_sync_full(self, remote_or_uri:str, flags:Flatpak.QueryFlags, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_remote_related_refs_sync(self, remote_name, ref, cancellable=None): # real signature unknown; restored from __doc__
        """ list_remote_related_refs_sync(self, remote_name:str, ref:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def list_unused_refs(self, arch=None, cancellable=None): # real signature unknown; restored from __doc__
        """ list_unused_refs(self, arch:str=None, cancellable:Gio.Cancellable=None) -> list """
        return []

    def load_app_overrides(self, app_id, cancellable=None): # real signature unknown; restored from __doc__
        """ load_app_overrides(self, app_id:str, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def modify_remote(self, remote, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_remote(self, remote:Flatpak.Remote, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_for_path(self, path, user, cancellable=None): # real signature unknown; restored from __doc__
        """ new_for_path(path:Gio.File, user:bool, cancellable:Gio.Cancellable=None) -> Flatpak.Installation """
        pass

    def new_system(self, cancellable=None): # real signature unknown; restored from __doc__
        """ new_system(cancellable:Gio.Cancellable=None) -> Flatpak.Installation """
        pass

    def new_system_with_id(self, id=None, cancellable=None): # real signature unknown; restored from __doc__
        """ new_system_with_id(id:str=None, cancellable:Gio.Cancellable=None) -> Flatpak.Installation """
        pass

    def new_user(self, cancellable=None): # real signature unknown; restored from __doc__
        """ new_user(cancellable:Gio.Cancellable=None) -> Flatpak.Installation """
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

    def prune_local_repo(self, cancellable=None): # real signature unknown; restored from __doc__
        """ prune_local_repo(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_local_ref_sync(self, remote_name, ref, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_local_ref_sync(self, remote_name:str, ref:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_remote(self, name, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_remote(self, name:str, cancellable:Gio.Cancellable=None) -> bool """
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

    def run_triggers(self, cancellable=None): # real signature unknown; restored from __doc__
        """ run_triggers(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_config_sync(self, key, value, cancellable=None): # real signature unknown; restored from __doc__
        """ set_config_sync(self, key:str, value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_no_interaction(self, no_interaction): # real signature unknown; restored from __doc__
        """ set_no_interaction(self, no_interaction:bool) """
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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def uninstall(self, kind, name, arch=None, branch=None, progress=None, progress_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ uninstall(self, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, progress:Flatpak.ProgressCallback=None, progress_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def uninstall_full(self, flags, kind, name, arch=None, branch=None, progress=None, progress_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ uninstall_full(self, flags:Flatpak.UninstallFlags, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, progress:Flatpak.ProgressCallback=None, progress_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update(self, flags, kind, name, arch=None, branch=None, progress=None, progress_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ update(self, flags:Flatpak.UpdateFlags, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, progress:Flatpak.ProgressCallback=None, progress_data=None, cancellable:Gio.Cancellable=None) -> Flatpak.InstalledRef """
        pass

    def update_appstream_full_sync(self, remote_name, arch=None, progress=None, progress_data=None, out_changed=None, cancellable=None): # real signature unknown; restored from __doc__
        """ update_appstream_full_sync(self, remote_name:str, arch:str=None, progress:Flatpak.ProgressCallback=None, progress_data=None, out_changed:bool=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def update_appstream_sync(self, remote_name, arch=None, out_changed=None, cancellable=None): # real signature unknown; restored from __doc__
        """ update_appstream_sync(self, remote_name:str, arch:str=None, out_changed:bool=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def update_full(self, flags, kind, name, arch=None, branch=None, subpaths=None, progress=None, progress_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ update_full(self, flags:Flatpak.UpdateFlags, kind:Flatpak.RefKind, name:str, arch:str=None, branch:str=None, subpaths:list=None, progress:Flatpak.ProgressCallback=None, progress_data=None, cancellable:Gio.Cancellable=None) -> Flatpak.InstalledRef """
        pass

    def update_remote_sync(self, name, cancellable=None): # real signature unknown; restored from __doc__
        """ update_remote_sync(self, name:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f29534d08e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Installation), '__module__': 'gi.repository.Flatpak', '__gtype__': <GType FlatpakInstallation (94781644065584)>, '__doc__': None, '__gsignals__': {}, 'new_for_path': gi.FunctionInfo(new_for_path), 'new_system': gi.FunctionInfo(new_system), 'new_system_with_id': gi.FunctionInfo(new_system_with_id), 'new_user': gi.FunctionInfo(new_user), 'add_remote': gi.FunctionInfo(add_remote), 'cleanup_local_refs_sync': gi.FunctionInfo(cleanup_local_refs_sync), 'create_monitor': gi.FunctionInfo(create_monitor), 'drop_caches': gi.FunctionInfo(drop_caches), 'fetch_remote_metadata_sync': gi.FunctionInfo(fetch_remote_metadata_sync), 'fetch_remote_ref_sync': gi.FunctionInfo(fetch_remote_ref_sync), 'fetch_remote_ref_sync_full': gi.FunctionInfo(fetch_remote_ref_sync_full), 'fetch_remote_size_sync': gi.FunctionInfo(fetch_remote_size_sync), 'get_config': gi.FunctionInfo(get_config), 'get_current_installed_app': gi.FunctionInfo(get_current_installed_app), 'get_default_languages': gi.FunctionInfo(get_default_languages), 'get_default_locales': gi.FunctionInfo(get_default_locales), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_id': gi.FunctionInfo(get_id), 'get_installed_ref': gi.FunctionInfo(get_installed_ref), 'get_is_user': gi.FunctionInfo(get_is_user), 'get_min_free_space_bytes': gi.FunctionInfo(get_min_free_space_bytes), 'get_no_interaction': gi.FunctionInfo(get_no_interaction), 'get_path': gi.FunctionInfo(get_path), 'get_priority': gi.FunctionInfo(get_priority), 'get_remote_by_name': gi.FunctionInfo(get_remote_by_name), 'get_storage_type': gi.FunctionInfo(get_storage_type), 'install': gi.FunctionInfo(install), 'install_bundle': gi.FunctionInfo(install_bundle), 'install_full': gi.FunctionInfo(install_full), 'install_ref_file': gi.FunctionInfo(install_ref_file), 'launch': gi.FunctionInfo(launch), 'launch_full': gi.FunctionInfo(launch_full), 'list_installed_refs': gi.FunctionInfo(list_installed_refs), 'list_installed_refs_by_kind': gi.FunctionInfo(list_installed_refs_by_kind), 'list_installed_refs_for_update': gi.FunctionInfo(list_installed_refs_for_update), 'list_installed_related_refs_sync': gi.FunctionInfo(list_installed_related_refs_sync), 'list_remote_refs_sync': gi.FunctionInfo(list_remote_refs_sync), 'list_remote_refs_sync_full': gi.FunctionInfo(list_remote_refs_sync_full), 'list_remote_related_refs_sync': gi.FunctionInfo(list_remote_related_refs_sync), 'list_remotes': gi.FunctionInfo(list_remotes), 'list_remotes_by_type': gi.FunctionInfo(list_remotes_by_type), 'list_unused_refs': gi.FunctionInfo(list_unused_refs), 'load_app_overrides': gi.FunctionInfo(load_app_overrides), 'modify_remote': gi.FunctionInfo(modify_remote), 'prune_local_repo': gi.FunctionInfo(prune_local_repo), 'remove_local_ref_sync': gi.FunctionInfo(remove_local_ref_sync), 'remove_remote': gi.FunctionInfo(remove_remote), 'run_triggers': gi.FunctionInfo(run_triggers), 'set_config_sync': gi.FunctionInfo(set_config_sync), 'set_no_interaction': gi.FunctionInfo(set_no_interaction), 'uninstall': gi.FunctionInfo(uninstall), 'uninstall_full': gi.FunctionInfo(uninstall_full), 'update': gi.FunctionInfo(update), 'update_appstream_full_sync': gi.FunctionInfo(update_appstream_full_sync), 'update_appstream_sync': gi.FunctionInfo(update_appstream_sync), 'update_full': gi.FunctionInfo(update_full), 'update_remote_sync': gi.FunctionInfo(update_remote_sync), 'parent': <property object at 0x7f29534e6450>})"
    __gdoc__ = 'Object FlatpakInstallation\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType FlatpakInstallation (94781644065584)>'
    __info__ = ObjectInfo(Installation)


