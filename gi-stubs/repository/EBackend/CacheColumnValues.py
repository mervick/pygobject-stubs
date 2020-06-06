# encoding: utf-8
# module gi.repository.EBackend
# from /usr/lib64/girepository-1.0/EBackend-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class CacheColumnValues(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> EBackend.CacheColumnValues
    """
    def contains(self, name): # real signature unknown; restored from __doc__
        """ contains(self, name:str) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EBackend.CacheColumnValues """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def init_iter(self, iter): # real signature unknown; restored from __doc__
        """ init_iter(self, iter:dict) """
        pass

    def lookup(self, name): # real signature unknown; restored from __doc__
        """ lookup(self, name:str) -> str """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> EBackend.CacheColumnValues """
        pass

    def put(self, name, value=None): # real signature unknown; restored from __doc__
        """ put(self, name:str, value:str=None) """
        pass

    def remove(self, name): # real signature unknown; restored from __doc__
        """ remove(self, name:str) -> bool """
        return False

    def remove_all(self): # real signature unknown; restored from __doc__
        """ remove_all(self) """
        pass

    def take(self, name, value=None): # real signature unknown; restored from __doc__
        """ take(self, name:str, value:str=None) """
        pass

    def take_value(self, name, value=None): # real signature unknown; restored from __doc__
        """ take_value(self, name:str, value:str=None) """
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
        """ new() -> EBackend.CacheColumnValues """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CacheColumnValues), '__module__': 'gi.repository.EBackend', '__gtype__': <GType ECacheColumnValues (94170535209184)>, '__dict__': <attribute '__dict__' of 'CacheColumnValues' objects>, '__weakref__': <attribute '__weakref__' of 'CacheColumnValues' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'contains': gi.FunctionInfo(contains), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_size': gi.FunctionInfo(get_size), 'init_iter': gi.FunctionInfo(init_iter), 'lookup': gi.FunctionInfo(lookup), 'put': gi.FunctionInfo(put), 'remove': gi.FunctionInfo(remove), 'remove_all': gi.FunctionInfo(remove_all), 'take': gi.FunctionInfo(take), 'take_value': gi.FunctionInfo(take_value), '__new__': <staticmethod object at 0x7f9dc2d787f0>, '__init__': <function nothing at 0x7f9dc301fee0>})"
    __gtype__ = None # (!) real value is '<GType ECacheColumnValues (94170535209184)>'
    __info__ = StructInfo(CacheColumnValues)


