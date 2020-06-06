# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class SettingsBackendClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        SettingsBackendClass()
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

    get_permission = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_writable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_user_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subscribe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unsubscribe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_tree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SettingsBackendClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'SettingsBackendClass' objects>, '__weakref__': <attribute '__weakref__' of 'SettingsBackendClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f4b87fb1810>, 'read': <property object at 0x7f4b87fb1900>, 'get_writable': <property object at 0x7f4b87fb19f0>, 'write': <property object at 0x7f4b87fb1ae0>, 'write_tree': <property object at 0x7f4b87fb1bd0>, 'reset': <property object at 0x7f4b87fb1cc0>, 'subscribe': <property object at 0x7f4b87fb1db0>, 'unsubscribe': <property object at 0x7f4b87fb1ea0>, 'sync': <property object at 0x7f4b87fb1f90>, 'get_permission': <property object at 0x7f4b87fb30e0>, 'read_user_value': <property object at 0x7f4b87fb31d0>, 'padding': <property object at 0x7f4b87fb32c0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(SettingsBackendClass)


