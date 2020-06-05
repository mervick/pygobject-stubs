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


class Tree(__gi.Struct):
    # no doc
    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def insert(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ insert(self, key=None, value=None) """
        pass

    def lookup(self, key=None): # real signature unknown; restored from __doc__
        """ lookup(self, key=None) """
        pass

    def lookup_extended(self, lookup_key=None): # real signature unknown; restored from __doc__
        """ lookup_extended(self, lookup_key=None) -> bool, orig_key, value """
        return False

    def nnodes(self): # real signature unknown; restored from __doc__
        """ nnodes(self) -> int """
        return 0

    def remove(self, key=None): # real signature unknown; restored from __doc__
        """ remove(self, key=None) -> bool """
        return False

    def replace(self, key=None, value=None): # real signature unknown; restored from __doc__
        """ replace(self, key=None, value=None) """
        pass

    def steal(self, key=None): # real signature unknown; restored from __doc__
        """ steal(self, key=None) -> bool """
        return False

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Tree), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Tree' objects>, '__weakref__': <attribute '__weakref__' of 'Tree' objects>, '__doc__': None, 'destroy': gi.FunctionInfo(destroy), 'height': gi.FunctionInfo(height), 'insert': gi.FunctionInfo(insert), 'lookup': gi.FunctionInfo(lookup), 'lookup_extended': gi.FunctionInfo(lookup_extended), 'nnodes': gi.FunctionInfo(nnodes), 'remove': gi.FunctionInfo(remove), 'replace': gi.FunctionInfo(replace), 'steal': gi.FunctionInfo(steal), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Tree)


