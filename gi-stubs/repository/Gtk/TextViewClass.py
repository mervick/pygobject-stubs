# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
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


class TextViewClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TextViewClass()
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

    backspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_clipboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cut_clipboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_from_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extend_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_at_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_emoji = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    paste_clipboard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    populate_popup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_anchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    toggle_overwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextViewClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TextViewClass' objects>, '__weakref__': <attribute '__weakref__' of 'TextViewClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fe830f98540>, 'populate_popup': <property object at 0x7fe830f98630>, 'move_cursor': <property object at 0x7fe830f98720>, 'set_anchor': <property object at 0x7fe830f98810>, 'insert_at_cursor': <property object at 0x7fe830f98950>, 'delete_from_cursor': <property object at 0x7fe830f98a40>, 'backspace': <property object at 0x7fe830f98ae0>, 'cut_clipboard': <property object at 0x7fe830f98bd0>, 'copy_clipboard': <property object at 0x7fe830f98cc0>, 'paste_clipboard': <property object at 0x7fe830f98db0>, 'toggle_overwrite': <property object at 0x7fe830f98ef0>, 'create_buffer': <property object at 0x7fe830f98f90>, 'draw_layer': <property object at 0x7fe830f990e0>, 'extend_selection': <property object at 0x7fe830f99220>, 'insert_emoji': <property object at 0x7fe830f99310>, '_gtk_reserved1': <property object at 0x7fe830f99400>, '_gtk_reserved2': <property object at 0x7fe830f994f0>, '_gtk_reserved3': <property object at 0x7fe830f995e0>, '_gtk_reserved4': <property object at 0x7fe830f996d0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TextViewClass)


