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


class PaintVolume(__gi.Boxed):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Clutter.PaintVolume """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_depth(self): # real signature unknown; restored from __doc__
        """ get_depth(self) -> float """
        return 0.0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> float """
        return 0.0

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> vertex:Clutter.Vertex """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> float """
        return 0.0

    def set_depth(self, depth): # real signature unknown; restored from __doc__
        """ set_depth(self, depth:float) """
        pass

    def set_from_allocation(self, actor): # real signature unknown; restored from __doc__
        """ set_from_allocation(self, actor:Clutter.Actor) -> bool """
        return False

    def set_height(self, height): # real signature unknown; restored from __doc__
        """ set_height(self, height:float) """
        pass

    def set_origin(self, origin): # real signature unknown; restored from __doc__
        """ set_origin(self, origin:Clutter.Vertex) """
        pass

    def set_width(self, width): # real signature unknown; restored from __doc__
        """ set_width(self, width:float) """
        pass

    def union(self, another_pv): # real signature unknown; restored from __doc__
        """ union(self, another_pv:Clutter.PaintVolume) """
        pass

    def union_box(self, box): # real signature unknown; restored from __doc__
        """ union_box(self, box:Clutter.ActorBox) """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PaintVolume), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterPaintVolume (94911696226640)>, '__dict__': <attribute '__dict__' of 'PaintVolume' objects>, '__weakref__': <attribute '__weakref__' of 'PaintVolume' objects>, '__doc__': None, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_depth': gi.FunctionInfo(get_depth), 'get_height': gi.FunctionInfo(get_height), 'get_origin': gi.FunctionInfo(get_origin), 'get_width': gi.FunctionInfo(get_width), 'set_depth': gi.FunctionInfo(set_depth), 'set_from_allocation': gi.FunctionInfo(set_from_allocation), 'set_height': gi.FunctionInfo(set_height), 'set_origin': gi.FunctionInfo(set_origin), 'set_width': gi.FunctionInfo(set_width), 'union': gi.FunctionInfo(union), 'union_box': gi.FunctionInfo(union_box)})"
    __gtype__ = None # (!) real value is '<GType ClutterPaintVolume (94911696226640)>'
    __info__ = StructInfo(PaintVolume)


