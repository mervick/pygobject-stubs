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


class Promise(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Promise()
        new() -> Gst.Promise
        new_with_change_func(func:Gst.PromiseChangeFunc, user_data=None) -> Gst.Promise
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def expire(self): # real signature unknown; restored from __doc__
        """ expire(self) """
        pass

    def get_reply(self): # real signature unknown; restored from __doc__
        """ get_reply(self) -> Gst.Structure """
        pass

    def interrupt(self): # real signature unknown; restored from __doc__
        """ interrupt(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gst.Promise """
        pass

    def new_with_change_func(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ new_with_change_func(func:Gst.PromiseChangeFunc, user_data=None) -> Gst.Promise """
        pass

    def reply(self, s): # real signature unknown; restored from __doc__
        """ reply(self, s:Gst.Structure) """
        pass

    def wait(self): # real signature unknown; restored from __doc__
        """ wait(self) -> Gst.PromiseResult """
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
        """ new() -> Gst.Promise """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Promise), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstPromise (94058977882880)>, '__dict__': <attribute '__dict__' of 'Promise' objects>, '__weakref__': <attribute '__weakref__' of 'Promise' objects>, '__doc__': None, 'parent': <property object at 0x7f426050c220>, 'new': gi.FunctionInfo(new), 'new_with_change_func': gi.FunctionInfo(new_with_change_func), 'expire': gi.FunctionInfo(expire), 'get_reply': gi.FunctionInfo(get_reply), 'interrupt': gi.FunctionInfo(interrupt), 'reply': gi.FunctionInfo(reply), 'wait': gi.FunctionInfo(wait), '__new__': <staticmethod object at 0x7f42605074f0>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstPromise (94058977882880)>'
    __info__ = StructInfo(Promise)


