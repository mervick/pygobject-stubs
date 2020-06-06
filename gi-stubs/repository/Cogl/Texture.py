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


class Texture(__gobject.GInterface):
    # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Texture), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglTexture (93970932290432)>, '__dict__': <attribute '__dict__' of 'Texture' objects>, '__weakref__': <attribute '__weakref__' of 'Texture' objects>, '__doc__': None, '__gsignals__': {}, 'allocate': gi.FunctionInfo(allocate), 'copy_sub_image': gi.FunctionInfo(copy_sub_image), 'get_components': gi.FunctionInfo(get_components), 'get_data': gi.FunctionInfo(get_data), 'get_gl_texture': gi.FunctionInfo(get_gl_texture), 'get_height': gi.FunctionInfo(get_height), 'get_max_waste': gi.FunctionInfo(get_max_waste), 'get_premultiplied': gi.FunctionInfo(get_premultiplied), 'get_width': gi.FunctionInfo(get_width), 'is_sliced': gi.FunctionInfo(is_sliced), 'set_components': gi.FunctionInfo(set_components), 'set_data': gi.FunctionInfo(set_data), 'set_premultiplied': gi.FunctionInfo(set_premultiplied), 'set_region': gi.FunctionInfo(set_region), 'set_region_from_bitmap': gi.FunctionInfo(set_region_from_bitmap)})"
    __gdoc__ = 'Interface CoglTexture\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglTexture (93970932290432)>'
    __info__ = InterfaceInfo(Texture)


