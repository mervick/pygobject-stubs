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


class glibtop_proc_state(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        glibtop_proc_state()
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

    cmd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_cpu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_processor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    processor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rgid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ruid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(glibtop_proc_state), '__module__': 'gi.repository.GTop', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'glibtop_proc_state' objects>, '__weakref__': <attribute '__weakref__' of 'glibtop_proc_state' objects>, '__doc__': None, 'flags': <property object at 0x7f9700c84950>, 'cmd': <property object at 0x7f9700c84a40>, 'state': <property object at 0x7f9700c84b30>, 'uid': <property object at 0x7f9700c84c20>, 'gid': <property object at 0x7f9700c84d10>, 'ruid': <property object at 0x7f9700c84e00>, 'rgid': <property object at 0x7f9700c84ef0>, 'has_cpu': <property object at 0x7f9700c85040>, 'processor': <property object at 0x7f9700c85130>, 'last_processor': <property object at 0x7f9700c85220>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(glibtop_proc_state)


