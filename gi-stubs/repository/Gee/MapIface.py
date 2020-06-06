# encoding: utf-8
# module gi.repository.Gee
# from /usr/lib64/girepository-1.0/Gee-0.8.typelib
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
import gobject as __gobject


class MapIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MapIface()
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

    clear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_is_empty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_only_view = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_iterator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unset_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MapIface), '__module__': 'gi.repository.Gee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MapIface' objects>, '__weakref__': <attribute '__weakref__' of 'MapIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f6a87b581d0>, 'has_key': <property object at 0x7f6a87b582c0>, 'has': <property object at 0x7f6a87b583b0>, 'get': <property object at 0x7f6a87b584a0>, 'set': <property object at 0x7f6a87b58590>, 'unset': <property object at 0x7f6a87b58680>, 'clear': <property object at 0x7f6a87b58770>, 'map_iterator': <property object at 0x7f6a87b58860>, 'set_all': <property object at 0x7f6a87b58950>, 'unset_all': <property object at 0x7f6a87b58a40>, 'has_all': <property object at 0x7f6a87b58b30>, 'get_size': <property object at 0x7f6a87b58c20>, 'get_is_empty': <property object at 0x7f6a87b58d10>, 'get_read_only': <property object at 0x7f6a87b58e00>, 'get_keys': <property object at 0x7f6a87b58ef0>, 'get_values': <property object at 0x7f6a87b59040>, 'get_entries': <property object at 0x7f6a87b59130>, 'get_read_only_view': <property object at 0x7f6a87b59270>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MapIface)


