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

class Attribute(Object):
    """
    :Constructors:
    
    ::
    
        Attribute(**properties)
        new(attribute_buffer:Cogl.AttributeBuffer, name:str, stride:int, offset:int, components:int, type:Cogl.AttributeType) -> Cogl.Attribute
        new_const_1f(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute
        new_const_2f(context:Cogl.Context, name:str, component0:float, component1:float) -> Cogl.Attribute
        new_const_2fv(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute
        new_const_2x2fv(context:Cogl.Context, name:str, matrix2x2:float, transpose:int) -> Cogl.Attribute
        new_const_3f(context:Cogl.Context, name:str, component0:float, component1:float, component2:float) -> Cogl.Attribute
        new_const_3fv(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute
        new_const_3x3fv(context:Cogl.Context, name:str, matrix3x3:float, transpose:int) -> Cogl.Attribute
        new_const_4f(context:Cogl.Context, name:str, component0:float, component1:float, component2:float, component3:float) -> Cogl.Attribute
        new_const_4fv(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute
        new_const_4x4fv(context:Cogl.Context, name:str, matrix4x4:float, transpose:int) -> Cogl.Attribute
    """
    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> Cogl.AttributeBuffer """
        pass

    def get_normalized(self): # real signature unknown; restored from __doc__
        """ get_normalized(self) -> int """
        return 0

    def new(self, attribute_buffer, name, stride, offset, components, type): # real signature unknown; restored from __doc__
        """ new(attribute_buffer:Cogl.AttributeBuffer, name:str, stride:int, offset:int, components:int, type:Cogl.AttributeType) -> Cogl.Attribute """
        pass

    def new_const_1f(self, context, name, value): # real signature unknown; restored from __doc__
        """ new_const_1f(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute """
        pass

    def new_const_2f(self, context, name, component0, component1): # real signature unknown; restored from __doc__
        """ new_const_2f(context:Cogl.Context, name:str, component0:float, component1:float) -> Cogl.Attribute """
        pass

    def new_const_2fv(self, context, name, value): # real signature unknown; restored from __doc__
        """ new_const_2fv(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute """
        pass

    def new_const_2x2fv(self, context, name, matrix2x2, transpose): # real signature unknown; restored from __doc__
        """ new_const_2x2fv(context:Cogl.Context, name:str, matrix2x2:float, transpose:int) -> Cogl.Attribute """
        pass

    def new_const_3f(self, context, name, component0, component1, component2): # real signature unknown; restored from __doc__
        """ new_const_3f(context:Cogl.Context, name:str, component0:float, component1:float, component2:float) -> Cogl.Attribute """
        pass

    def new_const_3fv(self, context, name, value): # real signature unknown; restored from __doc__
        """ new_const_3fv(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute """
        pass

    def new_const_3x3fv(self, context, name, matrix3x3, transpose): # real signature unknown; restored from __doc__
        """ new_const_3x3fv(context:Cogl.Context, name:str, matrix3x3:float, transpose:int) -> Cogl.Attribute """
        pass

    def new_const_4f(self, context, name, component0, component1, component2, component3): # real signature unknown; restored from __doc__
        """ new_const_4f(context:Cogl.Context, name:str, component0:float, component1:float, component2:float, component3:float) -> Cogl.Attribute """
        pass

    def new_const_4fv(self, context, name, value): # real signature unknown; restored from __doc__
        """ new_const_4fv(context:Cogl.Context, name:str, value:float) -> Cogl.Attribute """
        pass

    def new_const_4x4fv(self, context, name, matrix4x4, transpose): # real signature unknown; restored from __doc__
        """ new_const_4x4fv(context:Cogl.Context, name:str, matrix4x4:float, transpose:int) -> Cogl.Attribute """
        pass

    def set_buffer(self, attribute_buffer): # real signature unknown; restored from __doc__
        """ set_buffer(self, attribute_buffer:Cogl.AttributeBuffer) """
        pass

    def set_normalized(self, normalized): # real signature unknown; restored from __doc__
        """ set_normalized(self, normalized:int) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Attribute), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglAttribute (93970931532176)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_const_1f': gi.FunctionInfo(new_const_1f), 'new_const_2f': gi.FunctionInfo(new_const_2f), 'new_const_2fv': gi.FunctionInfo(new_const_2fv), 'new_const_2x2fv': gi.FunctionInfo(new_const_2x2fv), 'new_const_3f': gi.FunctionInfo(new_const_3f), 'new_const_3fv': gi.FunctionInfo(new_const_3fv), 'new_const_3x3fv': gi.FunctionInfo(new_const_3x3fv), 'new_const_4f': gi.FunctionInfo(new_const_4f), 'new_const_4fv': gi.FunctionInfo(new_const_4fv), 'new_const_4x4fv': gi.FunctionInfo(new_const_4x4fv), 'get_buffer': gi.FunctionInfo(get_buffer), 'get_normalized': gi.FunctionInfo(get_normalized), 'set_buffer': gi.FunctionInfo(set_buffer), 'set_normalized': gi.FunctionInfo(set_normalized)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglAttribute (93970931532176)>'
    __info__ = ObjectInfo(Attribute)


