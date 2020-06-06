# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Manager(__gobject.GInterface):
    # no doc
    def call_can_check(self, arg_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_can_check(self, arg_type:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_can_check_finish(self, res): # real signature unknown; restored from __doc__
        """ call_can_check_finish(self, res:Gio.AsyncResult) -> out_available:GLib.Variant """
        pass

    def call_can_check_sync(self, arg_type, cancellable=None): # real signature unknown; restored from __doc__
        """ call_can_check_sync(self, arg_type:str, cancellable:Gio.Cancellable=None) -> out_available:GLib.Variant """
        pass

    def call_can_format(self, arg_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_can_format(self, arg_type:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_can_format_finish(self, res): # real signature unknown; restored from __doc__
        """ call_can_format_finish(self, res:Gio.AsyncResult) -> out_available:GLib.Variant """
        pass

    def call_can_format_sync(self, arg_type, cancellable=None): # real signature unknown; restored from __doc__
        """ call_can_format_sync(self, arg_type:str, cancellable:Gio.Cancellable=None) -> out_available:GLib.Variant """
        pass

    def call_can_repair(self, arg_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_can_repair(self, arg_type:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_can_repair_finish(self, res): # real signature unknown; restored from __doc__
        """ call_can_repair_finish(self, res:Gio.AsyncResult) -> out_available:GLib.Variant """
        pass

    def call_can_repair_sync(self, arg_type, cancellable=None): # real signature unknown; restored from __doc__
        """ call_can_repair_sync(self, arg_type:str, cancellable:Gio.Cancellable=None) -> out_available:GLib.Variant """
        pass

    def call_can_resize(self, arg_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_can_resize(self, arg_type:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_can_resize_finish(self, res): # real signature unknown; restored from __doc__
        """ call_can_resize_finish(self, res:Gio.AsyncResult) -> out_available:GLib.Variant """
        pass

    def call_can_resize_sync(self, arg_type, cancellable=None): # real signature unknown; restored from __doc__
        """ call_can_resize_sync(self, arg_type:str, cancellable:Gio.Cancellable=None) -> out_available:GLib.Variant """
        pass

    def call_enable_modules(self, arg_enable, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_enable_modules(self, arg_enable:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_enable_modules_finish(self, res): # real signature unknown; restored from __doc__
        """ call_enable_modules_finish(self, res:Gio.AsyncResult) """
        pass

    def call_enable_modules_sync(self, arg_enable, cancellable=None): # real signature unknown; restored from __doc__
        """ call_enable_modules_sync(self, arg_enable:bool, cancellable:Gio.Cancellable=None) """
        pass

    def call_get_block_devices(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_get_block_devices(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_get_block_devices_finish(self, res): # real signature unknown; restored from __doc__
        """ call_get_block_devices_finish(self, res:Gio.AsyncResult) -> out_block_objects:list """
        pass

    def call_get_block_devices_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_get_block_devices_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_block_objects:list """
        pass

    def call_loop_setup(self, arg_fd, arg_options, fd_list=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_loop_setup(self, arg_fd:GLib.Variant, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_loop_setup_finish(self, res): # real signature unknown; restored from __doc__
        """ call_loop_setup_finish(self, res:Gio.AsyncResult) -> out_resulting_device:str, out_fd_list:Gio.UnixFDList """
        pass

    def call_loop_setup_sync(self, arg_fd, arg_options, fd_list=None, cancellable=None): # real signature unknown; restored from __doc__
        """ call_loop_setup_sync(self, arg_fd:GLib.Variant, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None) -> out_resulting_device:str, out_fd_list:Gio.UnixFDList """
        pass

    def call_mdraid_create(self, arg_blocks, arg_level, arg_name, arg_chunk, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_mdraid_create(self, arg_blocks:str, arg_level:str, arg_name:str, arg_chunk:int, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_mdraid_create_finish(self, res): # real signature unknown; restored from __doc__
        """ call_mdraid_create_finish(self, res:Gio.AsyncResult) -> out_resulting_array:str """
        pass

    def call_mdraid_create_sync(self, arg_blocks, arg_level, arg_name, arg_chunk, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_mdraid_create_sync(self, arg_blocks:str, arg_level:str, arg_name:str, arg_chunk:int, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_resulting_array:str """
        pass

    def call_resolve_device(self, arg_devspec, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_resolve_device(self, arg_devspec:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_resolve_device_finish(self, res): # real signature unknown; restored from __doc__
        """ call_resolve_device_finish(self, res:Gio.AsyncResult) -> out_devices:list """
        pass

    def call_resolve_device_sync(self, arg_devspec, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_resolve_device_sync(self, arg_devspec:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_devices:list """
        pass

    def complete_can_check(self, invocation, available): # real signature unknown; restored from __doc__
        """ complete_can_check(self, invocation:Gio.DBusMethodInvocation, available:GLib.Variant) """
        pass

    def complete_can_format(self, invocation, available): # real signature unknown; restored from __doc__
        """ complete_can_format(self, invocation:Gio.DBusMethodInvocation, available:GLib.Variant) """
        pass

    def complete_can_repair(self, invocation, available): # real signature unknown; restored from __doc__
        """ complete_can_repair(self, invocation:Gio.DBusMethodInvocation, available:GLib.Variant) """
        pass

    def complete_can_resize(self, invocation, available): # real signature unknown; restored from __doc__
        """ complete_can_resize(self, invocation:Gio.DBusMethodInvocation, available:GLib.Variant) """
        pass

    def complete_enable_modules(self, invocation): # real signature unknown; restored from __doc__
        """ complete_enable_modules(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_get_block_devices(self, invocation, block_objects): # real signature unknown; restored from __doc__
        """ complete_get_block_devices(self, invocation:Gio.DBusMethodInvocation, block_objects:str) """
        pass

    def complete_loop_setup(self, invocation, fd_list=None, resulting_device): # real signature unknown; restored from __doc__
        """ complete_loop_setup(self, invocation:Gio.DBusMethodInvocation, fd_list:Gio.UnixFDList=None, resulting_device:str) """
        pass

    def complete_mdraid_create(self, invocation, resulting_array): # real signature unknown; restored from __doc__
        """ complete_mdraid_create(self, invocation:Gio.DBusMethodInvocation, resulting_array:str) """
        pass

    def complete_resolve_device(self, invocation, devices): # real signature unknown; restored from __doc__
        """ complete_resolve_device(self, invocation:Gio.DBusMethodInvocation, devices:str) """
        pass

    def interface_info(self): # real signature unknown; restored from __doc__
        """ interface_info() -> Gio.DBusInterfaceInfo """
        pass

    def override_properties(self, klass, property_id_begin): # real signature unknown; restored from __doc__
        """ override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
        return 0

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Manager), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksManager (93969722491696)>, '__dict__': <attribute '__dict__' of 'Manager' objects>, '__weakref__': <attribute '__weakref__' of 'Manager' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_can_check': gi.FunctionInfo(call_can_check), 'call_can_check_finish': gi.FunctionInfo(call_can_check_finish), 'call_can_check_sync': gi.FunctionInfo(call_can_check_sync), 'call_can_format': gi.FunctionInfo(call_can_format), 'call_can_format_finish': gi.FunctionInfo(call_can_format_finish), 'call_can_format_sync': gi.FunctionInfo(call_can_format_sync), 'call_can_repair': gi.FunctionInfo(call_can_repair), 'call_can_repair_finish': gi.FunctionInfo(call_can_repair_finish), 'call_can_repair_sync': gi.FunctionInfo(call_can_repair_sync), 'call_can_resize': gi.FunctionInfo(call_can_resize), 'call_can_resize_finish': gi.FunctionInfo(call_can_resize_finish), 'call_can_resize_sync': gi.FunctionInfo(call_can_resize_sync), 'call_enable_modules': gi.FunctionInfo(call_enable_modules), 'call_enable_modules_finish': gi.FunctionInfo(call_enable_modules_finish), 'call_enable_modules_sync': gi.FunctionInfo(call_enable_modules_sync), 'call_get_block_devices': gi.FunctionInfo(call_get_block_devices), 'call_get_block_devices_finish': gi.FunctionInfo(call_get_block_devices_finish), 'call_get_block_devices_sync': gi.FunctionInfo(call_get_block_devices_sync), 'call_loop_setup': gi.FunctionInfo(call_loop_setup), 'call_loop_setup_finish': gi.FunctionInfo(call_loop_setup_finish), 'call_loop_setup_sync': gi.FunctionInfo(call_loop_setup_sync), 'call_mdraid_create': gi.FunctionInfo(call_mdraid_create), 'call_mdraid_create_finish': gi.FunctionInfo(call_mdraid_create_finish), 'call_mdraid_create_sync': gi.FunctionInfo(call_mdraid_create_sync), 'call_resolve_device': gi.FunctionInfo(call_resolve_device), 'call_resolve_device_finish': gi.FunctionInfo(call_resolve_device_finish), 'call_resolve_device_sync': gi.FunctionInfo(call_resolve_device_sync), 'complete_can_check': gi.FunctionInfo(complete_can_check), 'complete_can_format': gi.FunctionInfo(complete_can_format), 'complete_can_repair': gi.FunctionInfo(complete_can_repair), 'complete_can_resize': gi.FunctionInfo(complete_can_resize), 'complete_enable_modules': gi.FunctionInfo(complete_enable_modules), 'complete_get_block_devices': gi.FunctionInfo(complete_get_block_devices), 'complete_loop_setup': gi.FunctionInfo(complete_loop_setup), 'complete_mdraid_create': gi.FunctionInfo(complete_mdraid_create), 'complete_resolve_device': gi.FunctionInfo(complete_resolve_device)})"
    __gdoc__ = 'Interface UDisksManager\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksManager (93969722491696)>'
    __info__ = InterfaceInfo(Manager)


