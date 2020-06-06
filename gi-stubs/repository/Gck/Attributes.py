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


class Attributes(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(reserved:int) -> Gck.Attributes
    """
    def at(self, index): # real signature unknown; restored from __doc__
        """ at(self, index:int) -> Gck.Attribute """
        pass

    def contains(self, match): # real signature unknown; restored from __doc__
        """ contains(self, match:Gck.Attribute) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
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

    def new(self, reserved): # real signature unknown; restored from __doc__
        """ new(reserved:int) -> Gck.Attributes """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gck.Attributes """
        pass

    def ref_sink(self): # real signature unknown; restored from __doc__
        """ ref_sink(self) -> Gck.Attributes """
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
        """ new(reserved:int) -> Gck.Attributes """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Attributes), '__module__': 'gi.repository.Gck', '__gtype__': <GType GckAttributes (94702127680864)>, '__dict__': <attribute '__dict__' of 'Attributes' objects>, '__weakref__': <attribute '__weakref__' of 'Attributes' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'at': gi.FunctionInfo(at), 'contains': gi.FunctionInfo(contains), 'count': gi.FunctionInfo(count), 'dump': gi.FunctionInfo(dump), 'find': gi.FunctionInfo(find), 'find_boolean': gi.FunctionInfo(find_boolean), 'find_date': gi.FunctionInfo(find_date), 'find_string': gi.FunctionInfo(find_string), 'find_ulong': gi.FunctionInfo(find_ulong), 'ref': gi.FunctionInfo(ref), 'ref_sink': gi.FunctionInfo(ref_sink), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7fc2e613cc70>, '__init__': <function nothing at 0x7fc2e6382ee0>})"
    __gtype__ = None # (!) real value is '<GType GckAttributes (94702127680864)>'
    __info__ = StructInfo(Attributes)


