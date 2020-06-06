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


from .Action import Action

class DragAction(Action):
    """
    :Constructors:
    
    ::
    
        DragAction(**properties)
        new() -> Clutter.Action
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

    def do_drag_begin(self, *args, **kwargs): # real signature unknown
        """ drag_begin(self, actor:Clutter.Actor, event_x:float, event_y:float, modifiers:Clutter.ModifierType) """
        pass

    def do_drag_end(self, *args, **kwargs): # real signature unknown
        """ drag_end(self, actor:Clutter.Actor, event_x:float, event_y:float, modifiers:Clutter.ModifierType) """
        pass

    def do_drag_motion(self, *args, **kwargs): # real signature unknown
        """ drag_motion(self, actor:Clutter.Actor, delta_x:float, delta_y:float) """
        pass

    def do_drag_progress(self, *args, **kwargs): # real signature unknown
        """ drag_progress(self, actor:Clutter.Actor, delta_x:float, delta_y:float) -> bool """
        pass

    def do_set_actor(self, *args, **kwargs): # real signature unknown
        """ set_actor(self, actor:Clutter.Actor=None) """
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

    def get_drag_area(self): # real signature unknown; restored from __doc__
        """ get_drag_area(self) -> bool, drag_area:Clutter.Rect """
        return False

    def get_drag_axis(self): # real signature unknown; restored from __doc__
        """ get_drag_axis(self) -> Clutter.DragAxis """
        pass

    def get_drag_handle(self): # real signature unknown; restored from __doc__
        """ get_drag_handle(self) -> Clutter.Actor """
        pass

    def get_drag_threshold(self): # real signature unknown; restored from __doc__
        """ get_drag_threshold(self) -> x_threshold:int, y_threshold:int """
        pass

    def get_enabled(self): # real signature unknown; restored from __doc__
        """ get_enabled(self) -> bool """
        return False

    def get_motion_coords(self): # real signature unknown; restored from __doc__
        """ get_motion_coords(self) -> motion_x:float, motion_y:float """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_press_coords(self): # real signature unknown; restored from __doc__
        """ get_press_coords(self) -> press_x:float, press_y:float """
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

    def set_drag_area(self, drag_area=None): # real signature unknown; restored from __doc__
        """ set_drag_area(self, drag_area:Clutter.Rect=None) """
        pass

    def set_drag_axis(self, axis): # real signature unknown; restored from __doc__
        """ set_drag_axis(self, axis:Clutter.DragAxis) """
        pass

    def set_drag_handle(self, handle=None): # real signature unknown; restored from __doc__
        """ set_drag_handle(self, handle:Clutter.Actor=None) """
        pass

    def set_drag_threshold(self, x_threshold, y_threshold): # real signature unknown; restored from __doc__
        """ set_drag_threshold(self, x_threshold:int, y_threshold:int) """
        pass

    def set_enabled(self, is_enabled): # real signature unknown; restored from __doc__
        """ set_enabled(self, is_enabled:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f5413204cd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DragAction), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterDragAction (94911695974176)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_drag_area': gi.FunctionInfo(get_drag_area), 'get_drag_axis': gi.FunctionInfo(get_drag_axis), 'get_drag_handle': gi.FunctionInfo(get_drag_handle), 'get_drag_threshold': gi.FunctionInfo(get_drag_threshold), 'get_motion_coords': gi.FunctionInfo(get_motion_coords), 'get_press_coords': gi.FunctionInfo(get_press_coords), 'set_drag_area': gi.FunctionInfo(set_drag_area), 'set_drag_axis': gi.FunctionInfo(set_drag_axis), 'set_drag_handle': gi.FunctionInfo(set_drag_handle), 'set_drag_threshold': gi.FunctionInfo(set_drag_threshold), 'do_drag_begin': gi.VFuncInfo(drag_begin), 'do_drag_end': gi.VFuncInfo(drag_end), 'do_drag_motion': gi.VFuncInfo(drag_motion), 'do_drag_progress': gi.VFuncInfo(drag_progress), 'parent_instance': <property object at 0x7f5413ca8770>, 'priv': <property object at 0x7f5413ca8860>})"
    __gdoc__ = 'Object ClutterDragAction\n\nSignals from ClutterDragAction:\n  drag-begin (ClutterActor, gfloat, gfloat, ClutterModifierType)\n  drag-progress (ClutterActor, gfloat, gfloat) -> gboolean\n  drag-motion (ClutterActor, gfloat, gfloat)\n  drag-end (ClutterActor, gfloat, gfloat, ClutterModifierType)\n\nProperties from ClutterDragAction:\n  x-drag-threshold -> gint: Horizontal Drag Threshold\n    The horizontal amount of pixels required to start dragging\n  y-drag-threshold -> gint: Vertical Drag Threshold\n    The vertical amount of pixels required to start dragging\n  drag-handle -> ClutterActor: Drag Handle\n    The actor that is being dragged\n  drag-axis -> ClutterDragAxis: Drag Axis\n    Constraints the dragging to an axis\n  drag-area -> ClutterRect: Drag Area\n    Constrains the dragging to a rectangle\n  drag-area-set -> gboolean: Drag Area Set\n    Whether the drag area is set\n\nProperties from ClutterActorMeta:\n  actor -> ClutterActor: Actor\n    The actor attached to the meta\n  name -> gchararray: Name\n    The name of the meta\n  enabled -> gboolean: Enabled\n    Whether the meta is enabled\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterDragAction (94911695974176)>'
    __info__ = ObjectInfo(DragAction)


