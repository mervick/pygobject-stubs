# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Event(__gi.Boxed):
    # no doc
    def add_filter(self, stage=None, func, user_data=None): # real signature unknown; restored from __doc__
        """ add_filter(stage:Clutter.Stage=None, func:Clutter.EventFilterFunc, user_data=None) -> int """
        return 0

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Clutter.Event """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get() -> Clutter.Event """
        pass

    def get_angle(self, target): # real signature unknown; restored from __doc__
        """ get_angle(self, target:Clutter.Event) -> float """
        return 0.0

    def get_axes(self): # real signature unknown; restored from __doc__
        """ get_axes(self) -> float, n_axes:int """
        return 0.0

    def get_button(self): # real signature unknown; restored from __doc__
        """ get_button(self) -> int """
        return 0

    def get_click_count(self): # real signature unknown; restored from __doc__
        """ get_click_count(self) -> int """
        return 0

    def get_coords(self): # real signature unknown; restored from __doc__
        """ get_coords(self) -> x:float, y:float """
        return x

    def get_device(self): # real signature unknown; restored from __doc__
        """ get_device(self) -> Clutter.InputDevice """
        pass

    def get_device_id(self): # real signature unknown; restored from __doc__
        """ get_device_id(self) -> int """
        return 0

    def get_device_type(self): # real signature unknown; restored from __doc__
        """ get_device_type(self) -> Clutter.InputDeviceType """
        pass

    def get_distance(self, target): # real signature unknown; restored from __doc__
        """ get_distance(self, target:Clutter.Event) -> float """
        return 0.0

    def get_event_sequence(self): # real signature unknown; restored from __doc__
        """ get_event_sequence(self) -> Clutter.EventSequence """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Clutter.EventFlags """
        pass

    def get_gesture_motion_delta(self): # real signature unknown; restored from __doc__
        """ get_gesture_motion_delta(self) -> dx:float, dy:float """
        pass

    def get_gesture_phase(self): # real signature unknown; restored from __doc__
        """ get_gesture_phase(self) -> Clutter.TouchpadGesturePhase """
        pass

    def get_gesture_pinch_angle_delta(self): # real signature unknown; restored from __doc__
        """ get_gesture_pinch_angle_delta(self) -> float """
        return 0.0

    def get_gesture_pinch_scale(self): # real signature unknown; restored from __doc__
        """ get_gesture_pinch_scale(self) -> float """
        return 0.0

    def get_gesture_swipe_finger_count(self): # real signature unknown; restored from __doc__
        """ get_gesture_swipe_finger_count(self) -> int """
        return 0

    def get_key_code(self): # real signature unknown; restored from __doc__
        """ get_key_code(self) -> int """
        return 0

    def get_key_symbol(self): # real signature unknown; restored from __doc__
        """ get_key_symbol(self) -> int """
        return 0

    def get_key_unicode(self): # real signature unknown; restored from __doc__
        """ get_key_unicode(self) -> str """
        return ""

    def get_position(self, position): # real signature unknown; restored from __doc__
        """ get_position(self, position:Clutter.Point) """
        pass

    def get_related(self): # real signature unknown; restored from __doc__
        """ get_related(self) -> Clutter.Actor """
        pass

    def get_scroll_delta(self): # real signature unknown; restored from __doc__
        """ get_scroll_delta(self) -> dx:float, dy:float """
        pass

    def get_scroll_direction(self): # real signature unknown; restored from __doc__
        """ get_scroll_direction(self) -> Clutter.ScrollDirection """
        pass

    def get_scroll_finish_flags(self): # real signature unknown; restored from __doc__
        """ get_scroll_finish_flags(self) -> Clutter.ScrollFinishFlags """
        pass

    def get_scroll_source(self): # real signature unknown; restored from __doc__
        """ get_scroll_source(self) -> Clutter.ScrollSource """
        pass

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> Clutter.Actor """
        pass

    def get_source_device(self): # real signature unknown; restored from __doc__
        """ get_source_device(self) -> Clutter.InputDevice """
        pass

    def get_stage(self): # real signature unknown; restored from __doc__
        """ get_stage(self) -> Clutter.Stage """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Clutter.ModifierType """
        pass

    def get_state_full(self): # real signature unknown; restored from __doc__
        """ get_state_full(self) -> button_state:Clutter.ModifierType, base_state:Clutter.ModifierType, latched_state:Clutter.ModifierType, locked_state:Clutter.ModifierType, effective_state:Clutter.ModifierType """
        pass

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def has_control_modifier(self): # real signature unknown; restored from __doc__
        """ has_control_modifier(self) -> bool """
        return False

    def has_shift_modifier(self): # real signature unknown; restored from __doc__
        """ has_shift_modifier(self) -> bool """
        return False

    def is_pointer_emulated(self): # real signature unknown; restored from __doc__
        """ is_pointer_emulated(self) -> bool """
        return False

    def new(self, type): # real signature unknown; restored from __doc__
        """ new(type:Clutter.EventType) -> Clutter.Event """
        pass

    def peek(self): # real signature unknown; restored from __doc__
        """ peek() -> Clutter.Event """
        pass

    def put(self): # real signature unknown; restored from __doc__
        """ put(self) """
        pass

    def remove_filter(self, id): # real signature unknown; restored from __doc__
        """ remove_filter(id:int) """
        pass

    def set_button(self, button): # real signature unknown; restored from __doc__
        """ set_button(self, button:int) """
        pass

    def set_coords(self, x, y): # real signature unknown; restored from __doc__
        """ set_coords(self, x:float, y:float) """
        pass

    def set_device(self, device=None): # real signature unknown; restored from __doc__
        """ set_device(self, device:Clutter.InputDevice=None) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Clutter.EventFlags) """
        pass

    def set_key_code(self, key_code): # real signature unknown; restored from __doc__
        """ set_key_code(self, key_code:int) """
        pass

    def set_key_symbol(self, key_sym): # real signature unknown; restored from __doc__
        """ set_key_symbol(self, key_sym:int) """
        pass

    def set_key_unicode(self, key_unicode): # real signature unknown; restored from __doc__
        """ set_key_unicode(self, key_unicode:str) """
        pass

    def set_related(self, actor=None): # real signature unknown; restored from __doc__
        """ set_related(self, actor:Clutter.Actor=None) """
        pass

    def set_scroll_delta(self, dx, dy): # real signature unknown; restored from __doc__
        """ set_scroll_delta(self, dx:float, dy:float) """
        pass

    def set_scroll_direction(self, direction): # real signature unknown; restored from __doc__
        """ set_scroll_direction(self, direction:Clutter.ScrollDirection) """
        pass

    def set_source(self, actor=None): # real signature unknown; restored from __doc__
        """ set_source(self, actor:Clutter.Actor=None) """
        pass

    def set_source_device(self, device=None): # real signature unknown; restored from __doc__
        """ set_source_device(self, device:Clutter.InputDevice=None) """
        pass

    def set_stage(self, stage=None): # real signature unknown; restored from __doc__
        """ set_stage(self, stage:Clutter.Stage=None) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Clutter.ModifierType) """
        pass

    def set_time(self, time_): # real signature unknown; restored from __doc__
        """ set_time(self, time_:int) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> Clutter.EventType """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    any = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    crossing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    motion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stage_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touchpad_pinch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touchpad_swipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': gi.UnionInfo(Event), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterEvent (94911696131472)>, '__dict__': <attribute '__dict__' of 'Event' objects>, '__weakref__': <attribute '__weakref__' of 'Event' objects>, '__doc__': None, 'type': gi.FunctionInfo(type), 'any': <property object at 0x7f5413cac8b0>, 'button': <property object at 0x7f5413cac9a0>, 'key': <property object at 0x7f5413caca90>, 'motion': <property object at 0x7f5413cacb80>, 'scroll': <property object at 0x7f5413cacc70>, 'stage_state': <property object at 0x7f5413cacd60>, 'crossing': <property object at 0x7f5413cace50>, 'touch': <property object at 0x7f5413cacf40>, 'touchpad_pinch': <property object at 0x7f5413caf090>, 'touchpad_swipe': <property object at 0x7f5413caf180>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_angle': gi.FunctionInfo(get_angle), 'get_axes': gi.FunctionInfo(get_axes), 'get_button': gi.FunctionInfo(get_button), 'get_click_count': gi.FunctionInfo(get_click_count), 'get_coords': gi.FunctionInfo(get_coords), 'get_device': gi.FunctionInfo(get_device), 'get_device_id': gi.FunctionInfo(get_device_id), 'get_device_type': gi.FunctionInfo(get_device_type), 'get_distance': gi.FunctionInfo(get_distance), 'get_event_sequence': gi.FunctionInfo(get_event_sequence), 'get_flags': gi.FunctionInfo(get_flags), 'get_gesture_motion_delta': gi.FunctionInfo(get_gesture_motion_delta), 'get_gesture_phase': gi.FunctionInfo(get_gesture_phase), 'get_gesture_pinch_angle_delta': gi.FunctionInfo(get_gesture_pinch_angle_delta), 'get_gesture_pinch_scale': gi.FunctionInfo(get_gesture_pinch_scale), 'get_gesture_swipe_finger_count': gi.FunctionInfo(get_gesture_swipe_finger_count), 'get_key_code': gi.FunctionInfo(get_key_code), 'get_key_symbol': gi.FunctionInfo(get_key_symbol), 'get_key_unicode': gi.FunctionInfo(get_key_unicode), 'get_position': gi.FunctionInfo(get_position), 'get_related': gi.FunctionInfo(get_related), 'get_scroll_delta': gi.FunctionInfo(get_scroll_delta), 'get_scroll_direction': gi.FunctionInfo(get_scroll_direction), 'get_scroll_finish_flags': gi.FunctionInfo(get_scroll_finish_flags), 'get_scroll_source': gi.FunctionInfo(get_scroll_source), 'get_source': gi.FunctionInfo(get_source), 'get_source_device': gi.FunctionInfo(get_source_device), 'get_stage': gi.FunctionInfo(get_stage), 'get_state': gi.FunctionInfo(get_state), 'get_state_full': gi.FunctionInfo(get_state_full), 'get_time': gi.FunctionInfo(get_time), 'has_control_modifier': gi.FunctionInfo(has_control_modifier), 'has_shift_modifier': gi.FunctionInfo(has_shift_modifier), 'is_pointer_emulated': gi.FunctionInfo(is_pointer_emulated), 'put': gi.FunctionInfo(put), 'set_button': gi.FunctionInfo(set_button), 'set_coords': gi.FunctionInfo(set_coords), 'set_device': gi.FunctionInfo(set_device), 'set_flags': gi.FunctionInfo(set_flags), 'set_key_code': gi.FunctionInfo(set_key_code), 'set_key_symbol': gi.FunctionInfo(set_key_symbol), 'set_key_unicode': gi.FunctionInfo(set_key_unicode), 'set_related': gi.FunctionInfo(set_related), 'set_scroll_delta': gi.FunctionInfo(set_scroll_delta), 'set_scroll_direction': gi.FunctionInfo(set_scroll_direction), 'set_source': gi.FunctionInfo(set_source), 'set_source_device': gi.FunctionInfo(set_source_device), 'set_stage': gi.FunctionInfo(set_stage), 'set_state': gi.FunctionInfo(set_state), 'set_time': gi.FunctionInfo(set_time), 'add_filter': gi.FunctionInfo(add_filter), 'get': gi.FunctionInfo(get), 'peek': gi.FunctionInfo(peek), 'remove_filter': gi.FunctionInfo(remove_filter)})"
    __gtype__ = None # (!) real value is '<GType ClutterEvent (94911696131472)>'
    __info__ = gi.UnionInfo(Event)


