# encoding: utf-8
# module gi.repository.Gcr
# from /usr/lib64/girepository-1.0/Gcr-3.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gck as __gi_repository_Gck
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .Prompt import Prompt

class SystemPrompt(__gi_overrides_GObject.Object, Prompt, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        SystemPrompt(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, cancellable=None): # real signature unknown; restored from __doc__
        """ close(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def close_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ close_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def close_finish(self, result): # real signature unknown; restored from __doc__
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def confirm(self, cancellable=None): # real signature unknown; restored from __doc__
        """ confirm(self, cancellable:Gio.Cancellable=None) -> Gcr.PromptReply """
        pass

    def confirm_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ confirm_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def confirm_finish(self, result): # real signature unknown; restored from __doc__
        """ confirm_finish(self, result:Gio.AsyncResult) -> Gcr.PromptReply """
        pass

    def confirm_run(self, cancellable=None): # real signature unknown; restored from __doc__
        """ confirm_run(self, cancellable:Gio.Cancellable=None) -> Gcr.PromptReply """
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_get_domain(self): # real signature unknown; restored from __doc__
        """ error_get_domain() -> int """
        return 0

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_caller_window(self): # real signature unknown; restored from __doc__
        """ get_caller_window(self) -> str """
        return ""

    def get_cancel_label(self): # real signature unknown; restored from __doc__
        """ get_cancel_label(self) -> str """
        return ""

    def get_choice_chosen(self): # real signature unknown; restored from __doc__
        """ get_choice_chosen(self) -> bool """
        return False

    def get_choice_label(self): # real signature unknown; restored from __doc__
        """ get_choice_label(self) -> str """
        return ""

    def get_continue_label(self): # real signature unknown; restored from __doc__
        """ get_continue_label(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_message(self): # real signature unknown; restored from __doc__
        """ get_message(self) -> str """
        return ""

    def get_password_new(self): # real signature unknown; restored from __doc__
        """ get_password_new(self) -> bool """
        return False

    def get_password_strength(self): # real signature unknown; restored from __doc__
        """ get_password_strength(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_secret_exchange(self): # real signature unknown; restored from __doc__
        """ get_secret_exchange(self) -> Gcr.SecretExchange """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_warning(self): # real signature unknown; restored from __doc__
        """ get_warning(self) -> str """
        return ""

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_finish(self, res): # real signature unknown; restored from __doc__
        """ init_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, res): # real signature unknown; restored from __doc__
        """ new_finish(self, res:Gio.AsyncResult) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open(self, timeout_seconds, cancellable=None): # real signature unknown; restored from __doc__
        """ open(timeout_seconds:int, cancellable:Gio.Cancellable=None) -> Gcr.SystemPrompt """
        pass

    def open_async(self, timeout_seconds, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_async(timeout_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(result:Gio.AsyncResult) -> Gcr.SystemPrompt """
        pass

    def open_for_prompter(self, prompter_name=None, timeout_seconds, cancellable=None): # real signature unknown; restored from __doc__
        """ open_for_prompter(prompter_name:str=None, timeout_seconds:int, cancellable:Gio.Cancellable=None) -> Gcr.SystemPrompt """
        pass

    def open_for_prompter_async(self, prompter_name=None, timeout_seconds, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_for_prompter_async(prompter_name:str=None, timeout_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def password(self, cancellable=None): # real signature unknown; restored from __doc__
        """ password(self, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def password_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ password_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def password_finish(self, result): # real signature unknown; restored from __doc__
        """ password_finish(self, result:Gio.AsyncResult) -> str """
        return ""

    def password_run(self, cancellable=None): # real signature unknown; restored from __doc__
        """ password_run(self, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_caller_window(self, window_id): # real signature unknown; restored from __doc__
        """ set_caller_window(self, window_id:str) """
        pass

    def set_cancel_label(self, cancel_label): # real signature unknown; restored from __doc__
        """ set_cancel_label(self, cancel_label:str) """
        pass

    def set_choice_chosen(self, chosen): # real signature unknown; restored from __doc__
        """ set_choice_chosen(self, chosen:bool) """
        pass

    def set_choice_label(self, choice_label=None): # real signature unknown; restored from __doc__
        """ set_choice_label(self, choice_label:str=None) """
        pass

    def set_continue_label(self, continue_label): # real signature unknown; restored from __doc__
        """ set_continue_label(self, continue_label:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_message(self, message): # real signature unknown; restored from __doc__
        """ set_message(self, message:str) """
        pass

    def set_password_new(self, new_password): # real signature unknown; restored from __doc__
        """ set_password_new(self, new_password:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_warning(self, warning=None): # real signature unknown; restored from __doc__
        """ set_warning(self, warning:str=None) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7eff9cb5cd00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SystemPrompt), '__module__': 'gi.repository.Gcr', '__gtype__': <GType GcrSystemPrompt (94112497864880)>, '__doc__': None, '__gsignals__': {}, 'error_get_domain': gi.FunctionInfo(error_get_domain), 'open': gi.FunctionInfo(open), 'open_async': gi.FunctionInfo(open_async), 'open_finish': gi.FunctionInfo(open_finish), 'open_for_prompter': gi.FunctionInfo(open_for_prompter), 'open_for_prompter_async': gi.FunctionInfo(open_for_prompter_async), 'close': gi.FunctionInfo(close), 'close_async': gi.FunctionInfo(close_async), 'close_finish': gi.FunctionInfo(close_finish), 'get_secret_exchange': gi.FunctionInfo(get_secret_exchange), 'parent': <property object at 0x7eff9cfbad10>, 'pv': <property object at 0x7eff9cfbae00>})"
    __gdoc__ = 'Object GcrSystemPrompt\n\nProperties from GcrSystemPrompt:\n  bus-name -> gchararray: Bus name\n    Prompter bus name\n  secret-exchange -> GcrSecretExchange: Secret exchange\n    Secret exchange for passing passwords\n  timeout-seconds -> gint: Timeout seconds\n    Timeout (in seconds) for opening prompt\n\nSignals from GcrPrompt:\n  prompt-close ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GcrSystemPrompt (94112497864880)>'
    __info__ = ObjectInfo(SystemPrompt)

