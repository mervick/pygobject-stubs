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


class Registry(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Registry(**properties)
    """
    def activate_all_plugins(self): # real signature unknown; restored from __doc__
        """ activate_all_plugins(self) -> bool """
        return False

    def activate_plugin_by_id(self, plugin_id): # real signature unknown; restored from __doc__
        """ activate_plugin_by_id(self, plugin_id:str) -> bool """
        return False

    def add_config(self, config): # real signature unknown; restored from __doc__
        """ add_config(self, config:Grl.Config) -> bool """
        return False

    def add_config_from_file(self, config_file): # real signature unknown; restored from __doc__
        """ add_config_from_file(self, config_file:str) -> bool """
        return False

    def add_config_from_resource(self, resource_path): # real signature unknown; restored from __doc__
        """ add_config_from_resource(self, resource_path:str) -> bool """
        return False

    def add_directory(self, path): # real signature unknown; restored from __doc__
        """ add_directory(self, path:str) """
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

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Grl.Registry """
        pass

    def get_metadata_keys(self): # real signature unknown; restored from __doc__
        """ get_metadata_keys(self) -> list """
        return []

    def get_plugins(self, only_loaded): # real signature unknown; restored from __doc__
        """ get_plugins(self, only_loaded:bool) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sources(self, ranked): # real signature unknown; restored from __doc__
        """ get_sources(self, ranked:bool) -> list """
        return []

    def get_sources_by_operations(self, ops, ranked): # real signature unknown; restored from __doc__
        """ get_sources_by_operations(self, ops:Grl.SupportedOps, ranked:bool) -> list """
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

    def load_all_plugins(self, activate): # real signature unknown; restored from __doc__
        """ load_all_plugins(self, activate:bool) -> bool """
        return False

    def load_plugin(self, library_filename): # real signature unknown; restored from __doc__
        """ load_plugin(self, library_filename:str) -> bool """
        return False

    def load_plugin_directory(self, path): # real signature unknown; restored from __doc__
        """ load_plugin_directory(self, path:str) -> bool """
        return False

    def lookup_metadata_key(self, key_name): # real signature unknown; restored from __doc__
        """ lookup_metadata_key(self, key_name:str) -> int """
        return 0

    def lookup_metadata_key_desc(self, key): # real signature unknown; restored from __doc__
        """ lookup_metadata_key_desc(self, key:int) -> str """
        return ""

    def lookup_metadata_key_name(self, key): # real signature unknown; restored from __doc__
        """ lookup_metadata_key_name(self, key:int) -> str """
        return ""

    def lookup_metadata_key_relation(self, key): # real signature unknown; restored from __doc__
        """ lookup_metadata_key_relation(self, key:int) -> list """
        return []

    def lookup_metadata_key_type(self, key): # real signature unknown; restored from __doc__
        """ lookup_metadata_key_type(self, key:int) -> GType """
        pass

    def lookup_plugin(self, plugin_id): # real signature unknown; restored from __doc__
        """ lookup_plugin(self, plugin_id:str) -> Grl.Plugin """
        pass

    def lookup_source(self, source_id): # real signature unknown; restored from __doc__
        """ lookup_source(self, source_id:str) -> Grl.Source """
        pass

    def metadata_key_validate(self, key, value): # real signature unknown; restored from __doc__
        """ metadata_key_validate(self, key:int, value:GObject.Value) -> bool """
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

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register_metadata_key(self, param_spec, bind_key): # real signature unknown; restored from __doc__
        """ register_metadata_key(self, param_spec:GObject.ParamSpec, bind_key:int) -> int """
        return 0

    def register_source(self, plugin, source): # real signature unknown; restored from __doc__
        """ register_source(self, plugin:Grl.Plugin, source:Grl.Source) -> bool """
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

    def unload_plugin(self, plugin_id): # real signature unknown; restored from __doc__
        """ unload_plugin(self, plugin_id:str) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_source(self, source): # real signature unknown; restored from __doc__
        """ unregister_source(self, source:Grl.Source) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _grl_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa0403d83d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Registry), '__module__': 'gi.repository.Grl', '__gtype__': <GType GrlRegistry (94188897427888)>, '__doc__': None, '__gsignals__': {}, 'get_default': gi.FunctionInfo(get_default), 'activate_all_plugins': gi.FunctionInfo(activate_all_plugins), 'activate_plugin_by_id': gi.FunctionInfo(activate_plugin_by_id), 'add_config': gi.FunctionInfo(add_config), 'add_config_from_file': gi.FunctionInfo(add_config_from_file), 'add_config_from_resource': gi.FunctionInfo(add_config_from_resource), 'add_directory': gi.FunctionInfo(add_directory), 'get_metadata_keys': gi.FunctionInfo(get_metadata_keys), 'get_plugins': gi.FunctionInfo(get_plugins), 'get_sources': gi.FunctionInfo(get_sources), 'get_sources_by_operations': gi.FunctionInfo(get_sources_by_operations), 'load_all_plugins': gi.FunctionInfo(load_all_plugins), 'load_plugin': gi.FunctionInfo(load_plugin), 'load_plugin_directory': gi.FunctionInfo(load_plugin_directory), 'lookup_metadata_key': gi.FunctionInfo(lookup_metadata_key), 'lookup_metadata_key_desc': gi.FunctionInfo(lookup_metadata_key_desc), 'lookup_metadata_key_name': gi.FunctionInfo(lookup_metadata_key_name), 'lookup_metadata_key_relation': gi.FunctionInfo(lookup_metadata_key_relation), 'lookup_metadata_key_type': gi.FunctionInfo(lookup_metadata_key_type), 'lookup_plugin': gi.FunctionInfo(lookup_plugin), 'lookup_source': gi.FunctionInfo(lookup_source), 'metadata_key_validate': gi.FunctionInfo(metadata_key_validate), 'register_metadata_key': gi.FunctionInfo(register_metadata_key), 'register_source': gi.FunctionInfo(register_source), 'unload_plugin': gi.FunctionInfo(unload_plugin), 'unregister_source': gi.FunctionInfo(unregister_source), 'parent': <property object at 0x7fa041863ae0>, 'priv': <property object at 0x7fa0404a2c70>, '_grl_reserved': <property object at 0x7fa0404a2d60>})"
    __gdoc__ = 'Object GrlRegistry\n\nSignals from GrlRegistry:\n  source-added (GrlSource)\n  source-removed (GrlSource)\n  metadata-key-added (gchararray)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GrlRegistry (94188897427888)>'
    __info__ = ObjectInfo(Registry)


