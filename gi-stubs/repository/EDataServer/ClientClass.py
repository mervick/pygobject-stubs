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


class ClientClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ClientClass()
    """
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

    backend_died = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    backend_property_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_backend_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_backend_property_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_backend_property_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_dbus_proxy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refresh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refresh_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refresh_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    retrieve_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    retrieve_capabilities_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    retrieve_capabilities_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    retrieve_properties_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_backend_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_backend_property_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_backend_property_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unwrap_dbus_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ClientClass), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ClientClass' objects>, '__weakref__': <attribute '__weakref__' of 'ClientClass' objects>, '__doc__': None, 'parent': <property object at 0x7f6271bcfc20>, 'get_dbus_proxy': <property object at 0x7f6271bcfc70>, 'unwrap_dbus_error': <property object at 0x7f6271bcfd60>, 'retrieve_capabilities': <property object at 0x7f6271bcfe50>, 'retrieve_capabilities_finish': <property object at 0x7f6271bcff40>, 'retrieve_capabilities_sync': <property object at 0x7f6271bd2090>, 'get_backend_property': <property object at 0x7f6271bd2180>, 'get_backend_property_finish': <property object at 0x7f6271bd2270>, 'get_backend_property_sync': <property object at 0x7f6271bd2360>, 'set_backend_property': <property object at 0x7f6271bd2450>, 'set_backend_property_finish': <property object at 0x7f6271bd2540>, 'set_backend_property_sync': <property object at 0x7f6271bd2630>, 'open': <property object at 0x7f6271bd26d0>, 'open_finish': <property object at 0x7f6271bd27c0>, 'open_sync': <property object at 0x7f6271bd28b0>, 'remove': <property object at 0x7f6271bd29a0>, 'remove_finish': <property object at 0x7f6271bd2a90>, 'remove_sync': <property object at 0x7f6271bd2b80>, 'refresh': <property object at 0x7f6271bd2c70>, 'refresh_finish': <property object at 0x7f6271bd2d60>, 'refresh_sync': <property object at 0x7f6271bd2e50>, 'retrieve_properties_sync': <property object at 0x7f6271bd2f90>, 'opened': <property object at 0x7f6271bd3090>, 'backend_error': <property object at 0x7f6271bd3180>, 'backend_died': <property object at 0x7f6271bd3270>, 'backend_property_changed': <property object at 0x7f6271bd33b0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ClientClass)


