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


class BookmarkFile(__gi.Struct):
    # no doc
    def add_application(self, uri, name=None, exec=None): # real signature unknown; restored from __doc__
        """ add_application(self, uri:str, name:str=None, exec:str=None) """
        pass

    def add_group(self, uri, group): # real signature unknown; restored from __doc__
        """ add_group(self, uri:str, group:str) """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_added(self, uri): # real signature unknown; restored from __doc__
        """ get_added(self, uri:str) -> int """
        return 0

    def get_applications(self, uri): # real signature unknown; restored from __doc__
        """ get_applications(self, uri:str) -> list, length:int """
        return []

    def get_app_info(self, uri, name): # real signature unknown; restored from __doc__
        """ get_app_info(self, uri:str, name:str) -> bool, exec:str, count:int, stamp:int """
        return False

    def get_description(self, uri): # real signature unknown; restored from __doc__
        """ get_description(self, uri:str) -> str """
        return ""

    def get_groups(self, uri): # real signature unknown; restored from __doc__
        """ get_groups(self, uri:str) -> list, length:int """
        return []

    def get_icon(self, uri): # real signature unknown; restored from __doc__
        """ get_icon(self, uri:str) -> bool, href:str, mime_type:str """
        return False

    def get_is_private(self, uri): # real signature unknown; restored from __doc__
        """ get_is_private(self, uri:str) -> bool """
        return False

    def get_mime_type(self, uri): # real signature unknown; restored from __doc__
        """ get_mime_type(self, uri:str) -> str """
        return ""

    def get_modified(self, uri): # real signature unknown; restored from __doc__
        """ get_modified(self, uri:str) -> int """
        return 0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_title(self, uri=None): # real signature unknown; restored from __doc__
        """ get_title(self, uri:str=None) -> str """
        return ""

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list, length:int """
        return []

    def get_visited(self, uri): # real signature unknown; restored from __doc__
        """ get_visited(self, uri:str) -> int """
        return 0

    def has_application(self, uri, name): # real signature unknown; restored from __doc__
        """ has_application(self, uri:str, name:str) -> bool """
        return False

    def has_group(self, uri, group): # real signature unknown; restored from __doc__
        """ has_group(self, uri:str, group:str) -> bool """
        return False

    def has_item(self, uri): # real signature unknown; restored from __doc__
        """ has_item(self, uri:str) -> bool """
        return False

    def load_from_data(self, data): # real signature unknown; restored from __doc__
        """ load_from_data(self, data:list) -> bool """
        return False

    def load_from_data_dirs(self, file): # real signature unknown; restored from __doc__
        """ load_from_data_dirs(self, file:str) -> bool, full_path:str """
        return False

    def load_from_file(self, filename): # real signature unknown; restored from __doc__
        """ load_from_file(self, filename:str) -> bool """
        return False

    def move_item(self, old_uri, new_uri=None): # real signature unknown; restored from __doc__
        """ move_item(self, old_uri:str, new_uri:str=None) -> bool """
        return False

    def remove_application(self, uri, name): # real signature unknown; restored from __doc__
        """ remove_application(self, uri:str, name:str) -> bool """
        return False

    def remove_group(self, uri, group): # real signature unknown; restored from __doc__
        """ remove_group(self, uri:str, group:str) -> bool """
        return False

    def remove_item(self, uri): # real signature unknown; restored from __doc__
        """ remove_item(self, uri:str) -> bool """
        return False

    def set_added(self, uri, added): # real signature unknown; restored from __doc__
        """ set_added(self, uri:str, added:int) """
        pass

    def set_app_info(self, uri, name, exec, count, stamp): # real signature unknown; restored from __doc__
        """ set_app_info(self, uri:str, name:str, exec:str, count:int, stamp:int) -> bool """
        return False

    def set_description(self, uri=None, description): # real signature unknown; restored from __doc__
        """ set_description(self, uri:str=None, description:str) """
        pass

    def set_groups(self, uri, groups=None): # real signature unknown; restored from __doc__
        """ set_groups(self, uri:str, groups:list=None) """
        pass

    def set_icon(self, uri, href=None, mime_type): # real signature unknown; restored from __doc__
        """ set_icon(self, uri:str, href:str=None, mime_type:str) """
        pass

    def set_is_private(self, uri, is_private): # real signature unknown; restored from __doc__
        """ set_is_private(self, uri:str, is_private:bool) """
        pass

    def set_mime_type(self, uri, mime_type): # real signature unknown; restored from __doc__
        """ set_mime_type(self, uri:str, mime_type:str) """
        pass

    def set_modified(self, uri, modified): # real signature unknown; restored from __doc__
        """ set_modified(self, uri:str, modified:int) """
        pass

    def set_title(self, uri=None, title): # real signature unknown; restored from __doc__
        """ set_title(self, uri:str=None, title:str) """
        pass

    def set_visited(self, uri, visited): # real signature unknown; restored from __doc__
        """ set_visited(self, uri:str, visited:int) """
        pass

    def to_data(self): # real signature unknown; restored from __doc__
        """ to_data(self) -> list, length:int """
        return []

    def to_file(self, filename): # real signature unknown; restored from __doc__
        """ to_file(self, filename:str) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookmarkFile), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BookmarkFile' objects>, '__weakref__': <attribute '__weakref__' of 'BookmarkFile' objects>, '__doc__': None, 'add_application': gi.FunctionInfo(add_application), 'add_group': gi.FunctionInfo(add_group), 'free': gi.FunctionInfo(free), 'get_added': gi.FunctionInfo(get_added), 'get_app_info': gi.FunctionInfo(get_app_info), 'get_applications': gi.FunctionInfo(get_applications), 'get_description': gi.FunctionInfo(get_description), 'get_groups': gi.FunctionInfo(get_groups), 'get_icon': gi.FunctionInfo(get_icon), 'get_is_private': gi.FunctionInfo(get_is_private), 'get_mime_type': gi.FunctionInfo(get_mime_type), 'get_modified': gi.FunctionInfo(get_modified), 'get_size': gi.FunctionInfo(get_size), 'get_title': gi.FunctionInfo(get_title), 'get_uris': gi.FunctionInfo(get_uris), 'get_visited': gi.FunctionInfo(get_visited), 'has_application': gi.FunctionInfo(has_application), 'has_group': gi.FunctionInfo(has_group), 'has_item': gi.FunctionInfo(has_item), 'load_from_data': gi.FunctionInfo(load_from_data), 'load_from_data_dirs': gi.FunctionInfo(load_from_data_dirs), 'load_from_file': gi.FunctionInfo(load_from_file), 'move_item': gi.FunctionInfo(move_item), 'remove_application': gi.FunctionInfo(remove_application), 'remove_group': gi.FunctionInfo(remove_group), 'remove_item': gi.FunctionInfo(remove_item), 'set_added': gi.FunctionInfo(set_added), 'set_app_info': gi.FunctionInfo(set_app_info), 'set_description': gi.FunctionInfo(set_description), 'set_groups': gi.FunctionInfo(set_groups), 'set_icon': gi.FunctionInfo(set_icon), 'set_is_private': gi.FunctionInfo(set_is_private), 'set_mime_type': gi.FunctionInfo(set_mime_type), 'set_modified': gi.FunctionInfo(set_modified), 'set_title': gi.FunctionInfo(set_title), 'set_visited': gi.FunctionInfo(set_visited), 'to_data': gi.FunctionInfo(to_data), 'to_file': gi.FunctionInfo(to_file), 'error_quark': gi.FunctionInfo(error_quark)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BookmarkFile)


