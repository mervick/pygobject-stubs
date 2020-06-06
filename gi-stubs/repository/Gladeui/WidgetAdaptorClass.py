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


class WidgetAdaptorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        WidgetAdaptorClass()
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

    action_activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    action_submenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_verify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_action_activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_get_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_set_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    child_verify_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    construct_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_editable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_eprop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deep_post_create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deprecated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deprecated_since_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deprecated_since_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_internal_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glade_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    post_create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    string_from_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    toplevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_placeholders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version_since_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version_since_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_widget_after = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WidgetAdaptorClass), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'WidgetAdaptorClass' objects>, '__weakref__': <attribute '__weakref__' of 'WidgetAdaptorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f1341776130>, 'version_since_major': <property object at 0x7f1341776270>, 'version_since_minor': <property object at 0x7f13417763b0>, 'default_width': <property object at 0x7f13417764a0>, 'default_height': <property object at 0x7f1341776590>, 'deprecated': <property object at 0x7f1341776680>, 'toplevel': <property object at 0x7f1341776770>, 'use_placeholders': <property object at 0x7f13417768b0>, 'create_widget': <property object at 0x7f13417769a0>, 'construct_object': <property object at 0x7f1341776ae0>, 'deep_post_create': <property object at 0x7f1341776bd0>, 'post_create': <property object at 0x7f1341776cc0>, 'get_internal_child': <property object at 0x7f1341776e00>, 'verify_property': <property object at 0x7f1341776ea0>, 'set_property': <property object at 0x7f1341776f90>, 'get_property': <property object at 0x7f13417770e0>, 'add_verify': <property object at 0x7f13417771d0>, 'add': <property object at 0x7f13417772c0>, 'remove': <property object at 0x7f13417773b0>, 'get_children': <property object at 0x7f13417774a0>, 'child_verify_property': <property object at 0x7f13417775e0>, 'child_set_property': <property object at 0x7f13417776d0>, 'child_get_property': <property object at 0x7f13417777c0>, 'replace_child': <property object at 0x7f1341777860>, 'action_activate': <property object at 0x7f1341777950>, 'child_action_activate': <property object at 0x7f1341777a90>, 'action_submenu': <property object at 0x7f1341777b30>, 'depends': <property object at 0x7f1341777c20>, 'read_widget': <property object at 0x7f1341777d10>, 'write_widget': <property object at 0x7f1341777e00>, 'read_child': <property object at 0x7f1341777ef0>, 'write_child': <property object at 0x7f1341778040>, 'create_eprop': <property object at 0x7f1341778130>, 'string_from_value': <property object at 0x7f1341778270>, 'create_editable': <property object at 0x7f1341778310>, 'destroy_object': <property object at 0x7f1341778400>, 'write_widget_after': <property object at 0x7f1341778540>, 'deprecated_since_major': <property object at 0x7f1341778630>, 'deprecated_since_minor': <property object at 0x7f1341778770>, 'glade_reserved1': <property object at 0x7f1341778860>, 'glade_reserved2': <property object at 0x7f1341778950>, 'glade_reserved3': <property object at 0x7f1341778a40>, 'glade_reserved4': <property object at 0x7f1341778b30>, 'glade_reserved5': <property object at 0x7f1341778c20>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(WidgetAdaptorClass)


