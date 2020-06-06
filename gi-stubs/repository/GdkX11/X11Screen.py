# encoding: utf-8
# module gi.repository.GdkX11
# from /usr/lib64/girepository-1.0/GdkX11-2.0.typelib
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
import gi.overrides.Gdk as __gi_overrides_Gdk
import gi.repository.Gdk as __gi_repository_Gdk


class X11Screen(__gi_repository_Gdk.Screen):
    """
    :Constructors:
    
    ::
    
        X11Screen(**properties)
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

    def get_active_window(self): # real signature unknown; restored from __doc__
        """ get_active_window(self) -> Gdk.Window or None """
        pass

    def get_current_desktop(self): # real signature unknown; restored from __doc__
        """ get_current_desktop(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gdk.Screen or None """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_font_options(self): # real signature unknown; restored from __doc__
        """ get_font_options(self) -> cairo.FontOptions or None """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_height_mm(self): # real signature unknown; restored from __doc__
        """ get_height_mm(self) -> int """
        return 0

    def get_monitor_at_point(self, x, y): # real signature unknown; restored from __doc__
        """ get_monitor_at_point(self, x:int, y:int) -> int """
        return 0

    def get_monitor_at_window(self, window): # real signature unknown; restored from __doc__
        """ get_monitor_at_window(self, window:Gdk.Window) -> int """
        return 0

    def get_monitor_geometry(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor_geometry(self, monitor_num:int) -> dest:Gdk.Rectangle """
        pass

    def get_monitor_height_mm(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor_height_mm(self, monitor_num:int) -> int """
        return 0

    def get_monitor_output(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor_output(self, monitor_num:int) -> int """
        return 0

    def get_monitor_plug_name(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor_plug_name(self, monitor_num:int) -> str or None """
        return ""

    def get_monitor_scale_factor(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor_scale_factor(self, monitor_num:int) -> int """
        return 0

    def get_monitor_width_mm(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor_width_mm(self, monitor_num:int) -> int """
        return 0

    def get_monitor_workarea(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor_workarea(self, monitor_num:int) -> dest:Gdk.Rectangle """
        pass

    def get_number(self): # real signature unknown; restored from __doc__
        """ get_number(self) -> int """
        return 0

    def get_number_of_desktops(self): # real signature unknown; restored from __doc__
        """ get_number_of_desktops(self) -> int """
        return 0

    def get_n_monitors(self): # real signature unknown; restored from __doc__
        """ get_n_monitors(self) -> int """
        return 0

    def get_primary_monitor(self): # real signature unknown; restored from __doc__
        """ get_primary_monitor(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> float """
        return 0.0

    def get_rgba_visual(self): # real signature unknown; restored from __doc__
        """ get_rgba_visual(self) -> Gdk.Visual or None """
        pass

    def get_root_window(self): # real signature unknown; restored from __doc__
        """ get_root_window(self) -> Gdk.Window """
        pass

    def get_screen_number(self): # real signature unknown; restored from __doc__
        """ get_screen_number(self) -> int """
        return 0

    def get_setting(self, name, value): # real signature unknown; restored from __doc__
        """ get_setting(self, name:str, value:GObject.Value) -> bool """
        return False

    def get_system_visual(self): # real signature unknown; restored from __doc__
        """ get_system_visual(self) -> Gdk.Visual """
        pass

    def get_toplevel_windows(self): # real signature unknown; restored from __doc__
        """ get_toplevel_windows(self) -> list """
        return []

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def get_width_mm(self): # real signature unknown; restored from __doc__
        """ get_width_mm(self) -> int """
        return 0

    def get_window_manager_name(self): # real signature unknown; restored from __doc__
        """ get_window_manager_name(self) -> str """
        return ""

    def get_window_stack(self): # real signature unknown; restored from __doc__
        """ get_window_stack(self) -> list or None """
        return []

    def get_xscreen(self): # real signature unknown; restored from __doc__
        """ get_xscreen(self) -> xlib.Screen """
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

    def height(self): # real signature unknown; restored from __doc__
        """ height() -> int """
        return 0

    def height_mm(self): # real signature unknown; restored from __doc__
        """ height_mm() -> int """
        return 0

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

    def is_composited(self): # real signature unknown; restored from __doc__
        """ is_composited(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_visuals(self): # real signature unknown; restored from __doc__
        """ list_visuals(self) -> list """
        return []

    def lookup_visual(self, xvisualid): # real signature unknown; restored from __doc__
        """ lookup_visual(self, xvisualid:int) -> GdkX11.X11Visual """
        pass

    def make_display_name(self): # real signature unknown; restored from __doc__
        """ make_display_name(self) -> str """
        return ""

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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_font_options(self, options=None): # real signature unknown; restored from __doc__
        """ set_font_options(self, options:cairo.FontOptions=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, dpi): # real signature unknown; restored from __doc__
        """ set_resolution(self, dpi:float) """
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

    def supports_net_wm_hint(self, property): # real signature unknown; restored from __doc__
        """ supports_net_wm_hint(self, property:Gdk.Atom) -> bool """
        return False

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

    def width(self): # real signature unknown; restored from __doc__
        """ width() -> int """
        return 0

    def width_mm(self): # real signature unknown; restored from __doc__
        """ width_mm() -> int """
        return 0

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f08a17c2520>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(X11Screen), '__module__': 'gi.repository.GdkX11', '__gtype__': <GType GdkX11Screen (94435716652768)>, '__doc__': None, '__gsignals__': {}, 'get_current_desktop': gi.FunctionInfo(get_current_desktop), 'get_monitor_output': gi.FunctionInfo(get_monitor_output), 'get_number_of_desktops': gi.FunctionInfo(get_number_of_desktops), 'get_screen_number': gi.FunctionInfo(get_screen_number), 'get_window_manager_name': gi.FunctionInfo(get_window_manager_name), 'get_xscreen': gi.FunctionInfo(get_xscreen), 'lookup_visual': gi.FunctionInfo(lookup_visual), 'supports_net_wm_hint': gi.FunctionInfo(supports_net_wm_hint)})"
    __gdoc__ = 'Object GdkX11Screen\n\nSignals from GdkX11Screen:\n  window-manager-changed ()\n\nSignals from GdkScreen:\n  size-changed ()\n  composited-changed ()\n  monitors-changed ()\n\nProperties from GdkScreen:\n  font-options -> gpointer: Font options\n    The default font options for the screen\n  resolution -> gdouble: Font resolution\n    The resolution for fonts on the screen\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GdkX11Screen (94435716652768)>'
    __info__ = ObjectInfo(X11Screen)


