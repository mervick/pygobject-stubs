# encoding: utf-8
# module gi.repository.Xmlb
# from /usr/lib64/girepository-1.0/Xmlb-1.0.typelib
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


class Opcode(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        func_new(func:int) -> Xmlb.Opcode
        integer_new(val:int) -> Xmlb.Opcode
        text_new(str:str) -> Xmlb.Opcode
        text_new_static(str:str) -> Xmlb.Opcode
        text_new_steal(str:str) -> Xmlb.Opcode
    """
    def cmp_str(self): # real signature unknown; restored from __doc__
        """ cmp_str(self) -> bool """
        return False

    def cmp_val(self): # real signature unknown; restored from __doc__
        """ cmp_val(self) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def func_new(self, func): # real signature unknown; restored from __doc__
        """ func_new(func:int) -> Xmlb.Opcode """
        pass

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> Xmlb.OpcodeKind """
        pass

    def get_str(self): # real signature unknown; restored from __doc__
        """ get_str(self) -> str """
        return ""

    def get_val(self): # real signature unknown; restored from __doc__
        """ get_val(self) -> int """
        return 0

    def integer_new(self, val): # real signature unknown; restored from __doc__
        """ integer_new(val:int) -> Xmlb.Opcode """
        pass

    def kind_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ kind_from_string(str:str) -> Xmlb.OpcodeKind """
        pass

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:Xmlb.OpcodeKind) -> str """
        return ""

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Xmlb.Opcode """
        pass

    def text_new(self, p_str): # real signature unknown; restored from __doc__
        """ text_new(str:str) -> Xmlb.Opcode """
        pass

    def text_new_static(self, p_str): # real signature unknown; restored from __doc__
        """ text_new_static(str:str) -> Xmlb.Opcode """
        pass

    def text_new_steal(self, p_str): # real signature unknown; restored from __doc__
        """ text_new_steal(str:str) -> Xmlb.Opcode """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Opcode), '__module__': 'gi.repository.Xmlb', '__gtype__': <GType XbOpcode (94018414303456)>, '__dict__': <attribute '__dict__' of 'Opcode' objects>, '__weakref__': <attribute '__weakref__' of 'Opcode' objects>, '__doc__': None, 'func_new': gi.FunctionInfo(func_new), 'integer_new': gi.FunctionInfo(integer_new), 'text_new': gi.FunctionInfo(text_new), 'text_new_static': gi.FunctionInfo(text_new_static), 'text_new_steal': gi.FunctionInfo(text_new_steal), 'cmp_str': gi.FunctionInfo(cmp_str), 'cmp_val': gi.FunctionInfo(cmp_val), 'get_kind': gi.FunctionInfo(get_kind), 'get_str': gi.FunctionInfo(get_str), 'get_val': gi.FunctionInfo(get_val), 'ref': gi.FunctionInfo(ref), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_to_string': gi.FunctionInfo(kind_to_string)})"
    __gtype__ = None # (!) real value is '<GType XbOpcode (94018414303456)>'
    __info__ = StructInfo(Opcode)


