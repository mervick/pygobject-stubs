# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class URL(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        URL()
        new(url_string:str) -> Camel.URL
    """
    def addrspec_end(self, in_, pos, inend, match): # real signature unknown; restored from __doc__
        """ addrspec_end(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
        return False

    def addrspec_start(self, in_, pos, inend, match): # real signature unknown; restored from __doc__
        """ addrspec_start(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Camel.URL """
        pass

    def decode(self, part): # real signature unknown; restored from __doc__
        """ decode(part:str) """
        pass

    def decode_path(self, path): # real signature unknown; restored from __doc__
        """ decode_path(path:str) -> str """
        return ""

    def encode(self, part, escape_extra): # real signature unknown; restored from __doc__
        """ encode(part:str, escape_extra:str) -> str """
        return ""

    def equal(self, u2): # real signature unknown; restored from __doc__
        """ equal(self, u2:Camel.URL) -> bool """
        return False

    def file_end(self, in_, pos, inend, match): # real signature unknown; restored from __doc__
        """ file_end(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
        return False

    def file_start(self, in_, pos, inend, match): # real signature unknown; restored from __doc__
        """ file_start(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_param(self, name): # real signature unknown; restored from __doc__
        """ get_param(self, name:str) -> str """
        return ""

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def new(self, url_string): # real signature unknown; restored from __doc__
        """ new(url_string:str) -> Camel.URL """
        pass

    def new_with_base(self, url_string): # real signature unknown; restored from __doc__
        """ new_with_base(self, url_string:str) -> Camel.URL """
        pass

    def set_authmech(self, authmech): # real signature unknown; restored from __doc__
        """ set_authmech(self, authmech:str) """
        pass

    def set_fragment(self, fragment): # real signature unknown; restored from __doc__
        """ set_fragment(self, fragment:str) """
        pass

    def set_host(self, host): # real signature unknown; restored from __doc__
        """ set_host(self, host:str) """
        pass

    def set_param(self, name, value): # real signature unknown; restored from __doc__
        """ set_param(self, name:str, value:str) """
        pass

    def set_path(self, path): # real signature unknown; restored from __doc__
        """ set_path(self, path:str) """
        pass

    def set_port(self, port): # real signature unknown; restored from __doc__
        """ set_port(self, port:int) """
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ set_protocol(self, protocol:str) """
        pass

    def set_query(self, query): # real signature unknown; restored from __doc__
        """ set_query(self, query:str) """
        pass

    def set_user(self, user): # real signature unknown; restored from __doc__
        """ set_user(self, user:str) """
        pass

    def to_string(self, flags): # real signature unknown; restored from __doc__
        """ to_string(self, flags:Camel.URLFlags) -> str """
        return ""

    def web_end(self, in_, pos, inend, match): # real signature unknown; restored from __doc__
        """ web_end(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
        return False

    def web_start(self, in_, pos, inend, match): # real signature unknown; restored from __doc__
        """ web_start(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
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

    authmech = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fragment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    params = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(URL), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelURL (94124524398352)>, '__dict__': <attribute '__dict__' of 'URL' objects>, '__weakref__': <attribute '__weakref__' of 'URL' objects>, '__doc__': None, 'protocol': <property object at 0x7f7b34ef55e0>, 'user': <property object at 0x7f7b34ef56d0>, 'authmech': <property object at 0x7f7b34ef57c0>, 'host': <property object at 0x7f7b34ef58b0>, 'port': <property object at 0x7f7b34ef59a0>, 'path': <property object at 0x7f7b34ef5a90>, 'params': <property object at 0x7f7b34ef5b80>, 'query': <property object at 0x7f7b34ef5c70>, 'fragment': <property object at 0x7f7b34ef5d60>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_param': gi.FunctionInfo(get_param), 'hash': gi.FunctionInfo(hash), 'new_with_base': gi.FunctionInfo(new_with_base), 'set_authmech': gi.FunctionInfo(set_authmech), 'set_fragment': gi.FunctionInfo(set_fragment), 'set_host': gi.FunctionInfo(set_host), 'set_param': gi.FunctionInfo(set_param), 'set_path': gi.FunctionInfo(set_path), 'set_port': gi.FunctionInfo(set_port), 'set_protocol': gi.FunctionInfo(set_protocol), 'set_query': gi.FunctionInfo(set_query), 'set_user': gi.FunctionInfo(set_user), 'to_string': gi.FunctionInfo(to_string), 'addrspec_end': gi.FunctionInfo(addrspec_end), 'addrspec_start': gi.FunctionInfo(addrspec_start), 'decode': gi.FunctionInfo(decode), 'decode_path': gi.FunctionInfo(decode_path), 'encode': gi.FunctionInfo(encode), 'file_end': gi.FunctionInfo(file_end), 'file_start': gi.FunctionInfo(file_start), 'web_end': gi.FunctionInfo(web_end), 'web_start': gi.FunctionInfo(web_start)})"
    __gtype__ = None # (!) real value is '<GType CamelURL (94124524398352)>'
    __info__ = StructInfo(URL)


