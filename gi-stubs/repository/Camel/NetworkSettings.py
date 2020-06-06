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


class NetworkSettings(__gobject.GInterface):
    # no doc
    def dup_auth_mechanism(self): # real signature unknown; restored from __doc__
        """ dup_auth_mechanism(self) -> str """
        return ""

    def dup_host(self): # real signature unknown; restored from __doc__
        """ dup_host(self) -> str """
        return ""

    def dup_host_ensure_ascii(self): # real signature unknown; restored from __doc__
        """ dup_host_ensure_ascii(self) -> str """
        return ""

    def dup_user(self): # real signature unknown; restored from __doc__
        """ dup_user(self) -> str """
        return ""

    def get_auth_mechanism(self): # real signature unknown; restored from __doc__
        """ get_auth_mechanism(self) -> str """
        return ""

    def get_host(self): # real signature unknown; restored from __doc__
        """ get_host(self) -> str """
        return ""

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> int """
        return 0

    def get_security_method(self): # real signature unknown; restored from __doc__
        """ get_security_method(self) -> Camel.NetworkSecurityMethod """
        pass

    def get_user(self): # real signature unknown; restored from __doc__
        """ get_user(self) -> str """
        return ""

    def set_auth_mechanism(self, auth_mechanism): # real signature unknown; restored from __doc__
        """ set_auth_mechanism(self, auth_mechanism:str) """
        pass

    def set_host(self, host): # real signature unknown; restored from __doc__
        """ set_host(self, host:str) """
        pass

    def set_port(self, port): # real signature unknown; restored from __doc__
        """ set_port(self, port:int) """
        pass

    def set_security_method(self, method): # real signature unknown; restored from __doc__
        """ set_security_method(self, method:Camel.NetworkSecurityMethod) """
        pass

    def set_user(self, user): # real signature unknown; restored from __doc__
        """ set_user(self, user:str) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(NetworkSettings), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelNetworkSettings (94124524047856)>, '__dict__': <attribute '__dict__' of 'NetworkSettings' objects>, '__weakref__': <attribute '__weakref__' of 'NetworkSettings' objects>, '__doc__': None, '__gsignals__': {}, 'dup_auth_mechanism': gi.FunctionInfo(dup_auth_mechanism), 'dup_host': gi.FunctionInfo(dup_host), 'dup_host_ensure_ascii': gi.FunctionInfo(dup_host_ensure_ascii), 'dup_user': gi.FunctionInfo(dup_user), 'get_auth_mechanism': gi.FunctionInfo(get_auth_mechanism), 'get_host': gi.FunctionInfo(get_host), 'get_port': gi.FunctionInfo(get_port), 'get_security_method': gi.FunctionInfo(get_security_method), 'get_user': gi.FunctionInfo(get_user), 'set_auth_mechanism': gi.FunctionInfo(set_auth_mechanism), 'set_host': gi.FunctionInfo(set_host), 'set_port': gi.FunctionInfo(set_port), 'set_security_method': gi.FunctionInfo(set_security_method), 'set_user': gi.FunctionInfo(set_user)})"
    __gdoc__ = 'Interface CamelNetworkSettings\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelNetworkSettings (94124524047856)>'
    __info__ = InterfaceInfo(NetworkSettings)


