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


class MultiMap(__gobject.GInterface):
    # no doc
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, key=None): # real signature unknown; restored from __doc__
        """ contains(self, key=None) -> bool """
        return False

    def get(self, key=None): # real signature unknown; restored from __doc__
        """ get(self, key=None) -> Gee.Collection """
        pass

    def get_all_keys(self): # real signature unknown; restored from __doc__
        """ get_all_keys(self) -> Gee.MultiSet """
        pass

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
        """ get_read_only_view(self) -> Gee.MultiMap """
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

    def map_iterator(self): # real signature unknown; restored from __doc__
        """ map_iterator(self) -> Gee.MapIterator """
        pass

    def remove(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ remove(self, key=None, value=None) -> bool """
        return False

    def remove_all(self, key=None): # real signature unknown; restored from __doc__
        """ remove_all(self, key=None) -> bool """
        return False

    def set(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ set(self, key=None, value=None) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(MultiMap), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeMultiMap (94716266688688)>, '__dict__': <attribute '__dict__' of 'MultiMap' objects>, '__weakref__': <attribute '__weakref__' of 'MultiMap' objects>, '__doc__': None, '__gsignals__': {}, 'get_keys': gi.FunctionInfo(get_keys), 'get_all_keys': gi.FunctionInfo(get_all_keys), 'get_values': gi.FunctionInfo(get_values), 'contains': gi.FunctionInfo(contains), 'get': gi.FunctionInfo(get), 'set': gi.FunctionInfo(set), 'remove': gi.FunctionInfo(remove), 'remove_all': gi.FunctionInfo(remove_all), 'clear': gi.FunctionInfo(clear), 'map_iterator': gi.FunctionInfo(map_iterator), 'get_size': gi.FunctionInfo(get_size), 'get_read_only': gi.FunctionInfo(get_read_only), 'get_key_type': gi.FunctionInfo(get_key_type), 'get_value_type': gi.FunctionInfo(get_value_type), 'get_read_only_view': gi.FunctionInfo(get_read_only_view)})"
    __gdoc__ = 'Interface GeeMultiMap\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeMultiMap (94716266688688)>'
    __info__ = InterfaceInfo(MultiMap)


