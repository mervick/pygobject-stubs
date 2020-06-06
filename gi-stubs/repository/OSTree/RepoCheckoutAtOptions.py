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


class RepoCheckoutAtOptions(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RepoCheckoutAtOptions()
    """
    def set_devino(self, cache=None): # real signature unknown; restored from __doc__
        """ set_devino(self, cache:OSTree.RepoDevInoCache=None) """
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

    bareuseronly_dirs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    devino_to_csum_cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enable_fsync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enable_uncompressed_cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    filter_user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    force_copy_zerosized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    no_copy_fallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    overwrite_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    process_whiteouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sepolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sepolicy_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    subpath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unused_bools = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unused_ints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unused_ptrs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RepoCheckoutAtOptions), '__module__': 'gi.repository.OSTree', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RepoCheckoutAtOptions' objects>, '__weakref__': <attribute '__weakref__' of 'RepoCheckoutAtOptions' objects>, '__doc__': None, 'mode': <property object at 0x7feceb597270>, 'overwrite_mode': <property object at 0x7feceb597360>, 'enable_uncompressed_cache': <property object at 0x7feceb5974a0>, 'enable_fsync': <property object at 0x7feceb597590>, 'process_whiteouts': <property object at 0x7feceb5976d0>, 'no_copy_fallback': <property object at 0x7feceb597810>, 'force_copy': <property object at 0x7feceb597900>, 'bareuseronly_dirs': <property object at 0x7feceb597a40>, 'force_copy_zerosized': <property object at 0x7feceb597b80>, 'unused_bools': <property object at 0x7feceb597c70>, 'subpath': <property object at 0x7feceb597d60>, 'devino_to_csum_cache': <property object at 0x7feceb597ea0>, 'unused_ints': <property object at 0x7feceb597f40>, 'unused_ptrs': <property object at 0x7feceb598090>, 'filter': <property object at 0x7feceb598180>, 'filter_user_data': <property object at 0x7feceb5982c0>, 'sepolicy': <property object at 0x7feceb5983b0>, 'sepolicy_prefix': <property object at 0x7feceb5984a0>, 'set_devino': gi.FunctionInfo(set_devino)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RepoCheckoutAtOptions)


