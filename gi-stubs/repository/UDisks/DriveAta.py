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


class DriveAta(__gobject.GInterface):
    # no doc
    def call_pm_get_state(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_pm_get_state(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_pm_get_state_finish(self, res): # real signature unknown; restored from __doc__
        """ call_pm_get_state_finish(self, res:Gio.AsyncResult) -> out_state:int """
        pass

    def call_pm_get_state_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_pm_get_state_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_state:int """
        pass

    def call_pm_standby(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_pm_standby(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_pm_standby_finish(self, res): # real signature unknown; restored from __doc__
        """ call_pm_standby_finish(self, res:Gio.AsyncResult) """
        pass

    def call_pm_standby_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_pm_standby_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_pm_wakeup(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_pm_wakeup(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_pm_wakeup_finish(self, res): # real signature unknown; restored from __doc__
        """ call_pm_wakeup_finish(self, res:Gio.AsyncResult) """
        pass

    def call_pm_wakeup_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_pm_wakeup_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_security_erase_unit(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_security_erase_unit(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_security_erase_unit_finish(self, res): # real signature unknown; restored from __doc__
        """ call_security_erase_unit_finish(self, res:Gio.AsyncResult) """
        pass

    def call_security_erase_unit_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_security_erase_unit_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_smart_get_attributes(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_smart_get_attributes(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_smart_get_attributes_finish(self, res): # real signature unknown; restored from __doc__
        """ call_smart_get_attributes_finish(self, res:Gio.AsyncResult) -> out_attributes:GLib.Variant """
        pass

    def call_smart_get_attributes_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_smart_get_attributes_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_attributes:GLib.Variant """
        pass

    def call_smart_selftest_abort(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_smart_selftest_abort(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_smart_selftest_abort_finish(self, res): # real signature unknown; restored from __doc__
        """ call_smart_selftest_abort_finish(self, res:Gio.AsyncResult) """
        pass

    def call_smart_selftest_abort_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_smart_selftest_abort_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_smart_selftest_start(self, arg_type, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_smart_selftest_start(self, arg_type:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_smart_selftest_start_finish(self, res): # real signature unknown; restored from __doc__
        """ call_smart_selftest_start_finish(self, res:Gio.AsyncResult) """
        pass

    def call_smart_selftest_start_sync(self, arg_type, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_smart_selftest_start_sync(self, arg_type:str, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_smart_set_enabled(self, arg_value, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_smart_set_enabled(self, arg_value:bool, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_smart_set_enabled_finish(self, res): # real signature unknown; restored from __doc__
        """ call_smart_set_enabled_finish(self, res:Gio.AsyncResult) """
        pass

    def call_smart_set_enabled_sync(self, arg_value, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_smart_set_enabled_sync(self, arg_value:bool, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_smart_update(self, arg_options, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_smart_update(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_smart_update_finish(self, res): # real signature unknown; restored from __doc__
        """ call_smart_update_finish(self, res:Gio.AsyncResult) """
        pass

    def call_smart_update_sync(self, arg_options, cancellable=None): # real signature unknown; restored from __doc__
        """ call_smart_update_sync(self, arg_options:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def complete_pm_get_state(self, invocation, state): # real signature unknown; restored from __doc__
        """ complete_pm_get_state(self, invocation:Gio.DBusMethodInvocation, state:int) """
        pass

    def complete_pm_standby(self, invocation): # real signature unknown; restored from __doc__
        """ complete_pm_standby(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_pm_wakeup(self, invocation): # real signature unknown; restored from __doc__
        """ complete_pm_wakeup(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_security_erase_unit(self, invocation): # real signature unknown; restored from __doc__
        """ complete_security_erase_unit(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_smart_get_attributes(self, invocation, attributes): # real signature unknown; restored from __doc__
        """ complete_smart_get_attributes(self, invocation:Gio.DBusMethodInvocation, attributes:GLib.Variant) """
        pass

    def complete_smart_selftest_abort(self, invocation): # real signature unknown; restored from __doc__
        """ complete_smart_selftest_abort(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_smart_selftest_start(self, invocation): # real signature unknown; restored from __doc__
        """ complete_smart_selftest_start(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_smart_set_enabled(self, invocation): # real signature unknown; restored from __doc__
        """ complete_smart_set_enabled(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_smart_update(self, invocation): # real signature unknown; restored from __doc__
        """ complete_smart_update(self, invocation:Gio.DBusMethodInvocation) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DriveAta), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksDriveAta (93969722179200)>, '__dict__': <attribute '__dict__' of 'DriveAta' objects>, '__weakref__': <attribute '__weakref__' of 'DriveAta' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_pm_get_state': gi.FunctionInfo(call_pm_get_state), 'call_pm_get_state_finish': gi.FunctionInfo(call_pm_get_state_finish), 'call_pm_get_state_sync': gi.FunctionInfo(call_pm_get_state_sync), 'call_pm_standby': gi.FunctionInfo(call_pm_standby), 'call_pm_standby_finish': gi.FunctionInfo(call_pm_standby_finish), 'call_pm_standby_sync': gi.FunctionInfo(call_pm_standby_sync), 'call_pm_wakeup': gi.FunctionInfo(call_pm_wakeup), 'call_pm_wakeup_finish': gi.FunctionInfo(call_pm_wakeup_finish), 'call_pm_wakeup_sync': gi.FunctionInfo(call_pm_wakeup_sync), 'call_security_erase_unit': gi.FunctionInfo(call_security_erase_unit), 'call_security_erase_unit_finish': gi.FunctionInfo(call_security_erase_unit_finish), 'call_security_erase_unit_sync': gi.FunctionInfo(call_security_erase_unit_sync), 'call_smart_get_attributes': gi.FunctionInfo(call_smart_get_attributes), 'call_smart_get_attributes_finish': gi.FunctionInfo(call_smart_get_attributes_finish), 'call_smart_get_attributes_sync': gi.FunctionInfo(call_smart_get_attributes_sync), 'call_smart_selftest_abort': gi.FunctionInfo(call_smart_selftest_abort), 'call_smart_selftest_abort_finish': gi.FunctionInfo(call_smart_selftest_abort_finish), 'call_smart_selftest_abort_sync': gi.FunctionInfo(call_smart_selftest_abort_sync), 'call_smart_selftest_start': gi.FunctionInfo(call_smart_selftest_start), 'call_smart_selftest_start_finish': gi.FunctionInfo(call_smart_selftest_start_finish), 'call_smart_selftest_start_sync': gi.FunctionInfo(call_smart_selftest_start_sync), 'call_smart_set_enabled': gi.FunctionInfo(call_smart_set_enabled), 'call_smart_set_enabled_finish': gi.FunctionInfo(call_smart_set_enabled_finish), 'call_smart_set_enabled_sync': gi.FunctionInfo(call_smart_set_enabled_sync), 'call_smart_update': gi.FunctionInfo(call_smart_update), 'call_smart_update_finish': gi.FunctionInfo(call_smart_update_finish), 'call_smart_update_sync': gi.FunctionInfo(call_smart_update_sync), 'complete_pm_get_state': gi.FunctionInfo(complete_pm_get_state), 'complete_pm_standby': gi.FunctionInfo(complete_pm_standby), 'complete_pm_wakeup': gi.FunctionInfo(complete_pm_wakeup), 'complete_security_erase_unit': gi.FunctionInfo(complete_security_erase_unit), 'complete_smart_get_attributes': gi.FunctionInfo(complete_smart_get_attributes), 'complete_smart_selftest_abort': gi.FunctionInfo(complete_smart_selftest_abort), 'complete_smart_selftest_start': gi.FunctionInfo(complete_smart_selftest_start), 'complete_smart_set_enabled': gi.FunctionInfo(complete_smart_set_enabled), 'complete_smart_update': gi.FunctionInfo(complete_smart_update)})"
    __gdoc__ = 'Interface UDisksDriveAta\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksDriveAta (93969722179200)>'
    __info__ = InterfaceInfo(DriveAta)


