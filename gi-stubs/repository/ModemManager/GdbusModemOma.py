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


class GdbusModemOma(__gobject.GInterface):
    # no doc
    def call_accept_network_initiated_session(self, arg_session_id, arg_accept, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_accept_network_initiated_session(self, arg_session_id:int, arg_accept:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_accept_network_initiated_session_finish(self, res): # real signature unknown; restored from __doc__
        """ call_accept_network_initiated_session_finish(self, res:Gio.AsyncResult) """
        pass

    def call_accept_network_initiated_session_sync(self, arg_session_id, arg_accept, cancellable=None): # real signature unknown; restored from __doc__
        """ call_accept_network_initiated_session_sync(self, arg_session_id:int, arg_accept:bool, cancellable:Gio.Cancellable=None) """
        pass

    def call_cancel_session(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_cancel_session(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_cancel_session_finish(self, res): # real signature unknown; restored from __doc__
        """ call_cancel_session_finish(self, res:Gio.AsyncResult) """
        pass

    def call_cancel_session_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_cancel_session_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_setup(self, arg_features, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_setup(self, arg_features:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_setup_finish(self, res): # real signature unknown; restored from __doc__
        """ call_setup_finish(self, res:Gio.AsyncResult) """
        pass

    def call_setup_sync(self, arg_features, cancellable=None): # real signature unknown; restored from __doc__
        """ call_setup_sync(self, arg_features:int, cancellable:Gio.Cancellable=None) """
        pass

    def call_start_client_initiated_session(self, arg_session_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_start_client_initiated_session(self, arg_session_type:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_start_client_initiated_session_finish(self, res): # real signature unknown; restored from __doc__
        """ call_start_client_initiated_session_finish(self, res:Gio.AsyncResult) """
        pass

    def call_start_client_initiated_session_sync(self, arg_session_type, cancellable=None): # real signature unknown; restored from __doc__
        """ call_start_client_initiated_session_sync(self, arg_session_type:int, cancellable:Gio.Cancellable=None) """
        pass

    def complete_accept_network_initiated_session(self, invocation): # real signature unknown; restored from __doc__
        """ complete_accept_network_initiated_session(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_cancel_session(self, invocation): # real signature unknown; restored from __doc__
        """ complete_cancel_session(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_setup(self, invocation): # real signature unknown; restored from __doc__
        """ complete_setup(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_start_client_initiated_session(self, invocation): # real signature unknown; restored from __doc__
        """ complete_start_client_initiated_session(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def emit_session_state_changed(self, arg_old_session_state, arg_new_session_state, arg_session_state_failed_reason): # real signature unknown; restored from __doc__
        """ emit_session_state_changed(self, arg_old_session_state:int, arg_new_session_state:int, arg_session_state_failed_reason:int) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(GdbusModemOma), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusModemOma (94631948392352)>, '__dict__': <attribute '__dict__' of 'GdbusModemOma' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModemOma' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_accept_network_initiated_session': gi.FunctionInfo(call_accept_network_initiated_session), 'call_accept_network_initiated_session_finish': gi.FunctionInfo(call_accept_network_initiated_session_finish), 'call_accept_network_initiated_session_sync': gi.FunctionInfo(call_accept_network_initiated_session_sync), 'call_cancel_session': gi.FunctionInfo(call_cancel_session), 'call_cancel_session_finish': gi.FunctionInfo(call_cancel_session_finish), 'call_cancel_session_sync': gi.FunctionInfo(call_cancel_session_sync), 'call_setup': gi.FunctionInfo(call_setup), 'call_setup_finish': gi.FunctionInfo(call_setup_finish), 'call_setup_sync': gi.FunctionInfo(call_setup_sync), 'call_start_client_initiated_session': gi.FunctionInfo(call_start_client_initiated_session), 'call_start_client_initiated_session_finish': gi.FunctionInfo(call_start_client_initiated_session_finish), 'call_start_client_initiated_session_sync': gi.FunctionInfo(call_start_client_initiated_session_sync), 'complete_accept_network_initiated_session': gi.FunctionInfo(complete_accept_network_initiated_session), 'complete_cancel_session': gi.FunctionInfo(complete_cancel_session), 'complete_setup': gi.FunctionInfo(complete_setup), 'complete_start_client_initiated_session': gi.FunctionInfo(complete_start_client_initiated_session), 'emit_session_state_changed': gi.FunctionInfo(emit_session_state_changed)})"
    __gdoc__ = 'Interface MmGdbusModemOma\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusModemOma (94631948392352)>'
    __info__ = InterfaceInfo(GdbusModemOma)


