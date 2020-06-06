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

class Primitive(Object):
    """
    :Constructors:
    
    ::
    
        Primitive(**properties)
        new_p2(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_p2c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_p2t2(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_p2t2c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_p3(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_p3c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_p3t2(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_p3t2c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive
        new_with_attributes(mode:Cogl.VerticesMode, n_vertices:int, attributes:Cogl.Attribute, n_attributes:int) -> Cogl.Primitive
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Cogl.Primitive """
        pass

    def draw(self, framebuffer, pipeline): # real signature unknown; restored from __doc__
        """ draw(self, framebuffer:Cogl.Framebuffer, pipeline:Cogl.Pipeline) """
        pass

    def foreach_attribute(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_attribute(self, callback:Cogl.PrimitiveAttributeCallback, user_data=None) """
        pass

    def get_first_vertex(self): # real signature unknown; restored from __doc__
        """ get_first_vertex(self) -> int """
        return 0

    def get_indices(self): # real signature unknown; restored from __doc__
        """ get_indices(self) -> Cogl.Indices """
        pass

    def get_mode(self): # real signature unknown; restored from __doc__
        """ get_mode(self) -> Cogl.VerticesMode """
        pass

    def get_n_vertices(self): # real signature unknown; restored from __doc__
        """ get_n_vertices(self) -> int """
        return 0

    def new_p2(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p2(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_p2c4(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p2c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_p2t2(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p2t2(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_p2t2c4(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p2t2c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_p3(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p3(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_p3c4(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p3c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_p3t2(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p3t2(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_p3t2c4(self, context, mode, data): # real signature unknown; restored from __doc__
        """ new_p3t2c4(context:Cogl.Context, mode:Cogl.VerticesMode, data:list) -> Cogl.Primitive """
        pass

    def new_with_attributes(self, mode, n_vertices, attributes, n_attributes): # real signature unknown; restored from __doc__
        """ new_with_attributes(mode:Cogl.VerticesMode, n_vertices:int, attributes:Cogl.Attribute, n_attributes:int) -> Cogl.Primitive """
        pass

    def set_attributes(self, attributes, n_attributes): # real signature unknown; restored from __doc__
        """ set_attributes(self, attributes:Cogl.Attribute, n_attributes:int) """
        pass

    def set_first_vertex(self, first_vertex): # real signature unknown; restored from __doc__
        """ set_first_vertex(self, first_vertex:int) """
        pass

    def set_indices(self, indices, n_indices): # real signature unknown; restored from __doc__
        """ set_indices(self, indices:Cogl.Indices, n_indices:int) """
        pass

    def set_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_mode(self, mode:Cogl.VerticesMode) """
        pass

    def set_n_vertices(self, n_vertices): # real signature unknown; restored from __doc__
        """ set_n_vertices(self, n_vertices:int) """
        pass

    def texture_set_auto_mipmap(self, primitive_texture, value): # real signature unknown; restored from __doc__
        """ texture_set_auto_mipmap(primitive_texture, value:int) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Primitive), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglPrimitive (93970932249520)>, '__doc__': None, '__gsignals__': {}, 'new_p2': gi.FunctionInfo(new_p2), 'new_p2c4': gi.FunctionInfo(new_p2c4), 'new_p2t2': gi.FunctionInfo(new_p2t2), 'new_p2t2c4': gi.FunctionInfo(new_p2t2c4), 'new_p3': gi.FunctionInfo(new_p3), 'new_p3c4': gi.FunctionInfo(new_p3c4), 'new_p3t2': gi.FunctionInfo(new_p3t2), 'new_p3t2c4': gi.FunctionInfo(new_p3t2c4), 'new_with_attributes': gi.FunctionInfo(new_with_attributes), 'texture_set_auto_mipmap': gi.FunctionInfo(texture_set_auto_mipmap), 'copy': gi.FunctionInfo(copy), 'draw': gi.FunctionInfo(draw), 'foreach_attribute': gi.FunctionInfo(foreach_attribute), 'get_first_vertex': gi.FunctionInfo(get_first_vertex), 'get_indices': gi.FunctionInfo(get_indices), 'get_mode': gi.FunctionInfo(get_mode), 'get_n_vertices': gi.FunctionInfo(get_n_vertices), 'set_attributes': gi.FunctionInfo(set_attributes), 'set_first_vertex': gi.FunctionInfo(set_first_vertex), 'set_indices': gi.FunctionInfo(set_indices), 'set_mode': gi.FunctionInfo(set_mode), 'set_n_vertices': gi.FunctionInfo(set_n_vertices)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglPrimitive (93970932249520)>'
    __info__ = ObjectInfo(Primitive)


