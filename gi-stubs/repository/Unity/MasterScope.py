# encoding: utf-8
# module gi.repository.Unity
# from /usr/lib/girepository-1.0/Unity-7.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Unity as __gi_overrides_Unity
import gi.repository.Dee as __gi_repository_Dee
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .AggregatorScope import AggregatorScope

class MasterScope(AggregatorScope):
    """
    :Constructors:
    
    ::
    
        MasterScope(**properties)
        new(dbus_path_:str, id_:str) -> Unity.MasterScope
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
        # no doc
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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
        # no doc
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        # no doc
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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
        # no doc
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
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

    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        default dir() implementation
        """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ default object formatter """
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
        """ helper for pickle """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        size of object in memory, in bytes
        """
        return 0

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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    activate = gi.FunctionInfo(activate)
    activate_finish = gi.FunctionInfo(activate_finish)
    add_constraint = gi.FunctionInfo(add_constraint)
    add_sorter = gi.FunctionInfo(add_sorter)
    category_index_for_scope_id = gi.FunctionInfo(category_index_for_scope_id)
    do_activate = gi.VFuncInfo(activate)
    do_activate_finish = gi.VFuncInfo(activate_finish)
    do_category_index_for_scope_id = gi.VFuncInfo(category_index_for_scope_id)
    do_search = gi.VFuncInfo(search)
    do_search_finish = gi.VFuncInfo(search_finish)
    export = gi.FunctionInfo(export)
    getv = gi.FunctionInfo(getv)
    get_automatic_flushing = gi.FunctionInfo(get_automatic_flushing)
    get_categories = gi.FunctionInfo(get_categories)
    get_dbus_path = gi.FunctionInfo(get_dbus_path)
    get_filters = gi.FunctionInfo(get_filters)
    get_id = gi.FunctionInfo(get_id)
    get_is_master = gi.FunctionInfo(get_is_master)
    get_merge_mode = gi.FunctionInfo(get_merge_mode)
    get_no_content_hint = gi.FunctionInfo(get_no_content_hint)
    get_proxy_filter_hints = gi.FunctionInfo(get_proxy_filter_hints)
    get_schema = gi.FunctionInfo(get_schema)
    get_search_hint = gi.FunctionInfo(get_search_hint)
    get_search_in_global = gi.FunctionInfo(get_search_in_global)
    get_sources = gi.FunctionInfo(get_sources)
    get_visible = gi.FunctionInfo(get_visible)
    is_floating = gi.FunctionInfo(is_floating)
    new = gi.FunctionInfo(new)
    newv = gi.FunctionInfo(newv)
    notify = gi.FunctionInfo(notify)
    props = None # (!) real value is '<gi._gi.GProps object at 0x7f0cf0c93630>'
    search = gi.FunctionInfo(search)
    search_finish = gi.FunctionInfo(search_finish)
    set_automatic_flushing = gi.FunctionInfo(set_automatic_flushing)
    set_categories = gi.FunctionInfo(set_categories)
    set_filters = gi.FunctionInfo(set_filters)
    set_merge_mode = gi.FunctionInfo(set_merge_mode)
    set_no_content_hint = gi.FunctionInfo(set_no_content_hint)
    set_proxy_filter_hints = gi.FunctionInfo(set_proxy_filter_hints)
    set_schema = gi.FunctionInfo(set_schema)
    set_search_hint = gi.FunctionInfo(set_search_hint)
    set_search_in_global = gi.FunctionInfo(set_search_in_global)
    set_visible = gi.FunctionInfo(set_visible)
    thaw_notify = gi.FunctionInfo(thaw_notify)
    unexport = gi.FunctionInfo(unexport)
    _force_floating = gi.FunctionInfo(force_floating)
    _ref = gi.FunctionInfo(ref)
    _ref_sink = gi.FunctionInfo(ref_sink)
    _unref = gi.FunctionInfo(unref)
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MasterScope), '__module__': 'gi.repository.Unity', '__gtype__': <GType UnityMasterScope (26820912)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_no_content_hint': gi.FunctionInfo(get_no_content_hint), 'set_no_content_hint': gi.FunctionInfo(set_no_content_hint), 'parent_instance': <property object at 0x7f0cf0ebdea8>, 'priv': <property object at 0x7f0cf0ebdef8>})"
    __gdoc__ = 'Object UnityMasterScope\n\nProperties from UnityMasterScope:\n  no-content-hint -> gchararray: no-content-hint\n    no-content-hint\n\nProperties from UnityAggregatorScope:\n  merge-mode -> UnityAggregatorScopeMergeMode: merge-mode\n    merge-mode\n  proxy-filter-hints -> gboolean: proxy-filter-hints\n    proxy-filter-hints\n  automatic-flushing -> gboolean: automatic-flushing\n    automatic-flushing\n\nSignals from UnityDeprecatedScopeBase:\n  active-sources-changed (GStrv, gint)\n\nProperties from UnityDeprecatedScopeBase:\n  id -> gchararray: id\n    id\n  dbus-path -> gchararray: dbus-path\n    dbus-path\n  search-in-global -> gboolean: search-in-global\n    search-in-global\n  visible -> gboolean: visible\n    visible\n  is-master -> gboolean: is-master\n    is-master\n  search-hint -> gchararray: search-hint\n    search-hint\n  sources -> UnityOptionsFilter: sources\n    sources\n  categories -> UnityCategorySet: categories\n    categories\n  filters -> UnityFilterSet: filters\n    filters\n  schema -> UnitySchema: schema\n    schema\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UnityMasterScope (26820912)>'
    __info__ = ObjectInfo(MasterScope)


