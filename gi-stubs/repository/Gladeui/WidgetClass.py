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


class WidgetClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        WidgetClass()
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

    add_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_signal_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button_press_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button_release_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    change_signal_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    motion_notify_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_signal_handler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WidgetClass), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'WidgetClass' objects>, '__weakref__': <attribute '__weakref__' of 'WidgetClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f1341778e00>, 'add_child': <property object at 0x7f1341778ef0>, 'remove_child': <property object at 0x7f134177a040>, 'replace_child': <property object at 0x7f134177a130>, 'add_signal_handler': <property object at 0x7f134177a270>, 'remove_signal_handler': <property object at 0x7f134177a360>, 'change_signal_handler': <property object at 0x7f134177a450>, 'button_press_event': <property object at 0x7f134177a540>, 'button_release_event': <property object at 0x7f134177a680>, 'motion_notify_event': <property object at 0x7f134177a7c0>, 'event': <property object at 0x7f134177a8b0>, 'glade_reserved1': <property object at 0x7f134177a9a0>, 'glade_reserved2': <property object at 0x7f134177aa90>, 'glade_reserved3': <property object at 0x7f134177ab80>, 'glade_reserved4': <property object at 0x7f134177ac70>, 'glade_reserved5': <property object at 0x7f134177ad60>, 'glade_reserved6': <property object at 0x7f134177ae50>, 'glade_reserved7': <property object at 0x7f134177af40>, 'glade_reserved8': <property object at 0x7f134177b090>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(WidgetClass)


