# encoding: utf-8
# module gi.repository.Gee
# from /usr/lib64/girepository-1.0/Gee-0.8.typelib
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


from .AbstractMap import AbstractMap

from .SortedMap import SortedMap

class AbstractSortedMap(AbstractMap, SortedMap):
    """
    :Constructors:
    
    ::
    
        AbstractSortedMap(**properties)
    """
    def all_match(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ all_match(self, pred:Gee.Predicate, pred_target=None) -> bool """
        return False

    def any_match(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ any_match(self, pred:Gee.Predicate, pred_target=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def chop(self, offset, length): # real signature unknown; restored from __doc__
        """ chop(self, offset:int, length:int) -> Gee.Iterator """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
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

    def contains(self, key=None): # real signature unknown; restored from __doc__
        """ contains(self, key=None) -> bool """
        return False

    def contains_all(self, map): # real signature unknown; restored from __doc__
        """ contains_all(self, map:Gee.Map) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_clear(self, *args, **kwargs): # real signature unknown
        """ clear(self) """
        pass

    def do_foreach(self, *args, **kwargs): # real signature unknown
        """ foreach(self, f:Gee.ForallFunc, f_target=None) -> bool """
        pass

    def do_get(self, *args, **kwargs): # real signature unknown
        """ get(self, key=None) """
        pass

    def do_get_ascending_entries(self, *args, **kwargs): # real signature unknown
        """ get_ascending_entries(self) -> Gee.SortedSet """
        pass

    def do_get_ascending_keys(self, *args, **kwargs): # real signature unknown
        """ get_ascending_keys(self) -> Gee.SortedSet """
        pass

    def do_get_entries(self, *args, **kwargs): # real signature unknown
        """ get_entries(self) -> Gee.Set """
        pass

    def do_get_keys(self, *args, **kwargs): # real signature unknown
        """ get_keys(self) -> Gee.Set """
        pass

    def do_get_read_only(self, *args, **kwargs): # real signature unknown
        """ get_read_only(self) -> bool """
        pass

    def do_get_read_only_view(self, *args, **kwargs): # real signature unknown
        """ get_read_only_view(self) -> Gee.Map """
        pass

    def do_get_size(self, *args, **kwargs): # real signature unknown
        """ get_size(self) -> int """
        pass

    def do_get_values(self, *args, **kwargs): # real signature unknown
        """ get_values(self) -> Gee.Collection """
        pass

    def do_has(self, *args, **kwargs): # real signature unknown
        """ has(self, key=None, value=None) -> bool """
        pass

    def do_has_key(self, *args, **kwargs): # real signature unknown
        """ has_key(self, key=None) -> bool """
        pass

    def do_head_map(self, *args, **kwargs): # real signature unknown
        """ head_map(self, before=None) -> Gee.SortedMap """
        pass

    def do_map_iterator(self, *args, **kwargs): # real signature unknown
        """ map_iterator(self) -> Gee.MapIterator """
        pass

    def do_set(self, *args, **kwargs): # real signature unknown
        """ set(self, key=None, value=None) """
        pass

    def do_stream(self, *args, **kwargs): # real signature unknown
        """ stream(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.StreamFunc, f_target=None) -> Gee.Iterator """
        pass

    def do_sub_map(self, *args, **kwargs): # real signature unknown
        """ sub_map(self, before=None, after=None) -> Gee.SortedMap """
        pass

    def do_tail_map(self, *args, **kwargs): # real signature unknown
        """ tail_map(self, after=None) -> Gee.SortedMap """
        pass

    def do_unset(self, *args, **kwargs): # real signature unknown
        """ unset(self, key=None) -> bool, value """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def empty(self, k_type, k_dup_func, k_destroy_func, v_type, v_dup_func, v_destroy_func): # real signature unknown; restored from __doc__
        """ empty(k_type:GType, k_dup_func:GObject.BoxedCopyFunc, k_destroy_func:GLib.DestroyNotify, v_type:GType, v_dup_func:GObject.BoxedCopyFunc, v_destroy_func:GLib.DestroyNotify) -> Gee.Map """
        pass

    def filter(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ filter(self, pred:Gee.Predicate, pred_target=None) -> Gee.Iterator """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def first_match(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ first_match(self, pred:Gee.Predicate, pred_target=None) """
        pass

    def flat_map(self, a_type, a_dup_func, a_destroy_func, f, f_target=None): # real signature unknown; restored from __doc__
        """ flat_map(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.FlatMapFunc, f_target=None) -> Gee.Iterator """
        pass

    def fold(self, a_type, a_dup_func, a_destroy_func, f, f_target=None, seed=None): # real signature unknown; restored from __doc__
        """ fold(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.FoldFunc, f_target=None, seed=None) """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, f, f_target=None): # real signature unknown; restored from __doc__
        """ foreach(self, f:Gee.ForallFunc, f_target=None) -> bool """
        return False

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

    def get(self, key=None): # real signature unknown; restored from __doc__
        """ get(self, key=None) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_ascending_entries(self): # real signature unknown; restored from __doc__
        """ get_ascending_entries(self) -> Gee.SortedSet """
        pass

    def get_ascending_keys(self): # real signature unknown; restored from __doc__
        """ get_ascending_keys(self) -> Gee.SortedSet """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_element_type(self): # real signature unknown; restored from __doc__
        """ get_element_type(self) -> GType """
        pass

    def get_entries(self): # real signature unknown; restored from __doc__
        """ get_entries(self) -> Gee.Set """
        pass

    def get_is_empty(self): # real signature unknown; restored from __doc__
        """ get_is_empty(self) -> bool """
        return False

    def get_keys(self): # real signature unknown; restored from __doc__
        """ get_keys(self) -> Gee.Set """
        pass

    def get_key_type(self): # real signature unknown; restored from __doc__
        """ get_key_type(self) -> GType """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_read_only(self): # real signature unknown; restored from __doc__
        """ get_read_only(self) -> bool """
        return False

    def get_read_only_view(self): # real signature unknown; restored from __doc__
        """ get_read_only_view(self) -> Gee.Map """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_values(self): # real signature unknown; restored from __doc__
        """ get_values(self) -> Gee.Collection """
        pass

    def get_value_type(self): # real signature unknown; restored from __doc__
        """ get_value_type(self) -> GType """
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

    def has(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ has(self, key=None, value=None) -> bool """
        return False

    def has_all(self, map): # real signature unknown; restored from __doc__
        """ has_all(self, map:Gee.Map) -> bool """
        return False

    def has_key(self, key=None): # real signature unknown; restored from __doc__
        """ has_key(self, key=None) -> bool """
        return False

    def head_map(self, before=None): # real signature unknown; restored from __doc__
        """ head_map(self, before=None) -> Gee.SortedMap """
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

    def iterator(self): # real signature unknown; restored from __doc__
        """ iterator(self) -> Gee.Iterator """
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def map(self, a_type, a_dup_func, a_destroy_func, f, f_target=None): # real signature unknown; restored from __doc__
        """ map(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.MapFunc, f_target=None) -> Gee.Iterator """
        pass

    def map_iterator(self): # real signature unknown; restored from __doc__
        """ map_iterator(self) -> Gee.MapIterator """
        pass

    def max(self, compare, compare_target=None): # real signature unknown; restored from __doc__
        """ max(self, compare:GLib.CompareDataFunc, compare_target=None) """
        pass

    def min(self, compare, compare_target=None): # real signature unknown; restored from __doc__
        """ min(self, compare:GLib.CompareDataFunc, compare_target=None) """
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

    def order_by(self, compare=None, compare_target=None): # real signature unknown; restored from __doc__
        """ order_by(self, compare:GLib.CompareDataFunc=None, compare_target=None) -> Gee.Iterator """
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

    def remove(self, key=None): # real signature unknown; restored from __doc__
        """ remove(self, key=None) -> bool, value """
        return False

    def remove_all(self, map): # real signature unknown; restored from __doc__
        """ remove_all(self, map:Gee.Map) -> bool """
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

    def scan(self, a_type, a_dup_func, a_destroy_func, f, f_target=None, seed=None): # real signature unknown; restored from __doc__
        """ scan(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.FoldFunc, f_target=None, seed=None) -> Gee.Iterator """
        pass

    def set(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ set(self, key=None, value=None) """
        pass

    def set_all(self, map): # real signature unknown; restored from __doc__
        """ set_all(self, map:Gee.Map) """
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

    def stream(self, a_type, a_dup_func, a_destroy_func, f, f_target=None): # real signature unknown; restored from __doc__
        """ stream(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.StreamFunc, f_target=None) -> Gee.Iterator """
        pass

    def sub_map(self, before=None, after=None): # real signature unknown; restored from __doc__
        """ sub_map(self, before=None, after=None) -> Gee.SortedMap """
        pass

    def tail_map(self, after=None): # real signature unknown; restored from __doc__
        """ tail_map(self, after=None) -> Gee.SortedMap """
        pass

    def tee(self, forks): # real signature unknown; restored from __doc__
        """ tee(self, forks:int) -> list, result_length1:int """
        return []

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unset(self, key=None): # real signature unknown; restored from __doc__
        """ unset(self, key=None) -> bool, value """
        return False

    def unset_all(self, map): # real signature unknown; restored from __doc__
        """ unset_all(self, map:Gee.Map) -> bool """
        return False

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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f6a87c86a30>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(AbstractSortedMap), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeAbstractSortedMap (94716266590224)>, '__doc__': None, '__gsignals__': {}, 'head_map': gi.FunctionInfo(head_map), 'tail_map': gi.FunctionInfo(tail_map), 'sub_map': gi.FunctionInfo(sub_map), 'get_ascending_keys': gi.FunctionInfo(get_ascending_keys), 'get_ascending_entries': gi.FunctionInfo(get_ascending_entries), 'do_head_map': gi.VFuncInfo(head_map), 'do_tail_map': gi.VFuncInfo(tail_map), 'do_sub_map': gi.VFuncInfo(sub_map), 'do_get_ascending_keys': gi.VFuncInfo(get_ascending_keys), 'do_get_ascending_entries': gi.VFuncInfo(get_ascending_entries), 'parent_instance': <property object at 0x7f6a87ca0a90>, 'priv': <property object at 0x7f6a87ca0c20>})"
    __gdoc__ = 'Object GeeAbstractSortedMap\n\nProperties from GeeAbstractSortedMap:\n  k-type -> GType: type\n    type\n  k-dup-func -> gpointer: dup func\n    dup func\n  k-destroy-func -> gpointer: destroy func\n    destroy func\n  v-type -> GType: type\n    type\n  v-dup-func -> gpointer: dup func\n    dup func\n  v-destroy-func -> gpointer: destroy func\n    destroy func\n  ascending-keys -> GeeSortedSet: ascending-keys\n    ascending-keys\n  ascending-entries -> GeeSortedSet: ascending-entries\n    ascending-entries\n  read-only-view -> GeeSortedMap: read-only-view\n    read-only-view\n\nProperties from GeeAbstractMap:\n  k-type -> GType: type\n    type\n  k-dup-func -> gpointer: dup func\n    dup func\n  k-destroy-func -> gpointer: destroy func\n    destroy func\n  v-type -> GType: type\n    type\n  v-dup-func -> gpointer: dup func\n    dup func\n  v-destroy-func -> gpointer: destroy func\n    destroy func\n  size -> gint: size\n    size\n  read-only -> gboolean: read-only\n    read-only\n  keys -> GeeSet: keys\n    keys\n  values -> GeeCollection: values\n    values\n  entries -> GeeSet: entries\n    entries\n  read-only-view -> GeeMap: read-only-view\n    read-only-view\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeAbstractSortedMap (94716266590224)>'
    __info__ = ObjectInfo(AbstractSortedMap)


