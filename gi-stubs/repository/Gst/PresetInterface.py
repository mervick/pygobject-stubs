# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class PresetInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PresetInterface()
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

    delete_preset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preset_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_property_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load_preset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rename_preset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    save_preset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PresetInterface), '__module__': 'gi.repository.Gst', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PresetInterface' objects>, '__weakref__': <attribute '__weakref__' of 'PresetInterface' objects>, '__doc__': None, 'parent': <property object at 0x7f4260508540>, 'get_preset_names': <property object at 0x7f4260508680>, 'get_property_names': <property object at 0x7f4260508770>, 'load_preset': <property object at 0x7f4260508810>, 'save_preset': <property object at 0x7f4260508900>, 'rename_preset': <property object at 0x7f42605089f0>, 'delete_preset': <property object at 0x7f4260508ae0>, 'set_meta': <property object at 0x7f4260508bd0>, 'get_meta': <property object at 0x7f4260508cc0>, '_gst_reserved': <property object at 0x7f4260508db0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PresetInterface)


