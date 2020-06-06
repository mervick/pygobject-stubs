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


class glibtop_sysdeps(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        glibtop_sysdeps()
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

    cpu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    features = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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

    reserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sem_limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shm_limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    swap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uptime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(glibtop_sysdeps), '__module__': 'gi.repository.GTop', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'glibtop_sysdeps' objects>, '__weakref__': <attribute '__weakref__' of 'glibtop_sysdeps' objects>, '__doc__': None, 'flags': <property object at 0x7f9700c0d1d0>, 'features': <property object at 0x7f9700c0d2c0>, 'cpu': <property object at 0x7f9700c0d3b0>, 'mem': <property object at 0x7f9700c0d4a0>, 'swap': <property object at 0x7f9700c0d590>, 'uptime': <property object at 0x7f9700c0d680>, 'loadavg': <property object at 0x7f9700c0d770>, 'shm_limits': <property object at 0x7f9700c0d860>, 'msg_limits': <property object at 0x7f9700c0d950>, 'sem_limits': <property object at 0x7f9700c0da40>, 'proclist': <property object at 0x7f9700c0db30>, 'proc_state': <property object at 0x7f9700c0dc20>, 'proc_uid': <property object at 0x7f9700c0dd10>, 'proc_mem': <property object at 0x7f9700c0de00>, 'proc_time': <property object at 0x7f9700c0def0>, 'proc_signal': <property object at 0x7f9700c0e040>, 'proc_kernel': <property object at 0x7f9700c0e130>, 'proc_segment': <property object at 0x7f9700c0e220>, 'proc_args': <property object at 0x7f9700c0e310>, 'proc_map': <property object at 0x7f9700c0e400>, 'proc_open_files': <property object at 0x7f9700c0e4f0>, 'mountlist': <property object at 0x7f9700c0e5e0>, 'fsusage': <property object at 0x7f9700c0e6d0>, 'netlist': <property object at 0x7f9700c0e7c0>, 'netload': <property object at 0x7f9700c0e8b0>, 'ppp': <property object at 0x7f9700c0e9a0>, 'proc_wd': <property object at 0x7f9700c0ea90>, 'proc_affinity': <property object at 0x7f9700c0eb80>, 'proc_io': <property object at 0x7f9700c0ec70>, 'reserved0': <property object at 0x7f9700c0ed60>, 'reserved1': <property object at 0x7f9700c0ee50>, 'reserved2': <property object at 0x7f9700c0ef40>, 'reserved3': <property object at 0x7f9700c10090>, 'reserved4': <property object at 0x7f9700c10180>, 'reserved5': <property object at 0x7f9700c10270>, 'reserved6': <property object at 0x7f9700c10360>, 'reserved7': <property object at 0x7f9700c10450>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(glibtop_sysdeps)


