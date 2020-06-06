# encoding: utf-8
# module gi.repository.GUPnPAV
# from /usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib
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


class CDSLastChangeEntry(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_class(self): # real signature unknown; restored from __doc__
        """ get_class(self) -> str """
        return ""

    def get_event(self): # real signature unknown; restored from __doc__
        """ get_event(self) -> GUPnPAV.CDSLastChangeEvent """
        pass

    def get_object_id(self): # real signature unknown; restored from __doc__
        """ get_object_id(self) -> str """
        return ""

    def get_parent_id(self): # real signature unknown; restored from __doc__
        """ get_parent_id(self) -> str """
        return ""

    def get_update_id(self): # real signature unknown; restored from __doc__
        """ get_update_id(self) -> int """
        return 0

    def is_subtree_update(self): # real signature unknown; restored from __doc__
        """ is_subtree_update(self) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GUPnPAV.CDSLastChangeEntry """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CDSLastChangeEntry), '__module__': 'gi.repository.GUPnPAV', '__gtype__': <GType GUPnPCDSLastChangeEntry (94653147366592)>, '__dict__': <attribute '__dict__' of 'CDSLastChangeEntry' objects>, '__weakref__': <attribute '__weakref__' of 'CDSLastChangeEntry' objects>, '__doc__': None, 'get_class': gi.FunctionInfo(get_class), 'get_event': gi.FunctionInfo(get_event), 'get_object_id': gi.FunctionInfo(get_object_id), 'get_parent_id': gi.FunctionInfo(get_parent_id), 'get_update_id': gi.FunctionInfo(get_update_id), 'is_subtree_update': gi.FunctionInfo(is_subtree_update), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GUPnPCDSLastChangeEntry (94653147366592)>'
    __info__ = StructInfo(CDSLastChangeEntry)


