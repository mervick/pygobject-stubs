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


class WorkerManager(__gobject.GInterface):
    # no doc
    def call_choice_list_query(self, arg_service_name, arg_prompt_message, arg_query, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_choice_list_query(self, arg_service_name:str, arg_prompt_message:str, arg_query:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_choice_list_query_finish(self, res): # real signature unknown; restored from __doc__
        """ call_choice_list_query_finish(self, res:Gio.AsyncResult) -> out_answer:str """
        pass

    def call_choice_list_query_sync(self, arg_service_name, arg_prompt_message, arg_query, cancellable=None): # real signature unknown; restored from __doc__
        """ call_choice_list_query_sync(self, arg_service_name:str, arg_prompt_message:str, arg_query:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_answer:str """
        pass

    def call_hello(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_hello(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_hello_finish(self, res): # real signature unknown; restored from __doc__
        """ call_hello_finish(self, res:Gio.AsyncResult) """
        pass

    def call_hello_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_hello_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_info(self, arg_service_name, arg_info, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_info(self, arg_service_name:str, arg_info:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_info_finish(self, res): # real signature unknown; restored from __doc__
        """ call_info_finish(self, res:Gio.AsyncResult) """
        pass

    def call_info_query(self, arg_service_name, arg_query, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_info_query(self, arg_service_name:str, arg_query:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_info_query_finish(self, res): # real signature unknown; restored from __doc__
        """ call_info_query_finish(self, res:Gio.AsyncResult) -> out_answer:str """
        pass

    def call_info_query_sync(self, arg_service_name, arg_query, cancellable=None): # real signature unknown; restored from __doc__
        """ call_info_query_sync(self, arg_service_name:str, arg_query:str, cancellable:Gio.Cancellable=None) -> out_answer:str """
        pass

    def call_info_sync(self, arg_service_name, arg_info, cancellable=None): # real signature unknown; restored from __doc__
        """ call_info_sync(self, arg_service_name:str, arg_info:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_problem(self, arg_service_name, arg_problem, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_problem(self, arg_service_name:str, arg_problem:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_problem_finish(self, res): # real signature unknown; restored from __doc__
        """ call_problem_finish(self, res:Gio.AsyncResult) """
        pass

    def call_problem_sync(self, arg_service_name, arg_problem, cancellable=None): # real signature unknown; restored from __doc__
        """ call_problem_sync(self, arg_service_name:str, arg_problem:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_secret_info_query(self, arg_service_name, arg_query, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_secret_info_query(self, arg_service_name:str, arg_query:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_secret_info_query_finish(self, res): # real signature unknown; restored from __doc__
        """ call_secret_info_query_finish(self, res:Gio.AsyncResult) -> out_answer:str """
        pass

    def call_secret_info_query_sync(self, arg_service_name, arg_query, cancellable=None): # real signature unknown; restored from __doc__
        """ call_secret_info_query_sync(self, arg_service_name:str, arg_query:str, cancellable:Gio.Cancellable=None) -> out_answer:str """
        pass

    def complete_choice_list_query(self, invocation, answer): # real signature unknown; restored from __doc__
        """ complete_choice_list_query(self, invocation:Gio.DBusMethodInvocation, answer:str) """
        pass

    def complete_hello(self, invocation): # real signature unknown; restored from __doc__
        """ complete_hello(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_info(self, invocation): # real signature unknown; restored from __doc__
        """ complete_info(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_info_query(self, invocation, answer): # real signature unknown; restored from __doc__
        """ complete_info_query(self, invocation:Gio.DBusMethodInvocation, answer:str) """
        pass

    def complete_problem(self, invocation): # real signature unknown; restored from __doc__
        """ complete_problem(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_secret_info_query(self, invocation, answer): # real signature unknown; restored from __doc__
        """ complete_secret_info_query(self, invocation:Gio.DBusMethodInvocation, answer:str) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(WorkerManager), '__module__': 'gi.repository.Gdm', '__gtype__': <GType GdmWorkerManager (94876617242400)>, '__dict__': <attribute '__dict__' of 'WorkerManager' objects>, '__weakref__': <attribute '__weakref__' of 'WorkerManager' objects>, '__doc__': None, '__gsignals__': {}, 'interface_info': gi.FunctionInfo(interface_info), 'override_properties': gi.FunctionInfo(override_properties), 'call_choice_list_query': gi.FunctionInfo(call_choice_list_query), 'call_choice_list_query_finish': gi.FunctionInfo(call_choice_list_query_finish), 'call_choice_list_query_sync': gi.FunctionInfo(call_choice_list_query_sync), 'call_hello': gi.FunctionInfo(call_hello), 'call_hello_finish': gi.FunctionInfo(call_hello_finish), 'call_hello_sync': gi.FunctionInfo(call_hello_sync), 'call_info': gi.FunctionInfo(call_info), 'call_info_finish': gi.FunctionInfo(call_info_finish), 'call_info_query': gi.FunctionInfo(call_info_query), 'call_info_query_finish': gi.FunctionInfo(call_info_query_finish), 'call_info_query_sync': gi.FunctionInfo(call_info_query_sync), 'call_info_sync': gi.FunctionInfo(call_info_sync), 'call_problem': gi.FunctionInfo(call_problem), 'call_problem_finish': gi.FunctionInfo(call_problem_finish), 'call_problem_sync': gi.FunctionInfo(call_problem_sync), 'call_secret_info_query': gi.FunctionInfo(call_secret_info_query), 'call_secret_info_query_finish': gi.FunctionInfo(call_secret_info_query_finish), 'call_secret_info_query_sync': gi.FunctionInfo(call_secret_info_query_sync), 'complete_choice_list_query': gi.FunctionInfo(complete_choice_list_query), 'complete_hello': gi.FunctionInfo(complete_hello), 'complete_info': gi.FunctionInfo(complete_info), 'complete_info_query': gi.FunctionInfo(complete_info_query), 'complete_problem': gi.FunctionInfo(complete_problem), 'complete_secret_info_query': gi.FunctionInfo(complete_secret_info_query)})"
    __gdoc__ = 'Interface GdmWorkerManager\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GdmWorkerManager (94876617242400)>'
    __info__ = InterfaceInfo(WorkerManager)


