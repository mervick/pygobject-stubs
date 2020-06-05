# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class File(__gobject.GInterface):
    # no doc
    def append_to(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ append_to(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def append_to_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ append_to_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def append_to_finish(self, res): # real signature unknown; restored from __doc__
        """ append_to_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def copy(self, destination, flags, cancellable=None, progress_callback=None, progress_callback_data=None): # real signature unknown; restored from __doc__
        """ copy(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None) -> bool """
        return False

    def copy_async(self, destination, flags, io_priority, cancellable=None, progress_callback=None, progress_callback_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ copy_async(self, destination:Gio.File, flags:Gio.FileCopyFlags, io_priority:int, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def copy_attributes(self, destination, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ copy_attributes(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def copy_finish(self, res): # real signature unknown; restored from __doc__
        """ copy_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def create(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ create(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def create_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_finish(self, res): # real signature unknown; restored from __doc__
        """ create_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def create_readwrite(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ create_readwrite(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def create_readwrite_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_readwrite_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ create_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def delete(self, cancellable=None): # real signature unknown; restored from __doc__
        """ delete(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gio.File """
        pass

    def eject_mountable(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject_mountable(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def eject_mountable_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject_mountable_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_mountable_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_mountable_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def enumerate_children(self, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ enumerate_children(self, attributes:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileEnumerator """
        pass

    def enumerate_children_async(self, attributes, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_children_async(self, attributes:str, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def enumerate_children_finish(self, res): # real signature unknown; restored from __doc__
        """ enumerate_children_finish(self, res:Gio.AsyncResult) -> Gio.FileEnumerator """
        pass

    def equal(self, file2): # real signature unknown; restored from __doc__
        """ equal(self, file2:Gio.File) -> bool """
        return False

    def find_enclosing_mount(self, cancellable=None): # real signature unknown; restored from __doc__
        """ find_enclosing_mount(self, cancellable:Gio.Cancellable=None) -> Gio.Mount """
        pass

    def find_enclosing_mount_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_enclosing_mount_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_enclosing_mount_finish(self, res): # real signature unknown; restored from __doc__
        """ find_enclosing_mount_finish(self, res:Gio.AsyncResult) -> Gio.Mount """
        pass

    def get_basename(self): # real signature unknown; restored from __doc__
        """ get_basename(self) -> str or None """
        return ""

    def get_child(self, name): # real signature unknown; restored from __doc__
        """ get_child(self, name:str) -> Gio.File """
        pass

    def get_child_for_display_name(self, display_name): # real signature unknown; restored from __doc__
        """ get_child_for_display_name(self, display_name:str) -> Gio.File """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gio.File or None """
        pass

    def get_parse_name(self): # real signature unknown; restored from __doc__
        """ get_parse_name(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str or None """
        return ""

    def get_relative_path(self, descendant): # real signature unknown; restored from __doc__
        """ get_relative_path(self, descendant:Gio.File) -> str or None """
        return ""

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_uri_scheme(self): # real signature unknown; restored from __doc__
        """ get_uri_scheme(self) -> str """
        return ""

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def has_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ has_parent(self, parent:Gio.File=None) -> bool """
        return False

    def has_prefix(self, prefix): # real signature unknown; restored from __doc__
        """ has_prefix(self, prefix:Gio.File) -> bool """
        return False

    def has_uri_scheme(self, uri_scheme): # real signature unknown; restored from __doc__
        """ has_uri_scheme(self, uri_scheme:str) -> bool """
        return False

    def is_native(self): # real signature unknown; restored from __doc__
        """ is_native(self) -> bool """
        return False

    def load_bytes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_bytes(self, cancellable:Gio.Cancellable=None) -> GLib.Bytes, etag_out:str """
        pass

    def load_bytes_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_bytes_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_bytes_finish(self, result): # real signature unknown; restored from __doc__
        """ load_bytes_finish(self, result:Gio.AsyncResult) -> GLib.Bytes, etag_out:str """
        pass

    def load_contents(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_contents(self, cancellable:Gio.Cancellable=None) -> bool, contents:list, etag_out:str """
        return False

    def load_contents_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_contents_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ load_contents_finish(self, res:Gio.AsyncResult) -> bool, contents:list, etag_out:str """
        return False

    def load_partial_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ load_partial_contents_finish(self, res:Gio.AsyncResult) -> bool, contents:list, etag_out:str """
        return False

    def make_directory(self, cancellable=None): # real signature unknown; restored from __doc__
        """ make_directory(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def make_directory_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ make_directory_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def make_directory_finish(self, result): # real signature unknown; restored from __doc__
        """ make_directory_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def make_directory_with_parents(self, cancellable=None): # real signature unknown; restored from __doc__
        """ make_directory_with_parents(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def make_symbolic_link(self, symlink_value, cancellable=None): # real signature unknown; restored from __doc__
        """ make_symbolic_link(self, symlink_value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def measure_disk_usage_finish(self, result): # real signature unknown; restored from __doc__
        """ measure_disk_usage_finish(self, result:Gio.AsyncResult) -> bool, disk_usage:int, num_dirs:int, num_files:int """
        return False

    def monitor(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def monitor_directory(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor_directory(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def monitor_file(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor_file(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def mount_enclosing_volume(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mount_enclosing_volume(self, flags:Gio.MountMountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mount_enclosing_volume_finish(self, result): # real signature unknown; restored from __doc__
        """ mount_enclosing_volume_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def mount_mountable(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mount_mountable(self, flags:Gio.MountMountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mount_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ mount_mountable_finish(self, result:Gio.AsyncResult) -> Gio.File """
        pass

    def move(self, destination, flags, cancellable=None, progress_callback=None, progress_callback_data=None): # real signature unknown; restored from __doc__
        """ move(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None) -> bool """
        return False

    def new_for_commandline_arg(self, arg): # real signature unknown; restored from __doc__
        """ new_for_commandline_arg(arg:str) -> Gio.File """
        pass

    def new_for_commandline_arg_and_cwd(self, arg, cwd): # real signature unknown; restored from __doc__
        """ new_for_commandline_arg_and_cwd(arg:str, cwd:str) -> Gio.File """
        pass

    def new_for_path(self, path): # real signature unknown; restored from __doc__
        """ new_for_path(path:str) -> Gio.File """
        pass

    def new_for_uri(self, uri): # real signature unknown; restored from __doc__
        """ new_for_uri(uri:str) -> Gio.File """
        pass

    def new_tmp(self, tmpl=None): # real signature unknown; restored from __doc__
        """ new_tmp(tmpl:str=None) -> Gio.File, iostream:Gio.FileIOStream """
        pass

    def open_readwrite(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open_readwrite(self, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def open_readwrite_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_readwrite_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ open_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def parse_name(self, parse_name): # real signature unknown; restored from __doc__
        """ parse_name(parse_name:str) -> Gio.File """
        pass

    def peek_path(self): # real signature unknown; restored from __doc__
        """ peek_path(self) -> str or None """
        return ""

    def poll_mountable(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ poll_mountable(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def poll_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ poll_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def query_default_handler(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_default_handler(self, cancellable:Gio.Cancellable=None) -> Gio.AppInfo """
        pass

    def query_default_handler_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_default_handler_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_default_handler_finish(self, result): # real signature unknown; restored from __doc__
        """ query_default_handler_finish(self, result:Gio.AsyncResult) -> Gio.AppInfo """
        pass

    def query_exists(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_exists(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def query_filesystem_info(self, attributes, cancellable=None): # real signature unknown; restored from __doc__
        """ query_filesystem_info(self, attributes:str, cancellable:Gio.Cancellable=None) -> Gio.FileInfo """
        pass

    def query_filesystem_info_async(self, attributes, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_filesystem_info_async(self, attributes:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_filesystem_info_finish(self, res): # real signature unknown; restored from __doc__
        """ query_filesystem_info_finish(self, res:Gio.AsyncResult) -> Gio.FileInfo """
        pass

    def query_file_type(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ query_file_type(self, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileType """
        pass

    def query_info(self, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ query_info(self, attributes:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileInfo """
        pass

    def query_info_async(self, attributes, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_info_async(self, attributes:str, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_info_finish(self, res): # real signature unknown; restored from __doc__
        """ query_info_finish(self, res:Gio.AsyncResult) -> Gio.FileInfo """
        pass

    def query_settable_attributes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_settable_attributes(self, cancellable:Gio.Cancellable=None) -> Gio.FileAttributeInfoList """
        pass

    def query_writable_namespaces(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_writable_namespaces(self, cancellable:Gio.Cancellable=None) -> Gio.FileAttributeInfoList """
        pass

    def read(self, cancellable=None): # real signature unknown; restored from __doc__
        """ read(self, cancellable:Gio.Cancellable=None) -> Gio.FileInputStream """
        pass

    def read_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ read_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def read_finish(self, res): # real signature unknown; restored from __doc__
        """ read_finish(self, res:Gio.AsyncResult) -> Gio.FileInputStream """
        pass

    def replace(self, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def replace_async(self, etag=None, make_backup, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_async(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents(self, contents, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace_contents(self, contents:list, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> bool, new_etag:str """
        return False

    def replace_contents_async(self, contents, etag=None, make_backup, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_contents_async(self, contents:list, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents_bytes_async(self, contents, etag=None, make_backup, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_contents_bytes_async(self, contents:GLib.Bytes, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_contents_finish(self, res:Gio.AsyncResult) -> bool, new_etag:str """
        return False

    def replace_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def replace_readwrite(self, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace_readwrite(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def replace_readwrite_async(self, etag=None, make_backup, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_readwrite_async(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def resolve_relative_path(self, relative_path): # real signature unknown; restored from __doc__
        """ resolve_relative_path(self, relative_path:str) -> Gio.File """
        pass

    def set_attribute(self, attribute, type, value_p=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute(self, attribute:str, type:Gio.FileAttributeType, value_p=None, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attributes_async(self, info, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_attributes_async(self, info:Gio.FileInfo, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_attributes_finish(self, result): # real signature unknown; restored from __doc__
        """ set_attributes_finish(self, result:Gio.AsyncResult) -> bool, info:Gio.FileInfo """
        return False

    def set_attributes_from_info(self, info, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attributes_from_info(self, info:Gio.FileInfo, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_byte_string(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_byte_string(self, attribute:str, value:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_int32(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_int32(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_int64(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_int64(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_string(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_string(self, attribute:str, value:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_uint32(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_uint32(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_uint64(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_uint64(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_display_name(self, display_name, cancellable=None): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str, cancellable:Gio.Cancellable=None) -> Gio.File """
        pass

    def set_display_name_async(self, display_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_display_name_async(self, display_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_display_name_finish(self, res): # real signature unknown; restored from __doc__
        """ set_display_name_finish(self, res:Gio.AsyncResult) -> Gio.File """
        pass

    def start_mountable(self, flags, start_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ start_mountable(self, flags:Gio.DriveStartFlags, start_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def start_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ start_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def stop_mountable(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ stop_mountable(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def stop_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ stop_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def supports_thread_contexts(self): # real signature unknown; restored from __doc__
        """ supports_thread_contexts(self) -> bool """
        return False

    def trash(self, cancellable=None): # real signature unknown; restored from __doc__
        """ trash(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def trash_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ trash_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def trash_finish(self, result): # real signature unknown; restored from __doc__
        """ trash_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unmount_mountable(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount_mountable(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unmount_mountable_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount_mountable_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_mountable_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_mountable_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(File), '__module__': 'gi.repository.Gio', '__gtype__': <GType GFile (94125582096880)>, '__dict__': <attribute '__dict__' of 'File' objects>, '__weakref__': <attribute '__weakref__' of 'File' objects>, '__doc__': None, '__gsignals__': {}, 'new_for_commandline_arg': gi.FunctionInfo(new_for_commandline_arg), 'new_for_commandline_arg_and_cwd': gi.FunctionInfo(new_for_commandline_arg_and_cwd), 'new_for_path': gi.FunctionInfo(new_for_path), 'new_for_uri': gi.FunctionInfo(new_for_uri), 'new_tmp': gi.FunctionInfo(new_tmp), 'parse_name': gi.FunctionInfo(parse_name), 'append_to': gi.FunctionInfo(append_to), 'append_to_async': gi.FunctionInfo(append_to_async), 'append_to_finish': gi.FunctionInfo(append_to_finish), 'copy': gi.FunctionInfo(copy), 'copy_async': gi.FunctionInfo(copy_async), 'copy_attributes': gi.FunctionInfo(copy_attributes), 'copy_finish': gi.FunctionInfo(copy_finish), 'create': gi.FunctionInfo(create), 'create_async': gi.FunctionInfo(create_async), 'create_finish': gi.FunctionInfo(create_finish), 'create_readwrite': gi.FunctionInfo(create_readwrite), 'create_readwrite_async': gi.FunctionInfo(create_readwrite_async), 'create_readwrite_finish': gi.FunctionInfo(create_readwrite_finish), 'delete': gi.FunctionInfo(delete), 'delete_async': gi.FunctionInfo(delete_async), 'delete_finish': gi.FunctionInfo(delete_finish), 'dup': gi.FunctionInfo(dup), 'eject_mountable': gi.FunctionInfo(eject_mountable), 'eject_mountable_finish': gi.FunctionInfo(eject_mountable_finish), 'eject_mountable_with_operation': gi.FunctionInfo(eject_mountable_with_operation), 'eject_mountable_with_operation_finish': gi.FunctionInfo(eject_mountable_with_operation_finish), 'enumerate_children': gi.FunctionInfo(enumerate_children), 'enumerate_children_async': gi.FunctionInfo(enumerate_children_async), 'enumerate_children_finish': gi.FunctionInfo(enumerate_children_finish), 'equal': gi.FunctionInfo(equal), 'find_enclosing_mount': gi.FunctionInfo(find_enclosing_mount), 'find_enclosing_mount_async': gi.FunctionInfo(find_enclosing_mount_async), 'find_enclosing_mount_finish': gi.FunctionInfo(find_enclosing_mount_finish), 'get_basename': gi.FunctionInfo(get_basename), 'get_child': gi.FunctionInfo(get_child), 'get_child_for_display_name': gi.FunctionInfo(get_child_for_display_name), 'get_parent': gi.FunctionInfo(get_parent), 'get_parse_name': gi.FunctionInfo(get_parse_name), 'get_path': gi.FunctionInfo(get_path), 'get_relative_path': gi.FunctionInfo(get_relative_path), 'get_uri': gi.FunctionInfo(get_uri), 'get_uri_scheme': gi.FunctionInfo(get_uri_scheme), 'has_parent': gi.FunctionInfo(has_parent), 'has_prefix': gi.FunctionInfo(has_prefix), 'has_uri_scheme': gi.FunctionInfo(has_uri_scheme), 'hash': gi.FunctionInfo(hash), 'is_native': gi.FunctionInfo(is_native), 'load_bytes': gi.FunctionInfo(load_bytes), 'load_bytes_async': gi.FunctionInfo(load_bytes_async), 'load_bytes_finish': gi.FunctionInfo(load_bytes_finish), 'load_contents': gi.FunctionInfo(load_contents), 'load_contents_async': gi.FunctionInfo(load_contents_async), 'load_contents_finish': gi.FunctionInfo(load_contents_finish), 'load_partial_contents_finish': gi.FunctionInfo(load_partial_contents_finish), 'make_directory': gi.FunctionInfo(make_directory), 'make_directory_async': gi.FunctionInfo(make_directory_async), 'make_directory_finish': gi.FunctionInfo(make_directory_finish), 'make_directory_with_parents': gi.FunctionInfo(make_directory_with_parents), 'make_symbolic_link': gi.FunctionInfo(make_symbolic_link), 'measure_disk_usage_finish': gi.FunctionInfo(measure_disk_usage_finish), 'monitor': gi.FunctionInfo(monitor), 'monitor_directory': gi.FunctionInfo(monitor_directory), 'monitor_file': gi.FunctionInfo(monitor_file), 'mount_enclosing_volume': gi.FunctionInfo(mount_enclosing_volume), 'mount_enclosing_volume_finish': gi.FunctionInfo(mount_enclosing_volume_finish), 'mount_mountable': gi.FunctionInfo(mount_mountable), 'mount_mountable_finish': gi.FunctionInfo(mount_mountable_finish), 'move': gi.FunctionInfo(move), 'open_readwrite': gi.FunctionInfo(open_readwrite), 'open_readwrite_async': gi.FunctionInfo(open_readwrite_async), 'open_readwrite_finish': gi.FunctionInfo(open_readwrite_finish), 'peek_path': gi.FunctionInfo(peek_path), 'poll_mountable': gi.FunctionInfo(poll_mountable), 'poll_mountable_finish': gi.FunctionInfo(poll_mountable_finish), 'query_default_handler': gi.FunctionInfo(query_default_handler), 'query_default_handler_async': gi.FunctionInfo(query_default_handler_async), 'query_default_handler_finish': gi.FunctionInfo(query_default_handler_finish), 'query_exists': gi.FunctionInfo(query_exists), 'query_file_type': gi.FunctionInfo(query_file_type), 'query_filesystem_info': gi.FunctionInfo(query_filesystem_info), 'query_filesystem_info_async': gi.FunctionInfo(query_filesystem_info_async), 'query_filesystem_info_finish': gi.FunctionInfo(query_filesystem_info_finish), 'query_info': gi.FunctionInfo(query_info), 'query_info_async': gi.FunctionInfo(query_info_async), 'query_info_finish': gi.FunctionInfo(query_info_finish), 'query_settable_attributes': gi.FunctionInfo(query_settable_attributes), 'query_writable_namespaces': gi.FunctionInfo(query_writable_namespaces), 'read': gi.FunctionInfo(read), 'read_async': gi.FunctionInfo(read_async), 'read_finish': gi.FunctionInfo(read_finish), 'replace': gi.FunctionInfo(replace), 'replace_async': gi.FunctionInfo(replace_async), 'replace_contents': gi.FunctionInfo(replace_contents), 'replace_contents_async': gi.FunctionInfo(replace_contents_async), 'replace_contents_bytes_async': gi.FunctionInfo(replace_contents_bytes_async), 'replace_contents_finish': gi.FunctionInfo(replace_contents_finish), 'replace_finish': gi.FunctionInfo(replace_finish), 'replace_readwrite': gi.FunctionInfo(replace_readwrite), 'replace_readwrite_async': gi.FunctionInfo(replace_readwrite_async), 'replace_readwrite_finish': gi.FunctionInfo(replace_readwrite_finish), 'resolve_relative_path': gi.FunctionInfo(resolve_relative_path), 'set_attribute': gi.FunctionInfo(set_attribute), 'set_attribute_byte_string': gi.FunctionInfo(set_attribute_byte_string), 'set_attribute_int32': gi.FunctionInfo(set_attribute_int32), 'set_attribute_int64': gi.FunctionInfo(set_attribute_int64), 'set_attribute_string': gi.FunctionInfo(set_attribute_string), 'set_attribute_uint32': gi.FunctionInfo(set_attribute_uint32), 'set_attribute_uint64': gi.FunctionInfo(set_attribute_uint64), 'set_attributes_async': gi.FunctionInfo(set_attributes_async), 'set_attributes_finish': gi.FunctionInfo(set_attributes_finish), 'set_attributes_from_info': gi.FunctionInfo(set_attributes_from_info), 'set_display_name': gi.FunctionInfo(set_display_name), 'set_display_name_async': gi.FunctionInfo(set_display_name_async), 'set_display_name_finish': gi.FunctionInfo(set_display_name_finish), 'start_mountable': gi.FunctionInfo(start_mountable), 'start_mountable_finish': gi.FunctionInfo(start_mountable_finish), 'stop_mountable': gi.FunctionInfo(stop_mountable), 'stop_mountable_finish': gi.FunctionInfo(stop_mountable_finish), 'supports_thread_contexts': gi.FunctionInfo(supports_thread_contexts), 'trash': gi.FunctionInfo(trash), 'trash_async': gi.FunctionInfo(trash_async), 'trash_finish': gi.FunctionInfo(trash_finish), 'unmount_mountable': gi.FunctionInfo(unmount_mountable), 'unmount_mountable_finish': gi.FunctionInfo(unmount_mountable_finish), 'unmount_mountable_with_operation': gi.FunctionInfo(unmount_mountable_with_operation), 'unmount_mountable_with_operation_finish': gi.FunctionInfo(unmount_mountable_with_operation_finish)})"
    __gdoc__ = 'Interface GFile\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GFile (94125582096880)>'
    __info__ = InterfaceInfo(File)


