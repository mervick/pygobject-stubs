# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .GdbusObjectManagerClient import GdbusObjectManagerClient

class Manager(GdbusObjectManagerClient):
    """
    :Constructors:
    
    ::
    
        Manager(**properties)
        new_finish(res:Gio.AsyncResult) -> ModemManager.Manager
        new_sync(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, cancellable:Gio.Cancellable=None) -> ModemManager.Manager
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_interface_proxy_properties_changed(self, *args, **kwargs): # real signature unknown
        """ interface_proxy_properties_changed(self, object_proxy:Gio.DBusObjectProxy, interface_proxy:Gio.DBusProxy, changed_properties:GLib.Variant, invalidated_properties:str) """
        pass

    def do_interface_proxy_signal(self, *args, **kwargs): # real signature unknown
        """ interface_proxy_signal(self, object_proxy:Gio.DBusObjectProxy, interface_proxy:Gio.DBusProxy, sender_name:str, signal_name:str, parameters:GLib.Variant) """
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

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.DBusObjectManagerClientFlags """
        pass

    def get_interface(self, object_path, interface_name): # real signature unknown; restored from __doc__
        """ get_interface(self, object_path:str, interface_name:str) -> Gio.DBusInterface """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_name_owner(self): # real signature unknown; restored from __doc__
        """ get_name_owner(self) -> str or None """
        return ""

    def get_object(self, object_path): # real signature unknown; restored from __doc__
        """ get_object(self, object_path:str) -> Gio.DBusObject """
        pass

    def get_objects(self): # real signature unknown; restored from __doc__
        """ get_objects(self) -> list """
        return []

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_proxy(self): # real signature unknown; restored from __doc__
        """ get_proxy(self) -> Gio.DBusProxy """
        pass

    def get_proxy_type(self, manager, object_path, interface_name=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_proxy_type(manager:Gio.DBusObjectManagerClient, object_path:str, interface_name:str=None, user_data=None) -> GType """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
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

    def inhibit_device(self, uid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ inhibit_device(self, uid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def inhibit_device_finish(self, res): # real signature unknown; restored from __doc__
        """ inhibit_device_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def inhibit_device_sync(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ inhibit_device_sync(self, uid:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_finish(self, res): # real signature unknown; restored from __doc__
        """ init_finish(self, res:Gio.AsyncResult) -> bool """
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

    def new(self, connection, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, res): # real signature unknown; restored from __doc__
        """ new_finish(res:Gio.AsyncResult) -> ModemManager.Manager """
        pass

    def new_for_bus(self, bus_type, flags, name, object_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_for_bus(bus_type:Gio.BusType, flags:Gio.DBusObjectManagerClientFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_for_bus_finish(self, res): # real signature unknown; restored from __doc__
        """ new_for_bus_finish(res:Gio.AsyncResult) -> ModemManager.GdbusObjectManagerClient """
        pass

    def new_for_bus_sync(self, bus_type, flags, name, object_path, cancellable=None): # real signature unknown; restored from __doc__
        """ new_for_bus_sync(bus_type:Gio.BusType, flags:Gio.DBusObjectManagerClientFlags, name:str, object_path:str, cancellable:Gio.Cancellable=None) -> ModemManager.GdbusObjectManagerClient """
        pass

    def new_sync(self, connection, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ new_sync(connection:Gio.DBusConnection, flags:Gio.DBusObjectManagerClientFlags, cancellable:Gio.Cancellable=None) -> ModemManager.Manager """
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

    def peek_proxy(self): # real signature unknown; restored from __doc__
        """ peek_proxy(self) -> Gio.DBusProxy """
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

    def report_kernel_event(self, properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ report_kernel_event(self, properties:ModemManager.KernelEventProperties, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def report_kernel_event_finish(self, res): # real signature unknown; restored from __doc__
        """ report_kernel_event_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def report_kernel_event_sync(self, properties, cancellable=None): # real signature unknown; restored from __doc__
        """ report_kernel_event_sync(self, properties:ModemManager.KernelEventProperties, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def scan_devices(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ scan_devices(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def scan_devices_finish(self, res): # real signature unknown; restored from __doc__
        """ scan_devices_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def scan_devices_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ scan_devices_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_logging(self, level, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_logging(self, level:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_logging_finish(self, res): # real signature unknown; restored from __doc__
        """ set_logging_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_logging_sync(self, level, cancellable=None): # real signature unknown; restored from __doc__
        """ set_logging_sync(self, level:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def uninhibit_device(self, uid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ uninhibit_device(self, uid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def uninhibit_device_finish(self, res): # real signature unknown; restored from __doc__
        """ uninhibit_device_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def uninhibit_device_sync(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ uninhibit_device_sync(self, uid:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f694371ddf0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Manager), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MMManager (94631948617360)>, '__doc__': None, '__gsignals__': {}, 'new_finish': gi.FunctionInfo(new_finish), 'new_sync': gi.FunctionInfo(new_sync), 'new': gi.FunctionInfo(new), 'get_proxy': gi.FunctionInfo(get_proxy), 'get_version': gi.FunctionInfo(get_version), 'inhibit_device': gi.FunctionInfo(inhibit_device), 'inhibit_device_finish': gi.FunctionInfo(inhibit_device_finish), 'inhibit_device_sync': gi.FunctionInfo(inhibit_device_sync), 'peek_proxy': gi.FunctionInfo(peek_proxy), 'report_kernel_event': gi.FunctionInfo(report_kernel_event), 'report_kernel_event_finish': gi.FunctionInfo(report_kernel_event_finish), 'report_kernel_event_sync': gi.FunctionInfo(report_kernel_event_sync), 'scan_devices': gi.FunctionInfo(scan_devices), 'scan_devices_finish': gi.FunctionInfo(scan_devices_finish), 'scan_devices_sync': gi.FunctionInfo(scan_devices_sync), 'set_logging': gi.FunctionInfo(set_logging), 'set_logging_finish': gi.FunctionInfo(set_logging_finish), 'set_logging_sync': gi.FunctionInfo(set_logging_sync), 'uninhibit_device': gi.FunctionInfo(uninhibit_device), 'uninhibit_device_finish': gi.FunctionInfo(uninhibit_device_finish), 'uninhibit_device_sync': gi.FunctionInfo(uninhibit_device_sync), 'parent': <property object at 0x7f69438a1090>, 'priv': <property object at 0x7f69438a1180>})"
    __gdoc__ = 'Object MMManager\n\nSignals from GDBusObjectManager:\n  object-added (GDBusObject)\n  object-removed (GDBusObject)\n  interface-added (GDBusObject, GDBusInterface)\n  interface-removed (GDBusObject, GDBusInterface)\n\nSignals from GDBusObjectManager:\n  object-added (GDBusObject)\n  object-removed (GDBusObject)\n  interface-added (GDBusObject, GDBusInterface)\n  interface-removed (GDBusObject, GDBusInterface)\n\nSignals from GDBusObjectManagerClient:\n  interface-proxy-signal (GDBusObjectProxy, GDBusProxy, gchararray, gchararray, GVariant)\n  interface-proxy-properties-changed (GDBusObjectProxy, GDBusProxy, GVariant, GStrv)\n\nProperties from GDBusObjectManagerClient:\n  bus-type -> GBusType: Bus Type\n    The bus to connect to, if any\n  connection -> GDBusConnection: Connection\n    The connection to use\n  flags -> GDBusObjectManagerClientFlags: Flags\n    Flags for the proxy manager\n  object-path -> gchararray: Object Path\n    The object path of the control object\n  name -> gchararray: Name\n    Name that the manager is for\n  name-owner -> gchararray: Name Owner\n    The owner of the name we are watching\n  get-proxy-type-func -> gpointer: GDBusProxyTypeFunc Function Pointer\n    The GDBusProxyTypeFunc pointer to use\n  get-proxy-type-user-data -> gpointer: GDBusProxyTypeFunc User Data\n    The GDBusProxyTypeFunc user_data\n  get-proxy-type-destroy-notify -> gpointer: GDBusProxyTypeFunc user data free function\n    The GDBusProxyTypeFunc user data free function\n\nSignals from GDBusObjectManager:\n  object-added (GDBusObject)\n  object-removed (GDBusObject)\n  interface-added (GDBusObject, GDBusInterface)\n  interface-removed (GDBusObject, GDBusInterface)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MMManager (94631948617360)>'
    __info__ = ObjectInfo(Manager)


