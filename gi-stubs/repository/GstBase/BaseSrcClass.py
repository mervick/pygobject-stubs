# encoding: utf-8
# module gi.repository.GstBase
# from /usr/lib64/girepository-1.0/GstBase-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gobject as __gobject


class BaseSrcClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BaseSrcClass()
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

    alloc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    decide_allocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    do_seek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fixate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_times = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_seekable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    negotiate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prepare_seek_segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unlock_stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BaseSrcClass), '__module__': 'gi.repository.GstBase', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BaseSrcClass' objects>, '__weakref__': <attribute '__weakref__' of 'BaseSrcClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f9fb7bc2e00>, 'get_caps': <property object at 0x7f9fb7bc2ef0>, 'negotiate': <property object at 0x7f9fb7bc4040>, 'fixate': <property object at 0x7f9fb7bc4130>, 'set_caps': <property object at 0x7f9fb7bc4220>, 'decide_allocation': <property object at 0x7f9fb7bc4360>, 'start': <property object at 0x7f9fb7bc4400>, 'stop': <property object at 0x7f9fb7bc44f0>, 'get_times': <property object at 0x7f9fb7bc45e0>, 'get_size': <property object at 0x7f9fb7bc46d0>, 'is_seekable': <property object at 0x7f9fb7bc47c0>, 'prepare_seek_segment': <property object at 0x7f9fb7bc4900>, 'do_seek': <property object at 0x7f9fb7bc49f0>, 'unlock': <property object at 0x7f9fb7bc4ae0>, 'unlock_stop': <property object at 0x7f9fb7bc4bd0>, 'query': <property object at 0x7f9fb7bc4cc0>, 'event': <property object at 0x7f9fb7bc4db0>, 'create': <property object at 0x7f9fb7bc4ea0>, 'alloc': <property object at 0x7f9fb7bc4f90>, 'fill': <property object at 0x7f9fb7bc50e0>, '_gst_reserved': <property object at 0x7f9fb7bc51d0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BaseSrcClass)


