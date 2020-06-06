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


from .Part import Part

class ApplicationPkcs7Mime(Part):
    """
    :Constructors:
    
    ::
    
        ApplicationPkcs7Mime(**properties)
        new(type:GMime.SecureMimeType) -> GMime.ApplicationPkcs7Mime
    """
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

    def decrypt(self, flags, session_key, result): # real signature unknown; restored from __doc__
        """ decrypt(self, flags:GMime.DecryptFlags, session_key:str, result:GMime.DecryptResult) -> GMime.Object or None """
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

    def do_set_content(self, *args, **kwargs): # real signature unknown
        """ set_content(self, content:GMime.DataWrapper) """
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

    def encrypt(self, entity, flags, recipients): # real signature unknown; restored from __doc__
        """ encrypt(entity:GMime.Object, flags:GMime.EncryptFlags, recipients:list) -> GMime.ApplicationPkcs7Mime or None """
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

    def get_best_content_encoding(self, constraint): # real signature unknown; restored from __doc__
        """ get_best_content_encoding(self, constraint:GMime.EncodingConstraint) -> GMime.ContentEncoding """
        pass

    def get_content(self): # real signature unknown; restored from __doc__
        """ get_content(self) -> GMime.DataWrapper """
        pass

    def get_content_description(self): # real signature unknown; restored from __doc__
        """ get_content_description(self) -> str """
        return ""

    def get_content_disposition(self): # real signature unknown; restored from __doc__
        """ get_content_disposition(self) -> GMime.ContentDisposition """
        pass

    def get_content_disposition_parameter(self, name): # real signature unknown; restored from __doc__
        """ get_content_disposition_parameter(self, name:str) -> str """
        return ""

    def get_content_encoding(self): # real signature unknown; restored from __doc__
        """ get_content_encoding(self) -> GMime.ContentEncoding """
        pass

    def get_content_id(self): # real signature unknown; restored from __doc__
        """ get_content_id(self) -> str """
        return ""

    def get_content_location(self): # real signature unknown; restored from __doc__
        """ get_content_location(self) -> str """
        return ""

    def get_content_md5(self): # real signature unknown; restored from __doc__
        """ get_content_md5(self) -> str """
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

    def get_disposition(self): # real signature unknown; restored from __doc__
        """ get_disposition(self) -> str """
        return ""

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_header(self, header): # real signature unknown; restored from __doc__
        """ get_header(self, header:str) -> str """
        return ""

    def get_headers(self, options=None): # real signature unknown; restored from __doc__
        """ get_headers(self, options:GMime.FormatOptions=None) -> str """
        return ""

    def get_header_list(self): # real signature unknown; restored from __doc__
        """ get_header_list(self) -> GMime.HeaderList """
        pass

    def get_openpgp_data(self): # real signature unknown; restored from __doc__
        """ get_openpgp_data(self) -> GMime.OpenPGPData """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_smime_type(self): # real signature unknown; restored from __doc__
        """ get_smime_type(self) -> GMime.SecureMimeType """
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

    def is_attachment(self): # real signature unknown; restored from __doc__
        """ is_attachment(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, type): # real signature unknown; restored from __doc__
        """ new(type:GMime.SecureMimeType) -> GMime.ApplicationPkcs7Mime """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_type(self, options=None, type, subtype): # real signature unknown; restored from __doc__
        """ new_type(options:GMime.ParserOptions=None, type:str, subtype:str) -> GMime.Object """
        pass

    def new_with_type(self, type, subtype): # real signature unknown; restored from __doc__
        """ new_with_type(type:str, subtype:str) -> GMime.Part """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def openpgp_decrypt(self, flags, session_key=None): # real signature unknown; restored from __doc__
        """ openpgp_decrypt(self, flags:GMime.DecryptFlags, session_key:str=None) -> GMime.DecryptResult or None """
        pass

    def openpgp_encrypt(self, sign, userid=None, flags, recipients): # real signature unknown; restored from __doc__
        """ openpgp_encrypt(self, sign:bool, userid:str=None, flags:GMime.EncryptFlags, recipients:list) -> bool """
        return False

    def openpgp_sign(self, userid): # real signature unknown; restored from __doc__
        """ openpgp_sign(self, userid:str) -> bool """
        return False

    def openpgp_verify(self, flags): # real signature unknown; restored from __doc__
        """ openpgp_verify(self, flags:GMime.VerifyFlags) -> GMime.SignatureList or None """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
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

    def set_content(self, content): # real signature unknown; restored from __doc__
        """ set_content(self, content:GMime.DataWrapper) """
        pass

    def set_content_description(self, description): # real signature unknown; restored from __doc__
        """ set_content_description(self, description:str) """
        pass

    def set_content_disposition(self, disposition): # real signature unknown; restored from __doc__
        """ set_content_disposition(self, disposition:GMime.ContentDisposition) """
        pass

    def set_content_disposition_parameter(self, name, value): # real signature unknown; restored from __doc__
        """ set_content_disposition_parameter(self, name:str, value:str) """
        pass

    def set_content_encoding(self, encoding): # real signature unknown; restored from __doc__
        """ set_content_encoding(self, encoding:GMime.ContentEncoding) """
        pass

    def set_content_id(self, content_id): # real signature unknown; restored from __doc__
        """ set_content_id(self, content_id:str) """
        pass

    def set_content_location(self, content_location): # real signature unknown; restored from __doc__
        """ set_content_location(self, content_location:str) """
        pass

    def set_content_md5(self, content_md5): # real signature unknown; restored from __doc__
        """ set_content_md5(self, content_md5:str) """
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

    def set_disposition(self, disposition): # real signature unknown; restored from __doc__
        """ set_disposition(self, disposition:str) """
        pass

    def set_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_filename(self, filename:str) """
        pass

    def set_header(self, header, value, charset): # real signature unknown; restored from __doc__
        """ set_header(self, header:str, value:str, charset:str) """
        pass

    def set_openpgp_data(self, data): # real signature unknown; restored from __doc__
        """ set_openpgp_data(self, data:GMime.OpenPGPData) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def sign(self, entity, userid): # real signature unknown; restored from __doc__
        """ sign(entity:GMime.Object, userid:str) -> GMime.ApplicationPkcs7Mime or None """
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

    def verify(self, flags): # real signature unknown; restored from __doc__
        """ verify(self, flags:GMime.VerifyFlags) -> GMime.SignatureList or None, entity:GMime.Object """
        pass

    def verify_content_md5(self): # real signature unknown; restored from __doc__
        """ verify_content_md5(self) -> bool """
        return False

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

    content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_md5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disposition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ensure_newline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    openpgp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    smime_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc9706e6d60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ApplicationPkcs7Mime), '__module__': 'gi.repository.GMime', '__gtype__': <GType GMimeApplicationPkcs7Mime (94235495552144)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'encrypt': gi.FunctionInfo(encrypt), 'sign': gi.FunctionInfo(sign), 'decrypt': gi.FunctionInfo(decrypt), 'get_smime_type': gi.FunctionInfo(get_smime_type), 'verify': gi.FunctionInfo(verify), 'parent_object': <property object at 0x7fc9708bdd10>, 'smime_type': <property object at 0x7fc9708bde00>})"
    __gdoc__ = 'Object GMimeApplicationPkcs7Mime\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GMimeApplicationPkcs7Mime (94235495552144)>'
    __info__ = ObjectInfo(ApplicationPkcs7Mime)


