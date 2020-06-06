# encoding: utf-8
# module gi.repository.Colord
# from /usr/lib64/girepository-1.0/Colord-1.0.typelib
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


class ColorRGB(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ColorRGB()
        new() -> Colord.ColorRGB
    """
    def array_interpolate(self, array, new_length): # real signature unknown; restored from __doc__
        """ array_interpolate(array:list, new_length:int) -> list """
        return []

    def array_is_monotonic(self, array): # real signature unknown; restored from __doc__
        """ array_is_monotonic(array:list) -> bool """
        return False

    def array_new(self): # real signature unknown; restored from __doc__
        """ array_new() -> list """
        return []

    def copy(self, dest): # real signature unknown; restored from __doc__
        """ copy(self, dest:Colord.ColorRGB) """
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Colord.ColorRGB """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_wavelength(self, wavelength): # real signature unknown; restored from __doc__
        """ from_wavelength(self, wavelength:float) """
        pass

    def interpolate(self, p2, index, result): # real signature unknown; restored from __doc__
        """ interpolate(self, p2:Colord.ColorRGB, index:float, result:Colord.ColorRGB) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Colord.ColorRGB """
        pass

    def set(self, R, G, B): # real signature unknown; restored from __doc__
        """ set(self, R:float, G:float, B:float) """
        pass

    def to_rgb8(self, dest): # real signature unknown; restored from __doc__
        """ to_rgb8(self, dest:Colord.ColorRGB8) """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Colord.ColorRGB """
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

    B = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    G = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    R = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ColorRGB), '__module__': 'gi.repository.Colord', '__gtype__': <GType CdColorRGB (94892598484048)>, '__dict__': <attribute '__dict__' of 'ColorRGB' objects>, '__weakref__': <attribute '__weakref__' of 'ColorRGB' objects>, '__doc__': None, 'R': <property object at 0x7f0913371f90>, 'G': <property object at 0x7f09133730e0>, 'B': <property object at 0x7f09133731d0>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'dup': gi.FunctionInfo(dup), 'free': gi.FunctionInfo(free), 'from_wavelength': gi.FunctionInfo(from_wavelength), 'interpolate': gi.FunctionInfo(interpolate), 'set': gi.FunctionInfo(set), 'to_rgb8': gi.FunctionInfo(to_rgb8), 'array_interpolate': gi.FunctionInfo(array_interpolate), 'array_is_monotonic': gi.FunctionInfo(array_is_monotonic), 'array_new': gi.FunctionInfo(array_new), '__new__': <staticmethod object at 0x7f0913370370>, '__init__': <function nothing at 0x7f09135aaee0>})"
    __gtype__ = None # (!) real value is '<GType CdColorRGB (94892598484048)>'
    __info__ = StructInfo(ColorRGB)


