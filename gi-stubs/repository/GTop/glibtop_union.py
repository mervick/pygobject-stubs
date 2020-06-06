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


class glibtop_union(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    cpu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fsusage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    loadavg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mountlist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    msg_limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    netlist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    netload = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ppp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proclist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_affinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_io = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_kernel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_mem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_open_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_segment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_signal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proc_wd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sem_limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shm_limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    swap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uptime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': gi.UnionInfo(glibtop_union), '__module__': 'gi.repository.GTop', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'glibtop_union' objects>, '__weakref__': <attribute '__weakref__' of 'glibtop_union' objects>, '__doc__': None, 'cpu': <property object at 0x7f9700c109f0>, 'mem': <property object at 0x7f9700c10ae0>, 'swap': <property object at 0x7f9700c10bd0>, 'uptime': <property object at 0x7f9700c10cc0>, 'loadavg': <property object at 0x7f9700c10db0>, 'shm_limits': <property object at 0x7f9700c10ea0>, 'msg_limits': <property object at 0x7f9700c10f90>, 'sem_limits': <property object at 0x7f9700c120e0>, 'proclist': <property object at 0x7f9700c121d0>, 'proc_state': <property object at 0x7f9700c122c0>, 'proc_uid': <property object at 0x7f9700c123b0>, 'proc_mem': <property object at 0x7f9700c124a0>, 'proc_time': <property object at 0x7f9700c12590>, 'proc_signal': <property object at 0x7f9700c12680>, 'proc_kernel': <property object at 0x7f9700c12770>, 'proc_segment': <property object at 0x7f9700c12860>, 'proc_args': <property object at 0x7f9700c12950>, 'proc_map': <property object at 0x7f9700c12a40>, 'mountlist': <property object at 0x7f9700c12b30>, 'fsusage': <property object at 0x7f9700c12c20>, 'netlist': <property object at 0x7f9700c12d10>, 'netload': <property object at 0x7f9700c12e00>, 'ppp': <property object at 0x7f9700c12ef0>, 'proc_open_files': <property object at 0x7f9700c13040>, 'proc_wd': <property object at 0x7f9700c13130>, 'proc_affinity': <property object at 0x7f9700c13220>, 'proc_io': <property object at 0x7f9700c13310>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = gi.UnionInfo(glibtop_union)


