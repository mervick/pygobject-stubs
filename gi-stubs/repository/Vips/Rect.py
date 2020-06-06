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


class Rect(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Rect()
    """
    def includespoint(self, x, y): # real signature unknown; restored from __doc__
        """ includespoint(self, x:int, y:int) -> bool """
        return False

    def intersectrect(self, r2): # real signature unknown; restored from __doc__
        """ intersectrect(self, r2:Vips.Rect) -> out:Vips.Rect """
        pass

    def rect_equalsrect(self, r2): # real signature unknown; restored from __doc__
        """ rect_equalsrect(self, r2:Vips.Rect) -> bool """
        return False

    def rect_includesrect(self, r2): # real signature unknown; restored from __doc__
        """ rect_includesrect(self, r2:Vips.Rect) -> bool """
        return False

    def rect_isempty(self): # real signature unknown; restored from __doc__
        """ rect_isempty(self) -> bool """
        return False

    def rect_marginadjust(self, n): # real signature unknown; restored from __doc__
        """ rect_marginadjust(self, n:int) """
        pass

    def rect_normalise(self): # real signature unknown; restored from __doc__
        """ rect_normalise(self) """
        pass

    def rect_overlapsrect(self, r2): # real signature unknown; restored from __doc__
        """ rect_overlapsrect(self, r2:Vips.Rect) -> bool """
        return False

    def unionrect(self, r2): # real signature unknown; restored from __doc__
        """ unionrect(self, r2:Vips.Rect) -> out:Vips.Rect """
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

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Rect), '__module__': 'gi.repository.Vips', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Rect' objects>, '__weakref__': <attribute '__weakref__' of 'Rect' objects>, '__doc__': None, 'left': <property object at 0x7f41839a7c20>, 'top': <property object at 0x7f41839a7d10>, 'width': <property object at 0x7f41839a7e00>, 'height': <property object at 0x7f41839a7ef0>, 'includespoint': gi.FunctionInfo(includespoint), 'intersectrect': gi.FunctionInfo(intersectrect), 'rect_equalsrect': gi.FunctionInfo(rect_equalsrect), 'rect_includesrect': gi.FunctionInfo(rect_includesrect), 'rect_isempty': gi.FunctionInfo(rect_isempty), 'rect_marginadjust': gi.FunctionInfo(rect_marginadjust), 'rect_normalise': gi.FunctionInfo(rect_normalise), 'rect_overlapsrect': gi.FunctionInfo(rect_overlapsrect), 'unionrect': gi.FunctionInfo(unionrect)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Rect)


