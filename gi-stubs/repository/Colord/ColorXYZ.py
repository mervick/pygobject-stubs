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


class ColorXYZ(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ColorXYZ()
        new() -> Colord.ColorXYZ
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self, dest): # real signature unknown; restored from __doc__
        """ copy(self, dest:Colord.ColorXYZ) """
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Colord.ColorXYZ """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Colord.ColorXYZ """
        pass

    def normalize(self, max, dest): # real signature unknown; restored from __doc__
        """ normalize(self, max:float, dest:Colord.ColorXYZ) """
        pass

    def set(self, X, Y, Z): # real signature unknown; restored from __doc__
        """ set(self, X:float, Y:float, Z:float) """
        pass

    def to_cct(self): # real signature unknown; restored from __doc__
        """ to_cct(self) -> float """
        return 0.0

    def to_uvw(self, whitepoint, dest): # real signature unknown; restored from __doc__
        """ to_uvw(self, whitepoint:Colord.ColorXYZ, dest:Colord.ColorUVW) """
        pass

    def to_yxy(self, dest): # real signature unknown; restored from __doc__
        """ to_yxy(self, dest:Colord.ColorYxy) """
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
        """ new() -> Colord.ColorXYZ """
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

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ColorXYZ), '__module__': 'gi.repository.Colord', '__gtype__': <GType CdColorXYZ (94892598790720)>, '__dict__': <attribute '__dict__' of 'ColorXYZ' objects>, '__weakref__': <attribute '__weakref__' of 'ColorXYZ' objects>, '__doc__': None, 'X': <property object at 0x7f0913373c20>, 'Y': <property object at 0x7f0913373d10>, 'Z': <property object at 0x7f0913373e00>, 'new': gi.FunctionInfo(new), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'dup': gi.FunctionInfo(dup), 'free': gi.FunctionInfo(free), 'normalize': gi.FunctionInfo(normalize), 'set': gi.FunctionInfo(set), 'to_cct': gi.FunctionInfo(to_cct), 'to_uvw': gi.FunctionInfo(to_uvw), 'to_yxy': gi.FunctionInfo(to_yxy), '__new__': <staticmethod object at 0x7f0913370700>, '__init__': <function nothing at 0x7f09135aaee0>})"
    __gtype__ = None # (!) real value is '<GType CdColorXYZ (94892598790720)>'
    __info__ = StructInfo(ColorXYZ)


