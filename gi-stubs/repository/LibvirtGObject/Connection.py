# encoding: utf-8
# module gi.repository.LibvirtGObject
# from /usr/lib64/girepository-1.0/LibvirtGObject-1.0.typelib
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


class Connection(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Connection(**properties)
        new(uri:str) -> LibvirtGObject.Connection
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
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

    def create_domain(self, conf): # real signature unknown; restored from __doc__
        """ create_domain(self, conf:LibvirtGConfig.Domain) -> LibvirtGObject.Domain """
        pass

    def create_storage_pool(self, conf, flags): # real signature unknown; restored from __doc__
        """ create_storage_pool(self, conf:LibvirtGConfig.StoragePool, flags:int) -> LibvirtGObject.StoragePool """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_connection_closed(self, *args, **kwargs): # real signature unknown
        """ connection_closed(self) """
        pass

    def do_connection_opened(self, *args, **kwargs): # real signature unknown
        """ connection_opened(self) """
        pass

    def do_domain_added(self, *args, **kwargs): # real signature unknown
        """ domain_added(self, dom:LibvirtGObject.Domain) """
        pass

    def do_domain_removed(self, *args, **kwargs): # real signature unknown
        """ domain_removed(self, dom:LibvirtGObject.Domain) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def fetch_domains(self, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_domains(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def fetch_domains_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ fetch_domains_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def fetch_domains_finish(self, result): # real signature unknown; restored from __doc__
        """ fetch_domains_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def fetch_interfaces(self, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_interfaces(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def fetch_interfaces_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ fetch_interfaces_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def fetch_interfaces_finish(self, result): # real signature unknown; restored from __doc__
        """ fetch_interfaces_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def fetch_networks(self, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_networks(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def fetch_networks_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ fetch_networks_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def fetch_networks_finish(self, result): # real signature unknown; restored from __doc__
        """ fetch_networks_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def fetch_storage_pools(self, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_storage_pools(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def fetch_storage_pools_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ fetch_storage_pools_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def fetch_storage_pools_finish(self, result): # real signature unknown; restored from __doc__
        """ fetch_storage_pools_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def find_domain_by_id(self, id): # real signature unknown; restored from __doc__
        """ find_domain_by_id(self, id:int) -> LibvirtGObject.Domain """
        pass

    def find_domain_by_name(self, name): # real signature unknown; restored from __doc__
        """ find_domain_by_name(self, name:str) -> LibvirtGObject.Domain """
        pass

    def find_interface_by_mac(self, macaddr): # real signature unknown; restored from __doc__
        """ find_interface_by_mac(self, macaddr:str) -> LibvirtGObject.Interface """
        pass

    def find_network_by_name(self, name): # real signature unknown; restored from __doc__
        """ find_network_by_name(self, name:str) -> LibvirtGObject.Network """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_storage_pool_by_name(self, name): # real signature unknown; restored from __doc__
        """ find_storage_pool_by_name(self, name:str) -> LibvirtGObject.StoragePool """
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

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> LibvirtGConfig.Capabilities """
        pass

    def get_capabilities_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_capabilities_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_capabilities_finish(self, result): # real signature unknown; restored from __doc__
        """ get_capabilities_finish(self, result:Gio.AsyncResult) -> LibvirtGConfig.Capabilities """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_domain(self, uuid): # real signature unknown; restored from __doc__
        """ get_domain(self, uuid:str) -> LibvirtGObject.Domain """
        pass

    def get_domains(self): # real signature unknown; restored from __doc__
        """ get_domains(self) -> list """
        return []

    def get_domain_capabilities(self, emulatorbin=None, arch=None, machine=None, virttype=None, flags): # real signature unknown; restored from __doc__
        """ get_domain_capabilities(self, emulatorbin:str=None, arch:str=None, machine:str=None, virttype:str=None, flags:int) -> LibvirtGConfig.DomainCapabilities """
        pass

    def get_domain_capabilities_async(self, emulatorbin=None, arch=None, machine=None, virttype=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_domain_capabilities_async(self, emulatorbin:str=None, arch:str=None, machine:str=None, virttype:str=None, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_domain_capabilities_finish(self, result): # real signature unknown; restored from __doc__
        """ get_domain_capabilities_finish(self, result:Gio.AsyncResult) -> LibvirtGConfig.DomainCapabilities """
        pass

    def get_hypervisor_name(self): # real signature unknown; restored from __doc__
        """ get_hypervisor_name(self) -> str """
        return ""

    def get_interface(self, name): # real signature unknown; restored from __doc__
        """ get_interface(self, name:str) -> LibvirtGObject.Interface """
        pass

    def get_interfaces(self): # real signature unknown; restored from __doc__
        """ get_interfaces(self) -> list """
        return []

    def get_network(self, uuid): # real signature unknown; restored from __doc__
        """ get_network(self, uuid:str) -> LibvirtGObject.Network """
        pass

    def get_networks(self): # real signature unknown; restored from __doc__
        """ get_networks(self) -> list """
        return []

    def get_node_info(self): # real signature unknown; restored from __doc__
        """ get_node_info(self) -> LibvirtGObject.NodeInfo """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_storage_pool(self, uuid): # real signature unknown; restored from __doc__
        """ get_storage_pool(self, uuid:str) -> LibvirtGObject.StoragePool """
        pass

    def get_storage_pools(self): # real signature unknown; restored from __doc__
        """ get_storage_pools(self) -> list """
        return []

    def get_stream(self, flags): # real signature unknown; restored from __doc__
        """ get_stream(self, flags:int) -> LibvirtGObject.Stream """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> int """
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

    def is_open(self): # real signature unknown; restored from __doc__
        """ is_open(self) -> bool """
        return False

    def is_read_only(self): # real signature unknown; restored from __doc__
        """ is_read_only(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, uri): # real signature unknown; restored from __doc__
        """ new(uri:str) -> LibvirtGObject.Connection """
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

    def open(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def open_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def open_read_only(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open_read_only(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def open_read_only_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_read_only_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_read_only_finish(self, result): # real signature unknown; restored from __doc__
        """ open_read_only_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def restore_domain_from_file(self, filename, custom_conf=None, flags): # real signature unknown; restored from __doc__
        """ restore_domain_from_file(self, filename:str, custom_conf:LibvirtGConfig.Domain=None, flags:int) -> bool """
        return False

    def restore_domain_from_file_async(self, filename, custom_conf=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ restore_domain_from_file_async(self, filename:str, custom_conf:LibvirtGConfig.Domain=None, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def restore_domain_from_file_finish(self, result): # real signature unknown; restored from __doc__
        """ restore_domain_from_file_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def start_domain(self, conf, flags): # real signature unknown; restored from __doc__
        """ start_domain(self, conf:LibvirtGConfig.Domain, flags:int) -> LibvirtGObject.Domain """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffa6f9a27c0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Connection), '__module__': 'gi.repository.LibvirtGObject', '__gtype__': <GType GVirConnection (94394875739328)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'close': gi.FunctionInfo(close), 'create_domain': gi.FunctionInfo(create_domain), 'create_storage_pool': gi.FunctionInfo(create_storage_pool), 'fetch_domains': gi.FunctionInfo(fetch_domains), 'fetch_domains_async': gi.FunctionInfo(fetch_domains_async), 'fetch_domains_finish': gi.FunctionInfo(fetch_domains_finish), 'fetch_interfaces': gi.FunctionInfo(fetch_interfaces), 'fetch_interfaces_async': gi.FunctionInfo(fetch_interfaces_async), 'fetch_interfaces_finish': gi.FunctionInfo(fetch_interfaces_finish), 'fetch_networks': gi.FunctionInfo(fetch_networks), 'fetch_networks_async': gi.FunctionInfo(fetch_networks_async), 'fetch_networks_finish': gi.FunctionInfo(fetch_networks_finish), 'fetch_storage_pools': gi.FunctionInfo(fetch_storage_pools), 'fetch_storage_pools_async': gi.FunctionInfo(fetch_storage_pools_async), 'fetch_storage_pools_finish': gi.FunctionInfo(fetch_storage_pools_finish), 'find_domain_by_id': gi.FunctionInfo(find_domain_by_id), 'find_domain_by_name': gi.FunctionInfo(find_domain_by_name), 'find_interface_by_mac': gi.FunctionInfo(find_interface_by_mac), 'find_network_by_name': gi.FunctionInfo(find_network_by_name), 'find_storage_pool_by_name': gi.FunctionInfo(find_storage_pool_by_name), 'get_capabilities': gi.FunctionInfo(get_capabilities), 'get_capabilities_async': gi.FunctionInfo(get_capabilities_async), 'get_capabilities_finish': gi.FunctionInfo(get_capabilities_finish), 'get_domain': gi.FunctionInfo(get_domain), 'get_domain_capabilities': gi.FunctionInfo(get_domain_capabilities), 'get_domain_capabilities_async': gi.FunctionInfo(get_domain_capabilities_async), 'get_domain_capabilities_finish': gi.FunctionInfo(get_domain_capabilities_finish), 'get_domains': gi.FunctionInfo(get_domains), 'get_hypervisor_name': gi.FunctionInfo(get_hypervisor_name), 'get_interface': gi.FunctionInfo(get_interface), 'get_interfaces': gi.FunctionInfo(get_interfaces), 'get_network': gi.FunctionInfo(get_network), 'get_networks': gi.FunctionInfo(get_networks), 'get_node_info': gi.FunctionInfo(get_node_info), 'get_storage_pool': gi.FunctionInfo(get_storage_pool), 'get_storage_pools': gi.FunctionInfo(get_storage_pools), 'get_stream': gi.FunctionInfo(get_stream), 'get_uri': gi.FunctionInfo(get_uri), 'get_version': gi.FunctionInfo(get_version), 'is_open': gi.FunctionInfo(is_open), 'is_read_only': gi.FunctionInfo(is_read_only), 'open': gi.FunctionInfo(open), 'open_async': gi.FunctionInfo(open_async), 'open_finish': gi.FunctionInfo(open_finish), 'open_read_only': gi.FunctionInfo(open_read_only), 'open_read_only_async': gi.FunctionInfo(open_read_only_async), 'open_read_only_finish': gi.FunctionInfo(open_read_only_finish), 'restore_domain_from_file': gi.FunctionInfo(restore_domain_from_file), 'restore_domain_from_file_async': gi.FunctionInfo(restore_domain_from_file_async), 'restore_domain_from_file_finish': gi.FunctionInfo(restore_domain_from_file_finish), 'start_domain': gi.FunctionInfo(start_domain), 'do_connection_closed': gi.VFuncInfo(connection_closed), 'do_connection_opened': gi.VFuncInfo(connection_opened), 'do_domain_added': gi.VFuncInfo(domain_added), 'do_domain_removed': gi.VFuncInfo(domain_removed), 'parent': <property object at 0x7ffa6f99bc20>, 'priv': <property object at 0x7ffa6f99bc70>})"
    __gdoc__ = 'Object GVirConnection\n\nSignals from GVirConnection:\n  connection-opened ()\n  connection-closed ()\n  domain-added (GVirDomain)\n  domain-removed (GVirDomain)\n\nProperties from GVirConnection:\n  uri -> gchararray: URI\n    The connection URI\n  handle -> GVirConnectionHandle: Handle\n    The connection handle\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GVirConnection (94394875739328)>'
    __info__ = ObjectInfo(Connection)


