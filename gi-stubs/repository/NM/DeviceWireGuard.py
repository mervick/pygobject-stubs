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


from .Device import Device

class DeviceWireGuard(Device):
    """
    :Constructors:
    
    ::
    
        DeviceWireGuard(**properties)
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

    def connection_compatible(self, connection): # real signature unknown; restored from __doc__
        """ connection_compatible(self, connection:NM.Connection) -> bool """
        return False

    def connection_valid(self, connection): # real signature unknown; restored from __doc__
        """ connection_valid(self, connection:NM.Connection) -> bool """
        return False

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

    def delete(self, cancellable=None): # real signature unknown; restored from __doc__
        """ delete(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def disambiguate_names(self, devices): # real signature unknown; restored from __doc__
        """ disambiguate_names(devices:list) -> list """
        return []

    def disconnect(self, cancellable=None): # real signature unknown; restored from __doc__
        """ disconnect(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ disconnect_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect_finish(self, result): # real signature unknown; restored from __doc__
        """ disconnect_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def filter_connections(self, connections): # real signature unknown; restored from __doc__
        """ filter_connections(self, connections:list) -> list """
        return []

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

    def get_active_connection(self): # real signature unknown; restored from __doc__
        """ get_active_connection(self) -> NM.ActiveConnection """
        pass

    def get_applied_connection(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ get_applied_connection(self, flags:int, cancellable:Gio.Cancellable=None) -> NM.Connection, version_id:int """
        pass

    def get_applied_connection_async(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_applied_connection_async(self, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_applied_connection_finish(self, result): # real signature unknown; restored from __doc__
        """ get_applied_connection_finish(self, result:Gio.AsyncResult) -> NM.Connection, version_id:int """
        pass

    def get_autoconnect(self): # real signature unknown; restored from __doc__
        """ get_autoconnect(self) -> bool """
        return False

    def get_available_connections(self): # real signature unknown; restored from __doc__
        """ get_available_connections(self) -> list """
        return []

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> NM.DeviceCapabilities """
        pass

    def get_connectivity(self, addr_family): # real signature unknown; restored from __doc__
        """ get_connectivity(self, addr_family:int) -> NM.ConnectivityState """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_device_type(self): # real signature unknown; restored from __doc__
        """ get_device_type(self) -> NM.DeviceType """
        pass

    def get_dhcp4_config(self): # real signature unknown; restored from __doc__
        """ get_dhcp4_config(self) -> NM.DhcpConfig """
        pass

    def get_dhcp6_config(self): # real signature unknown; restored from __doc__
        """ get_dhcp6_config(self) -> NM.DhcpConfig """
        pass

    def get_driver(self): # real signature unknown; restored from __doc__
        """ get_driver(self) -> str """
        return ""

    def get_driver_version(self): # real signature unknown; restored from __doc__
        """ get_driver_version(self) -> str """
        return ""

    def get_firmware_missing(self): # real signature unknown; restored from __doc__
        """ get_firmware_missing(self) -> bool """
        return False

    def get_firmware_version(self): # real signature unknown; restored from __doc__
        """ get_firmware_version(self) -> str """
        return ""

    def get_fwmark(self): # real signature unknown; restored from __doc__
        """ get_fwmark(self) -> int """
        return 0

    def get_hw_address(self): # real signature unknown; restored from __doc__
        """ get_hw_address(self) -> str """
        return ""

    def get_iface(self): # real signature unknown; restored from __doc__
        """ get_iface(self) -> str """
        return ""

    def get_interface_flags(self): # real signature unknown; restored from __doc__
        """ get_interface_flags(self) -> NM.DeviceInterfaceFlags """
        pass

    def get_ip4_config(self): # real signature unknown; restored from __doc__
        """ get_ip4_config(self) -> NM.IPConfig """
        pass

    def get_ip6_config(self): # real signature unknown; restored from __doc__
        """ get_ip6_config(self) -> NM.IPConfig """
        pass

    def get_ip_iface(self): # real signature unknown; restored from __doc__
        """ get_ip_iface(self) -> str """
        return ""

    def get_listen_port(self): # real signature unknown; restored from __doc__
        """ get_listen_port(self) -> int """
        return 0

    def get_lldp_neighbors(self): # real signature unknown; restored from __doc__
        """ get_lldp_neighbors(self) -> list """
        return []

    def get_managed(self): # real signature unknown; restored from __doc__
        """ get_managed(self) -> bool """
        return False

    def get_metered(self): # real signature unknown; restored from __doc__
        """ get_metered(self) -> NM.Metered """
        pass

    def get_mtu(self): # real signature unknown; restored from __doc__
        """ get_mtu(self) -> int """
        return 0

    def get_nm_plugin_missing(self): # real signature unknown; restored from __doc__
        """ get_nm_plugin_missing(self) -> bool """
        return False

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_physical_port_id(self): # real signature unknown; restored from __doc__
        """ get_physical_port_id(self) -> str """
        return ""

    def get_product(self): # real signature unknown; restored from __doc__
        """ get_product(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_public_key(self): # real signature unknown; restored from __doc__
        """ get_public_key(self) -> GLib.Bytes """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_setting_type(self): # real signature unknown; restored from __doc__
        """ get_setting_type(self) -> GType """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> NM.DeviceState """
        pass

    def get_state_reason(self): # real signature unknown; restored from __doc__
        """ get_state_reason(self) -> NM.DeviceStateReason """
        pass

    def get_type_description(self): # real signature unknown; restored from __doc__
        """ get_type_description(self) -> str """
        return ""

    def get_udi(self): # real signature unknown; restored from __doc__
        """ get_udi(self) -> str """
        return ""

    def get_vendor(self): # real signature unknown; restored from __doc__
        """ get_vendor(self) -> str """
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

    def is_real(self): # real signature unknown; restored from __doc__
        """ is_real(self) -> bool """
        return False

    def is_software(self): # real signature unknown; restored from __doc__
        """ is_software(self) -> bool """
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

    def reapply(self, connection=None, version_id, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ reapply(self, connection:NM.Connection=None, version_id:int, flags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def reapply_async(self, connection=None, version_id, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ reapply_async(self, connection:NM.Connection=None, version_id:int, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def reapply_finish(self, result): # real signature unknown; restored from __doc__
        """ reapply_finish(self, result:Gio.AsyncResult) -> bool """
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

    def set_autoconnect(self, autoconnect): # real signature unknown; restored from __doc__
        """ set_autoconnect(self, autoconnect:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_managed(self, managed): # real signature unknown; restored from __doc__
        """ set_managed(self, managed:bool) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b8467a60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DeviceWireGuard), '__module__': 'gi.repository.NM', '__gtype__': <GType NMDeviceWireGuard (94741104303792)>, '__doc__': None, '__gsignals__': {}, 'get_fwmark': gi.FunctionInfo(get_fwmark), 'get_listen_port': gi.FunctionInfo(get_listen_port), 'get_public_key': gi.FunctionInfo(get_public_key)})"
    __gdoc__ = 'Object NMDeviceWireGuard\n\nProperties from NMDeviceWireGuard:\n  public-key -> GBytes: \n    \n  listen-port -> guint: \n    \n  fwmark -> guint: \n    \n\nSignals from NMDevice:\n  state-changed (guint, guint, guint)\n\nProperties from NMDevice:\n  interface -> gchararray: \n    \n  udi -> gchararray: \n    \n  driver -> gchararray: \n    \n  driver-version -> gchararray: \n    \n  firmware-version -> gchararray: \n    \n  capabilities -> NMDeviceCapabilities: \n    \n  real -> gboolean: \n    \n  managed -> gboolean: \n    \n  autoconnect -> gboolean: \n    \n  firmware-missing -> gboolean: \n    \n  nm-plugin-missing -> gboolean: \n    \n  ip4-config -> NMIPConfig: \n    \n  dhcp4-config -> NMDhcpConfig: \n    \n  ip6-config -> NMIPConfig: \n    \n  state -> NMDeviceState: \n    \n  state-reason -> guint: \n    \n  product -> gchararray: \n    \n  vendor -> gchararray: \n    \n  dhcp6-config -> NMDhcpConfig: \n    \n  ip-interface -> gchararray: \n    \n  device-type -> NMDeviceType: \n    \n  active-connection -> NMActiveConnection: \n    \n  available-connections -> GPtrArray: \n    \n  physical-port-id -> gchararray: \n    \n  mtu -> guint: \n    \n  metered -> guint: \n    \n  lldp-neighbors -> GPtrArray: \n    \n  ip4-connectivity -> NMConnectivityState: \n    \n  ip6-connectivity -> NMConnectivityState: \n    \n  interface-flags -> guint: \n    \n\nProperties from NMObject:\n  path -> gchararray: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMDeviceWireGuard (94741104303792)>'
    __info__ = ObjectInfo(DeviceWireGuard)


