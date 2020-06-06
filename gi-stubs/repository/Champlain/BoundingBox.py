# encoding: utf-8
# module gi.repository.Champlain
# from /usr/lib64/girepository-1.0/Champlain-0.12.typelib
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
import gi.repository.Clutter as __gi_repository_Clutter
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class BoundingBox(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        BoundingBox()
        new() -> Champlain.BoundingBox
    """
    def compose(self, other): # real signature unknown; restored from __doc__
        """ compose(self, other:Champlain.BoundingBox) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Champlain.BoundingBox """
        pass

    def covers(self, latitude, longitude): # real signature unknown; restored from __doc__
        """ covers(self, latitude:float, longitude:float) -> bool """
        return False

    def extend(self, latitude, longitude): # real signature unknown; restored from __doc__
        """ extend(self, latitude:float, longitude:float) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_center(self): # real signature unknown; restored from __doc__
        """ get_center(self) -> latitude:float, longitude:float """
        pass

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Champlain.BoundingBox """
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
        """ new() -> Champlain.BoundingBox """
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

    bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BoundingBox), '__module__': 'gi.repository.Champlain', '__gtype__': <GType ChamplainBoundingBox (94016587915024)>, '__dict__': <attribute '__dict__' of 'BoundingBox' objects>, '__weakref__': <attribute '__weakref__' of 'BoundingBox' objects>, '__doc__': None, 'left': <property object at 0x7f2e2d9b6220>, 'top': <property object at 0x7f2e2d9b6310>, 'right': <property object at 0x7f2e2d9b6400>, 'bottom': <property object at 0x7f2e2d9b64f0>, 'new': gi.FunctionInfo(new), 'compose': gi.FunctionInfo(compose), 'copy': gi.FunctionInfo(copy), 'covers': gi.FunctionInfo(covers), 'extend': gi.FunctionInfo(extend), 'free': gi.FunctionInfo(free), 'get_center': gi.FunctionInfo(get_center), 'is_valid': gi.FunctionInfo(is_valid), '__new__': <staticmethod object at 0x7f2e2d9b1910>, '__init__': <function nothing at 0x7f2e2de46ee0>})"
    __gtype__ = None # (!) real value is '<GType ChamplainBoundingBox (94016587915024)>'
    __info__ = StructInfo(BoundingBox)


