# encoding: utf-8
# module gi.repository.EBookContacts
# from /usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
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
import gobject as __gobject


class VCardAttribute(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(attr_group:str=None, attr_name:str) -> EBookContacts.VCardAttribute
    """
    def add_param(self, param): # real signature unknown; restored from __doc__
        """ add_param(self, param:EBookContacts.VCardAttributeParam) """
        pass

    def add_param_with_value(self, param, value): # real signature unknown; restored from __doc__
        """ add_param_with_value(self, param:EBookContacts.VCardAttributeParam, value:str) """
        pass

    def add_value(self, value): # real signature unknown; restored from __doc__
        """ add_value(self, value:str) """
        pass

    def add_value_decoded(self, value, len): # real signature unknown; restored from __doc__
        """ add_value_decoded(self, value:str, len:int) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EBookContacts.VCardAttribute """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_group(self): # real signature unknown; restored from __doc__
        """ get_group(self) -> str or None """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_param(self, name): # real signature unknown; restored from __doc__
        """ get_param(self, name:str) -> list or None """
        return []

    def get_params(self): # real signature unknown; restored from __doc__
        """ get_params(self) -> list """
        return []

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) -> str or None """
        return ""

    def get_values(self): # real signature unknown; restored from __doc__
        """ get_values(self) -> list """
        return []

    def get_values_decoded(self): # real signature unknown; restored from __doc__
        """ get_values_decoded(self) -> list """
        return []

    def get_value_decoded(self): # real signature unknown; restored from __doc__
        """ get_value_decoded(self) -> GLib.String or None """
        pass

    def has_type(self, typestr): # real signature unknown; restored from __doc__
        """ has_type(self, typestr:str) -> bool """
        return False

    def is_single_valued(self): # real signature unknown; restored from __doc__
        """ is_single_valued(self) -> bool """
        return False

    def new(self, attr_group=None, attr_name): # real signature unknown; restored from __doc__
        """ new(attr_group:str=None, attr_name:str) -> EBookContacts.VCardAttribute """
        pass

    def remove_param(self, param_name): # real signature unknown; restored from __doc__
        """ remove_param(self, param_name:str) """
        pass

    def remove_params(self): # real signature unknown; restored from __doc__
        """ remove_params(self) """
        pass

    def remove_param_value(self, param_name, s): # real signature unknown; restored from __doc__
        """ remove_param_value(self, param_name:str, s:str) """
        pass

    def remove_value(self, s): # real signature unknown; restored from __doc__
        """ remove_value(self, s:str) """
        pass

    def remove_values(self): # real signature unknown; restored from __doc__
        """ remove_values(self) """
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
        """ new(attr_group:str=None, attr_name:str) -> EBookContacts.VCardAttribute """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VCardAttribute), '__module__': 'gi.repository.EBookContacts', '__gtype__': <GType EVCardAttribute (94769385636720)>, '__dict__': <attribute '__dict__' of 'VCardAttribute' objects>, '__weakref__': <attribute '__weakref__' of 'VCardAttribute' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'add_param': gi.FunctionInfo(add_param), 'add_param_with_value': gi.FunctionInfo(add_param_with_value), 'add_value': gi.FunctionInfo(add_value), 'add_value_decoded': gi.FunctionInfo(add_value_decoded), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_group': gi.FunctionInfo(get_group), 'get_name': gi.FunctionInfo(get_name), 'get_param': gi.FunctionInfo(get_param), 'get_params': gi.FunctionInfo(get_params), 'get_value': gi.FunctionInfo(get_value), 'get_value_decoded': gi.FunctionInfo(get_value_decoded), 'get_values': gi.FunctionInfo(get_values), 'get_values_decoded': gi.FunctionInfo(get_values_decoded), 'has_type': gi.FunctionInfo(has_type), 'is_single_valued': gi.FunctionInfo(is_single_valued), 'remove_param': gi.FunctionInfo(remove_param), 'remove_param_value': gi.FunctionInfo(remove_param_value), 'remove_params': gi.FunctionInfo(remove_params), 'remove_value': gi.FunctionInfo(remove_value), 'remove_values': gi.FunctionInfo(remove_values), '__new__': <staticmethod object at 0x7f7148847670>, '__init__': <function nothing at 0x7f714bde4ee0>})"
    __gtype__ = None # (!) real value is '<GType EVCardAttribute (94769385636720)>'
    __info__ = StructInfo(VCardAttribute)


