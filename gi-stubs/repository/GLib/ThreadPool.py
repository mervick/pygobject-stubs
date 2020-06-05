# encoding: utf-8
# module gi.repository.GLib
# from /usr/lib64/girepository-1.0/GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # /usr/lib64/python3.8/site-packages/gi/_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class ThreadPool(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ThreadPool()
    """
    def free(self, immediate, wait_): # real signature unknown; restored from __doc__
        """ free(self, immediate:bool, wait_:bool) """
        pass

    def get_max_idle_time(self): # real signature unknown; restored from __doc__
        """ get_max_idle_time() -> int """
        return 0

    def get_max_threads(self): # real signature unknown; restored from __doc__
        """ get_max_threads(self) -> int """
        return 0

    def get_max_unused_threads(self): # real signature unknown; restored from __doc__
        """ get_max_unused_threads() -> int """
        return 0

    def get_num_threads(self): # real signature unknown; restored from __doc__
        """ get_num_threads(self) -> int """
        return 0

    def get_num_unused_threads(self): # real signature unknown; restored from __doc__
        """ get_num_unused_threads() -> int """
        return 0

    def move_to_front(self, data=None): # real signature unknown; restored from __doc__
        """ move_to_front(self, data=None) -> bool """
        return False

    def push(self, data=None): # real signature unknown; restored from __doc__
        """ push(self, data=None) -> bool """
        return False

    def set_max_idle_time(self, interval): # real signature unknown; restored from __doc__
        """ set_max_idle_time(interval:int) """
        pass

    def set_max_threads(self, max_threads): # real signature unknown; restored from __doc__
        """ set_max_threads(self, max_threads:int) -> bool """
        return False

    def set_max_unused_threads(self, max_threads): # real signature unknown; restored from __doc__
        """ set_max_unused_threads(max_threads:int) """
        pass

    def stop_unused_threads(self): # real signature unknown; restored from __doc__
        """ stop_unused_threads() """
        pass

    def unprocessed(self): # real signature unknown; restored from __doc__
        """ unprocessed(self) -> int """
        return 0

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

    exclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ThreadPool), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ThreadPool' objects>, '__weakref__': <attribute '__weakref__' of 'ThreadPool' objects>, '__doc__': None, 'func': <property object at 0x7f1d2b908d60>, 'user_data': <property object at 0x7f1d2b908e50>, 'exclusive': <property object at 0x7f1d2b908f40>, 'free': gi.FunctionInfo(free), 'get_max_threads': gi.FunctionInfo(get_max_threads), 'get_num_threads': gi.FunctionInfo(get_num_threads), 'move_to_front': gi.FunctionInfo(move_to_front), 'push': gi.FunctionInfo(push), 'set_max_threads': gi.FunctionInfo(set_max_threads), 'unprocessed': gi.FunctionInfo(unprocessed), 'get_max_idle_time': gi.FunctionInfo(get_max_idle_time), 'get_max_unused_threads': gi.FunctionInfo(get_max_unused_threads), 'get_num_unused_threads': gi.FunctionInfo(get_num_unused_threads), 'set_max_idle_time': gi.FunctionInfo(set_max_idle_time), 'set_max_unused_threads': gi.FunctionInfo(set_max_unused_threads), 'stop_unused_threads': gi.FunctionInfo(stop_unused_threads)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ThreadPool)


