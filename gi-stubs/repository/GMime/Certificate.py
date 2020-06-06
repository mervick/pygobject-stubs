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


class Certificate(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Certificate(**properties)
        new() -> GMime.Certificate
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

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> int """
        return 0

    def get_created64(self): # real signature unknown; restored from __doc__
        """ get_created64(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_digest_algo(self): # real signature unknown; restored from __doc__
        """ get_digest_algo(self) -> GMime.DigestAlgo """
        pass

    def get_email(self): # real signature unknown; restored from __doc__
        """ get_email(self) -> str """
        return ""

    def get_expires(self): # real signature unknown; restored from __doc__
        """ get_expires(self) -> int """
        return 0

    def get_expires64(self): # real signature unknown; restored from __doc__
        """ get_expires64(self) -> int """
        return 0

    def get_fingerprint(self): # real signature unknown; restored from __doc__
        """ get_fingerprint(self) -> str """
        return ""

    def get_id_validity(self): # real signature unknown; restored from __doc__
        """ get_id_validity(self) -> GMime.Validity """
        pass

    def get_issuer_name(self): # real signature unknown; restored from __doc__
        """ get_issuer_name(self) -> str """
        return ""

    def get_issuer_serial(self): # real signature unknown; restored from __doc__
        """ get_issuer_serial(self) -> str """
        return ""

    def get_key_id(self): # real signature unknown; restored from __doc__
        """ get_key_id(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_pubkey_algo(self): # real signature unknown; restored from __doc__
        """ get_pubkey_algo(self) -> GMime.PubKeyAlgo """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_trust(self): # real signature unknown; restored from __doc__
        """ get_trust(self) -> GMime.Trust """
        pass

    def get_user_id(self): # real signature unknown; restored from __doc__
        """ get_user_id(self) -> str """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GMime.Certificate """
        pass

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

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def set_created(self, created): # real signature unknown; restored from __doc__
        """ set_created(self, created:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_digest_algo(self, algo): # real signature unknown; restored from __doc__
        """ set_digest_algo(self, algo:GMime.DigestAlgo) """
        pass

    def set_email(self, email): # real signature unknown; restored from __doc__
        """ set_email(self, email:str) """
        pass

    def set_expires(self, expires): # real signature unknown; restored from __doc__
        """ set_expires(self, expires:int) """
        pass

    def set_fingerprint(self, fingerprint): # real signature unknown; restored from __doc__
        """ set_fingerprint(self, fingerprint:str) """
        pass

    def set_id_validity(self, validity): # real signature unknown; restored from __doc__
        """ set_id_validity(self, validity:GMime.Validity) """
        pass

    def set_issuer_name(self, issuer_name): # real signature unknown; restored from __doc__
        """ set_issuer_name(self, issuer_name:str) """
        pass

    def set_issuer_serial(self, issuer_serial): # real signature unknown; restored from __doc__
        """ set_issuer_serial(self, issuer_serial:str) """
        pass

    def set_key_id(self, key_id): # real signature unknown; restored from __doc__
        """ set_key_id(self, key_id:str) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_pubkey_algo(self, algo): # real signature unknown; restored from __doc__
        """ set_pubkey_algo(self, algo:GMime.PubKeyAlgo) """
        pass

    def set_trust(self, trust): # real signature unknown; restored from __doc__
        """ set_trust(self, trust:GMime.Trust) """
        pass

    def set_user_id(self, user_id): # real signature unknown; restored from __doc__
        """ set_user_id(self, user_id:str) """
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

    created = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_algo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fingerprint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id_validity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    issuer_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    issuer_serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pubkey_algo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trust = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc9708b5670>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Certificate), '__module__': 'gi.repository.GMime', '__gtype__': <GType GMimeCertificate (94235495744320)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_created': gi.FunctionInfo(get_created), 'get_created64': gi.FunctionInfo(get_created64), 'get_digest_algo': gi.FunctionInfo(get_digest_algo), 'get_email': gi.FunctionInfo(get_email), 'get_expires': gi.FunctionInfo(get_expires), 'get_expires64': gi.FunctionInfo(get_expires64), 'get_fingerprint': gi.FunctionInfo(get_fingerprint), 'get_id_validity': gi.FunctionInfo(get_id_validity), 'get_issuer_name': gi.FunctionInfo(get_issuer_name), 'get_issuer_serial': gi.FunctionInfo(get_issuer_serial), 'get_key_id': gi.FunctionInfo(get_key_id), 'get_name': gi.FunctionInfo(get_name), 'get_pubkey_algo': gi.FunctionInfo(get_pubkey_algo), 'get_trust': gi.FunctionInfo(get_trust), 'get_user_id': gi.FunctionInfo(get_user_id), 'set_created': gi.FunctionInfo(set_created), 'set_digest_algo': gi.FunctionInfo(set_digest_algo), 'set_email': gi.FunctionInfo(set_email), 'set_expires': gi.FunctionInfo(set_expires), 'set_fingerprint': gi.FunctionInfo(set_fingerprint), 'set_id_validity': gi.FunctionInfo(set_id_validity), 'set_issuer_name': gi.FunctionInfo(set_issuer_name), 'set_issuer_serial': gi.FunctionInfo(set_issuer_serial), 'set_key_id': gi.FunctionInfo(set_key_id), 'set_name': gi.FunctionInfo(set_name), 'set_pubkey_algo': gi.FunctionInfo(set_pubkey_algo), 'set_trust': gi.FunctionInfo(set_trust), 'set_user_id': gi.FunctionInfo(set_user_id), 'parent_object': <property object at 0x7fc9708c71d0>, 'pubkey_algo': <property object at 0x7fc9708c72c0>, 'digest_algo': <property object at 0x7fc9708c73b0>, 'trust': <property object at 0x7fc9708c74a0>, 'issuer_serial': <property object at 0x7fc9708c7590>, 'issuer_name': <property object at 0x7fc9708c7680>, 'fingerprint': <property object at 0x7fc9708c7770>, 'created': <property object at 0x7fc9708c7860>, 'expires': <property object at 0x7fc9708c7950>, 'keyid': <property object at 0x7fc9708c7a40>, 'email': <property object at 0x7fc9708c7b30>, 'name': <property object at 0x7fc9708c7c20>, 'user_id': <property object at 0x7fc9708c7d10>, 'id_validity': <property object at 0x7fc9708c7e00>})"
    __gdoc__ = 'Object GMimeCertificate\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GMimeCertificate (94235495744320)>'
    __info__ = ObjectInfo(Certificate)


