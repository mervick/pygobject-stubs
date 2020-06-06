# encoding: utf-8
# module gi.repository.Grl
# from /usr/lib64/girepository-1.0/Grl-0.3.typelib
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


class SourceClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        SourceClass()
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

    browse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    may_resolve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    media_from_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify_change_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify_change_stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resolve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    search = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    slow_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    store = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    store_metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supported_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supported_operations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    test_media_from_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    writable_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _grl_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SourceClass), '__module__': 'gi.repository.Grl', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'SourceClass' objects>, '__weakref__': <attribute '__weakref__' of 'SourceClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fa0403c02c0>, 'supported_operations': <property object at 0x7fa0403c0400>, 'supported_keys': <property object at 0x7fa0403c04a0>, 'slow_keys': <property object at 0x7fa0403c0590>, 'writable_keys': <property object at 0x7fa0403c0680>, 'get_caps': <property object at 0x7fa0403c0770>, 'resolve': <property object at 0x7fa0403c0860>, 'may_resolve': <property object at 0x7fa0403c0950>, 'test_media_from_uri': <property object at 0x7fa0403c0a90>, 'media_from_uri': <property object at 0x7fa0403c0b30>, 'browse': <property object at 0x7fa0403c0c20>, 'search': <property object at 0x7fa0403c0d10>, 'query': <property object at 0x7fa0403c0e00>, 'remove': <property object at 0x7fa0403c0ef0>, 'store': <property object at 0x7fa0403c1040>, 'store_metadata': <property object at 0x7fa0403c1130>, 'cancel': <property object at 0x7fa0403c1220>, 'notify_change_start': <property object at 0x7fa0403c1360>, 'notify_change_stop': <property object at 0x7fa0403c1450>, '_grl_reserved': <property object at 0x7fa0403c14f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(SourceClass)


