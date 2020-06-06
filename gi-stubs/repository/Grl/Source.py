# encoding: utf-8
# module gi.repository.Grl
# from /usr/lib64/girepository-1.0/Grl-0.3.typelib
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


class Source(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Source(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def browse(self, container=None, keys, options, callback, user_data=None): # real signature unknown; restored from __doc__
        """ browse(self, container:Grl.Media=None, keys:list, options:Grl.OperationOptions, callback:Grl.SourceResultCb, user_data=None) -> int """
        return 0

    def browse_sync(self, container=None, keys, options): # real signature unknown; restored from __doc__
        """ browse_sync(self, container:Grl.Media=None, keys:list, options:Grl.OperationOptions) -> list """
        return []

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

    def do_browse(self, *args, **kwargs): # real signature unknown
        """ browse(self, bs:Grl.SourceBrowseSpec) """
        pass

    def do_cancel(self, *args, **kwargs): # real signature unknown
        """ cancel(self, operation_id:int) """
        pass

    def do_get_caps(self, *args, **kwargs): # real signature unknown
        """ get_caps(self, operation:Grl.SupportedOps) -> Grl.Caps """
        pass

    def do_may_resolve(self, *args, **kwargs): # real signature unknown
        """ may_resolve(self, media:Grl.Media, key_id:int, missing_keys:list) -> bool """
        pass

    def do_media_from_uri(self, *args, **kwargs): # real signature unknown
        """ media_from_uri(self, mfus:Grl.SourceMediaFromUriSpec) """
        pass

    def do_notify_change_start(self, *args, **kwargs): # real signature unknown
        """ notify_change_start(self) -> bool """
        pass

    def do_notify_change_stop(self, *args, **kwargs): # real signature unknown
        """ notify_change_stop(self) -> bool """
        pass

    def do_query(self, *args, **kwargs): # real signature unknown
        """ query(self, qs:Grl.SourceQuerySpec) """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, rs:Grl.SourceRemoveSpec) """
        pass

    def do_resolve(self, *args, **kwargs): # real signature unknown
        """ resolve(self, ms:Grl.SourceResolveSpec) """
        pass

    def do_search(self, *args, **kwargs): # real signature unknown
        """ search(self, ss:Grl.SourceSearchSpec) """
        pass

    def do_slow_keys(self, *args, **kwargs): # real signature unknown
        """ slow_keys(self) -> list """
        pass

    def do_store(self, *args, **kwargs): # real signature unknown
        """ store(self, ss:Grl.SourceStoreSpec) """
        pass

    def do_store_metadata(self, *args, **kwargs): # real signature unknown
        """ store_metadata(self, sms:Grl.SourceStoreMetadataSpec) """
        pass

    def do_supported_keys(self, *args, **kwargs): # real signature unknown
        """ supported_keys(self) -> list """
        pass

    def do_supported_operations(self, *args, **kwargs): # real signature unknown
        """ supported_operations(self) -> Grl.SupportedOps """
        pass

    def do_test_media_from_uri(self, *args, **kwargs): # real signature unknown
        """ test_media_from_uri(self, uri:str) -> bool """
        pass

    def do_writable_keys(self, *args, **kwargs): # real signature unknown
        """ writable_keys(self) -> list """
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

    def get_auto_split_threshold(self): # real signature unknown; restored from __doc__
        """ get_auto_split_threshold(self) -> int """
        return 0

    def get_caps(self, operation): # real signature unknown; restored from __doc__
        """ get_caps(self, operation:Grl.SupportedOps) -> Grl.Caps """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_media_from_uri(self, uri, keys, options, callback, user_data=None): # real signature unknown; restored from __doc__
        """ get_media_from_uri(self, uri:str, keys:list, options:Grl.OperationOptions, callback:Grl.SourceResolveCb, user_data=None) -> int """
        return 0

    def get_media_from_uri_sync(self, uri, keys, options): # real signature unknown; restored from __doc__
        """ get_media_from_uri_sync(self, uri:str, keys:list, options:Grl.OperationOptions) -> Grl.Media """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_plugin(self): # real signature unknown; restored from __doc__
        """ get_plugin(self) -> Grl.Plugin """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rank(self): # real signature unknown; restored from __doc__
        """ get_rank(self) -> int """
        return 0

    def get_supported_media(self): # real signature unknown; restored from __doc__
        """ get_supported_media(self) -> Grl.SupportedMedia """
        pass

    def get_tags(self): # real signature unknown; restored from __doc__
        """ get_tags(self) -> list """
        return []

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

    def may_resolve(self, media, key_id, missing_keys): # real signature unknown; restored from __doc__
        """ may_resolve(self, media:Grl.Media, key_id:int, missing_keys:list) -> bool """
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

    def notify_change(self, media=None, change_type, location_unknown): # real signature unknown; restored from __doc__
        """ notify_change(self, media:Grl.Media=None, change_type:Grl.SourceChangeType, location_unknown:bool) """
        pass

    def notify_change_list(self, changed_medias, change_type, location_unknown): # real signature unknown; restored from __doc__
        """ notify_change_list(self, changed_medias:list, change_type:Grl.SourceChangeType, location_unknown:bool) """
        pass

    def notify_change_start(self): # real signature unknown; restored from __doc__
        """ notify_change_start(self) -> bool """
        return False

    def notify_change_stop(self): # real signature unknown; restored from __doc__
        """ notify_change_stop(self) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def query(self, query, keys, options, callback, user_data=None): # real signature unknown; restored from __doc__
        """ query(self, query:str, keys:list, options:Grl.OperationOptions, callback:Grl.SourceResultCb, user_data=None) -> int """
        return 0

    def query_sync(self, query, keys, options): # real signature unknown; restored from __doc__
        """ query_sync(self, query:str, keys:list, options:Grl.OperationOptions) -> list """
        return []

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self, media, callback, user_data=None): # real signature unknown; restored from __doc__
        """ remove(self, media:Grl.Media, callback:Grl.SourceRemoveCb, user_data=None) """
        pass

    def remove_sync(self, media): # real signature unknown; restored from __doc__
        """ remove_sync(self, media:Grl.Media) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def resolve(self, media=None, keys, options, callback, user_data=None): # real signature unknown; restored from __doc__
        """ resolve(self, media:Grl.Media=None, keys:list, options:Grl.OperationOptions, callback:Grl.SourceResolveCb, user_data=None) -> int """
        return 0

    def resolve_sync(self, media=None, keys, options): # real signature unknown; restored from __doc__
        """ resolve_sync(self, media:Grl.Media=None, keys:list, options:Grl.OperationOptions) -> Grl.Media """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def search(self, text, keys, options, callback, user_data=None): # real signature unknown; restored from __doc__
        """ search(self, text:str, keys:list, options:Grl.OperationOptions, callback:Grl.SourceResultCb, user_data=None) -> int """
        return 0

    def search_sync(self, text, keys, options): # real signature unknown; restored from __doc__
        """ search_sync(self, text:str, keys:list, options:Grl.OperationOptions) -> list """
        return []

    def set_auto_split_threshold(self, threshold): # real signature unknown; restored from __doc__
        """ set_auto_split_threshold(self, threshold:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def slow_keys(self): # real signature unknown; restored from __doc__
        """ slow_keys(self) -> list """
        return []

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

    def store(self, parent=None, media, flags, callback, user_data=None): # real signature unknown; restored from __doc__
        """ store(self, parent:Grl.Media=None, media:Grl.Media, flags:Grl.WriteFlags, callback:Grl.SourceStoreCb, user_data=None) """
        pass

    def store_metadata(self, media, keys=None, flags, callback, user_data=None): # real signature unknown; restored from __doc__
        """ store_metadata(self, media:Grl.Media, keys:list=None, flags:Grl.WriteFlags, callback:Grl.SourceStoreCb, user_data=None) """
        pass

    def store_metadata_sync(self, media, keys=None, flags): # real signature unknown; restored from __doc__
        """ store_metadata_sync(self, media:Grl.Media, keys:list=None, flags:Grl.WriteFlags) -> list """
        return []

    def store_sync(self, parent=None, media, flags): # real signature unknown; restored from __doc__
        """ store_sync(self, parent:Grl.Media=None, media:Grl.Media, flags:Grl.WriteFlags) """
        pass

    def supported_keys(self): # real signature unknown; restored from __doc__
        """ supported_keys(self) -> list """
        return []

    def supported_operations(self): # real signature unknown; restored from __doc__
        """ supported_operations(self) -> int """
        return 0

    def test_media_from_uri(self, uri): # real signature unknown; restored from __doc__
        """ test_media_from_uri(self, uri:str) -> bool """
        return False

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

    def writable_keys(self): # real signature unknown; restored from __doc__
        """ writable_keys(self) -> list """
        return []

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

    _grl_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa0404ce670>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Source), '__module__': 'gi.repository.Grl', '__gtype__': <GType GrlSource (94188897403200)>, '__doc__': None, '__gsignals__': {}, 'browse': gi.FunctionInfo(browse), 'browse_sync': gi.FunctionInfo(browse_sync), 'get_auto_split_threshold': gi.FunctionInfo(get_auto_split_threshold), 'get_caps': gi.FunctionInfo(get_caps), 'get_description': gi.FunctionInfo(get_description), 'get_icon': gi.FunctionInfo(get_icon), 'get_id': gi.FunctionInfo(get_id), 'get_media_from_uri': gi.FunctionInfo(get_media_from_uri), 'get_media_from_uri_sync': gi.FunctionInfo(get_media_from_uri_sync), 'get_name': gi.FunctionInfo(get_name), 'get_plugin': gi.FunctionInfo(get_plugin), 'get_rank': gi.FunctionInfo(get_rank), 'get_supported_media': gi.FunctionInfo(get_supported_media), 'get_tags': gi.FunctionInfo(get_tags), 'may_resolve': gi.FunctionInfo(may_resolve), 'notify_change': gi.FunctionInfo(notify_change), 'notify_change_list': gi.FunctionInfo(notify_change_list), 'notify_change_start': gi.FunctionInfo(notify_change_start), 'notify_change_stop': gi.FunctionInfo(notify_change_stop), 'query': gi.FunctionInfo(query), 'query_sync': gi.FunctionInfo(query_sync), 'remove': gi.FunctionInfo(remove), 'remove_sync': gi.FunctionInfo(remove_sync), 'resolve': gi.FunctionInfo(resolve), 'resolve_sync': gi.FunctionInfo(resolve_sync), 'search': gi.FunctionInfo(search), 'search_sync': gi.FunctionInfo(search_sync), 'set_auto_split_threshold': gi.FunctionInfo(set_auto_split_threshold), 'slow_keys': gi.FunctionInfo(slow_keys), 'store': gi.FunctionInfo(store), 'store_metadata': gi.FunctionInfo(store_metadata), 'store_metadata_sync': gi.FunctionInfo(store_metadata_sync), 'store_sync': gi.FunctionInfo(store_sync), 'supported_keys': gi.FunctionInfo(supported_keys), 'supported_operations': gi.FunctionInfo(supported_operations), 'test_media_from_uri': gi.FunctionInfo(test_media_from_uri), 'writable_keys': gi.FunctionInfo(writable_keys), 'do_browse': gi.VFuncInfo(browse), 'do_cancel': gi.VFuncInfo(cancel), 'do_get_caps': gi.VFuncInfo(get_caps), 'do_may_resolve': gi.VFuncInfo(may_resolve), 'do_media_from_uri': gi.VFuncInfo(media_from_uri), 'do_notify_change_start': gi.VFuncInfo(notify_change_start), 'do_notify_change_stop': gi.VFuncInfo(notify_change_stop), 'do_query': gi.VFuncInfo(query), 'do_remove': gi.VFuncInfo(remove), 'do_resolve': gi.VFuncInfo(resolve), 'do_search': gi.VFuncInfo(search), 'do_slow_keys': gi.VFuncInfo(slow_keys), 'do_store': gi.VFuncInfo(store), 'do_store_metadata': gi.VFuncInfo(store_metadata), 'do_supported_keys': gi.VFuncInfo(supported_keys), 'do_supported_operations': gi.VFuncInfo(supported_operations), 'do_test_media_from_uri': gi.VFuncInfo(test_media_from_uri), 'do_writable_keys': gi.VFuncInfo(writable_keys), 'parent': <property object at 0x7fa0403be450>, 'priv': <property object at 0x7fa0403be540>, '_grl_reserved': <property object at 0x7fa0403be630>})"
    __gdoc__ = 'Object GrlSource\n\nSignals from GrlSource:\n  content-changed (GPtrArray, GrlSourceChangeType, gboolean)\n\nProperties from GrlSource:\n  source-id -> gchararray: Source identifier\n    The identifier of the source\n  source-name -> gchararray: Source name\n    The name of the source\n  source-desc -> gchararray: Source description\n    A description of the source\n  source-icon -> GIcon: Source icon\n    Icon representing the source\n  plugin -> GrlPlugin: Plugin\n    Plugin source belongs to\n  rank -> gint: Rank\n    Source rank\n  auto-split-threshold -> guint: Auto-split threshold\n    Threshold to use auto-split of queries\n  supported-media -> GrlSupportedMedia: Supported media\n    List of supported media types\n  source-tags -> GStrv: Tags\n    String array of tags relevant this source\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GrlSource (94188897403200)>'
    __info__ = ObjectInfo(Source)


