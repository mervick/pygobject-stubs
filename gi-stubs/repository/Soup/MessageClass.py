# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class MessageClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MessageClass()
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

    finished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    got_body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    got_chunk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    got_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    got_informational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    restarted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    starting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrote_body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrote_chunk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrote_headers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrote_informational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _libsoup_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _libsoup_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _libsoup_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MessageClass), '__module__': 'gi.repository.Soup', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MessageClass' objects>, '__weakref__': <attribute '__weakref__' of 'MessageClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f8e47ee1ae0>, 'wrote_informational': <property object at 0x7f8e47ee1c20>, 'wrote_headers': <property object at 0x7f8e47ee1cc0>, 'wrote_chunk': <property object at 0x7f8e47ee1db0>, 'wrote_body': <property object at 0x7f8e47ee1ea0>, 'got_informational': <property object at 0x7f8e47ee4040>, 'got_headers': <property object at 0x7f8e47ee40e0>, 'got_chunk': <property object at 0x7f8e47ee41d0>, 'got_body': <property object at 0x7f8e47ee42c0>, 'restarted': <property object at 0x7f8e47ee43b0>, 'finished': <property object at 0x7f8e47ee44a0>, 'starting': <property object at 0x7f8e47ee4590>, '_libsoup_reserved1': <property object at 0x7f8e47ee46d0>, '_libsoup_reserved2': <property object at 0x7f8e47ee47c0>, '_libsoup_reserved3': <property object at 0x7f8e47ee48b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MessageClass)


