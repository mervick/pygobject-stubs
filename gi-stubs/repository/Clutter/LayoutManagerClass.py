# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class LayoutManagerClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        LayoutManagerClass()
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

    allocate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    begin_animation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_child_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_animation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_animation_progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_meta_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layout_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _clutter_padding_8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(LayoutManagerClass), '__module__': 'gi.repository.Clutter', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'LayoutManagerClass' objects>, '__weakref__': <attribute '__weakref__' of 'LayoutManagerClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f5413515860>, 'get_preferred_width': <property object at 0x7f54135159a0>, 'get_preferred_height': <property object at 0x7f5413515a90>, 'allocate': <property object at 0x7f5413515b30>, 'set_container': <property object at 0x7f5413515c20>, 'get_child_meta_type': <property object at 0x7f5413515d60>, 'create_child_meta': <property object at 0x7f5413515ea0>, 'begin_animation': <property object at 0x7f5413515f40>, 'get_animation_progress': <property object at 0x7f54135180e0>, 'end_animation': <property object at 0x7f5413518180>, 'layout_changed': <property object at 0x7f5413518270>, '_clutter_padding_1': <property object at 0x7f54135183b0>, '_clutter_padding_2': <property object at 0x7f54135184f0>, '_clutter_padding_3': <property object at 0x7f5413518630>, '_clutter_padding_4': <property object at 0x7f5413518770>, '_clutter_padding_5': <property object at 0x7f54135188b0>, '_clutter_padding_6': <property object at 0x7f54135189f0>, '_clutter_padding_7': <property object at 0x7f5413518b30>, '_clutter_padding_8': <property object at 0x7f5413518c70>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(LayoutManagerClass)


