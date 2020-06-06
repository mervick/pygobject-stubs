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


from .Connection import Connection

class SimpleConnection(__gi_overrides_GObject.Object, Connection):
    """
    :Constructors:
    
    ::
    
        SimpleConnection(**properties)
    """
    def add_setting(self, setting): # real signature unknown; restored from __doc__
        """ add_setting(self, setting:NM.Setting) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_secrets(self): # real signature unknown; restored from __doc__
        """ clear_secrets(self) """
        pass

    def clear_secrets_with_flags(self, func=None, user_data=None): # real signature unknown; restored from __doc__
        """ clear_secrets_with_flags(self, func:NM.SettingClearSecretsWithFlagsFn=None, user_data=None) """
        pass

    def clear_settings(self): # real signature unknown; restored from __doc__
        """ clear_settings(self) """
        pass

    def compare(self, b, flags): # real signature unknown; restored from __doc__
        """ compare(self, b:NM.Connection, flags:NM.SettingCompareFlags) -> bool """
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

    def diff(self, b, flags, out_settings): # real signature unknown; restored from __doc__
        """ diff(self, b:NM.Connection, flags:NM.SettingCompareFlags, out_settings:dict) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
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

    def for_each_setting_value(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ for_each_setting_value(self, func:NM.SettingValueIterFn, user_data=None) """
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

    def get_connection_type(self): # real signature unknown; restored from __doc__
        """ get_connection_type(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_interface_name(self): # real signature unknown; restored from __doc__
        """ get_interface_name(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_setting(self, setting_type): # real signature unknown; restored from __doc__
        """ get_setting(self, setting_type:GType) -> NM.Setting """
        pass

    def get_settings(self): # real signature unknown; restored from __doc__
        """ get_settings(self) -> list, out_length:int """
        return []

    def get_setting_802_1x(self): # real signature unknown; restored from __doc__
        """ get_setting_802_1x(self) -> NM.Setting8021x """
        pass

    def get_setting_adsl(self): # real signature unknown; restored from __doc__
        """ get_setting_adsl(self) -> NM.SettingAdsl """
        pass

    def get_setting_bluetooth(self): # real signature unknown; restored from __doc__
        """ get_setting_bluetooth(self) -> NM.SettingBluetooth """
        pass

    def get_setting_bond(self): # real signature unknown; restored from __doc__
        """ get_setting_bond(self) -> NM.SettingBond """
        pass

    def get_setting_bridge(self): # real signature unknown; restored from __doc__
        """ get_setting_bridge(self) -> NM.SettingBridge """
        pass

    def get_setting_bridge_port(self): # real signature unknown; restored from __doc__
        """ get_setting_bridge_port(self) -> NM.SettingBridgePort """
        pass

    def get_setting_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_setting_by_name(self, name:str) -> NM.Setting """
        pass

    def get_setting_cdma(self): # real signature unknown; restored from __doc__
        """ get_setting_cdma(self) -> NM.SettingCdma """
        pass

    def get_setting_connection(self): # real signature unknown; restored from __doc__
        """ get_setting_connection(self) -> NM.SettingConnection """
        pass

    def get_setting_dcb(self): # real signature unknown; restored from __doc__
        """ get_setting_dcb(self) -> NM.SettingDcb """
        pass

    def get_setting_dummy(self): # real signature unknown; restored from __doc__
        """ get_setting_dummy(self) -> NM.SettingDummy """
        pass

    def get_setting_generic(self): # real signature unknown; restored from __doc__
        """ get_setting_generic(self) -> NM.SettingGeneric """
        pass

    def get_setting_gsm(self): # real signature unknown; restored from __doc__
        """ get_setting_gsm(self) -> NM.SettingGsm """
        pass

    def get_setting_infiniband(self): # real signature unknown; restored from __doc__
        """ get_setting_infiniband(self) -> NM.SettingInfiniband """
        pass

    def get_setting_ip4_config(self): # real signature unknown; restored from __doc__
        """ get_setting_ip4_config(self) -> NM.SettingIP4Config """
        pass

    def get_setting_ip6_config(self): # real signature unknown; restored from __doc__
        """ get_setting_ip6_config(self) -> NM.SettingIP6Config """
        pass

    def get_setting_ip_tunnel(self): # real signature unknown; restored from __doc__
        """ get_setting_ip_tunnel(self) -> NM.SettingIPTunnel """
        pass

    def get_setting_macsec(self): # real signature unknown; restored from __doc__
        """ get_setting_macsec(self) -> NM.SettingMacsec """
        pass

    def get_setting_macvlan(self): # real signature unknown; restored from __doc__
        """ get_setting_macvlan(self) -> NM.SettingMacvlan """
        pass

    def get_setting_olpc_mesh(self): # real signature unknown; restored from __doc__
        """ get_setting_olpc_mesh(self) -> NM.SettingOlpcMesh """
        pass

    def get_setting_ovs_bridge(self): # real signature unknown; restored from __doc__
        """ get_setting_ovs_bridge(self) -> NM.SettingOvsBridge """
        pass

    def get_setting_ovs_interface(self): # real signature unknown; restored from __doc__
        """ get_setting_ovs_interface(self) -> NM.SettingOvsInterface """
        pass

    def get_setting_ovs_patch(self): # real signature unknown; restored from __doc__
        """ get_setting_ovs_patch(self) -> NM.SettingOvsPatch """
        pass

    def get_setting_ovs_port(self): # real signature unknown; restored from __doc__
        """ get_setting_ovs_port(self) -> NM.SettingOvsPort """
        pass

    def get_setting_ppp(self): # real signature unknown; restored from __doc__
        """ get_setting_ppp(self) -> NM.SettingPpp """
        pass

    def get_setting_pppoe(self): # real signature unknown; restored from __doc__
        """ get_setting_pppoe(self) -> NM.SettingPppoe """
        pass

    def get_setting_proxy(self): # real signature unknown; restored from __doc__
        """ get_setting_proxy(self) -> NM.SettingProxy """
        pass

    def get_setting_serial(self): # real signature unknown; restored from __doc__
        """ get_setting_serial(self) -> NM.SettingSerial """
        pass

    def get_setting_tc_config(self): # real signature unknown; restored from __doc__
        """ get_setting_tc_config(self) -> NM.SettingTCConfig """
        pass

    def get_setting_team(self): # real signature unknown; restored from __doc__
        """ get_setting_team(self) -> NM.SettingTeam """
        pass

    def get_setting_team_port(self): # real signature unknown; restored from __doc__
        """ get_setting_team_port(self) -> NM.SettingTeamPort """
        pass

    def get_setting_tun(self): # real signature unknown; restored from __doc__
        """ get_setting_tun(self) -> NM.SettingTun """
        pass

    def get_setting_vlan(self): # real signature unknown; restored from __doc__
        """ get_setting_vlan(self) -> NM.SettingVlan """
        pass

    def get_setting_vpn(self): # real signature unknown; restored from __doc__
        """ get_setting_vpn(self) -> NM.SettingVpn """
        pass

    def get_setting_vxlan(self): # real signature unknown; restored from __doc__
        """ get_setting_vxlan(self) -> NM.SettingVxlan """
        pass

    def get_setting_wimax(self): # real signature unknown; restored from __doc__
        """ get_setting_wimax(self) -> NM.SettingWimax """
        pass

    def get_setting_wired(self): # real signature unknown; restored from __doc__
        """ get_setting_wired(self) -> NM.SettingWired """
        pass

    def get_setting_wireless(self): # real signature unknown; restored from __doc__
        """ get_setting_wireless(self) -> NM.SettingWireless """
        pass

    def get_setting_wireless_security(self): # real signature unknown; restored from __doc__
        """ get_setting_wireless_security(self) -> NM.SettingWirelessSecurity """
        pass

    def get_uuid(self): # real signature unknown; restored from __doc__
        """ get_uuid(self) -> str """
        return ""

    def get_virtual_device_description(self): # real signature unknown; restored from __doc__
        """ get_virtual_device_description(self) -> str """
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

    def is_type(self, type): # real signature unknown; restored from __doc__
        """ is_type(self, type:str) -> bool """
        return False

    def is_virtual(self): # real signature unknown; restored from __doc__
        """ is_virtual(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def need_secrets(self): # real signature unknown; restored from __doc__
        """ need_secrets(self) -> str, hints:list """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> NM.Connection """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_clone(self, connection): # real signature unknown; restored from __doc__
        """ new_clone(connection:NM.Connection) -> NM.Connection """
        pass

    def new_from_dbus(self, dict): # real signature unknown; restored from __doc__
        """ new_from_dbus(dict:GLib.Variant) -> NM.Connection """
        pass

    def normalize(self, parameters=None): # real signature unknown; restored from __doc__
        """ normalize(self, parameters:dict=None) -> bool, modified:bool """
        return False

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

    def remove_setting(self, setting_type): # real signature unknown; restored from __doc__
        """ remove_setting(self, setting_type:GType) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_settings(self, new_settings): # real signature unknown; restored from __doc__
        """ replace_settings(self, new_settings:GLib.Variant) -> bool """
        return False

    def replace_settings_from_connection(self, new_connection): # real signature unknown; restored from __doc__
        """ replace_settings_from_connection(self, new_connection:NM.Connection) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_path(self, path): # real signature unknown; restored from __doc__
        """ set_path(self, path:str) """
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

    def to_dbus(self, flags): # real signature unknown; restored from __doc__
        """ to_dbus(self, flags:NM.ConnectionSerializationFlags) -> GLib.Variant """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update_secrets(self, setting_name, secrets): # real signature unknown; restored from __doc__
        """ update_secrets(self, setting_name:str, secrets:GLib.Variant) -> bool """
        return False

    def verify(self): # real signature unknown; restored from __doc__
        """ verify(self) -> bool """
        return False

    def verify_secrets(self): # real signature unknown; restored from __doc__
        """ verify_secrets(self) -> bool """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b7caac70>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SimpleConnection), '__module__': 'gi.repository.NM', '__gtype__': <GType NMSimpleConnection (94741104641120)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_clone': gi.FunctionInfo(new_clone), 'new_from_dbus': gi.FunctionInfo(new_from_dbus), 'parent': <property object at 0x7fb9b849d1d0>})"
    __gdoc__ = 'Object NMSimpleConnection\n\nSignals from NMConnection:\n  secrets-updated (gchararray)\n  secrets-cleared ()\n  changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMSimpleConnection (94741104641120)>'
    __info__ = ObjectInfo(SimpleConnection)


