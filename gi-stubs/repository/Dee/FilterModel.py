# encoding: utf-8
# module gi.repository.Dee
# from /usr/lib/girepository-1.0/Dee-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Dee as __gi_overrides_Dee
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


from .ProxyModel import ProxyModel

class FilterModel(ProxyModel):
    """
    :Constructors:
    
    ::
    
        FilterModel(**properties)
        new(orig_model:Dee.Model, filter:Dee.Filter) -> Dee.FilterModel
    """
    def append(self, *args, **kwargs): # reliably restored by inspect
        # no doc
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

    def find_row_sorted(self, row_spec, sort_func, data): # reliably restored by inspect
        # no doc
        pass

    def find_sorted(self, sort_func, *args, **kwargs): # reliably restored by inspect
        # no doc
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

    def get_row(self, itr): # reliably restored by inspect
        # no doc
        pass

    def get_schema(self): # reliably restored by inspect
        # no doc
        pass

    def get_value(self, itr, column): # reliably restored by inspect
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

    def insert(self, pos, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def insert_before(self, iter, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def insert_row_sorted(self, row_spec, sort_func, data): # reliably restored by inspect
        # no doc
        pass

    def insert_sorted(self, sort_func, *args, **kwargs): # reliably restored by inspect
        # no doc
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

    def prepend(self, *args, **kwargs): # reliably restored by inspect
        # no doc
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

    def set_column_names(self, *args): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_schema(self, *args): # reliably restored by inspect
        # no doc
        pass

    def set_value(self, itr, column, value): # reliably restored by inspect
        # no doc
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

    def _build_row(self, args, kwargs): # reliably restored by inspect
        # no doc
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

    def __getitem__(self, itr): # reliably restored by inspect
        # no doc
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

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
        # no doc
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

    def __setitem__(self, itr, row): # reliably restored by inspect
        # no doc
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    append_iter = gi.FunctionInfo(append_iter)
    append_row = gi.FunctionInfo(append_row)
    begin_changeset = gi.FunctionInfo(begin_changeset)
    clear = gi.FunctionInfo(clear)
    clear_tag = gi.FunctionInfo(clear_tag)
    contains = gi.FunctionInfo(contains)
    end_changeset = gi.FunctionInfo(end_changeset)
    externalize = gi.FunctionInfo(externalize)
    find_row_sorted_with_sizes = gi.FunctionInfo(find_row_sorted_with_sizes)
    getv = gi.FunctionInfo(getv)
    get_bool = gi.FunctionInfo(get_bool)
    get_column_index = gi.FunctionInfo(get_column_index)
    get_column_names = gi.FunctionInfo(get_column_names)
    get_column_schema = gi.FunctionInfo(get_column_schema)
    get_double = gi.FunctionInfo(get_double)
    get_field_schema = gi.FunctionInfo(get_field_schema)
    get_first_iter = gi.FunctionInfo(get_first_iter)
    get_int32 = gi.FunctionInfo(get_int32)
    get_int64 = gi.FunctionInfo(get_int64)
    get_iter_at_row = gi.FunctionInfo(get_iter_at_row)
    get_last_iter = gi.FunctionInfo(get_last_iter)
    get_n_columns = gi.FunctionInfo(get_n_columns)
    get_n_rows = gi.FunctionInfo(get_n_rows)
    get_position = gi.FunctionInfo(get_position)
    get_seqnum = gi.FunctionInfo(get_seqnum)
    get_string = gi.FunctionInfo(get_string)
    get_tag = gi.FunctionInfo(get_tag)
    get_uchar = gi.FunctionInfo(get_uchar)
    get_uint32 = gi.FunctionInfo(get_uint32)
    get_uint64 = gi.FunctionInfo(get_uint64)
    get_value_by_name = gi.FunctionInfo(get_value_by_name)
    get_vardict_schema = gi.FunctionInfo(get_vardict_schema)
    inc_seqnum = gi.FunctionInfo(inc_seqnum)
    insert_iter = gi.FunctionInfo(insert_iter)
    insert_iter_before = gi.FunctionInfo(insert_iter_before)
    insert_iter_with_original_order = gi.FunctionInfo(insert_iter_with_original_order)
    insert_row = gi.FunctionInfo(insert_row)
    insert_row_before = gi.FunctionInfo(insert_row_before)
    insert_row_sorted_with_sizes = gi.FunctionInfo(insert_row_sorted_with_sizes)
    is_first = gi.FunctionInfo(is_first)
    is_floating = gi.FunctionInfo(is_floating)
    is_last = gi.FunctionInfo(is_last)
    new = gi.FunctionInfo(new)
    newv = gi.FunctionInfo(newv)
    next = gi.FunctionInfo(next)
    notify = gi.FunctionInfo(notify)
    parse = gi.FunctionInfo(parse)
    parse_external = gi.FunctionInfo(parse_external)
    prepend_iter = gi.FunctionInfo(prepend_iter)
    prepend_row = gi.FunctionInfo(prepend_row)
    prev = gi.FunctionInfo(prev)
    props = None # (!) real value is '<gi._gi.GProps object at 0x7f5a2cf24a90>'
    register_tag = gi.FunctionInfo(register_tag)
    register_vardict_schema = gi.FunctionInfo(register_vardict_schema)
    remove = gi.FunctionInfo(remove)
    serialize = gi.FunctionInfo(serialize)
    set_column_names_full = gi.FunctionInfo(set_column_names_full)
    set_row = gi.FunctionInfo(set_row)
    set_schema_full = gi.FunctionInfo(set_schema_full)
    set_seqnum = gi.FunctionInfo(set_seqnum)
    set_tag = gi.FunctionInfo(set_tag)
    thaw_notify = gi.FunctionInfo(thaw_notify)
    _force_floating = gi.FunctionInfo(force_floating)
    _ref = gi.FunctionInfo(ref)
    _ref_sink = gi.FunctionInfo(ref_sink)
    _unref = gi.FunctionInfo(unref)
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(FilterModel), '__module__': 'gi.repository.Dee', '__gtype__': <GType DeeFilterModel (19269536)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'append_iter': gi.FunctionInfo(append_iter), 'contains': gi.FunctionInfo(contains), 'insert_iter': gi.FunctionInfo(insert_iter), 'insert_iter_before': gi.FunctionInfo(insert_iter_before), 'insert_iter_with_original_order': gi.FunctionInfo(insert_iter_with_original_order), 'prepend_iter': gi.FunctionInfo(prepend_iter), 'parent': <property object at 0x7f5a2cf3cb38>, 'priv': <property object at 0x7f5a2cf3cb88>})"
    __gdoc__ = 'Object DeeFilterModel\n\nProperties from DeeFilterModel:\n  filter -> gpointer: Filter\n    Filtering rules applied to the original model\n\nSignals from DeeModel:\n  row-added (DeeModelIter)\n  row-removed (DeeModelIter)\n  row-changed (DeeModelIter)\n  changeset-started ()\n  changeset-finished ()\n\nProperties from DeeProxyModel:\n  back-end -> DeeModel: Back end\n    Back end model\n  proxy-signals -> gboolean: Proxy signals\n    Whether or not to automatically forward signals from the back end\n  inherit-seqnums -> gboolean: Inherit seqnums\n    Whether or not to inherit seqnums\n\nSignals from DeeModel:\n  row-added (DeeModelIter)\n  row-removed (DeeModelIter)\n  row-changed (DeeModelIter)\n  changeset-started ()\n  changeset-finished ()\n\nSignals from DeeModel:\n  row-added (DeeModelIter)\n  row-removed (DeeModelIter)\n  row-changed (DeeModelIter)\n  changeset-started ()\n  changeset-finished ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DeeFilterModel (19269536)>'
    __info__ = ObjectInfo(FilterModel)


