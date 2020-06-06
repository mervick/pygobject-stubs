# encoding: utf-8
# module gi.repository.EDataCal
# from /usr/lib64/girepository-1.0/EDataCal-2.0.typelib
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
import gi.repository.EBackend as __gi_repository_EBackend
import gi.repository.ECal as __gi_repository_ECal
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio


class CalBackendSyncClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CalBackendSyncClass()
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

    add_timezone_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_objects_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    discard_alarm_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_attachment_uris_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_free_busy_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_object_list_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_object_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_timezone_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    modify_objects_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    receive_objects_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refresh_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_objects_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    send_objects_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CalBackendSyncClass), '__module__': 'gi.repository.EDataCal', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CalBackendSyncClass' objects>, '__weakref__': <attribute '__weakref__' of 'CalBackendSyncClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fb65e5f6220>, 'open_sync': <property object at 0x7fb65e5f6310>, 'refresh_sync': <property object at 0x7fb65e5f6400>, 'get_object_sync': <property object at 0x7fb65e5f64f0>, 'get_object_list_sync': <property object at 0x7fb65e5f6630>, 'get_free_busy_sync': <property object at 0x7fb65e5f6720>, 'create_objects_sync': <property object at 0x7fb65e5f6810>, 'modify_objects_sync': <property object at 0x7fb65e5f6900>, 'remove_objects_sync': <property object at 0x7fb65e5f69f0>, 'receive_objects_sync': <property object at 0x7fb65e5f6ae0>, 'send_objects_sync': <property object at 0x7fb65e5f6bd0>, 'get_attachment_uris_sync': <property object at 0x7fb65e5f6cc0>, 'discard_alarm_sync': <property object at 0x7fb65e5f6db0>, 'get_timezone_sync': <property object at 0x7fb65e5f6ea0>, 'add_timezone_sync': <property object at 0x7fb65e5f6f90>, 'reserved_padding': <property object at 0x7fb65e5f70e0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CalBackendSyncClass)


