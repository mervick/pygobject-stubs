# encoding: utf-8
# module gi.repository.Gdm
# from /usr/lib64/girepository-1.0/Gdm-1.0.typelib
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


class Greeter(__gobject.GInterface):
    # no doc
    def call_begin_auto_login(self, arg_username, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_begin_auto_login(self, arg_username:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_begin_auto_login_finish(self, res): # real signature unknown; restored from __doc__
        """ call_begin_auto_login_finish(self, res:Gio.AsyncResult) """
        pass

    def call_begin_auto_login_sync(self, arg_username, cancellable=None): # real signature unknown; restored from __doc__
        """ call_begin_auto_login_sync(self, arg_username:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_get_timed_login_details(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_get_timed_login_details(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_get_timed_login_details_finish(self, res): # real signature unknown; restored from __doc__
        """ call_get_timed_login_details_finish(self, res:Gio.AsyncResult) -> out_enabled:bool, out_username:str, out_delay:int """
        pass

    def call_get_timed_login_details_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_get_timed_login_details_sync(self, cancellable:Gio.Cancellable=None) -> out_enabled:bool, out_username:str, out_delay:int """
        pass

    def call_select_session(self, arg_session, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_select_session(self, arg_session:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_select_session_finish(self, res): # real signature unknown; restored from __doc__
        """ call_select_session_finish(self, res:Gio.AsyncResult) """
        pass

    def call_select_session_sync(self, arg_session, cancellable=None): # real signature unknown; restored from __doc__
        """ call_select_session_sync(self, arg_session:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_select_user(self, arg_username, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_select_user(self, arg_username:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_select_user_finish(self, res): # real signature unknown; restored from __doc__
        """ call_select_user_finish(self, res:Gio.AsyncResult) """
        pass

    def call_select_user_sync(self, arg_username, cancellable=None): # real signature unknown; restored from __doc__
        """ call_select_user_sync(self, arg_username:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_start_session_when_ready(self, arg_service_name, arg_should_start_session, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_start_session_when_ready(self, arg_service_name:str, arg_should_start_session:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_start_session_when_ready_finish(self, res): # real signature unknown; restored from __doc__
        """ call_start_session_when_ready_finish(self, res:Gio.AsyncResult) """
        pass

    def call_start_session_when_ready_sync(self, arg_service_name, arg_should_start_session, cancellable=None): # real signature unknown; restored from __doc__
        """ call_start_session_when_ready_sync(self, arg_service_name:str, arg_should_start_session:bool, cancellable:Gio.Cancellable=None) """
        pass

    def complete_begin_auto_login(self, invocation): # real signature unknown; restored from __doc__
        """ complete_begin_auto_login(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_get_timed_login_details(self, invocation, enabled, username, delay): # real signature unknown; restored from __doc__
        """ complete_get_timed_login_details(self, invocation:Gio.DBusMethodInvocation, enabled:bool, username:str, delay:int) """
        pass

    def complete_select_session(self, invocation): # real signature unknown; restored from __doc__
        """ complete_select_session(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_select_user(self, invocation): # real signature unknown; restored from __doc__
        """ complete_select_user(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_start_session_when_ready(self, invocation): # real signature unknown; restored from __doc__
        """ complete_start_session_when_ready(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def emit_default_language_name_changed(self, arg_language_name): # real signature unknown; restored from __doc__
        """ emit_default_language_name_changed(self, arg_language_name:str) """
        pass

    def emit_default_session_name_changed(self, arg_session_name): # real signature unknown; restored from __doc__
        """ emit_default_session_name_changed(self, arg_session_name:str) """
        pass

    def emit_reauthenticated(self, arg_service_name): # real signature unknown; restored from __doc__
        """ emit_reauthenticated(self, arg_service_name:str) """
        pass

    def emit_selected_user_changed(self, arg_username): # real signature unknown; restored from __doc__
        """ emit_selected_user_changed(self, arg_username:str) """
        pass

    def emit_session_opened(self, arg_service_name): # real signature unknown; restored from __doc__
        """ emit_session_opened(self, arg_service_name:str) """
        pass

    def emit_timed_login_requested(self, arg_username, arg_delay): # real signature unknown; restored from __doc__
        """ emit_timed_login_requested(self, arg_username:str, arg_delay:int) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Greeter), '__module__': 'gi.repository.Gdm', '__gtype__': <GType GdmGreeter (94876616979440)>, '__dict__': <attribute '__dict__' of 'Greeter' objects>, '__weakref__': <attribute '__weakref__' of 'Greeter' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_begin_auto_login': gi.FunctionInfo(call_begin_auto_login), 'call_begin_auto_login_finish': gi.FunctionInfo(call_begin_auto_login_finish), 'call_begin_auto_login_sync': gi.FunctionInfo(call_begin_auto_login_sync), 'call_get_timed_login_details': gi.FunctionInfo(call_get_timed_login_details), 'call_get_timed_login_details_finish': gi.FunctionInfo(call_get_timed_login_details_finish), 'call_get_timed_login_details_sync': gi.FunctionInfo(call_get_timed_login_details_sync), 'call_select_session': gi.FunctionInfo(call_select_session), 'call_select_session_finish': gi.FunctionInfo(call_select_session_finish), 'call_select_session_sync': gi.FunctionInfo(call_select_session_sync), 'call_select_user': gi.FunctionInfo(call_select_user), 'call_select_user_finish': gi.FunctionInfo(call_select_user_finish), 'call_select_user_sync': gi.FunctionInfo(call_select_user_sync), 'call_start_session_when_ready': gi.FunctionInfo(call_start_session_when_ready), 'call_start_session_when_ready_finish': gi.FunctionInfo(call_start_session_when_ready_finish), 'call_start_session_when_ready_sync': gi.FunctionInfo(call_start_session_when_ready_sync), 'complete_begin_auto_login': gi.FunctionInfo(complete_begin_auto_login), 'complete_get_timed_login_details': gi.FunctionInfo(complete_get_timed_login_details), 'complete_select_session': gi.FunctionInfo(complete_select_session), 'complete_select_user': gi.FunctionInfo(complete_select_user), 'complete_start_session_when_ready': gi.FunctionInfo(complete_start_session_when_ready), 'emit_default_language_name_changed': gi.FunctionInfo(emit_default_language_name_changed), 'emit_default_session_name_changed': gi.FunctionInfo(emit_default_session_name_changed), 'emit_reauthenticated': gi.FunctionInfo(emit_reauthenticated), 'emit_selected_user_changed': gi.FunctionInfo(emit_selected_user_changed), 'emit_session_opened': gi.FunctionInfo(emit_session_opened), 'emit_timed_login_requested': gi.FunctionInfo(emit_timed_login_requested)})"
    __gdoc__ = 'Interface GdmGreeter\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GdmGreeter (94876616979440)>'
    __info__ = InterfaceInfo(Greeter)


