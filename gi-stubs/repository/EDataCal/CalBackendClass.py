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


class CalBackendClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CalBackendClass()
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

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_add_timezone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_create_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_discard_alarm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_get_attachment_uris = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_get_backend_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_get_free_busy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_get_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_get_object_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_get_timezone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_modify_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_receive_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_refresh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_remove_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_send_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_start_view = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    impl_stop_view = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved_padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shutdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    use_serial_dispatch_queue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CalBackendClass), '__module__': 'gi.repository.EDataCal', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CalBackendClass' objects>, '__weakref__': <attribute '__weakref__' of 'CalBackendClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fb65e5f0180>, 'use_serial_dispatch_queue': <property object at 0x7fb65e5f02c0>, 'impl_get_backend_property': <property object at 0x7fb65e5f0400>, 'impl_open': <property object at 0x7fb65e5f04f0>, 'impl_refresh': <property object at 0x7fb65e5f05e0>, 'impl_get_object': <property object at 0x7fb65e5f06d0>, 'impl_get_object_list': <property object at 0x7fb65e5f0810>, 'impl_get_free_busy': <property object at 0x7fb65e5f0950>, 'impl_create_objects': <property object at 0x7fb65e5f0a90>, 'impl_modify_objects': <property object at 0x7fb65e5f0bd0>, 'impl_remove_objects': <property object at 0x7fb65e5f0d10>, 'impl_receive_objects': <property object at 0x7fb65e5f0e50>, 'impl_send_objects': <property object at 0x7fb65e5f0f90>, 'impl_get_attachment_uris': <property object at 0x7fb65e5f1130>, 'impl_discard_alarm': <property object at 0x7fb65e5f1270>, 'impl_get_timezone': <property object at 0x7fb65e5f13b0>, 'impl_add_timezone': <property object at 0x7fb65e5f14f0>, 'impl_start_view': <property object at 0x7fb65e5f15e0>, 'impl_stop_view': <property object at 0x7fb65e5f16d0>, 'closed': <property object at 0x7fb65e5f17c0>, 'shutdown': <property object at 0x7fb65e5f18b0>, 'reserved_padding': <property object at 0x7fb65e5f19f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CalBackendClass)


