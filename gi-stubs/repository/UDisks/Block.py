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


class Block(__gobject.GInterface):
    # no doc
    def call_add_configuration_item(self, arg_item, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_add_configuration_item(self, arg_item:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_add_configuration_item_finish(self, res): # real signature unknown; restored from __doc__
        """ call_add_configuration_item_finish(self, res:Gio.AsyncResult) """
        pass

    def call_add_configuration_item_sync(self, arg_item, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_add_configuration_item_sync(self, arg_item:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_format(self, arg_type, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_format(self, arg_type:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_format_finish(self, res): # real signature unknown; restored from __doc__
        """ call_format_finish(self, res:Gio.AsyncResult) """
        pass

    def call_format_sync(self, arg_type, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_format_sync(self, arg_type:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_get_secret_configuration(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_get_secret_configuration(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_get_secret_configuration_finish(self, res): # real signature unknown; restored from __doc__
        """ call_get_secret_configuration_finish(self, res:Gio.AsyncResult) -> out_configuration:GLib.Variant """
        pass

    def call_get_secret_configuration_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_get_secret_configuration_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_configuration:GLib.Variant """
        pass

    def call_open_device(self, arg_mode, arg_options, fd_list=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_open_device(self, arg_mode:str, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_open_device_finish(self, res): # real signature unknown; restored from __doc__
        """ call_open_device_finish(self, res:Gio.AsyncResult) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_open_device_sync(self, arg_mode, arg_options, fd_list=None, cancellable=None): # real signature unknown; restored from __doc__
        """ call_open_device_sync(self, arg_mode:str, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_open_for_backup(self, arg_options, fd_list=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_open_for_backup(self, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_open_for_backup_finish(self, res): # real signature unknown; restored from __doc__
        """ call_open_for_backup_finish(self, res:Gio.AsyncResult) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_open_for_backup_sync(self, arg_options, fd_list=None, cancellable=None): # real signature unknown; restored from __doc__
        """ call_open_for_backup_sync(self, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_open_for_benchmark(self, arg_options, fd_list=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_open_for_benchmark(self, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_open_for_benchmark_finish(self, res): # real signature unknown; restored from __doc__
        """ call_open_for_benchmark_finish(self, res:Gio.AsyncResult) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_open_for_benchmark_sync(self, arg_options, fd_list=None, cancellable=None): # real signature unknown; restored from __doc__
        """ call_open_for_benchmark_sync(self, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_open_for_restore(self, arg_options, fd_list=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_open_for_restore(self, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_open_for_restore_finish(self, res): # real signature unknown; restored from __doc__
        """ call_open_for_restore_finish(self, res:Gio.AsyncResult) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_open_for_restore_sync(self, arg_options, fd_list=None, cancellable=None): # real signature unknown; restored from __doc__
        """ call_open_for_restore_sync(self, arg_options:GLib.Variant, fd_list:Gio.UnixFDList=None, cancellable:Gio.Cancellable=None) -> out_fd:GLib.Variant, out_fd_list:Gio.UnixFDList """
        pass

    def call_remove_configuration_item(self, arg_item, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_remove_configuration_item(self, arg_item:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_remove_configuration_item_finish(self, res): # real signature unknown; restored from __doc__
        """ call_remove_configuration_item_finish(self, res:Gio.AsyncResult) """
        pass

    def call_remove_configuration_item_sync(self, arg_item, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_remove_configuration_item_sync(self, arg_item:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_rescan(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_rescan(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_rescan_finish(self, res): # real signature unknown; restored from __doc__
        """ call_rescan_finish(self, res:Gio.AsyncResult) """
        pass

    def call_rescan_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_rescan_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_update_configuration_item(self, arg_old_item, arg_new_item, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_update_configuration_item(self, arg_old_item:GLib.Variant, arg_new_item:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_update_configuration_item_finish(self, res): # real signature unknown; restored from __doc__
        """ call_update_configuration_item_finish(self, res:Gio.AsyncResult) """
        pass

    def call_update_configuration_item_sync(self, arg_old_item, arg_new_item, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_update_configuration_item_sync(self, arg_old_item:GLib.Variant, arg_new_item:GLib.Variant, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def complete_add_configuration_item(self, invocation): # real signature unknown; restored from __doc__
        """ complete_add_configuration_item(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_format(self, invocation): # real signature unknown; restored from __doc__
        """ complete_format(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_get_secret_configuration(self, invocation, configuration): # real signature unknown; restored from __doc__
        """ complete_get_secret_configuration(self, invocation:Gio.DBusMethodInvocation, configuration:GLib.Variant) """
        pass

    def complete_open_device(self, invocation, fd_list=None, fd): # real signature unknown; restored from __doc__
        """ complete_open_device(self, invocation:Gio.DBusMethodInvocation, fd_list:Gio.UnixFDList=None, fd:GLib.Variant) """
        pass

    def complete_open_for_backup(self, invocation, fd_list=None, fd): # real signature unknown; restored from __doc__
        """ complete_open_for_backup(self, invocation:Gio.DBusMethodInvocation, fd_list:Gio.UnixFDList=None, fd:GLib.Variant) """
        pass

    def complete_open_for_benchmark(self, invocation, fd_list=None, fd): # real signature unknown; restored from __doc__
        """ complete_open_for_benchmark(self, invocation:Gio.DBusMethodInvocation, fd_list:Gio.UnixFDList=None, fd:GLib.Variant) """
        pass

    def complete_open_for_restore(self, invocation, fd_list=None, fd): # real signature unknown; restored from __doc__
        """ complete_open_for_restore(self, invocation:Gio.DBusMethodInvocation, fd_list:Gio.UnixFDList=None, fd:GLib.Variant) """
        pass

    def complete_remove_configuration_item(self, invocation): # real signature unknown; restored from __doc__
        """ complete_remove_configuration_item(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_rescan(self, invocation): # real signature unknown; restored from __doc__
        """ complete_rescan(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_update_configuration_item(self, invocation): # real signature unknown; restored from __doc__
        """ complete_update_configuration_item(self, invocation:Gio.DBusMethodInvocation) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Block), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksBlock (93969722309008)>, '__dict__': <attribute '__dict__' of 'Block' objects>, '__weakref__': <attribute '__weakref__' of 'Block' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_add_configuration_item': gi.FunctionInfo(call_add_configuration_item), 'call_add_configuration_item_finish': gi.FunctionInfo(call_add_configuration_item_finish), 'call_add_configuration_item_sync': gi.FunctionInfo(call_add_configuration_item_sync), 'call_format': gi.FunctionInfo(call_format), 'call_format_finish': gi.FunctionInfo(call_format_finish), 'call_format_sync': gi.FunctionInfo(call_format_sync), 'call_get_secret_configuration': gi.FunctionInfo(call_get_secret_configuration), 'call_get_secret_configuration_finish': gi.FunctionInfo(call_get_secret_configuration_finish), 'call_get_secret_configuration_sync': gi.FunctionInfo(call_get_secret_configuration_sync), 'call_open_device': gi.FunctionInfo(call_open_device), 'call_open_device_finish': gi.FunctionInfo(call_open_device_finish), 'call_open_device_sync': gi.FunctionInfo(call_open_device_sync), 'call_open_for_backup': gi.FunctionInfo(call_open_for_backup), 'call_open_for_backup_finish': gi.FunctionInfo(call_open_for_backup_finish), 'call_open_for_backup_sync': gi.FunctionInfo(call_open_for_backup_sync), 'call_open_for_benchmark': gi.FunctionInfo(call_open_for_benchmark), 'call_open_for_benchmark_finish': gi.FunctionInfo(call_open_for_benchmark_finish), 'call_open_for_benchmark_sync': gi.FunctionInfo(call_open_for_benchmark_sync), 'call_open_for_restore': gi.FunctionInfo(call_open_for_restore), 'call_open_for_restore_finish': gi.FunctionInfo(call_open_for_restore_finish), 'call_open_for_restore_sync': gi.FunctionInfo(call_open_for_restore_sync), 'call_remove_configuration_item': gi.FunctionInfo(call_remove_configuration_item), 'call_remove_configuration_item_finish': gi.FunctionInfo(call_remove_configuration_item_finish), 'call_remove_configuration_item_sync': gi.FunctionInfo(call_remove_configuration_item_sync), 'call_rescan': gi.FunctionInfo(call_rescan), 'call_rescan_finish': gi.FunctionInfo(call_rescan_finish), 'call_rescan_sync': gi.FunctionInfo(call_rescan_sync), 'call_update_configuration_item': gi.FunctionInfo(call_update_configuration_item), 'call_update_configuration_item_finish': gi.FunctionInfo(call_update_configuration_item_finish), 'call_update_configuration_item_sync': gi.FunctionInfo(call_update_configuration_item_sync), 'complete_add_configuration_item': gi.FunctionInfo(complete_add_configuration_item), 'complete_format': gi.FunctionInfo(complete_format), 'complete_get_secret_configuration': gi.FunctionInfo(complete_get_secret_configuration), 'complete_open_device': gi.FunctionInfo(complete_open_device), 'complete_open_for_backup': gi.FunctionInfo(complete_open_for_backup), 'complete_open_for_benchmark': gi.FunctionInfo(complete_open_for_benchmark), 'complete_open_for_restore': gi.FunctionInfo(complete_open_for_restore), 'complete_remove_configuration_item': gi.FunctionInfo(complete_remove_configuration_item), 'complete_rescan': gi.FunctionInfo(complete_rescan), 'complete_update_configuration_item': gi.FunctionInfo(complete_update_configuration_item)})"
    __gdoc__ = 'Interface UDisksBlock\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksBlock (93969722309008)>'
    __info__ = InterfaceInfo(Block)


