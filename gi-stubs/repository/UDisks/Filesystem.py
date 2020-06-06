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


class Filesystem(__gobject.GInterface):
    # no doc
    def call_check(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_check(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_check_finish(self, res): # real signature unknown; restored from __doc__
        """ call_check_finish(self, res:Gio.AsyncResult) -> out_consistent:bool """
        pass

    def call_check_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_check_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_consistent:bool """
        pass

    def call_mount(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_mount(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_mount_finish(self, res): # real signature unknown; restored from __doc__
        """ call_mount_finish(self, res:Gio.AsyncResult) -> out_mount_path:str """
        pass

    def call_mount_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_mount_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_mount_path:str """
        pass

    def call_repair(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_repair(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_repair_finish(self, res): # real signature unknown; restored from __doc__
        """ call_repair_finish(self, res:Gio.AsyncResult) -> out_repaired:bool """
        pass

    def call_repair_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_repair_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_repaired:bool """
        pass

    def call_resize(self, arg_size, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_resize(self, arg_size:int, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_resize_finish(self, res): # real signature unknown; restored from __doc__
        """ call_resize_finish(self, res:Gio.AsyncResult) """
        pass

    def call_resize_sync(self, arg_size, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_resize_sync(self, arg_size:int, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_label(self, arg_label, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_label(self, arg_label:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_label_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_label_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_label_sync(self, arg_label, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_label_sync(self, arg_label:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_take_ownership(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_take_ownership(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_take_ownership_finish(self, res): # real signature unknown; restored from __doc__
        """ call_take_ownership_finish(self, res:Gio.AsyncResult) """
        pass

    def call_take_ownership_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_take_ownership_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_unmount(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_unmount(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_unmount_finish(self, res): # real signature unknown; restored from __doc__
        """ call_unmount_finish(self, res:Gio.AsyncResult) """
        pass

    def call_unmount_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_unmount_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def complete_check(self, invocation, consistent): # real signature unknown; restored from __doc__
        """ complete_check(self, invocation:Gio.DBusMethodInvocation, consistent:bool) """
        pass

    def complete_mount(self, invocation, mount_path): # real signature unknown; restored from __doc__
        """ complete_mount(self, invocation:Gio.DBusMethodInvocation, mount_path:str) """
        pass

    def complete_repair(self, invocation, repaired): # real signature unknown; restored from __doc__
        """ complete_repair(self, invocation:Gio.DBusMethodInvocation, repaired:bool) """
        pass

    def complete_resize(self, invocation): # real signature unknown; restored from __doc__
        """ complete_resize(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_label(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_label(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_take_ownership(self, invocation): # real signature unknown; restored from __doc__
        """ complete_take_ownership(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_unmount(self, invocation): # real signature unknown; restored from __doc__
        """ complete_unmount(self, invocation:Gio.DBusMethodInvocation) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Filesystem), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksFilesystem (93969722539984)>, '__dict__': <attribute '__dict__' of 'Filesystem' objects>, '__weakref__': <attribute '__weakref__' of 'Filesystem' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_check': gi.FunctionInfo(call_check), 'call_check_finish': gi.FunctionInfo(call_check_finish), 'call_check_sync': gi.FunctionInfo(call_check_sync), 'call_mount': gi.FunctionInfo(call_mount), 'call_mount_finish': gi.FunctionInfo(call_mount_finish), 'call_mount_sync': gi.FunctionInfo(call_mount_sync), 'call_repair': gi.FunctionInfo(call_repair), 'call_repair_finish': gi.FunctionInfo(call_repair_finish), 'call_repair_sync': gi.FunctionInfo(call_repair_sync), 'call_resize': gi.FunctionInfo(call_resize), 'call_resize_finish': gi.FunctionInfo(call_resize_finish), 'call_resize_sync': gi.FunctionInfo(call_resize_sync), 'call_set_label': gi.FunctionInfo(call_set_label), 'call_set_label_finish': gi.FunctionInfo(call_set_label_finish), 'call_set_label_sync': gi.FunctionInfo(call_set_label_sync), 'call_take_ownership': gi.FunctionInfo(call_take_ownership), 'call_take_ownership_finish': gi.FunctionInfo(call_take_ownership_finish), 'call_take_ownership_sync': gi.FunctionInfo(call_take_ownership_sync), 'call_unmount': gi.FunctionInfo(call_unmount), 'call_unmount_finish': gi.FunctionInfo(call_unmount_finish), 'call_unmount_sync': gi.FunctionInfo(call_unmount_sync), 'complete_check': gi.FunctionInfo(complete_check), 'complete_mount': gi.FunctionInfo(complete_mount), 'complete_repair': gi.FunctionInfo(complete_repair), 'complete_resize': gi.FunctionInfo(complete_resize), 'complete_set_label': gi.FunctionInfo(complete_set_label), 'complete_take_ownership': gi.FunctionInfo(complete_take_ownership), 'complete_unmount': gi.FunctionInfo(complete_unmount)})"
    __gdoc__ = 'Interface UDisksFilesystem\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksFilesystem (93969722539984)>'
    __info__ = InterfaceInfo(Filesystem)


