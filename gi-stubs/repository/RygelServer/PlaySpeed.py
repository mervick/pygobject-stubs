# encoding: utf-8
# module gi.repository.RygelServer
# from /usr/lib64/girepository-1.0/RygelServer-2.6.typelib
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
import gi.repository.Gee as __gi_repository_Gee
import gi.repository.GUPnP as __gi_repository_GUPnP
import gi.repository.RygelCore as __gi_repository_RygelCore
import gobject as __gobject


class PlaySpeed(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PlaySpeed()
        new(numerator:int, denominator:int) -> RygelServer.PlaySpeed
        from_string(speed:str) -> RygelServer.PlaySpeed
    """
    def equals(self, that): # real signature unknown; restored from __doc__
        """ equals(self, that:RygelServer.PlaySpeed) -> bool """
        return False

    def from_string(self, speed): # real signature unknown; restored from __doc__
        """ from_string(speed:str) -> RygelServer.PlaySpeed """
        pass

    def is_normal_rate(self): # real signature unknown; restored from __doc__
        """ is_normal_rate(self) -> bool """
        return False

    def is_positive(self): # real signature unknown; restored from __doc__
        """ is_positive(self) -> bool """
        return False

    def new(self, numerator, denominator): # real signature unknown; restored from __doc__
        """ new(numerator:int, denominator:int) -> RygelServer.PlaySpeed """
        pass

    def to_double(self): # real signature unknown; restored from __doc__
        """ to_double(self) -> float """
        return 0.0

    def to_float(self): # real signature unknown; restored from __doc__
        """ to_float(self) -> float """
        return 0.0

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

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PlaySpeed), '__module__': 'gi.repository.RygelServer', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PlaySpeed' objects>, '__weakref__': <attribute '__weakref__' of 'PlaySpeed' objects>, '__doc__': None, 'numerator': <property object at 0x7fe1d16828b0>, 'denominator': <property object at 0x7fe1d16829a0>, 'new': gi.FunctionInfo(new), 'from_string': gi.FunctionInfo(from_string), 'equals': gi.FunctionInfo(equals), 'is_positive': gi.FunctionInfo(is_positive), 'is_normal_rate': gi.FunctionInfo(is_normal_rate), 'to_string': gi.FunctionInfo(to_string), 'to_float': gi.FunctionInfo(to_float), 'to_double': gi.FunctionInfo(to_double)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PlaySpeed)


