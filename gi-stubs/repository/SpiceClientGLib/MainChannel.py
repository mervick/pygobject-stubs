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


from .Channel import Channel

class MainChannel(Channel):
    """
    :Constructors:
    
    ::
    
        MainChannel(**properties)
    """
    def agent_test_capability(self, cap): # real signature unknown; restored from __doc__
        """ agent_test_capability(self, cap:int) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clipboard_selection_grab(self, selection, types, ntypes): # real signature unknown; restored from __doc__
        """ clipboard_selection_grab(self, selection:int, types:int, ntypes:int) """
        pass

    def clipboard_selection_notify(self, selection, type, data, size): # real signature unknown; restored from __doc__
        """ clipboard_selection_notify(self, selection:int, type:int, data:int, size:int) """
        pass

    def clipboard_selection_release(self, selection): # real signature unknown; restored from __doc__
        """ clipboard_selection_release(self, selection:int) """
        pass

    def clipboard_selection_request(self, selection, type): # real signature unknown; restored from __doc__
        """ clipboard_selection_request(self, selection:int, type:int) """
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

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def disconnect(self, reason): # real signature unknown; restored from __doc__
        """ disconnect(self, reason:SpiceClientGLib.ChannelEvent) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_channel_event(self, *args, **kwargs): # real signature unknown
        """ channel_event(self, event:SpiceClientGLib.ChannelEvent) """
        pass

    def do_channel_reset(self, *args, **kwargs): # real signature unknown
        """ channel_reset(self, migrating:bool) """
        pass

    def do_channel_send_migration_handshake(self, *args, **kwargs): # real signature unknown
        """ channel_send_migration_handshake(self) """
        pass

    def do_channel_up(self, *args, **kwargs): # real signature unknown
        """ channel_up(self) """
        pass

    def do_handle_msg(self, *args, **kwargs): # real signature unknown
        """ handle_msg(self, msg:SpiceClientGLib.MsgIn) """
        pass

    def do_iterate_read(self, *args, **kwargs): # real signature unknown
        """ iterate_read(self) """
        pass

    def do_iterate_write(self, *args, **kwargs): # real signature unknown
        """ iterate_write(self) """
        pass

    def do_open_fd(self, *args, **kwargs): # real signature unknown
        """ open_fd(self, with_tls:int) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def file_copy_async(self, sources, flags, cancellable=None, progress_callback=None, progress_callback_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ file_copy_async(self, sources:list, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def file_copy_finish(self, result): # real signature unknown; restored from __doc__
        """ file_copy_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ flush_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def flush_finish(self, result): # real signature unknown; restored from __doc__
        """ flush_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def get_error(self): # real signature unknown; restored from __doc__
        """ get_error(self) -> error """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def new(self, s, type, id): # real signature unknown; restored from __doc__
        """ new(s:SpiceClientGLib.Session, type:int, id:int) -> SpiceClientGLib.Channel """
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

    def request_mouse_mode(self, mode): # real signature unknown; restored from __doc__
        """ request_mouse_mode(self, mode:int) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_monitor_config(self): # real signature unknown; restored from __doc__
        """ send_monitor_config(self) -> bool """
        return False

    def set_capability(self, cap): # real signature unknown; restored from __doc__
        """ set_capability(self, cap:int) """
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

    def string_to_type(self, p_str): # real signature unknown; restored from __doc__
        """ string_to_type(str:str) -> int """
        return 0

    def test_capability(self, cap): # real signature unknown; restored from __doc__
        """ test_capability(self, cap:int) -> bool """
        return False

    def test_common_capability(self, cap): # real signature unknown; restored from __doc__
        """ test_common_capability(self, cap:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def type_to_string(self, type): # real signature unknown; restored from __doc__
        """ type_to_string(type:int) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update_display(self, id, x, y, width, height, update): # real signature unknown; restored from __doc__
        """ update_display(self, id:int, x:int, y:int, width:int, height:int, update:bool) """
        pass

    def update_display_enabled(self, id, enabled, update): # real signature unknown; restored from __doc__
        """ update_display_enabled(self, id:int, enabled:bool, update:bool) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9dce6e9c10>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MainChannel), '__module__': 'gi.repository.SpiceClientGLib', '__gtype__': <GType SpiceMainChannel (93951199808448)>, '__doc__': None, '__gsignals__': {}, 'agent_test_capability': gi.FunctionInfo(agent_test_capability), 'clipboard_selection_grab': gi.FunctionInfo(clipboard_selection_grab), 'clipboard_selection_notify': gi.FunctionInfo(clipboard_selection_notify), 'clipboard_selection_release': gi.FunctionInfo(clipboard_selection_release), 'clipboard_selection_request': gi.FunctionInfo(clipboard_selection_request), 'file_copy_async': gi.FunctionInfo(file_copy_async), 'file_copy_finish': gi.FunctionInfo(file_copy_finish), 'request_mouse_mode': gi.FunctionInfo(request_mouse_mode), 'send_monitor_config': gi.FunctionInfo(send_monitor_config), 'update_display': gi.FunctionInfo(update_display), 'update_display_enabled': gi.FunctionInfo(update_display_enabled), 'parent': <property object at 0x7f9dce6df860>, 'priv': <property object at 0x7f9dce6df950>})"
    __gdoc__ = 'Object SpiceMainChannel\n\nSignals from SpiceMainChannel:\n  main-mouse-update ()\n  main-agent-update ()\n  main-clipboard (guint, gpointer, guint)\n  main-clipboard-selection (guint, guint, gpointer, guint)\n  main-clipboard-grab (gpointer, guint) -> gboolean\n  main-clipboard-selection-grab (guint, gpointer, guint) -> gboolean\n  main-clipboard-request (guint) -> gboolean\n  main-clipboard-selection-request (guint, guint) -> gboolean\n  main-clipboard-release ()\n  main-clipboard-selection-release (guint)\n  migration-started (GObject)\n  new-file-transfer (GObject)\n\nProperties from SpiceMainChannel:\n  mouse-mode -> gint: Mouse mode\n    Mouse mode\n  agent-connected -> gboolean: Agent connected\n    Whether the agent is connected\n  agent-caps-0 -> gint: Agent caps 0\n    Agent capability bits 0 -> 31\n  disable-wallpaper -> gboolean: Disable guest wallpaper\n    Disable guest wallpaper\n  disable-font-smooth -> gboolean: Disable guest font smooth\n    Disable guest font smoothing\n  disable-animation -> gboolean: Disable guest animations\n    Disable guest animations\n  color-depth -> guint: Color depth\n    Color depth\n  disable-display-position -> gboolean: Disable display position\n    Disable using display position when setting monitor config\n  disable-display-align -> gboolean: Disable display align\n    Disable display position alignment\n  max-clipboard -> gint: max clipboard\n    Maximum clipboard data size\n\nSignals from SpiceChannel:\n  channel-event (SpiceChannelEvent)\n  open-fd (gint)\n\nProperties from SpiceChannel:\n  spice-session -> SpiceSession: Spice session\n    Spice session\n  channel-type -> gint: Channel type\n    Channel type\n  channel-id -> gint: Channel ID\n    Channel ID\n  total-read-bytes -> gulong: Total read bytes\n    Total read bytes\n  socket -> GSocket: Socket\n    Underlying GSocket\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SpiceMainChannel (93951199808448)>'
    __info__ = ObjectInfo(MainChannel)


