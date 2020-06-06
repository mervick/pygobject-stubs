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


class NetworkService(__gobject.GInterface):
    # no doc
    def can_reach(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ can_reach(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def can_reach_finish(self, result): # real signature unknown; restored from __doc__
        """ can_reach_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def can_reach_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ can_reach_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def connect_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(self, cancellable:Gio.Cancellable=None) -> Gio.IOStream """
        pass

    def get_default_port(self, method): # real signature unknown; restored from __doc__
        """ get_default_port(self, method:Camel.NetworkSecurityMethod) -> int """
        return 0

    def get_host_reachable(self): # real signature unknown; restored from __doc__
        """ get_host_reachable(self) -> bool """
        return False

    def get_service_name(self, method): # real signature unknown; restored from __doc__
        """ get_service_name(self, method:Camel.NetworkSecurityMethod) -> str """
        return ""

    def ref_connectable(self): # real signature unknown; restored from __doc__
        """ ref_connectable(self) -> Gio.SocketConnectable """
        pass

    def set_connectable(self, connectable): # real signature unknown; restored from __doc__
        """ set_connectable(self, connectable:Gio.SocketConnectable) """
        pass

    def starttls(self, base_stream): # real signature unknown; restored from __doc__
        """ starttls(self, base_stream:Gio.IOStream) -> Gio.IOStream """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(NetworkService), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelNetworkService (94124524043232)>, '__dict__': <attribute '__dict__' of 'NetworkService' objects>, '__weakref__': <attribute '__weakref__' of 'NetworkService' objects>, '__doc__': None, '__gsignals__': {}, 'can_reach': gi.FunctionInfo(can_reach), 'can_reach_finish': gi.FunctionInfo(can_reach_finish), 'can_reach_sync': gi.FunctionInfo(can_reach_sync), 'connect_sync': gi.FunctionInfo(connect_sync), 'get_default_port': gi.FunctionInfo(get_default_port), 'get_host_reachable': gi.FunctionInfo(get_host_reachable), 'get_service_name': gi.FunctionInfo(get_service_name), 'ref_connectable': gi.FunctionInfo(ref_connectable), 'set_connectable': gi.FunctionInfo(set_connectable), 'starttls': gi.FunctionInfo(starttls)})"
    __gdoc__ = 'Interface CamelNetworkService\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelNetworkService (94124524043232)>'
    __info__ = InterfaceInfo(NetworkService)


