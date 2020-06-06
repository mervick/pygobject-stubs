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


class Caps(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Caps()
        new_any() -> Gst.Caps
        new_empty() -> Gst.Caps
        new_empty_simple(media_type:str) -> Gst.Caps
    """
    def append(self, caps2): # real signature unknown; restored from __doc__
        """ append(self, caps2:Gst.Caps) """
        pass

    def append_structure(self, structure): # real signature unknown; restored from __doc__
        """ append_structure(self, structure:Gst.Structure) """
        pass

    def append_structure_full(self, structure, features=None): # real signature unknown; restored from __doc__
        """ append_structure_full(self, structure:Gst.Structure, features:Gst.CapsFeatures=None) """
        pass

    def can_intersect(self, caps2): # real signature unknown; restored from __doc__
        """ can_intersect(self, caps2:Gst.Caps) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gst.Caps """
        pass

    def copy_nth(self, nth): # real signature unknown; restored from __doc__
        """ copy_nth(self, nth:int) -> Gst.Caps """
        pass

    def filter_and_map_in_place(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ filter_and_map_in_place(self, func:Gst.CapsFilterMapFunc, user_data=None) """
        pass

    def fixate(self): # real signature unknown; restored from __doc__
        """ fixate(self) -> Gst.Caps """
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gst.CapsForeachFunc, user_data=None) -> bool """
        return False

    def from_string(self, string): # real signature unknown; restored from __doc__
        """ from_string(string:str) -> Gst.Caps or None """
        pass

    def get_features(self, index): # real signature unknown; restored from __doc__
        """ get_features(self, index:int) -> Gst.CapsFeatures or None """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_structure(self, index): # real signature unknown; restored from __doc__
        """ get_structure(self, index:int) -> Gst.Structure """
        pass

    def intersect(self, caps2): # real signature unknown; restored from __doc__
        """ intersect(self, caps2:Gst.Caps) -> Gst.Caps """
        pass

    def intersect_full(self, caps2, mode): # real signature unknown; restored from __doc__
        """ intersect_full(self, caps2:Gst.Caps, mode:Gst.CapsIntersectMode) -> Gst.Caps """
        pass

    def is_always_compatible(self, caps2): # real signature unknown; restored from __doc__
        """ is_always_compatible(self, caps2:Gst.Caps) -> bool """
        return False

    def is_any(self): # real signature unknown; restored from __doc__
        """ is_any(self) -> bool """
        return False

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def is_equal(self, caps2): # real signature unknown; restored from __doc__
        """ is_equal(self, caps2:Gst.Caps) -> bool """
        return False

    def is_equal_fixed(self, caps2): # real signature unknown; restored from __doc__
        """ is_equal_fixed(self, caps2:Gst.Caps) -> bool """
        return False

    def is_fixed(self): # real signature unknown; restored from __doc__
        """ is_fixed(self) -> bool """
        return False

    def is_strictly_equal(self, caps2): # real signature unknown; restored from __doc__
        """ is_strictly_equal(self, caps2:Gst.Caps) -> bool """
        return False

    def is_subset(self, superset): # real signature unknown; restored from __doc__
        """ is_subset(self, superset:Gst.Caps) -> bool """
        return False

    def is_subset_structure(self, structure): # real signature unknown; restored from __doc__
        """ is_subset_structure(self, structure:Gst.Structure) -> bool """
        return False

    def is_subset_structure_full(self, structure, features=None): # real signature unknown; restored from __doc__
        """ is_subset_structure_full(self, structure:Gst.Structure, features:Gst.CapsFeatures=None) -> bool """
        return False

    def map_in_place(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ map_in_place(self, func:Gst.CapsMapFunc, user_data=None) -> bool """
        return False

    def merge(self, caps2): # real signature unknown; restored from __doc__
        """ merge(self, caps2:Gst.Caps) -> Gst.Caps """
        pass

    def merge_structure(self, structure): # real signature unknown; restored from __doc__
        """ merge_structure(self, structure:Gst.Structure) -> Gst.Caps """
        pass

    def merge_structure_full(self, structure, features=None): # real signature unknown; restored from __doc__
        """ merge_structure_full(self, structure:Gst.Structure, features:Gst.CapsFeatures=None) -> Gst.Caps """
        pass

    def new_any(self): # real signature unknown; restored from __doc__
        """ new_any() -> Gst.Caps """
        pass

    def new_empty(self): # real signature unknown; restored from __doc__
        """ new_empty() -> Gst.Caps """
        pass

    def new_empty_simple(self, media_type): # real signature unknown; restored from __doc__
        """ new_empty_simple(media_type:str) -> Gst.Caps """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> Gst.Caps """
        pass

    def remove_structure(self, idx): # real signature unknown; restored from __doc__
        """ remove_structure(self, idx:int) """
        pass

    def set_features(self, index, features=None): # real signature unknown; restored from __doc__
        """ set_features(self, index:int, features:Gst.CapsFeatures=None) """
        pass

    def set_features_simple(self, features=None): # real signature unknown; restored from __doc__
        """ set_features_simple(self, features:Gst.CapsFeatures=None) """
        pass

    def set_value(self, field, value): # real signature unknown; restored from __doc__
        """ set_value(self, field:str, value:GObject.Value) """
        pass

    def simplify(self): # real signature unknown; restored from __doc__
        """ simplify(self) -> Gst.Caps """
        pass

    def steal_structure(self, index): # real signature unknown; restored from __doc__
        """ steal_structure(self, index:int) -> Gst.Structure or None """
        pass

    def subtract(self, subtrahend): # real signature unknown; restored from __doc__
        """ subtract(self, subtrahend:Gst.Caps) -> Gst.Caps """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def truncate(self): # real signature unknown; restored from __doc__
        """ truncate(self) -> Gst.Caps """
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

    mini_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Caps), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstCaps (94058975595808)>, '__dict__': <attribute '__dict__' of 'Caps' objects>, '__weakref__': <attribute '__weakref__' of 'Caps' objects>, '__doc__': None, 'mini_object': <property object at 0x7f4260720950>, 'new_any': gi.FunctionInfo(new_any), 'new_empty': gi.FunctionInfo(new_empty), 'new_empty_simple': gi.FunctionInfo(new_empty_simple), 'append': gi.FunctionInfo(append), 'append_structure': gi.FunctionInfo(append_structure), 'append_structure_full': gi.FunctionInfo(append_structure_full), 'can_intersect': gi.FunctionInfo(can_intersect), 'copy': gi.FunctionInfo(copy), 'copy_nth': gi.FunctionInfo(copy_nth), 'filter_and_map_in_place': gi.FunctionInfo(filter_and_map_in_place), 'fixate': gi.FunctionInfo(fixate), 'foreach': gi.FunctionInfo(foreach), 'get_features': gi.FunctionInfo(get_features), 'get_size': gi.FunctionInfo(get_size), 'get_structure': gi.FunctionInfo(get_structure), 'intersect': gi.FunctionInfo(intersect), 'intersect_full': gi.FunctionInfo(intersect_full), 'is_always_compatible': gi.FunctionInfo(is_always_compatible), 'is_any': gi.FunctionInfo(is_any), 'is_empty': gi.FunctionInfo(is_empty), 'is_equal': gi.FunctionInfo(is_equal), 'is_equal_fixed': gi.FunctionInfo(is_equal_fixed), 'is_fixed': gi.FunctionInfo(is_fixed), 'is_strictly_equal': gi.FunctionInfo(is_strictly_equal), 'is_subset': gi.FunctionInfo(is_subset), 'is_subset_structure': gi.FunctionInfo(is_subset_structure), 'is_subset_structure_full': gi.FunctionInfo(is_subset_structure_full), 'map_in_place': gi.FunctionInfo(map_in_place), 'merge': gi.FunctionInfo(merge), 'merge_structure': gi.FunctionInfo(merge_structure), 'merge_structure_full': gi.FunctionInfo(merge_structure_full), 'normalize': gi.FunctionInfo(normalize), 'remove_structure': gi.FunctionInfo(remove_structure), 'set_features': gi.FunctionInfo(set_features), 'set_features_simple': gi.FunctionInfo(set_features_simple), 'set_value': gi.FunctionInfo(set_value), 'simplify': gi.FunctionInfo(simplify), 'steal_structure': gi.FunctionInfo(steal_structure), 'subtract': gi.FunctionInfo(subtract), 'to_string': gi.FunctionInfo(to_string), 'truncate': gi.FunctionInfo(truncate), 'from_string': gi.FunctionInfo(from_string)})"
    __gtype__ = None # (!) real value is '<GType GstCaps (94058975595808)>'
    __info__ = StructInfo(Caps)


