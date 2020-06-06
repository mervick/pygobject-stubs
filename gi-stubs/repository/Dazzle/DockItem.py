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


class DockItem(__gobject.GInterface):
    # no doc
    def adopt(self, child): # real signature unknown; restored from __doc__
        """ adopt(self, child:Dazzle.DockItem) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> bool """
        return False

    def emit_presented(self): # real signature unknown; restored from __doc__
        """ emit_presented(self) """
        pass

    def get_can_close(self): # real signature unknown; restored from __doc__
        """ get_can_close(self) -> bool """
        return False

    def get_can_minimize(self): # real signature unknown; restored from __doc__
        """ get_can_minimize(self) -> bool """
        return False

    def get_child_visible(self, child): # real signature unknown; restored from __doc__
        """ get_child_visible(self, child:Dazzle.DockItem) -> bool """
        return False

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str or None """
        return ""

    def get_manager(self): # real signature unknown; restored from __doc__
        """ get_manager(self) -> Dazzle.DockManager or None """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Dazzle.DockItem or None """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str or None """
        return ""

    def has_widgets(self): # real signature unknown; restored from __doc__
        """ has_widgets(self) -> bool """
        return False

    def minimize(self, child, position): # real signature unknown; restored from __doc__
        """ minimize(self, child:Dazzle.DockItem, position:Gtk.PositionType) -> bool, position:Gtk.PositionType """
        return False

    def needs_attention(self): # real signature unknown; restored from __doc__
        """ needs_attention(self) """
        pass

    def present(self): # real signature unknown; restored from __doc__
        """ present(self) """
        pass

    def present_child(self, child): # real signature unknown; restored from __doc__
        """ present_child(self, child:Dazzle.DockItem) """
        pass

    def ref_gicon(self): # real signature unknown; restored from __doc__
        """ ref_gicon(self) -> Gio.Icon or None """
        pass

    def release(self, child): # real signature unknown; restored from __doc__
        """ release(self, child:Dazzle.DockItem) """
        pass

    def set_child_visible(self, child, child_visible): # real signature unknown; restored from __doc__
        """ set_child_visible(self, child:Dazzle.DockItem, child_visible:bool) """
        pass

    def set_manager(self, manager=None): # real signature unknown; restored from __doc__
        """ set_manager(self, manager:Dazzle.DockManager=None) """
        pass

    def update_visibility(self): # real signature unknown; restored from __doc__
        """ update_visibility(self) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(DockItem), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType DzlDockItem (93962411361392)>, '__dict__': <attribute '__dict__' of 'DockItem' objects>, '__weakref__': <attribute '__weakref__' of 'DockItem' objects>, '__doc__': None, '__gsignals__': {}, 'adopt': gi.FunctionInfo(adopt), 'close': gi.FunctionInfo(close), 'emit_presented': gi.FunctionInfo(emit_presented), 'get_can_close': gi.FunctionInfo(get_can_close), 'get_can_minimize': gi.FunctionInfo(get_can_minimize), 'get_child_visible': gi.FunctionInfo(get_child_visible), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_manager': gi.FunctionInfo(get_manager), 'get_parent': gi.FunctionInfo(get_parent), 'get_title': gi.FunctionInfo(get_title), 'has_widgets': gi.FunctionInfo(has_widgets), 'minimize': gi.FunctionInfo(minimize), 'needs_attention': gi.FunctionInfo(needs_attention), 'present': gi.FunctionInfo(present), 'present_child': gi.FunctionInfo(present_child), 'ref_gicon': gi.FunctionInfo(ref_gicon), 'release': gi.FunctionInfo(release), 'set_child_visible': gi.FunctionInfo(set_child_visible), 'set_manager': gi.FunctionInfo(set_manager), 'update_visibility': gi.FunctionInfo(update_visibility)})"
    __gdoc__ = 'Interface DzlDockItem\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DzlDockItem (93962411361392)>'
    __info__ = InterfaceInfo(DockItem)


