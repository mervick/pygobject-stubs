# encoding: utf-8
# module gi.repository.Grl
# from /usr/lib64/girepository-1.0/Grl-0.3.typelib
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
import gobject as __gobject


class PluginDescriptor(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PluginDescriptor()
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

    author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deinit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    init = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    license = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    major_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minor_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    register_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _grl_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PluginDescriptor), '__module__': 'gi.repository.Grl', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PluginDescriptor' objects>, '__weakref__': <attribute '__weakref__' of 'PluginDescriptor' objects>, '__doc__': None, 'major_version': <property object at 0x7fa0404a12c0>, 'minor_version': <property object at 0x7fa0404a13b0>, 'id': <property object at 0x7fa0404a14a0>, 'name': <property object at 0x7fa0404a1590>, 'description': <property object at 0x7fa0404a1680>, 'author': <property object at 0x7fa0404a1770>, 'version': <property object at 0x7fa0404a1860>, 'license': <property object at 0x7fa0404a1950>, 'site': <property object at 0x7fa0404a1a40>, 'init': <property object at 0x7fa0404a1b30>, 'deinit': <property object at 0x7fa0404a1c20>, 'register_keys': <property object at 0x7fa0404a1d10>, '_grl_reserved': <property object at 0x7fa0404a1e00>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PluginDescriptor)


