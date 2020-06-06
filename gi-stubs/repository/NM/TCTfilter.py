# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


class TCTfilter(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(kind:str, parent:int) -> NM.TCTfilter
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> NM.TCTfilter """
        pass

    def equal(self, other): # real signature unknown; restored from __doc__
        """ equal(self, other:NM.TCTfilter) -> bool """
        return False

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> NM.TCAction """
        pass

    def get_handle(self): # real signature unknown; restored from __doc__
        """ get_handle(self) -> int """
        return 0

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> int """
        return 0

    def new(self, kind, parent): # real signature unknown; restored from __doc__
        """ new(kind:str, parent:int) -> NM.TCTfilter """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) """
        pass

    def set_action(self, action): # real signature unknown; restored from __doc__
        """ set_action(self, action:NM.TCAction) """
        pass

    def set_handle(self, handle): # real signature unknown; restored from __doc__
        """ set_handle(self, handle:int) """
        pass

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
        """ new(kind:str, parent:int) -> NM.TCTfilter """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TCTfilter), '__module__': 'gi.repository.NM', '__gtype__': <GType NMTCTfilter (94741104672240)>, '__dict__': <attribute '__dict__' of 'TCTfilter' objects>, '__weakref__': <attribute '__weakref__' of 'TCTfilter' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'dup': gi.FunctionInfo(dup), 'equal': gi.FunctionInfo(equal), 'get_action': gi.FunctionInfo(get_action), 'get_handle': gi.FunctionInfo(get_handle), 'get_kind': gi.FunctionInfo(get_kind), 'get_parent': gi.FunctionInfo(get_parent), 'ref': gi.FunctionInfo(ref), 'set_action': gi.FunctionInfo(set_action), 'set_handle': gi.FunctionInfo(set_handle), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7fb9b8497700>, '__init__': <function nothing at 0x7fb9b8f70ee0>})"
    __gtype__ = None # (!) real value is '<GType NMTCTfilter (94741104672240)>'
    __info__ = StructInfo(TCTfilter)


