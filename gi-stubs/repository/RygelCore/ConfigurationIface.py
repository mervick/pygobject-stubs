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


class ConfigurationIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ConfigurationIface()
    """
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

    get_allow_deletion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_allow_upload = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_bool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_engine_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_int = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_interface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_interfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_int_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_log_levels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_media_engine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_music_upload_folder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_picture_upload_folder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_plugin_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_string_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_transcoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_video_upload_folder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ConfigurationIface), '__module__': 'gi.repository.RygelCore', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ConfigurationIface' objects>, '__weakref__': <attribute '__weakref__' of 'ConfigurationIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f38205cf2c0>, 'get_interface': <property object at 0x7f38205cf3b0>, 'get_interfaces': <property object at 0x7f38205cf4a0>, 'get_port': <property object at 0x7f38205cf590>, 'get_transcoding': <property object at 0x7f38205cf680>, 'get_allow_upload': <property object at 0x7f38205cf7c0>, 'get_allow_deletion': <property object at 0x7f38205cf8b0>, 'get_log_levels': <property object at 0x7f38205cf950>, 'get_plugin_path': <property object at 0x7f38205cfa40>, 'get_engine_path': <property object at 0x7f38205cfb30>, 'get_media_engine': <property object at 0x7f38205cfc70>, 'get_video_upload_folder': <property object at 0x7f38205cfd60>, 'get_music_upload_folder': <property object at 0x7f38205cfe50>, 'get_picture_upload_folder': <property object at 0x7f38205cff40>, 'get_enabled': <property object at 0x7f38205d1040>, 'get_title': <property object at 0x7f38205d1130>, 'get_string': <property object at 0x7f38205d1220>, 'get_string_list': <property object at 0x7f38205d1310>, 'get_int': <property object at 0x7f38205d1400>, 'get_int_list': <property object at 0x7f38205d14f0>, 'get_bool': <property object at 0x7f38205d15e0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ConfigurationIface)


