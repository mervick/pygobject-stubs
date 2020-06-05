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


class ByteArray(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ByteArray()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self, array, free_segment): # real signature unknown; restored from __doc__
        """ free(array:list, free_segment:bool) -> int """
        return 0

    def free_to_bytes(self, array): # real signature unknown; restored from __doc__
        """ free_to_bytes(array:list) -> GLib.Bytes """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> list """
        return []

    def new_take(self, data): # real signature unknown; restored from __doc__
        """ new_take(data:list) -> list """
        return []

    def steal(self, array): # real signature unknown; restored from __doc__
        """ steal(array:list) -> int, len:int """
        return 0

    def unref(self, array): # real signature unknown; restored from __doc__
        """ unref(array:list) """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ByteArray), '__module__': 'gi.repository.GLib', '__gtype__': <GType GByteArray (94243598477680)>, '__dict__': <attribute '__dict__' of 'ByteArray' objects>, '__weakref__': <attribute '__weakref__' of 'ByteArray' objects>, '__doc__': None, 'data': <property object at 0x7f1d2b943e50>, 'len': <property object at 0x7f1d2b943ea0>, 'free': gi.FunctionInfo(free), 'free_to_bytes': gi.FunctionInfo(free_to_bytes), 'new': gi.FunctionInfo(new), 'new_take': gi.FunctionInfo(new_take), 'steal': gi.FunctionInfo(steal), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GByteArray (94243598477680)>'
    __info__ = StructInfo(ByteArray)


