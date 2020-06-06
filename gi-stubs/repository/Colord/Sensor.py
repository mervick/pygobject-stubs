# encoding: utf-8
# module gi.repository.Colord
# from /usr/lib64/girepository-1.0/Colord-1.0.typelib
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
import gobject as __gobject


class Sensor(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Sensor(**properties)
        new() -> Colord.Sensor
        new_with_object_path(object_path:str) -> Colord.Sensor
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cap_from_string(self, sensor_cap): # real signature unknown; restored from __doc__
        """ cap_from_string(sensor_cap:str) -> Colord.SensorCap """
        pass

    def cap_to_string(self, sensor_cap): # real signature unknown; restored from __doc__
        """ cap_to_string(sensor_cap:Colord.SensorCap) -> str """
        return ""

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def connect_finish(self, res): # real signature unknown; restored from __doc__
        """ connect_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_button_pressed(self, *args, **kwargs): # real signature unknown
        """ button_pressed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equal(self, sensor2): # real signature unknown; restored from __doc__
        """ equal(self, sensor2:Colord.Sensor) -> bool """
        return False

    def error_from_string(self, error_desc): # real signature unknown; restored from __doc__
        """ error_from_string(error_desc:str) -> Colord.SensorError """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def error_to_string(self, error_enum): # real signature unknown; restored from __doc__
        """ error_to_string(error_enum:Colord.SensorError) -> str """
        return ""

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

    def get_caps(self): # real signature unknown; restored from __doc__
        """ get_caps(self) -> int """
        return 0

    def get_connected(self): # real signature unknown; restored from __doc__
        """ get_connected(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_embedded(self): # real signature unknown; restored from __doc__
        """ get_embedded(self) -> bool """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> Colord.SensorKind """
        pass

    def get_locked(self): # real signature unknown; restored from __doc__
        """ get_locked(self) -> bool """
        return False

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> dict """
        return {}

    def get_metadata_item(self, key): # real signature unknown; restored from __doc__
        """ get_metadata_item(self, key:str) -> str """
        return ""

    def get_mode(self): # real signature unknown; restored from __doc__
        """ get_mode(self) -> Colord.SensorCap """
        pass

    def get_model(self): # real signature unknown; restored from __doc__
        """ get_model(self) -> str """
        return ""

    def get_native(self): # real signature unknown; restored from __doc__
        """ get_native(self) -> bool """
        return False

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_option(self, key): # real signature unknown; restored from __doc__
        """ get_option(self, key:str) -> str """
        return ""

    def get_options(self): # real signature unknown; restored from __doc__
        """ get_options(self) -> dict """
        return {}

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sample(self, cap, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_sample(self, cap:Colord.SensorCap, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_sample_finish(self, res): # real signature unknown; restored from __doc__
        """ get_sample_finish(self, res:Gio.AsyncResult) -> Colord.ColorXYZ """
        pass

    def get_sample_sync(self, cap, cancellable=None): # real signature unknown; restored from __doc__
        """ get_sample_sync(self, cap:Colord.SensorCap, cancellable:Gio.Cancellable=None) -> Colord.ColorXYZ """
        pass

    def get_serial(self): # real signature unknown; restored from __doc__
        """ get_serial(self) -> str """
        return ""

    def get_spectrum(self, cap, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_spectrum(self, cap:Colord.SensorCap, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_spectrum_finish(self, res): # real signature unknown; restored from __doc__
        """ get_spectrum_finish(self, res:Gio.AsyncResult) -> Colord.Spectrum """
        pass

    def get_spectrum_sync(self, cap, cancellable=None): # real signature unknown; restored from __doc__
        """ get_spectrum_sync(self, cap:Colord.SensorCap, cancellable:Gio.Cancellable=None) -> Colord.Spectrum """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Colord.SensorState """
        pass

    def get_vendor(self): # real signature unknown; restored from __doc__
        """ get_vendor(self) -> str """
        return ""

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

    def has_cap(self, cap): # real signature unknown; restored from __doc__
        """ has_cap(self, cap:Colord.SensorCap) -> bool """
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

    def kind_from_string(self, sensor_kind): # real signature unknown; restored from __doc__
        """ kind_from_string(sensor_kind:str) -> Colord.SensorKind """
        pass

    def kind_to_string(self, sensor_kind): # real signature unknown; restored from __doc__
        """ kind_to_string(sensor_kind:Colord.SensorKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lock(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lock(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lock_finish(self, res): # real signature unknown; restored from __doc__
        """ lock_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def lock_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ lock_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Colord.Sensor """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ new_with_object_path(object_path:str) -> Colord.Sensor """
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

    def set_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ set_object_path(self, object_path:str) """
        pass

    def set_options(self, values, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_options(self, values:dict, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_options_finish(self, res): # real signature unknown; restored from __doc__
        """ set_options_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_options_sync(self, values, cancellable=None): # real signature unknown; restored from __doc__
        """ set_options_sync(self, values:dict, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def state_from_string(self, sensor_state): # real signature unknown; restored from __doc__
        """ state_from_string(sensor_state:str) -> Colord.SensorState """
        pass

    def state_to_string(self, sensor_state): # real signature unknown; restored from __doc__
        """ state_to_string(sensor_state:Colord.SensorState) -> str """
        return ""

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

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unlock(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unlock(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unlock_finish(self, res): # real signature unknown; restored from __doc__
        """ unlock_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def unlock_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ unlock_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f09131e4dc0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Sensor), '__module__': 'gi.repository.Colord', '__gtype__': <GType CdSensor (94892598926448)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_object_path': gi.FunctionInfo(new_with_object_path), 'cap_from_string': gi.FunctionInfo(cap_from_string), 'cap_to_string': gi.FunctionInfo(cap_to_string), 'error_from_string': gi.FunctionInfo(error_from_string), 'error_quark': gi.FunctionInfo(error_quark), 'error_to_string': gi.FunctionInfo(error_to_string), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'state_from_string': gi.FunctionInfo(state_from_string), 'state_to_string': gi.FunctionInfo(state_to_string), 'connect': gi.FunctionInfo(connect), 'connect_finish': gi.FunctionInfo(connect_finish), 'connect_sync': gi.FunctionInfo(connect_sync), 'equal': gi.FunctionInfo(equal), 'get_caps': gi.FunctionInfo(get_caps), 'get_connected': gi.FunctionInfo(get_connected), 'get_embedded': gi.FunctionInfo(get_embedded), 'get_id': gi.FunctionInfo(get_id), 'get_kind': gi.FunctionInfo(get_kind), 'get_locked': gi.FunctionInfo(get_locked), 'get_metadata': gi.FunctionInfo(get_metadata), 'get_metadata_item': gi.FunctionInfo(get_metadata_item), 'get_mode': gi.FunctionInfo(get_mode), 'get_model': gi.FunctionInfo(get_model), 'get_native': gi.FunctionInfo(get_native), 'get_object_path': gi.FunctionInfo(get_object_path), 'get_option': gi.FunctionInfo(get_option), 'get_options': gi.FunctionInfo(get_options), 'get_sample': gi.FunctionInfo(get_sample), 'get_sample_finish': gi.FunctionInfo(get_sample_finish), 'get_sample_sync': gi.FunctionInfo(get_sample_sync), 'get_serial': gi.FunctionInfo(get_serial), 'get_spectrum': gi.FunctionInfo(get_spectrum), 'get_spectrum_finish': gi.FunctionInfo(get_spectrum_finish), 'get_spectrum_sync': gi.FunctionInfo(get_spectrum_sync), 'get_state': gi.FunctionInfo(get_state), 'get_vendor': gi.FunctionInfo(get_vendor), 'has_cap': gi.FunctionInfo(has_cap), 'lock': gi.FunctionInfo(lock), 'lock_finish': gi.FunctionInfo(lock_finish), 'lock_sync': gi.FunctionInfo(lock_sync), 'set_object_path': gi.FunctionInfo(set_object_path), 'set_options': gi.FunctionInfo(set_options), 'set_options_finish': gi.FunctionInfo(set_options_finish), 'set_options_sync': gi.FunctionInfo(set_options_sync), 'to_string': gi.FunctionInfo(to_string), 'unlock': gi.FunctionInfo(unlock), 'unlock_finish': gi.FunctionInfo(unlock_finish), 'unlock_sync': gi.FunctionInfo(unlock_sync), 'do_button_pressed': gi.VFuncInfo(button_pressed), 'parent_instance': <property object at 0x7f09131e3090>})"
    __gdoc__ = 'Object CdSensor\n\nSignals from CdSensor:\n  button-pressed ()\n\nProperties from CdSensor:\n  object-path -> gchararray: object-path\n  id -> gchararray: id\n  connected -> gchararray: connected\n  kind -> gchararray: kind\n  state -> gchararray: state\n  mode -> gchararray: mode\n  serial -> gchararray: serial\n  model -> gchararray: model\n  vendor -> gchararray: vendor\n  native -> gchararray: native\n  embedded -> gchararray: embedded\n  locked -> gchararray: locked\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CdSensor (94892598926448)>'
    __info__ = ObjectInfo(Sensor)


