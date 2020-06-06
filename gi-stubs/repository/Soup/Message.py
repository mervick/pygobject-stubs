# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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


class Message(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Message(**properties)
        new(method:str, uri_string:str) -> Soup.Message or None
        new_from_uri(method:str, uri:Soup.URI) -> Soup.Message
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

    def content_sniffed(self, content_type, params): # real signature unknown; restored from __doc__
        """ content_sniffed(self, content_type:str, params:dict) """
        pass

    def disable_feature(self, feature_type): # real signature unknown; restored from __doc__
        """ disable_feature(self, feature_type:GType) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_finished(self, *args, **kwargs): # real signature unknown
        """ finished(self) """
        pass

    def do_got_body(self, *args, **kwargs): # real signature unknown
        """ got_body(self) """
        pass

    def do_got_chunk(self, *args, **kwargs): # real signature unknown
        """ got_chunk(self, chunk:Soup.Buffer) """
        pass

    def do_got_headers(self, *args, **kwargs): # real signature unknown
        """ got_headers(self) """
        pass

    def do_got_informational(self, *args, **kwargs): # real signature unknown
        """ got_informational(self) """
        pass

    def do_restarted(self, *args, **kwargs): # real signature unknown
        """ restarted(self) """
        pass

    def do_starting(self, *args, **kwargs): # real signature unknown
        """ starting(self) """
        pass

    def do_wrote_body(self, *args, **kwargs): # real signature unknown
        """ wrote_body(self) """
        pass

    def do_wrote_chunk(self, *args, **kwargs): # real signature unknown
        """ wrote_chunk(self) """
        pass

    def do_wrote_headers(self, *args, **kwargs): # real signature unknown
        """ wrote_headers(self) """
        pass

    def do_wrote_informational(self, *args, **kwargs): # real signature unknown
        """ wrote_informational(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) """
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

    def get_address(self): # real signature unknown; restored from __doc__
        """ get_address(self) -> Soup.Address """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_first_party(self): # real signature unknown; restored from __doc__
        """ get_first_party(self) -> Soup.URI """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Soup.MessageFlags """
        pass

    def get_https_status(self): # real signature unknown; restored from __doc__
        """ get_https_status(self) -> bool, certificate:Gio.TlsCertificate, errors:Gio.TlsCertificateFlags """
        return False

    def get_http_version(self): # real signature unknown; restored from __doc__
        """ get_http_version(self) -> Soup.HTTPVersion """
        pass

    def get_is_top_level_navigation(self): # real signature unknown; restored from __doc__
        """ get_is_top_level_navigation(self) -> bool """
        return False

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> Soup.MessagePriority """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_site_for_cookies(self): # real signature unknown; restored from __doc__
        """ get_site_for_cookies(self) -> Soup.URI """
        pass

    def get_soup_request(self): # real signature unknown; restored from __doc__
        """ get_soup_request(self) -> Soup.Request """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> Soup.URI """
        pass

    def got_body(self): # real signature unknown; restored from __doc__
        """ got_body(self) """
        pass

    def got_chunk(self, chunk): # real signature unknown; restored from __doc__
        """ got_chunk(self, chunk:Soup.Buffer) """
        pass

    def got_headers(self): # real signature unknown; restored from __doc__
        """ got_headers(self) """
        pass

    def got_informational(self): # real signature unknown; restored from __doc__
        """ got_informational(self) """
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

    def is_keepalive(self): # real signature unknown; restored from __doc__
        """ is_keepalive(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, method, uri_string): # real signature unknown; restored from __doc__
        """ new(method:str, uri_string:str) -> Soup.Message or None """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_uri(self, method, uri): # real signature unknown; restored from __doc__
        """ new_from_uri(method:str, uri:Soup.URI) -> Soup.Message """
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

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def restarted(self): # real signature unknown; restored from __doc__
        """ restarted(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_chunk_allocator(self, allocator, user_data=None): # real signature unknown; restored from __doc__
        """ set_chunk_allocator(self, allocator:Soup.ChunkAllocator, user_data=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_first_party(self, first_party): # real signature unknown; restored from __doc__
        """ set_first_party(self, first_party:Soup.URI) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Soup.MessageFlags) """
        pass

    def set_http_version(self, version): # real signature unknown; restored from __doc__
        """ set_http_version(self, version:Soup.HTTPVersion) """
        pass

    def set_is_top_level_navigation(self, is_top_level_navigation): # real signature unknown; restored from __doc__
        """ set_is_top_level_navigation(self, is_top_level_navigation:bool) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:Soup.MessagePriority) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_redirect(self, status_code, redirect_uri): # real signature unknown; restored from __doc__
        """ set_redirect(self, status_code:int, redirect_uri:str) """
        pass

    def set_request(self, content_type=None, req_use, req_body=None): # real signature unknown; restored from __doc__
        """ set_request(self, content_type:str=None, req_use:Soup.MemoryUse, req_body:list=None) """
        pass

    def set_response(self, content_type=None, resp_use, resp_body=None): # real signature unknown; restored from __doc__
        """ set_response(self, content_type:str=None, resp_use:Soup.MemoryUse, resp_body:list=None) """
        pass

    def set_site_for_cookies(self, site_for_cookies=None): # real signature unknown; restored from __doc__
        """ set_site_for_cookies(self, site_for_cookies:Soup.URI=None) """
        pass

    def set_status(self, status_code): # real signature unknown; restored from __doc__
        """ set_status(self, status_code:int) """
        pass

    def set_status_full(self, status_code, reason_phrase): # real signature unknown; restored from __doc__
        """ set_status_full(self, status_code:int, reason_phrase:str) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:Soup.URI) """
        pass

    def starting(self): # real signature unknown; restored from __doc__
        """ starting(self) """
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

    def wrote_body(self): # real signature unknown; restored from __doc__
        """ wrote_body(self) """
        pass

    def wrote_body_data(self, chunk): # real signature unknown; restored from __doc__
        """ wrote_body_data(self, chunk:Soup.Buffer) """
        pass

    def wrote_chunk(self): # real signature unknown; restored from __doc__
        """ wrote_chunk(self) """
        pass

    def wrote_headers(self): # real signature unknown; restored from __doc__
        """ wrote_headers(self) """
        pass

    def wrote_informational(self): # real signature unknown; restored from __doc__
        """ wrote_informational(self) """
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

    method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reason_phrase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    request_body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    request_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    response_body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    response_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f8e47db9d90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Message), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupMessage (94750594803168)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_uri': gi.FunctionInfo(new_from_uri), 'content_sniffed': gi.FunctionInfo(content_sniffed), 'disable_feature': gi.FunctionInfo(disable_feature), 'finished': gi.FunctionInfo(finished), 'get_address': gi.FunctionInfo(get_address), 'get_first_party': gi.FunctionInfo(get_first_party), 'get_flags': gi.FunctionInfo(get_flags), 'get_http_version': gi.FunctionInfo(get_http_version), 'get_https_status': gi.FunctionInfo(get_https_status), 'get_is_top_level_navigation': gi.FunctionInfo(get_is_top_level_navigation), 'get_priority': gi.FunctionInfo(get_priority), 'get_site_for_cookies': gi.FunctionInfo(get_site_for_cookies), 'get_soup_request': gi.FunctionInfo(get_soup_request), 'get_uri': gi.FunctionInfo(get_uri), 'got_body': gi.FunctionInfo(got_body), 'got_chunk': gi.FunctionInfo(got_chunk), 'got_headers': gi.FunctionInfo(got_headers), 'got_informational': gi.FunctionInfo(got_informational), 'is_keepalive': gi.FunctionInfo(is_keepalive), 'restarted': gi.FunctionInfo(restarted), 'set_chunk_allocator': gi.FunctionInfo(set_chunk_allocator), 'set_first_party': gi.FunctionInfo(set_first_party), 'set_flags': gi.FunctionInfo(set_flags), 'set_http_version': gi.FunctionInfo(set_http_version), 'set_is_top_level_navigation': gi.FunctionInfo(set_is_top_level_navigation), 'set_priority': gi.FunctionInfo(set_priority), 'set_redirect': gi.FunctionInfo(set_redirect), 'set_request': gi.FunctionInfo(set_request), 'set_response': gi.FunctionInfo(set_response), 'set_site_for_cookies': gi.FunctionInfo(set_site_for_cookies), 'set_status': gi.FunctionInfo(set_status), 'set_status_full': gi.FunctionInfo(set_status_full), 'set_uri': gi.FunctionInfo(set_uri), 'starting': gi.FunctionInfo(starting), 'wrote_body': gi.FunctionInfo(wrote_body), 'wrote_body_data': gi.FunctionInfo(wrote_body_data), 'wrote_chunk': gi.FunctionInfo(wrote_chunk), 'wrote_headers': gi.FunctionInfo(wrote_headers), 'wrote_informational': gi.FunctionInfo(wrote_informational), 'do_finished': gi.VFuncInfo(finished), 'do_got_body': gi.VFuncInfo(got_body), 'do_got_chunk': gi.VFuncInfo(got_chunk), 'do_got_headers': gi.VFuncInfo(got_headers), 'do_got_informational': gi.VFuncInfo(got_informational), 'do_restarted': gi.VFuncInfo(restarted), 'do_starting': gi.VFuncInfo(starting), 'do_wrote_body': gi.VFuncInfo(wrote_body), 'do_wrote_chunk': gi.VFuncInfo(wrote_chunk), 'do_wrote_headers': gi.VFuncInfo(wrote_headers), 'do_wrote_informational': gi.VFuncInfo(wrote_informational), 'parent': <property object at 0x7f8e47edeef0>, 'method': <property object at 0x7f8e47ee1090>, 'status_code': <property object at 0x7f8e47ee1180>, 'reason_phrase': <property object at 0x7f8e47ee1270>, 'request_body': <property object at 0x7f8e47ee1360>, 'request_headers': <property object at 0x7f8e47ee1450>, 'response_body': <property object at 0x7f8e47ee1540>, 'response_headers': <property object at 0x7f8e47ee1680>})"
    __gdoc__ = "Object SoupMessage\n\nSignals from SoupMessage:\n  wrote-informational ()\n  wrote-headers ()\n  wrote-chunk ()\n  wrote-body-data (SoupBuffer)\n  wrote-body ()\n  got-informational ()\n  got-headers ()\n  got-chunk (SoupBuffer)\n  got-body ()\n  content-sniffed (gchararray, GHashTable)\n  starting ()\n  restarted ()\n  finished ()\n  network-event (GSocketClientEvent, GIOStream)\n\nProperties from SoupMessage:\n  method -> gchararray: Method\n    The message's HTTP method\n  uri -> SoupURI: URI\n    The message's Request-URI\n  http-version -> SoupHTTPVersion: HTTP Version\n    The HTTP protocol version to use\n  flags -> SoupMessageFlags: Flags\n    Various message options\n  server-side -> gboolean: Server-side\n    Whether or not the message is server-side rather than client-side\n  status-code -> guint: Status code\n    The HTTP response status code\n  reason-phrase -> gchararray: Reason phrase\n    The HTTP response reason phrase\n  first-party -> SoupURI: First party\n    The URI loaded in the application when the message was requested.\n  request-body -> SoupMessageBody: Request Body\n    The HTTP request content\n  request-body-data -> GBytes: Request Body Data\n    The HTTP request body\n  request-headers -> SoupMessageHeaders: Request Headers\n    The HTTP request headers\n  response-body -> SoupMessageBody: Response Body\n    The HTTP response content\n  response-body-data -> GBytes: Response Body Data\n    The HTTP response body\n  response-headers -> SoupMessageHeaders: Response Headers\n    The HTTP response headers\n  tls-certificate -> GTlsCertificate: TLS Certificate\n    The TLS certificate associated with the message\n  tls-errors -> GTlsCertificateFlags: TLS Errors\n    The verification errors on the message's TLS certificate\n  priority -> SoupMessagePriority: Priority\n    The priority of the message\n  site-for-cookies -> SoupURI: Site for cookies\n    The URI for the site to compare cookies against\n  is-top-level-navigation -> gboolean: Is top-level navigation\n    If the current messsage is navigating between top-levels\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType SoupMessage (94750594803168)>'
    __info__ = ObjectInfo(Message)


