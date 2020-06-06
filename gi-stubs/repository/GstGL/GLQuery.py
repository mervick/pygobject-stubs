# encoding: utf-8
# module gi.repository.GstGL
# from /usr/lib64/girepository-1.0/GstGL-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class GLQuery(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GLQuery()
    """
    def counter(self): # real signature unknown; restored from __doc__
        """ counter(self) """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self, context, query_type): # real signature unknown; restored from __doc__
        """ init(self, context:GstGL.GLContext, query_type:GstGL.GLQueryType) """
        pass

    def local_gl_context(self, element, direction, context_ptr): # real signature unknown; restored from __doc__
        """ local_gl_context(element:Gst.Element, direction:Gst.PadDirection, context_ptr:GstGL.GLContext) -> bool, context_ptr:GstGL.GLContext """
        return False

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def unset(self): # real signature unknown; restored from __doc__
        """ unset(self) """
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

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    debug = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_called = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLQuery), '__module__': 'gi.repository.GstGL', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GLQuery' objects>, '__weakref__': <attribute '__weakref__' of 'GLQuery' objects>, '__doc__': None, 'context': <property object at 0x7f56a3a260e0>, 'query_type': <property object at 0x7f56a3a261d0>, 'query_id': <property object at 0x7f56a3a262c0>, 'supported': <property object at 0x7f56a3a263b0>, 'start_called': <property object at 0x7f56a3a264a0>, 'debug': <property object at 0x7f56a3a26590>, '_padding': <property object at 0x7f56a3a26680>, 'counter': gi.FunctionInfo(counter), 'end': gi.FunctionInfo(end), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init), 'result': gi.FunctionInfo(result), 'start': gi.FunctionInfo(start), 'unset': gi.FunctionInfo(unset), 'local_gl_context': gi.FunctionInfo(local_gl_context)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GLQuery)


