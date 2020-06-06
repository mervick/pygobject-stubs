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


class glibtop_cpu(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        glibtop_cpu()
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    idle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iowait = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    irq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    softirq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_idle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_iowait = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_irq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_nice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_softirq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_sys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xcpu_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(glibtop_cpu), '__module__': 'gi.repository.GTop', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'glibtop_cpu' objects>, '__weakref__': <attribute '__weakref__' of 'glibtop_cpu' objects>, '__doc__': None, 'flags': <property object at 0x7f9700c72130>, 'total': <property object at 0x7f9700c72220>, 'user': <property object at 0x7f9700c72310>, 'nice': <property object at 0x7f9700c72400>, 'sys': <property object at 0x7f9700c724f0>, 'idle': <property object at 0x7f9700c725e0>, 'iowait': <property object at 0x7f9700c726d0>, 'irq': <property object at 0x7f9700c727c0>, 'softirq': <property object at 0x7f9700c728b0>, 'frequency': <property object at 0x7f9700c729a0>, 'xcpu_total': <property object at 0x7f9700c72a90>, 'xcpu_user': <property object at 0x7f9700c72b80>, 'xcpu_nice': <property object at 0x7f9700c72c70>, 'xcpu_sys': <property object at 0x7f9700c72d60>, 'xcpu_idle': <property object at 0x7f9700c72e50>, 'xcpu_iowait': <property object at 0x7f9700c72f40>, 'xcpu_irq': <property object at 0x7f9700c73090>, 'xcpu_softirq': <property object at 0x7f9700c73180>, 'xcpu_flags': <property object at 0x7f9700c73270>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(glibtop_cpu)


