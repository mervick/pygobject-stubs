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


from .Scriptable import Scriptable

class Timeline(__gi_overrides_GObject.Object, Scriptable):
    """
    :Constructors:
    
    ::
    
        Timeline(**properties)
        new(msecs:int) -> Clutter.Timeline
    """
    def add_marker(self, marker_name, progress): # real signature unknown; restored from __doc__
        """ add_marker(self, marker_name:str, progress:float) """
        pass

    def add_marker_at_time(self, marker_name, msecs): # real signature unknown; restored from __doc__
        """ add_marker_at_time(self, marker_name:str, msecs:int) """
        pass

    def advance(self, msecs): # real signature unknown; restored from __doc__
        """ advance(self, msecs:int) """
        pass

    def advance_to_marker(self, marker_name): # real signature unknown; restored from __doc__
        """ advance_to_marker(self, marker_name:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Clutter.Timeline """
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

    def do_completed(self, *args, **kwargs): # real signature unknown
        """ completed(self) """
        pass

    def do_marker_reached(self, *args, **kwargs): # real signature unknown
        """ marker_reached(self, marker_name:str, msecs:int) """
        pass

    def do_new_frame(self, *args, **kwargs): # real signature unknown
        """ new_frame(self, msecs:int) """
        pass

    def do_paused(self, *args, **kwargs): # real signature unknown
        """ paused(self) """
        pass

    def do_started(self, *args, **kwargs): # real signature unknown
        """ started(self) """
        pass

    def do_stopped(self, *args, **kwargs): # real signature unknown
        """ stopped(self, is_finished:bool) """
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

    def get_auto_reverse(self): # real signature unknown; restored from __doc__
        """ get_auto_reverse(self) -> bool """
        return False

    def get_cubic_bezier_progress(self): # real signature unknown; restored from __doc__
        """ get_cubic_bezier_progress(self) -> bool, c_1:Clutter.Point, c_2:Clutter.Point """
        return False

    def get_current_repeat(self): # real signature unknown; restored from __doc__
        """ get_current_repeat(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_delay(self): # real signature unknown; restored from __doc__
        """ get_delay(self) -> int """
        return 0

    def get_delta(self): # real signature unknown; restored from __doc__
        """ get_delta(self) -> int """
        return 0

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Clutter.TimelineDirection """
        pass

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> int """
        return 0

    def get_duration_hint(self): # real signature unknown; restored from __doc__
        """ get_duration_hint(self) -> int """
        return 0

    def get_elapsed_time(self): # real signature unknown; restored from __doc__
        """ get_elapsed_time(self) -> int """
        return 0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_loop(self): # real signature unknown; restored from __doc__
        """ get_loop(self) -> bool """
        return False

    def get_progress(self): # real signature unknown; restored from __doc__
        """ get_progress(self) -> float """
        return 0.0

    def get_progress_mode(self): # real signature unknown; restored from __doc__
        """ get_progress_mode(self) -> Clutter.AnimationMode """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_repeat_count(self): # real signature unknown; restored from __doc__
        """ get_repeat_count(self) -> int """
        return 0

    def get_step_progress(self): # real signature unknown; restored from __doc__
        """ get_step_progress(self) -> bool, n_steps:int, step_mode:Clutter.StepMode """
        return False

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

    def has_marker(self, marker_name): # real signature unknown; restored from __doc__
        """ has_marker(self, marker_name:str) -> bool """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_playing(self): # real signature unknown; restored from __doc__
        """ is_playing(self) -> bool """
        return False

    def list_markers(self, msecs): # real signature unknown; restored from __doc__
        """ list_markers(self, msecs:int) -> list, n_markers:int """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, msecs): # real signature unknown; restored from __doc__
        """ new(msecs:int) -> Clutter.Timeline """
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

    def parse_custom_node(self, script, value, name, node): # real signature unknown; restored from __doc__
        """ parse_custom_node(self, script:Clutter.Script, value:GObject.Value, name:str, node:Json.Node) -> bool """
        return False

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_marker(self, marker_name): # real signature unknown; restored from __doc__
        """ remove_marker(self, marker_name:str) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def rewind(self): # real signature unknown; restored from __doc__
        """ rewind(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_auto_reverse(self, reverse): # real signature unknown; restored from __doc__
        """ set_auto_reverse(self, reverse:bool) """
        pass

    def set_cubic_bezier_progress(self, c_1, c_2): # real signature unknown; restored from __doc__
        """ set_cubic_bezier_progress(self, c_1:Clutter.Point, c_2:Clutter.Point) """
        pass

    def set_custom_property(self, script, name, value): # real signature unknown; restored from __doc__
        """ set_custom_property(self, script:Clutter.Script, name:str, value:GObject.Value) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_delay(self, msecs): # real signature unknown; restored from __doc__
        """ set_delay(self, msecs:int) """
        pass

    def set_direction(self, direction): # real signature unknown; restored from __doc__
        """ set_direction(self, direction:Clutter.TimelineDirection) """
        pass

    def set_duration(self, msecs): # real signature unknown; restored from __doc__
        """ set_duration(self, msecs:int) """
        pass

    def set_id(self, id_): # real signature unknown; restored from __doc__
        """ set_id(self, id_:str) """
        pass

    def set_loop(self, loop): # real signature unknown; restored from __doc__
        """ set_loop(self, loop:bool) """
        pass

    def set_progress_func(self, func=None, data=None): # real signature unknown; restored from __doc__
        """ set_progress_func(self, func:Clutter.TimelineProgressFunc=None, data=None) """
        pass

    def set_progress_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_progress_mode(self, mode:Clutter.AnimationMode) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_repeat_count(self, count): # real signature unknown; restored from __doc__
        """ set_repeat_count(self, count:int) """
        pass

    def set_step_progress(self, n_steps, step_mode): # real signature unknown; restored from __doc__
        """ set_step_progress(self, n_steps:int, step_mode:Clutter.StepMode) """
        pass

    def skip(self, msecs): # real signature unknown; restored from __doc__
        """ skip(self, msecs:int) """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f54130dce80>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Timeline), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterTimeline (94911696157872)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_marker': gi.FunctionInfo(add_marker), 'add_marker_at_time': gi.FunctionInfo(add_marker_at_time), 'advance': gi.FunctionInfo(advance), 'advance_to_marker': gi.FunctionInfo(advance_to_marker), 'clone': gi.FunctionInfo(clone), 'get_auto_reverse': gi.FunctionInfo(get_auto_reverse), 'get_cubic_bezier_progress': gi.FunctionInfo(get_cubic_bezier_progress), 'get_current_repeat': gi.FunctionInfo(get_current_repeat), 'get_delay': gi.FunctionInfo(get_delay), 'get_delta': gi.FunctionInfo(get_delta), 'get_direction': gi.FunctionInfo(get_direction), 'get_duration': gi.FunctionInfo(get_duration), 'get_duration_hint': gi.FunctionInfo(get_duration_hint), 'get_elapsed_time': gi.FunctionInfo(get_elapsed_time), 'get_loop': gi.FunctionInfo(get_loop), 'get_progress': gi.FunctionInfo(get_progress), 'get_progress_mode': gi.FunctionInfo(get_progress_mode), 'get_repeat_count': gi.FunctionInfo(get_repeat_count), 'get_step_progress': gi.FunctionInfo(get_step_progress), 'has_marker': gi.FunctionInfo(has_marker), 'is_playing': gi.FunctionInfo(is_playing), 'list_markers': gi.FunctionInfo(list_markers), 'pause': gi.FunctionInfo(pause), 'remove_marker': gi.FunctionInfo(remove_marker), 'rewind': gi.FunctionInfo(rewind), 'set_auto_reverse': gi.FunctionInfo(set_auto_reverse), 'set_cubic_bezier_progress': gi.FunctionInfo(set_cubic_bezier_progress), 'set_delay': gi.FunctionInfo(set_delay), 'set_direction': gi.FunctionInfo(set_direction), 'set_duration': gi.FunctionInfo(set_duration), 'set_loop': gi.FunctionInfo(set_loop), 'set_progress_func': gi.FunctionInfo(set_progress_func), 'set_progress_mode': gi.FunctionInfo(set_progress_mode), 'set_repeat_count': gi.FunctionInfo(set_repeat_count), 'set_step_progress': gi.FunctionInfo(set_step_progress), 'skip': gi.FunctionInfo(skip), 'start': gi.FunctionInfo(start), 'stop': gi.FunctionInfo(stop), 'do_completed': gi.VFuncInfo(completed), 'do_marker_reached': gi.VFuncInfo(marker_reached), 'do_new_frame': gi.VFuncInfo(new_frame), 'do_paused': gi.VFuncInfo(paused), 'do_started': gi.VFuncInfo(started), 'do_stopped': gi.VFuncInfo(stopped), 'parent_instance': <property object at 0x7f541408a4f0>, 'priv': <property object at 0x7f5413512720>})"
    __gdoc__ = 'Object ClutterTimeline\n\nSignals from ClutterTimeline:\n  started ()\n  completed ()\n  new-frame (gint)\n  paused ()\n  marker-reached (gchararray, gint)\n  stopped (gboolean)\n\nProperties from ClutterTimeline:\n  loop -> gboolean: Loop\n    Should the timeline automatically restart\n  delay -> guint: Delay\n    Delay before start\n  duration -> guint: Duration\n    Duration of the timeline in milliseconds\n  direction -> ClutterTimelineDirection: Direction\n    Direction of the timeline\n  auto-reverse -> gboolean: Auto Reverse\n    Whether the direction should be reversed when reaching the end\n  repeat-count -> gint: Repeat Count\n    How many times the timeline should repeat\n  progress-mode -> ClutterAnimationMode: Progress Mode\n    How the timeline should compute the progress\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterTimeline (94911696157872)>'
    __info__ = ObjectInfo(Timeline)


