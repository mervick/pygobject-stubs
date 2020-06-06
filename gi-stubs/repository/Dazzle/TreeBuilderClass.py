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


class TreeBuilderClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TreeBuilderClass()
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

    added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cell_data_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_data_get = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_data_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_node_delete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drag_node_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_activated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_collapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_draggable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_droppable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_expanded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_popup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    node_unselected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TreeBuilderClass), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TreeBuilderClass' objects>, '__weakref__': <attribute '__weakref__' of 'TreeBuilderClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f3b25ef7270>, 'added': <property object at 0x7f3b25ef7360>, 'removed': <property object at 0x7f3b25ef7450>, 'build_node': <property object at 0x7f3b25ef7540>, 'build_children': <property object at 0x7f3b25ef7630>, 'node_activated': <property object at 0x7f3b25ef7720>, 'node_selected': <property object at 0x7f3b25ef7810>, 'node_unselected': <property object at 0x7f3b25ef7900>, 'node_popup': <property object at 0x7f3b25ef79f0>, 'node_expanded': <property object at 0x7f3b25ef7ae0>, 'node_collapsed': <property object at 0x7f3b25ef7bd0>, 'node_draggable': <property object at 0x7f3b25ef7cc0>, 'node_droppable': <property object at 0x7f3b25ef7db0>, 'drag_data_get': <property object at 0x7f3b25ef7ea0>, 'drag_node_received': <property object at 0x7f3b25ef8040>, 'drag_data_received': <property object at 0x7f3b25ef8180>, 'drag_node_delete': <property object at 0x7f3b25ef8270>, 'cell_data_func': <property object at 0x7f3b25ef8360>, '_padding': <property object at 0x7f3b25ef8450>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TreeBuilderClass)


