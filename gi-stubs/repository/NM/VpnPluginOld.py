# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


class VpnPluginOld(__gi_overrides_GObject.Object, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        VpnPluginOld(**properties)
    """
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

    def disconnect(self): # real signature unknown; restored from __doc__
        """ disconnect(self) -> bool """
        return False

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_config(self, *args, **kwargs): # real signature unknown
        """ config(self, config:GLib.Variant) """
        pass

    def do_connect(self, *args, **kwargs): # real signature unknown
        """ connect(self, connection:NM.Connection) -> bool """
        pass

    def do_connect_interactive(self, *args, **kwargs): # real signature unknown
        """ connect_interactive(self, connection:NM.Connection, details:GLib.Variant) -> bool """
        pass

    def do_disconnect(self, *args, **kwargs): # real signature unknown
        """ disconnect(self) -> bool """
        pass

    def do_failure(self, *args, **kwargs): # real signature unknown
        """ failure(self, reason:NM.VpnPluginFailure) """
        pass

    def do_ip4_config(self, *args, **kwargs): # real signature unknown
        """ ip4_config(self, ip4_config:GLib.Variant) """
        pass

    def do_ip6_config(self, *args, **kwargs): # real signature unknown
        """ ip6_config(self, config:GLib.Variant) """
        pass

    def do_login_banner(self, *args, **kwargs): # real signature unknown
        """ login_banner(self, banner:str) """
        pass

    def do_need_secrets(self, *args, **kwargs): # real signature unknown
        """ need_secrets(self, connection:NM.Connection, setting_name:str) -> bool """
        pass

    def do_new_secrets(self, *args, **kwargs): # real signature unknown
        """ new_secrets(self, connection:NM.Connection) -> bool """
        pass

    def do_quit(self, *args, **kwargs): # real signature unknown
        """ quit(self) """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, state:NM.VpnServiceState) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def failure(self, reason): # real signature unknown; restored from __doc__
        """ failure(self, reason:NM.VpnPluginFailure) """
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

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_secret_flags(self, data, secret_name): # real signature unknown; restored from __doc__
        """ get_secret_flags(data:dict, secret_name:str) -> bool, out_flags:NM.SettingSecretFlags """
        return False

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> NM.VpnServiceState """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

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

    def read_vpn_details(self, fd): # real signature unknown; restored from __doc__
        """ read_vpn_details(fd:int) -> bool, out_data:dict, out_secrets:dict """
        return False

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

    def secrets_required(self, message, hints): # real signature unknown; restored from __doc__
        """ secrets_required(self, message:str, hints:str) """
        pass

    def set_config(self, config): # real signature unknown; restored from __doc__
        """ set_config(self, config:GLib.Variant) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_ip4_config(self, ip4_config): # real signature unknown; restored from __doc__
        """ set_ip4_config(self, ip4_config:GLib.Variant) """
        pass

    def set_ip6_config(self, ip6_config): # real signature unknown; restored from __doc__
        """ set_ip6_config(self, ip6_config:GLib.Variant) """
        pass

    def set_login_banner(self, banner): # real signature unknown; restored from __doc__
        """ set_login_banner(self, banner:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:NM.VpnServiceState) """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b7e906d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(VpnPluginOld), '__module__': 'gi.repository.NM', '__gtype__': <GType NMVpnPluginOld (94741104712400)>, '__doc__': None, '__gsignals__': {}, 'get_secret_flags': gi.FunctionInfo(get_secret_flags), 'read_vpn_details': gi.FunctionInfo(read_vpn_details), 'disconnect': gi.FunctionInfo(disconnect), 'failure': gi.FunctionInfo(failure), 'get_connection': gi.FunctionInfo(get_connection), 'get_state': gi.FunctionInfo(get_state), 'secrets_required': gi.FunctionInfo(secrets_required), 'set_config': gi.FunctionInfo(set_config), 'set_ip4_config': gi.FunctionInfo(set_ip4_config), 'set_ip6_config': gi.FunctionInfo(set_ip6_config), 'set_login_banner': gi.FunctionInfo(set_login_banner), 'set_state': gi.FunctionInfo(set_state), 'do_config': gi.VFuncInfo(config), 'do_connect': gi.VFuncInfo(connect), 'do_connect_interactive': gi.VFuncInfo(connect_interactive), 'do_disconnect': gi.VFuncInfo(disconnect), 'do_failure': gi.VFuncInfo(failure), 'do_ip4_config': gi.VFuncInfo(ip4_config), 'do_ip6_config': gi.VFuncInfo(ip6_config), 'do_login_banner': gi.VFuncInfo(login_banner), 'do_need_secrets': gi.VFuncInfo(need_secrets), 'do_new_secrets': gi.VFuncInfo(new_secrets), 'do_quit': gi.VFuncInfo(quit), 'do_state_changed': gi.VFuncInfo(state_changed), 'parent': <property object at 0x7fb9b84ad0e0>})"
    __gdoc__ = 'Object NMVpnPluginOld\n\nSignals from NMVpnPluginOld:\n  ip4-config (GVariant)\n  ip6-config (GVariant)\n  state-changed (guint)\n  config (GVariant)\n  secrets-required (gchararray, GStrv)\n  login-banner (gchararray)\n  failure (guint)\n  quit ()\n\nProperties from NMVpnPluginOld:\n  service-name -> gchararray: \n    \n  state -> NMVpnServiceState: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMVpnPluginOld (94741104712400)>'
    __info__ = ObjectInfo(VpnPluginOld)


