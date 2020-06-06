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


class RepoFinderResult(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        RepoFinderResult()
        new(remote:OSTree.Remote, finder:OSTree.RepoFinder, priority:int, ref_to_checksum:dict, ref_to_timestamp:dict=None, summary_last_modified:int) -> OSTree.RepoFinderResult
    """
    def compare(self, b): # real signature unknown; restored from __doc__
        """ compare(self, b:OSTree.RepoFinderResult) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> OSTree.RepoFinderResult """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def freev(self, results): # real signature unknown; restored from __doc__
        """ freev(results:list) """
        pass

    def new(self, remote, finder, priority, ref_to_checksum, ref_to_timestamp=None, summary_last_modified): # real signature unknown; restored from __doc__
        """ new(remote:OSTree.Remote, finder:OSTree.RepoFinder, priority:int, ref_to_checksum:dict, ref_to_timestamp:dict=None, summary_last_modified:int) -> OSTree.RepoFinderResult """
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

    finder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_to_checksum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_to_timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    summary_last_modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RepoFinderResult), '__module__': 'gi.repository.OSTree', '__gtype__': <GType OstreeRepoFinderResult (94405993250256)>, '__dict__': <attribute '__dict__' of 'RepoFinderResult' objects>, '__weakref__': <attribute '__weakref__' of 'RepoFinderResult' objects>, '__doc__': None, 'remote': <property object at 0x7feceb5a5f90>, 'finder': <property object at 0x7feceb5a80e0>, 'priority': <property object at 0x7feceb5a81d0>, 'ref_to_checksum': <property object at 0x7feceb5a82c0>, 'summary_last_modified': <property object at 0x7feceb5a8400>, 'ref_to_timestamp': <property object at 0x7feceb5a8540>, 'padding': <property object at 0x7feceb5a8630>, 'new': gi.FunctionInfo(new), 'compare': gi.FunctionInfo(compare), 'dup': gi.FunctionInfo(dup), 'free': gi.FunctionInfo(free), 'freev': gi.FunctionInfo(freev)})"
    __gtype__ = None # (!) real value is '<GType OstreeRepoFinderResult (94405993250256)>'
    __info__ = StructInfo(RepoFinderResult)


