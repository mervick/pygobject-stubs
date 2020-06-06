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

from .Texture import Texture

class TextureRectangle(Object, Texture):
    """
    :Constructors:
    
    ::
    
        TextureRectangle(**properties)
        new_from_bitmap(bitmap:Cogl.Bitmap) -> Cogl.TextureRectangle
        new_from_foreign(ctx:Cogl.Context, gl_handle:int, width:int, height:int, format:Cogl.PixelFormat) -> Cogl.TextureRectangle
        new_with_size(ctx:Cogl.Context, width:int, height:int) -> Cogl.TextureRectangle
    """
    def allocate(self): # real signature unknown; restored from __doc__
        """ allocate(self) -> int """
        return 0

    def copy_sub_image(self, xoffset, yoffset, x, y, width, height): # real signature unknown; restored from __doc__
        """ copy_sub_image(self, xoffset:int, yoffset:int, x:int, y:int, width:int, height:int) -> int """
        return 0

    def get_components(self): # real signature unknown; restored from __doc__
        """ get_components(self) -> Cogl.TextureComponents """
        pass

    def get_data(self, format, rowstride, data): # real signature unknown; restored from __doc__
        """ get_data(self, format:Cogl.PixelFormat, rowstride:int, data:int) -> int """
        return 0

    def get_gl_texture(self): # real signature unknown; restored from __doc__
        """ get_gl_texture(self) -> int, out_gl_handle:int, out_gl_target:int """
        return 0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_max_waste(self): # real signature unknown; restored from __doc__
        """ get_max_waste(self) -> int """
        return 0

    def get_premultiplied(self): # real signature unknown; restored from __doc__
        """ get_premultiplied(self) -> int """
        return 0

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def is_sliced(self): # real signature unknown; restored from __doc__
        """ is_sliced(self) -> int """
        return 0

    def new_from_bitmap(self, bitmap): # real signature unknown; restored from __doc__
        """ new_from_bitmap(bitmap:Cogl.Bitmap) -> Cogl.TextureRectangle """
        pass

    def new_from_foreign(self, ctx, gl_handle, width, height, format): # real signature unknown; restored from __doc__
        """ new_from_foreign(ctx:Cogl.Context, gl_handle:int, width:int, height:int, format:Cogl.PixelFormat) -> Cogl.TextureRectangle """
        pass

    def new_with_size(self, ctx, width, height): # real signature unknown; restored from __doc__
        """ new_with_size(ctx:Cogl.Context, width:int, height:int) -> Cogl.TextureRectangle """
        pass

    def set_components(self, components): # real signature unknown; restored from __doc__
        """ set_components(self, components:Cogl.TextureComponents) """
        pass

    def set_data(self, format, rowstride, data, level): # real signature unknown; restored from __doc__
        """ set_data(self, format:Cogl.PixelFormat, rowstride:int, data:int, level:int) -> int """
        return 0

    def set_premultiplied(self, premultiplied): # real signature unknown; restored from __doc__
        """ set_premultiplied(self, premultiplied:int) """
        pass

    def set_region(self, src_x, src_y, dst_x, dst_y, dst_width, dst_height, width, height, format, rowstride, data): # real signature unknown; restored from __doc__
        """ set_region(self, src_x:int, src_y:int, dst_x:int, dst_y:int, dst_width:int, dst_height:int, width:int, height:int, format:Cogl.PixelFormat, rowstride:int, data:int) -> int """
        return 0

    def set_region_from_bitmap(self, src_x, src_y, dst_x, dst_y, dst_width, dst_height, bitmap): # real signature unknown; restored from __doc__
        """ set_region_from_bitmap(self, src_x:int, src_y:int, dst_x:int, dst_y:int, dst_width:int, dst_height:int, bitmap:Cogl.Bitmap) -> int """
        return 0

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TextureRectangle), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglTextureRectangle (93970932315920)>, '__doc__': None, '__gsignals__': {}, 'new_from_bitmap': gi.FunctionInfo(new_from_bitmap), 'new_from_foreign': gi.FunctionInfo(new_from_foreign), 'new_with_size': gi.FunctionInfo(new_with_size)})"
    __gdoc__ = 'CoglTextureRectangle\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglTextureRectangle (93970932315920)>'
    __info__ = ObjectInfo(TextureRectangle)


