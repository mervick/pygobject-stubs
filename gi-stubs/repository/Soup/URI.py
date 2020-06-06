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


class URI(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        URI()
        new(uri_string:str=None) -> Soup.URI or None
        new_with_base(base:Soup.URI, uri_string:str) -> Soup.URI
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Soup.URI """
        pass

    def copy_host(self): # real signature unknown; restored from __doc__
        """ copy_host(self) -> Soup.URI """
        pass

    def decode(self, part): # real signature unknown; restored from __doc__
        """ decode(part:str) -> str """
        return ""

    def encode(self, part, escape_extra=None): # real signature unknown; restored from __doc__
        """ encode(part:str, escape_extra:str=None) -> str """
        return ""

    def equal(self, uri2): # real signature unknown; restored from __doc__
        """ equal(self, uri2:Soup.URI) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_fragment(self): # real signature unknown; restored from __doc__
        """ get_fragment(self) -> str """
        return ""

    def get_host(self): # real signature unknown; restored from __doc__
        """ get_host(self) -> str """
        return ""

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> int """
        return 0

    def get_query(self): # real signature unknown; restored from __doc__
        """ get_query(self) -> str """
        return ""

    def get_scheme(self): # real signature unknown; restored from __doc__
        """ get_scheme(self) -> str """
        return ""

    def get_user(self): # real signature unknown; restored from __doc__
        """ get_user(self) -> str """
        return ""

    def host_equal(self, v2): # real signature unknown; restored from __doc__
        """ host_equal(self, v2:Soup.URI) -> bool """
        return False

    def host_hash(self): # real signature unknown; restored from __doc__
        """ host_hash(self) -> int """
        return 0

    def new(self, uri_string=None): # real signature unknown; restored from __doc__
        """ new(uri_string:str=None) -> Soup.URI or None """
        pass

    def new_with_base(self, base, uri_string): # real signature unknown; restored from __doc__
        """ new_with_base(base:Soup.URI, uri_string:str) -> Soup.URI """
        pass

    def normalize(self, part, unescape_extra=None): # real signature unknown; restored from __doc__
        """ normalize(part:str, unescape_extra:str=None) -> str """
        return ""

    def set_fragment(self, fragment=None): # real signature unknown; restored from __doc__
        """ set_fragment(self, fragment:str=None) """
        pass

    def set_host(self, host=None): # real signature unknown; restored from __doc__
        """ set_host(self, host:str=None) """
        pass

    def set_password(self, password=None): # real signature unknown; restored from __doc__
        """ set_password(self, password:str=None) """
        pass

    def set_path(self, path): # real signature unknown; restored from __doc__
        """ set_path(self, path:str) """
        pass

    def set_port(self, port): # real signature unknown; restored from __doc__
        """ set_port(self, port:int) """
        pass

    def set_query(self, query=None): # real signature unknown; restored from __doc__
        """ set_query(self, query:str=None) """
        pass

    def set_query_from_form(self, form): # real signature unknown; restored from __doc__
        """ set_query_from_form(self, form:dict) """
        pass

    def set_scheme(self, scheme): # real signature unknown; restored from __doc__
        """ set_scheme(self, scheme:str) """
        pass

    def set_user(self, user=None): # real signature unknown; restored from __doc__
        """ set_user(self, user:str=None) """
        pass

    def to_string(self, just_path_and_query): # real signature unknown; restored from __doc__
        """ to_string(self, just_path_and_query:bool) -> str """
        return ""

    def uses_default_port(self): # real signature unknown; restored from __doc__
        """ uses_default_port(self) -> bool """
        return False

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

    fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(URI), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupURI (94750594964848)>, '__dict__': <attribute '__dict__' of 'URI' objects>, '__weakref__': <attribute '__weakref__' of 'URI' objects>, '__doc__': None, 'scheme': <property object at 0x7f8e47f03310>, 'user': <property object at 0x7f8e47f03400>, 'password': <property object at 0x7f8e47f034f0>, 'host': <property object at 0x7f8e47f035e0>, 'port': <property object at 0x7f8e47f036d0>, 'path': <property object at 0x7f8e47f037c0>, 'query': <property object at 0x7f8e47f038b0>, 'fragment': <property object at 0x7f8e47f039a0>, 'new': gi.FunctionInfo(new), 'new_with_base': gi.FunctionInfo(new_with_base), 'copy': gi.FunctionInfo(copy), 'copy_host': gi.FunctionInfo(copy_host), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_fragment': gi.FunctionInfo(get_fragment), 'get_host': gi.FunctionInfo(get_host), 'get_password': gi.FunctionInfo(get_password), 'get_path': gi.FunctionInfo(get_path), 'get_port': gi.FunctionInfo(get_port), 'get_query': gi.FunctionInfo(get_query), 'get_scheme': gi.FunctionInfo(get_scheme), 'get_user': gi.FunctionInfo(get_user), 'host_equal': gi.FunctionInfo(host_equal), 'host_hash': gi.FunctionInfo(host_hash), 'set_fragment': gi.FunctionInfo(set_fragment), 'set_host': gi.FunctionInfo(set_host), 'set_password': gi.FunctionInfo(set_password), 'set_path': gi.FunctionInfo(set_path), 'set_port': gi.FunctionInfo(set_port), 'set_query': gi.FunctionInfo(set_query), 'set_query_from_form': gi.FunctionInfo(set_query_from_form), 'set_scheme': gi.FunctionInfo(set_scheme), 'set_user': gi.FunctionInfo(set_user), 'to_string': gi.FunctionInfo(to_string), 'uses_default_port': gi.FunctionInfo(uses_default_port), 'decode': gi.FunctionInfo(decode), 'encode': gi.FunctionInfo(encode), 'normalize': gi.FunctionInfo(normalize)})"
    __gtype__ = None # (!) real value is '<GType SoupURI (94750594964848)>'
    __info__ = StructInfo(URI)


