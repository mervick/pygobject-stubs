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


class GdbusModemVoice(__gobject.GInterface):
    # no doc
    def call_call_waiting_query(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_call_waiting_query(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_call_waiting_query_finish(self, res): # real signature unknown; restored from __doc__
        """ call_call_waiting_query_finish(self, res:Gio.AsyncResult) -> out_status:bool """
        pass

    def call_call_waiting_query_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_call_waiting_query_sync(self, cancellable:Gio.Cancellable=None) -> out_status:bool """
        pass

    def call_call_waiting_setup(self, arg_enable, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_call_waiting_setup(self, arg_enable:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_call_waiting_setup_finish(self, res): # real signature unknown; restored from __doc__
        """ call_call_waiting_setup_finish(self, res:Gio.AsyncResult) """
        pass

    def call_call_waiting_setup_sync(self, arg_enable, cancellable=None): # real signature unknown; restored from __doc__
        """ call_call_waiting_setup_sync(self, arg_enable:bool, cancellable:Gio.Cancellable=None) """
        pass

    def call_create_call(self, arg_properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_create_call(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_create_call_finish(self, res): # real signature unknown; restored from __doc__
        """ call_create_call_finish(self, res:Gio.AsyncResult) -> out_path:str """
        pass

    def call_create_call_sync(self, arg_properties, cancellable=None): # real signature unknown; restored from __doc__
        """ call_create_call_sync(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_path:str """
        pass

    def call_delete_call(self, arg_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_delete_call(self, arg_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_delete_call_finish(self, res): # real signature unknown; restored from __doc__
        """ call_delete_call_finish(self, res:Gio.AsyncResult) """
        pass

    def call_delete_call_sync(self, arg_path, cancellable=None): # real signature unknown; restored from __doc__
        """ call_delete_call_sync(self, arg_path:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_hangup_all(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_hangup_all(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_hangup_all_finish(self, res): # real signature unknown; restored from __doc__
        """ call_hangup_all_finish(self, res:Gio.AsyncResult) """
        pass

    def call_hangup_all_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_hangup_all_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_hangup_and_accept(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_hangup_and_accept(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_hangup_and_accept_finish(self, res): # real signature unknown; restored from __doc__
        """ call_hangup_and_accept_finish(self, res:Gio.AsyncResult) """
        pass

    def call_hangup_and_accept_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_hangup_and_accept_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_hold_and_accept(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_hold_and_accept(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_hold_and_accept_finish(self, res): # real signature unknown; restored from __doc__
        """ call_hold_and_accept_finish(self, res:Gio.AsyncResult) """
        pass

    def call_hold_and_accept_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_hold_and_accept_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_list_calls(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_list_calls(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_list_calls_finish(self, res): # real signature unknown; restored from __doc__
        """ call_list_calls_finish(self, res:Gio.AsyncResult) -> out_result:list """
        pass

    def call_list_calls_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_list_calls_sync(self, cancellable:Gio.Cancellable=None) -> out_result:list """
        pass

    def call_transfer(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_transfer(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_transfer_finish(self, res): # real signature unknown; restored from __doc__
        """ call_transfer_finish(self, res:Gio.AsyncResult) """
        pass

    def call_transfer_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_transfer_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def complete_call_waiting_query(self, invocation, status): # real signature unknown; restored from __doc__
        """ complete_call_waiting_query(self, invocation:Gio.DBusMethodInvocation, status:bool) """
        pass

    def complete_call_waiting_setup(self, invocation): # real signature unknown; restored from __doc__
        """ complete_call_waiting_setup(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_create_call(self, invocation, path): # real signature unknown; restored from __doc__
        """ complete_create_call(self, invocation:Gio.DBusMethodInvocation, path:str) """
        pass

    def complete_delete_call(self, invocation): # real signature unknown; restored from __doc__
        """ complete_delete_call(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_hangup_all(self, invocation): # real signature unknown; restored from __doc__
        """ complete_hangup_all(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_hangup_and_accept(self, invocation): # real signature unknown; restored from __doc__
        """ complete_hangup_and_accept(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_hold_and_accept(self, invocation): # real signature unknown; restored from __doc__
        """ complete_hold_and_accept(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_list_calls(self, invocation, result): # real signature unknown; restored from __doc__
        """ complete_list_calls(self, invocation:Gio.DBusMethodInvocation, result:str) """
        pass

    def complete_transfer(self, invocation): # real signature unknown; restored from __doc__
        """ complete_transfer(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def emit_call_added(self, arg_path): # real signature unknown; restored from __doc__
        """ emit_call_added(self, arg_path:str) """
        pass

    def emit_call_deleted(self, arg_path): # real signature unknown; restored from __doc__
        """ emit_call_deleted(self, arg_path:str) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(GdbusModemVoice), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusModemVoice (94631948458480)>, '__dict__': <attribute '__dict__' of 'GdbusModemVoice' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModemVoice' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_call_waiting_query': gi.FunctionInfo(call_call_waiting_query), 'call_call_waiting_query_finish': gi.FunctionInfo(call_call_waiting_query_finish), 'call_call_waiting_query_sync': gi.FunctionInfo(call_call_waiting_query_sync), 'call_call_waiting_setup': gi.FunctionInfo(call_call_waiting_setup), 'call_call_waiting_setup_finish': gi.FunctionInfo(call_call_waiting_setup_finish), 'call_call_waiting_setup_sync': gi.FunctionInfo(call_call_waiting_setup_sync), 'call_create_call': gi.FunctionInfo(call_create_call), 'call_create_call_finish': gi.FunctionInfo(call_create_call_finish), 'call_create_call_sync': gi.FunctionInfo(call_create_call_sync), 'call_delete_call': gi.FunctionInfo(call_delete_call), 'call_delete_call_finish': gi.FunctionInfo(call_delete_call_finish), 'call_delete_call_sync': gi.FunctionInfo(call_delete_call_sync), 'call_hangup_all': gi.FunctionInfo(call_hangup_all), 'call_hangup_all_finish': gi.FunctionInfo(call_hangup_all_finish), 'call_hangup_all_sync': gi.FunctionInfo(call_hangup_all_sync), 'call_hangup_and_accept': gi.FunctionInfo(call_hangup_and_accept), 'call_hangup_and_accept_finish': gi.FunctionInfo(call_hangup_and_accept_finish), 'call_hangup_and_accept_sync': gi.FunctionInfo(call_hangup_and_accept_sync), 'call_hold_and_accept': gi.FunctionInfo(call_hold_and_accept), 'call_hold_and_accept_finish': gi.FunctionInfo(call_hold_and_accept_finish), 'call_hold_and_accept_sync': gi.FunctionInfo(call_hold_and_accept_sync), 'call_list_calls': gi.FunctionInfo(call_list_calls), 'call_list_calls_finish': gi.FunctionInfo(call_list_calls_finish), 'call_list_calls_sync': gi.FunctionInfo(call_list_calls_sync), 'call_transfer': gi.FunctionInfo(call_transfer), 'call_transfer_finish': gi.FunctionInfo(call_transfer_finish), 'call_transfer_sync': gi.FunctionInfo(call_transfer_sync), 'complete_call_waiting_query': gi.FunctionInfo(complete_call_waiting_query), 'complete_call_waiting_setup': gi.FunctionInfo(complete_call_waiting_setup), 'complete_create_call': gi.FunctionInfo(complete_create_call), 'complete_delete_call': gi.FunctionInfo(complete_delete_call), 'complete_hangup_all': gi.FunctionInfo(complete_hangup_all), 'complete_hangup_and_accept': gi.FunctionInfo(complete_hangup_and_accept), 'complete_hold_and_accept': gi.FunctionInfo(complete_hold_and_accept), 'complete_list_calls': gi.FunctionInfo(complete_list_calls), 'complete_transfer': gi.FunctionInfo(complete_transfer), 'emit_call_added': gi.FunctionInfo(emit_call_added), 'emit_call_deleted': gi.FunctionInfo(emit_call_deleted)})"
    __gdoc__ = 'Interface MmGdbusModemVoice\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusModemVoice (94631948458480)>'
    __info__ = InterfaceInfo(GdbusModemVoice)


