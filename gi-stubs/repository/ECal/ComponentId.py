# encoding: utf-8
# module gi.repository.ECal
# from /usr/lib64/girepository-1.0/ECal-2.0.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ComponentId(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(uid:str, rid:str=None) -> ECal.ComponentId
        new_take(uid:str, rid:str=None) -> ECal.ComponentId
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentId """
        pass

    def equal(self, id2): # real signature unknown; restored from __doc__
        """ equal(self, id2:ECal.ComponentId) -> bool """
        return False

    def get_rid(self): # real signature unknown; restored from __doc__
        """ get_rid(self) -> str or None """
        return ""

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def new(self, uid, rid=None): # real signature unknown; restored from __doc__
        """ new(uid:str, rid:str=None) -> ECal.ComponentId """
        pass

    def new_take(self, uid, rid=None): # real signature unknown; restored from __doc__
        """ new_take(uid:str, rid:str=None) -> ECal.ComponentId """
        pass

    def set_rid(self, rid=None): # real signature unknown; restored from __doc__
        """ set_rid(self, rid:str=None) """
        pass

    def set_uid(self, uid): # real signature unknown; restored from __doc__
        """ set_uid(self, uid:str) """
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
        """ new(uid:str, rid:str=None) -> ECal.ComponentId """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentId), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentId (94764814889104)>, '__dict__': <attribute '__dict__' of 'ComponentId' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentId' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_take': gi.FunctionInfo(new_take), 'copy': gi.FunctionInfo(copy), 'equal': gi.FunctionInfo(equal), 'get_rid': gi.FunctionInfo(get_rid), 'get_uid': gi.FunctionInfo(get_uid), 'hash': gi.FunctionInfo(hash), 'set_rid': gi.FunctionInfo(set_rid), 'set_uid': gi.FunctionInfo(set_uid), '__new__': <staticmethod object at 0x7fe5cce05af0>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType ECalComponentId (94764814889104)>'
    __info__ = StructInfo(ComponentId)


