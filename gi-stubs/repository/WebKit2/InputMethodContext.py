# encoding: utf-8
# module gi.repository.WebKit2
# from /usr/lib64/girepository-1.0/WebKit2-4.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class InputMethodContext(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        InputMethodContext(**properties)
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

    def do_committed(self, *args, **kwargs): # real signature unknown
        """ committed(self, text:str) """
        pass

    def do_delete_surrounding(self, *args, **kwargs): # real signature unknown
        """ delete_surrounding(self, offset:int, n_chars:int) """
        pass

    def do_filter_key_event(self, *args, **kwargs): # real signature unknown
        """ filter_key_event(self, key_event:Gdk.EventKey) -> bool """
        pass

    def do_get_preedit(self, *args, **kwargs): # real signature unknown
        """ get_preedit(self) -> text:str, underlines:list, cursor_offset:int """
        pass

    def do_notify_cursor_area(self, *args, **kwargs): # real signature unknown
        """ notify_cursor_area(self, x:int, y:int, width:int, height:int) """
        pass

    def do_notify_focus_in(self, *args, **kwargs): # real signature unknown
        """ notify_focus_in(self) """
        pass

    def do_notify_focus_out(self, *args, **kwargs): # real signature unknown
        """ notify_focus_out(self) """
        pass

    def do_notify_surrounding(self, *args, **kwargs): # real signature unknown
        """ notify_surrounding(self, text:str, length:int, cursor_index:int, selection_index:int) """
        pass

    def do_preedit_changed(self, *args, **kwargs): # real signature unknown
        """ preedit_changed(self) """
        pass

    def do_preedit_finished(self, *args, **kwargs): # real signature unknown
        """ preedit_finished(self) """
        pass

    def do_preedit_started(self, *args, **kwargs): # real signature unknown
        """ preedit_started(self) """
        pass

    def do_reset(self, *args, **kwargs): # real signature unknown
        """ reset(self) """
        pass

    def do_set_enable_preedit(self, *args, **kwargs): # real signature unknown
        """ set_enable_preedit(self, enabled:bool) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def filter_key_event(self, key_event): # real signature unknown; restored from __doc__
        """ filter_key_event(self, key_event:Gdk.EventKey) -> bool """
        return False

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

    def get_input_hints(self): # real signature unknown; restored from __doc__
        """ get_input_hints(self) -> WebKit2.InputHints """
        pass

    def get_input_purpose(self): # real signature unknown; restored from __doc__
        """ get_input_purpose(self) -> WebKit2.InputPurpose """
        pass

    def get_preedit(self): # real signature unknown; restored from __doc__
        """ get_preedit(self) -> text:str, underlines:list, cursor_offset:int """
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

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_cursor_area(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ notify_cursor_area(self, x:int, y:int, width:int, height:int) """
        pass

    def notify_focus_in(self): # real signature unknown; restored from __doc__
        """ notify_focus_in(self) """
        pass

    def notify_focus_out(self): # real signature unknown; restored from __doc__
        """ notify_focus_out(self) """
        pass

    def notify_surrounding(self, text, length, cursor_index, selection_index): # real signature unknown; restored from __doc__
        """ notify_surrounding(self, text:str, length:int, cursor_index:int, selection_index:int) """
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

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_enable_preedit(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_preedit(self, enabled:bool) """
        pass

    def set_input_hints(self, hints): # real signature unknown; restored from __doc__
        """ set_input_hints(self, hints:WebKit2.InputHints) """
        pass

    def set_input_purpose(self, purpose): # real signature unknown; restored from __doc__
        """ set_input_purpose(self, purpose:WebKit2.InputPurpose) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc3e7197be0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(InputMethodContext), '__module__': 'gi.repository.WebKit2', '__gtype__': <GType WebKitInputMethodContext (94869774750576)>, '__doc__': None, '__gsignals__': {}, 'filter_key_event': gi.FunctionInfo(filter_key_event), 'get_input_hints': gi.FunctionInfo(get_input_hints), 'get_input_purpose': gi.FunctionInfo(get_input_purpose), 'get_preedit': gi.FunctionInfo(get_preedit), 'notify_cursor_area': gi.FunctionInfo(notify_cursor_area), 'notify_focus_in': gi.FunctionInfo(notify_focus_in), 'notify_focus_out': gi.FunctionInfo(notify_focus_out), 'notify_surrounding': gi.FunctionInfo(notify_surrounding), 'reset': gi.FunctionInfo(reset), 'set_enable_preedit': gi.FunctionInfo(set_enable_preedit), 'set_input_hints': gi.FunctionInfo(set_input_hints), 'set_input_purpose': gi.FunctionInfo(set_input_purpose), 'do_committed': gi.VFuncInfo(committed), 'do_delete_surrounding': gi.VFuncInfo(delete_surrounding), 'do_filter_key_event': gi.VFuncInfo(filter_key_event), 'do_get_preedit': gi.VFuncInfo(get_preedit), 'do_notify_cursor_area': gi.VFuncInfo(notify_cursor_area), 'do_notify_focus_in': gi.VFuncInfo(notify_focus_in), 'do_notify_focus_out': gi.VFuncInfo(notify_focus_out), 'do_notify_surrounding': gi.VFuncInfo(notify_surrounding), 'do_preedit_changed': gi.VFuncInfo(preedit_changed), 'do_preedit_finished': gi.VFuncInfo(preedit_finished), 'do_preedit_started': gi.VFuncInfo(preedit_started), 'do_reset': gi.VFuncInfo(reset), 'do_set_enable_preedit': gi.VFuncInfo(set_enable_preedit), 'parent': <property object at 0x7fc3eec10ea0>, 'priv': <property object at 0x7fc3eec126d0>})"
    __gdoc__ = 'Object WebKitInputMethodContext\n\nSignals from WebKitInputMethodContext:\n  preedit-started ()\n  preedit-changed ()\n  preedit-finished ()\n  committed (gchararray)\n  delete-surrounding (gint, guint)\n\nProperties from WebKitInputMethodContext:\n  input-purpose -> WebKitInputPurpose: Input Purpose\n    The purpose of the input associated\n  input-hints -> WebKitInputHints: Input Hints\n    The hints of the input associated\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitInputMethodContext (94869774750576)>'
    __info__ = ObjectInfo(InputMethodContext)


