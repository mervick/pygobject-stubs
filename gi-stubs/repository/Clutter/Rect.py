# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Rect(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Rect()
        alloc() -> Clutter.Rect
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Clutter.Rect """
        pass

    def clamp_to_pixel(self): # real signature unknown; restored from __doc__
        """ clamp_to_pixel(self) """
        pass

    def contains_point(self, point): # real signature unknown; restored from __doc__
        """ contains_point(self, point:Clutter.Point) -> bool """
        return False

    def contains_rect(self, b): # real signature unknown; restored from __doc__
        """ contains_rect(self, b:Clutter.Rect) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Clutter.Rect """
        pass

    def equals(self, b): # real signature unknown; restored from __doc__
        """ equals(self, b:Clutter.Rect) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_center(self): # real signature unknown; restored from __doc__
        """ get_center(self) -> center:Clutter.Point """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> float """
        return 0.0

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> float """
        return 0.0

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def init(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float, width:float, height:float) -> Clutter.Rect """
        pass

    def inset(self, d_x, d_y): # real signature unknown; restored from __doc__
        """ inset(self, d_x:float, d_y:float) """
        pass

    def intersection(self, b): # real signature unknown; restored from __doc__
        """ intersection(self, b:Clutter.Rect) -> bool, res:Clutter.Rect """
        return False

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> Clutter.Rect """
        pass

    def offset(self, d_x, d_y): # real signature unknown; restored from __doc__
        """ offset(self, d_x:float, d_y:float) """
        pass

    def union(self, b): # real signature unknown; restored from __doc__
        """ union(self, b:Clutter.Rect) -> res:Clutter.Rect """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Clutter.Rect """
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

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Rect), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterRect (94911696263104)>, '__dict__': <attribute '__dict__' of 'Rect' objects>, '__weakref__': <attribute '__weakref__' of 'Rect' objects>, '__doc__': None, 'origin': <property object at 0x7f54135329f0>, 'size': <property object at 0x7f5413532ae0>, 'alloc': gi.FunctionInfo(alloc), 'clamp_to_pixel': gi.FunctionInfo(clamp_to_pixel), 'contains_point': gi.FunctionInfo(contains_point), 'contains_rect': gi.FunctionInfo(contains_rect), 'copy': gi.FunctionInfo(copy), 'equals': gi.FunctionInfo(equals), 'free': gi.FunctionInfo(free), 'get_center': gi.FunctionInfo(get_center), 'get_height': gi.FunctionInfo(get_height), 'get_width': gi.FunctionInfo(get_width), 'get_x': gi.FunctionInfo(get_x), 'get_y': gi.FunctionInfo(get_y), 'init': gi.FunctionInfo(init), 'inset': gi.FunctionInfo(inset), 'intersection': gi.FunctionInfo(intersection), 'normalize': gi.FunctionInfo(normalize), 'offset': gi.FunctionInfo(offset), 'union': gi.FunctionInfo(union), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType ClutterRect (94911696263104)>'
    __info__ = StructInfo(Rect)


