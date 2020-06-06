# encoding: utf-8
# module gi.repository.RygelCore
# from /usr/lib64/girepository-1.0/RygelCore-2.6.typelib
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
import gi.repository.GUPnP as __gi_repository_GUPnP
import gobject as __gobject


class Configuration(__gobject.GInterface):
    # no doc
    def get_allow_deletion(self): # real signature unknown; restored from __doc__
        """ get_allow_deletion(self) -> bool """
        return False

    def get_allow_upload(self): # real signature unknown; restored from __doc__
        """ get_allow_upload(self) -> bool """
        return False

    def get_bool(self, section, key): # real signature unknown; restored from __doc__
        """ get_bool(self, section:str, key:str) -> bool """
        return False

    def get_enabled(self, section): # real signature unknown; restored from __doc__
        """ get_enabled(self, section:str) -> bool """
        return False

    def get_engine_path(self): # real signature unknown; restored from __doc__
        """ get_engine_path(self) -> str """
        return ""

    def get_int(self, section, key, min, max): # real signature unknown; restored from __doc__
        """ get_int(self, section:str, key:str, min:int, max:int) -> int """
        return 0

    def get_interface(self): # real signature unknown; restored from __doc__
        """ get_interface(self) -> str """
        return ""

    def get_interfaces(self): # real signature unknown; restored from __doc__
        """ get_interfaces(self) -> list """
        return []

    def get_int_list(self, section, key): # real signature unknown; restored from __doc__
        """ get_int_list(self, section:str, key:str) -> Gee.ArrayList """
        pass

    def get_log_levels(self): # real signature unknown; restored from __doc__
        """ get_log_levels(self) -> str """
        return ""

    def get_media_engine(self): # real signature unknown; restored from __doc__
        """ get_media_engine(self) -> str """
        return ""

    def get_music_upload_folder(self): # real signature unknown; restored from __doc__
        """ get_music_upload_folder(self) -> str """
        return ""

    def get_picture_upload_folder(self): # real signature unknown; restored from __doc__
        """ get_picture_upload_folder(self) -> str """
        return ""

    def get_plugin_path(self): # real signature unknown; restored from __doc__
        """ get_plugin_path(self) -> str """
        return ""

    def get_port(self): # real signature unknown; restored from __doc__
        """ get_port(self) -> int """
        return 0

    def get_string(self, section, key): # real signature unknown; restored from __doc__
        """ get_string(self, section:str, key:str) -> str """
        return ""

    def get_string_list(self, section, key): # real signature unknown; restored from __doc__
        """ get_string_list(self, section:str, key:str) -> Gee.ArrayList """
        pass

    def get_title(self, section): # real signature unknown; restored from __doc__
        """ get_title(self, section:str) -> str """
        return ""

    def get_transcoding(self): # real signature unknown; restored from __doc__
        """ get_transcoding(self) -> bool """
        return False

    def get_video_upload_folder(self): # real signature unknown; restored from __doc__
        """ get_video_upload_folder(self) -> str """
        return ""

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Configuration), '__module__': 'gi.repository.RygelCore', '__gtype__': <GType RygelConfiguration (94624372598640)>, '__dict__': <attribute '__dict__' of 'Configuration' objects>, '__weakref__': <attribute '__weakref__' of 'Configuration' objects>, '__doc__': None, '__gsignals__': {}, 'get_interface': gi.FunctionInfo(get_interface), 'get_interfaces': gi.FunctionInfo(get_interfaces), 'get_port': gi.FunctionInfo(get_port), 'get_transcoding': gi.FunctionInfo(get_transcoding), 'get_allow_upload': gi.FunctionInfo(get_allow_upload), 'get_allow_deletion': gi.FunctionInfo(get_allow_deletion), 'get_log_levels': gi.FunctionInfo(get_log_levels), 'get_plugin_path': gi.FunctionInfo(get_plugin_path), 'get_engine_path': gi.FunctionInfo(get_engine_path), 'get_media_engine': gi.FunctionInfo(get_media_engine), 'get_video_upload_folder': gi.FunctionInfo(get_video_upload_folder), 'get_music_upload_folder': gi.FunctionInfo(get_music_upload_folder), 'get_picture_upload_folder': gi.FunctionInfo(get_picture_upload_folder), 'get_enabled': gi.FunctionInfo(get_enabled), 'get_title': gi.FunctionInfo(get_title), 'get_string': gi.FunctionInfo(get_string), 'get_string_list': gi.FunctionInfo(get_string_list), 'get_int': gi.FunctionInfo(get_int), 'get_int_list': gi.FunctionInfo(get_int_list), 'get_bool': gi.FunctionInfo(get_bool)})"
    __gdoc__ = 'Interface RygelConfiguration\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelConfiguration (94624372598640)>'
    __info__ = InterfaceInfo(Configuration)


