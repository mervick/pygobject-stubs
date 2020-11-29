# encoding: utf-8
# module gi.repository.Dee
# from /usr/lib/girepository-1.0/Dee-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Dee as __gi_overrides_Dee
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


from .Model import Model

class Model(Model):
    # no doc
    def append(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def find_row_sorted(self, row_spec, sort_func, data): # reliably restored by inspect
        # no doc
        pass

    def find_sorted(self, sort_func, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def get_row(self, itr): # reliably restored by inspect
        # no doc
        pass

    def get_schema(self): # reliably restored by inspect
        # no doc
        pass

    def get_value(self, itr, column): # reliably restored by inspect
        # no doc
        pass

    def insert(self, pos, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def insert_before(self, iter, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def insert_row_sorted(self, row_spec, sort_func, data): # reliably restored by inspect
        # no doc
        pass

    def insert_sorted(self, sort_func, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def prepend(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def set_column_names(self, *args): # reliably restored by inspect
        # no doc
        pass

    def set_schema(self, *args): # reliably restored by inspect
        # no doc
        pass

    def set_value(self, itr, column, value): # reliably restored by inspect
        # no doc
        pass

    def _build_row(self, args, kwargs): # reliably restored by inspect
        # no doc
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        default dir() implementation
        """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ default object formatter """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, itr): # reliably restored by inspect
        # no doc
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

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
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
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, itr, row): # reliably restored by inspect
        # no doc
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        size of object in memory, in bytes
        """
        return 0

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

    append_row = gi.FunctionInfo(append_row)
    begin_changeset = gi.FunctionInfo(begin_changeset)
    clear = gi.FunctionInfo(clear)
    clear_tag = gi.FunctionInfo(clear_tag)
    end_changeset = gi.FunctionInfo(end_changeset)
    find_row_sorted_with_sizes = gi.FunctionInfo(find_row_sorted_with_sizes)
    get_bool = gi.FunctionInfo(get_bool)
    get_column_index = gi.FunctionInfo(get_column_index)
    get_column_names = gi.FunctionInfo(get_column_names)
    get_column_schema = gi.FunctionInfo(get_column_schema)
    get_double = gi.FunctionInfo(get_double)
    get_field_schema = gi.FunctionInfo(get_field_schema)
    get_first_iter = gi.FunctionInfo(get_first_iter)
    get_int32 = gi.FunctionInfo(get_int32)
    get_int64 = gi.FunctionInfo(get_int64)
    get_iter_at_row = gi.FunctionInfo(get_iter_at_row)
    get_last_iter = gi.FunctionInfo(get_last_iter)
    get_n_columns = gi.FunctionInfo(get_n_columns)
    get_n_rows = gi.FunctionInfo(get_n_rows)
    get_position = gi.FunctionInfo(get_position)
    get_string = gi.FunctionInfo(get_string)
    get_tag = gi.FunctionInfo(get_tag)
    get_uchar = gi.FunctionInfo(get_uchar)
    get_uint32 = gi.FunctionInfo(get_uint32)
    get_uint64 = gi.FunctionInfo(get_uint64)
    get_value_by_name = gi.FunctionInfo(get_value_by_name)
    get_vardict_schema = gi.FunctionInfo(get_vardict_schema)
    insert_row = gi.FunctionInfo(insert_row)
    insert_row_before = gi.FunctionInfo(insert_row_before)
    insert_row_sorted_with_sizes = gi.FunctionInfo(insert_row_sorted_with_sizes)
    is_first = gi.FunctionInfo(is_first)
    is_last = gi.FunctionInfo(is_last)
    next = gi.FunctionInfo(next)
    prepend_row = gi.FunctionInfo(prepend_row)
    prev = gi.FunctionInfo(prev)
    register_tag = gi.FunctionInfo(register_tag)
    register_vardict_schema = gi.FunctionInfo(register_vardict_schema)
    remove = gi.FunctionInfo(remove)
    set_column_names_full = gi.FunctionInfo(set_column_names_full)
    set_row = gi.FunctionInfo(set_row)
    set_schema_full = gi.FunctionInfo(set_schema_full)
    set_tag = gi.FunctionInfo(set_tag)
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Dee', '__init__': <function Model.__init__ at 0x7f5a33652488>, 'set_schema': <function Model.set_schema at 0x7f5a33652510>, 'set_column_names': <function Model.set_column_names at 0x7f5a33652598>, '_build_row': <function Model._build_row at 0x7f5a33652620>, 'prepend': <function Model.prepend at 0x7f5a336526a8>, 'append': <function Model.append at 0x7f5a33652730>, 'insert': <function Model.insert at 0x7f5a336527b8>, 'insert_before': <function Model.insert_before at 0x7f5a33652840>, 'insert_row_sorted': <function Model.insert_row_sorted at 0x7f5a336528c8>, 'insert_sorted': <function Model.insert_sorted at 0x7f5a33652950>, 'find_row_sorted': <function Model.find_row_sorted at 0x7f5a336529d8>, 'find_sorted': <function Model.find_sorted at 0x7f5a33652a60>, 'get_schema': <function Model.get_schema at 0x7f5a33652ae8>, 'get_value': <function Model.get_value at 0x7f5a33652b70>, 'set_value': <function Model.set_value at 0x7f5a33652bf8>, '__getitem__': <function Model.__getitem__ at 0x7f5a33652c80>, '__setitem__': <function Model.__setitem__ at 0x7f5a33652d08>, 'get_row': <function Model.get_row at 0x7f5a33652d90>, '__iter__': <function Model.__iter__ at 0x7f5a33652e18>, '__len__': <function Model.__len__ at 0x7f5a33652ea0>, '__doc__': None, '__gsignals__': {}})"
    __gdoc__ = 'Interface DeeModel\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DeeModel (19107504)>'
    __info__ = InterfaceInfo(Model)


