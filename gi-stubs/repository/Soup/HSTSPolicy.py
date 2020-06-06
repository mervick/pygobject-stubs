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


class HSTSPolicy(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        HSTSPolicy()
        new(domain:str, max_age:int, include_subdomains:bool) -> Soup.HSTSPolicy
        new_from_response(msg:Soup.Message) -> Soup.HSTSPolicy or None
        new_full(domain:str, max_age:int, expires:Soup.Date, include_subdomains:bool) -> Soup.HSTSPolicy
        new_session_policy(domain:str, include_subdomains:bool) -> Soup.HSTSPolicy
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Soup.HSTSPolicy """
        pass

    def equal(self, policy2): # real signature unknown; restored from __doc__
        """ equal(self, policy2:Soup.HSTSPolicy) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_domain(self): # real signature unknown; restored from __doc__
        """ get_domain(self) -> str """
        return ""

    def includes_subdomains(self): # real signature unknown; restored from __doc__
        """ includes_subdomains(self) -> bool """
        return False

    def is_expired(self): # real signature unknown; restored from __doc__
        """ is_expired(self) -> bool """
        return False

    def is_session_policy(self): # real signature unknown; restored from __doc__
        """ is_session_policy(self) -> bool """
        return False

    def new(self, domain, max_age, include_subdomains): # real signature unknown; restored from __doc__
        """ new(domain:str, max_age:int, include_subdomains:bool) -> Soup.HSTSPolicy """
        pass

    def new_from_response(self, msg): # real signature unknown; restored from __doc__
        """ new_from_response(msg:Soup.Message) -> Soup.HSTSPolicy or None """
        pass

    def new_full(self, domain, max_age, expires, include_subdomains): # real signature unknown; restored from __doc__
        """ new_full(domain:str, max_age:int, expires:Soup.Date, include_subdomains:bool) -> Soup.HSTSPolicy """
        pass

    def new_session_policy(self, domain, include_subdomains): # real signature unknown; restored from __doc__
        """ new_session_policy(domain:str, include_subdomains:bool) -> Soup.HSTSPolicy """
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

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expires = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    include_subdomains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_age = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HSTSPolicy), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupHSTSPolicy (94750594770816)>, '__dict__': <attribute '__dict__' of 'HSTSPolicy' objects>, '__weakref__': <attribute '__weakref__' of 'HSTSPolicy' objects>, '__doc__': None, 'domain': <property object at 0x7f8e47ed7810>, 'max_age': <property object at 0x7f8e47ed7900>, 'expires': <property object at 0x7f8e47ed79f0>, 'include_subdomains': <property object at 0x7f8e47ed7b30>, 'new': gi.FunctionInfo(new), 'new_from_response': gi.FunctionInfo(new_from_response), 'new_full': gi.FunctionInfo(new_full), 'new_session_policy': gi.FunctionInfo(new_session_policy), 'copy': gi.FunctionInfo(copy), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_domain': gi.FunctionInfo(get_domain), 'includes_subdomains': gi.FunctionInfo(includes_subdomains), 'is_expired': gi.FunctionInfo(is_expired), 'is_session_policy': gi.FunctionInfo(is_session_policy)})"
    __gtype__ = None # (!) real value is '<GType SoupHSTSPolicy (94750594770816)>'
    __info__ = StructInfo(HSTSPolicy)


