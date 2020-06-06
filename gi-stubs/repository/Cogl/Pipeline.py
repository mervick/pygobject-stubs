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


from .Object import Object

class Pipeline(Object):
    """
    :Constructors:
    
    ::
    
        Pipeline(**properties)
        new(context:Cogl.Context) -> Cogl.Pipeline
    """
    def add_layer_snippet(self, layer, snippet): # real signature unknown; restored from __doc__
        """ add_layer_snippet(self, layer:int, snippet:Cogl.Snippet) """
        pass

    def add_snippet(self, snippet): # real signature unknown; restored from __doc__
        """ add_snippet(self, snippet:Cogl.Snippet) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Cogl.Pipeline """
        pass

    def foreach_layer(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_layer(self, callback:Cogl.PipelineLayerCallback, user_data=None) """
        pass

    def get_alpha_test_function(self): # real signature unknown; restored from __doc__
        """ get_alpha_test_function(self) -> Cogl.PipelineAlphaFunc """
        pass

    def get_alpha_test_reference(self): # real signature unknown; restored from __doc__
        """ get_alpha_test_reference(self) -> float """
        return 0.0

    def get_ambient(self, ambient): # real signature unknown; restored from __doc__
        """ get_ambient(self, ambient:Cogl.Color) """
        pass

    def get_color(self): # real signature unknown; restored from __doc__
        """ get_color(self) -> color:Cogl.Color """
        pass

    def get_color_mask(self): # real signature unknown; restored from __doc__
        """ get_color_mask(self) -> Cogl.ColorMask """
        pass

    def get_cull_face_mode(self): # real signature unknown; restored from __doc__
        """ get_cull_face_mode(self) -> Cogl.PipelineCullFaceMode """
        pass

    def get_depth_state(self): # real signature unknown; restored from __doc__
        """ get_depth_state(self) -> state_out:Cogl.DepthState """
        pass

    def get_diffuse(self, diffuse): # real signature unknown; restored from __doc__
        """ get_diffuse(self, diffuse:Cogl.Color) """
        pass

    def get_emission(self, emission): # real signature unknown; restored from __doc__
        """ get_emission(self, emission:Cogl.Color) """
        pass

    def get_front_face_winding(self): # real signature unknown; restored from __doc__
        """ get_front_face_winding(self) -> Cogl.Winding """
        pass

    def get_layer_mag_filter(self, layer_index): # real signature unknown; restored from __doc__
        """ get_layer_mag_filter(self, layer_index:int) -> Cogl.PipelineFilter """
        pass

    def get_layer_min_filter(self, layer_index): # real signature unknown; restored from __doc__
        """ get_layer_min_filter(self, layer_index:int) -> Cogl.PipelineFilter """
        pass

    def get_layer_point_sprite_coords_enabled(self, layer_index): # real signature unknown; restored from __doc__
        """ get_layer_point_sprite_coords_enabled(self, layer_index:int) -> int """
        return 0

    def get_layer_texture(self, layer_index): # real signature unknown; restored from __doc__
        """ get_layer_texture(self, layer_index:int) -> Cogl.Texture """
        pass

    def get_layer_wrap_mode_p(self, layer_index): # real signature unknown; restored from __doc__
        """ get_layer_wrap_mode_p(self, layer_index:int) -> Cogl.PipelineWrapMode """
        pass

    def get_layer_wrap_mode_s(self, layer_index): # real signature unknown; restored from __doc__
        """ get_layer_wrap_mode_s(self, layer_index:int) -> Cogl.PipelineWrapMode """
        pass

    def get_layer_wrap_mode_t(self, layer_index): # real signature unknown; restored from __doc__
        """ get_layer_wrap_mode_t(self, layer_index:int) -> Cogl.PipelineWrapMode """
        pass

    def get_n_layers(self): # real signature unknown; restored from __doc__
        """ get_n_layers(self) -> int """
        return 0

    def get_per_vertex_point_size(self): # real signature unknown; restored from __doc__
        """ get_per_vertex_point_size(self) -> int """
        return 0

    def get_point_size(self): # real signature unknown; restored from __doc__
        """ get_point_size(self) -> float """
        return 0.0

    def get_shininess(self): # real signature unknown; restored from __doc__
        """ get_shininess(self) -> float """
        return 0.0

    def get_specular(self, specular): # real signature unknown; restored from __doc__
        """ get_specular(self, specular:Cogl.Color) """
        pass

    def get_uniform_location(self, uniform_name): # real signature unknown; restored from __doc__
        """ get_uniform_location(self, uniform_name:str) -> int """
        return 0

    def get_user_program(self): # real signature unknown; restored from __doc__
        """ get_user_program(self) """
        pass

    def new(self, context): # real signature unknown; restored from __doc__
        """ new(context:Cogl.Context) -> Cogl.Pipeline """
        pass

    def remove_layer(self, layer_index): # real signature unknown; restored from __doc__
        """ remove_layer(self, layer_index:int) """
        pass

    def set_alpha_test_function(self, alpha_func, alpha_reference): # real signature unknown; restored from __doc__
        """ set_alpha_test_function(self, alpha_func:Cogl.PipelineAlphaFunc, alpha_reference:float) """
        pass

    def set_ambient(self, ambient): # real signature unknown; restored from __doc__
        """ set_ambient(self, ambient:Cogl.Color) """
        pass

    def set_ambient_and_diffuse(self, color): # real signature unknown; restored from __doc__
        """ set_ambient_and_diffuse(self, color:Cogl.Color) """
        pass

    def set_blend(self, blend_string): # real signature unknown; restored from __doc__
        """ set_blend(self, blend_string:str) -> int """
        return 0

    def set_blend_constant(self, constant_color): # real signature unknown; restored from __doc__
        """ set_blend_constant(self, constant_color:Cogl.Color) """
        pass

    def set_color(self, color): # real signature unknown; restored from __doc__
        """ set_color(self, color:Cogl.Color) """
        pass

    def set_color4f(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ set_color4f(self, red:float, green:float, blue:float, alpha:float) """
        pass

    def set_color4ub(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ set_color4ub(self, red:int, green:int, blue:int, alpha:int) """
        pass

    def set_color_mask(self, color_mask): # real signature unknown; restored from __doc__
        """ set_color_mask(self, color_mask:Cogl.ColorMask) """
        pass

    def set_cull_face_mode(self, cull_face_mode): # real signature unknown; restored from __doc__
        """ set_cull_face_mode(self, cull_face_mode:Cogl.PipelineCullFaceMode) """
        pass

    def set_depth_state(self, state): # real signature unknown; restored from __doc__
        """ set_depth_state(self, state:Cogl.DepthState) -> int """
        return 0

    def set_diffuse(self, diffuse): # real signature unknown; restored from __doc__
        """ set_diffuse(self, diffuse:Cogl.Color) """
        pass

    def set_emission(self, emission): # real signature unknown; restored from __doc__
        """ set_emission(self, emission:Cogl.Color) """
        pass

    def set_front_face_winding(self, front_winding): # real signature unknown; restored from __doc__
        """ set_front_face_winding(self, front_winding:Cogl.Winding) """
        pass

    def set_layer_combine(self, layer_index, blend_string): # real signature unknown; restored from __doc__
        """ set_layer_combine(self, layer_index:int, blend_string:str) -> int """
        return 0

    def set_layer_combine_constant(self, layer_index, constant): # real signature unknown; restored from __doc__
        """ set_layer_combine_constant(self, layer_index:int, constant:Cogl.Color) """
        pass

    def set_layer_filters(self, layer_index, min_filter, mag_filter): # real signature unknown; restored from __doc__
        """ set_layer_filters(self, layer_index:int, min_filter:Cogl.PipelineFilter, mag_filter:Cogl.PipelineFilter) """
        pass

    def set_layer_matrix(self, layer_index, matrix): # real signature unknown; restored from __doc__
        """ set_layer_matrix(self, layer_index:int, matrix:Cogl.Matrix) """
        pass

    def set_layer_null_texture(self, layer_index, texture_type): # real signature unknown; restored from __doc__
        """ set_layer_null_texture(self, layer_index:int, texture_type:Cogl.TextureType) """
        pass

    def set_layer_point_sprite_coords_enabled(self, layer_index, enable): # real signature unknown; restored from __doc__
        """ set_layer_point_sprite_coords_enabled(self, layer_index:int, enable:int) -> int """
        return 0

    def set_layer_texture(self, layer_index, texture): # real signature unknown; restored from __doc__
        """ set_layer_texture(self, layer_index:int, texture:Cogl.Texture) """
        pass

    def set_layer_wrap_mode(self, layer_index, mode): # real signature unknown; restored from __doc__
        """ set_layer_wrap_mode(self, layer_index:int, mode:Cogl.PipelineWrapMode) """
        pass

    def set_layer_wrap_mode_p(self, layer_index, mode): # real signature unknown; restored from __doc__
        """ set_layer_wrap_mode_p(self, layer_index:int, mode:Cogl.PipelineWrapMode) """
        pass

    def set_layer_wrap_mode_s(self, layer_index, mode): # real signature unknown; restored from __doc__
        """ set_layer_wrap_mode_s(self, layer_index:int, mode:Cogl.PipelineWrapMode) """
        pass

    def set_layer_wrap_mode_t(self, layer_index, mode): # real signature unknown; restored from __doc__
        """ set_layer_wrap_mode_t(self, layer_index:int, mode:Cogl.PipelineWrapMode) """
        pass

    def set_per_vertex_point_size(self, enable): # real signature unknown; restored from __doc__
        """ set_per_vertex_point_size(self, enable:int) -> int """
        return 0

    def set_point_size(self, point_size): # real signature unknown; restored from __doc__
        """ set_point_size(self, point_size:float) """
        pass

    def set_shininess(self, shininess): # real signature unknown; restored from __doc__
        """ set_shininess(self, shininess:float) """
        pass

    def set_specular(self, specular): # real signature unknown; restored from __doc__
        """ set_specular(self, specular:Cogl.Color) """
        pass

    def set_uniform_1f(self, uniform_location, value): # real signature unknown; restored from __doc__
        """ set_uniform_1f(self, uniform_location:int, value:float) """
        pass

    def set_uniform_1i(self, uniform_location, value): # real signature unknown; restored from __doc__
        """ set_uniform_1i(self, uniform_location:int, value:int) """
        pass

    def set_uniform_float(self, uniform_location, n_components, count, value): # real signature unknown; restored from __doc__
        """ set_uniform_float(self, uniform_location:int, n_components:int, count:int, value:float) """
        pass

    def set_uniform_int(self, uniform_location, n_components, count, value): # real signature unknown; restored from __doc__
        """ set_uniform_int(self, uniform_location:int, n_components:int, count:int, value:int) """
        pass

    def set_uniform_matrix(self, uniform_location, dimensions, count, transpose, value): # real signature unknown; restored from __doc__
        """ set_uniform_matrix(self, uniform_location:int, dimensions:int, count:int, transpose:int, value:float) """
        pass

    def set_user_program(self, program): # real signature unknown; restored from __doc__
        """ set_user_program(self, program) """
        pass

    def value_get_object(self, value): # real signature unknown; restored from __doc__
        """ value_get_object(value:GObject.Value) """
        pass

    def value_set_object(self, value, p_object=None): # real signature unknown; restored from __doc__
        """ value_set_object(value:GObject.Value, object=None) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Pipeline), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglPipeline (93970932213280)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_layer_snippet': gi.FunctionInfo(add_layer_snippet), 'add_snippet': gi.FunctionInfo(add_snippet), 'copy': gi.FunctionInfo(copy), 'foreach_layer': gi.FunctionInfo(foreach_layer), 'get_alpha_test_function': gi.FunctionInfo(get_alpha_test_function), 'get_alpha_test_reference': gi.FunctionInfo(get_alpha_test_reference), 'get_ambient': gi.FunctionInfo(get_ambient), 'get_color': gi.FunctionInfo(get_color), 'get_color_mask': gi.FunctionInfo(get_color_mask), 'get_cull_face_mode': gi.FunctionInfo(get_cull_face_mode), 'get_depth_state': gi.FunctionInfo(get_depth_state), 'get_diffuse': gi.FunctionInfo(get_diffuse), 'get_emission': gi.FunctionInfo(get_emission), 'get_front_face_winding': gi.FunctionInfo(get_front_face_winding), 'get_layer_mag_filter': gi.FunctionInfo(get_layer_mag_filter), 'get_layer_min_filter': gi.FunctionInfo(get_layer_min_filter), 'get_layer_point_sprite_coords_enabled': gi.FunctionInfo(get_layer_point_sprite_coords_enabled), 'get_layer_texture': gi.FunctionInfo(get_layer_texture), 'get_layer_wrap_mode_p': gi.FunctionInfo(get_layer_wrap_mode_p), 'get_layer_wrap_mode_s': gi.FunctionInfo(get_layer_wrap_mode_s), 'get_layer_wrap_mode_t': gi.FunctionInfo(get_layer_wrap_mode_t), 'get_n_layers': gi.FunctionInfo(get_n_layers), 'get_per_vertex_point_size': gi.FunctionInfo(get_per_vertex_point_size), 'get_point_size': gi.FunctionInfo(get_point_size), 'get_shininess': gi.FunctionInfo(get_shininess), 'get_specular': gi.FunctionInfo(get_specular), 'get_uniform_location': gi.FunctionInfo(get_uniform_location), 'get_user_program': gi.FunctionInfo(get_user_program), 'remove_layer': gi.FunctionInfo(remove_layer), 'set_alpha_test_function': gi.FunctionInfo(set_alpha_test_function), 'set_ambient': gi.FunctionInfo(set_ambient), 'set_ambient_and_diffuse': gi.FunctionInfo(set_ambient_and_diffuse), 'set_blend': gi.FunctionInfo(set_blend), 'set_blend_constant': gi.FunctionInfo(set_blend_constant), 'set_color': gi.FunctionInfo(set_color), 'set_color4f': gi.FunctionInfo(set_color4f), 'set_color4ub': gi.FunctionInfo(set_color4ub), 'set_color_mask': gi.FunctionInfo(set_color_mask), 'set_cull_face_mode': gi.FunctionInfo(set_cull_face_mode), 'set_depth_state': gi.FunctionInfo(set_depth_state), 'set_diffuse': gi.FunctionInfo(set_diffuse), 'set_emission': gi.FunctionInfo(set_emission), 'set_front_face_winding': gi.FunctionInfo(set_front_face_winding), 'set_layer_combine': gi.FunctionInfo(set_layer_combine), 'set_layer_combine_constant': gi.FunctionInfo(set_layer_combine_constant), 'set_layer_filters': gi.FunctionInfo(set_layer_filters), 'set_layer_matrix': gi.FunctionInfo(set_layer_matrix), 'set_layer_null_texture': gi.FunctionInfo(set_layer_null_texture), 'set_layer_point_sprite_coords_enabled': gi.FunctionInfo(set_layer_point_sprite_coords_enabled), 'set_layer_texture': gi.FunctionInfo(set_layer_texture), 'set_layer_wrap_mode': gi.FunctionInfo(set_layer_wrap_mode), 'set_layer_wrap_mode_p': gi.FunctionInfo(set_layer_wrap_mode_p), 'set_layer_wrap_mode_s': gi.FunctionInfo(set_layer_wrap_mode_s), 'set_layer_wrap_mode_t': gi.FunctionInfo(set_layer_wrap_mode_t), 'set_per_vertex_point_size': gi.FunctionInfo(set_per_vertex_point_size), 'set_point_size': gi.FunctionInfo(set_point_size), 'set_shininess': gi.FunctionInfo(set_shininess), 'set_specular': gi.FunctionInfo(set_specular), 'set_uniform_1f': gi.FunctionInfo(set_uniform_1f), 'set_uniform_1i': gi.FunctionInfo(set_uniform_1i), 'set_uniform_float': gi.FunctionInfo(set_uniform_float), 'set_uniform_int': gi.FunctionInfo(set_uniform_int), 'set_uniform_matrix': gi.FunctionInfo(set_uniform_matrix), 'set_user_program': gi.FunctionInfo(set_user_program)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglPipeline (93970932213280)>'
    __info__ = ObjectInfo(Pipeline)


