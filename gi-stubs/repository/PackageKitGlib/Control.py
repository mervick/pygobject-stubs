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


class Control(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Control(**properties)
        new() -> PackageKitGlib.Control
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_authorize_async(self, action_id, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ can_authorize_async(self, action_id:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def can_authorize_finish(self, res): # real signature unknown; restored from __doc__
        """ can_authorize_finish(self, res:Gio.AsyncResult) -> PackageKitGlib.AuthorizeEnum """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_connection_changed(self, *args, **kwargs): # real signature unknown
        """ connection_changed(self, connected:bool) """
        pass

    def do_locked(self, *args, **kwargs): # real signature unknown
        """ locked(self, is_locked:bool) """
        pass

    def do_network_state_changed(self, *args, **kwargs): # real signature unknown
        """ network_state_changed(self) """
        pass

    def do_repo_list_changed(self, *args, **kwargs): # real signature unknown
        """ repo_list_changed(self) """
        pass

    def do_restart_schedule(self, *args, **kwargs): # real signature unknown
        """ restart_schedule(self) """
        pass

    def do_transaction_list_changed(self, *args, **kwargs): # real signature unknown
        """ transaction_list_changed(self, transaction_ids:str) """
        pass

    def do_updates_changed(self, *args, **kwargs): # real signature unknown
        """ updates_changed(self) """
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

    def get_daemon_state_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_daemon_state_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_daemon_state_finish(self, res): # real signature unknown; restored from __doc__
        """ get_daemon_state_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_properties(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_properties_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_properties_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_properties_finish(self, res): # real signature unknown; restored from __doc__
        """ get_properties_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_tid_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_tid_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_tid_finish(self, res): # real signature unknown; restored from __doc__
        """ get_tid_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def get_time_since_action_async(self, role, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_time_since_action_async(self, role:PackageKitGlib.RoleEnum, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_time_since_action_finish(self, res): # real signature unknown; restored from __doc__
        """ get_time_since_action_finish(self, res:Gio.AsyncResult) -> int """
        return 0

    def get_transaction_list(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_transaction_list(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_transaction_list_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_transaction_list_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_transaction_list_finish(self, res): # real signature unknown; restored from __doc__
        """ get_transaction_list_finish(self, res:Gio.AsyncResult) -> list """
        return []

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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> PackageKitGlib.Control """
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

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_proxy(self, proxy_http, proxy_ftp, cancellable=None): # real signature unknown; restored from __doc__
        """ set_proxy(self, proxy_http:str, proxy_ftp:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_proxy2(self, proxy_http, proxy_https, proxy_ftp, proxy_socks, no_proxy, pac, cancellable=None): # real signature unknown; restored from __doc__
        """ set_proxy2(self, proxy_http:str, proxy_https:str, proxy_ftp:str, proxy_socks:str, no_proxy:str, pac:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_proxy2_async(self, proxy_http, proxy_https, proxy_ftp, proxy_socks, no_proxy, pac, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_proxy2_async(self, proxy_http:str, proxy_https:str, proxy_ftp:str, proxy_socks:str, no_proxy:str, pac:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_proxy_async(self, proxy_http, proxy_ftp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_proxy_async(self, proxy_http:str, proxy_ftp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_proxy_finish(self, res): # real signature unknown; restored from __doc__
        """ set_proxy_finish(self, res:Gio.AsyncResult) -> bool """
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

    def suggest_daemon_quit(self, cancellable=None): # real signature unknown; restored from __doc__
        """ suggest_daemon_quit(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def suggest_daemon_quit_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ suggest_daemon_quit_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def suggest_daemon_quit_finish(self, res): # real signature unknown; restored from __doc__
        """ suggest_daemon_quit_finish(self, res:Gio.AsyncResult) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f121f8aaa90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Control), '__module__': 'gi.repository.PackageKitGlib', '__gtype__': <GType PkControl (94016446937488)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'can_authorize_async': gi.FunctionInfo(can_authorize_async), 'can_authorize_finish': gi.FunctionInfo(can_authorize_finish), 'get_daemon_state_async': gi.FunctionInfo(get_daemon_state_async), 'get_daemon_state_finish': gi.FunctionInfo(get_daemon_state_finish), 'get_properties': gi.FunctionInfo(get_properties), 'get_properties_async': gi.FunctionInfo(get_properties_async), 'get_properties_finish': gi.FunctionInfo(get_properties_finish), 'get_tid_async': gi.FunctionInfo(get_tid_async), 'get_tid_finish': gi.FunctionInfo(get_tid_finish), 'get_time_since_action_async': gi.FunctionInfo(get_time_since_action_async), 'get_time_since_action_finish': gi.FunctionInfo(get_time_since_action_finish), 'get_transaction_list': gi.FunctionInfo(get_transaction_list), 'get_transaction_list_async': gi.FunctionInfo(get_transaction_list_async), 'get_transaction_list_finish': gi.FunctionInfo(get_transaction_list_finish), 'set_proxy': gi.FunctionInfo(set_proxy), 'set_proxy2': gi.FunctionInfo(set_proxy2), 'set_proxy2_async': gi.FunctionInfo(set_proxy2_async), 'set_proxy_async': gi.FunctionInfo(set_proxy_async), 'set_proxy_finish': gi.FunctionInfo(set_proxy_finish), 'suggest_daemon_quit': gi.FunctionInfo(suggest_daemon_quit), 'suggest_daemon_quit_async': gi.FunctionInfo(suggest_daemon_quit_async), 'suggest_daemon_quit_finish': gi.FunctionInfo(suggest_daemon_quit_finish), 'do_connection_changed': gi.VFuncInfo(connection_changed), 'do_locked': gi.VFuncInfo(locked), 'do_network_state_changed': gi.VFuncInfo(network_state_changed), 'do_repo_list_changed': gi.VFuncInfo(repo_list_changed), 'do_restart_schedule': gi.VFuncInfo(restart_schedule), 'do_transaction_list_changed': gi.VFuncInfo(transaction_list_changed), 'do_updates_changed': gi.VFuncInfo(updates_changed), 'parent': <property object at 0x7f121fb32ea0>, 'priv': <property object at 0x7f121fb32f90>})"
    __gdoc__ = 'Object PkControl\n\nSignals from PkControl:\n  updates-changed ()\n  repo-list-changed ()\n  restart-schedule ()\n  transaction-list-changed (GStrv)\n\nProperties from PkControl:\n  version-major -> guint: version-major\n  version-minor -> guint: version-minor\n  version-micro -> guint: version-micro\n  backend-name -> gchararray: backend-name\n  backend-description -> gchararray: backend-description\n  backend-author -> gchararray: backend-author\n  roles -> guint64: roles\n  groups -> guint64: groups\n  filters -> guint64: filters\n  provides -> guint64: provides\n  mime-types -> GStrv: mime-types\n  locked -> gboolean: locked\n  network-state -> PkNetworkEnum: network-state\n  connected -> gboolean: connected\n  distro-id -> gchararray: distro-id\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PkControl (94016446937488)>'
    __info__ = ObjectInfo(Control)


