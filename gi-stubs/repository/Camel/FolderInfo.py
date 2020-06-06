# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class FolderInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        FolderInfo()
        new() -> Camel.FolderInfo
    """
    def build(self, folders, namespace_, separator, short_names): # real signature unknown; restored from __doc__
        """ build(folders:list, namespace_:str, separator:int, short_names:bool) -> Camel.FolderInfo """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Camel.FolderInfo """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Camel.FolderInfo """
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
        """ new() -> Camel.FolderInfo """
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

    child = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unread = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FolderInfo), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelFolderInfo (94124523664112)>, '__dict__': <attribute '__dict__' of 'FolderInfo' objects>, '__weakref__': <attribute '__weakref__' of 'FolderInfo' objects>, '__doc__': None, 'next': <property object at 0x7f7b34fcf0e0>, 'parent': <property object at 0x7f7b34fcf1d0>, 'child': <property object at 0x7f7b34fcf2c0>, 'full_name': <property object at 0x7f7b34fcf3b0>, 'display_name': <property object at 0x7f7b34fcf4a0>, 'flags': <property object at 0x7f7b34fcf590>, 'unread': <property object at 0x7f7b34fcf680>, 'total': <property object at 0x7f7b34fcf770>, 'new': gi.FunctionInfo(new), 'clone': gi.FunctionInfo(clone), 'free': gi.FunctionInfo(free), 'build': gi.FunctionInfo(build), '__new__': <staticmethod object at 0x7f7b34fcbb80>, '__init__': <function nothing at 0x7f7b37797ee0>})"
    __gtype__ = None # (!) real value is '<GType CamelFolderInfo (94124523664112)>'
    __info__ = StructInfo(FolderInfo)


