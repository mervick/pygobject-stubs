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


class Connection(__gobject.GInterface):
    # no doc
    def add_setting(self, setting): # real signature unknown; restored from __doc__
        """ add_setting(self, setting:NM.Setting) """
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

    def diff(self, b, flags, out_settings): # real signature unknown; restored from __doc__
        """ diff(self, b:NM.Connection, flags:NM.SettingCompareFlags, out_settings:dict) -> bool """
        return False

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
        pass

    def for_each_setting_value(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ for_each_setting_value(self, func:NM.SettingValueIterFn, user_data=None) """
        pass

    def get_connection_type(self): # real signature unknown; restored from __doc__
        """ get_connection_type(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_interface_name(self): # real signature unknown; restored from __doc__
        """ get_interface_name(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

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

    def is_type(self, type): # real signature unknown; restored from __doc__
        """ is_type(self, type:str) -> bool """
        return False

    def is_virtual(self): # real signature unknown; restored from __doc__
        """ is_virtual(self) -> bool """
        return False

    def need_secrets(self): # real signature unknown; restored from __doc__
        """ need_secrets(self) -> str, hints:list """
        return ""

    def normalize(self, parameters=None): # real signature unknown; restored from __doc__
        """ normalize(self, parameters:dict=None) -> bool, modified:bool """
        return False

    def remove_setting(self, setting_type): # real signature unknown; restored from __doc__
        """ remove_setting(self, setting_type:GType) """
        pass

    def replace_settings(self, new_settings): # real signature unknown; restored from __doc__
        """ replace_settings(self, new_settings:GLib.Variant) -> bool """
        return False

    def replace_settings_from_connection(self, new_connection): # real signature unknown; restored from __doc__
        """ replace_settings_from_connection(self, new_connection:NM.Connection) """
        pass

    def set_path(self, path): # real signature unknown; restored from __doc__
        """ set_path(self, path:str) """
        pass

    def to_dbus(self, flags): # real signature unknown; restored from __doc__
        """ to_dbus(self, flags:NM.ConnectionSerializationFlags) -> GLib.Variant """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Connection), '__module__': 'gi.repository.NM', '__gtype__': <GType NMConnection (94741104175856)>, '__dict__': <attribute '__dict__' of 'Connection' objects>, '__weakref__': <attribute '__weakref__' of 'Connection' objects>, '__doc__': None, '__gsignals__': {}, 'add_setting': gi.FunctionInfo(add_setting), 'clear_secrets': gi.FunctionInfo(clear_secrets), 'clear_secrets_with_flags': gi.FunctionInfo(clear_secrets_with_flags), 'clear_settings': gi.FunctionInfo(clear_settings), 'compare': gi.FunctionInfo(compare), 'diff': gi.FunctionInfo(diff), 'dump': gi.FunctionInfo(dump), 'for_each_setting_value': gi.FunctionInfo(for_each_setting_value), 'get_connection_type': gi.FunctionInfo(get_connection_type), 'get_id': gi.FunctionInfo(get_id), 'get_interface_name': gi.FunctionInfo(get_interface_name), 'get_path': gi.FunctionInfo(get_path), 'get_setting': gi.FunctionInfo(get_setting), 'get_setting_802_1x': gi.FunctionInfo(get_setting_802_1x), 'get_setting_adsl': gi.FunctionInfo(get_setting_adsl), 'get_setting_bluetooth': gi.FunctionInfo(get_setting_bluetooth), 'get_setting_bond': gi.FunctionInfo(get_setting_bond), 'get_setting_bridge': gi.FunctionInfo(get_setting_bridge), 'get_setting_bridge_port': gi.FunctionInfo(get_setting_bridge_port), 'get_setting_by_name': gi.FunctionInfo(get_setting_by_name), 'get_setting_cdma': gi.FunctionInfo(get_setting_cdma), 'get_setting_connection': gi.FunctionInfo(get_setting_connection), 'get_setting_dcb': gi.FunctionInfo(get_setting_dcb), 'get_setting_dummy': gi.FunctionInfo(get_setting_dummy), 'get_setting_generic': gi.FunctionInfo(get_setting_generic), 'get_setting_gsm': gi.FunctionInfo(get_setting_gsm), 'get_setting_infiniband': gi.FunctionInfo(get_setting_infiniband), 'get_setting_ip4_config': gi.FunctionInfo(get_setting_ip4_config), 'get_setting_ip6_config': gi.FunctionInfo(get_setting_ip6_config), 'get_setting_ip_tunnel': gi.FunctionInfo(get_setting_ip_tunnel), 'get_setting_macsec': gi.FunctionInfo(get_setting_macsec), 'get_setting_macvlan': gi.FunctionInfo(get_setting_macvlan), 'get_setting_olpc_mesh': gi.FunctionInfo(get_setting_olpc_mesh), 'get_setting_ovs_bridge': gi.FunctionInfo(get_setting_ovs_bridge), 'get_setting_ovs_interface': gi.FunctionInfo(get_setting_ovs_interface), 'get_setting_ovs_patch': gi.FunctionInfo(get_setting_ovs_patch), 'get_setting_ovs_port': gi.FunctionInfo(get_setting_ovs_port), 'get_setting_ppp': gi.FunctionInfo(get_setting_ppp), 'get_setting_pppoe': gi.FunctionInfo(get_setting_pppoe), 'get_setting_proxy': gi.FunctionInfo(get_setting_proxy), 'get_setting_serial': gi.FunctionInfo(get_setting_serial), 'get_setting_tc_config': gi.FunctionInfo(get_setting_tc_config), 'get_setting_team': gi.FunctionInfo(get_setting_team), 'get_setting_team_port': gi.FunctionInfo(get_setting_team_port), 'get_setting_tun': gi.FunctionInfo(get_setting_tun), 'get_setting_vlan': gi.FunctionInfo(get_setting_vlan), 'get_setting_vpn': gi.FunctionInfo(get_setting_vpn), 'get_setting_vxlan': gi.FunctionInfo(get_setting_vxlan), 'get_setting_wimax': gi.FunctionInfo(get_setting_wimax), 'get_setting_wired': gi.FunctionInfo(get_setting_wired), 'get_setting_wireless': gi.FunctionInfo(get_setting_wireless), 'get_setting_wireless_security': gi.FunctionInfo(get_setting_wireless_security), 'get_settings': gi.FunctionInfo(get_settings), 'get_uuid': gi.FunctionInfo(get_uuid), 'get_virtual_device_description': gi.FunctionInfo(get_virtual_device_description), 'is_type': gi.FunctionInfo(is_type), 'is_virtual': gi.FunctionInfo(is_virtual), 'need_secrets': gi.FunctionInfo(need_secrets), 'normalize': gi.FunctionInfo(normalize), 'remove_setting': gi.FunctionInfo(remove_setting), 'replace_settings': gi.FunctionInfo(replace_settings), 'replace_settings_from_connection': gi.FunctionInfo(replace_settings_from_connection), 'set_path': gi.FunctionInfo(set_path), 'to_dbus': gi.FunctionInfo(to_dbus), 'update_secrets': gi.FunctionInfo(update_secrets), 'verify': gi.FunctionInfo(verify), 'verify_secrets': gi.FunctionInfo(verify_secrets)})"
    __gdoc__ = 'Interface NMConnection\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMConnection (94741104175856)>'
    __info__ = InterfaceInfo(Connection)


