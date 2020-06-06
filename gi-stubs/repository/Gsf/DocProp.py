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


class DocProp(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(name:str) -> Gsf.DocProp
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_link(self): # real signature unknown; restored from __doc__
        """ get_link(self) -> str or None """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_val(self): # real signature unknown; restored from __doc__
        """ get_val(self) -> GObject.Value """
        pass

    def new(self, name): # real signature unknown; restored from __doc__
        """ new(name:str) -> Gsf.DocProp """
        pass

    def set_link(self, link=None): # real signature unknown; restored from __doc__
        """ set_link(self, link:str=None) """
        pass

    def set_val(self, val): # real signature unknown; restored from __doc__
        """ set_val(self, val:GObject.Value) """
        pass

    def swap_val(self, val): # real signature unknown; restored from __doc__
        """ swap_val(self, val:GObject.Value) -> GObject.Value """
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
        """ new(name:str) -> Gsf.DocProp """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DocProp), '__module__': 'gi.repository.Gsf', '__gtype__': <GType GsfDocProp (94877076480128)>, '__dict__': <attribute '__dict__' of 'DocProp' objects>, '__weakref__': <attribute '__weakref__' of 'DocProp' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'dump': gi.FunctionInfo(dump), 'free': gi.FunctionInfo(free), 'get_link': gi.FunctionInfo(get_link), 'get_name': gi.FunctionInfo(get_name), 'get_val': gi.FunctionInfo(get_val), 'set_link': gi.FunctionInfo(set_link), 'set_val': gi.FunctionInfo(set_val), 'swap_val': gi.FunctionInfo(swap_val), '__new__': <staticmethod object at 0x7f95c498d070>, '__init__': <function nothing at 0x7f95c4bcbee0>})"
    __gtype__ = None # (!) real value is '<GType GsfDocProp (94877076480128)>'
    __info__ = StructInfo(DocProp)


