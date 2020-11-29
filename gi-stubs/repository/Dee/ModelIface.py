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


class ModelIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ModelIface()
    """
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

    append_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    begin_changeset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changeset_finished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changeset_started = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_changeset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_row_sorted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_bool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_column_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_column_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_column_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_field_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_first_iter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_int32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_int64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_iter_at_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_last_iter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uchar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uint32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uint64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_value_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_vardict_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_row_before = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    insert_row_sorted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_first = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_last = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prepend_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    register_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    register_vardict_schema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    row_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_column_names_full = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_row = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_schema_full = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_model_1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_model_2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_model_3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ModelIface), '__module__': 'gi.repository.Dee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ModelIface' objects>, '__weakref__': <attribute '__weakref__' of 'ModelIface' objects>, '__doc__': None, 'g_iface': <property object at 0x7f5a2cf43958>, 'row_added': <property object at 0x7f5a2cf439a8>, 'row_removed': <property object at 0x7f5a2cf439f8>, 'row_changed': <property object at 0x7f5a2cf43a48>, 'set_schema_full': <property object at 0x7f5a2cf43a98>, 'get_schema': <property object at 0x7f5a2cf43ae8>, 'get_column_schema': <property object at 0x7f5a2cf43b38>, 'get_field_schema': <property object at 0x7f5a2cf43b88>, 'get_column_index': <property object at 0x7f5a2cf43bd8>, 'set_column_names_full': <property object at 0x7f5a2cf43c28>, 'get_column_names': <property object at 0x7f5a2cf43c78>, 'register_vardict_schema': <property object at 0x7f5a2cf43cc8>, 'get_vardict_schema': <property object at 0x7f5a2cf43d18>, 'get_n_columns': <property object at 0x7f5a2cf43d68>, 'get_n_rows': <property object at 0x7f5a2cf43db8>, 'append_row': <property object at 0x7f5a2cf43e08>, 'prepend_row': <property object at 0x7f5a2cf43e58>, 'insert_row': <property object at 0x7f5a2cf43ea8>, 'insert_row_before': <property object at 0x7f5a2cf43ef8>, 'insert_row_sorted': <property object at 0x7f5a2cf43f48>, 'find_row_sorted': <property object at 0x7f5a2cf43f98>, 'remove': <property object at 0x7f5a2cf49048>, 'clear': <property object at 0x7f5a2cf49098>, 'set_value': <property object at 0x7f5a2cf490e8>, 'set_row': <property object at 0x7f5a2cf49138>, 'get_value': <property object at 0x7f5a2cf49188>, 'get_value_by_name': <property object at 0x7f5a2cf491d8>, 'get_first_iter': <property object at 0x7f5a2cf49228>, 'get_last_iter': <property object at 0x7f5a2cf49278>, 'get_iter_at_row': <property object at 0x7f5a2cf492c8>, 'get_bool': <property object at 0x7f5a2cf49318>, 'get_uchar': <property object at 0x7f5a2cf49368>, 'get_int32': <property object at 0x7f5a2cf493b8>, 'get_uint32': <property object at 0x7f5a2cf49408>, 'get_int64': <property object at 0x7f5a2cf49458>, 'get_uint64': <property object at 0x7f5a2cf494a8>, 'get_double': <property object at 0x7f5a2cf494f8>, 'get_string': <property object at 0x7f5a2cf49548>, 'next': <property object at 0x7f5a2cf49598>, 'prev': <property object at 0x7f5a2cf495e8>, 'is_first': <property object at 0x7f5a2cf49638>, 'is_last': <property object at 0x7f5a2cf49688>, 'get_position': <property object at 0x7f5a2cf496d8>, 'register_tag': <property object at 0x7f5a2cf49728>, 'get_tag': <property object at 0x7f5a2cf49778>, 'set_tag': <property object at 0x7f5a2cf497c8>, 'get_row': <property object at 0x7f5a2cf49818>, 'begin_changeset': <property object at 0x7f5a2cf49868>, 'end_changeset': <property object at 0x7f5a2cf498b8>, 'changeset_started': <property object at 0x7f5a2cf49908>, 'changeset_finished': <property object at 0x7f5a2cf49958>, '_dee_model_1': <property object at 0x7f5a2cf499a8>, '_dee_model_2': <property object at 0x7f5a2cf499f8>, '_dee_model_3': <property object at 0x7f5a2cf49a48>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ModelIface)


