# encoding: utf-8
# module gi.repository.RygelServer
# from /usr/lib64/girepository-1.0/RygelServer-2.6.typelib
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
import gi.repository.Gee as __gi_repository_Gee
import gi.repository.GUPnP as __gi_repository_GUPnP
import gi.repository.RygelCore as __gi_repository_RygelCore
import gobject as __gobject


class MediaObject(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        MediaObject(**properties)
    """
    def add_uri(self, uri): # real signature unknown; restored from __doc__
        """ add_uri(self, uri:str) """
        pass

    def apply_replacements(self, replacement_pairs, source_string=None): # real signature unknown; restored from __doc__
        """ apply_replacements(replacement_pairs:dict, source_string:str=None) -> str """
        return ""

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compare_int_props(self, prop1, prop2): # real signature unknown; restored from __doc__
        """ compare_int_props(self, prop1:int, prop2:int) -> int """
        return 0

    def compare_string_props(self, prop1, prop2): # real signature unknown; restored from __doc__
        """ compare_string_props(self, prop1:str, prop2:str) -> int """
        return 0

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

    def create_stream_source_for_resource(self, request, resource): # real signature unknown; restored from __doc__
        """ create_stream_source_for_resource(self, request:RygelServer.HTTPRequest, resource:RygelServer.MediaResource) -> RygelServer.DataSource """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add_uri(self, *args, **kwargs): # real signature unknown
        """ add_uri(self, uri:str) """
        pass

    def do_create_stream_source_for_resource(self, *args, **kwargs): # real signature unknown
        """ create_stream_source_for_resource(self, request:RygelServer.HTTPRequest, resource:RygelServer.MediaResource) -> RygelServer.DataSource """
        pass

    def do_get_ocm_flags(self, *args, **kwargs): # real signature unknown
        """ get_ocm_flags(self) -> GUPnPAV.OCMFlags """
        pass

    def do_serialize(self, *args, **kwargs): # real signature unknown
        """ serialize(self, serializer:RygelServer.Serializer, http_server:RygelServer.HTTPServer) -> GUPnPAV.DIDLLiteObject """
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

    def get_artist(self): # real signature unknown; restored from __doc__
        """ get_artist(self) -> str """
        return ""

    def get_creator(self): # real signature unknown; restored from __doc__
        """ get_creator(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date(self): # real signature unknown; restored from __doc__
        """ get_date(self) -> str """
        return ""

    def get_genre(self): # real signature unknown; restored from __doc__
        """ get_genre(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_modified(self): # real signature unknown; restored from __doc__
        """ get_modified(self) -> int """
        return 0

    def get_object_update_id(self): # real signature unknown; restored from __doc__
        """ get_object_update_id(self) -> int """
        return 0

    def get_ocm_flags(self): # real signature unknown; restored from __doc__
        """ get_ocm_flags(self) -> GUPnPAV.OCMFlags """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> RygelServer.MediaContainer """
        pass

    def get_parent_ref(self): # real signature unknown; restored from __doc__
        """ get_parent_ref(self) -> RygelServer.MediaContainer """
        pass

    def get_primary_uri(self): # real signature unknown; restored from __doc__
        """ get_primary_uri(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_ref_id(self): # real signature unknown; restored from __doc__
        """ get_ref_id(self) -> str """
        return ""

    def get_resource_by_name(self, resource_name): # real signature unknown; restored from __doc__
        """ get_resource_by_name(self, resource_name:str) -> RygelServer.MediaResource """
        pass

    def get_resource_list(self): # real signature unknown; restored from __doc__
        """ get_resource_list(self) -> Gee.List """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_upnp_class(self): # real signature unknown; restored from __doc__
        """ get_upnp_class(self) -> str """
        return ""

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> Gee.List """
        pass

    def get_writable(self, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ get_writable(self, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def get_writables(self, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ get_writables(self, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def get_writables_finish(self, _res_): # real signature unknown; restored from __doc__
        """ get_writables_finish(self, _res_:Gio.AsyncResult) -> Gee.ArrayList """
        pass

    def get_writable_finish(self, _res_): # real signature unknown; restored from __doc__
        """ get_writable_finish(self, _res_:Gio.AsyncResult) -> Gio.File """
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

    def serialize(self, serializer, http_server): # real signature unknown; restored from __doc__
        """ serialize(self, serializer:RygelServer.Serializer, http_server:RygelServer.HTTPServer) -> GUPnPAV.DIDLLiteObject """
        pass

    def serialize_resource_list(self, didl_object, http_server): # real signature unknown; restored from __doc__
        """ serialize_resource_list(self, didl_object:GUPnPAV.DIDLLiteObject, http_server:RygelServer.HTTPServer) """
        pass

    def set_artist(self, value): # real signature unknown; restored from __doc__
        """ set_artist(self, value:str) """
        pass

    def set_creator(self, value): # real signature unknown; restored from __doc__
        """ set_creator(self, value:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date(self, value): # real signature unknown; restored from __doc__
        """ set_date(self, value:str) """
        pass

    def set_genre(self, value): # real signature unknown; restored from __doc__
        """ set_genre(self, value:str) """
        pass

    def set_id(self, value): # real signature unknown; restored from __doc__
        """ set_id(self, value:str) """
        pass

    def set_modified(self, value): # real signature unknown; restored from __doc__
        """ set_modified(self, value:int) """
        pass

    def set_object_update_id(self, value): # real signature unknown; restored from __doc__
        """ set_object_update_id(self, value:int) """
        pass

    def set_parent(self, value): # real signature unknown; restored from __doc__
        """ set_parent(self, value:RygelServer.MediaContainer) """
        pass

    def set_parent_ref(self, value): # real signature unknown; restored from __doc__
        """ set_parent_ref(self, value:RygelServer.MediaContainer) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_ref_id(self, value): # real signature unknown; restored from __doc__
        """ set_ref_id(self, value:str) """
        pass

    def set_title(self, value): # real signature unknown; restored from __doc__
        """ set_title(self, value:str) """
        pass

    def set_upnp_class(self, value): # real signature unknown; restored from __doc__
        """ set_upnp_class(self, value:str) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_ptr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fe1d16936a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MediaObject), '__module__': 'gi.repository.RygelServer', '__gtype__': <GType RygelMediaObject (94219762255904)>, '__doc__': None, '__gsignals__': {}, 'get_uris': gi.FunctionInfo(get_uris), 'get_primary_uri': gi.FunctionInfo(get_primary_uri), 'add_uri': gi.FunctionInfo(add_uri), 'get_writable': gi.FunctionInfo(get_writable), 'get_writable_finish': gi.FunctionInfo(get_writable_finish), 'get_writables': gi.FunctionInfo(get_writables), 'get_writables_finish': gi.FunctionInfo(get_writables_finish), 'get_resource_list': gi.FunctionInfo(get_resource_list), 'get_resource_by_name': gi.FunctionInfo(get_resource_by_name), 'serialize': gi.FunctionInfo(serialize), 'serialize_resource_list': gi.FunctionInfo(serialize_resource_list), 'apply_replacements': gi.FunctionInfo(apply_replacements), 'create_stream_source_for_resource': gi.FunctionInfo(create_stream_source_for_resource), 'compare_string_props': gi.FunctionInfo(compare_string_props), 'compare_int_props': gi.FunctionInfo(compare_int_props), 'get_id': gi.FunctionInfo(get_id), 'set_id': gi.FunctionInfo(set_id), 'get_ref_id': gi.FunctionInfo(get_ref_id), 'set_ref_id': gi.FunctionInfo(set_ref_id), 'get_upnp_class': gi.FunctionInfo(get_upnp_class), 'set_upnp_class': gi.FunctionInfo(set_upnp_class), 'get_date': gi.FunctionInfo(get_date), 'set_date': gi.FunctionInfo(set_date), 'get_creator': gi.FunctionInfo(get_creator), 'set_creator': gi.FunctionInfo(set_creator), 'get_modified': gi.FunctionInfo(get_modified), 'set_modified': gi.FunctionInfo(set_modified), 'get_object_update_id': gi.FunctionInfo(get_object_update_id), 'set_object_update_id': gi.FunctionInfo(set_object_update_id), 'get_artist': gi.FunctionInfo(get_artist), 'set_artist': gi.FunctionInfo(set_artist), 'get_genre': gi.FunctionInfo(get_genre), 'set_genre': gi.FunctionInfo(set_genre), 'get_parent': gi.FunctionInfo(get_parent), 'set_parent': gi.FunctionInfo(set_parent), 'get_parent_ref': gi.FunctionInfo(get_parent_ref), 'set_parent_ref': gi.FunctionInfo(set_parent_ref), 'get_title': gi.FunctionInfo(get_title), 'set_title': gi.FunctionInfo(set_title), 'get_ocm_flags': gi.FunctionInfo(get_ocm_flags), 'do_add_uri': gi.VFuncInfo(add_uri), 'do_serialize': gi.VFuncInfo(serialize), 'do_create_stream_source_for_resource': gi.VFuncInfo(create_stream_source_for_resource), 'do_get_ocm_flags': gi.VFuncInfo(get_ocm_flags), 'parent_instance': <property object at 0x7fe1d2039ef0>, 'priv': <property object at 0x7fe1d2039f40>, 'parent_ptr': <property object at 0x7fe1d2039f90>})"
    __gdoc__ = 'Object RygelMediaObject\n\nProperties from RygelMediaObject:\n  id -> gchararray: id\n    id\n  ref-id -> gchararray: ref-id\n    ref-id\n  upnp-class -> gchararray: upnp-class\n    upnp-class\n  date -> gchararray: date\n    date\n  creator -> gchararray: creator\n    creator\n  modified -> guint64: modified\n    modified\n  object-update-id -> guint: object-update-id\n    object-update-id\n  artist -> gchararray: artist\n    artist\n  genre -> gchararray: genre\n    genre\n  parent -> RygelMediaContainer: parent\n    parent\n  parent-ref -> RygelMediaContainer: parent-ref\n    parent-ref\n  title -> gchararray: title\n    title\n  ocm-flags -> GUPnPOCMFlags: ocm-flags\n    ocm-flags\n  restricted -> gboolean: restricted\n    restricted\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelMediaObject (94219762255904)>'
    __info__ = ObjectInfo(MediaObject)


