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


class Device(__gi_repository_Fwupd.Device):
    """
    :Constructors:
    
    ::
    
        Device(**properties)
        new() -> FwupdPlugin.Device
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def add_checksum(self, checksum): # real signature unknown; restored from __doc__
        """ add_checksum(self, checksum:str) """
        pass

    def add_child(self, child): # real signature unknown; restored from __doc__
        """ add_child(self, child:FwupdPlugin.Device) """
        pass

    def add_counterpart_guid(self, guid): # real signature unknown; restored from __doc__
        """ add_counterpart_guid(self, guid:str) """
        pass

    def add_flag(self, flag): # real signature unknown; restored from __doc__
        """ add_flag(self, flag:int) """
        pass

    def add_guid(self, guid): # real signature unknown; restored from __doc__
        """ add_guid(self, guid:str) """
        pass

    def add_icon(self, icon): # real signature unknown; restored from __doc__
        """ add_icon(self, icon:str) """
        pass

    def add_instance_id(self, instance_id): # real signature unknown; restored from __doc__
        """ add_instance_id(self, instance_id:str) """
        pass

    def add_instance_id_full(self, instance_id, flags): # real signature unknown; restored from __doc__
        """ add_instance_id_full(self, instance_id:str, flags:FwupdPlugin.DeviceInstanceFlags) """
        pass

    def add_parent_guid(self, guid): # real signature unknown; restored from __doc__
        """ add_parent_guid(self, guid:str) """
        pass

    def add_release(self, release): # real signature unknown; restored from __doc__
        """ add_release(self, release:Fwupd.Release) """
        pass

    def array_ensure_parents(self, devices): # real signature unknown; restored from __doc__
        """ array_ensure_parents(devices:list) """
        pass

    def array_from_variant(self, value): # real signature unknown; restored from __doc__
        """ array_from_variant(value:GLib.Variant) -> list """
        return []

    def attach(self): # real signature unknown; restored from __doc__
        """ attach(self) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def cleanup(self, flags): # real signature unknown; restored from __doc__
        """ cleanup(self, flags:Fwupd.InstallFlags) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def compare(self, device2): # real signature unknown; restored from __doc__
        """ compare(self, device2:Fwupd.Device) -> int """
        return 0

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

    def convert_instance_ids(self): # real signature unknown; restored from __doc__
        """ convert_instance_ids(self) """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) -> bool """
        pass

    def do_attach(self, *args, **kwargs): # real signature unknown
        """ attach(self) -> bool """
        pass

    def do_cleanup(self, *args, **kwargs): # real signature unknown
        """ cleanup(self, flags:Fwupd.InstallFlags) -> bool """
        pass

    def do_close(self, *args, **kwargs): # real signature unknown
        """ close(self) -> bool """
        pass

    def do_detach(self, *args, **kwargs): # real signature unknown
        """ detach(self) -> bool """
        pass

    def do_incorporate(self, *args, **kwargs): # real signature unknown
        """ incorporate(self, donor:FwupdPlugin.Device) """
        pass

    def do_open(self, *args, **kwargs): # real signature unknown
        """ open(self) -> bool """
        pass

    def do_poll(self, *args, **kwargs): # real signature unknown
        """ poll(self) -> bool """
        pass

    def do_prepare(self, *args, **kwargs): # real signature unknown
        """ prepare(self, flags:Fwupd.InstallFlags) -> bool """
        pass

    def do_prepare_firmware(self, *args, **kwargs): # real signature unknown
        """ prepare_firmware(self, fw:GLib.Bytes, flags:Fwupd.InstallFlags) -> FwupdPlugin.Firmware """
        pass

    def do_probe(self, *args, **kwargs): # real signature unknown
        """ probe(self) -> bool """
        pass

    def do_read_firmware(self, *args, **kwargs): # real signature unknown
        """ read_firmware(self) -> FwupdPlugin.Firmware """
        pass

    def do_reload(self, *args, **kwargs): # real signature unknown
        """ reload(self) -> bool """
        pass

    def do_rescan(self, *args, **kwargs): # real signature unknown
        """ rescan(self) -> bool """
        pass

    def do_setup(self, *args, **kwargs): # real signature unknown
        """ setup(self) -> bool """
        pass

    def do_set_quirk_kv(self, *args, **kwargs): # real signature unknown
        """ set_quirk_kv(self, key:str, value:str) -> bool """
        pass

    def do_to_string(self, *args, **kwargs): # real signature unknown
        """ to_string(self, indent:int, str:GLib.String) """
        pass

    def do_write_firmware(self, *args, **kwargs): # real signature unknown
        """ write_firmware(self, firmware:FwupdPlugin.Firmware, flags:Fwupd.InstallFlags) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_id(self): # real signature unknown; restored from __doc__
        """ ensure_id(self) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flag_from_string(self, device_flag): # real signature unknown; restored from __doc__
        """ flag_from_string(device_flag:str) -> int """
        return 0

    def flag_to_string(self, device_flag): # real signature unknown; restored from __doc__
        """ flag_to_string(device_flag:int) -> str """
        return ""

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

    def from_variant(self, value): # real signature unknown; restored from __doc__
        """ from_variant(value:GLib.Variant) -> Fwupd.Device """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_alternate(self): # real signature unknown; restored from __doc__
        """ get_alternate(self) -> FwupdPlugin.Device """
        pass

    def get_alternate_id(self): # real signature unknown; restored from __doc__
        """ get_alternate_id(self) -> str """
        return ""

    def get_checksums(self): # real signature unknown; restored from __doc__
        """ get_checksums(self) -> list """
        return []

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> int """
        return 0

    def get_custom_flags(self): # real signature unknown; restored from __doc__
        """ get_custom_flags(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_equivalent_id(self): # real signature unknown; restored from __doc__
        """ get_equivalent_id(self) -> str """
        return ""

    def get_firmware_size_max(self): # real signature unknown; restored from __doc__
        """ get_firmware_size_max(self) -> int """
        return 0

    def get_firmware_size_min(self): # real signature unknown; restored from __doc__
        """ get_firmware_size_min(self) -> int """
        return 0

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_flashes_left(self): # real signature unknown; restored from __doc__
        """ get_flashes_left(self) -> int """
        return 0

    def get_guids(self): # real signature unknown; restored from __doc__
        """ get_guids(self) -> list """
        return []

    def get_guids_as_str(self): # real signature unknown; restored from __doc__
        """ get_guids_as_str(self) -> str """
        return ""

    def get_guid_default(self): # real signature unknown; restored from __doc__
        """ get_guid_default(self) -> str """
        return ""

    def get_icons(self): # real signature unknown; restored from __doc__
        """ get_icons(self) -> list """
        return []

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_install_duration(self): # real signature unknown; restored from __doc__
        """ get_install_duration(self) -> int """
        return 0

    def get_instance_ids(self): # real signature unknown; restored from __doc__
        """ get_instance_ids(self) -> list """
        return []

    def get_logical_id(self): # real signature unknown; restored from __doc__
        """ get_logical_id(self) -> str """
        return ""

    def get_metadata(self, key): # real signature unknown; restored from __doc__
        """ get_metadata(self, key:str) -> str """
        return ""

    def get_metadata_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_metadata_boolean(self, key:str) -> bool """
        return False

    def get_metadata_integer(self, key): # real signature unknown; restored from __doc__
        """ get_metadata_integer(self, key:str) -> int """
        return 0

    def get_modified(self): # real signature unknown; restored from __doc__
        """ get_modified(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_order(self): # real signature unknown; restored from __doc__
        """ get_order(self) -> int """
        return 0

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> FwupdPlugin.Device """
        pass

    def get_parent_guids(self): # real signature unknown; restored from __doc__
        """ get_parent_guids(self) -> list """
        return []

    def get_parent_id(self): # real signature unknown; restored from __doc__
        """ get_parent_id(self) -> str """
        return ""

    def get_physical_id(self): # real signature unknown; restored from __doc__
        """ get_physical_id(self) -> str """
        return ""

    def get_plugin(self): # real signature unknown; restored from __doc__
        """ get_plugin(self) -> str """
        return ""

    def get_possible_plugins(self): # real signature unknown; restored from __doc__
        """ get_possible_plugins(self) -> list """
        return []

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_progress(self): # real signature unknown; restored from __doc__
        """ get_progress(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> str """
        return ""

    def get_proxy(self): # real signature unknown; restored from __doc__
        """ get_proxy(self) -> FwupdPlugin.Device """
        pass

    def get_proxy_guid(self): # real signature unknown; restored from __doc__
        """ get_proxy_guid(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_quirks(self): # real signature unknown; restored from __doc__
        """ get_quirks(self) -> FwupdPlugin.Quirks """
        pass

    def get_releases(self): # real signature unknown; restored from __doc__
        """ get_releases(self) -> list """
        return []

    def get_release_default(self): # real signature unknown; restored from __doc__
        """ get_release_default(self) -> Fwupd.Release """
        pass

    def get_remove_delay(self): # real signature unknown; restored from __doc__
        """ get_remove_delay(self) -> int """
        return 0

    def get_root(self): # real signature unknown; restored from __doc__
        """ get_root(self) -> FwupdPlugin.Device """
        pass

    def get_serial(self): # real signature unknown; restored from __doc__
        """ get_serial(self) -> str """
        return ""

    def get_specialized_gtype(self): # real signature unknown; restored from __doc__
        """ get_specialized_gtype(self) -> GType """
        pass

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> Fwupd.Status """
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_update_error(self): # real signature unknown; restored from __doc__
        """ get_update_error(self) -> str """
        return ""

    def get_update_message(self): # real signature unknown; restored from __doc__
        """ get_update_message(self) -> str """
        return ""

    def get_update_state(self): # real signature unknown; restored from __doc__
        """ get_update_state(self) -> Fwupd.UpdateState """
        pass

    def get_vendor(self): # real signature unknown; restored from __doc__
        """ get_vendor(self) -> str """
        return ""

    def get_vendor_id(self): # real signature unknown; restored from __doc__
        """ get_vendor_id(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
        return ""

    def get_version_bootloader(self): # real signature unknown; restored from __doc__
        """ get_version_bootloader(self) -> str """
        return ""

    def get_version_bootloader_raw(self): # real signature unknown; restored from __doc__
        """ get_version_bootloader_raw(self) -> int """
        return 0

    def get_version_format(self): # real signature unknown; restored from __doc__
        """ get_version_format(self) -> Fwupd.VersionFormat """
        pass

    def get_version_lowest(self): # real signature unknown; restored from __doc__
        """ get_version_lowest(self) -> str """
        return ""

    def get_version_lowest_raw(self): # real signature unknown; restored from __doc__
        """ get_version_lowest_raw(self) -> int """
        return 0

    def get_version_raw(self): # real signature unknown; restored from __doc__
        """ get_version_raw(self) -> int """
        return 0

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

    def has_custom_flag(self, hint): # real signature unknown; restored from __doc__
        """ has_custom_flag(self, hint:str) -> bool """
        return False

    def has_flag(self, flag): # real signature unknown; restored from __doc__
        """ has_flag(self, flag:int) -> bool """
        return False

    def has_guid(self, guid): # real signature unknown; restored from __doc__
        """ has_guid(self, guid:str) -> bool """
        return False

    def has_instance_id(self, instance_id): # real signature unknown; restored from __doc__
        """ has_instance_id(self, instance_id:str) -> bool """
        return False

    def has_parent_guid(self, guid): # real signature unknown; restored from __doc__
        """ has_parent_guid(self, guid:str) -> bool """
        return False

    def id_is_valid(self, device_id): # real signature unknown; restored from __doc__
        """ id_is_valid(device_id:str) -> bool """
        return False

    def incorporate(self, donor): # real signature unknown; restored from __doc__
        """ incorporate(self, donor:FwupdPlugin.Device) """
        pass

    def incorporate_flag(self, donor, flag): # real signature unknown; restored from __doc__
        """ incorporate_flag(self, donor:FwupdPlugin.Device, flag:int) """
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
        """ new() -> FwupdPlugin.Device """
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

    def open(self): # real signature unknown; restored from __doc__
        """ open(self) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def poll(self): # real signature unknown; restored from __doc__
        """ poll(self) -> bool """
        return False

    def prepare(self, flags): # real signature unknown; restored from __doc__
        """ prepare(self, flags:Fwupd.InstallFlags) -> bool """
        return False

    def prepare_firmware(self, fw, flags): # real signature unknown; restored from __doc__
        """ prepare_firmware(self, fw:GLib.Bytes, flags:Fwupd.InstallFlags) -> FwupdPlugin.Firmware """
        pass

    def probe(self): # real signature unknown; restored from __doc__
        """ probe(self) -> bool """
        return False

    def probe_invalidate(self): # real signature unknown; restored from __doc__
        """ probe_invalidate(self) """
        pass

    def read_firmware(self): # real signature unknown; restored from __doc__
        """ read_firmware(self) -> FwupdPlugin.Firmware """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reload(self): # real signature unknown; restored from __doc__
        """ reload(self) -> bool """
        return False

    def remove_flag(self, flag): # real signature unknown; restored from __doc__
        """ remove_flag(self, flag:int) """
        pass

    def remove_metadata(self, key): # real signature unknown; restored from __doc__
        """ remove_metadata(self, key:str) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def rescan(self): # real signature unknown; restored from __doc__
        """ rescan(self) -> bool """
        return False

    def retry(self, func, count, user_data=None): # real signature unknown; restored from __doc__
        """ retry(self, func:FwupdPlugin.DeviceRetryFunc, count:int, user_data=None) -> bool """
        return False

    def retry_add_recovery(self, domain, code, func=None): # real signature unknown; restored from __doc__
        """ retry_add_recovery(self, domain:int, code:int, func:FwupdPlugin.DeviceRetryFunc=None) """
        pass

    def retry_set_delay(self, delay): # real signature unknown; restored from __doc__
        """ retry_set_delay(self, delay:int) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def setup(self): # real signature unknown; restored from __doc__
        """ setup(self) -> bool """
        return False

    def set_alternate(self, alternate): # real signature unknown; restored from __doc__
        """ set_alternate(self, alternate:FwupdPlugin.Device) """
        pass

    def set_alternate_id(self, alternate_id): # real signature unknown; restored from __doc__
        """ set_alternate_id(self, alternate_id:str) """
        pass

    def set_created(self, created): # real signature unknown; restored from __doc__
        """ set_created(self, created:int) """
        pass

    def set_custom_flags(self, custom_flags): # real signature unknown; restored from __doc__
        """ set_custom_flags(self, custom_flags:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_equivalent_id(self, equivalent_id): # real signature unknown; restored from __doc__
        """ set_equivalent_id(self, equivalent_id:str) """
        pass

    def set_firmware_size(self, size): # real signature unknown; restored from __doc__
        """ set_firmware_size(self, size:int) """
        pass

    def set_firmware_size_max(self, size_max): # real signature unknown; restored from __doc__
        """ set_firmware_size_max(self, size_max:int) """
        pass

    def set_firmware_size_min(self, size_min): # real signature unknown; restored from __doc__
        """ set_firmware_size_min(self, size_min:int) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:int) """
        pass

    def set_flashes_left(self, flashes_left): # real signature unknown; restored from __doc__
        """ set_flashes_left(self, flashes_left:int) """
        pass

    def set_id(self, id): # real signature unknown; restored from __doc__
        """ set_id(self, id:str) """
        pass

    def set_install_duration(self, duration): # real signature unknown; restored from __doc__
        """ set_install_duration(self, duration:int) """
        pass

    def set_logical_id(self, logical_id): # real signature unknown; restored from __doc__
        """ set_logical_id(self, logical_id:str) """
        pass

    def set_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ set_metadata(self, key:str, value:str) """
        pass

    def set_metadata_boolean(self, key, value): # real signature unknown; restored from __doc__
        """ set_metadata_boolean(self, key:str, value:bool) """
        pass

    def set_metadata_integer(self, key, value): # real signature unknown; restored from __doc__
        """ set_metadata_integer(self, key:str, value:int) """
        pass

    def set_modified(self, modified): # real signature unknown; restored from __doc__
        """ set_modified(self, modified:int) """
        pass

    def set_name(self, value): # real signature unknown; restored from __doc__
        """ set_name(self, value:str) """
        pass

    def set_order(self, order): # real signature unknown; restored from __doc__
        """ set_order(self, order:int) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:FwupdPlugin.Device) """
        pass

    def set_parent_id(self, parent_id): # real signature unknown; restored from __doc__
        """ set_parent_id(self, parent_id:str) """
        pass

    def set_physical_id(self, physical_id): # real signature unknown; restored from __doc__
        """ set_physical_id(self, physical_id:str) """
        pass

    def set_plugin(self, plugin): # real signature unknown; restored from __doc__
        """ set_plugin(self, plugin:str) """
        pass

    def set_poll_interval(self, interval): # real signature unknown; restored from __doc__
        """ set_poll_interval(self, interval:int) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_progress(self, progress): # real signature unknown; restored from __doc__
        """ set_progress(self, progress:int) """
        pass

    def set_progress_full(self, progress_done, progress_total): # real signature unknown; restored from __doc__
        """ set_progress_full(self, progress_done:int, progress_total:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ set_protocol(self, protocol:str) """
        pass

    def set_proxy(self, proxy): # real signature unknown; restored from __doc__
        """ set_proxy(self, proxy:FwupdPlugin.Device) """
        pass

    def set_proxy_guid(self, proxy_guid): # real signature unknown; restored from __doc__
        """ set_proxy_guid(self, proxy_guid:str) """
        pass

    def set_quirks(self, quirks): # real signature unknown; restored from __doc__
        """ set_quirks(self, quirks:FwupdPlugin.Quirks) """
        pass

    def set_remove_delay(self, remove_delay): # real signature unknown; restored from __doc__
        """ set_remove_delay(self, remove_delay:int) """
        pass

    def set_serial(self, serial): # real signature unknown; restored from __doc__
        """ set_serial(self, serial:str) """
        pass

    def set_status(self, status): # real signature unknown; restored from __doc__
        """ set_status(self, status:Fwupd.Status) """
        pass

    def set_summary(self, summary): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str) """
        pass

    def set_update_error(self, update_error): # real signature unknown; restored from __doc__
        """ set_update_error(self, update_error:str) """
        pass

    def set_update_message(self, update_message): # real signature unknown; restored from __doc__
        """ set_update_message(self, update_message:str) """
        pass

    def set_update_state(self, update_state): # real signature unknown; restored from __doc__
        """ set_update_state(self, update_state:Fwupd.UpdateState) """
        pass

    def set_vendor(self, vendor): # real signature unknown; restored from __doc__
        """ set_vendor(self, vendor:str) """
        pass

    def set_vendor_id(self, vendor_id): # real signature unknown; restored from __doc__
        """ set_vendor_id(self, vendor_id:str) """
        pass

    def set_version(self, version=None): # real signature unknown; restored from __doc__
        """ set_version(self, version:str=None) """
        pass

    def set_version_bootloader(self, version=None): # real signature unknown; restored from __doc__
        """ set_version_bootloader(self, version:str=None) """
        pass

    def set_version_bootloader_raw(self, version_bootloader_raw): # real signature unknown; restored from __doc__
        """ set_version_bootloader_raw(self, version_bootloader_raw:int) """
        pass

    def set_version_format(self, fmt): # real signature unknown; restored from __doc__
        """ set_version_format(self, fmt:Fwupd.VersionFormat) """
        pass

    def set_version_lowest(self, version=None): # real signature unknown; restored from __doc__
        """ set_version_lowest(self, version:str=None) """
        pass

    def set_version_lowest_raw(self, version_lowest_raw): # real signature unknown; restored from __doc__
        """ set_version_lowest_raw(self, version_lowest_raw:int) """
        pass

    def set_version_raw(self, version_raw): # real signature unknown; restored from __doc__
        """ set_version_raw(self, version_raw:int) """
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

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def to_variant(self): # real signature unknown; restored from __doc__
        """ to_variant(self) -> GLib.Variant """
        pass

    def to_variant_full(self, flags): # real signature unknown; restored from __doc__
        """ to_variant_full(self, flags:int) -> GLib.Variant """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write_firmware(self, fw, flags): # real signature unknown; restored from __doc__
        """ write_firmware(self, fw:GLib.Bytes, flags:Fwupd.InstallFlags) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7feb1a3625b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Device), '__module__': 'gi.repository.FwupdPlugin', '__gtype__': <GType void (4)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'activate': gi.FunctionInfo(activate), 'add_child': gi.FunctionInfo(add_child), 'add_counterpart_guid': gi.FunctionInfo(add_counterpart_guid), 'add_flag': gi.FunctionInfo(add_flag), 'add_guid': gi.FunctionInfo(add_guid), 'add_instance_id': gi.FunctionInfo(add_instance_id), 'add_instance_id_full': gi.FunctionInfo(add_instance_id_full), 'add_parent_guid': gi.FunctionInfo(add_parent_guid), 'attach': gi.FunctionInfo(attach), 'cleanup': gi.FunctionInfo(cleanup), 'close': gi.FunctionInfo(close), 'convert_instance_ids': gi.FunctionInfo(convert_instance_ids), 'detach': gi.FunctionInfo(detach), 'ensure_id': gi.FunctionInfo(ensure_id), 'get_alternate': gi.FunctionInfo(get_alternate), 'get_alternate_id': gi.FunctionInfo(get_alternate_id), 'get_children': gi.FunctionInfo(get_children), 'get_custom_flags': gi.FunctionInfo(get_custom_flags), 'get_equivalent_id': gi.FunctionInfo(get_equivalent_id), 'get_firmware_size_max': gi.FunctionInfo(get_firmware_size_max), 'get_firmware_size_min': gi.FunctionInfo(get_firmware_size_min), 'get_guids_as_str': gi.FunctionInfo(get_guids_as_str), 'get_logical_id': gi.FunctionInfo(get_logical_id), 'get_metadata': gi.FunctionInfo(get_metadata), 'get_metadata_boolean': gi.FunctionInfo(get_metadata_boolean), 'get_metadata_integer': gi.FunctionInfo(get_metadata_integer), 'get_order': gi.FunctionInfo(get_order), 'get_parent': gi.FunctionInfo(get_parent), 'get_parent_guids': gi.FunctionInfo(get_parent_guids), 'get_physical_id': gi.FunctionInfo(get_physical_id), 'get_possible_plugins': gi.FunctionInfo(get_possible_plugins), 'get_priority': gi.FunctionInfo(get_priority), 'get_progress': gi.FunctionInfo(get_progress), 'get_protocol': gi.FunctionInfo(get_protocol), 'get_proxy': gi.FunctionInfo(get_proxy), 'get_proxy_guid': gi.FunctionInfo(get_proxy_guid), 'get_quirks': gi.FunctionInfo(get_quirks), 'get_release_default': gi.FunctionInfo(get_release_default), 'get_remove_delay': gi.FunctionInfo(get_remove_delay), 'get_root': gi.FunctionInfo(get_root), 'get_specialized_gtype': gi.FunctionInfo(get_specialized_gtype), 'get_status': gi.FunctionInfo(get_status), 'has_custom_flag': gi.FunctionInfo(has_custom_flag), 'has_guid': gi.FunctionInfo(has_guid), 'has_parent_guid': gi.FunctionInfo(has_parent_guid), 'incorporate': gi.FunctionInfo(incorporate), 'incorporate_flag': gi.FunctionInfo(incorporate_flag), 'open': gi.FunctionInfo(open), 'poll': gi.FunctionInfo(poll), 'prepare': gi.FunctionInfo(prepare), 'prepare_firmware': gi.FunctionInfo(prepare_firmware), 'probe': gi.FunctionInfo(probe), 'probe_invalidate': gi.FunctionInfo(probe_invalidate), 'read_firmware': gi.FunctionInfo(read_firmware), 'reload': gi.FunctionInfo(reload), 'remove_metadata': gi.FunctionInfo(remove_metadata), 'rescan': gi.FunctionInfo(rescan), 'retry': gi.FunctionInfo(retry), 'retry_add_recovery': gi.FunctionInfo(retry_add_recovery), 'retry_set_delay': gi.FunctionInfo(retry_set_delay), 'set_alternate': gi.FunctionInfo(set_alternate), 'set_alternate_id': gi.FunctionInfo(set_alternate_id), 'set_custom_flags': gi.FunctionInfo(set_custom_flags), 'set_equivalent_id': gi.FunctionInfo(set_equivalent_id), 'set_firmware_size': gi.FunctionInfo(set_firmware_size), 'set_firmware_size_max': gi.FunctionInfo(set_firmware_size_max), 'set_firmware_size_min': gi.FunctionInfo(set_firmware_size_min), 'set_id': gi.FunctionInfo(set_id), 'set_logical_id': gi.FunctionInfo(set_logical_id), 'set_metadata': gi.FunctionInfo(set_metadata), 'set_metadata_boolean': gi.FunctionInfo(set_metadata_boolean), 'set_metadata_integer': gi.FunctionInfo(set_metadata_integer), 'set_name': gi.FunctionInfo(set_name), 'set_order': gi.FunctionInfo(set_order), 'set_parent': gi.FunctionInfo(set_parent), 'set_physical_id': gi.FunctionInfo(set_physical_id), 'set_poll_interval': gi.FunctionInfo(set_poll_interval), 'set_priority': gi.FunctionInfo(set_priority), 'set_progress': gi.FunctionInfo(set_progress), 'set_progress_full': gi.FunctionInfo(set_progress_full), 'set_protocol': gi.FunctionInfo(set_protocol), 'set_proxy': gi.FunctionInfo(set_proxy), 'set_proxy_guid': gi.FunctionInfo(set_proxy_guid), 'set_quirks': gi.FunctionInfo(set_quirks), 'set_remove_delay': gi.FunctionInfo(set_remove_delay), 'set_status': gi.FunctionInfo(set_status), 'set_version': gi.FunctionInfo(set_version), 'set_version_bootloader': gi.FunctionInfo(set_version_bootloader), 'set_version_format': gi.FunctionInfo(set_version_format), 'set_version_lowest': gi.FunctionInfo(set_version_lowest), 'setup': gi.FunctionInfo(setup), 'to_string': gi.FunctionInfo(to_string), 'write_firmware': gi.FunctionInfo(write_firmware), 'do_activate': gi.VFuncInfo(activate), 'do_attach': gi.VFuncInfo(attach), 'do_cleanup': gi.VFuncInfo(cleanup), 'do_close': gi.VFuncInfo(close), 'do_detach': gi.VFuncInfo(detach), 'do_incorporate': gi.VFuncInfo(incorporate), 'do_open': gi.VFuncInfo(open), 'do_poll': gi.VFuncInfo(poll), 'do_prepare': gi.VFuncInfo(prepare), 'do_prepare_firmware': gi.VFuncInfo(prepare_firmware), 'do_probe': gi.VFuncInfo(probe), 'do_read_firmware': gi.VFuncInfo(read_firmware), 'do_reload': gi.VFuncInfo(reload), 'do_rescan': gi.VFuncInfo(rescan), 'do_set_quirk_kv': gi.VFuncInfo(set_quirk_kv), 'do_setup': gi.VFuncInfo(setup), 'do_to_string': gi.VFuncInfo(to_string), 'do_write_firmware': gi.VFuncInfo(write_firmware), 'parent_instance': <property object at 0x7feb1afdc770>})"
    __gdoc__ = 'void\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = ObjectInfo(Device)


