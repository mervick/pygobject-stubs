# encoding: utf-8
# module gi.repository.AppStream
# from /usr/lib64/girepository-1.0/AppStream-1.0.typelib
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


class Pool(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Pool(**properties)
        new() -> AppStream.Pool
    """
    def add_component(self, cpt): # real signature unknown; restored from __doc__
        """ add_component(self, cpt:AppStream.Component) -> bool """
        return False

    def add_metadata_location(self, directory): # real signature unknown; restored from __doc__
        """ add_metadata_location(self, directory:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear2(self): # real signature unknown; restored from __doc__
        """ clear2(self) -> bool """
        return False

    def clear_metadata_locations(self): # real signature unknown; restored from __doc__
        """ clear_metadata_locations(self) """
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

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

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

    def get_cache_flags(self): # real signature unknown; restored from __doc__
        """ get_cache_flags(self) -> AppStream.CacheFlags """
        pass

    def get_cache_location(self): # real signature unknown; restored from __doc__
        """ get_cache_location(self) -> str """
        return ""

    def get_components(self): # real signature unknown; restored from __doc__
        """ get_components(self) -> list """
        return []

    def get_components_by_categories(self, categories): # real signature unknown; restored from __doc__
        """ get_components_by_categories(self, categories:str) -> list """
        return []

    def get_components_by_id(self, cid): # real signature unknown; restored from __doc__
        """ get_components_by_id(self, cid:str) -> list """
        return []

    def get_components_by_kind(self, kind): # real signature unknown; restored from __doc__
        """ get_components_by_kind(self, kind:AppStream.ComponentKind) -> list """
        return []

    def get_components_by_launchable(self, kind, id): # real signature unknown; restored from __doc__
        """ get_components_by_launchable(self, kind:AppStream.LaunchableKind, id:str) -> list """
        return []

    def get_components_by_provided_item(self, kind, item): # real signature unknown; restored from __doc__
        """ get_components_by_provided_item(self, kind:AppStream.ProvidedKind, item:str) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> AppStream.PoolFlags """
        pass

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str """
        return ""

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

    def load(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def load_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_cache_file(self, fname): # real signature unknown; restored from __doc__
        """ load_cache_file(self, fname:str) -> bool """
        return False

    def load_finish(self, result): # real signature unknown; restored from __doc__
        """ load_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> AppStream.Pool """
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

    def refresh_cache(self, force): # real signature unknown; restored from __doc__
        """ refresh_cache(self, force:bool) -> bool """
        return False

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

    def save_cache_file(self, fname): # real signature unknown; restored from __doc__
        """ save_cache_file(self, fname:str) -> bool """
        return False

    def search(self, search): # real signature unknown; restored from __doc__
        """ search(self, search:str) -> list """
        return []

    def set_cache_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_cache_flags(self, flags:AppStream.CacheFlags) """
        pass

    def set_cache_location(self, fname): # real signature unknown; restored from __doc__
        """ set_cache_location(self, fname:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:AppStream.PoolFlags) """
        pass

    def set_locale(self, locale): # real signature unknown; restored from __doc__
        """ set_locale(self, locale:str) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f75420d4cd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Pool), '__module__': 'gi.repository.AppStream', '__gtype__': <GType AsPool (94779631127696)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'error_quark': gi.FunctionInfo(error_quark), 'add_component': gi.FunctionInfo(add_component), 'add_metadata_location': gi.FunctionInfo(add_metadata_location), 'clear': gi.FunctionInfo(clear), 'clear2': gi.FunctionInfo(clear2), 'clear_metadata_locations': gi.FunctionInfo(clear_metadata_locations), 'get_cache_flags': gi.FunctionInfo(get_cache_flags), 'get_cache_location': gi.FunctionInfo(get_cache_location), 'get_components': gi.FunctionInfo(get_components), 'get_components_by_categories': gi.FunctionInfo(get_components_by_categories), 'get_components_by_id': gi.FunctionInfo(get_components_by_id), 'get_components_by_kind': gi.FunctionInfo(get_components_by_kind), 'get_components_by_launchable': gi.FunctionInfo(get_components_by_launchable), 'get_components_by_provided_item': gi.FunctionInfo(get_components_by_provided_item), 'get_flags': gi.FunctionInfo(get_flags), 'get_locale': gi.FunctionInfo(get_locale), 'load': gi.FunctionInfo(load), 'load_async': gi.FunctionInfo(load_async), 'load_cache_file': gi.FunctionInfo(load_cache_file), 'load_finish': gi.FunctionInfo(load_finish), 'refresh_cache': gi.FunctionInfo(refresh_cache), 'save_cache_file': gi.FunctionInfo(save_cache_file), 'search': gi.FunctionInfo(search), 'set_cache_flags': gi.FunctionInfo(set_cache_flags), 'set_cache_location': gi.FunctionInfo(set_cache_location), 'set_flags': gi.FunctionInfo(set_flags), 'set_locale': gi.FunctionInfo(set_locale), 'parent_instance': <property object at 0x7f75421914a0>})"
    __gdoc__ = 'Object AsPool\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AsPool (94779631127696)>'
    __info__ = ObjectInfo(Pool)


