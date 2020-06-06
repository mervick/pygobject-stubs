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


class InputDevice(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        InputDevice(**properties)
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

    def get_associated_device(self): # real signature unknown; restored from __doc__
        """ get_associated_device(self) -> Clutter.InputDevice """
        pass

    def get_axis(self, index_): # real signature unknown; restored from __doc__
        """ get_axis(self, index_:int) -> Clutter.InputAxis """
        pass

    def get_axis_value(self, axes, axis): # real signature unknown; restored from __doc__
        """ get_axis_value(self, axes:list, axis:Clutter.InputAxis) -> bool, value:float """
        return False

    def get_coords(self, sequence=None): # real signature unknown; restored from __doc__
        """ get_coords(self, sequence:Clutter.EventSequence=None) -> bool, point:Clutter.Point """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_device_coords(self): # real signature unknown; restored from __doc__
        """ get_device_coords(self) -> x:int, y:int """
        return x

    def get_device_id(self): # real signature unknown; restored from __doc__
        """ get_device_id(self) -> int """
        return 0

    def get_device_mode(self): # real signature unknown; restored from __doc__
        """ get_device_mode(self) -> Clutter.InputMode """
        pass

    def get_device_name(self): # real signature unknown; restored from __doc__
        """ get_device_name(self) -> str """
        return ""

    def get_device_type(self): # real signature unknown; restored from __doc__
        """ get_device_type(self) -> Clutter.InputDeviceType """
        pass

    def get_enabled(self): # real signature unknown; restored from __doc__
        """ get_enabled(self) -> bool """
        return False

    def get_grabbed_actor(self): # real signature unknown; restored from __doc__
        """ get_grabbed_actor(self) -> Clutter.Actor """
        pass

    def get_has_cursor(self): # real signature unknown; restored from __doc__
        """ get_has_cursor(self) -> bool """
        return False

    def get_key(self, index_): # real signature unknown; restored from __doc__
        """ get_key(self, index_:int) -> bool, keyval:int, modifiers:Clutter.ModifierType """
        return False

    def get_modifier_state(self): # real signature unknown; restored from __doc__
        """ get_modifier_state(self) -> Clutter.ModifierType """
        pass

    def get_n_axes(self): # real signature unknown; restored from __doc__
        """ get_n_axes(self) -> int """
        return 0

    def get_n_keys(self): # real signature unknown; restored from __doc__
        """ get_n_keys(self) -> int """
        return 0

    def get_pointer_actor(self): # real signature unknown; restored from __doc__
        """ get_pointer_actor(self) -> Clutter.Actor """
        pass

    def get_pointer_stage(self): # real signature unknown; restored from __doc__
        """ get_pointer_stage(self) -> Clutter.Stage """
        pass

    def get_product_id(self): # real signature unknown; restored from __doc__
        """ get_product_id(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_slave_devices(self): # real signature unknown; restored from __doc__
        """ get_slave_devices(self) -> list """
        return []

    def get_vendor_id(self): # real signature unknown; restored from __doc__
        """ get_vendor_id(self) -> str """
        return ""

    def grab(self, actor): # real signature unknown; restored from __doc__
        """ grab(self, actor:Clutter.Actor) """
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

    def keycode_to_evdev(self, hardware_keycode, evdev_keycode): # real signature unknown; restored from __doc__
        """ keycode_to_evdev(self, hardware_keycode:int, evdev_keycode:int) -> bool """
        return False

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

    def sequence_get_grabbed_actor(self, sequence): # real signature unknown; restored from __doc__
        """ sequence_get_grabbed_actor(self, sequence:Clutter.EventSequence) -> Clutter.Actor """
        pass

    def sequence_grab(self, sequence, actor): # real signature unknown; restored from __doc__
        """ sequence_grab(self, sequence:Clutter.EventSequence, actor:Clutter.Actor) """
        pass

    def sequence_ungrab(self, sequence): # real signature unknown; restored from __doc__
        """ sequence_ungrab(self, sequence:Clutter.EventSequence) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_enabled(self, enabled:bool) """
        pass

    def set_key(self, index_, keyval, modifiers): # real signature unknown; restored from __doc__
        """ set_key(self, index_:int, keyval:int, modifiers:Clutter.ModifierType) """
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

    def ungrab(self): # real signature unknown; restored from __doc__
        """ ungrab(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update_from_event(self, event, update_stage): # real signature unknown; restored from __doc__
        """ update_from_event(self, event:Clutter.Event, update_stage:bool) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f5413204fd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(InputDevice), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterInputDevice (94911696107872)>, '__doc__': None, '__gsignals__': {}, 'get_associated_device': gi.FunctionInfo(get_associated_device), 'get_axis': gi.FunctionInfo(get_axis), 'get_axis_value': gi.FunctionInfo(get_axis_value), 'get_coords': gi.FunctionInfo(get_coords), 'get_device_coords': gi.FunctionInfo(get_device_coords), 'get_device_id': gi.FunctionInfo(get_device_id), 'get_device_mode': gi.FunctionInfo(get_device_mode), 'get_device_name': gi.FunctionInfo(get_device_name), 'get_device_type': gi.FunctionInfo(get_device_type), 'get_enabled': gi.FunctionInfo(get_enabled), 'get_grabbed_actor': gi.FunctionInfo(get_grabbed_actor), 'get_has_cursor': gi.FunctionInfo(get_has_cursor), 'get_key': gi.FunctionInfo(get_key), 'get_modifier_state': gi.FunctionInfo(get_modifier_state), 'get_n_axes': gi.FunctionInfo(get_n_axes), 'get_n_keys': gi.FunctionInfo(get_n_keys), 'get_pointer_actor': gi.FunctionInfo(get_pointer_actor), 'get_pointer_stage': gi.FunctionInfo(get_pointer_stage), 'get_product_id': gi.FunctionInfo(get_product_id), 'get_slave_devices': gi.FunctionInfo(get_slave_devices), 'get_vendor_id': gi.FunctionInfo(get_vendor_id), 'grab': gi.FunctionInfo(grab), 'keycode_to_evdev': gi.FunctionInfo(keycode_to_evdev), 'sequence_get_grabbed_actor': gi.FunctionInfo(sequence_get_grabbed_actor), 'sequence_grab': gi.FunctionInfo(sequence_grab), 'sequence_ungrab': gi.FunctionInfo(sequence_ungrab), 'set_enabled': gi.FunctionInfo(set_enabled), 'set_key': gi.FunctionInfo(set_key), 'ungrab': gi.FunctionInfo(ungrab), 'update_from_event': gi.FunctionInfo(update_from_event)})"
    __gdoc__ = 'Object ClutterInputDevice\n\nProperties from ClutterInputDevice:\n  backend -> ClutterBackend: Backend\n    The backend instance\n  id -> gint: Id\n    Unique identifier of the device\n  name -> gchararray: Name\n    The name of the device\n  device-type -> ClutterInputDeviceType: Device Type\n    The type of the device\n  device-manager -> ClutterDeviceManager: Device Manager\n    The device manager instance\n  device-mode -> ClutterInputMode: Device Mode\n    The mode of the device\n  has-cursor -> gboolean: Has Cursor\n    Whether the device has a cursor\n  enabled -> gboolean: Enabled\n    Whether the device is enabled\n  n-axes -> guint: Number of Axes\n    The number of axes on the device\n  vendor-id -> gchararray: Vendor ID\n    Vendor ID\n  product-id -> gchararray: Product ID\n    Product ID\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterInputDevice (94911696107872)>'
    __info__ = ObjectInfo(InputDevice)


