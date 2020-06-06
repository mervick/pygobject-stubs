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


class ActorBox(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ActorBox()
        new(x_1:float, y_1:float, x_2:float, y_2:float) -> Clutter.ActorBox
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Clutter.ActorBox """
        pass

    def clamp_to_pixel(self): # real signature unknown; restored from __doc__
        """ clamp_to_pixel(self) """
        pass

    def contains(self, x, y): # real signature unknown; restored from __doc__
        """ contains(self, x:float, y:float) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Clutter.ActorBox """
        pass

    def equal(self, box_b): # real signature unknown; restored from __doc__
        """ equal(self, box_b:Clutter.ActorBox) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_vertices(self, verts): # real signature unknown; restored from __doc__
        """ from_vertices(self, verts:list) """
        pass

    def get_area(self): # real signature unknown; restored from __doc__
        """ get_area(self) -> float """
        return 0.0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> float """
        return 0.0

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> x:float, y:float """
        return x

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:float, height:float """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> float """
        return 0.0

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def init(self, x_1, y_1, x_2, y_2): # real signature unknown; restored from __doc__
        """ init(self, x_1:float, y_1:float, x_2:float, y_2:float) -> Clutter.ActorBox """
        pass

    def init_rect(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ init_rect(self, x:float, y:float, width:float, height:float) """
        pass

    def interpolate(self, final, progress): # real signature unknown; restored from __doc__
        """ interpolate(self, final:Clutter.ActorBox, progress:float) -> result:Clutter.ActorBox """
        pass

    def new(self, x_1, y_1, x_2, y_2): # real signature unknown; restored from __doc__
        """ new(x_1:float, y_1:float, x_2:float, y_2:float) -> Clutter.ActorBox """
        pass

    def set_origin(self, x, y): # real signature unknown; restored from __doc__
        """ set_origin(self, x:float, y:float) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:float, height:float) """
        pass

    def union(self, b): # real signature unknown; restored from __doc__
        """ union(self, b:Clutter.ActorBox) -> result:Clutter.ActorBox """
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

    x1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ActorBox), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterActorBox (94911695376800)>, '__dict__': <attribute '__dict__' of 'ActorBox' objects>, '__weakref__': <attribute '__weakref__' of 'ActorBox' objects>, '__doc__': None, 'x1': <property object at 0x7f5413e10e50>, 'y1': <property object at 0x7f5413e10f40>, 'x2': <property object at 0x7f5413e13090>, 'y2': <property object at 0x7f5413e13180>, 'new': gi.FunctionInfo(new), 'clamp_to_pixel': gi.FunctionInfo(clamp_to_pixel), 'contains': gi.FunctionInfo(contains), 'copy': gi.FunctionInfo(copy), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'from_vertices': gi.FunctionInfo(from_vertices), 'get_area': gi.FunctionInfo(get_area), 'get_height': gi.FunctionInfo(get_height), 'get_origin': gi.FunctionInfo(get_origin), 'get_size': gi.FunctionInfo(get_size), 'get_width': gi.FunctionInfo(get_width), 'get_x': gi.FunctionInfo(get_x), 'get_y': gi.FunctionInfo(get_y), 'init': gi.FunctionInfo(init), 'init_rect': gi.FunctionInfo(init_rect), 'interpolate': gi.FunctionInfo(interpolate), 'set_origin': gi.FunctionInfo(set_origin), 'set_size': gi.FunctionInfo(set_size), 'union': gi.FunctionInfo(union), 'alloc': gi.FunctionInfo(alloc)})"
    __gtype__ = None # (!) real value is '<GType ClutterActorBox (94911695376800)>'
    __info__ = StructInfo(ActorBox)


