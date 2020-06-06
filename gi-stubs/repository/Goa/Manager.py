# encoding: utf-8
# module gi.repository.Goa
# from /usr/lib64/girepository-1.0/Goa-1.0.typelib
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
    def call_add_account(self, arg_provider, arg_identity, arg_presentation_identity, arg_credentials, arg_details, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_add_account(self, arg_provider:str, arg_identity:str, arg_presentation_identity:str, arg_credentials:GLib.Variant, arg_details:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_add_account_finish(self, res): # real signature unknown; restored from __doc__
        """ call_add_account_finish(self, res:Gio.AsyncResult) -> out_account_object_path:str """
        pass

    def call_add_account_sync(self, arg_provider, arg_identity, arg_presentation_identity, arg_credentials, arg_details, cancellable=None): # real signature unknown; restored from __doc__
        """ call_add_account_sync(self, arg_provider:str, arg_identity:str, arg_presentation_identity:str, arg_credentials:GLib.Variant, arg_details:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_account_object_path:str """
        pass

    def call_is_supported_provider(self, arg_provider_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_is_supported_provider(self, arg_provider_type:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_is_supported_provider_finish(self, res): # real signature unknown; restored from __doc__
        """ call_is_supported_provider_finish(self, res:Gio.AsyncResult) -> out_is_supported:bool """
        pass

    def call_is_supported_provider_sync(self, arg_provider_type, cancellable=None): # real signature unknown; restored from __doc__
        """ call_is_supported_provider_sync(self, arg_provider_type:str, cancellable:Gio.Cancellable=None) -> out_is_supported:bool """
        pass

    def complete_add_account(self, invocation, account_object_path): # real signature unknown; restored from __doc__
        """ complete_add_account(self, invocation:Gio.DBusMethodInvocation, account_object_path:str) """
        pass

    def complete_is_supported_provider(self, invocation, is_supported): # real signature unknown; restored from __doc__
        """ complete_is_supported_provider(self, invocation:Gio.DBusMethodInvocation, is_supported:bool) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Manager), '__module__': 'gi.repository.Goa', '__gtype__': <GType GoaManager (94357270956176)>, '__dict__': <attribute '__dict__' of 'Manager' objects>, '__weakref__': <attribute '__weakref__' of 'Manager' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_add_account': gi.FunctionInfo(call_add_account), 'call_add_account_finish': gi.FunctionInfo(call_add_account_finish), 'call_add_account_sync': gi.FunctionInfo(call_add_account_sync), 'call_is_supported_provider': gi.FunctionInfo(call_is_supported_provider), 'call_is_supported_provider_finish': gi.FunctionInfo(call_is_supported_provider_finish), 'call_is_supported_provider_sync': gi.FunctionInfo(call_is_supported_provider_sync), 'complete_add_account': gi.FunctionInfo(complete_add_account), 'complete_is_supported_provider': gi.FunctionInfo(complete_is_supported_provider)})"
    __gdoc__ = 'Interface GoaManager\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GoaManager (94357270956176)>'
    __info__ = InterfaceInfo(Manager)


