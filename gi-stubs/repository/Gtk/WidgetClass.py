# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class WidgetClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        WidgetClass()
    """
    def bind_template_callback_full(self, callback_name, callback_symbol): # real signature unknown; restored from __doc__
        """ bind_template_callback_full(self, callback_name:str, callback_symbol:GObject.Callback) """
        pass

    def bind_template_child_full(self, name, internal_child, struct_offset): # real signature unknown; restored from __doc__
        """ bind_template_child_full(self, name:str, internal_child:bool, struct_offset:int) """
        pass

    def find_style_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_style_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def get_css_name(self): # real signature unknown; restored from __doc__
        """ get_css_name(self) -> str """
        return ""

    def install_style_property(self, pspec): # real signature unknown; restored from __doc__
        """ install_style_property(self, pspec:GObject.ParamSpec) """
        pass

    def list_style_properties(self): # real signature unknown; restored from __doc__
        """ list_style_properties(self) -> list, n_properties:int """
        return []

    def set_accessible_role(self, role): # real signature unknown; restored from __doc__
        """ set_accessible_role(self, role:Atk.Role) """
        pass

    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
        pass

    def set_connect_func(self, connect_func, connect_data=None): # real signature unknown; restored from __doc__
        """ set_connect_func(self, connect_func:Gtk.BuilderConnectFunc, connect_data=None) """
        pass

    def set_css_name(self, name): # real signature unknown; restored from __doc__
        """ set_css_name(self, name:str) """
        pass

    def set_template(self, template_bytes): # real signature unknown; restored from __doc__
        """ set_template(self, template_bytes:GLib.Bytes) """
        pass

    def set_template_from_resource(self, resource_name): # real signature unknown; restored from __doc__
        """ set_template_from_resource(self, resource_name:str) """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    activate_signal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    adjust_baseline_allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    adjust_baseline_request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    adjust_size_allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    adjust_size_request = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button_press_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button_release_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_activate_accel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    composited_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compute_expand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    configure_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    damage_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    direction_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dispatch_child_properties_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_begin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_data_delete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_data_get = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_data_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_drop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_failed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_leave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_motion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enter_notify_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_in_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_out_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_accessible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height_and_baseline_for_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height_for_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width_for_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_request_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_broken_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hierarchy_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keynav_failed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_press_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_release_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leave_notify_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mnemonic_activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    motion_notify_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    popup_menu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property_notify_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proximity_in_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proximity_out_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_tooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue_draw_region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    realize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    screen_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_clear_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_get = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_notify_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_request_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_help = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size_allocate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_flags_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    style_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    style_updated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touch_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmap_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unrealize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visibility_notify_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_state_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WidgetClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'WidgetClass' objects>, '__weakref__': <attribute '__weakref__' of 'WidgetClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fe830f443b0>, 'activate_signal': <property object at 0x7fe830f444a0>, 'dispatch_child_properties_changed': <property object at 0x7fe830f44590>, 'destroy': <property object at 0x7fe830f44680>, 'show': <property object at 0x7fe830f44770>, 'show_all': <property object at 0x7fe830f44860>, 'hide': <property object at 0x7fe830f44950>, 'map': <property object at 0x7fe830f44a40>, 'unmap': <property object at 0x7fe830f44b30>, 'realize': <property object at 0x7fe830f44c20>, 'unrealize': <property object at 0x7fe830f44d10>, 'size_allocate': <property object at 0x7fe830f44e00>, 'state_changed': <property object at 0x7fe830f44ef0>, 'state_flags_changed': <property object at 0x7fe830f48090>, 'parent_set': <property object at 0x7fe830f48180>, 'hierarchy_changed': <property object at 0x7fe830f482c0>, 'style_set': <property object at 0x7fe830f483b0>, 'direction_changed': <property object at 0x7fe830f484f0>, 'grab_notify': <property object at 0x7fe830f485e0>, 'child_notify': <property object at 0x7fe830f486d0>, 'draw': <property object at 0x7fe830f487c0>, 'get_request_mode': <property object at 0x7fe830f48900>, 'get_preferred_height': <property object at 0x7fe830f489f0>, 'get_preferred_width_for_height': <property object at 0x7fe830f48ae0>, 'get_preferred_width': <property object at 0x7fe830f48bd0>, 'get_preferred_height_for_width': <property object at 0x7fe830f48cc0>, 'mnemonic_activate': <property object at 0x7fe830f48db0>, 'grab_focus': <property object at 0x7fe830f48e50>, 'focus': <property object at 0x7fe830f48f40>, 'move_focus': <property object at 0x7fe830f49090>, 'keynav_failed': <property object at 0x7fe830f49180>, 'event': <property object at 0x7fe830f49270>, 'button_press_event': <property object at 0x7fe830f493b0>, 'button_release_event': <property object at 0x7fe830f494a0>, 'scroll_event': <property object at 0x7fe830f49540>, 'motion_notify_event': <property object at 0x7fe830f49680>, 'delete_event': <property object at 0x7fe830f49770>, 'destroy_event': <property object at 0x7fe830f49860>, 'key_press_event': <property object at 0x7fe830f49950>, 'key_release_event': <property object at 0x7fe830f49a90>, 'enter_notify_event': <property object at 0x7fe830f49bd0>, 'leave_notify_event': <property object at 0x7fe830f49d10>, 'configure_event': <property object at 0x7fe830f49e00>, 'focus_in_event': <property object at 0x7fe830f49ef0>, 'focus_out_event': <property object at 0x7fe830f4a040>, 'map_event': <property object at 0x7fe830f4a130>, 'unmap_event': <property object at 0x7fe830f4a220>, 'property_notify_event': <property object at 0x7fe830f4a360>, 'selection_clear_event': <property object at 0x7fe830f4a4a0>, 'selection_request_event': <property object at 0x7fe830f4a5e0>, 'selection_notify_event': <property object at 0x7fe830f4a720>, 'proximity_in_event': <property object at 0x7fe830f4a860>, 'proximity_out_event': <property object at 0x7fe830f4a9a0>, 'visibility_notify_event': <property object at 0x7fe830f4aae0>, 'window_state_event': <property object at 0x7fe830f4ac20>, 'damage_event': <property object at 0x7fe830f4ad10>, 'grab_broken_event': <property object at 0x7fe830f4ae50>, 'selection_get': <property object at 0x7fe830f4af40>, 'selection_received': <property object at 0x7fe830f4b0e0>, 'drag_begin': <property object at 0x7fe830f4b1d0>, 'drag_end': <property object at 0x7fe830f4b2c0>, 'drag_data_get': <property object at 0x7fe830f4b3b0>, 'drag_data_delete': <property object at 0x7fe830f4b4f0>, 'drag_leave': <property object at 0x7fe830f4b590>, 'drag_motion': <property object at 0x7fe830f4b680>, 'drag_drop': <property object at 0x7fe830f4b770>, 'drag_data_received': <property object at 0x7fe830f4b8b0>, 'drag_failed': <property object at 0x7fe830f4b950>, 'popup_menu': <property object at 0x7fe830f4ba40>, 'show_help': <property object at 0x7fe830f4bb30>, 'get_accessible': <property object at 0x7fe830f4bc20>, 'screen_changed': <property object at 0x7fe830f4bd10>, 'can_activate_accel': <property object at 0x7fe830f4be50>, 'composited_changed': <property object at 0x7fe830f4bf40>, 'query_tooltip': <property object at 0x7fe830f4c090>, 'compute_expand': <property object at 0x7fe830f4c180>, 'adjust_size_request': <property object at 0x7fe830f4c2c0>, 'adjust_size_allocation': <property object at 0x7fe830f4c400>, 'style_updated': <property object at 0x7fe830f4c4f0>, 'touch_event': <property object at 0x7fe830f4c5e0>, 'get_preferred_height_and_baseline_for_width': <property object at 0x7fe830f4c6d0>, 'adjust_baseline_request': <property object at 0x7fe830f4c810>, 'adjust_baseline_allocation': <property object at 0x7fe830f4c950>, 'queue_draw_region': <property object at 0x7fe830f4ca90>, 'priv': <property object at 0x7fe830f4cb30>, '_gtk_reserved6': <property object at 0x7fe830f4cc20>, '_gtk_reserved7': <property object at 0x7fe830f4cd10>, 'bind_template_callback_full': gi.FunctionInfo(bind_template_callback_full), 'bind_template_child_full': gi.FunctionInfo(bind_template_child_full), 'find_style_property': gi.FunctionInfo(find_style_property), 'get_css_name': gi.FunctionInfo(get_css_name), 'install_style_property': gi.FunctionInfo(install_style_property), 'list_style_properties': gi.FunctionInfo(list_style_properties), 'set_accessible_role': gi.FunctionInfo(set_accessible_role), 'set_accessible_type': gi.FunctionInfo(set_accessible_type), 'set_connect_func': gi.FunctionInfo(set_connect_func), 'set_css_name': gi.FunctionInfo(set_css_name), 'set_template': gi.FunctionInfo(set_template), 'set_template_from_resource': gi.FunctionInfo(set_template_from_resource)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(WidgetClass)


