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


class Map(__gobject.GInterface):
    # no doc
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, key=None): # real signature unknown; restored from __doc__
        """ contains(self, key=None) -> bool """
        return False

    def contains_all(self, map): # real signature unknown; restored from __doc__
        """ contains_all(self, map:Gee.Map) -> bool """
        return False

    def empty(self, k_type, k_dup_func, k_destroy_func, v_type, v_dup_func, v_destroy_func): # real signature unknown; restored from __doc__
        """ empty(k_type:GType, k_dup_func:GObject.BoxedCopyFunc, k_destroy_func:GLib.DestroyNotify, v_type:GType, v_dup_func:GObject.BoxedCopyFunc, v_destroy_func:GLib.DestroyNotify) -> Gee.Map """
        pass

    def get(self, key=None): # real signature unknown; restored from __doc__
        """ get(self, key=None) """
        pass

    def get_entries(self): # real signature unknown; restored from __doc__
        """ get_entries(self) -> Gee.Set """
        pass

    def get_is_empty(self): # real signature unknown; restored from __doc__
        """ get_is_empty(self) -> bool """
        return False

    def get_keys(self): # real signature unknown; restored from __doc__
        """ get_keys(self) -> Gee.Set """
        pass

    def get_key_type(self): # real signature unknown; restored from __doc__
        """ get_key_type(self) -> GType """
        pass

    def get_read_only(self): # real signature unknown; restored from __doc__
        """ get_read_only(self) -> bool """
        return False

    def get_read_only_view(self): # real signature unknown; restored from __doc__
        """ get_read_only_view(self) -> Gee.Map """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_values(self): # real signature unknown; restored from __doc__
        """ get_values(self) -> Gee.Collection """
        pass

    def get_value_type(self): # real signature unknown; restored from __doc__
        """ get_value_type(self) -> GType """
        pass

    def has(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ has(self, key=None, value=None) -> bool """
        return False

    def has_all(self, map): # real signature unknown; restored from __doc__
        """ has_all(self, map:Gee.Map) -> bool """
        return False

    def has_key(self, key=None): # real signature unknown; restored from __doc__
        """ has_key(self, key=None) -> bool """
        return False

    def map_iterator(self): # real signature unknown; restored from __doc__
        """ map_iterator(self) -> Gee.MapIterator """
        pass

    def remove(self, key=None): # real signature unknown; restored from __doc__
        """ remove(self, key=None) -> bool, value """
        return False

    def remove_all(self, map): # real signature unknown; restored from __doc__
        """ remove_all(self, map:Gee.Map) -> bool """
        return False

    def set(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ set(self, key=None, value=None) """
        pass

    def set_all(self, map): # real signature unknown; restored from __doc__
        """ set_all(self, map:Gee.Map) """
        pass

    def unset(self, key=None): # real signature unknown; restored from __doc__
        """ unset(self, key=None) -> bool, value """
        return False

    def unset_all(self, map): # real signature unknown; restored from __doc__
        """ unset_all(self, map:Gee.Map) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Map), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeMap (94716266382656)>, '__dict__': <attribute '__dict__' of 'Map' objects>, '__weakref__': <attribute '__weakref__' of 'Map' objects>, '__doc__': None, '__gsignals__': {}, 'has_key': gi.FunctionInfo(has_key), 'contains': gi.FunctionInfo(contains), 'has': gi.FunctionInfo(has), 'get': gi.FunctionInfo(get), 'set': gi.FunctionInfo(set), 'unset': gi.FunctionInfo(unset), 'remove': gi.FunctionInfo(remove), 'clear': gi.FunctionInfo(clear), 'map_iterator': gi.FunctionInfo(map_iterator), 'set_all': gi.FunctionInfo(set_all), 'unset_all': gi.FunctionInfo(unset_all), 'remove_all': gi.FunctionInfo(remove_all), 'has_all': gi.FunctionInfo(has_all), 'contains_all': gi.FunctionInfo(contains_all), 'empty': gi.FunctionInfo(empty), 'get_size': gi.FunctionInfo(get_size), 'get_is_empty': gi.FunctionInfo(get_is_empty), 'get_read_only': gi.FunctionInfo(get_read_only), 'get_keys': gi.FunctionInfo(get_keys), 'get_values': gi.FunctionInfo(get_values), 'get_entries': gi.FunctionInfo(get_entries), 'get_read_only_view': gi.FunctionInfo(get_read_only_view), 'get_key_type': gi.FunctionInfo(get_key_type), 'get_value_type': gi.FunctionInfo(get_value_type)})"
    __gdoc__ = 'Interface GeeMap\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeMap (94716266382656)>'
    __info__ = InterfaceInfo(Map)


