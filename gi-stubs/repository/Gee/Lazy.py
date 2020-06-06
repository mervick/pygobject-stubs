# encoding: utf-8
# module gi.repository.Gee
# from /usr/lib64/girepository-1.0/Gee-0.8.typelib
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


from .object import object

class Lazy(object):
    """
    :Constructors:
    
    ::
    
        Lazy(**properties)
        new(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, func:Gee.LazyFunc, func_target=None) -> Gee.Lazy
        from_value(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, item=None) -> Gee.Lazy
    """
    def eval(self): # real signature unknown; restored from __doc__
        """ eval(self) """
        pass

    def from_value(self, g_type, g_dup_func, g_destroy_func, item=None): # real signature unknown; restored from __doc__
        """ from_value(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, item=None) -> Gee.Lazy """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get(self) """
        pass

    def get_future(self): # real signature unknown; restored from __doc__
        """ get_future(self) -> Gee.Future """
        pass

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) """
        pass

    def new(self, g_type, g_dup_func, g_destroy_func, func, func_target=None): # real signature unknown; restored from __doc__
        """ new(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, func:Gee.LazyFunc, func_target=None) -> Gee.Lazy """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Lazy), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeLazy (196)>, '__dict__': <attribute '__dict__' of 'Lazy' objects>, '__weakref__': <attribute '__weakref__' of 'Lazy' objects>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'from_value': gi.FunctionInfo(from_value), 'eval': gi.FunctionInfo(eval), 'get': gi.FunctionInfo(get), 'get_value': gi.FunctionInfo(get_value), 'get_future': gi.FunctionInfo(get_future), 'parent_instance': <property object at 0x7f6a87b51d60>, 'ref_count': <property object at 0x7f6a87b51e50>, 'priv': <property object at 0x7f6a87b51f40>})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeLazy (196)>'
    __info__ = ObjectInfo(Lazy)


