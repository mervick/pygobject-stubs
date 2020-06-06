# encoding: utf-8
# module gi.repository.GUPnP
# from /usr/lib64/girepository-1.0/GUPnP-1.0.typelib
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
import gi.repository.GSSDP as __gi_repository_GSSDP
import gobject as __gobject


class ServiceAction(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_argument_count(self): # real signature unknown; restored from __doc__
        """ get_argument_count(self) -> int """
        return 0

    def get_locales(self): # real signature unknown; restored from __doc__
        """ get_locales(self) -> list """
        return []

    def get_message(self): # real signature unknown; restored from __doc__
        """ get_message(self) -> Soup.Message """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_value(self, argument, type): # real signature unknown; restored from __doc__
        """ get_value(self, argument:str, type:GType) -> GObject.Value """
        pass

    def get_values(self, arg_names, arg_types): # real signature unknown; restored from __doc__
        """ get_values(self, arg_names:list, arg_types:list) -> list """
        return []

    def return_(self): # real signature unknown; restored from __doc__
        """ return_(self) """
        pass

    def return_error(self, error_code, error_description): # real signature unknown; restored from __doc__
        """ return_error(self, error_code:int, error_description:str) """
        pass

    def set_value(self, argument, value): # real signature unknown; restored from __doc__
        """ set_value(self, argument:str, value:GObject.Value) """
        pass

    def set_values(self, arg_names, arg_values): # real signature unknown; restored from __doc__
        """ set_values(self, arg_names:list, arg_values:list) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ServiceAction), '__module__': 'gi.repository.GUPnP', '__gtype__': <GType GUPnPServiceAction (94417776008160)>, '__dict__': <attribute '__dict__' of 'ServiceAction' objects>, '__weakref__': <attribute '__weakref__' of 'ServiceAction' objects>, '__doc__': None, 'get_argument_count': gi.FunctionInfo(get_argument_count), 'get_value': gi.FunctionInfo(get_value), 'get_locales': gi.FunctionInfo(get_locales), 'get_message': gi.FunctionInfo(get_message), 'get_name': gi.FunctionInfo(get_name), 'get_values': gi.FunctionInfo(get_values), 'return_': gi.FunctionInfo(return), 'return_error': gi.FunctionInfo(return_error), 'set_value': gi.FunctionInfo(set_value), 'set_values': gi.FunctionInfo(set_values)})"
    __gtype__ = None # (!) real value is '<GType GUPnPServiceAction (94417776008160)>'
    __info__ = StructInfo(ServiceAction)


