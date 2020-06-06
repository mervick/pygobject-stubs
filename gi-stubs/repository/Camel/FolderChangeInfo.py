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


class FolderChangeInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        FolderChangeInfo()
        new() -> Camel.FolderChangeInfo
    """
    def add_source(self, uid): # real signature unknown; restored from __doc__
        """ add_source(self, uid:str) """
        pass

    def add_source_list(self, p_list): # real signature unknown; restored from __doc__
        """ add_source_list(self, list:list) """
        pass

    def add_uid(self, uid): # real signature unknown; restored from __doc__
        """ add_uid(self, uid:str) """
        pass

    def add_update(self, uid): # real signature unknown; restored from __doc__
        """ add_update(self, uid:str) """
        pass

    def add_update_list(self, p_list): # real signature unknown; restored from __doc__
        """ add_update_list(self, list:list) """
        pass

    def build_diff(self): # real signature unknown; restored from __doc__
        """ build_diff(self) """
        pass

    def cat(self, src): # real signature unknown; restored from __doc__
        """ cat(self, src:Camel.FolderChangeInfo) """
        pass

    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) -> bool """
        return False

    def change_uid(self, uid): # real signature unknown; restored from __doc__
        """ change_uid(self, uid:str) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Camel.FolderChangeInfo """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_added_uids(self): # real signature unknown; restored from __doc__
        """ get_added_uids(self) -> list """
        return []

    def get_changed_uids(self): # real signature unknown; restored from __doc__
        """ get_changed_uids(self) -> list """
        return []

    def get_recent_uids(self): # real signature unknown; restored from __doc__
        """ get_recent_uids(self) -> list """
        return []

    def get_removed_uids(self): # real signature unknown; restored from __doc__
        """ get_removed_uids(self) -> list """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Camel.FolderChangeInfo """
        pass

    def recent_uid(self, uid): # real signature unknown; restored from __doc__
        """ recent_uid(self, uid:str) """
        pass

    def remove_uid(self, uid): # real signature unknown; restored from __doc__
        """ remove_uid(self, uid:str) """
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
        """ new() -> Camel.FolderChangeInfo """
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

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid_recent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FolderChangeInfo), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelFolderChangeInfo (94124523649408)>, '__dict__': <attribute '__dict__' of 'FolderChangeInfo' objects>, '__weakref__': <attribute '__weakref__' of 'FolderChangeInfo' objects>, '__doc__': None, 'uid_added': <property object at 0x7f7b34fc7400>, 'uid_removed': <property object at 0x7f7b34fc74f0>, 'uid_changed': <property object at 0x7f7b34fc75e0>, 'uid_recent': <property object at 0x7f7b34fc76d0>, 'priv': <property object at 0x7f7b34fc77c0>, 'new': gi.FunctionInfo(new), 'add_source': gi.FunctionInfo(add_source), 'add_source_list': gi.FunctionInfo(add_source_list), 'add_uid': gi.FunctionInfo(add_uid), 'add_update': gi.FunctionInfo(add_update), 'add_update_list': gi.FunctionInfo(add_update_list), 'build_diff': gi.FunctionInfo(build_diff), 'cat': gi.FunctionInfo(cat), 'change_uid': gi.FunctionInfo(change_uid), 'changed': gi.FunctionInfo(changed), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_added_uids': gi.FunctionInfo(get_added_uids), 'get_changed_uids': gi.FunctionInfo(get_changed_uids), 'get_recent_uids': gi.FunctionInfo(get_recent_uids), 'get_removed_uids': gi.FunctionInfo(get_removed_uids), 'recent_uid': gi.FunctionInfo(recent_uid), 'remove_uid': gi.FunctionInfo(remove_uid), '__new__': <staticmethod object at 0x7f7b34fb8f70>, '__init__': <function nothing at 0x7f7b37797ee0>})"
    __gtype__ = None # (!) real value is '<GType CamelFolderChangeInfo (94124523649408)>'
    __info__ = StructInfo(FolderChangeInfo)


