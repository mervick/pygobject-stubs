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


class Toc(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(scope:Gst.TocScope) -> Gst.Toc
    """
    def append_entry(self, entry): # real signature unknown; restored from __doc__
        """ append_entry(self, entry:Gst.TocEntry) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
        pass

    def find_entry(self, uid): # real signature unknown; restored from __doc__
        """ find_entry(self, uid:str) -> Gst.TocEntry or None """
        pass

    def get_entries(self): # real signature unknown; restored from __doc__
        """ get_entries(self) -> list """
        return []

    def get_scope(self): # real signature unknown; restored from __doc__
        """ get_scope(self) -> Gst.TocScope """
        pass

    def get_tags(self): # real signature unknown; restored from __doc__
        """ get_tags(self) -> Gst.TagList """
        pass

    def merge_tags(self, tags=None, mode): # real signature unknown; restored from __doc__
        """ merge_tags(self, tags:Gst.TagList=None, mode:Gst.TagMergeMode) """
        pass

    def new(self, scope): # real signature unknown; restored from __doc__
        """ new(scope:Gst.TocScope) -> Gst.Toc """
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
        """ new(scope:Gst.TocScope) -> Gst.Toc """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Toc), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstToc (94058978068176)>, '__dict__': <attribute '__dict__' of 'Toc' objects>, '__weakref__': <attribute '__weakref__' of 'Toc' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'append_entry': gi.FunctionInfo(append_entry), 'dump': gi.FunctionInfo(dump), 'find_entry': gi.FunctionInfo(find_entry), 'get_entries': gi.FunctionInfo(get_entries), 'get_scope': gi.FunctionInfo(get_scope), 'get_tags': gi.FunctionInfo(get_tags), 'merge_tags': gi.FunctionInfo(merge_tags), 'set_tags': gi.FunctionInfo(set_tags), '__new__': <staticmethod object at 0x7f4260528a30>, '__init__': <function nothing at 0x7f4260937ee0>})"
    __gtype__ = None # (!) real value is '<GType GstToc (94058978068176)>'
    __info__ = StructInfo(Toc)


