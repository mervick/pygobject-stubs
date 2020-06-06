# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class VolumeMonitorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VolumeMonitorClass()
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

    adopt_orphan_mount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_connected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_disconnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_eject_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_stop_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_connected_drives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mount_for_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_volumes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_volume_for_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_pre_unmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VolumeMonitorClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VolumeMonitorClass' objects>, '__weakref__': <attribute '__weakref__' of 'VolumeMonitorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f4b87774c20>, 'volume_added': <property object at 0x7f4b87774d10>, 'volume_removed': <property object at 0x7f4b87774e00>, 'volume_changed': <property object at 0x7f4b87774ef0>, 'mount_added': <property object at 0x7f4b87776040>, 'mount_removed': <property object at 0x7f4b87776130>, 'mount_pre_unmount': <property object at 0x7f4b87776270>, 'mount_changed': <property object at 0x7f4b87776360>, 'drive_connected': <property object at 0x7f4b87776450>, 'drive_disconnected': <property object at 0x7f4b87776590>, 'drive_changed': <property object at 0x7f4b87776680>, 'is_supported': <property object at 0x7f4b87776770>, 'get_connected_drives': <property object at 0x7f4b877768b0>, 'get_volumes': <property object at 0x7f4b87776950>, 'get_mounts': <property object at 0x7f4b87776a40>, 'get_volume_for_uuid': <property object at 0x7f4b87776b80>, 'get_mount_for_uuid': <property object at 0x7f4b87776c70>, 'adopt_orphan_mount': <property object at 0x7f4b87776d60>, 'drive_eject_button': <property object at 0x7f4b87776e50>, 'drive_stop_button': <property object at 0x7f4b87776f90>, '_g_reserved1': <property object at 0x7f4b877770e0>, '_g_reserved2': <property object at 0x7f4b877771d0>, '_g_reserved3': <property object at 0x7f4b877772c0>, '_g_reserved4': <property object at 0x7f4b877773b0>, '_g_reserved5': <property object at 0x7f4b877774a0>, '_g_reserved6': <property object at 0x7f4b87777590>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VolumeMonitorClass)


