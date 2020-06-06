# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


class VpnServicePluginClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VpnServicePluginClass()
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

    config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    connect_interactive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disconnect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    failure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ip4_config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ip6_config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    login_banner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_secrets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_secrets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VpnServicePluginClass), '__module__': 'gi.repository.NM', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VpnServicePluginClass' objects>, '__weakref__': <attribute '__weakref__' of 'VpnServicePluginClass' objects>, '__doc__': None, 'parent': <property object at 0x7fb9b84ae270>, 'state_changed': <property object at 0x7fb9b84ae360>, 'ip4_config': <property object at 0x7fb9b84ae450>, 'login_banner': <property object at 0x7fb9b84ae540>, 'failure': <property object at 0x7fb9b84ae630>, 'quit': <property object at 0x7fb9b84ae720>, 'config': <property object at 0x7fb9b84ae810>, 'ip6_config': <property object at 0x7fb9b84ae900>, 'connect': <property object at 0x7fb9b84ae9f0>, 'need_secrets': <property object at 0x7fb9b84aeae0>, 'disconnect': <property object at 0x7fb9b84aebd0>, 'new_secrets': <property object at 0x7fb9b84aecc0>, 'connect_interactive': <property object at 0x7fb9b84aee00>, 'padding': <property object at 0x7fb9b84aeea0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VpnServicePluginClass)


