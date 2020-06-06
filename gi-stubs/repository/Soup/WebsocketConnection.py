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


class WebsocketConnection(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        WebsocketConnection(**properties)
        new(stream:Gio.IOStream, uri:Soup.URI, type:Soup.WebsocketConnectionType, origin:str=None, protocol:str=None) -> Soup.WebsocketConnection
        new_with_extensions(stream:Gio.IOStream, uri:Soup.URI, type:Soup.WebsocketConnectionType, origin:str=None, protocol:str=None, extensions:list) -> Soup.WebsocketConnection
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, code, data=None): # real signature unknown; restored from __doc__
        """ close(self, code:int, data:str=None) """
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

    def do_closed(self, *args, **kwargs): # real signature unknown
        """ closed(self) """
        pass

    def do_closing(self, *args, **kwargs): # real signature unknown
        """ closing(self) """
        pass

    def do_error(self, *args, **kwargs): # real signature unknown
        """ error(self, error:error) """
        pass

    def do_message(self, *args, **kwargs): # real signature unknown
        """ message(self, type:Soup.WebsocketDataType, message:GLib.Bytes) """
        pass

    def do_pong(self, *args, **kwargs): # real signature unknown
        """ pong(self, message:GLib.Bytes) """
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

    def get_close_code(self): # real signature unknown; restored from __doc__
        """ get_close_code(self) -> int """
        return 0

    def get_close_data(self): # real signature unknown; restored from __doc__
        """ get_close_data(self) -> str """
        return ""

    def get_connection_type(self): # real signature unknown; restored from __doc__
        """ get_connection_type(self) -> Soup.WebsocketConnectionType """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_extensions(self): # real signature unknown; restored from __doc__
        """ get_extensions(self) -> list """
        return []

    def get_io_stream(self): # real signature unknown; restored from __doc__
        """ get_io_stream(self) -> Gio.IOStream """
        pass

    def get_keepalive_interval(self): # real signature unknown; restored from __doc__
        """ get_keepalive_interval(self) -> int """
        return 0

    def get_max_incoming_payload_size(self): # real signature unknown; restored from __doc__
        """ get_max_incoming_payload_size(self) -> int """
        return 0

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> str or None """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Soup.WebsocketState """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> Soup.URI """
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

    def new(self, stream, uri, type, origin=None, protocol=None): # real signature unknown; restored from __doc__
        """ new(stream:Gio.IOStream, uri:Soup.URI, type:Soup.WebsocketConnectionType, origin:str=None, protocol:str=None) -> Soup.WebsocketConnection """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_extensions(self, stream, uri, type, origin=None, protocol=None, extensions): # real signature unknown; restored from __doc__
        """ new_with_extensions(stream:Gio.IOStream, uri:Soup.URI, type:Soup.WebsocketConnectionType, origin:str=None, protocol:str=None, extensions:list) -> Soup.WebsocketConnection """
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

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_binary(self, data=None): # real signature unknown; restored from __doc__
        """ send_binary(self, data:list=None) """
        pass

    def send_message(self, type, message): # real signature unknown; restored from __doc__
        """ send_message(self, type:Soup.WebsocketDataType, message:GLib.Bytes) """
        pass

    def send_text(self, text): # real signature unknown; restored from __doc__
        """ send_text(self, text:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_keepalive_interval(self, interval): # real signature unknown; restored from __doc__
        """ set_keepalive_interval(self, interval:int) """
        pass

    def set_max_incoming_payload_size(self, max_incoming_payload_size): # real signature unknown; restored from __doc__
        """ set_max_incoming_payload_size(self, max_incoming_payload_size:int) """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f8e47e8d7c0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(WebsocketConnection), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupWebsocketConnection (94750594965312)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_extensions': gi.FunctionInfo(new_with_extensions), 'close': gi.FunctionInfo(close), 'get_close_code': gi.FunctionInfo(get_close_code), 'get_close_data': gi.FunctionInfo(get_close_data), 'get_connection_type': gi.FunctionInfo(get_connection_type), 'get_extensions': gi.FunctionInfo(get_extensions), 'get_io_stream': gi.FunctionInfo(get_io_stream), 'get_keepalive_interval': gi.FunctionInfo(get_keepalive_interval), 'get_max_incoming_payload_size': gi.FunctionInfo(get_max_incoming_payload_size), 'get_origin': gi.FunctionInfo(get_origin), 'get_protocol': gi.FunctionInfo(get_protocol), 'get_state': gi.FunctionInfo(get_state), 'get_uri': gi.FunctionInfo(get_uri), 'send_binary': gi.FunctionInfo(send_binary), 'send_message': gi.FunctionInfo(send_message), 'send_text': gi.FunctionInfo(send_text), 'set_keepalive_interval': gi.FunctionInfo(set_keepalive_interval), 'set_max_incoming_payload_size': gi.FunctionInfo(set_max_incoming_payload_size), 'do_closed': gi.VFuncInfo(closed), 'do_closing': gi.VFuncInfo(closing), 'do_error': gi.VFuncInfo(error), 'do_message': gi.VFuncInfo(message), 'do_pong': gi.VFuncInfo(pong), 'parent': <property object at 0x7f8e47f06400>, 'pv': <property object at 0x7f8e47f064f0>})"
    __gdoc__ = 'Object SoupWebsocketConnection\n\nSignals from SoupWebsocketConnection:\n  message (gint, GBytes)\n  error (GError)\n  closing ()\n  closed ()\n  pong (GBytes)\n\nProperties from SoupWebsocketConnection:\n  io-stream -> GIOStream: I/O Stream\n    Underlying I/O stream\n  connection-type -> SoupWebsocketConnectionType: Connection type\n    Connection type (client/server)\n  uri -> SoupURI: URI\n    The WebSocket URI\n  origin -> gchararray: Origin\n    The WebSocket origin\n  protocol -> gchararray: Protocol\n    The chosen WebSocket protocol\n  state -> SoupWebsocketState: State\n    State \n  max-incoming-payload-size -> guint64: Max incoming payload size\n    Max incoming payload size \n  keepalive-interval -> guint: Keepalive interval\n    Keepalive interval\n  extensions -> gpointer: Active extensions\n    The list of active extensions\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SoupWebsocketConnection (94750594965312)>'
    __info__ = ObjectInfo(WebsocketConnection)


