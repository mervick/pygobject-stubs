# encoding: utf-8
# module gi.repository.EDataBook
# from /usr/lib64/girepository-1.0/EDataBook-1.2.typelib
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
import gi.repository.EBackend as __gi_repository_EBackend
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class BookMetaBackendInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        BookMetaBackendInfo()
        new(uid:str, revision:str=None, object:str=None, extra:str=None) -> EDataBook.BookMetaBackendInfo
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EDataBook.BookMetaBackendInfo """
        pass

    def free(self, ptr=None): # real signature unknown; restored from __doc__
        """ free(ptr=None) """
        pass

    def new(self, uid, revision=None, p_object=None, extra=None): # real signature unknown; restored from __doc__
        """ new(uid:str, revision:str=None, object:str=None, extra:str=None) -> EDataBook.BookMetaBackendInfo """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

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

    extra = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookMetaBackendInfo), '__module__': 'gi.repository.EDataBook', '__gtype__': <GType EBookMetaBackendInfo (94654337922080)>, '__dict__': <attribute '__dict__' of 'BookMetaBackendInfo' objects>, '__weakref__': <attribute '__weakref__' of 'BookMetaBackendInfo' objects>, '__doc__': None, 'uid': <property object at 0x7f09d41b8db0>, 'revision': <property object at 0x7f09d41b8ea0>, 'object': <property object at 0x7f09d41b8f90>, 'extra': <property object at 0x7f09d41b90e0>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free)})"
    __gtype__ = None # (!) real value is '<GType EBookMetaBackendInfo (94654337922080)>'
    __info__ = StructInfo(BookMetaBackendInfo)


