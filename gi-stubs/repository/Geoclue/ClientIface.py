# encoding: utf-8
# module gi.repository.Geoclue
# from /usr/lib64/girepository-1.0/Geoclue-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ClientIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ClientIface()
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

    get_active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_desktop_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_distance_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_requested_accuracy_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_time_threshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    location_updated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ClientIface), '__module__': 'gi.repository.Geoclue', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ClientIface' objects>, '__weakref__': <attribute '__weakref__' of 'ClientIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7fec083f0680>, 'handle_start': <property object at 0x7fec083f04f0>, 'handle_stop': <property object at 0x7fec0840c0e0>, 'get_active': <property object at 0x7fec0840c130>, 'get_desktop_id': <property object at 0x7fec0840c220>, 'get_distance_threshold': <property object at 0x7fec0840c360>, 'get_location': <property object at 0x7fec0840c450>, 'get_requested_accuracy_level': <property object at 0x7fec0840c590>, 'get_time_threshold': <property object at 0x7fec0840c6d0>, 'location_updated': <property object at 0x7fec0840c810>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ClientIface)


