# encoding: utf-8
# module gi.repository.OSTree
# from /usr/lib64/girepository-1.0/OSTree-1.0.typelib
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


class RepoTransactionStats(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        RepoTransactionStats()
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

    content_bytes_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_objects_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    content_objects_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    devino_cache_hits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata_objects_total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    metadata_objects_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RepoTransactionStats), '__module__': 'gi.repository.OSTree', '__gtype__': <GType OstreeRepoTransactionStats (94405993407888)>, '__dict__': <attribute '__dict__' of 'RepoTransactionStats' objects>, '__weakref__': <attribute '__weakref__' of 'RepoTransactionStats' objects>, '__doc__': None, 'metadata_objects_total': <property object at 0x7feceb5ac540>, 'metadata_objects_written': <property object at 0x7feceb5ac680>, 'content_objects_total': <property object at 0x7feceb5ac7c0>, 'content_objects_written': <property object at 0x7feceb5ac900>, 'content_bytes_written': <property object at 0x7feceb5aca40>, 'devino_cache_hits': <property object at 0x7feceb5acb80>, 'padding1': <property object at 0x7feceb5acc70>, 'padding2': <property object at 0x7feceb5acd60>, 'padding3': <property object at 0x7feceb5ace50>, 'padding4': <property object at 0x7feceb5acf40>})"
    __gtype__ = None # (!) real value is '<GType OstreeRepoTransactionStats (94405993407888)>'
    __info__ = StructInfo(RepoTransactionStats)


