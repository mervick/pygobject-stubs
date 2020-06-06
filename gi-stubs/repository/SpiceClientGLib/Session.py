# encoding: utf-8
# module gi.repository.SpiceClientGLib
# from /usr/lib64/girepository-1.0/SpiceClientGLib-2.0.typelib
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


class Session(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Session(**properties)
        new() -> SpiceClientGLib.Session
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

    def connect(self): # real signature unknown; restored from __doc__
        """ connect(self) -> bool """
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

    def disconnect(self): # real signature unknown; restored from __doc__
        """ disconnect(self) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_channel_destroy(self, *args, **kwargs): # real signature unknown
        """ channel_destroy(self, channel:SpiceClientGLib.Channel) """
        pass

    def do_channel_new(self, *args, **kwargs): # real signature unknown
        """ channel_new(self, channel:SpiceClientGLib.Channel) """
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

    def get_channels(self): # real signature unknown; restored from __doc__
        """ get_channels(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_proxy_uri(self): # real signature unknown; restored from __doc__
        """ get_proxy_uri(self) -> SpiceClientGLib.URI """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_read_only(self): # real signature unknown; restored from __doc__
        """ get_read_only(self) -> bool """
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

    def has_channel_type(self, type): # real signature unknown; restored from __doc__
        """ has_channel_type(self, type:int) -> bool """
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

    def is_for_migration(self): # real signature unknown; restored from __doc__
        """ is_for_migration(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> SpiceClientGLib.Session """
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

    def open_fd(self, fd): # real signature unknown; restored from __doc__
        """ open_fd(self, fd:int) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9dcd5c7fd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Session), '__module__': 'gi.repository.SpiceClientGLib', '__gtype__': <GType SpiceSession (93951199846064)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'connect': gi.FunctionInfo(connect), 'disconnect': gi.FunctionInfo(disconnect), 'get_channels': gi.FunctionInfo(get_channels), 'get_proxy_uri': gi.FunctionInfo(get_proxy_uri), 'get_read_only': gi.FunctionInfo(get_read_only), 'has_channel_type': gi.FunctionInfo(has_channel_type), 'is_for_migration': gi.FunctionInfo(is_for_migration), 'open_fd': gi.FunctionInfo(open_fd), 'do_channel_destroy': gi.VFuncInfo(channel_destroy), 'do_channel_new': gi.VFuncInfo(channel_new), 'parent': <property object at 0x7f9dce6e53b0>, 'priv': <property object at 0x7f9dce6e54a0>})"
    __gdoc__ = "Object SpiceSession\n\nSignals from SpiceSession:\n  channel-new (SpiceChannel)\n  channel-destroy (SpiceChannel)\n  disconnected ()\n  mm-time-reset ()\n\nProperties from SpiceSession:\n  host -> gchararray: Host\n    Remote host\n  port -> gchararray: Port\n    Remote port (plaintext)\n  tls-port -> gchararray: TLS port\n    Remote port (encrypted)\n  password -> gchararray: Password\n    \n  ca-file -> gchararray: CA file\n    File holding the CA certificates\n  ciphers -> gchararray: Ciphers\n    SSL cipher list\n  protocol -> gint: Protocol\n    Spice protocol major version\n  uri -> gchararray: URI\n    Spice connection URI\n  client-sockets -> gboolean: Client sockets\n    Sockets are provided by the client\n  pubkey -> GByteArray: Pub Key\n    Public key to check\n  cert-subject -> gchararray: Cert Subject\n    Certificate subject to check\n  verify -> SpiceSessionVerify: Verify\n    Certificate verification parameters\n  migration-state -> SpiceSessionMigration: Migration state\n    Migration state\n  enable-audio -> gboolean: Enable audio channels\n    Enable audio channels\n  enable-smartcard -> gboolean: Enable smartcard event forwarding\n    Forward smartcard events to the SPICE server\n  smartcard-certificates -> GStrv: Smartcard certificates\n    Smartcard certificates for software-based smartcards\n  smartcard-db -> gchararray: Smartcard certificate database\n    Path to the database for smartcard certificates\n  enable-usbredir -> gboolean: Enable USB device redirection\n    Forward USB devices to the SPICE server\n  inhibit-keyboard-grab -> gboolean: Inhibit Keyboard Grab\n    Request that SpiceDisplays don't grab the keyboard\n  disable-effects -> GStrv: Disable effects\n    Comma-separated effects to disable\n  color-depth -> gint: Color depth\n    Display channel color depth\n  read-only -> gboolean: Read-only\n    Whether this connection is read-only mode\n  cache-size -> gint: Cache size\n    Images cache size (bytes)\n  glz-window-size -> gint: Glz window size\n    Glz window size (bytes)\n  uuid -> gpointer: UUID\n    Spice server uuid\n  name -> gchararray: Name\n    Spice server name\n  ca -> GByteArray: CA\n    The CA certificates data\n  proxy -> gchararray: Proxy\n    The proxy server\n  secure-channels -> GStrv: Secure channels\n    Array of channel type to secure\n  shared-dir -> gchararray: Shared directory\n    Shared directory\n  share-dir-ro -> gboolean: Share directory read-only\n    Share directory read-only\n  username -> gchararray: Username\n    Username used for SASL connections\n  unix-path -> gchararray: Unix path\n    Unix path\n  preferred-compression -> SpiceImageCompress: Preferred image compression algorithm\n    Preferred image compression algorithm\n  gl-scanout -> gboolean: Enable GL scanout support\n    Enable GL scanout support\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SpiceSession (93951199846064)>'
    __info__ = ObjectInfo(Session)


