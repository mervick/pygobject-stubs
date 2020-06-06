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


class SortedSet(__gobject.GInterface):
    # no doc
    def ceil(self, element=None): # real signature unknown; restored from __doc__
        """ ceil(self, element=None) """
        pass

    def empty(self, g_type, g_dup_func, g_destroy_func): # real signature unknown; restored from __doc__
        """ empty(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify) -> Gee.SortedSet """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) """
        pass

    def floor(self, element=None): # real signature unknown; restored from __doc__
        """ floor(self, element=None) """
        pass

    def get_read_only_view(self): # real signature unknown; restored from __doc__
        """ get_read_only_view(self) -> Gee.SortedSet """
        pass

    def head_set(self, before=None): # real signature unknown; restored from __doc__
        """ head_set(self, before=None) -> Gee.SortedSet """
        pass

    def higher(self, element=None): # real signature unknown; restored from __doc__
        """ higher(self, element=None) """
        pass

    def iterator_at(self, element=None): # real signature unknown; restored from __doc__
        """ iterator_at(self, element=None) -> Gee.Iterator """
        pass

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) """
        pass

    def lower(self, element=None): # real signature unknown; restored from __doc__
        """ lower(self, element=None) """
        pass

    def sub_set(self, from_=None, to=None): # real signature unknown; restored from __doc__
        """ sub_set(self, from_=None, to=None) -> Gee.SortedSet """
        pass

    def tail_set(self, after=None): # real signature unknown; restored from __doc__
        """ tail_set(self, after=None) -> Gee.SortedSet """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(SortedSet), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeSortedSet (94716266691568)>, '__dict__': <attribute '__dict__' of 'SortedSet' objects>, '__weakref__': <attribute '__weakref__' of 'SortedSet' objects>, '__doc__': None, '__gsignals__': {}, 'first': gi.FunctionInfo(first), 'last': gi.FunctionInfo(last), 'iterator_at': gi.FunctionInfo(iterator_at), 'lower': gi.FunctionInfo(lower), 'higher': gi.FunctionInfo(higher), 'floor': gi.FunctionInfo(floor), 'ceil': gi.FunctionInfo(ceil), 'head_set': gi.FunctionInfo(head_set), 'tail_set': gi.FunctionInfo(tail_set), 'sub_set': gi.FunctionInfo(sub_set), 'empty': gi.FunctionInfo(empty), 'get_read_only_view': gi.FunctionInfo(get_read_only_view)})"
    __gdoc__ = 'Interface GeeSortedSet\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeSortedSet (94716266691568)>'
    __info__ = InterfaceInfo(SortedSet)


