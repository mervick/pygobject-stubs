# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class NamedFlags(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Camel.NamedFlags
        new_sized(reserve_size:int) -> Camel.NamedFlags
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, name): # real signature unknown; restored from __doc__
        """ contains(self, name:str) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Camel.NamedFlags """
        pass

    def equal(self, named_flags_b=None): # real signature unknown; restored from __doc__
        """ equal(self, named_flags_b:Camel.NamedFlags=None) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self, index): # real signature unknown; restored from __doc__
        """ get(self, index:int) -> str or None """
        return ""

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def insert(self, name): # real signature unknown; restored from __doc__
        """ insert(self, name:str) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Camel.NamedFlags """
        pass

    def new_sized(self, reserve_size): # real signature unknown; restored from __doc__
        """ new_sized(reserve_size:int) -> Camel.NamedFlags """
        pass

    def remove(self, name): # real signature unknown; restored from __doc__
        """ remove(self, name:str) -> bool """
        return False

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
        """ new() -> Camel.NamedFlags """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NamedFlags), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelNamedFlags (94124523736416)>, '__dict__': <attribute '__dict__' of 'NamedFlags' objects>, '__weakref__': <attribute '__weakref__' of 'NamedFlags' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_sized': gi.FunctionInfo(new_sized), 'clear': gi.FunctionInfo(clear), 'contains': gi.FunctionInfo(contains), 'copy': gi.FunctionInfo(copy), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get': gi.FunctionInfo(get), 'get_length': gi.FunctionInfo(get_length), 'insert': gi.FunctionInfo(insert), 'remove': gi.FunctionInfo(remove), '__new__': <staticmethod object at 0x7f7b34f9c970>, '__init__': <function nothing at 0x7f7b37797ee0>})"
    __gtype__ = None # (!) real value is '<GType CamelNamedFlags (94124523736416)>'
    __info__ = StructInfo(NamedFlags)


