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


class glibtop_proc_uid(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        glibtop_proc_uid()
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

    egid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    euid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fsgid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fsuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pgrp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ppid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sgid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    suid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tpgid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(glibtop_proc_uid), '__module__': 'gi.repository.GTop', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'glibtop_proc_uid' objects>, '__weakref__': <attribute '__weakref__' of 'glibtop_proc_uid' objects>, '__doc__': None, 'flags': <property object at 0x7f9700c86090>, 'uid': <property object at 0x7f9700c86180>, 'euid': <property object at 0x7f9700c86270>, 'gid': <property object at 0x7f9700c86360>, 'egid': <property object at 0x7f9700c86450>, 'suid': <property object at 0x7f9700c86540>, 'sgid': <property object at 0x7f9700c86630>, 'fsuid': <property object at 0x7f9700c86720>, 'fsgid': <property object at 0x7f9700c86810>, 'pid': <property object at 0x7f9700c86900>, 'ppid': <property object at 0x7f9700c869f0>, 'pgrp': <property object at 0x7f9700c86ae0>, 'session': <property object at 0x7f9700c86bd0>, 'tty': <property object at 0x7f9700c86cc0>, 'tpgid': <property object at 0x7f9700c86db0>, 'priority': <property object at 0x7f9700c86ea0>, 'nice': <property object at 0x7f9700c86f90>, 'ngroups': <property object at 0x7f9700c080e0>, 'groups': <property object at 0x7f9700c081d0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(glibtop_proc_uid)


