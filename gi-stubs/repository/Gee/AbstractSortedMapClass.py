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


class AbstractSortedMapClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AbstractSortedMapClass()
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

    head_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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

    sub_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tail_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AbstractSortedMapClass), '__module__': 'gi.repository.Gee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AbstractSortedMapClass' objects>, '__weakref__': <attribute '__weakref__' of 'AbstractSortedMapClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f6a87b381d0>, 'head_map': <property object at 0x7f6a87b382c0>, 'tail_map': <property object at 0x7f6a87b383b0>, 'sub_map': <property object at 0x7f6a87b384a0>, 'reserved0': <property object at 0x7f6a87b38590>, 'reserved1': <property object at 0x7f6a87b38680>, 'reserved2': <property object at 0x7f6a87b38770>, 'reserved3': <property object at 0x7f6a87b38860>, 'reserved4': <property object at 0x7f6a87b38950>, 'reserved5': <property object at 0x7f6a87b38a40>, 'reserved6': <property object at 0x7f6a87b38b30>, 'reserved7': <property object at 0x7f6a87b38c20>, 'reserved8': <property object at 0x7f6a87b38d10>, 'reserved9': <property object at 0x7f6a87b38e00>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AbstractSortedMapClass)


