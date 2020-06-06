# encoding: utf-8
# module gi.repository.GUPnP
# from /usr/lib64/girepository-1.0/GUPnP-1.0.typelib
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
import gi.repository.GSSDP as __gi_repository_GSSDP
import gobject as __gobject


class Context(__gi_repository_GSSDP.Client):
    """
    :Constructors:
    
    ::
    
        Context(**properties)
        new(main_context:GLib.MainContext=None, iface:str=None, port:int) -> GUPnP.Context
    """
    def add_cache_entry(self, ip_address, user_agent): # real signature unknown; restored from __doc__
        """ add_cache_entry(self, ip_address:str, user_agent:str) """
        pass

    def add_server_handler(self, use_acl, path, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_server_handler(self, use_acl:bool, path:str, callback:Soup.ServerCallback, user_data=None) """
        pass

    def append_header(self, name, value): # real signature unknown; restored from __doc__
        """ append_header(self, name:str, value:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_headers(self): # real signature unknown; restored from __doc__
        """ clear_headers(self) """
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

    def get_acl(self): # real signature unknown; restored from __doc__
        """ get_acl(self) -> GUPnP.Acl """
        pass

    def get_active(self): # real signature unknown; restored from __doc__
        """ get_active(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_language(self): # real signature unknown; restored from __doc__
        """ get_default_language(self) -> str """
        return ""

    def get_host_ip(self): # real signature unknown; restored from __doc__
        """ get_host_ip(self) -> str """
        return ""

    def get_interface(self): # real signature unknown; restored from __doc__
        """ get_interface(self) -> str """
        return ""

    def get_main_context(self): # real signature unknown; restored from __doc__
        """ get_main_context(self) -> GLib.MainContext """
        pass

    def get_network(self): # real signature unknown; restored from __doc__
        """ get_network(self) -> str """
        return ""

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_server(self): # real signature unknown; restored from __doc__
        """ get_server(self) -> Soup.Server """
        pass

    def get_server_id(self): # real signature unknown; restored from __doc__
        """ get_server_id(self) -> str """
        return ""

    def get_session(self): # real signature unknown; restored from __doc__
        """ get_session(self) -> Soup.Session """
        pass

    def get_subscription_timeout(self): # real signature unknown; restored from __doc__
        """ get_subscription_timeout(self) -> int """
        return 0

    def guess_user_agent(self, ip_address): # real signature unknown; restored from __doc__
        """ guess_user_agent(self, ip_address:str) -> str """
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

    def host_path(self, local_path, server_path): # real signature unknown; restored from __doc__
        """ host_path(self, local_path:str, server_path:str) """
        pass

    def host_path_for_agent(self, local_path, server_path, user_agent): # real signature unknown; restored from __doc__
        """ host_path_for_agent(self, local_path:str, server_path:str, user_agent:GLib.Regex) -> bool """
        return False

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

    def new(self, main_context=None, iface=None, port): # real signature unknown; restored from __doc__
        """ new(main_context:GLib.MainContext=None, iface:str=None, port:int) -> GUPnP.Context """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_port(self, iface=None, msearch_port): # real signature unknown; restored from __doc__
        """ new_with_port(iface:str=None, msearch_port:int) -> GSSDP.Client """
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

    def remove_header(self, name): # real signature unknown; restored from __doc__
        """ remove_header(self, name:str) """
        pass

    def remove_server_handler(self, path): # real signature unknown; restored from __doc__
        """ remove_server_handler(self, path:str) """
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

    def set_acl(self, acl=None): # real signature unknown; restored from __doc__
        """ set_acl(self, acl:GUPnP.Acl=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_language(self, language): # real signature unknown; restored from __doc__
        """ set_default_language(self, language:str) """
        pass

    def set_network(self, network): # real signature unknown; restored from __doc__
        """ set_network(self, network:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_server_id(self, server_id): # real signature unknown; restored from __doc__
        """ set_server_id(self, server_id:str) """
        pass

    def set_subscription_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_subscription_timeout(self, timeout:int) """
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

    def unhost_path(self, server_path): # real signature unknown; restored from __doc__
        """ unhost_path(self, server_path:str) """
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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f24e9bfd8b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Context), '__module__': 'gi.repository.GUPnP', '__gtype__': <GType GUPnPContext (94417774991792)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_server_handler': gi.FunctionInfo(add_server_handler), 'get_acl': gi.FunctionInfo(get_acl), 'get_default_language': gi.FunctionInfo(get_default_language), 'get_host_ip': gi.FunctionInfo(get_host_ip), 'get_port': gi.FunctionInfo(get_port), 'get_server': gi.FunctionInfo(get_server), 'get_session': gi.FunctionInfo(get_session), 'get_subscription_timeout': gi.FunctionInfo(get_subscription_timeout), 'host_path': gi.FunctionInfo(host_path), 'host_path_for_agent': gi.FunctionInfo(host_path_for_agent), 'remove_server_handler': gi.FunctionInfo(remove_server_handler), 'set_acl': gi.FunctionInfo(set_acl), 'set_default_language': gi.FunctionInfo(set_default_language), 'set_subscription_timeout': gi.FunctionInfo(set_subscription_timeout), 'unhost_path': gi.FunctionInfo(unhost_path), 'parent': <property object at 0x7f24ea3afe00>, 'priv': <property object at 0x7f24ea3afef0>})"
    __gdoc__ = "Object GUPnPContext\n\nProperties from GUPnPContext:\n  port -> guint: Port\n    Port to run on\n  server -> SoupServer: SoupServer\n    SoupServer HTTP server\n  session -> SoupSession: SoupSession\n    SoupSession object\n  subscription-timeout -> guint: Subscription timeout\n    Subscription timeout\n  default-language -> gchararray: Default language\n    Default language\n  acl -> GUPnPAcl: Access control list\n    Access control list\n\nSignals from GSSDPClient:\n  message-received (gchararray, guint, gint, gpointer)\n\nProperties from GSSDPClient:\n  main-context -> gpointer: Main context\n    The associated GMainContext.\n  server-id -> gchararray: Server ID\n    The SSDP server's identifier.\n  interface -> gchararray: Network interface\n    The name of the associated network interface.\n  network -> gchararray: Network ID\n    The network this client is currently connected to.\n  host-ip -> gchararray: Host IP\n    The IP address of the associatednetwork interface\n  active -> gboolean: Active\n    TRUE if the client is active.\n  socket-ttl -> guint: Socket TTL\n    Time To Live for client's sockets\n  msearch-port -> guint: M-SEARCH port\n    UDP port to use for M-SEARCH requests\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GUPnPContext (94417774991792)>'
    __info__ = ObjectInfo(Context)


