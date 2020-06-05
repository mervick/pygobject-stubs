# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .DatagramBased import DatagramBased

from .Initable import Initable

class Socket(__gi_overrides_GObject.Object, DatagramBased, Initable):
    """
    :Constructors:
    
    ::
    
        Socket(**properties)
        new(family:Gio.SocketFamily, type:Gio.SocketType, protocol:Gio.SocketProtocol) -> Gio.Socket
        new_from_fd(fd:int) -> Gio.Socket
    """
    def accept(self, cancellable=None): # real signature unknown; restored from __doc__
        """ accept(self, cancellable:Gio.Cancellable=None) -> Gio.Socket """
        pass

    def bind(self, address, allow_reuse): # real signature unknown; restored from __doc__
        """ bind(self, address:Gio.SocketAddress, allow_reuse:bool) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_connect_result(self): # real signature unknown; restored from __doc__
        """ check_connect_result(self) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def condition_check(self, condition): # real signature unknown; restored from __doc__
        """ condition_check(self, condition:GLib.IOCondition) -> GLib.IOCondition """
        pass

    def condition_timed_wait(self, condition, timeout_us, cancellable=None): # real signature unknown; restored from __doc__
        """ condition_timed_wait(self, condition:GLib.IOCondition, timeout_us:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def condition_wait(self, condition, cancellable=None): # real signature unknown; restored from __doc__
        """ condition_wait(self, condition:GLib.IOCondition, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def connect(self, address, cancellable=None): # real signature unknown; restored from __doc__
        """ connect(self, address:Gio.SocketAddress, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def connection_factory_create_connection(self): # real signature unknown; restored from __doc__
        """ connection_factory_create_connection(self) -> Gio.SocketConnection """
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

    def create_source(self, condition, cancellable=None): # real signature unknown; restored from __doc__
        """ create_source(self, condition:GLib.IOCondition, cancellable:Gio.Cancellable=None) -> GLib.Source """
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

    def get_available_bytes(self): # real signature unknown; restored from __doc__
        """ get_available_bytes(self) -> int """
        return 0

    def get_blocking(self): # real signature unknown; restored from __doc__
        """ get_blocking(self) -> bool """
        return False

    def get_broadcast(self): # real signature unknown; restored from __doc__
        """ get_broadcast(self) -> bool """
        return False

    def get_credentials(self): # real signature unknown; restored from __doc__
        """ get_credentials(self) -> Gio.Credentials """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_family(self): # real signature unknown; restored from __doc__
        """ get_family(self) -> Gio.SocketFamily """
        pass

    def get_fd(self): # real signature unknown; restored from __doc__
        """ get_fd(self) -> int """
        return 0

    def get_keepalive(self): # real signature unknown; restored from __doc__
        """ get_keepalive(self) -> bool """
        return False

    def get_listen_backlog(self): # real signature unknown; restored from __doc__
        """ get_listen_backlog(self) -> int """
        return 0

    def get_local_address(self): # real signature unknown; restored from __doc__
        """ get_local_address(self) -> Gio.SocketAddress """
        pass

    def get_multicast_loopback(self): # real signature unknown; restored from __doc__
        """ get_multicast_loopback(self) -> bool """
        return False

    def get_multicast_ttl(self): # real signature unknown; restored from __doc__
        """ get_multicast_ttl(self) -> int """
        return 0

    def get_option(self, level, optname): # real signature unknown; restored from __doc__
        """ get_option(self, level:int, optname:int) -> bool, value:int """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> Gio.SocketProtocol """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_address(self): # real signature unknown; restored from __doc__
        """ get_remote_address(self) -> Gio.SocketAddress """
        pass

    def get_socket_type(self): # real signature unknown; restored from __doc__
        """ get_socket_type(self) -> Gio.SocketType """
        pass

    def get_timeout(self): # real signature unknown; restored from __doc__
        """ get_timeout(self) -> int """
        return 0

    def get_ttl(self): # real signature unknown; restored from __doc__
        """ get_ttl(self) -> int """
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

    def is_closed(self): # real signature unknown; restored from __doc__
        """ is_closed(self) -> bool """
        return False

    def is_connected(self): # real signature unknown; restored from __doc__
        """ is_connected(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def join_multicast_group(self, group, source_specific, iface=None): # real signature unknown; restored from __doc__
        """ join_multicast_group(self, group:Gio.InetAddress, source_specific:bool, iface:str=None) -> bool """
        return False

    def join_multicast_group_ssm(self, group, source_specific=None, iface=None): # real signature unknown; restored from __doc__
        """ join_multicast_group_ssm(self, group:Gio.InetAddress, source_specific:Gio.InetAddress=None, iface:str=None) -> bool """
        return False

    def leave_multicast_group(self, group, source_specific, iface=None): # real signature unknown; restored from __doc__
        """ leave_multicast_group(self, group:Gio.InetAddress, source_specific:bool, iface:str=None) -> bool """
        return False

    def leave_multicast_group_ssm(self, group, source_specific=None, iface=None): # real signature unknown; restored from __doc__
        """ leave_multicast_group_ssm(self, group:Gio.InetAddress, source_specific:Gio.InetAddress=None, iface:str=None) -> bool """
        return False

    def listen(self): # real signature unknown; restored from __doc__
        """ listen(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, family, type, protocol): # real signature unknown; restored from __doc__
        """ new(family:Gio.SocketFamily, type:Gio.SocketType, protocol:Gio.SocketProtocol) -> Gio.Socket """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_fd(self, fd): # real signature unknown; restored from __doc__
        """ new_from_fd(fd:int) -> Gio.Socket """
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

    def receive(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ receive(self, buffer:list, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def receive_from(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ receive_from(self, buffer:list, cancellable:Gio.Cancellable=None) -> int, address:Gio.SocketAddress """
        return 0

    def receive_message(self, vectors, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ receive_message(self, vectors:list, flags:int, cancellable:Gio.Cancellable=None) -> int, address:Gio.SocketAddress, messages:list, flags:int """
        return 0

    def receive_messages(self, messages, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ receive_messages(self, messages:list, flags:int, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def receive_with_blocking(self, buffer, blocking, cancellable=None): # real signature unknown; restored from __doc__
        """ receive_with_blocking(self, buffer:list, blocking:bool, cancellable:Gio.Cancellable=None) -> int """
        return 0

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

    def send(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ send(self, buffer:list, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def send_message(self, address=None, vectors, messages=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ send_message(self, address:Gio.SocketAddress=None, vectors:list, messages:list=None, flags:int, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def send_messages(self, messages, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ send_messages(self, messages:list, flags:int, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def send_message_with_timeout(self, address=None, vectors, messages=None, flags, timeout_us, cancellable=None): # real signature unknown; restored from __doc__
        """ send_message_with_timeout(self, address:Gio.SocketAddress=None, vectors:list, messages:list=None, flags:int, timeout_us:int, cancellable:Gio.Cancellable=None) -> Gio.PollableReturn, bytes_written:int """
        pass

    def send_to(self, address=None, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ send_to(self, address:Gio.SocketAddress=None, buffer:list, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def send_with_blocking(self, buffer, blocking, cancellable=None): # real signature unknown; restored from __doc__
        """ send_with_blocking(self, buffer:list, blocking:bool, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def set_blocking(self, blocking): # real signature unknown; restored from __doc__
        """ set_blocking(self, blocking:bool) """
        pass

    def set_broadcast(self, broadcast): # real signature unknown; restored from __doc__
        """ set_broadcast(self, broadcast:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_keepalive(self, keepalive): # real signature unknown; restored from __doc__
        """ set_keepalive(self, keepalive:bool) """
        pass

    def set_listen_backlog(self, backlog): # real signature unknown; restored from __doc__
        """ set_listen_backlog(self, backlog:int) """
        pass

    def set_multicast_loopback(self, loopback): # real signature unknown; restored from __doc__
        """ set_multicast_loopback(self, loopback:bool) """
        pass

    def set_multicast_ttl(self, ttl): # real signature unknown; restored from __doc__
        """ set_multicast_ttl(self, ttl:int) """
        pass

    def set_option(self, level, optname, value): # real signature unknown; restored from __doc__
        """ set_option(self, level:int, optname:int, value:int) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_timeout(self, timeout:int) """
        pass

    def set_ttl(self, ttl): # real signature unknown; restored from __doc__
        """ set_ttl(self, ttl:int) """
        pass

    def shutdown(self, shutdown_read, shutdown_write): # real signature unknown; restored from __doc__
        """ shutdown(self, shutdown_read:bool, shutdown_write:bool) -> bool """
        return False

    def speaks_ipv4(self): # real signature unknown; restored from __doc__
        """ speaks_ipv4(self) -> bool """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f28dd15bac0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Socket), '__module__': 'gi.repository.Gio', '__gtype__': <GType GSocket (94125582723648)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_fd': gi.FunctionInfo(new_from_fd), 'accept': gi.FunctionInfo(accept), 'bind': gi.FunctionInfo(bind), 'check_connect_result': gi.FunctionInfo(check_connect_result), 'close': gi.FunctionInfo(close), 'condition_check': gi.FunctionInfo(condition_check), 'condition_timed_wait': gi.FunctionInfo(condition_timed_wait), 'condition_wait': gi.FunctionInfo(condition_wait), 'connect': gi.FunctionInfo(connect), 'connection_factory_create_connection': gi.FunctionInfo(connection_factory_create_connection), 'get_available_bytes': gi.FunctionInfo(get_available_bytes), 'get_blocking': gi.FunctionInfo(get_blocking), 'get_broadcast': gi.FunctionInfo(get_broadcast), 'get_credentials': gi.FunctionInfo(get_credentials), 'get_family': gi.FunctionInfo(get_family), 'get_fd': gi.FunctionInfo(get_fd), 'get_keepalive': gi.FunctionInfo(get_keepalive), 'get_listen_backlog': gi.FunctionInfo(get_listen_backlog), 'get_local_address': gi.FunctionInfo(get_local_address), 'get_multicast_loopback': gi.FunctionInfo(get_multicast_loopback), 'get_multicast_ttl': gi.FunctionInfo(get_multicast_ttl), 'get_option': gi.FunctionInfo(get_option), 'get_protocol': gi.FunctionInfo(get_protocol), 'get_remote_address': gi.FunctionInfo(get_remote_address), 'get_socket_type': gi.FunctionInfo(get_socket_type), 'get_timeout': gi.FunctionInfo(get_timeout), 'get_ttl': gi.FunctionInfo(get_ttl), 'is_closed': gi.FunctionInfo(is_closed), 'is_connected': gi.FunctionInfo(is_connected), 'join_multicast_group': gi.FunctionInfo(join_multicast_group), 'join_multicast_group_ssm': gi.FunctionInfo(join_multicast_group_ssm), 'leave_multicast_group': gi.FunctionInfo(leave_multicast_group), 'leave_multicast_group_ssm': gi.FunctionInfo(leave_multicast_group_ssm), 'listen': gi.FunctionInfo(listen), 'receive': gi.FunctionInfo(receive), 'receive_from': gi.FunctionInfo(receive_from), 'receive_message': gi.FunctionInfo(receive_message), 'receive_messages': gi.FunctionInfo(receive_messages), 'receive_with_blocking': gi.FunctionInfo(receive_with_blocking), 'send': gi.FunctionInfo(send), 'send_message': gi.FunctionInfo(send_message), 'send_message_with_timeout': gi.FunctionInfo(send_message_with_timeout), 'send_messages': gi.FunctionInfo(send_messages), 'send_to': gi.FunctionInfo(send_to), 'send_with_blocking': gi.FunctionInfo(send_with_blocking), 'set_blocking': gi.FunctionInfo(set_blocking), 'set_broadcast': gi.FunctionInfo(set_broadcast), 'set_keepalive': gi.FunctionInfo(set_keepalive), 'set_listen_backlog': gi.FunctionInfo(set_listen_backlog), 'set_multicast_loopback': gi.FunctionInfo(set_multicast_loopback), 'set_multicast_ttl': gi.FunctionInfo(set_multicast_ttl), 'set_option': gi.FunctionInfo(set_option), 'set_timeout': gi.FunctionInfo(set_timeout), 'set_ttl': gi.FunctionInfo(set_ttl), 'shutdown': gi.FunctionInfo(shutdown), 'speaks_ipv4': gi.FunctionInfo(speaks_ipv4), 'parent_instance': <property object at 0x7f28dde56e00>, 'priv': <property object at 0x7f28dde56ef0>})"
    __gdoc__ = 'Object GSocket\n\nProperties from GSocket:\n  family -> GSocketFamily: Socket family\n    The sockets address family\n  type -> GSocketType: Socket type\n    The sockets type\n  protocol -> GSocketProtocol: Socket protocol\n    The id of the protocol to use, or -1 for unknown\n  fd -> gint: File descriptor\n    The sockets file descriptor\n  blocking -> gboolean: blocking\n    Whether or not I/O on this socket is blocking\n  listen-backlog -> gint: Listen backlog\n    Outstanding connections in the listen queue\n  keepalive -> gboolean: Keep connection alive\n    Keep connection alive by sending periodic pings\n  local-address -> GSocketAddress: Local address\n    The local address the socket is bound to\n  remote-address -> GSocketAddress: Remote address\n    The remote address the socket is connected to\n  timeout -> guint: Timeout\n    The timeout in seconds on socket I/O\n  ttl -> guint: TTL\n    Time-to-live of outgoing unicast packets\n  broadcast -> gboolean: Broadcast\n    Whether to allow sending to broadcast addresses\n  multicast-loopback -> gboolean: Multicast loopback\n    Whether outgoing multicast packets loop back to the local host\n  multicast-ttl -> guint: Multicast TTL\n    Time-to-live of outgoing multicast packets\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GSocket (94125582723648)>'
    __info__ = ObjectInfo(Socket)


