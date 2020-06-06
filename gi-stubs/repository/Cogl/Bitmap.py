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

class Bitmap(Object):
    """
    :Constructors:
    
    ::
    
        Bitmap(**properties)
        new_for_data(context:Cogl.Context, width:int, height:int, format:Cogl.PixelFormat, rowstride:int, data:int) -> Cogl.Bitmap
        new_from_buffer(buffer, format:Cogl.PixelFormat, width:int, height:int, rowstride:int, offset:int) -> Cogl.Bitmap
        new_from_file(filename:str) -> Cogl.Bitmap
        new_with_size(context:Cogl.Context, width:int, height:int, format:Cogl.PixelFormat) -> Cogl.Bitmap
    """
    def get_buffer(self): # real signature unknown; restored from __doc__
        """ get_buffer(self) -> Cogl.PixelBuffer """
        pass

    def get_format(self): # real signature unknown; restored from __doc__
        """ get_format(self) -> Cogl.PixelFormat """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_rowstride(self): # real signature unknown; restored from __doc__
        """ get_rowstride(self) -> int """
        return 0

    def get_size_from_file(self, filename): # real signature unknown; restored from __doc__
        """ get_size_from_file(filename:str) -> int, width:int, height:int """
        return 0

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def new_for_data(self, context, width, height, format, rowstride, data): # real signature unknown; restored from __doc__
        """ new_for_data(context:Cogl.Context, width:int, height:int, format:Cogl.PixelFormat, rowstride:int, data:int) -> Cogl.Bitmap """
        pass

    def new_from_buffer(self, buffer, format, width, height, rowstride, offset): # real signature unknown; restored from __doc__
        """ new_from_buffer(buffer, format:Cogl.PixelFormat, width:int, height:int, rowstride:int, offset:int) -> Cogl.Bitmap """
        pass

    def new_from_file(self, filename): # real signature unknown; restored from __doc__
        """ new_from_file(filename:str) -> Cogl.Bitmap """
        pass

    def new_with_size(self, context, width, height, format): # real signature unknown; restored from __doc__
        """ new_with_size(context:Cogl.Context, width:int, height:int, format:Cogl.PixelFormat) -> Cogl.Bitmap """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Bitmap), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglBitmap (93970931793296)>, '__doc__': None, '__gsignals__': {}, 'new_for_data': gi.FunctionInfo(new_for_data), 'new_from_buffer': gi.FunctionInfo(new_from_buffer), 'new_from_file': gi.FunctionInfo(new_from_file), 'new_with_size': gi.FunctionInfo(new_with_size), 'get_size_from_file': gi.FunctionInfo(get_size_from_file), 'get_buffer': gi.FunctionInfo(get_buffer), 'get_format': gi.FunctionInfo(get_format), 'get_height': gi.FunctionInfo(get_height), 'get_rowstride': gi.FunctionInfo(get_rowstride), 'get_width': gi.FunctionInfo(get_width)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglBitmap (93970931793296)>'
    __info__ = ObjectInfo(Bitmap)


