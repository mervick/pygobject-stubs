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


class TraversableIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TraversableIface()
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

    all_match = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    any_match = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    chop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    first_match = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flat_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    foreach = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_element_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    order_by = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tee = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TraversableIface), '__module__': 'gi.repository.Gee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TraversableIface' objects>, '__weakref__': <attribute '__weakref__' of 'TraversableIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f6a87b61c70>, 'foreach': <property object at 0x7f6a87b61d60>, 'stream': <property object at 0x7f6a87b61e50>, 'fold': <property object at 0x7f6a87b61f40>, 'map': <property object at 0x7f6a87b63090>, 'scan': <property object at 0x7f6a87b63180>, 'filter': <property object at 0x7f6a87b63270>, 'chop': <property object at 0x7f6a87b63360>, 'flat_map': <property object at 0x7f6a87b63450>, 'tee': <property object at 0x7f6a87b63540>, 'first_match': <property object at 0x7f6a87b63630>, 'any_match': <property object at 0x7f6a87b63720>, 'all_match': <property object at 0x7f6a87b63810>, 'max': <property object at 0x7f6a87b63900>, 'min': <property object at 0x7f6a87b639f0>, 'order_by': <property object at 0x7f6a87b63ae0>, 'get_element_type': <property object at 0x7f6a87b63c20>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TraversableIface)


