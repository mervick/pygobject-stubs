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


# Variables with simple values

BUILD_HASH = '5367246fb4838e97209f30d30ddffb6cb9887e54300edfab66491368e6ff0ca6'

DEVICE_METADATA_TBT_CAN_FORCE_POWER = 'Thunderbolt::CanForcePower'

DEVICE_METADATA_TBT_IS_SAFE_MODE = 'Thunderbolt::IsSafeMode'

DEVICE_METADATA_UEFI_CAPSULE_FLAGS = 'UefiCapsuleFlags'

DEVICE_METADATA_UEFI_DEVICE_KIND = 'UefiDeviceKind'

DEVICE_METADATA_UEFI_FW_VERSION = 'UefiFwVersion'

DEVICE_REMOVE_DELAY_RE_ENUMERATE = 10000

DEVICE_REMOVE_DELAY_USER_REPLUG = 40000

EFIVAR_ATTR_APPEND_WRITE = 64

EFIVAR_ATTR_AUTHENTICATED_WRITE_ACCESS = 16

EFIVAR_ATTR_BOOTSERVICE_ACCESS = 2

EFIVAR_ATTR_HARDWARE_ERROR_RECORD = 8

EFIVAR_ATTR_NON_VOLATILE = 1

EFIVAR_ATTR_RUNTIME_ACCESS = 4

EFIVAR_ATTR_TIME_BASED_AUTHENTICATED_WRITE_ACCESS = 5

EFIVAR_GUID_EFI_GLOBAL = '8be4df61-93ca-11d2-aa0d-00e098032b8c'

EFIVAR_GUID_FWUPDATE = '0abba7dc-e516-4167-bbf5-4d9d1c739416'

EFIVAR_GUID_UX_CAPSULE = '3b8c8162-188c-46a4-aec9-be43f1d65697'

FIRMWARE_IMAGE_ID_HEADER = 'header'
FIRMWARE_IMAGE_ID_PAYLOAD = 'payload'
FIRMWARE_IMAGE_ID_SIGNATURE = 'signature'

HWIDS_KEY_BASEBOARD_MANUFACTURER = 'BaseboardManufacturer'
HWIDS_KEY_BASEBOARD_PRODUCT = 'BaseboardProduct'

HWIDS_KEY_BIOS_MAJOR_RELEASE = 'BiosMajorRelease'

HWIDS_KEY_BIOS_MINOR_RELEASE = 'BiosMinorRelease'

HWIDS_KEY_BIOS_VENDOR = 'BiosVendor'
HWIDS_KEY_BIOS_VERSION = 'BiosVersion'

HWIDS_KEY_ENCLOSURE_KIND = 'EnclosureKind'

HWIDS_KEY_FAMILY = 'Family'
HWIDS_KEY_MANUFACTURER = 'Manufacturer'

HWIDS_KEY_PRODUCT_NAME = 'ProductName'
HWIDS_KEY_PRODUCT_SKU = 'ProductSku'

QUIRKS_CHILDREN = 'Children'

QUIRKS_COUNTERPART_GUID = 'CounterpartGuid'

QUIRKS_FIRMWARE_SIZE = 'FirmwareSize'

QUIRKS_FIRMWARE_SIZE_MAX = 'FirmwareSizeMax'
QUIRKS_FIRMWARE_SIZE_MIN = 'FirmwareSizeMin'

QUIRKS_FLAGS = 'Flags'
QUIRKS_GTYPE = 'GType'
QUIRKS_GUID = 'Guid'
QUIRKS_ICON = 'Icon'

QUIRKS_INSTALL_DURATION = 'InstallDuration'

QUIRKS_NAME = 'Name'

QUIRKS_PARENT_GUID = 'ParentGuid'

QUIRKS_PLUGIN = 'Plugin'
QUIRKS_PRIORITY = 'Priority'
QUIRKS_PROTOCOL = 'Protocol'

QUIRKS_PROXY_GUID = 'ProxyGuid'

QUIRKS_SUMMARY = 'Summary'

QUIRKS_UPDATE_MESSAGE = 'UpdateMessage'

QUIRKS_VENDOR = 'Vendor'

QUIRKS_VENDOR_ID = 'VendorId'

QUIRKS_VERSION = 'Version'

QUIRKS_VERSION_FORMAT = 'VersionFormat'

SMBIOS_STRUCTURE_TYPE_BASEBOARD = 2
SMBIOS_STRUCTURE_TYPE_BIOS = 0
SMBIOS_STRUCTURE_TYPE_CHASSIS = 3
SMBIOS_STRUCTURE_TYPE_SYSTEM = 1

_namespace = 'FwupdPlugin'

_version = '1.0'

__weakref__ = None

# functions

def byte_array_append_uint16(array, data, endian): # real signature unknown; restored from __doc__
    """ byte_array_append_uint16(array:list, data:int, endian:int) """
    pass

def byte_array_append_uint32(array, data, endian): # real signature unknown; restored from __doc__
    """ byte_array_append_uint32(array:list, data:int, endian:int) """
    pass

def byte_array_append_uint8(array, data): # real signature unknown; restored from __doc__
    """ byte_array_append_uint8(array:list, data:int) """
    pass

def chunk_array_to_string(chunks): # real signature unknown; restored from __doc__
    """ chunk_array_to_string(chunks:list) -> str """
    return ""

def common_bytes_align(bytes, blksz, padval): # real signature unknown; restored from __doc__
    """ common_bytes_align(bytes:GLib.Bytes, blksz:int, padval:int) -> GLib.Bytes """
    pass

def common_bytes_compare(bytes1, bytes2): # real signature unknown; restored from __doc__
    """ common_bytes_compare(bytes1:GLib.Bytes, bytes2:GLib.Bytes) -> bool """
    return False

def common_bytes_compare_raw(buf1, bufsz1, buf2, bufsz2): # real signature unknown; restored from __doc__
    """ common_bytes_compare_raw(buf1:int, bufsz1:int, buf2:int, bufsz2:int) -> bool """
    return False

def common_bytes_is_empty(bytes): # real signature unknown; restored from __doc__
    """ common_bytes_is_empty(bytes:GLib.Bytes) -> bool """
    return False

def common_bytes_pad(bytes, sz): # real signature unknown; restored from __doc__
    """ common_bytes_pad(bytes:GLib.Bytes, sz:int) -> GLib.Bytes """
    pass

def common_dump_bytes(log_domain, title, bytes): # real signature unknown; restored from __doc__
    """ common_dump_bytes(log_domain:str, title:str, bytes:GLib.Bytes) """
    pass

def common_dump_full(log_domain, title, data, len, columns, flags): # real signature unknown; restored from __doc__
    """ common_dump_full(log_domain:str, title:str, data:int, len:int, columns:int, flags:FwupdPlugin.DumpFlags) """
    pass

def common_dump_raw(log_domain, title, data, len): # real signature unknown; restored from __doc__
    """ common_dump_raw(log_domain:str, title:str, data:int, len:int) """
    pass

def common_error_array_get_best(errors): # real signature unknown; restored from __doc__
    """ common_error_array_get_best(errors:list) -> error """
    pass

def common_extract_archive(blob, dir): # real signature unknown; restored from __doc__
    """ common_extract_archive(blob:GLib.Bytes, dir:str) -> bool """
    return False

def common_find_program_in_path(basename): # real signature unknown; restored from __doc__
    """ common_find_program_in_path(basename:str) -> str """
    return ""

def common_firmware_builder(bytes, script_fn, output_fn): # real signature unknown; restored from __doc__
    """ common_firmware_builder(bytes:GLib.Bytes, script_fn:str, output_fn:str) -> GLib.Bytes """
    pass

def common_fnmatch(pattern, p_str): # real signature unknown; restored from __doc__
    """ common_fnmatch(pattern:str, str:str) -> bool """
    return False

def common_get_contents_bytes(filename): # real signature unknown; restored from __doc__
    """ common_get_contents_bytes(filename:str) -> GLib.Bytes """
    pass

def common_get_contents_fd(fd, count): # real signature unknown; restored from __doc__
    """ common_get_contents_fd(fd:int, count:int) -> GLib.Bytes """
    pass

def common_get_files_recursive(path): # real signature unknown; restored from __doc__
    """ common_get_files_recursive(path:str) -> list """
    return []

def common_get_path(path_kind): # real signature unknown; restored from __doc__
    """ common_get_path(path_kind:FwupdPlugin.PathKind) -> str """
    return ""

def common_guid_is_plausible(buf): # real signature unknown; restored from __doc__
    """ common_guid_is_plausible(buf:int) -> bool """
    return False

def common_kernel_locked_down(): # real signature unknown; restored from __doc__
    """ common_kernel_locked_down() -> bool """
    return False

def common_mkdir_parent(filename): # real signature unknown; restored from __doc__
    """ common_mkdir_parent(filename:str) -> bool """
    return False

def common_read_uint16(buf, endian): # real signature unknown; restored from __doc__
    """ common_read_uint16(buf:int, endian:int) -> int """
    return 0

def common_read_uint16_safe(buf, bufsz, offset, endian): # real signature unknown; restored from __doc__
    """ common_read_uint16_safe(buf:int, bufsz:int, offset:int, endian:int) -> bool, value:int """
    return False

def common_read_uint32(buf, endian): # real signature unknown; restored from __doc__
    """ common_read_uint32(buf:int, endian:int) -> int """
    return 0

def common_read_uint32_safe(buf, bufsz, offset, endian): # real signature unknown; restored from __doc__
    """ common_read_uint32_safe(buf:int, bufsz:int, offset:int, endian:int) -> bool, value:int """
    return False

def common_read_uint8_safe(buf, bufsz, offset): # real signature unknown; restored from __doc__
    """ common_read_uint8_safe(buf:int, bufsz:int, offset:int) -> bool, value:int """
    return False

def common_realpath(filename): # real signature unknown; restored from __doc__
    """ common_realpath(filename:str) -> str """
    return ""

def common_rmtree(directory): # real signature unknown; restored from __doc__
    """ common_rmtree(directory:str) -> bool """
    return False

def common_set_contents_bytes(filename, bytes): # real signature unknown; restored from __doc__
    """ common_set_contents_bytes(filename:str, bytes:GLib.Bytes) -> bool """
    return False

def common_spawn_sync(argv, handler_cb, handler_user_data=None, timeout_ms, cancellable=None): # real signature unknown; restored from __doc__
    """ common_spawn_sync(argv:str, handler_cb:FwupdPlugin.OutputHandler, handler_user_data=None, timeout_ms:int, cancellable:Gio.Cancellable=None) -> bool """
    return False

def common_string_append_kb(p_str, idt, key, value): # real signature unknown; restored from __doc__
    """ common_string_append_kb(str:GLib.String, idt:int, key:str, value:bool) """
    pass

def common_string_append_ku(p_str, idt, key, value): # real signature unknown; restored from __doc__
    """ common_string_append_ku(str:GLib.String, idt:int, key:str, value:int) """
    pass

def common_string_append_kv(p_str, idt, key, value): # real signature unknown; restored from __doc__
    """ common_string_append_kv(str:GLib.String, idt:int, key:str, value:str) """
    pass

def common_string_append_kx(p_str, idt, key, value): # real signature unknown; restored from __doc__
    """ common_string_append_kx(str:GLib.String, idt:int, key:str, value:int) """
    pass

def common_string_replace(string, search, replace): # real signature unknown; restored from __doc__
    """ common_string_replace(string:GLib.String, search:str, replace:str) -> int """
    return 0

def common_strnsplit(p_str, sz, delimiter, max_tokens): # real signature unknown; restored from __doc__
    """ common_strnsplit(str:str, sz:int, delimiter:str, max_tokens:int) -> list """
    return []

def common_strstrip(p_str): # real signature unknown; restored from __doc__
    """ common_strstrip(str:str) -> str """
    return ""

def common_strtoull(p_str): # real signature unknown; restored from __doc__
    """ common_strtoull(str:str) -> int """
    return 0

def common_strwidth(text): # real signature unknown; restored from __doc__
    """ common_strwidth(text:str) -> int """
    return 0

def common_vercmp(version_a, version_b): # real signature unknown; restored from __doc__
    """ common_vercmp(version_a:str, version_b:str) -> int """
    return 0

def common_vercmp_full(version_a, version_b, fmt): # real signature unknown; restored from __doc__
    """ common_vercmp_full(version_a:str, version_b:str, fmt:Fwupd.VersionFormat) -> int """
    return 0

def common_version_ensure_semver(version): # real signature unknown; restored from __doc__
    """ common_version_ensure_semver(version:str) -> str """
    return ""

def common_version_from_uint16(val, kind): # real signature unknown; restored from __doc__
    """ common_version_from_uint16(val:int, kind:Fwupd.VersionFormat) -> str """
    return ""

def common_version_from_uint32(val, kind): # real signature unknown; restored from __doc__
    """ common_version_from_uint32(val:int, kind:Fwupd.VersionFormat) -> str """
    return ""

def common_version_from_uint64(val, kind): # real signature unknown; restored from __doc__
    """ common_version_from_uint64(val:int, kind:Fwupd.VersionFormat) -> str """
    return ""

def common_version_guess_format(version): # real signature unknown; restored from __doc__
    """ common_version_guess_format(version:str) -> Fwupd.VersionFormat """
    pass

def common_version_parse(version): # real signature unknown; restored from __doc__
    """ common_version_parse(version:str) -> str """
    return ""

def common_version_parse_from_format(version, fmt): # real signature unknown; restored from __doc__
    """ common_version_parse_from_format(version:str, fmt:Fwupd.VersionFormat) -> str """
    return ""

def common_version_verify_format(version, fmt): # real signature unknown; restored from __doc__
    """ common_version_verify_format(version:str, fmt:Fwupd.VersionFormat) -> bool """
    return False

def common_write_uint16(buf, val_native, endian): # real signature unknown; restored from __doc__
    """ common_write_uint16(buf:int, val_native:int, endian:int) """
    pass

def common_write_uint32(buf, val_native, endian): # real signature unknown; restored from __doc__
    """ common_write_uint32(buf:int, val_native:int, endian:int) """
    pass

def efivar_delete(guid, name): # real signature unknown; restored from __doc__
    """ efivar_delete(guid:str, name:str) -> bool """
    return False

def efivar_delete_with_glob(guid, name_glob): # real signature unknown; restored from __doc__
    """ efivar_delete_with_glob(guid:str, name_glob:str) -> bool """
    return False

def efivar_exists(guid, name): # real signature unknown; restored from __doc__
    """ efivar_exists(guid:str, name:str) -> bool """
    return False

def efivar_get_data(guid, name, data, data_sz, attr): # real signature unknown; restored from __doc__
    """ efivar_get_data(guid:str, name:str, data:int, data_sz:int, attr:int) -> bool """
    return False

def efivar_secure_boot_enabled(): # real signature unknown; restored from __doc__
    """ efivar_secure_boot_enabled() -> bool """
    return False

def efivar_set_data(guid, name, data, sz, attr): # real signature unknown; restored from __doc__
    """ efivar_set_data(guid:str, name:str, data:int, sz:int, attr:int) -> bool """
    return False

def efivar_supported(): # real signature unknown; restored from __doc__
    """ efivar_supported() -> bool """
    return False

def memcpy_safe(dst, dst_sz, dst_offset, src, src_sz, src_offset, n): # real signature unknown; restored from __doc__
    """ memcpy_safe(dst:int, dst_sz:int, dst_offset:int, src:int, src_sz:int, src_offset:int, n:int) -> bool """
    return False

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

from .AppFlags import AppFlags
from .Archive import Archive
from .ArchiveClass import ArchiveClass
from .ArchiveFlags import ArchiveFlags
from .Cabinet import Cabinet
from .CabinetClass import CabinetClass
from .CabinetParseFlags import CabinetParseFlags
from .Chunk import Chunk
from .Device import Device
from .DeviceClass import DeviceClass
from .DeviceInstanceFlags import DeviceInstanceFlags
from .DeviceLocker import DeviceLocker
from .DeviceLockerClass import DeviceLockerClass
from .Firmware import Firmware
from .DfuFirmware import DfuFirmware
from .DfuFirmwareClass import DfuFirmwareClass
from .DumpFlags import DumpFlags
from .FirmareSrecRecordKind import FirmareSrecRecordKind
from .FirmwareClass import FirmwareClass
from .FirmwareImage import FirmwareImage
from .FirmwareImageClass import FirmwareImageClass
from .UsbDevice import UsbDevice
from .HidDevice import HidDevice
from .HidDeviceClass import HidDeviceClass
from .HidDeviceFlags import HidDeviceFlags
from .Hwids import Hwids
from .HwidsClass import HwidsClass
from .IhexFirmware import IhexFirmware
from .IhexFirmwareClass import IhexFirmwareClass
from .IhexFirmwareRecord import IhexFirmwareRecord
from .IOChannel import IOChannel
from .IOChannelClass import IOChannelClass
from .IOChannelFlags import IOChannelFlags
from .PathKind import PathKind
from .Plugin import Plugin
from .PluginClass import PluginClass
from .PluginData import PluginData
from .PluginRule import PluginRule
from .PluginVerifyFlags import PluginVerifyFlags
from .Quirks import Quirks
from .QuirksClass import QuirksClass
from .QuirksLoadFlags import QuirksLoadFlags
from .Smbios import Smbios
from .SmbiosClass import SmbiosClass
from .SrecFirmware import SrecFirmware
from .SrecFirmwareClass import SrecFirmwareClass
from .SrecFirmwareRecord import SrecFirmwareRecord
from .UdevDevice import UdevDevice
from .UdevDeviceClass import UdevDeviceClass
from .UdevDeviceFlags import UdevDeviceFlags
from .UsbDeviceClass import UsbDeviceClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7feb1be73d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/FwupdPlugin-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.FwupdPlugin', loader=<gi.importer.DynamicImporter object at 0x7feb1be73d00>)"

