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


class Meta(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Meta()
    """
    def api_type_get_tags(self, api): # real signature unknown; restored from __doc__
        """ api_type_get_tags(api:GType) -> list """
        return []

    def api_type_has_tag(self, api, tag): # real signature unknown; restored from __doc__
        """ api_type_has_tag(api:GType, tag:int) -> bool """
        return False

    def api_type_register(self, api, tags): # real signature unknown; restored from __doc__
        """ api_type_register(api:str, tags:list) -> GType """
        pass

    def compare_seqnum(self, meta2): # real signature unknown; restored from __doc__
        """ compare_seqnum(self, meta2:Gst.Meta) -> int """
        return 0

    def get_info(self, impl): # real signature unknown; restored from __doc__
        """ get_info(impl:str) -> Gst.MetaInfo or None """
        pass

    def get_seqnum(self): # real signature unknown; restored from __doc__
        """ get_seqnum(self) -> int """
        return 0

    def register(self, api, impl, size, init_func, free_func, transform_func): # real signature unknown; restored from __doc__
        """ register(api:GType, impl:str, size:int, init_func:Gst.MetaInitFunction, free_func:Gst.MetaFreeFunction, transform_func:Gst.MetaTransformFunction) -> Gst.MetaInfo or None """
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Meta), '__module__': 'gi.repository.Gst', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Meta' objects>, '__weakref__': <attribute '__weakref__' of 'Meta' objects>, '__doc__': None, 'flags': <property object at 0x7f4260569e50>, 'info': <property object at 0x7f4260569f40>, 'compare_seqnum': gi.FunctionInfo(compare_seqnum), 'get_seqnum': gi.FunctionInfo(get_seqnum), 'api_type_get_tags': gi.FunctionInfo(api_type_get_tags), 'api_type_has_tag': gi.FunctionInfo(api_type_has_tag), 'api_type_register': gi.FunctionInfo(api_type_register), 'get_info': gi.FunctionInfo(get_info), 'register': gi.FunctionInfo(register)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Meta)


