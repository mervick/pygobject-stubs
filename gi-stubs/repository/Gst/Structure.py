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


class Structure(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Structure()
        new_empty(name:str) -> Gst.Structure
        new_from_string(string:str) -> Gst.Structure or None
        new_id_empty(quark:int) -> Gst.Structure
    """
    def can_intersect(self, struct2): # real signature unknown; restored from __doc__
        """ can_intersect(self, struct2:Gst.Structure) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gst.Structure """
        pass

    def filter_and_map_in_place(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ filter_and_map_in_place(self, func:Gst.StructureFilterMapFunc, user_data=None) """
        pass

    def fixate(self): # real signature unknown; restored from __doc__
        """ fixate(self) """
        pass

    def fixate_field(self, field_name): # real signature unknown; restored from __doc__
        """ fixate_field(self, field_name:str) -> bool """
        return False

    def fixate_field_boolean(self, field_name, target): # real signature unknown; restored from __doc__
        """ fixate_field_boolean(self, field_name:str, target:bool) -> bool """
        return False

    def fixate_field_nearest_double(self, field_name, target): # real signature unknown; restored from __doc__
        """ fixate_field_nearest_double(self, field_name:str, target:float) -> bool """
        return False

    def fixate_field_nearest_fraction(self, field_name, target_numerator, target_denominator): # real signature unknown; restored from __doc__
        """ fixate_field_nearest_fraction(self, field_name:str, target_numerator:int, target_denominator:int) -> bool """
        return False

    def fixate_field_nearest_int(self, field_name, target): # real signature unknown; restored from __doc__
        """ fixate_field_nearest_int(self, field_name:str, target:int) -> bool """
        return False

    def fixate_field_string(self, field_name, target): # real signature unknown; restored from __doc__
        """ fixate_field_string(self, field_name:str, target:str) -> bool """
        return False

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gst.StructureForeachFunc, user_data=None) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_string(self, string): # real signature unknown; restored from __doc__
        """ from_string(string:str) -> Gst.Structure or None, end:str """
        pass

    def get_array(self, fieldname): # real signature unknown; restored from __doc__
        """ get_array(self, fieldname:str) -> bool, array:GObject.ValueArray """
        return False

    def get_boolean(self, fieldname): # real signature unknown; restored from __doc__
        """ get_boolean(self, fieldname:str) -> bool, value:bool """
        return False

    def get_clock_time(self, fieldname): # real signature unknown; restored from __doc__
        """ get_clock_time(self, fieldname:str) -> bool, value:int """
        return False

    def get_date(self, fieldname): # real signature unknown; restored from __doc__
        """ get_date(self, fieldname:str) -> bool, value:GLib.Date """
        return False

    def get_date_time(self, fieldname): # real signature unknown; restored from __doc__
        """ get_date_time(self, fieldname:str) -> bool, value:Gst.DateTime """
        return False

    def get_double(self, fieldname): # real signature unknown; restored from __doc__
        """ get_double(self, fieldname:str) -> bool, value:float """
        return False

    def get_enum(self, fieldname, enumtype): # real signature unknown; restored from __doc__
        """ get_enum(self, fieldname:str, enumtype:GType) -> bool, value:int """
        return False

    def get_field_type(self, fieldname): # real signature unknown; restored from __doc__
        """ get_field_type(self, fieldname:str) -> GType """
        pass

    def get_flagset(self, fieldname): # real signature unknown; restored from __doc__
        """ get_flagset(self, fieldname:str) -> bool, value_flags:int, value_mask:int """
        return False

    def get_fraction(self, fieldname): # real signature unknown; restored from __doc__
        """ get_fraction(self, fieldname:str) -> bool, value_numerator:int, value_denominator:int """
        return False

    def get_int(self, fieldname): # real signature unknown; restored from __doc__
        """ get_int(self, fieldname:str) -> bool, value:int """
        return False

    def get_int64(self, fieldname): # real signature unknown; restored from __doc__
        """ get_int64(self, fieldname:str) -> bool, value:int """
        return False

    def get_list(self, fieldname): # real signature unknown; restored from __doc__
        """ get_list(self, fieldname:str) -> bool, array:GObject.ValueArray """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_name_id(self): # real signature unknown; restored from __doc__
        """ get_name_id(self) -> int """
        return 0

    def get_string(self, fieldname): # real signature unknown; restored from __doc__
        """ get_string(self, fieldname:str) -> str or None """
        return ""

    def get_uint(self, fieldname): # real signature unknown; restored from __doc__
        """ get_uint(self, fieldname:str) -> bool, value:int """
        return False

    def get_uint64(self, fieldname): # real signature unknown; restored from __doc__
        """ get_uint64(self, fieldname:str) -> bool, value:int """
        return False

    def get_value(self, fieldname): # real signature unknown; restored from __doc__
        """ get_value(self, fieldname:str) -> GObject.Value or None """
        pass

    def has_field(self, fieldname): # real signature unknown; restored from __doc__
        """ has_field(self, fieldname:str) -> bool """
        return False

    def has_field_typed(self, fieldname, type): # real signature unknown; restored from __doc__
        """ has_field_typed(self, fieldname:str, type:GType) -> bool """
        return False

    def has_name(self, name): # real signature unknown; restored from __doc__
        """ has_name(self, name:str) -> bool """
        return False

    def id_get_value(self, field): # real signature unknown; restored from __doc__
        """ id_get_value(self, field:int) -> GObject.Value or None """
        pass

    def id_has_field(self, field): # real signature unknown; restored from __doc__
        """ id_has_field(self, field:int) -> bool """
        return False

    def id_has_field_typed(self, field, type): # real signature unknown; restored from __doc__
        """ id_has_field_typed(self, field:int, type:GType) -> bool """
        return False

    def id_set_value(self, field, value): # real signature unknown; restored from __doc__
        """ id_set_value(self, field:int, value:GObject.Value) """
        pass

    def id_take_value(self, field, value): # real signature unknown; restored from __doc__
        """ id_take_value(self, field:int, value:GObject.Value) """
        pass

    def intersect(self, struct2): # real signature unknown; restored from __doc__
        """ intersect(self, struct2:Gst.Structure) -> Gst.Structure or None """
        pass

    def is_equal(self, structure2): # real signature unknown; restored from __doc__
        """ is_equal(self, structure2:Gst.Structure) -> bool """
        return False

    def is_subset(self, superset): # real signature unknown; restored from __doc__
        """ is_subset(self, superset:Gst.Structure) -> bool """
        return False

    def map_in_place(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ map_in_place(self, func:Gst.StructureMapFunc, user_data=None) -> bool """
        return False

    def new_empty(self, name): # real signature unknown; restored from __doc__
        """ new_empty(name:str) -> Gst.Structure """
        pass

    def new_from_string(self, string): # real signature unknown; restored from __doc__
        """ new_from_string(string:str) -> Gst.Structure or None """
        pass

    def new_id_empty(self, quark): # real signature unknown; restored from __doc__
        """ new_id_empty(quark:int) -> Gst.Structure """
        pass

    def nth_field_name(self, index): # real signature unknown; restored from __doc__
        """ nth_field_name(self, index:int) -> str """
        return ""

    def n_fields(self): # real signature unknown; restored from __doc__
        """ n_fields(self) -> int """
        return 0

    def remove_all_fields(self): # real signature unknown; restored from __doc__
        """ remove_all_fields(self) """
        pass

    def remove_field(self, fieldname): # real signature unknown; restored from __doc__
        """ remove_field(self, fieldname:str) """
        pass

    def set_array(self, fieldname, array): # real signature unknown; restored from __doc__
        """ set_array(self, fieldname:str, array:GObject.ValueArray) """
        pass

    def set_list(self, fieldname, array): # real signature unknown; restored from __doc__
        """ set_list(self, fieldname:str, array:GObject.ValueArray) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent_refcount(self, refcount): # real signature unknown; restored from __doc__
        """ set_parent_refcount(self, refcount:int) -> bool """
        return False

    def set_value(self, fieldname, value): # real signature unknown; restored from __doc__
        """ set_value(self, fieldname:str, value:GObject.Value) """
        pass

    def take_value(self, fieldname, value): # real signature unknown; restored from __doc__
        """ take_value(self, fieldname:str, value:GObject.Value) """
        pass

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

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Structure), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstStructure (94058977991664)>, '__dict__': <attribute '__dict__' of 'Structure' objects>, '__weakref__': <attribute '__weakref__' of 'Structure' objects>, '__doc__': None, 'type': <property object at 0x7f4260521f40>, 'name': <property object at 0x7f4260523090>, 'new_empty': gi.FunctionInfo(new_empty), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_id_empty': gi.FunctionInfo(new_id_empty), 'can_intersect': gi.FunctionInfo(can_intersect), 'copy': gi.FunctionInfo(copy), 'filter_and_map_in_place': gi.FunctionInfo(filter_and_map_in_place), 'fixate': gi.FunctionInfo(fixate), 'fixate_field': gi.FunctionInfo(fixate_field), 'fixate_field_boolean': gi.FunctionInfo(fixate_field_boolean), 'fixate_field_nearest_double': gi.FunctionInfo(fixate_field_nearest_double), 'fixate_field_nearest_fraction': gi.FunctionInfo(fixate_field_nearest_fraction), 'fixate_field_nearest_int': gi.FunctionInfo(fixate_field_nearest_int), 'fixate_field_string': gi.FunctionInfo(fixate_field_string), 'foreach': gi.FunctionInfo(foreach), 'free': gi.FunctionInfo(free), 'get_array': gi.FunctionInfo(get_array), 'get_boolean': gi.FunctionInfo(get_boolean), 'get_clock_time': gi.FunctionInfo(get_clock_time), 'get_date': gi.FunctionInfo(get_date), 'get_date_time': gi.FunctionInfo(get_date_time), 'get_double': gi.FunctionInfo(get_double), 'get_enum': gi.FunctionInfo(get_enum), 'get_field_type': gi.FunctionInfo(get_field_type), 'get_flagset': gi.FunctionInfo(get_flagset), 'get_fraction': gi.FunctionInfo(get_fraction), 'get_int': gi.FunctionInfo(get_int), 'get_int64': gi.FunctionInfo(get_int64), 'get_list': gi.FunctionInfo(get_list), 'get_name': gi.FunctionInfo(get_name), 'get_name_id': gi.FunctionInfo(get_name_id), 'get_string': gi.FunctionInfo(get_string), 'get_uint': gi.FunctionInfo(get_uint), 'get_uint64': gi.FunctionInfo(get_uint64), 'get_value': gi.FunctionInfo(get_value), 'has_field': gi.FunctionInfo(has_field), 'has_field_typed': gi.FunctionInfo(has_field_typed), 'has_name': gi.FunctionInfo(has_name), 'id_get_value': gi.FunctionInfo(id_get_value), 'id_has_field': gi.FunctionInfo(id_has_field), 'id_has_field_typed': gi.FunctionInfo(id_has_field_typed), 'id_set_value': gi.FunctionInfo(id_set_value), 'id_take_value': gi.FunctionInfo(id_take_value), 'intersect': gi.FunctionInfo(intersect), 'is_equal': gi.FunctionInfo(is_equal), 'is_subset': gi.FunctionInfo(is_subset), 'map_in_place': gi.FunctionInfo(map_in_place), 'n_fields': gi.FunctionInfo(n_fields), 'nth_field_name': gi.FunctionInfo(nth_field_name), 'remove_all_fields': gi.FunctionInfo(remove_all_fields), 'remove_field': gi.FunctionInfo(remove_field), 'set_array': gi.FunctionInfo(set_array), 'set_list': gi.FunctionInfo(set_list), 'set_name': gi.FunctionInfo(set_name), 'set_parent_refcount': gi.FunctionInfo(set_parent_refcount), 'set_value': gi.FunctionInfo(set_value), 'take_value': gi.FunctionInfo(take_value), 'to_string': gi.FunctionInfo(to_string), 'from_string': gi.FunctionInfo(from_string)})"
    __gtype__ = None # (!) real value is '<GType GstStructure (94058977991664)>'
    __info__ = StructInfo(Structure)


