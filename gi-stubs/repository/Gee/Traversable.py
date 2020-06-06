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


class Traversable(__gobject.GInterface):
    # no doc
    def all_match(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ all_match(self, pred:Gee.Predicate, pred_target=None) -> bool """
        return False

    def any_match(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ any_match(self, pred:Gee.Predicate, pred_target=None) -> bool """
        return False

    def chop(self, offset, length): # real signature unknown; restored from __doc__
        """ chop(self, offset:int, length:int) -> Gee.Iterator """
        pass

    def filter(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ filter(self, pred:Gee.Predicate, pred_target=None) -> Gee.Iterator """
        pass

    def first_match(self, pred, pred_target=None): # real signature unknown; restored from __doc__
        """ first_match(self, pred:Gee.Predicate, pred_target=None) """
        pass

    def flat_map(self, a_type, a_dup_func, a_destroy_func, f, f_target=None): # real signature unknown; restored from __doc__
        """ flat_map(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.FlatMapFunc, f_target=None) -> Gee.Iterator """
        pass

    def fold(self, a_type, a_dup_func, a_destroy_func, f, f_target=None, seed=None): # real signature unknown; restored from __doc__
        """ fold(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.FoldFunc, f_target=None, seed=None) """
        pass

    def foreach(self, f, f_target=None): # real signature unknown; restored from __doc__
        """ foreach(self, f:Gee.ForallFunc, f_target=None) -> bool """
        return False

    def get_element_type(self): # real signature unknown; restored from __doc__
        """ get_element_type(self) -> GType """
        pass

    def map(self, a_type, a_dup_func, a_destroy_func, f, f_target=None): # real signature unknown; restored from __doc__
        """ map(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.MapFunc, f_target=None) -> Gee.Iterator """
        pass

    def max(self, compare, compare_target=None): # real signature unknown; restored from __doc__
        """ max(self, compare:GLib.CompareDataFunc, compare_target=None) """
        pass

    def min(self, compare, compare_target=None): # real signature unknown; restored from __doc__
        """ min(self, compare:GLib.CompareDataFunc, compare_target=None) """
        pass

    def order_by(self, compare=None, compare_target=None): # real signature unknown; restored from __doc__
        """ order_by(self, compare:GLib.CompareDataFunc=None, compare_target=None) -> Gee.Iterator """
        pass

    def scan(self, a_type, a_dup_func, a_destroy_func, f, f_target=None, seed=None): # real signature unknown; restored from __doc__
        """ scan(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.FoldFunc, f_target=None, seed=None) -> Gee.Iterator """
        pass

    def stream(self, a_type, a_dup_func, a_destroy_func, f, f_target=None): # real signature unknown; restored from __doc__
        """ stream(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, f:Gee.StreamFunc, f_target=None) -> Gee.Iterator """
        pass

    def tee(self, forks): # real signature unknown; restored from __doc__
        """ tee(self, forks:int) -> list, result_length1:int """
        return []

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Traversable), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeTraversable (94716266426976)>, '__dict__': <attribute '__dict__' of 'Traversable' objects>, '__weakref__': <attribute '__weakref__' of 'Traversable' objects>, '__doc__': None, '__gsignals__': {}, 'foreach': gi.FunctionInfo(foreach), 'stream': gi.FunctionInfo(stream), 'fold': gi.FunctionInfo(fold), 'map': gi.FunctionInfo(map), 'scan': gi.FunctionInfo(scan), 'filter': gi.FunctionInfo(filter), 'chop': gi.FunctionInfo(chop), 'flat_map': gi.FunctionInfo(flat_map), 'tee': gi.FunctionInfo(tee), 'first_match': gi.FunctionInfo(first_match), 'any_match': gi.FunctionInfo(any_match), 'all_match': gi.FunctionInfo(all_match), 'max': gi.FunctionInfo(max), 'min': gi.FunctionInfo(min), 'order_by': gi.FunctionInfo(order_by), 'get_element_type': gi.FunctionInfo(get_element_type)})"
    __gdoc__ = 'Interface GeeTraversable\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeTraversable (94716266426976)>'
    __info__ = InterfaceInfo(Traversable)


