# encoding: utf-8
# module gi.repository.EBackend
# from /usr/lib64/girepository-1.0/EBackend-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class DataFactoryClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DataFactoryClass()
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

    backend_factory_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    complete_open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data_object_path_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    factory_object_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_dbus_interface_skeleton = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_factory_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_backend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subprocess_bus_name_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subprocess_object_path_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DataFactoryClass), '__module__': 'gi.repository.EBackend', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DataFactoryClass' objects>, '__weakref__': <attribute '__weakref__' of 'DataFactoryClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f9dc2d8ce50>, 'backend_factory_type': <property object at 0x7f9dc2d8cf90>, 'factory_object_path': <property object at 0x7f9dbf88d130>, 'data_object_path_prefix': <property object at 0x7f9dbf88d270>, 'subprocess_object_path_prefix': <property object at 0x7f9dbf88d3b0>, 'subprocess_bus_name_prefix': <property object at 0x7f9dbf88d4f0>, 'get_dbus_interface_skeleton': <property object at 0x7f9dbf88d630>, 'get_factory_name': <property object at 0x7f9dbf88d770>, 'complete_open': <property object at 0x7f9dbf88d860>, 'create_backend': <property object at 0x7f9dbf88d950>, 'open_backend': <property object at 0x7f9dbf88da40>, 'reserved': <property object at 0x7f9dbf88db30>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DataFactoryClass)


