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


from .IOStream import IOStream

class TlsConnection(IOStream):
    """
    :Constructors:
    
    ::
    
        TlsConnection(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_pending(self): # real signature unknown; restored from __doc__
        """ clear_pending(self) """
        pass

    def close(self, cancellable=None): # real signature unknown; restored from __doc__
        """ close(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def close_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ close_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def close_finish(self, result): # real signature unknown; restored from __doc__
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def do_accept_certificate(self, *args, **kwargs): # real signature unknown
        """ accept_certificate(self, peer_cert:Gio.TlsCertificate, errors:Gio.TlsCertificateFlags) -> bool """
        pass

    def do_close_async(self, *args, **kwargs): # real signature unknown
        """ close_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_close_finish(self, *args, **kwargs): # real signature unknown
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_close_fn(self, *args, **kwargs): # real signature unknown
        """ close_fn(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_get_input_stream(self, *args, **kwargs): # real signature unknown
        """ get_input_stream(self) -> Gio.InputStream """
        pass

    def do_get_output_stream(self, *args, **kwargs): # real signature unknown
        """ get_output_stream(self) -> Gio.OutputStream """
        pass

    def do_handshake(self, *args, **kwargs): # real signature unknown
        """ handshake(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_handshake_async(self, *args, **kwargs): # real signature unknown
        """ handshake_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_handshake_finish(self, *args, **kwargs): # real signature unknown
        """ handshake_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_accept_certificate(self, peer_cert, errors): # real signature unknown; restored from __doc__
        """ emit_accept_certificate(self, peer_cert:Gio.TlsCertificate, errors:Gio.TlsCertificateFlags) -> bool """
        return False

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

    def get_certificate(self): # real signature unknown; restored from __doc__
        """ get_certificate(self) -> Gio.TlsCertificate """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_database(self): # real signature unknown; restored from __doc__
        """ get_database(self) -> Gio.TlsDatabase """
        pass

    def get_input_stream(self): # real signature unknown; restored from __doc__
        """ get_input_stream(self) -> Gio.InputStream """
        pass

    def get_interaction(self): # real signature unknown; restored from __doc__
        """ get_interaction(self) -> Gio.TlsInteraction """
        pass

    def get_negotiated_protocol(self): # real signature unknown; restored from __doc__
        """ get_negotiated_protocol(self) -> str or None """
        return ""

    def get_output_stream(self): # real signature unknown; restored from __doc__
        """ get_output_stream(self) -> Gio.OutputStream """
        pass

    def get_peer_certificate(self): # real signature unknown; restored from __doc__
        """ get_peer_certificate(self) -> Gio.TlsCertificate """
        pass

    def get_peer_certificate_errors(self): # real signature unknown; restored from __doc__
        """ get_peer_certificate_errors(self) -> Gio.TlsCertificateFlags """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rehandshake_mode(self): # real signature unknown; restored from __doc__
        """ get_rehandshake_mode(self) -> Gio.TlsRehandshakeMode """
        pass

    def get_require_close_notify(self): # real signature unknown; restored from __doc__
        """ get_require_close_notify(self) -> bool """
        return False

    def get_use_system_certdb(self): # real signature unknown; restored from __doc__
        """ get_use_system_certdb(self) -> bool """
        return False

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

    def handshake(self, cancellable=None): # real signature unknown; restored from __doc__
        """ handshake(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def handshake_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ handshake_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def handshake_finish(self, result): # real signature unknown; restored from __doc__
        """ handshake_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def has_pending(self): # real signature unknown; restored from __doc__
        """ has_pending(self) -> bool """
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

    def set_advertised_protocols(self, protocols=None): # real signature unknown; restored from __doc__
        """ set_advertised_protocols(self, protocols:list=None) """
        pass

    def set_certificate(self, certificate): # real signature unknown; restored from __doc__
        """ set_certificate(self, certificate:Gio.TlsCertificate) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_database(self, database): # real signature unknown; restored from __doc__
        """ set_database(self, database:Gio.TlsDatabase) """
        pass

    def set_interaction(self, interaction=None): # real signature unknown; restored from __doc__
        """ set_interaction(self, interaction:Gio.TlsInteraction=None) """
        pass

    def set_pending(self): # real signature unknown; restored from __doc__
        """ set_pending(self) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rehandshake_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_rehandshake_mode(self, mode:Gio.TlsRehandshakeMode) """
        pass

    def set_require_close_notify(self, require_close_notify): # real signature unknown; restored from __doc__
        """ set_require_close_notify(self, require_close_notify:bool) """
        pass

    def set_use_system_certdb(self, use_system_certdb): # real signature unknown; restored from __doc__
        """ set_use_system_certdb(self, use_system_certdb:bool) """
        pass

    def splice_async(self, stream2, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ splice_async(self, stream2:Gio.IOStream, flags:Gio.IOStreamSpliceFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def splice_finish(self, result): # real signature unknown; restored from __doc__
        """ splice_finish(result:Gio.AsyncResult) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f28dd07cbb0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TlsConnection), '__module__': 'gi.repository.Gio', '__gtype__': <GType GTlsConnection (94125582872416)>, '__doc__': None, '__gsignals__': {}, 'emit_accept_certificate': gi.FunctionInfo(emit_accept_certificate), 'get_certificate': gi.FunctionInfo(get_certificate), 'get_database': gi.FunctionInfo(get_database), 'get_interaction': gi.FunctionInfo(get_interaction), 'get_negotiated_protocol': gi.FunctionInfo(get_negotiated_protocol), 'get_peer_certificate': gi.FunctionInfo(get_peer_certificate), 'get_peer_certificate_errors': gi.FunctionInfo(get_peer_certificate_errors), 'get_rehandshake_mode': gi.FunctionInfo(get_rehandshake_mode), 'get_require_close_notify': gi.FunctionInfo(get_require_close_notify), 'get_use_system_certdb': gi.FunctionInfo(get_use_system_certdb), 'handshake': gi.FunctionInfo(handshake), 'handshake_async': gi.FunctionInfo(handshake_async), 'handshake_finish': gi.FunctionInfo(handshake_finish), 'set_advertised_protocols': gi.FunctionInfo(set_advertised_protocols), 'set_certificate': gi.FunctionInfo(set_certificate), 'set_database': gi.FunctionInfo(set_database), 'set_interaction': gi.FunctionInfo(set_interaction), 'set_rehandshake_mode': gi.FunctionInfo(set_rehandshake_mode), 'set_require_close_notify': gi.FunctionInfo(set_require_close_notify), 'set_use_system_certdb': gi.FunctionInfo(set_use_system_certdb), 'do_accept_certificate': gi.VFuncInfo(accept_certificate), 'do_handshake': gi.VFuncInfo(handshake), 'do_handshake_async': gi.VFuncInfo(handshake_async), 'do_handshake_finish': gi.VFuncInfo(handshake_finish), 'parent_instance': <property object at 0x7f28dde766d0>, 'priv': <property object at 0x7f28dde76810>})"
    __gdoc__ = 'Object GTlsConnection\n\nSignals from GTlsConnection:\n  accept-certificate (GTlsCertificate, GTlsCertificateFlags) -> gboolean\n\nProperties from GTlsConnection:\n  base-io-stream -> GIOStream: Base IOStream\n    The GIOStream that the connection wraps\n  require-close-notify -> gboolean: Require close notify\n    Whether to require proper TLS close notification\n  rehandshake-mode -> GTlsRehandshakeMode: Rehandshake mode\n    When to allow rehandshaking\n  use-system-certdb -> gboolean: Use system certificate database\n    Whether to verify peer certificates against the system certificate database\n  database -> GTlsDatabase: Database\n    Certificate database to use for looking up or verifying certificates\n  interaction -> GTlsInteraction: Interaction\n    Optional object for user interaction\n  certificate -> GTlsCertificate: Certificate\n    The connection’s certificate\n  peer-certificate -> GTlsCertificate: Peer Certificate\n    The connection’s peer’s certificate\n  peer-certificate-errors -> GTlsCertificateFlags: Peer Certificate Errors\n    Errors found with the peer’s certificate\n  advertised-protocols -> GStrv: Advertised Protocols\n    Application-layer protocols available on this connection\n  negotiated-protocol -> gchararray: Negotiated Protocol\n    Application-layer protocol negotiated for this connection\n\nProperties from GIOStream:\n  input-stream -> GInputStream: Input stream\n    The GInputStream to read from\n  output-stream -> GOutputStream: Output stream\n    The GOutputStream to write to\n  closed -> gboolean: Closed\n    Is the stream closed\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GTlsConnection (94125582872416)>'
    __info__ = ObjectInfo(TlsConnection)


