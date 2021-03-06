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


class ClientContext(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_address(self): # real signature unknown; restored from __doc__
        """ get_address(self) -> Soup.Address or None """
        pass

    def get_auth_domain(self): # real signature unknown; restored from __doc__
        """ get_auth_domain(self) -> Soup.AuthDomain or None """
        pass

    def get_auth_user(self): # real signature unknown; restored from __doc__
        """ get_auth_user(self) -> str or None """
        return ""

    def get_gsocket(self): # real signature unknown; restored from __doc__
        """ get_gsocket(self) -> Gio.Socket or None """
        pass

    def get_host(self): # real signature unknown; restored from __doc__
        """ get_host(self) -> str or None """
        return ""

    def get_local_address(self): # real signature unknown; restored from __doc__
        """ get_local_address(self) -> Gio.SocketAddress or None """
        pass

    def get_remote_address(self): # real signature unknown; restored from __doc__
        """ get_remote_address(self) -> Gio.SocketAddress or None """
        pass

    def get_socket(self): # real signature unknown; restored from __doc__
        """ get_socket(self) -> Soup.Socket """
        pass

    def steal_connection(self): # real signature unknown; restored from __doc__
        """ steal_connection(self) -> Gio.IOStream """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ClientContext), '__module__': 'gi.repository.Soup', '__gtype__': <GType SoupClientContext (94750594715856)>, '__dict__': <attribute '__dict__' of 'ClientContext' objects>, '__weakref__': <attribute '__weakref__' of 'ClientContext' objects>, '__doc__': None, 'get_address': gi.FunctionInfo(get_address), 'get_auth_domain': gi.FunctionInfo(get_auth_domain), 'get_auth_user': gi.FunctionInfo(get_auth_user), 'get_gsocket': gi.FunctionInfo(get_gsocket), 'get_host': gi.FunctionInfo(get_host), 'get_local_address': gi.FunctionInfo(get_local_address), 'get_remote_address': gi.FunctionInfo(get_remote_address), 'get_socket': gi.FunctionInfo(get_socket), 'steal_connection': gi.FunctionInfo(steal_connection)})"
    __gtype__ = None # (!) real value is '<GType SoupClientContext (94750594715856)>'
    __info__ = StructInfo(ClientContext)


