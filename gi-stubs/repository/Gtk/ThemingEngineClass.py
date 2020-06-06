# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class ThemingEngineClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ThemingEngineClass()
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

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_activity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_arrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_background = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_expander = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_frame_gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_icon_pixbuf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_icon_surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_slider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ThemingEngineClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ThemingEngineClass' objects>, '__weakref__': <attribute '__weakref__' of 'ThemingEngineClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fc63a6b1b80>, 'render_line': <property object at 0x7fc63a6b1c70>, 'render_background': <property object at 0x7fc63a6b1db0>, 'render_frame': <property object at 0x7fc63a6b1ea0>, 'render_frame_gap': <property object at 0x7fc63a634040>, 'render_extension': <property object at 0x7fc63a634180>, 'render_check': <property object at 0x7fc63a634270>, 'render_option': <property object at 0x7fc63a634360>, 'render_arrow': <property object at 0x7fc63a634450>, 'render_expander': <property object at 0x7fc63a634540>, 'render_focus': <property object at 0x7fc63a634630>, 'render_layout': <property object at 0x7fc63a634720>, 'render_slider': <property object at 0x7fc63a634810>, 'render_handle': <property object at 0x7fc63a634900>, 'render_activity': <property object at 0x7fc63a6349f0>, 'render_icon_pixbuf': <property object at 0x7fc63a634b30>, 'render_icon': <property object at 0x7fc63a634bd0>, 'render_icon_surface': <property object at 0x7fc63a634d10>, 'padding': <property object at 0x7fc63a634db0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ThemingEngineClass)


