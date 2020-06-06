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


class Collection(__gobject.GInterface):
    # no doc
    def add(self, item=None): # real signature unknown; restored from __doc__
        """ add(self, item=None) -> bool """
        return False

    def add_all(self, collection): # real signature unknown; restored from __doc__
        """ add_all(self, collection:Gee.Collection) -> bool """
        return False

    def add_all_array(self, array): # real signature unknown; restored from __doc__
        """ add_all_array(self, array:list) -> bool """
        return False

    def add_all_iterator(self, iter): # real signature unknown; restored from __doc__
        """ add_all_iterator(self, iter:Gee.Iterator) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, item=None): # real signature unknown; restored from __doc__
        """ contains(self, item=None) -> bool """
        return False

    def contains_all(self, collection): # real signature unknown; restored from __doc__
        """ contains_all(self, collection:Gee.Collection) -> bool """
        return False

    def contains_all_array(self, array): # real signature unknown; restored from __doc__
        """ contains_all_array(self, array:list) -> bool """
        return False

    def contains_all_iterator(self, iter): # real signature unknown; restored from __doc__
        """ contains_all_iterator(self, iter:Gee.Iterator) -> bool """
        return False

    def empty(self, g_type, g_dup_func, g_destroy_func): # real signature unknown; restored from __doc__
        """ empty(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify) -> Gee.Collection """
        pass

    def get_is_empty(self): # real signature unknown; restored from __doc__
        """ get_is_empty(self) -> bool """
        return False

    def get_read_only(self): # real signature unknown; restored from __doc__
        """ get_read_only(self) -> bool """
        return False

    def get_read_only_view(self): # real signature unknown; restored from __doc__
        """ get_read_only_view(self) -> Gee.Collection """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def remove(self, item=None): # real signature unknown; restored from __doc__
        """ remove(self, item=None) -> bool """
        return False

    def remove_all(self, collection): # real signature unknown; restored from __doc__
        """ remove_all(self, collection:Gee.Collection) -> bool """
        return False

    def remove_all_array(self, array): # real signature unknown; restored from __doc__
        """ remove_all_array(self, array:list) -> bool """
        return False

    def remove_all_iterator(self, iter): # real signature unknown; restored from __doc__
        """ remove_all_iterator(self, iter:Gee.Iterator) -> bool """
        return False

    def retain_all(self, collection): # real signature unknown; restored from __doc__
        """ retain_all(self, collection:Gee.Collection) -> bool """
        return False

    def to_array(self): # real signature unknown; restored from __doc__
        """ to_array(self) -> list, result_length1:int """
        return []

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Collection), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeCollection (94716266572752)>, '__dict__': <attribute '__dict__' of 'Collection' objects>, '__weakref__': <attribute '__weakref__' of 'Collection' objects>, '__doc__': None, '__gsignals__': {}, 'contains': gi.FunctionInfo(contains), 'add': gi.FunctionInfo(add), 'remove': gi.FunctionInfo(remove), 'clear': gi.FunctionInfo(clear), 'add_all': gi.FunctionInfo(add_all), 'contains_all': gi.FunctionInfo(contains_all), 'remove_all': gi.FunctionInfo(remove_all), 'retain_all': gi.FunctionInfo(retain_all), 'to_array': gi.FunctionInfo(to_array), 'add_all_array': gi.FunctionInfo(add_all_array), 'contains_all_array': gi.FunctionInfo(contains_all_array), 'remove_all_array': gi.FunctionInfo(remove_all_array), 'add_all_iterator': gi.FunctionInfo(add_all_iterator), 'contains_all_iterator': gi.FunctionInfo(contains_all_iterator), 'remove_all_iterator': gi.FunctionInfo(remove_all_iterator), 'empty': gi.FunctionInfo(empty), 'get_size': gi.FunctionInfo(get_size), 'get_is_empty': gi.FunctionInfo(get_is_empty), 'get_read_only': gi.FunctionInfo(get_read_only), 'get_read_only_view': gi.FunctionInfo(get_read_only_view)})"
    __gdoc__ = 'Interface GeeCollection\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeCollection (94716266572752)>'
    __info__ = InterfaceInfo(Collection)


