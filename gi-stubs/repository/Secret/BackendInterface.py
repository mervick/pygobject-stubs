# encoding: utf-8
# module gi.repository.Secret
# from /usr/lib64/girepository-1.0/Secret-1.typelib
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
import gobject as __gobject


class BackendInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BackendInterface()
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

    clear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ensure_for_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ensure_for_flags_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    search = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    search_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    store = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    store_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BackendInterface), '__module__': 'gi.repository.Secret', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BackendInterface' objects>, '__weakref__': <attribute '__weakref__' of 'BackendInterface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7fa0c59a39f0>, 'ensure_for_flags': <property object at 0x7fa0c59a37c0>, 'ensure_for_flags_finish': <property object at 0x7fa0c59a0090>, 'store': <property object at 0x7fa0c59a0130>, 'store_finish': <property object at 0x7fa0c59a0040>, 'lookup': <property object at 0x7fa0c59a04f0>, 'lookup_finish': <property object at 0x7fa0c59b61d0>, 'clear': <property object at 0x7fa0c59b62c0>, 'clear_finish': <property object at 0x7fa0c59b63b0>, 'search': <property object at 0x7fa0c59b64a0>, 'search_finish': <property object at 0x7fa0c59b6590>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BackendInterface)


