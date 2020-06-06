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


class Future(__gobject.GInterface):
    # no doc
    def flat_map(self, a_type, a_dup_func, a_destroy_func, func, func_target=None): # real signature unknown; restored from __doc__
        """ flat_map(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, func:Gee.FutureFlatMapFunc, func_target=None) -> Gee.Future """
        pass

    def get_exception(self): # real signature unknown; restored from __doc__
        """ get_exception(self) -> error """
        pass

    def get_ready(self): # real signature unknown; restored from __doc__
        """ get_ready(self) -> bool """
        return False

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) """
        pass

    def light_map(self, a_type, a_dup_func, a_destroy_func, func, func_target=None): # real signature unknown; restored from __doc__
        """ light_map(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, func:Gee.FutureLightMapFunc, func_target=None) -> Gee.Future """
        pass

    def light_map_broken(self, a_type, a_dup_func, a_destroy_func, func, func_target=None): # real signature unknown; restored from __doc__
        """ light_map_broken(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, func:Gee.FutureLightMapFunc, func_target=None) -> Gee.Future """
        pass

    def map(self, a_type, a_dup_func, a_destroy_func, func, func_target=None): # real signature unknown; restored from __doc__
        """ map(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, func:Gee.FutureMapFunc, func_target=None) -> Gee.Future """
        pass

    def wait(self): # real signature unknown; restored from __doc__
        """ wait(self) """
        pass

    def wait_async(self, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ wait_async(self, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def wait_finish(self, _res_): # real signature unknown; restored from __doc__
        """ wait_finish(self, _res_:Gio.AsyncResult) """
        pass

    def wait_until(self, end_time): # real signature unknown; restored from __doc__
        """ wait_until(self, end_time:int) -> bool, value """
        return False

    def zip(self, a_type, a_dup_func, a_destroy_func, b_type, b_dup_func, b_destroy_func, zip_func, zip_func_target=None, second): # real signature unknown; restored from __doc__
        """ zip(self, a_type:GType, a_dup_func:GObject.BoxedCopyFunc, a_destroy_func:GLib.DestroyNotify, b_type:GType, b_dup_func:GObject.BoxedCopyFunc, b_destroy_func:GLib.DestroyNotify, zip_func:Gee.FutureZipFunc, zip_func_target=None, second:Gee.Future) -> Gee.Future """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Future), '__module__': 'gi.repository.Gee', '__gtype__': <GType GeeFuture (94716266983824)>, '__dict__': <attribute '__dict__' of 'Future' objects>, '__weakref__': <attribute '__weakref__' of 'Future' objects>, '__doc__': None, '__gsignals__': {}, 'wait': gi.FunctionInfo(wait), 'wait_until': gi.FunctionInfo(wait_until), 'wait_async': gi.FunctionInfo(wait_async), 'wait_finish': gi.FunctionInfo(wait_finish), 'map': gi.FunctionInfo(map), 'light_map': gi.FunctionInfo(light_map), 'light_map_broken': gi.FunctionInfo(light_map_broken), 'zip': gi.FunctionInfo(zip), 'flat_map': gi.FunctionInfo(flat_map), 'get_value': gi.FunctionInfo(get_value), 'get_ready': gi.FunctionInfo(get_ready), 'get_exception': gi.FunctionInfo(get_exception)})"
    __gdoc__ = 'Interface GeeFuture\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeeFuture (94716266983824)>'
    __info__ = InterfaceInfo(Future)


