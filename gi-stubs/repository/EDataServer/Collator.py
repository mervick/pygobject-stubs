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


class Collator(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(locale:str) -> EDataServer.Collator
        new_interpret_country(locale:str) -> EDataServer.Collator, country_code:str
    """
    def collate(self, str_a=None, str_b=None): # real signature unknown; restored from __doc__
        """ collate(self, str_a:str=None, str_b:str=None) -> bool, result:int """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def generate_key(self, p_str): # real signature unknown; restored from __doc__
        """ generate_key(self, str:str) -> str """
        return ""

    def generate_key_for_index(self, index): # real signature unknown; restored from __doc__
        """ generate_key_for_index(self, index:int) -> str """
        return ""

    def get_index(self, p_str): # real signature unknown; restored from __doc__
        """ get_index(self, str:str) -> int """
        return 0

    def get_index_labels(self): # real signature unknown; restored from __doc__
        """ get_index_labels(self) -> list, n_labels:int, underflow:int, inflow:int, overflow:int """
        return []

    def new(self, locale): # real signature unknown; restored from __doc__
        """ new(locale:str) -> EDataServer.Collator """
        pass

    def new_interpret_country(self, locale): # real signature unknown; restored from __doc__
        """ new_interpret_country(locale:str) -> EDataServer.Collator, country_code:str """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> EDataServer.Collator """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
        """ new(locale:str) -> EDataServer.Collator """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Collator), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ECollator (94877536959808)>, '__dict__': <attribute '__dict__' of 'Collator' objects>, '__weakref__': <attribute '__weakref__' of 'Collator' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_interpret_country': gi.FunctionInfo(new_interpret_country), 'collate': gi.FunctionInfo(collate), 'generate_key': gi.FunctionInfo(generate_key), 'generate_key_for_index': gi.FunctionInfo(generate_key_for_index), 'get_index': gi.FunctionInfo(get_index), 'get_index_labels': gi.FunctionInfo(get_index_labels), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), 'error_quark': gi.FunctionInfo(error_quark), '__new__': <staticmethod object at 0x7f6271bd14f0>, '__init__': <function nothing at 0x7f6271e70ee0>})"
    __gtype__ = None # (!) real value is '<GType ECollator (94877536959808)>'
    __info__ = StructInfo(Collator)


