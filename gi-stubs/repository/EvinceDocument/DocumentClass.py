# encoding: utf-8
# module gi.repository.EvinceDocument
# from /usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib
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


class DocumentClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DocumentClass()
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

    base_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_backend_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_pages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_page = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_page_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_page_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_thumbnail_surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load_gfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    load_stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    save = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    support_synctex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DocumentClass), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DocumentClass' objects>, '__weakref__': <attribute '__weakref__' of 'DocumentClass' objects>, '__doc__': None, 'base_class': <property object at 0x7f6ab1654950>, 'load': <property object at 0x7f6ab1654a40>, 'save': <property object at 0x7f6ab1654b30>, 'get_n_pages': <property object at 0x7f6ab1654c20>, 'get_page': <property object at 0x7f6ab1654d10>, 'get_page_size': <property object at 0x7f6ab1654e00>, 'get_page_label': <property object at 0x7f6ab1654ef0>, 'render': <property object at 0x7f6ab1655040>, 'get_thumbnail': <property object at 0x7f6ab1655130>, 'get_info': <property object at 0x7f6ab1655220>, 'get_backend_info': <property object at 0x7f6ab1655360>, 'support_synctex': <property object at 0x7f6ab1655400>, 'load_stream': <property object at 0x7f6ab16554f0>, 'load_gfile': <property object at 0x7f6ab16555e0>, 'get_thumbnail_surface': <property object at 0x7f6ab1655720>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DocumentClass)


