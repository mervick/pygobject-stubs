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


from .GestureAction import GestureAction

class ZoomAction(GestureAction):
    """
    :Constructors:
    
    ::
    
        ZoomAction(**properties)
        new() -> Clutter.Action
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) """
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

    def do_gesture_begin(self, *args, **kwargs): # real signature unknown
        """ gesture_begin(self, actor:Clutter.Actor) -> bool """
        pass

    def do_gesture_cancel(self, *args, **kwargs): # real signature unknown
        """ gesture_cancel(self, actor:Clutter.Actor) """
        pass

    def do_gesture_end(self, *args, **kwargs): # real signature unknown
        """ gesture_end(self, actor:Clutter.Actor) """
        pass

    def do_gesture_prepare(self, *args, **kwargs): # real signature unknown
        """ gesture_prepare(self, actor:Clutter.Actor) -> bool """
        pass

    def do_gesture_progress(self, *args, **kwargs): # real signature unknown
        """ gesture_progress(self, actor:Clutter.Actor) -> bool """
        pass

    def do_set_actor(self, *args, **kwargs): # real signature unknown
        """ set_actor(self, actor:Clutter.Actor=None) """
        pass

    def do_zoom(self, *args, **kwargs): # real signature unknown
        """ zoom(self, actor:Clutter.Actor, focal_point:Clutter.Point, factor:float) -> bool """
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

    def get_actor(self): # real signature unknown; restored from __doc__
        """ get_actor(self) -> Clutter.Actor """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_device(self, point): # real signature unknown; restored from __doc__
        """ get_device(self, point:int) -> Clutter.InputDevice """
        pass

    def get_enabled(self): # real signature unknown; restored from __doc__
        """ get_enabled(self) -> bool """
        return False

    def get_focal_point(self): # real signature unknown; restored from __doc__
        """ get_focal_point(self) -> point:Clutter.Point """
        pass

    def get_last_event(self, point): # real signature unknown; restored from __doc__
        """ get_last_event(self, point:int) -> Clutter.Event """
        pass

    def get_motion_coords(self, point): # real signature unknown; restored from __doc__
        """ get_motion_coords(self, point:int) -> motion_x:float, motion_y:float """
        pass

    def get_motion_delta(self, point): # real signature unknown; restored from __doc__
        """ get_motion_delta(self, point:int) -> float, delta_x:float, delta_y:float """
        return 0.0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_current_points(self): # real signature unknown; restored from __doc__
        """ get_n_current_points(self) -> int """
        return 0

    def get_n_touch_points(self): # real signature unknown; restored from __doc__
        """ get_n_touch_points(self) -> int """
        return 0

    def get_press_coords(self, point): # real signature unknown; restored from __doc__
        """ get_press_coords(self, point:int) -> press_x:float, press_y:float """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_release_coords(self, point): # real signature unknown; restored from __doc__
        """ get_release_coords(self, point:int) -> release_x:float, release_y:float """
        pass

    def get_sequence(self, point): # real signature unknown; restored from __doc__
        """ get_sequence(self, point:int) -> Clutter.EventSequence """
        pass

    def get_threshold_trigger_distance(self): # real signature unknown; restored from __doc__
        """ get_threshold_trigger_distance(self) -> x:float, y:float """
        return x

    def get_threshold_trigger_edge(self): # real signature unknown; restored from __doc__
        """ get_threshold_trigger_edge(self) -> Clutter.GestureTriggerEdge """
        pass

    def get_threshold_trigger_egde(self): # real signature unknown; restored from __doc__
        """ get_threshold_trigger_egde(self) -> Clutter.GestureTriggerEdge """
        pass

    def get_transformed_focal_point(self): # real signature unknown; restored from __doc__
        """ get_transformed_focal_point(self) -> point:Clutter.Point """
        pass

    def get_velocity(self, point): # real signature unknown; restored from __doc__
        """ get_velocity(self, point:int) -> float, velocity_x:float, velocity_y:float """
        return 0.0

    def get_zoom_axis(self): # real signature unknown; restored from __doc__
        """ get_zoom_axis(self) -> Clutter.ZoomAxis """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Clutter.Action """
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

    def set_enabled(self, is_enabled): # real signature unknown; restored from __doc__
        """ set_enabled(self, is_enabled:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_n_touch_points(self, nb_points): # real signature unknown; restored from __doc__
        """ set_n_touch_points(self, nb_points:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_threshold_trigger_distance(self, x, y): # real signature unknown; restored from __doc__
        """ set_threshold_trigger_distance(self, x:float, y:float) """
        pass

    def set_threshold_trigger_edge(self, edge): # real signature unknown; restored from __doc__
        """ set_threshold_trigger_edge(self, edge:Clutter.GestureTriggerEdge) """
        pass

    def set_zoom_axis(self, axis): # real signature unknown; restored from __doc__
        """ set_zoom_axis(self, axis:Clutter.ZoomAxis) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f5412f78250>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ZoomAction), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterZoomAction (94911696721824)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_focal_point': gi.FunctionInfo(get_focal_point), 'get_transformed_focal_point': gi.FunctionInfo(get_transformed_focal_point), 'get_zoom_axis': gi.FunctionInfo(get_zoom_axis), 'set_zoom_axis': gi.FunctionInfo(set_zoom_axis), 'do_zoom': gi.VFuncInfo(zoom), 'parent_instance': <property object at 0x7f54134ef590>, 'priv': <property object at 0x7f54134ef680>})"
    __gdoc__ = 'Object ClutterZoomAction\n\nSignals from ClutterZoomAction:\n  zoom (ClutterActor, ClutterPoint, gdouble) -> gboolean\n\nProperties from ClutterZoomAction:\n  zoom-axis -> ClutterZoomAxis: Zoom Axis\n    Constraints the zoom to an axis\n\nSignals from ClutterGestureAction:\n  gesture-begin (ClutterActor) -> gboolean\n  gesture-progress (ClutterActor) -> gboolean\n  gesture-end (ClutterActor)\n  gesture-cancel (ClutterActor)\n\nProperties from ClutterGestureAction:\n  n-touch-points -> gint: Number touch points\n    Number of touch points\n  threshold-trigger-edge -> ClutterGestureTriggerEdge: Threshold Trigger Edge\n    The trigger edge used by the action\n  threshold-trigger-distance-x -> gfloat: Threshold Trigger Horizontal Distance\n    The horizontal trigger distance used by the action\n  threshold-trigger-distance-y -> gfloat: Threshold Trigger Vertical Distance\n    The vertical trigger distance used by the action\n\nProperties from ClutterActorMeta:\n  actor -> ClutterActor: Actor\n    The actor attached to the meta\n  name -> gchararray: Name\n    The name of the meta\n  enabled -> gboolean: Enabled\n    Whether the meta is enabled\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterZoomAction (94911696721824)>'
    __info__ = ObjectInfo(ZoomAction)


