# encoding: utf-8
# module gi.repository.GstTag
# from /usr/lib64/girepository-1.0/GstTag-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gobject as __gobject


# Variables with simple values

TAG_CAPTURING_CONTRAST = 'capturing-contrast'

TAG_CAPTURING_DIGITAL_ZOOM_RATIO = 'capturing-digital-zoom-ratio'

TAG_CAPTURING_EXPOSURE_COMPENSATION = 'capturing-exposure-compensation'
TAG_CAPTURING_EXPOSURE_MODE = 'capturing-exposure-mode'
TAG_CAPTURING_EXPOSURE_PROGRAM = 'capturing-exposure-program'

TAG_CAPTURING_FLASH_FIRED = 'capturing-flash-fired'
TAG_CAPTURING_FLASH_MODE = 'capturing-flash-mode'

TAG_CAPTURING_FOCAL_LENGTH = 'capturing-focal-length'

TAG_CAPTURING_FOCAL_LENGTH_35_MM = 'capturing-focal-length-35mm'

TAG_CAPTURING_FOCAL_RATIO = 'capturing-focal-ratio'

TAG_CAPTURING_GAIN_ADJUSTMENT = 'capturing-gain-adjustment'

TAG_CAPTURING_ISO_SPEED = 'capturing-iso-speed'

TAG_CAPTURING_METERING_MODE = 'capturing-metering-mode'

TAG_CAPTURING_SATURATION = 'capturing-saturation'

TAG_CAPTURING_SCENE_CAPTURE_TYPE = 'capturing-scene-capture-type'

TAG_CAPTURING_SHARPNESS = 'capturing-sharpness'

TAG_CAPTURING_SHUTTER_SPEED = 'capturing-shutter-speed'

TAG_CAPTURING_SOURCE = 'capturing-source'

TAG_CAPTURING_WHITE_BALANCE = 'capturing-white-balance'

TAG_CDDA_CDDB_DISCID = 'discid'

TAG_CDDA_CDDB_DISCID_FULL = 'discid-full'

TAG_CDDA_MUSICBRAINZ_DISCID = 'musicbrainz-discid'

TAG_CDDA_MUSICBRAINZ_DISCID_FULL = 'musicbrainz-discid-full'

TAG_CMML_CLIP = 'cmml-clip'
TAG_CMML_HEAD = 'cmml-head'
TAG_CMML_STREAM = 'cmml-stream'

TAG_ID3V2_HEADER_SIZE = 10

TAG_IMAGE_HORIZONTAL_PPI = 'image-horizontal-ppi'

TAG_IMAGE_VERTICAL_PPI = 'image-vertical-ppi'

TAG_MUSICAL_KEY = 'musical-key'

TAG_MUSICBRAINZ_ALBUMARTISTID = 'musicbrainz-albumartistid'
TAG_MUSICBRAINZ_ALBUMID = 'musicbrainz-albumid'
TAG_MUSICBRAINZ_ARTISTID = 'musicbrainz-artistid'
TAG_MUSICBRAINZ_TRACKID = 'musicbrainz-trackid'
TAG_MUSICBRAINZ_TRMID = 'musicbrainz-trmid'

_namespace = 'GstTag'

_version = '1.0'

__weakref__ = None

# functions

def tag_check_language_code(lang_code): # real signature unknown; restored from __doc__
    """ tag_check_language_code(lang_code:str) -> bool """
    return False

def tag_freeform_string_to_utf8(data, env_vars): # real signature unknown; restored from __doc__
    """ tag_freeform_string_to_utf8(data:list, env_vars:list) -> str """
    return ""

def tag_from_id3_tag(id3_tag): # real signature unknown; restored from __doc__
    """ tag_from_id3_tag(id3_tag:str) -> str """
    return ""

def tag_from_id3_user_tag(type, id3_user_tag): # real signature unknown; restored from __doc__
    """ tag_from_id3_user_tag(type:str, id3_user_tag:str) -> str """
    return ""

def tag_from_vorbis_tag(vorbis_tag): # real signature unknown; restored from __doc__
    """ tag_from_vorbis_tag(vorbis_tag:str) -> str """
    return ""

def tag_get_id3v2_tag_size(buffer): # real signature unknown; restored from __doc__
    """ tag_get_id3v2_tag_size(buffer:Gst.Buffer) -> int """
    return 0

def tag_get_language_codes(): # real signature unknown; restored from __doc__
    """ tag_get_language_codes() -> list """
    return []

def tag_get_language_code_iso_639_1(lang_code): # real signature unknown; restored from __doc__
    """ tag_get_language_code_iso_639_1(lang_code:str) -> str """
    return ""

def tag_get_language_code_iso_639_2B(lang_code): # real signature unknown; restored from __doc__
    """ tag_get_language_code_iso_639_2B(lang_code:str) -> str """
    return ""

def tag_get_language_code_iso_639_2T(lang_code): # real signature unknown; restored from __doc__
    """ tag_get_language_code_iso_639_2T(lang_code:str) -> str """
    return ""

def tag_get_language_name(language_code): # real signature unknown; restored from __doc__
    """ tag_get_language_name(language_code:str) -> str """
    return ""

def tag_get_licenses(): # real signature unknown; restored from __doc__
    """ tag_get_licenses() -> list """
    return []

def tag_get_license_description(license_ref): # real signature unknown; restored from __doc__
    """ tag_get_license_description(license_ref:str) -> str """
    return ""

def tag_get_license_flags(license_ref): # real signature unknown; restored from __doc__
    """ tag_get_license_flags(license_ref:str) -> GstTag.TagLicenseFlags """
    pass

def tag_get_license_jurisdiction(license_ref): # real signature unknown; restored from __doc__
    """ tag_get_license_jurisdiction(license_ref:str) -> str """
    return ""

def tag_get_license_nick(license_ref): # real signature unknown; restored from __doc__
    """ tag_get_license_nick(license_ref:str) -> str """
    return ""

def tag_get_license_title(license_ref): # real signature unknown; restored from __doc__
    """ tag_get_license_title(license_ref:str) -> str """
    return ""

def tag_get_license_version(license_ref): # real signature unknown; restored from __doc__
    """ tag_get_license_version(license_ref:str) -> str """
    return ""

def tag_id3_genre_count(): # real signature unknown; restored from __doc__
    """ tag_id3_genre_count() -> int """
    return 0

def tag_id3_genre_get(id): # real signature unknown; restored from __doc__
    """ tag_id3_genre_get(id:int) -> str """
    return ""

def tag_image_data_to_image_sample(image_data, image_type): # real signature unknown; restored from __doc__
    """ tag_image_data_to_image_sample(image_data:list, image_type:GstTag.TagImageType) -> Gst.Sample """
    pass

def tag_list_add_id3_image(tag_list, image_data, id3_picture_type): # real signature unknown; restored from __doc__
    """ tag_list_add_id3_image(tag_list:Gst.TagList, image_data:list, id3_picture_type:int) -> bool """
    return False

def tag_list_from_exif_buffer(buffer, byte_order, base_offset): # real signature unknown; restored from __doc__
    """ tag_list_from_exif_buffer(buffer:Gst.Buffer, byte_order:int, base_offset:int) -> Gst.TagList """
    pass

def tag_list_from_exif_buffer_with_tiff_header(buffer): # real signature unknown; restored from __doc__
    """ tag_list_from_exif_buffer_with_tiff_header(buffer:Gst.Buffer) -> Gst.TagList """
    pass

def tag_list_from_id3v2_tag(buffer): # real signature unknown; restored from __doc__
    """ tag_list_from_id3v2_tag(buffer:Gst.Buffer) -> Gst.TagList """
    pass

def tag_list_from_vorbiscomment(data, id_data): # real signature unknown; restored from __doc__
    """ tag_list_from_vorbiscomment(data:list, id_data:list) -> Gst.TagList, vendor_string:str """
    pass

def tag_list_from_vorbiscomment_buffer(buffer, id_data): # real signature unknown; restored from __doc__
    """ tag_list_from_vorbiscomment_buffer(buffer:Gst.Buffer, id_data:list) -> Gst.TagList, vendor_string:str """
    pass

def tag_list_from_xmp_buffer(buffer): # real signature unknown; restored from __doc__
    """ tag_list_from_xmp_buffer(buffer:Gst.Buffer) -> Gst.TagList """
    pass

def tag_list_new_from_id3v1(data): # real signature unknown; restored from __doc__
    """ tag_list_new_from_id3v1(data:list) -> Gst.TagList """
    pass

def tag_list_to_exif_buffer(taglist, byte_order, base_offset): # real signature unknown; restored from __doc__
    """ tag_list_to_exif_buffer(taglist:Gst.TagList, byte_order:int, base_offset:int) -> Gst.Buffer """
    pass

def tag_list_to_exif_buffer_with_tiff_header(taglist): # real signature unknown; restored from __doc__
    """ tag_list_to_exif_buffer_with_tiff_header(taglist:Gst.TagList) -> Gst.Buffer """
    pass

def tag_list_to_vorbiscomment_buffer(p_list, id_data, vendor_string=None): # real signature unknown; restored from __doc__
    """ tag_list_to_vorbiscomment_buffer(list:Gst.TagList, id_data:list, vendor_string:str=None) -> Gst.Buffer """
    pass

def tag_list_to_xmp_buffer(p_list, read_only, schemas): # real signature unknown; restored from __doc__
    """ tag_list_to_xmp_buffer(list:Gst.TagList, read_only:bool, schemas:list) -> Gst.Buffer """
    pass

def tag_parse_extended_comment(ext_comment, fail_if_no_key): # real signature unknown; restored from __doc__
    """ tag_parse_extended_comment(ext_comment:str, fail_if_no_key:bool) -> bool, key:str, lang:str, value:str """
    return False

def tag_register_musicbrainz_tags(): # real signature unknown; restored from __doc__
    """ tag_register_musicbrainz_tags() """
    pass

def tag_to_id3_tag(gst_tag): # real signature unknown; restored from __doc__
    """ tag_to_id3_tag(gst_tag:str) -> str """
    return ""

def tag_to_vorbis_comments(p_list, tag): # real signature unknown; restored from __doc__
    """ tag_to_vorbis_comments(list:Gst.TagList, tag:str) -> list """
    return []

def tag_to_vorbis_tag(gst_tag): # real signature unknown; restored from __doc__
    """ tag_to_vorbis_tag(gst_tag:str) -> str """
    return ""

def tag_xmp_list_schemas(): # real signature unknown; restored from __doc__
    """ tag_xmp_list_schemas() -> list """
    return []

def vorbis_tag_add(p_list, tag, value): # real signature unknown; restored from __doc__
    """ vorbis_tag_add(list:Gst.TagList, tag:str, value:str) """
    pass

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

class TagDemux(__gi_repository_Gst.Element):
    """
    :Constructors:
    
    ::
    
        TagDemux(**properties)
    """
    def abort_state(self): # real signature unknown; restored from __doc__
        """ abort_state(self) """
        pass

    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_metadata(self, key:str, value:str) """
        pass

    def add_pad(self, pad): # real signature unknown; restored from __doc__
        """ add_pad(self, pad:Gst.Pad) -> bool """
        return False

    def add_pad_template(self, templ): # real signature unknown; restored from __doc__
        """ add_pad_template(self, templ:Gst.PadTemplate) """
        pass

    def add_property_deep_notify_watch(self, property_name=None, include_value): # real signature unknown; restored from __doc__
        """ add_property_deep_notify_watch(self, property_name:str=None, include_value:bool) -> int """
        return 0

    def add_property_notify_watch(self, property_name=None, include_value): # real signature unknown; restored from __doc__
        """ add_property_notify_watch(self, property_name:str=None, include_value:bool) -> int """
        return 0

    def add_static_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_static_metadata(self, key:str, value:str) """
        pass

    def add_static_pad_template(self, static_templ): # real signature unknown; restored from __doc__
        """ add_static_pad_template(self, static_templ:Gst.StaticPadTemplate) """
        pass

    def add_static_pad_template_with_gtype(self, static_templ, pad_type): # real signature unknown; restored from __doc__
        """ add_static_pad_template_with_gtype(self, static_templ:Gst.StaticPadTemplate, pad_type:GType) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def call_async(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ call_async(self, func:Gst.ElementCallAsyncFunc, user_data=None) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_state(self, transition): # real signature unknown; restored from __doc__
        """ change_state(self, transition:Gst.StateChange) -> Gst.StateChangeReturn """
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
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

    def continue_state(self, ret): # real signature unknown; restored from __doc__
        """ continue_state(self, ret:Gst.StateChangeReturn) -> Gst.StateChangeReturn """
        pass

    def create_all_pads(self): # real signature unknown; restored from __doc__
        """ create_all_pads(self) """
        pass

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_change_state(self, *args, **kwargs): # real signature unknown
        """ change_state(self, transition:Gst.StateChange) -> Gst.StateChangeReturn """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_get_state(self, *args, **kwargs): # real signature unknown
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def do_identify_tag(self, *args, **kwargs): # real signature unknown
        """ identify_tag(self, buffer:Gst.Buffer, start_tag:bool, tag_size:int) -> bool """
        pass

    def do_merge_tags(self, *args, **kwargs): # real signature unknown
        """ merge_tags(self, start_tags:Gst.TagList, end_tags:Gst.TagList) -> Gst.TagList """
        pass

    def do_no_more_pads(self, *args, **kwargs): # real signature unknown
        """ no_more_pads(self) """
        pass

    def do_pad_added(self, *args, **kwargs): # real signature unknown
        """ pad_added(self, pad:Gst.Pad) """
        pass

    def do_pad_removed(self, *args, **kwargs): # real signature unknown
        """ pad_removed(self, pad:Gst.Pad) """
        pass

    def do_parse_tag(self, *args, **kwargs): # real signature unknown
        """ parse_tag(self, buffer:Gst.Buffer, start_tag:bool, tag_size:int, tags:Gst.TagList) -> GstTag.TagDemuxResult """
        pass

    def do_post_message(self, *args, **kwargs): # real signature unknown
        """ post_message(self, message:Gst.Message) -> bool """
        pass

    def do_provide_clock(self, *args, **kwargs): # real signature unknown
        """ provide_clock(self) -> Gst.Clock or None """
        pass

    def do_query(self, *args, **kwargs): # real signature unknown
        """ query(self, query:Gst.Query) -> bool """
        pass

    def do_release_pad(self, *args, **kwargs): # real signature unknown
        """ release_pad(self, pad:Gst.Pad) """
        pass

    def do_request_new_pad(self, *args, **kwargs): # real signature unknown
        """ request_new_pad(self, templ:Gst.PadTemplate, name:str=None, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def do_send_event(self, *args, **kwargs): # real signature unknown
        """ send_event(self, event:Gst.Event) -> bool """
        pass

    def do_set_bus(self, *args, **kwargs): # real signature unknown
        """ set_bus(self, bus:Gst.Bus=None) """
        pass

    def do_set_clock(self, *args, **kwargs): # real signature unknown
        """ set_clock(self, clock:Gst.Clock=None) -> bool """
        pass

    def do_set_context(self, *args, **kwargs): # real signature unknown
        """ set_context(self, context:Gst.Context) """
        pass

    def do_set_state(self, *args, **kwargs): # real signature unknown
        """ set_state(self, state:Gst.State) -> Gst.StateChangeReturn """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, oldstate:Gst.State, newstate:Gst.State, pending:Gst.State) """
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

    def foreach_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
        return False

    def foreach_sink_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_sink_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
        return False

    def foreach_src_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_src_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_base_time(self): # real signature unknown; restored from __doc__
        """ get_base_time(self) -> int """
        return 0

    def get_bus(self): # real signature unknown; restored from __doc__
        """ get_bus(self) -> Gst.Bus or None """
        pass

    def get_clock(self): # real signature unknown; restored from __doc__
        """ get_clock(self) -> Gst.Clock or None """
        pass

    def get_compatible_pad(self, pad, caps=None): # real signature unknown; restored from __doc__
        """ get_compatible_pad(self, pad:Gst.Pad, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def get_compatible_pad_template(self, compattempl): # real signature unknown; restored from __doc__
        """ get_compatible_pad_template(self, compattempl:Gst.PadTemplate) -> Gst.PadTemplate or None """
        pass

    def get_context(self, context_type): # real signature unknown; restored from __doc__
        """ get_context(self, context_type:str) -> Gst.Context """
        pass

    def get_contexts(self): # real signature unknown; restored from __doc__
        """ get_contexts(self) -> list """
        return []

    def get_context_unlocked(self, context_type): # real signature unknown; restored from __doc__
        """ get_context_unlocked(self, context_type:str) -> Gst.Context or None """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_factory(self): # real signature unknown; restored from __doc__
        """ get_factory(self) -> Gst.ElementFactory or None """
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_metadata(self, key): # real signature unknown; restored from __doc__
        """ get_metadata(self, key:str) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_pad_template(self, name): # real signature unknown; restored from __doc__
        """ get_pad_template(self, name:str) -> Gst.PadTemplate or None """
        pass

    def get_pad_template_list(self): # real signature unknown; restored from __doc__
        """ get_pad_template_list(self) -> list """
        return []

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_request_pad(self, name): # real signature unknown; restored from __doc__
        """ get_request_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_start_time(self): # real signature unknown; restored from __doc__
        """ get_start_time(self) -> int """
        return 0

    def get_state(self, timeout): # real signature unknown; restored from __doc__
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def get_static_pad(self, name): # real signature unknown; restored from __doc__
        """ get_static_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
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

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
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

    def is_locked_state(self): # real signature unknown; restored from __doc__
        """ is_locked_state(self) -> bool """
        return False

    def iterate_pads(self): # real signature unknown; restored from __doc__
        """ iterate_pads(self) -> Gst.Iterator """
        pass

    def iterate_sink_pads(self): # real signature unknown; restored from __doc__
        """ iterate_sink_pads(self) -> Gst.Iterator """
        pass

    def iterate_src_pads(self): # real signature unknown; restored from __doc__
        """ iterate_src_pads(self) -> Gst.Iterator """
        pass

    def link(self, dest): # real signature unknown; restored from __doc__
        """ link(self, dest:Gst.Element) -> bool """
        return False

    def link_filtered(self, dest, filter=None): # real signature unknown; restored from __doc__
        """ link_filtered(self, dest:Gst.Element, filter:Gst.Caps=None) -> bool """
        return False

    def link_pads(self, srcpadname=None, dest, destpadname=None): # real signature unknown; restored from __doc__
        """ link_pads(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None) -> bool """
        return False

    def link_pads_filtered(self, srcpadname=None, dest, destpadname=None, filter=None): # real signature unknown; restored from __doc__
        """ link_pads_filtered(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None, filter:Gst.Caps=None) -> bool """
        return False

    def link_pads_full(self, srcpadname=None, dest, destpadname=None, flags): # real signature unknown; restored from __doc__
        """ link_pads_full(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None, flags:Gst.PadLinkCheck) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lost_state(self): # real signature unknown; restored from __doc__
        """ lost_state(self) """
        pass

    def make_from_uri(self, type, uri, elementname=None): # real signature unknown; restored from __doc__
        """ make_from_uri(type:Gst.URIType, uri:str, elementname:str=None) -> Gst.Element or None """
        pass

    def message_full(self, type, domain, code, text=None, debug=None, file, function, line): # real signature unknown; restored from __doc__
        """ message_full(self, type:Gst.MessageType, domain:int, code:int, text:str=None, debug:str=None, file:str, function:str, line:int) """
        pass

    def message_full_with_details(self, type, domain, code, text=None, debug=None, file, function, line, structure): # real signature unknown; restored from __doc__
        """ message_full_with_details(self, type:Gst.MessageType, domain:int, code:int, text:str=None, debug:str=None, file:str, function:str, line:int, structure:Gst.Structure) """
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

    def no_more_pads(self): # real signature unknown; restored from __doc__
        """ no_more_pads(self) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def post_message(self, message): # real signature unknown; restored from __doc__
        """ post_message(self, message:Gst.Message) -> bool """
        return False

    def provide_clock(self): # real signature unknown; restored from __doc__
        """ provide_clock(self) -> Gst.Clock or None """
        pass

    def query(self, query): # real signature unknown; restored from __doc__
        """ query(self, query:Gst.Query) -> bool """
        return False

    def query_convert(self, src_format, src_val, dest_format): # real signature unknown; restored from __doc__
        """ query_convert(self, src_format:Gst.Format, src_val:int, dest_format:Gst.Format) -> bool, dest_val:int """
        return False

    def query_duration(self, format): # real signature unknown; restored from __doc__
        """ query_duration(self, format:Gst.Format) -> bool, duration:int """
        return False

    def query_position(self, format): # real signature unknown; restored from __doc__
        """ query_position(self, format:Gst.Format) -> bool, cur:int """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self, plugin=None, name, rank, type): # real signature unknown; restored from __doc__
        """ register(plugin:Gst.Plugin=None, name:str, rank:int, type:GType) -> bool """
        return False

    def release_request_pad(self, pad): # real signature unknown; restored from __doc__
        """ release_request_pad(self, pad:Gst.Pad) """
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def remove_pad(self, pad): # real signature unknown; restored from __doc__
        """ remove_pad(self, pad:Gst.Pad) -> bool """
        return False

    def remove_property_notify_watch(self, watch_id): # real signature unknown; restored from __doc__
        """ remove_property_notify_watch(self, watch_id:int) """
        pass

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def request_pad(self, templ, name=None, caps=None): # real signature unknown; restored from __doc__
        """ request_pad(self, templ:Gst.PadTemplate, name:str=None, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def seek(self, rate, format, flags, start_type, start, stop_type, stop): # real signature unknown; restored from __doc__
        """ seek(self, rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int) -> bool """
        return False

    def seek_simple(self, format, seek_flags, seek_pos): # real signature unknown; restored from __doc__
        """ seek_simple(self, format:Gst.Format, seek_flags:Gst.SeekFlags, seek_pos:int) -> bool """
        return False

    def send_event(self, event): # real signature unknown; restored from __doc__
        """ send_event(self, event:Gst.Event) -> bool """
        return False

    def set_base_time(self, time): # real signature unknown; restored from __doc__
        """ set_base_time(self, time:int) """
        pass

    def set_bus(self, bus=None): # real signature unknown; restored from __doc__
        """ set_bus(self, bus:Gst.Bus=None) """
        pass

    def set_clock(self, clock=None): # real signature unknown; restored from __doc__
        """ set_clock(self, clock:Gst.Clock=None) -> bool """
        return False

    def set_context(self, context): # real signature unknown; restored from __doc__
        """ set_context(self, context:Gst.Context) """
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_locked_state(self, locked_state): # real signature unknown; restored from __doc__
        """ set_locked_state(self, locked_state:bool) -> bool """
        return False

    def set_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_start_time(self, time): # real signature unknown; restored from __doc__
        """ set_start_time(self, time:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gst.State) -> Gst.StateChangeReturn """
        pass

    def set_static_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_static_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def state_change_return_get_name(self, state_ret): # real signature unknown; restored from __doc__
        """ state_change_return_get_name(state_ret:Gst.StateChangeReturn) -> str """
        return ""

    def state_get_name(self, state): # real signature unknown; restored from __doc__
        """ state_get_name(state:Gst.State) -> str """
        return ""

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

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_state_with_parent(self): # real signature unknown; restored from __doc__
        """ sync_state_with_parent(self) -> bool """
        return False

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlink(self, dest): # real signature unknown; restored from __doc__
        """ unlink(self, dest:Gst.Element) """
        pass

    def unlink_pads(self, srcpadname, dest, destpadname): # real signature unknown; restored from __doc__
        """ unlink_pads(self, srcpadname:str, dest:Gst.Element, destpadname:str) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    base_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_return = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsrcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f8c0ac13340>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TagDemux), '__module__': 'gi.repository.GstTag', '__gtype__': <GType GstTagDemux (94256106267136)>, '__doc__': None, '__gsignals__': {}, 'do_identify_tag': gi.VFuncInfo(identify_tag), 'do_merge_tags': gi.VFuncInfo(merge_tags), 'do_parse_tag': gi.VFuncInfo(parse_tag), 'element': <property object at 0x7f8c0ac0b720>, 'priv': <property object at 0x7f8c0ac0b810>, 'reserved': <property object at 0x7f8c0ac0b900>})"
    __gdoc__ = 'Object GstTagDemux\n\nSignals from GstElement:\n  pad-added (GstPad)\n  pad-removed (GstPad)\n  no-more-pads ()\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstTagDemux (94256106267136)>'
    __info__ = ObjectInfo(TagDemux)


class TagDemuxClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TagDemuxClass()
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

    identify_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    merge_tags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_end_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_start_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parse_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TagDemuxClass), '__module__': 'gi.repository.GstTag', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TagDemuxClass' objects>, '__weakref__': <attribute '__weakref__' of 'TagDemuxClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f8c0ac0ba40>, 'min_start_size': <property object at 0x7f8c0ac0bb30>, 'min_end_size': <property object at 0x7f8c0ac0bc20>, 'identify_tag': <property object at 0x7f8c0ac0bd10>, 'parse_tag': <property object at 0x7f8c0ac0be00>, 'merge_tags': <property object at 0x7f8c0ac0bef0>, 'reserved': <property object at 0x7f8c0ac0d040>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TagDemuxClass)


class TagDemuxPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TagDemuxPrivate), '__module__': 'gi.repository.GstTag', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TagDemuxPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'TagDemuxPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TagDemuxPrivate)


class TagDemuxResult(__gobject.GEnum):
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


    AGAIN = 1
    BROKEN_TAG = 0
    OK = 2
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstTag', '__dict__': <attribute '__dict__' of 'TagDemuxResult' objects>, '__doc__': None, '__gtype__': <GType GstTagDemuxResult (94256106240928)>, '__enum_values__': {0: <enum GST_TAG_DEMUX_RESULT_BROKEN_TAG of type GstTag.TagDemuxResult>, 1: <enum GST_TAG_DEMUX_RESULT_AGAIN of type GstTag.TagDemuxResult>, 2: <enum GST_TAG_DEMUX_RESULT_OK of type GstTag.TagDemuxResult>}, '__info__': gi.EnumInfo(TagDemuxResult), 'BROKEN_TAG': <enum GST_TAG_DEMUX_RESULT_BROKEN_TAG of type GstTag.TagDemuxResult>, 'AGAIN': <enum GST_TAG_DEMUX_RESULT_AGAIN of type GstTag.TagDemuxResult>, 'OK': <enum GST_TAG_DEMUX_RESULT_OK of type GstTag.TagDemuxResult>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType GstTagDemuxResult (94256106240928)>'
    __info__ = gi.EnumInfo(TagDemuxResult)


class TagImageType(__gobject.GEnum):
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


    ARTIST = 6
    BACK_COVER = 2
    BAND_ARTIST_LOGO = 17
    BAND_ORCHESTRA = 8
    COMPOSER = 9
    CONDUCTOR = 7
    DURING_PERFORMANCE = 13
    DURING_RECORDING = 12
    FISH = 15
    FRONT_COVER = 1
    ILLUSTRATION = 16
    LEAD_ARTIST = 5
    LEAFLET_PAGE = 3
    LYRICIST = 10
    MEDIUM = 4
    NONE = -1
    PUBLISHER_STUDIO_LOGO = 18
    RECORDING_LOCATION = 11
    UNDEFINED = 0
    VIDEO_CAPTURE = 14
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstTag', '__dict__': <attribute '__dict__' of 'TagImageType' objects>, '__doc__': None, '__gtype__': <GType GstTagImageType (94256106348208)>, '__enum_values__': {-1: <enum GST_TAG_IMAGE_TYPE_NONE of type GstTag.TagImageType>, 0: <enum GST_TAG_IMAGE_TYPE_UNDEFINED of type GstTag.TagImageType>, 1: <enum GST_TAG_IMAGE_TYPE_FRONT_COVER of type GstTag.TagImageType>, 2: <enum GST_TAG_IMAGE_TYPE_BACK_COVER of type GstTag.TagImageType>, 3: <enum GST_TAG_IMAGE_TYPE_LEAFLET_PAGE of type GstTag.TagImageType>, 4: <enum GST_TAG_IMAGE_TYPE_MEDIUM of type GstTag.TagImageType>, 5: <enum GST_TAG_IMAGE_TYPE_LEAD_ARTIST of type GstTag.TagImageType>, 6: <enum GST_TAG_IMAGE_TYPE_ARTIST of type GstTag.TagImageType>, 7: <enum GST_TAG_IMAGE_TYPE_CONDUCTOR of type GstTag.TagImageType>, 8: <enum GST_TAG_IMAGE_TYPE_BAND_ORCHESTRA of type GstTag.TagImageType>, 9: <enum GST_TAG_IMAGE_TYPE_COMPOSER of type GstTag.TagImageType>, 10: <enum GST_TAG_IMAGE_TYPE_LYRICIST of type GstTag.TagImageType>, 11: <enum GST_TAG_IMAGE_TYPE_RECORDING_LOCATION of type GstTag.TagImageType>, 12: <enum GST_TAG_IMAGE_TYPE_DURING_RECORDING of type GstTag.TagImageType>, 13: <enum GST_TAG_IMAGE_TYPE_DURING_PERFORMANCE of type GstTag.TagImageType>, 14: <enum GST_TAG_IMAGE_TYPE_VIDEO_CAPTURE of type GstTag.TagImageType>, 15: <enum GST_TAG_IMAGE_TYPE_FISH of type GstTag.TagImageType>, 16: <enum GST_TAG_IMAGE_TYPE_ILLUSTRATION of type GstTag.TagImageType>, 17: <enum GST_TAG_IMAGE_TYPE_BAND_ARTIST_LOGO of type GstTag.TagImageType>, 18: <enum GST_TAG_IMAGE_TYPE_PUBLISHER_STUDIO_LOGO of type GstTag.TagImageType>}, '__info__': gi.EnumInfo(TagImageType), 'NONE': <enum GST_TAG_IMAGE_TYPE_NONE of type GstTag.TagImageType>, 'UNDEFINED': <enum GST_TAG_IMAGE_TYPE_UNDEFINED of type GstTag.TagImageType>, 'FRONT_COVER': <enum GST_TAG_IMAGE_TYPE_FRONT_COVER of type GstTag.TagImageType>, 'BACK_COVER': <enum GST_TAG_IMAGE_TYPE_BACK_COVER of type GstTag.TagImageType>, 'LEAFLET_PAGE': <enum GST_TAG_IMAGE_TYPE_LEAFLET_PAGE of type GstTag.TagImageType>, 'MEDIUM': <enum GST_TAG_IMAGE_TYPE_MEDIUM of type GstTag.TagImageType>, 'LEAD_ARTIST': <enum GST_TAG_IMAGE_TYPE_LEAD_ARTIST of type GstTag.TagImageType>, 'ARTIST': <enum GST_TAG_IMAGE_TYPE_ARTIST of type GstTag.TagImageType>, 'CONDUCTOR': <enum GST_TAG_IMAGE_TYPE_CONDUCTOR of type GstTag.TagImageType>, 'BAND_ORCHESTRA': <enum GST_TAG_IMAGE_TYPE_BAND_ORCHESTRA of type GstTag.TagImageType>, 'COMPOSER': <enum GST_TAG_IMAGE_TYPE_COMPOSER of type GstTag.TagImageType>, 'LYRICIST': <enum GST_TAG_IMAGE_TYPE_LYRICIST of type GstTag.TagImageType>, 'RECORDING_LOCATION': <enum GST_TAG_IMAGE_TYPE_RECORDING_LOCATION of type GstTag.TagImageType>, 'DURING_RECORDING': <enum GST_TAG_IMAGE_TYPE_DURING_RECORDING of type GstTag.TagImageType>, 'DURING_PERFORMANCE': <enum GST_TAG_IMAGE_TYPE_DURING_PERFORMANCE of type GstTag.TagImageType>, 'VIDEO_CAPTURE': <enum GST_TAG_IMAGE_TYPE_VIDEO_CAPTURE of type GstTag.TagImageType>, 'FISH': <enum GST_TAG_IMAGE_TYPE_FISH of type GstTag.TagImageType>, 'ILLUSTRATION': <enum GST_TAG_IMAGE_TYPE_ILLUSTRATION of type GstTag.TagImageType>, 'BAND_ARTIST_LOGO': <enum GST_TAG_IMAGE_TYPE_BAND_ARTIST_LOGO of type GstTag.TagImageType>, 'PUBLISHER_STUDIO_LOGO': <enum GST_TAG_IMAGE_TYPE_PUBLISHER_STUDIO_LOGO of type GstTag.TagImageType>})"
    __enum_values__ = {
        -1: -1,
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
    }
    __gtype__ = None # (!) real value is '<GType GstTagImageType (94256106348208)>'
    __info__ = gi.EnumInfo(TagImageType)


class TagLicenseFlags(__gobject.GFlags):
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
        """ Helper for pickle. """
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

    first_value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    CREATIVE_COMMONS_LICENSE = 16777216
    FREE_SOFTWARE_FOUNDATION_LICENSE = 33554432
    PERMITS_DERIVATIVE_WORKS = 4
    PERMITS_DISTRIBUTION = 2
    PERMITS_REPRODUCTION = 1
    PERMITS_SHARING = 8
    PROHIBITS_COMMERCIAL_USE = 65536
    PROHIBITS_HIGH_INCOME_NATION_USE = 131072
    REQUIRES_ATTRIBUTION = 512
    REQUIRES_COPYLEFT = 4096
    REQUIRES_LESSER_COPYLEFT = 8192
    REQUIRES_NOTICE = 256
    REQUIRES_SHARE_ALIKE = 1024
    REQUIRES_SOURCE_CODE = 2048
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GstTag', '__dict__': <attribute '__dict__' of 'TagLicenseFlags' objects>, '__doc__': None, '__gtype__': <GType GstTagLicenseFlags (94256106335504)>, '__flags_values__': {1: <flags GST_TAG_LICENSE_PERMITS_REPRODUCTION of type GstTag.TagLicenseFlags>, 2: <flags GST_TAG_LICENSE_PERMITS_DISTRIBUTION of type GstTag.TagLicenseFlags>, 4: <flags GST_TAG_LICENSE_PERMITS_DERIVATIVE_WORKS of type GstTag.TagLicenseFlags>, 8: <flags GST_TAG_LICENSE_PERMITS_SHARING of type GstTag.TagLicenseFlags>, 256: <flags GST_TAG_LICENSE_REQUIRES_NOTICE of type GstTag.TagLicenseFlags>, 512: <flags GST_TAG_LICENSE_REQUIRES_ATTRIBUTION of type GstTag.TagLicenseFlags>, 1024: <flags GST_TAG_LICENSE_REQUIRES_SHARE_ALIKE of type GstTag.TagLicenseFlags>, 2048: <flags GST_TAG_LICENSE_REQUIRES_SOURCE_CODE of type GstTag.TagLicenseFlags>, 4096: <flags GST_TAG_LICENSE_REQUIRES_COPYLEFT of type GstTag.TagLicenseFlags>, 8192: <flags GST_TAG_LICENSE_REQUIRES_LESSER_COPYLEFT of type GstTag.TagLicenseFlags>, 65536: <flags GST_TAG_LICENSE_PROHIBITS_COMMERCIAL_USE of type GstTag.TagLicenseFlags>, 131072: <flags GST_TAG_LICENSE_PROHIBITS_HIGH_INCOME_NATION_USE of type GstTag.TagLicenseFlags>, 16777216: <flags GST_TAG_LICENSE_CREATIVE_COMMONS_LICENSE of type GstTag.TagLicenseFlags>, 33554432: <flags GST_TAG_LICENSE_FREE_SOFTWARE_FOUNDATION_LICENSE of type GstTag.TagLicenseFlags>}, '__info__': gi.EnumInfo(TagLicenseFlags), 'PERMITS_REPRODUCTION': <flags GST_TAG_LICENSE_PERMITS_REPRODUCTION of type GstTag.TagLicenseFlags>, 'PERMITS_DISTRIBUTION': <flags GST_TAG_LICENSE_PERMITS_DISTRIBUTION of type GstTag.TagLicenseFlags>, 'PERMITS_DERIVATIVE_WORKS': <flags GST_TAG_LICENSE_PERMITS_DERIVATIVE_WORKS of type GstTag.TagLicenseFlags>, 'PERMITS_SHARING': <flags GST_TAG_LICENSE_PERMITS_SHARING of type GstTag.TagLicenseFlags>, 'REQUIRES_NOTICE': <flags GST_TAG_LICENSE_REQUIRES_NOTICE of type GstTag.TagLicenseFlags>, 'REQUIRES_ATTRIBUTION': <flags GST_TAG_LICENSE_REQUIRES_ATTRIBUTION of type GstTag.TagLicenseFlags>, 'REQUIRES_SHARE_ALIKE': <flags GST_TAG_LICENSE_REQUIRES_SHARE_ALIKE of type GstTag.TagLicenseFlags>, 'REQUIRES_SOURCE_CODE': <flags GST_TAG_LICENSE_REQUIRES_SOURCE_CODE of type GstTag.TagLicenseFlags>, 'REQUIRES_COPYLEFT': <flags GST_TAG_LICENSE_REQUIRES_COPYLEFT of type GstTag.TagLicenseFlags>, 'REQUIRES_LESSER_COPYLEFT': <flags GST_TAG_LICENSE_REQUIRES_LESSER_COPYLEFT of type GstTag.TagLicenseFlags>, 'PROHIBITS_COMMERCIAL_USE': <flags GST_TAG_LICENSE_PROHIBITS_COMMERCIAL_USE of type GstTag.TagLicenseFlags>, 'PROHIBITS_HIGH_INCOME_NATION_USE': <flags GST_TAG_LICENSE_PROHIBITS_HIGH_INCOME_NATION_USE of type GstTag.TagLicenseFlags>, 'CREATIVE_COMMONS_LICENSE': <flags GST_TAG_LICENSE_CREATIVE_COMMONS_LICENSE of type GstTag.TagLicenseFlags>, 'FREE_SOFTWARE_FOUNDATION_LICENSE': <flags GST_TAG_LICENSE_FREE_SOFTWARE_FOUNDATION_LICENSE of type GstTag.TagLicenseFlags>})"
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        4096: 4096,
        8192: 8192,
        65536: 65536,
        131072: 131072,
        16777216: 16777216,
        33554432: 33554432,
    }
    __gtype__ = None # (!) real value is '<GType GstTagLicenseFlags (94256106335504)>'
    __info__ = gi.EnumInfo(TagLicenseFlags)


class TagMux(__gi_repository_Gst.Element, __gi_repository_Gst.TagSetter):
    """
    :Constructors:
    
    ::
    
        TagMux(**properties)
    """
    def abort_state(self): # real signature unknown; restored from __doc__
        """ abort_state(self) """
        pass

    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_metadata(self, key:str, value:str) """
        pass

    def add_pad(self, pad): # real signature unknown; restored from __doc__
        """ add_pad(self, pad:Gst.Pad) -> bool """
        return False

    def add_pad_template(self, templ): # real signature unknown; restored from __doc__
        """ add_pad_template(self, templ:Gst.PadTemplate) """
        pass

    def add_property_deep_notify_watch(self, property_name=None, include_value): # real signature unknown; restored from __doc__
        """ add_property_deep_notify_watch(self, property_name:str=None, include_value:bool) -> int """
        return 0

    def add_property_notify_watch(self, property_name=None, include_value): # real signature unknown; restored from __doc__
        """ add_property_notify_watch(self, property_name:str=None, include_value:bool) -> int """
        return 0

    def add_static_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_static_metadata(self, key:str, value:str) """
        pass

    def add_static_pad_template(self, static_templ): # real signature unknown; restored from __doc__
        """ add_static_pad_template(self, static_templ:Gst.StaticPadTemplate) """
        pass

    def add_static_pad_template_with_gtype(self, static_templ, pad_type): # real signature unknown; restored from __doc__
        """ add_static_pad_template_with_gtype(self, static_templ:Gst.StaticPadTemplate, pad_type:GType) """
        pass

    def add_tag_value(self, mode, tag, value): # real signature unknown; restored from __doc__
        """ add_tag_value(self, mode:Gst.TagMergeMode, tag:str, value:GObject.Value) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def call_async(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ call_async(self, func:Gst.ElementCallAsyncFunc, user_data=None) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_state(self, transition): # real signature unknown; restored from __doc__
        """ change_state(self, transition:Gst.StateChange) -> Gst.StateChangeReturn """
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
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

    def continue_state(self, ret): # real signature unknown; restored from __doc__
        """ continue_state(self, ret:Gst.StateChangeReturn) -> Gst.StateChangeReturn """
        pass

    def create_all_pads(self): # real signature unknown; restored from __doc__
        """ create_all_pads(self) """
        pass

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_change_state(self, *args, **kwargs): # real signature unknown
        """ change_state(self, transition:Gst.StateChange) -> Gst.StateChangeReturn """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_get_state(self, *args, **kwargs): # real signature unknown
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def do_no_more_pads(self, *args, **kwargs): # real signature unknown
        """ no_more_pads(self) """
        pass

    def do_pad_added(self, *args, **kwargs): # real signature unknown
        """ pad_added(self, pad:Gst.Pad) """
        pass

    def do_pad_removed(self, *args, **kwargs): # real signature unknown
        """ pad_removed(self, pad:Gst.Pad) """
        pass

    def do_post_message(self, *args, **kwargs): # real signature unknown
        """ post_message(self, message:Gst.Message) -> bool """
        pass

    def do_provide_clock(self, *args, **kwargs): # real signature unknown
        """ provide_clock(self) -> Gst.Clock or None """
        pass

    def do_query(self, *args, **kwargs): # real signature unknown
        """ query(self, query:Gst.Query) -> bool """
        pass

    def do_release_pad(self, *args, **kwargs): # real signature unknown
        """ release_pad(self, pad:Gst.Pad) """
        pass

    def do_render_end_tag(self, *args, **kwargs): # real signature unknown
        """ render_end_tag(self, tag_list:Gst.TagList) -> Gst.Buffer """
        pass

    def do_render_start_tag(self, *args, **kwargs): # real signature unknown
        """ render_start_tag(self, tag_list:Gst.TagList) -> Gst.Buffer """
        pass

    def do_request_new_pad(self, *args, **kwargs): # real signature unknown
        """ request_new_pad(self, templ:Gst.PadTemplate, name:str=None, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def do_send_event(self, *args, **kwargs): # real signature unknown
        """ send_event(self, event:Gst.Event) -> bool """
        pass

    def do_set_bus(self, *args, **kwargs): # real signature unknown
        """ set_bus(self, bus:Gst.Bus=None) """
        pass

    def do_set_clock(self, *args, **kwargs): # real signature unknown
        """ set_clock(self, clock:Gst.Clock=None) -> bool """
        pass

    def do_set_context(self, *args, **kwargs): # real signature unknown
        """ set_context(self, context:Gst.Context) """
        pass

    def do_set_state(self, *args, **kwargs): # real signature unknown
        """ set_state(self, state:Gst.State) -> Gst.StateChangeReturn """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, oldstate:Gst.State, newstate:Gst.State, pending:Gst.State) """
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

    def foreach_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
        return False

    def foreach_sink_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_sink_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
        return False

    def foreach_src_pad(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_src_pad(self, func:Gst.ElementForeachPadFunc, user_data=None) -> bool """
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_base_time(self): # real signature unknown; restored from __doc__
        """ get_base_time(self) -> int """
        return 0

    def get_bus(self): # real signature unknown; restored from __doc__
        """ get_bus(self) -> Gst.Bus or None """
        pass

    def get_clock(self): # real signature unknown; restored from __doc__
        """ get_clock(self) -> Gst.Clock or None """
        pass

    def get_compatible_pad(self, pad, caps=None): # real signature unknown; restored from __doc__
        """ get_compatible_pad(self, pad:Gst.Pad, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def get_compatible_pad_template(self, compattempl): # real signature unknown; restored from __doc__
        """ get_compatible_pad_template(self, compattempl:Gst.PadTemplate) -> Gst.PadTemplate or None """
        pass

    def get_context(self, context_type): # real signature unknown; restored from __doc__
        """ get_context(self, context_type:str) -> Gst.Context """
        pass

    def get_contexts(self): # real signature unknown; restored from __doc__
        """ get_contexts(self) -> list """
        return []

    def get_context_unlocked(self, context_type): # real signature unknown; restored from __doc__
        """ get_context_unlocked(self, context_type:str) -> Gst.Context or None """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_factory(self): # real signature unknown; restored from __doc__
        """ get_factory(self) -> Gst.ElementFactory or None """
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_metadata(self, key): # real signature unknown; restored from __doc__
        """ get_metadata(self, key:str) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_pad_template(self, name): # real signature unknown; restored from __doc__
        """ get_pad_template(self, name:str) -> Gst.PadTemplate or None """
        pass

    def get_pad_template_list(self): # real signature unknown; restored from __doc__
        """ get_pad_template_list(self) -> list """
        return []

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_request_pad(self, name): # real signature unknown; restored from __doc__
        """ get_request_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_start_time(self): # real signature unknown; restored from __doc__
        """ get_start_time(self) -> int """
        return 0

    def get_state(self, timeout): # real signature unknown; restored from __doc__
        """ get_state(self, timeout:int) -> Gst.StateChangeReturn, state:Gst.State, pending:Gst.State """
        pass

    def get_static_pad(self, name): # real signature unknown; restored from __doc__
        """ get_static_pad(self, name:str) -> Gst.Pad or None """
        pass

    def get_tag_list(self): # real signature unknown; restored from __doc__
        """ get_tag_list(self) -> Gst.TagList or None """
        pass

    def get_tag_merge_mode(self): # real signature unknown; restored from __doc__
        """ get_tag_merge_mode(self) -> Gst.TagMergeMode """
        pass

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
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

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
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

    def is_locked_state(self): # real signature unknown; restored from __doc__
        """ is_locked_state(self) -> bool """
        return False

    def iterate_pads(self): # real signature unknown; restored from __doc__
        """ iterate_pads(self) -> Gst.Iterator """
        pass

    def iterate_sink_pads(self): # real signature unknown; restored from __doc__
        """ iterate_sink_pads(self) -> Gst.Iterator """
        pass

    def iterate_src_pads(self): # real signature unknown; restored from __doc__
        """ iterate_src_pads(self) -> Gst.Iterator """
        pass

    def link(self, dest): # real signature unknown; restored from __doc__
        """ link(self, dest:Gst.Element) -> bool """
        return False

    def link_filtered(self, dest, filter=None): # real signature unknown; restored from __doc__
        """ link_filtered(self, dest:Gst.Element, filter:Gst.Caps=None) -> bool """
        return False

    def link_pads(self, srcpadname=None, dest, destpadname=None): # real signature unknown; restored from __doc__
        """ link_pads(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None) -> bool """
        return False

    def link_pads_filtered(self, srcpadname=None, dest, destpadname=None, filter=None): # real signature unknown; restored from __doc__
        """ link_pads_filtered(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None, filter:Gst.Caps=None) -> bool """
        return False

    def link_pads_full(self, srcpadname=None, dest, destpadname=None, flags): # real signature unknown; restored from __doc__
        """ link_pads_full(self, srcpadname:str=None, dest:Gst.Element, destpadname:str=None, flags:Gst.PadLinkCheck) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lost_state(self): # real signature unknown; restored from __doc__
        """ lost_state(self) """
        pass

    def make_from_uri(self, type, uri, elementname=None): # real signature unknown; restored from __doc__
        """ make_from_uri(type:Gst.URIType, uri:str, elementname:str=None) -> Gst.Element or None """
        pass

    def merge_tags(self, p_list, mode): # real signature unknown; restored from __doc__
        """ merge_tags(self, list:Gst.TagList, mode:Gst.TagMergeMode) """
        pass

    def message_full(self, type, domain, code, text=None, debug=None, file, function, line): # real signature unknown; restored from __doc__
        """ message_full(self, type:Gst.MessageType, domain:int, code:int, text:str=None, debug:str=None, file:str, function:str, line:int) """
        pass

    def message_full_with_details(self, type, domain, code, text=None, debug=None, file, function, line, structure): # real signature unknown; restored from __doc__
        """ message_full_with_details(self, type:Gst.MessageType, domain:int, code:int, text:str=None, debug:str=None, file:str, function:str, line:int, structure:Gst.Structure) """
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

    def no_more_pads(self): # real signature unknown; restored from __doc__
        """ no_more_pads(self) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def post_message(self, message): # real signature unknown; restored from __doc__
        """ post_message(self, message:Gst.Message) -> bool """
        return False

    def provide_clock(self): # real signature unknown; restored from __doc__
        """ provide_clock(self) -> Gst.Clock or None """
        pass

    def query(self, query): # real signature unknown; restored from __doc__
        """ query(self, query:Gst.Query) -> bool """
        return False

    def query_convert(self, src_format, src_val, dest_format): # real signature unknown; restored from __doc__
        """ query_convert(self, src_format:Gst.Format, src_val:int, dest_format:Gst.Format) -> bool, dest_val:int """
        return False

    def query_duration(self, format): # real signature unknown; restored from __doc__
        """ query_duration(self, format:Gst.Format) -> bool, duration:int """
        return False

    def query_position(self, format): # real signature unknown; restored from __doc__
        """ query_position(self, format:Gst.Format) -> bool, cur:int """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self, plugin=None, name, rank, type): # real signature unknown; restored from __doc__
        """ register(plugin:Gst.Plugin=None, name:str, rank:int, type:GType) -> bool """
        return False

    def release_request_pad(self, pad): # real signature unknown; restored from __doc__
        """ release_request_pad(self, pad:Gst.Pad) """
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def remove_pad(self, pad): # real signature unknown; restored from __doc__
        """ remove_pad(self, pad:Gst.Pad) -> bool """
        return False

    def remove_property_notify_watch(self, watch_id): # real signature unknown; restored from __doc__
        """ remove_property_notify_watch(self, watch_id:int) """
        pass

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def request_pad(self, templ, name=None, caps=None): # real signature unknown; restored from __doc__
        """ request_pad(self, templ:Gst.PadTemplate, name:str=None, caps:Gst.Caps=None) -> Gst.Pad or None """
        pass

    def reset_tags(self): # real signature unknown; restored from __doc__
        """ reset_tags(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def seek(self, rate, format, flags, start_type, start, stop_type, stop): # real signature unknown; restored from __doc__
        """ seek(self, rate:float, format:Gst.Format, flags:Gst.SeekFlags, start_type:Gst.SeekType, start:int, stop_type:Gst.SeekType, stop:int) -> bool """
        return False

    def seek_simple(self, format, seek_flags, seek_pos): # real signature unknown; restored from __doc__
        """ seek_simple(self, format:Gst.Format, seek_flags:Gst.SeekFlags, seek_pos:int) -> bool """
        return False

    def send_event(self, event): # real signature unknown; restored from __doc__
        """ send_event(self, event:Gst.Event) -> bool """
        return False

    def set_base_time(self, time): # real signature unknown; restored from __doc__
        """ set_base_time(self, time:int) """
        pass

    def set_bus(self, bus=None): # real signature unknown; restored from __doc__
        """ set_bus(self, bus:Gst.Bus=None) """
        pass

    def set_clock(self, clock=None): # real signature unknown; restored from __doc__
        """ set_clock(self, clock:Gst.Clock=None) -> bool """
        return False

    def set_context(self, context): # real signature unknown; restored from __doc__
        """ set_context(self, context:Gst.Context) """
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_locked_state(self, locked_state): # real signature unknown; restored from __doc__
        """ set_locked_state(self, locked_state:bool) -> bool """
        return False

    def set_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_start_time(self, time): # real signature unknown; restored from __doc__
        """ set_start_time(self, time:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gst.State) -> Gst.StateChangeReturn """
        pass

    def set_static_metadata(self, longname, classification, description, author): # real signature unknown; restored from __doc__
        """ set_static_metadata(self, longname:str, classification:str, description:str, author:str) """
        pass

    def set_tag_merge_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_tag_merge_mode(self, mode:Gst.TagMergeMode) """
        pass

    def state_change_return_get_name(self, state_ret): # real signature unknown; restored from __doc__
        """ state_change_return_get_name(state_ret:Gst.StateChangeReturn) -> str """
        return ""

    def state_get_name(self, state): # real signature unknown; restored from __doc__
        """ state_get_name(state:Gst.State) -> str """
        return ""

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

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_state_with_parent(self): # real signature unknown; restored from __doc__
        """ sync_state_with_parent(self) -> bool """
        return False

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlink(self, dest): # real signature unknown; restored from __doc__
        """ unlink(self, dest:Gst.Element) """
        pass

    def unlink_pads(self, srcpadname, dest, destpadname): # real signature unknown; restored from __doc__
        """ unlink_pads(self, srcpadname:str, dest:Gst.Element, destpadname:str) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    base_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_return = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numsrcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pads_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pending_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sinkpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    srcpads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f8c0ac13610>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TagMux), '__module__': 'gi.repository.GstTag', '__gtype__': <GType GstTagMux (94256106779504)>, '__doc__': None, '__gsignals__': {}, 'do_render_end_tag': gi.VFuncInfo(render_end_tag), 'do_render_start_tag': gi.VFuncInfo(render_start_tag), 'element': <property object at 0x7f8c0ac0fa90>, 'priv': <property object at 0x7f8c0ac0fbd0>, '_gst_reserved': <property object at 0x7f8c0ac0fcc0>})"
    __gdoc__ = 'Object GstTagMux\n\nSignals from GstElement:\n  pad-added (GstPad)\n  pad-removed (GstPad)\n  no-more-pads ()\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstTagMux (94256106779504)>'
    __info__ = ObjectInfo(TagMux)


class TagMuxClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TagMuxClass()
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_end_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_start_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TagMuxClass), '__module__': 'gi.repository.GstTag', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TagMuxClass' objects>, '__weakref__': <attribute '__weakref__' of 'TagMuxClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f8c0ac0fe50>, 'render_start_tag': <property object at 0x7f8c0ac0ff90>, 'render_end_tag': <property object at 0x7f8c0ac120e0>, '_gst_reserved': <property object at 0x7f8c0ac121d0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TagMuxClass)


class TagMuxPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TagMuxPrivate), '__module__': 'gi.repository.GstTag', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TagMuxPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'TagMuxPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TagMuxPrivate)


class TagXmpWriter(__gobject.GInterface):
    # no doc
    def add_all_schemas(self): # real signature unknown; restored from __doc__
        """ add_all_schemas(self) """
        pass

    def add_schema(self, schema): # real signature unknown; restored from __doc__
        """ add_schema(self, schema:str) """
        pass

    def has_schema(self, schema): # real signature unknown; restored from __doc__
        """ has_schema(self, schema:str) -> bool """
        return False

    def remove_all_schemas(self): # real signature unknown; restored from __doc__
        """ remove_all_schemas(self) """
        pass

    def remove_schema(self, schema): # real signature unknown; restored from __doc__
        """ remove_schema(self, schema:str) """
        pass

    def tag_list_to_xmp_buffer(self, taglist, read_only): # real signature unknown; restored from __doc__
        """ tag_list_to_xmp_buffer(self, taglist:Gst.TagList, read_only:bool) -> Gst.Buffer """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(TagXmpWriter), '__module__': 'gi.repository.GstTag', '__gtype__': <GType GstTagXmpWriter (94256106390064)>, '__dict__': <attribute '__dict__' of 'TagXmpWriter' objects>, '__weakref__': <attribute '__weakref__' of 'TagXmpWriter' objects>, '__doc__': None, '__gsignals__': {}, 'add_all_schemas': gi.FunctionInfo(add_all_schemas), 'add_schema': gi.FunctionInfo(add_schema), 'has_schema': gi.FunctionInfo(has_schema), 'remove_all_schemas': gi.FunctionInfo(remove_all_schemas), 'remove_schema': gi.FunctionInfo(remove_schema), 'tag_list_to_xmp_buffer': gi.FunctionInfo(tag_list_to_xmp_buffer)})"
    __gdoc__ = 'Interface GstTagXmpWriter\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstTagXmpWriter (94256106390064)>'
    __info__ = InterfaceInfo(TagXmpWriter)


class TagXmpWriterInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TagXmpWriterInterface()
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TagXmpWriterInterface), '__module__': 'gi.repository.GstTag', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TagXmpWriterInterface' objects>, '__weakref__': <attribute '__weakref__' of 'TagXmpWriterInterface' objects>, '__doc__': None, 'parent': <property object at 0x7f8c0ac12540>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TagXmpWriterInterface)


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f8c0ae3d1f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f8c0ae3d280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f8c0ae3d310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f8c0ae3d3a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f8c0ba79d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstTag-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstTag', loader=<gi.importer.DynamicImporter object at 0x7f8c0ba79d00>)"

