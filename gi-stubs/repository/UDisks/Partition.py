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


class Partition(__gobject.GInterface):
    # no doc
    def call_delete(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_delete(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_delete_finish(self, res): # real signature unknown; restored from __doc__
        """ call_delete_finish(self, res:Gio.AsyncResult) """
        pass

    def call_delete_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_delete_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
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

    def call_set_flags(self, arg_flags, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_flags(self, arg_flags:int, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_flags_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_flags_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_flags_sync(self, arg_flags, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_flags_sync(self, arg_flags:int, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_name(self, arg_name, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_name(self, arg_name:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_name_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_name_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_name_sync(self, arg_name, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_name_sync(self, arg_name:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_type(self, arg_type, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_type(self, arg_type:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_type_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_type_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_type_sync(self, arg_type, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_type_sync(self, arg_type:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def complete_delete(self, invocation): # real signature unknown; restored from __doc__
        """ complete_delete(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_resize(self, invocation): # real signature unknown; restored from __doc__
        """ complete_resize(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_flags(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_flags(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_name(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_name(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_type(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_type(self, invocation:Gio.DBusMethodInvocation) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Partition), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksPartition (93969722809552)>, '__dict__': <attribute '__dict__' of 'Partition' objects>, '__weakref__': <attribute '__weakref__' of 'Partition' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_delete': gi.FunctionInfo(call_delete), 'call_delete_finish': gi.FunctionInfo(call_delete_finish), 'call_delete_sync': gi.FunctionInfo(call_delete_sync), 'call_resize': gi.FunctionInfo(call_resize), 'call_resize_finish': gi.FunctionInfo(call_resize_finish), 'call_resize_sync': gi.FunctionInfo(call_resize_sync), 'call_set_flags': gi.FunctionInfo(call_set_flags), 'call_set_flags_finish': gi.FunctionInfo(call_set_flags_finish), 'call_set_flags_sync': gi.FunctionInfo(call_set_flags_sync), 'call_set_name': gi.FunctionInfo(call_set_name), 'call_set_name_finish': gi.FunctionInfo(call_set_name_finish), 'call_set_name_sync': gi.FunctionInfo(call_set_name_sync), 'call_set_type': gi.FunctionInfo(call_set_type), 'call_set_type_finish': gi.FunctionInfo(call_set_type_finish), 'call_set_type_sync': gi.FunctionInfo(call_set_type_sync), 'complete_delete': gi.FunctionInfo(complete_delete), 'complete_resize': gi.FunctionInfo(complete_resize), 'complete_set_flags': gi.FunctionInfo(complete_set_flags), 'complete_set_name': gi.FunctionInfo(complete_set_name), 'complete_set_type': gi.FunctionInfo(complete_set_type)})"
    __gdoc__ = 'Interface UDisksPartition\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksPartition (93969722809552)>'
    __info__ = InterfaceInfo(Partition)


