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


from .Engine import Engine

class EngineSimple(Engine):
    """
    :Constructors:
    
    ::
    
        EngineSimple(**properties)
    """
    def add_compose_file(self, file): # real signature unknown; restored from __doc__
        """ add_compose_file(self, file:str) -> bool """
        return False

    def add_interfaces(self, xml_data): # real signature unknown; restored from __doc__
        """ add_interfaces(self, xml_data:str) -> bool """
        return False

    def add_table(self, data, max_seq_len, n_seqs): # real signature unknown; restored from __doc__
        """ add_table(self, data:list, max_seq_len:int, n_seqs:int) """
        pass

    def add_table_by_locale(self, locale=None): # real signature unknown; restored from __doc__
        """ add_table_by_locale(self, locale:str=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def commit_text(self, text): # real signature unknown; restored from __doc__
        """ commit_text(self, text:IBus.Text) """
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

    def delete_surrounding_text(self, offset, nchars): # real signature unknown; restored from __doc__
        """ delete_surrounding_text(self, offset:int, nchars:int) """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_cancel_hand_writing(self, *args, **kwargs): # real signature unknown
        """ cancel_hand_writing(self, n_strokes:int) """
        pass

    def do_candidate_clicked(self, *args, **kwargs): # real signature unknown
        """ candidate_clicked(self, index:int, button:int, state:int) """
        pass

    def do_cursor_down(self, *args, **kwargs): # real signature unknown
        """ cursor_down(self) """
        pass

    def do_cursor_up(self, *args, **kwargs): # real signature unknown
        """ cursor_up(self) """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_disable(self, *args, **kwargs): # real signature unknown
        """ disable(self) """
        pass

    def do_enable(self, *args, **kwargs): # real signature unknown
        """ enable(self) """
        pass

    def do_focus_in(self, *args, **kwargs): # real signature unknown
        """ focus_in(self) """
        pass

    def do_focus_out(self, *args, **kwargs): # real signature unknown
        """ focus_out(self) """
        pass

    def do_page_down(self, *args, **kwargs): # real signature unknown
        """ page_down(self) """
        pass

    def do_page_up(self, *args, **kwargs): # real signature unknown
        """ page_up(self) """
        pass

    def do_process_hand_writing_event(self, *args, **kwargs): # real signature unknown
        """ process_hand_writing_event(self, coordinates:float, coordinates_len:int) """
        pass

    def do_process_key_event(self, *args, **kwargs): # real signature unknown
        """ process_key_event(self, keyval:int, keycode:int, state:int) -> bool """
        pass

    def do_property_activate(self, *args, **kwargs): # real signature unknown
        """ property_activate(self, prop_name:str, prop_state:int) """
        pass

    def do_property_hide(self, *args, **kwargs): # real signature unknown
        """ property_hide(self, prop_name:str) """
        pass

    def do_property_show(self, *args, **kwargs): # real signature unknown
        """ property_show(self, prop_name:str) """
        pass

    def do_reset(self, *args, **kwargs): # real signature unknown
        """ reset(self) """
        pass

    def do_service_get_property(self, *args, **kwargs): # real signature unknown
        """ service_get_property(self, connection:Gio.DBusConnection, sender:str, object_path:str, interface_name:str, property_name:str) -> GLib.Variant or None """
        pass

    def do_service_method_call(self, *args, **kwargs): # real signature unknown
        """ service_method_call(self, connection:Gio.DBusConnection, sender:str, object_path:str, interface_name:str, method_name:str, parameters:GLib.Variant, invocation:Gio.DBusMethodInvocation) """
        pass

    def do_service_set_property(self, *args, **kwargs): # real signature unknown
        """ service_set_property(self, connection:Gio.DBusConnection, sender:str, object_path:str, interface_name:str, property_name:str, value:GLib.Variant) -> bool """
        pass

    def do_set_capabilities(self, *args, **kwargs): # real signature unknown
        """ set_capabilities(self, caps:int) """
        pass

    def do_set_content_type(self, *args, **kwargs): # real signature unknown
        """ set_content_type(self, purpose:int, hints:int) """
        pass

    def do_set_cursor_location(self, *args, **kwargs): # real signature unknown
        """ set_cursor_location(self, x:int, y:int, w:int, h:int) """
        pass

    def do_set_surrounding_text(self, *args, **kwargs): # real signature unknown
        """ set_surrounding_text(self, text:IBus.Text, cursor_index:int, anchor_pos:int) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_signal(self, dest_bus_name, interface_name, signal_name, parameters): # real signature unknown; restored from __doc__
        """ emit_signal(self, dest_bus_name:str, interface_name:str, signal_name:str, parameters:GLib.Variant) -> bool """
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

    def forward_key_event(self, keyval, keycode, state): # real signature unknown; restored from __doc__
        """ forward_key_event(self, keyval:int, keycode:int, state:int) """
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

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> purpose:int, hints:int """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_surrounding_text(self): # real signature unknown; restored from __doc__
        """ get_surrounding_text(self) -> text:IBus.Text, cursor_pos:int, anchor_pos:int """
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

    def hide_auxiliary_text(self): # real signature unknown; restored from __doc__
        """ hide_auxiliary_text(self) """
        pass

    def hide_lookup_table(self): # real signature unknown; restored from __doc__
        """ hide_lookup_table(self) """
        pass

    def hide_preedit_text(self): # real signature unknown; restored from __doc__
        """ hide_preedit_text(self) """
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

    def new(self, engine_name, object_path, connection): # real signature unknown; restored from __doc__
        """ new(engine_name:str, object_path:str, connection:Gio.DBusConnection) -> IBus.Engine """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_type(self, engine_type, engine_name, object_path, connection): # real signature unknown; restored from __doc__
        """ new_with_type(engine_type:GType, engine_name:str, object_path:str, connection:Gio.DBusConnection) -> IBus.Engine """
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

    def register(self, connection): # real signature unknown; restored from __doc__
        """ register(self, connection:Gio.DBusConnection) -> bool """
        return False

    def register_properties(self, prop_list): # real signature unknown; restored from __doc__
        """ register_properties(self, prop_list:IBus.PropList) """
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

    def show_auxiliary_text(self): # real signature unknown; restored from __doc__
        """ show_auxiliary_text(self) """
        pass

    def show_lookup_table(self): # real signature unknown; restored from __doc__
        """ show_lookup_table(self) """
        pass

    def show_preedit_text(self): # real signature unknown; restored from __doc__
        """ show_preedit_text(self) """
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

    def unregister(self, connection): # real signature unknown; restored from __doc__
        """ unregister(self, connection:Gio.DBusConnection) """
        pass

    def update_auxiliary_text(self, text, visible): # real signature unknown; restored from __doc__
        """ update_auxiliary_text(self, text:IBus.Text, visible:bool) """
        pass

    def update_lookup_table(self, lookup_table, visible): # real signature unknown; restored from __doc__
        """ update_lookup_table(self, lookup_table:IBus.LookupTable, visible:bool) """
        pass

    def update_lookup_table_fast(self, lookup_table, visible): # real signature unknown; restored from __doc__
        """ update_lookup_table_fast(self, lookup_table:IBus.LookupTable, visible:bool) """
        pass

    def update_preedit_text(self, text, cursor_pos, visible): # real signature unknown; restored from __doc__
        """ update_preedit_text(self, text:IBus.Text, cursor_pos:int, visible:bool) """
        pass

    def update_preedit_text_with_mode(self, text, cursor_pos, visible, mode): # real signature unknown; restored from __doc__
        """ update_preedit_text_with_mode(self, text:IBus.Text, cursor_pos:int, visible:bool, mode:IBus.PreeditFocusMode) """
        pass

    def update_property(self, prop): # real signature unknown; restored from __doc__
        """ update_property(self, prop:IBus.Property) """
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

    client_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f59b1235be0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(EngineSimple), '__module__': 'gi.repository.IBus', '__gtype__': <GType IBusEngineSimple (94061790152704)>, '__doc__': None, '__gsignals__': {}, 'add_compose_file': gi.FunctionInfo(add_compose_file), 'add_table': gi.FunctionInfo(add_table), 'add_table_by_locale': gi.FunctionInfo(add_table_by_locale), 'parent': <property object at 0x7f59b12b1630>, 'priv': <property object at 0x7f59b12b1720>})"
    __gdoc__ = 'Object IBusEngineSimple\n\nSignals from IBusEngine:\n  process-key-event (guint, guint, guint) -> gboolean\n  focus-in ()\n  focus-out ()\n  reset ()\n  enable ()\n  disable ()\n  set-cursor-location (gint, gint, gint, gint)\n  set-capabilities (guint)\n  page-up ()\n  page-down ()\n  cursor-up ()\n  cursor-down ()\n  candidate-clicked (guint, guint, guint)\n  property-activate (gchararray, guint)\n  property-show (gchararray)\n  property-hide (gchararray)\n  process-hand-writing-event (gpointer, guint)\n  cancel-hand-writing (guint)\n  set-surrounding-text (GObject, guint, guint)\n  set-content-type (guint, guint)\n\nProperties from IBusEngine:\n  engine-name -> gchararray: engine name\n    engine name\n\nProperties from IBusService:\n  object-path -> gchararray: object path\n    The path of service object\n  connection -> GDBusConnection: connection\n    The connection of service object\n\nSignals from IBusObject:\n  destroy ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType IBusEngineSimple (94061790152704)>'
    __info__ = ObjectInfo(EngineSimple)


