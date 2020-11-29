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


class ModelReader(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ModelReader()
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

    reader_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    userdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    destroy = gi.FunctionInfo(destroy)
    new = gi.FunctionInfo(new)
    new_for_int32_column = gi.FunctionInfo(new_for_int32_column)
    new_for_string_column = gi.FunctionInfo(new_for_string_column)
    new_for_uint32_column = gi.FunctionInfo(new_for_uint32_column)
    read = gi.FunctionInfo(read)
    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ModelReader), '__module__': 'gi.repository.Dee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ModelReader' objects>, '__weakref__': <attribute '__weakref__' of 'ModelReader' objects>, '__doc__': None, 'reader_func': <property object at 0x7f5a2cf49b38>, 'userdata': <property object at 0x7f5a2cf49b88>, 'destroy': gi.FunctionInfo(destroy), '_padding1': <property object at 0x7f5a2cf49c28>, '_padding2': <property object at 0x7f5a2cf49c78>, '_padding3': <property object at 0x7f5a2cf49cc8>, '_padding4': <property object at 0x7f5a2cf49d18>, '_padding5': <property object at 0x7f5a2cf49d68>, 'read': gi.FunctionInfo(read), 'new': gi.FunctionInfo(new), 'new_for_int32_column': gi.FunctionInfo(new_for_int32_column), 'new_for_string_column': gi.FunctionInfo(new_for_string_column), 'new_for_uint32_column': gi.FunctionInfo(new_for_uint32_column)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ModelReader)


