# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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
import gobject as __gobject


from .Object import Object

class Message(Object):
    """
    :Constructors:
    
    ::
    
        Message(**properties)
        new(pretty_headers:bool) -> GMime.Message
    """
    def add_mailbox(self, type, name, addr): # real signature unknown; restored from __doc__
        """ add_mailbox(self, type:GMime.AddressType, name:str, addr:str) """
        pass

    def append_header(self, header, value, charset): # real signature unknown; restored from __doc__
        """ append_header(self, header:str, value:str, charset:str) """
        pass

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

    def do_encode(self, *args, **kwargs): # real signature unknown
        """ encode(self, constraint:GMime.EncodingConstraint) """
        pass

    def do_get_headers(self, *args, **kwargs): # real signature unknown
        """ get_headers(self, options:GMime.FormatOptions=None) -> str """
        pass

    def do_headers_cleared(self, *args, **kwargs): # real signature unknown
        """ headers_cleared(self) """
        pass

    def do_header_added(self, *args, **kwargs): # real signature unknown
        """ header_added(self, header:GMime.Header) """
        pass

    def do_header_changed(self, *args, **kwargs): # real signature unknown
        """ header_changed(self, header:GMime.Header) """
        pass

    def do_header_removed(self, *args, **kwargs): # real signature unknown
        """ header_removed(self, header:GMime.Header) """
        pass

    def do_set_content_type(self, *args, **kwargs): # real signature unknown
        """ set_content_type(self, content_type:GMime.ContentType) """
        pass

    def do_write_to_stream(self, *args, **kwargs): # real signature unknown
        """ write_to_stream(self, options:GMime.FormatOptions, content_only:bool, stream:GMime.Stream) -> int """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def encode(self, constraint): # real signature unknown; restored from __doc__
        """ encode(self, constraint:GMime.EncodingConstraint) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, callback:GMime.ObjectForeachFunc, user_data=None) """
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

    def get_addresses(self, type): # real signature unknown; restored from __doc__
        """ get_addresses(self, type:GMime.AddressType) -> GMime.InternetAddressList """
        pass

    def get_all_recipients(self): # real signature unknown; restored from __doc__
        """ get_all_recipients(self) -> GMime.InternetAddressList """
        pass

    def get_autocrypt_gossip_headers(self, now, flags, session_key): # real signature unknown; restored from __doc__
        """ get_autocrypt_gossip_headers(self, now:GLib.DateTime, flags:GMime.DecryptFlags, session_key:str) -> GMime.AutocryptHeaderList """
        pass

    def get_autocrypt_gossip_headers_from_inner_part(self, now, inner_part): # real signature unknown; restored from __doc__
        """ get_autocrypt_gossip_headers_from_inner_part(self, now:GLib.DateTime, inner_part:GMime.Object) -> GMime.AutocryptHeaderList """
        pass

    def get_autocrypt_header(self, now): # real signature unknown; restored from __doc__
        """ get_autocrypt_header(self, now:GLib.DateTime) -> GMime.AutocryptHeader """
        pass

    def get_bcc(self): # real signature unknown; restored from __doc__
        """ get_bcc(self) -> GMime.InternetAddressList """
        pass

    def get_body(self): # real signature unknown; restored from __doc__
        """ get_body(self) -> GMime.Object """
        pass

    def get_cc(self): # real signature unknown; restored from __doc__
        """ get_cc(self) -> GMime.InternetAddressList """
        pass

    def get_content_disposition(self): # real signature unknown; restored from __doc__
        """ get_content_disposition(self) -> GMime.ContentDisposition """
        pass

    def get_content_disposition_parameter(self, name): # real signature unknown; restored from __doc__
        """ get_content_disposition_parameter(self, name:str) -> str """
        return ""

    def get_content_id(self): # real signature unknown; restored from __doc__
        """ get_content_id(self) -> str """
        return ""

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> GMime.ContentType """
        pass

    def get_content_type_parameter(self, name): # real signature unknown; restored from __doc__
        """ get_content_type_parameter(self, name:str) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date(self): # real signature unknown; restored from __doc__
        """ get_date(self) -> GLib.DateTime """
        pass

    def get_disposition(self): # real signature unknown; restored from __doc__
        """ get_disposition(self) -> str """
        return ""

    def get_from(self): # real signature unknown; restored from __doc__
        """ get_from(self) -> GMime.InternetAddressList """
        pass

    def get_header(self, header): # real signature unknown; restored from __doc__
        """ get_header(self, header:str) -> str """
        return ""

    def get_headers(self, options=None): # real signature unknown; restored from __doc__
        """ get_headers(self, options:GMime.FormatOptions=None) -> str """
        return ""

    def get_header_list(self): # real signature unknown; restored from __doc__
        """ get_header_list(self) -> GMime.HeaderList """
        pass

    def get_message_id(self): # real signature unknown; restored from __doc__
        """ get_message_id(self) -> str """
        return ""

    def get_mime_part(self): # real signature unknown; restored from __doc__
        """ get_mime_part(self) -> GMime.Object """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_reply_to(self): # real signature unknown; restored from __doc__
        """ get_reply_to(self) -> GMime.InternetAddressList """
        pass

    def get_sender(self): # real signature unknown; restored from __doc__
        """ get_sender(self) -> GMime.InternetAddressList """
        pass

    def get_subject(self): # real signature unknown; restored from __doc__
        """ get_subject(self) -> str """
        return ""

    def get_to(self): # real signature unknown; restored from __doc__
        """ get_to(self) -> GMime.InternetAddressList """
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

    def new(self, pretty_headers): # real signature unknown; restored from __doc__
        """ new(pretty_headers:bool) -> GMime.Message """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_type(self, options=None, type, subtype): # real signature unknown; restored from __doc__
        """ new_type(options:GMime.ParserOptions=None, type:str, subtype:str) -> GMime.Object """
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

    def partial_split_message(self, max_size): # real signature unknown; restored from __doc__
        """ partial_split_message(self, max_size:int) -> GMime.Message or None, nparts:int """
        pass

    def prepend_header(self, header, value, charset): # real signature unknown; restored from __doc__
        """ prepend_header(self, header:str, value:str, charset:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register_type(self, type, subtype, object_type): # real signature unknown; restored from __doc__
        """ register_type(type:str, subtype:str, object_type:GType) """
        pass

    def remove_header(self, header): # real signature unknown; restored from __doc__
        """ remove_header(self, header:str) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_content_disposition(self, disposition): # real signature unknown; restored from __doc__
        """ set_content_disposition(self, disposition:GMime.ContentDisposition) """
        pass

    def set_content_disposition_parameter(self, name, value): # real signature unknown; restored from __doc__
        """ set_content_disposition_parameter(self, name:str, value:str) """
        pass

    def set_content_id(self, content_id): # real signature unknown; restored from __doc__
        """ set_content_id(self, content_id:str) """
        pass

    def set_content_type(self, content_type): # real signature unknown; restored from __doc__
        """ set_content_type(self, content_type:GMime.ContentType) """
        pass

    def set_content_type_parameter(self, name, value): # real signature unknown; restored from __doc__
        """ set_content_type_parameter(self, name:str, value:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date(self, date): # real signature unknown; restored from __doc__
        """ set_date(self, date:GLib.DateTime) """
        pass

    def set_disposition(self, disposition): # real signature unknown; restored from __doc__
        """ set_disposition(self, disposition:str) """
        pass

    def set_header(self, header, value, charset): # real signature unknown; restored from __doc__
        """ set_header(self, header:str, value:str, charset:str) """
        pass

    def set_message_id(self, message_id): # real signature unknown; restored from __doc__
        """ set_message_id(self, message_id:str) """
        pass

    def set_mime_part(self, mime_part): # real signature unknown; restored from __doc__
        """ set_mime_part(self, mime_part:GMime.Object) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_subject(self, subject, charset): # real signature unknown; restored from __doc__
        """ set_subject(self, subject:str, charset:str) """
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

    def to_string(self, options=None): # real signature unknown; restored from __doc__
        """ to_string(self, options:GMime.FormatOptions=None) -> str """
        return ""

    def type_registry_init(self): # real signature unknown; restored from __doc__
        """ type_registry_init() """
        pass

    def type_registry_shutdown(self): # real signature unknown; restored from __doc__
        """ type_registry_shutdown() """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write_to_stream(self, options=None, stream): # real signature unknown; restored from __doc__
        """ write_to_stream(self, options:GMime.FormatOptions=None, stream:GMime.Stream) -> int """
        return 0

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

    addrlists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disposition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ensure_newline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    marker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mime_part = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc97050cbe0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Message), '__module__': 'gi.repository.GMime', '__gtype__': <GType GMimeMessage (94235496107856)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_mailbox': gi.FunctionInfo(add_mailbox), 'foreach': gi.FunctionInfo(foreach), 'get_addresses': gi.FunctionInfo(get_addresses), 'get_all_recipients': gi.FunctionInfo(get_all_recipients), 'get_autocrypt_gossip_headers': gi.FunctionInfo(get_autocrypt_gossip_headers), 'get_autocrypt_gossip_headers_from_inner_part': gi.FunctionInfo(get_autocrypt_gossip_headers_from_inner_part), 'get_autocrypt_header': gi.FunctionInfo(get_autocrypt_header), 'get_bcc': gi.FunctionInfo(get_bcc), 'get_body': gi.FunctionInfo(get_body), 'get_cc': gi.FunctionInfo(get_cc), 'get_date': gi.FunctionInfo(get_date), 'get_from': gi.FunctionInfo(get_from), 'get_message_id': gi.FunctionInfo(get_message_id), 'get_mime_part': gi.FunctionInfo(get_mime_part), 'get_reply_to': gi.FunctionInfo(get_reply_to), 'get_sender': gi.FunctionInfo(get_sender), 'get_subject': gi.FunctionInfo(get_subject), 'get_to': gi.FunctionInfo(get_to), 'partial_split_message': gi.FunctionInfo(partial_split_message), 'set_date': gi.FunctionInfo(set_date), 'set_message_id': gi.FunctionInfo(set_message_id), 'set_mime_part': gi.FunctionInfo(set_mime_part), 'set_subject': gi.FunctionInfo(set_subject), 'parent_object': <property object at 0x7fc970739680>, 'addrlists': <property object at 0x7fc970739770>, 'mime_part': <property object at 0x7fc970739860>, 'message_id': <property object at 0x7fc970739950>, 'date': <property object at 0x7fc970739a40>, 'subject': <property object at 0x7fc970739b30>, 'marker': <property object at 0x7fc970739c20>})"
    __gdoc__ = 'Object GMimeMessage\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GMimeMessage (94235496107856)>'
    __info__ = ObjectInfo(Message)


