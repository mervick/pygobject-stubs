# encoding: utf-8
# module gi.repository.Polkit
# from /usr/lib64/girepository-1.0/Polkit-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Authority(__gi_overrides_GObject.Object, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        Authority(**properties)
    """
    def authentication_agent_response(self, cookie, identity, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ authentication_agent_response(self, cookie:str, identity:Polkit.Identity, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def authentication_agent_response_finish(self, res): # real signature unknown; restored from __doc__
        """ authentication_agent_response_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def authentication_agent_response_sync(self, cookie, identity, cancellable=None): # real signature unknown; restored from __doc__
        """ authentication_agent_response_sync(self, cookie:str, identity:Polkit.Identity, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_authorization(self, subject, action_id, details=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ check_authorization(self, subject:Polkit.Subject, action_id:str, details:Polkit.Details=None, flags:Polkit.CheckAuthorizationFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def check_authorization_finish(self, res): # real signature unknown; restored from __doc__
        """ check_authorization_finish(self, res:Gio.AsyncResult) -> Polkit.AuthorizationResult """
        pass

    def check_authorization_sync(self, subject, action_id, details=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ check_authorization_sync(self, subject:Polkit.Subject, action_id:str, details:Polkit.Details=None, flags:Polkit.CheckAuthorizationFlags, cancellable:Gio.Cancellable=None) -> Polkit.AuthorizationResult """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def enumerate_actions(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_actions(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def enumerate_actions_finish(self, res): # real signature unknown; restored from __doc__
        """ enumerate_actions_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def enumerate_actions_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ enumerate_actions_sync(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def enumerate_temporary_authorizations(self, subject, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_temporary_authorizations(self, subject:Polkit.Subject, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def enumerate_temporary_authorizations_finish(self, res): # real signature unknown; restored from __doc__
        """ enumerate_temporary_authorizations_finish(self, res:Gio.AsyncResult) -> list """
        return []

    def enumerate_temporary_authorizations_sync(self, subject, cancellable=None): # real signature unknown; restored from __doc__
        """ enumerate_temporary_authorizations_sync(self, subject:Polkit.Subject, cancellable:Gio.Cancellable=None) -> list """
        return []

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

    def get(self): # real signature unknown; restored from __doc__
        """ get() -> Polkit.Authority """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_async(cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_backend_features(self): # real signature unknown; restored from __doc__
        """ get_backend_features(self) -> Polkit.AuthorityFeatures """
        pass

    def get_backend_name(self): # real signature unknown; restored from __doc__
        """ get_backend_name(self) -> str """
        return ""

    def get_backend_version(self): # real signature unknown; restored from __doc__
        """ get_backend_version(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_finish(self, res): # real signature unknown; restored from __doc__
        """ get_finish(res:Gio.AsyncResult) -> Polkit.Authority """
        pass

    def get_owner(self): # real signature unknown; restored from __doc__
        """ get_owner(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_sync(cancellable:Gio.Cancellable=None) -> Polkit.Authority """
        pass

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

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register_authentication_agent(self, subject, locale, object_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ register_authentication_agent(self, subject:Polkit.Subject, locale:str, object_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def register_authentication_agent_finish(self, res): # real signature unknown; restored from __doc__
        """ register_authentication_agent_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def register_authentication_agent_sync(self, subject, locale, object_path, cancellable=None): # real signature unknown; restored from __doc__
        """ register_authentication_agent_sync(self, subject:Polkit.Subject, locale:str, object_path:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def register_authentication_agent_with_options(self, subject, locale, object_path, options=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ register_authentication_agent_with_options(self, subject:Polkit.Subject, locale:str, object_path:str, options:GLib.Variant=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def register_authentication_agent_with_options_finish(self, res): # real signature unknown; restored from __doc__
        """ register_authentication_agent_with_options_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def register_authentication_agent_with_options_sync(self, subject, locale, object_path, options=None, cancellable=None): # real signature unknown; restored from __doc__
        """ register_authentication_agent_with_options_sync(self, subject:Polkit.Subject, locale:str, object_path:str, options:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def revoke_temporary_authorizations(self, subject, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ revoke_temporary_authorizations(self, subject:Polkit.Subject, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def revoke_temporary_authorizations_finish(self, res): # real signature unknown; restored from __doc__
        """ revoke_temporary_authorizations_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def revoke_temporary_authorizations_sync(self, subject, cancellable=None): # real signature unknown; restored from __doc__
        """ revoke_temporary_authorizations_sync(self, subject:Polkit.Subject, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def revoke_temporary_authorization_by_id(self, id, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ revoke_temporary_authorization_by_id(self, id:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def revoke_temporary_authorization_by_id_finish(self, res): # real signature unknown; restored from __doc__
        """ revoke_temporary_authorization_by_id_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def revoke_temporary_authorization_by_id_sync(self, id, cancellable=None): # real signature unknown; restored from __doc__
        """ revoke_temporary_authorization_by_id_sync(self, id:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    def unregister_authentication_agent(self, subject, object_path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unregister_authentication_agent(self, subject:Polkit.Subject, object_path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unregister_authentication_agent_finish(self, res): # real signature unknown; restored from __doc__
        """ unregister_authentication_agent_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def unregister_authentication_agent_sync(self, subject, object_path, cancellable=None): # real signature unknown; restored from __doc__
        """ unregister_authentication_agent_sync(self, subject:Polkit.Subject, object_path:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9827007d30>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Authority), '__module__': 'gi.repository.Polkit', '__gtype__': <GType PolkitAuthority (94810842971728)>, '__doc__': None, '__gsignals__': {}, 'get': gi.FunctionInfo(get), 'get_async': gi.FunctionInfo(get_async), 'get_finish': gi.FunctionInfo(get_finish), 'get_sync': gi.FunctionInfo(get_sync), 'authentication_agent_response': gi.FunctionInfo(authentication_agent_response), 'authentication_agent_response_finish': gi.FunctionInfo(authentication_agent_response_finish), 'authentication_agent_response_sync': gi.FunctionInfo(authentication_agent_response_sync), 'check_authorization': gi.FunctionInfo(check_authorization), 'check_authorization_finish': gi.FunctionInfo(check_authorization_finish), 'check_authorization_sync': gi.FunctionInfo(check_authorization_sync), 'enumerate_actions': gi.FunctionInfo(enumerate_actions), 'enumerate_actions_finish': gi.FunctionInfo(enumerate_actions_finish), 'enumerate_actions_sync': gi.FunctionInfo(enumerate_actions_sync), 'enumerate_temporary_authorizations': gi.FunctionInfo(enumerate_temporary_authorizations), 'enumerate_temporary_authorizations_finish': gi.FunctionInfo(enumerate_temporary_authorizations_finish), 'enumerate_temporary_authorizations_sync': gi.FunctionInfo(enumerate_temporary_authorizations_sync), 'get_backend_features': gi.FunctionInfo(get_backend_features), 'get_backend_name': gi.FunctionInfo(get_backend_name), 'get_backend_version': gi.FunctionInfo(get_backend_version), 'get_owner': gi.FunctionInfo(get_owner), 'register_authentication_agent': gi.FunctionInfo(register_authentication_agent), 'register_authentication_agent_finish': gi.FunctionInfo(register_authentication_agent_finish), 'register_authentication_agent_sync': gi.FunctionInfo(register_authentication_agent_sync), 'register_authentication_agent_with_options': gi.FunctionInfo(register_authentication_agent_with_options), 'register_authentication_agent_with_options_finish': gi.FunctionInfo(register_authentication_agent_with_options_finish), 'register_authentication_agent_with_options_sync': gi.FunctionInfo(register_authentication_agent_with_options_sync), 'revoke_temporary_authorization_by_id': gi.FunctionInfo(revoke_temporary_authorization_by_id), 'revoke_temporary_authorization_by_id_finish': gi.FunctionInfo(revoke_temporary_authorization_by_id_finish), 'revoke_temporary_authorization_by_id_sync': gi.FunctionInfo(revoke_temporary_authorization_by_id_sync), 'revoke_temporary_authorizations': gi.FunctionInfo(revoke_temporary_authorizations), 'revoke_temporary_authorizations_finish': gi.FunctionInfo(revoke_temporary_authorizations_finish), 'revoke_temporary_authorizations_sync': gi.FunctionInfo(revoke_temporary_authorizations_sync), 'unregister_authentication_agent': gi.FunctionInfo(unregister_authentication_agent), 'unregister_authentication_agent_finish': gi.FunctionInfo(unregister_authentication_agent_finish), 'unregister_authentication_agent_sync': gi.FunctionInfo(unregister_authentication_agent_sync)})"
    __gdoc__ = 'Object PolkitAuthority\n\nSignals from PolkitAuthority:\n  changed ()\n\nProperties from PolkitAuthority:\n  owner -> gchararray: Owner\n    Owner.\n  backend-name -> gchararray: Backend name\n    The name of the currently used Authority backend.\n  backend-version -> gchararray: Backend version\n    The version of the currently used Authority backend.\n  backend-features -> PolkitAuthorityFeatures: Backend features\n    The features of the currently used Authority backend.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PolkitAuthority (94810842971728)>'
    __info__ = ObjectInfo(Authority)


