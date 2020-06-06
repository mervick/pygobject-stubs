# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


from .SourceExtension import SourceExtension

class SourceProxy(SourceExtension):
    """
    :Constructors:
    
    ::
    
        SourceProxy(**properties)
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

    def dup_autoconfig_url(self): # real signature unknown; restored from __doc__
        """ dup_autoconfig_url(self) -> str """
        return ""

    def dup_ftp_host(self): # real signature unknown; restored from __doc__
        """ dup_ftp_host(self) -> str """
        return ""

    def dup_https_host(self): # real signature unknown; restored from __doc__
        """ dup_https_host(self) -> str """
        return ""

    def dup_http_auth_password(self): # real signature unknown; restored from __doc__
        """ dup_http_auth_password(self) -> str """
        return ""

    def dup_http_auth_user(self): # real signature unknown; restored from __doc__
        """ dup_http_auth_user(self) -> str """
        return ""

    def dup_http_host(self): # real signature unknown; restored from __doc__
        """ dup_http_host(self) -> str """
        return ""

    def dup_ignore_hosts(self): # real signature unknown; restored from __doc__
        """ dup_ignore_hosts(self) -> list """
        return []

    def dup_socks_host(self): # real signature unknown; restored from __doc__
        """ dup_socks_host(self) -> str """
        return ""

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

    def get_autoconfig_url(self): # real signature unknown; restored from __doc__
        """ get_autoconfig_url(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_ftp_host(self): # real signature unknown; restored from __doc__
        """ get_ftp_host(self) -> str """
        return ""

    def get_ftp_port(self): # real signature unknown; restored from __doc__
        """ get_ftp_port(self) -> int """
        return 0

    def get_https_host(self): # real signature unknown; restored from __doc__
        """ get_https_host(self) -> str """
        return ""

    def get_https_port(self): # real signature unknown; restored from __doc__
        """ get_https_port(self) -> int """
        return 0

    def get_http_auth_password(self): # real signature unknown; restored from __doc__
        """ get_http_auth_password(self) -> str """
        return ""

    def get_http_auth_user(self): # real signature unknown; restored from __doc__
        """ get_http_auth_user(self) -> str """
        return ""

    def get_http_host(self): # real signature unknown; restored from __doc__
        """ get_http_host(self) -> str """
        return ""

    def get_http_port(self): # real signature unknown; restored from __doc__
        """ get_http_port(self) -> int """
        return 0

    def get_http_use_auth(self): # real signature unknown; restored from __doc__
        """ get_http_use_auth(self) -> bool """
        return False

    def get_ignore_hosts(self): # real signature unknown; restored from __doc__
        """ get_ignore_hosts(self) -> list """
        return []

    def get_method(self): # real signature unknown; restored from __doc__
        """ get_method(self) -> EDataServer.ProxyMethod """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_socks_host(self): # real signature unknown; restored from __doc__
        """ get_socks_host(self) -> str """
        return ""

    def get_socks_port(self): # real signature unknown; restored from __doc__
        """ get_socks_port(self) -> int """
        return 0

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
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

    def property_lock(self): # real signature unknown; restored from __doc__
        """ property_lock(self) """
        pass

    def property_unlock(self): # real signature unknown; restored from __doc__
        """ property_unlock(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_source(self): # real signature unknown; restored from __doc__
        """ ref_source(self) -> EDataServer.Source """
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

    def set_autoconfig_url(self, autoconfig_url): # real signature unknown; restored from __doc__
        """ set_autoconfig_url(self, autoconfig_url:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_ftp_host(self, ftp_host): # real signature unknown; restored from __doc__
        """ set_ftp_host(self, ftp_host:str) """
        pass

    def set_ftp_port(self, ftp_port): # real signature unknown; restored from __doc__
        """ set_ftp_port(self, ftp_port:int) """
        pass

    def set_https_host(self, https_host): # real signature unknown; restored from __doc__
        """ set_https_host(self, https_host:str) """
        pass

    def set_https_port(self, https_port): # real signature unknown; restored from __doc__
        """ set_https_port(self, https_port:int) """
        pass

    def set_http_auth_password(self, http_auth_password): # real signature unknown; restored from __doc__
        """ set_http_auth_password(self, http_auth_password:str) """
        pass

    def set_http_auth_user(self, http_auth_user): # real signature unknown; restored from __doc__
        """ set_http_auth_user(self, http_auth_user:str) """
        pass

    def set_http_host(self, http_host): # real signature unknown; restored from __doc__
        """ set_http_host(self, http_host:str) """
        pass

    def set_http_port(self, http_port): # real signature unknown; restored from __doc__
        """ set_http_port(self, http_port:int) """
        pass

    def set_http_use_auth(self, http_use_auth): # real signature unknown; restored from __doc__
        """ set_http_use_auth(self, http_use_auth:bool) """
        pass

    def set_ignore_hosts(self, ignore_hosts): # real signature unknown; restored from __doc__
        """ set_ignore_hosts(self, ignore_hosts:str) """
        pass

    def set_method(self, method): # real signature unknown; restored from __doc__
        """ set_method(self, method:EDataServer.ProxyMethod) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_socks_host(self, socks_host): # real signature unknown; restored from __doc__
        """ set_socks_host(self, socks_host:str) """
        pass

    def set_socks_port(self, socks_port): # real signature unknown; restored from __doc__
        """ set_socks_port(self, socks_port:int) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f626e6238e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SourceProxy), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ESourceProxy (94877537255952)>, '__doc__': None, '__gsignals__': {}, 'dup_autoconfig_url': gi.FunctionInfo(dup_autoconfig_url), 'dup_ftp_host': gi.FunctionInfo(dup_ftp_host), 'dup_http_auth_password': gi.FunctionInfo(dup_http_auth_password), 'dup_http_auth_user': gi.FunctionInfo(dup_http_auth_user), 'dup_http_host': gi.FunctionInfo(dup_http_host), 'dup_https_host': gi.FunctionInfo(dup_https_host), 'dup_ignore_hosts': gi.FunctionInfo(dup_ignore_hosts), 'dup_socks_host': gi.FunctionInfo(dup_socks_host), 'get_autoconfig_url': gi.FunctionInfo(get_autoconfig_url), 'get_ftp_host': gi.FunctionInfo(get_ftp_host), 'get_ftp_port': gi.FunctionInfo(get_ftp_port), 'get_http_auth_password': gi.FunctionInfo(get_http_auth_password), 'get_http_auth_user': gi.FunctionInfo(get_http_auth_user), 'get_http_host': gi.FunctionInfo(get_http_host), 'get_http_port': gi.FunctionInfo(get_http_port), 'get_http_use_auth': gi.FunctionInfo(get_http_use_auth), 'get_https_host': gi.FunctionInfo(get_https_host), 'get_https_port': gi.FunctionInfo(get_https_port), 'get_ignore_hosts': gi.FunctionInfo(get_ignore_hosts), 'get_method': gi.FunctionInfo(get_method), 'get_socks_host': gi.FunctionInfo(get_socks_host), 'get_socks_port': gi.FunctionInfo(get_socks_port), 'set_autoconfig_url': gi.FunctionInfo(set_autoconfig_url), 'set_ftp_host': gi.FunctionInfo(set_ftp_host), 'set_ftp_port': gi.FunctionInfo(set_ftp_port), 'set_http_auth_password': gi.FunctionInfo(set_http_auth_password), 'set_http_auth_user': gi.FunctionInfo(set_http_auth_user), 'set_http_host': gi.FunctionInfo(set_http_host), 'set_http_port': gi.FunctionInfo(set_http_port), 'set_http_use_auth': gi.FunctionInfo(set_http_use_auth), 'set_https_host': gi.FunctionInfo(set_https_host), 'set_https_port': gi.FunctionInfo(set_https_port), 'set_ignore_hosts': gi.FunctionInfo(set_ignore_hosts), 'set_method': gi.FunctionInfo(set_method), 'set_socks_host': gi.FunctionInfo(set_socks_host), 'set_socks_port': gi.FunctionInfo(set_socks_port), 'parent': <property object at 0x7f626e9401d0>, 'priv': <property object at 0x7f626e9402c0>})"
    __gdoc__ = 'Object ESourceProxy\n\nProperties from ESourceProxy:\n  autoconfig-url -> gchararray: Autoconfig URL\n    Proxy autoconfiguration URL\n  ftp-host -> gchararray: FTP Host\n    FTP proxy host name\n  ftp-port -> guint: FTP Port\n    FTP proxy port\n  http-auth-password -> gchararray: HTTP Auth Password\n    HTTP proxy password\n  http-auth-user -> gchararray: HTTP Auth User\n    HTTP proxy username\n  http-host -> gchararray: HTTP Host\n    HTTP proxy host name\n  http-port -> guint: HTTP Port\n    HTTP proxy port\n  http-use-auth -> gboolean: HTTP Use Auth\n    Whether HTTP proxy server connections require authentication\n  https-host -> gchararray: HTTPS Host\n    Secure HTTP proxy host name\n  https-port -> guint: HTTPS Port\n    Secure HTTP proxy port\n  ignore-hosts -> GStrv: Ignore Hosts\n    Hosts to connect directly\n  method -> EProxyMethod: Method\n    Proxy configuration method\n  socks-host -> gchararray: SOCKS Host\n    SOCKS proxy host name\n  socks-port -> guint: SOCKS Port\n    SOCKS proxy port\n\nProperties from ESourceExtension:\n  source -> ESource: Source\n    The ESource being extended\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ESourceProxy (94877537255952)>'
    __info__ = ObjectInfo(SourceProxy)


