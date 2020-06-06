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


class ResourceUsage(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ResourceUsage()
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

    n_colormap_entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_cursors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_fonts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_gcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_glyphsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_other = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_passive_grabs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_pictures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_pixmaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_windows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixmap_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_bytes_estimate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ResourceUsage), '__module__': 'gi.repository.Wnck', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ResourceUsage' objects>, '__weakref__': <attribute '__weakref__' of 'ResourceUsage' objects>, '__doc__': None, 'total_bytes_estimate': <property object at 0x7f75c3226450>, 'pixmap_bytes': <property object at 0x7f75c3226540>, 'n_pixmaps': <property object at 0x7f75c3226630>, 'n_windows': <property object at 0x7f75c3226720>, 'n_gcs': <property object at 0x7f75c3226810>, 'n_pictures': <property object at 0x7f75c3226900>, 'n_glyphsets': <property object at 0x7f75c32269f0>, 'n_fonts': <property object at 0x7f75c3226ae0>, 'n_colormap_entries': <property object at 0x7f75c3226c20>, 'n_passive_grabs': <property object at 0x7f75c3226d10>, 'n_cursors': <property object at 0x7f75c3226e00>, 'n_other': <property object at 0x7f75c3226ef0>, 'pad1': <property object at 0x7f75c3229040>, 'pad2': <property object at 0x7f75c3229130>, 'pad3': <property object at 0x7f75c3229220>, 'pad4': <property object at 0x7f75c3229310>, 'pad5': <property object at 0x7f75c3229400>, 'pad6': <property object at 0x7f75c32294f0>, 'pad7': <property object at 0x7f75c32295e0>, 'pad8': <property object at 0x7f75c32296d0>, 'pad9': <property object at 0x7f75c32297c0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ResourceUsage)


