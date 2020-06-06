# encoding: utf-8
# module gi.repository.Gsf
# from /usr/lib64/girepository-1.0/Gsf-1.typelib
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


class Timestamp(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Timestamp()
        new() -> Gsf.Timestamp
    """
    def as_string(self): # real signature unknown; restored from __doc__
        """ as_string(self) -> str """
        return ""

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gsf.Timestamp """
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Gsf.Timestamp) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def load_from_string(self, spec): # real signature unknown; restored from __doc__
        """ load_from_string(self, spec:str) -> int """
        return 0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gsf.Timestamp """
        pass

    def set_time(self, t): # real signature unknown; restored from __doc__
        """ set_time(self, t:int) """
        pass

    def to_value(self, value): # real signature unknown; restored from __doc__
        """ to_value(self, value:GObject.Value) """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Gsf.Timestamp """
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

    date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Timestamp), '__module__': 'gi.repository.Gsf', '__gtype__': <GType GsfTimestamp (94877076998704)>, '__dict__': <attribute '__dict__' of 'Timestamp' objects>, '__weakref__': <attribute '__weakref__' of 'Timestamp' objects>, '__doc__': None, 'date': <property object at 0x7f95c49a4bd0>, 'seconds': <property object at 0x7f95c49a4cc0>, 'time_zone': <property object at 0x7f95c49a4db0>, 'timet': <property object at 0x7f95c49a4ea0>, 'new': gi.FunctionInfo(new), 'as_string': gi.FunctionInfo(as_string), 'copy': gi.FunctionInfo(copy), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'hash': gi.FunctionInfo(hash), 'load_from_string': gi.FunctionInfo(load_from_string), 'set_time': gi.FunctionInfo(set_time), 'to_value': gi.FunctionInfo(to_value), '__new__': <staticmethod object at 0x7f95c4744040>, '__init__': <function nothing at 0x7f95c4bcbee0>})"
    __gtype__ = None # (!) real value is '<GType GsfTimestamp (94877076998704)>'
    __info__ = StructInfo(Timestamp)


