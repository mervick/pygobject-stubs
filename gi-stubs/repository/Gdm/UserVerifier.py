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


class UserVerifier(__gobject.GInterface):
    # no doc
    def call_answer_query(self, arg_service_name, arg_answer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_answer_query(self, arg_service_name:str, arg_answer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_answer_query_finish(self, res): # real signature unknown; restored from __doc__
        """ call_answer_query_finish(self, res:Gio.AsyncResult) """
        pass

    def call_answer_query_sync(self, arg_service_name, arg_answer, cancellable=None): # real signature unknown; restored from __doc__
        """ call_answer_query_sync(self, arg_service_name:str, arg_answer:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_begin_verification(self, arg_service_name, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_begin_verification(self, arg_service_name:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_begin_verification_finish(self, res): # real signature unknown; restored from __doc__
        """ call_begin_verification_finish(self, res:Gio.AsyncResult) """
        pass

    def call_begin_verification_for_user(self, arg_service_name, arg_username, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_begin_verification_for_user(self, arg_service_name:str, arg_username:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_begin_verification_for_user_finish(self, res): # real signature unknown; restored from __doc__
        """ call_begin_verification_for_user_finish(self, res:Gio.AsyncResult) """
        pass

    def call_begin_verification_for_user_sync(self, arg_service_name, arg_username, cancellable=None): # real signature unknown; restored from __doc__
        """ call_begin_verification_for_user_sync(self, arg_service_name:str, arg_username:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_begin_verification_sync(self, arg_service_name, cancellable=None): # real signature unknown; restored from __doc__
        """ call_begin_verification_sync(self, arg_service_name:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_cancel(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_cancel(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_cancel_finish(self, res): # real signature unknown; restored from __doc__
        """ call_cancel_finish(self, res:Gio.AsyncResult) """
        pass

    def call_cancel_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_cancel_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_enable_extensions(self, arg_extensions, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_enable_extensions(self, arg_extensions:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_enable_extensions_finish(self, res): # real signature unknown; restored from __doc__
        """ call_enable_extensions_finish(self, res:Gio.AsyncResult) """
        pass

    def call_enable_extensions_sync(self, arg_extensions, cancellable=None): # real signature unknown; restored from __doc__
        """ call_enable_extensions_sync(self, arg_extensions:str, cancellable:Gio.Cancellable=None) """
        pass

    def complete_answer_query(self, invocation): # real signature unknown; restored from __doc__
        """ complete_answer_query(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_begin_verification(self, invocation): # real signature unknown; restored from __doc__
        """ complete_begin_verification(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_begin_verification_for_user(self, invocation): # real signature unknown; restored from __doc__
        """ complete_begin_verification_for_user(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_cancel(self, invocation): # real signature unknown; restored from __doc__
        """ complete_cancel(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_enable_extensions(self, invocation): # real signature unknown; restored from __doc__
        """ complete_enable_extensions(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def emit_conversation_started(self, arg_service_name): # real signature unknown; restored from __doc__
        """ emit_conversation_started(self, arg_service_name:str) """
        pass

    def emit_conversation_stopped(self, arg_service_name): # real signature unknown; restored from __doc__
        """ emit_conversation_stopped(self, arg_service_name:str) """
        pass

    def emit_info(self, arg_service_name, arg_info): # real signature unknown; restored from __doc__
        """ emit_info(self, arg_service_name:str, arg_info:str) """
        pass

    def emit_info_query(self, arg_service_name, arg_query): # real signature unknown; restored from __doc__
        """ emit_info_query(self, arg_service_name:str, arg_query:str) """
        pass

    def emit_problem(self, arg_service_name, arg_problem): # real signature unknown; restored from __doc__
        """ emit_problem(self, arg_service_name:str, arg_problem:str) """
        pass

    def emit_reauthentication_started(self, arg_pid_of_caller): # real signature unknown; restored from __doc__
        """ emit_reauthentication_started(self, arg_pid_of_caller:int) """
        pass

    def emit_reset(self): # real signature unknown; restored from __doc__
        """ emit_reset(self) """
        pass

    def emit_secret_info_query(self, arg_service_name, arg_query): # real signature unknown; restored from __doc__
        """ emit_secret_info_query(self, arg_service_name:str, arg_query:str) """
        pass

    def emit_service_unavailable(self, arg_service_name, arg_message): # real signature unknown; restored from __doc__
        """ emit_service_unavailable(self, arg_service_name:str, arg_message:str) """
        pass

    def emit_verification_complete(self, arg_service_name): # real signature unknown; restored from __doc__
        """ emit_verification_complete(self, arg_service_name:str) """
        pass

    def emit_verification_failed(self, arg_service_name): # real signature unknown; restored from __doc__
        """ emit_verification_failed(self, arg_service_name:str) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(UserVerifier), '__module__': 'gi.repository.Gdm', '__gtype__': <GType GdmUserVerifier (94876617051472)>, '__dict__': <attribute '__dict__' of 'UserVerifier' objects>, '__weakref__': <attribute '__weakref__' of 'UserVerifier' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_answer_query': gi.FunctionInfo(call_answer_query), 'call_answer_query_finish': gi.FunctionInfo(call_answer_query_finish), 'call_answer_query_sync': gi.FunctionInfo(call_answer_query_sync), 'call_begin_verification': gi.FunctionInfo(call_begin_verification), 'call_begin_verification_finish': gi.FunctionInfo(call_begin_verification_finish), 'call_begin_verification_for_user': gi.FunctionInfo(call_begin_verification_for_user), 'call_begin_verification_for_user_finish': gi.FunctionInfo(call_begin_verification_for_user_finish), 'call_begin_verification_for_user_sync': gi.FunctionInfo(call_begin_verification_for_user_sync), 'call_begin_verification_sync': gi.FunctionInfo(call_begin_verification_sync), 'call_cancel': gi.FunctionInfo(call_cancel), 'call_cancel_finish': gi.FunctionInfo(call_cancel_finish), 'call_cancel_sync': gi.FunctionInfo(call_cancel_sync), 'call_enable_extensions': gi.FunctionInfo(call_enable_extensions), 'call_enable_extensions_finish': gi.FunctionInfo(call_enable_extensions_finish), 'call_enable_extensions_sync': gi.FunctionInfo(call_enable_extensions_sync), 'complete_answer_query': gi.FunctionInfo(complete_answer_query), 'complete_begin_verification': gi.FunctionInfo(complete_begin_verification), 'complete_begin_verification_for_user': gi.FunctionInfo(complete_begin_verification_for_user), 'complete_cancel': gi.FunctionInfo(complete_cancel), 'complete_enable_extensions': gi.FunctionInfo(complete_enable_extensions), 'emit_conversation_started': gi.FunctionInfo(emit_conversation_started), 'emit_conversation_stopped': gi.FunctionInfo(emit_conversation_stopped), 'emit_info': gi.FunctionInfo(emit_info), 'emit_info_query': gi.FunctionInfo(emit_info_query), 'emit_problem': gi.FunctionInfo(emit_problem), 'emit_reauthentication_started': gi.FunctionInfo(emit_reauthentication_started), 'emit_reset': gi.FunctionInfo(emit_reset), 'emit_secret_info_query': gi.FunctionInfo(emit_secret_info_query), 'emit_service_unavailable': gi.FunctionInfo(emit_service_unavailable), 'emit_verification_complete': gi.FunctionInfo(emit_verification_complete), 'emit_verification_failed': gi.FunctionInfo(emit_verification_failed)})"
    __gdoc__ = 'Interface GdmUserVerifier\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GdmUserVerifier (94876617051472)>'
    __info__ = InterfaceInfo(UserVerifier)


