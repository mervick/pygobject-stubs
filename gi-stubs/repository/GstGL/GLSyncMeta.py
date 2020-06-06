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


class GLSyncMeta(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GLSyncMeta()
    """
    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info() -> Gst.MetaInfo """
        pass

    def set_sync_point(self, context): # real signature unknown; restored from __doc__
        """ set_sync_point(self, context:GstGL.GLContext) """
        pass

    def wait(self, context): # real signature unknown; restored from __doc__
        """ wait(self, context:GstGL.GLContext) """
        pass

    def wait_cpu(self, context): # real signature unknown; restored from __doc__
        """ wait_cpu(self, context:GstGL.GLContext) """
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

    copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free_gl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_sync_gl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wait_cpu_gl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wait_gl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLSyncMeta), '__module__': 'gi.repository.GstGL', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GLSyncMeta' objects>, '__weakref__': <attribute '__weakref__' of 'GLSyncMeta' objects>, '__doc__': None, 'parent': <property object at 0x7f56a3a32360>, 'context': <property object at 0x7f56a3a32450>, 'data': <property object at 0x7f56a3a32540>, 'set_sync': <property object at 0x7f56a3a32630>, 'set_sync_gl': <property object at 0x7f56a3a32720>, 'wait': gi.FunctionInfo(wait), 'wait_gl': <property object at 0x7f56a3a32900>, 'wait_cpu': gi.FunctionInfo(wait_cpu), 'wait_cpu_gl': <property object at 0x7f56a3a32ae0>, 'copy': <property object at 0x7f56a3a32bd0>, 'free': <property object at 0x7f56a3a32cc0>, 'free_gl': <property object at 0x7f56a3a32db0>, 'set_sync_point': gi.FunctionInfo(set_sync_point), 'get_info': gi.FunctionInfo(get_info)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GLSyncMeta)


