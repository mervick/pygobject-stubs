# encoding: utf-8
# module gi.repository.Wnck
# from /usr/lib64/girepository-1.0/Wnck-3.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class ScreenClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ScreenClass()
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

    active_window_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    active_workspace_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    application_closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    application_opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    background_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    class_group_closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    class_group_opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    showing_desktop_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    viewports_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_manager_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_stacking_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    workspace_created = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    workspace_destroyed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ScreenClass), '__module__': 'gi.repository.Wnck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ScreenClass' objects>, '__weakref__': <attribute '__weakref__' of 'ScreenClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f75c322b4f0>, 'active_window_changed': <property object at 0x7f75c322b630>, 'active_workspace_changed': <property object at 0x7f75c322b770>, 'window_stacking_changed': <property object at 0x7f75c322b8b0>, 'window_opened': <property object at 0x7f75c322b9a0>, 'window_closed': <property object at 0x7f75c322ba90>, 'workspace_created': <property object at 0x7f75c322bbd0>, 'workspace_destroyed': <property object at 0x7f75c322bd10>, 'application_opened': <property object at 0x7f75c322be50>, 'application_closed': <property object at 0x7f75c322bf90>, 'background_changed': <property object at 0x7f75c322d130>, 'class_group_opened': <property object at 0x7f75c322d270>, 'class_group_closed': <property object at 0x7f75c322d3b0>, 'showing_desktop_changed': <property object at 0x7f75c322d4f0>, 'viewports_changed': <property object at 0x7f75c322d630>, 'window_manager_changed': <property object at 0x7f75c322d770>, 'pad2': <property object at 0x7f75c322d860>, 'pad3': <property object at 0x7f75c322d950>, 'pad4': <property object at 0x7f75c322da40>, 'pad5': <property object at 0x7f75c322db30>, 'pad6': <property object at 0x7f75c322dc20>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ScreenClass)


