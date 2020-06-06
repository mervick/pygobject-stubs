# encoding: utf-8
# module gi.repository.GstVideo
# from /usr/lib64/girepository-1.0/GstVideo-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


# Variables with simple values

BUFFER_POOL_OPTION_VIDEO_AFFINE_TRANSFORMATION_META = 'GstBufferPoolOptionVideoAffineTransformation'

BUFFER_POOL_OPTION_VIDEO_ALIGNMENT = 'GstBufferPoolOptionVideoAlignment'

BUFFER_POOL_OPTION_VIDEO_GL_TEXTURE_UPLOAD_META = 'GstBufferPoolOptionVideoGLTextureUploadMeta'

BUFFER_POOL_OPTION_VIDEO_META = 'GstBufferPoolOptionVideoMeta'

CAPS_FEATURE_FORMAT_INTERLACED = 'format:Interlaced'

CAPS_FEATURE_META_GST_VIDEO_AFFINE_TRANSFORMATION_META = 'meta:GstVideoAffineTransformation'

CAPS_FEATURE_META_GST_VIDEO_GL_TEXTURE_UPLOAD_META = 'meta:GstVideoGLTextureUploadMeta'

CAPS_FEATURE_META_GST_VIDEO_META = 'meta:GstVideoMeta'

CAPS_FEATURE_META_GST_VIDEO_OVERLAY_COMPOSITION = 'meta:GstVideoOverlayComposition'

META_TAG_VIDEO_COLORSPACE_STR = 'colorspace'

META_TAG_VIDEO_ORIENTATION_STR = 'orientation'

META_TAG_VIDEO_SIZE_STR = 'size'

META_TAG_VIDEO_STR = 'video'

VIDEO_COLORIMETRY_BT2020 = 'bt2020'
VIDEO_COLORIMETRY_BT601 = 'bt601'
VIDEO_COLORIMETRY_BT709 = 'bt709'
VIDEO_COLORIMETRY_SMPTE240M = 'smpte240m'
VIDEO_COLORIMETRY_SRGB = 'sRGB'

VIDEO_COMP_A = 3
VIDEO_COMP_B = 2
VIDEO_COMP_G = 1
VIDEO_COMP_INDEX = 0
VIDEO_COMP_PALETTE = 1
VIDEO_COMP_R = 0
VIDEO_COMP_U = 1
VIDEO_COMP_V = 2
VIDEO_COMP_Y = 0

VIDEO_CONVERTER_OPT_ALPHA_MODE = 'GstVideoConverter.alpha-mode'
VIDEO_CONVERTER_OPT_ALPHA_VALUE = 'GstVideoConverter.alpha-value'

VIDEO_CONVERTER_OPT_BORDER_ARGB = 'GstVideoConverter.border-argb'

VIDEO_CONVERTER_OPT_CHROMA_MODE = 'GstVideoConverter.chroma-mode'

VIDEO_CONVERTER_OPT_CHROMA_RESAMPLER_METHOD = 'GstVideoConverter.chroma-resampler-method'

VIDEO_CONVERTER_OPT_DEST_HEIGHT = 'GstVideoConverter.dest-height'
VIDEO_CONVERTER_OPT_DEST_WIDTH = 'GstVideoConverter.dest-width'
VIDEO_CONVERTER_OPT_DEST_X = 'GstVideoConverter.dest-x'
VIDEO_CONVERTER_OPT_DEST_Y = 'GstVideoConverter.dest-y'

VIDEO_CONVERTER_OPT_DITHER_METHOD = 'GstVideoConverter.dither-method'
VIDEO_CONVERTER_OPT_DITHER_QUANTIZATION = 'GstVideoConverter.dither-quantization'

VIDEO_CONVERTER_OPT_FILL_BORDER = 'GstVideoConverter.fill-border'

VIDEO_CONVERTER_OPT_GAMMA_MODE = 'GstVideoConverter.gamma-mode'

VIDEO_CONVERTER_OPT_MATRIX_MODE = 'GstVideoConverter.matrix-mode'

VIDEO_CONVERTER_OPT_PRIMARIES_MODE = 'GstVideoConverter.primaries-mode'

VIDEO_CONVERTER_OPT_RESAMPLER_METHOD = 'GstVideoConverter.resampler-method'
VIDEO_CONVERTER_OPT_RESAMPLER_TAPS = 'GstVideoConverter.resampler-taps'

VIDEO_CONVERTER_OPT_SRC_HEIGHT = 'GstVideoConverter.src-height'
VIDEO_CONVERTER_OPT_SRC_WIDTH = 'GstVideoConverter.src-width'
VIDEO_CONVERTER_OPT_SRC_X = 'GstVideoConverter.src-x'
VIDEO_CONVERTER_OPT_SRC_Y = 'GstVideoConverter.src-y'

VIDEO_CONVERTER_OPT_THREADS = 'GstVideoConverter.threads'

VIDEO_DECODER_MAX_ERRORS = 10

VIDEO_DECODER_SINK_NAME = 'sink'

VIDEO_DECODER_SRC_NAME = 'src'

VIDEO_ENCODER_SINK_NAME = 'sink'

VIDEO_ENCODER_SRC_NAME = 'src'

VIDEO_FORMATS_ALL = '{ I420, YV12, YUY2, UYVY, AYUV, VUYA, RGBx, BGRx, xRGB, xBGR, RGBA, BGRA, ARGB, ABGR, RGB, BGR, Y41B, Y42B, YVYU, Y444, v210, v216, Y210, Y410, NV12, NV21, GRAY8, GRAY16_BE, GRAY16_LE, v308, RGB16, BGR16, RGB15, BGR15, UYVP, A420, RGB8P, YUV9, YVU9, IYU1, ARGB64, AYUV64, r210, I420_10BE, I420_10LE, I422_10BE, I422_10LE, Y444_10BE, Y444_10LE, GBR, GBR_10BE, GBR_10LE, NV16, NV24, NV12_64Z32, A420_10BE, A420_10LE, A422_10BE, A422_10LE, A444_10BE, A444_10LE, NV61, P010_10BE, P010_10LE, IYU2, VYUY, GBRA, GBRA_10BE, GBRA_10LE, BGR10A2_LE, GBR_12BE, GBR_12LE, GBRA_12BE, GBRA_12LE, I420_12BE, I420_12LE, I422_12BE, I422_12LE, Y444_12BE, Y444_12LE, GRAY10_LE32, NV12_10LE32, NV16_10LE32, NV12_10LE40 }'

VIDEO_FPS_RANGE = '(fraction) [ 0, max ]'

VIDEO_MAX_COMPONENTS = 4
VIDEO_MAX_PLANES = 4

VIDEO_OVERLAY_COMPOSITION_BLEND_FORMATS = '{ BGRx, RGBx, xRGB, xBGR, RGBA, BGRA, ARGB, ABGR, RGB, BGR, I420, YV12, AYUV, YUY2, UYVY, v308, Y41B, Y42B, Y444, NV12, NV21, A420, YUV9, YVU9, IYU1, GRAY8 }'

VIDEO_RESAMPLER_OPT_CUBIC_B = 'GstVideoResampler.cubic-b'
VIDEO_RESAMPLER_OPT_CUBIC_C = 'GstVideoResampler.cubic-c'

VIDEO_RESAMPLER_OPT_ENVELOPE = 'GstVideoResampler.envelope'

VIDEO_RESAMPLER_OPT_MAX_TAPS = 'GstVideoResampler.max-taps'

VIDEO_RESAMPLER_OPT_SHARPEN = 'GstVideoResampler.sharpen'
VIDEO_RESAMPLER_OPT_SHARPNESS = 'GstVideoResampler.sharpness'

VIDEO_SCALER_OPT_DITHER_METHOD = 'GstVideoScaler.dither-method'

VIDEO_SIZE_RANGE = '(int) [ 1, max ]'

VIDEO_TILE_TYPE_MASK = 65535
VIDEO_TILE_TYPE_SHIFT = 16

VIDEO_TILE_X_TILES_MASK = 65535

VIDEO_TILE_Y_TILES_SHIFT = 16

_namespace = 'GstVideo'

_version = '1.0'

__weakref__ = None

# functions

def buffer_add_video_affine_transformation_meta(buffer): # real signature unknown; restored from __doc__
    """ buffer_add_video_affine_transformation_meta(buffer:Gst.Buffer) -> GstVideo.VideoAffineTransformationMeta """
    pass

def buffer_add_video_caption_meta(buffer, caption_type, data): # real signature unknown; restored from __doc__
    """ buffer_add_video_caption_meta(buffer:Gst.Buffer, caption_type:GstVideo.VideoCaptionType, data:list) -> GstVideo.VideoCaptionMeta """
    pass

def buffer_add_video_gl_texture_upload_meta(buffer, texture_orientation, n_textures, texture_type, upload, user_data=None, user_data_copy, user_data_free): # real signature unknown; restored from __doc__
    """ buffer_add_video_gl_texture_upload_meta(buffer:Gst.Buffer, texture_orientation:GstVideo.VideoGLTextureOrientation, n_textures:int, texture_type:GstVideo.VideoGLTextureType, upload:GstVideo.VideoGLTextureUpload, user_data=None, user_data_copy:GObject.BoxedCopyFunc, user_data_free:GObject.BoxedFreeFunc) -> GstVideo.VideoGLTextureUploadMeta """
    pass

def buffer_add_video_meta(buffer, flags, format, width, height): # real signature unknown; restored from __doc__
    """ buffer_add_video_meta(buffer:Gst.Buffer, flags:GstVideo.VideoFrameFlags, format:GstVideo.VideoFormat, width:int, height:int) -> GstVideo.VideoMeta """
    pass

def buffer_add_video_meta_full(buffer, flags, format, width, height, n_planes, offset, stride): # real signature unknown; restored from __doc__
    """ buffer_add_video_meta_full(buffer:Gst.Buffer, flags:GstVideo.VideoFrameFlags, format:GstVideo.VideoFormat, width:int, height:int, n_planes:int, offset:list, stride:list) -> GstVideo.VideoMeta """
    pass

def buffer_add_video_overlay_composition_meta(buf, comp=None): # real signature unknown; restored from __doc__
    """ buffer_add_video_overlay_composition_meta(buf:Gst.Buffer, comp:GstVideo.VideoOverlayComposition=None) -> GstVideo.VideoOverlayCompositionMeta """
    pass

def buffer_add_video_region_of_interest_meta(buffer, roi_type, x, y, w, h): # real signature unknown; restored from __doc__
    """ buffer_add_video_region_of_interest_meta(buffer:Gst.Buffer, roi_type:str, x:int, y:int, w:int, h:int) -> GstVideo.VideoRegionOfInterestMeta """
    pass

def buffer_add_video_region_of_interest_meta_id(buffer, roi_type, x, y, w, h): # real signature unknown; restored from __doc__
    """ buffer_add_video_region_of_interest_meta_id(buffer:Gst.Buffer, roi_type:int, x:int, y:int, w:int, h:int) -> GstVideo.VideoRegionOfInterestMeta """
    pass

def buffer_add_video_time_code_meta(buffer, tc): # real signature unknown; restored from __doc__
    """ buffer_add_video_time_code_meta(buffer:Gst.Buffer, tc:GstVideo.VideoTimeCode) -> GstVideo.VideoTimeCodeMeta or None """
    pass

def buffer_add_video_time_code_meta_full(buffer, fps_n, fps_d, latest_daily_jam, flags, hours, minutes, seconds, frames, field_count): # real signature unknown; restored from __doc__
    """ buffer_add_video_time_code_meta_full(buffer:Gst.Buffer, fps_n:int, fps_d:int, latest_daily_jam:GLib.DateTime, flags:GstVideo.VideoTimeCodeFlags, hours:int, minutes:int, seconds:int, frames:int, field_count:int) -> GstVideo.VideoTimeCodeMeta """
    pass

def buffer_get_video_meta(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_video_meta(buffer:Gst.Buffer) -> GstVideo.VideoMeta """
    pass

def buffer_get_video_meta_id(buffer, id): # real signature unknown; restored from __doc__
    """ buffer_get_video_meta_id(buffer:Gst.Buffer, id:int) -> GstVideo.VideoMeta """
    pass

def buffer_get_video_region_of_interest_meta_id(buffer, id): # real signature unknown; restored from __doc__
    """ buffer_get_video_region_of_interest_meta_id(buffer:Gst.Buffer, id:int) -> GstVideo.VideoRegionOfInterestMeta """
    pass

def buffer_pool_config_get_video_alignment(config, align): # real signature unknown; restored from __doc__
    """ buffer_pool_config_get_video_alignment(config:Gst.Structure, align:GstVideo.VideoAlignment) -> bool """
    return False

def buffer_pool_config_set_video_alignment(config, align): # real signature unknown; restored from __doc__
    """ buffer_pool_config_set_video_alignment(config:Gst.Structure, align:GstVideo.VideoAlignment) """
    pass

def is_video_overlay_prepare_window_handle_message(msg): # real signature unknown; restored from __doc__
    """ is_video_overlay_prepare_window_handle_message(msg:Gst.Message) -> bool """
    return False

def navigation_event_get_type(event): # real signature unknown; restored from __doc__
    """ navigation_event_get_type(event:Gst.Event) -> GstVideo.NavigationEventType """
    pass

def navigation_event_parse_command(event): # real signature unknown; restored from __doc__
    """ navigation_event_parse_command(event:Gst.Event) -> bool, command:GstVideo.NavigationCommand """
    return False

def navigation_event_parse_key_event(event): # real signature unknown; restored from __doc__
    """ navigation_event_parse_key_event(event:Gst.Event) -> bool, key:str """
    return False

def navigation_event_parse_mouse_button_event(event): # real signature unknown; restored from __doc__
    """ navigation_event_parse_mouse_button_event(event:Gst.Event) -> bool, button:int, x:float, y:float """
    return False

def navigation_event_parse_mouse_move_event(event): # real signature unknown; restored from __doc__
    """ navigation_event_parse_mouse_move_event(event:Gst.Event) -> bool, x:float, y:float """
    return False

def navigation_message_get_type(message): # real signature unknown; restored from __doc__
    """ navigation_message_get_type(message:Gst.Message) -> GstVideo.NavigationMessageType """
    pass

def navigation_message_new_angles_changed(src, cur_angle, n_angles): # real signature unknown; restored from __doc__
    """ navigation_message_new_angles_changed(src:Gst.Object, cur_angle:int, n_angles:int) -> Gst.Message """
    pass

def navigation_message_new_commands_changed(src): # real signature unknown; restored from __doc__
    """ navigation_message_new_commands_changed(src:Gst.Object) -> Gst.Message """
    pass

def navigation_message_new_event(src, event): # real signature unknown; restored from __doc__
    """ navigation_message_new_event(src:Gst.Object, event:Gst.Event) -> Gst.Message """
    pass

def navigation_message_new_mouse_over(src, active): # real signature unknown; restored from __doc__
    """ navigation_message_new_mouse_over(src:Gst.Object, active:bool) -> Gst.Message """
    pass

def navigation_message_parse_angles_changed(message): # real signature unknown; restored from __doc__
    """ navigation_message_parse_angles_changed(message:Gst.Message) -> bool, cur_angle:int, n_angles:int """
    return False

def navigation_message_parse_event(message): # real signature unknown; restored from __doc__
    """ navigation_message_parse_event(message:Gst.Message) -> bool, event:Gst.Event """
    return False

def navigation_message_parse_mouse_over(message): # real signature unknown; restored from __doc__
    """ navigation_message_parse_mouse_over(message:Gst.Message) -> bool, active:bool """
    return False

def navigation_query_get_type(query): # real signature unknown; restored from __doc__
    """ navigation_query_get_type(query:Gst.Query) -> GstVideo.NavigationQueryType """
    pass

def navigation_query_new_angles(): # real signature unknown; restored from __doc__
    """ navigation_query_new_angles() -> Gst.Query """
    pass

def navigation_query_new_commands(): # real signature unknown; restored from __doc__
    """ navigation_query_new_commands() -> Gst.Query """
    pass

def navigation_query_parse_angles(query): # real signature unknown; restored from __doc__
    """ navigation_query_parse_angles(query:Gst.Query) -> bool, cur_angle:int, n_angles:int """
    return False

def navigation_query_parse_commands_length(query): # real signature unknown; restored from __doc__
    """ navigation_query_parse_commands_length(query:Gst.Query) -> bool, n_cmds:int """
    return False

def navigation_query_parse_commands_nth(query, nth): # real signature unknown; restored from __doc__
    """ navigation_query_parse_commands_nth(query:Gst.Query, nth:int) -> bool, cmd:GstVideo.NavigationCommand """
    return False

def navigation_query_set_angles(query, cur_angle, n_angles): # real signature unknown; restored from __doc__
    """ navigation_query_set_angles(query:Gst.Query, cur_angle:int, n_angles:int) """
    pass

def navigation_query_set_commandsv(query, cmds): # real signature unknown; restored from __doc__
    """ navigation_query_set_commandsv(query:Gst.Query, cmds:list) """
    pass

def video_affine_transformation_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_affine_transformation_meta_api_get_type() -> GType """
    pass

def video_affine_transformation_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_affine_transformation_meta_get_info() -> Gst.MetaInfo """
    pass

def video_blend(dest, src, x, y, global_alpha): # real signature unknown; restored from __doc__
    """ video_blend(dest:GstVideo.VideoFrame, src:GstVideo.VideoFrame, x:int, y:int, global_alpha:float) -> bool """
    return False

def video_blend_scale_linear_RGBA(src, src_buffer, dest_height, dest_width): # real signature unknown; restored from __doc__
    """ video_blend_scale_linear_RGBA(src:GstVideo.VideoInfo, src_buffer:Gst.Buffer, dest_height:int, dest_width:int) -> dest:GstVideo.VideoInfo, dest_buffer:Gst.Buffer """
    pass

def video_calculate_display_ratio(video_width, video_height, video_par_n, video_par_d, display_par_n, display_par_d): # real signature unknown; restored from __doc__
    """ video_calculate_display_ratio(video_width:int, video_height:int, video_par_n:int, video_par_d:int, display_par_n:int, display_par_d:int) -> bool, dar_n:int, dar_d:int """
    return False

def video_caption_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_caption_meta_api_get_type() -> GType """
    pass

def video_caption_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_caption_meta_get_info() -> Gst.MetaInfo """
    pass

def video_caption_type_from_caps(caps): # real signature unknown; restored from __doc__
    """ video_caption_type_from_caps(caps:Gst.Caps) -> GstVideo.VideoCaptionType """
    pass

def video_caption_type_to_caps(type): # real signature unknown; restored from __doc__
    """ video_caption_type_to_caps(type:GstVideo.VideoCaptionType) -> Gst.Caps """
    pass

def video_chroma_from_string(s): # real signature unknown; restored from __doc__
    """ video_chroma_from_string(s:str) -> GstVideo.VideoChromaSite """
    pass

def video_chroma_resample(resample, lines=None, width): # real signature unknown; restored from __doc__
    """ video_chroma_resample(resample:GstVideo.VideoChromaResample, lines=None, width:int) """
    pass

def video_chroma_to_string(site): # real signature unknown; restored from __doc__
    """ video_chroma_to_string(site:GstVideo.VideoChromaSite) -> str """
    return ""

def video_color_matrix_get_Kr_Kb(matrix): # real signature unknown; restored from __doc__
    """ video_color_matrix_get_Kr_Kb(matrix:GstVideo.VideoColorMatrix) -> bool, Kr:float, Kb:float """
    return False

def video_color_primaries_get_info(primaries): # real signature unknown; restored from __doc__
    """ video_color_primaries_get_info(primaries:GstVideo.VideoColorPrimaries) -> GstVideo.VideoColorPrimariesInfo """
    pass

def video_color_range_offsets(range, info): # real signature unknown; restored from __doc__
    """ video_color_range_offsets(range:GstVideo.VideoColorRange, info:GstVideo.VideoFormatInfo) -> offset:list, scale:list """
    pass

def video_color_transfer_decode(func, val): # real signature unknown; restored from __doc__
    """ video_color_transfer_decode(func:GstVideo.VideoTransferFunction, val:float) -> float """
    return 0.0

def video_color_transfer_encode(func, val): # real signature unknown; restored from __doc__
    """ video_color_transfer_encode(func:GstVideo.VideoTransferFunction, val:float) -> float """
    return 0.0

def video_convert_sample(sample, to_caps, timeout): # real signature unknown; restored from __doc__
    """ video_convert_sample(sample:Gst.Sample, to_caps:Gst.Caps, timeout:int) -> Gst.Sample """
    pass

def video_convert_sample_async(sample, to_caps, timeout, callback, user_data=None): # real signature unknown; restored from __doc__
    """ video_convert_sample_async(sample:Gst.Sample, to_caps:Gst.Caps, timeout:int, callback:GstVideo.VideoConvertSampleCallback, user_data=None) """
    pass

def video_crop_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_crop_meta_api_get_type() -> GType """
    pass

def video_crop_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_crop_meta_get_info() -> Gst.MetaInfo """
    pass

def video_event_is_force_key_unit(event): # real signature unknown; restored from __doc__
    """ video_event_is_force_key_unit(event:Gst.Event) -> bool """
    return False

def video_event_new_downstream_force_key_unit(timestamp, stream_time, running_time, all_headers, count): # real signature unknown; restored from __doc__
    """ video_event_new_downstream_force_key_unit(timestamp:int, stream_time:int, running_time:int, all_headers:bool, count:int) -> Gst.Event """
    pass

def video_event_new_still_frame(in_still): # real signature unknown; restored from __doc__
    """ video_event_new_still_frame(in_still:bool) -> Gst.Event """
    pass

def video_event_new_upstream_force_key_unit(running_time, all_headers, count): # real signature unknown; restored from __doc__
    """ video_event_new_upstream_force_key_unit(running_time:int, all_headers:bool, count:int) -> Gst.Event """
    pass

def video_event_parse_downstream_force_key_unit(event): # real signature unknown; restored from __doc__
    """ video_event_parse_downstream_force_key_unit(event:Gst.Event) -> bool, timestamp:int, stream_time:int, running_time:int, all_headers:bool, count:int """
    return False

def video_event_parse_still_frame(event): # real signature unknown; restored from __doc__
    """ video_event_parse_still_frame(event:Gst.Event) -> bool, in_still:bool """
    return False

def video_event_parse_upstream_force_key_unit(event): # real signature unknown; restored from __doc__
    """ video_event_parse_upstream_force_key_unit(event:Gst.Event) -> bool, running_time:int, all_headers:bool, count:int """
    return False

def video_field_order_from_string(order): # real signature unknown; restored from __doc__
    """ video_field_order_from_string(order:str) -> GstVideo.VideoFieldOrder """
    pass

def video_field_order_to_string(order): # real signature unknown; restored from __doc__
    """ video_field_order_to_string(order:GstVideo.VideoFieldOrder) -> str """
    return ""

def video_format_from_fourcc(fourcc): # real signature unknown; restored from __doc__
    """ video_format_from_fourcc(fourcc:int) -> GstVideo.VideoFormat """
    pass

def video_format_from_masks(depth, bpp, endianness, red_mask, green_mask, blue_mask, alpha_mask): # real signature unknown; restored from __doc__
    """ video_format_from_masks(depth:int, bpp:int, endianness:int, red_mask:int, green_mask:int, blue_mask:int, alpha_mask:int) -> GstVideo.VideoFormat """
    pass

def video_format_from_string(format): # real signature unknown; restored from __doc__
    """ video_format_from_string(format:str) -> GstVideo.VideoFormat """
    pass

def video_format_get_info(format): # real signature unknown; restored from __doc__
    """ video_format_get_info(format:GstVideo.VideoFormat) -> GstVideo.VideoFormatInfo """
    pass

def video_format_get_palette(format): # real signature unknown; restored from __doc__
    """ video_format_get_palette(format:GstVideo.VideoFormat) -> size:int """
    pass

def video_format_to_fourcc(format): # real signature unknown; restored from __doc__
    """ video_format_to_fourcc(format:GstVideo.VideoFormat) -> int """
    return 0

def video_format_to_string(format): # real signature unknown; restored from __doc__
    """ video_format_to_string(format:GstVideo.VideoFormat) -> str """
    return ""

def video_gl_texture_upload_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_gl_texture_upload_meta_api_get_type() -> GType """
    pass

def video_gl_texture_upload_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_gl_texture_upload_meta_get_info() -> Gst.MetaInfo """
    pass

def video_guess_framerate(duration): # real signature unknown; restored from __doc__
    """ video_guess_framerate(duration:int) -> bool, dest_n:int, dest_d:int """
    return False

def video_interlace_mode_from_string(mode): # real signature unknown; restored from __doc__
    """ video_interlace_mode_from_string(mode:str) -> GstVideo.VideoInterlaceMode """
    pass

def video_interlace_mode_to_string(mode): # real signature unknown; restored from __doc__
    """ video_interlace_mode_to_string(mode:GstVideo.VideoInterlaceMode) -> str """
    return ""

def video_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_meta_api_get_type() -> GType """
    pass

def video_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_meta_get_info() -> Gst.MetaInfo """
    pass

def video_meta_transform_scale_get_quark(): # real signature unknown; restored from __doc__
    """ video_meta_transform_scale_get_quark() -> int """
    return 0

def video_multiview_get_doubled_height_modes(): # real signature unknown; restored from __doc__
    """ video_multiview_get_doubled_height_modes() -> GObject.Value """
    pass

def video_multiview_get_doubled_size_modes(): # real signature unknown; restored from __doc__
    """ video_multiview_get_doubled_size_modes() -> GObject.Value """
    pass

def video_multiview_get_doubled_width_modes(): # real signature unknown; restored from __doc__
    """ video_multiview_get_doubled_width_modes() -> GObject.Value """
    pass

def video_multiview_get_mono_modes(): # real signature unknown; restored from __doc__
    """ video_multiview_get_mono_modes() -> GObject.Value """
    pass

def video_multiview_get_unpacked_modes(): # real signature unknown; restored from __doc__
    """ video_multiview_get_unpacked_modes() -> GObject.Value """
    pass

def video_multiview_guess_half_aspect(mv_mode, width, height, par_n, par_d): # real signature unknown; restored from __doc__
    """ video_multiview_guess_half_aspect(mv_mode:GstVideo.VideoMultiviewMode, width:int, height:int, par_n:int, par_d:int) -> bool """
    return False

def video_multiview_mode_from_caps_string(caps_mview_mode): # real signature unknown; restored from __doc__
    """ video_multiview_mode_from_caps_string(caps_mview_mode:str) -> GstVideo.VideoMultiviewMode """
    pass

def video_multiview_mode_to_caps_string(mview_mode): # real signature unknown; restored from __doc__
    """ video_multiview_mode_to_caps_string(mview_mode:GstVideo.VideoMultiviewMode) -> str """
    return ""

def video_multiview_video_info_change_mode(info, out_mview_mode, out_mview_flags): # real signature unknown; restored from __doc__
    """ video_multiview_video_info_change_mode(info:GstVideo.VideoInfo, out_mview_mode:GstVideo.VideoMultiviewMode, out_mview_flags:GstVideo.VideoMultiviewFlags) """
    pass

def video_overlay_composition_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_overlay_composition_meta_api_get_type() -> GType """
    pass

def video_overlay_composition_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_overlay_composition_meta_get_info() -> Gst.MetaInfo """
    pass

def video_overlay_install_properties(oclass, last_prop_id): # real signature unknown; restored from __doc__
    """ video_overlay_install_properties(oclass:GObject.ObjectClass, last_prop_id:int) """
    pass

def video_overlay_set_property(p_object, last_prop_id, property_id, value): # real signature unknown; restored from __doc__
    """ video_overlay_set_property(object:GObject.Object, last_prop_id:int, property_id:int, value:GObject.Value) -> bool """
    return False

def video_region_of_interest_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_region_of_interest_meta_api_get_type() -> GType """
    pass

def video_region_of_interest_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_region_of_interest_meta_get_info() -> Gst.MetaInfo """
    pass

def video_tile_get_index(mode, x, y, x_tiles, y_tiles): # real signature unknown; restored from __doc__
    """ video_tile_get_index(mode:GstVideo.VideoTileMode, x:int, y:int, x_tiles:int, y_tiles:int) -> int """
    return 0

def video_time_code_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ video_time_code_meta_api_get_type() -> GType """
    pass

def video_time_code_meta_get_info(): # real signature unknown; restored from __doc__
    """ video_time_code_meta_get_info() -> Gst.MetaInfo """
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

from .ColorBalance import ColorBalance
from .ColorBalanceChannel import ColorBalanceChannel
from .ColorBalanceChannelClass import ColorBalanceChannelClass
from .ColorBalanceInterface import ColorBalanceInterface
from .ColorBalanceType import ColorBalanceType
from .Navigation import Navigation
from .NavigationCommand import NavigationCommand
from .NavigationEventType import NavigationEventType
from .NavigationInterface import NavigationInterface
from .NavigationMessageType import NavigationMessageType
from .NavigationQueryType import NavigationQueryType
from .VideoAffineTransformationMeta import VideoAffineTransformationMeta
from .VideoAggregator import VideoAggregator
from .VideoAggregatorClass import VideoAggregatorClass
from .VideoAggregatorPad import VideoAggregatorPad
from .VideoAggregatorConvertPad import VideoAggregatorConvertPad
from .VideoAggregatorConvertPadClass import VideoAggregatorConvertPadClass
from .VideoAggregatorConvertPadPrivate import VideoAggregatorConvertPadPrivate
from .VideoAggregatorPadClass import VideoAggregatorPadClass
from .VideoAggregatorPadPrivate import VideoAggregatorPadPrivate
from .VideoAggregatorPrivate import VideoAggregatorPrivate
from .VideoAlignment import VideoAlignment
from .VideoAlphaMode import VideoAlphaMode
from .VideoAncillary import VideoAncillary
from .VideoAncillaryDID import VideoAncillaryDID
from .VideoAncillaryDID16 import VideoAncillaryDID16
from .VideoBufferFlags import VideoBufferFlags
from .VideoBufferPool import VideoBufferPool
from .VideoBufferPoolClass import VideoBufferPoolClass
from .VideoBufferPoolPrivate import VideoBufferPoolPrivate
from .VideoCaptionMeta import VideoCaptionMeta
from .VideoCaptionType import VideoCaptionType
from .VideoChromaFlags import VideoChromaFlags
from .VideoChromaMethod import VideoChromaMethod
from .VideoChromaMode import VideoChromaMode
from .VideoChromaResample import VideoChromaResample
from .VideoChromaSite import VideoChromaSite
from .VideoCodecFrame import VideoCodecFrame
from .VideoCodecFrameFlags import VideoCodecFrameFlags
from .VideoCodecState import VideoCodecState
from .VideoColorimetry import VideoColorimetry
from .VideoColorMatrix import VideoColorMatrix
from .VideoColorPrimaries import VideoColorPrimaries
from .VideoColorPrimariesInfo import VideoColorPrimariesInfo
from .VideoColorRange import VideoColorRange
from .VideoConverter import VideoConverter
from .VideoCropMeta import VideoCropMeta
from .VideoDecoder import VideoDecoder
from .VideoDecoderClass import VideoDecoderClass
from .VideoDecoderPrivate import VideoDecoderPrivate
from .VideoDirection import VideoDirection
from .VideoDirectionInterface import VideoDirectionInterface
from .VideoDither import VideoDither
from .VideoDitherFlags import VideoDitherFlags
from .VideoDitherMethod import VideoDitherMethod
from .VideoEncoder import VideoEncoder
from .VideoEncoderClass import VideoEncoderClass
from .VideoEncoderPrivate import VideoEncoderPrivate
from .VideoFieldOrder import VideoFieldOrder
from .VideoFilter import VideoFilter
from .VideoFilterClass import VideoFilterClass
from .VideoFlags import VideoFlags
from .VideoFormat import VideoFormat
from .VideoFormatFlags import VideoFormatFlags
from .VideoFormatInfo import VideoFormatInfo
from .VideoFrame import VideoFrame
from .VideoFrameFlags import VideoFrameFlags
from .VideoFrameMapFlags import VideoFrameMapFlags
from .VideoGammaMode import VideoGammaMode
from .VideoGLTextureOrientation import VideoGLTextureOrientation
from .VideoGLTextureType import VideoGLTextureType
from .VideoGLTextureUploadMeta import VideoGLTextureUploadMeta
from .VideoInfo import VideoInfo
from .VideoInterlaceMode import VideoInterlaceMode
from .VideoMatrixMode import VideoMatrixMode
from .VideoMeta import VideoMeta
from .VideoMetaTransform import VideoMetaTransform
from .VideoMultiviewFlags import VideoMultiviewFlags
from .VideoMultiviewFlagsSet import VideoMultiviewFlagsSet
from .VideoMultiviewFramePacking import VideoMultiviewFramePacking
from .VideoMultiviewMode import VideoMultiviewMode
from .VideoOrientation import VideoOrientation
from .VideoOrientationInterface import VideoOrientationInterface
from .VideoOrientationMethod import VideoOrientationMethod
from .VideoOverlay import VideoOverlay
from .VideoOverlayComposition import VideoOverlayComposition
from .VideoOverlayCompositionMeta import VideoOverlayCompositionMeta
from .VideoOverlayFormatFlags import VideoOverlayFormatFlags
from .VideoOverlayInterface import VideoOverlayInterface
from .VideoOverlayRectangle import VideoOverlayRectangle
from .VideoPackFlags import VideoPackFlags
from .VideoPrimariesMode import VideoPrimariesMode
from .VideoRectangle import VideoRectangle
from .VideoRegionOfInterestMeta import VideoRegionOfInterestMeta
from .VideoResampler import VideoResampler
from .VideoResamplerFlags import VideoResamplerFlags
from .VideoResamplerMethod import VideoResamplerMethod
from .VideoScaler import VideoScaler
from .VideoScalerFlags import VideoScalerFlags
from .VideoSink import VideoSink
from .VideoSinkClass import VideoSinkClass
from .VideoSinkPrivate import VideoSinkPrivate
from .VideoTileMode import VideoTileMode
from .VideoTileType import VideoTileType
from .VideoTimeCode import VideoTimeCode
from .VideoTimeCodeConfig import VideoTimeCodeConfig
from .VideoTimeCodeFlags import VideoTimeCodeFlags
from .VideoTimeCodeInterval import VideoTimeCodeInterval
from .VideoTimeCodeMeta import VideoTimeCodeMeta
from .VideoTransferFunction import VideoTransferFunction
from .VideoVBIEncoder import VideoVBIEncoder
from .VideoVBIParser import VideoVBIParser
from .VideoVBIParserResult import VideoVBIParserResult
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f930e46cd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstVideo-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstVideo', loader=<gi.importer.DynamicImporter object at 0x7f930e46cd00>)"

