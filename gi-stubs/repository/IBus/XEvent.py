# encoding: utf-8
# module gi.repository.IBus
# from /usr/lib64/girepository-1.0/IBus-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .Serializable import Serializable

class XEvent(Serializable):
    """
    :Constructors:
    
    ::
    
        XEvent(**properties)
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

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> IBus.Serializable """
        pass

    def deserialize_object(self, variant): # real signature unknown; restored from __doc__
        """ deserialize_object(variant:GLib.Variant) -> IBus.Serializable """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_copy(self, *args, **kwargs): # real signature unknown
        """ copy(self, src:IBus.Serializable) -> bool """
        pass

    def do_deserialize(self, *args, **kwargs): # real signature unknown
        """ deserialize(self, variant:GLib.Variant) -> int """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_serialize(self, *args, **kwargs): # real signature unknown
        """ serialize(self, builder:GLib.VariantBuilder) -> bool """
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

    def get_event_type(self): # real signature unknown; restored from __doc__
        """ get_event_type(self) -> IBus.XEventType """
        pass

    def get_group(self): # real signature unknown; restored from __doc__
        """ get_group(self) -> int """
        return 0

    def get_hardware_keycode(self): # real signature unknown; restored from __doc__
        """ get_hardware_keycode(self) -> int """
        return 0

    def get_is_modifier(self): # real signature unknown; restored from __doc__
        """ get_is_modifier(self) -> bool """
        return False

    def get_keyval(self): # real signature unknown; restored from __doc__
        """ get_keyval(self) -> int """
        return 0

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_purpose(self): # real signature unknown; restored from __doc__
        """ get_purpose(self) -> str """
        return ""

    def get_qattachment(self, key): # real signature unknown; restored from __doc__
        """ get_qattachment(self, key:int) -> GLib.Variant """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_root(self): # real signature unknown; restored from __doc__
        """ get_root(self) -> int """
        return 0

    def get_same_screen(self): # real signature unknown; restored from __doc__
        """ get_same_screen(self) -> bool """
        return False

    def get_send_event(self): # real signature unknown; restored from __doc__
        """ get_send_event(self) -> int """
        return 0

    def get_serial(self): # real signature unknown; restored from __doc__
        """ get_serial(self) -> int """
        return 0

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> int """
        return 0

    def get_string(self): # real signature unknown; restored from __doc__
        """ get_string(self) -> str """
        return ""

    def get_subwindow(self): # real signature unknown; restored from __doc__
        """ get_subwindow(self) -> int """
        return 0

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> int """
        return 0

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> int """
        return 0

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> int """
        return 0

    def get_x_root(self): # real signature unknown; restored from __doc__
        """ get_x_root(self) -> int """
        return 0

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> int """
        return 0

    def get_y_root(self): # real signature unknown; restored from __doc__
        """ get_y_root(self) -> int """
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> IBus.Serializable """
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

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_qattachment(self, key): # real signature unknown; restored from __doc__
        """ remove_qattachment(self, key:int) """
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

    def serialize_object(self): # real signature unknown; restored from __doc__
        """ serialize_object(self) -> GLib.Variant """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_qattachment(self, key, value): # real signature unknown; restored from __doc__
        """ set_qattachment(self, key:int, value:GLib.Variant) """
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

    event_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    send_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f59b10db5e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(XEvent), '__module__': 'gi.repository.IBus', '__gtype__': <GType IBusXEvent (94061790389776)>, '__doc__': None, '__gsignals__': {}, 'get_event_type': gi.FunctionInfo(get_event_type), 'get_group': gi.FunctionInfo(get_group), 'get_hardware_keycode': gi.FunctionInfo(get_hardware_keycode), 'get_is_modifier': gi.FunctionInfo(get_is_modifier), 'get_keyval': gi.FunctionInfo(get_keyval), 'get_length': gi.FunctionInfo(get_length), 'get_purpose': gi.FunctionInfo(get_purpose), 'get_root': gi.FunctionInfo(get_root), 'get_same_screen': gi.FunctionInfo(get_same_screen), 'get_send_event': gi.FunctionInfo(get_send_event), 'get_serial': gi.FunctionInfo(get_serial), 'get_state': gi.FunctionInfo(get_state), 'get_string': gi.FunctionInfo(get_string), 'get_subwindow': gi.FunctionInfo(get_subwindow), 'get_time': gi.FunctionInfo(get_time), 'get_version': gi.FunctionInfo(get_version), 'get_window': gi.FunctionInfo(get_window), 'get_x': gi.FunctionInfo(get_x), 'get_x_root': gi.FunctionInfo(get_x_root), 'get_y': gi.FunctionInfo(get_y), 'get_y_root': gi.FunctionInfo(get_y_root), 'parent': <property object at 0x7f59b12dd450>, 'priv': <property object at 0x7f59b12dd540>, 'event_type': <property object at 0x7f59b12dd630>, 'window': <property object at 0x7f59b12dd720>, 'send_event': <property object at 0x7f59b12dd810>, 'serial': <property object at 0x7f59b12dd900>})"
    __gdoc__ = 'Object IBusXEvent\n\nProperties from IBusXEvent:\n  version -> guint: version\n    version\n  event-type -> gint: event type\n    event type\n  window -> guint: window\n    window\n  send-event -> gint: send event\n    send event\n  serial -> gulong: serial\n    serial\n  time -> guint: time\n    time\n  state -> guint: state\n    state\n  keyval -> guint: keyval\n    keyval\n  length -> gint: length\n    length\n  string -> gchararray: string\n    string\n  hardware-keycode -> guint: hardware keycode\n    hardware keycode\n  group -> guint: group\n    group\n  is-modifier -> gboolean: is modifier\n    is modifier\n  root -> guint: root\n    root\n  subwindow -> guint: subwindow\n    subwindow\n  x -> gint: x\n    x\n  y -> gint: y\n    y\n  x-root -> gint: x root\n    x root\n  y-root -> gint: y root\n    y root\n  same-screen -> gboolean: same screen\n    same screen\n  purpose -> gchararray: purpose\n    purpose\n\nSignals from IBusObject:\n  destroy ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType IBusXEvent (94061790389776)>'
    __info__ = ObjectInfo(XEvent)


