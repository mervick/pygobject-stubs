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


class WebDAVResource(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        WebDAVResource()
        new(kind:EDataServer.WebDAVResourceKind, supports:int, href:str, etag:str=None, display_name:str=None, content_type:str=None, content_length:int, creation_date:int, last_modified:int, description:str=None, color:str=None) -> EDataServer.WebDAVResource
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EDataServer.WebDAVResource """
        pass

    def free(self, ptr=None): # real signature unknown; restored from __doc__
        """ free(ptr=None) """
        pass

    def new(self, kind, supports, href, etag=None, display_name=None, content_type=None, content_length, creation_date, last_modified, description=None, color=None): # real signature unknown; restored from __doc__
        """ new(kind:EDataServer.WebDAVResourceKind, supports:int, href:str, etag:str=None, display_name:str=None, content_type:str=None, content_length:int, creation_date:int, last_modified:int, description:str=None, color:str=None) -> EDataServer.WebDAVResource """
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

    color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    creation_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    etag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    href = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WebDAVResource), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType EWebDAVResource (94877537393840)>, '__dict__': <attribute '__dict__' of 'WebDAVResource' objects>, '__weakref__': <attribute '__weakref__' of 'WebDAVResource' objects>, '__doc__': None, 'kind': <property object at 0x7f626e8d9e00>, 'supports': <property object at 0x7f626e8d9ef0>, 'href': <property object at 0x7f626e8dc040>, 'etag': <property object at 0x7f626e8dc130>, 'display_name': <property object at 0x7f626e8dc220>, 'content_type': <property object at 0x7f626e8dc310>, 'content_length': <property object at 0x7f626e8dc400>, 'creation_date': <property object at 0x7f626e8dc4f0>, 'last_modified': <property object at 0x7f626e8dc5e0>, 'description': <property object at 0x7f626e8dc6d0>, 'color': <property object at 0x7f626e8dc7c0>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free)})"
    __gtype__ = None # (!) real value is '<GType EWebDAVResource (94877537393840)>'
    __info__ = StructInfo(WebDAVResource)


