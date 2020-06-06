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


class Screen(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Screen(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def calc_workspace_layout(self, num_workspaces, space_index, layout): # real signature unknown; restored from __doc__
        """ calc_workspace_layout(self, num_workspaces:int, space_index:int, layout:Wnck.WorkspaceLayout) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_workspace_count(self, count): # real signature unknown; restored from __doc__
        """ change_workspace_count(self, count:int) """
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

    def do_active_window_changed(self, *args, **kwargs): # real signature unknown
        """ active_window_changed(self, previous_window:Wnck.Window) """
        pass

    def do_active_workspace_changed(self, *args, **kwargs): # real signature unknown
        """ active_workspace_changed(self, previous_workspace:Wnck.Workspace) """
        pass

    def do_application_closed(self, *args, **kwargs): # real signature unknown
        """ application_closed(self, app:Wnck.Application) """
        pass

    def do_application_opened(self, *args, **kwargs): # real signature unknown
        """ application_opened(self, app:Wnck.Application) """
        pass

    def do_background_changed(self, *args, **kwargs): # real signature unknown
        """ background_changed(self) """
        pass

    def do_class_group_closed(self, *args, **kwargs): # real signature unknown
        """ class_group_closed(self, class_group:Wnck.ClassGroup) """
        pass

    def do_class_group_opened(self, *args, **kwargs): # real signature unknown
        """ class_group_opened(self, class_group:Wnck.ClassGroup) """
        pass

    def do_showing_desktop_changed(self, *args, **kwargs): # real signature unknown
        """ showing_desktop_changed(self) """
        pass

    def do_viewports_changed(self, *args, **kwargs): # real signature unknown
        """ viewports_changed(self) """
        pass

    def do_window_closed(self, *args, **kwargs): # real signature unknown
        """ window_closed(self, window:Wnck.Window) """
        pass

    def do_window_manager_changed(self, *args, **kwargs): # real signature unknown
        """ window_manager_changed(self) """
        pass

    def do_window_opened(self, *args, **kwargs): # real signature unknown
        """ window_opened(self, window:Wnck.Window) """
        pass

    def do_window_stacking_changed(self, *args, **kwargs): # real signature unknown
        """ window_stacking_changed(self) """
        pass

    def do_workspace_created(self, *args, **kwargs): # real signature unknown
        """ workspace_created(self, space:Wnck.Workspace) """
        pass

    def do_workspace_destroyed(self, *args, **kwargs): # real signature unknown
        """ workspace_destroyed(self, space:Wnck.Workspace) """
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

    def force_update(self): # real signature unknown; restored from __doc__
        """ force_update(self) """
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

    def free_workspace_layout(self, layout): # real signature unknown; restored from __doc__
        """ free_workspace_layout(layout:Wnck.WorkspaceLayout) """
        pass

    def get(self, index): # real signature unknown; restored from __doc__
        """ get(index:int) -> Wnck.Screen """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_active_window(self): # real signature unknown; restored from __doc__
        """ get_active_window(self) -> Wnck.Window """
        pass

    def get_active_workspace(self): # real signature unknown; restored from __doc__
        """ get_active_workspace(self) -> Wnck.Workspace """
        pass

    def get_background_pixmap(self): # real signature unknown; restored from __doc__
        """ get_background_pixmap(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Wnck.Screen or None """
        pass

    def get_for_root(self, root_window_id): # real signature unknown; restored from __doc__
        """ get_for_root(root_window_id:int) -> Wnck.Screen """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_number(self): # real signature unknown; restored from __doc__
        """ get_number(self) -> int """
        return 0

    def get_previously_active_window(self): # real signature unknown; restored from __doc__
        """ get_previously_active_window(self) -> Wnck.Window """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_showing_desktop(self): # real signature unknown; restored from __doc__
        """ get_showing_desktop(self) -> bool """
        return False

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def get_windows(self): # real signature unknown; restored from __doc__
        """ get_windows(self) -> list """
        return []

    def get_windows_stacked(self): # real signature unknown; restored from __doc__
        """ get_windows_stacked(self) -> list """
        return []

    def get_window_manager_name(self): # real signature unknown; restored from __doc__
        """ get_window_manager_name(self) -> str """
        return ""

    def get_workspace(self, workspace): # real signature unknown; restored from __doc__
        """ get_workspace(self, workspace:int) -> Wnck.Workspace """
        pass

    def get_workspaces(self): # real signature unknown; restored from __doc__
        """ get_workspaces(self) -> list """
        return []

    def get_workspace_count(self): # real signature unknown; restored from __doc__
        """ get_workspace_count(self) -> int """
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

    def move_viewport(self, x, y): # real signature unknown; restored from __doc__
        """ move_viewport(self, x:int, y:int) """
        pass

    def net_wm_supports(self, atom): # real signature unknown; restored from __doc__
        """ net_wm_supports(self, atom:str) -> bool """
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

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def release_workspace_layout(self, current_token): # real signature unknown; restored from __doc__
        """ release_workspace_layout(self, current_token:int) """
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

    def toggle_showing_desktop(self, show): # real signature unknown; restored from __doc__
        """ toggle_showing_desktop(self, show:bool) """
        pass

    def try_set_workspace_layout(self, current_token, rows, columns): # real signature unknown; restored from __doc__
        """ try_set_workspace_layout(self, current_token:int, rows:int, columns:int) -> int """
        return 0

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f75c3278490>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Screen), '__module__': 'gi.repository.Wnck', '__gtype__': <GType WnckScreen (94401668724928)>, '__doc__': None, '__gsignals__': {}, 'free_workspace_layout': gi.FunctionInfo(free_workspace_layout), 'get': gi.FunctionInfo(get), 'get_default': gi.FunctionInfo(get_default), 'get_for_root': gi.FunctionInfo(get_for_root), 'calc_workspace_layout': gi.FunctionInfo(calc_workspace_layout), 'change_workspace_count': gi.FunctionInfo(change_workspace_count), 'force_update': gi.FunctionInfo(force_update), 'get_active_window': gi.FunctionInfo(get_active_window), 'get_active_workspace': gi.FunctionInfo(get_active_workspace), 'get_background_pixmap': gi.FunctionInfo(get_background_pixmap), 'get_height': gi.FunctionInfo(get_height), 'get_number': gi.FunctionInfo(get_number), 'get_previously_active_window': gi.FunctionInfo(get_previously_active_window), 'get_showing_desktop': gi.FunctionInfo(get_showing_desktop), 'get_width': gi.FunctionInfo(get_width), 'get_window_manager_name': gi.FunctionInfo(get_window_manager_name), 'get_windows': gi.FunctionInfo(get_windows), 'get_windows_stacked': gi.FunctionInfo(get_windows_stacked), 'get_workspace': gi.FunctionInfo(get_workspace), 'get_workspace_count': gi.FunctionInfo(get_workspace_count), 'get_workspaces': gi.FunctionInfo(get_workspaces), 'move_viewport': gi.FunctionInfo(move_viewport), 'net_wm_supports': gi.FunctionInfo(net_wm_supports), 'release_workspace_layout': gi.FunctionInfo(release_workspace_layout), 'toggle_showing_desktop': gi.FunctionInfo(toggle_showing_desktop), 'try_set_workspace_layout': gi.FunctionInfo(try_set_workspace_layout), 'do_active_window_changed': gi.VFuncInfo(active_window_changed), 'do_active_workspace_changed': gi.VFuncInfo(active_workspace_changed), 'do_application_closed': gi.VFuncInfo(application_closed), 'do_application_opened': gi.VFuncInfo(application_opened), 'do_background_changed': gi.VFuncInfo(background_changed), 'do_class_group_closed': gi.VFuncInfo(class_group_closed), 'do_class_group_opened': gi.VFuncInfo(class_group_opened), 'do_showing_desktop_changed': gi.VFuncInfo(showing_desktop_changed), 'do_viewports_changed': gi.VFuncInfo(viewports_changed), 'do_window_closed': gi.VFuncInfo(window_closed), 'do_window_manager_changed': gi.VFuncInfo(window_manager_changed), 'do_window_opened': gi.VFuncInfo(window_opened), 'do_window_stacking_changed': gi.VFuncInfo(window_stacking_changed), 'do_workspace_created': gi.VFuncInfo(workspace_created), 'do_workspace_destroyed': gi.VFuncInfo(workspace_destroyed), 'parent_instance': <property object at 0x7f75c322b180>, 'priv': <property object at 0x7f75c322b360>})"
    __gdoc__ = 'Object WnckScreen\n\nSignals from WnckScreen:\n  window-manager-changed ()\n  active-window-changed (WnckWindow)\n  active-workspace-changed (WnckWorkspace)\n  window-stacking-changed ()\n  window-opened (WnckWindow)\n  window-closed (WnckWindow)\n  workspace-created (WnckWorkspace)\n  workspace-destroyed (WnckWorkspace)\n  application-opened (WnckApplication)\n  application-closed (WnckApplication)\n  class-group-opened (WnckClassGroup)\n  class-group-closed (WnckClassGroup)\n  background-changed ()\n  showing-desktop-changed ()\n  viewports-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WnckScreen (94401668724928)>'
    __info__ = ObjectInfo(Screen)


