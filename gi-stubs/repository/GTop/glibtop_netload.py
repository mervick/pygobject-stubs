# encoding: utf-8
# module gi.repository.GTop
# from /usr/lib64/girepository-1.0/GTop-2.0.typelib
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


class glibtop_netload(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        glibtop_netload()
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

    address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    address6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bytes_in = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bytes_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bytes_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    collisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors_in = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hwaddress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    if_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mtu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    packets_in = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    packets_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    packets_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prefix6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scope6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subnet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(glibtop_netload), '__module__': 'gi.repository.GTop', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'glibtop_netload' objects>, '__weakref__': <attribute '__weakref__' of 'glibtop_netload' objects>, '__doc__': None, 'flags': <property object at 0x7f9700c7b5e0>, 'if_flags': <property object at 0x7f9700c7b6d0>, 'mtu': <property object at 0x7f9700c7b7c0>, 'subnet': <property object at 0x7f9700c7b8b0>, 'address': <property object at 0x7f9700c7b9a0>, 'packets_in': <property object at 0x7f9700c7ba90>, 'packets_out': <property object at 0x7f9700c7bb80>, 'packets_total': <property object at 0x7f9700c7bc70>, 'bytes_in': <property object at 0x7f9700c7bd60>, 'bytes_out': <property object at 0x7f9700c7be50>, 'bytes_total': <property object at 0x7f9700c7bf40>, 'errors_in': <property object at 0x7f9700c7c090>, 'errors_out': <property object at 0x7f9700c7c180>, 'errors_total': <property object at 0x7f9700c7c270>, 'collisions': <property object at 0x7f9700c7c360>, 'address6': <property object at 0x7f9700c7c450>, 'prefix6': <property object at 0x7f9700c7c540>, 'scope6': <property object at 0x7f9700c7c630>, 'hwaddress': <property object at 0x7f9700c7c720>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(glibtop_netload)


