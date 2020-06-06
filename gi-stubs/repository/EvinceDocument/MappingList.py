# encoding: utf-8
# module gi.repository.EvinceDocument
# from /usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib
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


class MappingList(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(page:int, list:list, data_destroy_func:GLib.DestroyNotify) -> EvinceDocument.MappingList
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, data=None): # real signature unknown; restored from __doc__
        """ find(self, data=None) -> EvinceDocument.Mapping """
        pass

    def find_custom(self, data=None, func): # real signature unknown; restored from __doc__
        """ find_custom(self, data=None, func:GLib.CompareFunc) -> EvinceDocument.Mapping """
        pass

    def get(self, x, y): # real signature unknown; restored from __doc__
        """ get(self, x:float, y:float) -> EvinceDocument.Mapping """
        pass

    def get_data(self, x, y): # real signature unknown; restored from __doc__
        """ get_data(self, x:float, y:float) """
        pass

    def get_list(self): # real signature unknown; restored from __doc__
        """ get_list(self) -> list """
        return []

    def get_page(self): # real signature unknown; restored from __doc__
        """ get_page(self) -> int """
        return 0

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def new(self, page, p_list, data_destroy_func): # real signature unknown; restored from __doc__
        """ new(page:int, list:list, data_destroy_func:GLib.DestroyNotify) -> EvinceDocument.MappingList """
        pass

    def nth(self, n): # real signature unknown; restored from __doc__
        """ nth(self, n:int) -> EvinceDocument.Mapping """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> EvinceDocument.MappingList """
        pass

    def remove(self, mapping): # real signature unknown; restored from __doc__
        """ remove(self, mapping:EvinceDocument.Mapping) """
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
        """ new(page:int, list:list, data_destroy_func:GLib.DestroyNotify) -> EvinceDocument.MappingList """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MappingList), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType EvMappingList (94742334221520)>, '__dict__': <attribute '__dict__' of 'MappingList' objects>, '__weakref__': <attribute '__weakref__' of 'MappingList' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'find': gi.FunctionInfo(find), 'find_custom': gi.FunctionInfo(find_custom), 'get': gi.FunctionInfo(get), 'get_data': gi.FunctionInfo(get_data), 'get_list': gi.FunctionInfo(get_list), 'get_page': gi.FunctionInfo(get_page), 'length': gi.FunctionInfo(length), 'nth': gi.FunctionInfo(nth), 'ref': gi.FunctionInfo(ref), 'remove': gi.FunctionInfo(remove), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7f6ab1678190>, '__init__': <function nothing at 0x7f6ab2a89ee0>})"
    __gtype__ = None # (!) real value is '<GType EvMappingList (94742334221520)>'
    __info__ = StructInfo(MappingList)


