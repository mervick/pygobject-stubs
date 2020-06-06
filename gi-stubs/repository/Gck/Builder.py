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


class Builder(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Builder()
        new(flags:Gck.BuilderFlags) -> Gck.Builder
    """
    def add_all(self, attrs): # real signature unknown; restored from __doc__
        """ add_all(self, attrs:Gck.Attributes) """
        pass

    def add_attribute(self, attr): # real signature unknown; restored from __doc__
        """ add_attribute(self, attr:Gck.Attribute) """
        pass

    def add_boolean(self, attr_type, value): # real signature unknown; restored from __doc__
        """ add_boolean(self, attr_type:int, value:bool) """
        pass

    def add_data(self, attr_type, value=None): # real signature unknown; restored from __doc__
        """ add_data(self, attr_type:int, value:list=None) """
        pass

    def add_date(self, attr_type, value): # real signature unknown; restored from __doc__
        """ add_date(self, attr_type:int, value:GLib.Date) """
        pass

    def add_empty(self, attr_type): # real signature unknown; restored from __doc__
        """ add_empty(self, attr_type:int) """
        pass

    def add_invalid(self, attr_type): # real signature unknown; restored from __doc__
        """ add_invalid(self, attr_type:int) """
        pass

    def add_only(self, attrs, only_types): # real signature unknown; restored from __doc__
        """ add_only(self, attrs:Gck.Attributes, only_types:list) """
        pass

    def add_string(self, attr_type, value=None): # real signature unknown; restored from __doc__
        """ add_string(self, attr_type:int, value:str=None) """
        pass

    def add_ulong(self, attr_type, value): # real signature unknown; restored from __doc__
        """ add_ulong(self, attr_type:int, value:int) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gck.Builder """
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> Gck.Attributes """
        pass

    def find(self, attr_type): # real signature unknown; restored from __doc__
        """ find(self, attr_type:int) -> Gck.Attribute """
        pass

    def find_boolean(self, attr_type): # real signature unknown; restored from __doc__
        """ find_boolean(self, attr_type:int) -> bool, value:bool """
        return False

    def find_date(self, attr_type): # real signature unknown; restored from __doc__
        """ find_date(self, attr_type:int) -> bool, value:GLib.Date """
        return False

    def find_string(self, attr_type): # real signature unknown; restored from __doc__
        """ find_string(self, attr_type:int) -> bool, value:str """
        return False

    def find_ulong(self, attr_type): # real signature unknown; restored from __doc__
        """ find_ulong(self, attr_type:int) -> bool, value:int """
        return False

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) """
        pass

    def init_full(self, flags): # real signature unknown; restored from __doc__
        """ init_full(self, flags:Gck.BuilderFlags) """
        pass

    def new(self, flags): # real signature unknown; restored from __doc__
        """ new(flags:Gck.BuilderFlags) -> Gck.Builder """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gck.Builder """
        pass

    def set_all(self, attrs): # real signature unknown; restored from __doc__
        """ set_all(self, attrs:Gck.Attributes) """
        pass

    def set_boolean(self, attr_type, value): # real signature unknown; restored from __doc__
        """ set_boolean(self, attr_type:int, value:bool) """
        pass

    def set_data(self, attr_type, value=None): # real signature unknown; restored from __doc__
        """ set_data(self, attr_type:int, value:list=None) """
        pass

    def set_date(self, attr_type, value): # real signature unknown; restored from __doc__
        """ set_date(self, attr_type:int, value:GLib.Date) """
        pass

    def set_empty(self, attr_type): # real signature unknown; restored from __doc__
        """ set_empty(self, attr_type:int) """
        pass

    def set_invalid(self, attr_type): # real signature unknown; restored from __doc__
        """ set_invalid(self, attr_type:int) """
        pass

    def set_string(self, attr_type, value): # real signature unknown; restored from __doc__
        """ set_string(self, attr_type:int, value:str) """
        pass

    def set_ulong(self, attr_type, value): # real signature unknown; restored from __doc__
        """ set_ulong(self, attr_type:int, value:int) """
        pass

    def steal(self): # real signature unknown; restored from __doc__
        """ steal(self) -> Gck.Attributes """
        pass

    def take_data(self, attr_type, value=None): # real signature unknown; restored from __doc__
        """ take_data(self, attr_type:int, value:list=None) """
        pass

    def unref(self, builder=None): # real signature unknown; restored from __doc__
        """ unref(builder=None) """
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

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Builder), '__module__': 'gi.repository.Gck', '__gtype__': <GType GckBuilder (94702127693024)>, '__dict__': <attribute '__dict__' of 'Builder' objects>, '__weakref__': <attribute '__weakref__' of 'Builder' objects>, '__doc__': None, 'x': <property object at 0x7fc2e6170b80>, 'new': gi.FunctionInfo(new), 'add_all': gi.FunctionInfo(add_all), 'add_attribute': gi.FunctionInfo(add_attribute), 'add_boolean': gi.FunctionInfo(add_boolean), 'add_data': gi.FunctionInfo(add_data), 'add_date': gi.FunctionInfo(add_date), 'add_empty': gi.FunctionInfo(add_empty), 'add_invalid': gi.FunctionInfo(add_invalid), 'add_only': gi.FunctionInfo(add_only), 'add_string': gi.FunctionInfo(add_string), 'add_ulong': gi.FunctionInfo(add_ulong), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'end': gi.FunctionInfo(end), 'find': gi.FunctionInfo(find), 'find_boolean': gi.FunctionInfo(find_boolean), 'find_date': gi.FunctionInfo(find_date), 'find_string': gi.FunctionInfo(find_string), 'find_ulong': gi.FunctionInfo(find_ulong), 'init': gi.FunctionInfo(init), 'init_full': gi.FunctionInfo(init_full), 'ref': gi.FunctionInfo(ref), 'set_all': gi.FunctionInfo(set_all), 'set_boolean': gi.FunctionInfo(set_boolean), 'set_data': gi.FunctionInfo(set_data), 'set_date': gi.FunctionInfo(set_date), 'set_empty': gi.FunctionInfo(set_empty), 'set_invalid': gi.FunctionInfo(set_invalid), 'set_string': gi.FunctionInfo(set_string), 'set_ulong': gi.FunctionInfo(set_ulong), 'steal': gi.FunctionInfo(steal), 'take_data': gi.FunctionInfo(take_data), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GckBuilder (94702127693024)>'
    __info__ = StructInfo(Builder)


