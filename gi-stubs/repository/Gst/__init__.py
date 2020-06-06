# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


# Variables with simple values

ALLOCATOR_SYSMEM = 'SystemMemory'

BUFFER_COPY_ALL = 0
BUFFER_COPY_METADATA = 0

BUFFER_OFFSET_NONE = 18446744073709551615

CAN_INLINE = 1

CAPS_FEATURE_MEMORY_SYSTEM_MEMORY = 'memory:SystemMemory'

CLOCK_TIME_NONE = 18446744073709551615

DEBUG_BG_MASK = 240

DEBUG_FG_MASK = 15

DEBUG_FORMAT_MASK = 65280

ELEMENT_FACTORY_KLASS_DECODER = 'Decoder'
ELEMENT_FACTORY_KLASS_DECRYPTOR = 'Decryptor'
ELEMENT_FACTORY_KLASS_DEMUXER = 'Demuxer'
ELEMENT_FACTORY_KLASS_DEPAYLOADER = 'Depayloader'
ELEMENT_FACTORY_KLASS_ENCODER = 'Encoder'
ELEMENT_FACTORY_KLASS_ENCRYPTOR = 'Encryptor'
ELEMENT_FACTORY_KLASS_FORMATTER = 'Formatter'
ELEMENT_FACTORY_KLASS_HARDWARE = 'Hardware'

ELEMENT_FACTORY_KLASS_MEDIA_AUDIO = 'Audio'
ELEMENT_FACTORY_KLASS_MEDIA_IMAGE = 'Image'
ELEMENT_FACTORY_KLASS_MEDIA_METADATA = 'Metadata'
ELEMENT_FACTORY_KLASS_MEDIA_SUBTITLE = 'Subtitle'
ELEMENT_FACTORY_KLASS_MEDIA_VIDEO = 'Video'

ELEMENT_FACTORY_KLASS_MUXER = 'Muxer'
ELEMENT_FACTORY_KLASS_PARSER = 'Parser'
ELEMENT_FACTORY_KLASS_PAYLOADER = 'Payloader'
ELEMENT_FACTORY_KLASS_SINK = 'Sink'
ELEMENT_FACTORY_KLASS_SRC = 'Source'

ELEMENT_FACTORY_TYPE_ANY = 562949953421311

ELEMENT_FACTORY_TYPE_AUDIOVIDEO_SINKS = 3940649673949188

ELEMENT_FACTORY_TYPE_AUDIO_ENCODER = 1125899906842626

ELEMENT_FACTORY_TYPE_DECODABLE = 1377
ELEMENT_FACTORY_TYPE_DECODER = 1
ELEMENT_FACTORY_TYPE_DECRYPTOR = 1024
ELEMENT_FACTORY_TYPE_DEMUXER = 32
ELEMENT_FACTORY_TYPE_DEPAYLOADER = 256
ELEMENT_FACTORY_TYPE_ENCODER = 2
ELEMENT_FACTORY_TYPE_ENCRYPTOR = 2048
ELEMENT_FACTORY_TYPE_FORMATTER = 512

ELEMENT_FACTORY_TYPE_MAX_ELEMENTS = 281474976710656

ELEMENT_FACTORY_TYPE_MEDIA_ANY = 18446462598732840960
ELEMENT_FACTORY_TYPE_MEDIA_AUDIO = 1125899906842624
ELEMENT_FACTORY_TYPE_MEDIA_IMAGE = 2251799813685248
ELEMENT_FACTORY_TYPE_MEDIA_METADATA = 9007199254740992
ELEMENT_FACTORY_TYPE_MEDIA_SUBTITLE = 4503599627370496
ELEMENT_FACTORY_TYPE_MEDIA_VIDEO = 562949953421312

ELEMENT_FACTORY_TYPE_MUXER = 16
ELEMENT_FACTORY_TYPE_PARSER = 64
ELEMENT_FACTORY_TYPE_PAYLOADER = 128
ELEMENT_FACTORY_TYPE_SINK = 4
ELEMENT_FACTORY_TYPE_SRC = 8

ELEMENT_FACTORY_TYPE_VIDEO_ENCODER = 2814749767106562

ELEMENT_METADATA_AUTHOR = 'author'
ELEMENT_METADATA_DESCRIPTION = 'description'

ELEMENT_METADATA_DOC_URI = 'doc-uri'

ELEMENT_METADATA_ICON_NAME = 'icon-name'

ELEMENT_METADATA_KLASS = 'klass'
ELEMENT_METADATA_LONGNAME = 'long-name'

EVENT_NUM_SHIFT = 8

EVENT_TYPE_BOTH = 0

FLAG_SET_MASK_EXACT = 4294967295

FORMAT_PERCENT_MAX = 1000000
FORMAT_PERCENT_SCALE = 10000

GROUP_ID_INVALID = 0

LICENSE_UNKNOWN = 'unknown'

LOCK_FLAG_READWRITE = 0

MAP_READWRITE = 0

META_TAG_MEMORY_STR = 'memory'

MSECOND = 1000000

NSECOND = 1

PARAM_CONTROLLABLE = 512

PARAM_MUTABLE_PAUSED = 2048
PARAM_MUTABLE_PLAYING = 4096
PARAM_MUTABLE_READY = 1024

PARAM_USER_SHIFT = 65536

PROTECTION_SYSTEM_ID_CAPS_FIELD = 'protection-system'

PROTECTION_UNSPECIFIED_SYSTEM_ID = 'unspecified-system-id'

QUERY_NUM_SHIFT = 8

QUERY_TYPE_BOTH = 0

SECOND = 1000000000

SEQNUM_INVALID = 0

TAG_ALBUM = 'album'

TAG_ALBUM_ARTIST = 'album-artist'

TAG_ALBUM_ARTIST_SORTNAME = 'album-artist-sortname'

TAG_ALBUM_GAIN = 'replaygain-album-gain'
TAG_ALBUM_PEAK = 'replaygain-album-peak'
TAG_ALBUM_SORTNAME = 'album-sortname'

TAG_ALBUM_VOLUME_COUNT = 'album-disc-count'
TAG_ALBUM_VOLUME_NUMBER = 'album-disc-number'

TAG_APPLICATION_DATA = 'application-data'
TAG_APPLICATION_NAME = 'application-name'

TAG_ARTIST = 'artist'

TAG_ARTIST_SORTNAME = 'artist-sortname'

TAG_ATTACHMENT = 'attachment'

TAG_AUDIO_CODEC = 'audio-codec'

TAG_BEATS_PER_MINUTE = 'beats-per-minute'

TAG_BITRATE = 'bitrate'
TAG_CODEC = 'codec'
TAG_COMMENT = 'comment'
TAG_COMPOSER = 'composer'

TAG_COMPOSER_SORTNAME = 'composer-sortname'

TAG_CONDUCTOR = 'conductor'
TAG_CONTACT = 'contact'

TAG_CONTAINER_FORMAT = 'container-format'

TAG_COPYRIGHT = 'copyright'

TAG_COPYRIGHT_URI = 'copyright-uri'

TAG_DATE = 'date'

TAG_DATE_TIME = 'datetime'

TAG_DESCRIPTION = 'description'

TAG_DEVICE_MANUFACTURER = 'device-manufacturer'
TAG_DEVICE_MODEL = 'device-model'

TAG_DURATION = 'duration'

TAG_ENCODED_BY = 'encoded-by'

TAG_ENCODER = 'encoder'

TAG_ENCODER_VERSION = 'encoder-version'

TAG_EXTENDED_COMMENT = 'extended-comment'

TAG_GENRE = 'genre'

TAG_GEO_LOCATION_CAPTURE_DIRECTION = 'geo-location-capture-direction'

TAG_GEO_LOCATION_CITY = 'geo-location-city'
TAG_GEO_LOCATION_COUNTRY = 'geo-location-country'
TAG_GEO_LOCATION_ELEVATION = 'geo-location-elevation'

TAG_GEO_LOCATION_HORIZONTAL_ERROR = 'geo-location-horizontal-error'

TAG_GEO_LOCATION_LATITUDE = 'geo-location-latitude'
TAG_GEO_LOCATION_LONGITUDE = 'geo-location-longitude'

TAG_GEO_LOCATION_MOVEMENT_DIRECTION = 'geo-location-movement-direction'
TAG_GEO_LOCATION_MOVEMENT_SPEED = 'geo-location-movement-speed'

TAG_GEO_LOCATION_NAME = 'geo-location-name'
TAG_GEO_LOCATION_SUBLOCATION = 'geo-location-sublocation'

TAG_GROUPING = 'grouping'
TAG_HOMEPAGE = 'homepage'
TAG_IMAGE = 'image'

TAG_IMAGE_ORIENTATION = 'image-orientation'

TAG_INTERPRETED_BY = 'interpreted-by'

TAG_ISRC = 'isrc'
TAG_KEYWORDS = 'keywords'

TAG_LANGUAGE_CODE = 'language-code'
TAG_LANGUAGE_NAME = 'language-name'

TAG_LICENSE = 'license'

TAG_LICENSE_URI = 'license-uri'

TAG_LOCATION = 'location'
TAG_LYRICS = 'lyrics'

TAG_MAXIMUM_BITRATE = 'maximum-bitrate'

TAG_MIDI_BASE_NOTE = 'midi-base-note'

TAG_MINIMUM_BITRATE = 'minimum-bitrate'

TAG_NOMINAL_BITRATE = 'nominal-bitrate'

TAG_ORGANIZATION = 'organization'
TAG_PERFORMER = 'performer'

TAG_PREVIEW_IMAGE = 'preview-image'

TAG_PRIVATE_DATA = 'private-data'

TAG_PUBLISHER = 'publisher'

TAG_REFERENCE_LEVEL = 'replaygain-reference-level'

TAG_SERIAL = 'serial'

TAG_SHOW_EPISODE_NUMBER = 'show-episode-number'

TAG_SHOW_NAME = 'show-name'

TAG_SHOW_SEASON_NUMBER = 'show-season-number'

TAG_SHOW_SORTNAME = 'show-sortname'

TAG_SUBTITLE_CODEC = 'subtitle-codec'

TAG_TITLE = 'title'

TAG_TITLE_SORTNAME = 'title-sortname'

TAG_TRACK_COUNT = 'track-count'
TAG_TRACK_GAIN = 'replaygain-track-gain'
TAG_TRACK_NUMBER = 'track-number'
TAG_TRACK_PEAK = 'replaygain-track-peak'

TAG_USER_RATING = 'user-rating'

TAG_VERSION = 'version'

TAG_VIDEO_CODEC = 'video-codec'

TOC_REPEAT_COUNT_INFINITE = -1

URI_NO_PORT = 0

USECOND = 1000

VALUE_EQUAL = 0

VALUE_GREATER_THAN = 1

VALUE_LESS_THAN = -1

VALUE_UNORDERED = 2

VERSION_MAJOR = 1
VERSION_MICRO = 2
VERSION_MINOR = 16
VERSION_NANO = 0

_namespace = 'Gst'

_version = '1.0'

__weakref__ = None

# functions

def buffer_get_max_memory(): # real signature unknown; restored from __doc__
    """ buffer_get_max_memory() -> int """
    return 0

def caps_features_from_string(features): # real signature unknown; restored from __doc__
    """ caps_features_from_string(features:str) -> Gst.CapsFeatures or None """
    pass

def caps_from_string(string): # real signature unknown; restored from __doc__
    """ caps_from_string(string:str) -> Gst.Caps or None """
    pass

def core_error_quark(): # real signature unknown; restored from __doc__
    """ core_error_quark() -> int """
    return 0

def debug_add_log_function(func, user_data=None): # real signature unknown; restored from __doc__
    """ debug_add_log_function(func:Gst.LogFunction, user_data=None) """
    pass

def debug_add_ring_buffer_logger(max_size_per_thread, thread_timeout): # real signature unknown; restored from __doc__
    """ debug_add_ring_buffer_logger(max_size_per_thread:int, thread_timeout:int) """
    pass

def debug_bin_to_dot_data(bin, details): # real signature unknown; restored from __doc__
    """ debug_bin_to_dot_data(bin:Gst.Bin, details:Gst.DebugGraphDetails) -> str """
    return ""

def debug_bin_to_dot_file(bin, details, file_name): # real signature unknown; restored from __doc__
    """ debug_bin_to_dot_file(bin:Gst.Bin, details:Gst.DebugGraphDetails, file_name:str) """
    pass

def debug_bin_to_dot_file_with_ts(bin, details, file_name): # real signature unknown; restored from __doc__
    """ debug_bin_to_dot_file_with_ts(bin:Gst.Bin, details:Gst.DebugGraphDetails, file_name:str) """
    pass

def debug_construct_term_color(colorinfo): # real signature unknown; restored from __doc__
    """ debug_construct_term_color(colorinfo:int) -> str """
    return ""

def debug_construct_win_color(colorinfo): # real signature unknown; restored from __doc__
    """ debug_construct_win_color(colorinfo:int) -> int """
    return 0

def debug_get_all_categories(): # real signature unknown; restored from __doc__
    """ debug_get_all_categories() -> list """
    return []

def debug_get_color_mode(): # real signature unknown; restored from __doc__
    """ debug_get_color_mode() -> Gst.DebugColorMode """
    pass

def debug_get_default_threshold(): # real signature unknown; restored from __doc__
    """ debug_get_default_threshold() -> Gst.DebugLevel """
    pass

def debug_get_stack_trace(flags): # real signature unknown; restored from __doc__
    """ debug_get_stack_trace(flags:Gst.StackTraceFlags) -> str or None """
    return ""

def debug_is_active(): # real signature unknown; restored from __doc__
    """ debug_is_active() -> bool """
    return False

def debug_is_colored(): # real signature unknown; restored from __doc__
    """ debug_is_colored() -> bool """
    return False

def debug_level_get_name(level): # real signature unknown; restored from __doc__
    """ debug_level_get_name(level:Gst.DebugLevel) -> str """
    return ""

def debug_log_default(category, level, file, function, line, p_object=None, message, user_data=None): # real signature unknown; restored from __doc__
    """ debug_log_default(category:Gst.DebugCategory, level:Gst.DebugLevel, file:str, function:str, line:int, object:GObject.Object=None, message:Gst.DebugMessage, user_data=None) """
    pass

def debug_print_stack_trace(): # real signature unknown; restored from __doc__
    """ debug_print_stack_trace() """
    pass

def debug_remove_log_function(func=None): # real signature unknown; restored from __doc__
    """ debug_remove_log_function(func:Gst.LogFunction=None) -> int """
    return 0

def debug_remove_log_function_by_data(data=None): # real signature unknown; restored from __doc__
    """ debug_remove_log_function_by_data(data=None) -> int """
    return 0

def debug_remove_ring_buffer_logger(): # real signature unknown; restored from __doc__
    """ debug_remove_ring_buffer_logger() """
    pass

def debug_ring_buffer_logger_get_logs(): # real signature unknown; restored from __doc__
    """ debug_ring_buffer_logger_get_logs() -> list """
    return []

def debug_set_active(active): # real signature unknown; restored from __doc__
    """ debug_set_active(active:bool) """
    pass

def debug_set_colored(colored): # real signature unknown; restored from __doc__
    """ debug_set_colored(colored:bool) """
    pass

def debug_set_color_mode(mode): # real signature unknown; restored from __doc__
    """ debug_set_color_mode(mode:Gst.DebugColorMode) """
    pass

def debug_set_color_mode_from_string(mode): # real signature unknown; restored from __doc__
    """ debug_set_color_mode_from_string(mode:str) """
    pass

def debug_set_default_threshold(level): # real signature unknown; restored from __doc__
    """ debug_set_default_threshold(level:Gst.DebugLevel) """
    pass

def debug_set_threshold_for_name(name, level): # real signature unknown; restored from __doc__
    """ debug_set_threshold_for_name(name:str, level:Gst.DebugLevel) """
    pass

def debug_set_threshold_from_string(p_list, reset): # real signature unknown; restored from __doc__
    """ debug_set_threshold_from_string(list:str, reset:bool) """
    pass

def debug_unset_threshold_for_name(name): # real signature unknown; restored from __doc__
    """ debug_unset_threshold_for_name(name:str) """
    pass

def deinit(): # real signature unknown; restored from __doc__
    """ deinit() """
    pass

def dynamic_type_register(plugin, type): # real signature unknown; restored from __doc__
    """ dynamic_type_register(plugin:Gst.Plugin, type:GType) -> bool """
    return False

def error_get_message(domain, code): # real signature unknown; restored from __doc__
    """ error_get_message(domain:int, code:int) -> str """
    return ""

def event_type_get_flags(type): # real signature unknown; restored from __doc__
    """ event_type_get_flags(type:Gst.EventType) -> Gst.EventTypeFlags """
    pass

def event_type_get_name(type): # real signature unknown; restored from __doc__
    """ event_type_get_name(type:Gst.EventType) -> str """
    return ""

def event_type_to_quark(type): # real signature unknown; restored from __doc__
    """ event_type_to_quark(type:Gst.EventType) -> int """
    return 0

def filename_to_uri(filename): # real signature unknown; restored from __doc__
    """ filename_to_uri(filename:str) -> str """
    return ""

def flow_get_name(ret): # real signature unknown; restored from __doc__
    """ flow_get_name(ret:Gst.FlowReturn) -> str """
    return ""

def flow_to_quark(ret): # real signature unknown; restored from __doc__
    """ flow_to_quark(ret:Gst.FlowReturn) -> int """
    return 0

def formats_contains(formats, format): # real signature unknown; restored from __doc__
    """ formats_contains(formats:list, format:Gst.Format) -> bool """
    return False

def format_get_by_nick(nick): # real signature unknown; restored from __doc__
    """ format_get_by_nick(nick:str) -> Gst.Format """
    pass

def format_get_details(format): # real signature unknown; restored from __doc__
    """ format_get_details(format:Gst.Format) -> Gst.FormatDefinition or None """
    pass

def format_get_name(format): # real signature unknown; restored from __doc__
    """ format_get_name(format:Gst.Format) -> str or None """
    return ""

def format_iterate_definitions(): # real signature unknown; restored from __doc__
    """ format_iterate_definitions() -> Gst.Iterator """
    pass

def format_register(nick, description): # real signature unknown; restored from __doc__
    """ format_register(nick:str, description:str) -> Gst.Format """
    pass

def format_to_quark(format): # real signature unknown; restored from __doc__
    """ format_to_quark(format:Gst.Format) -> int """
    return 0

def get_main_executable_path(): # real signature unknown; restored from __doc__
    """ get_main_executable_path() -> str or None """
    return ""

def init(argv=None): # real signature unknown; restored from __doc__
    """ init(argv:list=None) -> argv:list """
    pass

def init_check(argv=None): # real signature unknown; restored from __doc__
    """ init_check(argv:list=None) -> bool, argv:list """
    return False

def is_caps_features(obj=None): # real signature unknown; restored from __doc__
    """ is_caps_features(obj=None) -> bool """
    return False

def is_initialized(): # real signature unknown; restored from __doc__
    """ is_initialized() -> bool """
    return False

def library_error_quark(): # real signature unknown; restored from __doc__
    """ library_error_quark() -> int """
    return 0

def message_type_get_name(type): # real signature unknown; restored from __doc__
    """ message_type_get_name(type:Gst.MessageType) -> str """
    return ""

def message_type_to_quark(type): # real signature unknown; restored from __doc__
    """ message_type_to_quark(type:Gst.MessageType) -> int """
    return 0

def meta_api_type_get_tags(api): # real signature unknown; restored from __doc__
    """ meta_api_type_get_tags(api:GType) -> list """
    return []

def meta_api_type_has_tag(api, tag): # real signature unknown; restored from __doc__
    """ meta_api_type_has_tag(api:GType, tag:int) -> bool """
    return False

def meta_api_type_register(api, tags): # real signature unknown; restored from __doc__
    """ meta_api_type_register(api:str, tags:list) -> GType """
    pass

def meta_get_info(impl): # real signature unknown; restored from __doc__
    """ meta_get_info(impl:str) -> Gst.MetaInfo or None """
    pass

def meta_register(api, impl, size, init_func, free_func, transform_func): # real signature unknown; restored from __doc__
    """ meta_register(api:GType, impl:str, size:int, init_func:Gst.MetaInitFunction, free_func:Gst.MetaFreeFunction, transform_func:Gst.MetaTransformFunction) -> Gst.MetaInfo or None """
    pass

def mini_object_replace(olddata=None, newdata=None): # real signature unknown; restored from __doc__
    """ mini_object_replace(olddata:Gst.MiniObject=None, newdata:Gst.MiniObject=None) -> bool, olddata:Gst.MiniObject """
    return False

def mini_object_take(olddata, newdata): # real signature unknown; restored from __doc__
    """ mini_object_take(olddata:Gst.MiniObject, newdata:Gst.MiniObject) -> bool, olddata:Gst.MiniObject """
    return False

def pad_mode_get_name(mode): # real signature unknown; restored from __doc__
    """ pad_mode_get_name(mode:Gst.PadMode) -> str """
    return ""

def param_spec_array(name, nick, blurb, element_spec, flags): # real signature unknown; restored from __doc__
    """ param_spec_array(name:str, nick:str, blurb:str, element_spec:GObject.ParamSpec, flags:GObject.ParamFlags) -> GObject.ParamSpec """
    pass

def param_spec_fraction(name, nick, blurb, min_num, min_denom, max_num, max_denom, default_num, default_denom, flags): # real signature unknown; restored from __doc__
    """ param_spec_fraction(name:str, nick:str, blurb:str, min_num:int, min_denom:int, max_num:int, max_denom:int, default_num:int, default_denom:int, flags:GObject.ParamFlags) -> GObject.ParamSpec or None """
    pass

def parent_buffer_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ parent_buffer_meta_api_get_type() -> GType """
    pass

def parent_buffer_meta_get_info(): # real signature unknown; restored from __doc__
    """ parent_buffer_meta_get_info() -> Gst.MetaInfo """
    pass

def parse_bin_from_description(bin_description, ghost_unlinked_pads): # real signature unknown; restored from __doc__
    """ parse_bin_from_description(bin_description:str, ghost_unlinked_pads:bool) -> Gst.Bin or None """
    pass

def parse_bin_from_description_full(bin_description, ghost_unlinked_pads, context=None, flags): # real signature unknown; restored from __doc__
    """ parse_bin_from_description_full(bin_description:str, ghost_unlinked_pads:bool, context:Gst.ParseContext=None, flags:Gst.ParseFlags) -> Gst.Element or None """
    pass

def parse_error_quark(): # real signature unknown; restored from __doc__
    """ parse_error_quark() -> int """
    return 0

def parse_launch(pipeline_description): # real signature unknown; restored from __doc__
    """ parse_launch(pipeline_description:str) -> Gst.Element or None """
    pass

def parse_launchv(argv): # real signature unknown; restored from __doc__
    """ parse_launchv(argv:list) -> Gst.Element or None """
    pass

def parse_launchv_full(argv, context=None, flags): # real signature unknown; restored from __doc__
    """ parse_launchv_full(argv:list, context:Gst.ParseContext=None, flags:Gst.ParseFlags) -> Gst.Element or None """
    pass

def parse_launch_full(pipeline_description, context=None, flags): # real signature unknown; restored from __doc__
    """ parse_launch_full(pipeline_description:str, context:Gst.ParseContext=None, flags:Gst.ParseFlags) -> Gst.Element or None """
    pass

def plugin_error_quark(): # real signature unknown; restored from __doc__
    """ plugin_error_quark() -> int """
    return 0

def preset_get_app_dir(): # real signature unknown; restored from __doc__
    """ preset_get_app_dir() -> str or None """
    return ""

def preset_set_app_dir(app_dir): # real signature unknown; restored from __doc__
    """ preset_set_app_dir(app_dir:str) -> bool """
    return False

def protection_filter_systems_by_available_decryptors(system_identifiers): # real signature unknown; restored from __doc__
    """ protection_filter_systems_by_available_decryptors(system_identifiers:list) -> list or None """
    return []

def protection_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ protection_meta_api_get_type() -> GType """
    pass

def protection_meta_get_info(): # real signature unknown; restored from __doc__
    """ protection_meta_get_info() -> Gst.MetaInfo """
    pass

def protection_select_system(system_identifiers): # real signature unknown; restored from __doc__
    """ protection_select_system(system_identifiers:list) -> str or None """
    return ""

def query_type_get_flags(type): # real signature unknown; restored from __doc__
    """ query_type_get_flags(type:Gst.QueryType) -> Gst.QueryTypeFlags """
    pass

def query_type_get_name(type): # real signature unknown; restored from __doc__
    """ query_type_get_name(type:Gst.QueryType) -> str """
    return ""

def query_type_to_quark(type): # real signature unknown; restored from __doc__
    """ query_type_to_quark(type:Gst.QueryType) -> int """
    return 0

def reference_timestamp_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ reference_timestamp_meta_api_get_type() -> GType """
    pass

def reference_timestamp_meta_get_info(): # real signature unknown; restored from __doc__
    """ reference_timestamp_meta_get_info() -> Gst.MetaInfo """
    pass

def resource_error_quark(): # real signature unknown; restored from __doc__
    """ resource_error_quark() -> int """
    return 0

def segtrap_is_enabled(): # real signature unknown; restored from __doc__
    """ segtrap_is_enabled() -> bool """
    return False

def segtrap_set_enabled(enabled): # real signature unknown; restored from __doc__
    """ segtrap_set_enabled(enabled:bool) """
    pass

def state_change_get_name(transition): # real signature unknown; restored from __doc__
    """ state_change_get_name(transition:Gst.StateChange) -> str """
    return ""

def static_caps_get_type(): # real signature unknown; restored from __doc__
    """ static_caps_get_type() -> GType """
    pass

def static_pad_template_get_type(): # real signature unknown; restored from __doc__
    """ static_pad_template_get_type() -> GType """
    pass

def stream_error_quark(): # real signature unknown; restored from __doc__
    """ stream_error_quark() -> int """
    return 0

def stream_type_get_name(stype): # real signature unknown; restored from __doc__
    """ stream_type_get_name(stype:Gst.StreamType) -> str or None """
    return ""

def structure_from_string(string): # real signature unknown; restored from __doc__
    """ structure_from_string(string:str) -> Gst.Structure or None, end:str """
    pass

def tag_exists(tag): # real signature unknown; restored from __doc__
    """ tag_exists(tag:str) -> bool """
    return False

def tag_get_description(tag): # real signature unknown; restored from __doc__
    """ tag_get_description(tag:str) -> str or None """
    return ""

def tag_get_flag(tag): # real signature unknown; restored from __doc__
    """ tag_get_flag(tag:str) -> Gst.TagFlag """
    pass

def tag_get_nick(tag): # real signature unknown; restored from __doc__
    """ tag_get_nick(tag:str) -> str or None """
    return ""

def tag_get_type(tag): # real signature unknown; restored from __doc__
    """ tag_get_type(tag:str) -> GType """
    pass

def tag_is_fixed(tag): # real signature unknown; restored from __doc__
    """ tag_is_fixed(tag:str) -> bool """
    return False

def tag_list_copy_value(p_list, tag): # real signature unknown; restored from __doc__
    """ tag_list_copy_value(list:Gst.TagList, tag:str) -> bool, dest:GObject.Value """
    return False

def tag_merge_strings_with_comma(src): # real signature unknown; restored from __doc__
    """ tag_merge_strings_with_comma(src:GObject.Value) -> dest:GObject.Value """
    pass

def tag_merge_use_first(src): # real signature unknown; restored from __doc__
    """ tag_merge_use_first(src:GObject.Value) -> dest:GObject.Value """
    pass

def toc_entry_type_get_nick(type): # real signature unknown; restored from __doc__
    """ toc_entry_type_get_nick(type:Gst.TocEntryType) -> str """
    return ""

def type_find_get_type(): # real signature unknown; restored from __doc__
    """ type_find_get_type() -> GType """
    pass

def type_find_register(plugin=None, name, rank, func, extensions=None, possible_caps, data=None): # real signature unknown; restored from __doc__
    """ type_find_register(plugin:Gst.Plugin=None, name:str, rank:int, func:Gst.TypeFindFunction, extensions:str=None, possible_caps:Gst.Caps, data=None) -> bool """
    return False

def update_registry(): # real signature unknown; restored from __doc__
    """ update_registry() -> bool """
    return False

def uri_construct(protocol, location): # real signature unknown; restored from __doc__
    """ uri_construct(protocol:str, location:str) -> str """
    return ""

def uri_error_quark(): # real signature unknown; restored from __doc__
    """ uri_error_quark() -> int """
    return 0

def uri_from_string(uri): # real signature unknown; restored from __doc__
    """ uri_from_string(uri:str) -> Gst.Uri or None """
    pass

def uri_get_location(uri): # real signature unknown; restored from __doc__
    """ uri_get_location(uri:str) -> str or None """
    return ""

def uri_get_protocol(uri): # real signature unknown; restored from __doc__
    """ uri_get_protocol(uri:str) -> str or None """
    return ""

def uri_has_protocol(uri, protocol): # real signature unknown; restored from __doc__
    """ uri_has_protocol(uri:str, protocol:str) -> bool """
    return False

def uri_is_valid(uri): # real signature unknown; restored from __doc__
    """ uri_is_valid(uri:str) -> bool """
    return False

def uri_join_strings(base_uri, ref_uri): # real signature unknown; restored from __doc__
    """ uri_join_strings(base_uri:str, ref_uri:str) -> str """
    return ""

def uri_protocol_is_supported(type, protocol): # real signature unknown; restored from __doc__
    """ uri_protocol_is_supported(type:Gst.URIType, protocol:str) -> bool """
    return False

def uri_protocol_is_valid(protocol): # real signature unknown; restored from __doc__
    """ uri_protocol_is_valid(protocol:str) -> bool """
    return False

def util_array_binary_search(array=None, num_elements, element_size, search_func, mode, search_data=None, user_data=None): # real signature unknown; restored from __doc__
    """ util_array_binary_search(array=None, num_elements:int, element_size:int, search_func:GLib.CompareDataFunc, mode:Gst.SearchMode, search_data=None, user_data=None) """
    pass

def util_double_to_fraction(src): # real signature unknown; restored from __doc__
    """ util_double_to_fraction(src:float) -> dest_n:int, dest_d:int """
    pass

def util_dump_buffer(buf): # real signature unknown; restored from __doc__
    """ util_dump_buffer(buf:Gst.Buffer) """
    pass

def util_dump_mem(mem): # real signature unknown; restored from __doc__
    """ util_dump_mem(mem:list) """
    pass

def util_fraction_add(a_n, a_d, b_n, b_d): # real signature unknown; restored from __doc__
    """ util_fraction_add(a_n:int, a_d:int, b_n:int, b_d:int) -> bool, res_n:int, res_d:int """
    return False

def util_fraction_compare(a_n, a_d, b_n, b_d): # real signature unknown; restored from __doc__
    """ util_fraction_compare(a_n:int, a_d:int, b_n:int, b_d:int) -> int """
    return 0

def util_fraction_multiply(a_n, a_d, b_n, b_d): # real signature unknown; restored from __doc__
    """ util_fraction_multiply(a_n:int, a_d:int, b_n:int, b_d:int) -> bool, res_n:int, res_d:int """
    return False

def util_fraction_to_double(src_n, src_d): # real signature unknown; restored from __doc__
    """ util_fraction_to_double(src_n:int, src_d:int) -> dest:float """
    pass

def util_gdouble_to_guint64(value): # real signature unknown; restored from __doc__
    """ util_gdouble_to_guint64(value:float) -> int """
    return 0

def util_get_object_array(p_object, name): # real signature unknown; restored from __doc__
    """ util_get_object_array(object:GObject.Object, name:str) -> bool, array:GObject.ValueArray """
    return False

def util_get_timestamp(): # real signature unknown; restored from __doc__
    """ util_get_timestamp() -> int """
    return 0

def util_greatest_common_divisor(a, b): # real signature unknown; restored from __doc__
    """ util_greatest_common_divisor(a:int, b:int) -> int """
    return 0

def util_greatest_common_divisor_int64(a, b): # real signature unknown; restored from __doc__
    """ util_greatest_common_divisor_int64(a:int, b:int) -> int """
    return 0

def util_group_id_next(): # real signature unknown; restored from __doc__
    """ util_group_id_next() -> int """
    return 0

def util_guint64_to_gdouble(value): # real signature unknown; restored from __doc__
    """ util_guint64_to_gdouble(value:int) -> float """
    return 0.0

def util_seqnum_compare(s1, s2): # real signature unknown; restored from __doc__
    """ util_seqnum_compare(s1:int, s2:int) -> int """
    return 0

def util_seqnum_next(): # real signature unknown; restored from __doc__
    """ util_seqnum_next() -> int """
    return 0

def util_set_object_arg(p_object, name, value): # real signature unknown; restored from __doc__
    """ util_set_object_arg(object:GObject.Object, name:str, value:str) """
    pass

def util_set_object_array(p_object, name, array): # real signature unknown; restored from __doc__
    """ util_set_object_array(object:GObject.Object, name:str, array:GObject.ValueArray) -> bool """
    return False

def util_set_value_from_string(value_str): # real signature unknown; restored from __doc__
    """ util_set_value_from_string(value_str:str) -> value:GObject.Value """
    pass

def util_uint64_scale(val, num, denom): # real signature unknown; restored from __doc__
    """ util_uint64_scale(val:int, num:int, denom:int) -> int """
    return 0

def util_uint64_scale_ceil(val, num, denom): # real signature unknown; restored from __doc__
    """ util_uint64_scale_ceil(val:int, num:int, denom:int) -> int """
    return 0

def util_uint64_scale_int(val, num, denom): # real signature unknown; restored from __doc__
    """ util_uint64_scale_int(val:int, num:int, denom:int) -> int """
    return 0

def util_uint64_scale_int_ceil(val, num, denom): # real signature unknown; restored from __doc__
    """ util_uint64_scale_int_ceil(val:int, num:int, denom:int) -> int """
    return 0

def util_uint64_scale_int_round(val, num, denom): # real signature unknown; restored from __doc__
    """ util_uint64_scale_int_round(val:int, num:int, denom:int) -> int """
    return 0

def util_uint64_scale_round(val, num, denom): # real signature unknown; restored from __doc__
    """ util_uint64_scale_round(val:int, num:int, denom:int) -> int """
    return 0

def value_can_compare(value1, value2): # real signature unknown; restored from __doc__
    """ value_can_compare(value1:GObject.Value, value2:GObject.Value) -> bool """
    return False

def value_can_intersect(value1, value2): # real signature unknown; restored from __doc__
    """ value_can_intersect(value1:GObject.Value, value2:GObject.Value) -> bool """
    return False

def value_can_subtract(minuend, subtrahend): # real signature unknown; restored from __doc__
    """ value_can_subtract(minuend:GObject.Value, subtrahend:GObject.Value) -> bool """
    return False

def value_can_union(value1, value2): # real signature unknown; restored from __doc__
    """ value_can_union(value1:GObject.Value, value2:GObject.Value) -> bool """
    return False

def value_compare(value1, value2): # real signature unknown; restored from __doc__
    """ value_compare(value1:GObject.Value, value2:GObject.Value) -> int """
    return 0

def value_deserialize(src): # real signature unknown; restored from __doc__
    """ value_deserialize(src:str) -> bool, dest:GObject.Value """
    return False

def value_fixate(dest, src): # real signature unknown; restored from __doc__
    """ value_fixate(dest:GObject.Value, src:GObject.Value) -> bool """
    return False

def value_fraction_multiply(product, factor1, factor2): # real signature unknown; restored from __doc__
    """ value_fraction_multiply(product:GObject.Value, factor1:GObject.Value, factor2:GObject.Value) -> bool """
    return False

def value_fraction_subtract(dest, minuend, subtrahend): # real signature unknown; restored from __doc__
    """ value_fraction_subtract(dest:GObject.Value, minuend:GObject.Value, subtrahend:GObject.Value) -> bool """
    return False

def value_get_bitmask(value): # real signature unknown; restored from __doc__
    """ value_get_bitmask(value:GObject.Value) -> int """
    return 0

def value_get_caps(value): # real signature unknown; restored from __doc__
    """ value_get_caps(value:GObject.Value) -> Gst.Caps """
    pass

def value_get_caps_features(value): # real signature unknown; restored from __doc__
    """ value_get_caps_features(value:GObject.Value) -> Gst.CapsFeatures """
    pass

def value_get_double_range_max(value): # real signature unknown; restored from __doc__
    """ value_get_double_range_max(value:GObject.Value) -> float """
    return 0.0

def value_get_double_range_min(value): # real signature unknown; restored from __doc__
    """ value_get_double_range_min(value:GObject.Value) -> float """
    return 0.0

def value_get_flagset_flags(value): # real signature unknown; restored from __doc__
    """ value_get_flagset_flags(value:GObject.Value) -> int """
    return 0

def value_get_flagset_mask(value): # real signature unknown; restored from __doc__
    """ value_get_flagset_mask(value:GObject.Value) -> int """
    return 0

def value_get_fraction_denominator(value): # real signature unknown; restored from __doc__
    """ value_get_fraction_denominator(value:GObject.Value) -> int """
    return 0

def value_get_fraction_numerator(value): # real signature unknown; restored from __doc__
    """ value_get_fraction_numerator(value:GObject.Value) -> int """
    return 0

def value_get_fraction_range_max(value): # real signature unknown; restored from __doc__
    """ value_get_fraction_range_max(value:GObject.Value) -> GObject.Value or None """
    pass

def value_get_fraction_range_min(value): # real signature unknown; restored from __doc__
    """ value_get_fraction_range_min(value:GObject.Value) -> GObject.Value or None """
    pass

def value_get_int64_range_max(value): # real signature unknown; restored from __doc__
    """ value_get_int64_range_max(value:GObject.Value) -> int """
    return 0

def value_get_int64_range_min(value): # real signature unknown; restored from __doc__
    """ value_get_int64_range_min(value:GObject.Value) -> int """
    return 0

def value_get_int64_range_step(value): # real signature unknown; restored from __doc__
    """ value_get_int64_range_step(value:GObject.Value) -> int """
    return 0

def value_get_int_range_max(value): # real signature unknown; restored from __doc__
    """ value_get_int_range_max(value:GObject.Value) -> int """
    return 0

def value_get_int_range_min(value): # real signature unknown; restored from __doc__
    """ value_get_int_range_min(value:GObject.Value) -> int """
    return 0

def value_get_int_range_step(value): # real signature unknown; restored from __doc__
    """ value_get_int_range_step(value:GObject.Value) -> int """
    return 0

def value_get_structure(value): # real signature unknown; restored from __doc__
    """ value_get_structure(value:GObject.Value) -> Gst.Structure """
    pass

def value_init_and_copy(src): # real signature unknown; restored from __doc__
    """ value_init_and_copy(src:GObject.Value) -> dest:GObject.Value """
    pass

def value_intersect(value1, value2): # real signature unknown; restored from __doc__
    """ value_intersect(value1:GObject.Value, value2:GObject.Value) -> bool, dest:GObject.Value """
    return False

def value_is_fixed(value): # real signature unknown; restored from __doc__
    """ value_is_fixed(value:GObject.Value) -> bool """
    return False

def value_is_subset(value1, value2): # real signature unknown; restored from __doc__
    """ value_is_subset(value1:GObject.Value, value2:GObject.Value) -> bool """
    return False

def value_register(table): # real signature unknown; restored from __doc__
    """ value_register(table:Gst.ValueTable) """
    pass

def value_serialize(value): # real signature unknown; restored from __doc__
    """ value_serialize(value:GObject.Value) -> str or None """
    return ""

def value_set_bitmask(value, bitmask): # real signature unknown; restored from __doc__
    """ value_set_bitmask(value:GObject.Value, bitmask:int) """
    pass

def value_set_caps(value, caps): # real signature unknown; restored from __doc__
    """ value_set_caps(value:GObject.Value, caps:Gst.Caps) """
    pass

def value_set_caps_features(value, features): # real signature unknown; restored from __doc__
    """ value_set_caps_features(value:GObject.Value, features:Gst.CapsFeatures) """
    pass

def value_set_double_range(value, start, end): # real signature unknown; restored from __doc__
    """ value_set_double_range(value:GObject.Value, start:float, end:float) """
    pass

def value_set_flagset(value, flags, mask): # real signature unknown; restored from __doc__
    """ value_set_flagset(value:GObject.Value, flags:int, mask:int) """
    pass

def value_set_fraction(value, numerator, denominator): # real signature unknown; restored from __doc__
    """ value_set_fraction(value:GObject.Value, numerator:int, denominator:int) """
    pass

def value_set_fraction_range(value, start, end): # real signature unknown; restored from __doc__
    """ value_set_fraction_range(value:GObject.Value, start:GObject.Value, end:GObject.Value) """
    pass

def value_set_fraction_range_full(value, numerator_start, denominator_start, numerator_end, denominator_end): # real signature unknown; restored from __doc__
    """ value_set_fraction_range_full(value:GObject.Value, numerator_start:int, denominator_start:int, numerator_end:int, denominator_end:int) """
    pass

def value_set_int64_range(value, start, end): # real signature unknown; restored from __doc__
    """ value_set_int64_range(value:GObject.Value, start:int, end:int) """
    pass

def value_set_int64_range_step(value, start, end, step): # real signature unknown; restored from __doc__
    """ value_set_int64_range_step(value:GObject.Value, start:int, end:int, step:int) """
    pass

def value_set_int_range(value, start, end): # real signature unknown; restored from __doc__
    """ value_set_int_range(value:GObject.Value, start:int, end:int) """
    pass

def value_set_int_range_step(value, start, end, step): # real signature unknown; restored from __doc__
    """ value_set_int_range_step(value:GObject.Value, start:int, end:int, step:int) """
    pass

def value_set_structure(value, structure): # real signature unknown; restored from __doc__
    """ value_set_structure(value:GObject.Value, structure:Gst.Structure) """
    pass

def value_subtract(minuend, subtrahend): # real signature unknown; restored from __doc__
    """ value_subtract(minuend:GObject.Value, subtrahend:GObject.Value) -> bool, dest:GObject.Value """
    return False

def value_union(value1, value2): # real signature unknown; restored from __doc__
    """ value_union(value1:GObject.Value, value2:GObject.Value) -> bool, dest:GObject.Value """
    return False

def version(): # real signature unknown; restored from __doc__
    """ version() -> major:int, minor:int, micro:int, nano:int """
    pass

def version_string(): # real signature unknown; restored from __doc__
    """ version_string() -> str """
    return ""

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

from .AllocationParams import AllocationParams
from .Object import Object
from .Allocator import Allocator
from .AllocatorClass import AllocatorClass
from .AllocatorFlags import AllocatorFlags
from .AllocatorPrivate import AllocatorPrivate
from .AtomicQueue import AtomicQueue
from .ChildProxy import ChildProxy
from .Element import Element
from .Bin import Bin
from .BinClass import BinClass
from .BinFlags import BinFlags
from .BinPrivate import BinPrivate
from .Bitmask import Bitmask
from .Buffer import Buffer
from .BufferCopyFlags import BufferCopyFlags
from .BufferFlags import BufferFlags
from .BufferingMode import BufferingMode
from .BufferList import BufferList
from .BufferPool import BufferPool
from .BufferPoolAcquireFlags import BufferPoolAcquireFlags
from .BufferPoolAcquireParams import BufferPoolAcquireParams
from .BufferPoolClass import BufferPoolClass
from .BufferPoolPrivate import BufferPoolPrivate
from .Bus import Bus
from .BusClass import BusClass
from .BusFlags import BusFlags
from .BusPrivate import BusPrivate
from .BusSyncReply import BusSyncReply
from .Caps import Caps
from .CapsFeatures import CapsFeatures
from .CapsFlags import CapsFlags
from .CapsIntersectMode import CapsIntersectMode
from .ChildProxyInterface import ChildProxyInterface
from .Clock import Clock
from .ClockClass import ClockClass
from .ClockEntry import ClockEntry
from .ClockEntryType import ClockEntryType
from .ClockFlags import ClockFlags
from .ClockPrivate import ClockPrivate
from .ClockReturn import ClockReturn
from .ClockType import ClockType
from .Context import Context
from .ControlBinding import ControlBinding
from .ControlBindingClass import ControlBindingClass
from .ControlBindingPrivate import ControlBindingPrivate
from .ControlSource import ControlSource
from .ControlSourceClass import ControlSourceClass
from .CoreError import CoreError
from .DateTime import DateTime
from .DebugCategory import DebugCategory
from .DebugColorFlags import DebugColorFlags
from .DebugColorMode import DebugColorMode
from .DebugGraphDetails import DebugGraphDetails
from .DebugLevel import DebugLevel
from .DebugMessage import DebugMessage
from .Device import Device
from .DeviceClass import DeviceClass
from .DeviceMonitor import DeviceMonitor
from .DeviceMonitorClass import DeviceMonitorClass
from .DeviceMonitorPrivate import DeviceMonitorPrivate
from .DevicePrivate import DevicePrivate
from .DeviceProvider import DeviceProvider
from .DeviceProviderClass import DeviceProviderClass
from .PluginFeature import PluginFeature
from .DeviceProviderFactory import DeviceProviderFactory
from .DeviceProviderFactoryClass import DeviceProviderFactoryClass
from .DeviceProviderPrivate import DeviceProviderPrivate
from .DoubleRange import DoubleRange
from .DynamicTypeFactory import DynamicTypeFactory
from .DynamicTypeFactoryClass import DynamicTypeFactoryClass
from .ElementClass import ElementClass
from .ElementFactory import ElementFactory
from .ElementFactoryClass import ElementFactoryClass
from .ElementFlags import ElementFlags
from .Event import Event
from .EventType import EventType
from .EventTypeFlags import EventTypeFlags
from .FlagSet import FlagSet
from .FlowReturn import FlowReturn
from .Format import Format
from .FormatDefinition import FormatDefinition
from .Fraction import Fraction
from .FractionRange import FractionRange
from .Pad import Pad
from .ProxyPad import ProxyPad
from .GhostPad import GhostPad
from .GhostPadClass import GhostPadClass
from .GhostPadPrivate import GhostPadPrivate
from .Int64Range import Int64Range
from .IntRange import IntRange
from .Iterator import Iterator
from .IteratorItem import IteratorItem
from .IteratorResult import IteratorResult
from .LibraryError import LibraryError
from .LockFlags import LockFlags
from .MapFlags import MapFlags
from .MapInfo import MapInfo
from .Memory import Memory
from .MemoryFlags import MemoryFlags
from .Message import Message
from .MessageType import MessageType
from .Meta import Meta
from .MetaFlags import MetaFlags
from .MetaInfo import MetaInfo
from .MetaTransformCopy import MetaTransformCopy
from .MiniObject import MiniObject
from .MiniObjectFlags import MiniObjectFlags
from .ObjectClass import ObjectClass
from .ObjectFlags import ObjectFlags
from .PadClass import PadClass
from .PadDirection import PadDirection
from .PadFlags import PadFlags
from .PadLinkCheck import PadLinkCheck
from .PadLinkReturn import PadLinkReturn
from .PadMode import PadMode
from .PadPresence import PadPresence
from .PadPrivate import PadPrivate
from .PadProbeInfo import PadProbeInfo
from .PadProbeReturn import PadProbeReturn
from .PadProbeType import PadProbeType
from .PadTemplate import PadTemplate
from .PadTemplateClass import PadTemplateClass
from .PadTemplateFlags import PadTemplateFlags
from .ParamArray import ParamArray
from .ParamFraction import ParamFraction
from .ParamSpecArray import ParamSpecArray
from .ParamSpecFraction import ParamSpecFraction
from .ParentBufferMeta import ParentBufferMeta
from .ParseContext import ParseContext
from .ParseError import ParseError
from .ParseFlags import ParseFlags
from .Pipeline import Pipeline
from .PipelineClass import PipelineClass
from .PipelineFlags import PipelineFlags
from .PipelinePrivate import PipelinePrivate
from .Plugin import Plugin
from .PluginClass import PluginClass
from .PluginDependencyFlags import PluginDependencyFlags
from .PluginDesc import PluginDesc
from .PluginError import PluginError
from .PluginFeatureClass import PluginFeatureClass
from .PluginFlags import PluginFlags
from .Poll import Poll
from .PollFD import PollFD
from .Preset import Preset
from .PresetInterface import PresetInterface
from .ProgressType import ProgressType
from .Promise import Promise
from .PromiseResult import PromiseResult
from .ProtectionMeta import ProtectionMeta
from .ProxyPadClass import ProxyPadClass
from .ProxyPadPrivate import ProxyPadPrivate
from .QOSType import QOSType
from .Query import Query
from .QueryType import QueryType
from .QueryTypeFlags import QueryTypeFlags
from .Rank import Rank
from .ReferenceTimestampMeta import ReferenceTimestampMeta
from .Registry import Registry
from .RegistryClass import RegistryClass
from .RegistryPrivate import RegistryPrivate
from .ResourceError import ResourceError
from .Sample import Sample
from .SchedulingFlags import SchedulingFlags
from .SearchMode import SearchMode
from .SeekFlags import SeekFlags
from .SeekType import SeekType
from .Segment import Segment
from .SegmentFlags import SegmentFlags
from .StackTraceFlags import StackTraceFlags
from .State import State
from .StateChange import StateChange
from .StateChangeReturn import StateChangeReturn
from .StaticCaps import StaticCaps
from .StaticPadTemplate import StaticPadTemplate
from .Stream import Stream
from .StreamClass import StreamClass
from .StreamCollection import StreamCollection
from .StreamCollectionClass import StreamCollectionClass
from .StreamCollectionPrivate import StreamCollectionPrivate
from .StreamError import StreamError
from .StreamFlags import StreamFlags
from .StreamPrivate import StreamPrivate
from .StreamStatusType import StreamStatusType
from .StreamType import StreamType
from .Structure import Structure
from .StructureChangeType import StructureChangeType
from .SystemClock import SystemClock
from .SystemClockClass import SystemClockClass
from .SystemClockPrivate import SystemClockPrivate
from .TagFlag import TagFlag
from .TagList import TagList
from .TagMergeMode import TagMergeMode
from .TagScope import TagScope
from .TagSetter import TagSetter
from .TagSetterInterface import TagSetterInterface
from .Task import Task
from .TaskClass import TaskClass
from .TaskPool import TaskPool
from .TaskPoolClass import TaskPoolClass
from .TaskPrivate import TaskPrivate
from .TaskState import TaskState
from .TimedValue import TimedValue
from .Toc import Toc
from .TocEntry import TocEntry
from .TocEntryType import TocEntryType
from .TocLoopType import TocLoopType
from .TocScope import TocScope
from .TocSetter import TocSetter
from .TocSetterInterface import TocSetterInterface
from .Tracer import Tracer
from .TracerClass import TracerClass
from .TracerFactory import TracerFactory
from .TracerFactoryClass import TracerFactoryClass
from .TracerPrivate import TracerPrivate
from .TracerRecord import TracerRecord
from .TracerRecordClass import TracerRecordClass
from .TracerValueFlags import TracerValueFlags
from .TracerValueScope import TracerValueScope
from .TypeFind import TypeFind
from .TypeFindFactory import TypeFindFactory
from .TypeFindFactoryClass import TypeFindFactoryClass
from .TypeFindProbability import TypeFindProbability
from .Uri import Uri
from .URIError import URIError
from .URIHandler import URIHandler
from .URIHandlerInterface import URIHandlerInterface
from .URIType import URIType
from .ValueArray import ValueArray
from .ValueList import ValueList
from .ValueTable import ValueTable
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f4261575d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gst-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gst', loader=<gi.importer.DynamicImporter object at 0x7f4261575d00>)"

