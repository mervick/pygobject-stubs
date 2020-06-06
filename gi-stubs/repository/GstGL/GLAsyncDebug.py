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


class GLAsyncDebug(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GLAsyncDebug()
    """
    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def freeze(self): # real signature unknown; restored from __doc__
        """ freeze(self) """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def output_log_msg(self): # real signature unknown; restored from __doc__
        """ output_log_msg(self) """
        pass

    def thaw(self): # real signature unknown; restored from __doc__
        """ thaw(self) """
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

    callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    debug_msg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLAsyncDebug), '__module__': 'gi.repository.GstGL', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GLAsyncDebug' objects>, '__weakref__': <attribute '__weakref__' of 'GLAsyncDebug' objects>, '__doc__': None, 'state_flags': <property object at 0x7f56a3fd3590>, 'cat': <property object at 0x7f56a3fd35e0>, 'level': <property object at 0x7f56a3fd3680>, 'file': <property object at 0x7f56a3fd3770>, 'function': <property object at 0x7f56a3fd3860>, 'line': <property object at 0x7f56a3fd3950>, 'object': <property object at 0x7f56a3fd3a40>, 'debug_msg': <property object at 0x7f56a3fd3b30>, 'callback': <property object at 0x7f56a3fd3c20>, 'user_data': <property object at 0x7f56a3fd3d10>, 'notify': <property object at 0x7f56a3fd3e00>, '_padding': <property object at 0x7f56a3fd3ef0>, 'free': gi.FunctionInfo(free), 'freeze': gi.FunctionInfo(freeze), 'init': gi.FunctionInfo(init), 'output_log_msg': gi.FunctionInfo(output_log_msg), 'thaw': gi.FunctionInfo(thaw), 'unset': gi.FunctionInfo(unset)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GLAsyncDebug)


