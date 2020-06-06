# encoding: utf-8
# module gi.repository.Dazzle
# from /usr/lib64/girepository-1.0/Dazzle-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class ShortcutChordTable(__gi.Struct):
    # no doc
    def add(self, chord, data=None): # real signature unknown; restored from __doc__
        """ add(self, chord:Dazzle.ShortcutChord, data=None) """
        pass

    def foreach(self, foreach_func, foreach_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, foreach_func:Dazzle.ShortcutChordTableForeach, foreach_data=None) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def lookup(self, chord, data=None): # real signature unknown; restored from __doc__
        """ lookup(self, chord:Dazzle.ShortcutChord, data=None) -> Dazzle.ShortcutMatch """
        pass

    def lookup_data(self, data=None): # real signature unknown; restored from __doc__
        """ lookup_data(self, data=None) -> Dazzle.ShortcutChord """
        pass

    def printf(self): # real signature unknown; restored from __doc__
        """ printf(self) """
        pass

    def remove(self, chord): # real signature unknown; restored from __doc__
        """ remove(self, chord:Dazzle.ShortcutChord) -> bool """
        return False

    def remove_data(self, data=None): # real signature unknown; restored from __doc__
        """ remove_data(self, data=None) -> bool """
        return False

    def set_free_func(self, notify): # real signature unknown; restored from __doc__
        """ set_free_func(self, notify:GLib.DestroyNotify) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ShortcutChordTable), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ShortcutChordTable' objects>, '__weakref__': <attribute '__weakref__' of 'ShortcutChordTable' objects>, '__doc__': None, 'add': gi.FunctionInfo(add), 'foreach': gi.FunctionInfo(foreach), 'free': gi.FunctionInfo(free), 'lookup': gi.FunctionInfo(lookup), 'lookup_data': gi.FunctionInfo(lookup_data), 'printf': gi.FunctionInfo(printf), 'remove': gi.FunctionInfo(remove), 'remove_data': gi.FunctionInfo(remove_data), 'set_free_func': gi.FunctionInfo(set_free_func), 'size': gi.FunctionInfo(size)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ShortcutChordTable)


