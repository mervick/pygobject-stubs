# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-2.0.typelib
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WidgetClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'WidgetClass' objects>, '__weakref__': <attribute '__weakref__' of 'WidgetClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fc63a659c70>, 'activate_signal': <property object at 0x7fc63a659d60>, 'dispatch_child_properties_changed': <property object at 0x7fc63a659e50>, 'destroy': <property object at 0x7fc63a659f40>, 'show': <property object at 0x7fc63a65e090>, 'show_all': <property object at 0x7fc63a65e180>, 'hide': <property object at 0x7fc63a65e270>, 'map': <property object at 0x7fc63a65e360>, 'unmap': <property object at 0x7fc63a65e450>, 'realize': <property object at 0x7fc63a65e540>, 'unrealize': <property object at 0x7fc63a65e630>, 'size_allocate': <property object at 0x7fc63a65e720>, 'state_changed': <property object at 0x7fc63a65e810>, 'state_flags_changed': <property object at 0x7fc63a65e950>, 'parent_set': <property object at 0x7fc63a65ea40>, 'hierarchy_changed': <property object at 0x7fc63a65eb80>, 'style_set': <property object at 0x7fc63a65ec70>, 'direction_changed': <property object at 0x7fc63a65edb0>, 'grab_notify': <property object at 0x7fc63a65eea0>, 'child_notify': <property object at 0x7fc63a65ef90>, 'draw': <property object at 0x7fc63a65f0e0>, 'get_request_mode': <property object at 0x7fc63a65f220>, 'get_preferred_height': <property object at 0x7fc63a65f310>, 'get_preferred_width_for_height': <property object at 0x7fc63a65f400>, 'get_preferred_width': <property object at 0x7fc63a65f4f0>, 'get_preferred_height_for_width': <property object at 0x7fc63a65f5e0>, 'mnemonic_activate': <property object at 0x7fc63a65f6d0>, 'grab_focus': <property object at 0x7fc63a65f770>, 'focus': <property object at 0x7fc63a65f860>, 'move_focus': <property object at 0x7fc63a65f950>, 'keynav_failed': <property object at 0x7fc63a65fa40>, 'event': <property object at 0x7fc63a65fb30>, 'button_press_event': <property object at 0x7fc63a65fc70>, 'button_release_event': <property object at 0x7fc63a65fd60>, 'scroll_event': <property object at 0x7fc63a65fe00>, 'motion_notify_event': <property object at 0x7fc63a65ff40>, 'delete_event': <property object at 0x7fc63a660090>, 'destroy_event': <property object at 0x7fc63a660180>, 'key_press_event': <property object at 0x7fc63a660270>, 'key_release_event': <property object at 0x7fc63a6603b0>, 'enter_notify_event': <property object at 0x7fc63a6604f0>, 'leave_notify_event': <property object at 0x7fc63a660630>, 'configure_event': <property object at 0x7fc63a660720>, 'focus_in_event': <property object at 0x7fc63a660810>, 'focus_out_event': <property object at 0x7fc63a660900>, 'map_event': <property object at 0x7fc63a6609f0>, 'unmap_event': <property object at 0x7fc63a660ae0>, 'property_notify_event': <property object at 0x7fc63a660c20>, 'selection_clear_event': <property object at 0x7fc63a660d60>, 'selection_request_event': <property object at 0x7fc63a660ea0>, 'selection_notify_event': <property object at 0x7fc63a661040>, 'proximity_in_event': <property object at 0x7fc63a661180>, 'proximity_out_event': <property object at 0x7fc63a6612c0>, 'visibility_notify_event': <property object at 0x7fc63a661400>, 'window_state_event': <property object at 0x7fc63a661540>, 'damage_event': <property object at 0x7fc63a661630>, 'grab_broken_event': <property object at 0x7fc63a661770>, 'selection_get': <property object at 0x7fc63a661860>, 'selection_received': <property object at 0x7fc63a6619a0>, 'drag_begin': <property object at 0x7fc63a661a90>, 'drag_end': <property object at 0x7fc63a661b80>, 'drag_data_get': <property object at 0x7fc63a661c70>, 'drag_data_delete': <property object at 0x7fc63a661db0>, 'drag_leave': <property object at 0x7fc63a661e50>, 'drag_motion': <property object at 0x7fc63a661f40>, 'drag_drop': <property object at 0x7fc63a662090>, 'drag_data_received': <property object at 0x7fc63a6621d0>, 'drag_failed': <property object at 0x7fc63a662270>, 'popup_menu': <property object at 0x7fc63a662360>, 'show_help': <property object at 0x7fc63a662450>, 'get_accessible': <property object at 0x7fc63a662540>, 'screen_changed': <property object at 0x7fc63a662630>, 'can_activate_accel': <property object at 0x7fc63a662770>, 'composited_changed': <property object at 0x7fc63a662860>, 'query_tooltip': <property object at 0x7fc63a662950>, 'compute_expand': <property object at 0x7fc63a662a40>, 'adjust_size_request': <property object at 0x7fc63a662b80>, 'adjust_size_allocation': <property object at 0x7fc63a662cc0>, 'style_updated': <property object at 0x7fc63a662db0>, 'touch_event': <property object at 0x7fc63a662ea0>, 'get_preferred_height_and_baseline_for_width': <property object at 0x7fc63a662f90>, 'adjust_baseline_request': <property object at 0x7fc63a663130>, 'adjust_baseline_allocation': <property object at 0x7fc63a663270>, 'queue_draw_region': <property object at 0x7fc63a6633b0>, 'priv': <property object at 0x7fc63a663450>, '_gtk_reserved6': <property object at 0x7fc63a663540>, '_gtk_reserved7': <property object at 0x7fc63a663630>, 'bind_template_callback_full': gi.FunctionInfo(bind_template_callback_full), 'bind_template_child_full': gi.FunctionInfo(bind_template_child_full), 'find_style_property': gi.FunctionInfo(find_style_property), 'get_css_name': gi.FunctionInfo(get_css_name), 'install_style_property': gi.FunctionInfo(install_style_property), 'list_style_properties': gi.FunctionInfo(list_style_properties), 'set_accessible_role': gi.FunctionInfo(set_accessible_role), 'set_accessible_type': gi.FunctionInfo(set_accessible_type), 'set_connect_func': gi.FunctionInfo(set_connect_func), 'set_css_name': gi.FunctionInfo(set_css_name), 'set_template': gi.FunctionInfo(set_template), 'set_template_from_resource': gi.FunctionInfo(set_template_from_resource)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(WidgetClass)


