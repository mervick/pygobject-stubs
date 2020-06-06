# encoding: utf-8
# module gi.repository.EBookContacts
# from /usr/lib64/girepository-1.0/EBookContacts-1.2.typelib
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
import gobject as __gobject


class NameWestern(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        NameWestern()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EBookContacts.NameWestern """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def parse(self, full_name): # real signature unknown; restored from __doc__
        """ parse(full_name:str) -> EBookContacts.NameWestern """
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

    first = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    middle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NameWestern), '__module__': 'gi.repository.EBookContacts', '__gtype__': <GType ENameWestern (94769385600128)>, '__dict__': <attribute '__dict__' of 'NameWestern' objects>, '__weakref__': <attribute '__weakref__' of 'NameWestern' objects>, '__doc__': None, 'prefix': <property object at 0x7f7148846270>, 'first': <property object at 0x7f7148846360>, 'middle': <property object at 0x7f7148846450>, 'nick': <property object at 0x7f7148846540>, 'last': <property object at 0x7f7148846630>, 'suffix': <property object at 0x7f7148846720>, 'full': <property object at 0x7f7148846810>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'parse': gi.FunctionInfo(parse)})"
    __gtype__ = None # (!) real value is '<GType ENameWestern (94769385600128)>'
    __info__ = StructInfo(NameWestern)


