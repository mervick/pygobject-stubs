# encoding: utf-8
# module gi.repository.LibvirtGObject
# from /usr/lib64/girepository-1.0/LibvirtGObject-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class DomainInterfaceStats(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        DomainInterfaceStats()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

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

    rx_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rx_drop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rx_errs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rx_packets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tx_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tx_drop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tx_errs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tx_packets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DomainInterfaceStats), '__module__': 'gi.repository.LibvirtGObject', '__gtype__': <GType GVirDomainInterfaceStats (94394875784896)>, '__dict__': <attribute '__dict__' of 'DomainInterfaceStats' objects>, '__weakref__': <attribute '__weakref__' of 'DomainInterfaceStats' objects>, '__doc__': None, 'rx_bytes': <property object at 0x7ffa6f96f2c0>, 'rx_packets': <property object at 0x7ffa6f96f3b0>, 'rx_errs': <property object at 0x7ffa6f96f4a0>, 'rx_drop': <property object at 0x7ffa6f96f590>, 'tx_bytes': <property object at 0x7ffa6f96f680>, 'tx_packets': <property object at 0x7ffa6f96f770>, 'tx_errs': <property object at 0x7ffa6f96f860>, 'tx_drop': <property object at 0x7ffa6f96f950>})"
    __gtype__ = None # (!) real value is '<GType GVirDomainInterfaceStats (94394875784896)>'
    __info__ = StructInfo(DomainInterfaceStats)


