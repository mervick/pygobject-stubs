# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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


class PartIter(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(toplevel:GMime.Object) -> GMime.PartIter
    """
    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> GMime.PartIter """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_current(self): # real signature unknown; restored from __doc__
        """ get_current(self) -> GMime.Object """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> GMime.Object """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> GMime.Object """
        pass

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def jump_to(self, path): # real signature unknown; restored from __doc__
        """ jump_to(self, path:str) -> bool """
        return False

    def new(self, toplevel): # real signature unknown; restored from __doc__
        """ new(toplevel:GMime.Object) -> GMime.PartIter """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def prev(self): # real signature unknown; restored from __doc__
        """ prev(self) -> bool """
        return False

    def remove(self): # real signature unknown; restored from __doc__
        """ remove(self) -> bool """
        return False

    def replace(self, replacement): # real signature unknown; restored from __doc__
        """ replace(self, replacement:GMime.Object) -> bool """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
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
        """ new(toplevel:GMime.Object) -> GMime.PartIter """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PartIter), '__module__': 'gi.repository.GMime', '__gtype__': <GType GMimePartIter (94235496188736)>, '__dict__': <attribute '__dict__' of 'PartIter' objects>, '__weakref__': <attribute '__weakref__' of 'PartIter' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'clone': gi.FunctionInfo(clone), 'free': gi.FunctionInfo(free), 'get_current': gi.FunctionInfo(get_current), 'get_parent': gi.FunctionInfo(get_parent), 'get_path': gi.FunctionInfo(get_path), 'get_toplevel': gi.FunctionInfo(get_toplevel), 'is_valid': gi.FunctionInfo(is_valid), 'jump_to': gi.FunctionInfo(jump_to), 'next': gi.FunctionInfo(next), 'prev': gi.FunctionInfo(prev), 'remove': gi.FunctionInfo(remove), 'replace': gi.FunctionInfo(replace), 'reset': gi.FunctionInfo(reset), '__new__': <staticmethod object at 0x7fc970741ca0>, '__init__': <function nothing at 0x7fc970afcee0>})"
    __gtype__ = None # (!) real value is '<GType GMimePartIter (94235496188736)>'
    __info__ = StructInfo(PartIter)


