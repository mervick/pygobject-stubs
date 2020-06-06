# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class MiniObject(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MiniObject()
    """
    def add_parent(self, parent): # real signature unknown; restored from __doc__
        """ add_parent(self, parent:Gst.MiniObject) """
        pass

    def get_qdata(self, quark): # real signature unknown; restored from __doc__
        """ get_qdata(self, quark:int) """
        pass

    def is_writable(self): # real signature unknown; restored from __doc__
        """ is_writable(self) -> bool """
        return False

    def lock(self, flags): # real signature unknown; restored from __doc__
        """ lock(self, flags:Gst.LockFlags) -> bool """
        return False

    def remove_parent(self, parent): # real signature unknown; restored from __doc__
        """ remove_parent(self, parent:Gst.MiniObject) """
        pass

    def replace(self, olddata=None, newdata=None): # real signature unknown; restored from __doc__
        """ replace(olddata:Gst.MiniObject=None, newdata:Gst.MiniObject=None) -> bool, olddata:Gst.MiniObject """
        return False

    def set_qdata(self, quark, data=None, destroy): # real signature unknown; restored from __doc__
        """ set_qdata(self, quark:int, data=None, destroy:GLib.DestroyNotify) """
        pass

    def steal_qdata(self, quark): # real signature unknown; restored from __doc__
        """ steal_qdata(self, quark:int) """
        pass

    def take(self, olddata, newdata): # real signature unknown; restored from __doc__
        """ take(olddata:Gst.MiniObject, newdata:Gst.MiniObject) -> bool, olddata:Gst.MiniObject """
        return False

    def unlock(self, flags): # real signature unknown; restored from __doc__
        """ unlock(self, flags:Gst.LockFlags) """
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

    copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dispose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lockstate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv_pointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv_uint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MiniObject), '__module__': 'gi.repository.Gst', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MiniObject' objects>, '__weakref__': <attribute '__weakref__' of 'MiniObject' objects>, '__doc__': None, 'type': <property object at 0x7f4260571130>, 'refcount': <property object at 0x7f4260571220>, 'lockstate': <property object at 0x7f4260571310>, 'flags': <property object at 0x7f4260571400>, 'copy': <property object at 0x7f42605714f0>, 'dispose': <property object at 0x7f42605715e0>, 'free': <property object at 0x7f42605716d0>, 'priv_uint': <property object at 0x7f42605717c0>, 'priv_pointer': <property object at 0x7f42605718b0>, 'add_parent': gi.FunctionInfo(add_parent), 'get_qdata': gi.FunctionInfo(get_qdata), 'is_writable': gi.FunctionInfo(is_writable), 'lock': gi.FunctionInfo(lock), 'remove_parent': gi.FunctionInfo(remove_parent), 'set_qdata': gi.FunctionInfo(set_qdata), 'steal_qdata': gi.FunctionInfo(steal_qdata), 'unlock': gi.FunctionInfo(unlock), 'replace': gi.FunctionInfo(replace), 'take': gi.FunctionInfo(take)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MiniObject)


