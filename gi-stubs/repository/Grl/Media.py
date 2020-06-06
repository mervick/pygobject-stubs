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


from .Data import Data

class Media(Data):
    """
    :Constructors:
    
    ::
    
        Media(**properties)
        audio_new() -> Grl.Media
        container_new() -> Grl.Media
        image_new() -> Grl.Media
        new() -> Grl.Media
        video_new() -> Grl.Media
    """
    def add_artist(self, artist): # real signature unknown; restored from __doc__
        """ add_artist(self, artist:str) """
        pass

    def add_author(self, author): # real signature unknown; restored from __doc__
        """ add_author(self, author:str) """
        pass

    def add_binary(self, key, buf, size): # real signature unknown; restored from __doc__
        """ add_binary(self, key:int, buf:int, size:int) """
        pass

    def add_boxed(self, key, boxed=None): # real signature unknown; restored from __doc__
        """ add_boxed(self, key:int, boxed=None) """
        pass

    def add_director(self, director): # real signature unknown; restored from __doc__
        """ add_director(self, director:str) """
        pass

    def add_external_player(self, player): # real signature unknown; restored from __doc__
        """ add_external_player(self, player:str) """
        pass

    def add_external_url(self, url): # real signature unknown; restored from __doc__
        """ add_external_url(self, url:str) """
        pass

    def add_float(self, key, floatvalue): # real signature unknown; restored from __doc__
        """ add_float(self, key:int, floatvalue:float) """
        pass

    def add_for_id(self, key_name, value): # real signature unknown; restored from __doc__
        """ add_for_id(self, key_name:str, value:GObject.Value) -> bool """
        return False

    def add_genre(self, genre): # real signature unknown; restored from __doc__
        """ add_genre(self, genre:str) """
        pass

    def add_int(self, key, intvalue): # real signature unknown; restored from __doc__
        """ add_int(self, key:int, intvalue:int) """
        pass

    def add_int64(self, key, intvalue): # real signature unknown; restored from __doc__
        """ add_int64(self, key:int, intvalue:int) """
        pass

    def add_keyword(self, keyword): # real signature unknown; restored from __doc__
        """ add_keyword(self, keyword:str) """
        pass

    def add_lyrics(self, lyrics): # real signature unknown; restored from __doc__
        """ add_lyrics(self, lyrics:str) """
        pass

    def add_mb_artist_id(self, mb_artist_id): # real signature unknown; restored from __doc__
        """ add_mb_artist_id(self, mb_artist_id:str) """
        pass

    def add_performer(self, performer): # real signature unknown; restored from __doc__
        """ add_performer(self, performer:str) """
        pass

    def add_producer(self, producer): # real signature unknown; restored from __doc__
        """ add_producer(self, producer:str) """
        pass

    def add_region_data(self, region, publication_date, certificate): # real signature unknown; restored from __doc__
        """ add_region_data(self, region:str, publication_date:GLib.DateTime, certificate:str) """
        pass

    def add_related_keys(self, relkeys): # real signature unknown; restored from __doc__
        """ add_related_keys(self, relkeys:Grl.RelatedKeys) """
        pass

    def add_string(self, key, strvalue): # real signature unknown; restored from __doc__
        """ add_string(self, key:int, strvalue:str) """
        pass

    def add_thumbnail(self, thumbnail): # real signature unknown; restored from __doc__
        """ add_thumbnail(self, thumbnail:str) """
        pass

    def add_thumbnail_binary(self, thumbnail, size): # real signature unknown; restored from __doc__
        """ add_thumbnail_binary(self, thumbnail:int, size:int) """
        pass

    def add_url_data(self, url, mime, bitrate, framerate, width, height): # real signature unknown; restored from __doc__
        """ add_url_data(self, url:str, mime:str, bitrate:int, framerate:float, width:int, height:int) """
        pass

    def audio_new(self): # real signature unknown; restored from __doc__
        """ audio_new() -> Grl.Media """
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

    def container_new(self): # real signature unknown; restored from __doc__
        """ container_new() -> Grl.Media """
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

    def get_album(self): # real signature unknown; restored from __doc__
        """ get_album(self) -> str """
        return ""

    def get_album_artist(self): # real signature unknown; restored from __doc__
        """ get_album_artist(self) -> str """
        return ""

    def get_album_disc_number(self): # real signature unknown; restored from __doc__
        """ get_album_disc_number(self) -> int """
        return 0

    def get_artist(self): # real signature unknown; restored from __doc__
        """ get_artist(self) -> str """
        return ""

    def get_artist_nth(self, index): # real signature unknown; restored from __doc__
        """ get_artist_nth(self, index:int) -> str """
        return ""

    def get_author(self): # real signature unknown; restored from __doc__
        """ get_author(self) -> str """
        return ""

    def get_author_nth(self, index): # real signature unknown; restored from __doc__
        """ get_author_nth(self, index:int) -> str """
        return ""

    def get_binary(self, key): # real signature unknown; restored from __doc__
        """ get_binary(self, key:int) -> int, size:int """
        return 0

    def get_bitrate(self): # real signature unknown; restored from __doc__
        """ get_bitrate(self) -> int """
        return 0

    def get_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_boolean(self, key:int) -> bool """
        return False

    def get_boxed(self, key): # real signature unknown; restored from __doc__
        """ get_boxed(self, key:int) """
        pass

    def get_camera_model(self): # real signature unknown; restored from __doc__
        """ get_camera_model(self) -> str """
        return ""

    def get_certificate(self): # real signature unknown; restored from __doc__
        """ get_certificate(self) -> str """
        return ""

    def get_childcount(self): # real signature unknown; restored from __doc__
        """ get_childcount(self) -> int """
        return 0

    def get_composer(self): # real signature unknown; restored from __doc__
        """ get_composer(self) -> str """
        return ""

    def get_composer_nth(self, index): # real signature unknown; restored from __doc__
        """ get_composer_nth(self, index:int) -> str """
        return ""

    def get_creation_date(self): # real signature unknown; restored from __doc__
        """ get_creation_date(self) -> GLib.DateTime """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_director(self): # real signature unknown; restored from __doc__
        """ get_director(self) -> str """
        return ""

    def get_director_nth(self, index): # real signature unknown; restored from __doc__
        """ get_director_nth(self, index:int) -> str """
        return ""

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> int """
        return 0

    def get_episode(self): # real signature unknown; restored from __doc__
        """ get_episode(self) -> int """
        return 0

    def get_episode_title(self): # real signature unknown; restored from __doc__
        """ get_episode_title(self) -> str """
        return ""

    def get_exposure_time(self): # real signature unknown; restored from __doc__
        """ get_exposure_time(self) -> float """
        return 0.0

    def get_external_url(self): # real signature unknown; restored from __doc__
        """ get_external_url(self) -> str """
        return ""

    def get_external_url_nth(self, index): # real signature unknown; restored from __doc__
        """ get_external_url_nth(self, index:int) -> str """
        return ""

    def get_favourite(self): # real signature unknown; restored from __doc__
        """ get_favourite(self) -> bool """
        return False

    def get_flash_used(self): # real signature unknown; restored from __doc__
        """ get_flash_used(self) -> str """
        return ""

    def get_float(self, key): # real signature unknown; restored from __doc__
        """ get_float(self, key:int) -> float """
        return 0.0

    def get_framerate(self): # real signature unknown; restored from __doc__
        """ get_framerate(self) -> float """
        return 0.0

    def get_genre(self): # real signature unknown; restored from __doc__
        """ get_genre(self) -> str """
        return ""

    def get_genre_nth(self, index): # real signature unknown; restored from __doc__
        """ get_genre_nth(self, index:int) -> str """
        return ""

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_int(self, key): # real signature unknown; restored from __doc__
        """ get_int(self, key:int) -> int """
        return 0

    def get_int64(self, key): # real signature unknown; restored from __doc__
        """ get_int64(self, key:int) -> int """
        return 0

    def get_iso_speed(self): # real signature unknown; restored from __doc__
        """ get_iso_speed(self) -> float """
        return 0.0

    def get_keys(self): # real signature unknown; restored from __doc__
        """ get_keys(self) -> list """
        return []

    def get_keyword(self): # real signature unknown; restored from __doc__
        """ get_keyword(self) -> str """
        return ""

    def get_keyword_nth(self, index): # real signature unknown; restored from __doc__
        """ get_keyword_nth(self, index:int) -> str """
        return ""

    def get_last_played(self): # real signature unknown; restored from __doc__
        """ get_last_played(self) -> GLib.DateTime """
        pass

    def get_last_position(self): # real signature unknown; restored from __doc__
        """ get_last_position(self) -> int """
        return 0

    def get_license(self): # real signature unknown; restored from __doc__
        """ get_license(self) -> str """
        return ""

    def get_lyrics(self): # real signature unknown; restored from __doc__
        """ get_lyrics(self) -> str """
        return ""

    def get_lyrics_nth(self, index): # real signature unknown; restored from __doc__
        """ get_lyrics_nth(self, index:int) -> str """
        return ""

    def get_mb_album_id(self): # real signature unknown; restored from __doc__
        """ get_mb_album_id(self) -> str """
        return ""

    def get_mb_artist_id(self): # real signature unknown; restored from __doc__
        """ get_mb_artist_id(self) -> str """
        return ""

    def get_mb_artist_id_nth(self, index): # real signature unknown; restored from __doc__
        """ get_mb_artist_id_nth(self, index:int) -> str """
        return ""

    def get_mb_recording_id(self): # real signature unknown; restored from __doc__
        """ get_mb_recording_id(self) -> str """
        return ""

    def get_mb_release_group_id(self): # real signature unknown; restored from __doc__
        """ get_mb_release_group_id(self) -> str """
        return ""

    def get_mb_release_id(self): # real signature unknown; restored from __doc__
        """ get_mb_release_id(self) -> str """
        return ""

    def get_mb_track_id(self): # real signature unknown; restored from __doc__
        """ get_mb_track_id(self) -> str """
        return ""

    def get_media_type(self): # real signature unknown; restored from __doc__
        """ get_media_type(self) -> Grl.MediaType """
        pass

    def get_mime(self): # real signature unknown; restored from __doc__
        """ get_mime(self) -> str """
        return ""

    def get_modification_date(self): # real signature unknown; restored from __doc__
        """ get_modification_date(self) -> GLib.DateTime """
        pass

    def get_orientation(self): # real signature unknown; restored from __doc__
        """ get_orientation(self) -> int """
        return 0

    def get_original_title(self): # real signature unknown; restored from __doc__
        """ get_original_title(self) -> str """
        return ""

    def get_performer(self): # real signature unknown; restored from __doc__
        """ get_performer(self) -> str """
        return ""

    def get_performer_nth(self, index): # real signature unknown; restored from __doc__
        """ get_performer_nth(self, index:int) -> str """
        return ""

    def get_player(self): # real signature unknown; restored from __doc__
        """ get_player(self) -> str """
        return ""

    def get_player_nth(self, index): # real signature unknown; restored from __doc__
        """ get_player_nth(self, index:int) -> str """
        return ""

    def get_play_count(self): # real signature unknown; restored from __doc__
        """ get_play_count(self) -> int """
        return 0

    def get_producer(self): # real signature unknown; restored from __doc__
        """ get_producer(self) -> str """
        return ""

    def get_producer_nth(self, index): # real signature unknown; restored from __doc__
        """ get_producer_nth(self, index:int) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_publication_date(self): # real signature unknown; restored from __doc__
        """ get_publication_date(self) -> GLib.DateTime """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rating(self): # real signature unknown; restored from __doc__
        """ get_rating(self) -> float """
        return 0.0

    def get_region(self): # real signature unknown; restored from __doc__
        """ get_region(self) -> str """
        return ""

    def get_region_data(self): # real signature unknown; restored from __doc__
        """ get_region_data(self) -> str, publication_date:GLib.DateTime, certificate:str """
        return ""

    def get_region_data_nth(self, index): # real signature unknown; restored from __doc__
        """ get_region_data_nth(self, index:int) -> str, publication_date:GLib.DateTime, certificate:str """
        return ""

    def get_related_keys(self, key, index): # real signature unknown; restored from __doc__
        """ get_related_keys(self, key:int, index:int) -> Grl.RelatedKeys """
        pass

    def get_season(self): # real signature unknown; restored from __doc__
        """ get_season(self) -> int """
        return 0

    def get_show(self): # real signature unknown; restored from __doc__
        """ get_show(self) -> str """
        return ""

    def get_single_values_for_key(self, key): # real signature unknown; restored from __doc__
        """ get_single_values_for_key(self, key:int) -> list """
        return []

    def get_single_values_for_key_string(self, key): # real signature unknown; restored from __doc__
        """ get_single_values_for_key_string(self, key:int) -> list """
        return []

    def get_site(self): # real signature unknown; restored from __doc__
        """ get_site(self) -> str """
        return ""

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> str """
        return ""

    def get_start_time(self): # real signature unknown; restored from __doc__
        """ get_start_time(self) -> float """
        return 0.0

    def get_string(self, key): # real signature unknown; restored from __doc__
        """ get_string(self, key:int) -> str """
        return ""

    def get_studio(self): # real signature unknown; restored from __doc__
        """ get_studio(self) -> str """
        return ""

    def get_thumbnail(self): # real signature unknown; restored from __doc__
        """ get_thumbnail(self) -> str """
        return ""

    def get_thumbnail_binary(self, size): # real signature unknown; restored from __doc__
        """ get_thumbnail_binary(self, size:int) -> int """
        return 0

    def get_thumbnail_binary_nth(self, size, index): # real signature unknown; restored from __doc__
        """ get_thumbnail_binary_nth(self, size:int, index:int) -> int """
        return 0

    def get_thumbnail_nth(self, index): # real signature unknown; restored from __doc__
        """ get_thumbnail_nth(self, index:int) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_track_number(self): # real signature unknown; restored from __doc__
        """ get_track_number(self) -> int """
        return 0

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> str """
        return ""

    def get_url_data(self, framerate, width, height): # real signature unknown; restored from __doc__
        """ get_url_data(self, framerate:float, width:int, height:int) -> str, mime:str, bitrate:int """
        return ""

    def get_url_data_nth(self, index, framerate, width, height): # real signature unknown; restored from __doc__
        """ get_url_data_nth(self, index:int, framerate:float, width:int, height:int) -> str, mime:str, bitrate:int """
        return ""

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

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

    def image_new(self): # real signature unknown; restored from __doc__
        """ image_new() -> Grl.Media """
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

    def is_audio(self): # real signature unknown; restored from __doc__
        """ is_audio(self) -> bool """
        return False

    def is_container(self): # real signature unknown; restored from __doc__
        """ is_container(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_image(self): # real signature unknown; restored from __doc__
        """ is_image(self) -> bool """
        return False

    def is_video(self): # real signature unknown; restored from __doc__
        """ is_video(self) -> bool """
        return False

    def length(self, key): # real signature unknown; restored from __doc__
        """ length(self, key:int) -> int """
        return 0

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Grl.Media """
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

    def serialize(self): # real signature unknown; restored from __doc__
        """ serialize(self) -> str """
        return ""

    def set(self, key, value): # real signature unknown; restored from __doc__
        """ set(self, key:int, value:GObject.Value) """
        pass

    def set_album(self, album): # real signature unknown; restored from __doc__
        """ set_album(self, album:str) """
        pass

    def set_album_artist(self, album_artist): # real signature unknown; restored from __doc__
        """ set_album_artist(self, album_artist:str) """
        pass

    def set_album_disc_number(self, disc_number): # real signature unknown; restored from __doc__
        """ set_album_disc_number(self, disc_number:int) """
        pass

    def set_artist(self, artist): # real signature unknown; restored from __doc__
        """ set_artist(self, artist:str) """
        pass

    def set_author(self, author): # real signature unknown; restored from __doc__
        """ set_author(self, author:str) """
        pass

    def set_binary(self, key, buf, size): # real signature unknown; restored from __doc__
        """ set_binary(self, key:int, buf:int, size:int) """
        pass

    def set_bitrate(self, bitrate): # real signature unknown; restored from __doc__
        """ set_bitrate(self, bitrate:int) """
        pass

    def set_boolean(self, key, boolvalue): # real signature unknown; restored from __doc__
        """ set_boolean(self, key:int, boolvalue:bool) """
        pass

    def set_boxed(self, key, boxed=None): # real signature unknown; restored from __doc__
        """ set_boxed(self, key:int, boxed=None) """
        pass

    def set_camera_model(self, camera_model): # real signature unknown; restored from __doc__
        """ set_camera_model(self, camera_model:str) """
        pass

    def set_certificate(self, certificate): # real signature unknown; restored from __doc__
        """ set_certificate(self, certificate:str) """
        pass

    def set_childcount(self, childcount): # real signature unknown; restored from __doc__
        """ set_childcount(self, childcount:int) """
        pass

    def set_composer(self, composer): # real signature unknown; restored from __doc__
        """ set_composer(self, composer:str) """
        pass

    def set_creation_date(self, creation_date): # real signature unknown; restored from __doc__
        """ set_creation_date(self, creation_date:GLib.DateTime) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_director(self, director): # real signature unknown; restored from __doc__
        """ set_director(self, director:str) """
        pass

    def set_duration(self, duration): # real signature unknown; restored from __doc__
        """ set_duration(self, duration:int) """
        pass

    def set_episode(self, episode): # real signature unknown; restored from __doc__
        """ set_episode(self, episode:int) """
        pass

    def set_episode_title(self, episode_title): # real signature unknown; restored from __doc__
        """ set_episode_title(self, episode_title:str) """
        pass

    def set_exposure_time(self, exposure_time): # real signature unknown; restored from __doc__
        """ set_exposure_time(self, exposure_time:float) """
        pass

    def set_external_player(self, player): # real signature unknown; restored from __doc__
        """ set_external_player(self, player:str) """
        pass

    def set_external_url(self, url): # real signature unknown; restored from __doc__
        """ set_external_url(self, url:str) """
        pass

    def set_favourite(self, favourite): # real signature unknown; restored from __doc__
        """ set_favourite(self, favourite:bool) """
        pass

    def set_flash_used(self, flash_used): # real signature unknown; restored from __doc__
        """ set_flash_used(self, flash_used:str) """
        pass

    def set_float(self, key, floatvalue): # real signature unknown; restored from __doc__
        """ set_float(self, key:int, floatvalue:float) """
        pass

    def set_for_id(self, key_name, value): # real signature unknown; restored from __doc__
        """ set_for_id(self, key_name:str, value:GObject.Value) -> bool """
        return False

    def set_framerate(self, framerate): # real signature unknown; restored from __doc__
        """ set_framerate(self, framerate:float) """
        pass

    def set_genre(self, genre): # real signature unknown; restored from __doc__
        """ set_genre(self, genre:str) """
        pass

    def set_height(self, height): # real signature unknown; restored from __doc__
        """ set_height(self, height:int) """
        pass

    def set_id(self, id): # real signature unknown; restored from __doc__
        """ set_id(self, id:str) """
        pass

    def set_int(self, key, intvalue): # real signature unknown; restored from __doc__
        """ set_int(self, key:int, intvalue:int) """
        pass

    def set_int64(self, key, intvalue): # real signature unknown; restored from __doc__
        """ set_int64(self, key:int, intvalue:int) """
        pass

    def set_iso_speed(self, iso_speed): # real signature unknown; restored from __doc__
        """ set_iso_speed(self, iso_speed:float) """
        pass

    def set_keyword(self, keyword): # real signature unknown; restored from __doc__
        """ set_keyword(self, keyword:str) """
        pass

    def set_last_played(self, last_played): # real signature unknown; restored from __doc__
        """ set_last_played(self, last_played:GLib.DateTime) """
        pass

    def set_last_position(self, last_position): # real signature unknown; restored from __doc__
        """ set_last_position(self, last_position:int) """
        pass

    def set_license(self, license): # real signature unknown; restored from __doc__
        """ set_license(self, license:str) """
        pass

    def set_lyrics(self, lyrics): # real signature unknown; restored from __doc__
        """ set_lyrics(self, lyrics:str) """
        pass

    def set_mb_album_id(self, mb_album_id): # real signature unknown; restored from __doc__
        """ set_mb_album_id(self, mb_album_id:str) """
        pass

    def set_mb_artist_id(self, mb_artist_id): # real signature unknown; restored from __doc__
        """ set_mb_artist_id(self, mb_artist_id:str) """
        pass

    def set_mb_recording_id(self, mb_recording_id): # real signature unknown; restored from __doc__
        """ set_mb_recording_id(self, mb_recording_id:str) """
        pass

    def set_mb_release_group_id(self, mb_release_group_id): # real signature unknown; restored from __doc__
        """ set_mb_release_group_id(self, mb_release_group_id:str) """
        pass

    def set_mb_release_id(self, mb_release_id): # real signature unknown; restored from __doc__
        """ set_mb_release_id(self, mb_release_id:str) """
        pass

    def set_mb_track_id(self, mb_track_id): # real signature unknown; restored from __doc__
        """ set_mb_track_id(self, mb_track_id:str) """
        pass

    def set_mime(self, mime): # real signature unknown; restored from __doc__
        """ set_mime(self, mime:str) """
        pass

    def set_modification_date(self, modification_date): # real signature unknown; restored from __doc__
        """ set_modification_date(self, modification_date:GLib.DateTime) """
        pass

    def set_orientation(self, orientation): # real signature unknown; restored from __doc__
        """ set_orientation(self, orientation:int) """
        pass

    def set_original_title(self, original_title): # real signature unknown; restored from __doc__
        """ set_original_title(self, original_title:str) """
        pass

    def set_performer(self, performer): # real signature unknown; restored from __doc__
        """ set_performer(self, performer:str) """
        pass

    def set_play_count(self, play_count): # real signature unknown; restored from __doc__
        """ set_play_count(self, play_count:int) """
        pass

    def set_producer(self, producer): # real signature unknown; restored from __doc__
        """ set_producer(self, producer:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_publication_date(self, date): # real signature unknown; restored from __doc__
        """ set_publication_date(self, date:GLib.DateTime) """
        pass

    def set_rating(self, rating, max): # real signature unknown; restored from __doc__
        """ set_rating(self, rating:float, max:float) """
        pass

    def set_region(self, region): # real signature unknown; restored from __doc__
        """ set_region(self, region:str) """
        pass

    def set_region_data(self, region, publication_date, certificate): # real signature unknown; restored from __doc__
        """ set_region_data(self, region:str, publication_date:GLib.DateTime, certificate:str) """
        pass

    def set_related_keys(self, relkeys, index): # real signature unknown; restored from __doc__
        """ set_related_keys(self, relkeys:Grl.RelatedKeys, index:int) """
        pass

    def set_season(self, season): # real signature unknown; restored from __doc__
        """ set_season(self, season:int) """
        pass

    def set_show(self, show): # real signature unknown; restored from __doc__
        """ set_show(self, show:str) """
        pass

    def set_site(self, site): # real signature unknown; restored from __doc__
        """ set_site(self, site:str) """
        pass

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
        pass

    def set_source(self, source): # real signature unknown; restored from __doc__
        """ set_source(self, source:str) """
        pass

    def set_string(self, key, strvalue): # real signature unknown; restored from __doc__
        """ set_string(self, key:int, strvalue:str) """
        pass

    def set_studio(self, studio): # real signature unknown; restored from __doc__
        """ set_studio(self, studio:str) """
        pass

    def set_thumbnail(self, thumbnail): # real signature unknown; restored from __doc__
        """ set_thumbnail(self, thumbnail:str) """
        pass

    def set_thumbnail_binary(self, thumbnail, size): # real signature unknown; restored from __doc__
        """ set_thumbnail_binary(self, thumbnail:int, size:int) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_track_number(self, track_number): # real signature unknown; restored from __doc__
        """ set_track_number(self, track_number:int) """
        pass

    def set_url(self, url): # real signature unknown; restored from __doc__
        """ set_url(self, url:str) """
        pass

    def set_url_data(self, url, mime, bitrate, framerate, width, height): # real signature unknown; restored from __doc__
        """ set_url_data(self, url:str, mime:str, bitrate:int, framerate:float, width:int, height:int) """
        pass

    def set_width(self, width): # real signature unknown; restored from __doc__
        """ set_width(self, width:int) """
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

    def unserialize(self, serial): # real signature unknown; restored from __doc__
        """ unserialize(serial:str) -> Grl.Media """
        pass

    def video_new(self): # real signature unknown; restored from __doc__
        """ video_new() -> Grl.Media """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa0404a69a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Media), '__module__': 'gi.repository.Grl', '__gtype__': <GType GrlMedia (94188897605792)>, '__doc__': None, '__gsignals__': {}, 'audio_new': gi.FunctionInfo(audio_new), 'container_new': gi.FunctionInfo(container_new), 'image_new': gi.FunctionInfo(image_new), 'new': gi.FunctionInfo(new), 'video_new': gi.FunctionInfo(video_new), 'unserialize': gi.FunctionInfo(unserialize), 'add_artist': gi.FunctionInfo(add_artist), 'add_author': gi.FunctionInfo(add_author), 'add_director': gi.FunctionInfo(add_director), 'add_external_player': gi.FunctionInfo(add_external_player), 'add_external_url': gi.FunctionInfo(add_external_url), 'add_genre': gi.FunctionInfo(add_genre), 'add_keyword': gi.FunctionInfo(add_keyword), 'add_lyrics': gi.FunctionInfo(add_lyrics), 'add_mb_artist_id': gi.FunctionInfo(add_mb_artist_id), 'add_performer': gi.FunctionInfo(add_performer), 'add_producer': gi.FunctionInfo(add_producer), 'add_region_data': gi.FunctionInfo(add_region_data), 'add_thumbnail': gi.FunctionInfo(add_thumbnail), 'add_thumbnail_binary': gi.FunctionInfo(add_thumbnail_binary), 'add_url_data': gi.FunctionInfo(add_url_data), 'get_album': gi.FunctionInfo(get_album), 'get_album_artist': gi.FunctionInfo(get_album_artist), 'get_album_disc_number': gi.FunctionInfo(get_album_disc_number), 'get_artist': gi.FunctionInfo(get_artist), 'get_artist_nth': gi.FunctionInfo(get_artist_nth), 'get_author': gi.FunctionInfo(get_author), 'get_author_nth': gi.FunctionInfo(get_author_nth), 'get_bitrate': gi.FunctionInfo(get_bitrate), 'get_camera_model': gi.FunctionInfo(get_camera_model), 'get_certificate': gi.FunctionInfo(get_certificate), 'get_childcount': gi.FunctionInfo(get_childcount), 'get_composer': gi.FunctionInfo(get_composer), 'get_composer_nth': gi.FunctionInfo(get_composer_nth), 'get_creation_date': gi.FunctionInfo(get_creation_date), 'get_description': gi.FunctionInfo(get_description), 'get_director': gi.FunctionInfo(get_director), 'get_director_nth': gi.FunctionInfo(get_director_nth), 'get_duration': gi.FunctionInfo(get_duration), 'get_episode': gi.FunctionInfo(get_episode), 'get_episode_title': gi.FunctionInfo(get_episode_title), 'get_exposure_time': gi.FunctionInfo(get_exposure_time), 'get_external_url': gi.FunctionInfo(get_external_url), 'get_external_url_nth': gi.FunctionInfo(get_external_url_nth), 'get_favourite': gi.FunctionInfo(get_favourite), 'get_flash_used': gi.FunctionInfo(get_flash_used), 'get_framerate': gi.FunctionInfo(get_framerate), 'get_genre': gi.FunctionInfo(get_genre), 'get_genre_nth': gi.FunctionInfo(get_genre_nth), 'get_height': gi.FunctionInfo(get_height), 'get_id': gi.FunctionInfo(get_id), 'get_iso_speed': gi.FunctionInfo(get_iso_speed), 'get_keyword': gi.FunctionInfo(get_keyword), 'get_keyword_nth': gi.FunctionInfo(get_keyword_nth), 'get_last_played': gi.FunctionInfo(get_last_played), 'get_last_position': gi.FunctionInfo(get_last_position), 'get_license': gi.FunctionInfo(get_license), 'get_lyrics': gi.FunctionInfo(get_lyrics), 'get_lyrics_nth': gi.FunctionInfo(get_lyrics_nth), 'get_mb_album_id': gi.FunctionInfo(get_mb_album_id), 'get_mb_artist_id': gi.FunctionInfo(get_mb_artist_id), 'get_mb_artist_id_nth': gi.FunctionInfo(get_mb_artist_id_nth), 'get_mb_recording_id': gi.FunctionInfo(get_mb_recording_id), 'get_mb_release_group_id': gi.FunctionInfo(get_mb_release_group_id), 'get_mb_release_id': gi.FunctionInfo(get_mb_release_id), 'get_mb_track_id': gi.FunctionInfo(get_mb_track_id), 'get_media_type': gi.FunctionInfo(get_media_type), 'get_mime': gi.FunctionInfo(get_mime), 'get_modification_date': gi.FunctionInfo(get_modification_date), 'get_orientation': gi.FunctionInfo(get_orientation), 'get_original_title': gi.FunctionInfo(get_original_title), 'get_performer': gi.FunctionInfo(get_performer), 'get_performer_nth': gi.FunctionInfo(get_performer_nth), 'get_play_count': gi.FunctionInfo(get_play_count), 'get_player': gi.FunctionInfo(get_player), 'get_player_nth': gi.FunctionInfo(get_player_nth), 'get_producer': gi.FunctionInfo(get_producer), 'get_producer_nth': gi.FunctionInfo(get_producer_nth), 'get_publication_date': gi.FunctionInfo(get_publication_date), 'get_rating': gi.FunctionInfo(get_rating), 'get_region': gi.FunctionInfo(get_region), 'get_region_data': gi.FunctionInfo(get_region_data), 'get_region_data_nth': gi.FunctionInfo(get_region_data_nth), 'get_season': gi.FunctionInfo(get_season), 'get_show': gi.FunctionInfo(get_show), 'get_site': gi.FunctionInfo(get_site), 'get_size': gi.FunctionInfo(get_size), 'get_source': gi.FunctionInfo(get_source), 'get_start_time': gi.FunctionInfo(get_start_time), 'get_studio': gi.FunctionInfo(get_studio), 'get_thumbnail': gi.FunctionInfo(get_thumbnail), 'get_thumbnail_binary': gi.FunctionInfo(get_thumbnail_binary), 'get_thumbnail_binary_nth': gi.FunctionInfo(get_thumbnail_binary_nth), 'get_thumbnail_nth': gi.FunctionInfo(get_thumbnail_nth), 'get_title': gi.FunctionInfo(get_title), 'get_track_number': gi.FunctionInfo(get_track_number), 'get_url': gi.FunctionInfo(get_url), 'get_url_data': gi.FunctionInfo(get_url_data), 'get_url_data_nth': gi.FunctionInfo(get_url_data_nth), 'get_width': gi.FunctionInfo(get_width), 'is_audio': gi.FunctionInfo(is_audio), 'is_container': gi.FunctionInfo(is_container), 'is_image': gi.FunctionInfo(is_image), 'is_video': gi.FunctionInfo(is_video), 'serialize': gi.FunctionInfo(serialize), 'set_album': gi.FunctionInfo(set_album), 'set_album_artist': gi.FunctionInfo(set_album_artist), 'set_album_disc_number': gi.FunctionInfo(set_album_disc_number), 'set_artist': gi.FunctionInfo(set_artist), 'set_author': gi.FunctionInfo(set_author), 'set_bitrate': gi.FunctionInfo(set_bitrate), 'set_camera_model': gi.FunctionInfo(set_camera_model), 'set_certificate': gi.FunctionInfo(set_certificate), 'set_childcount': gi.FunctionInfo(set_childcount), 'set_composer': gi.FunctionInfo(set_composer), 'set_creation_date': gi.FunctionInfo(set_creation_date), 'set_description': gi.FunctionInfo(set_description), 'set_director': gi.FunctionInfo(set_director), 'set_duration': gi.FunctionInfo(set_duration), 'set_episode': gi.FunctionInfo(set_episode), 'set_episode_title': gi.FunctionInfo(set_episode_title), 'set_exposure_time': gi.FunctionInfo(set_exposure_time), 'set_external_player': gi.FunctionInfo(set_external_player), 'set_external_url': gi.FunctionInfo(set_external_url), 'set_favourite': gi.FunctionInfo(set_favourite), 'set_flash_used': gi.FunctionInfo(set_flash_used), 'set_framerate': gi.FunctionInfo(set_framerate), 'set_genre': gi.FunctionInfo(set_genre), 'set_height': gi.FunctionInfo(set_height), 'set_id': gi.FunctionInfo(set_id), 'set_iso_speed': gi.FunctionInfo(set_iso_speed), 'set_keyword': gi.FunctionInfo(set_keyword), 'set_last_played': gi.FunctionInfo(set_last_played), 'set_last_position': gi.FunctionInfo(set_last_position), 'set_license': gi.FunctionInfo(set_license), 'set_lyrics': gi.FunctionInfo(set_lyrics), 'set_mb_album_id': gi.FunctionInfo(set_mb_album_id), 'set_mb_artist_id': gi.FunctionInfo(set_mb_artist_id), 'set_mb_recording_id': gi.FunctionInfo(set_mb_recording_id), 'set_mb_release_group_id': gi.FunctionInfo(set_mb_release_group_id), 'set_mb_release_id': gi.FunctionInfo(set_mb_release_id), 'set_mb_track_id': gi.FunctionInfo(set_mb_track_id), 'set_mime': gi.FunctionInfo(set_mime), 'set_modification_date': gi.FunctionInfo(set_modification_date), 'set_orientation': gi.FunctionInfo(set_orientation), 'set_original_title': gi.FunctionInfo(set_original_title), 'set_performer': gi.FunctionInfo(set_performer), 'set_play_count': gi.FunctionInfo(set_play_count), 'set_producer': gi.FunctionInfo(set_producer), 'set_publication_date': gi.FunctionInfo(set_publication_date), 'set_rating': gi.FunctionInfo(set_rating), 'set_region': gi.FunctionInfo(set_region), 'set_region_data': gi.FunctionInfo(set_region_data), 'set_season': gi.FunctionInfo(set_season), 'set_show': gi.FunctionInfo(set_show), 'set_site': gi.FunctionInfo(set_site), 'set_size': gi.FunctionInfo(set_size), 'set_source': gi.FunctionInfo(set_source), 'set_studio': gi.FunctionInfo(set_studio), 'set_thumbnail': gi.FunctionInfo(set_thumbnail), 'set_thumbnail_binary': gi.FunctionInfo(set_thumbnail_binary), 'set_title': gi.FunctionInfo(set_title), 'set_track_number': gi.FunctionInfo(set_track_number), 'set_url': gi.FunctionInfo(set_url), 'set_url_data': gi.FunctionInfo(set_url_data), 'set_width': gi.FunctionInfo(set_width), 'parent': <property object at 0x7fa0418b4cc0>, 'priv': <property object at 0x7fa04049b950>, '_grl_reserved': <property object at 0x7fa04049ba40>})"
    __gdoc__ = 'Object GrlMedia\n\nProperties from GrlMedia:\n  media-type -> GrlMediaType: Media type\n    Type of media\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GrlMedia (94188897605792)>'
    __info__ = ObjectInfo(Media)


