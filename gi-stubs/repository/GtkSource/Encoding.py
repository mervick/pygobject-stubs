# encoding: utf-8
# module gi.repository.GtkSource
# from /usr/lib64/girepository-1.0/GtkSource-3.0.typelib
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


class Encoding(__gi.Boxed):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GtkSource.Encoding """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_all(self): # real signature unknown; restored from __doc__
        """ get_all() -> list """
        return []

    def get_charset(self): # real signature unknown; restored from __doc__
        """ get_charset(self) -> str """
        return ""

    def get_current(self): # real signature unknown; restored from __doc__
        """ get_current() -> GtkSource.Encoding """
        pass

    def get_default_candidates(self): # real signature unknown; restored from __doc__
        """ get_default_candidates() -> list """
        return []

    def get_from_charset(self, charset): # real signature unknown; restored from __doc__
        """ get_from_charset(charset:str) -> GtkSource.Encoding or None """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_utf8(self): # real signature unknown; restored from __doc__
        """ get_utf8() -> GtkSource.Encoding """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Encoding), '__module__': 'gi.repository.GtkSource', '__gtype__': <GType GtkSourceEncoding (94260244251424)>, '__dict__': <attribute '__dict__' of 'Encoding' objects>, '__weakref__': <attribute '__weakref__' of 'Encoding' objects>, '__doc__': None, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_charset': gi.FunctionInfo(get_charset), 'get_name': gi.FunctionInfo(get_name), 'to_string': gi.FunctionInfo(to_string), 'get_all': gi.FunctionInfo(get_all), 'get_current': gi.FunctionInfo(get_current), 'get_default_candidates': gi.FunctionInfo(get_default_candidates), 'get_from_charset': gi.FunctionInfo(get_from_charset), 'get_utf8': gi.FunctionInfo(get_utf8)})"
    __gtype__ = None # (!) real value is '<GType GtkSourceEncoding (94260244251424)>'
    __info__ = StructInfo(Encoding)


