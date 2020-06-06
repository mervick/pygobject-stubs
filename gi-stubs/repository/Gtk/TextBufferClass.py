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


class TextBufferClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TextBufferClass()
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

    apply_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    begin_user_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_user_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_child_anchor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_pixbuf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mark_deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mark_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modified_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    paste_done = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextBufferClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TextBufferClass' objects>, '__weakref__': <attribute '__weakref__' of 'TextBufferClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fc63a6a3090>, 'insert_text': <property object at 0x7fc63a6a3180>, 'insert_pixbuf': <property object at 0x7fc63a6a3270>, 'insert_child_anchor': <property object at 0x7fc63a6a33b0>, 'delete_range': <property object at 0x7fc63a6a3450>, 'changed': <property object at 0x7fc63a6a3540>, 'modified_changed': <property object at 0x7fc63a6a3680>, 'mark_set': <property object at 0x7fc63a6a3770>, 'mark_deleted': <property object at 0x7fc63a6a3860>, 'apply_tag': <property object at 0x7fc63a6a3950>, 'remove_tag': <property object at 0x7fc63a6a3a40>, 'begin_user_action': <property object at 0x7fc63a6a3b80>, 'end_user_action': <property object at 0x7fc63a6a3c20>, 'paste_done': <property object at 0x7fc63a6a3d10>, '_gtk_reserved1': <property object at 0x7fc63a6a3e00>, '_gtk_reserved2': <property object at 0x7fc63a6a3ef0>, '_gtk_reserved3': <property object at 0x7fc63a6a4040>, '_gtk_reserved4': <property object at 0x7fc63a6a4130>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TextBufferClass)


