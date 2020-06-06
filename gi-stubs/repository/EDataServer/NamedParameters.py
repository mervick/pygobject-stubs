# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


class NamedParameters(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> EDataServer.NamedParameters
        new_string(str:str) -> EDataServer.NamedParameters
        new_strv(strv:str) -> EDataServer.NamedParameters
    """
    def assign(self, from_=None): # real signature unknown; restored from __doc__
        """ assign(self, from_:EDataServer.NamedParameters=None) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def exists(self, name): # real signature unknown; restored from __doc__
        """ exists(self, name:str) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self, name): # real signature unknown; restored from __doc__
        """ get(self, name:str) -> str """
        return ""

    def get_name(self, index): # real signature unknown; restored from __doc__
        """ get_name(self, index:int) -> str """
        return ""

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> EDataServer.NamedParameters """
        pass

    def new_clone(self): # real signature unknown; restored from __doc__
        """ new_clone(self) -> EDataServer.NamedParameters """
        pass

    def new_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_string(str:str) -> EDataServer.NamedParameters """
        pass

    def new_strv(self, strv): # real signature unknown; restored from __doc__
        """ new_strv(strv:str) -> EDataServer.NamedParameters """
        pass

    def set(self, name, value=None): # real signature unknown; restored from __doc__
        """ set(self, name:str, value:str=None) """
        pass

    def test(self, name, value, case_sensitively): # real signature unknown; restored from __doc__
        """ test(self, name:str, value:str, case_sensitively:bool) -> bool """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def to_strv(self): # real signature unknown; restored from __doc__
        """ to_strv(self) -> list """
        return []

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
        """ new() -> EDataServer.NamedParameters """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NamedParameters), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ENamedParameters (94877536991424)>, '__dict__': <attribute '__dict__' of 'NamedParameters' objects>, '__weakref__': <attribute '__weakref__' of 'NamedParameters' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_string': gi.FunctionInfo(new_string), 'new_strv': gi.FunctionInfo(new_strv), 'assign': gi.FunctionInfo(assign), 'clear': gi.FunctionInfo(clear), 'count': gi.FunctionInfo(count), 'exists': gi.FunctionInfo(exists), 'free': gi.FunctionInfo(free), 'get': gi.FunctionInfo(get), 'get_name': gi.FunctionInfo(get_name), 'new_clone': gi.FunctionInfo(new_clone), 'set': gi.FunctionInfo(set), 'test': gi.FunctionInfo(test), 'to_string': gi.FunctionInfo(to_string), 'to_strv': gi.FunctionInfo(to_strv), '__new__': <staticmethod object at 0x7f6271be30a0>, '__init__': <function nothing at 0x7f6271e70ee0>})"
    __gtype__ = None # (!) real value is '<GType ENamedParameters (94877536991424)>'
    __info__ = StructInfo(NamedParameters)


