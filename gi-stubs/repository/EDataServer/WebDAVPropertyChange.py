# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


class WebDAVPropertyChange(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        WebDAVPropertyChange()
        new_remove(ns_uri:str, name:str) -> EDataServer.WebDAVPropertyChange
        new_set(ns_uri:str, name:str, value:str=None) -> EDataServer.WebDAVPropertyChange
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EDataServer.WebDAVPropertyChange """
        pass

    def free(self, ptr=None): # real signature unknown; restored from __doc__
        """ free(ptr=None) """
        pass

    def new_remove(self, ns_uri, name): # real signature unknown; restored from __doc__
        """ new_remove(ns_uri:str, name:str) -> EDataServer.WebDAVPropertyChange """
        pass

    def new_set(self, ns_uri, name, value=None): # real signature unknown; restored from __doc__
        """ new_set(ns_uri:str, name:str, value:str=None) -> EDataServer.WebDAVPropertyChange """
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

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ns_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WebDAVPropertyChange), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType EWebDAVPropertyChange (94877537390272)>, '__dict__': <attribute '__dict__' of 'WebDAVPropertyChange' objects>, '__weakref__': <attribute '__weakref__' of 'WebDAVPropertyChange' objects>, '__doc__': None, 'kind': <property object at 0x7f626e8d97c0>, 'ns_uri': <property object at 0x7f626e8d98b0>, 'name': <property object at 0x7f626e8d99a0>, 'value': <property object at 0x7f626e8d9a90>, 'new_remove': gi.FunctionInfo(new_remove), 'new_set': gi.FunctionInfo(new_set), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free)})"
    __gtype__ = None # (!) real value is '<GType EWebDAVPropertyChange (94877537390272)>'
    __info__ = StructInfo(WebDAVPropertyChange)


