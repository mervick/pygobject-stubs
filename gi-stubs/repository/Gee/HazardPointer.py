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


class HazardPointer(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        new(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, ptr=None) -> Gee.HazardPointer
    """
    def compare_and_exchange_pointer(self, g_type, g_dup_func, g_destroy_func, aptr=None, old_ptr=None, _new_ptr=None, mask, old_mask, new_mask): # real signature unknown; restored from __doc__
        """ compare_and_exchange_pointer(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, aptr=None, old_ptr=None, _new_ptr=None, mask:int, old_mask:int, new_mask:int) -> bool """
        return False

    def exchange_hazard_pointer(self, g_type, g_dup_func, g_destroy_func, aptr=None, new_ptr=None, mask, new_mask): # real signature unknown; restored from __doc__
        """ exchange_hazard_pointer(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, aptr=None, new_ptr=None, mask:int, new_mask:int) -> Gee.HazardPointer, old_mask:int """
        pass

    def exchange_pointer(self, g_type, g_dup_func, g_destroy_func, aptr=None, new_ptr=None, mask, new_mask): # real signature unknown; restored from __doc__
        """ exchange_pointer(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, aptr=None, new_ptr=None, mask:int, new_mask:int) -> old_mask:int """
        pass

    def get(self, other_thread): # real signature unknown; restored from __doc__
        """ get(self, other_thread:bool) """
        pass

    def get_hazard_pointer(self, g_type, g_dup_func, g_destroy_func, aptr=None, mask): # real signature unknown; restored from __doc__
        """ get_hazard_pointer(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, aptr=None, mask:int) -> Gee.HazardPointer, mask_out:int """
        pass

    def get_pointer(self, g_type, g_dup_func, g_destroy_func, aptr=None, mask): # real signature unknown; restored from __doc__
        """ get_pointer(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, aptr=None, mask:int) -> mask_out:int """
        pass

    def new(self, g_type, g_dup_func, g_destroy_func, ptr=None): # real signature unknown; restored from __doc__
        """ new(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, ptr=None) -> Gee.HazardPointer """
        pass

    def release(self, notify): # real signature unknown; restored from __doc__
        """ release(self, notify:GLib.DestroyNotify) """
        pass

    def set_default_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_default_policy(policy:Gee.HazardPointerPolicy) """
        pass

    def set_pointer(self, g_type, g_dup_func, g_destroy_func, aptr=None, new_ptr=None, mask, new_mask): # real signature unknown; restored from __doc__
        """ set_pointer(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, aptr=None, new_ptr=None, mask:int, new_mask:int) """
        pass

    def set_release_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_release_policy(policy:Gee.HazardPointerReleasePolicy) -> bool """
        return False

    def set_thread_exit_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_thread_exit_policy(policy:Gee.HazardPointerPolicy) """
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
        """ new(g_type:GType, g_dup_func:GObject.BoxedCopyFunc, g_destroy_func:GLib.DestroyNotify, ptr=None) -> Gee.HazardPointer """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HazardPointer), '__module__': 'gi.repository.Gee', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'HazardPointer' objects>, '__weakref__': <attribute '__weakref__' of 'HazardPointer' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'get_hazard_pointer': gi.FunctionInfo(get_hazard_pointer), 'get_pointer': gi.FunctionInfo(get_pointer), 'exchange_hazard_pointer': gi.FunctionInfo(exchange_hazard_pointer), 'set_pointer': gi.FunctionInfo(set_pointer), 'exchange_pointer': gi.FunctionInfo(exchange_pointer), 'compare_and_exchange_pointer': gi.FunctionInfo(compare_and_exchange_pointer), 'get': gi.FunctionInfo(get), 'release': gi.FunctionInfo(release), 'set_default_policy': gi.FunctionInfo(set_default_policy), 'set_thread_exit_policy': gi.FunctionInfo(set_thread_exit_policy), 'set_release_policy': gi.FunctionInfo(set_release_policy), '__new__': <staticmethod object at 0x7f6a87b4d4f0>, '__init__': <function nothing at 0x7f6a87ed7ee0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(HazardPointer)


