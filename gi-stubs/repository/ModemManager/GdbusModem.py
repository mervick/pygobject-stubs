# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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


class GdbusModem(__gobject.GInterface):
    # no doc
    def call_command(self, arg_cmd, arg_timeout, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_command(self, arg_cmd:str, arg_timeout:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_command_finish(self, res): # real signature unknown; restored from __doc__
        """ call_command_finish(self, res:Gio.AsyncResult) -> out_response:str """
        pass

    def call_command_sync(self, arg_cmd, arg_timeout, cancellable=None): # real signature unknown; restored from __doc__
        """ call_command_sync(self, arg_cmd:str, arg_timeout:int, cancellable:Gio.Cancellable=None) -> out_response:str """
        pass

    def call_create_bearer(self, arg_properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_create_bearer(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_create_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ call_create_bearer_finish(self, res:Gio.AsyncResult) -> out_path:str """
        pass

    def call_create_bearer_sync(self, arg_properties, cancellable=None): # real signature unknown; restored from __doc__
        """ call_create_bearer_sync(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_path:str """
        pass

    def call_delete_bearer(self, arg_bearer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_delete_bearer(self, arg_bearer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_delete_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ call_delete_bearer_finish(self, res:Gio.AsyncResult) """
        pass

    def call_delete_bearer_sync(self, arg_bearer, cancellable=None): # real signature unknown; restored from __doc__
        """ call_delete_bearer_sync(self, arg_bearer:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_enable(self, arg_enable, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_enable(self, arg_enable:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_enable_finish(self, res): # real signature unknown; restored from __doc__
        """ call_enable_finish(self, res:Gio.AsyncResult) """
        pass

    def call_enable_sync(self, arg_enable, cancellable=None): # real signature unknown; restored from __doc__
        """ call_enable_sync(self, arg_enable:bool, cancellable:Gio.Cancellable=None) """
        pass

    def call_factory_reset(self, arg_code, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_factory_reset(self, arg_code:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_factory_reset_finish(self, res): # real signature unknown; restored from __doc__
        """ call_factory_reset_finish(self, res:Gio.AsyncResult) """
        pass

    def call_factory_reset_sync(self, arg_code, cancellable=None): # real signature unknown; restored from __doc__
        """ call_factory_reset_sync(self, arg_code:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_list_bearers(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_list_bearers(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_list_bearers_finish(self, res): # real signature unknown; restored from __doc__
        """ call_list_bearers_finish(self, res:Gio.AsyncResult) -> out_bearers:list """
        pass

    def call_list_bearers_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_list_bearers_sync(self, cancellable:Gio.Cancellable=None) -> out_bearers:list """
        pass

    def call_reset(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_reset(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_reset_finish(self, res): # real signature unknown; restored from __doc__
        """ call_reset_finish(self, res:Gio.AsyncResult) """
        pass

    def call_reset_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_reset_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_bands(self, arg_bands, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_bands(self, arg_bands:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_bands_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_bands_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_bands_sync(self, arg_bands, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_bands_sync(self, arg_bands:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_capabilities(self, arg_capabilities, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities(self, arg_capabilities:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_capabilities_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_capabilities_sync(self, arg_capabilities, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities_sync(self, arg_capabilities:int, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_modes(self, arg_modes, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_modes(self, arg_modes:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_modes_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_modes_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_modes_sync(self, arg_modes, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_modes_sync(self, arg_modes:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_power_state(self, arg_state, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_power_state(self, arg_state:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_power_state_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_power_state_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_power_state_sync(self, arg_state, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_power_state_sync(self, arg_state:int, cancellable:Gio.Cancellable=None) """
        pass

    def complete_command(self, invocation, response): # real signature unknown; restored from __doc__
        """ complete_command(self, invocation:Gio.DBusMethodInvocation, response:str) """
        pass

    def complete_create_bearer(self, invocation, path): # real signature unknown; restored from __doc__
        """ complete_create_bearer(self, invocation:Gio.DBusMethodInvocation, path:str) """
        pass

    def complete_delete_bearer(self, invocation): # real signature unknown; restored from __doc__
        """ complete_delete_bearer(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_enable(self, invocation): # real signature unknown; restored from __doc__
        """ complete_enable(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_factory_reset(self, invocation): # real signature unknown; restored from __doc__
        """ complete_factory_reset(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_list_bearers(self, invocation, bearers): # real signature unknown; restored from __doc__
        """ complete_list_bearers(self, invocation:Gio.DBusMethodInvocation, bearers:str) """
        pass

    def complete_reset(self, invocation): # real signature unknown; restored from __doc__
        """ complete_reset(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_bands(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_bands(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_capabilities(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_capabilities(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_modes(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_modes(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_power_state(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_power_state(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def emit_state_changed(self, arg_old, arg_new, arg_reason): # real signature unknown; restored from __doc__
        """ emit_state_changed(self, arg_old:int, arg_new:int, arg_reason:int) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(GdbusModem), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusModem (94631948083616)>, '__dict__': <attribute '__dict__' of 'GdbusModem' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModem' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_command': gi.FunctionInfo(call_command), 'call_command_finish': gi.FunctionInfo(call_command_finish), 'call_command_sync': gi.FunctionInfo(call_command_sync), 'call_create_bearer': gi.FunctionInfo(call_create_bearer), 'call_create_bearer_finish': gi.FunctionInfo(call_create_bearer_finish), 'call_create_bearer_sync': gi.FunctionInfo(call_create_bearer_sync), 'call_delete_bearer': gi.FunctionInfo(call_delete_bearer), 'call_delete_bearer_finish': gi.FunctionInfo(call_delete_bearer_finish), 'call_delete_bearer_sync': gi.FunctionInfo(call_delete_bearer_sync), 'call_enable': gi.FunctionInfo(call_enable), 'call_enable_finish': gi.FunctionInfo(call_enable_finish), 'call_enable_sync': gi.FunctionInfo(call_enable_sync), 'call_factory_reset': gi.FunctionInfo(call_factory_reset), 'call_factory_reset_finish': gi.FunctionInfo(call_factory_reset_finish), 'call_factory_reset_sync': gi.FunctionInfo(call_factory_reset_sync), 'call_list_bearers': gi.FunctionInfo(call_list_bearers), 'call_list_bearers_finish': gi.FunctionInfo(call_list_bearers_finish), 'call_list_bearers_sync': gi.FunctionInfo(call_list_bearers_sync), 'call_reset': gi.FunctionInfo(call_reset), 'call_reset_finish': gi.FunctionInfo(call_reset_finish), 'call_reset_sync': gi.FunctionInfo(call_reset_sync), 'call_set_current_bands': gi.FunctionInfo(call_set_current_bands), 'call_set_current_bands_finish': gi.FunctionInfo(call_set_current_bands_finish), 'call_set_current_bands_sync': gi.FunctionInfo(call_set_current_bands_sync), 'call_set_current_capabilities': gi.FunctionInfo(call_set_current_capabilities), 'call_set_current_capabilities_finish': gi.FunctionInfo(call_set_current_capabilities_finish), 'call_set_current_capabilities_sync': gi.FunctionInfo(call_set_current_capabilities_sync), 'call_set_current_modes': gi.FunctionInfo(call_set_current_modes), 'call_set_current_modes_finish': gi.FunctionInfo(call_set_current_modes_finish), 'call_set_current_modes_sync': gi.FunctionInfo(call_set_current_modes_sync), 'call_set_power_state': gi.FunctionInfo(call_set_power_state), 'call_set_power_state_finish': gi.FunctionInfo(call_set_power_state_finish), 'call_set_power_state_sync': gi.FunctionInfo(call_set_power_state_sync), 'complete_command': gi.FunctionInfo(complete_command), 'complete_create_bearer': gi.FunctionInfo(complete_create_bearer), 'complete_delete_bearer': gi.FunctionInfo(complete_delete_bearer), 'complete_enable': gi.FunctionInfo(complete_enable), 'complete_factory_reset': gi.FunctionInfo(complete_factory_reset), 'complete_list_bearers': gi.FunctionInfo(complete_list_bearers), 'complete_reset': gi.FunctionInfo(complete_reset), 'complete_set_current_bands': gi.FunctionInfo(complete_set_current_bands), 'complete_set_current_capabilities': gi.FunctionInfo(complete_set_current_capabilities), 'complete_set_current_modes': gi.FunctionInfo(complete_set_current_modes), 'complete_set_power_state': gi.FunctionInfo(complete_set_power_state), 'emit_state_changed': gi.FunctionInfo(emit_state_changed)})"
    __gdoc__ = 'Interface MmGdbusModem\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusModem (94631948083616)>'
    __info__ = InterfaceInfo(GdbusModem)


