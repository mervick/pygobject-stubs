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


class Iterator(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Iterator()
        new_single(type:GType, object:GObject.Value) -> Gst.Iterator
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gst.Iterator """
        pass

    def filter(self, func, user_data): # real signature unknown; restored from __doc__
        """ filter(self, func:GLib.CompareFunc, user_data:GObject.Value) -> Gst.Iterator """
        pass

    def find_custom(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ find_custom(self, func:GLib.CompareFunc, user_data=None) -> bool, elem:GObject.Value """
        return False

    def fold(self, func, ret, user_data=None): # real signature unknown; restored from __doc__
        """ fold(self, func:Gst.IteratorFoldFunction, ret:GObject.Value, user_data=None) -> Gst.IteratorResult """
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gst.IteratorForeachFunction, user_data=None) -> Gst.IteratorResult """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new_single(self, type, p_object): # real signature unknown; restored from __doc__
        """ new_single(type:GType, object:GObject.Value) -> Gst.Iterator """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> Gst.IteratorResult, elem:GObject.Value """
        pass

    def push(self, other): # real signature unknown; restored from __doc__
        """ push(self, other:Gst.Iterator) """
        pass

    def resync(self): # real signature unknown; restored from __doc__
        """ resync(self) """
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

    cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    master_cookie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pushed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Iterator), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstIterator (94058977571408)>, '__dict__': <attribute '__dict__' of 'Iterator' objects>, '__weakref__': <attribute '__weakref__' of 'Iterator' objects>, '__doc__': None, 'copy': gi.FunctionInfo(copy), 'next': gi.FunctionInfo(next), 'item': <property object at 0x7f4260560770>, 'resync': gi.FunctionInfo(resync), 'free': gi.FunctionInfo(free), 'pushed': <property object at 0x7f4260560a40>, 'type': <property object at 0x7f4260560b30>, 'lock': <property object at 0x7f4260560c20>, 'cookie': <property object at 0x7f4260560d10>, 'master_cookie': <property object at 0x7f4260560e00>, 'size': <property object at 0x7f4260560ef0>, '_gst_reserved': <property object at 0x7f4260563040>, 'new_single': gi.FunctionInfo(new_single), 'filter': gi.FunctionInfo(filter), 'find_custom': gi.FunctionInfo(find_custom), 'fold': gi.FunctionInfo(fold), 'foreach': gi.FunctionInfo(foreach), 'push': gi.FunctionInfo(push)})"
    __gtype__ = None # (!) real value is '<GType GstIterator (94058977571408)>'
    __info__ = StructInfo(Iterator)


