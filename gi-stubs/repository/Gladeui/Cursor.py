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


class Cursor(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Cursor()
    """
    def get_add_widget_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_add_widget_pixbuf() -> GdkPixbuf.Pixbuf """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init() """
        pass

    def set(self, project, window, type): # real signature unknown; restored from __doc__
        """ set(project:Gladeui.Project, window:Gdk.Window, type:Gladeui.CursorType) """
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

    add_widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_widget_pixbuf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_bottom_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_bottom_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_top_left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resize_top_right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Cursor), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Cursor' objects>, '__weakref__': <attribute '__weakref__' of 'Cursor' objects>, '__doc__': None, 'selector': <property object at 0x7f1341a2cae0>, 'add_widget': <property object at 0x7f1341a2cbd0>, 'resize_top_left': <property object at 0x7f1341a2ccc0>, 'resize_top_right': <property object at 0x7f1341a2ce00>, 'resize_bottom_left': <property object at 0x7f1341a2cf40>, 'resize_bottom_right': <property object at 0x7f1341a2e0e0>, 'resize_left': <property object at 0x7f1341a2e1d0>, 'resize_right': <property object at 0x7f1341a2e2c0>, 'resize_top': <property object at 0x7f1341a2e3b0>, 'resize_bottom': <property object at 0x7f1341a2e4a0>, 'drag': <property object at 0x7f1341a2e590>, 'add_widget_pixbuf': <property object at 0x7f1341a2e6d0>, 'get_add_widget_pixbuf': gi.FunctionInfo(get_add_widget_pixbuf), 'init': gi.FunctionInfo(init), 'set': gi.FunctionInfo(set)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Cursor)


