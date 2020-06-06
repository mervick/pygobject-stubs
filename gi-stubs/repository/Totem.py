# encoding: utf-8
# module gi.repository.Totem
# from /usr/lib64/girepository-1.0/Totem-1.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

GSETTINGS_SCHEMA = 'org.gnome.totem'

_namespace = 'Totem'

_version = '1.0'

__weakref__ = None

# functions

def get_plugin_paths(): # real signature unknown; restored from __doc__
    """ get_plugin_paths() -> list """
    return []

def interface_create_header_button(header, button, icon_name, pack_type): # real signature unknown; restored from __doc__
    """ interface_create_header_button(header:Gtk.Widget, button:Gtk.Widget, icon_name:str, pack_type:Gtk.PackType) -> Gtk.Widget """
    pass

def interface_error(title, reason, parent): # real signature unknown; restored from __doc__
    """ interface_error(title:str, reason:str, parent:Gtk.Window) """
    pass

def interface_error_blocking(title, reason, parent): # real signature unknown; restored from __doc__
    """ interface_error_blocking(title:str, reason:str, parent:Gtk.Window) """
    pass

def interface_error_with_link(title, reason, uri, label, parent): # real signature unknown; restored from __doc__
    """ interface_error_with_link(title:str, reason:str, uri:str, label:str, parent:Gtk.Window) """
    pass

def interface_get_full_path(name): # real signature unknown; restored from __doc__
    """ interface_get_full_path(name:str) -> str """
    return ""

def interface_load(name, fatal, parent=None, user_data=None): # real signature unknown; restored from __doc__
    """ interface_load(name:str, fatal:bool, parent:Gtk.Window=None, user_data=None) -> Gtk.Builder """
    pass

def interface_load_pixbuf(name): # real signature unknown; restored from __doc__
    """ interface_load_pixbuf(name:str) -> GdkPixbuf.Pixbuf """
    pass

def interface_load_with_full_path(filename, fatal, parent=None, user_data=None): # real signature unknown; restored from __doc__
    """ interface_load_with_full_path(filename:str, fatal:bool, parent:Gtk.Window=None, user_data=None) -> Gtk.Builder """
    pass

def plugin_find_file(plugin_name, file): # real signature unknown; restored from __doc__
    """ plugin_find_file(plugin_name:str, file:str) -> str """
    return ""

def plugin_load_interface(plugin_name, name, fatal, parent=None, user_data=None): # real signature unknown; restored from __doc__
    """ plugin_load_interface(plugin_name:str, name:str, fatal:bool, parent:Gtk.Window=None, user_data=None) -> Gtk.Builder """
    pass

def remote_command_quark(): # real signature unknown; restored from __doc__
    """ remote_command_quark() -> int """
    return 0

def remote_setting_quark(): # real signature unknown; restored from __doc__
    """ remote_setting_quark() -> int """
    return 0

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class Object(__gi_repository_Gtk.Application):
    """
    :Constructors:
    
    ::
    
        Object(**properties)
    """
    def action_added(self, action_name): # real signature unknown; restored from __doc__
        """ action_added(self, action_name:str) """
        pass

    def action_enabled_changed(self, action_name, enabled): # real signature unknown; restored from __doc__
        """ action_enabled_changed(self, action_name:str, enabled:bool) """
        pass

    def action_removed(self, action_name): # real signature unknown; restored from __doc__
        """ action_removed(self, action_name:str) """
        pass

    def action_state_changed(self, action_name, state): # real signature unknown; restored from __doc__
        """ action_state_changed(self, action_name:str, state:GLib.Variant) """
        pass

    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) """
        pass

    def activate_action(self, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ activate_action(self, action_name:str, parameter:GLib.Variant=None) """
        pass

    def add_accelerator(self, accelerator, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ add_accelerator(self, accelerator:str, action_name:str, parameter:GLib.Variant=None) """
        pass

    def add_action(self, action): # real signature unknown; restored from __doc__
        """ add_action(self, action:Gio.Action) """
        pass

    def add_action_entries(self, entries, user_data=None): # real signature unknown; restored from __doc__
        """ add_action_entries(self, entries:list, user_data=None) """
        pass

    def add_main_option(self, long_name, short_name, flags, arg, description, arg_description=None): # real signature unknown; restored from __doc__
        """ add_main_option(self, long_name:str, short_name:int, flags:GLib.OptionFlags, arg:GLib.OptionArg, description:str, arg_description:str=None) """
        pass

    def add_main_option_entries(self, entries): # real signature unknown; restored from __doc__
        """ add_main_option_entries(self, entries:list) """
        pass

    def add_option_group(self, group): # real signature unknown; restored from __doc__
        """ add_option_group(self, group:GLib.OptionGroup) """
        pass

    def add_to_playlist(self, uri, display_name, play): # real signature unknown; restored from __doc__
        """ add_to_playlist(self, uri:str, display_name:str, play:bool) """
        pass

    def add_to_view(self, file, title): # real signature unknown; restored from __doc__
        """ add_to_view(self, file:Gio.File, title:str) """
        pass

    def add_window(self, window): # real signature unknown; restored from __doc__
        """ add_window(self, window:Gtk.Window) """
        pass

    def bind_busy_property(self, p_object, property): # real signature unknown; restored from __doc__
        """ bind_busy_property(self, object:GObject.Object, property:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_seek_next(self): # real signature unknown; restored from __doc__
        """ can_seek_next(self) -> bool """
        return False

    def can_seek_previous(self): # real signature unknown; restored from __doc__
        """ can_seek_previous(self) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_action_state(self, action_name, value): # real signature unknown; restored from __doc__
        """ change_action_state(self, action_name:str, value:GLib.Variant) """
        pass

    def clear_playlist(self): # real signature unknown; restored from __doc__
        """ clear_playlist(self) """
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

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) """
        pass

    def do_add_platform_data(self, *args, **kwargs): # real signature unknown
        """ add_platform_data(self, builder:GLib.VariantBuilder) """
        pass

    def do_after_emit(self, *args, **kwargs): # real signature unknown
        """ after_emit(self, platform_data:GLib.Variant) """
        pass

    def do_before_emit(self, *args, **kwargs): # real signature unknown
        """ before_emit(self, platform_data:GLib.Variant) """
        pass

    def do_command_line(self, *args, **kwargs): # real signature unknown
        """ command_line(self, command_line:Gio.ApplicationCommandLine) -> int """
        pass

    def do_dbus_register(self, *args, **kwargs): # real signature unknown
        """ dbus_register(self, connection:Gio.DBusConnection, object_path:str) -> bool """
        pass

    def do_dbus_unregister(self, *args, **kwargs): # real signature unknown
        """ dbus_unregister(self, connection:Gio.DBusConnection, object_path:str) """
        pass

    def do_file_closed(self, *args, **kwargs): # real signature unknown
        """ file_closed(self) """
        pass

    def do_file_has_played(self, *args, **kwargs): # real signature unknown
        """ file_has_played(self, mrl:str) """
        pass

    def do_file_opened(self, *args, **kwargs): # real signature unknown
        """ file_opened(self, mrl:str) """
        pass

    def do_get_text_subtitle(self, *args, **kwargs): # real signature unknown
        """ get_text_subtitle(self, mrl:str) -> str """
        pass

    def do_get_user_agent(self, *args, **kwargs): # real signature unknown
        """ get_user_agent(self, mrl:str) -> str """
        pass

    def do_handle_local_options(self, *args, **kwargs): # real signature unknown
        """ handle_local_options(self, options:GLib.VariantDict) -> int """
        pass

    def do_local_command_line(self, *args, **kwargs): # real signature unknown
        """ local_command_line(self, arguments:list) -> bool, arguments:list, exit_status:int """
        pass

    def do_metadata_updated(self, *args, **kwargs): # real signature unknown
        """ metadata_updated(self, artist:str, title:str, album:str, track_num:int) """
        pass

    def do_name_lost(self, *args, **kwargs): # real signature unknown
        """ name_lost(self) -> bool """
        pass

    def do_open(self, *args, **kwargs): # real signature unknown
        """ open(self, files:list, hint:str) """
        pass

    def do_quit_mainloop(self, *args, **kwargs): # real signature unknown
        """ quit_mainloop(self) """
        pass

    def do_run_mainloop(self, *args, **kwargs): # real signature unknown
        """ run_mainloop(self) """
        pass

    def do_shutdown(self, *args, **kwargs): # real signature unknown
        """ shutdown(self) """
        pass

    def do_startup(self, *args, **kwargs): # real signature unknown
        """ startup(self) """
        pass

    def do_window_added(self, *args, **kwargs): # real signature unknown
        """ window_added(self, window:Gtk.Window) """
        pass

    def do_window_removed(self, *args, **kwargs): # real signature unknown
        """ window_removed(self, window:Gtk.Window) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def empty_menu_section(self, id): # real signature unknown; restored from __doc__
        """ empty_menu_section(self, id:str) """
        pass

    def exit(self): # real signature unknown; restored from __doc__
        """ exit(self) """
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

    def get_accels_for_action(self, detailed_action_name): # real signature unknown; restored from __doc__
        """ get_accels_for_action(self, detailed_action_name:str) -> list """
        return []

    def get_actions_for_accel(self, accel): # real signature unknown; restored from __doc__
        """ get_actions_for_accel(self, accel:str) -> list """
        return []

    def get_action_enabled(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_enabled(self, action_name:str) -> bool """
        return False

    def get_action_parameter_type(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_parameter_type(self, action_name:str) -> GLib.VariantType or None """
        pass

    def get_action_state(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state(self, action_name:str) -> GLib.Variant or None """
        pass

    def get_action_state_hint(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state_hint(self, action_name:str) -> GLib.Variant or None """
        pass

    def get_action_state_type(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state_type(self, action_name:str) -> GLib.VariantType or None """
        pass

    def get_active_window(self): # real signature unknown; restored from __doc__
        """ get_active_window(self) -> Gtk.Window or None """
        pass

    def get_application_id(self): # real signature unknown; restored from __doc__
        """ get_application_id(self) -> str """
        return ""

    def get_app_menu(self): # real signature unknown; restored from __doc__
        """ get_app_menu(self) -> Gio.MenuModel or None """
        pass

    def get_current_mrl(self): # real signature unknown; restored from __doc__
        """ get_current_mrl(self) -> str """
        return ""

    def get_current_time(self): # real signature unknown; restored from __doc__
        """ get_current_time(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dbus_connection(self): # real signature unknown; restored from __doc__
        """ get_dbus_connection(self) -> Gio.DBusConnection """
        pass

    def get_dbus_object_path(self): # real signature unknown; restored from __doc__
        """ get_dbus_object_path(self) -> str """
        return ""

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gio.Application """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.ApplicationFlags """
        pass

    def get_inactivity_timeout(self): # real signature unknown; restored from __doc__
        """ get_inactivity_timeout(self) -> int """
        return 0

    def get_is_busy(self): # real signature unknown; restored from __doc__
        """ get_is_busy(self) -> bool """
        return False

    def get_is_registered(self): # real signature unknown; restored from __doc__
        """ get_is_registered(self) -> bool """
        return False

    def get_is_remote(self): # real signature unknown; restored from __doc__
        """ get_is_remote(self) -> bool """
        return False

    def get_main_window(self): # real signature unknown; restored from __doc__
        """ get_main_window(self) -> Gtk.Window """
        pass

    def get_menubar(self): # real signature unknown; restored from __doc__
        """ get_menubar(self) -> Gio.MenuModel """
        pass

    def get_menu_by_id(self, id): # real signature unknown; restored from __doc__
        """ get_menu_by_id(self, id:str) -> Gio.Menu """
        pass

    def get_menu_section(self, id): # real signature unknown; restored from __doc__
        """ get_menu_section(self, id:str) -> Gio.Menu or None """
        pass

    def get_playlist_length(self): # real signature unknown; restored from __doc__
        """ get_playlist_length(self) -> int """
        return 0

    def get_playlist_pos(self): # real signature unknown; restored from __doc__
        """ get_playlist_pos(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rate(self): # real signature unknown; restored from __doc__
        """ get_rate(self) -> float """
        return 0.0

    def get_resource_base_path(self): # real signature unknown; restored from __doc__
        """ get_resource_base_path(self) -> str or None """
        return ""

    def get_short_title(self): # real signature unknown; restored from __doc__
        """ get_short_title(self) -> str """
        return ""

    def get_supported_content_types(self): # real signature unknown; restored from __doc__
        """ get_supported_content_types() -> list """
        return []

    def get_supported_uri_schemes(self): # real signature unknown; restored from __doc__
        """ get_supported_uri_schemes() -> list """
        return []

    def get_title_at_playlist_pos(self, playlist_index): # real signature unknown; restored from __doc__
        """ get_title_at_playlist_pos(self, playlist_index:int) -> str """
        return ""

    def get_video_widget(self): # real signature unknown; restored from __doc__
        """ get_video_widget(self) -> Gtk.Widget """
        pass

    def get_volume(self): # real signature unknown; restored from __doc__
        """ get_volume(self) -> float """
        return 0.0

    def get_windows(self): # real signature unknown; restored from __doc__
        """ get_windows(self) -> list """
        return []

    def get_window_by_id(self, id): # real signature unknown; restored from __doc__
        """ get_window_by_id(self, id:int) -> Gtk.Window or None """
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

    def has_action(self, action_name): # real signature unknown; restored from __doc__
        """ has_action(self, action_name:str) -> bool """
        return False

    def hold(self): # real signature unknown; restored from __doc__
        """ hold(self) """
        pass

    def id_is_valid(self, application_id): # real signature unknown; restored from __doc__
        """ id_is_valid(application_id:str) -> bool """
        return False

    def inhibit(self, window=None, flags, reason=None): # real signature unknown; restored from __doc__
        """ inhibit(self, window:Gtk.Window=None, flags:Gtk.ApplicationInhibitFlags, reason:str=None) -> int """
        return 0

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

    def is_fullscreen(self): # real signature unknown; restored from __doc__
        """ is_fullscreen(self) -> bool """
        return False

    def is_inhibited(self, flags): # real signature unknown; restored from __doc__
        """ is_inhibited(self, flags:Gtk.ApplicationInhibitFlags) -> bool """
        return False

    def is_paused(self): # real signature unknown; restored from __doc__
        """ is_paused(self) -> bool """
        return False

    def is_playing(self): # real signature unknown; restored from __doc__
        """ is_playing(self) -> bool """
        return False

    def is_seekable(self): # real signature unknown; restored from __doc__
        """ is_seekable(self) -> bool """
        return False

    def list_actions(self): # real signature unknown; restored from __doc__
        """ list_actions(self) -> list """
        return []

    def list_action_descriptions(self): # real signature unknown; restored from __doc__
        """ list_action_descriptions(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lookup_action(self, action_name): # real signature unknown; restored from __doc__
        """ lookup_action(self, action_name:str) -> Gio.Action """
        pass

    def mark_busy(self): # real signature unknown; restored from __doc__
        """ mark_busy(self) """
        pass

    def new(self, application_id=None, flags): # real signature unknown; restored from __doc__
        """ new(application_id:str=None, flags:Gio.ApplicationFlags) -> Gtk.Application """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def next_angle(self): # real signature unknown; restored from __doc__
        """ next_angle(self) """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open(self, files, hint): # real signature unknown; restored from __doc__
        """ open(self, files:list, hint:str) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) """
        pass

    def play_pause(self): # real signature unknown; restored from __doc__
        """ play_pause(self) """
        pass

    def prefers_app_menu(self): # real signature unknown; restored from __doc__
        """ prefers_app_menu(self) -> bool """
        return False

    def query_action(self, action_name): # real signature unknown; restored from __doc__
        """ query_action(self, action_name:str) -> bool, enabled:bool, parameter_type:GLib.VariantType, state_type:GLib.VariantType, state_hint:GLib.Variant, state:GLib.Variant """
        return False

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self, cancellable=None): # real signature unknown; restored from __doc__
        """ register(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def remote_command(self, cmd, url): # real signature unknown; restored from __doc__
        """ remote_command(self, cmd:Totem.RemoteCommand, url:str) """
        pass

    def remote_get_setting(self, setting): # real signature unknown; restored from __doc__
        """ remote_get_setting(self, setting:Totem.RemoteSetting) -> bool """
        return False

    def remote_set_setting(self, setting, value): # real signature unknown; restored from __doc__
        """ remote_set_setting(self, setting:Totem.RemoteSetting, value:bool) """
        pass

    def remove_accelerator(self, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ remove_accelerator(self, action_name:str, parameter:GLib.Variant=None) """
        pass

    def remove_action(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action(self, action_name:str) """
        pass

    def remove_window(self, window): # real signature unknown; restored from __doc__
        """ remove_window(self, window:Gtk.Window) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def seek_next(self): # real signature unknown; restored from __doc__
        """ seek_next(self) """
        pass

    def seek_previous(self): # real signature unknown; restored from __doc__
        """ seek_previous(self) """
        pass

    def seek_relative(self, offset, accurate): # real signature unknown; restored from __doc__
        """ seek_relative(self, offset:int, accurate:bool) """
        pass

    def seek_time(self, msec, accurate): # real signature unknown; restored from __doc__
        """ seek_time(self, msec:int, accurate:bool) """
        pass

    def send_notification(self, id=None, notification): # real signature unknown; restored from __doc__
        """ send_notification(self, id:str=None, notification:Gio.Notification) """
        pass

    def set_accels_for_action(self, detailed_action_name, accels): # real signature unknown; restored from __doc__
        """ set_accels_for_action(self, detailed_action_name:str, accels:list) """
        pass

    def set_action_group(self, action_group=None): # real signature unknown; restored from __doc__
        """ set_action_group(self, action_group:Gio.ActionGroup=None) """
        pass

    def set_application_id(self, application_id=None): # real signature unknown; restored from __doc__
        """ set_application_id(self, application_id:str=None) """
        pass

    def set_app_menu(self, app_menu=None): # real signature unknown; restored from __doc__
        """ set_app_menu(self, app_menu:Gio.MenuModel=None) """
        pass

    def set_current_subtitle(self, subtitle_uri): # real signature unknown; restored from __doc__
        """ set_current_subtitle(self, subtitle_uri:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default(self): # real signature unknown; restored from __doc__
        """ set_default(self) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Gio.ApplicationFlags) """
        pass

    def set_inactivity_timeout(self, inactivity_timeout): # real signature unknown; restored from __doc__
        """ set_inactivity_timeout(self, inactivity_timeout:int) """
        pass

    def set_menubar(self, menubar=None): # real signature unknown; restored from __doc__
        """ set_menubar(self, menubar:Gio.MenuModel=None) """
        pass

    def set_option_context_description(self, description=None): # real signature unknown; restored from __doc__
        """ set_option_context_description(self, description:str=None) """
        pass

    def set_option_context_parameter_string(self, parameter_string=None): # real signature unknown; restored from __doc__
        """ set_option_context_parameter_string(self, parameter_string:str=None) """
        pass

    def set_option_context_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_option_context_summary(self, summary:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rate(self, rate): # real signature unknown; restored from __doc__
        """ set_rate(self, rate:float) -> bool """
        return False

    def set_resource_base_path(self, resource_path=None): # real signature unknown; restored from __doc__
        """ set_resource_base_path(self, resource_path:str=None) """
        pass

    def set_volume(self, volume): # real signature unknown; restored from __doc__
        """ set_volume(self, volume:float) """
        pass

    def show_error(self, title, reason): # real signature unknown; restored from __doc__
        """ show_error(self, title:str, reason:str) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
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

    def unbind_busy_property(self, p_object, property): # real signature unknown; restored from __doc__
        """ unbind_busy_property(self, object:GObject.Object, property:str) """
        pass

    def uninhibit(self, cookie): # real signature unknown; restored from __doc__
        """ uninhibit(self, cookie:int) """
        pass

    def unmark_busy(self): # real signature unknown; restored from __doc__
        """ unmark_busy(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def withdraw_notification(self, id): # real signature unknown; restored from __doc__
        """ withdraw_notification(self, id:str) """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f26aa6f2dc0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Object), '__module__': 'gi.repository.Totem', '__gtype__': <GType TotemObject (94711330071232)>, '__doc__': None, '__gsignals__': {}, 'get_supported_content_types': gi.FunctionInfo(get_supported_content_types), 'get_supported_uri_schemes': gi.FunctionInfo(get_supported_uri_schemes), 'add_to_playlist': gi.FunctionInfo(add_to_playlist), 'add_to_view': gi.FunctionInfo(add_to_view), 'can_seek_next': gi.FunctionInfo(can_seek_next), 'can_seek_previous': gi.FunctionInfo(can_seek_previous), 'clear_playlist': gi.FunctionInfo(clear_playlist), 'empty_menu_section': gi.FunctionInfo(empty_menu_section), 'exit': gi.FunctionInfo(exit), 'get_current_mrl': gi.FunctionInfo(get_current_mrl), 'get_current_time': gi.FunctionInfo(get_current_time), 'get_main_window': gi.FunctionInfo(get_main_window), 'get_menu_section': gi.FunctionInfo(get_menu_section), 'get_playlist_length': gi.FunctionInfo(get_playlist_length), 'get_playlist_pos': gi.FunctionInfo(get_playlist_pos), 'get_rate': gi.FunctionInfo(get_rate), 'get_short_title': gi.FunctionInfo(get_short_title), 'get_title_at_playlist_pos': gi.FunctionInfo(get_title_at_playlist_pos), 'get_video_widget': gi.FunctionInfo(get_video_widget), 'get_volume': gi.FunctionInfo(get_volume), 'is_fullscreen': gi.FunctionInfo(is_fullscreen), 'is_paused': gi.FunctionInfo(is_paused), 'is_playing': gi.FunctionInfo(is_playing), 'is_seekable': gi.FunctionInfo(is_seekable), 'next_angle': gi.FunctionInfo(next_angle), 'pause': gi.FunctionInfo(pause), 'play': gi.FunctionInfo(play), 'play_pause': gi.FunctionInfo(play_pause), 'remote_command': gi.FunctionInfo(remote_command), 'remote_get_setting': gi.FunctionInfo(remote_get_setting), 'remote_set_setting': gi.FunctionInfo(remote_set_setting), 'seek_next': gi.FunctionInfo(seek_next), 'seek_previous': gi.FunctionInfo(seek_previous), 'seek_relative': gi.FunctionInfo(seek_relative), 'seek_time': gi.FunctionInfo(seek_time), 'set_current_subtitle': gi.FunctionInfo(set_current_subtitle), 'set_rate': gi.FunctionInfo(set_rate), 'set_volume': gi.FunctionInfo(set_volume), 'show_error': gi.FunctionInfo(show_error), 'stop': gi.FunctionInfo(stop), 'do_file_closed': gi.VFuncInfo(file_closed), 'do_file_has_played': gi.VFuncInfo(file_has_played), 'do_file_opened': gi.VFuncInfo(file_opened), 'do_get_text_subtitle': gi.VFuncInfo(get_text_subtitle), 'do_get_user_agent': gi.VFuncInfo(get_user_agent), 'do_metadata_updated': gi.VFuncInfo(metadata_updated)})"
    __gdoc__ = "Object TotemObject\n\nSignals from TotemObject:\n  file-opened (gchararray)\n  file-has-played (gchararray)\n  file-closed ()\n  metadata-updated (gchararray, gchararray, gchararray, guint)\n  get-user-agent (gchararray) -> gchararray\n  get-text-subtitle (gchararray) -> gchararray\n\nProperties from TotemObject:\n  fullscreen -> gboolean: Fullscreen?\n    Whether Totem is in fullscreen mode.\n  playing -> gboolean: Playing?\n    Whether Totem is currently playing a file.\n  stream-length -> gint64: Stream length\n    The length of the current stream.\n  seekable -> gboolean: Seekable?\n    Whether the current stream is seekable.\n  current-time -> gint64: Current time\n    The player's position (time) in the current stream.\n  current-mrl -> gchararray: Current MRL\n    The MRL of the current stream.\n  current-content-type -> gchararray: Current stream's content-type\n    Current stream's content-type.\n  current-display-name -> gchararray: Current stream's display name\n    Current stream's display name.\n  main-page -> gchararray: Current main page\n    Current main page.\n\nSignals from GActionGroup:\n  action-added (gchararray)\n  action-removed (gchararray)\n  action-enabled-changed (gchararray, gboolean)\n  action-state-changed (gchararray, GVariant)\n\nSignals from GtkApplication:\n  window-added (GtkWindow)\n  window-removed (GtkWindow)\n  query-end ()\n\nProperties from GtkApplication:\n  register-session -> gboolean: Register session\n    Register with the session manager\n  screensaver-active -> gboolean: Screensaver Active\n    Whether the screensaver is active\n  app-menu -> GMenuModel: Application menu\n    The GMenuModel for the application menu\n  menubar -> GMenuModel: Menubar\n    The GMenuModel for the menubar\n  active-window -> GtkWindow: Active window\n    The window which most recently had focus\n\nSignals from GActionGroup:\n  action-added (gchararray)\n  action-removed (gchararray)\n  action-enabled-changed (gchararray, gboolean)\n  action-state-changed (gchararray, GVariant)\n\nSignals from GApplication:\n  activate ()\n  startup ()\n  shutdown ()\n  open (gpointer, gint, gchararray)\n  command-line (GApplicationCommandLine) -> gint\n  handle-local-options (GVariantDict) -> gint\n  name-lost () -> gboolean\n\nProperties from GApplication:\n  application-id -> gchararray: Application identifier\n    The unique identifier for the application\n  flags -> GApplicationFlags: Application flags\n    Flags specifying the behaviour of the application\n  resource-base-path -> gchararray: Resource base path\n    The base resource path for the application\n  is-registered -> gboolean: Is registered\n    If g_application_register() has been called\n  is-remote -> gboolean: Is remote\n    If this application instance is remote\n  inactivity-timeout -> guint: Inactivity timeout\n    Time (ms) to stay alive after becoming idle\n  action-group -> GActionGroup: Action group\n    The group of actions that the application exports\n  is-busy -> gboolean: Is busy\n    If this application is currently marked busy\n\nSignals from GActionGroup:\n  action-added (gchararray)\n  action-removed (gchararray)\n  action-enabled-changed (gchararray, gboolean)\n  action-state-changed (gchararray, GVariant)\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType TotemObject (94711330071232)>'
    __info__ = ObjectInfo(Object)


class ObjectClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ObjectClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    file_closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_has_played = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text_subtitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_user_agent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata_updated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ObjectClass), '__module__': 'gi.repository.Totem', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ObjectClass' objects>, '__weakref__': <attribute '__weakref__' of 'ObjectClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f26aa67d860>, 'file_opened': <property object at 0x7f26aa67d8b0>, 'file_closed': <property object at 0x7f26aa67d9a0>, 'file_has_played': <property object at 0x7f26aa67da90>, 'metadata_updated': <property object at 0x7f26aa67dbd0>, 'get_user_agent': <property object at 0x7f26aa67dcc0>, 'get_text_subtitle': <property object at 0x7f26aa67de00>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ObjectClass)


class RemoteCommand(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def quark(self): # real signature unknown; restored from __doc__
        """ quark() -> int """
        return 0

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DOWN = 17
    DVD_MENU = 21
    EJECT = 24
    ENQUEUE = 13
    FULLSCREEN = 11
    LEFT = 18
    MUTE = 26
    NEXT = 5
    PAUSE = 2
    PLAY = 1
    PLAY_DVD = 25
    PLAY_PAUSE = 4
    PREVIOUS = 6
    QUIT = 12
    REPLACE = 14
    RIGHT = 19
    SEEK_BACKWARD = 8
    SEEK_FORWARD = 7
    SELECT = 20
    SHOW = 15
    STOP = 3
    TOGGLE_ASPECT_RATIO = 27
    UNKNOWN = 0
    UP = 16
    VOLUME_DOWN = 10
    VOLUME_UP = 9
    ZOOM_DOWN = 23
    ZOOM_UP = 22
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Totem', '__dict__': <attribute '__dict__' of 'RemoteCommand' objects>, '__doc__': None, '__gtype__': <GType TotemRemoteCommand (94711330081952)>, '__enum_values__': {0: <enum TOTEM_REMOTE_COMMAND_UNKNOWN of type Totem.RemoteCommand>, 1: <enum TOTEM_REMOTE_COMMAND_PLAY of type Totem.RemoteCommand>, 2: <enum TOTEM_REMOTE_COMMAND_PAUSE of type Totem.RemoteCommand>, 3: <enum TOTEM_REMOTE_COMMAND_STOP of type Totem.RemoteCommand>, 4: <enum TOTEM_REMOTE_COMMAND_PLAYPAUSE of type Totem.RemoteCommand>, 5: <enum TOTEM_REMOTE_COMMAND_NEXT of type Totem.RemoteCommand>, 6: <enum TOTEM_REMOTE_COMMAND_PREVIOUS of type Totem.RemoteCommand>, 7: <enum TOTEM_REMOTE_COMMAND_SEEK_FORWARD of type Totem.RemoteCommand>, 8: <enum TOTEM_REMOTE_COMMAND_SEEK_BACKWARD of type Totem.RemoteCommand>, 9: <enum TOTEM_REMOTE_COMMAND_VOLUME_UP of type Totem.RemoteCommand>, 10: <enum TOTEM_REMOTE_COMMAND_VOLUME_DOWN of type Totem.RemoteCommand>, 11: <enum TOTEM_REMOTE_COMMAND_FULLSCREEN of type Totem.RemoteCommand>, 12: <enum TOTEM_REMOTE_COMMAND_QUIT of type Totem.RemoteCommand>, 13: <enum TOTEM_REMOTE_COMMAND_ENQUEUE of type Totem.RemoteCommand>, 14: <enum TOTEM_REMOTE_COMMAND_REPLACE of type Totem.RemoteCommand>, 15: <enum TOTEM_REMOTE_COMMAND_SHOW of type Totem.RemoteCommand>, 16: <enum TOTEM_REMOTE_COMMAND_UP of type Totem.RemoteCommand>, 17: <enum TOTEM_REMOTE_COMMAND_DOWN of type Totem.RemoteCommand>, 18: <enum TOTEM_REMOTE_COMMAND_LEFT of type Totem.RemoteCommand>, 19: <enum TOTEM_REMOTE_COMMAND_RIGHT of type Totem.RemoteCommand>, 20: <enum TOTEM_REMOTE_COMMAND_SELECT of type Totem.RemoteCommand>, 21: <enum TOTEM_REMOTE_COMMAND_DVD_MENU of type Totem.RemoteCommand>, 22: <enum TOTEM_REMOTE_COMMAND_ZOOM_UP of type Totem.RemoteCommand>, 23: <enum TOTEM_REMOTE_COMMAND_ZOOM_DOWN of type Totem.RemoteCommand>, 24: <enum TOTEM_REMOTE_COMMAND_EJECT of type Totem.RemoteCommand>, 25: <enum TOTEM_REMOTE_COMMAND_PLAY_DVD of type Totem.RemoteCommand>, 26: <enum TOTEM_REMOTE_COMMAND_MUTE of type Totem.RemoteCommand>, 27: <enum TOTEM_REMOTE_COMMAND_TOGGLE_ASPECT of type Totem.RemoteCommand>}, '__info__': gi.EnumInfo(RemoteCommand), 'UNKNOWN': <enum TOTEM_REMOTE_COMMAND_UNKNOWN of type Totem.RemoteCommand>, 'PLAY': <enum TOTEM_REMOTE_COMMAND_PLAY of type Totem.RemoteCommand>, 'PAUSE': <enum TOTEM_REMOTE_COMMAND_PAUSE of type Totem.RemoteCommand>, 'STOP': <enum TOTEM_REMOTE_COMMAND_STOP of type Totem.RemoteCommand>, 'PLAY_PAUSE': <enum TOTEM_REMOTE_COMMAND_PLAYPAUSE of type Totem.RemoteCommand>, 'NEXT': <enum TOTEM_REMOTE_COMMAND_NEXT of type Totem.RemoteCommand>, 'PREVIOUS': <enum TOTEM_REMOTE_COMMAND_PREVIOUS of type Totem.RemoteCommand>, 'SEEK_FORWARD': <enum TOTEM_REMOTE_COMMAND_SEEK_FORWARD of type Totem.RemoteCommand>, 'SEEK_BACKWARD': <enum TOTEM_REMOTE_COMMAND_SEEK_BACKWARD of type Totem.RemoteCommand>, 'VOLUME_UP': <enum TOTEM_REMOTE_COMMAND_VOLUME_UP of type Totem.RemoteCommand>, 'VOLUME_DOWN': <enum TOTEM_REMOTE_COMMAND_VOLUME_DOWN of type Totem.RemoteCommand>, 'FULLSCREEN': <enum TOTEM_REMOTE_COMMAND_FULLSCREEN of type Totem.RemoteCommand>, 'QUIT': <enum TOTEM_REMOTE_COMMAND_QUIT of type Totem.RemoteCommand>, 'ENQUEUE': <enum TOTEM_REMOTE_COMMAND_ENQUEUE of type Totem.RemoteCommand>, 'REPLACE': <enum TOTEM_REMOTE_COMMAND_REPLACE of type Totem.RemoteCommand>, 'SHOW': <enum TOTEM_REMOTE_COMMAND_SHOW of type Totem.RemoteCommand>, 'UP': <enum TOTEM_REMOTE_COMMAND_UP of type Totem.RemoteCommand>, 'DOWN': <enum TOTEM_REMOTE_COMMAND_DOWN of type Totem.RemoteCommand>, 'LEFT': <enum TOTEM_REMOTE_COMMAND_LEFT of type Totem.RemoteCommand>, 'RIGHT': <enum TOTEM_REMOTE_COMMAND_RIGHT of type Totem.RemoteCommand>, 'SELECT': <enum TOTEM_REMOTE_COMMAND_SELECT of type Totem.RemoteCommand>, 'DVD_MENU': <enum TOTEM_REMOTE_COMMAND_DVD_MENU of type Totem.RemoteCommand>, 'ZOOM_UP': <enum TOTEM_REMOTE_COMMAND_ZOOM_UP of type Totem.RemoteCommand>, 'ZOOM_DOWN': <enum TOTEM_REMOTE_COMMAND_ZOOM_DOWN of type Totem.RemoteCommand>, 'EJECT': <enum TOTEM_REMOTE_COMMAND_EJECT of type Totem.RemoteCommand>, 'PLAY_DVD': <enum TOTEM_REMOTE_COMMAND_PLAY_DVD of type Totem.RemoteCommand>, 'MUTE': <enum TOTEM_REMOTE_COMMAND_MUTE of type Totem.RemoteCommand>, 'TOGGLE_ASPECT_RATIO': <enum TOTEM_REMOTE_COMMAND_TOGGLE_ASPECT of type Totem.RemoteCommand>, 'quark': gi.FunctionInfo(quark)})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
    }
    __gtype__ = None # (!) real value is '<GType TotemRemoteCommand (94711330081952)>'
    __info__ = gi.EnumInfo(RemoteCommand)


class RemoteSetting(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def quark(self): # real signature unknown; restored from __doc__
        """ quark() -> int """
        return 0

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    REPEAT = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Totem', '__dict__': <attribute '__dict__' of 'RemoteSetting' objects>, '__doc__': None, '__gtype__': <GType TotemRemoteSetting (94711330091680)>, '__enum_values__': {0: <enum TOTEM_REMOTE_SETTING_REPEAT of type Totem.RemoteSetting>}, '__info__': gi.EnumInfo(RemoteSetting), 'REPEAT': <enum TOTEM_REMOTE_SETTING_REPEAT of type Totem.RemoteSetting>, 'quark': gi.FunctionInfo(quark)})"
    __enum_values__ = {
        0: 0,
    }
    __gtype__ = None # (!) real value is '<GType TotemRemoteSetting (94711330091680)>'
    __info__ = gi.EnumInfo(RemoteSetting)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f26abab91f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f26abab9280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f26abab9310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f26abab93a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f26ac6f5d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Totem-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Totem', loader=<gi.importer.DynamicImporter object at 0x7f26ac6f5d00>)"

