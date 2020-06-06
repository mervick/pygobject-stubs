# encoding: utf-8
# module gi.repository.Gee
# from /usr/lib64/girepository-1.0/Gee-0.8.typelib
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


class Deque(__gobject.GInterface):
    # no doc
    def drain_head(self, recipient, amount): # real signature unknown; restored from __doc__
        """ drain_head(self, recipient:Gee.Collection, amount:int) -> int """
        return 0

    def drain_tail(self, recipient, amount): # real signature unknown; restored from __doc__
        """ drain_tail(self, recipient:Gee.Collection, amount:int) -> int """
        return 0

    def offer_head(self, element=None): # real signature unknown; restored from __doc__
        """ offer_head(self, element=None) -> bool """
        return False

    def offer_tail(self, element=None): # real signature unknown; restored from __doc__
        """ offer_tail(self, element=None) -> bool """
        return False

    def peek_head(self): # real signature unknown; restored from __doc__
        """ peek_head(self) """
        pass

    def peek_tail(self): # real signature unknown; restored from __doc__
        """ peek_tail(self) """
        pass

    def poll_head(self): # real signature unknown; restored from __doc__
        """ poll_head(self) """
        pass

    def poll_tail(self): # real signature unknown; restored from __doc__
        """ poll_tail(self) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Deque), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeDeque (94716266940416)>, '__dict__': <attribute '__dict__' of 'Deque' objects>, '__weakref__': <attribute '__weakref__' of 'Deque' objects>, '__doc__': None, '__gsignals__': {}, 'offer_head': gi.FunctionInfo(offer_head), 'peek_head': gi.FunctionInfo(peek_head), 'poll_head': gi.FunctionInfo(poll_head), 'drain_head': gi.FunctionInfo(drain_head), 'offer_tail': gi.FunctionInfo(offer_tail), 'peek_tail': gi.FunctionInfo(peek_tail), 'poll_tail': gi.FunctionInfo(poll_tail), 'drain_tail': gi.FunctionInfo(drain_tail)})"
    __gdoc__ = 'Interface GeeDeque\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeDeque (94716266940416)>'
    __info__ = InterfaceInfo(Deque)


