# encoding: utf-8
# module gi.repository.Gee
# from /usr/lib64/girepository-1.0/Gee-0.8.typelib
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


class AbstractListClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AbstractListClass()
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

    get = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index_of = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    list_iterator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AbstractListClass), '__module__': 'gi.repository.Gee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AbstractListClass' objects>, '__weakref__': <attribute '__weakref__' of 'AbstractListClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f6a87cab720>, 'list_iterator': <property object at 0x7f6a87cab810>, 'get': <property object at 0x7f6a87cab900>, 'set': <property object at 0x7f6a87cab9f0>, 'index_of': <property object at 0x7f6a87cabae0>, 'insert': <property object at 0x7f6a87cabbd0>, 'remove_at': <property object at 0x7f6a87cabcc0>, 'slice': <property object at 0x7f6a87cabdb0>, 'reserved0': <property object at 0x7f6a87cabea0>, 'reserved1': <property object at 0x7f6a87cabf90>, 'reserved2': <property object at 0x7f6a87cac0e0>, 'reserved3': <property object at 0x7f6a87cac1d0>, 'reserved4': <property object at 0x7f6a87cac2c0>, 'reserved5': <property object at 0x7f6a87cac3b0>, 'reserved6': <property object at 0x7f6a87cac4a0>, 'reserved7': <property object at 0x7f6a87cac590>, 'reserved8': <property object at 0x7f6a87cac680>, 'reserved9': <property object at 0x7f6a87cac770>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AbstractListClass)


