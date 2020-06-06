# encoding: utf-8
# module gi.repository.GData
# from /usr/lib64/girepository-1.0/GData-0.0.typelib
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


from .Authorizer import Authorizer

class OAuth1Authorizer(__gi_overrides_GObject.Object, Authorizer):
    """
    :Constructors:
    
    ::
    
        OAuth1Authorizer(**properties)
        new(application_name:str=None, service_type:GType) -> GData.OAuth1Authorizer
        new_for_authorization_domains(application_name:str=None, authorization_domains:list) -> GData.OAuth1Authorizer
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
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

    def get_application_name(self): # real signature unknown; restored from __doc__
        """ get_application_name(self) -> str or None """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_proxy_resolver(self): # real signature unknown; restored from __doc__
        """ get_proxy_resolver(self) -> Gio.ProxyResolver or None """
        pass

    def get_proxy_uri(self): # real signature unknown; restored from __doc__
        """ get_proxy_uri(self) -> Soup.URI or None """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_timeout(self): # real signature unknown; restored from __doc__
        """ get_timeout(self) -> int """
        return 0

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

    def is_authorized_for_domain(self, domain): # real signature unknown; restored from __doc__
        """ is_authorized_for_domain(self, domain:GData.AuthorizationDomain) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, application_name=None, service_type): # real signature unknown; restored from __doc__
        """ new(application_name:str=None, service_type:GType) -> GData.OAuth1Authorizer """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_for_authorization_domains(self, application_name=None, authorization_domains): # real signature unknown; restored from __doc__
        """ new_for_authorization_domains(application_name:str=None, authorization_domains:list) -> GData.OAuth1Authorizer """
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

    def process_request(self, domain=None, message): # real signature unknown; restored from __doc__
        """ process_request(self, domain:GData.AuthorizationDomain=None, message:Soup.Message) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh_authorization(self, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_authorization(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def refresh_authorization_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ refresh_authorization_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def refresh_authorization_finish(self, async_result): # real signature unknown; restored from __doc__
        """ refresh_authorization_finish(self, async_result:Gio.AsyncResult) -> bool """
        return False

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def request_authentication_uri(self, cancellable=None): # real signature unknown; restored from __doc__
        """ request_authentication_uri(self, cancellable:Gio.Cancellable=None) -> str, token:str, token_secret:str """
        return ""

    def request_authentication_uri_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ request_authentication_uri_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def request_authentication_uri_finish(self, async_result): # real signature unknown; restored from __doc__
        """ request_authentication_uri_finish(self, async_result:Gio.AsyncResult) -> str, token:str, token_secret:str """
        return ""

    def request_authorization(self, token, token_secret, verifier, cancellable=None): # real signature unknown; restored from __doc__
        """ request_authorization(self, token:str, token_secret:str, verifier:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def request_authorization_async(self, token, token_secret, verifier, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ request_authorization_async(self, token:str, token_secret:str, verifier:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def request_authorization_finish(self, async_result): # real signature unknown; restored from __doc__
        """ request_authorization_finish(self, async_result:Gio.AsyncResult) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_locale(self, locale=None): # real signature unknown; restored from __doc__
        """ set_locale(self, locale:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_proxy_resolver(self, proxy_resolver=None): # real signature unknown; restored from __doc__
        """ set_proxy_resolver(self, proxy_resolver:Gio.ProxyResolver=None) """
        pass

    def set_proxy_uri(self, proxy_uri=None): # real signature unknown; restored from __doc__
        """ set_proxy_uri(self, proxy_uri:Soup.URI=None) """
        pass

    def set_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_timeout(self, timeout:int) """
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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fd5e1365040>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(OAuth1Authorizer), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataOAuth1Authorizer (94233464764096)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_for_authorization_domains': gi.FunctionInfo(new_for_authorization_domains), 'get_application_name': gi.FunctionInfo(get_application_name), 'get_locale': gi.FunctionInfo(get_locale), 'get_proxy_resolver': gi.FunctionInfo(get_proxy_resolver), 'get_proxy_uri': gi.FunctionInfo(get_proxy_uri), 'get_timeout': gi.FunctionInfo(get_timeout), 'request_authentication_uri': gi.FunctionInfo(request_authentication_uri), 'request_authentication_uri_async': gi.FunctionInfo(request_authentication_uri_async), 'request_authentication_uri_finish': gi.FunctionInfo(request_authentication_uri_finish), 'request_authorization': gi.FunctionInfo(request_authorization), 'request_authorization_async': gi.FunctionInfo(request_authorization_async), 'request_authorization_finish': gi.FunctionInfo(request_authorization_finish), 'set_locale': gi.FunctionInfo(set_locale), 'set_proxy_resolver': gi.FunctionInfo(set_proxy_resolver), 'set_proxy_uri': gi.FunctionInfo(set_proxy_uri), 'set_timeout': gi.FunctionInfo(set_timeout), 'parent': <property object at 0x7fd5e17521d0>, 'priv': <property object at 0x7fd5e17522c0>})"
    __gdoc__ = 'Object GDataOAuth1Authorizer\n\nProperties from GDataOAuth1Authorizer:\n  application-name -> gchararray: Application name\n    The human-readable, translated application name for the client.\n  locale -> gchararray: Locale\n    The locale to use for network requests, in Unix locale format.\n  proxy-uri -> SoupURI: Proxy URI\n    The proxy URI used internally for all network requests.\n  timeout -> guint: Timeout\n    A timeout, in seconds, for network operations.\n  proxy-resolver -> GProxyResolver: Proxy Resolver\n    A GProxyResolver used to determine a proxy URI.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataOAuth1Authorizer (94233464764096)>'
    __info__ = ObjectInfo(OAuth1Authorizer)


