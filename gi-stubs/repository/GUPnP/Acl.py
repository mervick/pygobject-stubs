# encoding: utf-8
# module gi.repository.GUPnP
# from /usr/lib64/girepository-1.0/GUPnP-1.0.typelib
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
import gi.repository.GSSDP as __gi_repository_GSSDP
import gobject as __gobject


class Acl(__gobject.GInterface):
    # no doc
    def can_sync(self): # real signature unknown; restored from __doc__
        """ can_sync(self) -> bool """
        return False

    def is_allowed(self, device=None, service=None, path, address, agent=None): # real signature unknown; restored from __doc__
        """ is_allowed(self, device=None, service=None, path:str, address:str, agent:str=None) -> bool """
        return False

    def is_allowed_async(self, device=None, service=None, path, address, agent=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ is_allowed_async(self, device=None, service=None, path:str, address:str, agent:str=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def is_allowed_finish(self, res): # real signature unknown; restored from __doc__
        """ is_allowed_finish(self, res:Gio.AsyncResult) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Acl), '__module__': 'gi.repository.GUPnP', '__gtype__': <GType GUPnPAcl (94417775839968)>, '__dict__': <attribute '__dict__' of 'Acl' objects>, '__weakref__': <attribute '__weakref__' of 'Acl' objects>, '__doc__': None, '__gsignals__': {}, 'can_sync': gi.FunctionInfo(can_sync), 'is_allowed': gi.FunctionInfo(is_allowed), 'is_allowed_async': gi.FunctionInfo(is_allowed_async), 'is_allowed_finish': gi.FunctionInfo(is_allowed_finish)})"
    __gdoc__ = 'Interface GUPnPAcl\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GUPnPAcl (94417775839968)>'
    __info__ = InterfaceInfo(Acl)


