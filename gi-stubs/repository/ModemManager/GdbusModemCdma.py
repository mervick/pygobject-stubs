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


class GdbusModemCdma(__gobject.GInterface):
    # no doc
    def call_activate(self, arg_carrier_code, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_activate(self, arg_carrier_code:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_activate_finish(self, res): # real signature unknown; restored from __doc__
        """ call_activate_finish(self, res:Gio.AsyncResult) """
        pass

    def call_activate_manual(self, arg_properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_activate_manual(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_activate_manual_finish(self, res): # real signature unknown; restored from __doc__
        """ call_activate_manual_finish(self, res:Gio.AsyncResult) """
        pass

    def call_activate_manual_sync(self, arg_properties, cancellable=None): # real signature unknown; restored from __doc__
        """ call_activate_manual_sync(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_activate_sync(self, arg_carrier_code, cancellable=None): # real signature unknown; restored from __doc__
        """ call_activate_sync(self, arg_carrier_code:str, cancellable:Gio.Cancellable=None) """
        pass

    def complete_activate(self, invocation): # real signature unknown; restored from __doc__
        """ complete_activate(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_activate_manual(self, invocation): # real signature unknown; restored from __doc__
        """ complete_activate_manual(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def emit_activation_state_changed(self, arg_activation_state, arg_activation_error, arg_status_changes): # real signature unknown; restored from __doc__
        """ emit_activation_state_changed(self, arg_activation_state:int, arg_activation_error:int, arg_status_changes:GLib.Variant) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(GdbusModemCdma), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusModemCdma (94631948333536)>, '__dict__': <attribute '__dict__' of 'GdbusModemCdma' objects>, '__weakref__': <attribute '__weakref__' of 'GdbusModemCdma' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_activate': gi.FunctionInfo(call_activate), 'call_activate_finish': gi.FunctionInfo(call_activate_finish), 'call_activate_manual': gi.FunctionInfo(call_activate_manual), 'call_activate_manual_finish': gi.FunctionInfo(call_activate_manual_finish), 'call_activate_manual_sync': gi.FunctionInfo(call_activate_manual_sync), 'call_activate_sync': gi.FunctionInfo(call_activate_sync), 'complete_activate': gi.FunctionInfo(complete_activate), 'complete_activate_manual': gi.FunctionInfo(complete_activate_manual), 'emit_activation_state_changed': gi.FunctionInfo(emit_activation_state_changed)})"
    __gdoc__ = 'Interface MmGdbusModemCdma\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusModemCdma (94631948333536)>'
    __info__ = InterfaceInfo(GdbusModemCdma)


