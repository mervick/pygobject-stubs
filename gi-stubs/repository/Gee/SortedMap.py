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


class SortedMap(__gobject.GInterface):
    # no doc
    def empty(self, k_type, k_dup_func, k_destroy_func, v_type, v_dup_func, v_destroy_func): # real signature unknown; restored from __doc__
        """ empty(k_type:GType, k_dup_func:GObject.BoxedCopyFunc, k_destroy_func:GLib.DestroyNotify, v_type:GType, v_dup_func:GObject.BoxedCopyFunc, v_destroy_func:GLib.DestroyNotify) -> Gee.Map """
        pass

    def get_ascending_entries(self): # real signature unknown; restored from __doc__
        """ get_ascending_entries(self) -> Gee.SortedSet """
        pass

    def get_ascending_keys(self): # real signature unknown; restored from __doc__
        """ get_ascending_keys(self) -> Gee.SortedSet """
        pass

    def get_read_only_view(self): # real signature unknown; restored from __doc__
        """ get_read_only_view(self) -> Gee.SortedMap """
        pass

    def head_map(self, before=None): # real signature unknown; restored from __doc__
        """ head_map(self, before=None) -> Gee.SortedMap """
        pass

    def sub_map(self, before=None, after=None): # real signature unknown; restored from __doc__
        """ sub_map(self, before=None, after=None) -> Gee.SortedMap """
        pass

    def tail_map(self, after=None): # real signature unknown; restored from __doc__
        """ tail_map(self, after=None) -> Gee.SortedMap """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(SortedMap), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeSortedMap (94716266384320)>, '__dict__': <attribute '__dict__' of 'SortedMap' objects>, '__weakref__': <attribute '__weakref__' of 'SortedMap' objects>, '__doc__': None, '__gsignals__': {}, 'head_map': gi.FunctionInfo(head_map), 'tail_map': gi.FunctionInfo(tail_map), 'sub_map': gi.FunctionInfo(sub_map), 'empty': gi.FunctionInfo(empty), 'get_ascending_keys': gi.FunctionInfo(get_ascending_keys), 'get_ascending_entries': gi.FunctionInfo(get_ascending_entries), 'get_read_only_view': gi.FunctionInfo(get_read_only_view)})"
    __gdoc__ = 'Interface GeeSortedMap\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeSortedMap (94716266384320)>'
    __info__ = InterfaceInfo(SortedMap)


