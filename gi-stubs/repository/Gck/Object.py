# encoding: utf-8
# module gi.repository.Gck
# from /usr/lib64/girepository-1.0/Gck-1.typelib
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


class Object(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Object(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cache_lookup(self, attr_types, cancellable=None): # real signature unknown; restored from __doc__
        """ cache_lookup(self, attr_types:list, cancellable:Gio.Cancellable=None) -> Gck.Attributes """
        pass

    def cache_lookup_async(self, attr_types, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ cache_lookup_async(self, attr_types:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def cache_lookup_finish(self, result): # real signature unknown; restored from __doc__
        """ cache_lookup_finish(self, result:Gio.AsyncResult) -> Gck.Attributes """
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

    def destroy(self, cancellable=None): # real signature unknown; restored from __doc__
        """ destroy(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def destroy_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ destroy_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def destroy_finish(self, result): # real signature unknown; restored from __doc__
        """ destroy_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def equal(self, object2): # real signature unknown; restored from __doc__
        """ equal(self, object2:Gck.Object) -> bool """
        return False

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

    def from_handle(self, session, object_handle): # real signature unknown; restored from __doc__
        """ from_handle(session:Gck.Session, object_handle:int) -> Gck.Object """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_async(self, attr_types, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_async(self, attr_types:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_data(self, attr_type, cancellable=None): # real signature unknown; restored from __doc__
        """ get_data(self, attr_type:int, cancellable:Gio.Cancellable=None) -> list, n_data:int """
        return []

    def get_data_async(self, attr_type, allocator, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_data_async(self, attr_type:int, allocator:Gck.Allocator, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_data_finish(self, result): # real signature unknown; restored from __doc__
        """ get_data_finish(self, result:Gio.AsyncResult) -> list, n_data:int """
        return []

    def get_finish(self, result): # real signature unknown; restored from __doc__
        """ get_finish(self, result:Gio.AsyncResult) -> Gck.Attributes """
        pass

    def get_full(self, attr_types, cancellable=None): # real signature unknown; restored from __doc__
        """ get_full(self, attr_types:list, cancellable:Gio.Cancellable=None) -> Gck.Attributes """
        pass

    def get_handle(self): # real signature unknown; restored from __doc__
        """ get_handle(self) -> int """
        return 0

    def get_module(self): # real signature unknown; restored from __doc__
        """ get_module(self) -> Gck.Module """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_session(self): # real signature unknown; restored from __doc__
        """ get_session(self) -> Gck.Session """
        pass

    def get_template(self, attr_type, cancellable=None): # real signature unknown; restored from __doc__
        """ get_template(self, attr_type:int, cancellable:Gio.Cancellable=None) -> Gck.Attributes """
        pass

    def get_template_async(self, attr_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_template_async(self, attr_type:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_template_finish(self, result): # real signature unknown; restored from __doc__
        """ get_template_finish(self, result:Gio.AsyncResult) -> Gck.Attributes """
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

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
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

    def set(self, attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ set(self, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_async(self, attrs, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_async(self, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_finish(self, result): # real signature unknown; restored from __doc__
        """ set_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_template(self, attr_type, attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ set_template(self, attr_type:int, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_template_async(self, attr_type, attrs, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_template_async(self, attr_type:int, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_template_finish(self, result): # real signature unknown; restored from __doc__
        """ set_template_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    pv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc2e5f4b2e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Object), '__module__': 'gi.repository.Gck', '__gtype__': <GType GckObject (94702127729408)>, '__doc__': None, '__gsignals__': {}, 'from_handle': gi.FunctionInfo(from_handle), 'cache_lookup': gi.FunctionInfo(cache_lookup), 'cache_lookup_async': gi.FunctionInfo(cache_lookup_async), 'cache_lookup_finish': gi.FunctionInfo(cache_lookup_finish), 'destroy': gi.FunctionInfo(destroy), 'destroy_async': gi.FunctionInfo(destroy_async), 'destroy_finish': gi.FunctionInfo(destroy_finish), 'equal': gi.FunctionInfo(equal), 'get_async': gi.FunctionInfo(get_async), 'get_data': gi.FunctionInfo(get_data), 'get_data_async': gi.FunctionInfo(get_data_async), 'get_data_finish': gi.FunctionInfo(get_data_finish), 'get_finish': gi.FunctionInfo(get_finish), 'get_full': gi.FunctionInfo(get_full), 'get_handle': gi.FunctionInfo(get_handle), 'get_module': gi.FunctionInfo(get_module), 'get_session': gi.FunctionInfo(get_session), 'get_template': gi.FunctionInfo(get_template), 'get_template_async': gi.FunctionInfo(get_template_async), 'get_template_finish': gi.FunctionInfo(get_template_finish), 'hash': gi.FunctionInfo(hash), 'set': gi.FunctionInfo(set), 'set_async': gi.FunctionInfo(set_async), 'set_finish': gi.FunctionInfo(set_finish), 'set_template': gi.FunctionInfo(set_template), 'set_template_async': gi.FunctionInfo(set_template_async), 'set_template_finish': gi.FunctionInfo(set_template_finish), 'parent': <property object at 0x7fc2e614a360>, 'pv': <property object at 0x7fc2e614a450>, 'reserved': <property object at 0x7fc2e614a540>})"
    __gdoc__ = 'Object GckObject\n\nProperties from GckObject:\n  module -> GckModule: Module\n    PKCS11 Module\n  session -> GckSession: session\n    PKCS11 Session to make calls on\n  handle -> gulong: Object Handle\n    PKCS11 Object Handle\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GckObject (94702127729408)>'
    __info__ = ObjectInfo(Object)


