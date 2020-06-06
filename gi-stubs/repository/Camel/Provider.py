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


class Provider(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Provider()
    """
    def auto_detect(self, url): # real signature unknown; restored from __doc__
        """ auto_detect(self, url:Camel.URL) -> int, auto_detected:dict """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, protocol): # real signature unknown; restored from __doc__
        """ get(protocol:str) -> Camel.Provider """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init() """
        pass

    def list(self, load): # real signature unknown; restored from __doc__
        """ list(load:bool) -> list """
        return []

    def load(self, path): # real signature unknown; restored from __doc__
        """ load(path:str) -> bool """
        return False

    def register(self): # real signature unknown; restored from __doc__
        """ register(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    authtypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    extra_conf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    port_entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    protocol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    translation_domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    url_equal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    url_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    url_hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Provider), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelProvider (94124523982128)>, '__dict__': <attribute '__dict__' of 'Provider' objects>, '__weakref__': <attribute '__weakref__' of 'Provider' objects>, '__doc__': None, 'protocol': <property object at 0x7f7b34f335e0>, 'name': <property object at 0x7f7b34f336d0>, 'description': <property object at 0x7f7b34f337c0>, 'domain': <property object at 0x7f7b34f338b0>, 'flags': <property object at 0x7f7b34f339a0>, 'url_flags': <property object at 0x7f7b34f33a90>, 'extra_conf': <property object at 0x7f7b34f33b80>, 'port_entries': <property object at 0x7f7b34f33c70>, 'auto_detect': gi.FunctionInfo(auto_detect), 'object_types': <property object at 0x7f7b34f33e50>, 'authtypes': <property object at 0x7f7b34f33f40>, 'url_hash': <property object at 0x7f7b34f36090>, 'url_equal': <property object at 0x7f7b34f36180>, 'translation_domain': <property object at 0x7f7b34f362c0>, 'priv': <property object at 0x7f7b34f36360>, 'register': gi.FunctionInfo(register), 'get': gi.FunctionInfo(get), 'init': gi.FunctionInfo(init), 'list': gi.FunctionInfo(list), 'load': gi.FunctionInfo(load)})"
    __gtype__ = None # (!) real value is '<GType CamelProvider (94124523982128)>'
    __info__ = StructInfo(Provider)


