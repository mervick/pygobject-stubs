# encoding: utf-8
# module gi.repository.FwupdPlugin
# from /usr/lib64/girepository-1.0/FwupdPlugin-1.0.typelib
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
import gi.repository.Fwupd as __gi_repository_Fwupd
import gobject as __gobject


class Plugin(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Plugin(**properties)
        new() -> FwupdPlugin.Plugin
    """
    def add_compile_version(self, component_id, version): # real signature unknown; restored from __doc__
        """ add_compile_version(self, component_id:str, version:str) """
        pass

    def add_firmware_gtype(self, id, gtype): # real signature unknown; restored from __doc__
        """ add_firmware_gtype(self, id:str, gtype:GType) """
        pass

    def add_report_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_report_metadata(self, key:str, value:str) """
        pass

    def add_rule(self, rule, name): # real signature unknown; restored from __doc__
        """ add_rule(self, rule:FwupdPlugin.PluginRule, name:str) """
        pass

    def add_runtime_version(self, component_id, version): # real signature unknown; restored from __doc__
        """ add_runtime_version(self, component_id:str, version:str) """
        pass

    def add_udev_subsystem(self, subsystem): # real signature unknown; restored from __doc__
        """ add_udev_subsystem(self, subsystem:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cache_add(self, id, dev=None): # real signature unknown; restored from __doc__
        """ cache_add(self, id:str, dev=None) """
        pass

    def cache_lookup(self, id): # real signature unknown; restored from __doc__
        """ cache_lookup(self, id:str) """
        pass

    def cache_remove(self, id): # real signature unknown; restored from __doc__
        """ cache_remove(self, id:str) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_hwid(self, hwid): # real signature unknown; restored from __doc__
        """ check_hwid(self, hwid:str) -> bool """
        return False

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

    def device_add(self, device): # real signature unknown; restored from __doc__
        """ device_add(self, device:FwupdPlugin.Device) """
        pass

    def device_register(self, device): # real signature unknown; restored from __doc__
        """ device_register(self, device:FwupdPlugin.Device) """
        pass

    def device_remove(self, device): # real signature unknown; restored from __doc__
        """ device_remove(self, device:FwupdPlugin.Device) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add_firmware_gtype(self, *args, **kwargs): # real signature unknown
        """ add_firmware_gtype(self, id:str, gtype:GType) -> bool """
        pass

    def do_check_supported(self, *args, **kwargs): # real signature unknown
        """ check_supported(self, guid:str) -> bool """
        pass

    def do_device_added(self, *args, **kwargs): # real signature unknown
        """ device_added(self, device:FwupdPlugin.Device) """
        pass

    def do_device_register(self, *args, **kwargs): # real signature unknown
        """ device_register(self, device:FwupdPlugin.Device) """
        pass

    def do_device_removed(self, *args, **kwargs): # real signature unknown
        """ device_removed(self, device:FwupdPlugin.Device) """
        pass

    def do_percentage_changed(self, *args, **kwargs): # real signature unknown
        """ percentage_changed(self, percentage:int) """
        pass

    def do_recoldplug(self, *args, **kwargs): # real signature unknown
        """ recoldplug(self) """
        pass

    def do_rules_changed(self, *args, **kwargs): # real signature unknown
        """ rules_changed(self) """
        pass

    def do_set_coldplug_delay(self, *args, **kwargs): # real signature unknown
        """ set_coldplug_delay(self, duration:int) """
        pass

    def do_status_changed(self, *args, **kwargs): # real signature unknown
        """ status_changed(self, status:Fwupd.Status) """
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

    def get_build_hash(self): # real signature unknown; restored from __doc__
        """ get_build_hash(self) -> str """
        return ""

    def get_config_value(self, key): # real signature unknown; restored from __doc__
        """ get_config_value(self, key:str) -> str """
        return ""

    def get_config_value_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_config_value_boolean(self, key:str) -> bool """
        return False

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> FwupdPlugin.PluginData """
        pass

    def get_dmi_value(self, dmi_id): # real signature unknown; restored from __doc__
        """ get_dmi_value(self, dmi_id:str) -> str """
        return ""

    def get_enabled(self): # real signature unknown; restored from __doc__
        """ get_enabled(self) -> bool """
        return False

    def get_hwids(self): # real signature unknown; restored from __doc__
        """ get_hwids(self) -> list """
        return []

    def get_hwid_replace_value(self, keys): # real signature unknown; restored from __doc__
        """ get_hwid_replace_value(self, keys:str) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_order(self): # real signature unknown; restored from __doc__
        """ get_order(self) -> int """
        return 0

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_quirks(self): # real signature unknown; restored from __doc__
        """ get_quirks(self) -> FwupdPlugin.Quirks """
        pass

    def get_report_metadata(self): # real signature unknown; restored from __doc__
        """ get_report_metadata(self) -> dict """
        return {}

    def get_rules(self, rule): # real signature unknown; restored from __doc__
        """ get_rules(self, rule:FwupdPlugin.PluginRule) -> list """
        return []

    def get_smbios_data(self, structure_type): # real signature unknown; restored from __doc__
        """ get_smbios_data(self, structure_type:int) -> GLib.Bytes """
        pass

    def get_smbios_string(self, structure_type, offset): # real signature unknown; restored from __doc__
        """ get_smbios_string(self, structure_type:int, offset:int) -> str """
        return ""

    def get_usb_context(self): # real signature unknown; restored from __doc__
        """ get_usb_context(self) -> GUsb.Context """
        pass

    def guess_name_from_fn(self, filename): # real signature unknown; restored from __doc__
        """ guess_name_from_fn(filename:str) -> str """
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

    def has_custom_flag(self, flag): # real signature unknown; restored from __doc__
        """ has_custom_flag(self, flag:str) -> bool """
        return False

    def has_rule(self, rule, name): # real signature unknown; restored from __doc__
        """ has_rule(self, rule:FwupdPlugin.PluginRule, name:str) -> bool """
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

    def is_open(self): # real signature unknown; restored from __doc__
        """ is_open(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lookup_quirk_by_id(self, group, key): # real signature unknown; restored from __doc__
        """ lookup_quirk_by_id(self, group:str, key:str) -> str """
        return ""

    def lookup_quirk_by_id_as_uint64(self, group, key): # real signature unknown; restored from __doc__
        """ lookup_quirk_by_id_as_uint64(self, group:str, key:str) -> int """
        return 0

    def name_compare(self, plugin2): # real signature unknown; restored from __doc__
        """ name_compare(self, plugin2:FwupdPlugin.Plugin) -> int """
        return 0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> FwupdPlugin.Plugin """
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

    def open(self, filename): # real signature unknown; restored from __doc__
        """ open(self, filename:str) -> bool """
        return False

    def order_compare(self, plugin2): # real signature unknown; restored from __doc__
        """ order_compare(self, plugin2:FwupdPlugin.Plugin) -> int """
        return 0

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

    def request_recoldplug(self): # real signature unknown; restored from __doc__
        """ request_recoldplug(self) """
        pass

    def runner_activate(self, device): # real signature unknown; restored from __doc__
        """ runner_activate(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_clear_results(self, device): # real signature unknown; restored from __doc__
        """ runner_clear_results(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_coldplug(self): # real signature unknown; restored from __doc__
        """ runner_coldplug(self) -> bool """
        return False

    def runner_coldplug_cleanup(self): # real signature unknown; restored from __doc__
        """ runner_coldplug_cleanup(self) -> bool """
        return False

    def runner_coldplug_prepare(self): # real signature unknown; restored from __doc__
        """ runner_coldplug_prepare(self) -> bool """
        return False

    def runner_composite_cleanup(self, devices): # real signature unknown; restored from __doc__
        """ runner_composite_cleanup(self, devices:list) -> bool """
        return False

    def runner_composite_prepare(self, devices): # real signature unknown; restored from __doc__
        """ runner_composite_prepare(self, devices:list) -> bool """
        return False

    def runner_device_created(self, device): # real signature unknown; restored from __doc__
        """ runner_device_created(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_device_register(self, device): # real signature unknown; restored from __doc__
        """ runner_device_register(self, device:FwupdPlugin.Device) """
        pass

    def runner_device_removed(self, device): # real signature unknown; restored from __doc__
        """ runner_device_removed(self, device:FwupdPlugin.Device) """
        pass

    def runner_get_results(self, device): # real signature unknown; restored from __doc__
        """ runner_get_results(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_recoldplug(self): # real signature unknown; restored from __doc__
        """ runner_recoldplug(self) -> bool """
        return False

    def runner_startup(self): # real signature unknown; restored from __doc__
        """ runner_startup(self) -> bool """
        return False

    def runner_udev_device_added(self, device): # real signature unknown; restored from __doc__
        """ runner_udev_device_added(self, device:FwupdPlugin.UdevDevice) -> bool """
        return False

    def runner_udev_device_changed(self, device): # real signature unknown; restored from __doc__
        """ runner_udev_device_changed(self, device:FwupdPlugin.UdevDevice) -> bool """
        return False

    def runner_unlock(self, device): # real signature unknown; restored from __doc__
        """ runner_unlock(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_update(self, device, blob_fw, flags): # real signature unknown; restored from __doc__
        """ runner_update(self, device:FwupdPlugin.Device, blob_fw:GLib.Bytes, flags:Fwupd.InstallFlags) -> bool """
        return False

    def runner_update_attach(self, device): # real signature unknown; restored from __doc__
        """ runner_update_attach(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_update_cleanup(self, flags, device): # real signature unknown; restored from __doc__
        """ runner_update_cleanup(self, flags:Fwupd.InstallFlags, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_update_detach(self, device): # real signature unknown; restored from __doc__
        """ runner_update_detach(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_update_prepare(self, flags, device): # real signature unknown; restored from __doc__
        """ runner_update_prepare(self, flags:Fwupd.InstallFlags, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_update_reload(self, device): # real signature unknown; restored from __doc__
        """ runner_update_reload(self, device:FwupdPlugin.Device) -> bool """
        return False

    def runner_usb_device_added(self, device): # real signature unknown; restored from __doc__
        """ runner_usb_device_added(self, device:FwupdPlugin.UsbDevice) -> bool """
        return False

    def runner_verify(self, device, flags): # real signature unknown; restored from __doc__
        """ runner_verify(self, device:FwupdPlugin.Device, flags:FwupdPlugin.PluginVerifyFlags) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_build_hash(self, build_hash): # real signature unknown; restored from __doc__
        """ set_build_hash(self, build_hash:str) """
        pass

    def set_coldplug_delay(self, duration): # real signature unknown; restored from __doc__
        """ set_coldplug_delay(self, duration:int) """
        pass

    def set_compile_versions(self, compile_versions): # real signature unknown; restored from __doc__
        """ set_compile_versions(self, compile_versions:dict) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_device_gtype(self, device_gtype): # real signature unknown; restored from __doc__
        """ set_device_gtype(self, device_gtype:GType) """
        pass

    def set_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_enabled(self, enabled:bool) """
        pass

    def set_hwids(self, hwids): # real signature unknown; restored from __doc__
        """ set_hwids(self, hwids:FwupdPlugin.Hwids) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_order(self, order): # real signature unknown; restored from __doc__
        """ set_order(self, order:int) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_quirks(self, quirks): # real signature unknown; restored from __doc__
        """ set_quirks(self, quirks:FwupdPlugin.Quirks) """
        pass

    def set_runtime_versions(self, runtime_versions): # real signature unknown; restored from __doc__
        """ set_runtime_versions(self, runtime_versions:dict) """
        pass

    def set_smbios(self, smbios): # real signature unknown; restored from __doc__
        """ set_smbios(self, smbios:FwupdPlugin.Smbios) """
        pass

    def set_udev_subsystems(self, udev_subsystems): # real signature unknown; restored from __doc__
        """ set_udev_subsystems(self, udev_subsystems:list) """
        pass

    def set_usb_context(self, usb_ctx): # real signature unknown; restored from __doc__
        """ set_usb_context(self, usb_ctx:GUsb.Context) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7feb1a362d60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Plugin), '__module__': 'gi.repository.FwupdPlugin', '__gtype__': <GType void (4)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'guess_name_from_fn': gi.FunctionInfo(guess_name_from_fn), 'add_compile_version': gi.FunctionInfo(add_compile_version), 'add_firmware_gtype': gi.FunctionInfo(add_firmware_gtype), 'add_report_metadata': gi.FunctionInfo(add_report_metadata), 'add_rule': gi.FunctionInfo(add_rule), 'add_runtime_version': gi.FunctionInfo(add_runtime_version), 'add_udev_subsystem': gi.FunctionInfo(add_udev_subsystem), 'cache_add': gi.FunctionInfo(cache_add), 'cache_lookup': gi.FunctionInfo(cache_lookup), 'cache_remove': gi.FunctionInfo(cache_remove), 'check_hwid': gi.FunctionInfo(check_hwid), 'device_add': gi.FunctionInfo(device_add), 'device_register': gi.FunctionInfo(device_register), 'device_remove': gi.FunctionInfo(device_remove), 'get_build_hash': gi.FunctionInfo(get_build_hash), 'get_config_value': gi.FunctionInfo(get_config_value), 'get_config_value_boolean': gi.FunctionInfo(get_config_value_boolean), 'get_data': gi.FunctionInfo(get_data), 'get_dmi_value': gi.FunctionInfo(get_dmi_value), 'get_enabled': gi.FunctionInfo(get_enabled), 'get_hwid_replace_value': gi.FunctionInfo(get_hwid_replace_value), 'get_hwids': gi.FunctionInfo(get_hwids), 'get_name': gi.FunctionInfo(get_name), 'get_order': gi.FunctionInfo(get_order), 'get_priority': gi.FunctionInfo(get_priority), 'get_quirks': gi.FunctionInfo(get_quirks), 'get_report_metadata': gi.FunctionInfo(get_report_metadata), 'get_rules': gi.FunctionInfo(get_rules), 'get_smbios_data': gi.FunctionInfo(get_smbios_data), 'get_smbios_string': gi.FunctionInfo(get_smbios_string), 'get_usb_context': gi.FunctionInfo(get_usb_context), 'has_custom_flag': gi.FunctionInfo(has_custom_flag), 'has_rule': gi.FunctionInfo(has_rule), 'is_open': gi.FunctionInfo(is_open), 'lookup_quirk_by_id': gi.FunctionInfo(lookup_quirk_by_id), 'lookup_quirk_by_id_as_uint64': gi.FunctionInfo(lookup_quirk_by_id_as_uint64), 'name_compare': gi.FunctionInfo(name_compare), 'open': gi.FunctionInfo(open), 'order_compare': gi.FunctionInfo(order_compare), 'request_recoldplug': gi.FunctionInfo(request_recoldplug), 'runner_activate': gi.FunctionInfo(runner_activate), 'runner_clear_results': gi.FunctionInfo(runner_clear_results), 'runner_coldplug': gi.FunctionInfo(runner_coldplug), 'runner_coldplug_cleanup': gi.FunctionInfo(runner_coldplug_cleanup), 'runner_coldplug_prepare': gi.FunctionInfo(runner_coldplug_prepare), 'runner_composite_cleanup': gi.FunctionInfo(runner_composite_cleanup), 'runner_composite_prepare': gi.FunctionInfo(runner_composite_prepare), 'runner_device_created': gi.FunctionInfo(runner_device_created), 'runner_device_register': gi.FunctionInfo(runner_device_register), 'runner_device_removed': gi.FunctionInfo(runner_device_removed), 'runner_get_results': gi.FunctionInfo(runner_get_results), 'runner_recoldplug': gi.FunctionInfo(runner_recoldplug), 'runner_startup': gi.FunctionInfo(runner_startup), 'runner_udev_device_added': gi.FunctionInfo(runner_udev_device_added), 'runner_udev_device_changed': gi.FunctionInfo(runner_udev_device_changed), 'runner_unlock': gi.FunctionInfo(runner_unlock), 'runner_update': gi.FunctionInfo(runner_update), 'runner_update_attach': gi.FunctionInfo(runner_update_attach), 'runner_update_cleanup': gi.FunctionInfo(runner_update_cleanup), 'runner_update_detach': gi.FunctionInfo(runner_update_detach), 'runner_update_prepare': gi.FunctionInfo(runner_update_prepare), 'runner_update_reload': gi.FunctionInfo(runner_update_reload), 'runner_usb_device_added': gi.FunctionInfo(runner_usb_device_added), 'runner_verify': gi.FunctionInfo(runner_verify), 'set_build_hash': gi.FunctionInfo(set_build_hash), 'set_coldplug_delay': gi.FunctionInfo(set_coldplug_delay), 'set_compile_versions': gi.FunctionInfo(set_compile_versions), 'set_device_gtype': gi.FunctionInfo(set_device_gtype), 'set_enabled': gi.FunctionInfo(set_enabled), 'set_hwids': gi.FunctionInfo(set_hwids), 'set_name': gi.FunctionInfo(set_name), 'set_order': gi.FunctionInfo(set_order), 'set_priority': gi.FunctionInfo(set_priority), 'set_quirks': gi.FunctionInfo(set_quirks), 'set_runtime_versions': gi.FunctionInfo(set_runtime_versions), 'set_smbios': gi.FunctionInfo(set_smbios), 'set_udev_subsystems': gi.FunctionInfo(set_udev_subsystems), 'set_usb_context': gi.FunctionInfo(set_usb_context), 'do_add_firmware_gtype': gi.VFuncInfo(add_firmware_gtype), 'do_check_supported': gi.VFuncInfo(check_supported), 'do_device_added': gi.VFuncInfo(device_added), 'do_device_register': gi.VFuncInfo(device_register), 'do_device_removed': gi.VFuncInfo(device_removed), 'do_percentage_changed': gi.VFuncInfo(percentage_changed), 'do_recoldplug': gi.VFuncInfo(recoldplug), 'do_rules_changed': gi.VFuncInfo(rules_changed), 'do_set_coldplug_delay': gi.VFuncInfo(set_coldplug_delay), 'do_status_changed': gi.VFuncInfo(status_changed), 'parent_instance': <property object at 0x7feb1a35bb80>})"
    __gdoc__ = 'void\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = ObjectInfo(Plugin)


