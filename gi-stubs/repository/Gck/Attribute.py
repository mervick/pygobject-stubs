# encoding: utf-8
# module gi.repository.Gck
# from /usr/lib64/girepository-1.0/Gck-1.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Attribute(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Attribute()
        new(attr_type:int, value:int, length:int) -> Gck.Attribute
        new_boolean(attr_type:int, value:bool) -> Gck.Attribute
        new_date(attr_type:int, value:GLib.Date) -> Gck.Attribute
        new_empty(attr_type:int) -> Gck.Attribute
        new_invalid(attr_type:int) -> Gck.Attribute
        new_string(attr_type:int, value:str) -> Gck.Attribute
        new_ulong(attr_type:int, value:int) -> Gck.Attribute
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gck.Attribute """
        pass

    def equal(self, attr2): # real signature unknown; restored from __doc__
        """ equal(self, attr2:Gck.Attribute) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_boolean(self): # real signature unknown; restored from __doc__
        """ get_boolean(self) -> bool """
        return False

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> list, length:int """
        return []

    def get_date(self, value): # real signature unknown; restored from __doc__
        """ get_date(self, value:GLib.Date) """
        pass

    def get_string(self): # real signature unknown; restored from __doc__
        """ get_string(self) -> str or None """
        return ""

    def get_ulong(self): # real signature unknown; restored from __doc__
        """ get_ulong(self) -> int """
        return 0

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def init_copy(self, src): # real signature unknown; restored from __doc__
        """ init_copy(self, src:Gck.Attribute) """
        pass

    def is_invalid(self): # real signature unknown; restored from __doc__
        """ is_invalid(self) -> bool """
        return False

    def new(self, attr_type, value, length): # real signature unknown; restored from __doc__
        """ new(attr_type:int, value:int, length:int) -> Gck.Attribute """
        pass

    def new_boolean(self, attr_type, value): # real signature unknown; restored from __doc__
        """ new_boolean(attr_type:int, value:bool) -> Gck.Attribute """
        pass

    def new_date(self, attr_type, value): # real signature unknown; restored from __doc__
        """ new_date(attr_type:int, value:GLib.Date) -> Gck.Attribute """
        pass

    def new_empty(self, attr_type): # real signature unknown; restored from __doc__
        """ new_empty(attr_type:int) -> Gck.Attribute """
        pass

    def new_invalid(self, attr_type): # real signature unknown; restored from __doc__
        """ new_invalid(attr_type:int) -> Gck.Attribute """
        pass

    def new_string(self, attr_type, value): # real signature unknown; restored from __doc__
        """ new_string(attr_type:int, value:str) -> Gck.Attribute """
        pass

    def new_ulong(self, attr_type, value): # real signature unknown; restored from __doc__
        """ new_ulong(attr_type:int, value:int) -> Gck.Attribute """
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

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Attribute), '__module__': 'gi.repository.Gck', '__gtype__': <GType GckAttribute (94702127684944)>, '__dict__': <attribute '__dict__' of 'Attribute' objects>, '__weakref__': <attribute '__weakref__' of 'Attribute' objects>, '__doc__': None, 'type': <property object at 0x7fc2e6170e50>, 'value': <property object at 0x7fc2e6170e00>, 'length': <property object at 0x7fc2e6170d10>, 'new': gi.FunctionInfo(new), 'new_boolean': gi.FunctionInfo(new_boolean), 'new_date': gi.FunctionInfo(new_date), 'new_empty': gi.FunctionInfo(new_empty), 'new_invalid': gi.FunctionInfo(new_invalid), 'new_string': gi.FunctionInfo(new_string), 'new_ulong': gi.FunctionInfo(new_ulong), 'clear': gi.FunctionInfo(clear), 'dump': gi.FunctionInfo(dump), 'dup': gi.FunctionInfo(dup), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_boolean': gi.FunctionInfo(get_boolean), 'get_data': gi.FunctionInfo(get_data), 'get_date': gi.FunctionInfo(get_date), 'get_string': gi.FunctionInfo(get_string), 'get_ulong': gi.FunctionInfo(get_ulong), 'hash': gi.FunctionInfo(hash), 'init_copy': gi.FunctionInfo(init_copy), 'is_invalid': gi.FunctionInfo(is_invalid)})"
    __gtype__ = None # (!) real value is '<GType GckAttribute (94702127684944)>'
    __info__ = StructInfo(Attribute)


