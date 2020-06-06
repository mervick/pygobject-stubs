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


class ShortcutChord(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_from_event(event:Gdk.EventKey) -> Dazzle.ShortcutChord
        new_from_string(accelerator:str) -> Dazzle.ShortcutChord
    """
    def append_event(self, event): # real signature unknown; restored from __doc__
        """ append_event(self, event:Gdk.EventKey) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Dazzle.ShortcutChord """
        pass

    def equal(self, data1=None, data2=None): # real signature unknown; restored from __doc__
        """ equal(data1=None, data2=None) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def get_nth_key(self, nth, keyval, modifier): # real signature unknown; restored from __doc__
        """ get_nth_key(self, nth:int, keyval:int, modifier:Gdk.ModifierType) """
        pass

    def hash(self, data=None): # real signature unknown; restored from __doc__
        """ hash(data=None) -> int """
        return 0

    def has_modifier(self): # real signature unknown; restored from __doc__
        """ has_modifier(self) -> bool """
        return False

    def match(self, other): # real signature unknown; restored from __doc__
        """ match(self, other:Dazzle.ShortcutChord) -> Dazzle.ShortcutMatch """
        pass

    def new_from_event(self, event): # real signature unknown; restored from __doc__
        """ new_from_event(event:Gdk.EventKey) -> Dazzle.ShortcutChord """
        pass

    def new_from_string(self, accelerator): # real signature unknown; restored from __doc__
        """ new_from_string(accelerator:str) -> Dazzle.ShortcutChord """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ShortcutChord), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType DzlShortcutChord (93962411488496)>, '__dict__': <attribute '__dict__' of 'ShortcutChord' objects>, '__weakref__': <attribute '__weakref__' of 'ShortcutChord' objects>, '__doc__': None, 'new_from_event': gi.FunctionInfo(new_from_event), 'new_from_string': gi.FunctionInfo(new_from_string), 'append_event': gi.FunctionInfo(append_event), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_label': gi.FunctionInfo(get_label), 'get_length': gi.FunctionInfo(get_length), 'get_nth_key': gi.FunctionInfo(get_nth_key), 'has_modifier': gi.FunctionInfo(has_modifier), 'match': gi.FunctionInfo(match), 'to_string': gi.FunctionInfo(to_string), 'equal': gi.FunctionInfo(equal), 'hash': gi.FunctionInfo(hash)})"
    __gtype__ = None # (!) real value is '<GType DzlShortcutChord (93962411488496)>'
    __info__ = StructInfo(ShortcutChord)


