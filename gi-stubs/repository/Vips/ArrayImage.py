# encoding: utf-8
# module gi.repository.Vips
# from /usr/lib64/girepository-1.0/Vips-8.0.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class ArrayImage(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ArrayImage()
        empty() -> Vips.ArrayImage
        new(array:list) -> Vips.ArrayImage
        new_from_string(string:str, flags:Vips.Access) -> Vips.ArrayImage
    """
    def array_image_append(self, image): # real signature unknown; restored from __doc__
        """ array_image_append(self, image:Vips.Image) -> Vips.ArrayImage """
        pass

    def array_image_get(self): # real signature unknown; restored from __doc__
        """ array_image_get(self) -> list, n:int """
        return []

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """ empty() -> Vips.ArrayImage """
        pass

    def new(self, array): # real signature unknown; restored from __doc__
        """ new(array:list) -> Vips.ArrayImage """
        pass

    def new_from_string(self, string, flags): # real signature unknown; restored from __doc__
        """ new_from_string(string:str, flags:Vips.Access) -> Vips.ArrayImage """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ArrayImage), '__module__': 'gi.repository.Vips', '__gtype__': <GType VipsArrayImage (94317410451584)>, '__dict__': <attribute '__dict__' of 'ArrayImage' objects>, '__weakref__': <attribute '__weakref__' of 'ArrayImage' objects>, '__doc__': None, 'area': <property object at 0x7f41868d0bd0>, 'empty': gi.FunctionInfo(empty), 'new': gi.FunctionInfo(new), 'new_from_string': gi.FunctionInfo(new_from_string), 'array_image_append': gi.FunctionInfo(array_image_append), 'array_image_get': gi.FunctionInfo(array_image_get)})"
    __gtype__ = None # (!) real value is '<GType VipsArrayImage (94317410451584)>'
    __info__ = StructInfo(ArrayImage)


