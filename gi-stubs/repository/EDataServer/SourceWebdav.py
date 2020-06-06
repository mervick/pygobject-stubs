# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


from .SourceExtension import SourceExtension

class SourceWebdav(SourceExtension):
    """
    :Constructors:
    
    ::
    
        SourceWebdav(**properties)
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

    def dup_color(self): # real signature unknown; restored from __doc__
        """ dup_color(self) -> str """
        return ""

    def dup_display_name(self): # real signature unknown; restored from __doc__
        """ dup_display_name(self) -> str """
        return ""

    def dup_email_address(self): # real signature unknown; restored from __doc__
        """ dup_email_address(self) -> str """
        return ""

    def dup_resource_path(self): # real signature unknown; restored from __doc__
        """ dup_resource_path(self) -> str """
        return ""

    def dup_resource_query(self): # real signature unknown; restored from __doc__
        """ dup_resource_query(self) -> str """
        return ""

    def dup_soup_uri(self): # real signature unknown; restored from __doc__
        """ dup_soup_uri(self) -> Soup.URI """
        pass

    def dup_ssl_trust(self): # real signature unknown; restored from __doc__
        """ dup_ssl_trust(self) -> str """
        return ""

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

    def get_avoid_ifmatch(self): # real signature unknown; restored from __doc__
        """ get_avoid_ifmatch(self) -> bool """
        return False

    def get_calendar_auto_schedule(self): # real signature unknown; restored from __doc__
        """ get_calendar_auto_schedule(self) -> bool """
        return False

    def get_color(self): # real signature unknown; restored from __doc__
        """ get_color(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_email_address(self): # real signature unknown; restored from __doc__
        """ get_email_address(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resource_path(self): # real signature unknown; restored from __doc__
        """ get_resource_path(self) -> str """
        return ""

    def get_resource_query(self): # real signature unknown; restored from __doc__
        """ get_resource_query(self) -> str """
        return ""

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_ssl_trust(self): # real signature unknown; restored from __doc__
        """ get_ssl_trust(self) -> str """
        return ""

    def get_ssl_trust_response(self): # real signature unknown; restored from __doc__
        """ get_ssl_trust_response(self) -> EDataServer.TrustPromptResponse """
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

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def property_lock(self): # real signature unknown; restored from __doc__
        """ property_lock(self) """
        pass

    def property_unlock(self): # real signature unknown; restored from __doc__
        """ property_unlock(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_source(self): # real signature unknown; restored from __doc__
        """ ref_source(self) -> EDataServer.Source """
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

    def set_avoid_ifmatch(self, avoid_ifmatch): # real signature unknown; restored from __doc__
        """ set_avoid_ifmatch(self, avoid_ifmatch:bool) """
        pass

    def set_calendar_auto_schedule(self, calendar_auto_schedule): # real signature unknown; restored from __doc__
        """ set_calendar_auto_schedule(self, calendar_auto_schedule:bool) """
        pass

    def set_color(self, color=None): # real signature unknown; restored from __doc__
        """ set_color(self, color:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_display_name(self, display_name=None): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str=None) """
        pass

    def set_email_address(self, email_address=None): # real signature unknown; restored from __doc__
        """ set_email_address(self, email_address:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resource_path(self, resource_path=None): # real signature unknown; restored from __doc__
        """ set_resource_path(self, resource_path:str=None) """
        pass

    def set_resource_query(self, resource_query=None): # real signature unknown; restored from __doc__
        """ set_resource_query(self, resource_query:str=None) """
        pass

    def set_soup_uri(self, soup_uri): # real signature unknown; restored from __doc__
        """ set_soup_uri(self, soup_uri:Soup.URI) """
        pass

    def set_ssl_trust(self, ssl_trust=None): # real signature unknown; restored from __doc__
        """ set_ssl_trust(self, ssl_trust:str=None) """
        pass

    def set_ssl_trust_response(self, response): # real signature unknown; restored from __doc__
        """ set_ssl_trust_response(self, response:EDataServer.TrustPromptResponse) """
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

    def unset_temporary_ssl_trust(self): # real signature unknown; restored from __doc__
        """ unset_temporary_ssl_trust(self) """
        pass

    def update_ssl_trust(self, host, cert, response): # real signature unknown; restored from __doc__
        """ update_ssl_trust(self, host:str, cert:Gio.TlsCertificate, response:EDataServer.TrustPromptResponse) """
        pass

    def verify_ssl_trust(self, host, cert, cert_errors): # real signature unknown; restored from __doc__
        """ verify_ssl_trust(self, host:str, cert:Gio.TlsCertificate, cert_errors:Gio.TlsCertificateFlags) -> EDataServer.TrustPromptResponse """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f626e645250>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SourceWebdav), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ESourceWebdav (94877537343792)>, '__doc__': None, '__gsignals__': {}, 'dup_color': gi.FunctionInfo(dup_color), 'dup_display_name': gi.FunctionInfo(dup_display_name), 'dup_email_address': gi.FunctionInfo(dup_email_address), 'dup_resource_path': gi.FunctionInfo(dup_resource_path), 'dup_resource_query': gi.FunctionInfo(dup_resource_query), 'dup_soup_uri': gi.FunctionInfo(dup_soup_uri), 'dup_ssl_trust': gi.FunctionInfo(dup_ssl_trust), 'get_avoid_ifmatch': gi.FunctionInfo(get_avoid_ifmatch), 'get_calendar_auto_schedule': gi.FunctionInfo(get_calendar_auto_schedule), 'get_color': gi.FunctionInfo(get_color), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_email_address': gi.FunctionInfo(get_email_address), 'get_resource_path': gi.FunctionInfo(get_resource_path), 'get_resource_query': gi.FunctionInfo(get_resource_query), 'get_ssl_trust': gi.FunctionInfo(get_ssl_trust), 'get_ssl_trust_response': gi.FunctionInfo(get_ssl_trust_response), 'set_avoid_ifmatch': gi.FunctionInfo(set_avoid_ifmatch), 'set_calendar_auto_schedule': gi.FunctionInfo(set_calendar_auto_schedule), 'set_color': gi.FunctionInfo(set_color), 'set_display_name': gi.FunctionInfo(set_display_name), 'set_email_address': gi.FunctionInfo(set_email_address), 'set_resource_path': gi.FunctionInfo(set_resource_path), 'set_resource_query': gi.FunctionInfo(set_resource_query), 'set_soup_uri': gi.FunctionInfo(set_soup_uri), 'set_ssl_trust': gi.FunctionInfo(set_ssl_trust), 'set_ssl_trust_response': gi.FunctionInfo(set_ssl_trust_response), 'unset_temporary_ssl_trust': gi.FunctionInfo(unset_temporary_ssl_trust), 'update_ssl_trust': gi.FunctionInfo(update_ssl_trust), 'verify_ssl_trust': gi.FunctionInfo(verify_ssl_trust), 'parent': <property object at 0x7f626e8cee50>, 'priv': <property object at 0x7f626e8cef40>})"
    __gdoc__ = "Object ESourceWebdav\n\nProperties from ESourceWebdav:\n  avoid-ifmatch -> gboolean: Avoid If-Match\n    Work around a bug in old Apache servers\n  calendar-auto-schedule -> gboolean: Calendar Auto-Schedule\n    Whether the server handles meeting invitations (CalDAV-only)\n  color -> gchararray: Color\n    Color of the WebDAV resource\n  display-name -> gchararray: Display Name\n    Display name of the WebDAV resource\n  email-address -> gchararray: Email Address\n    The user's email address\n  resource-path -> gchararray: Resource Path\n    Absolute path to a WebDAV resource\n  resource-query -> gchararray: Resource Query\n    Query to access a WebDAV resource\n  soup-uri -> SoupURI: SoupURI\n    WebDAV service as a SoupURI\n  ssl-trust -> gchararray: SSL/TLS Trust\n    SSL/TLS certificate trust setting, for invalid server certificates\n\nProperties from ESourceExtension:\n  source -> ESource: Source\n    The ESource being extended\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ESourceWebdav (94877537343792)>'
    __info__ = ObjectInfo(SourceWebdav)


