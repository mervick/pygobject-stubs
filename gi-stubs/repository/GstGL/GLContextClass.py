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


class GLContextClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GLContextClass()
    """
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

    activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    check_feature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    choose_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_current_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_gl_api = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_gl_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_gl_platform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_gl_platform_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_proc_address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    swap_buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLContextClass), '__module__': 'gi.repository.GstGL', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GLContextClass' objects>, '__weakref__': <attribute '__weakref__' of 'GLContextClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f56a3ff09a0>, 'get_current_context': <property object at 0x7f56a3ff0ae0>, 'get_gl_context': <property object at 0x7f56a3ff0bd0>, 'get_gl_api': <property object at 0x7f56a3ff0cc0>, 'get_gl_platform': <property object at 0x7f56a3ff0db0>, 'get_proc_address': <property object at 0x7f56a3ff0ef0>, 'activate': <property object at 0x7f56a3ff0f90>, 'choose_format': <property object at 0x7f56a3ff10e0>, 'create_context': <property object at 0x7f56a3ff11d0>, 'destroy_context': <property object at 0x7f56a3ff12c0>, 'swap_buffers': <property object at 0x7f56a3ff13b0>, 'check_feature': <property object at 0x7f56a3ff14a0>, 'get_gl_platform_version': <property object at 0x7f56a3ff15e0>, '_reserved': <property object at 0x7f56a3ff1680>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GLContextClass)


