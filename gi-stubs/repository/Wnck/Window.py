# encoding: utf-8
# module gi.repository.Wnck
# from /usr/lib64/girepository-1.0/Wnck-3.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class Window(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Window(**properties)
    """
    def activate(self, timestamp): # real signature unknown; restored from __doc__
        """ activate(self, timestamp:int) """
        pass

    def activate_transient(self, timestamp): # real signature unknown; restored from __doc__
        """ activate_transient(self, timestamp:int) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, timestamp): # real signature unknown; restored from __doc__
        """ close(self, timestamp:int) """
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

    def do_actions_changed(self, *args, **kwargs): # real signature unknown
        """ actions_changed(self, changed_mask:Wnck.WindowActions, new_actions:Wnck.WindowActions) """
        pass

    def do_class_changed(self, *args, **kwargs): # real signature unknown
        """ class_changed(self) """
        pass

    def do_geometry_changed(self, *args, **kwargs): # real signature unknown
        """ geometry_changed(self) """
        pass

    def do_icon_changed(self, *args, **kwargs): # real signature unknown
        """ icon_changed(self) """
        pass

    def do_name_changed(self, *args, **kwargs): # real signature unknown
        """ name_changed(self) """
        pass

    def do_role_changed(self, *args, **kwargs): # real signature unknown
        """ role_changed(self) """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, changed_mask:Wnck.WindowState, new_state:Wnck.WindowState) """
        pass

    def do_type_changed(self, *args, **kwargs): # real signature unknown
        """ type_changed(self) """
        pass

    def do_workspace_changed(self, *args, **kwargs): # real signature unknown
        """ workspace_changed(self) """
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

    def get(self, xwindow): # real signature unknown; restored from __doc__
        """ get(xwindow:int) -> Wnck.Window """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_actions(self): # real signature unknown; restored from __doc__
        """ get_actions(self) -> Wnck.WindowActions """
        pass

    def get_application(self): # real signature unknown; restored from __doc__
        """ get_application(self) -> Wnck.Application """
        pass

    def get_class_group(self): # real signature unknown; restored from __doc__
        """ get_class_group(self) -> Wnck.ClassGroup """
        pass

    def get_class_group_name(self): # real signature unknown; restored from __doc__
        """ get_class_group_name(self) -> str """
        return ""

    def get_class_instance_name(self): # real signature unknown; restored from __doc__
        """ get_class_instance_name(self) -> str """
        return ""

    def get_client_window_geometry(self): # real signature unknown; restored from __doc__
        """ get_client_window_geometry(self) -> xp:int, yp:int, widthp:int, heightp:int """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_geometry(self): # real signature unknown; restored from __doc__
        """ get_geometry(self) -> xp:int, yp:int, widthp:int, heightp:int """
        pass

    def get_group_leader(self): # real signature unknown; restored from __doc__
        """ get_group_leader(self) -> int """
        return 0

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> GdkPixbuf.Pixbuf """
        pass

    def get_icon_is_fallback(self): # real signature unknown; restored from __doc__
        """ get_icon_is_fallback(self) -> bool """
        return False

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_mini_icon(self): # real signature unknown; restored from __doc__
        """ get_mini_icon(self) -> GdkPixbuf.Pixbuf """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_pid(self): # real signature unknown; restored from __doc__
        """ get_pid(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> str """
        return ""

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Wnck.Screen """
        pass

    def get_session_id(self): # real signature unknown; restored from __doc__
        """ get_session_id(self) -> str """
        return ""

    def get_session_id_utf8(self): # real signature unknown; restored from __doc__
        """ get_session_id_utf8(self) -> str """
        return ""

    def get_sort_order(self): # real signature unknown; restored from __doc__
        """ get_sort_order(self) -> int """
        return 0

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Wnck.WindowState """
        pass

    def get_transient(self): # real signature unknown; restored from __doc__
        """ get_transient(self) -> Wnck.Window """
        pass

    def get_window_type(self): # real signature unknown; restored from __doc__
        """ get_window_type(self) -> Wnck.WindowType """
        pass

    def get_workspace(self): # real signature unknown; restored from __doc__
        """ get_workspace(self) -> Wnck.Workspace """
        pass

    def get_xid(self): # real signature unknown; restored from __doc__
        """ get_xid(self) -> int """
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

    def has_icon_name(self): # real signature unknown; restored from __doc__
        """ has_icon_name(self) -> bool """
        return False

    def has_name(self): # real signature unknown; restored from __doc__
        """ has_name(self) -> bool """
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

    def is_above(self): # real signature unknown; restored from __doc__
        """ is_above(self) -> bool """
        return False

    def is_active(self): # real signature unknown; restored from __doc__
        """ is_active(self) -> bool """
        return False

    def is_below(self): # real signature unknown; restored from __doc__
        """ is_below(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_fullscreen(self): # real signature unknown; restored from __doc__
        """ is_fullscreen(self) -> bool """
        return False

    def is_in_viewport(self, workspace): # real signature unknown; restored from __doc__
        """ is_in_viewport(self, workspace:Wnck.Workspace) -> bool """
        return False

    def is_maximized(self): # real signature unknown; restored from __doc__
        """ is_maximized(self) -> bool """
        return False

    def is_maximized_horizontally(self): # real signature unknown; restored from __doc__
        """ is_maximized_horizontally(self) -> bool """
        return False

    def is_maximized_vertically(self): # real signature unknown; restored from __doc__
        """ is_maximized_vertically(self) -> bool """
        return False

    def is_minimized(self): # real signature unknown; restored from __doc__
        """ is_minimized(self) -> bool """
        return False

    def is_most_recently_activated(self): # real signature unknown; restored from __doc__
        """ is_most_recently_activated(self) -> bool """
        return False

    def is_on_workspace(self, workspace): # real signature unknown; restored from __doc__
        """ is_on_workspace(self, workspace:Wnck.Workspace) -> bool """
        return False

    def is_pinned(self): # real signature unknown; restored from __doc__
        """ is_pinned(self) -> bool """
        return False

    def is_shaded(self): # real signature unknown; restored from __doc__
        """ is_shaded(self) -> bool """
        return False

    def is_skip_pager(self): # real signature unknown; restored from __doc__
        """ is_skip_pager(self) -> bool """
        return False

    def is_skip_tasklist(self): # real signature unknown; restored from __doc__
        """ is_skip_tasklist(self) -> bool """
        return False

    def is_sticky(self): # real signature unknown; restored from __doc__
        """ is_sticky(self) -> bool """
        return False

    def is_visible_on_workspace(self, workspace): # real signature unknown; restored from __doc__
        """ is_visible_on_workspace(self, workspace:Wnck.Workspace) -> bool """
        return False

    def keyboard_move(self): # real signature unknown; restored from __doc__
        """ keyboard_move(self) """
        pass

    def keyboard_size(self): # real signature unknown; restored from __doc__
        """ keyboard_size(self) """
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def make_above(self): # real signature unknown; restored from __doc__
        """ make_above(self) """
        pass

    def make_below(self): # real signature unknown; restored from __doc__
        """ make_below(self) """
        pass

    def maximize(self): # real signature unknown; restored from __doc__
        """ maximize(self) """
        pass

    def maximize_horizontally(self): # real signature unknown; restored from __doc__
        """ maximize_horizontally(self) """
        pass

    def maximize_vertically(self): # real signature unknown; restored from __doc__
        """ maximize_vertically(self) """
        pass

    def minimize(self): # real signature unknown; restored from __doc__
        """ minimize(self) """
        pass

    def move_to_workspace(self, space): # real signature unknown; restored from __doc__
        """ move_to_workspace(self, space:Wnck.Workspace) """
        pass

    def needs_attention(self): # real signature unknown; restored from __doc__
        """ needs_attention(self) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def or_transient_needs_attention(self): # real signature unknown; restored from __doc__
        """ or_transient_needs_attention(self) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def pin(self): # real signature unknown; restored from __doc__
        """ pin(self) """
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

    def set_fullscreen(self, fullscreen): # real signature unknown; restored from __doc__
        """ set_fullscreen(self, fullscreen:bool) """
        pass

    def set_geometry(self, gravity, geometry_mask, x, y, width, height): # real signature unknown; restored from __doc__
        """ set_geometry(self, gravity:Wnck.WindowGravity, geometry_mask:Wnck.WindowMoveResizeMask, x:int, y:int, width:int, height:int) """
        pass

    def set_icon_geometry(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ set_icon_geometry(self, x:int, y:int, width:int, height:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_skip_pager(self, skip): # real signature unknown; restored from __doc__
        """ set_skip_pager(self, skip:bool) """
        pass

    def set_skip_tasklist(self, skip): # real signature unknown; restored from __doc__
        """ set_skip_tasklist(self, skip:bool) """
        pass

    def set_sort_order(self, order): # real signature unknown; restored from __doc__
        """ set_sort_order(self, order:int) """
        pass

    def set_window_type(self, wintype): # real signature unknown; restored from __doc__
        """ set_window_type(self, wintype:Wnck.WindowType) """
        pass

    def shade(self): # real signature unknown; restored from __doc__
        """ shade(self) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stick(self): # real signature unknown; restored from __doc__
        """ stick(self) """
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

    def transient_is_most_recently_activated(self): # real signature unknown; restored from __doc__
        """ transient_is_most_recently_activated(self) -> bool """
        return False

    def unmake_above(self): # real signature unknown; restored from __doc__
        """ unmake_above(self) """
        pass

    def unmake_below(self): # real signature unknown; restored from __doc__
        """ unmake_below(self) """
        pass

    def unmaximize(self): # real signature unknown; restored from __doc__
        """ unmaximize(self) """
        pass

    def unmaximize_horizontally(self): # real signature unknown; restored from __doc__
        """ unmaximize_horizontally(self) """
        pass

    def unmaximize_vertically(self): # real signature unknown; restored from __doc__
        """ unmaximize_vertically(self) """
        pass

    def unminimize(self, timestamp): # real signature unknown; restored from __doc__
        """ unminimize(self, timestamp:int) """
        pass

    def unpin(self): # real signature unknown; restored from __doc__
        """ unpin(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unshade(self): # real signature unknown; restored from __doc__
        """ unshade(self) """
        pass

    def unstick(self): # real signature unknown; restored from __doc__
        """ unstick(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f75c30b94f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Window), '__module__': 'gi.repository.Wnck', '__gtype__': <GType WnckWindow (94401669352448)>, '__doc__': None, '__gsignals__': {}, 'get': gi.FunctionInfo(get), 'activate': gi.FunctionInfo(activate), 'activate_transient': gi.FunctionInfo(activate_transient), 'close': gi.FunctionInfo(close), 'get_actions': gi.FunctionInfo(get_actions), 'get_application': gi.FunctionInfo(get_application), 'get_class_group': gi.FunctionInfo(get_class_group), 'get_class_group_name': gi.FunctionInfo(get_class_group_name), 'get_class_instance_name': gi.FunctionInfo(get_class_instance_name), 'get_client_window_geometry': gi.FunctionInfo(get_client_window_geometry), 'get_geometry': gi.FunctionInfo(get_geometry), 'get_group_leader': gi.FunctionInfo(get_group_leader), 'get_icon': gi.FunctionInfo(get_icon), 'get_icon_is_fallback': gi.FunctionInfo(get_icon_is_fallback), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_mini_icon': gi.FunctionInfo(get_mini_icon), 'get_name': gi.FunctionInfo(get_name), 'get_pid': gi.FunctionInfo(get_pid), 'get_role': gi.FunctionInfo(get_role), 'get_screen': gi.FunctionInfo(get_screen), 'get_session_id': gi.FunctionInfo(get_session_id), 'get_session_id_utf8': gi.FunctionInfo(get_session_id_utf8), 'get_sort_order': gi.FunctionInfo(get_sort_order), 'get_state': gi.FunctionInfo(get_state), 'get_transient': gi.FunctionInfo(get_transient), 'get_window_type': gi.FunctionInfo(get_window_type), 'get_workspace': gi.FunctionInfo(get_workspace), 'get_xid': gi.FunctionInfo(get_xid), 'has_icon_name': gi.FunctionInfo(has_icon_name), 'has_name': gi.FunctionInfo(has_name), 'is_above': gi.FunctionInfo(is_above), 'is_active': gi.FunctionInfo(is_active), 'is_below': gi.FunctionInfo(is_below), 'is_fullscreen': gi.FunctionInfo(is_fullscreen), 'is_in_viewport': gi.FunctionInfo(is_in_viewport), 'is_maximized': gi.FunctionInfo(is_maximized), 'is_maximized_horizontally': gi.FunctionInfo(is_maximized_horizontally), 'is_maximized_vertically': gi.FunctionInfo(is_maximized_vertically), 'is_minimized': gi.FunctionInfo(is_minimized), 'is_most_recently_activated': gi.FunctionInfo(is_most_recently_activated), 'is_on_workspace': gi.FunctionInfo(is_on_workspace), 'is_pinned': gi.FunctionInfo(is_pinned), 'is_shaded': gi.FunctionInfo(is_shaded), 'is_skip_pager': gi.FunctionInfo(is_skip_pager), 'is_skip_tasklist': gi.FunctionInfo(is_skip_tasklist), 'is_sticky': gi.FunctionInfo(is_sticky), 'is_visible_on_workspace': gi.FunctionInfo(is_visible_on_workspace), 'keyboard_move': gi.FunctionInfo(keyboard_move), 'keyboard_size': gi.FunctionInfo(keyboard_size), 'make_above': gi.FunctionInfo(make_above), 'make_below': gi.FunctionInfo(make_below), 'maximize': gi.FunctionInfo(maximize), 'maximize_horizontally': gi.FunctionInfo(maximize_horizontally), 'maximize_vertically': gi.FunctionInfo(maximize_vertically), 'minimize': gi.FunctionInfo(minimize), 'move_to_workspace': gi.FunctionInfo(move_to_workspace), 'needs_attention': gi.FunctionInfo(needs_attention), 'or_transient_needs_attention': gi.FunctionInfo(or_transient_needs_attention), 'pin': gi.FunctionInfo(pin), 'set_fullscreen': gi.FunctionInfo(set_fullscreen), 'set_geometry': gi.FunctionInfo(set_geometry), 'set_icon_geometry': gi.FunctionInfo(set_icon_geometry), 'set_skip_pager': gi.FunctionInfo(set_skip_pager), 'set_skip_tasklist': gi.FunctionInfo(set_skip_tasklist), 'set_sort_order': gi.FunctionInfo(set_sort_order), 'set_window_type': gi.FunctionInfo(set_window_type), 'shade': gi.FunctionInfo(shade), 'stick': gi.FunctionInfo(stick), 'transient_is_most_recently_activated': gi.FunctionInfo(transient_is_most_recently_activated), 'unmake_above': gi.FunctionInfo(unmake_above), 'unmake_below': gi.FunctionInfo(unmake_below), 'unmaximize': gi.FunctionInfo(unmaximize), 'unmaximize_horizontally': gi.FunctionInfo(unmaximize_horizontally), 'unmaximize_vertically': gi.FunctionInfo(unmaximize_vertically), 'unminimize': gi.FunctionInfo(unminimize), 'unpin': gi.FunctionInfo(unpin), 'unshade': gi.FunctionInfo(unshade), 'unstick': gi.FunctionInfo(unstick), 'do_actions_changed': gi.VFuncInfo(actions_changed), 'do_class_changed': gi.VFuncInfo(class_changed), 'do_geometry_changed': gi.VFuncInfo(geometry_changed), 'do_icon_changed': gi.VFuncInfo(icon_changed), 'do_name_changed': gi.VFuncInfo(name_changed), 'do_role_changed': gi.VFuncInfo(role_changed), 'do_state_changed': gi.VFuncInfo(state_changed), 'do_type_changed': gi.VFuncInfo(type_changed), 'do_workspace_changed': gi.VFuncInfo(workspace_changed), 'parent_instance': <property object at 0x7f75c3230e00>, 'priv': <property object at 0x7f75c3233040>})"
    __gdoc__ = 'Object WnckWindow\n\nSignals from WnckWindow:\n  state-changed (WnckWindowState, WnckWindowState)\n  name-changed ()\n  icon-changed ()\n  workspace-changed ()\n  actions-changed (WnckWindowActions, WnckWindowActions)\n  geometry-changed ()\n  class-changed ()\n  role-changed ()\n  type-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WnckWindow (94401669352448)>'
    __info__ = ObjectInfo(Window)


