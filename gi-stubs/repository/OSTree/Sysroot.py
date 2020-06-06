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


class Sysroot(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Sysroot(**properties)
        new(path:Gio.File=None) -> OSTree.Sysroot
        new_default() -> OSTree.Sysroot
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def cleanup(self, cancellable=None): # real signature unknown; restored from __doc__
        """ cleanup(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def cleanup_prune_repo(self, options, cancellable=None): # real signature unknown; restored from __doc__
        """ cleanup_prune_repo(self, options:OSTree.RepoPruneOptions, cancellable:Gio.Cancellable=None) -> bool, out_objects_total:int, out_objects_pruned:int, out_pruned_object_size_total:int """
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

    def deployment_set_kargs(self, deployment, new_kargs, cancellable=None): # real signature unknown; restored from __doc__
        """ deployment_set_kargs(self, deployment:OSTree.Deployment, new_kargs:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def deployment_set_mutable(self, deployment, is_mutable, cancellable=None): # real signature unknown; restored from __doc__
        """ deployment_set_mutable(self, deployment:OSTree.Deployment, is_mutable:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def deployment_set_pinned(self, deployment, is_pinned): # real signature unknown; restored from __doc__
        """ deployment_set_pinned(self, deployment:OSTree.Deployment, is_pinned:bool) -> bool """
        return False

    def deployment_unlock(self, deployment, unlocked_state, cancellable=None): # real signature unknown; restored from __doc__
        """ deployment_unlock(self, deployment:OSTree.Deployment, unlocked_state:OSTree.DeploymentUnlockedState, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def deploy_tree(self, osname=None, revision, origin=None, provided_merge_deployment=None, override_kernel_argv=None, cancellable=None): # real signature unknown; restored from __doc__
        """ deploy_tree(self, osname:str=None, revision:str, origin:GLib.KeyFile=None, provided_merge_deployment:OSTree.Deployment=None, override_kernel_argv:list=None, cancellable:Gio.Cancellable=None) -> bool, out_new_deployment:OSTree.Deployment """
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

    def ensure_initialized(self, cancellable=None): # real signature unknown; restored from __doc__
        """ ensure_initialized(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def get_booted_deployment(self): # real signature unknown; restored from __doc__
        """ get_booted_deployment(self) -> OSTree.Deployment """
        pass

    def get_bootversion(self): # real signature unknown; restored from __doc__
        """ get_bootversion(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_deployments(self): # real signature unknown; restored from __doc__
        """ get_deployments(self) -> list """
        return []

    def get_deployment_directory(self, deployment): # real signature unknown; restored from __doc__
        """ get_deployment_directory(self, deployment:OSTree.Deployment) -> Gio.File """
        pass

    def get_deployment_dirpath(self, deployment): # real signature unknown; restored from __doc__
        """ get_deployment_dirpath(self, deployment:OSTree.Deployment) -> str """
        return ""

    def get_deployment_origin_path(self, deployment_path): # real signature unknown; restored from __doc__
        """ get_deployment_origin_path(deployment_path:Gio.File) -> Gio.File """
        pass

    def get_fd(self): # real signature unknown; restored from __doc__
        """ get_fd(self) -> int """
        return 0

    def get_merge_deployment(self, osname=None): # real signature unknown; restored from __doc__
        """ get_merge_deployment(self, osname:str=None) -> OSTree.Deployment """
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

    def get_repo(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_repo(self, cancellable:Gio.Cancellable=None) -> bool, out_repo:OSTree.Repo """
        return False

    def get_staged_deployment(self): # real signature unknown; restored from __doc__
        """ get_staged_deployment(self) -> OSTree.Deployment """
        pass

    def get_subbootversion(self): # real signature unknown; restored from __doc__
        """ get_subbootversion(self) -> int """
        return 0

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

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) -> bool """
        return False

    def init_osname(self, osname, cancellable=None): # real signature unknown; restored from __doc__
        """ init_osname(self, osname:str, cancellable:Gio.Cancellable=None) -> bool """
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

    def is_booted(self): # real signature unknown; restored from __doc__
        """ is_booted(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def load_if_changed(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_if_changed(self, cancellable:Gio.Cancellable=None) -> bool, out_changed:bool """
        return False

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) -> bool """
        return False

    def lock_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lock_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lock_finish(self, result): # real signature unknown; restored from __doc__
        """ lock_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def lock_with_mount_namespace(self): # real signature unknown; restored from __doc__
        """ lock_with_mount_namespace(self) -> bool """
        return False

    def new(self, path=None): # real signature unknown; restored from __doc__
        """ new(path:Gio.File=None) -> OSTree.Sysroot """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_default(self): # real signature unknown; restored from __doc__
        """ new_default() -> OSTree.Sysroot """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def origin_new_from_refspec(self, refspec): # real signature unknown; restored from __doc__
        """ origin_new_from_refspec(self, refspec:str) -> GLib.KeyFile """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def prepare_cleanup(self, cancellable=None): # real signature unknown; restored from __doc__
        """ prepare_cleanup(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def query_deployments_for(self, osname=None): # real signature unknown; restored from __doc__
        """ query_deployments_for(self, osname:str=None) -> out_pending:OSTree.Deployment, out_rollback:OSTree.Deployment """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def repo(self): # real signature unknown; restored from __doc__
        """ repo(self) -> OSTree.Repo """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_mount_namespace_in_use(self): # real signature unknown; restored from __doc__
        """ set_mount_namespace_in_use(self) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def simple_write_deployment(self, osname=None, new_deployment, merge_deployment=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ simple_write_deployment(self, osname:str=None, new_deployment:OSTree.Deployment, merge_deployment:OSTree.Deployment=None, flags:OSTree.SysrootSimpleWriteDeploymentFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def stage_tree(self, osname=None, revision, origin=None, merge_deployment=None, override_kernel_argv=None, cancellable=None): # real signature unknown; restored from __doc__
        """ stage_tree(self, osname:str=None, revision:str, origin:GLib.KeyFile=None, merge_deployment:OSTree.Deployment=None, override_kernel_argv:list=None, cancellable:Gio.Cancellable=None) -> bool, out_new_deployment:OSTree.Deployment """
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

    def try_lock(self): # real signature unknown; restored from __doc__
        """ try_lock(self) -> bool, out_acquired:bool """
        return False

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) """
        pass

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

    def write_deployments(self, new_deployments, cancellable=None): # real signature unknown; restored from __doc__
        """ write_deployments(self, new_deployments:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_deployments_with_options(self, new_deployments, opts, cancellable=None): # real signature unknown; restored from __doc__
        """ write_deployments_with_options(self, new_deployments:list, opts:OSTree.SysrootWriteDeploymentsOpts, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def write_origin_file(self, deployment, new_origin=None, cancellable=None): # real signature unknown; restored from __doc__
        """ write_origin_file(self, deployment:OSTree.Deployment, new_origin:GLib.KeyFile=None, cancellable:Gio.Cancellable=None) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7feceb58de20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Sysroot), '__module__': 'gi.repository.OSTree', '__gtype__': <GType OstreeSysroot (94405993422784)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_default': gi.FunctionInfo(new_default), 'get_deployment_origin_path': gi.FunctionInfo(get_deployment_origin_path), 'cleanup': gi.FunctionInfo(cleanup), 'cleanup_prune_repo': gi.FunctionInfo(cleanup_prune_repo), 'deploy_tree': gi.FunctionInfo(deploy_tree), 'deployment_set_kargs': gi.FunctionInfo(deployment_set_kargs), 'deployment_set_mutable': gi.FunctionInfo(deployment_set_mutable), 'deployment_set_pinned': gi.FunctionInfo(deployment_set_pinned), 'deployment_unlock': gi.FunctionInfo(deployment_unlock), 'ensure_initialized': gi.FunctionInfo(ensure_initialized), 'get_booted_deployment': gi.FunctionInfo(get_booted_deployment), 'get_bootversion': gi.FunctionInfo(get_bootversion), 'get_deployment_directory': gi.FunctionInfo(get_deployment_directory), 'get_deployment_dirpath': gi.FunctionInfo(get_deployment_dirpath), 'get_deployments': gi.FunctionInfo(get_deployments), 'get_fd': gi.FunctionInfo(get_fd), 'get_merge_deployment': gi.FunctionInfo(get_merge_deployment), 'get_path': gi.FunctionInfo(get_path), 'get_repo': gi.FunctionInfo(get_repo), 'get_staged_deployment': gi.FunctionInfo(get_staged_deployment), 'get_subbootversion': gi.FunctionInfo(get_subbootversion), 'init_osname': gi.FunctionInfo(init_osname), 'initialize': gi.FunctionInfo(initialize), 'is_booted': gi.FunctionInfo(is_booted), 'load': gi.FunctionInfo(load), 'load_if_changed': gi.FunctionInfo(load_if_changed), 'lock': gi.FunctionInfo(lock), 'lock_async': gi.FunctionInfo(lock_async), 'lock_finish': gi.FunctionInfo(lock_finish), 'lock_with_mount_namespace': gi.FunctionInfo(lock_with_mount_namespace), 'origin_new_from_refspec': gi.FunctionInfo(origin_new_from_refspec), 'prepare_cleanup': gi.FunctionInfo(prepare_cleanup), 'query_deployments_for': gi.FunctionInfo(query_deployments_for), 'repo': gi.FunctionInfo(repo), 'set_mount_namespace_in_use': gi.FunctionInfo(set_mount_namespace_in_use), 'simple_write_deployment': gi.FunctionInfo(simple_write_deployment), 'stage_tree': gi.FunctionInfo(stage_tree), 'try_lock': gi.FunctionInfo(try_lock), 'unload': gi.FunctionInfo(unload), 'unlock': gi.FunctionInfo(unlock), 'write_deployments': gi.FunctionInfo(write_deployments), 'write_deployments_with_options': gi.FunctionInfo(write_deployments_with_options), 'write_origin_file': gi.FunctionInfo(write_origin_file)})"
    __gdoc__ = 'Object OstreeSysroot\n\nSignals from OstreeSysroot:\n  journal-msg (gchararray)\n\nProperties from OstreeSysroot:\n  path -> GFile: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OstreeSysroot (94405993422784)>'
    __info__ = ObjectInfo(Sysroot)


