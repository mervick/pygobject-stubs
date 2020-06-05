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


class TreeModelIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TreeModelIface()
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

    get_column_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_iter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iter_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iter_has_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iter_next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iter_nth_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iter_n_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iter_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iter_previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rows_reordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_has_child_toggled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_inserted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unref_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TreeModelIface), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TreeModelIface' objects>, '__weakref__': <attribute '__weakref__' of 'TreeModelIface' objects>, '__doc__': None, 'g_iface': <property object at 0x7fe830f2fef0>, 'row_changed': <property object at 0x7fe830f31040>, 'row_inserted': <property object at 0x7fe830f31130>, 'row_has_child_toggled': <property object at 0x7fe830f31270>, 'row_deleted': <property object at 0x7fe830f31310>, 'rows_reordered': <property object at 0x7fe830f31400>, 'get_flags': <property object at 0x7fe830f314f0>, 'get_n_columns': <property object at 0x7fe830f315e0>, 'get_column_type': <property object at 0x7fe830f316d0>, 'get_iter': <property object at 0x7fe830f317c0>, 'get_path': <property object at 0x7fe830f318b0>, 'get_value': <property object at 0x7fe830f319a0>, 'iter_next': <property object at 0x7fe830f31a90>, 'iter_previous': <property object at 0x7fe830f31b80>, 'iter_children': <property object at 0x7fe830f31c70>, 'iter_has_child': <property object at 0x7fe830f31d60>, 'iter_n_children': <property object at 0x7fe830f31e50>, 'iter_nth_child': <property object at 0x7fe830f31f40>, 'iter_parent': <property object at 0x7fe830f32090>, 'ref_node': <property object at 0x7fe830f32180>, 'unref_node': <property object at 0x7fe830f32270>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TreeModelIface)


