# encoding: utf-8
# module gi.repository.WebKit2
# from /usr/lib64/girepository-1.0/WebKit2-4.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class WebContext(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        WebContext(**properties)
        new() -> WebKit2.WebContext
        new_ephemeral() -> WebKit2.WebContext
        new_with_website_data_manager(manager:WebKit2.WebsiteDataManager) -> WebKit2.WebContext
    """
    def add_path_to_sandbox(self, path, read_only): # real signature unknown; restored from __doc__
        """ add_path_to_sandbox(self, path:str, read_only:bool) """
        pass

    def allow_tls_certificate_for_host(self, certificate, host): # real signature unknown; restored from __doc__
        """ allow_tls_certificate_for_host(self, certificate:Gio.TlsCertificate, host:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_cache(self): # real signature unknown; restored from __doc__
        """ clear_cache(self) """
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

    def download_uri(self, uri): # real signature unknown; restored from __doc__
        """ download_uri(self, uri:str) -> WebKit2.Download """
        pass

    def do_automation_started(self, *args, **kwargs): # real signature unknown
        """ automation_started(self, session:WebKit2.AutomationSession) """
        pass

    def do_download_started(self, *args, **kwargs): # real signature unknown
        """ download_started(self, download:WebKit2.Download) """
        pass

    def do_initialize_notification_permissions(self, *args, **kwargs): # real signature unknown
        """ initialize_notification_permissions(self) """
        pass

    def do_initialize_web_extensions(self, *args, **kwargs): # real signature unknown
        """ initialize_web_extensions(self) """
        pass

    def do_user_message_received(self, *args, **kwargs): # real signature unknown
        """ user_message_received(self, message:WebKit2.UserMessage) -> bool """
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

    def get_cache_model(self): # real signature unknown; restored from __doc__
        """ get_cache_model(self) -> WebKit2.CacheModel """
        pass

    def get_cookie_manager(self): # real signature unknown; restored from __doc__
        """ get_cookie_manager(self) -> WebKit2.CookieManager """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> WebKit2.WebContext """
        pass

    def get_favicon_database(self): # real signature unknown; restored from __doc__
        """ get_favicon_database(self) -> WebKit2.FaviconDatabase """
        pass

    def get_favicon_database_directory(self): # real signature unknown; restored from __doc__
        """ get_favicon_database_directory(self) -> str """
        return ""

    def get_geolocation_manager(self): # real signature unknown; restored from __doc__
        """ get_geolocation_manager(self) -> WebKit2.GeolocationManager """
        pass

    def get_plugins(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_plugins(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_plugins_finish(self, result): # real signature unknown; restored from __doc__
        """ get_plugins_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def get_process_model(self): # real signature unknown; restored from __doc__
        """ get_process_model(self) -> WebKit2.ProcessModel """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sandbox_enabled(self): # real signature unknown; restored from __doc__
        """ get_sandbox_enabled(self) -> bool """
        return False

    def get_security_manager(self): # real signature unknown; restored from __doc__
        """ get_security_manager(self) -> WebKit2.SecurityManager """
        pass

    def get_spell_checking_enabled(self): # real signature unknown; restored from __doc__
        """ get_spell_checking_enabled(self) -> bool """
        return False

    def get_spell_checking_languages(self): # real signature unknown; restored from __doc__
        """ get_spell_checking_languages(self) -> list """
        return []

    def get_tls_errors_policy(self): # real signature unknown; restored from __doc__
        """ get_tls_errors_policy(self) -> WebKit2.TLSErrorsPolicy """
        pass

    def get_website_data_manager(self): # real signature unknown; restored from __doc__
        """ get_website_data_manager(self) -> WebKit2.WebsiteDataManager """
        pass

    def get_web_process_count_limit(self): # real signature unknown; restored from __doc__
        """ get_web_process_count_limit(self) -> int """
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

    def initialize_notification_permissions(self, allowed_origins, disallowed_origins): # real signature unknown; restored from __doc__
        """ initialize_notification_permissions(self, allowed_origins:list, disallowed_origins:list) """
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

    def is_automation_allowed(self): # real signature unknown; restored from __doc__
        """ is_automation_allowed(self) -> bool """
        return False

    def is_ephemeral(self): # real signature unknown; restored from __doc__
        """ is_ephemeral(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> WebKit2.WebContext """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_ephemeral(self): # real signature unknown; restored from __doc__
        """ new_ephemeral() -> WebKit2.WebContext """
        pass

    def new_with_website_data_manager(self, manager): # real signature unknown; restored from __doc__
        """ new_with_website_data_manager(manager:WebKit2.WebsiteDataManager) -> WebKit2.WebContext """
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

    def prefetch_dns(self, hostname): # real signature unknown; restored from __doc__
        """ prefetch_dns(self, hostname:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register_uri_scheme(self, scheme, callback, user_data=None): # real signature unknown; restored from __doc__
        """ register_uri_scheme(self, scheme:str, callback:WebKit2.URISchemeRequestCallback, user_data=None) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_message_to_all_extensions(self, message): # real signature unknown; restored from __doc__
        """ send_message_to_all_extensions(self, message:WebKit2.UserMessage) """
        pass

    def set_additional_plugins_directory(self, directory): # real signature unknown; restored from __doc__
        """ set_additional_plugins_directory(self, directory:str) """
        pass

    def set_automation_allowed(self, allowed): # real signature unknown; restored from __doc__
        """ set_automation_allowed(self, allowed:bool) """
        pass

    def set_cache_model(self, cache_model): # real signature unknown; restored from __doc__
        """ set_cache_model(self, cache_model:WebKit2.CacheModel) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_disk_cache_directory(self, directory): # real signature unknown; restored from __doc__
        """ set_disk_cache_directory(self, directory:str) """
        pass

    def set_favicon_database_directory(self, path=None): # real signature unknown; restored from __doc__
        """ set_favicon_database_directory(self, path:str=None) """
        pass

    def set_network_proxy_settings(self, proxy_mode, proxy_settings=None): # real signature unknown; restored from __doc__
        """ set_network_proxy_settings(self, proxy_mode:WebKit2.NetworkProxyMode, proxy_settings:WebKit2.NetworkProxySettings=None) """
        pass

    def set_preferred_languages(self, languages=None): # real signature unknown; restored from __doc__
        """ set_preferred_languages(self, languages:list=None) """
        pass

    def set_process_model(self, process_model): # real signature unknown; restored from __doc__
        """ set_process_model(self, process_model:WebKit2.ProcessModel) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sandbox_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_sandbox_enabled(self, enabled:bool) """
        pass

    def set_spell_checking_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_spell_checking_enabled(self, enabled:bool) """
        pass

    def set_spell_checking_languages(self, languages): # real signature unknown; restored from __doc__
        """ set_spell_checking_languages(self, languages:list) """
        pass

    def set_tls_errors_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_tls_errors_policy(self, policy:WebKit2.TLSErrorsPolicy) """
        pass

    def set_web_extensions_directory(self, directory): # real signature unknown; restored from __doc__
        """ set_web_extensions_directory(self, directory:str) """
        pass

    def set_web_extensions_initialization_user_data(self, user_data): # real signature unknown; restored from __doc__
        """ set_web_extensions_initialization_user_data(self, user_data:GLib.Variant) """
        pass

    def set_web_process_count_limit(self, limit): # real signature unknown; restored from __doc__
        """ set_web_process_count_limit(self, limit:int) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc3e6f4a9a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(WebContext), '__module__': 'gi.repository.WebKit2', '__gtype__': <GType WebKitWebContext (94869774796976)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_ephemeral': gi.FunctionInfo(new_ephemeral), 'new_with_website_data_manager': gi.FunctionInfo(new_with_website_data_manager), 'get_default': gi.FunctionInfo(get_default), 'add_path_to_sandbox': gi.FunctionInfo(add_path_to_sandbox), 'allow_tls_certificate_for_host': gi.FunctionInfo(allow_tls_certificate_for_host), 'clear_cache': gi.FunctionInfo(clear_cache), 'download_uri': gi.FunctionInfo(download_uri), 'get_cache_model': gi.FunctionInfo(get_cache_model), 'get_cookie_manager': gi.FunctionInfo(get_cookie_manager), 'get_favicon_database': gi.FunctionInfo(get_favicon_database), 'get_favicon_database_directory': gi.FunctionInfo(get_favicon_database_directory), 'get_geolocation_manager': gi.FunctionInfo(get_geolocation_manager), 'get_plugins': gi.FunctionInfo(get_plugins), 'get_plugins_finish': gi.FunctionInfo(get_plugins_finish), 'get_process_model': gi.FunctionInfo(get_process_model), 'get_sandbox_enabled': gi.FunctionInfo(get_sandbox_enabled), 'get_security_manager': gi.FunctionInfo(get_security_manager), 'get_spell_checking_enabled': gi.FunctionInfo(get_spell_checking_enabled), 'get_spell_checking_languages': gi.FunctionInfo(get_spell_checking_languages), 'get_tls_errors_policy': gi.FunctionInfo(get_tls_errors_policy), 'get_web_process_count_limit': gi.FunctionInfo(get_web_process_count_limit), 'get_website_data_manager': gi.FunctionInfo(get_website_data_manager), 'initialize_notification_permissions': gi.FunctionInfo(initialize_notification_permissions), 'is_automation_allowed': gi.FunctionInfo(is_automation_allowed), 'is_ephemeral': gi.FunctionInfo(is_ephemeral), 'prefetch_dns': gi.FunctionInfo(prefetch_dns), 'register_uri_scheme': gi.FunctionInfo(register_uri_scheme), 'send_message_to_all_extensions': gi.FunctionInfo(send_message_to_all_extensions), 'set_additional_plugins_directory': gi.FunctionInfo(set_additional_plugins_directory), 'set_automation_allowed': gi.FunctionInfo(set_automation_allowed), 'set_cache_model': gi.FunctionInfo(set_cache_model), 'set_disk_cache_directory': gi.FunctionInfo(set_disk_cache_directory), 'set_favicon_database_directory': gi.FunctionInfo(set_favicon_database_directory), 'set_network_proxy_settings': gi.FunctionInfo(set_network_proxy_settings), 'set_preferred_languages': gi.FunctionInfo(set_preferred_languages), 'set_process_model': gi.FunctionInfo(set_process_model), 'set_sandbox_enabled': gi.FunctionInfo(set_sandbox_enabled), 'set_spell_checking_enabled': gi.FunctionInfo(set_spell_checking_enabled), 'set_spell_checking_languages': gi.FunctionInfo(set_spell_checking_languages), 'set_tls_errors_policy': gi.FunctionInfo(set_tls_errors_policy), 'set_web_extensions_directory': gi.FunctionInfo(set_web_extensions_directory), 'set_web_extensions_initialization_user_data': gi.FunctionInfo(set_web_extensions_initialization_user_data), 'set_web_process_count_limit': gi.FunctionInfo(set_web_process_count_limit), 'do_automation_started': gi.VFuncInfo(automation_started), 'do_download_started': gi.VFuncInfo(download_started), 'do_initialize_notification_permissions': gi.VFuncInfo(initialize_notification_permissions), 'do_initialize_web_extensions': gi.VFuncInfo(initialize_web_extensions), 'do_user_message_received': gi.VFuncInfo(user_message_received), 'parent': <property object at 0x7fc3e7186400>, 'priv': <property object at 0x7fc3e7186630>})"
    __gdoc__ = 'Object WebKitWebContext\n\nSignals from WebKitWebContext:\n  download-started (WebKitDownload)\n  initialize-web-extensions ()\n  initialize-notification-permissions ()\n  automation-started (WebKitAutomationSession)\n  user-message-received (WebKitUserMessage) -> gboolean\n\nProperties from WebKitWebContext:\n  local-storage-directory -> gchararray: Local Storage Directory\n    The directory where local storage data will be saved\n  website-data-manager -> WebKitWebsiteDataManager: Website Data Manager\n    The WebKitWebsiteDataManager associated with this context\n  process-swap-on-cross-site-navigation-enabled -> gboolean: Swap Processes on Cross-Site Navigation\n    Whether swap Web processes on cross-site navigations is enabled\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitWebContext (94869774796976)>'
    __info__ = ObjectInfo(WebContext)


