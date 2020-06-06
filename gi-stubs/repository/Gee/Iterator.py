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


class Iterator(__gobject.GInterface):
    # no doc
    def concat(self, g_type, g_dup_func, g_destroy_func, iters): # real signature unknown; restored from __doc__
        """ concat(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, iters:Gee.Iterator) -> Gee.Iterator """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get(self) """
        pass

    def get_read_only(self): # real signature unknown; restored from __doc__
        """ get_read_only(self) -> bool """
        return False

    def get_valid(self): # real signature unknown; restored from __doc__
        """ get_valid(self) -> bool """
        return False

    def has_next(self): # real signature unknown; restored from __doc__
        """ has_next(self) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def remove(self): # real signature unknown; restored from __doc__
        """ remove(self) """
        pass

    def unfold(self, a_type, a_dup_func, a_destroy_func, f, f_target=None, current=None): # real signature unknown; restored from __doc__
        """ unfold(a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.UnfoldFunc, f_target=None, current:Gee.Lazy=None) -> Gee.Iterator """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Iterator), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeIterator (94716266944992)>, '__dict__': <attribute '__dict__' of 'Iterator' objects>, '__weakref__': <attribute '__weakref__' of 'Iterator' objects>, '__doc__': None, '__gsignals__': {}, 'next': gi.FunctionInfo(next), 'has_next': gi.FunctionInfo(has_next), 'get': gi.FunctionInfo(get), 'remove': gi.FunctionInfo(remove), 'unfold': gi.FunctionInfo(unfold), 'concat': gi.FunctionInfo(concat), 'get_valid': gi.FunctionInfo(get_valid), 'get_read_only': gi.FunctionInfo(get_read_only)})"
    __gdoc__ = 'Interface GeeIterator\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeIterator (94716266944992)>'
    __info__ = InterfaceInfo(Iterator)


