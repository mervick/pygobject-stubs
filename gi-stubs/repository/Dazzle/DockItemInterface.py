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


class DockItemInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DockItemInterface()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    can_minimize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_can_close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_icon_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_manager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    manager_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minimize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    needs_attention = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    presented = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    present_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_gicon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    release = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_child_visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_manager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    update_visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DockItemInterface), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DockItemInterface' objects>, '__weakref__': <attribute '__weakref__' of 'DockItemInterface' objects>, '__doc__': None, 'parent': <property object at 0x7f3b2608c360>, 'set_manager': <property object at 0x7f3b2608c450>, 'get_manager': <property object at 0x7f3b2608c540>, 'manager_set': <property object at 0x7f3b2608c630>, 'present_child': <property object at 0x7f3b2608c720>, 'update_visibility': <property object at 0x7f3b2608c860>, 'get_child_visible': <property object at 0x7f3b2608c950>, 'set_child_visible': <property object at 0x7f3b2608ca40>, 'get_title': <property object at 0x7f3b2608cae0>, 'get_icon_name': <property object at 0x7f3b2608cbd0>, 'get_can_close': <property object at 0x7f3b2608ccc0>, 'can_minimize': <property object at 0x7f3b2608cdb0>, 'close': <property object at 0x7f3b2608cea0>, 'minimize': <property object at 0x7f3b2608cf90>, 'release': <property object at 0x7f3b2608d0e0>, 'presented': <property object at 0x7f3b2608d1d0>, 'ref_gicon': <property object at 0x7f3b2608d2c0>, 'needs_attention': <property object at 0x7f3b2608d3b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DockItemInterface)


