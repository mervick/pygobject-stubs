# encoding: utf-8
# module gi.repository.OSTree
# from /usr/lib64/girepository-1.0/OSTree-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class KernelArgs(__gi.Struct):
    # no doc
    def append(self, arg): # real signature unknown; restored from __doc__
        """ append(self, arg:str) """
        pass

    def append_argv(self, argv): # real signature unknown; restored from __doc__
        """ append_argv(self, argv:str) """
        pass

    def append_argv_filtered(self, argv, prefixes): # real signature unknown; restored from __doc__
        """ append_argv_filtered(self, argv:str, prefixes:str) """
        pass

    def append_proc_cmdline(self, cancellable=None): # real signature unknown; restored from __doc__
        """ append_proc_cmdline(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def cleanup(self, loc=None): # real signature unknown; restored from __doc__
        """ cleanup(loc=None) """
        pass

    def delete(self, arg): # real signature unknown; restored from __doc__
        """ delete(self, arg:str) -> bool """
        return False

    def delete_key_entry(self, key): # real signature unknown; restored from __doc__
        """ delete_key_entry(self, key:str) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_last_value(self, key): # real signature unknown; restored from __doc__
        """ get_last_value(self, key:str) -> str """
        return ""

    def new_replace(self, arg): # real signature unknown; restored from __doc__
        """ new_replace(self, arg:str) -> bool """
        return False

    def parse_append(self, options): # real signature unknown; restored from __doc__
        """ parse_append(self, options:str) """
        pass

    def replace(self, arg): # real signature unknown; restored from __doc__
        """ replace(self, arg:str) """
        pass

    def replace_argv(self, argv): # real signature unknown; restored from __doc__
        """ replace_argv(self, argv:str) """
        pass

    def replace_take(self, arg): # real signature unknown; restored from __doc__
        """ replace_take(self, arg:str) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def to_strv(self): # real signature unknown; restored from __doc__
        """ to_strv(self) -> list """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(KernelArgs), '__module__': 'gi.repository.OSTree', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'KernelArgs' objects>, '__weakref__': <attribute '__weakref__' of 'KernelArgs' objects>, '__doc__': None, 'append': gi.FunctionInfo(append), 'append_argv': gi.FunctionInfo(append_argv), 'append_argv_filtered': gi.FunctionInfo(append_argv_filtered), 'append_proc_cmdline': gi.FunctionInfo(append_proc_cmdline), 'delete': gi.FunctionInfo(delete), 'delete_key_entry': gi.FunctionInfo(delete_key_entry), 'free': gi.FunctionInfo(free), 'get_last_value': gi.FunctionInfo(get_last_value), 'new_replace': gi.FunctionInfo(new_replace), 'parse_append': gi.FunctionInfo(parse_append), 'replace': gi.FunctionInfo(replace), 'replace_argv': gi.FunctionInfo(replace_argv), 'replace_take': gi.FunctionInfo(replace_take), 'to_string': gi.FunctionInfo(to_string), 'to_strv': gi.FunctionInfo(to_strv), 'cleanup': gi.FunctionInfo(cleanup)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(KernelArgs)


