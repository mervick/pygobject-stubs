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


class Client(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Client(**properties)
        new() -> Colord.Client
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

    def create_device(self, id, scope, properties=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_device(self, id:str, scope:Colord.ObjectScope, properties:dict=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_device_finish(self, res): # real signature unknown; restored from __doc__
        """ create_device_finish(self, res:Gio.AsyncResult) -> Colord.Device """
        pass

    def create_device_sync(self, id, scope, properties=None, cancellable=None): # real signature unknown; restored from __doc__
        """ create_device_sync(self, id:str, scope:Colord.ObjectScope, properties:dict=None, cancellable:Gio.Cancellable=None) -> Colord.Device """
        pass

    def create_profile(self, id, scope, properties=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_profile(self, id:str, scope:Colord.ObjectScope, properties:dict=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_profile_finish(self, res): # real signature unknown; restored from __doc__
        """ create_profile_finish(self, res:Gio.AsyncResult) -> Colord.Profile """
        pass

    def create_profile_for_icc(self, icc, scope, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_profile_for_icc(self, icc:Colord.Icc, scope:Colord.ObjectScope, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_profile_for_icc_finish(self, res): # real signature unknown; restored from __doc__
        """ create_profile_for_icc_finish(self, res:Gio.AsyncResult) -> Colord.Profile """
        pass

    def create_profile_for_icc_sync(self, icc, scope, cancellable=None): # real signature unknown; restored from __doc__
        """ create_profile_for_icc_sync(self, icc:Colord.Icc, scope:Colord.ObjectScope, cancellable:Gio.Cancellable=None) -> Colord.Profile """
        pass

    def create_profile_sync(self, id, scope, properties=None, cancellable=None): # real signature unknown; restored from __doc__
        """ create_profile_sync(self, id:str, scope:Colord.ObjectScope, properties:dict=None, cancellable:Gio.Cancellable=None) -> Colord.Profile """
        pass

    def delete_device(self, device, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_device(self, device:Colord.Device, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_device_finish(self, res): # real signature unknown; restored from __doc__
        """ delete_device_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def delete_device_sync(self, device, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_device_sync(self, device:Colord.Device, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_profile(self, profile, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_profile(self, profile:Colord.Profile, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_profile_finish(self, res): # real signature unknown; restored from __doc__
        """ delete_profile_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def delete_profile_sync(self, profile, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_profile_sync(self, profile:Colord.Profile, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_device_added(self, *args, **kwargs): # real signature unknown
        """ device_added(self, device:Colord.Device) """
        pass

    def do_device_changed(self, *args, **kwargs): # real signature unknown
        """ device_changed(self, device:Colord.Device) """
        pass

    def do_device_removed(self, *args, **kwargs): # real signature unknown
        """ device_removed(self, device:Colord.Device) """
        pass

    def do_profile_added(self, *args, **kwargs): # real signature unknown
        """ profile_added(self, profile:Colord.Profile) """
        pass

    def do_profile_changed(self, *args, **kwargs): # real signature unknown
        """ profile_changed(self, profile:Colord.Profile) """
        pass

    def do_profile_removed(self, *args, **kwargs): # real signature unknown
        """ profile_removed(self, profile:Colord.Profile) """
        pass

    def do_sensor_added(self, *args, **kwargs): # real signature unknown
        """ sensor_added(self, sensor:Colord.Sensor) """
        pass

    def do_sensor_changed(self, *args, **kwargs): # real signature unknown
        """ sensor_changed(self, sensor:Colord.Sensor) """
        pass

    def do_sensor_removed(self, *args, **kwargs): # real signature unknown
        """ sensor_removed(self, sensor:Colord.Sensor) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_from_string(self, error_desc): # real signature unknown; restored from __doc__
        """ error_from_string(error_desc:str) -> Colord.ClientError """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def error_to_string(self, error_enum): # real signature unknown; restored from __doc__
        """ error_to_string(error_enum:Colord.ClientError) -> str """
        return ""

    def find_device(self, id, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_device(self, id:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_device_by_property(self, key, value, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_device_by_property(self, key:str, value:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_device_by_property_finish(self, res): # real signature unknown; restored from __doc__
        """ find_device_by_property_finish(self, res:Gio.AsyncResult) -> Colord.Device """
        pass

    def find_device_by_property_sync(self, key, value, cancellable=None): # real signature unknown; restored from __doc__
        """ find_device_by_property_sync(self, key:str, value:str, cancellable:Gio.Cancellable=None) -> Colord.Device """
        pass

    def find_device_finish(self, res): # real signature unknown; restored from __doc__
        """ find_device_finish(self, res:Gio.AsyncResult) -> Colord.Device """
        pass

    def find_device_sync(self, id, cancellable=None): # real signature unknown; restored from __doc__
        """ find_device_sync(self, id:str, cancellable:Gio.Cancellable=None) -> Colord.Device """
        pass

    def find_profile(self, id, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_profile(self, id:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_profile_by_filename(self, filename, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_profile_by_filename(self, filename:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_profile_by_filename_finish(self, res): # real signature unknown; restored from __doc__
        """ find_profile_by_filename_finish(self, res:Gio.AsyncResult) -> Colord.Profile """
        pass

    def find_profile_by_filename_sync(self, filename, cancellable=None): # real signature unknown; restored from __doc__
        """ find_profile_by_filename_sync(self, filename:str, cancellable:Gio.Cancellable=None) -> Colord.Profile """
        pass

    def find_profile_by_property(self, key, value, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_profile_by_property(self, key:str, value:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_profile_by_property_finish(self, res): # real signature unknown; restored from __doc__
        """ find_profile_by_property_finish(self, res:Gio.AsyncResult) -> Colord.Profile """
        pass

    def find_profile_by_property_sync(self, key, value, cancellable=None): # real signature unknown; restored from __doc__
        """ find_profile_by_property_sync(self, key:str, value:str, cancellable:Gio.Cancellable=None) -> Colord.Profile """
        pass

    def find_profile_finish(self, res): # real signature unknown; restored from __doc__
        """ find_profile_finish(self, res:Gio.AsyncResult) -> Colord.Profile """
        pass

    def find_profile_sync(self, id, cancellable=None): # real signature unknown; restored from __doc__
        """ find_profile_sync(self, id:str, cancellable:Gio.Cancellable=None) -> Colord.Profile """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_sensor(self, id, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_sensor(self, id:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_sensor_finish(self, res): # real signature unknown; restored from __doc__
        """ find_sensor_finish(self, res:Gio.AsyncResult) -> Colord.Sensor """
        pass

    def find_sensor_sync(self, id, cancellable=None): # real signature unknown; restored from __doc__
        """ find_sensor_sync(self, id:str, cancellable:Gio.Cancellable=None) -> Colord.Sensor """
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

    def get_connected(self): # real signature unknown; restored from __doc__
        """ get_connected(self) -> bool """
        return False

    def get_daemon_version(self): # real signature unknown; restored from __doc__
        """ get_daemon_version(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_devices(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_devices(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_devices_by_kind(self, kind, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_devices_by_kind(self, kind:Colord.DeviceKind, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_devices_by_kind_finish(self, res): # real signature unknown; restored from __doc__
        """ get_devices_by_kind_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def get_devices_by_kind_sync(self, kind, cancellable=None): # real signature unknown; restored from __doc__
        """ get_devices_by_kind_sync(self, kind:Colord.DeviceKind, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_devices_finish(self, res): # real signature unknown; restored from __doc__
        """ get_devices_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def get_devices_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_devices_sync(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_has_server(self): # real signature unknown; restored from __doc__
        """ get_has_server(self) -> bool """
        return False

    def get_profiles(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_profiles(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_profiles_finish(self, res): # real signature unknown; restored from __doc__
        """ get_profiles_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def get_profiles_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_profiles_sync(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sensors(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_sensors(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_sensors_finish(self, res): # real signature unknown; restored from __doc__
        """ get_sensors_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def get_sensors_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_sensors_sync(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_standard_space(self, standard_space, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_standard_space(self, standard_space:Colord.StandardSpace, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_standard_space_finish(self, res): # real signature unknown; restored from __doc__
        """ get_standard_space_finish(self, res:Gio.AsyncResult) -> Colord.Profile """
        pass

    def get_standard_space_sync(self, standard_space, cancellable=None): # real signature unknown; restored from __doc__
        """ get_standard_space_sync(self, standard_space:Colord.StandardSpace, cancellable:Gio.Cancellable=None) -> Colord.Profile """
        pass

    def get_system_model(self): # real signature unknown; restored from __doc__
        """ get_system_model(self) -> str """
        return ""

    def get_system_vendor(self): # real signature unknown; restored from __doc__
        """ get_system_vendor(self) -> str """
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

    def import_profile(self, file, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ import_profile(self, file:Gio.File, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def import_profile_finish(self, res): # real signature unknown; restored from __doc__
        """ import_profile_finish(self, res:Gio.AsyncResult) -> Colord.Profile """
        pass

    def import_profile_sync(self, file, cancellable=None): # real signature unknown; restored from __doc__
        """ import_profile_sync(self, file:Gio.File, cancellable:Gio.Cancellable=None) -> Colord.Profile """
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
        """ new() -> Colord.Client """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f09131e4fa0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Client), '__module__': 'gi.repository.Colord', '__gtype__': <GType CdClient (94892598804320)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'error_from_string': gi.FunctionInfo(error_from_string), 'error_quark': gi.FunctionInfo(error_quark), 'error_to_string': gi.FunctionInfo(error_to_string), 'connect': gi.FunctionInfo(connect), 'connect_finish': gi.FunctionInfo(connect_finish), 'connect_sync': gi.FunctionInfo(connect_sync), 'create_device': gi.FunctionInfo(create_device), 'create_device_finish': gi.FunctionInfo(create_device_finish), 'create_device_sync': gi.FunctionInfo(create_device_sync), 'create_profile': gi.FunctionInfo(create_profile), 'create_profile_finish': gi.FunctionInfo(create_profile_finish), 'create_profile_for_icc': gi.FunctionInfo(create_profile_for_icc), 'create_profile_for_icc_finish': gi.FunctionInfo(create_profile_for_icc_finish), 'create_profile_for_icc_sync': gi.FunctionInfo(create_profile_for_icc_sync), 'create_profile_sync': gi.FunctionInfo(create_profile_sync), 'delete_device': gi.FunctionInfo(delete_device), 'delete_device_finish': gi.FunctionInfo(delete_device_finish), 'delete_device_sync': gi.FunctionInfo(delete_device_sync), 'delete_profile': gi.FunctionInfo(delete_profile), 'delete_profile_finish': gi.FunctionInfo(delete_profile_finish), 'delete_profile_sync': gi.FunctionInfo(delete_profile_sync), 'find_device': gi.FunctionInfo(find_device), 'find_device_by_property': gi.FunctionInfo(find_device_by_property), 'find_device_by_property_finish': gi.FunctionInfo(find_device_by_property_finish), 'find_device_by_property_sync': gi.FunctionInfo(find_device_by_property_sync), 'find_device_finish': gi.FunctionInfo(find_device_finish), 'find_device_sync': gi.FunctionInfo(find_device_sync), 'find_profile': gi.FunctionInfo(find_profile), 'find_profile_by_filename': gi.FunctionInfo(find_profile_by_filename), 'find_profile_by_filename_finish': gi.FunctionInfo(find_profile_by_filename_finish), 'find_profile_by_filename_sync': gi.FunctionInfo(find_profile_by_filename_sync), 'find_profile_by_property': gi.FunctionInfo(find_profile_by_property), 'find_profile_by_property_finish': gi.FunctionInfo(find_profile_by_property_finish), 'find_profile_by_property_sync': gi.FunctionInfo(find_profile_by_property_sync), 'find_profile_finish': gi.FunctionInfo(find_profile_finish), 'find_profile_sync': gi.FunctionInfo(find_profile_sync), 'find_sensor': gi.FunctionInfo(find_sensor), 'find_sensor_finish': gi.FunctionInfo(find_sensor_finish), 'find_sensor_sync': gi.FunctionInfo(find_sensor_sync), 'get_connected': gi.FunctionInfo(get_connected), 'get_daemon_version': gi.FunctionInfo(get_daemon_version), 'get_devices': gi.FunctionInfo(get_devices), 'get_devices_by_kind': gi.FunctionInfo(get_devices_by_kind), 'get_devices_by_kind_finish': gi.FunctionInfo(get_devices_by_kind_finish), 'get_devices_by_kind_sync': gi.FunctionInfo(get_devices_by_kind_sync), 'get_devices_finish': gi.FunctionInfo(get_devices_finish), 'get_devices_sync': gi.FunctionInfo(get_devices_sync), 'get_has_server': gi.FunctionInfo(get_has_server), 'get_profiles': gi.FunctionInfo(get_profiles), 'get_profiles_finish': gi.FunctionInfo(get_profiles_finish), 'get_profiles_sync': gi.FunctionInfo(get_profiles_sync), 'get_sensors': gi.FunctionInfo(get_sensors), 'get_sensors_finish': gi.FunctionInfo(get_sensors_finish), 'get_sensors_sync': gi.FunctionInfo(get_sensors_sync), 'get_standard_space': gi.FunctionInfo(get_standard_space), 'get_standard_space_finish': gi.FunctionInfo(get_standard_space_finish), 'get_standard_space_sync': gi.FunctionInfo(get_standard_space_sync), 'get_system_model': gi.FunctionInfo(get_system_model), 'get_system_vendor': gi.FunctionInfo(get_system_vendor), 'import_profile': gi.FunctionInfo(import_profile), 'import_profile_finish': gi.FunctionInfo(import_profile_finish), 'import_profile_sync': gi.FunctionInfo(import_profile_sync), 'do_changed': gi.VFuncInfo(changed), 'do_device_added': gi.VFuncInfo(device_added), 'do_device_changed': gi.VFuncInfo(device_changed), 'do_device_removed': gi.VFuncInfo(device_removed), 'do_profile_added': gi.VFuncInfo(profile_added), 'do_profile_changed': gi.VFuncInfo(profile_changed), 'do_profile_removed': gi.VFuncInfo(profile_removed), 'do_sensor_added': gi.VFuncInfo(sensor_added), 'do_sensor_changed': gi.VFuncInfo(sensor_changed), 'do_sensor_removed': gi.VFuncInfo(sensor_removed), 'parent_instance': <property object at 0x7f091336b2c0>})"
    __gdoc__ = 'Object CdClient\n\nSignals from CdClient:\n  device-added (CdDevice)\n  device-removed (CdDevice)\n  device-changed (CdDevice)\n  profile-added (CdProfile)\n  profile-removed (CdProfile)\n  profile-changed (CdProfile)\n  sensor-added (CdSensor)\n  sensor-removed (CdSensor)\n  sensor-changed (CdSensor)\n  changed ()\n\nProperties from CdClient:\n  daemon-version -> gchararray: Daemon version\n  connected -> gchararray: connected\n  system-vendor -> gchararray: System Vendor\n  system-model -> gchararray: System model\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CdClient (94892598804320)>'
    __info__ = ObjectInfo(Client)


