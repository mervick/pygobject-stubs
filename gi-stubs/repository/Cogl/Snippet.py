# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
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
import gobject as __gobject


from .Object import Object

class Snippet(Object):
    """
    :Constructors:
    
    ::
    
        Snippet(**properties)
        new(hook:Cogl.SnippetHook, declarations:str, post:str) -> Cogl.Snippet
    """
    def get_declarations(self): # real signature unknown; restored from __doc__
        """ get_declarations(self) -> str """
        return ""

    def get_hook(self): # real signature unknown; restored from __doc__
        """ get_hook(self) -> Cogl.SnippetHook """
        pass

    def get_post(self): # real signature unknown; restored from __doc__
        """ get_post(self) -> str """
        return ""

    def get_pre(self): # real signature unknown; restored from __doc__
        """ get_pre(self) -> str """
        return ""

    def get_replace(self): # real signature unknown; restored from __doc__
        """ get_replace(self) -> str """
        return ""

    def new(self, hook, declarations, post): # real signature unknown; restored from __doc__
        """ new(hook:Cogl.SnippetHook, declarations:str, post:str) -> Cogl.Snippet """
        pass

    def set_declarations(self, declarations): # real signature unknown; restored from __doc__
        """ set_declarations(self, declarations:str) """
        pass

    def set_post(self, post): # real signature unknown; restored from __doc__
        """ set_post(self, post:str) """
        pass

    def set_pre(self, pre): # real signature unknown; restored from __doc__
        """ set_pre(self, pre:str) """
        pass

    def set_replace(self, replace): # real signature unknown; restored from __doc__
        """ set_replace(self, replace:str) """
        pass

    def value_get_object(self, value): # real signature unknown; restored from __doc__
        """ value_get_object(value:GObject.Value) """
        pass

    def value_set_object(self, value, p_object=None): # real signature unknown; restored from __doc__
        """ value_set_object(value:GObject.Value, object=None) """
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Snippet), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglSnippet (93970932115632)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_declarations': gi.FunctionInfo(get_declarations), 'get_hook': gi.FunctionInfo(get_hook), 'get_post': gi.FunctionInfo(get_post), 'get_pre': gi.FunctionInfo(get_pre), 'get_replace': gi.FunctionInfo(get_replace), 'set_declarations': gi.FunctionInfo(set_declarations), 'set_post': gi.FunctionInfo(set_post), 'set_pre': gi.FunctionInfo(set_pre), 'set_replace': gi.FunctionInfo(set_replace)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglSnippet (93970932115632)>'
    __info__ = ObjectInfo(Snippet)


