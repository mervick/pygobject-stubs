# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .AppInfo import AppInfo

class DesktopAppInfo(__gi_overrides_GObject.Object, AppInfo):
    """
    :Constructors:
    
    ::
    
        DesktopAppInfo(**properties)
        new(desktop_id:str) -> Gio.DesktopAppInfo or None
        new_from_filename(filename:str) -> Gio.DesktopAppInfo or None
        new_from_keyfile(key_file:GLib.KeyFile) -> Gio.DesktopAppInfo or None
    """
    def add_supports_type(self, content_type): # real signature unknown; restored from __doc__
        """ add_supports_type(self, content_type:str) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_delete(self): # real signature unknown; restored from __doc__
        """ can_delete(self) -> bool """
        return False

    def can_remove_supports_type(self): # real signature unknown; restored from __doc__
        """ can_remove_supports_type(self) -> bool """
        return False

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

    def create_from_commandline(self, commandline, application_name=None, flags): # real signature unknown; restored from __doc__
        """ create_from_commandline(commandline:str, application_name:str=None, flags:Gio.AppInfoCreateFlags) -> Gio.AppInfo """
        pass

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gio.AppInfo """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equal(self, appinfo2): # real signature unknown; restored from __doc__
        """ equal(self, appinfo2:Gio.AppInfo) -> bool """
        return False

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

    def get_action_name(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_name(self, action_name:str) -> str """
        return ""

    def get_all(self): # real signature unknown; restored from __doc__
        """ get_all() -> list """
        return []

    def get_all_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ get_all_for_type(content_type:str) -> list """
        return []

    def get_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_boolean(self, key:str) -> bool """
        return False

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> str """
        return ""

    def get_commandline(self): # real signature unknown; restored from __doc__
        """ get_commandline(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_for_type(self, content_type, must_support_uris): # real signature unknown; restored from __doc__
        """ get_default_for_type(content_type:str, must_support_uris:bool) -> Gio.AppInfo """
        pass

    def get_default_for_uri_scheme(self, uri_scheme): # real signature unknown; restored from __doc__
        """ get_default_for_uri_scheme(uri_scheme:str) -> Gio.AppInfo """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_executable(self): # real signature unknown; restored from __doc__
        """ get_executable(self) -> str """
        return ""

    def get_fallback_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ get_fallback_for_type(content_type:str) -> list """
        return []

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_generic_name(self): # real signature unknown; restored from __doc__
        """ get_generic_name(self) -> str """
        return ""

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_implementations(self, interface): # real signature unknown; restored from __doc__
        """ get_implementations(interface:str) -> list """
        return []

    def get_is_hidden(self): # real signature unknown; restored from __doc__
        """ get_is_hidden(self) -> bool """
        return False

    def get_keywords(self): # real signature unknown; restored from __doc__
        """ get_keywords(self) -> list """
        return []

    def get_locale_string(self, key): # real signature unknown; restored from __doc__
        """ get_locale_string(self, key:str) -> str or None """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_nodisplay(self): # real signature unknown; restored from __doc__
        """ get_nodisplay(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_recommended_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ get_recommended_for_type(content_type:str) -> list """
        return []

    def get_show_in(self, desktop_env=None): # real signature unknown; restored from __doc__
        """ get_show_in(self, desktop_env:str=None) -> bool """
        return False

    def get_startup_wm_class(self): # real signature unknown; restored from __doc__
        """ get_startup_wm_class(self) -> str """
        return ""

    def get_string(self, key): # real signature unknown; restored from __doc__
        """ get_string(self, key:str) -> str """
        return ""

    def get_string_list(self, key): # real signature unknown; restored from __doc__
        """ get_string_list(self, key:str) -> list, length:int """
        return []

    def get_supported_types(self): # real signature unknown; restored from __doc__
        """ get_supported_types(self) -> list """
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

    def has_key(self, key): # real signature unknown; restored from __doc__
        """ has_key(self, key:str) -> bool """
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

    def launch(self, files=None, context=None): # real signature unknown; restored from __doc__
        """ launch(self, files:list=None, context:Gio.AppLaunchContext=None) -> bool """
        return False

    def launch_action(self, action_name, launch_context=None): # real signature unknown; restored from __doc__
        """ launch_action(self, action_name:str, launch_context:Gio.AppLaunchContext=None) """
        pass

    def launch_default_for_uri(self, uri, context=None): # real signature unknown; restored from __doc__
        """ launch_default_for_uri(uri:str, context:Gio.AppLaunchContext=None) -> bool """
        return False

    def launch_default_for_uri_async(self, uri, context=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ launch_default_for_uri_async(uri:str, context:Gio.AppLaunchContext=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def launch_default_for_uri_finish(self, result): # real signature unknown; restored from __doc__
        """ launch_default_for_uri_finish(result:Gio.AsyncResult) -> bool """
        return False

    def launch_uris(self, uris=None, context=None): # real signature unknown; restored from __doc__
        """ launch_uris(self, uris:list=None, context:Gio.AppLaunchContext=None) -> bool """
        return False

    def launch_uris_async(self, uris=None, context=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ launch_uris_async(self, uris:list=None, context:Gio.AppLaunchContext=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def launch_uris_as_manager(self, uris, launch_context=None, spawn_flags, user_setup=None, user_setup_data=None, pid_callback=None, pid_callback_data=None): # real signature unknown; restored from __doc__
        """ launch_uris_as_manager(self, uris:list, launch_context:Gio.AppLaunchContext=None, spawn_flags:GLib.SpawnFlags, user_setup:GLib.SpawnChildSetupFunc=None, user_setup_data=None, pid_callback:Gio.DesktopAppLaunchCallback=None, pid_callback_data=None) -> bool """
        return False

    def launch_uris_as_manager_with_fds(self, uris, launch_context=None, spawn_flags, user_setup=None, user_setup_data=None, pid_callback=None, pid_callback_data=None, stdin_fd, stdout_fd, stderr_fd): # real signature unknown; restored from __doc__
        """ launch_uris_as_manager_with_fds(self, uris:list, launch_context:Gio.AppLaunchContext=None, spawn_flags:GLib.SpawnFlags, user_setup:GLib.SpawnChildSetupFunc=None, user_setup_data=None, pid_callback:Gio.DesktopAppLaunchCallback=None, pid_callback_data=None, stdin_fd:int, stdout_fd:int, stderr_fd:int) -> bool """
        return False

    def launch_uris_finish(self, result): # real signature unknown; restored from __doc__
        """ launch_uris_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def list_actions(self): # real signature unknown; restored from __doc__
        """ list_actions(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, desktop_id): # real signature unknown; restored from __doc__
        """ new(desktop_id:str) -> Gio.DesktopAppInfo or None """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_filename(self, filename): # real signature unknown; restored from __doc__
        """ new_from_filename(filename:str) -> Gio.DesktopAppInfo or None """
        pass

    def new_from_keyfile(self, key_file): # real signature unknown; restored from __doc__
        """ new_from_keyfile(key_file:GLib.KeyFile) -> Gio.DesktopAppInfo or None """
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

    def remove_supports_type(self, content_type): # real signature unknown; restored from __doc__
        """ remove_supports_type(self, content_type:str) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_type_associations(self, content_type): # real signature unknown; restored from __doc__
        """ reset_type_associations(content_type:str) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def search(self, search_string): # real signature unknown; restored from __doc__
        """ search(search_string:str) -> list """
        return []

    def set_as_default_for_extension(self, extension): # real signature unknown; restored from __doc__
        """ set_as_default_for_extension(self, extension:str) -> bool """
        return False

    def set_as_default_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ set_as_default_for_type(self, content_type:str) -> bool """
        return False

    def set_as_last_used_for_type(self, content_type): # real signature unknown; restored from __doc__
        """ set_as_last_used_for_type(self, content_type:str) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_desktop_env(self, desktop_env): # real signature unknown; restored from __doc__
        """ set_desktop_env(desktop_env:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def should_show(self): # real signature unknown; restored from __doc__
        """ should_show(self) -> bool """
        return False

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

    def supports_files(self): # real signature unknown; restored from __doc__
        """ supports_files(self) -> bool """
        return False

    def supports_uris(self): # real signature unknown; restored from __doc__
        """ supports_uris(self) -> bool """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f4b875632b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DesktopAppInfo), '__module__': 'gi.repository.Gio', '__gtype__': <GType GDesktopAppInfo (94269256838736)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_filename': gi.FunctionInfo(new_from_filename), 'new_from_keyfile': gi.FunctionInfo(new_from_keyfile), 'get_implementations': gi.FunctionInfo(get_implementations), 'search': gi.FunctionInfo(search), 'set_desktop_env': gi.FunctionInfo(set_desktop_env), 'get_action_name': gi.FunctionInfo(get_action_name), 'get_boolean': gi.FunctionInfo(get_boolean), 'get_categories': gi.FunctionInfo(get_categories), 'get_filename': gi.FunctionInfo(get_filename), 'get_generic_name': gi.FunctionInfo(get_generic_name), 'get_is_hidden': gi.FunctionInfo(get_is_hidden), 'get_keywords': gi.FunctionInfo(get_keywords), 'get_locale_string': gi.FunctionInfo(get_locale_string), 'get_nodisplay': gi.FunctionInfo(get_nodisplay), 'get_show_in': gi.FunctionInfo(get_show_in), 'get_startup_wm_class': gi.FunctionInfo(get_startup_wm_class), 'get_string': gi.FunctionInfo(get_string), 'get_string_list': gi.FunctionInfo(get_string_list), 'has_key': gi.FunctionInfo(has_key), 'launch_action': gi.FunctionInfo(launch_action), 'launch_uris_as_manager': gi.FunctionInfo(launch_uris_as_manager), 'launch_uris_as_manager_with_fds': gi.FunctionInfo(launch_uris_as_manager_with_fds), 'list_actions': gi.FunctionInfo(list_actions)})"
    __gdoc__ = 'Object GDesktopAppInfo\n\nProperties from GDesktopAppInfo:\n  filename -> gchararray: Filename\n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDesktopAppInfo (94269256838736)>'
    __info__ = ObjectInfo(DesktopAppInfo)


