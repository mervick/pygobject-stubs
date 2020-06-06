# encoding: utf-8
# module gi.repository.Colord
# from /usr/lib64/girepository-1.0/Colord-1.0.typelib
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
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class Vec3(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Vec3()
    """
    def add(self, src2, dest): # real signature unknown; restored from __doc__
        """ add(self, src2:Colord.Vec3, dest:Colord.Vec3) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self, dest): # real signature unknown; restored from __doc__
        """ copy(self, dest:Colord.Vec3) """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> float """
        return 0.0

    def init(self, v0, v1, v2): # real signature unknown; restored from __doc__
        """ init(self, v0:float, v1:float, v2:float) """
        pass

    def scalar_multiply(self, value, dest): # real signature unknown; restored from __doc__
        """ scalar_multiply(self, value:float, dest:Colord.Vec3) """
        pass

    def squared_error(self, src2): # real signature unknown; restored from __doc__
        """ squared_error(self, src2:Colord.Vec3) -> float """
        return 0.0

    def subtract(self, src2, dest): # real signature unknown; restored from __doc__
        """ subtract(self, src2:Colord.Vec3, dest:Colord.Vec3) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    v0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    v2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Vec3), '__module__': 'gi.repository.Colord', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Vec3' objects>, '__weakref__': <attribute '__weakref__' of 'Vec3' objects>, '__doc__': None, 'v0': <property object at 0x7f09131e8e50>, 'v1': <property object at 0x7f09131e8f40>, 'v2': <property object at 0x7f09131ec090>, 'add': gi.FunctionInfo(add), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'get_data': gi.FunctionInfo(get_data), 'init': gi.FunctionInfo(init), 'scalar_multiply': gi.FunctionInfo(scalar_multiply), 'squared_error': gi.FunctionInfo(squared_error), 'subtract': gi.FunctionInfo(subtract), 'to_string': gi.FunctionInfo(to_string)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Vec3)


