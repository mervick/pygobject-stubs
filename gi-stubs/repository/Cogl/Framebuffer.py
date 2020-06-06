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


class Framebuffer(__gobject.GInterface):
    # no doc
    def allocate(self): # real signature unknown; restored from __doc__
        """ allocate(self) -> int """
        return 0

    def cancel_fence_callback(self, closure): # real signature unknown; restored from __doc__
        """ cancel_fence_callback(self, closure:Cogl.FenceClosure) """
        pass

    def clear(self, buffers, color): # real signature unknown; restored from __doc__
        """ clear(self, buffers:int, color:Cogl.Color) """
        pass

    def clear4f(self, buffers, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ clear4f(self, buffers:int, red:float, green:float, blue:float, alpha:float) """
        pass

    def discard_buffers(self, buffers): # real signature unknown; restored from __doc__
        """ discard_buffers(self, buffers:int) """
        pass

    def draw_attributes(self, pipeline, mode, first_vertex, n_vertices, attributes, n_attributes): # real signature unknown; restored from __doc__
        """ draw_attributes(self, pipeline:Cogl.Pipeline, mode:Cogl.VerticesMode, first_vertex:int, n_vertices:int, attributes:Cogl.Attribute, n_attributes:int) """
        pass

    def draw_indexed_attributes(self, pipeline, mode, first_vertex, n_vertices, indices, attributes, n_attributes): # real signature unknown; restored from __doc__
        """ draw_indexed_attributes(self, pipeline:Cogl.Pipeline, mode:Cogl.VerticesMode, first_vertex:int, n_vertices:int, indices:Cogl.Indices, attributes:Cogl.Attribute, n_attributes:int) """
        pass

    def draw_multitextured_rectangle(self, pipeline, x_1, y_1, x_2, y_2, tex_coords, tex_coords_len): # real signature unknown; restored from __doc__
        """ draw_multitextured_rectangle(self, pipeline:Cogl.Pipeline, x_1:float, y_1:float, x_2:float, y_2:float, tex_coords:list, tex_coords_len:int) """
        pass

    def draw_primitive(self, pipeline, primitive): # real signature unknown; restored from __doc__
        """ draw_primitive(self, pipeline:Cogl.Pipeline, primitive:Cogl.Primitive) """
        pass

    def draw_rectangle(self, pipeline, x_1, y_1, x_2, y_2): # real signature unknown; restored from __doc__
        """ draw_rectangle(self, pipeline:Cogl.Pipeline, x_1:float, y_1:float, x_2:float, y_2:float) """
        pass

    def draw_rectangles(self, pipeline, coordinates, n_rectangles): # real signature unknown; restored from __doc__
        """ draw_rectangles(self, pipeline:Cogl.Pipeline, coordinates:list, n_rectangles:int) """
        pass

    def draw_textured_rectangle(self, pipeline, x_1, y_1, x_2, y_2, s_1, t_1, s_2, t_2): # real signature unknown; restored from __doc__
        """ draw_textured_rectangle(self, pipeline:Cogl.Pipeline, x_1:float, y_1:float, x_2:float, y_2:float, s_1:float, t_1:float, s_2:float, t_2:float) """
        pass

    def draw_textured_rectangles(self, pipeline, coordinates, n_rectangles): # real signature unknown; restored from __doc__
        """ draw_textured_rectangles(self, pipeline:Cogl.Pipeline, coordinates:list, n_rectangles:int) """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def finish(self): # real signature unknown; restored from __doc__
        """ finish(self) """
        pass

    def frustum(self, left, right, bottom, top, z_near, z_far): # real signature unknown; restored from __doc__
        """ frustum(self, left:float, right:float, bottom:float, top:float, z_near:float, z_far:float) """
        pass

    def get_alpha_bits(self): # real signature unknown; restored from __doc__
        """ get_alpha_bits(self) -> int """
        return 0

    def get_blue_bits(self): # real signature unknown; restored from __doc__
        """ get_blue_bits(self) -> int """
        return 0

    def get_color_mask(self): # real signature unknown; restored from __doc__
        """ get_color_mask(self) -> Cogl.ColorMask """
        pass

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) -> Cogl.Context """
        pass

    def get_depth_bits(self): # real signature unknown; restored from __doc__
        """ get_depth_bits(self) -> int """
        return 0

    def get_depth_texture(self): # real signature unknown; restored from __doc__
        """ get_depth_texture(self) -> Cogl.Texture """
        pass

    def get_depth_texture_enabled(self): # real signature unknown; restored from __doc__
        """ get_depth_texture_enabled(self) -> int """
        return 0

    def get_depth_write_enabled(self): # real signature unknown; restored from __doc__
        """ get_depth_write_enabled(self) -> int """
        return 0

    def get_dither_enabled(self): # real signature unknown; restored from __doc__
        """ get_dither_enabled(self) -> int """
        return 0

    def get_green_bits(self): # real signature unknown; restored from __doc__
        """ get_green_bits(self) -> int """
        return 0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_is_stereo(self): # real signature unknown; restored from __doc__
        """ get_is_stereo(self) -> int """
        return 0

    def get_modelview_matrix(self): # real signature unknown; restored from __doc__
        """ get_modelview_matrix(self) -> matrix:Cogl.Matrix """
        pass

    def get_projection_matrix(self): # real signature unknown; restored from __doc__
        """ get_projection_matrix(self) -> matrix:Cogl.Matrix """
        pass

    def get_red_bits(self): # real signature unknown; restored from __doc__
        """ get_red_bits(self) -> int """
        return 0

    def get_samples_per_pixel(self): # real signature unknown; restored from __doc__
        """ get_samples_per_pixel(self) -> int """
        return 0

    def get_stereo_mode(self): # real signature unknown; restored from __doc__
        """ get_stereo_mode(self) -> Cogl.StereoMode """
        pass

    def get_viewport4fv(self): # real signature unknown; restored from __doc__
        """ get_viewport4fv(self) -> viewport:list """
        pass

    def get_viewport_height(self): # real signature unknown; restored from __doc__
        """ get_viewport_height(self) -> float """
        return 0.0

    def get_viewport_width(self): # real signature unknown; restored from __doc__
        """ get_viewport_width(self) -> float """
        return 0.0

    def get_viewport_x(self): # real signature unknown; restored from __doc__
        """ get_viewport_x(self) -> float """
        return 0.0

    def get_viewport_y(self): # real signature unknown; restored from __doc__
        """ get_viewport_y(self) -> float """
        return 0.0

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def identity_matrix(self): # real signature unknown; restored from __doc__
        """ identity_matrix(self) """
        pass

    def orthographic(self, x_1, y_1, x_2, y_2, near, far): # real signature unknown; restored from __doc__
        """ orthographic(self, x_1:float, y_1:float, x_2:float, y_2:float, near:float, far:float) """
        pass

    def perspective(self, fov_y, aspect, z_near, z_far): # real signature unknown; restored from __doc__
        """ perspective(self, fov_y:float, aspect:float, z_near:float, z_far:float) """
        pass

    def pop_clip(self): # real signature unknown; restored from __doc__
        """ pop_clip(self) """
        pass

    def pop_matrix(self): # real signature unknown; restored from __doc__
        """ pop_matrix(self) """
        pass

    def push_matrix(self): # real signature unknown; restored from __doc__
        """ push_matrix(self) """
        pass

    def push_primitive_clip(self, primitive, bounds_x1, bounds_y1, bounds_x2, bounds_y2): # real signature unknown; restored from __doc__
        """ push_primitive_clip(self, primitive:Cogl.Primitive, bounds_x1:float, bounds_y1:float, bounds_x2:float, bounds_y2:float) """
        pass

    def push_rectangle_clip(self, x_1, y_1, x_2, y_2): # real signature unknown; restored from __doc__
        """ push_rectangle_clip(self, x_1:float, y_1:float, x_2:float, y_2:float) """
        pass

    def push_scissor_clip(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ push_scissor_clip(self, x:int, y:int, width:int, height:int) """
        pass

    def read_pixels(self, x, y, width, height, format, pixels): # real signature unknown; restored from __doc__
        """ read_pixels(self, x:int, y:int, width:int, height:int, format:Cogl.PixelFormat, pixels:int) -> int """
        return 0

    def read_pixels_into_bitmap(self, x, y, source, bitmap): # real signature unknown; restored from __doc__
        """ read_pixels_into_bitmap(self, x:int, y:int, source:Cogl.ReadPixelsFlags, bitmap:Cogl.Bitmap) -> int """
        return 0

    def resolve_samples(self): # real signature unknown; restored from __doc__
        """ resolve_samples(self) """
        pass

    def resolve_samples_region(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ resolve_samples_region(self, x:int, y:int, width:int, height:int) """
        pass

    def rotate(self, angle, x, y, z): # real signature unknown; restored from __doc__
        """ rotate(self, angle:float, x:float, y:float, z:float) """
        pass

    def rotate_euler(self, euler): # real signature unknown; restored from __doc__
        """ rotate_euler(self, euler:Cogl.Euler) """
        pass

    def rotate_quaternion(self, quaternion): # real signature unknown; restored from __doc__
        """ rotate_quaternion(self, quaternion:Cogl.Quaternion) """
        pass

    def scale(self, x, y, z): # real signature unknown; restored from __doc__
        """ scale(self, x:float, y:float, z:float) """
        pass

    def set_color_mask(self, color_mask): # real signature unknown; restored from __doc__
        """ set_color_mask(self, color_mask:Cogl.ColorMask) """
        pass

    def set_depth_texture_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_depth_texture_enabled(self, enabled:int) """
        pass

    def set_depth_write_enabled(self, depth_write_enabled): # real signature unknown; restored from __doc__
        """ set_depth_write_enabled(self, depth_write_enabled:int) """
        pass

    def set_dither_enabled(self, dither_enabled): # real signature unknown; restored from __doc__
        """ set_dither_enabled(self, dither_enabled:int) """
        pass

    def set_modelview_matrix(self, matrix): # real signature unknown; restored from __doc__
        """ set_modelview_matrix(self, matrix:Cogl.Matrix) """
        pass

    def set_projection_matrix(self, matrix): # real signature unknown; restored from __doc__
        """ set_projection_matrix(self, matrix:Cogl.Matrix) """
        pass

    def set_samples_per_pixel(self, samples_per_pixel): # real signature unknown; restored from __doc__
        """ set_samples_per_pixel(self, samples_per_pixel:int) """
        pass

    def set_stereo_mode(self, stereo_mode): # real signature unknown; restored from __doc__
        """ set_stereo_mode(self, stereo_mode:Cogl.StereoMode) """
        pass

    def set_viewport(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ set_viewport(self, x:float, y:float, width:float, height:float) """
        pass

    def transform(self, matrix): # real signature unknown; restored from __doc__
        """ transform(self, matrix:Cogl.Matrix) """
        pass

    def translate(self, x, y, z): # real signature unknown; restored from __doc__
        """ translate(self, x:float, y:float, z:float) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Framebuffer), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglFramebuffer (93970932117728)>, '__dict__': <attribute '__dict__' of 'Framebuffer' objects>, '__weakref__': <attribute '__weakref__' of 'Framebuffer' objects>, '__doc__': None, '__gsignals__': {}, 'error_quark': gi.FunctionInfo(error_quark), 'allocate': gi.FunctionInfo(allocate), 'cancel_fence_callback': gi.FunctionInfo(cancel_fence_callback), 'clear': gi.FunctionInfo(clear), 'clear4f': gi.FunctionInfo(clear4f), 'discard_buffers': gi.FunctionInfo(discard_buffers), 'draw_attributes': gi.FunctionInfo(draw_attributes), 'draw_indexed_attributes': gi.FunctionInfo(draw_indexed_attributes), 'draw_multitextured_rectangle': gi.FunctionInfo(draw_multitextured_rectangle), 'draw_primitive': gi.FunctionInfo(draw_primitive), 'draw_rectangle': gi.FunctionInfo(draw_rectangle), 'draw_rectangles': gi.FunctionInfo(draw_rectangles), 'draw_textured_rectangle': gi.FunctionInfo(draw_textured_rectangle), 'draw_textured_rectangles': gi.FunctionInfo(draw_textured_rectangles), 'finish': gi.FunctionInfo(finish), 'frustum': gi.FunctionInfo(frustum), 'get_alpha_bits': gi.FunctionInfo(get_alpha_bits), 'get_blue_bits': gi.FunctionInfo(get_blue_bits), 'get_color_mask': gi.FunctionInfo(get_color_mask), 'get_context': gi.FunctionInfo(get_context), 'get_depth_bits': gi.FunctionInfo(get_depth_bits), 'get_depth_texture': gi.FunctionInfo(get_depth_texture), 'get_depth_texture_enabled': gi.FunctionInfo(get_depth_texture_enabled), 'get_depth_write_enabled': gi.FunctionInfo(get_depth_write_enabled), 'get_dither_enabled': gi.FunctionInfo(get_dither_enabled), 'get_green_bits': gi.FunctionInfo(get_green_bits), 'get_height': gi.FunctionInfo(get_height), 'get_is_stereo': gi.FunctionInfo(get_is_stereo), 'get_modelview_matrix': gi.FunctionInfo(get_modelview_matrix), 'get_projection_matrix': gi.FunctionInfo(get_projection_matrix), 'get_red_bits': gi.FunctionInfo(get_red_bits), 'get_samples_per_pixel': gi.FunctionInfo(get_samples_per_pixel), 'get_stereo_mode': gi.FunctionInfo(get_stereo_mode), 'get_viewport4fv': gi.FunctionInfo(get_viewport4fv), 'get_viewport_height': gi.FunctionInfo(get_viewport_height), 'get_viewport_width': gi.FunctionInfo(get_viewport_width), 'get_viewport_x': gi.FunctionInfo(get_viewport_x), 'get_viewport_y': gi.FunctionInfo(get_viewport_y), 'get_width': gi.FunctionInfo(get_width), 'identity_matrix': gi.FunctionInfo(identity_matrix), 'orthographic': gi.FunctionInfo(orthographic), 'perspective': gi.FunctionInfo(perspective), 'pop_clip': gi.FunctionInfo(pop_clip), 'pop_matrix': gi.FunctionInfo(pop_matrix), 'push_matrix': gi.FunctionInfo(push_matrix), 'push_primitive_clip': gi.FunctionInfo(push_primitive_clip), 'push_rectangle_clip': gi.FunctionInfo(push_rectangle_clip), 'push_scissor_clip': gi.FunctionInfo(push_scissor_clip), 'read_pixels': gi.FunctionInfo(read_pixels), 'read_pixels_into_bitmap': gi.FunctionInfo(read_pixels_into_bitmap), 'resolve_samples': gi.FunctionInfo(resolve_samples), 'resolve_samples_region': gi.FunctionInfo(resolve_samples_region), 'rotate': gi.FunctionInfo(rotate), 'rotate_euler': gi.FunctionInfo(rotate_euler), 'rotate_quaternion': gi.FunctionInfo(rotate_quaternion), 'scale': gi.FunctionInfo(scale), 'set_color_mask': gi.FunctionInfo(set_color_mask), 'set_depth_texture_enabled': gi.FunctionInfo(set_depth_texture_enabled), 'set_depth_write_enabled': gi.FunctionInfo(set_depth_write_enabled), 'set_dither_enabled': gi.FunctionInfo(set_dither_enabled), 'set_modelview_matrix': gi.FunctionInfo(set_modelview_matrix), 'set_projection_matrix': gi.FunctionInfo(set_projection_matrix), 'set_samples_per_pixel': gi.FunctionInfo(set_samples_per_pixel), 'set_stereo_mode': gi.FunctionInfo(set_stereo_mode), 'set_viewport': gi.FunctionInfo(set_viewport), 'transform': gi.FunctionInfo(transform), 'translate': gi.FunctionInfo(translate)})"
    __gdoc__ = 'Interface CoglFramebuffer\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglFramebuffer (93970932117728)>'
    __info__ = InterfaceInfo(Framebuffer)


