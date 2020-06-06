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

class AtlasTexture(Object):
    """
    :Constructors:
    
    ::
    
        AtlasTexture(**properties)
        new_from_bitmap(bmp:Cogl.Bitmap) -> Cogl.AtlasTexture
        new_from_data(ctx:Cogl.Context, width:int, height:int, format:Cogl.PixelFormat, rowstride:int, data:int) -> Cogl.AtlasTexture
        new_from_file(ctx:Cogl.Context, filename:str) -> Cogl.AtlasTexture
        new_with_size(ctx:Cogl.Context, width:int, height:int) -> Cogl.AtlasTexture
    """
    def new_from_bitmap(self, bmp): # real signature unknown; restored from __doc__
        """ new_from_bitmap(bmp:Cogl.Bitmap) -> Cogl.AtlasTexture """
        pass

    def new_from_data(self, ctx, width, height, format, rowstride, data): # real signature unknown; restored from __doc__
        """ new_from_data(ctx:Cogl.Context, width:int, height:int, format:Cogl.PixelFormat, rowstride:int, data:int) -> Cogl.AtlasTexture """
        pass

    def new_from_file(self, ctx, filename): # real signature unknown; restored from __doc__
        """ new_from_file(ctx:Cogl.Context, filename:str) -> Cogl.AtlasTexture """
        pass

    def new_with_size(self, ctx, width, height): # real signature unknown; restored from __doc__
        """ new_with_size(ctx:Cogl.Context, width:int, height:int) -> Cogl.AtlasTexture """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(AtlasTexture), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglAtlasTexture (93970931785856)>, '__doc__': None, '__gsignals__': {}, 'new_from_bitmap': gi.FunctionInfo(new_from_bitmap), 'new_from_data': gi.FunctionInfo(new_from_data), 'new_from_file': gi.FunctionInfo(new_from_file), 'new_with_size': gi.FunctionInfo(new_with_size)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglAtlasTexture (93970931785856)>'
    __info__ = ObjectInfo(AtlasTexture)


