# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class Session(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Session(**properties)
    """
    def add_service(self, uid, protocol, type): # real signature unknown; restored from __doc__
        """ add_service(self, uid:str, protocol:str, type:Camel.ProviderType) -> Camel.Service """
        pass

    def authenticate(self, service, mechanism=None, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ authenticate(self, service:Camel.Service, mechanism:str=None, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def authenticate_finish(self, result): # real signature unknown; restored from __doc__
        """ authenticate_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def authenticate_sync(self, service, mechanism=None, cancellable=None): # real signature unknown; restored from __doc__
        """ authenticate_sync(self, service:Camel.Service, mechanism:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def do_add_service(self, *args, **kwargs): # real signature unknown
        """ add_service(self, uid:str, protocol:str, type:Camel.ProviderType) -> Camel.Service """
        pass

    def do_authenticate_sync(self, *args, **kwargs): # real signature unknown
        """ authenticate_sync(self, service:Camel.Service, mechanism:str=None, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_forget_password(self, *args, **kwargs): # real signature unknown
        """ forget_password(self, service:Camel.Service, item:str) -> bool """
        pass

    def do_forward_to_sync(self, *args, **kwargs): # real signature unknown
        """ forward_to_sync(self, folder:Camel.Folder, message:Camel.MimeMessage, address:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_get_filter_driver(self, *args, **kwargs): # real signature unknown
        """ get_filter_driver(self, type:str, for_folder:Camel.Folder=None) -> Camel.FilterDriver """
        pass

    def do_get_oauth2_access_token_sync(self, *args, **kwargs): # real signature unknown
        """ get_oauth2_access_token_sync(self, service:Camel.Service, cancellable:Gio.Cancellable=None) -> bool, out_access_token:str, out_expires_in:int """
        pass

    def do_get_password(self, *args, **kwargs): # real signature unknown
        """ get_password(self, service:Camel.Service, prompt:str, item:str, flags:int) -> str """
        pass

    def do_get_recipient_certificates_sync(self, *args, **kwargs): # real signature unknown
        """ get_recipient_certificates_sync(self, flags:int, recipients:list, cancellable:Gio.Cancellable=None) -> bool, out_certificates:list """
        pass

    def do_job_finished(self, *args, **kwargs): # real signature unknown
        """ job_finished(self, cancellable:Gio.Cancellable=None, error:error) """
        pass

    def do_job_started(self, *args, **kwargs): # real signature unknown
        """ job_started(self, cancellable:Gio.Cancellable=None) """
        pass

    def do_lookup_addressbook(self, *args, **kwargs): # real signature unknown
        """ lookup_addressbook(self, name:str) -> bool """
        pass

    def do_remove_service(self, *args, **kwargs): # real signature unknown
        """ remove_service(self, service:Camel.Service) """
        pass

    def do_trust_prompt(self, *args, **kwargs): # real signature unknown
        """ trust_prompt(self, service:Camel.Service, certificate:Gio.TlsCertificate, errors:Gio.TlsCertificateFlags) -> Camel.CertTrust """
        pass

    def do_user_alert(self, *args, **kwargs): # real signature unknown
        """ user_alert(self, service:Camel.Service, type:Camel.SessionAlertType, message:str) """
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

    def forget_password(self, service, item): # real signature unknown; restored from __doc__
        """ forget_password(self, service:Camel.Service, item:str) -> bool """
        return False

    def forward_to(self, folder, message, address, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ forward_to(self, folder:Camel.Folder, message:Camel.MimeMessage, address:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def forward_to_finish(self, result): # real signature unknown; restored from __doc__
        """ forward_to_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def forward_to_sync(self, folder, message, address, cancellable=None): # real signature unknown; restored from __doc__
        """ forward_to_sync(self, folder:Camel.Folder, message:Camel.MimeMessage, address:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_filter_driver(self, type, for_folder=None): # real signature unknown; restored from __doc__
        """ get_filter_driver(self, type:str, for_folder:Camel.Folder=None) -> Camel.FilterDriver """
        pass

    def get_junk_filter(self): # real signature unknown; restored from __doc__
        """ get_junk_filter(self) -> Camel.JunkFilter """
        pass

    def get_junk_headers(self): # real signature unknown; restored from __doc__
        """ get_junk_headers(self) -> dict """
        return {}

    def get_oauth2_access_token_sync(self, service, cancellable=None): # real signature unknown; restored from __doc__
        """ get_oauth2_access_token_sync(self, service:Camel.Service, cancellable:Gio.Cancellable=None) -> bool, out_access_token:str, out_expires_in:int """
        return False

    def get_online(self): # real signature unknown; restored from __doc__
        """ get_online(self) -> bool """
        return False

    def get_password(self, service, prompt, item, flags): # real signature unknown; restored from __doc__
        """ get_password(self, service:Camel.Service, prompt:str, item:str, flags:int) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_recipient_certificates_sync(self, flags, recipients, cancellable=None): # real signature unknown; restored from __doc__
        """ get_recipient_certificates_sync(self, flags:int, recipients:list, cancellable:Gio.Cancellable=None) -> bool, out_certificates:list """
        return False

    def get_user_cache_dir(self): # real signature unknown; restored from __doc__
        """ get_user_cache_dir(self) -> str """
        return ""

    def get_user_data_dir(self): # real signature unknown; restored from __doc__
        """ get_user_data_dir(self) -> str """
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

    def idle_add(self, priority, function, data=None): # real signature unknown; restored from __doc__
        """ idle_add(self, priority:int, function:GLib.SourceFunc, data=None) -> int """
        return 0

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

    def list_services(self): # real signature unknown; restored from __doc__
        """ list_services(self) -> list """
        return []

    def lookup_addressbook(self, name): # real signature unknown; restored from __doc__
        """ lookup_addressbook(self, name:str) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
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

    def ref_main_context(self): # real signature unknown; restored from __doc__
        """ ref_main_context(self) -> GLib.MainContext """
        pass

    def ref_network_monitor(self): # real signature unknown; restored from __doc__
        """ ref_network_monitor(self) -> Gio.NetworkMonitor """
        pass

    def ref_service(self, uid): # real signature unknown; restored from __doc__
        """ ref_service(self, uid:str) -> Camel.Service """
        pass

    def ref_service_by_url(self, url, type): # real signature unknown; restored from __doc__
        """ ref_service_by_url(self, url:Camel.URL, type:Camel.ProviderType) -> Camel.Service """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_service(self, service): # real signature unknown; restored from __doc__
        """ remove_service(self, service:Camel.Service) """
        pass

    def remove_services(self): # real signature unknown; restored from __doc__
        """ remove_services(self) """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_junk_filter(self, junk_filter): # real signature unknown; restored from __doc__
        """ set_junk_filter(self, junk_filter:Camel.JunkFilter) """
        pass

    def set_junk_headers(self, headers, values): # real signature unknown; restored from __doc__
        """ set_junk_headers(self, headers:list, values:list) """
        pass

    def set_network_monitor(self, network_monitor=None): # real signature unknown; restored from __doc__
        """ set_network_monitor(self, network_monitor:Gio.NetworkMonitor=None) """
        pass

    def set_online(self, online): # real signature unknown; restored from __doc__
        """ set_online(self, online:bool) """
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

    def submit_job(self, description, callback, user_data=None): # real signature unknown; restored from __doc__
        """ submit_job(self, description:str, callback:Camel.SessionCallback, user_data=None) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def trust_prompt(self, service, certificate, errors): # real signature unknown; restored from __doc__
        """ trust_prompt(self, service:Camel.Service, certificate:Gio.TlsCertificate, errors:Gio.TlsCertificateFlags) -> Camel.CertTrust """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def user_alert(self, service, type, message): # real signature unknown; restored from __doc__
        """ user_alert(self, service:Camel.Service, type:Camel.SessionAlertType, message:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7b34c04550>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Session), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelSession (94124524160736)>, '__doc__': None, '__gsignals__': {}, 'add_service': gi.FunctionInfo(add_service), 'authenticate': gi.FunctionInfo(authenticate), 'authenticate_finish': gi.FunctionInfo(authenticate_finish), 'authenticate_sync': gi.FunctionInfo(authenticate_sync), 'forget_password': gi.FunctionInfo(forget_password), 'forward_to': gi.FunctionInfo(forward_to), 'forward_to_finish': gi.FunctionInfo(forward_to_finish), 'forward_to_sync': gi.FunctionInfo(forward_to_sync), 'get_filter_driver': gi.FunctionInfo(get_filter_driver), 'get_junk_filter': gi.FunctionInfo(get_junk_filter), 'get_junk_headers': gi.FunctionInfo(get_junk_headers), 'get_oauth2_access_token_sync': gi.FunctionInfo(get_oauth2_access_token_sync), 'get_online': gi.FunctionInfo(get_online), 'get_password': gi.FunctionInfo(get_password), 'get_recipient_certificates_sync': gi.FunctionInfo(get_recipient_certificates_sync), 'get_user_cache_dir': gi.FunctionInfo(get_user_cache_dir), 'get_user_data_dir': gi.FunctionInfo(get_user_data_dir), 'idle_add': gi.FunctionInfo(idle_add), 'list_services': gi.FunctionInfo(list_services), 'lookup_addressbook': gi.FunctionInfo(lookup_addressbook), 'ref_main_context': gi.FunctionInfo(ref_main_context), 'ref_network_monitor': gi.FunctionInfo(ref_network_monitor), 'ref_service': gi.FunctionInfo(ref_service), 'ref_service_by_url': gi.FunctionInfo(ref_service_by_url), 'remove_service': gi.FunctionInfo(remove_service), 'remove_services': gi.FunctionInfo(remove_services), 'set_junk_filter': gi.FunctionInfo(set_junk_filter), 'set_junk_headers': gi.FunctionInfo(set_junk_headers), 'set_network_monitor': gi.FunctionInfo(set_network_monitor), 'set_online': gi.FunctionInfo(set_online), 'submit_job': gi.FunctionInfo(submit_job), 'trust_prompt': gi.FunctionInfo(trust_prompt), 'user_alert': gi.FunctionInfo(user_alert), 'do_add_service': gi.VFuncInfo(add_service), 'do_authenticate_sync': gi.VFuncInfo(authenticate_sync), 'do_forget_password': gi.VFuncInfo(forget_password), 'do_forward_to_sync': gi.VFuncInfo(forward_to_sync), 'do_get_filter_driver': gi.VFuncInfo(get_filter_driver), 'do_get_oauth2_access_token_sync': gi.VFuncInfo(get_oauth2_access_token_sync), 'do_get_password': gi.VFuncInfo(get_password), 'do_get_recipient_certificates_sync': gi.VFuncInfo(get_recipient_certificates_sync), 'do_job_finished': gi.VFuncInfo(job_finished), 'do_job_started': gi.VFuncInfo(job_started), 'do_lookup_addressbook': gi.VFuncInfo(lookup_addressbook), 'do_remove_service': gi.VFuncInfo(remove_service), 'do_trust_prompt': gi.VFuncInfo(trust_prompt), 'do_user_alert': gi.VFuncInfo(user_alert), 'parent': <property object at 0x7f7b34f54040>, 'priv': <property object at 0x7f7b34f54130>})"
    __gdoc__ = 'Object CamelSession\n\nSignals from CamelSession:\n  job-started (GCancellable)\n  job-finished (GCancellable, GError)\n  user-alert (CamelService, CamelSessionAlertType, gchararray)\n\nProperties from CamelSession:\n  junk-filter -> CamelJunkFilter: Junk Filter\n    Classifies messages as junk or not junk\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  network-monitor -> GNetworkMonitor: Network Monitor\n  online -> gboolean: Online\n    Whether the shell is online\n  user-data-dir -> gchararray: User Data Directory\n    User-specific base directory for mail data\n  user-cache-dir -> gchararray: User Cache Directory\n    User-specific base directory for mail cache\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelSession (94124524160736)>'
    __info__ = ObjectInfo(Session)


