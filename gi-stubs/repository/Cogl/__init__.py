# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
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
import gobject as __gobject


# Variables with simple values

AFIRST_BIT = 64

A_BIT = 16

BGR_BIT = 32

DEPTH_BIT = 256

PREMULT_BIT = 128

STENCIL_BIT = 512

TEXTURE_MAX_WASTE = 127

VERSION_COMPONENT_BITS = 10

VERSION_MAX_COMPONENT_VALUE = 0

_namespace = 'Cogl'

_version = '2.0'

__weakref__ = None

# functions

def bitmap_error_quark(): # real signature unknown; restored from __doc__
    """ bitmap_error_quark() -> int """
    return 0

def blend_string_error_quark(): # real signature unknown; restored from __doc__
    """ blend_string_error_quark() -> int """
    return 0

def buffer_get_size(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_size(buffer) -> int """
    return 0

def buffer_get_update_hint(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_update_hint(buffer) -> Cogl.BufferUpdateHint """
    pass

def buffer_map(buffer, access, hints): # real signature unknown; restored from __doc__
    """ buffer_map(buffer, access:Cogl.BufferAccess, hints:Cogl.BufferMapHint) """
    pass

def buffer_map_range(buffer, offset, size, access, hints): # real signature unknown; restored from __doc__
    """ buffer_map_range(buffer, offset:int, size:int, access:Cogl.BufferAccess, hints:Cogl.BufferMapHint) """
    pass

def buffer_set_data(buffer, offset, data=None, size): # real signature unknown; restored from __doc__
    """ buffer_set_data(buffer, offset:int, data=None, size:int) -> int """
    return 0

def buffer_set_update_hint(buffer, hint): # real signature unknown; restored from __doc__
    """ buffer_set_update_hint(buffer, hint:Cogl.BufferUpdateHint) """
    pass

def buffer_unmap(buffer): # real signature unknown; restored from __doc__
    """ buffer_unmap(buffer) """
    pass

def color_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ color_equal(v1=None, v2=None) -> int """
    return 0

def color_init_from_hsl(hue, saturation, luminance): # real signature unknown; restored from __doc__
    """ color_init_from_hsl(hue:float, saturation:float, luminance:float) -> color:Cogl.Color """
    pass

def debug_matrix_entry_print(entry): # real signature unknown; restored from __doc__
    """ debug_matrix_entry_print(entry:Cogl.MatrixEntry) """
    pass

def debug_matrix_print(matrix): # real signature unknown; restored from __doc__
    """ debug_matrix_print(matrix:Cogl.Matrix) """
    pass

def debug_object_foreach_type(func, user_data=None): # real signature unknown; restored from __doc__
    """ debug_object_foreach_type(func:Cogl.DebugObjectForeachTypeCallback, user_data=None) """
    pass

def debug_object_print_instances(): # real signature unknown; restored from __doc__
    """ debug_object_print_instances() """
    pass

def error_copy(error): # real signature unknown; restored from __doc__
    """ error_copy(error:error) -> error """
    pass

def error_free(error): # real signature unknown; restored from __doc__
    """ error_free(error:error) """
    pass

def error_matches(error, domain, code): # real signature unknown; restored from __doc__
    """ error_matches(error:error, domain:int, code:int) -> int """
    return 0

def euler_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ euler_equal(v1=None, v2=None) -> int """
    return 0

def foreach_feature(context, callback, user_data=None): # real signature unknown; restored from __doc__
    """ foreach_feature(context:Cogl.Context, callback:Cogl.FeatureCallback, user_data=None) """
    pass

def framebuffer_error_quark(): # real signature unknown; restored from __doc__
    """ framebuffer_error_quark() -> int """
    return 0

def get_clock_time(context): # real signature unknown; restored from __doc__
    """ get_clock_time(context:Cogl.Context) -> int """
    return 0

def get_draw_framebuffer(): # real signature unknown; restored from __doc__
    """ get_draw_framebuffer() -> Cogl.Framebuffer """
    pass

def get_static_identity_quaternion(): # real signature unknown; restored from __doc__
    """ get_static_identity_quaternion() -> Cogl.Quaternion """
    pass

def get_static_zero_quaternion(): # real signature unknown; restored from __doc__
    """ get_static_zero_quaternion() -> Cogl.Quaternion """
    pass

def gles2_texture_get_handle(texture, handle, target): # real signature unknown; restored from __doc__
    """ gles2_texture_get_handle(texture:Cogl.Texture, handle:int, target:int) -> int """
    return 0

def glib_renderer_source_new(renderer, priority): # real signature unknown; restored from __doc__
    """ glib_renderer_source_new(renderer:Cogl.Renderer, priority:int) -> GLib.Source """
    pass

def glib_source_new(context, priority): # real signature unknown; restored from __doc__
    """ glib_source_new(context:Cogl.Context, priority:int) -> GLib.Source """
    pass

def gtype_matrix_get_type(): # real signature unknown; restored from __doc__
    """ gtype_matrix_get_type() -> GType """
    pass

def handle_get_type(): # real signature unknown; restored from __doc__
    """ handle_get_type() -> GType """
    pass

def handle_ref(handle): # real signature unknown; restored from __doc__
    """ handle_ref(handle) """
    pass

def handle_unref(handle): # real signature unknown; restored from __doc__
    """ handle_unref(handle) """
    pass

def has_feature(context, feature): # real signature unknown; restored from __doc__
    """ has_feature(context:Cogl.Context, feature:Cogl.FeatureID) -> int """
    return 0

def is_atlas_texture(p_object=None): # real signature unknown; restored from __doc__
    """ is_atlas_texture(object=None) -> int """
    return 0

def is_attribute(p_object=None): # real signature unknown; restored from __doc__
    """ is_attribute(object=None) -> int """
    return 0

def is_attribute_buffer(p_object=None): # real signature unknown; restored from __doc__
    """ is_attribute_buffer(object=None) -> int """
    return 0

def is_bitmap(p_object=None): # real signature unknown; restored from __doc__
    """ is_bitmap(object=None) -> int """
    return 0

def is_buffer(p_object=None): # real signature unknown; restored from __doc__
    """ is_buffer(object=None) -> int """
    return 0

def is_context(p_object=None): # real signature unknown; restored from __doc__
    """ is_context(object=None) -> int """
    return 0

def is_display(p_object=None): # real signature unknown; restored from __doc__
    """ is_display(object=None) -> int """
    return 0

def is_framebuffer(p_object=None): # real signature unknown; restored from __doc__
    """ is_framebuffer(object=None) -> int """
    return 0

def is_frame_info(p_object=None): # real signature unknown; restored from __doc__
    """ is_frame_info(object=None) -> int """
    return 0

def is_gles2_context(p_object=None): # real signature unknown; restored from __doc__
    """ is_gles2_context(object=None) -> int """
    return 0

def is_index_buffer(p_object=None): # real signature unknown; restored from __doc__
    """ is_index_buffer(object=None) -> int """
    return 0

def is_indices(p_object=None): # real signature unknown; restored from __doc__
    """ is_indices(object=None) -> int """
    return 0

def is_matrix_stack(p_object=None): # real signature unknown; restored from __doc__
    """ is_matrix_stack(object=None) -> int """
    return 0

def is_onscreen(p_object=None): # real signature unknown; restored from __doc__
    """ is_onscreen(object=None) -> int """
    return 0

def is_onscreen_template(p_object=None): # real signature unknown; restored from __doc__
    """ is_onscreen_template(object=None) -> int """
    return 0

def is_output(p_object=None): # real signature unknown; restored from __doc__
    """ is_output(object=None) -> int """
    return 0

def is_pipeline(p_object=None): # real signature unknown; restored from __doc__
    """ is_pipeline(object=None) -> int """
    return 0

def is_pixel_buffer(p_object=None): # real signature unknown; restored from __doc__
    """ is_pixel_buffer(object=None) -> int """
    return 0

def is_primitive(p_object=None): # real signature unknown; restored from __doc__
    """ is_primitive(object=None) -> int """
    return 0

def is_primitive_texture(p_object=None): # real signature unknown; restored from __doc__
    """ is_primitive_texture(object=None) -> int """
    return 0

def is_renderer(p_object=None): # real signature unknown; restored from __doc__
    """ is_renderer(object=None) -> int """
    return 0

def is_snippet(p_object=None): # real signature unknown; restored from __doc__
    """ is_snippet(object=None) -> int """
    return 0

def is_sub_texture(p_object=None): # real signature unknown; restored from __doc__
    """ is_sub_texture(object=None) -> int """
    return 0

def is_swap_chain(p_object=None): # real signature unknown; restored from __doc__
    """ is_swap_chain(object=None) -> int """
    return 0

def is_texture(p_object=None): # real signature unknown; restored from __doc__
    """ is_texture(object=None) -> int """
    return 0

def is_texture_2d(p_object=None): # real signature unknown; restored from __doc__
    """ is_texture_2d(object=None) -> int """
    return 0

def is_texture_2d_sliced(p_object=None): # real signature unknown; restored from __doc__
    """ is_texture_2d_sliced(object=None) -> int """
    return 0

def is_texture_3d(p_object=None): # real signature unknown; restored from __doc__
    """ is_texture_3d(object=None) -> int """
    return 0

def is_texture_pixmap_x11(p_object=None): # real signature unknown; restored from __doc__
    """ is_texture_pixmap_x11(object=None) -> int """
    return 0

def is_texture_rectangle(p_object=None): # real signature unknown; restored from __doc__
    """ is_texture_rectangle(object=None) -> int """
    return 0

def kms_display_queue_modes_reset(display): # real signature unknown; restored from __doc__
    """ kms_display_queue_modes_reset(display:Cogl.Display) """
    pass

def kms_display_set_ignore_crtc(display, id, ignore): # real signature unknown; restored from __doc__
    """ kms_display_set_ignore_crtc(display:Cogl.Display, id:int, ignore:int) """
    pass

def kms_display_set_layout(display, width, height, crtcs, n_crtcs): # real signature unknown; restored from __doc__
    """ kms_display_set_layout(display:Cogl.Display, width:int, height:int, crtcs:Cogl.KmsCrtc, n_crtcs:int) -> int """
    return 0

def kms_renderer_get_gbm(renderer): # real signature unknown; restored from __doc__
    """ kms_renderer_get_gbm(renderer:Cogl.Renderer) """
    pass

def kms_renderer_get_kms_fd(renderer): # real signature unknown; restored from __doc__
    """ kms_renderer_get_kms_fd(renderer:Cogl.Renderer) -> int """
    return 0

def kms_renderer_set_kms_fd(renderer, fd): # real signature unknown; restored from __doc__
    """ kms_renderer_set_kms_fd(renderer:Cogl.Renderer, fd:int) """
    pass

def matrix_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ matrix_equal(v1=None, v2=None) -> int """
    return 0

def poll_renderer_dispatch(renderer, poll_fds, n_poll_fds): # real signature unknown; restored from __doc__
    """ poll_renderer_dispatch(renderer:Cogl.Renderer, poll_fds:Cogl.PollFD, n_poll_fds:int) """
    pass

def poll_renderer_get_info(renderer, poll_fds, n_poll_fds, timeout): # real signature unknown; restored from __doc__
    """ poll_renderer_get_info(renderer:Cogl.Renderer, poll_fds:Cogl.PollFD, n_poll_fds:int, timeout:int) -> int """
    return 0

def pop_gles2_context(ctx): # real signature unknown; restored from __doc__
    """ pop_gles2_context(ctx:Cogl.Context) """
    pass

def push_gles2_context(ctx, gles2_ctx, read_buffer, write_buffer): # real signature unknown; restored from __doc__
    """ push_gles2_context(ctx:Cogl.Context, gles2_ctx:Cogl.GLES2Context, read_buffer:Cogl.Framebuffer, write_buffer:Cogl.Framebuffer) -> int """
    return 0

def quaternion_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ quaternion_equal(v1=None, v2=None) -> int """
    return 0

def renderer_error_quark(): # real signature unknown; restored from __doc__
    """ renderer_error_quark() -> int """
    return 0

def texture_error_quark(): # real signature unknown; restored from __doc__
    """ texture_error_quark() -> int """
    return 0

def vector3_add(result, a, b): # real signature unknown; restored from __doc__
    """ vector3_add(result:float, a:float, b:float) """
    pass

def vector3_copy(vector): # real signature unknown; restored from __doc__
    """ vector3_copy(vector:float) -> float """
    return 0.0

def vector3_cross_product(result, u, v): # real signature unknown; restored from __doc__
    """ vector3_cross_product(result:float, u:float, v:float) """
    pass

def vector3_distance(a, b): # real signature unknown; restored from __doc__
    """ vector3_distance(a:float, b:float) -> float """
    return 0.0

def vector3_divide_scalar(vector, scalar): # real signature unknown; restored from __doc__
    """ vector3_divide_scalar(vector:float, scalar:float) """
    pass

def vector3_dot_product(a, b): # real signature unknown; restored from __doc__
    """ vector3_dot_product(a:float, b:float) -> float """
    return 0.0

def vector3_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ vector3_equal(v1=None, v2=None) -> int """
    return 0

def vector3_equal_with_epsilon(vector0, vector1, epsilon): # real signature unknown; restored from __doc__
    """ vector3_equal_with_epsilon(vector0:float, vector1:float, epsilon:float) -> int """
    return 0

def vector3_free(vector): # real signature unknown; restored from __doc__
    """ vector3_free(vector:float) """
    pass

def vector3_init(vector, x, y, z): # real signature unknown; restored from __doc__
    """ vector3_init(vector:float, x:float, y:float, z:float) """
    pass

def vector3_init_zero(vector): # real signature unknown; restored from __doc__
    """ vector3_init_zero(vector:float) """
    pass

def vector3_invert(vector): # real signature unknown; restored from __doc__
    """ vector3_invert(vector:float) """
    pass

def vector3_magnitude(vector): # real signature unknown; restored from __doc__
    """ vector3_magnitude(vector:float) -> float """
    return 0.0

def vector3_multiply_scalar(vector, scalar): # real signature unknown; restored from __doc__
    """ vector3_multiply_scalar(vector:float, scalar:float) """
    pass

def vector3_normalize(vector): # real signature unknown; restored from __doc__
    """ vector3_normalize(vector:float) """
    pass

def vector3_subtract(result, a, b): # real signature unknown; restored from __doc__
    """ vector3_subtract(result:float, a:float, b:float) """
    pass

def wayland_display_set_compositor_display(display, wayland_display=None): # real signature unknown; restored from __doc__
    """ wayland_display_set_compositor_display(display:Cogl.Display, wayland_display=None) """
    pass

def wayland_onscreen_get_shell_surface(onscreen): # real signature unknown; restored from __doc__
    """ wayland_onscreen_get_shell_surface(onscreen:Cogl.Onscreen) """
    pass

def wayland_onscreen_get_surface(onscreen): # real signature unknown; restored from __doc__
    """ wayland_onscreen_get_surface(onscreen:Cogl.Onscreen) """
    pass

def wayland_onscreen_resize(onscreen, width, height, offset_x, offset_y): # real signature unknown; restored from __doc__
    """ wayland_onscreen_resize(onscreen:Cogl.Onscreen, width:int, height:int, offset_x:int, offset_y:int) """
    pass

def wayland_onscreen_set_foreign_surface(onscreen, surface=None): # real signature unknown; restored from __doc__
    """ wayland_onscreen_set_foreign_surface(onscreen:Cogl.Onscreen, surface=None) """
    pass

def wayland_renderer_get_display(renderer): # real signature unknown; restored from __doc__
    """ wayland_renderer_get_display(renderer:Cogl.Renderer) """
    pass

def wayland_renderer_set_event_dispatch_enabled(renderer, enable): # real signature unknown; restored from __doc__
    """ wayland_renderer_set_event_dispatch_enabled(renderer:Cogl.Renderer, enable:int) """
    pass

def wayland_renderer_set_foreign_display(renderer, display=None): # real signature unknown; restored from __doc__
    """ wayland_renderer_set_foreign_display(renderer:Cogl.Renderer, display=None) """
    pass

def wayland_texture_set_region_from_shm_buffer(texture, src_x, src_y, width, height, shm_buffer=None, dst_x, dst_y, level): # real signature unknown; restored from __doc__
    """ wayland_texture_set_region_from_shm_buffer(texture:Cogl.Texture, src_x:int, src_y:int, width:int, height:int, shm_buffer=None, dst_x:int, dst_y:int, level:int) -> int """
    return 0

def x11_onscreen_get_visual_xid(onscreen): # real signature unknown; restored from __doc__
    """ x11_onscreen_get_visual_xid(onscreen:Cogl.Onscreen) -> int """
    return 0

def x11_onscreen_get_window_xid(onscreen): # real signature unknown; restored from __doc__
    """ x11_onscreen_get_window_xid(onscreen:Cogl.Onscreen) -> int """
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

from .Object import Object
from .AtlasTexture import AtlasTexture
from .Attribute import Attribute
from .AttributeBuffer import AttributeBuffer
from .AttributeType import AttributeType
from .Bitmap import Bitmap
from .BitmapError import BitmapError
from .BlendStringError import BlendStringError
from .BufferAccess import BufferAccess
from .BufferBit import BufferBit
from .BufferError import BufferError
from .BufferMapHint import BufferMapHint
from .BufferTarget import BufferTarget
from .BufferUpdateHint import BufferUpdateHint
from .Color import Color
from .ColorMask import ColorMask
from .Context import Context
from .DebugObjectTypeInfo import DebugObjectTypeInfo
from .DepthState import DepthState
from .DepthTestFunction import DepthTestFunction
from .Display import Display
from .Driver import Driver
from .Euler import Euler
from .FeatureFlags import FeatureFlags
from .FeatureID import FeatureID
from .Fence import Fence
from .FenceClosure import FenceClosure
from .FilterReturn import FilterReturn
from .Fixed import Fixed
from .FogMode import FogMode
from .Framebuffer import Framebuffer
from .FramebufferError import FramebufferError
from .FrameClosure import FrameClosure
from .FrameEvent import FrameEvent
from .FrameInfo import FrameInfo
from .GLES2Context import GLES2Context
from .GLES2ContextError import GLES2ContextError
from .GLES2Vtable import GLES2Vtable
from .GtypeClass import GtypeClass
from .GtypeObject import GtypeObject
from .IndexBuffer import IndexBuffer
from .Indices import Indices
from .IndicesType import IndicesType
from .KmsCrtc import KmsCrtc
from .MaterialAlphaFunc import MaterialAlphaFunc
from .MaterialFilter import MaterialFilter
from .MaterialLayerType import MaterialLayerType
from .MaterialWrapMode import MaterialWrapMode
from .Matrix import Matrix
from .MatrixEntry import MatrixEntry
from .MatrixStack import MatrixStack
from .Onscreen import Onscreen
from .OnscreenDirtyClosure import OnscreenDirtyClosure
from .OnscreenDirtyInfo import OnscreenDirtyInfo
from .OnscreenResizeClosure import OnscreenResizeClosure
from .OnscreenTemplate import OnscreenTemplate
from .Output import Output
from .Pipeline import Pipeline
from .PipelineAlphaFunc import PipelineAlphaFunc
from .PipelineCullFaceMode import PipelineCullFaceMode
from .PipelineFilter import PipelineFilter
from .PipelineWrapMode import PipelineWrapMode
from .PixelBuffer import PixelBuffer
from .PixelFormat import PixelFormat
from .PollFD import PollFD
from .PollFDEvent import PollFDEvent
from .Primitive import Primitive
from .Quaternion import Quaternion
from .ReadPixelsFlags import ReadPixelsFlags
from .Renderer import Renderer
from .RendererConstraint import RendererConstraint
from .RendererError import RendererError
from .ShaderType import ShaderType
from .Snippet import Snippet
from .SnippetHook import SnippetHook
from .StereoMode import StereoMode
from .SubpixelOrder import SubpixelOrder
from .SubTexture import SubTexture
from .SwapChain import SwapChain
from .SystemError import SystemError
from .Texture import Texture
from .Texture2D import Texture2D
from .Texture2DSliced import Texture2DSliced
from .Texture3D import Texture3D
from .TextureComponents import TextureComponents
from .TextureError import TextureError
from .TextureFlags import TextureFlags
from .TexturePixmapX11 import TexturePixmapX11
from .TexturePixmapX11Error import TexturePixmapX11Error
from .TexturePixmapX11ReportLevel import TexturePixmapX11ReportLevel
from .TextureRectangle import TextureRectangle
from .TextureType import TextureType
from .TextureVertex import TextureVertex
from .UserDataKey import UserDataKey
from .VertexP2 import VertexP2
from .VertexP2C4 import VertexP2C4
from .VertexP2T2 import VertexP2T2
from .VertexP2T2C4 import VertexP2T2C4
from .VertexP3 import VertexP3
from .VertexP3C4 import VertexP3C4
from .VertexP3T2 import VertexP3T2
from .VertexP3T2C4 import VertexP3T2C4
from .VerticesMode import VerticesMode
from .Winding import Winding
from .WinsysFeature import WinsysFeature
from .WinsysID import WinsysID
from ._ColorSizeCheck import _ColorSizeCheck
from ._EulerSizeCheck import _EulerSizeCheck
from ._MatrixSizeCheck import _MatrixSizeCheck
from ._QuaternionSizeCheck import _QuaternionSizeCheck
from ._TextureVertexSizeCheck import _TextureVertexSizeCheck
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fba89e5ad00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Cogl-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Cogl', loader=<gi.importer.DynamicImporter object at 0x7fba89e5ad00>)"

