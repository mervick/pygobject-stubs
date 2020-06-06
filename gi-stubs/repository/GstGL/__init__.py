# encoding: utf-8
# module gi.repository.GstGL
# from /usr/lib64/girepository-1.0/GstGL-1.0.typelib
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
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


# Variables with simple values

BUFFER_POOL_OPTION_GL_SYNC_META = 'GstBufferPoolOptionGLSyncMeta'

BUFFER_POOL_OPTION_GL_TEXTURE_TARGET_2D = 'GstBufferPoolOptionGLTextureTarget2D'

BUFFER_POOL_OPTION_GL_TEXTURE_TARGET_EXTERNAL_OES = 'GstBufferPoolOptionGLTextureTargetExternalOES'

BUFFER_POOL_OPTION_GL_TEXTURE_TARGET_RECTANGLE = 'GstBufferPoolOptionGLTextureTargetRectangle'

CAPS_FEATURE_MEMORY_GL_BUFFER = 'memory:GLBuffer'
CAPS_FEATURE_MEMORY_GL_MEMORY = 'memory:GLMemory'

GL_ALLOCATION_PARAMS_ALLOC_FLAG_ALLOC = 1
GL_ALLOCATION_PARAMS_ALLOC_FLAG_BUFFER = 16
GL_ALLOCATION_PARAMS_ALLOC_FLAG_USER = 65536
GL_ALLOCATION_PARAMS_ALLOC_FLAG_VIDEO = 8

GL_ALLOCATION_PARAMS_ALLOC_FLAG_WRAP_GPU_HANDLE = 4

GL_ALLOCATION_PARAMS_ALLOC_FLAG_WRAP_SYSMEM = 2

GL_API_GLES1_NAME = 'gles1'

GL_API_GLES2_NAME = 'gles2'

GL_API_OPENGL3_NAME = 'opengl3'

GL_API_OPENGL_NAME = 'opengl'

GL_BASE_MEMORY_ALLOCATOR_NAME = 'GLBaseMemory'

GL_BUFFER_ALLOCATOR_NAME = 'GLBuffer'

GL_COLOR_CONVERT_FORMATS = '{ RGBA, RGB, RGBx, BGR, BGRx, BGRA, xRGB, xBGR, ARGB, ABGR, Y444, I420, YV12, Y42B, Y41B, NV12, NV21, YUY2, UYVY, AYUV, VUYA, GRAY8, GRAY16_LE, GRAY16_BE, RGB16, BGR16, ARGB64 }'

GL_COLOR_CONVERT_VIDEO_CAPS = 'video/x-raw('

GL_CONTEXT_TYPE_CGL = 'gst.gl.context.CGL'
GL_CONTEXT_TYPE_EAGL = 'gst.gl.context.EAGL'
GL_CONTEXT_TYPE_EGL = 'gst.gl.context.EGL'
GL_CONTEXT_TYPE_GLX = 'gst.gl.context.GLX'
GL_CONTEXT_TYPE_WGL = 'gst.gl.context.WGL'

GL_DISPLAY_CONTEXT_TYPE = 'gst.gl.GLDisplay'

GL_DISPLAY_EGL_NAME = 'gst.gl.display.egl'

GL_MEMORY_ALLOCATOR_NAME = 'GLMemory'

GL_MEMORY_PBO_ALLOCATOR_NAME = 'GLMemoryPBO'

GL_MEMORY_VIDEO_FORMATS_STR = '{ RGBA, BGRA, RGBx, BGRx, ARGB, ABGR, xRGB, xBGR, RGB, BGR, RGB16, BGR16, AYUV, VUYA, I420, YV12, NV12, NV21, YUY2, UYVY, Y41B, Y42B, Y444, GRAY8, GRAY16_LE, GRAY16_BE, ARGB64 }'

GL_RENDERBUFFER_ALLOCATOR_NAME = 'GLRenderbuffer'

GL_TEXTURE_TARGET_2D_STR = '2D'

GL_TEXTURE_TARGET_EXTERNAL_OES_STR = 'external-oes'

GL_TEXTURE_TARGET_RECTANGLE_STR = 'rectangle'

MAP_GL = 131072

_namespace = 'GstGL'

_version = '1.0'

__weakref__ = None

# functions

def buffer_add_gl_sync_meta(context, buffer): # real signature unknown; restored from __doc__
    """ buffer_add_gl_sync_meta(context:GstGL.GLContext, buffer:Gst.Buffer) -> GstGL.GLSyncMeta """
    pass

def buffer_add_gl_sync_meta_full(context, buffer, data=None): # real signature unknown; restored from __doc__
    """ buffer_add_gl_sync_meta_full(context:GstGL.GLContext, buffer:Gst.Buffer, data=None) -> GstGL.GLSyncMeta """
    pass

def buffer_pool_config_get_gl_allocation_params(config): # real signature unknown; restored from __doc__
    """ buffer_pool_config_get_gl_allocation_params(config:Gst.Structure) -> GstGL.GLAllocationParams """
    pass

def buffer_pool_config_set_gl_allocation_params(config, params): # real signature unknown; restored from __doc__
    """ buffer_pool_config_set_gl_allocation_params(config:Gst.Structure, params:GstGL.GLAllocationParams) """
    pass

def context_get_gl_display(context): # real signature unknown; restored from __doc__
    """ context_get_gl_display(context:Gst.Context) -> bool, display:GstGL.GLDisplay """
    return False

def context_set_gl_display(context, display): # real signature unknown; restored from __doc__
    """ context_set_gl_display(context:Gst.Context, display:GstGL.GLDisplay) """
    pass

def glsl_error_quark(): # real signature unknown; restored from __doc__
    """ glsl_error_quark() -> int """
    return 0

def glsl_profile_from_string(string): # real signature unknown; restored from __doc__
    """ glsl_profile_from_string(string:str) -> GstGL.GLSLProfile """
    pass

def glsl_profile_to_string(profile): # real signature unknown; restored from __doc__
    """ glsl_profile_to_string(profile:GstGL.GLSLProfile) -> str or None """
    return ""

def glsl_string_get_version_profile(s): # real signature unknown; restored from __doc__
    """ glsl_string_get_version_profile(s:str) -> bool, version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile """
    return False

def glsl_version_from_string(string): # real signature unknown; restored from __doc__
    """ glsl_version_from_string(string:str) -> GstGL.GLSLVersion """
    pass

def glsl_version_profile_from_string(string): # real signature unknown; restored from __doc__
    """ glsl_version_profile_from_string(string:str) -> bool, version_ret:GstGL.GLSLVersion, profile_ret:GstGL.GLSLProfile """
    return False

def glsl_version_profile_to_string(version, profile): # real signature unknown; restored from __doc__
    """ glsl_version_profile_to_string(version:GstGL.GLSLVersion, profile:GstGL.GLSLProfile) -> str """
    return ""

def glsl_version_to_string(version): # real signature unknown; restored from __doc__
    """ glsl_version_to_string(version:GstGL.GLSLVersion) -> str or None """
    return ""

def gl_api_from_string(api_s): # real signature unknown; restored from __doc__
    """ gl_api_from_string(api_s:str) -> GstGL.GLAPI """
    pass

def gl_api_to_string(api): # real signature unknown; restored from __doc__
    """ gl_api_to_string(api:GstGL.GLAPI) -> str """
    return ""

def gl_base_memory_alloc(allocator, params): # real signature unknown; restored from __doc__
    """ gl_base_memory_alloc(allocator:GstGL.GLBaseMemoryAllocator, params:GstGL.GLAllocationParams) -> GstGL.GLBaseMemory """
    pass

def gl_base_memory_error_quark(): # real signature unknown; restored from __doc__
    """ gl_base_memory_error_quark() -> int """
    return 0

def gl_base_memory_init_once(): # real signature unknown; restored from __doc__
    """ gl_base_memory_init_once() """
    pass

def gl_buffer_init_once(): # real signature unknown; restored from __doc__
    """ gl_buffer_init_once() """
    pass

def gl_check_extension(name, ext): # real signature unknown; restored from __doc__
    """ gl_check_extension(name:str, ext:str) -> bool """
    return False

def gl_context_error_quark(): # real signature unknown; restored from __doc__
    """ gl_context_error_quark() -> int """
    return 0

def gl_element_propagate_display_context(element, display): # real signature unknown; restored from __doc__
    """ gl_element_propagate_display_context(element:Gst.Element, display:GstGL.GLDisplay) """
    pass

def gl_ensure_element_data(element=None, display_ptr, other_context_ptr): # real signature unknown; restored from __doc__
    """ gl_ensure_element_data(element=None, display_ptr:GstGL.GLDisplay, other_context_ptr:GstGL.GLContext) -> bool, display_ptr:GstGL.GLDisplay, other_context_ptr:GstGL.GLContext """
    return False

def gl_format_from_video_info(context, vinfo, plane): # real signature unknown; restored from __doc__
    """ gl_format_from_video_info(context:GstGL.GLContext, vinfo:GstVideo.VideoInfo, plane:int) -> GstGL.GLFormat """
    pass

def gl_format_is_supported(context, format): # real signature unknown; restored from __doc__
    """ gl_format_is_supported(context:GstGL.GLContext, format:GstGL.GLFormat) -> bool """
    return False

def gl_format_type_from_sized_gl_format(format): # real signature unknown; restored from __doc__
    """ gl_format_type_from_sized_gl_format(format:GstGL.GLFormat) -> unsized_format:GstGL.GLFormat, gl_type:int """
    pass

def gl_format_type_n_bytes(format, type): # real signature unknown; restored from __doc__
    """ gl_format_type_n_bytes(format:int, type:int) -> int """
    return 0

def gl_get_plane_data_size(info, align, plane): # real signature unknown; restored from __doc__
    """ gl_get_plane_data_size(info:GstVideo.VideoInfo, align:GstVideo.VideoAlignment, plane:int) -> int """
    return 0

def gl_get_plane_start(info, valign, plane): # real signature unknown; restored from __doc__
    """ gl_get_plane_start(info:GstVideo.VideoInfo, valign:GstVideo.VideoAlignment, plane:int) -> int """
    return 0

def gl_handle_context_query(element, query, display=None, context=None, other_context=None): # real signature unknown; restored from __doc__
    """ gl_handle_context_query(element:Gst.Element, query:Gst.Query, display:GstGL.GLDisplay=None, context:GstGL.GLContext=None, other_context:GstGL.GLContext=None) -> bool """
    return False

def gl_handle_set_context(element, context, display, other_context): # real signature unknown; restored from __doc__
    """ gl_handle_set_context(element:Gst.Element, context:Gst.Context, display:GstGL.GLDisplay, other_context:GstGL.GLContext) -> bool, display:GstGL.GLDisplay, other_context:GstGL.GLContext """
    return False

def gl_memory_init_once(): # real signature unknown; restored from __doc__
    """ gl_memory_init_once() """
    pass

def gl_memory_pbo_init_once(): # real signature unknown; restored from __doc__
    """ gl_memory_pbo_init_once() """
    pass

def gl_platform_from_string(platform_s): # real signature unknown; restored from __doc__
    """ gl_platform_from_string(platform_s:str) -> GstGL.GLPlatform """
    pass

def gl_platform_to_string(platform): # real signature unknown; restored from __doc__
    """ gl_platform_to_string(platform:GstGL.GLPlatform) -> str """
    return ""

def gl_query_local_gl_context(element, direction, context_ptr): # real signature unknown; restored from __doc__
    """ gl_query_local_gl_context(element:Gst.Element, direction:Gst.PadDirection, context_ptr:GstGL.GLContext) -> bool, context_ptr:GstGL.GLContext """
    return False

def gl_renderbuffer_init_once(): # real signature unknown; restored from __doc__
    """ gl_renderbuffer_init_once() """
    pass

def gl_sized_gl_format_from_gl_format_type(context, format, type): # real signature unknown; restored from __doc__
    """ gl_sized_gl_format_from_gl_format_type(context:GstGL.GLContext, format:int, type:int) -> int """
    return 0

def gl_stereo_downmix_mode_get_type(): # real signature unknown; restored from __doc__
    """ gl_stereo_downmix_mode_get_type() -> GType """
    pass

def gl_sync_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ gl_sync_meta_api_get_type() -> GType """
    pass

def gl_sync_meta_get_info(): # real signature unknown; restored from __doc__
    """ gl_sync_meta_get_info() -> Gst.MetaInfo """
    pass

def gl_texture_target_from_gl(target): # real signature unknown; restored from __doc__
    """ gl_texture_target_from_gl(target:int) -> GstGL.GLTextureTarget """
    pass

def gl_texture_target_from_string(p_str): # real signature unknown; restored from __doc__
    """ gl_texture_target_from_string(str:str) -> GstGL.GLTextureTarget """
    pass

def gl_texture_target_to_buffer_pool_option(target): # real signature unknown; restored from __doc__
    """ gl_texture_target_to_buffer_pool_option(target:GstGL.GLTextureTarget) -> str """
    return ""

def gl_texture_target_to_gl(target): # real signature unknown; restored from __doc__
    """ gl_texture_target_to_gl(target:GstGL.GLTextureTarget) -> int """
    return 0

def gl_texture_target_to_string(target): # real signature unknown; restored from __doc__
    """ gl_texture_target_to_string(target:GstGL.GLTextureTarget) -> str """
    return ""

def gl_value_get_texture_target_mask(value): # real signature unknown; restored from __doc__
    """ gl_value_get_texture_target_mask(value:GObject.Value) -> GstGL.GLTextureTarget """
    pass

def gl_value_set_texture_target(value, target): # real signature unknown; restored from __doc__
    """ gl_value_set_texture_target(value:GObject.Value, target:GstGL.GLTextureTarget) -> bool """
    return False

def gl_value_set_texture_target_from_mask(value, target_mask): # real signature unknown; restored from __doc__
    """ gl_value_set_texture_target_from_mask(value:GObject.Value, target_mask:GstGL.GLTextureTarget) -> bool """
    return False

def gl_version_to_glsl_version(gl_api, maj, min): # real signature unknown; restored from __doc__
    """ gl_version_to_glsl_version(gl_api:GstGL.GLAPI, maj:int, min:int) -> GstGL.GLSLVersion """
    pass

def gl_window_error_quark(): # real signature unknown; restored from __doc__
    """ gl_window_error_quark() -> int """
    return 0

def is_gl_base_memory(mem): # real signature unknown; restored from __doc__
    """ is_gl_base_memory(mem:Gst.Memory) -> bool """
    return False

def is_gl_buffer(mem): # real signature unknown; restored from __doc__
    """ is_gl_buffer(mem:Gst.Memory) -> bool """
    return False

def is_gl_memory(mem): # real signature unknown; restored from __doc__
    """ is_gl_memory(mem:Gst.Memory) -> bool """
    return False

def is_gl_memory_pbo(mem): # real signature unknown; restored from __doc__
    """ is_gl_memory_pbo(mem:Gst.Memory) -> bool """
    return False

def is_gl_renderbuffer(mem): # real signature unknown; restored from __doc__
    """ is_gl_renderbuffer(mem:Gst.Memory) -> bool """
    return False

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

from .GLAllocationParams import GLAllocationParams
from .GLAPI import GLAPI
from .GLAsyncDebug import GLAsyncDebug
from .GLBaseFilter import GLBaseFilter
from .GLBaseFilterClass import GLBaseFilterClass
from .GLBaseFilterPrivate import GLBaseFilterPrivate
from .GLBaseMemory import GLBaseMemory
from .GLBaseMemoryAllocator import GLBaseMemoryAllocator
from .GLBaseMemoryAllocatorClass import GLBaseMemoryAllocatorClass
from .GLBaseMemoryError import GLBaseMemoryError
from .GLBaseMemoryTransfer import GLBaseMemoryTransfer
from .GLBuffer import GLBuffer
from .GLBufferAllocationParams import GLBufferAllocationParams
from .GLBufferAllocator import GLBufferAllocator
from .GLBufferAllocatorClass import GLBufferAllocatorClass
from .GLBufferPool import GLBufferPool
from .GLBufferPoolClass import GLBufferPoolClass
from .GLBufferPoolPrivate import GLBufferPoolPrivate
from .GLColorConvert import GLColorConvert
from .GLColorConvertClass import GLColorConvertClass
from .GLColorConvertPrivate import GLColorConvertPrivate
from .GLContext import GLContext
from .GLContextClass import GLContextClass
from .GLContextError import GLContextError
from .GLContextPrivate import GLContextPrivate
from .GLDisplay import GLDisplay
from .GLDisplayClass import GLDisplayClass
from .GLDisplayEGL import GLDisplayEGL
from .GLDisplayEGLClass import GLDisplayEGLClass
from .GLDisplayPrivate import GLDisplayPrivate
from .GLDisplayType import GLDisplayType
from .GLDisplayWayland import GLDisplayWayland
from .GLDisplayWaylandClass import GLDisplayWaylandClass
from .GLDisplayX11 import GLDisplayX11
from .GLDisplayX11Class import GLDisplayX11Class
from .GLFilter import GLFilter
from .GLFilterClass import GLFilterClass
from .GLFormat import GLFormat
from .GLFramebuffer import GLFramebuffer
from .GLFramebufferClass import GLFramebufferClass
from .GLFramebufferPrivate import GLFramebufferPrivate
from .GLFuncs import GLFuncs
from .GLMemory import GLMemory
from .GLMemoryAllocator import GLMemoryAllocator
from .GLMemoryAllocatorClass import GLMemoryAllocatorClass
from .GLMemoryEGL import GLMemoryEGL
from .GLMemoryEGLAllocator import GLMemoryEGLAllocator
from .GLMemoryEGLAllocatorClass import GLMemoryEGLAllocatorClass
from .GLMemoryPBO import GLMemoryPBO
from .GLMemoryPBOAllocator import GLMemoryPBOAllocator
from .GLMemoryPBOAllocatorClass import GLMemoryPBOAllocatorClass
from .GLOverlayCompositor import GLOverlayCompositor
from .GLOverlayCompositorClass import GLOverlayCompositorClass
from .GLPlatform import GLPlatform
from .GLQuery import GLQuery
from .GLQueryType import GLQueryType
from .GLRenderbuffer import GLRenderbuffer
from .GLRenderbufferAllocationParams import GLRenderbufferAllocationParams
from .GLRenderbufferAllocator import GLRenderbufferAllocator
from .GLRenderbufferAllocatorClass import GLRenderbufferAllocatorClass
from .GLShader import GLShader
from .GLShaderClass import GLShaderClass
from .GLShaderPrivate import GLShaderPrivate
from .GLSLError import GLSLError
from .GLSLProfile import GLSLProfile
from .GLSLStage import GLSLStage
from .GLSLStageClass import GLSLStageClass
from .GLSLStagePrivate import GLSLStagePrivate
from .GLSLVersion import GLSLVersion
from .GLStereoDownmix import GLStereoDownmix
from .GLSyncMeta import GLSyncMeta
from .GLTextureTarget import GLTextureTarget
from .GLUpload import GLUpload
from .GLUploadClass import GLUploadClass
from .GLUploadPrivate import GLUploadPrivate
from .GLUploadReturn import GLUploadReturn
from .GLVideoAllocationParams import GLVideoAllocationParams
from .GLViewConvert import GLViewConvert
from .GLViewConvertClass import GLViewConvertClass
from .GLViewConvertPrivate import GLViewConvertPrivate
from .GLWindow import GLWindow
from .GLWindowClass import GLWindowClass
from .GLWindowError import GLWindowError
from .GLWindowPrivate import GLWindowPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f56a4e63d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstGL-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstGL', loader=<gi.importer.DynamicImporter object at 0x7f56a4e63d00>)"

