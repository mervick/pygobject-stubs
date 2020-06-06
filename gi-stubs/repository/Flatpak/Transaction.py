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


class Transaction(__gi_overrides_GObject.Object, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        Transaction(**properties)
        new_for_installation(installation:Flatpak.Installation, cancellable:Gio.Cancellable=None) -> Flatpak.Transaction
    """
    def abort_webflow(self, id): # real signature unknown; restored from __doc__
        """ abort_webflow(self, id:int) """
        pass

    def add_default_dependency_sources(self): # real signature unknown; restored from __doc__
        """ add_default_dependency_sources(self) """
        pass

    def add_dependency_source(self, installation): # real signature unknown; restored from __doc__
        """ add_dependency_source(self, installation:Flatpak.Installation) """
        pass

    def add_install(self, remote, ref, subpaths=None): # real signature unknown; restored from __doc__
        """ add_install(self, remote:str, ref:str, subpaths:list=None) -> bool """
        return False

    def add_install_bundle(self, file, gpg_data=None): # real signature unknown; restored from __doc__
        """ add_install_bundle(self, file:Gio.File, gpg_data:GLib.Bytes=None) -> bool """
        return False

    def add_install_flatpakref(self, flatpakref_data): # real signature unknown; restored from __doc__
        """ add_install_flatpakref(self, flatpakref_data:GLib.Bytes) -> bool """
        return False

    def add_rebase(self, remote, ref, subpaths=None, previous_ids=None): # real signature unknown; restored from __doc__
        """ add_rebase(self, remote:str, ref:str, subpaths:str=None, previous_ids:list=None) -> bool """
        return False

    def add_uninstall(self, ref): # real signature unknown; restored from __doc__
        """ add_uninstall(self, ref:str) -> bool """
        return False

    def add_update(self, ref, subpaths=None, commit=None): # real signature unknown; restored from __doc__
        """ add_update(self, ref:str, subpaths:list=None, commit:str=None) -> bool """
        return False

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

    def complete_basic_auth(self, id, user, password, options): # real signature unknown; restored from __doc__
        """ complete_basic_auth(self, id:int, user:str, password:str, options:GLib.Variant) """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add_new_remote(self, *args, **kwargs): # real signature unknown
        """ add_new_remote(self, reason:Flatpak.TransactionRemoteReason, from_id:str, remote_name:str, url:str) -> bool """
        pass

    def do_basic_auth_start(self, *args, **kwargs): # real signature unknown
        """ basic_auth_start(self, remote:str, realm:str, options:GLib.Variant, id:int) -> bool """
        pass

    def do_choose_remote_for_ref(self, *args, **kwargs): # real signature unknown
        """ choose_remote_for_ref(self, for_ref:str, runtime_ref:str, remotes:str) -> int """
        pass

    def do_end_of_lifed(self, *args, **kwargs): # real signature unknown
        """ end_of_lifed(self, ref:str, reason:str, rebase:str) """
        pass

    def do_end_of_lifed_with_rebase(self, *args, **kwargs): # real signature unknown
        """ end_of_lifed_with_rebase(self, remote:str, ref:str, reason:str, rebased_to_ref:str, previous_ids:str) -> bool """
        pass

    def do_new_operation(self, *args, **kwargs): # real signature unknown
        """ new_operation(self, operation:Flatpak.TransactionOperation, progress:Flatpak.TransactionProgress) """
        pass

    def do_operation_done(self, *args, **kwargs): # real signature unknown
        """ operation_done(self, operation:Flatpak.TransactionOperation, commit:str, details:Flatpak.TransactionResult) """
        pass

    def do_operation_error(self, *args, **kwargs): # real signature unknown
        """ operation_error(self, operation:Flatpak.TransactionOperation, error:error, detail:Flatpak.TransactionErrorDetails) -> bool """
        pass

    def do_ready(self, *args, **kwargs): # real signature unknown
        """ ready(self) -> bool """
        pass

    def do_run(self, *args, **kwargs): # real signature unknown
        """ run(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_webflow_done(self, *args, **kwargs): # real signature unknown
        """ webflow_done(self, options:GLib.Variant, id:int) """
        pass

    def do_webflow_start(self, *args, **kwargs): # real signature unknown
        """ webflow_start(self, remote:str, url:str, options:GLib.Variant, id:int) -> bool """
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_current_operation(self): # real signature unknown; restored from __doc__
        """ get_current_operation(self) -> Flatpak.TransactionOperation """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_installation(self): # real signature unknown; restored from __doc__
        """ get_installation(self) -> Flatpak.Installation """
        pass

    def get_no_deploy(self): # real signature unknown; restored from __doc__
        """ get_no_deploy(self) -> bool """
        return False

    def get_no_pull(self): # real signature unknown; restored from __doc__
        """ get_no_pull(self) -> bool """
        return False

    def get_operations(self): # real signature unknown; restored from __doc__
        """ get_operations(self) -> list """
        return []

    def get_parent_window(self): # real signature unknown; restored from __doc__
        """ get_parent_window(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_for_installation(self, installation, cancellable=None): # real signature unknown; restored from __doc__
        """ new_for_installation(installation:Flatpak.Installation, cancellable:Gio.Cancellable=None) -> Flatpak.Transaction """
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

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run(self, cancellable=None): # real signature unknown; restored from __doc__
        """ run(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_arch(self, arch): # real signature unknown; restored from __doc__
        """ set_default_arch(self, arch:str) """
        pass

    def set_disable_dependencies(self, disable_dependencies): # real signature unknown; restored from __doc__
        """ set_disable_dependencies(self, disable_dependencies:bool) """
        pass

    def set_disable_prune(self, disable_prune): # real signature unknown; restored from __doc__
        """ set_disable_prune(self, disable_prune:bool) """
        pass

    def set_disable_related(self, disable_related): # real signature unknown; restored from __doc__
        """ set_disable_related(self, disable_related:bool) """
        pass

    def set_disable_static_deltas(self, disable_static_deltas): # real signature unknown; restored from __doc__
        """ set_disable_static_deltas(self, disable_static_deltas:bool) """
        pass

    def set_force_uninstall(self, force_uninstall): # real signature unknown; restored from __doc__
        """ set_force_uninstall(self, force_uninstall:bool) """
        pass

    def set_no_deploy(self, no_deploy): # real signature unknown; restored from __doc__
        """ set_no_deploy(self, no_deploy:bool) """
        pass

    def set_no_pull(self, no_pull): # real signature unknown; restored from __doc__
        """ set_no_pull(self, no_pull:bool) """
        pass

    def set_parent_window(self, parent_window): # real signature unknown; restored from __doc__
        """ set_parent_window(self, parent_window:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_reinstall(self, reinstall): # real signature unknown; restored from __doc__
        """ set_reinstall(self, reinstall:bool) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f29524570d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Transaction), '__module__': 'gi.repository.Flatpak', '__gtype__': <GType FlatpakTransaction (94781644122848)>, '__doc__': None, '__gsignals__': {}, 'new_for_installation': gi.FunctionInfo(new_for_installation), 'abort_webflow': gi.FunctionInfo(abort_webflow), 'add_default_dependency_sources': gi.FunctionInfo(add_default_dependency_sources), 'add_dependency_source': gi.FunctionInfo(add_dependency_source), 'add_install': gi.FunctionInfo(add_install), 'add_install_bundle': gi.FunctionInfo(add_install_bundle), 'add_install_flatpakref': gi.FunctionInfo(add_install_flatpakref), 'add_rebase': gi.FunctionInfo(add_rebase), 'add_uninstall': gi.FunctionInfo(add_uninstall), 'add_update': gi.FunctionInfo(add_update), 'complete_basic_auth': gi.FunctionInfo(complete_basic_auth), 'get_current_operation': gi.FunctionInfo(get_current_operation), 'get_installation': gi.FunctionInfo(get_installation), 'get_no_deploy': gi.FunctionInfo(get_no_deploy), 'get_no_pull': gi.FunctionInfo(get_no_pull), 'get_operations': gi.FunctionInfo(get_operations), 'get_parent_window': gi.FunctionInfo(get_parent_window), 'is_empty': gi.FunctionInfo(is_empty), 'run': gi.FunctionInfo(run), 'set_default_arch': gi.FunctionInfo(set_default_arch), 'set_disable_dependencies': gi.FunctionInfo(set_disable_dependencies), 'set_disable_prune': gi.FunctionInfo(set_disable_prune), 'set_disable_related': gi.FunctionInfo(set_disable_related), 'set_disable_static_deltas': gi.FunctionInfo(set_disable_static_deltas), 'set_force_uninstall': gi.FunctionInfo(set_force_uninstall), 'set_no_deploy': gi.FunctionInfo(set_no_deploy), 'set_no_pull': gi.FunctionInfo(set_no_pull), 'set_parent_window': gi.FunctionInfo(set_parent_window), 'set_reinstall': gi.FunctionInfo(set_reinstall), 'do_add_new_remote': gi.VFuncInfo(add_new_remote), 'do_basic_auth_start': gi.VFuncInfo(basic_auth_start), 'do_choose_remote_for_ref': gi.VFuncInfo(choose_remote_for_ref), 'do_end_of_lifed': gi.VFuncInfo(end_of_lifed), 'do_end_of_lifed_with_rebase': gi.VFuncInfo(end_of_lifed_with_rebase), 'do_new_operation': gi.VFuncInfo(new_operation), 'do_operation_done': gi.VFuncInfo(operation_done), 'do_operation_error': gi.VFuncInfo(operation_error), 'do_ready': gi.VFuncInfo(ready), 'do_run': gi.VFuncInfo(run), 'do_webflow_done': gi.VFuncInfo(webflow_done), 'do_webflow_start': gi.VFuncInfo(webflow_start), 'parent_instance': <property object at 0x7f29534f1270>})"
    __gdoc__ = 'Object FlatpakTransaction\n\nSignals from FlatpakTransaction:\n  new-operation (FlatpakTransactionOperation, FlatpakTransactionProgress)\n  operation-error (FlatpakTransactionOperation, GError, gint) -> gboolean\n  operation-done (FlatpakTransactionOperation, gchararray, gint)\n  choose-remote-for-ref (gchararray, gchararray, GStrv) -> gint\n  end-of-lifed (gchararray, gchararray, gchararray)\n  end-of-lifed-with-rebase (gchararray, gchararray, gchararray, gchararray, GStrv) -> gboolean\n  ready () -> gboolean\n  add-new-remote (gint, gchararray, gchararray, gchararray) -> gboolean\n  webflow-start (gchararray, gchararray, GVariant, gint) -> gboolean\n  webflow-done (GVariant, gint)\n  basic-auth-start (gchararray, gchararray, GVariant, gint) -> gboolean\n\nProperties from FlatpakTransaction:\n  installation -> FlatpakInstallation: Installation\n    The installation instance\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType FlatpakTransaction (94781644122848)>'
    __info__ = ObjectInfo(Transaction)


