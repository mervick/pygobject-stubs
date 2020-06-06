# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class CapsFeatures(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_any() -> Gst.CapsFeatures
        new_empty() -> Gst.CapsFeatures
    """
    def add(self, feature): # real signature unknown; restored from __doc__
        """ add(self, feature:str) """
        pass

    def add_id(self, feature): # real signature unknown; restored from __doc__
        """ add_id(self, feature:int) """
        pass

    def contains(self, feature): # real signature unknown; restored from __doc__
        """ contains(self, feature:str) -> bool """
        return False

    def contains_id(self, feature): # real signature unknown; restored from __doc__
        """ contains_id(self, feature:int) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gst.CapsFeatures """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_string(self, features): # real signature unknown; restored from __doc__
        """ from_string(features:str) -> Gst.CapsFeatures or None """
        pass

    def get_nth(self, i): # real signature unknown; restored from __doc__
        """ get_nth(self, i:int) -> str or None """
        return ""

    def get_nth_id(self, i): # real signature unknown; restored from __doc__
        """ get_nth_id(self, i:int) -> int """
        return 0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def is_any(self): # real signature unknown; restored from __doc__
        """ is_any(self) -> bool """
        return False

    def is_equal(self, features2): # real signature unknown; restored from __doc__
        """ is_equal(self, features2:Gst.CapsFeatures) -> bool """
        return False

    def new_any(self): # real signature unknown; restored from __doc__
        """ new_any() -> Gst.CapsFeatures """
        pass

    def new_empty(self): # real signature unknown; restored from __doc__
        """ new_empty() -> Gst.CapsFeatures """
        pass

    def remove(self, feature): # real signature unknown; restored from __doc__
        """ remove(self, feature:str) """
        pass

    def remove_id(self, feature): # real signature unknown; restored from __doc__
        """ remove_id(self, feature:int) """
        pass

    def set_parent_refcount(self, refcount): # real signature unknown; restored from __doc__
        """ set_parent_refcount(self, refcount:int) -> bool """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CapsFeatures), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstCapsFeatures (94058977503168)>, '__dict__': <attribute '__dict__' of 'CapsFeatures' objects>, '__weakref__': <attribute '__weakref__' of 'CapsFeatures' objects>, '__doc__': None, 'new_any': gi.FunctionInfo(new_any), 'new_empty': gi.FunctionInfo(new_empty), 'add': gi.FunctionInfo(add), 'add_id': gi.FunctionInfo(add_id), 'contains': gi.FunctionInfo(contains), 'contains_id': gi.FunctionInfo(contains_id), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_nth': gi.FunctionInfo(get_nth), 'get_nth_id': gi.FunctionInfo(get_nth_id), 'get_size': gi.FunctionInfo(get_size), 'is_any': gi.FunctionInfo(is_any), 'is_equal': gi.FunctionInfo(is_equal), 'remove': gi.FunctionInfo(remove), 'remove_id': gi.FunctionInfo(remove_id), 'set_parent_refcount': gi.FunctionInfo(set_parent_refcount), 'to_string': gi.FunctionInfo(to_string), 'from_string': gi.FunctionInfo(from_string)})"
    __gtype__ = None # (!) real value is '<GType GstCapsFeatures (94058977503168)>'
    __info__ = StructInfo(CapsFeatures)


