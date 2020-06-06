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


class MultiMapIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MultiMapIface()
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

    contains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_all_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_only_view = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_iterator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MultiMapIface), '__module__': 'gi.repository.Gee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MultiMapIface' objects>, '__weakref__': <attribute '__weakref__' of 'MultiMapIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f6a87b5b130>, 'get_keys': <property object at 0x7f6a87b5b220>, 'get_all_keys': <property object at 0x7f6a87b5b310>, 'get_values': <property object at 0x7f6a87b5b400>, 'contains': <property object at 0x7f6a87b5b4f0>, 'get': <property object at 0x7f6a87b5b5e0>, 'set': <property object at 0x7f6a87b5b6d0>, 'remove': <property object at 0x7f6a87b5b7c0>, 'remove_all': <property object at 0x7f6a87b5b8b0>, 'clear': <property object at 0x7f6a87b5b9a0>, 'map_iterator': <property object at 0x7f6a87b5ba90>, 'get_size': <property object at 0x7f6a87b5bb80>, 'get_read_only': <property object at 0x7f6a87b5bc70>, 'get_read_only_view': <property object at 0x7f6a87b5bdb0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MultiMapIface)


