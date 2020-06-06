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


class Socket(__gi_overrides_GObject.Object, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        Socket(**properties)
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

    def connect_async(self, cancellable=None, callback, user_data=None): # real signature unknown; restored from __doc__
        """ connect_async(self, cancellable:Gio.Cancellable=None, callback:Soup.SocketCallback, user_data=None) """
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

    def connect_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(self, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def disconnect(self): # real signature unknown; restored from __doc__
        """ disconnect(self) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_disconnected(self, *args, **kwargs): # real signature unknown
        """ disconnected(self) """
        pass

    def do_new_connection(self, *args, **kwargs): # real signature unknown
        """ new_connection(self, new_sock:Soup.Socket) """
        pass

    def do_readable(self, *args, **kwargs): # real signature unknown
        """ readable(self) """
        pass

    def do_writable(self, *args, **kwargs): # real signature unknown
        """ writable(self) """
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_fd(self): # real signature unknown; restored from __doc__
        """ get_fd(self) -> int """
        return 0

    def get_local_address(self): # real signature unknown; restored from __doc__
        """ get_local_address(self) -> Soup.Address """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_address(self): # real signature unknown; restored from __doc__
        """ get_remote_address(self) -> Soup.Address """
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

    def is_connected(self): # real signature unknown; restored from __doc__
        """ is_connected(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_ssl(self): # real signature unknown; restored from __doc__
        """ is_ssl(self) -> bool """
        return False

    def listen(self): # real signature unknown; restored from __doc__
        """ listen(self) -> bool """
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

    def read(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ read(self, buffer:list, cancellable:Gio.Cancellable=None) -> Soup.SocketIOStatus, nread:int """
        pass

    def read_until(self, buffer, boundary=None, boundary_len, got_boundary, cancellable=None): # real signature unknown; restored from __doc__
        """ read_until(self, buffer:list, boundary=None, boundary_len:int, got_boundary:bool, cancellable:Gio.Cancellable=None) -> Soup.SocketIOStatus, nread:int """
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

    def start_proxy_ssl(self, ssl_host, cancellable=None): # real signature unknown; restored from __doc__
        """ start_proxy_ssl(self, ssl_host:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def start_ssl(self, cancellable=None): # real signature unknown; restored from __doc__
        """ start_ssl(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ write(self, buffer:list, cancellable:Gio.Cancellable=None) -> Soup.SocketIOStatus, nwrote:int """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f8e47f0ab20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Socket), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupSocket (94750594926480)>, '__doc__': None, '__gsignals__': {}, 'connect_async': gi.FunctionInfo(connect_async), 'connect_sync': gi.FunctionInfo(connect_sync), 'disconnect': gi.FunctionInfo(disconnect), 'get_fd': gi.FunctionInfo(get_fd), 'get_local_address': gi.FunctionInfo(get_local_address), 'get_remote_address': gi.FunctionInfo(get_remote_address), 'is_connected': gi.FunctionInfo(is_connected), 'is_ssl': gi.FunctionInfo(is_ssl), 'listen': gi.FunctionInfo(listen), 'read': gi.FunctionInfo(read), 'read_until': gi.FunctionInfo(read_until), 'start_proxy_ssl': gi.FunctionInfo(start_proxy_ssl), 'start_ssl': gi.FunctionInfo(start_ssl), 'write': gi.FunctionInfo(write), 'do_disconnected': gi.VFuncInfo(disconnected), 'do_new_connection': gi.VFuncInfo(new_connection), 'do_readable': gi.VFuncInfo(readable), 'do_writable': gi.VFuncInfo(writable), 'parent': <property object at 0x7f8e47efed10>})"
    __gdoc__ = "Object SoupSocket\n\nSignals from SoupSocket:\n  readable ()\n  writable ()\n  disconnected ()\n  new-connection (SoupSocket)\n  event (GSocketClientEvent, GIOStream)\n\nProperties from SoupSocket:\n  fd -> gint: FD\n    The socket's file descriptor\n  gsocket -> GSocket: GSocket\n    The socket's underlying GSocket\n  iostream -> GIOStream: GIOStream\n    The socket's underlying GIOStream\n  local-address -> SoupAddress: Local address\n    Address of local end of socket\n  remote-address -> SoupAddress: Remote address\n    Address of remote end of socket\n  non-blocking -> gboolean: Non-blocking\n    Whether or not the socket uses non-blocking I/O\n  ipv6-only -> gboolean: IPv6 only\n    IPv6 only\n  is-server -> gboolean: Server\n    Whether or not the socket is a server socket\n  ssl-creds -> gpointer: SSL credentials\n    SSL credential information, passed from the session to the SSL implementation\n  ssl-strict -> gboolean: Strictly validate SSL certificates\n    Whether certificate errors should be considered a connection error\n  ssl-fallback -> gboolean: SSLv3 fallback\n    Use SSLv3 instead of TLS (client-side only)\n  async-context -> gpointer: Async GMainContext\n    The GMainContext to dispatch this socket's async I/O in\n  use-thread-context -> gboolean: Use thread context\n    Use g_main_context_get_thread_default\n  timeout -> guint: Timeout value\n    Value in seconds to timeout a blocking I/O\n  trusted-certificate -> gboolean: Trusted Certificate\n    Whether the server certificate is trusted, if this is an SSL socket\n  tls-certificate -> GTlsCertificate: TLS certificate\n    The peer's TLS certificate\n  tls-errors -> GTlsCertificateFlags: TLS errors\n    Errors with the peer's TLS certificate\n  socket-properties -> SoupSocketProperties: Socket properties\n    Socket properties\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SoupSocket (94750594926480)>'
    __info__ = ObjectInfo(Socket)


