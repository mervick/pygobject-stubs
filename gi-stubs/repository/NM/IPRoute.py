# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


class IPRoute(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(family:int, dest:str, prefix:int, next_hop:str=None, metric:int) -> NM.IPRoute
        new_binary(family:int, dest=None, prefix:int, next_hop=None, metric:int) -> NM.IPRoute
    """
    def attribute_validate(self, name, value, family): # real signature unknown; restored from __doc__
        """ attribute_validate(name:str, value:GLib.Variant, family:int) -> bool, known:bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> NM.IPRoute """
        pass

    def equal(self, other): # real signature unknown; restored from __doc__
        """ equal(self, other:NM.IPRoute) -> bool """
        return False

    def equal_full(self, other, cmp_flags): # real signature unknown; restored from __doc__
        """ equal_full(self, other:NM.IPRoute, cmp_flags:int) -> bool """
        return False

    def get_attribute(self, name): # real signature unknown; restored from __doc__
        """ get_attribute(self, name:str) -> GLib.Variant """
        pass

    def get_attribute_names(self): # real signature unknown; restored from __doc__
        """ get_attribute_names(self) -> list """
        return []

    def get_dest(self): # real signature unknown; restored from __doc__
        """ get_dest(self) -> str """
        return ""

    def get_family(self): # real signature unknown; restored from __doc__
        """ get_family(self) -> int """
        return 0

    def get_metric(self): # real signature unknown; restored from __doc__
        """ get_metric(self) -> int """
        return 0

    def get_next_hop(self): # real signature unknown; restored from __doc__
        """ get_next_hop(self) -> str """
        return ""

    def get_prefix(self): # real signature unknown; restored from __doc__
        """ get_prefix(self) -> int """
        return 0

    def get_variant_attribute_spec(self): # real signature unknown; restored from __doc__
        """ get_variant_attribute_spec() -> NM.VariantAttributeSpec """
        pass

    def new(self, family, dest, prefix, next_hop=None, metric): # real signature unknown; restored from __doc__
        """ new(family:int, dest:str, prefix:int, next_hop:str=None, metric:int) -> NM.IPRoute """
        pass

    def new_binary(self, family, dest=None, prefix, next_hop=None, metric): # real signature unknown; restored from __doc__
        """ new_binary(family:int, dest=None, prefix:int, next_hop=None, metric:int) -> NM.IPRoute """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) """
        pass

    def set_attribute(self, name, value=None): # real signature unknown; restored from __doc__
        """ set_attribute(self, name:str, value:GLib.Variant=None) """
        pass

    def set_dest(self, dest): # real signature unknown; restored from __doc__
        """ set_dest(self, dest:str) """
        pass

    def set_metric(self, metric): # real signature unknown; restored from __doc__
        """ set_metric(self, metric:int) """
        pass

    def set_next_hop(self, next_hop=None): # real signature unknown; restored from __doc__
        """ set_next_hop(self, next_hop:str=None) """
        pass

    def set_prefix(self, prefix): # real signature unknown; restored from __doc__
        """ set_prefix(self, prefix:int) """
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
        """ new(family:int, dest:str, prefix:int, next_hop:str=None, metric:int) -> NM.IPRoute """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IPRoute), '__module__': 'gi.repository.NM', '__gtype__': <GType NMIPRoute (94741104320496)>, '__dict__': <attribute '__dict__' of 'IPRoute' objects>, '__weakref__': <attribute '__weakref__' of 'IPRoute' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_binary': gi.FunctionInfo(new_binary), 'dup': gi.FunctionInfo(dup), 'equal': gi.FunctionInfo(equal), 'equal_full': gi.FunctionInfo(equal_full), 'get_attribute': gi.FunctionInfo(get_attribute), 'get_attribute_names': gi.FunctionInfo(get_attribute_names), 'get_dest': gi.FunctionInfo(get_dest), 'get_family': gi.FunctionInfo(get_family), 'get_metric': gi.FunctionInfo(get_metric), 'get_next_hop': gi.FunctionInfo(get_next_hop), 'get_prefix': gi.FunctionInfo(get_prefix), 'ref': gi.FunctionInfo(ref), 'set_attribute': gi.FunctionInfo(set_attribute), 'set_dest': gi.FunctionInfo(set_dest), 'set_metric': gi.FunctionInfo(set_metric), 'set_next_hop': gi.FunctionInfo(set_next_hop), 'set_prefix': gi.FunctionInfo(set_prefix), 'unref': gi.FunctionInfo(unref), 'attribute_validate': gi.FunctionInfo(attribute_validate), 'get_variant_attribute_spec': gi.FunctionInfo(get_variant_attribute_spec), '__new__': <staticmethod object at 0x7fb9b8cb73d0>, '__init__': <function nothing at 0x7fb9b8f70ee0>})"
    __gtype__ = None # (!) real value is '<GType NMIPRoute (94741104320496)>'
    __info__ = StructInfo(IPRoute)


