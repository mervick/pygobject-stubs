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


class LayoutManager(__gi_repository_GObject.InitiallyUnowned):
    """
    :Constructors:
    
    ::
    
        LayoutManager(**properties)
    """
    def allocate(self, container, allocation, flags): # real signature unknown; restored from __doc__
        """ allocate(self, container:Clutter.Container, allocation:Clutter.ActorBox, flags:Clutter.AllocationFlags) """
        pass

    def begin_animation(self, duration, mode): # real signature unknown; restored from __doc__
        """ begin_animation(self, duration:int, mode:int) -> Clutter.Alpha """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def child_get_property(self, container, actor, property_name, value): # real signature unknown; restored from __doc__
        """ child_get_property(self, container:Clutter.Container, actor:Clutter.Actor, property_name:str, value:GObject.Value) """
        pass

    def child_set_property(self, container, actor, property_name, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, container:Clutter.Container, actor:Clutter.Actor, property_name:str, value:GObject.Value) """
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

    def do_allocate(self, *args, **kwargs): # real signature unknown
        """ allocate(self, container:Clutter.Container, allocation:Clutter.ActorBox, flags:Clutter.AllocationFlags) """
        pass

    def do_begin_animation(self, *args, **kwargs): # real signature unknown
        """ begin_animation(self, duration:int, mode:int) -> Clutter.Alpha """
        pass

    def do_end_animation(self, *args, **kwargs): # real signature unknown
        """ end_animation(self) """
        pass

    def do_get_animation_progress(self, *args, **kwargs): # real signature unknown
        """ get_animation_progress(self) -> float """
        pass

    def do_get_child_meta_type(self, *args, **kwargs): # real signature unknown
        """ get_child_meta_type(self) -> GType """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self, container:Clutter.Container, for_width:float) -> min_height_p:float, nat_height_p:float """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self, container:Clutter.Container, for_height:float) -> min_width_p:float, nat_width_p:float """
        pass

    def do_layout_changed(self, *args, **kwargs): # real signature unknown
        """ layout_changed(self) """
        pass

    def do_set_container(self, *args, **kwargs): # real signature unknown
        """ set_container(self, container:Clutter.Container=None) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def end_animation(self): # real signature unknown; restored from __doc__
        """ end_animation(self) """
        pass

    def find_child_property(self, name): # real signature unknown; restored from __doc__
        """ find_child_property(self, name:str) -> GObject.ParamSpec """
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

    def get_animation_progress(self): # real signature unknown; restored from __doc__
        """ get_animation_progress(self) -> float """
        return 0.0

    def get_child_meta(self, container, actor): # real signature unknown; restored from __doc__
        """ get_child_meta(self, container:Clutter.Container, actor:Clutter.Actor) -> Clutter.LayoutMeta """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_preferred_height(self, container, for_width): # real signature unknown; restored from __doc__
        """ get_preferred_height(self, container:Clutter.Container, for_width:float) -> min_height_p:float, nat_height_p:float """
        pass

    def get_preferred_width(self, container, for_height): # real signature unknown; restored from __doc__
        """ get_preferred_width(self, container:Clutter.Container, for_height:float) -> min_width_p:float, nat_width_p:float """
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

    def layout_changed(self): # real signature unknown; restored from __doc__
        """ layout_changed(self) """
        pass

    def list_child_properties(self): # real signature unknown; restored from __doc__
        """ list_child_properties(self) -> list, n_pspecs:int """
        return []

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

    def set_container(self, container=None): # real signature unknown; restored from __doc__
        """ set_container(self, container:Clutter.Container=None) """
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

    dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f54133044f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(LayoutManager), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterLayoutManager (94911696000864)>, '__doc__': None, '__gsignals__': {}, 'allocate': gi.FunctionInfo(allocate), 'begin_animation': gi.FunctionInfo(begin_animation), 'child_get_property': gi.FunctionInfo(child_get_property), 'child_set_property': gi.FunctionInfo(child_set_property), 'end_animation': gi.FunctionInfo(end_animation), 'find_child_property': gi.FunctionInfo(find_child_property), 'get_animation_progress': gi.FunctionInfo(get_animation_progress), 'get_child_meta': gi.FunctionInfo(get_child_meta), 'get_preferred_height': gi.FunctionInfo(get_preferred_height), 'get_preferred_width': gi.FunctionInfo(get_preferred_width), 'layout_changed': gi.FunctionInfo(layout_changed), 'list_child_properties': gi.FunctionInfo(list_child_properties), 'set_container': gi.FunctionInfo(set_container), 'do_allocate': gi.VFuncInfo(allocate), 'do_begin_animation': gi.VFuncInfo(begin_animation), 'do_end_animation': gi.VFuncInfo(end_animation), 'do_get_animation_progress': gi.VFuncInfo(get_animation_progress), 'do_get_child_meta_type': gi.VFuncInfo(get_child_meta_type), 'do_get_preferred_height': gi.VFuncInfo(get_preferred_height), 'do_get_preferred_width': gi.VFuncInfo(get_preferred_width), 'do_layout_changed': gi.VFuncInfo(layout_changed), 'do_set_container': gi.VFuncInfo(set_container), 'parent_instance': <property object at 0x7f5413db30e0>, 'dummy': <property object at 0x7f5413db3310>})"
    __gdoc__ = 'Object ClutterLayoutManager\n\nSignals from ClutterLayoutManager:\n  layout-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterLayoutManager (94911696000864)>'
    __info__ = ObjectInfo(LayoutManager)

