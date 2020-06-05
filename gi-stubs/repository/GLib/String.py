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


class String(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        String()
    """
    def append(self, val): # real signature unknown; restored from __doc__
        """ append(self, val:str) -> GLib.String """
        pass

    def append_c(self, c): # real signature unknown; restored from __doc__
        """ append_c(self, c:int) -> GLib.String """
        pass

    def append_len(self, val, len): # real signature unknown; restored from __doc__
        """ append_len(self, val:str, len:int) -> GLib.String """
        pass

    def append_unichar(self, wc): # real signature unknown; restored from __doc__
        """ append_unichar(self, wc:str) -> GLib.String """
        pass

    def append_uri_escaped(self, unescaped, reserved_chars_allowed, allow_utf8): # real signature unknown; restored from __doc__
        """ append_uri_escaped(self, unescaped:str, reserved_chars_allowed:str, allow_utf8:bool) -> GLib.String """
        pass

    def ascii_down(self): # real signature unknown; restored from __doc__
        """ ascii_down(self) -> GLib.String """
        pass

    def ascii_up(self): # real signature unknown; restored from __doc__
        """ ascii_up(self) -> GLib.String """
        pass

    def assign(self, rval): # real signature unknown; restored from __doc__
        """ assign(self, rval:str) -> GLib.String """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def down(self): # real signature unknown; restored from __doc__
        """ down(self) -> GLib.String """
        pass

    def equal(self, v2): # real signature unknown; restored from __doc__
        """ equal(self, v2:GLib.String) -> bool """
        return False

    def erase(self, pos, len): # real signature unknown; restored from __doc__
        """ erase(self, pos:int, len:int) -> GLib.String """
        pass

    def free(self, free_segment): # real signature unknown; restored from __doc__
        """ free(self, free_segment:bool) -> str or None """
        return ""

    def free_to_bytes(self): # real signature unknown; restored from __doc__
        """ free_to_bytes(self) -> GLib.Bytes """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def insert(self, pos, val): # real signature unknown; restored from __doc__
        """ insert(self, pos:int, val:str) -> GLib.String """
        pass

    def insert_c(self, pos, c): # real signature unknown; restored from __doc__
        """ insert_c(self, pos:int, c:int) -> GLib.String """
        pass

    def insert_len(self, pos, val, len): # real signature unknown; restored from __doc__
        """ insert_len(self, pos:int, val:str, len:int) -> GLib.String """
        pass

    def insert_unichar(self, pos, wc): # real signature unknown; restored from __doc__
        """ insert_unichar(self, pos:int, wc:str) -> GLib.String """
        pass

    def overwrite(self, pos, val): # real signature unknown; restored from __doc__
        """ overwrite(self, pos:int, val:str) -> GLib.String """
        pass

    def overwrite_len(self, pos, val, len): # real signature unknown; restored from __doc__
        """ overwrite_len(self, pos:int, val:str, len:int) -> GLib.String """
        pass

    def prepend(self, val): # real signature unknown; restored from __doc__
        """ prepend(self, val:str) -> GLib.String """
        pass

    def prepend_c(self, c): # real signature unknown; restored from __doc__
        """ prepend_c(self, c:int) -> GLib.String """
        pass

    def prepend_len(self, val, len): # real signature unknown; restored from __doc__
        """ prepend_len(self, val:str, len:int) -> GLib.String """
        pass

    def prepend_unichar(self, wc): # real signature unknown; restored from __doc__
        """ prepend_unichar(self, wc:str) -> GLib.String """
        pass

    def set_size(self, len): # real signature unknown; restored from __doc__
        """ set_size(self, len:int) -> GLib.String """
        pass

    def truncate(self, len): # real signature unknown; restored from __doc__
        """ truncate(self, len:int) -> GLib.String """
        pass

    def up(self): # real signature unknown; restored from __doc__
        """ up(self) -> GLib.String """
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

    allocated_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(String), '__module__': 'gi.repository.GLib', '__gtype__': <GType GString (94243598054640)>, '__dict__': <attribute '__dict__' of 'String' objects>, '__weakref__': <attribute '__weakref__' of 'String' objects>, '__doc__': None, 'str': <property object at 0x7f1d2b9bf630>, 'len': <property object at 0x7f1d2b9bf720>, 'allocated_len': <property object at 0x7f1d2b9bf810>, 'append': gi.FunctionInfo(append), 'append_c': gi.FunctionInfo(append_c), 'append_len': gi.FunctionInfo(append_len), 'append_unichar': gi.FunctionInfo(append_unichar), 'append_uri_escaped': gi.FunctionInfo(append_uri_escaped), 'ascii_down': gi.FunctionInfo(ascii_down), 'ascii_up': gi.FunctionInfo(ascii_up), 'assign': gi.FunctionInfo(assign), 'down': gi.FunctionInfo(down), 'equal': gi.FunctionInfo(equal), 'erase': gi.FunctionInfo(erase), 'free': gi.FunctionInfo(free), 'free_to_bytes': gi.FunctionInfo(free_to_bytes), 'hash': gi.FunctionInfo(hash), 'insert': gi.FunctionInfo(insert), 'insert_c': gi.FunctionInfo(insert_c), 'insert_len': gi.FunctionInfo(insert_len), 'insert_unichar': gi.FunctionInfo(insert_unichar), 'overwrite': gi.FunctionInfo(overwrite), 'overwrite_len': gi.FunctionInfo(overwrite_len), 'prepend': gi.FunctionInfo(prepend), 'prepend_c': gi.FunctionInfo(prepend_c), 'prepend_len': gi.FunctionInfo(prepend_len), 'prepend_unichar': gi.FunctionInfo(prepend_unichar), 'set_size': gi.FunctionInfo(set_size), 'truncate': gi.FunctionInfo(truncate), 'up': gi.FunctionInfo(up)})"
    __gtype__ = None # (!) real value is '<GType GString (94243598054640)>'
    __info__ = StructInfo(String)


