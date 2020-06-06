# encoding: utf-8
# module gi.repository.Fwupd
# from /usr/lib64/girepository-1.0/Fwupd-2.0.typelib
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


# Variables with simple values

DBUS_INTERFACE = 'org.freedesktop.fwupd'
DBUS_PATH = '/'
DBUS_SERVICE = 'org.freedesktop.fwupd'

DEVICE_FLAG_ADD_COUNTERPART_GUIDS = 0

DEVICE_FLAG_ANOTHER_WRITE_REQUIRED = 262144

DEVICE_FLAG_CAN_VERIFY = 33554432

DEVICE_FLAG_CAN_VERIFY_IMAGE = 67108864

DEVICE_FLAG_DUAL_IMAGE = 134217728

DEVICE_FLAG_ENSURE_SEMVER = 2097152

DEVICE_FLAG_HISTORICAL = 4194304

DEVICE_FLAG_IGNORE_VALIDATION = 32768

DEVICE_FLAG_INSTALL_ALL_RELEASES = -2147483648

DEVICE_FLAG_INSTALL_PARENT_FIRST = 4096

DEVICE_FLAG_INTERNAL = 1

DEVICE_FLAG_IS_BOOTLOADER = 8192

DEVICE_FLAG_LOCKED = 16

DEVICE_FLAG_MD_SET_NAME = 0

DEVICE_FLAG_MD_SET_NAME_CATEGORY = 0

DEVICE_FLAG_MD_SET_VERFMT = 0

DEVICE_FLAG_NEEDS_ACTIVATION = 1048576
DEVICE_FLAG_NEEDS_BOOTLOADER = 64
DEVICE_FLAG_NEEDS_REBOOT = 256
DEVICE_FLAG_NEEDS_SHUTDOWN = 131072

DEVICE_FLAG_NONE = 0
DEVICE_FLAG_NOTIFIED = 1024

DEVICE_FLAG_NO_AUTO_INSTANCE_IDS = 524288

DEVICE_FLAG_NO_GUID_MATCHING = 0

DEVICE_FLAG_ONLY_OFFLINE = 4
DEVICE_FLAG_ONLY_SUPPORTED = 8388608

DEVICE_FLAG_REGISTERED = 128
DEVICE_FLAG_REPORTED = 512

DEVICE_FLAG_REQUIRE_AC = 8

DEVICE_FLAG_SELF_RECOVERY = 268435456

DEVICE_FLAG_SUPPORTED = 32
DEVICE_FLAG_TRUSTED = 65536
DEVICE_FLAG_UPDATABLE = 2

DEVICE_FLAG_UPDATABLE_HIDDEN = 0

DEVICE_FLAG_USABLE_DURING_UPDATE = 536870912

DEVICE_FLAG_USE_RUNTIME_VERSION = 2048

DEVICE_FLAG_VERSION_CHECK_REQUIRED = 1073741824

DEVICE_FLAG_WAIT_FOR_REPLUG = 16384

DEVICE_FLAG_WILL_DISAPPEAR = 16777216

DEVICE_ID_ANY = '*'

RELEASE_FLAG_BLOCKED_APPROVAL = 32
RELEASE_FLAG_BLOCKED_VERSION = 16

RELEASE_FLAG_IS_DOWNGRADE = 8
RELEASE_FLAG_IS_UPGRADE = 4

RELEASE_FLAG_NONE = 0

RELEASE_FLAG_TRUSTED_METADATA = 2
RELEASE_FLAG_TRUSTED_PAYLOAD = 1

RESULT_KEY_APPSTREAM_ID = 'AppstreamId'

RESULT_KEY_CATEGORIES = 'Categories'
RESULT_KEY_CHECKSUM = 'Checksum'
RESULT_KEY_CREATED = 'Created'
RESULT_KEY_DESCRIPTION = 'Description'

RESULT_KEY_DETACH_CAPTION = 'DetachCaption'
RESULT_KEY_DETACH_IMAGE = 'DetachImage'

RESULT_KEY_DETAILS_URL = 'DetailsUrl'

RESULT_KEY_DEVICE_ID = 'DeviceId'

RESULT_KEY_FILENAME = 'Filename'
RESULT_KEY_FLAGS = 'Flags'

RESULT_KEY_FLASHES_LEFT = 'FlashesLeft'

RESULT_KEY_GUID = 'Guid'
RESULT_KEY_HOMEPAGE = 'Homepage'
RESULT_KEY_ICON = 'Icon'

RESULT_KEY_INSTALL_DURATION = 'InstallDuration'

RESULT_KEY_INSTANCE_IDS = 'InstanceIds'

RESULT_KEY_ISSUES = 'Issues'
RESULT_KEY_LICENSE = 'License'
RESULT_KEY_METADATA = 'Metadata'
RESULT_KEY_MODIFIED = 'Modified'
RESULT_KEY_NAME = 'Name'

RESULT_KEY_NAME_VARIANT_SUFFIX = 'NameVariantSuffix'

RESULT_KEY_PARENT_DEVICE_ID = 'ParentDeviceId'

RESULT_KEY_PLUGIN = 'Plugin'
RESULT_KEY_PROTOCOL = 'Protocol'
RESULT_KEY_RELEASE = 'Release'

RESULT_KEY_REMOTE_ID = 'RemoteId'

RESULT_KEY_SERIAL = 'Serial'
RESULT_KEY_SIZE = 'Size'

RESULT_KEY_SOURCE_URL = 'SourceUrl'

RESULT_KEY_STATUS = 'Status'
RESULT_KEY_SUMMARY = 'Summary'

RESULT_KEY_TRUST_FLAGS = 'TrustFlags'

RESULT_KEY_UPDATE_ERROR = 'UpdateError'
RESULT_KEY_UPDATE_MESSAGE = 'UpdateMessage'
RESULT_KEY_UPDATE_STATE = 'UpdateState'

RESULT_KEY_URGENCY = 'Urgency'
RESULT_KEY_URI = 'Uri'
RESULT_KEY_VENDOR = 'Vendor'

RESULT_KEY_VENDOR_ID = 'VendorId'

RESULT_KEY_VERSION = 'Version'

RESULT_KEY_VERSION_BOOTLOADER = 'VersionBootloader'

RESULT_KEY_VERSION_BOOTLOADER_RAW = 'VersionBootloaderRaw'

RESULT_KEY_VERSION_FORMAT = 'VersionFormat'
RESULT_KEY_VERSION_LOWEST = 'VersionLowest'

RESULT_KEY_VERSION_LOWEST_RAW = 'VersionLowestRaw'

RESULT_KEY_VERSION_RAW = 'VersionRaw'

_namespace = 'Fwupd'

_version = '2.0'

__weakref__ = None

# functions

def build_history_report_json(devices): # real signature unknown; restored from __doc__
    """ build_history_report_json(devices:list) -> str """
    return ""

def build_machine_id(salt): # real signature unknown; restored from __doc__
    """ build_machine_id(salt:str) -> str """
    return ""

def build_user_agent(package_name, package_version): # real signature unknown; restored from __doc__
    """ build_user_agent(package_name:str, package_version:str) -> str """
    return ""

def checksum_format_for_display(checksum): # real signature unknown; restored from __doc__
    """ checksum_format_for_display(checksum:str) -> str """
    return ""

def checksum_get_best(checksums): # real signature unknown; restored from __doc__
    """ checksum_get_best(checksums:list) -> str """
    return ""

def checksum_get_by_kind(checksums, kind): # real signature unknown; restored from __doc__
    """ checksum_get_by_kind(checksums:list, kind:GLib.ChecksumType) -> str """
    return ""

def checksum_guess_kind(checksum): # real signature unknown; restored from __doc__
    """ checksum_guess_kind(checksum:str) -> GLib.ChecksumType """
    pass

def error_from_string(error): # real signature unknown; restored from __doc__
    """ error_from_string(error:str) -> Fwupd.Error """
    pass

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def error_to_string(error): # real signature unknown; restored from __doc__
    """ error_to_string(error:Fwupd.Error) -> str """
    return ""

def get_os_release(): # real signature unknown; restored from __doc__
    """ get_os_release() -> dict """
    return {}

def guid_from_string(guidstr=None, guid, flags): # real signature unknown; restored from __doc__
    """ guid_from_string(guidstr:str=None, guid:int, flags:Fwupd.GuidFlags) -> bool """
    return False

def guid_hash_data(data, datasz, flags): # real signature unknown; restored from __doc__
    """ guid_hash_data(data:int, datasz:int, flags:Fwupd.GuidFlags) -> str """
    return ""

def guid_hash_string(p_str): # real signature unknown; restored from __doc__
    """ guid_hash_string(str:str) -> str """
    return ""

def guid_is_valid(guid): # real signature unknown; restored from __doc__
    """ guid_is_valid(guid:str) -> bool """
    return False

def guid_to_string(guid, flags): # real signature unknown; restored from __doc__
    """ guid_to_string(guid:int, flags:Fwupd.GuidFlags) -> str """
    return ""

def keyring_kind_from_string(keyring_kind): # real signature unknown; restored from __doc__
    """ keyring_kind_from_string(keyring_kind:str) -> Fwupd.KeyringKind """
    pass

def keyring_kind_to_string(keyring_kind): # real signature unknown; restored from __doc__
    """ keyring_kind_to_string(keyring_kind:Fwupd.KeyringKind) -> str """
    return ""

def status_from_string(status): # real signature unknown; restored from __doc__
    """ status_from_string(status:str) -> Fwupd.Status """
    pass

def status_to_string(status): # real signature unknown; restored from __doc__
    """ status_to_string(status:Fwupd.Status) -> str """
    return ""

def trust_flag_from_string(trust_flag): # real signature unknown; restored from __doc__
    """ trust_flag_from_string(trust_flag:str) -> Fwupd.TrustFlags """
    pass

def trust_flag_to_string(trust_flag): # real signature unknown; restored from __doc__
    """ trust_flag_to_string(trust_flag:Fwupd.TrustFlags) -> str """
    return ""

def update_state_from_string(update_state): # real signature unknown; restored from __doc__
    """ update_state_from_string(update_state:str) -> Fwupd.UpdateState """
    pass

def update_state_to_string(update_state): # real signature unknown; restored from __doc__
    """ update_state_to_string(update_state:Fwupd.UpdateState) -> str """
    return ""

def version_format_from_string(p_str): # real signature unknown; restored from __doc__
    """ version_format_from_string(str:str) -> Fwupd.VersionFormat """
    pass

def version_format_to_string(kind): # real signature unknown; restored from __doc__
    """ version_format_to_string(kind:Fwupd.VersionFormat) -> str """
    return ""

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class Client(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Client(**properties)
        new() -> Fwupd.Client
    """
    def activate(self, cancellable=None, device_id): # real signature unknown; restored from __doc__
        """ activate(self, cancellable:Gio.Cancellable=None, device_id:str) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_results(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ clear_results(self, device_id:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, cancellable=None): # real signature unknown; restored from __doc__
        """ connect(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_device_added(self, *args, **kwargs): # real signature unknown
        """ device_added(self, result:Fwupd.Device) """
        pass

    def do_device_changed(self, *args, **kwargs): # real signature unknown
        """ device_changed(self, result:Fwupd.Device) """
        pass

    def do_device_removed(self, *args, **kwargs): # real signature unknown
        """ device_removed(self, result:Fwupd.Device) """
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

    def get_approved_firmware(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_approved_firmware(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_daemon_interactive(self): # real signature unknown; restored from __doc__
        """ get_daemon_interactive(self) -> bool """
        return False

    def get_daemon_version(self): # real signature unknown; restored from __doc__
        """ get_daemon_version(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_details(self, filename, cancellable=None): # real signature unknown; restored from __doc__
        """ get_details(self, filename:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_devices(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_devices(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_devices_by_guid(self, guid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_devices_by_guid(self, guid:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_device_by_id(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ get_device_by_id(self, device_id:str, cancellable:Gio.Cancellable=None) -> Fwupd.Device """
        pass

    def get_downgrades(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ get_downgrades(self, device_id:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_history(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_history(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_host_machine_id(self): # real signature unknown; restored from __doc__
        """ get_host_machine_id(self) -> str """
        return ""

    def get_host_product(self): # real signature unknown; restored from __doc__
        """ get_host_product(self) -> str """
        return ""

    def get_percentage(self): # real signature unknown; restored from __doc__
        """ get_percentage(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_releases(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ get_releases(self, device_id:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_remotes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_remotes(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_remote_by_id(self, remote_id, cancellable=None): # real signature unknown; restored from __doc__
        """ get_remote_by_id(self, remote_id:str, cancellable:Gio.Cancellable=None) -> Fwupd.Remote """
        pass

    def get_results(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ get_results(self, device_id:str, cancellable:Gio.Cancellable=None) -> Fwupd.Device """
        pass

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> Fwupd.Status """
        pass

    def get_tainted(self): # real signature unknown; restored from __doc__
        """ get_tainted(self) -> bool """
        return False

    def get_upgrades(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ get_upgrades(self, device_id:str, cancellable:Gio.Cancellable=None) -> list """
        return []

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

    def install(self, device_id, filename, install_flags, cancellable=None): # real signature unknown; restored from __doc__
        """ install(self, device_id:str, filename:str, install_flags:Fwupd.InstallFlags, cancellable:Gio.Cancellable=None) -> bool """
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def modify_config(self, key, value, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_config(self, key:str, value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def modify_device(self, device_id, key, value, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_device(self, device_id:str, key:str, value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def modify_remote(self, remote_id, key, value, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_remote(self, remote_id:str, key:str, value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Fwupd.Client """
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

    def self_sign(self, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ self_sign(self, value:str, flags:Fwupd.SelfSignFlags, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def set_approved_firmware(self, checksums, cancellable=None): # real signature unknown; restored from __doc__
        """ set_approved_firmware(self, checksums:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def unlock(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ unlock(self, device_id:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update_metadata(self, remote_id, metadata_fn, signature_fn, cancellable=None): # real signature unknown; restored from __doc__
        """ update_metadata(self, remote_id:str, metadata_fn:str, signature_fn:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def verify(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ verify(self, device_id:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def verify_update(self, device_id, cancellable=None): # real signature unknown; restored from __doc__
        """ verify_update(self, device_id:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f66f43ab910>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Client), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType FwupdClient (94734970094496)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'activate': gi.FunctionInfo(activate), 'clear_results': gi.FunctionInfo(clear_results), 'connect': gi.FunctionInfo(connect), 'get_approved_firmware': gi.FunctionInfo(get_approved_firmware), 'get_daemon_interactive': gi.FunctionInfo(get_daemon_interactive), 'get_daemon_version': gi.FunctionInfo(get_daemon_version), 'get_details': gi.FunctionInfo(get_details), 'get_device_by_id': gi.FunctionInfo(get_device_by_id), 'get_devices': gi.FunctionInfo(get_devices), 'get_devices_by_guid': gi.FunctionInfo(get_devices_by_guid), 'get_downgrades': gi.FunctionInfo(get_downgrades), 'get_history': gi.FunctionInfo(get_history), 'get_host_machine_id': gi.FunctionInfo(get_host_machine_id), 'get_host_product': gi.FunctionInfo(get_host_product), 'get_percentage': gi.FunctionInfo(get_percentage), 'get_releases': gi.FunctionInfo(get_releases), 'get_remote_by_id': gi.FunctionInfo(get_remote_by_id), 'get_remotes': gi.FunctionInfo(get_remotes), 'get_results': gi.FunctionInfo(get_results), 'get_status': gi.FunctionInfo(get_status), 'get_tainted': gi.FunctionInfo(get_tainted), 'get_upgrades': gi.FunctionInfo(get_upgrades), 'install': gi.FunctionInfo(install), 'modify_config': gi.FunctionInfo(modify_config), 'modify_device': gi.FunctionInfo(modify_device), 'modify_remote': gi.FunctionInfo(modify_remote), 'self_sign': gi.FunctionInfo(self_sign), 'set_approved_firmware': gi.FunctionInfo(set_approved_firmware), 'unlock': gi.FunctionInfo(unlock), 'update_metadata': gi.FunctionInfo(update_metadata), 'verify': gi.FunctionInfo(verify), 'verify_update': gi.FunctionInfo(verify_update), 'do_changed': gi.VFuncInfo(changed), 'do_device_added': gi.VFuncInfo(device_added), 'do_device_changed': gi.VFuncInfo(device_changed), 'do_device_removed': gi.VFuncInfo(device_removed), 'do_status_changed': gi.VFuncInfo(status_changed), 'parent_instance': <property object at 0x7f66f43d9770>})"
    __gdoc__ = 'Object FwupdClient\n\nSignals from FwupdClient:\n  changed ()\n  status-changed (guint)\n  device-added (FwupdDevice)\n  device-removed (FwupdDevice)\n  device-changed (FwupdDevice)\n\nProperties from FwupdClient:\n  status -> guint: status\n  percentage -> guint: percentage\n  daemon-version -> gchararray: daemon-version\n  tainted -> gboolean: tainted\n  host-product -> gchararray: host-product\n  host-machine-id -> gchararray: host-machine-id\n  interactive -> gboolean: interactive\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType FwupdClient (94734970094496)>'
    __info__ = ObjectInfo(Client)


class ClientClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ClientClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    device_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    device_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    device_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ClientClass), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ClientClass' objects>, '__weakref__': <attribute '__weakref__' of 'ClientClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f66f43d9860>, 'changed': <property object at 0x7f66f43d98b0>, 'status_changed': <property object at 0x7f66f43d9900>, 'device_added': <property object at 0x7f66f43d99f0>, 'device_removed': <property object at 0x7f66f43d9ae0>, 'device_changed': <property object at 0x7f66f43d9bd0>, '_fwupd_reserved1': <property object at 0x7f66f43d9d10>, '_fwupd_reserved2': <property object at 0x7f66f43d9e50>, '_fwupd_reserved3': <property object at 0x7f66f43d9f90>, '_fwupd_reserved4': <property object at 0x7f66f43d6130>, '_fwupd_reserved5': <property object at 0x7f66f43d6270>, '_fwupd_reserved6': <property object at 0x7f66f43d63b0>, '_fwupd_reserved7': <property object at 0x7f66f43d64f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ClientClass)


class Device(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Device(**properties)
        new() -> Fwupd.Device
    """
    def add_checksum(self, checksum): # real signature unknown; restored from __doc__
        """ add_checksum(self, checksum:str) """
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

    def add_release(self, release): # real signature unknown; restored from __doc__
        """ add_release(self, release:Fwupd.Release) """
        pass

    def array_ensure_parents(self, devices): # real signature unknown; restored from __doc__
        """ array_ensure_parents(devices:list) """
        pass

    def array_from_variant(self, value): # real signature unknown; restored from __doc__
        """ array_from_variant(value:GLib.Variant) -> list """
        return []

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

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

    def get_checksums(self): # real signature unknown; restored from __doc__
        """ get_checksums(self) -> list """
        return []

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_flashes_left(self): # real signature unknown; restored from __doc__
        """ get_flashes_left(self) -> int """
        return 0

    def get_guids(self): # real signature unknown; restored from __doc__
        """ get_guids(self) -> list """
        return []

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

    def get_modified(self): # real signature unknown; restored from __doc__
        """ get_modified(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Fwupd.Device """
        pass

    def get_parent_id(self): # real signature unknown; restored from __doc__
        """ get_parent_id(self) -> str """
        return ""

    def get_plugin(self): # real signature unknown; restored from __doc__
        """ get_plugin(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_releases(self): # real signature unknown; restored from __doc__
        """ get_releases(self) -> list """
        return []

    def get_release_default(self): # real signature unknown; restored from __doc__
        """ get_release_default(self) -> Fwupd.Release """
        pass

    def get_serial(self): # real signature unknown; restored from __doc__
        """ get_serial(self) -> str """
        return ""

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

    def has_flag(self, flag): # real signature unknown; restored from __doc__
        """ has_flag(self, flag:int) -> bool """
        return False

    def has_guid(self, guid): # real signature unknown; restored from __doc__
        """ has_guid(self, guid:str) -> bool """
        return False

    def has_instance_id(self, instance_id): # real signature unknown; restored from __doc__
        """ has_instance_id(self, instance_id:str) -> bool """
        return False

    def id_is_valid(self, device_id): # real signature unknown; restored from __doc__
        """ id_is_valid(device_id:str) -> bool """
        return False

    def incorporate(self, donor): # real signature unknown; restored from __doc__
        """ incorporate(self, donor:Fwupd.Device) """
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
        """ new() -> Fwupd.Device """
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

    def remove_flag(self, flag): # real signature unknown; restored from __doc__
        """ remove_flag(self, flag:int) """
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

    def set_created(self, created): # real signature unknown; restored from __doc__
        """ set_created(self, created:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
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

    def set_modified(self, modified): # real signature unknown; restored from __doc__
        """ set_modified(self, modified:int) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Fwupd.Device) """
        pass

    def set_parent_id(self, parent_id): # real signature unknown; restored from __doc__
        """ set_parent_id(self, parent_id:str) """
        pass

    def set_plugin(self, plugin): # real signature unknown; restored from __doc__
        """ set_plugin(self, plugin:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ set_protocol(self, protocol:str) """
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

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:str) """
        pass

    def set_version_bootloader(self, version_bootloader): # real signature unknown; restored from __doc__
        """ set_version_bootloader(self, version_bootloader:str) """
        pass

    def set_version_bootloader_raw(self, version_bootloader_raw): # real signature unknown; restored from __doc__
        """ set_version_bootloader_raw(self, version_bootloader_raw:int) """
        pass

    def set_version_format(self, version_format): # real signature unknown; restored from __doc__
        """ set_version_format(self, version_format:Fwupd.VersionFormat) """
        pass

    def set_version_lowest(self, version_lowest): # real signature unknown; restored from __doc__
        """ set_version_lowest(self, version_lowest:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f66f43d5fd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Device), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType FwupdDevice (94734970101808)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'array_ensure_parents': gi.FunctionInfo(array_ensure_parents), 'array_from_variant': gi.FunctionInfo(array_from_variant), 'flag_from_string': gi.FunctionInfo(flag_from_string), 'flag_to_string': gi.FunctionInfo(flag_to_string), 'from_variant': gi.FunctionInfo(from_variant), 'id_is_valid': gi.FunctionInfo(id_is_valid), 'add_checksum': gi.FunctionInfo(add_checksum), 'add_flag': gi.FunctionInfo(add_flag), 'add_guid': gi.FunctionInfo(add_guid), 'add_icon': gi.FunctionInfo(add_icon), 'add_instance_id': gi.FunctionInfo(add_instance_id), 'add_release': gi.FunctionInfo(add_release), 'compare': gi.FunctionInfo(compare), 'get_checksums': gi.FunctionInfo(get_checksums), 'get_children': gi.FunctionInfo(get_children), 'get_created': gi.FunctionInfo(get_created), 'get_description': gi.FunctionInfo(get_description), 'get_flags': gi.FunctionInfo(get_flags), 'get_flashes_left': gi.FunctionInfo(get_flashes_left), 'get_guid_default': gi.FunctionInfo(get_guid_default), 'get_guids': gi.FunctionInfo(get_guids), 'get_icons': gi.FunctionInfo(get_icons), 'get_id': gi.FunctionInfo(get_id), 'get_install_duration': gi.FunctionInfo(get_install_duration), 'get_instance_ids': gi.FunctionInfo(get_instance_ids), 'get_modified': gi.FunctionInfo(get_modified), 'get_name': gi.FunctionInfo(get_name), 'get_parent': gi.FunctionInfo(get_parent), 'get_parent_id': gi.FunctionInfo(get_parent_id), 'get_plugin': gi.FunctionInfo(get_plugin), 'get_protocol': gi.FunctionInfo(get_protocol), 'get_release_default': gi.FunctionInfo(get_release_default), 'get_releases': gi.FunctionInfo(get_releases), 'get_serial': gi.FunctionInfo(get_serial), 'get_status': gi.FunctionInfo(get_status), 'get_summary': gi.FunctionInfo(get_summary), 'get_update_error': gi.FunctionInfo(get_update_error), 'get_update_message': gi.FunctionInfo(get_update_message), 'get_update_state': gi.FunctionInfo(get_update_state), 'get_vendor': gi.FunctionInfo(get_vendor), 'get_vendor_id': gi.FunctionInfo(get_vendor_id), 'get_version': gi.FunctionInfo(get_version), 'get_version_bootloader': gi.FunctionInfo(get_version_bootloader), 'get_version_bootloader_raw': gi.FunctionInfo(get_version_bootloader_raw), 'get_version_format': gi.FunctionInfo(get_version_format), 'get_version_lowest': gi.FunctionInfo(get_version_lowest), 'get_version_lowest_raw': gi.FunctionInfo(get_version_lowest_raw), 'get_version_raw': gi.FunctionInfo(get_version_raw), 'has_flag': gi.FunctionInfo(has_flag), 'has_guid': gi.FunctionInfo(has_guid), 'has_instance_id': gi.FunctionInfo(has_instance_id), 'incorporate': gi.FunctionInfo(incorporate), 'remove_flag': gi.FunctionInfo(remove_flag), 'set_created': gi.FunctionInfo(set_created), 'set_description': gi.FunctionInfo(set_description), 'set_flags': gi.FunctionInfo(set_flags), 'set_flashes_left': gi.FunctionInfo(set_flashes_left), 'set_id': gi.FunctionInfo(set_id), 'set_install_duration': gi.FunctionInfo(set_install_duration), 'set_modified': gi.FunctionInfo(set_modified), 'set_name': gi.FunctionInfo(set_name), 'set_parent': gi.FunctionInfo(set_parent), 'set_parent_id': gi.FunctionInfo(set_parent_id), 'set_plugin': gi.FunctionInfo(set_plugin), 'set_protocol': gi.FunctionInfo(set_protocol), 'set_serial': gi.FunctionInfo(set_serial), 'set_status': gi.FunctionInfo(set_status), 'set_summary': gi.FunctionInfo(set_summary), 'set_update_error': gi.FunctionInfo(set_update_error), 'set_update_message': gi.FunctionInfo(set_update_message), 'set_update_state': gi.FunctionInfo(set_update_state), 'set_vendor': gi.FunctionInfo(set_vendor), 'set_vendor_id': gi.FunctionInfo(set_vendor_id), 'set_version': gi.FunctionInfo(set_version), 'set_version_bootloader': gi.FunctionInfo(set_version_bootloader), 'set_version_bootloader_raw': gi.FunctionInfo(set_version_bootloader_raw), 'set_version_format': gi.FunctionInfo(set_version_format), 'set_version_lowest': gi.FunctionInfo(set_version_lowest), 'set_version_lowest_raw': gi.FunctionInfo(set_version_lowest_raw), 'set_version_raw': gi.FunctionInfo(set_version_raw), 'to_string': gi.FunctionInfo(to_string), 'to_variant': gi.FunctionInfo(to_variant), 'to_variant_full': gi.FunctionInfo(to_variant_full), 'parent_instance': <property object at 0x7f66f43d6f40>})"
    __gdoc__ = 'Object FwupdDevice\n\nProperties from FwupdDevice:\n  version-format -> guint: version-format\n  flags -> guint64: flags\n  protocol -> gchararray: protocol\n  status -> guint: status\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType FwupdDevice (94734970101808)>'
    __info__ = ObjectInfo(Device)


class DeviceClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DeviceClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DeviceClass), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DeviceClass' objects>, '__weakref__': <attribute '__weakref__' of 'DeviceClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f66f43dc130>, '_fwupd_reserved1': <property object at 0x7f66f43dc270>, '_fwupd_reserved2': <property object at 0x7f66f43dc360>, '_fwupd_reserved3': <property object at 0x7f66f43dc450>, '_fwupd_reserved4': <property object at 0x7f66f43dc540>, '_fwupd_reserved5': <property object at 0x7f66f43dc630>, '_fwupd_reserved6': <property object at 0x7f66f43dc720>, '_fwupd_reserved7': <property object at 0x7f66f43dc810>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DeviceClass)


class Error(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    AC_POWER_REQUIRED = 12
    ALREADY_PENDING = 3
    AUTH_FAILED = 4
    BATTERY_LEVEL_TOO_LOW = 15
    BROKEN_SYSTEM = 14
    INTERNAL = 0
    INVALID_FILE = 7
    NEEDS_USER_ACTION = 16
    NOTHING_TO_DO = 9
    NOT_FOUND = 8
    NOT_SUPPORTED = 10
    PERMISSION_DENIED = 13
    READ = 5
    SIGNATURE_INVALID = 11
    VERSION_NEWER = 1
    VERSION_SAME = 2
    WRITE = 6
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'Error' objects>, '__doc__': None, '__gtype__': <GType PyFwupdError (94734970111248)>, '__enum_values__': {0: <enum FWUPD_ERROR_INTERNAL of type Fwupd.Error>, 1: <enum FWUPD_ERROR_VERSION_NEWER of type Fwupd.Error>, 2: <enum FWUPD_ERROR_VERSION_SAME of type Fwupd.Error>, 3: <enum FWUPD_ERROR_ALREADY_PENDING of type Fwupd.Error>, 4: <enum FWUPD_ERROR_AUTH_FAILED of type Fwupd.Error>, 5: <enum FWUPD_ERROR_READ of type Fwupd.Error>, 6: <enum FWUPD_ERROR_WRITE of type Fwupd.Error>, 7: <enum FWUPD_ERROR_INVALID_FILE of type Fwupd.Error>, 8: <enum FWUPD_ERROR_NOT_FOUND of type Fwupd.Error>, 9: <enum FWUPD_ERROR_NOTHING_TO_DO of type Fwupd.Error>, 10: <enum FWUPD_ERROR_NOT_SUPPORTED of type Fwupd.Error>, 11: <enum FWUPD_ERROR_SIGNATURE_INVALID of type Fwupd.Error>, 12: <enum FWUPD_ERROR_AC_POWER_REQUIRED of type Fwupd.Error>, 13: <enum FWUPD_ERROR_PERMISSION_DENIED of type Fwupd.Error>, 14: <enum FWUPD_ERROR_BROKEN_SYSTEM of type Fwupd.Error>, 15: <enum FWUPD_ERROR_BATTERY_LEVEL_TOO_LOW of type Fwupd.Error>, 16: <enum FWUPD_ERROR_NEEDS_USER_ACTION of type Fwupd.Error>}, '__info__': gi.EnumInfo(Error), 'INTERNAL': <enum FWUPD_ERROR_INTERNAL of type Fwupd.Error>, 'VERSION_NEWER': <enum FWUPD_ERROR_VERSION_NEWER of type Fwupd.Error>, 'VERSION_SAME': <enum FWUPD_ERROR_VERSION_SAME of type Fwupd.Error>, 'ALREADY_PENDING': <enum FWUPD_ERROR_ALREADY_PENDING of type Fwupd.Error>, 'AUTH_FAILED': <enum FWUPD_ERROR_AUTH_FAILED of type Fwupd.Error>, 'READ': <enum FWUPD_ERROR_READ of type Fwupd.Error>, 'WRITE': <enum FWUPD_ERROR_WRITE of type Fwupd.Error>, 'INVALID_FILE': <enum FWUPD_ERROR_INVALID_FILE of type Fwupd.Error>, 'NOT_FOUND': <enum FWUPD_ERROR_NOT_FOUND of type Fwupd.Error>, 'NOTHING_TO_DO': <enum FWUPD_ERROR_NOTHING_TO_DO of type Fwupd.Error>, 'NOT_SUPPORTED': <enum FWUPD_ERROR_NOT_SUPPORTED of type Fwupd.Error>, 'SIGNATURE_INVALID': <enum FWUPD_ERROR_SIGNATURE_INVALID of type Fwupd.Error>, 'AC_POWER_REQUIRED': <enum FWUPD_ERROR_AC_POWER_REQUIRED of type Fwupd.Error>, 'PERMISSION_DENIED': <enum FWUPD_ERROR_PERMISSION_DENIED of type Fwupd.Error>, 'BROKEN_SYSTEM': <enum FWUPD_ERROR_BROKEN_SYSTEM of type Fwupd.Error>, 'BATTERY_LEVEL_TOO_LOW': <enum FWUPD_ERROR_BATTERY_LEVEL_TOO_LOW of type Fwupd.Error>, 'NEEDS_USER_ACTION': <enum FWUPD_ERROR_NEEDS_USER_ACTION of type Fwupd.Error>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdError (94734970111248)>'
    __info__ = gi.EnumInfo(Error)


class GuidFlags(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MIXED_ENDIAN = 2
    NAMESPACE_MICROSOFT = 1
    NONE = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'GuidFlags' objects>, '__doc__': None, '__gtype__': <GType PyFwupdGuidFlags (94734970112560)>, '__flags_values__': {0: <flags 0 of type Fwupd.GuidFlags>, 1: <flags FWUPD_GUID_FLAG_NAMESPACE_MICROSOFT of type Fwupd.GuidFlags>, 2: <flags FWUPD_GUID_FLAG_MIXED_ENDIAN of type Fwupd.GuidFlags>}, '__info__': gi.EnumInfo(GuidFlags), 'NONE': <flags 0 of type Fwupd.GuidFlags>, 'NAMESPACE_MICROSOFT': <flags FWUPD_GUID_FLAG_NAMESPACE_MICROSOFT of type Fwupd.GuidFlags>, 'MIXED_ENDIAN': <flags FWUPD_GUID_FLAG_MIXED_ENDIAN of type Fwupd.GuidFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdGuidFlags (94734970112560)>'
    __info__ = gi.EnumInfo(GuidFlags)


class InstallFlags(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ALLOW_OLDER = 4
    ALLOW_REINSTALL = 2
    FORCE = 8
    NONE = 0
    NO_HISTORY = 16
    OFFLINE = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'InstallFlags' objects>, '__doc__': None, '__gtype__': <GType PyFwupdInstallFlags (94734970118992)>, '__flags_values__': {0: <flags 0 of type Fwupd.InstallFlags>, 1: <flags FWUPD_INSTALL_FLAG_OFFLINE of type Fwupd.InstallFlags>, 2: <flags FWUPD_INSTALL_FLAG_ALLOW_REINSTALL of type Fwupd.InstallFlags>, 4: <flags FWUPD_INSTALL_FLAG_ALLOW_OLDER of type Fwupd.InstallFlags>, 8: <flags FWUPD_INSTALL_FLAG_FORCE of type Fwupd.InstallFlags>, 16: <flags FWUPD_INSTALL_FLAG_NO_HISTORY of type Fwupd.InstallFlags>}, '__info__': gi.EnumInfo(InstallFlags), 'NONE': <flags 0 of type Fwupd.InstallFlags>, 'OFFLINE': <flags FWUPD_INSTALL_FLAG_OFFLINE of type Fwupd.InstallFlags>, 'ALLOW_REINSTALL': <flags FWUPD_INSTALL_FLAG_ALLOW_REINSTALL of type Fwupd.InstallFlags>, 'ALLOW_OLDER': <flags FWUPD_INSTALL_FLAG_ALLOW_OLDER of type Fwupd.InstallFlags>, 'FORCE': <flags FWUPD_INSTALL_FLAG_FORCE of type Fwupd.InstallFlags>, 'NO_HISTORY': <flags FWUPD_INSTALL_FLAG_NO_HISTORY of type Fwupd.InstallFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdInstallFlags (94734970118992)>'
    __info__ = gi.EnumInfo(InstallFlags)


class KeyringKind(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    GPG = 2
    JCAT = 4
    NONE = 1
    PKCS7 = 3
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'KeyringKind' objects>, '__doc__': None, '__gtype__': <GType PyFwupdKeyringKind (94734970123744)>, '__enum_values__': {0: <enum FWUPD_KEYRING_KIND_UNKNOWN of type Fwupd.KeyringKind>, 1: <enum FWUPD_KEYRING_KIND_NONE of type Fwupd.KeyringKind>, 2: <enum FWUPD_KEYRING_KIND_GPG of type Fwupd.KeyringKind>, 3: <enum FWUPD_KEYRING_KIND_PKCS7 of type Fwupd.KeyringKind>, 4: <enum FWUPD_KEYRING_KIND_JCAT of type Fwupd.KeyringKind>}, '__info__': gi.EnumInfo(KeyringKind), 'UNKNOWN': <enum FWUPD_KEYRING_KIND_UNKNOWN of type Fwupd.KeyringKind>, 'NONE': <enum FWUPD_KEYRING_KIND_NONE of type Fwupd.KeyringKind>, 'GPG': <enum FWUPD_KEYRING_KIND_GPG of type Fwupd.KeyringKind>, 'PKCS7': <enum FWUPD_KEYRING_KIND_PKCS7 of type Fwupd.KeyringKind>, 'JCAT': <enum FWUPD_KEYRING_KIND_JCAT of type Fwupd.KeyringKind>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdKeyringKind (94734970123744)>'
    __info__ = gi.EnumInfo(KeyringKind)


class Release(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Release(**properties)
        new() -> Fwupd.Release
    """
    def add_category(self, category): # real signature unknown; restored from __doc__
        """ add_category(self, category:str) """
        pass

    def add_checksum(self, checksum): # real signature unknown; restored from __doc__
        """ add_checksum(self, checksum:str) """
        pass

    def add_flag(self, flag): # real signature unknown; restored from __doc__
        """ add_flag(self, flag:int) """
        pass

    def add_issue(self, issue): # real signature unknown; restored from __doc__
        """ add_issue(self, issue:str) """
        pass

    def add_metadata(self, hash): # real signature unknown; restored from __doc__
        """ add_metadata(self, hash:dict) """
        pass

    def add_metadata_item(self, key, value): # real signature unknown; restored from __doc__
        """ add_metadata_item(self, key:str, value:str) """
        pass

    def array_from_variant(self, value): # real signature unknown; restored from __doc__
        """ array_from_variant(value:GLib.Variant) -> list """
        return []

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

    def flag_from_string(self, release_flag): # real signature unknown; restored from __doc__
        """ flag_from_string(release_flag:str) -> int """
        return 0

    def flag_to_string(self, release_flag): # real signature unknown; restored from __doc__
        """ flag_to_string(release_flag:int) -> str """
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
        """ from_variant(value:GLib.Variant) -> Fwupd.Release """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_appstream_id(self): # real signature unknown; restored from __doc__
        """ get_appstream_id(self) -> str """
        return ""

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> list """
        return []

    def get_checksums(self): # real signature unknown; restored from __doc__
        """ get_checksums(self) -> list """
        return []

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_detach_caption(self): # real signature unknown; restored from __doc__
        """ get_detach_caption(self) -> str """
        return ""

    def get_detach_image(self): # real signature unknown; restored from __doc__
        """ get_detach_image(self) -> str """
        return ""

    def get_details_url(self): # real signature unknown; restored from __doc__
        """ get_details_url(self) -> str """
        return ""

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_homepage(self): # real signature unknown; restored from __doc__
        """ get_homepage(self) -> str """
        return ""

    def get_install_duration(self): # real signature unknown; restored from __doc__
        """ get_install_duration(self) -> int """
        return 0

    def get_issues(self): # real signature unknown; restored from __doc__
        """ get_issues(self) -> list """
        return []

    def get_license(self): # real signature unknown; restored from __doc__
        """ get_license(self) -> str """
        return ""

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> dict """
        return {}

    def get_metadata_item(self, key): # real signature unknown; restored from __doc__
        """ get_metadata_item(self, key:str) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_name_variant_suffix(self): # real signature unknown; restored from __doc__
        """ get_name_variant_suffix(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote_id(self): # real signature unknown; restored from __doc__
        """ get_remote_id(self) -> str """
        return ""

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_source_url(self): # real signature unknown; restored from __doc__
        """ get_source_url(self) -> str """
        return ""

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_trust_flags(self): # real signature unknown; restored from __doc__
        """ get_trust_flags(self) -> Fwupd.TrustFlags """
        pass

    def get_update_message(self): # real signature unknown; restored from __doc__
        """ get_update_message(self) -> str """
        return ""

    def get_urgency(self): # real signature unknown; restored from __doc__
        """ get_urgency(self) -> Fwupd.ReleaseUrgency """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_vendor(self): # real signature unknown; restored from __doc__
        """ get_vendor(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
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

    def has_category(self, category): # real signature unknown; restored from __doc__
        """ has_category(self, category:str) -> bool """
        return False

    def has_checksum(self, checksum): # real signature unknown; restored from __doc__
        """ has_checksum(self, checksum:str) -> bool """
        return False

    def has_flag(self, flag): # real signature unknown; restored from __doc__
        """ has_flag(self, flag:int) -> bool """
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Fwupd.Release """
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

    def remove_flag(self, flag): # real signature unknown; restored from __doc__
        """ remove_flag(self, flag:int) """
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

    def set_appstream_id(self, appstream_id): # real signature unknown; restored from __doc__
        """ set_appstream_id(self, appstream_id:str) """
        pass

    def set_created(self, created): # real signature unknown; restored from __doc__
        """ set_created(self, created:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_detach_caption(self, detach_caption): # real signature unknown; restored from __doc__
        """ set_detach_caption(self, detach_caption:str) """
        pass

    def set_detach_image(self, detach_image): # real signature unknown; restored from __doc__
        """ set_detach_image(self, detach_image:str) """
        pass

    def set_details_url(self, details_url): # real signature unknown; restored from __doc__
        """ set_details_url(self, details_url:str) """
        pass

    def set_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_filename(self, filename:str) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:int) """
        pass

    def set_homepage(self, homepage): # real signature unknown; restored from __doc__
        """ set_homepage(self, homepage:str) """
        pass

    def set_install_duration(self, duration): # real signature unknown; restored from __doc__
        """ set_install_duration(self, duration:int) """
        pass

    def set_license(self, license): # real signature unknown; restored from __doc__
        """ set_license(self, license:str) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_name_variant_suffix(self, name_variant_suffix): # real signature unknown; restored from __doc__
        """ set_name_variant_suffix(self, name_variant_suffix:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ set_protocol(self, protocol:str) """
        pass

    def set_remote_id(self, remote_id): # real signature unknown; restored from __doc__
        """ set_remote_id(self, remote_id:str) """
        pass

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
        pass

    def set_source_url(self, source_url): # real signature unknown; restored from __doc__
        """ set_source_url(self, source_url:str) """
        pass

    def set_summary(self, summary): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str) """
        pass

    def set_trust_flags(self, trust_flags): # real signature unknown; restored from __doc__
        """ set_trust_flags(self, trust_flags:Fwupd.TrustFlags) """
        pass

    def set_update_message(self, update_message): # real signature unknown; restored from __doc__
        """ set_update_message(self, update_message:str) """
        pass

    def set_urgency(self, urgency): # real signature unknown; restored from __doc__
        """ set_urgency(self, urgency:Fwupd.ReleaseUrgency) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) """
        pass

    def set_vendor(self, vendor): # real signature unknown; restored from __doc__
        """ set_vendor(self, vendor:str) """
        pass

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:str) """
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

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def urgency_from_string(self, release_urgency): # real signature unknown; restored from __doc__
        """ urgency_from_string(release_urgency:str) -> Fwupd.ReleaseUrgency """
        pass

    def urgency_to_string(self, release_urgency): # real signature unknown; restored from __doc__
        """ urgency_to_string(release_urgency:Fwupd.ReleaseUrgency) -> str """
        return ""

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f66f43d5df0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Release), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType FwupdRelease (94734970101968)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'array_from_variant': gi.FunctionInfo(array_from_variant), 'flag_from_string': gi.FunctionInfo(flag_from_string), 'flag_to_string': gi.FunctionInfo(flag_to_string), 'from_variant': gi.FunctionInfo(from_variant), 'urgency_from_string': gi.FunctionInfo(urgency_from_string), 'urgency_to_string': gi.FunctionInfo(urgency_to_string), 'add_category': gi.FunctionInfo(add_category), 'add_checksum': gi.FunctionInfo(add_checksum), 'add_flag': gi.FunctionInfo(add_flag), 'add_issue': gi.FunctionInfo(add_issue), 'add_metadata': gi.FunctionInfo(add_metadata), 'add_metadata_item': gi.FunctionInfo(add_metadata_item), 'get_appstream_id': gi.FunctionInfo(get_appstream_id), 'get_categories': gi.FunctionInfo(get_categories), 'get_checksums': gi.FunctionInfo(get_checksums), 'get_created': gi.FunctionInfo(get_created), 'get_description': gi.FunctionInfo(get_description), 'get_detach_caption': gi.FunctionInfo(get_detach_caption), 'get_detach_image': gi.FunctionInfo(get_detach_image), 'get_details_url': gi.FunctionInfo(get_details_url), 'get_filename': gi.FunctionInfo(get_filename), 'get_flags': gi.FunctionInfo(get_flags), 'get_homepage': gi.FunctionInfo(get_homepage), 'get_install_duration': gi.FunctionInfo(get_install_duration), 'get_issues': gi.FunctionInfo(get_issues), 'get_license': gi.FunctionInfo(get_license), 'get_metadata': gi.FunctionInfo(get_metadata), 'get_metadata_item': gi.FunctionInfo(get_metadata_item), 'get_name': gi.FunctionInfo(get_name), 'get_name_variant_suffix': gi.FunctionInfo(get_name_variant_suffix), 'get_protocol': gi.FunctionInfo(get_protocol), 'get_remote_id': gi.FunctionInfo(get_remote_id), 'get_size': gi.FunctionInfo(get_size), 'get_source_url': gi.FunctionInfo(get_source_url), 'get_summary': gi.FunctionInfo(get_summary), 'get_trust_flags': gi.FunctionInfo(get_trust_flags), 'get_update_message': gi.FunctionInfo(get_update_message), 'get_urgency': gi.FunctionInfo(get_urgency), 'get_uri': gi.FunctionInfo(get_uri), 'get_vendor': gi.FunctionInfo(get_vendor), 'get_version': gi.FunctionInfo(get_version), 'has_category': gi.FunctionInfo(has_category), 'has_checksum': gi.FunctionInfo(has_checksum), 'has_flag': gi.FunctionInfo(has_flag), 'remove_flag': gi.FunctionInfo(remove_flag), 'set_appstream_id': gi.FunctionInfo(set_appstream_id), 'set_created': gi.FunctionInfo(set_created), 'set_description': gi.FunctionInfo(set_description), 'set_detach_caption': gi.FunctionInfo(set_detach_caption), 'set_detach_image': gi.FunctionInfo(set_detach_image), 'set_details_url': gi.FunctionInfo(set_details_url), 'set_filename': gi.FunctionInfo(set_filename), 'set_flags': gi.FunctionInfo(set_flags), 'set_homepage': gi.FunctionInfo(set_homepage), 'set_install_duration': gi.FunctionInfo(set_install_duration), 'set_license': gi.FunctionInfo(set_license), 'set_name': gi.FunctionInfo(set_name), 'set_name_variant_suffix': gi.FunctionInfo(set_name_variant_suffix), 'set_protocol': gi.FunctionInfo(set_protocol), 'set_remote_id': gi.FunctionInfo(set_remote_id), 'set_size': gi.FunctionInfo(set_size), 'set_source_url': gi.FunctionInfo(set_source_url), 'set_summary': gi.FunctionInfo(set_summary), 'set_trust_flags': gi.FunctionInfo(set_trust_flags), 'set_update_message': gi.FunctionInfo(set_update_message), 'set_urgency': gi.FunctionInfo(set_urgency), 'set_uri': gi.FunctionInfo(set_uri), 'set_vendor': gi.FunctionInfo(set_vendor), 'set_version': gi.FunctionInfo(set_version), 'to_string': gi.FunctionInfo(to_string), 'to_variant': gi.FunctionInfo(to_variant), 'parent_instance': <property object at 0x7f66f43def40>})"
    __gdoc__ = 'Object FwupdRelease\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType FwupdRelease (94734970101968)>'
    __info__ = ObjectInfo(Release)


class ReleaseClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ReleaseClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ReleaseClass), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ReleaseClass' objects>, '__weakref__': <attribute '__weakref__' of 'ReleaseClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f66f43e2130>, '_fwupd_reserved1': <property object at 0x7f66f43e2270>, '_fwupd_reserved2': <property object at 0x7f66f43e2360>, '_fwupd_reserved3': <property object at 0x7f66f43e2450>, '_fwupd_reserved4': <property object at 0x7f66f43e2540>, '_fwupd_reserved5': <property object at 0x7f66f43e2630>, '_fwupd_reserved6': <property object at 0x7f66f43e2720>, '_fwupd_reserved7': <property object at 0x7f66f43e2810>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ReleaseClass)


class ReleaseUrgency(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CRITICAL = 4
    HIGH = 3
    LOW = 1
    MEDIUM = 2
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'ReleaseUrgency' objects>, '__doc__': None, '__gtype__': <GType PyFwupdReleaseUrgency (94734970106160)>, '__enum_values__': {0: <enum FWUPD_RELEASE_URGENCY_UNKNOWN of type Fwupd.ReleaseUrgency>, 1: <enum FWUPD_RELEASE_URGENCY_LOW of type Fwupd.ReleaseUrgency>, 2: <enum FWUPD_RELEASE_URGENCY_MEDIUM of type Fwupd.ReleaseUrgency>, 3: <enum FWUPD_RELEASE_URGENCY_HIGH of type Fwupd.ReleaseUrgency>, 4: <enum FWUPD_RELEASE_URGENCY_CRITICAL of type Fwupd.ReleaseUrgency>}, '__info__': gi.EnumInfo(ReleaseUrgency), 'UNKNOWN': <enum FWUPD_RELEASE_URGENCY_UNKNOWN of type Fwupd.ReleaseUrgency>, 'LOW': <enum FWUPD_RELEASE_URGENCY_LOW of type Fwupd.ReleaseUrgency>, 'MEDIUM': <enum FWUPD_RELEASE_URGENCY_MEDIUM of type Fwupd.ReleaseUrgency>, 'HIGH': <enum FWUPD_RELEASE_URGENCY_HIGH of type Fwupd.ReleaseUrgency>, 'CRITICAL': <enum FWUPD_RELEASE_URGENCY_CRITICAL of type Fwupd.ReleaseUrgency>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdReleaseUrgency (94734970106160)>'
    __info__ = gi.EnumInfo(ReleaseUrgency)


class Remote(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Remote(**properties)
        new() -> Fwupd.Remote
    """
    def array_from_variant(self, value): # real signature unknown; restored from __doc__
        """ array_from_variant(value:GLib.Variant) -> list """
        return []

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def build_firmware_uri(self, url): # real signature unknown; restored from __doc__
        """ build_firmware_uri(self, url:str) -> str """
        return ""

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

    def from_variant(self, value): # real signature unknown; restored from __doc__
        """ from_variant(value:GLib.Variant) -> Fwupd.Remote """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_age(self): # real signature unknown; restored from __doc__
        """ get_age(self) -> int """
        return 0

    def get_agreement(self): # real signature unknown; restored from __doc__
        """ get_agreement(self) -> str """
        return ""

    def get_approval_required(self): # real signature unknown; restored from __doc__
        """ get_approval_required(self) -> bool """
        return False

    def get_automatic_reports(self): # real signature unknown; restored from __doc__
        """ get_automatic_reports(self) -> bool """
        return False

    def get_checksum(self): # real signature unknown; restored from __doc__
        """ get_checksum(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_enabled(self): # real signature unknown; restored from __doc__
        """ get_enabled(self) -> bool """
        return False

    def get_filename_cache(self): # real signature unknown; restored from __doc__
        """ get_filename_cache(self) -> str """
        return ""

    def get_filename_cache_sig(self): # real signature unknown; restored from __doc__
        """ get_filename_cache_sig(self) -> str """
        return ""

    def get_filename_source(self): # real signature unknown; restored from __doc__
        """ get_filename_source(self) -> str """
        return ""

    def get_firmware_base_uri(self): # real signature unknown; restored from __doc__
        """ get_firmware_base_uri(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_keyring_kind(self): # real signature unknown; restored from __doc__
        """ get_keyring_kind(self) -> Fwupd.KeyringKind """
        pass

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> Fwupd.RemoteKind """
        pass

    def get_metadata_uri(self): # real signature unknown; restored from __doc__
        """ get_metadata_uri(self) -> str """
        return ""

    def get_metadata_uri_sig(self): # real signature unknown; restored from __doc__
        """ get_metadata_uri_sig(self) -> str """
        return ""

    def get_order_after(self): # real signature unknown; restored from __doc__
        """ get_order_after(self) -> list """
        return []

    def get_order_before(self): # real signature unknown; restored from __doc__
        """ get_order_before(self) -> list """
        return []

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str """
        return ""

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

    def get_remotes_dir(self): # real signature unknown; restored from __doc__
        """ get_remotes_dir(self) -> str """
        return ""

    def get_report_uri(self): # real signature unknown; restored from __doc__
        """ get_report_uri(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_username(self): # real signature unknown; restored from __doc__
        """ get_username(self) -> str """
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

    def kind_from_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_from_string(kind:str) -> Fwupd.RemoteKind """
        pass

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:Fwupd.RemoteKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load_from_filename(self, filename, cancellable=None): # real signature unknown; restored from __doc__
        """ load_from_filename(self, filename:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def load_signature(self, filename): # real signature unknown; restored from __doc__
        """ load_signature(self, filename:str) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Fwupd.Remote """
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

    def set_agreement(self, agreement): # real signature unknown; restored from __doc__
        """ set_agreement(self, agreement:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_mtime(self, mtime): # real signature unknown; restored from __doc__
        """ set_mtime(self, mtime:int) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_remotes_dir(self, directory): # real signature unknown; restored from __doc__
        """ set_remotes_dir(self, directory:str) """
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

    def to_variant(self): # real signature unknown; restored from __doc__
        """ to_variant(self) -> GLib.Variant """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f66f43eca60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Remote), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType FwupdRemote (94734970151408)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'array_from_variant': gi.FunctionInfo(array_from_variant), 'from_variant': gi.FunctionInfo(from_variant), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'build_firmware_uri': gi.FunctionInfo(build_firmware_uri), 'get_age': gi.FunctionInfo(get_age), 'get_agreement': gi.FunctionInfo(get_agreement), 'get_approval_required': gi.FunctionInfo(get_approval_required), 'get_automatic_reports': gi.FunctionInfo(get_automatic_reports), 'get_checksum': gi.FunctionInfo(get_checksum), 'get_enabled': gi.FunctionInfo(get_enabled), 'get_filename_cache': gi.FunctionInfo(get_filename_cache), 'get_filename_cache_sig': gi.FunctionInfo(get_filename_cache_sig), 'get_filename_source': gi.FunctionInfo(get_filename_source), 'get_firmware_base_uri': gi.FunctionInfo(get_firmware_base_uri), 'get_id': gi.FunctionInfo(get_id), 'get_keyring_kind': gi.FunctionInfo(get_keyring_kind), 'get_kind': gi.FunctionInfo(get_kind), 'get_metadata_uri': gi.FunctionInfo(get_metadata_uri), 'get_metadata_uri_sig': gi.FunctionInfo(get_metadata_uri_sig), 'get_order_after': gi.FunctionInfo(get_order_after), 'get_order_before': gi.FunctionInfo(get_order_before), 'get_password': gi.FunctionInfo(get_password), 'get_priority': gi.FunctionInfo(get_priority), 'get_remotes_dir': gi.FunctionInfo(get_remotes_dir), 'get_report_uri': gi.FunctionInfo(get_report_uri), 'get_title': gi.FunctionInfo(get_title), 'get_username': gi.FunctionInfo(get_username), 'load_from_filename': gi.FunctionInfo(load_from_filename), 'load_signature': gi.FunctionInfo(load_signature), 'set_agreement': gi.FunctionInfo(set_agreement), 'set_mtime': gi.FunctionInfo(set_mtime), 'set_priority': gi.FunctionInfo(set_priority), 'set_remotes_dir': gi.FunctionInfo(set_remotes_dir), 'to_variant': gi.FunctionInfo(to_variant), 'parent_instance': <property object at 0x7f66f43e2f90>})"
    __gdoc__ = 'Object FwupdRemote\n\nProperties from FwupdRemote:\n  id -> gchararray: id\n  enabled -> gboolean: enabled\n  approval-required -> gboolean: approval-required\n  automatic-reports -> gboolean: automatic-reports\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType FwupdRemote (94734970151408)>'
    __info__ = ObjectInfo(Remote)


class RemoteClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RemoteClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _fwupd_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RemoteClass), '__module__': 'gi.repository.Fwupd', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RemoteClass' objects>, '__weakref__': <attribute '__weakref__' of 'RemoteClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f66f43e4180>, '_fwupd_reserved1': <property object at 0x7f66f43e42c0>, '_fwupd_reserved2': <property object at 0x7f66f43e43b0>, '_fwupd_reserved3': <property object at 0x7f66f43e44a0>, '_fwupd_reserved4': <property object at 0x7f66f43e4590>, '_fwupd_reserved5': <property object at 0x7f66f43e4680>, '_fwupd_reserved6': <property object at 0x7f66f43e4770>, '_fwupd_reserved7': <property object at 0x7f66f43e4860>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RemoteClass)


class RemoteKind(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DIRECTORY = 3
    DOWNLOAD = 1
    LOCAL = 2
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'RemoteKind' objects>, '__doc__': None, '__gtype__': <GType PyFwupdRemoteKind (94734970161824)>, '__enum_values__': {0: <enum FWUPD_REMOTE_KIND_UNKNOWN of type Fwupd.RemoteKind>, 1: <enum FWUPD_REMOTE_KIND_DOWNLOAD of type Fwupd.RemoteKind>, 2: <enum FWUPD_REMOTE_KIND_LOCAL of type Fwupd.RemoteKind>, 3: <enum FWUPD_REMOTE_KIND_DIRECTORY of type Fwupd.RemoteKind>}, '__info__': gi.EnumInfo(RemoteKind), 'UNKNOWN': <enum FWUPD_REMOTE_KIND_UNKNOWN of type Fwupd.RemoteKind>, 'DOWNLOAD': <enum FWUPD_REMOTE_KIND_DOWNLOAD of type Fwupd.RemoteKind>, 'LOCAL': <enum FWUPD_REMOTE_KIND_LOCAL of type Fwupd.RemoteKind>, 'DIRECTORY': <enum FWUPD_REMOTE_KIND_DIRECTORY of type Fwupd.RemoteKind>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdRemoteKind (94734970161824)>'
    __info__ = gi.EnumInfo(RemoteKind)


class SelfSignFlags(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ADD_CERT = 2
    ADD_TIMESTAMP = 1
    NONE = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'SelfSignFlags' objects>, '__doc__': None, '__gtype__': <GType PyFwupdSelfSignFlags (94734970163984)>, '__flags_values__': {0: <flags 0 of type Fwupd.SelfSignFlags>, 1: <flags FWUPD_SELF_SIGN_FLAG_ADD_TIMESTAMP of type Fwupd.SelfSignFlags>, 2: <flags FWUPD_SELF_SIGN_FLAG_ADD_CERT of type Fwupd.SelfSignFlags>}, '__info__': gi.EnumInfo(SelfSignFlags), 'NONE': <flags 0 of type Fwupd.SelfSignFlags>, 'ADD_TIMESTAMP': <flags FWUPD_SELF_SIGN_FLAG_ADD_TIMESTAMP of type Fwupd.SelfSignFlags>, 'ADD_CERT': <flags FWUPD_SELF_SIGN_FLAG_ADD_CERT of type Fwupd.SelfSignFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdSelfSignFlags (94734970163984)>'
    __info__ = gi.EnumInfo(SelfSignFlags)


class Status(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DECOMPRESSING = 3
    DEVICE_BUSY = 12
    DEVICE_ERASE = 10
    DEVICE_READ = 9
    DEVICE_RESTART = 4
    DEVICE_VERIFY = 6
    DEVICE_WRITE = 5
    DOWNLOADING = 8
    IDLE = 1
    LOADING = 2
    SCHEDULING = 7
    SHUTDOWN = 13
    UNKNOWN = 0
    WAITING_FOR_AUTH = 11
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'Status' objects>, '__doc__': None, '__gtype__': <GType PyFwupdStatus (94734970165968)>, '__enum_values__': {0: <enum FWUPD_STATUS_UNKNOWN of type Fwupd.Status>, 1: <enum FWUPD_STATUS_IDLE of type Fwupd.Status>, 2: <enum FWUPD_STATUS_LOADING of type Fwupd.Status>, 3: <enum FWUPD_STATUS_DECOMPRESSING of type Fwupd.Status>, 4: <enum FWUPD_STATUS_DEVICE_RESTART of type Fwupd.Status>, 5: <enum FWUPD_STATUS_DEVICE_WRITE of type Fwupd.Status>, 6: <enum FWUPD_STATUS_DEVICE_VERIFY of type Fwupd.Status>, 7: <enum FWUPD_STATUS_SCHEDULING of type Fwupd.Status>, 8: <enum FWUPD_STATUS_DOWNLOADING of type Fwupd.Status>, 9: <enum FWUPD_STATUS_DEVICE_READ of type Fwupd.Status>, 10: <enum FWUPD_STATUS_DEVICE_ERASE of type Fwupd.Status>, 11: <enum FWUPD_STATUS_WAITING_FOR_AUTH of type Fwupd.Status>, 12: <enum FWUPD_STATUS_DEVICE_BUSY of type Fwupd.Status>, 13: <enum FWUPD_STATUS_SHUTDOWN of type Fwupd.Status>}, '__info__': gi.EnumInfo(Status), 'UNKNOWN': <enum FWUPD_STATUS_UNKNOWN of type Fwupd.Status>, 'IDLE': <enum FWUPD_STATUS_IDLE of type Fwupd.Status>, 'LOADING': <enum FWUPD_STATUS_LOADING of type Fwupd.Status>, 'DECOMPRESSING': <enum FWUPD_STATUS_DECOMPRESSING of type Fwupd.Status>, 'DEVICE_RESTART': <enum FWUPD_STATUS_DEVICE_RESTART of type Fwupd.Status>, 'DEVICE_WRITE': <enum FWUPD_STATUS_DEVICE_WRITE of type Fwupd.Status>, 'DEVICE_VERIFY': <enum FWUPD_STATUS_DEVICE_VERIFY of type Fwupd.Status>, 'SCHEDULING': <enum FWUPD_STATUS_SCHEDULING of type Fwupd.Status>, 'DOWNLOADING': <enum FWUPD_STATUS_DOWNLOADING of type Fwupd.Status>, 'DEVICE_READ': <enum FWUPD_STATUS_DEVICE_READ of type Fwupd.Status>, 'DEVICE_ERASE': <enum FWUPD_STATUS_DEVICE_ERASE of type Fwupd.Status>, 'WAITING_FOR_AUTH': <enum FWUPD_STATUS_WAITING_FOR_AUTH of type Fwupd.Status>, 'DEVICE_BUSY': <enum FWUPD_STATUS_DEVICE_BUSY of type Fwupd.Status>, 'SHUTDOWN': <enum FWUPD_STATUS_SHUTDOWN of type Fwupd.Status>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdStatus (94734970165968)>'
    __info__ = gi.EnumInfo(Status)


class TrustFlags(__gobject.GFlags):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
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

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    METADATA = 2
    NONE = 0
    PAYLOAD = 1
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'TrustFlags' objects>, '__doc__': None, '__gtype__': <GType PyFwupdTrustFlags (94734970168000)>, '__flags_values__': {0: <flags 0 of type Fwupd.TrustFlags>, 1: <flags FWUPD_TRUST_FLAG_PAYLOAD of type Fwupd.TrustFlags>, 2: <flags FWUPD_TRUST_FLAG_METADATA of type Fwupd.TrustFlags>}, '__info__': gi.EnumInfo(TrustFlags), 'NONE': <flags 0 of type Fwupd.TrustFlags>, 'PAYLOAD': <flags FWUPD_TRUST_FLAG_PAYLOAD of type Fwupd.TrustFlags>, 'METADATA': <flags FWUPD_TRUST_FLAG_METADATA of type Fwupd.TrustFlags>})"
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdTrustFlags (94734970168000)>'
    __info__ = gi.EnumInfo(TrustFlags)


class UpdateState(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    FAILED = 3
    FAILED_TRANSIENT = 5
    NEEDS_REBOOT = 4
    PENDING = 1
    SUCCESS = 2
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'UpdateState' objects>, '__doc__': None, '__gtype__': <GType PyFwupdUpdateState (94734970174112)>, '__enum_values__': {0: <enum FWUPD_UPDATE_STATE_UNKNOWN of type Fwupd.UpdateState>, 1: <enum FWUPD_UPDATE_STATE_PENDING of type Fwupd.UpdateState>, 2: <enum FWUPD_UPDATE_STATE_SUCCESS of type Fwupd.UpdateState>, 3: <enum FWUPD_UPDATE_STATE_FAILED of type Fwupd.UpdateState>, 4: <enum FWUPD_UPDATE_STATE_NEEDS_REBOOT of type Fwupd.UpdateState>, 5: <enum FWUPD_UPDATE_STATE_FAILED_TRANSIENT of type Fwupd.UpdateState>}, '__info__': gi.EnumInfo(UpdateState), 'UNKNOWN': <enum FWUPD_UPDATE_STATE_UNKNOWN of type Fwupd.UpdateState>, 'PENDING': <enum FWUPD_UPDATE_STATE_PENDING of type Fwupd.UpdateState>, 'SUCCESS': <enum FWUPD_UPDATE_STATE_SUCCESS of type Fwupd.UpdateState>, 'FAILED': <enum FWUPD_UPDATE_STATE_FAILED of type Fwupd.UpdateState>, 'NEEDS_REBOOT': <enum FWUPD_UPDATE_STATE_NEEDS_REBOOT of type Fwupd.UpdateState>, 'FAILED_TRANSIENT': <enum FWUPD_UPDATE_STATE_FAILED_TRANSIENT of type Fwupd.UpdateState>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdUpdateState (94734970174112)>'
    __info__ = gi.EnumInfo(UpdateState)


class VersionFormat(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BCD = 6
    DELL_BIOS = 11
    HEX = 12
    INTEL_ME = 7
    INTEL_ME2 = 8
    NUMBER = 2
    PAIR = 3
    PLAIN = 1
    QUAD = 5
    SURFACE = 10
    SURFACE_LEGACY = 9
    TRIPLET = 4
    UNKNOWN = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Fwupd', '__dict__': <attribute '__dict__' of 'VersionFormat' objects>, '__doc__': None, '__gtype__': <GType PyFwupdVersionFormat (94734970176416)>, '__enum_values__': {0: <enum FWUPD_VERSION_FORMAT_UNKNOWN of type Fwupd.VersionFormat>, 1: <enum FWUPD_VERSION_FORMAT_PLAIN of type Fwupd.VersionFormat>, 2: <enum FWUPD_VERSION_FORMAT_NUMBER of type Fwupd.VersionFormat>, 3: <enum FWUPD_VERSION_FORMAT_PAIR of type Fwupd.VersionFormat>, 4: <enum FWUPD_VERSION_FORMAT_TRIPLET of type Fwupd.VersionFormat>, 5: <enum FWUPD_VERSION_FORMAT_QUAD of type Fwupd.VersionFormat>, 6: <enum FWUPD_VERSION_FORMAT_BCD of type Fwupd.VersionFormat>, 7: <enum FWUPD_VERSION_FORMAT_INTEL_ME of type Fwupd.VersionFormat>, 8: <enum FWUPD_VERSION_FORMAT_INTEL_ME2 of type Fwupd.VersionFormat>, 9: <enum FWUPD_VERSION_FORMAT_SURFACE_LEGACY of type Fwupd.VersionFormat>, 10: <enum FWUPD_VERSION_FORMAT_SURFACE of type Fwupd.VersionFormat>, 11: <enum FWUPD_VERSION_FORMAT_DELL_BIOS of type Fwupd.VersionFormat>, 12: <enum FWUPD_VERSION_FORMAT_HEX of type Fwupd.VersionFormat>}, '__info__': gi.EnumInfo(VersionFormat), 'UNKNOWN': <enum FWUPD_VERSION_FORMAT_UNKNOWN of type Fwupd.VersionFormat>, 'PLAIN': <enum FWUPD_VERSION_FORMAT_PLAIN of type Fwupd.VersionFormat>, 'NUMBER': <enum FWUPD_VERSION_FORMAT_NUMBER of type Fwupd.VersionFormat>, 'PAIR': <enum FWUPD_VERSION_FORMAT_PAIR of type Fwupd.VersionFormat>, 'TRIPLET': <enum FWUPD_VERSION_FORMAT_TRIPLET of type Fwupd.VersionFormat>, 'QUAD': <enum FWUPD_VERSION_FORMAT_QUAD of type Fwupd.VersionFormat>, 'BCD': <enum FWUPD_VERSION_FORMAT_BCD of type Fwupd.VersionFormat>, 'INTEL_ME': <enum FWUPD_VERSION_FORMAT_INTEL_ME of type Fwupd.VersionFormat>, 'INTEL_ME2': <enum FWUPD_VERSION_FORMAT_INTEL_ME2 of type Fwupd.VersionFormat>, 'SURFACE_LEGACY': <enum FWUPD_VERSION_FORMAT_SURFACE_LEGACY of type Fwupd.VersionFormat>, 'SURFACE': <enum FWUPD_VERSION_FORMAT_SURFACE of type Fwupd.VersionFormat>, 'DELL_BIOS': <enum FWUPD_VERSION_FORMAT_DELL_BIOS of type Fwupd.VersionFormat>, 'HEX': <enum FWUPD_VERSION_FORMAT_HEX of type Fwupd.VersionFormat>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
    }
    __gtype__ = None # (!) real value is '<GType PyFwupdVersionFormat (94734970176416)>'
    __info__ = gi.EnumInfo(VersionFormat)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f66f46221f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f66f4622280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f66f4622310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f66f46223a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f66f525ed00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Fwupd-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Fwupd', loader=<gi.importer.DynamicImporter object at 0x7f66f525ed00>)"

