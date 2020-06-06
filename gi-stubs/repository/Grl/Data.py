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


class Data(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Data(**properties)
        new() -> Grl.Data
    """
    def add_binary(self, key, buf, size): # real signature unknown; restored from __doc__
        """ add_binary(self, key:int, buf:int, size:int) """
        pass

    def add_boxed(self, key, boxed=None): # real signature unknown; restored from __doc__
        """ add_boxed(self, key:int, boxed=None) """
        pass

    def add_float(self, key, floatvalue): # real signature unknown; restored from __doc__
        """ add_float(self, key:int, floatvalue:float) """
        pass

    def add_for_id(self, key_name, value): # real signature unknown; restored from __doc__
        """ add_for_id(self, key_name:str, value:GObject.Value) -> bool """
        return False

    def add_int(self, key, intvalue): # real signature unknown; restored from __doc__
        """ add_int(self, key:int, intvalue:int) """
        pass

    def add_int64(self, key, intvalue): # real signature unknown; restored from __doc__
        """ add_int64(self, key:int, intvalue:int) """
        pass

    def add_related_keys(self, relkeys): # real signature unknown; restored from __doc__
        """ add_related_keys(self, relkeys:Grl.RelatedKeys) """
        pass

    def add_string(self, key, strvalue): # real signature unknown; restored from __doc__
        """ add_string(self, key:int, strvalue:str) """
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

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Grl.Data """
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

    def get(self, key): # real signature unknown; restored from __doc__
        """ get(self, key:int) -> GObject.Value """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_binary(self, key): # real signature unknown; restored from __doc__
        """ get_binary(self, key:int) -> int, size:int """
        return 0

    def get_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_boolean(self, key:int) -> bool """
        return False

    def get_boxed(self, key): # real signature unknown; restored from __doc__
        """ get_boxed(self, key:int) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_float(self, key): # real signature unknown; restored from __doc__
        """ get_float(self, key:int) -> float """
        return 0.0

    def get_int(self, key): # real signature unknown; restored from __doc__
        """ get_int(self, key:int) -> int """
        return 0

    def get_int64(self, key): # real signature unknown; restored from __doc__
        """ get_int64(self, key:int) -> int """
        return 0

    def get_keys(self): # real signature unknown; restored from __doc__
        """ get_keys(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_related_keys(self, key, index): # real signature unknown; restored from __doc__
        """ get_related_keys(self, key:int, index:int) -> Grl.RelatedKeys """
        pass

    def get_single_values_for_key(self, key): # real signature unknown; restored from __doc__
        """ get_single_values_for_key(self, key:int) -> list """
        return []

    def get_single_values_for_key_string(self, key): # real signature unknown; restored from __doc__
        """ get_single_values_for_key_string(self, key:int) -> list """
        return []

    def get_string(self, key): # real signature unknown; restored from __doc__
        """ get_string(self, key:int) -> str """
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

    def has_key(self, key): # real signature unknown; restored from __doc__
        """ has_key(self, key:int) -> bool """
        return False

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

    def length(self, key): # real signature unknown; restored from __doc__
        """ length(self, key:int) -> int """
        return 0

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Grl.Data """
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

    def remove(self, key): # real signature unknown; restored from __doc__
        """ remove(self, key:int) """
        pass

    def remove_nth(self, key, index): # real signature unknown; restored from __doc__
        """ remove_nth(self, key:int, index:int) """
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

    def set(self, key, value): # real signature unknown; restored from __doc__
        """ set(self, key:int, value:GObject.Value) """
        pass

    def set_binary(self, key, buf, size): # real signature unknown; restored from __doc__
        """ set_binary(self, key:int, buf:int, size:int) """
        pass

    def set_boolean(self, key, boolvalue): # real signature unknown; restored from __doc__
        """ set_boolean(self, key:int, boolvalue:bool) """
        pass

    def set_boxed(self, key, boxed=None): # real signature unknown; restored from __doc__
        """ set_boxed(self, key:int, boxed=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_float(self, key, floatvalue): # real signature unknown; restored from __doc__
        """ set_float(self, key:int, floatvalue:float) """
        pass

    def set_for_id(self, key_name, value): # real signature unknown; restored from __doc__
        """ set_for_id(self, key_name:str, value:GObject.Value) -> bool """
        return False

    def set_int(self, key, intvalue): # real signature unknown; restored from __doc__
        """ set_int(self, key:int, intvalue:int) """
        pass

    def set_int64(self, key, intvalue): # real signature unknown; restored from __doc__
        """ set_int64(self, key:int, intvalue:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_related_keys(self, relkeys, index): # real signature unknown; restored from __doc__
        """ set_related_keys(self, relkeys:Grl.RelatedKeys, index:int) """
        pass

    def set_string(self, key, strvalue): # real signature unknown; restored from __doc__
        """ set_string(self, key:int, strvalue:str) """
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

    _grl_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa0403d8df0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Data), '__module__': 'gi.repository.Grl', '__gtype__': <GType GrlData (94188897281968)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_binary': gi.FunctionInfo(add_binary), 'add_boxed': gi.FunctionInfo(add_boxed), 'add_float': gi.FunctionInfo(add_float), 'add_for_id': gi.FunctionInfo(add_for_id), 'add_int': gi.FunctionInfo(add_int), 'add_int64': gi.FunctionInfo(add_int64), 'add_related_keys': gi.FunctionInfo(add_related_keys), 'add_string': gi.FunctionInfo(add_string), 'dup': gi.FunctionInfo(dup), 'get': gi.FunctionInfo(get), 'get_binary': gi.FunctionInfo(get_binary), 'get_boolean': gi.FunctionInfo(get_boolean), 'get_boxed': gi.FunctionInfo(get_boxed), 'get_float': gi.FunctionInfo(get_float), 'get_int': gi.FunctionInfo(get_int), 'get_int64': gi.FunctionInfo(get_int64), 'get_keys': gi.FunctionInfo(get_keys), 'get_related_keys': gi.FunctionInfo(get_related_keys), 'get_single_values_for_key': gi.FunctionInfo(get_single_values_for_key), 'get_single_values_for_key_string': gi.FunctionInfo(get_single_values_for_key_string), 'get_string': gi.FunctionInfo(get_string), 'has_key': gi.FunctionInfo(has_key), 'length': gi.FunctionInfo(length), 'remove': gi.FunctionInfo(remove), 'remove_nth': gi.FunctionInfo(remove_nth), 'set': gi.FunctionInfo(set), 'set_binary': gi.FunctionInfo(set_binary), 'set_boolean': gi.FunctionInfo(set_boolean), 'set_boxed': gi.FunctionInfo(set_boxed), 'set_float': gi.FunctionInfo(set_float), 'set_for_id': gi.FunctionInfo(set_for_id), 'set_int': gi.FunctionInfo(set_int), 'set_int64': gi.FunctionInfo(set_int64), 'set_related_keys': gi.FunctionInfo(set_related_keys), 'set_string': gi.FunctionInfo(set_string), 'parent': <property object at 0x7fa040494f90>, 'priv': <property object at 0x7fa0404960e0>, '_grl_reserved': <property object at 0x7fa0404961d0>})"
    __gdoc__ = 'Object GrlData\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GrlData (94188897281968)>'
    __info__ = ObjectInfo(Data)


