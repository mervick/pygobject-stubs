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


class TocEntry(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(type:Gst.TocEntryType, uid:str) -> Gst.TocEntry
    """
    def append_sub_entry(self, subentry): # real signature unknown; restored from __doc__
        """ append_sub_entry(self, subentry:Gst.TocEntry) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_entry_type(self): # real signature unknown; restored from __doc__
        """ get_entry_type(self) -> Gst.TocEntryType """
        pass

    def get_loop(self): # real signature unknown; restored from __doc__
        """ get_loop(self) -> bool, loop_type:Gst.TocLoopType, repeat_count:int """
        return False

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.TocEntry or None """
        pass

    def get_start_stop_times(self): # real signature unknown; restored from __doc__
        """ get_start_stop_times(self) -> bool, start:int, stop:int """
        return False

    def get_sub_entries(self): # real signature unknown; restored from __doc__
        """ get_sub_entries(self) -> list """
        return []

    def get_tags(self): # real signature unknown; restored from __doc__
        """ get_tags(self) -> Gst.TagList """
        pass

    def get_toc(self): # real signature unknown; restored from __doc__
        """ get_toc(self) -> Gst.Toc """
        pass

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def is_alternative(self): # real signature unknown; restored from __doc__
        """ is_alternative(self) -> bool """
        return False

    def is_sequence(self): # real signature unknown; restored from __doc__
        """ is_sequence(self) -> bool """
        return False

    def merge_tags(self, tags=None, mode): # real signature unknown; restored from __doc__
        """ merge_tags(self, tags:Gst.TagList=None, mode:Gst.TagMergeMode) """
        pass

    def new(self, type, uid): # real signature unknown; restored from __doc__
        """ new(type:Gst.TocEntryType, uid:str) -> Gst.TocEntry """
        pass

    def set_loop(self, loop_type, repeat_count): # real signature unknown; restored from __doc__
        """ set_loop(self, loop_type:Gst.TocLoopType, repeat_count:int) """
        pass

    def set_start_stop_times(self, start, stop): # real signature unknown; restored from __doc__
        """ set_start_stop_times(self, start:int, stop:int) """
        pass

    def set_tags(self, tags=None): # real signature unknown; restored from __doc__
        """ set_tags(self, tags:Gst.TagList=None) """
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
        """ new(type:Gst.TocEntryType, uid:str) -> Gst.TocEntry """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TocEntry), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstTocEntry (94058978071520)>, '__dict__': <attribute '__dict__' of 'TocEntry' objects>, '__weakref__': <attribute '__weakref__' of 'TocEntry' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'append_sub_entry': gi.FunctionInfo(append_sub_entry), 'get_entry_type': gi.FunctionInfo(get_entry_type), 'get_loop': gi.FunctionInfo(get_loop), 'get_parent': gi.FunctionInfo(get_parent), 'get_start_stop_times': gi.FunctionInfo(get_start_stop_times), 'get_sub_entries': gi.FunctionInfo(get_sub_entries), 'get_tags': gi.FunctionInfo(get_tags), 'get_toc': gi.FunctionInfo(get_toc), 'get_uid': gi.FunctionInfo(get_uid), 'is_alternative': gi.FunctionInfo(is_alternative), 'is_sequence': gi.FunctionInfo(is_sequence), 'merge_tags': gi.FunctionInfo(merge_tags), 'set_loop': gi.FunctionInfo(set_loop), 'set_start_stop_times': gi.FunctionInfo(set_start_stop_times), 'set_tags': gi.FunctionInfo(set_tags), '__new__': <staticmethod object at 0x7f4260528ac0>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstTocEntry (94058978071520)>'
    __info__ = StructInfo(TocEntry)


