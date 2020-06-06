# encoding: utf-8
# module gi.repository.WebKit2
# from /usr/lib64/girepository-1.0/WebKit2-4.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Settings(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Settings(**properties)
        new() -> WebKit2.Settings
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

    def font_size_to_pixels(self, points): # real signature unknown; restored from __doc__
        """ font_size_to_pixels(points:int) -> int """
        return 0

    def font_size_to_points(self, pixels): # real signature unknown; restored from __doc__
        """ font_size_to_points(pixels:int) -> int """
        return 0

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

    def get_allow_file_access_from_file_urls(self): # real signature unknown; restored from __doc__
        """ get_allow_file_access_from_file_urls(self) -> bool """
        return False

    def get_allow_modal_dialogs(self): # real signature unknown; restored from __doc__
        """ get_allow_modal_dialogs(self) -> bool """
        return False

    def get_allow_top_navigation_to_data_urls(self): # real signature unknown; restored from __doc__
        """ get_allow_top_navigation_to_data_urls(self) -> bool """
        return False

    def get_allow_universal_access_from_file_urls(self): # real signature unknown; restored from __doc__
        """ get_allow_universal_access_from_file_urls(self) -> bool """
        return False

    def get_auto_load_images(self): # real signature unknown; restored from __doc__
        """ get_auto_load_images(self) -> bool """
        return False

    def get_cursive_font_family(self): # real signature unknown; restored from __doc__
        """ get_cursive_font_family(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_charset(self): # real signature unknown; restored from __doc__
        """ get_default_charset(self) -> str """
        return ""

    def get_default_font_family(self): # real signature unknown; restored from __doc__
        """ get_default_font_family(self) -> str """
        return ""

    def get_default_font_size(self): # real signature unknown; restored from __doc__
        """ get_default_font_size(self) -> int """
        return 0

    def get_default_monospace_font_size(self): # real signature unknown; restored from __doc__
        """ get_default_monospace_font_size(self) -> int """
        return 0

    def get_draw_compositing_indicators(self): # real signature unknown; restored from __doc__
        """ get_draw_compositing_indicators(self) -> bool """
        return False

    def get_enable_accelerated_2d_canvas(self): # real signature unknown; restored from __doc__
        """ get_enable_accelerated_2d_canvas(self) -> bool """
        return False

    def get_enable_back_forward_navigation_gestures(self): # real signature unknown; restored from __doc__
        """ get_enable_back_forward_navigation_gestures(self) -> bool """
        return False

    def get_enable_caret_browsing(self): # real signature unknown; restored from __doc__
        """ get_enable_caret_browsing(self) -> bool """
        return False

    def get_enable_developer_extras(self): # real signature unknown; restored from __doc__
        """ get_enable_developer_extras(self) -> bool """
        return False

    def get_enable_dns_prefetching(self): # real signature unknown; restored from __doc__
        """ get_enable_dns_prefetching(self) -> bool """
        return False

    def get_enable_encrypted_media(self): # real signature unknown; restored from __doc__
        """ get_enable_encrypted_media(self) -> bool """
        return False

    def get_enable_frame_flattening(self): # real signature unknown; restored from __doc__
        """ get_enable_frame_flattening(self) -> bool """
        return False

    def get_enable_fullscreen(self): # real signature unknown; restored from __doc__
        """ get_enable_fullscreen(self) -> bool """
        return False

    def get_enable_html5_database(self): # real signature unknown; restored from __doc__
        """ get_enable_html5_database(self) -> bool """
        return False

    def get_enable_html5_local_storage(self): # real signature unknown; restored from __doc__
        """ get_enable_html5_local_storage(self) -> bool """
        return False

    def get_enable_hyperlink_auditing(self): # real signature unknown; restored from __doc__
        """ get_enable_hyperlink_auditing(self) -> bool """
        return False

    def get_enable_java(self): # real signature unknown; restored from __doc__
        """ get_enable_java(self) -> bool """
        return False

    def get_enable_javascript(self): # real signature unknown; restored from __doc__
        """ get_enable_javascript(self) -> bool """
        return False

    def get_enable_javascript_markup(self): # real signature unknown; restored from __doc__
        """ get_enable_javascript_markup(self) -> bool """
        return False

    def get_enable_media(self): # real signature unknown; restored from __doc__
        """ get_enable_media(self) -> bool """
        return False

    def get_enable_mediasource(self): # real signature unknown; restored from __doc__
        """ get_enable_mediasource(self) -> bool """
        return False

    def get_enable_media_capabilities(self): # real signature unknown; restored from __doc__
        """ get_enable_media_capabilities(self) -> bool """
        return False

    def get_enable_media_stream(self): # real signature unknown; restored from __doc__
        """ get_enable_media_stream(self) -> bool """
        return False

    def get_enable_mock_capture_devices(self): # real signature unknown; restored from __doc__
        """ get_enable_mock_capture_devices(self) -> bool """
        return False

    def get_enable_offline_web_application_cache(self): # real signature unknown; restored from __doc__
        """ get_enable_offline_web_application_cache(self) -> bool """
        return False

    def get_enable_page_cache(self): # real signature unknown; restored from __doc__
        """ get_enable_page_cache(self) -> bool """
        return False

    def get_enable_plugins(self): # real signature unknown; restored from __doc__
        """ get_enable_plugins(self) -> bool """
        return False

    def get_enable_private_browsing(self): # real signature unknown; restored from __doc__
        """ get_enable_private_browsing(self) -> bool """
        return False

    def get_enable_resizable_text_areas(self): # real signature unknown; restored from __doc__
        """ get_enable_resizable_text_areas(self) -> bool """
        return False

    def get_enable_site_specific_quirks(self): # real signature unknown; restored from __doc__
        """ get_enable_site_specific_quirks(self) -> bool """
        return False

    def get_enable_smooth_scrolling(self): # real signature unknown; restored from __doc__
        """ get_enable_smooth_scrolling(self) -> bool """
        return False

    def get_enable_spatial_navigation(self): # real signature unknown; restored from __doc__
        """ get_enable_spatial_navigation(self) -> bool """
        return False

    def get_enable_tabs_to_links(self): # real signature unknown; restored from __doc__
        """ get_enable_tabs_to_links(self) -> bool """
        return False

    def get_enable_webaudio(self): # real signature unknown; restored from __doc__
        """ get_enable_webaudio(self) -> bool """
        return False

    def get_enable_webgl(self): # real signature unknown; restored from __doc__
        """ get_enable_webgl(self) -> bool """
        return False

    def get_enable_write_console_messages_to_stdout(self): # real signature unknown; restored from __doc__
        """ get_enable_write_console_messages_to_stdout(self) -> bool """
        return False

    def get_enable_xss_auditor(self): # real signature unknown; restored from __doc__
        """ get_enable_xss_auditor(self) -> bool """
        return False

    def get_fantasy_font_family(self): # real signature unknown; restored from __doc__
        """ get_fantasy_font_family(self) -> str """
        return ""

    def get_hardware_acceleration_policy(self): # real signature unknown; restored from __doc__
        """ get_hardware_acceleration_policy(self) -> WebKit2.HardwareAccelerationPolicy """
        pass

    def get_javascript_can_access_clipboard(self): # real signature unknown; restored from __doc__
        """ get_javascript_can_access_clipboard(self) -> bool """
        return False

    def get_javascript_can_open_windows_automatically(self): # real signature unknown; restored from __doc__
        """ get_javascript_can_open_windows_automatically(self) -> bool """
        return False

    def get_load_icons_ignoring_image_load_setting(self): # real signature unknown; restored from __doc__
        """ get_load_icons_ignoring_image_load_setting(self) -> bool """
        return False

    def get_media_playback_allows_inline(self): # real signature unknown; restored from __doc__
        """ get_media_playback_allows_inline(self) -> bool """
        return False

    def get_media_playback_requires_user_gesture(self): # real signature unknown; restored from __doc__
        """ get_media_playback_requires_user_gesture(self) -> bool """
        return False

    def get_minimum_font_size(self): # real signature unknown; restored from __doc__
        """ get_minimum_font_size(self) -> int """
        return 0

    def get_monospace_font_family(self): # real signature unknown; restored from __doc__
        """ get_monospace_font_family(self) -> str """
        return ""

    def get_pictograph_font_family(self): # real signature unknown; restored from __doc__
        """ get_pictograph_font_family(self) -> str """
        return ""

    def get_print_backgrounds(self): # real signature unknown; restored from __doc__
        """ get_print_backgrounds(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sans_serif_font_family(self): # real signature unknown; restored from __doc__
        """ get_sans_serif_font_family(self) -> str """
        return ""

    def get_serif_font_family(self): # real signature unknown; restored from __doc__
        """ get_serif_font_family(self) -> str """
        return ""

    def get_user_agent(self): # real signature unknown; restored from __doc__
        """ get_user_agent(self) -> str """
        return ""

    def get_zoom_text_only(self): # real signature unknown; restored from __doc__
        """ get_zoom_text_only(self) -> bool """
        return False

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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> WebKit2.Settings """
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

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_allow_file_access_from_file_urls(self, allowed): # real signature unknown; restored from __doc__
        """ set_allow_file_access_from_file_urls(self, allowed:bool) """
        pass

    def set_allow_modal_dialogs(self, allowed): # real signature unknown; restored from __doc__
        """ set_allow_modal_dialogs(self, allowed:bool) """
        pass

    def set_allow_top_navigation_to_data_urls(self, allowed): # real signature unknown; restored from __doc__
        """ set_allow_top_navigation_to_data_urls(self, allowed:bool) """
        pass

    def set_allow_universal_access_from_file_urls(self, allowed): # real signature unknown; restored from __doc__
        """ set_allow_universal_access_from_file_urls(self, allowed:bool) """
        pass

    def set_auto_load_images(self, enabled): # real signature unknown; restored from __doc__
        """ set_auto_load_images(self, enabled:bool) """
        pass

    def set_cursive_font_family(self, cursive_font_family): # real signature unknown; restored from __doc__
        """ set_cursive_font_family(self, cursive_font_family:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_charset(self, default_charset): # real signature unknown; restored from __doc__
        """ set_default_charset(self, default_charset:str) """
        pass

    def set_default_font_family(self, default_font_family): # real signature unknown; restored from __doc__
        """ set_default_font_family(self, default_font_family:str) """
        pass

    def set_default_font_size(self, font_size): # real signature unknown; restored from __doc__
        """ set_default_font_size(self, font_size:int) """
        pass

    def set_default_monospace_font_size(self, font_size): # real signature unknown; restored from __doc__
        """ set_default_monospace_font_size(self, font_size:int) """
        pass

    def set_draw_compositing_indicators(self, enabled): # real signature unknown; restored from __doc__
        """ set_draw_compositing_indicators(self, enabled:bool) """
        pass

    def set_enable_accelerated_2d_canvas(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_accelerated_2d_canvas(self, enabled:bool) """
        pass

    def set_enable_back_forward_navigation_gestures(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_back_forward_navigation_gestures(self, enabled:bool) """
        pass

    def set_enable_caret_browsing(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_caret_browsing(self, enabled:bool) """
        pass

    def set_enable_developer_extras(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_developer_extras(self, enabled:bool) """
        pass

    def set_enable_dns_prefetching(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_dns_prefetching(self, enabled:bool) """
        pass

    def set_enable_encrypted_media(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_encrypted_media(self, enabled:bool) """
        pass

    def set_enable_frame_flattening(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_frame_flattening(self, enabled:bool) """
        pass

    def set_enable_fullscreen(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_fullscreen(self, enabled:bool) """
        pass

    def set_enable_html5_database(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_html5_database(self, enabled:bool) """
        pass

    def set_enable_html5_local_storage(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_html5_local_storage(self, enabled:bool) """
        pass

    def set_enable_hyperlink_auditing(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_hyperlink_auditing(self, enabled:bool) """
        pass

    def set_enable_java(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_java(self, enabled:bool) """
        pass

    def set_enable_javascript(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_javascript(self, enabled:bool) """
        pass

    def set_enable_javascript_markup(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_javascript_markup(self, enabled:bool) """
        pass

    def set_enable_media(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_media(self, enabled:bool) """
        pass

    def set_enable_mediasource(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_mediasource(self, enabled:bool) """
        pass

    def set_enable_media_capabilities(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_media_capabilities(self, enabled:bool) """
        pass

    def set_enable_media_stream(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_media_stream(self, enabled:bool) """
        pass

    def set_enable_mock_capture_devices(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_mock_capture_devices(self, enabled:bool) """
        pass

    def set_enable_offline_web_application_cache(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_offline_web_application_cache(self, enabled:bool) """
        pass

    def set_enable_page_cache(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_page_cache(self, enabled:bool) """
        pass

    def set_enable_plugins(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_plugins(self, enabled:bool) """
        pass

    def set_enable_private_browsing(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_private_browsing(self, enabled:bool) """
        pass

    def set_enable_resizable_text_areas(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_resizable_text_areas(self, enabled:bool) """
        pass

    def set_enable_site_specific_quirks(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_site_specific_quirks(self, enabled:bool) """
        pass

    def set_enable_smooth_scrolling(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_smooth_scrolling(self, enabled:bool) """
        pass

    def set_enable_spatial_navigation(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_spatial_navigation(self, enabled:bool) """
        pass

    def set_enable_tabs_to_links(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_tabs_to_links(self, enabled:bool) """
        pass

    def set_enable_webaudio(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_webaudio(self, enabled:bool) """
        pass

    def set_enable_webgl(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_webgl(self, enabled:bool) """
        pass

    def set_enable_write_console_messages_to_stdout(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_write_console_messages_to_stdout(self, enabled:bool) """
        pass

    def set_enable_xss_auditor(self, enabled): # real signature unknown; restored from __doc__
        """ set_enable_xss_auditor(self, enabled:bool) """
        pass

    def set_fantasy_font_family(self, fantasy_font_family): # real signature unknown; restored from __doc__
        """ set_fantasy_font_family(self, fantasy_font_family:str) """
        pass

    def set_hardware_acceleration_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_hardware_acceleration_policy(self, policy:WebKit2.HardwareAccelerationPolicy) """
        pass

    def set_javascript_can_access_clipboard(self, enabled): # real signature unknown; restored from __doc__
        """ set_javascript_can_access_clipboard(self, enabled:bool) """
        pass

    def set_javascript_can_open_windows_automatically(self, enabled): # real signature unknown; restored from __doc__
        """ set_javascript_can_open_windows_automatically(self, enabled:bool) """
        pass

    def set_load_icons_ignoring_image_load_setting(self, enabled): # real signature unknown; restored from __doc__
        """ set_load_icons_ignoring_image_load_setting(self, enabled:bool) """
        pass

    def set_media_playback_allows_inline(self, enabled): # real signature unknown; restored from __doc__
        """ set_media_playback_allows_inline(self, enabled:bool) """
        pass

    def set_media_playback_requires_user_gesture(self, enabled): # real signature unknown; restored from __doc__
        """ set_media_playback_requires_user_gesture(self, enabled:bool) """
        pass

    def set_minimum_font_size(self, font_size): # real signature unknown; restored from __doc__
        """ set_minimum_font_size(self, font_size:int) """
        pass

    def set_monospace_font_family(self, monospace_font_family): # real signature unknown; restored from __doc__
        """ set_monospace_font_family(self, monospace_font_family:str) """
        pass

    def set_pictograph_font_family(self, pictograph_font_family): # real signature unknown; restored from __doc__
        """ set_pictograph_font_family(self, pictograph_font_family:str) """
        pass

    def set_print_backgrounds(self, print_backgrounds): # real signature unknown; restored from __doc__
        """ set_print_backgrounds(self, print_backgrounds:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sans_serif_font_family(self, sans_serif_font_family): # real signature unknown; restored from __doc__
        """ set_sans_serif_font_family(self, sans_serif_font_family:str) """
        pass

    def set_serif_font_family(self, serif_font_family): # real signature unknown; restored from __doc__
        """ set_serif_font_family(self, serif_font_family:str) """
        pass

    def set_user_agent(self, user_agent=None): # real signature unknown; restored from __doc__
        """ set_user_agent(self, user_agent:str=None) """
        pass

    def set_user_agent_with_application_details(self, application_name=None, application_version=None): # real signature unknown; restored from __doc__
        """ set_user_agent_with_application_details(self, application_name:str=None, application_version:str=None) """
        pass

    def set_zoom_text_only(self, zoom_text_only): # real signature unknown; restored from __doc__
        """ set_zoom_text_only(self, zoom_text_only:bool) """
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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc3e6f4aac0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Settings), '__module__': 'gi.repository.WebKit2', '__gtype__': <GType WebKitSettings (94869774879616)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'font_size_to_pixels': gi.FunctionInfo(font_size_to_pixels), 'font_size_to_points': gi.FunctionInfo(font_size_to_points), 'get_allow_file_access_from_file_urls': gi.FunctionInfo(get_allow_file_access_from_file_urls), 'get_allow_modal_dialogs': gi.FunctionInfo(get_allow_modal_dialogs), 'get_allow_top_navigation_to_data_urls': gi.FunctionInfo(get_allow_top_navigation_to_data_urls), 'get_allow_universal_access_from_file_urls': gi.FunctionInfo(get_allow_universal_access_from_file_urls), 'get_auto_load_images': gi.FunctionInfo(get_auto_load_images), 'get_cursive_font_family': gi.FunctionInfo(get_cursive_font_family), 'get_default_charset': gi.FunctionInfo(get_default_charset), 'get_default_font_family': gi.FunctionInfo(get_default_font_family), 'get_default_font_size': gi.FunctionInfo(get_default_font_size), 'get_default_monospace_font_size': gi.FunctionInfo(get_default_monospace_font_size), 'get_draw_compositing_indicators': gi.FunctionInfo(get_draw_compositing_indicators), 'get_enable_accelerated_2d_canvas': gi.FunctionInfo(get_enable_accelerated_2d_canvas), 'get_enable_back_forward_navigation_gestures': gi.FunctionInfo(get_enable_back_forward_navigation_gestures), 'get_enable_caret_browsing': gi.FunctionInfo(get_enable_caret_browsing), 'get_enable_developer_extras': gi.FunctionInfo(get_enable_developer_extras), 'get_enable_dns_prefetching': gi.FunctionInfo(get_enable_dns_prefetching), 'get_enable_encrypted_media': gi.FunctionInfo(get_enable_encrypted_media), 'get_enable_frame_flattening': gi.FunctionInfo(get_enable_frame_flattening), 'get_enable_fullscreen': gi.FunctionInfo(get_enable_fullscreen), 'get_enable_html5_database': gi.FunctionInfo(get_enable_html5_database), 'get_enable_html5_local_storage': gi.FunctionInfo(get_enable_html5_local_storage), 'get_enable_hyperlink_auditing': gi.FunctionInfo(get_enable_hyperlink_auditing), 'get_enable_java': gi.FunctionInfo(get_enable_java), 'get_enable_javascript': gi.FunctionInfo(get_enable_javascript), 'get_enable_javascript_markup': gi.FunctionInfo(get_enable_javascript_markup), 'get_enable_media': gi.FunctionInfo(get_enable_media), 'get_enable_media_capabilities': gi.FunctionInfo(get_enable_media_capabilities), 'get_enable_media_stream': gi.FunctionInfo(get_enable_media_stream), 'get_enable_mediasource': gi.FunctionInfo(get_enable_mediasource), 'get_enable_mock_capture_devices': gi.FunctionInfo(get_enable_mock_capture_devices), 'get_enable_offline_web_application_cache': gi.FunctionInfo(get_enable_offline_web_application_cache), 'get_enable_page_cache': gi.FunctionInfo(get_enable_page_cache), 'get_enable_plugins': gi.FunctionInfo(get_enable_plugins), 'get_enable_private_browsing': gi.FunctionInfo(get_enable_private_browsing), 'get_enable_resizable_text_areas': gi.FunctionInfo(get_enable_resizable_text_areas), 'get_enable_site_specific_quirks': gi.FunctionInfo(get_enable_site_specific_quirks), 'get_enable_smooth_scrolling': gi.FunctionInfo(get_enable_smooth_scrolling), 'get_enable_spatial_navigation': gi.FunctionInfo(get_enable_spatial_navigation), 'get_enable_tabs_to_links': gi.FunctionInfo(get_enable_tabs_to_links), 'get_enable_webaudio': gi.FunctionInfo(get_enable_webaudio), 'get_enable_webgl': gi.FunctionInfo(get_enable_webgl), 'get_enable_write_console_messages_to_stdout': gi.FunctionInfo(get_enable_write_console_messages_to_stdout), 'get_enable_xss_auditor': gi.FunctionInfo(get_enable_xss_auditor), 'get_fantasy_font_family': gi.FunctionInfo(get_fantasy_font_family), 'get_hardware_acceleration_policy': gi.FunctionInfo(get_hardware_acceleration_policy), 'get_javascript_can_access_clipboard': gi.FunctionInfo(get_javascript_can_access_clipboard), 'get_javascript_can_open_windows_automatically': gi.FunctionInfo(get_javascript_can_open_windows_automatically), 'get_load_icons_ignoring_image_load_setting': gi.FunctionInfo(get_load_icons_ignoring_image_load_setting), 'get_media_playback_allows_inline': gi.FunctionInfo(get_media_playback_allows_inline), 'get_media_playback_requires_user_gesture': gi.FunctionInfo(get_media_playback_requires_user_gesture), 'get_minimum_font_size': gi.FunctionInfo(get_minimum_font_size), 'get_monospace_font_family': gi.FunctionInfo(get_monospace_font_family), 'get_pictograph_font_family': gi.FunctionInfo(get_pictograph_font_family), 'get_print_backgrounds': gi.FunctionInfo(get_print_backgrounds), 'get_sans_serif_font_family': gi.FunctionInfo(get_sans_serif_font_family), 'get_serif_font_family': gi.FunctionInfo(get_serif_font_family), 'get_user_agent': gi.FunctionInfo(get_user_agent), 'get_zoom_text_only': gi.FunctionInfo(get_zoom_text_only), 'set_allow_file_access_from_file_urls': gi.FunctionInfo(set_allow_file_access_from_file_urls), 'set_allow_modal_dialogs': gi.FunctionInfo(set_allow_modal_dialogs), 'set_allow_top_navigation_to_data_urls': gi.FunctionInfo(set_allow_top_navigation_to_data_urls), 'set_allow_universal_access_from_file_urls': gi.FunctionInfo(set_allow_universal_access_from_file_urls), 'set_auto_load_images': gi.FunctionInfo(set_auto_load_images), 'set_cursive_font_family': gi.FunctionInfo(set_cursive_font_family), 'set_default_charset': gi.FunctionInfo(set_default_charset), 'set_default_font_family': gi.FunctionInfo(set_default_font_family), 'set_default_font_size': gi.FunctionInfo(set_default_font_size), 'set_default_monospace_font_size': gi.FunctionInfo(set_default_monospace_font_size), 'set_draw_compositing_indicators': gi.FunctionInfo(set_draw_compositing_indicators), 'set_enable_accelerated_2d_canvas': gi.FunctionInfo(set_enable_accelerated_2d_canvas), 'set_enable_back_forward_navigation_gestures': gi.FunctionInfo(set_enable_back_forward_navigation_gestures), 'set_enable_caret_browsing': gi.FunctionInfo(set_enable_caret_browsing), 'set_enable_developer_extras': gi.FunctionInfo(set_enable_developer_extras), 'set_enable_dns_prefetching': gi.FunctionInfo(set_enable_dns_prefetching), 'set_enable_encrypted_media': gi.FunctionInfo(set_enable_encrypted_media), 'set_enable_frame_flattening': gi.FunctionInfo(set_enable_frame_flattening), 'set_enable_fullscreen': gi.FunctionInfo(set_enable_fullscreen), 'set_enable_html5_database': gi.FunctionInfo(set_enable_html5_database), 'set_enable_html5_local_storage': gi.FunctionInfo(set_enable_html5_local_storage), 'set_enable_hyperlink_auditing': gi.FunctionInfo(set_enable_hyperlink_auditing), 'set_enable_java': gi.FunctionInfo(set_enable_java), 'set_enable_javascript': gi.FunctionInfo(set_enable_javascript), 'set_enable_javascript_markup': gi.FunctionInfo(set_enable_javascript_markup), 'set_enable_media': gi.FunctionInfo(set_enable_media), 'set_enable_media_capabilities': gi.FunctionInfo(set_enable_media_capabilities), 'set_enable_media_stream': gi.FunctionInfo(set_enable_media_stream), 'set_enable_mediasource': gi.FunctionInfo(set_enable_mediasource), 'set_enable_mock_capture_devices': gi.FunctionInfo(set_enable_mock_capture_devices), 'set_enable_offline_web_application_cache': gi.FunctionInfo(set_enable_offline_web_application_cache), 'set_enable_page_cache': gi.FunctionInfo(set_enable_page_cache), 'set_enable_plugins': gi.FunctionInfo(set_enable_plugins), 'set_enable_private_browsing': gi.FunctionInfo(set_enable_private_browsing), 'set_enable_resizable_text_areas': gi.FunctionInfo(set_enable_resizable_text_areas), 'set_enable_site_specific_quirks': gi.FunctionInfo(set_enable_site_specific_quirks), 'set_enable_smooth_scrolling': gi.FunctionInfo(set_enable_smooth_scrolling), 'set_enable_spatial_navigation': gi.FunctionInfo(set_enable_spatial_navigation), 'set_enable_tabs_to_links': gi.FunctionInfo(set_enable_tabs_to_links), 'set_enable_webaudio': gi.FunctionInfo(set_enable_webaudio), 'set_enable_webgl': gi.FunctionInfo(set_enable_webgl), 'set_enable_write_console_messages_to_stdout': gi.FunctionInfo(set_enable_write_console_messages_to_stdout), 'set_enable_xss_auditor': gi.FunctionInfo(set_enable_xss_auditor), 'set_fantasy_font_family': gi.FunctionInfo(set_fantasy_font_family), 'set_hardware_acceleration_policy': gi.FunctionInfo(set_hardware_acceleration_policy), 'set_javascript_can_access_clipboard': gi.FunctionInfo(set_javascript_can_access_clipboard), 'set_javascript_can_open_windows_automatically': gi.FunctionInfo(set_javascript_can_open_windows_automatically), 'set_load_icons_ignoring_image_load_setting': gi.FunctionInfo(set_load_icons_ignoring_image_load_setting), 'set_media_playback_allows_inline': gi.FunctionInfo(set_media_playback_allows_inline), 'set_media_playback_requires_user_gesture': gi.FunctionInfo(set_media_playback_requires_user_gesture), 'set_minimum_font_size': gi.FunctionInfo(set_minimum_font_size), 'set_monospace_font_family': gi.FunctionInfo(set_monospace_font_family), 'set_pictograph_font_family': gi.FunctionInfo(set_pictograph_font_family), 'set_print_backgrounds': gi.FunctionInfo(set_print_backgrounds), 'set_sans_serif_font_family': gi.FunctionInfo(set_sans_serif_font_family), 'set_serif_font_family': gi.FunctionInfo(set_serif_font_family), 'set_user_agent': gi.FunctionInfo(set_user_agent), 'set_user_agent_with_application_details': gi.FunctionInfo(set_user_agent_with_application_details), 'set_zoom_text_only': gi.FunctionInfo(set_zoom_text_only), 'parent_instance': <property object at 0x7fc3e7175630>, 'priv': <property object at 0x7fc3e7175720>})"
    __gdoc__ = 'Object WebKitSettings\n\nProperties from WebKitSettings:\n  enable-javascript -> gboolean: Enable JavaScript\n    Enable JavaScript.\n  auto-load-images -> gboolean: Auto load images\n    Load images automatically.\n  load-icons-ignoring-image-load-setting -> gboolean: Load icons ignoring image load setting\n    Whether to load site icons ignoring image load setting.\n  enable-offline-web-application-cache -> gboolean: Enable offline web application cache\n    Whether to enable offline web application cache.\n  enable-html5-local-storage -> gboolean: Enable HTML5 local storage\n    Whether to enable HTML5 Local Storage support.\n  enable-html5-database -> gboolean: Enable HTML5 database\n    Whether to enable HTML5 database support.\n  enable-xss-auditor -> gboolean: Enable XSS auditor\n    Whether to enable the XSS auditor.\n  enable-frame-flattening -> gboolean: Enable frame flattening\n    Whether to enable frame flattening.\n  enable-plugins -> gboolean: Enable plugins\n    Enable embedded plugin objects.\n  enable-java -> gboolean: Enable Java\n    Whether Java support should be enabled.\n  javascript-can-open-windows-automatically -> gboolean: JavaScript can open windows automatically\n    Whether JavaScript can open windows automatically.\n  enable-hyperlink-auditing -> gboolean: Enable hyperlink auditing\n    Whether <a ping> should be able to send pings.\n  default-font-family -> gchararray: Default font family\n    The font family to use as the default for content that does not specify a font.\n  monospace-font-family -> gchararray: Monospace font family\n    The font family used as the default for content using monospace font.\n  serif-font-family -> gchararray: Serif font family\n    The font family used as the default for content using serif font.\n  sans-serif-font-family -> gchararray: Sans-serif font family\n    The font family used as the default for content using sans-serif font.\n  cursive-font-family -> gchararray: Cursive font family\n    The font family used as the default for content using cursive font.\n  fantasy-font-family -> gchararray: Fantasy font family\n    The font family used as the default for content using fantasy font.\n  pictograph-font-family -> gchararray: Pictograph font family\n    The font family used as the default for content using pictograph font.\n  default-font-size -> guint: Default font size\n    The default font size used to display text.\n  default-monospace-font-size -> guint: Default monospace font size\n    The default font size used to display monospace text.\n  minimum-font-size -> guint: Minimum font size\n    The minimum font size used to display text.\n  default-charset -> gchararray: Default charset\n    The default text charset used when interpreting content with unspecified charset.\n  enable-private-browsing -> gboolean: Enable private browsing\n    Whether to enable private browsing\n  enable-developer-extras -> gboolean: Enable developer extras\n    Whether to enable developer extras\n  enable-resizable-text-areas -> gboolean: Enable resizable text areas\n    Whether to enable resizable text areas\n  enable-tabs-to-links -> gboolean: Enable tabs to links\n    Whether to enable tabs to links\n  enable-dns-prefetching -> gboolean: Enable DNS prefetching\n    Whether to enable DNS prefetching\n  enable-caret-browsing -> gboolean: Enable Caret Browsing\n    Whether to enable accessibility enhanced keyboard navigation\n  enable-fullscreen -> gboolean: Enable Fullscreen\n    Whether to enable the Javascript Fullscreen API\n  print-backgrounds -> gboolean: Print Backgrounds\n    Whether background images should be drawn during printing\n  enable-webaudio -> gboolean: Enable WebAudio\n    Whether WebAudio content should be handled\n  enable-webgl -> gboolean: Enable WebGL\n    Whether WebGL content should be rendered\n  allow-modal-dialogs -> gboolean: Allow modal dialogs\n    Whether it is possible to create modal dialogs\n  zoom-text-only -> gboolean: Zoom Text Only\n    Whether zoom level of web view changes only the text size\n  javascript-can-access-clipboard -> gboolean: JavaScript can access clipboard\n    Whether JavaScript can access Clipboard\n  media-playback-requires-user-gesture -> gboolean: Media playback requires user gesture\n    Whether media playback requires user gesture\n  media-playback-allows-inline -> gboolean: Media playback allows inline\n    Whether media playback allows inline\n  draw-compositing-indicators -> gboolean: Draw compositing indicators\n    Whether to draw compositing borders and repaint counters\n  enable-site-specific-quirks -> gboolean: Enable Site Specific Quirks\n    Enables the site-specific compatibility workarounds\n  enable-page-cache -> gboolean: Enable page cache\n    Whether the page cache should be used\n  user-agent -> gchararray: User agent string\n    The user agent string\n  enable-smooth-scrolling -> gboolean: Enable smooth scrolling\n    Whether to enable smooth scrolling\n  enable-accelerated-2d-canvas -> gboolean: Enable accelerated 2D canvas\n    Whether to enable accelerated 2D canvas\n  enable-write-console-messages-to-stdout -> gboolean: Write console messages on stdout\n    Whether to write console messages on stdout\n  enable-media-stream -> gboolean: Enable MediaStream\n    Whether MediaStream content should be handled\n  enable-mock-capture-devices -> gboolean: Enable mock capture devices\n    Whether we expose mock capture devices or not\n  enable-spatial-navigation -> gboolean: Enable Spatial Navigation\n    Whether to enable Spatial Navigation support.\n  enable-mediasource -> gboolean: Enable MediaSource\n    Whether MediaSource should be enabled.\n  enable-encrypted-media -> gboolean: Enable EncryptedMedia\n    Whether EncryptedMedia should be enabled.\n  enable-media-capabilities -> gboolean: Enable MediaCapabilities\n    Whether MediaCapabilities should be enabled.\n  allow-file-access-from-file-urls -> gboolean: Allow file access from file URLs\n    Whether file access is allowed from file URLs.\n  allow-universal-access-from-file-urls -> gboolean: Allow universal access from the context of file scheme URLs\n    Whether or not universal access is allowed from the context of file scheme URLs\n  allow-top-navigation-to-data-urls -> gboolean: Allow top frame navigation to data URLs\n    Whether or not top frame navigation is allowed to data URLs\n  hardware-acceleration-policy -> WebKitHardwareAccelerationPolicy: Hardware Acceleration Policy\n    The policy to decide how to enable and disable hardware acceleration\n  enable-back-forward-navigation-gestures -> gboolean: Enable back-forward navigation gestures\n    Whether horizontal swipe gesture will trigger back-forward navigation\n  enable-javascript-markup -> gboolean: Enable JavaScript Markup\n    Enable JavaScript in document markup.\n  enable-media -> gboolean: Enable media\n    Whether media content should be handled\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType WebKitSettings (94869774879616)>'
    __info__ = ObjectInfo(Settings)


