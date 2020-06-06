# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class DriveIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DriveIface()
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

    get_can_power_off = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_connection_bus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_ejectable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_media = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_media_available = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_media_change_detected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_media_compatibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_media_removable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_optical = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_optical_blank = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_optical_num_audio_tracks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_optical_num_data_tracks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_optical_num_sessions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_optical_num_tracks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_removable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_revision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_rotation_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_seat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sibling_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sort_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_time_detected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_time_media_detected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_vendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_wwn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_eject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_power_off = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DriveIface), '__module__': 'gi.repository.UDisks', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DriveIface' objects>, '__weakref__': <attribute '__weakref__' of 'DriveIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f13a816c4a0>, 'handle_eject': <property object at 0x7f13a816c590>, 'handle_set_configuration': <property object at 0x7f13a816c6d0>, 'get_configuration': <property object at 0x7f13a816c810>, 'get_connection_bus': <property object at 0x7f13a816c900>, 'get_ejectable': <property object at 0x7f13a816c9f0>, 'get_id': <property object at 0x7f13a816cae0>, 'get_media': <property object at 0x7f13a816cbd0>, 'get_media_available': <property object at 0x7f13a816cd10>, 'get_media_change_detected': <property object at 0x7f13a816ce50>, 'get_media_compatibility': <property object at 0x7f13a816cf90>, 'get_media_removable': <property object at 0x7f13a816e130>, 'get_model': <property object at 0x7f13a816e1d0>, 'get_optical': <property object at 0x7f13a816e2c0>, 'get_optical_blank': <property object at 0x7f13a816e400>, 'get_optical_num_audio_tracks': <property object at 0x7f13a816e540>, 'get_optical_num_data_tracks': <property object at 0x7f13a816e680>, 'get_optical_num_sessions': <property object at 0x7f13a816e7c0>, 'get_optical_num_tracks': <property object at 0x7f13a816e900>, 'get_removable': <property object at 0x7f13a816e9f0>, 'get_revision': <property object at 0x7f13a816eae0>, 'get_rotation_rate': <property object at 0x7f13a816ec20>, 'get_seat': <property object at 0x7f13a816ed10>, 'get_serial': <property object at 0x7f13a816ee00>, 'get_size': <property object at 0x7f13a816eef0>, 'get_sort_key': <property object at 0x7f13a816f040>, 'get_time_detected': <property object at 0x7f13a816f180>, 'get_time_media_detected': <property object at 0x7f13a816f2c0>, 'get_vendor': <property object at 0x7f13a816f3b0>, 'get_wwn': <property object at 0x7f13a816f4a0>, 'handle_power_off': <property object at 0x7f13a816f5e0>, 'get_can_power_off': <property object at 0x7f13a816f720>, 'get_sibling_id': <property object at 0x7f13a816f810>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DriveIface)


