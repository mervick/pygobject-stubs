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


class MDRaidIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        MDRaidIface()
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

    get_active_devices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_bitmap_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_chunk_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_degraded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_num_devices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sync_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sync_completed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sync_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sync_remaining_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_add_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_delete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_remove_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_request_sync_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_bitmap_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MDRaidIface), '__module__': 'gi.repository.UDisks', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'MDRaidIface' objects>, '__weakref__': <attribute '__weakref__' of 'MDRaidIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f13a805dd10>, 'handle_add_device': <property object at 0x7f13a805de50>, 'handle_delete': <property object at 0x7f13a805df40>, 'handle_remove_device': <property object at 0x7f13a80600e0>, 'handle_request_sync_action': <property object at 0x7f13a8060220>, 'handle_set_bitmap_location': <property object at 0x7f13a8060360>, 'handle_start': <property object at 0x7f13a8060450>, 'handle_stop': <property object at 0x7f13a8060540>, 'get_active_devices': <property object at 0x7f13a8060680>, 'get_bitmap_location': <property object at 0x7f13a80607c0>, 'get_child_configuration': <property object at 0x7f13a8060900>, 'get_chunk_size': <property object at 0x7f13a80609a0>, 'get_degraded': <property object at 0x7f13a8060a90>, 'get_level': <property object at 0x7f13a8060b80>, 'get_name': <property object at 0x7f13a8060c70>, 'get_num_devices': <property object at 0x7f13a8060d60>, 'get_running': <property object at 0x7f13a8060e50>, 'get_size': <property object at 0x7f13a8060f40>, 'get_sync_action': <property object at 0x7f13a8061090>, 'get_sync_completed': <property object at 0x7f13a80611d0>, 'get_sync_rate': <property object at 0x7f13a80612c0>, 'get_sync_remaining_time': <property object at 0x7f13a8061400>, 'get_uuid': <property object at 0x7f13a80614f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(MDRaidIface)


