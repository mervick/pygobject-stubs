# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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


class Server(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Server(**properties)
    """
    def accept_iostream(self, stream, local_addr=None, remote_addr=None): # real signature unknown; restored from __doc__
        """ accept_iostream(self, stream:Gio.IOStream, local_addr:Gio.SocketAddress=None, remote_addr:Gio.SocketAddress=None) -> bool """
        return False

    def add_auth_domain(self, auth_domain): # real signature unknown; restored from __doc__
        """ add_auth_domain(self, auth_domain:Soup.AuthDomain) """
        pass

    def add_early_handler(self, path=None, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_early_handler(self, path:str=None, callback:Soup.ServerCallback, user_data=None) """
        pass

    def add_handler(self, path=None, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_handler(self, path:str=None, callback:Soup.ServerCallback, user_data=None) """
        pass

    def add_websocket_extension(self, extension_type): # real signature unknown; restored from __doc__
        """ add_websocket_extension(self, extension_type:GType) """
        pass

    def add_websocket_handler(self, path=None, origin=None, protocols=None, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_websocket_handler(self, path:str=None, origin:str=None, protocols:list=None, callback:Soup.ServerWebsocketCallback, user_data=None) """
        pass

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
        """ disconnect(self) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_request_aborted(self, *args, **kwargs): # real signature unknown
        """ request_aborted(self, msg:Soup.Message, client:Soup.ClientContext) """
        pass

    def do_request_finished(self, *args, **kwargs): # real signature unknown
        """ request_finished(self, msg:Soup.Message, client:Soup.ClientContext) """
        pass

    def do_request_read(self, *args, **kwargs): # real signature unknown
        """ request_read(self, msg:Soup.Message, client:Soup.ClientContext) """
        pass

    def do_request_started(self, *args, **kwargs): # real signature unknown
        """ request_started(self, msg:Soup.Message, client:Soup.ClientContext) """
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

    def get_async_context(self): # real signature unknown; restored from __doc__
        """ get_async_context(self) -> GLib.MainContext or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_listener(self): # real signature unknown; restored from __doc__
        """ get_listener(self) -> Soup.Socket """
        pass

    def get_listeners(self): # real signature unknown; restored from __doc__
        """ get_listeners(self) -> list """
        return []

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

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list """
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

    def is_https(self): # real signature unknown; restored from __doc__
        """ is_https(self) -> bool """
        return False

    def listen(self, address, options): # real signature unknown; restored from __doc__
        """ listen(self, address:Gio.SocketAddress, options:Soup.ServerListenOptions) -> bool """
        return False

    def listen_all(self, port, options): # real signature unknown; restored from __doc__
        """ listen_all(self, port:int, options:Soup.ServerListenOptions) -> bool """
        return False

    def listen_fd(self, fd, options): # real signature unknown; restored from __doc__
        """ listen_fd(self, fd:int, options:Soup.ServerListenOptions) -> bool """
        return False

    def listen_local(self, port, options): # real signature unknown; restored from __doc__
        """ listen_local(self, port:int, options:Soup.ServerListenOptions) -> bool """
        return False

    def listen_socket(self, socket, options): # real signature unknown; restored from __doc__
        """ listen_socket(self, socket:Gio.Socket, options:Soup.ServerListenOptions) -> bool """
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

    def pause_message(self, msg): # real signature unknown; restored from __doc__
        """ pause_message(self, msg:Soup.Message) """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_auth_domain(self, auth_domain): # real signature unknown; restored from __doc__
        """ remove_auth_domain(self, auth_domain:Soup.AuthDomain) """
        pass

    def remove_handler(self, path): # real signature unknown; restored from __doc__
        """ remove_handler(self, path:str) """
        pass

    def remove_websocket_extension(self, extension_type): # real signature unknown; restored from __doc__
        """ remove_websocket_extension(self, extension_type:GType) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ run(self) """
        pass

    def run_async(self): # real signature unknown; restored from __doc__
        """ run_async(self) """
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

    def set_ssl_cert_file(self, ssl_cert_file, ssl_key_file): # real signature unknown; restored from __doc__
        """ set_ssl_cert_file(self, ssl_cert_file:str, ssl_key_file:str) -> bool """
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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unpause_message(self, msg): # real signature unknown; restored from __doc__
        """ unpause_message(self, msg:Soup.Message) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f8e47e9c0a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Server), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupServer (94750594800400)>, '__doc__': None, '__gsignals__': {}, 'accept_iostream': gi.FunctionInfo(accept_iostream), 'add_auth_domain': gi.FunctionInfo(add_auth_domain), 'add_early_handler': gi.FunctionInfo(add_early_handler), 'add_handler': gi.FunctionInfo(add_handler), 'add_websocket_extension': gi.FunctionInfo(add_websocket_extension), 'add_websocket_handler': gi.FunctionInfo(add_websocket_handler), 'disconnect': gi.FunctionInfo(disconnect), 'get_async_context': gi.FunctionInfo(get_async_context), 'get_listener': gi.FunctionInfo(get_listener), 'get_listeners': gi.FunctionInfo(get_listeners), 'get_port': gi.FunctionInfo(get_port), 'get_uris': gi.FunctionInfo(get_uris), 'is_https': gi.FunctionInfo(is_https), 'listen': gi.FunctionInfo(listen), 'listen_all': gi.FunctionInfo(listen_all), 'listen_fd': gi.FunctionInfo(listen_fd), 'listen_local': gi.FunctionInfo(listen_local), 'listen_socket': gi.FunctionInfo(listen_socket), 'pause_message': gi.FunctionInfo(pause_message), 'quit': gi.FunctionInfo(quit), 'remove_auth_domain': gi.FunctionInfo(remove_auth_domain), 'remove_handler': gi.FunctionInfo(remove_handler), 'remove_websocket_extension': gi.FunctionInfo(remove_websocket_extension), 'run': gi.FunctionInfo(run), 'run_async': gi.FunctionInfo(run_async), 'set_ssl_cert_file': gi.FunctionInfo(set_ssl_cert_file), 'unpause_message': gi.FunctionInfo(unpause_message), 'do_request_aborted': gi.VFuncInfo(request_aborted), 'do_request_finished': gi.VFuncInfo(request_finished), 'do_request_read': gi.VFuncInfo(request_read), 'do_request_started': gi.VFuncInfo(request_started), 'parent': <property object at 0x7f8e47ef7540>})"
    __gdoc__ = "Object SoupServer\n\nSignals from SoupServer:\n  request-started (SoupMessage, SoupClientContext)\n  request-read (SoupMessage, SoupClientContext)\n  request-finished (SoupMessage, SoupClientContext)\n  request-aborted (SoupMessage, SoupClientContext)\n\nProperties from SoupServer:\n  port -> guint: Port\n    Port to listen on (Deprecated)\n  interface -> SoupAddress: Interface\n    Address of interface to listen on (Deprecated)\n  ssl-cert-file -> gchararray: TLS (aka SSL) certificate file\n    File containing server TLS (aka SSL) certificate\n  ssl-key-file -> gchararray: TLS (aka SSL) key file\n    File containing server TLS (aka SSL) key\n  tls-certificate -> GTlsCertificate: TLS certificate\n    GTlsCertificate to use for https\n  async-context -> gpointer: Async GMainContext\n    The GMainContext to dispatch async I/O in\n  raw-paths -> gboolean: Raw paths\n    If %TRUE, percent-encoding in the Request-URI path will not be automatically decoded.\n  server-header -> gchararray: Server header\n    Server header\n  http-aliases -> GStrv: http aliases\n    URI schemes that are considered aliases for 'http'\n  https-aliases -> GStrv: https aliases\n    URI schemes that are considered aliases for 'https'\n  add-websocket-extension -> GType: Add support for a WebSocket extension\n    Add support for a WebSocket extension of the given type\n  remove-websocket-extension -> GType: Remove support for a WebSocket extension\n    Remove support for a WebSocket extension of the given type\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SoupServer (94750594800400)>'
    __info__ = ObjectInfo(Server)


