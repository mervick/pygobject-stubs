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


class Filter(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Filter()
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

    map_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    userdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    destroy = gi.FunctionInfo(destroy)
    map = gi.FunctionInfo(map)
    new = gi.FunctionInfo(new)
    new_collator = gi.FunctionInfo(new_collator)
    new_collator_desc = gi.FunctionInfo(new_collator_desc)
    new_for_any_column = gi.FunctionInfo(new_for_any_column)
    new_for_key_column = gi.FunctionInfo(new_for_key_column)
    new_regex = gi.FunctionInfo(new_regex)
    new_sort = gi.FunctionInfo(new_sort)
    notify = gi.FunctionInfo(notify)
    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Filter), '__module__': 'gi.repository.Dee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Filter' objects>, '__weakref__': <attribute '__weakref__' of 'Filter' objects>, '__doc__': None, 'map_func': <property object at 0x7f5a2cf3c638>, 'map_notify': <property object at 0x7f5a2cf3c688>, 'destroy': gi.FunctionInfo(destroy), 'userdata': <property object at 0x7f5a2cf3c728>, '_padding_1': <property object at 0x7f5a2cf3c778>, '_padding_2': <property object at 0x7f5a2cf3c7c8>, '_padding_3': <property object at 0x7f5a2cf3c818>, '_padding_4': <property object at 0x7f5a2cf3c868>, 'map': gi.FunctionInfo(map), 'notify': gi.FunctionInfo(notify), 'new': gi.FunctionInfo(new), 'new_collator': gi.FunctionInfo(new_collator), 'new_collator_desc': gi.FunctionInfo(new_collator_desc), 'new_for_any_column': gi.FunctionInfo(new_for_any_column), 'new_for_key_column': gi.FunctionInfo(new_for_key_column), 'new_regex': gi.FunctionInfo(new_regex), 'new_sort': gi.FunctionInfo(new_sort)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Filter)


