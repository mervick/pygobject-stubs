# encoding: utf-8
# module gi.repository.GLib
# from /usr/lib64/girepository-1.0/GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # /usr/lib64/python3.8/site-packages/gi/_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class HashTable(__gi.Boxed):
    # no doc
    def add(self, hash_table, key=None): # real signature unknown; restored from __doc__
        """ add(hash_table:dict, key=None) -> bool """
        return False

    def contains(self, hash_table, key=None): # real signature unknown; restored from __doc__
        """ contains(hash_table:dict, key=None) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, hash_table): # real signature unknown; restored from __doc__
        """ destroy(hash_table:dict) """
        pass

    def insert(self, hash_table, key=None, value=None): # real signature unknown; restored from __doc__
        """ insert(hash_table:dict, key=None, value=None) -> bool """
        return False

    def lookup(self, hash_table, key=None): # real signature unknown; restored from __doc__
        """ lookup(hash_table:dict, key=None) """
        pass

    def lookup_extended(self, hash_table, lookup_key=None): # real signature unknown; restored from __doc__
        """ lookup_extended(hash_table:dict, lookup_key=None) -> bool, orig_key, value """
        return False

    def remove(self, hash_table, key=None): # real signature unknown; restored from __doc__
        """ remove(hash_table:dict, key=None) -> bool """
        return False

    def remove_all(self, hash_table): # real signature unknown; restored from __doc__
        """ remove_all(hash_table:dict) """
        pass

    def replace(self, hash_table, key=None, value=None): # real signature unknown; restored from __doc__
        """ replace(hash_table:dict, key=None, value=None) -> bool """
        return False

    def size(self, hash_table): # real signature unknown; restored from __doc__
        """ size(hash_table:dict) -> int """
        return 0

    def steal(self, hash_table, key=None): # real signature unknown; restored from __doc__
        """ steal(hash_table:dict, key=None) -> bool """
        return False

    def steal_all(self, hash_table): # real signature unknown; restored from __doc__
        """ steal_all(hash_table:dict) """
        pass

    def steal_extended(self, hash_table, lookup_key=None): # real signature unknown; restored from __doc__
        """ steal_extended(hash_table:dict, lookup_key=None) -> bool, stolen_key, stolen_value """
        return False

    def unref(self, hash_table): # real signature unknown; restored from __doc__
        """ unref(hash_table:dict) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HashTable), '__module__': 'gi.repository.GLib', '__gtype__': <GType GHashTable (94581033701392)>, '__dict__': <attribute '__dict__' of 'HashTable' objects>, '__weakref__': <attribute '__weakref__' of 'HashTable' objects>, '__doc__': None, 'add': gi.FunctionInfo(add), 'contains': gi.FunctionInfo(contains), 'destroy': gi.FunctionInfo(destroy), 'insert': gi.FunctionInfo(insert), 'lookup': gi.FunctionInfo(lookup), 'lookup_extended': gi.FunctionInfo(lookup_extended), 'remove': gi.FunctionInfo(remove), 'remove_all': gi.FunctionInfo(remove_all), 'replace': gi.FunctionInfo(replace), 'size': gi.FunctionInfo(size), 'steal': gi.FunctionInfo(steal), 'steal_all': gi.FunctionInfo(steal_all), 'steal_extended': gi.FunctionInfo(steal_extended), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GHashTable (94581033701392)>'
    __info__ = StructInfo(HashTable)


