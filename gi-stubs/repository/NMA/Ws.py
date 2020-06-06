# encoding: utf-8
# module gi.repository.NMA
# from /usr/lib64/girepository-1.0/NMA-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class Ws(__gobject.GInterface):
    # no doc
    def add_to_size_group(self, group): # real signature unknown; restored from __doc__
        """ add_to_size_group(self, group:Gtk.SizeGroup) """
        pass

    def adhoc_compatible(self): # real signature unknown; restored from __doc__
        """ adhoc_compatible(self) -> bool """
        return False

    def fill_connection(self, connection): # real signature unknown; restored from __doc__
        """ fill_connection(self, connection:NM.Connection) """
        pass

    def hotspot_compatible(self): # real signature unknown; restored from __doc__
        """ hotspot_compatible(self) -> bool """
        return False

    def update_secrets(self, connection): # real signature unknown; restored from __doc__
        """ update_secrets(self, connection:NM.Connection) """
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """ validate(self) -> bool """
        return False

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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Ws), '__module__': 'gi.repository.NMA', '__gtype__': <GType NMAWs (94779697303360)>, '__dict__': <attribute '__dict__' of 'Ws' objects>, '__weakref__': <attribute '__weakref__' of 'Ws' objects>, '__doc__': None, '__gsignals__': {}, 'add_to_size_group': gi.FunctionInfo(add_to_size_group), 'adhoc_compatible': gi.FunctionInfo(adhoc_compatible), 'fill_connection': gi.FunctionInfo(fill_connection), 'hotspot_compatible': gi.FunctionInfo(hotspot_compatible), 'update_secrets': gi.FunctionInfo(update_secrets), 'validate': gi.FunctionInfo(validate)})"
    __gdoc__ = 'Interface NMAWs\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMAWs (94779697303360)>'
    __info__ = InterfaceInfo(Ws)


