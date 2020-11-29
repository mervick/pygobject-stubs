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


class ResultSetIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ResultSetIface()
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

    get_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    peek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_result_set_1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_result_set_2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_result_set_3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_result_set_4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _dee_result_set_5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ResultSetIface), '__module__': 'gi.repository.Dee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ResultSetIface' objects>, '__weakref__': <attribute '__weakref__' of 'ResultSetIface' objects>, '__doc__': None, 'g_iface': <property object at 0x7f5a2cf4dae8>, 'get_n_rows': <property object at 0x7f5a2cf4db38>, 'next': <property object at 0x7f5a2cf4db88>, 'has_next': <property object at 0x7f5a2cf4dbd8>, 'peek': <property object at 0x7f5a2cf4dc28>, 'seek': <property object at 0x7f5a2cf4dc78>, 'tell': <property object at 0x7f5a2cf4dcc8>, 'get_model': <property object at 0x7f5a2cf4dd18>, '_dee_result_set_1': <property object at 0x7f5a2cf4dd68>, '_dee_result_set_2': <property object at 0x7f5a2cf4ddb8>, '_dee_result_set_3': <property object at 0x7f5a2cf4de08>, '_dee_result_set_4': <property object at 0x7f5a2cf4de58>, '_dee_result_set_5': <property object at 0x7f5a2cf4dea8>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ResultSetIface)


