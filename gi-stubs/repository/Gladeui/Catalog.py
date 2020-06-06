# encoding: utf-8
# module gi.repository.Gladeui
# from /usr/lib64/girepository-1.0/Gladeui-2.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class Catalog(__gi.Struct):
    # no doc
    def add_path(self, path): # real signature unknown; restored from __doc__
        """ add_path(path:str) """
        pass

    def destroy_all(self): # real signature unknown; restored from __doc__
        """ destroy_all() """
        pass

    def get_adaptors(self): # real signature unknown; restored from __doc__
        """ get_adaptors(self) -> list """
        return []

    def get_book(self): # real signature unknown; restored from __doc__
        """ get_book(self) -> str """
        return ""

    def get_domain(self): # real signature unknown; restored from __doc__
        """ get_domain(self) -> str """
        return ""

    def get_extra_paths(self): # real signature unknown; restored from __doc__
        """ get_extra_paths() -> list """
        return []

    def get_icon_prefix(self): # real signature unknown; restored from __doc__
        """ get_icon_prefix(self) -> str """
        return ""

    def get_major_version(self): # real signature unknown; restored from __doc__
        """ get_major_version(self) -> int """
        return 0

    def get_minor_version(self): # real signature unknown; restored from __doc__
        """ get_minor_version(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_prefix(self): # real signature unknown; restored from __doc__
        """ get_prefix(self) -> str """
        return ""

    def get_targets(self): # real signature unknown; restored from __doc__
        """ get_targets(self) -> list """
        return []

    def get_widget_groups(self): # real signature unknown; restored from __doc__
        """ get_widget_groups(self) -> list """
        return []

    def is_loaded(self, name): # real signature unknown; restored from __doc__
        """ is_loaded(name:str) -> bool """
        return False

    def load_all(self): # real signature unknown; restored from __doc__
        """ load_all() -> list """
        return []

    def remove_path(self, path=None): # real signature unknown; restored from __doc__
        """ remove_path(path:str=None) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Catalog), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Catalog' objects>, '__weakref__': <attribute '__weakref__' of 'Catalog' objects>, '__doc__': None, 'get_adaptors': gi.FunctionInfo(get_adaptors), 'get_book': gi.FunctionInfo(get_book), 'get_domain': gi.FunctionInfo(get_domain), 'get_icon_prefix': gi.FunctionInfo(get_icon_prefix), 'get_major_version': gi.FunctionInfo(get_major_version), 'get_minor_version': gi.FunctionInfo(get_minor_version), 'get_name': gi.FunctionInfo(get_name), 'get_prefix': gi.FunctionInfo(get_prefix), 'get_targets': gi.FunctionInfo(get_targets), 'get_widget_groups': gi.FunctionInfo(get_widget_groups), 'add_path': gi.FunctionInfo(add_path), 'destroy_all': gi.FunctionInfo(destroy_all), 'get_extra_paths': gi.FunctionInfo(get_extra_paths), 'is_loaded': gi.FunctionInfo(is_loaded), 'load_all': gi.FunctionInfo(load_all), 'remove_path': gi.FunctionInfo(remove_path)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Catalog)


