# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


class Client(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Client(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cancel_all(self): # real signature unknown; restored from __doc__
        """ cancel_all(self) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_capability(self, capability): # real signature unknown; restored from __doc__
        """ check_capability(self, capability:str) -> bool """
        return False

    def check_refresh_supported(self): # real signature unknown; restored from __doc__
        """ check_refresh_supported(self) -> bool """
        return False

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

    def do_backend_died(self, *args, **kwargs): # real signature unknown
        """ backend_died(self) """
        pass

    def do_backend_error(self, *args, **kwargs): # real signature unknown
        """ backend_error(self, error_msg:str) """
        pass

    def do_backend_property_changed(self, *args, **kwargs): # real signature unknown
        """ backend_property_changed(self, prop_name:str, prop_value:str) """
        pass

    def do_get_backend_property(self, *args, **kwargs): # real signature unknown
        """ get_backend_property(self, prop_name:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_get_backend_property_finish(self, *args, **kwargs): # real signature unknown
        """ get_backend_property_finish(self, result:Gio.AsyncResult) -> bool, prop_value:str """
        pass

    def do_get_backend_property_sync(self, *args, **kwargs): # real signature unknown
        """ get_backend_property_sync(self, prop_name:str, cancellable:Gio.Cancellable=None) -> bool, prop_value:str """
        pass

    def do_open(self, *args, **kwargs): # real signature unknown
        """ open(self, only_if_exists:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_opened(self, *args, **kwargs): # real signature unknown
        """ opened(self, error:error) """
        pass

    def do_open_finish(self, *args, **kwargs): # real signature unknown
        """ open_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_open_sync(self, *args, **kwargs): # real signature unknown
        """ open_sync(self, only_if_exists:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_refresh(self, *args, **kwargs): # real signature unknown
        """ refresh(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_refresh_finish(self, *args, **kwargs): # real signature unknown
        """ refresh_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_refresh_sync(self, *args, **kwargs): # real signature unknown
        """ refresh_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_remove_finish(self, *args, **kwargs): # real signature unknown
        """ remove_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_remove_sync(self, *args, **kwargs): # real signature unknown
        """ remove_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_retrieve_capabilities(self, *args, **kwargs): # real signature unknown
        """ retrieve_capabilities(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_retrieve_capabilities_finish(self, *args, **kwargs): # real signature unknown
        """ retrieve_capabilities_finish(self, result:Gio.AsyncResult) -> bool, capabilities:str """
        pass

    def do_retrieve_capabilities_sync(self, *args, **kwargs): # real signature unknown
        """ retrieve_capabilities_sync(self, cancellable:Gio.Cancellable=None) -> bool, capabilities:str """
        pass

    def do_retrieve_properties_sync(self, *args, **kwargs): # real signature unknown
        """ retrieve_properties_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_set_backend_property(self, *args, **kwargs): # real signature unknown
        """ set_backend_property(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_set_backend_property_finish(self, *args, **kwargs): # real signature unknown
        """ set_backend_property_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_set_backend_property_sync(self, *args, **kwargs): # real signature unknown
        """ set_backend_property_sync(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_unwrap_dbus_error(self, *args, **kwargs): # real signature unknown
        """ unwrap_dbus_error(self, dbus_error:error) """
        pass

    def dup_bus_name(self): # real signature unknown; restored from __doc__
        """ dup_bus_name(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_create(self, code, custom_msg=None): # real signature unknown; restored from __doc__
        """ error_create(code:EDataServer.ClientError, custom_msg:str=None) -> error """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def error_to_string(self, code): # real signature unknown; restored from __doc__
        """ error_to_string(code:EDataServer.ClientError) -> str """
        return ""

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

    def get_backend_property(self, prop_name, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_backend_property(self, prop_name:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_backend_property_finish(self, result): # real signature unknown; restored from __doc__
        """ get_backend_property_finish(self, result:Gio.AsyncResult) -> bool, prop_value:str """
        return False

    def get_backend_property_sync(self, prop_name, cancellable=None): # real signature unknown; restored from __doc__
        """ get_backend_property_sync(self, prop_name:str, cancellable:Gio.Cancellable=None) -> bool, prop_value:str """
        return False

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> list """
        return []

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

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
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

    def is_online(self): # real signature unknown; restored from __doc__
        """ is_online(self) -> bool """
        return False

    def is_opened(self): # real signature unknown; restored from __doc__
        """ is_opened(self) -> bool """
        return False

    def is_readonly(self): # real signature unknown; restored from __doc__
        """ is_readonly(self) -> bool """
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

    def open(self, only_if_exists, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open(self, only_if_exists:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def open_sync(self, only_if_exists, cancellable=None): # real signature unknown; restored from __doc__
        """ open_sync(self, only_if_exists:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ refresh(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def refresh_finish(self, result): # real signature unknown; restored from __doc__
        """ refresh_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def refresh_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref_main_context(self): # real signature unknown; restored from __doc__
        """ ref_main_context(self) -> GLib.MainContext """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def retrieve_capabilities(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ retrieve_capabilities(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def retrieve_capabilities_finish(self, result): # real signature unknown; restored from __doc__
        """ retrieve_capabilities_finish(self, result:Gio.AsyncResult) -> bool, capabilities:str """
        return False

    def retrieve_capabilities_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ retrieve_capabilities_sync(self, cancellable:Gio.Cancellable=None) -> bool, capabilities:str """
        return False

    def retrieve_properties(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ retrieve_properties(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def retrieve_properties_finish(self, result): # real signature unknown; restored from __doc__
        """ retrieve_properties_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def retrieve_properties_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ retrieve_properties_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_backend_property(self, prop_name, prop_value, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_backend_property(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_backend_property_finish(self, result): # real signature unknown; restored from __doc__
        """ set_backend_property_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_backend_property_sync(self, prop_name, prop_value, cancellable=None): # real signature unknown; restored from __doc__
        """ set_backend_property_sync(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_bus_name(self, bus_name): # real signature unknown; restored from __doc__
        """ set_bus_name(self, bus_name:str) """
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

    def unwrap_dbus_error(self, dbus_error): # real signature unknown; restored from __doc__
        """ unwrap_dbus_error(self, dbus_error:error) """
        pass

    def util_copy_object_slist(self, copy_to=None, objects): # real signature unknown; restored from __doc__
        """ util_copy_object_slist(copy_to:list=None, objects:list) -> list """
        return []

    def util_copy_string_slist(self, copy_to=None, strings): # real signature unknown; restored from __doc__
        """ util_copy_string_slist(copy_to:list=None, strings:list) -> list """
        return []

    def util_free_object_slist(self, objects): # real signature unknown; restored from __doc__
        """ util_free_object_slist(objects:list) """
        pass

    def util_free_string_slist(self, strings): # real signature unknown; restored from __doc__
        """ util_free_string_slist(strings:list) """
        pass

    def util_parse_comma_strings(self, strings): # real signature unknown; restored from __doc__
        """ util_parse_comma_strings(strings:str) -> list """
        return []

    def util_slist_to_strv(self, strings): # real signature unknown; restored from __doc__
        """ util_slist_to_strv(strings:list) -> list """
        return []

    def util_strv_to_slist(self, strv): # real signature unknown; restored from __doc__
        """ util_strv_to_slist(strv:str) -> list """
        return []

    def util_unwrap_dbus_error(self, dbus_error, known_errors, known_errors_count, known_errors_domain, fail_when_none_matched): # real signature unknown; restored from __doc__
        """ util_unwrap_dbus_error(dbus_error:error, known_errors:EDataServer.ClientErrorsList, known_errors_count:int, known_errors_domain:int, fail_when_none_matched:bool) -> bool, client_error:error """
        return False

    def wait_for_connected(self, timeout_seconds, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ wait_for_connected(self, timeout_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def wait_for_connected_finish(self, result): # real signature unknown; restored from __doc__
        """ wait_for_connected_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def wait_for_connected_sync(self, timeout_seconds, cancellable=None): # real signature unknown; restored from __doc__
        """ wait_for_connected_sync(self, timeout_seconds:int, cancellable:Gio.Cancellable=None) -> bool """
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

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f6271bb2670>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Client), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType EClient (94877536840592)>, '__doc__': None, '__gsignals__': {}, 'error_create': gi.FunctionInfo(error_create), 'error_quark': gi.FunctionInfo(error_quark), 'error_to_string': gi.FunctionInfo(error_to_string), 'util_copy_object_slist': gi.FunctionInfo(util_copy_object_slist), 'util_copy_string_slist': gi.FunctionInfo(util_copy_string_slist), 'util_free_object_slist': gi.FunctionInfo(util_free_object_slist), 'util_free_string_slist': gi.FunctionInfo(util_free_string_slist), 'util_parse_comma_strings': gi.FunctionInfo(util_parse_comma_strings), 'util_slist_to_strv': gi.FunctionInfo(util_slist_to_strv), 'util_strv_to_slist': gi.FunctionInfo(util_strv_to_slist), 'util_unwrap_dbus_error': gi.FunctionInfo(util_unwrap_dbus_error), 'cancel_all': gi.FunctionInfo(cancel_all), 'check_capability': gi.FunctionInfo(check_capability), 'check_refresh_supported': gi.FunctionInfo(check_refresh_supported), 'dup_bus_name': gi.FunctionInfo(dup_bus_name), 'get_backend_property': gi.FunctionInfo(get_backend_property), 'get_backend_property_finish': gi.FunctionInfo(get_backend_property_finish), 'get_backend_property_sync': gi.FunctionInfo(get_backend_property_sync), 'get_capabilities': gi.FunctionInfo(get_capabilities), 'get_source': gi.FunctionInfo(get_source), 'is_online': gi.FunctionInfo(is_online), 'is_opened': gi.FunctionInfo(is_opened), 'is_readonly': gi.FunctionInfo(is_readonly), 'open': gi.FunctionInfo(open), 'open_finish': gi.FunctionInfo(open_finish), 'open_sync': gi.FunctionInfo(open_sync), 'ref_main_context': gi.FunctionInfo(ref_main_context), 'refresh': gi.FunctionInfo(refresh), 'refresh_finish': gi.FunctionInfo(refresh_finish), 'refresh_sync': gi.FunctionInfo(refresh_sync), 'remove': gi.FunctionInfo(remove), 'remove_finish': gi.FunctionInfo(remove_finish), 'remove_sync': gi.FunctionInfo(remove_sync), 'retrieve_capabilities': gi.FunctionInfo(retrieve_capabilities), 'retrieve_capabilities_finish': gi.FunctionInfo(retrieve_capabilities_finish), 'retrieve_capabilities_sync': gi.FunctionInfo(retrieve_capabilities_sync), 'retrieve_properties': gi.FunctionInfo(retrieve_properties), 'retrieve_properties_finish': gi.FunctionInfo(retrieve_properties_finish), 'retrieve_properties_sync': gi.FunctionInfo(retrieve_properties_sync), 'set_backend_property': gi.FunctionInfo(set_backend_property), 'set_backend_property_finish': gi.FunctionInfo(set_backend_property_finish), 'set_backend_property_sync': gi.FunctionInfo(set_backend_property_sync), 'set_bus_name': gi.FunctionInfo(set_bus_name), 'unwrap_dbus_error': gi.FunctionInfo(unwrap_dbus_error), 'wait_for_connected': gi.FunctionInfo(wait_for_connected), 'wait_for_connected_finish': gi.FunctionInfo(wait_for_connected_finish), 'wait_for_connected_sync': gi.FunctionInfo(wait_for_connected_sync), 'do_backend_died': gi.VFuncInfo(backend_died), 'do_backend_error': gi.VFuncInfo(backend_error), 'do_backend_property_changed': gi.VFuncInfo(backend_property_changed), 'do_get_backend_property': gi.VFuncInfo(get_backend_property), 'do_get_backend_property_finish': gi.VFuncInfo(get_backend_property_finish), 'do_get_backend_property_sync': gi.VFuncInfo(get_backend_property_sync), 'do_open': gi.VFuncInfo(open), 'do_open_finish': gi.VFuncInfo(open_finish), 'do_open_sync': gi.VFuncInfo(open_sync), 'do_opened': gi.VFuncInfo(opened), 'do_refresh': gi.VFuncInfo(refresh), 'do_refresh_finish': gi.VFuncInfo(refresh_finish), 'do_refresh_sync': gi.VFuncInfo(refresh_sync), 'do_remove': gi.VFuncInfo(remove), 'do_remove_finish': gi.VFuncInfo(remove_finish), 'do_remove_sync': gi.VFuncInfo(remove_sync), 'do_retrieve_capabilities': gi.VFuncInfo(retrieve_capabilities), 'do_retrieve_capabilities_finish': gi.VFuncInfo(retrieve_capabilities_finish), 'do_retrieve_capabilities_sync': gi.VFuncInfo(retrieve_capabilities_sync), 'do_retrieve_properties_sync': gi.VFuncInfo(retrieve_properties_sync), 'do_set_backend_property': gi.VFuncInfo(set_backend_property), 'do_set_backend_property_finish': gi.VFuncInfo(set_backend_property_finish), 'do_set_backend_property_sync': gi.VFuncInfo(set_backend_property_sync), 'do_unwrap_dbus_error': gi.VFuncInfo(unwrap_dbus_error), 'parent': <property object at 0x7f6271bcf860>, 'priv': <property object at 0x7f6271bcfb30>})"
    __gdoc__ = "Object EClient\n\nSignals from EClient:\n  opened (GError)\n  backend-error (gchararray)\n  backend-died ()\n  backend-property-changed (gchararray, gchararray)\n\nProperties from EClient:\n  capabilities -> gpointer: Capabilities\n    The capabilities of this client\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  online -> gboolean: Online\n    Whether this client is online\n  opened -> gboolean: Opened\n    Whether this client is open and ready to use\n  readonly -> gboolean: Read only\n    Whether this client's backing data is readonly\n  source -> ESource: Source\n    The ESource for which this client was created\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EClient (94877536840592)>'
    __info__ = ObjectInfo(Client)


