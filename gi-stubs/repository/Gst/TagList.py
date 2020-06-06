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


class TagList(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        TagList()
        new_empty() -> Gst.TagList
        new_from_string(str:str) -> Gst.TagList or None
    """
    def add_value(self, mode, tag, value): # real signature unknown; restored from __doc__
        """ add_value(self, mode:Gst.TagMergeMode, tag:str, value:GObject.Value) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copy_value(self, p_list, tag): # real signature unknown; restored from __doc__
        """ copy_value(list:Gst.TagList, tag:str) -> bool, dest:GObject.Value """
        return False

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gst.TagForeachFunc, user_data=None) """
        pass

    def get_boolean(self, tag): # real signature unknown; restored from __doc__
        """ get_boolean(self, tag:str) -> bool, value:bool """
        return False

    def get_boolean_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_boolean_index(self, tag:str, index:int) -> bool, value:bool """
        return False

    def get_date(self, tag): # real signature unknown; restored from __doc__
        """ get_date(self, tag:str) -> bool, value:GLib.Date """
        return False

    def get_date_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_date_index(self, tag:str, index:int) -> bool, value:GLib.Date """
        return False

    def get_date_time(self, tag): # real signature unknown; restored from __doc__
        """ get_date_time(self, tag:str) -> bool, value:Gst.DateTime """
        return False

    def get_date_time_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_date_time_index(self, tag:str, index:int) -> bool, value:Gst.DateTime """
        return False

    def get_double(self, tag): # real signature unknown; restored from __doc__
        """ get_double(self, tag:str) -> bool, value:float """
        return False

    def get_double_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_double_index(self, tag:str, index:int) -> bool, value:float """
        return False

    def get_float(self, tag): # real signature unknown; restored from __doc__
        """ get_float(self, tag:str) -> bool, value:float """
        return False

    def get_float_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_float_index(self, tag:str, index:int) -> bool, value:float """
        return False

    def get_int(self, tag): # real signature unknown; restored from __doc__
        """ get_int(self, tag:str) -> bool, value:int """
        return False

    def get_int64(self, tag): # real signature unknown; restored from __doc__
        """ get_int64(self, tag:str) -> bool, value:int """
        return False

    def get_int64_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_int64_index(self, tag:str, index:int) -> bool, value:int """
        return False

    def get_int_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_int_index(self, tag:str, index:int) -> bool, value:int """
        return False

    def get_pointer(self, tag): # real signature unknown; restored from __doc__
        """ get_pointer(self, tag:str) -> bool, value """
        return False

    def get_pointer_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_pointer_index(self, tag:str, index:int) -> bool, value """
        return False

    def get_sample(self, tag): # real signature unknown; restored from __doc__
        """ get_sample(self, tag:str) -> bool, sample:Gst.Sample """
        return False

    def get_sample_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_sample_index(self, tag:str, index:int) -> bool, sample:Gst.Sample """
        return False

    def get_scope(self): # real signature unknown; restored from __doc__
        """ get_scope(self) -> Gst.TagScope """
        pass

    def get_string(self, tag): # real signature unknown; restored from __doc__
        """ get_string(self, tag:str) -> bool, value:str """
        return False

    def get_string_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_string_index(self, tag:str, index:int) -> bool, value:str """
        return False

    def get_tag_size(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_size(self, tag:str) -> int """
        return 0

    def get_uint(self, tag): # real signature unknown; restored from __doc__
        """ get_uint(self, tag:str) -> bool, value:int """
        return False

    def get_uint64(self, tag): # real signature unknown; restored from __doc__
        """ get_uint64(self, tag:str) -> bool, value:int """
        return False

    def get_uint64_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_uint64_index(self, tag:str, index:int) -> bool, value:int """
        return False

    def get_uint_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_uint_index(self, tag:str, index:int) -> bool, value:int """
        return False

    def get_value_index(self, tag, index): # real signature unknown; restored from __doc__
        """ get_value_index(self, tag:str, index:int) -> GObject.Value or None """
        pass

    def insert(self, from_, mode): # real signature unknown; restored from __doc__
        """ insert(self, from_:Gst.TagList, mode:Gst.TagMergeMode) """
        pass

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def is_equal(self, list2): # real signature unknown; restored from __doc__
        """ is_equal(self, list2:Gst.TagList) -> bool """
        return False

    def merge(self, list2=None, mode): # real signature unknown; restored from __doc__
        """ merge(self, list2:Gst.TagList=None, mode:Gst.TagMergeMode) -> Gst.TagList or None """
        pass

    def new_empty(self): # real signature unknown; restored from __doc__
        """ new_empty() -> Gst.TagList """
        pass

    def new_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_from_string(str:str) -> Gst.TagList or None """
        pass

    def nth_tag_name(self, index): # real signature unknown; restored from __doc__
        """ nth_tag_name(self, index:int) -> str """
        return ""

    def n_tags(self): # real signature unknown; restored from __doc__
        """ n_tags(self) -> int """
        return 0

    def peek_string_index(self, tag, index): # real signature unknown; restored from __doc__
        """ peek_string_index(self, tag:str, index:int) -> bool, value:str """
        return False

    def remove_tag(self, tag): # real signature unknown; restored from __doc__
        """ remove_tag(self, tag:str) """
        pass

    def set_scope(self, scope): # real signature unknown; restored from __doc__
        """ set_scope(self, scope:Gst.TagScope) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str or None """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TagList), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstTagList (94058977642896)>, '__dict__': <attribute '__dict__' of 'TagList' objects>, '__weakref__': <attribute '__weakref__' of 'TagList' objects>, '__doc__': None, 'mini_object': <property object at 0x7f4260527720>, 'new_empty': gi.FunctionInfo(new_empty), 'new_from_string': gi.FunctionInfo(new_from_string), 'add_value': gi.FunctionInfo(add_value), 'foreach': gi.FunctionInfo(foreach), 'get_boolean': gi.FunctionInfo(get_boolean), 'get_boolean_index': gi.FunctionInfo(get_boolean_index), 'get_date': gi.FunctionInfo(get_date), 'get_date_index': gi.FunctionInfo(get_date_index), 'get_date_time': gi.FunctionInfo(get_date_time), 'get_date_time_index': gi.FunctionInfo(get_date_time_index), 'get_double': gi.FunctionInfo(get_double), 'get_double_index': gi.FunctionInfo(get_double_index), 'get_float': gi.FunctionInfo(get_float), 'get_float_index': gi.FunctionInfo(get_float_index), 'get_int': gi.FunctionInfo(get_int), 'get_int64': gi.FunctionInfo(get_int64), 'get_int64_index': gi.FunctionInfo(get_int64_index), 'get_int_index': gi.FunctionInfo(get_int_index), 'get_pointer': gi.FunctionInfo(get_pointer), 'get_pointer_index': gi.FunctionInfo(get_pointer_index), 'get_sample': gi.FunctionInfo(get_sample), 'get_sample_index': gi.FunctionInfo(get_sample_index), 'get_scope': gi.FunctionInfo(get_scope), 'get_string': gi.FunctionInfo(get_string), 'get_string_index': gi.FunctionInfo(get_string_index), 'get_tag_size': gi.FunctionInfo(get_tag_size), 'get_uint': gi.FunctionInfo(get_uint), 'get_uint64': gi.FunctionInfo(get_uint64), 'get_uint64_index': gi.FunctionInfo(get_uint64_index), 'get_uint_index': gi.FunctionInfo(get_uint_index), 'get_value_index': gi.FunctionInfo(get_value_index), 'insert': gi.FunctionInfo(insert), 'is_empty': gi.FunctionInfo(is_empty), 'is_equal': gi.FunctionInfo(is_equal), 'merge': gi.FunctionInfo(merge), 'n_tags': gi.FunctionInfo(n_tags), 'nth_tag_name': gi.FunctionInfo(nth_tag_name), 'peek_string_index': gi.FunctionInfo(peek_string_index), 'remove_tag': gi.FunctionInfo(remove_tag), 'set_scope': gi.FunctionInfo(set_scope), 'to_string': gi.FunctionInfo(to_string), 'copy_value': gi.FunctionInfo(copy_value)})"
    __gtype__ = None # (!) real value is '<GType GstTagList (94058977642896)>'
    __info__ = StructInfo(TagList)


