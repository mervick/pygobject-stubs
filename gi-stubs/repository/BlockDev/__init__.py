# encoding: utf-8
# module gi.repository.BlockDev
# from /usr/lib64/girepository-1.0/BlockDev-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.BlockDev as __gi_overrides_BlockDev
import gobject as __gobject


# Variables with simple values

BTRFS_MAIN_VOLUME_ID = 5

BTRFS_MIN_MEMBER_SIZE = 134217728

CRYPTO_LUKS_METADATA_SIZE = 2097152

LVM_DEFAULT_CHUNK_SIZE = 65536

LVM_DEFAULT_PE_SIZE = 4194304
LVM_DEFAULT_PE_START = 1048576

LVM_MAX_LV_SIZE = 9223372036854775808

LVM_MAX_PE_SIZE = 0

LVM_MAX_THPOOL_CHUNK_SIZE = 1073741824

LVM_MAX_THPOOL_MD_SIZE = 0

LVM_MIN_CACHE_MD_SIZE = 8388608

LVM_MIN_PE_SIZE = 1024

LVM_MIN_THPOOL_CHUNK_SIZE = 65536

LVM_MIN_THPOOL_MD_SIZE = 2097152

MD_CHUNK_SIZE = 524288

MD_SUPERBLOCK_SIZE = 2097152

_namespace = 'BlockDev'

_version = '2.0'

__weakref__ = None

# functions

def btrfs_add_device(mountpoint, device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_change_label(mountpoint, label, extra=None): # real signature unknown; restored from __doc__
    """ btrfs_change_label(mountpoint:str, label:str, extra:list=None) -> bool """
    return False

def btrfs_check(mountpoint, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_create_snapshot(source, dest, ro=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_create_subvolume(mountpoint, name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_create_volume(devices, label=None, data_level=None, md_level=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_delete_subvolume(mountpoint, name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_error_quark(): # real signature unknown; restored from __doc__
    """ btrfs_error_quark() -> int """
    return 0

def btrfs_filesystem_info(device): # real signature unknown; restored from __doc__
    """ btrfs_filesystem_info(device:str) -> BlockDev.BtrfsFilesystemInfo """
    pass

def btrfs_get_default_subvolume_id(mountpoint): # real signature unknown; restored from __doc__
    """ btrfs_get_default_subvolume_id(mountpoint:str) -> int """
    return 0

def btrfs_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ btrfs_is_tech_avail(tech:BlockDev.BtrfsTech, mode:int) -> bool """
    return False

def btrfs_list_devices(device): # real signature unknown; restored from __doc__
    """ btrfs_list_devices(device:str) -> list """
    return []

def btrfs_list_subvolumes(mountpoint, snapshots_only=False): # reliably restored by inspect
    # no doc
    pass

def btrfs_mkfs(devices, label=None, data_level=None, md_level=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_remove_device(mountpoint, device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_repair(device, extra=None): # real signature unknown; restored from __doc__
    """ btrfs_repair(device:str, extra:list=None) -> bool """
    return False

def btrfs_resize(mountpoint, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def btrfs_set_default_subvolume(mountpoint, subvol_id, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def crypto_bitlk_close(bitlk_device): # real signature unknown; restored from __doc__
    """ crypto_bitlk_close(bitlk_device:str) -> bool """
    return False

def crypto_bitlk_open(device, name, passphrase, read_only=False): # reliably restored by inspect
    # no doc
    pass

def crypto_device_is_luks(device): # real signature unknown; restored from __doc__
    """ crypto_device_is_luks(device:str) -> bool """
    return False

def crypto_device_seems_encrypted(device): # real signature unknown; restored from __doc__
    """ crypto_device_seems_encrypted(device:str) -> bool """
    return False

def crypto_error_quark(): # real signature unknown; restored from __doc__
    """ crypto_error_quark() -> int """
    return 0

def crypto_escrow_device(device, passphrase, cert_data, directory, backup_passphrase=None): # reliably restored by inspect
    # no doc
    pass

def crypto_generate_backup_passphrase(): # real signature unknown; restored from __doc__
    """ crypto_generate_backup_passphrase() -> str """
    return ""

def crypto_integrity_info(device): # real signature unknown; restored from __doc__
    """ crypto_integrity_info(device:str) -> BlockDev.CryptoIntegrityInfo """
    pass

def crypto_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ crypto_is_tech_avail(tech:BlockDev.CryptoTech, mode:int) -> bool """
    return False

def crypto_luks_add_key(device, pass_=None, key_file=None, npass=None, nkey_file=None): # reliably restored by inspect
    # no doc
    pass

def crypto_luks_add_key_blob(device, pass_data, npass_data): # real signature unknown; restored from __doc__
    """ crypto_luks_add_key_blob(device:str, pass_data:list, npass_data:list) -> bool """
    return False

def crypto_luks_change_key(device, pass_, npass): # real signature unknown; restored from __doc__
    """ crypto_luks_change_key(device:str, pass_:str, npass:str) -> bool """
    return False

def crypto_luks_change_key_blob(device, pass_data, npass_data): # real signature unknown; restored from __doc__
    """ crypto_luks_change_key_blob(device:str, pass_data:list, npass_data:list) -> bool """
    return False

def crypto_luks_close(luks_device): # real signature unknown; restored from __doc__
    """ crypto_luks_close(luks_device:str) -> bool """
    return False

def crypto_luks_format(device, cipher=None, key_size=0, passphrase=None, key_file=None, min_entropy=0, luks_version=0, extra=None): # reliably restored by inspect
    # no doc
    pass

def crypto_luks_format_blob(device, cipher=None, key_size, pass_data, min_entropy): # real signature unknown; restored from __doc__
    """ crypto_luks_format_blob(device:str, cipher:str=None, key_size:int, pass_data:list, min_entropy:int) -> bool """
    return False

def crypto_luks_format_luks2(device, cipher=None, key_size, passphrase=None, key_file=None, min_entropy, luks_version, extra=None): # real signature unknown; restored from __doc__
    """ crypto_luks_format_luks2(device:str, cipher:str=None, key_size:int, passphrase:str=None, key_file:str=None, min_entropy:int, luks_version:BlockDev.CryptoLUKSVersion, extra:BlockDev.CryptoLUKSExtra=None) -> bool """
    return False

def crypto_luks_format_luks2_blob(device, cipher=None, key_size, pass_data, min_entropy, luks_version, extra=None): # real signature unknown; restored from __doc__
    """ crypto_luks_format_luks2_blob(device:str, cipher:str=None, key_size:int, pass_data:list, min_entropy:int, luks_version:BlockDev.CryptoLUKSVersion, extra:BlockDev.CryptoLUKSExtra=None) -> bool """
    return False

def crypto_luks_get_metadata_size(device): # real signature unknown; restored from __doc__
    """ crypto_luks_get_metadata_size(device:str) -> int """
    return 0

def crypto_luks_header_backup(device, backup_file): # real signature unknown; restored from __doc__
    """ crypto_luks_header_backup(device:str, backup_file:str) -> bool """
    return False

def crypto_luks_header_restore(device, backup_file): # real signature unknown; restored from __doc__
    """ crypto_luks_header_restore(device:str, backup_file:str) -> bool """
    return False

def crypto_luks_info(luks_device): # real signature unknown; restored from __doc__
    """ crypto_luks_info(luks_device:str) -> BlockDev.CryptoLUKSInfo """
    pass

def crypto_luks_kill_slot(device, slot): # real signature unknown; restored from __doc__
    """ crypto_luks_kill_slot(device:str, slot:int) -> bool """
    return False

def crypto_luks_open(device, name, passphrase=None, key_file=None, read_only=False): # reliably restored by inspect
    # no doc
    pass

def crypto_luks_open_blob(device, name, pass_data, read_only): # real signature unknown; restored from __doc__
    """ crypto_luks_open_blob(device:str, name:str, pass_data:list, read_only:bool) -> bool """
    return False

def crypto_luks_remove_key(device, pass_=None, key_file=None): # reliably restored by inspect
    # no doc
    pass

def crypto_luks_remove_key_blob(device, pass_data): # real signature unknown; restored from __doc__
    """ crypto_luks_remove_key_blob(device:str, pass_data:list) -> bool """
    return False

def crypto_luks_resize(luks_device, size=0, passphrase=None, key_file=None): # reliably restored by inspect
    # no doc
    pass

def crypto_luks_resize_luks2(luks_device, size, passphrase=None, key_file=None): # real signature unknown; restored from __doc__
    """ crypto_luks_resize_luks2(luks_device:str, size:int, passphrase:str=None, key_file:str=None) -> bool """
    return False

def crypto_luks_resize_luks2_blob(luks_device, size, pass_data): # real signature unknown; restored from __doc__
    """ crypto_luks_resize_luks2_blob(luks_device:str, size:int, pass_data:list) -> bool """
    return False

def crypto_luks_resume(device, passphrase=None, key_file=None): # reliably restored by inspect
    # no doc
    pass

def crypto_luks_resume_blob(luks_device, pass_data): # real signature unknown; restored from __doc__
    """ crypto_luks_resume_blob(luks_device:str, pass_data:list) -> bool """
    return False

def crypto_luks_status(luks_device): # real signature unknown; restored from __doc__
    """ crypto_luks_status(luks_device:str) -> str """
    return ""

def crypto_luks_suspend(luks_device): # real signature unknown; restored from __doc__
    """ crypto_luks_suspend(luks_device:str) -> bool """
    return False

def crypto_luks_uuid(device): # real signature unknown; restored from __doc__
    """ crypto_luks_uuid(device:str) -> str """
    return ""

def crypto_tc_close(tc_device): # real signature unknown; restored from __doc__
    """ crypto_tc_close(tc_device:str) -> bool """
    return False

def crypto_tc_open(device, name, passphrase, read_only=False, keyfiles=None, hidden=False, system=False, veracrypt=False, veracrypt_pim=0): # reliably restored by inspect
    # no doc
    pass

def crypto_tc_open_full(device, name, pass_data, keyfiles=None, hidden, system, veracrypt, veracrypt_pim, read_only): # real signature unknown; restored from __doc__
    """ crypto_tc_open_full(device:str, name:str, pass_data:list, keyfiles:list=None, hidden:bool, system:bool, veracrypt:bool, veracrypt_pim:int, read_only:bool) -> bool """
    return False

def dm_activate_raid_set(name): # real signature unknown; restored from __doc__
    """ dm_activate_raid_set(name:str) -> bool """
    return False

def dm_create_linear(map_name, device, length, uuid=None): # reliably restored by inspect
    # no doc
    pass

def dm_deactivate_raid_set(name): # real signature unknown; restored from __doc__
    """ dm_deactivate_raid_set(name:str) -> bool """
    return False

def dm_error_quark(): # real signature unknown; restored from __doc__
    """ dm_error_quark() -> int """
    return 0

def dm_get_member_raid_sets(name=None, uuid=None, major=-1, minor=-1): # reliably restored by inspect
    # no doc
    pass

def dm_get_raid_set_type(name): # real signature unknown; restored from __doc__
    """ dm_get_raid_set_type(name:str) -> str """
    return ""

def dm_get_subsystem_from_name(device_name): # real signature unknown; restored from __doc__
    """ dm_get_subsystem_from_name(device_name:str) -> str """
    return ""

def dm_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ dm_is_tech_avail(tech:BlockDev.DMTech, mode:int) -> bool """
    return False

def dm_map_exists(map_name, live_only, active_only): # real signature unknown; restored from __doc__
    """ dm_map_exists(map_name:str, live_only:bool, active_only:bool) -> bool """
    return False

def dm_name_from_node(dm_node): # real signature unknown; restored from __doc__
    """ dm_name_from_node(dm_node:str) -> str """
    return ""

def dm_node_from_name(map_name): # real signature unknown; restored from __doc__
    """ dm_node_from_name(map_name:str) -> str """
    return ""

def dm_remove(map_name): # real signature unknown; restored from __doc__
    """ dm_remove(map_name:str) -> bool """
    return False

def ensure_init(require_plugins=None, log_func=None): # reliably restored by inspect
    # no doc
    pass

def fs_can_check(type): # real signature unknown; restored from __doc__
    """ fs_can_check(type:str) -> bool, required_utility:str """
    return False

def fs_can_repair(type): # real signature unknown; restored from __doc__
    """ fs_can_repair(type:str) -> bool, required_utility:str """
    return False

def fs_can_resize(type): # real signature unknown; restored from __doc__
    """ fs_can_resize(type:str) -> bool, mode:BlockDev.FsResizeFlags, required_utility:str """
    return False

def fs_can_set_label(type): # real signature unknown; restored from __doc__
    """ fs_can_set_label(type:str) -> bool, required_utility:str """
    return False

def fs_check(device): # real signature unknown; restored from __doc__
    """ fs_check(device:str) -> bool """
    return False

def fs_clean(device): # real signature unknown; restored from __doc__
    """ fs_clean(device:str) -> bool """
    return False

def fs_error_quark(): # real signature unknown; restored from __doc__
    """ fs_error_quark() -> int """
    return 0

def fs_ext2_check(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext2_get_info(device): # real signature unknown; restored from __doc__
    """ fs_ext2_get_info(device:str) -> BlockDev.FSExt2Info """
    pass

def fs_ext2_mkfs(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext2_repair(device, unsafe=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext2_resize(device, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext2_set_label(device, label): # real signature unknown; restored from __doc__
    """ fs_ext2_set_label(device:str, label:str) -> bool """
    return False

def fs_ext2_wipe(device): # real signature unknown; restored from __doc__
    """ fs_ext2_wipe(device:str) -> bool """
    return False

def fs_ext3_check(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext3_get_info(device): # real signature unknown; restored from __doc__
    """ fs_ext3_get_info(device:str) -> BlockDev.FSExt3Info """
    pass

def fs_ext3_mkfs(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext3_repair(device, unsafe=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext3_resize(device, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext3_set_label(device, label): # real signature unknown; restored from __doc__
    """ fs_ext3_set_label(device:str, label:str) -> bool """
    return False

def fs_ext3_wipe(device): # real signature unknown; restored from __doc__
    """ fs_ext3_wipe(device:str) -> bool """
    return False

def fs_ext4_check(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext4_get_info(device): # real signature unknown; restored from __doc__
    """ fs_ext4_get_info(device:str) -> BlockDev.FSExt4Info """
    pass

def fs_ext4_mkfs(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext4_repair(device, unsafe=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext4_resize(device, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ext4_set_label(device, label): # real signature unknown; restored from __doc__
    """ fs_ext4_set_label(device:str, label:str) -> bool """
    return False

def fs_ext4_wipe(device): # real signature unknown; restored from __doc__
    """ fs_ext4_wipe(device:str) -> bool """
    return False

def fs_freeze(mountpoint): # real signature unknown; restored from __doc__
    """ fs_freeze(mountpoint:str) -> bool """
    return False

def fs_get_fstype(device): # real signature unknown; restored from __doc__
    """ fs_get_fstype(device:str) -> str """
    return ""

def fs_get_mountpoint(device): # real signature unknown; restored from __doc__
    """ fs_get_mountpoint(device:str) -> str """
    return ""

def fs_is_mountpoint(path): # real signature unknown; restored from __doc__
    """ fs_is_mountpoint(path:str) -> bool """
    return False

def fs_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ fs_is_tech_avail(tech:BlockDev.FSTech, mode:int) -> bool """
    return False

def fs_mount(device=None, mountpoint=None, fstype=None, options=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_ntfs_check(device): # real signature unknown; restored from __doc__
    """ fs_ntfs_check(device:str) -> bool """
    return False

def fs_ntfs_get_info(device): # real signature unknown; restored from __doc__
    """ fs_ntfs_get_info(device:str) -> BlockDev.FSNtfsInfo """
    pass

def fs_ntfs_mkfs(device, extra=None): # real signature unknown; restored from __doc__
    """ fs_ntfs_mkfs(device:str, extra:list=None) -> bool """
    return False

def fs_ntfs_repair(device): # real signature unknown; restored from __doc__
    """ fs_ntfs_repair(device:str) -> bool """
    return False

def fs_ntfs_resize(device, new_size): # real signature unknown; restored from __doc__
    """ fs_ntfs_resize(device:str, new_size:int) -> bool """
    return False

def fs_ntfs_set_label(device, label): # real signature unknown; restored from __doc__
    """ fs_ntfs_set_label(device:str, label:str) -> bool """
    return False

def fs_ntfs_wipe(device): # real signature unknown; restored from __doc__
    """ fs_ntfs_wipe(device:str) -> bool """
    return False

def fs_repair(device): # real signature unknown; restored from __doc__
    """ fs_repair(device:str) -> bool """
    return False

def fs_resize(device, new_size): # real signature unknown; restored from __doc__
    """ fs_resize(device:str, new_size:int) -> bool """
    return False

def fs_set_label(device, label): # real signature unknown; restored from __doc__
    """ fs_set_label(device:str, label:str) -> bool """
    return False

def fs_unfreeze(mountpoint): # real signature unknown; restored from __doc__
    """ fs_unfreeze(mountpoint:str) -> bool """
    return False

def fs_unmount(spec, lazy=False, force=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_vfat_check(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_vfat_get_info(device): # real signature unknown; restored from __doc__
    """ fs_vfat_get_info(device:str) -> BlockDev.FSVfatInfo """
    pass

def fs_vfat_mkfs(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_vfat_repair(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_vfat_resize(device, new_size): # real signature unknown; restored from __doc__
    """ fs_vfat_resize(device:str, new_size:int) -> bool """
    return False

def fs_vfat_set_label(device, label): # real signature unknown; restored from __doc__
    """ fs_vfat_set_label(device:str, label:str) -> bool """
    return False

def fs_vfat_wipe(device): # real signature unknown; restored from __doc__
    """ fs_vfat_wipe(device:str) -> bool """
    return False

def fs_wipe(device, all): # real signature unknown; restored from __doc__
    """ fs_wipe(device:str, all:bool) -> bool """
    return False

def fs_wipe_force(device, all, force): # real signature unknown; restored from __doc__
    """ fs_wipe_force(device:str, all:bool, force:bool) -> bool """
    return False

def fs_xfs_check(device): # real signature unknown; restored from __doc__
    """ fs_xfs_check(device:str) -> bool """
    return False

def fs_xfs_get_info(device): # real signature unknown; restored from __doc__
    """ fs_xfs_get_info(device:str) -> BlockDev.FSXfsInfo """
    pass

def fs_xfs_mkfs(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_xfs_repair(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_xfs_resize(device, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def fs_xfs_set_label(device, label): # real signature unknown; restored from __doc__
    """ fs_xfs_set_label(device:str, label:str) -> bool """
    return False

def fs_xfs_wipe(device): # real signature unknown; restored from __doc__
    """ fs_xfs_wipe(device:str) -> bool """
    return False

def get_available_plugin_names(): # real signature unknown; restored from __doc__
    """ get_available_plugin_names() -> list """
    return []

def get_plugin_name(plugin): # real signature unknown; restored from __doc__
    """ get_plugin_name(plugin:BlockDev.Plugin) -> str """
    return ""

def get_plugin_soname(plugin): # real signature unknown; restored from __doc__
    """ get_plugin_soname(plugin:BlockDev.Plugin) -> str """
    return ""

def init(require_plugins=None, log_func=None): # reliably restored by inspect
    # no doc
    pass

def is_initialized(): # real signature unknown; restored from __doc__
    """ is_initialized() -> bool """
    return False

def is_plugin_available(plugin): # real signature unknown; restored from __doc__
    """ is_plugin_available(plugin:BlockDev.Plugin) -> bool """
    return False

def kbd_bcache_attach(c_set_uuid, bcache_device): # real signature unknown; restored from __doc__
    """ kbd_bcache_attach(c_set_uuid:str, bcache_device:str) -> bool """
    return False

def kbd_bcache_create(backing_device, cache_device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def kbd_bcache_destroy(bcache_device): # real signature unknown; restored from __doc__
    """ kbd_bcache_destroy(bcache_device:str) -> bool """
    return False

def kbd_bcache_detach(bcache_device): # real signature unknown; restored from __doc__
    """ kbd_bcache_detach(bcache_device:str) -> bool, c_set_uuid:str """
    return False

def kbd_bcache_get_backing_device(bcache_device): # real signature unknown; restored from __doc__
    """ kbd_bcache_get_backing_device(bcache_device:str) -> str """
    return ""

def kbd_bcache_get_cache_device(bcache_device): # real signature unknown; restored from __doc__
    """ kbd_bcache_get_cache_device(bcache_device:str) -> str """
    return ""

def kbd_bcache_get_mode(bcache_device): # real signature unknown; restored from __doc__
    """ kbd_bcache_get_mode(bcache_device:str) -> BlockDev.KBDBcacheMode """
    pass

def kbd_bcache_get_mode_from_str(mode_str): # real signature unknown; restored from __doc__
    """ kbd_bcache_get_mode_from_str(mode_str:str) -> BlockDev.KBDBcacheMode """
    pass

def kbd_bcache_get_mode_str(mode): # real signature unknown; restored from __doc__
    """ kbd_bcache_get_mode_str(mode:BlockDev.KBDBcacheMode) -> str """
    return ""

def kbd_bcache_set_mode(bcache_device, mode): # real signature unknown; restored from __doc__
    """ kbd_bcache_set_mode(bcache_device:str, mode:BlockDev.KBDBcacheMode) -> bool """
    return False

def kbd_bcache_status(bcache_device): # real signature unknown; restored from __doc__
    """ kbd_bcache_status(bcache_device:str) -> BlockDev.KBDBcacheStats """
    pass

def kbd_error_quark(): # real signature unknown; restored from __doc__
    """ kbd_error_quark() -> int """
    return 0

def kbd_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ kbd_is_tech_avail(tech:BlockDev.KBDTech, mode:int) -> bool """
    return False

def kbd_zram_add_device(size, nstreams=0): # reliably restored by inspect
    # no doc
    pass

def kbd_zram_create_devices(num_devices, sizes, nstreams=None): # reliably restored by inspect
    # no doc
    pass

def kbd_zram_destroy_devices(): # real signature unknown; restored from __doc__
    """ kbd_zram_destroy_devices() -> bool """
    return False

def kbd_zram_get_stats(device): # real signature unknown; restored from __doc__
    """ kbd_zram_get_stats(device:str) -> BlockDev.KBDZramStats """
    pass

def kbd_zram_remove_device(device): # real signature unknown; restored from __doc__
    """ kbd_zram_remove_device(device:str) -> bool """
    return False

def loop_error_quark(): # real signature unknown; restored from __doc__
    """ loop_error_quark() -> int """
    return 0

def loop_get_autoclear(loop): # real signature unknown; restored from __doc__
    """ loop_get_autoclear(loop:str) -> bool """
    return False

def loop_get_backing_file(dev_name): # real signature unknown; restored from __doc__
    """ loop_get_backing_file(dev_name:str) -> str """
    return ""

def loop_get_loop_name(file): # real signature unknown; restored from __doc__
    """ loop_get_loop_name(file:str) -> str """
    return ""

def loop_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ loop_is_tech_avail(tech:BlockDev.LoopTech, mode:int) -> bool """
    return False

def loop_setup(file, offset=0, size=0, read_only=False, part_scan=True): # reliably restored by inspect
    # no doc
    pass

def loop_setup_from_fd(fd, offset, size, read_only, part_scan): # real signature unknown; restored from __doc__
    """ loop_setup_from_fd(fd:int, offset:int, size:int, read_only:bool, part_scan:bool) -> bool, loop_name:str """
    return False

def loop_set_autoclear(loop, autoclear): # real signature unknown; restored from __doc__
    """ loop_set_autoclear(loop:str, autoclear:bool) -> bool """
    return False

def loop_teardown(loop): # real signature unknown; restored from __doc__
    """ loop_teardown(loop:str) -> bool """
    return False

def lvm_cache_attach(vg_name, data_lv, cache_pool_lv, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_cache_create_cached_lv(vg_name, lv_name, data_size, cache_size, md_size, mode, flags, slow_pvs, fast_pvs): # real signature unknown; restored from __doc__
    """ lvm_cache_create_cached_lv(vg_name:str, lv_name:str, data_size:int, cache_size:int, md_size:int, mode:BlockDev.LVMCacheMode, flags:BlockDev.LVMCachePoolFlags, slow_pvs:list, fast_pvs:list) -> bool """
    return False

def lvm_cache_create_pool(vg_name, pool_name, pool_size, md_size, mode, flags, fast_pvs): # real signature unknown; restored from __doc__
    """ lvm_cache_create_pool(vg_name:str, pool_name:str, pool_size:int, md_size:int, mode:BlockDev.LVMCacheMode, flags:BlockDev.LVMCachePoolFlags, fast_pvs:list) -> bool """
    return False

def lvm_cache_detach(vg_name, cached_lv, destroy=True, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_cache_get_default_md_size(cache_size): # real signature unknown; restored from __doc__
    """ lvm_cache_get_default_md_size(cache_size:int) -> int """
    return 0

def lvm_cache_get_mode_from_str(mode_str): # real signature unknown; restored from __doc__
    """ lvm_cache_get_mode_from_str(mode_str:str) -> BlockDev.LVMCacheMode """
    pass

def lvm_cache_get_mode_str(mode): # real signature unknown; restored from __doc__
    """ lvm_cache_get_mode_str(mode:BlockDev.LVMCacheMode) -> str """
    return ""

def lvm_cache_pool_convert(vg_name, data_lv, metadata_lv, name=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_cache_pool_name(vg_name, cached_lv): # real signature unknown; restored from __doc__
    """ lvm_cache_pool_name(vg_name:str, cached_lv:str) -> str """
    return ""

def lvm_cache_stats(vg_name, cached_lv): # real signature unknown; restored from __doc__
    """ lvm_cache_stats(vg_name:str, cached_lv:str) -> BlockDev.LVMCacheStats """
    pass

def lvm_data_lv_name(vg_name, lv_name): # real signature unknown; restored from __doc__
    """ lvm_data_lv_name(vg_name:str, lv_name:str) -> str """
    return ""

def lvm_error_quark(): # real signature unknown; restored from __doc__
    """ lvm_error_quark() -> int """
    return 0

def lvm_get_global_config(): # real signature unknown; restored from __doc__
    """ lvm_get_global_config() -> str """
    return ""

def lvm_get_lv_physical_size(lv_size, pe_size): # real signature unknown; restored from __doc__
    """ lvm_get_lv_physical_size(lv_size:int, pe_size:int) -> int """
    return 0

def lvm_get_max_lv_size(): # real signature unknown; restored from __doc__
    """ lvm_get_max_lv_size() -> int """
    return 0

def lvm_get_supported_pe_sizes(): # real signature unknown; restored from __doc__
    """ lvm_get_supported_pe_sizes() -> list """
    return []

def lvm_get_thpool_meta_size(size, chunk_size, n_snapshots): # real signature unknown; restored from __doc__
    """ lvm_get_thpool_meta_size(size:int, chunk_size:int, n_snapshots:int) -> int """
    return 0

def lvm_get_thpool_padding(size, pe_size=0, included=False): # reliably restored by inspect
    # no doc
    pass

def lvm_get_vdo_compression_state_str(state): # real signature unknown; restored from __doc__
    """ lvm_get_vdo_compression_state_str(state:BlockDev.LVMVDOCompressionState) -> str """
    return ""

def lvm_get_vdo_index_state_str(state): # real signature unknown; restored from __doc__
    """ lvm_get_vdo_index_state_str(state:BlockDev.LVMVDOIndexState) -> str """
    return ""

def lvm_get_vdo_operating_mode_str(mode): # real signature unknown; restored from __doc__
    """ lvm_get_vdo_operating_mode_str(mode:BlockDev.LVMVDOOperatingMode) -> str """
    return ""

def lvm_get_vdo_write_policy_from_str(policy_str): # real signature unknown; restored from __doc__
    """ lvm_get_vdo_write_policy_from_str(policy_str:str) -> BlockDev.LVMVDOWritePolicy """
    pass

def lvm_get_vdo_write_policy_str(policy): # real signature unknown; restored from __doc__
    """ lvm_get_vdo_write_policy_str(policy:BlockDev.LVMVDOWritePolicy) -> str """
    return ""

def lvm_is_supported_pe_size(size): # real signature unknown; restored from __doc__
    """ lvm_is_supported_pe_size(size:int) -> bool """
    return False

def lvm_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ lvm_is_tech_avail(tech:BlockDev.LVMTech, mode:int) -> bool """
    return False

def lvm_is_valid_thpool_chunk_size(size, discard=False): # reliably restored by inspect
    # no doc
    pass

def lvm_is_valid_thpool_md_size(size): # real signature unknown; restored from __doc__
    """ lvm_is_valid_thpool_md_size(size:int) -> bool """
    return False

def lvm_lvactivate(vg_name, lv_name, ignore_skip=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_lvcreate(vg_name, lv_name, size, type=None, pv_list=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_lvdeactivate(vg_name, lv_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_lvinfo(vg_name, lv_name): # real signature unknown; restored from __doc__
    """ lvm_lvinfo(vg_name:str, lv_name:str) -> BlockDev.LVMLVdata """
    pass

def lvm_lvorigin(vg_name, lv_name): # real signature unknown; restored from __doc__
    """ lvm_lvorigin(vg_name:str, lv_name:str) -> str """
    return ""

def lvm_lvremove(vg_name, lv_name, force=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_lvrename(vg_name, lv_name, new_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_lvresize(vg_name, lv_name, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_lvs(vg_name=None): # reliably restored by inspect
    # no doc
    pass

def lvm_lvsnapshotcreate(vg_name, origin_name, snapshot_name, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_lvsnapshotmerge(vg_name, snapshot_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_metadata_lv_name(vg_name, lv_name): # real signature unknown; restored from __doc__
    """ lvm_metadata_lv_name(vg_name:str, lv_name:str) -> str """
    return ""

def lvm_pvcreate(device, data_alignment=0, metadata_size=0, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_pvinfo(device): # real signature unknown; restored from __doc__
    """ lvm_pvinfo(device:str) -> BlockDev.LVMPVdata """
    pass

def lvm_pvmove(src, dest=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_pvremove(device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_pvresize(device, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_pvs(): # real signature unknown; restored from __doc__
    """ lvm_pvs() -> list """
    return []

def lvm_pvscan(device=None, update_cache=True, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_round_size_to_pe(size, pe_size=0, roundup=True): # reliably restored by inspect
    # no doc
    pass

def lvm_set_global_config(new_config=None): # reliably restored by inspect
    # no doc
    pass

def lvm_thlvcreate(vg_name, pool_name, lv_name, size, extra=None): # real signature unknown; restored from __doc__
    """ lvm_thlvcreate(vg_name:str, pool_name:str, lv_name:str, size:int, extra:list=None) -> bool """
    return False

def lvm_thlvpoolname(vg_name, lv_name): # real signature unknown; restored from __doc__
    """ lvm_thlvpoolname(vg_name:str, lv_name:str) -> str """
    return ""

def lvm_thpoolcreate(vg_name, lv_name, size, md_size=0, chunk_size=0, profile=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_thpool_convert(vg_name, data_lv, metadata_lv, name=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_thsnapshotcreate(vg_name, origin_name, snapshot_name, pool_name=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdolvpoolname(vg_name, lv_name): # real signature unknown; restored from __doc__
    """ lvm_vdolvpoolname(vg_name:str, lv_name:str) -> str """
    return ""

def lvm_vdo_disable_compression(vg_name, pool_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdo_disable_deduplication(vg_name, pool_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdo_enable_compression(vg_name, pool_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdo_enable_deduplication(vg_name, pool_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdo_get_stats(vg_name, pool_name): # real signature unknown; restored from __doc__
    """ lvm_vdo_get_stats(vg_name:str, pool_name:str) -> BlockDev.LVMVDOStats """
    pass

def lvm_vdo_get_stats_full(vg_name, pool_name): # real signature unknown; restored from __doc__
    """ lvm_vdo_get_stats_full(vg_name:str, pool_name:str) -> dict """
    return {}

def lvm_vdo_info(vg_name, lv_name): # real signature unknown; restored from __doc__
    """ lvm_vdo_info(vg_name:str, lv_name:str) -> BlockDev.LVMVDOPooldata """
    pass

def lvm_vdo_pool_convert(vg_name, lv_name, pool_name, virtual_size, index_memory=0, compression=True, deduplication=True, write_policy=0, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdo_pool_create(vg_name, lv_name, pool_name, data_size, virtual_size, index_memory=0, compression=True, deduplication=True, write_policy=0, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdo_pool_resize(vg_name, lv_name, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vdo_resize(vg_name, lv_name, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vgactivate(vg_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vgcreate(name, pv_list, pe_size=0, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vgdeactivate(vg_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vgextend(vg_name, device, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vginfo(vg_name): # real signature unknown; restored from __doc__
    """ lvm_vginfo(vg_name:str) -> BlockDev.LVMVGdata """
    pass

def lvm_vgreduce(vg_name, device=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vgremove(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vgrename(old_name, new_name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def lvm_vgs(): # real signature unknown; restored from __doc__
    """ lvm_vgs() -> list """
    return []

def md_activate(raid_spec=None, members=None, uuid=None, start_degraded=True, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def md_add(raid_spec, device, raid_devs=0, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def md_canonicalize_uuid(uuid): # real signature unknown; restored from __doc__
    """ md_canonicalize_uuid(uuid:str) -> str """
    return ""

def md_create(device_name, level, disks, spares=0, version=None, bitmap=False, chunk_size=0, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def md_deactivate(raid_spec): # real signature unknown; restored from __doc__
    """ md_deactivate(raid_spec:str) -> bool """
    return False

def md_denominate(device): # real signature unknown; restored from __doc__
    """ md_denominate(device:str) -> bool """
    return False

def md_destroy(device): # real signature unknown; restored from __doc__
    """ md_destroy(device:str) -> bool """
    return False

def md_detail(raid_spec): # real signature unknown; restored from __doc__
    """ md_detail(raid_spec:str) -> BlockDev.MDDetailData """
    pass

def md_error_quark(): # real signature unknown; restored from __doc__
    """ md_error_quark() -> int """
    return 0

def md_examine(device): # real signature unknown; restored from __doc__
    """ md_examine(device:str) -> BlockDev.MDExamineData """
    pass

def md_get_bitmap_location(raid_spec): # real signature unknown; restored from __doc__
    """ md_get_bitmap_location(raid_spec:str) -> str """
    return ""

def md_get_md_uuid(uuid): # real signature unknown; restored from __doc__
    """ md_get_md_uuid(uuid:str) -> str """
    return ""

def md_get_status(raid_spec): # real signature unknown; restored from __doc__
    """ md_get_status(raid_spec:str) -> str """
    return ""

def md_get_superblock_size(size, version=None): # reliably restored by inspect
    # no doc
    pass

def md_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ md_is_tech_avail(tech:BlockDev.MDTech, mode:int) -> bool """
    return False

def md_name_from_node(node): # real signature unknown; restored from __doc__
    """ md_name_from_node(node:str) -> str """
    return ""

def md_node_from_name(name): # real signature unknown; restored from __doc__
    """ md_node_from_name(name:str) -> str """
    return ""

def md_nominate(device): # real signature unknown; restored from __doc__
    """ md_nominate(device:str) -> bool """
    return False

def md_remove(raid_spec, device, fail, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def md_request_sync_action(raid_spec, action): # real signature unknown; restored from __doc__
    """ md_request_sync_action(raid_spec:str, action:str) -> bool """
    return False

def md_run(raid_spec): # real signature unknown; restored from __doc__
    """ md_run(raid_spec:str) -> bool """
    return False

def md_set_bitmap_location(raid_spec, location): # real signature unknown; restored from __doc__
    """ md_set_bitmap_location(raid_spec:str, location:str) -> bool """
    return False

def mpath_error_quark(): # real signature unknown; restored from __doc__
    """ mpath_error_quark() -> int """
    return 0

def mpath_flush_mpaths(): # real signature unknown; restored from __doc__
    """ mpath_flush_mpaths() -> bool """
    return False

def mpath_get_mpath_members(): # real signature unknown; restored from __doc__
    """ mpath_get_mpath_members() -> list """
    return []

def mpath_is_mpath_member(device): # real signature unknown; restored from __doc__
    """ mpath_is_mpath_member(device:str) -> bool """
    return False

def mpath_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ mpath_is_tech_avail(tech:BlockDev.MpathTech, mode:int) -> bool """
    return False

def mpath_set_friendly_names(enabled): # real signature unknown; restored from __doc__
    """ mpath_set_friendly_names(enabled:bool) -> bool """
    return False

def nvdimm_error_quark(): # real signature unknown; restored from __doc__
    """ nvdimm_error_quark() -> int """
    return 0

def nvdimm_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ nvdimm_is_tech_avail(tech:BlockDev.NVDIMMTech, mode:int) -> bool """
    return False

def nvdimm_list_namespaces(bus=None, region=None, idle=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def nvdimm_namepace_get_supported_sector_sizes(mode): # real signature unknown; restored from __doc__
    """ nvdimm_namepace_get_supported_sector_sizes(mode:BlockDev.NVDIMMNamespaceMode) -> list """
    return []

def nvdimm_namespace_disable(namespace, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def nvdimm_namespace_enable(namespace, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def nvdimm_namespace_get_devname(device): # real signature unknown; restored from __doc__
    """ nvdimm_namespace_get_devname(device:str) -> str """
    return ""

def nvdimm_namespace_get_mode_from_str(mode_str): # real signature unknown; restored from __doc__
    """ nvdimm_namespace_get_mode_from_str(mode_str:str) -> BlockDev.NVDIMMNamespaceMode """
    pass

def nvdimm_namespace_get_mode_str(mode): # real signature unknown; restored from __doc__
    """ nvdimm_namespace_get_mode_str(mode:BlockDev.NVDIMMNamespaceMode) -> str """
    return ""

def nvdimm_namespace_info(namespace, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def nvdimm_namespace_reconfigure(namespace, mode, force=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def part_create_part(disk, type, start, size, align): # real signature unknown; restored from __doc__
    """ part_create_part(disk:str, type:BlockDev.PartTypeReq, start:int, size:int, align:BlockDev.PartAlign) -> BlockDev.PartSpec """
    pass

def part_create_table(disk, type, ignore_existing=True): # reliably restored by inspect
    # no doc
    pass

def part_delete_part(disk, part): # real signature unknown; restored from __doc__
    """ part_delete_part(disk:str, part:str) -> bool """
    return False

def part_error_quark(): # real signature unknown; restored from __doc__
    """ part_error_quark() -> int """
    return 0

def part_get_best_free_region(disk, type, size): # real signature unknown; restored from __doc__
    """ part_get_best_free_region(disk:str, type:BlockDev.PartType, size:int) -> BlockDev.PartSpec """
    pass

def part_get_disk_free_regions(disk): # real signature unknown; restored from __doc__
    """ part_get_disk_free_regions(disk:str) -> list """
    return []

def part_get_disk_parts(disk): # real signature unknown; restored from __doc__
    """ part_get_disk_parts(disk:str) -> list """
    return []

def part_get_disk_spec(disk): # real signature unknown; restored from __doc__
    """ part_get_disk_spec(disk:str) -> BlockDev.PartDiskSpec """
    pass

def part_get_flag_str(flag): # real signature unknown; restored from __doc__
    """ part_get_flag_str(flag:BlockDev.PartFlag) -> str """
    return ""

def part_get_part_by_pos(disk, position): # real signature unknown; restored from __doc__
    """ part_get_part_by_pos(disk:str, position:int) -> BlockDev.PartSpec """
    pass

def part_get_part_id(disk, part): # real signature unknown; restored from __doc__
    """ part_get_part_id(disk:str, part:str) -> str """
    return ""

def part_get_part_spec(disk, part): # real signature unknown; restored from __doc__
    """ part_get_part_spec(disk:str, part:str) -> BlockDev.PartSpec """
    pass

def part_get_part_table_type_str(type): # real signature unknown; restored from __doc__
    """ part_get_part_table_type_str(type:BlockDev.PartTableType) -> str """
    return ""

def part_get_type_str(type): # real signature unknown; restored from __doc__
    """ part_get_type_str(type:BlockDev.PartType) -> str """
    return ""

def part_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ part_is_tech_avail(tech:BlockDev.PartTech, mode:int) -> bool """
    return False

def part_resize_part(disk, part, size, align): # real signature unknown; restored from __doc__
    """ part_resize_part(disk:str, part:str, size:int, align:BlockDev.PartAlign) -> bool """
    return False

def part_set_disk_flag(disk, flag, state): # real signature unknown; restored from __doc__
    """ part_set_disk_flag(disk:str, flag:BlockDev.PartDiskFlag, state:bool) -> bool """
    return False

def part_set_part_flag(disk, part, flag, state): # real signature unknown; restored from __doc__
    """ part_set_part_flag(disk:str, part:str, flag:BlockDev.PartFlag, state:bool) -> bool """
    return False

def part_set_part_flags(disk, part, flags): # real signature unknown; restored from __doc__
    """ part_set_part_flags(disk:str, part:str, flags:int) -> bool """
    return False

def part_set_part_id(disk, part, part_id): # real signature unknown; restored from __doc__
    """ part_set_part_id(disk:str, part:str, part_id:str) -> bool """
    return False

def part_set_part_name(disk, part, name): # real signature unknown; restored from __doc__
    """ part_set_part_name(disk:str, part:str, name:str) -> bool """
    return False

def part_set_part_type(disk, part, type_guid): # real signature unknown; restored from __doc__
    """ part_set_part_type(disk:str, part:str, type_guid:str) -> bool """
    return False

def plugin_specs_from_names(plugin_names): # reliably restored by inspect
    # no doc
    pass

def reinit(require_plugins=None, reload=False, log_func=None): # reliably restored by inspect
    # no doc
    pass

def swap_error_quark(): # real signature unknown; restored from __doc__
    """ swap_error_quark() -> int """
    return 0

def swap_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ swap_is_tech_avail(tech:BlockDev.SwapTech, mode:int) -> bool """
    return False

def swap_mkswap(device, label=None, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def swap_set_label(device, label): # real signature unknown; restored from __doc__
    """ swap_set_label(device:str, label:str) -> bool """
    return False

def swap_swapoff(device): # real signature unknown; restored from __doc__
    """ swap_swapoff(device:str) -> bool """
    return False

def swap_swapon(device, priority=-1): # reliably restored by inspect
    # no doc
    pass

def swap_swapstatus(device): # real signature unknown; restored from __doc__
    """ swap_swapstatus(device:str) -> bool """
    return False

def switch_init_checks(enable): # real signature unknown; restored from __doc__
    """ switch_init_checks(enable:bool) -> bool """
    return False

def try_init(require_plugins=None, log_func=None): # reliably restored by inspect
    # no doc
    pass

def try_reinit(require_plugins=None, reload=False, log_func=None): # reliably restored by inspect
    # no doc
    pass

def utils_check_linux_version(major, minor, micro): # real signature unknown; restored from __doc__
    """ utils_check_linux_version(major:int, minor:int, micro:int) -> int """
    return 0

def utils_check_util_version(util, version=None, version_arg=None, version_regexp=None): # real signature unknown; restored from __doc__
    """ utils_check_util_version(util:str, version:str=None, version_arg:str=None, version_regexp:str=None) -> bool """
    return False

def utils_dbus_service_available(connection=None, bus_type, bus_name, obj_prefix): # real signature unknown; restored from __doc__
    """ utils_dbus_service_available(connection:Gio.DBusConnection=None, bus_type:Gio.BusType, bus_name:str, obj_prefix:str) -> bool """
    return False

def utils_echo_str_to_file(p_str, file_path): # real signature unknown; restored from __doc__
    """ utils_echo_str_to_file(str:str, file_path:str) -> bool """
    return False

def utils_exec_and_capture_output(argv, extra=None): # real signature unknown; restored from __doc__
    """ utils_exec_and_capture_output(argv:list, extra:list=None) -> bool, output:str """
    return False

def utils_exec_and_report_error(argv, extra=None): # real signature unknown; restored from __doc__
    """ utils_exec_and_report_error(argv:list, extra:list=None) -> bool """
    return False

def utils_exec_and_report_error_no_progress(argv, extra=None): # real signature unknown; restored from __doc__
    """ utils_exec_and_report_error_no_progress(argv:list, extra:list=None) -> bool """
    return False

def utils_exec_and_report_progress(argv, extra=None, prog_extract): # real signature unknown; restored from __doc__
    """ utils_exec_and_report_progress(argv:list, extra:list=None, prog_extract:BlockDev.UtilsProgExtract) -> bool, proc_status:int """
    return False

def utils_exec_and_report_status_error(argv, extra=None): # real signature unknown; restored from __doc__
    """ utils_exec_and_report_status_error(argv:list, extra:list=None) -> bool, status:int """
    return False

def utils_get_device_symlinks(dev_spec): # real signature unknown; restored from __doc__
    """ utils_get_device_symlinks(dev_spec:str) -> list """
    return []

def utils_get_linux_version(): # real signature unknown; restored from __doc__
    """ utils_get_linux_version() -> BlockDev.UtilsLinuxVersion """
    pass

def utils_have_kernel_module(module_name): # real signature unknown; restored from __doc__
    """ utils_have_kernel_module(module_name:str) -> bool """
    return False

def utils_init_logging(new_log_func=None): # real signature unknown; restored from __doc__
    """ utils_init_logging(new_log_func:BlockDev.UtilsLogFunc=None) -> bool """
    return False

def utils_init_prog_reporting(new_prog_func=None): # real signature unknown; restored from __doc__
    """ utils_init_prog_reporting(new_prog_func:BlockDev.UtilsProgFunc=None) -> bool """
    return False

def utils_init_prog_reporting_thread(new_prog_func=None): # real signature unknown; restored from __doc__
    """ utils_init_prog_reporting_thread(new_prog_func:BlockDev.UtilsProgFunc=None) -> bool """
    return False

def utils_load_kernel_module(module_name, options=None): # real signature unknown; restored from __doc__
    """ utils_load_kernel_module(module_name:str, options:str=None) -> bool """
    return False

def utils_log(level, msg): # real signature unknown; restored from __doc__
    """ utils_log(level:int, msg:str) """
    pass

def utils_mute_prog_reporting_thread(): # real signature unknown; restored from __doc__
    """ utils_mute_prog_reporting_thread() -> bool """
    return False

def utils_prog_reporting_initialized(): # real signature unknown; restored from __doc__
    """ utils_prog_reporting_initialized() -> bool """
    return False

def utils_report_finished(task_id, msg): # real signature unknown; restored from __doc__
    """ utils_report_finished(task_id:int, msg:str) """
    pass

def utils_report_progress(task_id, completion, msg): # real signature unknown; restored from __doc__
    """ utils_report_progress(task_id:int, completion:int, msg:str) """
    pass

def utils_report_started(msg): # real signature unknown; restored from __doc__
    """ utils_report_started(msg:str) -> int """
    return 0

def utils_resolve_device(dev_spec): # real signature unknown; restored from __doc__
    """ utils_resolve_device(dev_spec:str) -> str """
    return ""

def utils_unload_kernel_module(module_name): # real signature unknown; restored from __doc__
    """ utils_unload_kernel_module(module_name:str) -> bool """
    return False

def utils_version_cmp(ver_string1, ver_string2): # real signature unknown; restored from __doc__
    """ utils_version_cmp(ver_string1:str, ver_string2:str) -> int """
    return 0

def vdo_activate(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_change_write_policy(name, write_policy, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_create(name, backing_device, logical_size=0, index_memory=0, compression=True, deduplication=True, write_policy=2, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_deactivate(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_disable_compression(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_disable_deduplication(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_enable_compression(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_enable_deduplication(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_error_quark(): # real signature unknown; restored from __doc__
    """ vdo_error_quark() -> int """
    return 0

def vdo_get_stats(name): # real signature unknown; restored from __doc__
    """ vdo_get_stats(name:str) -> BlockDev.VDOStats """
    pass

def vdo_get_stats_full(name): # real signature unknown; restored from __doc__
    """ vdo_get_stats_full(name:str) -> dict """
    return {}

def vdo_get_write_policy_from_str(policy_str): # real signature unknown; restored from __doc__
    """ vdo_get_write_policy_from_str(policy_str:str) -> BlockDev.VDOWritePolicy """
    pass

def vdo_get_write_policy_str(policy): # real signature unknown; restored from __doc__
    """ vdo_get_write_policy_str(policy:BlockDev.VDOWritePolicy) -> str """
    return ""

def vdo_grow_logical(name, size, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_grow_physical(name, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_info(name): # real signature unknown; restored from __doc__
    """ vdo_info(name:str) -> BlockDev.VDOInfo """
    pass

def vdo_is_tech_avail(tech, mode): # real signature unknown; restored from __doc__
    """ vdo_is_tech_avail(tech:BlockDev.VDOTech, mode:int) -> bool """
    return False

def vdo_remove(name, force=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_start(name, rebuild=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

def vdo_stop(name, force=False, extra=None, **kwargs): # reliably restored by inspect
    # no doc
    pass

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

from .BlockDevError import BlockDevError
from .BlockDevNotImplementedError import BlockDevNotImplementedError
from .BtrfsDeviceInfo import BtrfsDeviceInfo
from .BtrfsError import BtrfsError
from .BtrfsFilesystemInfo import BtrfsFilesystemInfo
from .BtrfsSubvolumeInfo import BtrfsSubvolumeInfo
from .BtrfsTech import BtrfsTech
from .BtrfsTechMode import BtrfsTechMode
from .CryptoError import CryptoError
from .CryptoIntegrityInfo import CryptoIntegrityInfo
from .CryptoLUKSExtra import CryptoLUKSExtra
from .CryptoLUKSInfo import CryptoLUKSInfo
from .CryptoLUKSPBKDF import CryptoLUKSPBKDF
from .CryptoLUKSVersion import CryptoLUKSVersion
from .CryptoTech import CryptoTech
from .CryptoTechMode import CryptoTechMode
from .DMError import DMError
from .DMTech import DMTech
from .DMTechMode import DMTechMode
from .ExtraArg import ExtraArg
from .FSError import FSError
from .FsError import FsError
from .FSExt2Info import FSExt2Info
from .FSExt3Info import FSExt3Info
from .FSExt4Info import FSExt4Info
from .FSExtInfo import FSExtInfo
from .FSNoFSError import FSNoFSError
from .FSNtfsInfo import FSNtfsInfo
from .FsResizeFlags import FsResizeFlags
from .FSTech import FSTech
from .FSTechMode import FSTechMode
from .FSVfatInfo import FSVfatInfo
from .FSXfsInfo import FSXfsInfo
from .InitError import InitError
from .KBDBcacheMode import KBDBcacheMode
from .KBDBcacheStats import KBDBcacheStats
from .KBDError import KBDError
from .KbdError import KbdError
from .KBDTech import KBDTech
from .KBDTechMode import KBDTechMode
from .KBDZramStats import KBDZramStats
from .LoopError import LoopError
from .LoopTech import LoopTech
from .LoopTechMode import LoopTechMode
from .LVMCacheMode import LVMCacheMode
from .LVMCachePoolFlags import LVMCachePoolFlags
from .LVMCacheStats import LVMCacheStats
from .LVMError import LVMError
from .LVMLVdata import LVMLVdata
from .LVMPVdata import LVMPVdata
from .LVMTech import LVMTech
from .LVMTechMode import LVMTechMode
from .LVMVDOCompressionState import LVMVDOCompressionState
from .LVMVDOIndexState import LVMVDOIndexState
from .LVMVDOOperatingMode import LVMVDOOperatingMode
from .LVMVDOPooldata import LVMVDOPooldata
from .LVMVDOStats import LVMVDOStats
from .LVMVDOWritePolicy import LVMVDOWritePolicy
from .LVMVGdata import LVMVGdata
from .MDDetailData import MDDetailData
from .MDError import MDError
from .MDExamineData import MDExamineData
from .MDRaidError import MDRaidError
from .MDTech import MDTech
from .MDTechMode import MDTechMode
from .MpathError import MpathError
from .MpathTech import MpathTech
from .MpathTechMode import MpathTechMode
from .NVDIMMError import NVDIMMError
from .NVDIMMNamespaceInfo import NVDIMMNamespaceInfo
from .NVDIMMNamespaceMode import NVDIMMNamespaceMode
from .NVDIMMTech import NVDIMMTech
from .NVDIMMTechMode import NVDIMMTechMode
from .PartAlign import PartAlign
from .PartDiskFlag import PartDiskFlag
from .PartDiskSpec import PartDiskSpec
from .PartError import PartError
from .PartFlag import PartFlag
from .PartSpec import PartSpec
from .PartTableType import PartTableType
from .PartTech import PartTech
from .PartTechMode import PartTechMode
from .PartType import PartType
from .PartTypeReq import PartTypeReq
from .Plugin import Plugin
from .PluginSpec import PluginSpec
from .S390Error import S390Error
from .SwapError import SwapError
from .SwapActivateError import SwapActivateError
from .SwapOldError import SwapOldError
from .SwapPagesizeError import SwapPagesizeError
from .SwapSuspendError import SwapSuspendError
from .SwapTech import SwapTech
from .SwapTechMode import SwapTechMode
from .SwapUnknownError import SwapUnknownError
from .UtilsDBusError import UtilsDBusError
from .UtilsDevUtilsError import UtilsDevUtilsError
from .UtilsError import UtilsError
from .UtilsExecError import UtilsExecError
from .UtilsLinuxVersion import UtilsLinuxVersion
from .UtilsModuleError import UtilsModuleError
from .UtilsProgStatus import UtilsProgStatus
from .VDOError import VDOError
from .VDOInfo import VDOInfo
from .VDOStats import VDOStats
from .VDOTech import VDOTech
from .VDOTechMode import VDOTechMode
from .VDOWritePolicy import VDOWritePolicy
from .__class__ import __class__
# variables with complex values

btrfs = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5f40>'

crypto = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5f70>'

dm = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5fa0>'

fs = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbd6070>'

kbd = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc59d0>'

loop = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5fd0>'

lvm = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5ee0>'

md = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5f10>'

mpath = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5d00>'

nvdimm = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbd60a0>'

part = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbd6040>'

s390 = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbd60d0>'

swap = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbc5eb0>'

utils = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbd6100>'

vdo = None # (!) real value is '<gi.overrides.BlockDev.ErrorProxy object at 0x7fa27bbd6130>'

_introspection_module = None # (!) real value is "<IntrospectionModule 'BlockDev' from '/usr/lib64/girepository-1.0/BlockDev-2.0.typelib'>"

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fa27c9a0d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/BlockDev-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.BlockDev', loader=<gi.importer.DynamicImporter object at 0x7fa27c9a0d00>)"

