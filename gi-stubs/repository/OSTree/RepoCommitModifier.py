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


class RepoCommitModifier(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(flags:OSTree.RepoCommitModifierFlags, commit_filter:OSTree.RepoCommitFilter=None, user_data=None) -> OSTree.RepoCommitModifier
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def new(self, flags, commit_filter=None, user_data=None): # real signature unknown; restored from __doc__
        """ new(flags:OSTree.RepoCommitModifierFlags, commit_filter:OSTree.RepoCommitFilter=None, user_data=None) -> OSTree.RepoCommitModifier """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> OSTree.RepoCommitModifier """
        pass

    def set_devino_cache(self, cache): # real signature unknown; restored from __doc__
        """ set_devino_cache(self, cache:OSTree.RepoDevInoCache) """
        pass

    def set_sepolicy(self, sepolicy=None): # real signature unknown; restored from __doc__
        """ set_sepolicy(self, sepolicy:OSTree.SePolicy=None) """
        pass

    def set_xattr_callback(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ set_xattr_callback(self, callback:OSTree.RepoCommitModifierXattrCallback, user_data=None) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new(flags:OSTree.RepoCommitModifierFlags, commit_filter:OSTree.RepoCommitFilter=None, user_data=None) -> OSTree.RepoCommitModifier """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RepoCommitModifier), '__module__': 'gi.repository.OSTree', '__gtype__': <GType OstreeRepoCommitModifier (94405993315152)>, '__dict__': <attribute '__dict__' of 'RepoCommitModifier' objects>, '__weakref__': <attribute '__weakref__' of 'RepoCommitModifier' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'ref': gi.FunctionInfo(ref), 'set_devino_cache': gi.FunctionInfo(set_devino_cache), 'set_sepolicy': gi.FunctionInfo(set_sepolicy), 'set_xattr_callback': gi.FunctionInfo(set_xattr_callback), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7fecec2b6b50>, '__init__': <function nothing at 0x7fecec4e4ee0>})"
    __gtype__ = None # (!) real value is '<GType OstreeRepoCommitModifier (94405993315152)>'
    __info__ = StructInfo(RepoCommitModifier)


