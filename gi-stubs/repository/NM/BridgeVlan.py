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


class BridgeVlan(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(vid_start:int, vid_end:int) -> NM.BridgeVlan
    """
    def cmp(self, b): # real signature unknown; restored from __doc__
        """ cmp(self, b:NM.BridgeVlan) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def from_str(self, p_str): # real signature unknown; restored from __doc__
        """ from_str(str:str) -> NM.BridgeVlan """
        pass

    def get_vid_range(self): # real signature unknown; restored from __doc__
        """ get_vid_range(self) -> bool, vid_start:int, vid_end:int """
        return False

    def is_pvid(self): # real signature unknown; restored from __doc__
        """ is_pvid(self) -> bool """
        return False

    def is_sealed(self): # real signature unknown; restored from __doc__
        """ is_sealed(self) -> bool """
        return False

    def is_untagged(self): # real signature unknown; restored from __doc__
        """ is_untagged(self) -> bool """
        return False

    def new(self, vid_start, vid_end): # real signature unknown; restored from __doc__
        """ new(vid_start:int, vid_end:int) -> NM.BridgeVlan """
        pass

    def new_clone(self): # real signature unknown; restored from __doc__
        """ new_clone(self) -> NM.BridgeVlan """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> NM.BridgeVlan """
        pass

    def seal(self): # real signature unknown; restored from __doc__
        """ seal(self) """
        pass

    def set_pvid(self, value): # real signature unknown; restored from __doc__
        """ set_pvid(self, value:bool) """
        pass

    def set_untagged(self, value): # real signature unknown; restored from __doc__
        """ set_untagged(self, value:bool) """
        pass

    def to_str(self): # real signature unknown; restored from __doc__
        """ to_str(self) -> str """
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
        """ new(vid_start:int, vid_end:int) -> NM.BridgeVlan """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BridgeVlan), '__module__': 'gi.repository.NM', '__gtype__': <GType NMBridgeVlan (94741104149184)>, '__dict__': <attribute '__dict__' of 'BridgeVlan' objects>, '__weakref__': <attribute '__weakref__' of 'BridgeVlan' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'cmp': gi.FunctionInfo(cmp), 'get_vid_range': gi.FunctionInfo(get_vid_range), 'is_pvid': gi.FunctionInfo(is_pvid), 'is_sealed': gi.FunctionInfo(is_sealed), 'is_untagged': gi.FunctionInfo(is_untagged), 'new_clone': gi.FunctionInfo(new_clone), 'ref': gi.FunctionInfo(ref), 'seal': gi.FunctionInfo(seal), 'set_pvid': gi.FunctionInfo(set_pvid), 'set_untagged': gi.FunctionInfo(set_untagged), 'to_str': gi.FunctionInfo(to_str), 'unref': gi.FunctionInfo(unref), 'from_str': gi.FunctionInfo(from_str), '__new__': <staticmethod object at 0x7fb9b8cec070>, '__init__': <function nothing at 0x7fb9b8f70ee0>})"
    __gtype__ = None # (!) real value is '<GType NMBridgeVlan (94741104149184)>'
    __info__ = StructInfo(BridgeVlan)


