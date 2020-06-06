# encoding: utf-8
# module gi.repository.Gom
# from /usr/lib64/girepository-1.0/Gom-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Filter(__gi_repository_GObject.InitiallyUnowned):
    """
    :Constructors:
    
    ::
    
        Filter(**properties)
        new_and(left:Gom.Filter, right:Gom.Filter) -> Gom.Filter
        new_and_fullv(filter_array:Gom.Filter) -> Gom.Filter
        new_eq(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_glob(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_gt(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_gte(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_is_not_null(resource_type:GType, property_name:str) -> Gom.Filter
        new_is_null(resource_type:GType, property_name:str) -> Gom.Filter
        new_like(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_lt(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_lte(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_neq(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter
        new_or(left:Gom.Filter, right:Gom.Filter) -> Gom.Filter
        new_or_fullv(filter_array:Gom.Filter) -> Gom.Filter
        new_sql(sql:str, values:list) -> Gom.Filter
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

    def get_sql(self, table_map): # real signature unknown; restored from __doc__
        """ get_sql(self, table_map:dict) -> str """
        return ""

    def get_values(self): # real signature unknown; restored from __doc__
        """ get_values(self) -> list """
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

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_and(self, left, right): # real signature unknown; restored from __doc__
        """ new_and(left:Gom.Filter, right:Gom.Filter) -> Gom.Filter """
        pass

    def new_and_fullv(self, filter_array): # real signature unknown; restored from __doc__
        """ new_and_fullv(filter_array:Gom.Filter) -> Gom.Filter """
        pass

    def new_eq(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_eq(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_glob(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_glob(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_gt(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_gt(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_gte(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_gte(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_is_not_null(self, resource_type, property_name): # real signature unknown; restored from __doc__
        """ new_is_not_null(resource_type:GType, property_name:str) -> Gom.Filter """
        pass

    def new_is_null(self, resource_type, property_name): # real signature unknown; restored from __doc__
        """ new_is_null(resource_type:GType, property_name:str) -> Gom.Filter """
        pass

    def new_like(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_like(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_lt(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_lt(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_lte(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_lte(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_neq(self, resource_type, property_name, value): # real signature unknown; restored from __doc__
        """ new_neq(resource_type:GType, property_name:str, value:GObject.Value) -> Gom.Filter """
        pass

    def new_or(self, left, right): # real signature unknown; restored from __doc__
        """ new_or(left:Gom.Filter, right:Gom.Filter) -> Gom.Filter """
        pass

    def new_or_fullv(self, filter_array): # real signature unknown; restored from __doc__
        """ new_or_fullv(filter_array:Gom.Filter) -> Gom.Filter """
        pass

    def new_sql(self, sql, values): # real signature unknown; restored from __doc__
        """ new_sql(sql:str, values:list) -> Gom.Filter """
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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ff300be16a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Filter), '__module__': 'gi.repository.Gom', '__gtype__': <GType GomFilter (93947029393296)>, '__doc__': None, '__gsignals__': {}, 'new_and': gi.FunctionInfo(new_and), 'new_and_fullv': gi.FunctionInfo(new_and_fullv), 'new_eq': gi.FunctionInfo(new_eq), 'new_glob': gi.FunctionInfo(new_glob), 'new_gt': gi.FunctionInfo(new_gt), 'new_gte': gi.FunctionInfo(new_gte), 'new_is_not_null': gi.FunctionInfo(new_is_not_null), 'new_is_null': gi.FunctionInfo(new_is_null), 'new_like': gi.FunctionInfo(new_like), 'new_lt': gi.FunctionInfo(new_lt), 'new_lte': gi.FunctionInfo(new_lte), 'new_neq': gi.FunctionInfo(new_neq), 'new_or': gi.FunctionInfo(new_or), 'new_or_fullv': gi.FunctionInfo(new_or_fullv), 'new_sql': gi.FunctionInfo(new_sql), 'get_sql': gi.FunctionInfo(get_sql), 'get_values': gi.FunctionInfo(get_values), 'parent': <property object at 0x7ff300bdab30>, 'priv': <property object at 0x7ff300bdac70>})"
    __gdoc__ = 'Object GomFilter\n\nProperties from GomFilter:\n  mode -> GomFilterMode: Mode\n    The mode of the filter.\n  sql -> gchararray: SQL\n    The SQL for the filter.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GomFilter (93947029393296)>'
    __info__ = ObjectInfo(Filter)


