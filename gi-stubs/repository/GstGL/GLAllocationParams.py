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


class GLAllocationParams(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        GLAllocationParams()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstGL.GLAllocationParams """
        pass

    def copy_data(self, dest): # real signature unknown; restored from __doc__
        """ copy_data(self, dest:GstGL.GLAllocationParams) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def free_data(self): # real signature unknown; restored from __doc__
        """ free_data(self) """
        pass

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

    alloc_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alloc_params = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alloc_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gl_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    struct_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrapped_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLAllocationParams), '__module__': 'gi.repository.GstGL', '__gtype__': <GType GstGLAllocationParams (93979012024176)>, '__dict__': <attribute '__dict__' of 'GLAllocationParams' objects>, '__weakref__': <attribute '__weakref__' of 'GLAllocationParams' objects>, '__doc__': None, 'struct_size': <property object at 0x7f56a3fd6cc0>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'alloc_flags': <property object at 0x7f56a3fd6db0>, 'alloc_size': <property object at 0x7f56a3fd6ea0>, 'alloc_params': <property object at 0x7f56a3fd6f90>, 'context': <property object at 0x7f56a3fd30e0>, 'notify': <property object at 0x7f56a3fd31d0>, 'user_data': <property object at 0x7f56a3fd32c0>, 'wrapped_data': <property object at 0x7f56a3fd33b0>, 'gl_handle': <property object at 0x7f56a3fd34a0>, '_padding': <property object at 0x7f56a3fd3540>, 'copy_data': gi.FunctionInfo(copy_data), 'free_data': gi.FunctionInfo(free_data)})"
    __gtype__ = None # (!) real value is '<GType GstGLAllocationParams (93979012024176)>'
    __info__ = StructInfo(GLAllocationParams)


