# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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


class ManagerIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ManagerIface()
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

    get_default_encryption_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_encryption_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_filesystems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_can_check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_can_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_can_repair = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_can_resize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_enable_modules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_get_block_devices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_loop_setup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_mdraid_create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_resolve_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ManagerIface), '__module__': 'gi.repository.UDisks', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ManagerIface' objects>, '__weakref__': <attribute '__weakref__' of 'ManagerIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f13a8063c20>, 'handle_enable_modules': <property object at 0x7f13a8063d60>, 'handle_loop_setup': <property object at 0x7f13a8063ea0>, 'get_default_encryption_type': <property object at 0x7f13a8065040>, 'get_supported_encryption_types': <property object at 0x7f13a8065180>, 'get_supported_filesystems': <property object at 0x7f13a80652c0>, 'get_version': <property object at 0x7f13a80653b0>, 'handle_mdraid_create': <property object at 0x7f13a80654f0>, 'handle_can_check': <property object at 0x7f13a8065630>, 'handle_can_format': <property object at 0x7f13a8065770>, 'handle_can_repair': <property object at 0x7f13a80658b0>, 'handle_can_resize': <property object at 0x7f13a80659f0>, 'handle_get_block_devices': <property object at 0x7f13a8065b30>, 'handle_resolve_device': <property object at 0x7f13a8065c70>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ManagerIface)


