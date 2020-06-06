# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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


class StreamClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        StreamClass()
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

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    substream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StreamClass), '__module__': 'gi.repository.GMime', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'StreamClass' objects>, '__weakref__': <attribute '__weakref__' of 'StreamClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fc9707554a0>, 'read': <property object at 0x7fc970755590>, 'write': <property object at 0x7fc970755680>, 'flush': <property object at 0x7fc970755770>, 'close': <property object at 0x7fc970755860>, 'eos': <property object at 0x7fc970755950>, 'reset': <property object at 0x7fc970755a40>, 'seek': <property object at 0x7fc970755b30>, 'tell': <property object at 0x7fc970755c20>, 'length': <property object at 0x7fc970755d10>, 'substream': <property object at 0x7fc970755e00>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(StreamClass)


