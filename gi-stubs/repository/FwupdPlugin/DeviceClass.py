# encoding: utf-8
# module gi.repository.FwupdPlugin
# from /usr/lib64/girepository-1.0/FwupdPlugin-1.0.typelib
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
import gi.repository.Fwupd as __gi_repository_Fwupd
import gobject as __gobject


class DeviceClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DeviceClass()
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

    activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    attach = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cleanup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    detach = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    incorporate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prepare = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prepare_firmware = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    probe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_firmware = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reload = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rescan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    setup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_quirk_kv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    to_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    write_firmware = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DeviceClass), '__module__': 'gi.repository.FwupdPlugin', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DeviceClass' objects>, '__weakref__': <attribute '__weakref__' of 'DeviceClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7feb1afdc900>, 'to_string': <property object at 0x7feb1afdc9f0>, 'write_firmware': <property object at 0x7feb1afdcae0>, 'read_firmware': <property object at 0x7feb1afdcbd0>, 'detach': <property object at 0x7feb1afdccc0>, 'attach': <property object at 0x7feb1afdcdb0>, 'open': <property object at 0x7feb1afdcea0>, 'close': <property object at 0x7feb1afdcf90>, 'probe': <property object at 0x7feb1afde0e0>, 'rescan': <property object at 0x7feb1afde180>, 'prepare_firmware': <property object at 0x7feb1afde2c0>, 'set_quirk_kv': <property object at 0x7feb1afde360>, 'setup': <property object at 0x7feb1afde450>, 'incorporate': <property object at 0x7feb1afde540>, 'poll': <property object at 0x7feb1afde630>, 'activate': <property object at 0x7feb1afde720>, 'reload': <property object at 0x7feb1afde810>, 'prepare': <property object at 0x7feb1afde900>, 'cleanup': <property object at 0x7feb1afde9f0>, 'padding': <property object at 0x7feb1afdeae0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DeviceClass)


