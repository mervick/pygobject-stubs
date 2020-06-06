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


class AbstractSortedSetClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AbstractSortedSetClass()
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

    ceil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    floor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    head_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    higher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterator_at = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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

    sub_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tail_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AbstractSortedSetClass), '__module__': 'gi.repository.Gee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AbstractSortedSetClass' objects>, '__weakref__': <attribute '__weakref__' of 'AbstractSortedSetClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f6a87b39130>, 'first': <property object at 0x7f6a87b39220>, 'last': <property object at 0x7f6a87b39310>, 'iterator_at': <property object at 0x7f6a87b39400>, 'lower': <property object at 0x7f6a87b394f0>, 'higher': <property object at 0x7f6a87b395e0>, 'floor': <property object at 0x7f6a87b396d0>, 'ceil': <property object at 0x7f6a87b397c0>, 'head_set': <property object at 0x7f6a87b398b0>, 'tail_set': <property object at 0x7f6a87b399a0>, 'sub_set': <property object at 0x7f6a87b39a90>, 'reserved0': <property object at 0x7f6a87b39b80>, 'reserved1': <property object at 0x7f6a87b39c70>, 'reserved2': <property object at 0x7f6a87b39d60>, 'reserved3': <property object at 0x7f6a87b39e50>, 'reserved4': <property object at 0x7f6a87b39f40>, 'reserved5': <property object at 0x7f6a87b3b090>, 'reserved6': <property object at 0x7f6a87b3b180>, 'reserved7': <property object at 0x7f6a87b3b270>, 'reserved8': <property object at 0x7f6a87b3b360>, 'reserved9': <property object at 0x7f6a87b3b450>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AbstractSortedSetClass)


