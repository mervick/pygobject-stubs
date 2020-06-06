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


class Cookie(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Cookie()
        new(name:str, value:str, domain:str, path:str, max_age:int) -> Soup.Cookie
    """
    def applies_to_uri(self, uri): # real signature unknown; restored from __doc__
        """ applies_to_uri(self, uri:Soup.URI) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Soup.Cookie """
        pass

    def domain_matches(self, host): # real signature unknown; restored from __doc__
        """ domain_matches(self, host:str) -> bool """
        return False

    def equal(self, cookie2): # real signature unknown; restored from __doc__
        """ equal(self, cookie2:Soup.Cookie) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_domain(self): # real signature unknown; restored from __doc__
        """ get_domain(self) -> str """
        return ""

    def get_expires(self): # real signature unknown; restored from __doc__
        """ get_expires(self) -> Soup.Date or None """
        pass

    def get_http_only(self): # real signature unknown; restored from __doc__
        """ get_http_only(self) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str """
        return ""

    def get_same_site_policy(self): # real signature unknown; restored from __doc__
        """ get_same_site_policy(self) -> Soup.SameSitePolicy """
        pass

    def get_secure(self): # real signature unknown; restored from __doc__
        """ get_secure(self) -> bool """
        return False

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) -> str """
        return ""

    def new(self, name, value, domain, path, max_age): # real signature unknown; restored from __doc__
        """ new(name:str, value:str, domain:str, path:str, max_age:int) -> Soup.Cookie """
        pass

    def parse(self, header, origin): # real signature unknown; restored from __doc__
        """ parse(header:str, origin:Soup.URI) -> Soup.Cookie or None """
        pass

    def set_domain(self, domain): # real signature unknown; restored from __doc__
        """ set_domain(self, domain:str) """
        pass

    def set_expires(self, expires): # real signature unknown; restored from __doc__
        """ set_expires(self, expires:Soup.Date) """
        pass

    def set_http_only(self, http_only): # real signature unknown; restored from __doc__
        """ set_http_only(self, http_only:bool) """
        pass

    def set_max_age(self, max_age): # real signature unknown; restored from __doc__
        """ set_max_age(self, max_age:int) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_path(self, path): # real signature unknown; restored from __doc__
        """ set_path(self, path:str) """
        pass

    def set_same_site_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_same_site_policy(self, policy:Soup.SameSitePolicy) """
        pass

    def set_secure(self, secure): # real signature unknown; restored from __doc__
        """ set_secure(self, secure:bool) """
        pass

    def set_value(self, value): # real signature unknown; restored from __doc__
        """ set_value(self, value:str) """
        pass

    def to_cookie_header(self): # real signature unknown; restored from __doc__
        """ to_cookie_header(self) -> str """
        return ""

    def to_set_cookie_header(self): # real signature unknown; restored from __doc__
        """ to_set_cookie_header(self) -> str """
        return ""

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

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    http_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    secure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Cookie), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupCookie (94750594729184)>, '__dict__': <attribute '__dict__' of 'Cookie' objects>, '__weakref__': <attribute '__weakref__' of 'Cookie' objects>, '__doc__': None, 'name': <property object at 0x7f8e48614b30>, 'value': <property object at 0x7f8e48614c20>, 'domain': <property object at 0x7f8e48614d10>, 'path': <property object at 0x7f8e48614e00>, 'expires': <property object at 0x7f8e48614ef0>, 'secure': <property object at 0x7f8e48615040>, 'http_only': <property object at 0x7f8e48615130>, 'new': gi.FunctionInfo(new), 'applies_to_uri': gi.FunctionInfo(applies_to_uri), 'copy': gi.FunctionInfo(copy), 'domain_matches': gi.FunctionInfo(domain_matches), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_domain': gi.FunctionInfo(get_domain), 'get_expires': gi.FunctionInfo(get_expires), 'get_http_only': gi.FunctionInfo(get_http_only), 'get_name': gi.FunctionInfo(get_name), 'get_path': gi.FunctionInfo(get_path), 'get_same_site_policy': gi.FunctionInfo(get_same_site_policy), 'get_secure': gi.FunctionInfo(get_secure), 'get_value': gi.FunctionInfo(get_value), 'set_domain': gi.FunctionInfo(set_domain), 'set_expires': gi.FunctionInfo(set_expires), 'set_http_only': gi.FunctionInfo(set_http_only), 'set_max_age': gi.FunctionInfo(set_max_age), 'set_name': gi.FunctionInfo(set_name), 'set_path': gi.FunctionInfo(set_path), 'set_same_site_policy': gi.FunctionInfo(set_same_site_policy), 'set_secure': gi.FunctionInfo(set_secure), 'set_value': gi.FunctionInfo(set_value), 'to_cookie_header': gi.FunctionInfo(to_cookie_header), 'to_set_cookie_header': gi.FunctionInfo(to_set_cookie_header), 'parse': gi.FunctionInfo(parse)})"
    __gtype__ = None # (!) real value is '<GType SoupCookie (94750594729184)>'
    __info__ = StructInfo(Cookie)


