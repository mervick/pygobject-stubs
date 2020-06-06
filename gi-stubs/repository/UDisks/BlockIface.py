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


class BlockIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BlockIface()
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

    get_configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_crypto_backing_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_device_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_drive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hint_auto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hint_icon_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hint_ignore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hint_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hint_partitionable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hint_symbolic_icon_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_hint_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id_label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id_usage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mdraid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mdraid_member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_read_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_symlinks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_userspace_mount_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_add_configuration_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_get_secret_configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_open_device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_open_for_backup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_open_for_benchmark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_open_for_restore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_remove_configuration_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_rescan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_update_configuration_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BlockIface), '__module__': 'gi.repository.UDisks', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BlockIface' objects>, '__weakref__': <attribute '__weakref__' of 'BlockIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f13a815a720>, 'handle_add_configuration_item': <property object at 0x7f13a815a7c0>, 'handle_format': <property object at 0x7f13a815a810>, 'handle_get_secret_configuration': <property object at 0x7f13a815a8b0>, 'handle_open_for_backup': <property object at 0x7f13a815a9f0>, 'handle_open_for_benchmark': <property object at 0x7f13a815ab30>, 'handle_open_for_restore': <property object at 0x7f13a815ac70>, 'handle_remove_configuration_item': <property object at 0x7f13a815ad60>, 'handle_rescan': <property object at 0x7f13a815ae50>, 'handle_update_configuration_item': <property object at 0x7f13a815af40>, 'get_configuration': <property object at 0x7f13a815f0e0>, 'get_crypto_backing_device': <property object at 0x7f13a815f220>, 'get_device': <property object at 0x7f13a815f310>, 'get_device_number': <property object at 0x7f13a815f450>, 'get_drive': <property object at 0x7f13a815f540>, 'get_hint_auto': <property object at 0x7f13a815f630>, 'get_hint_icon_name': <property object at 0x7f13a815f770>, 'get_hint_ignore': <property object at 0x7f13a815f860>, 'get_hint_name': <property object at 0x7f13a815f950>, 'get_hint_partitionable': <property object at 0x7f13a815fa90>, 'get_hint_system': <property object at 0x7f13a815fb80>, 'get_id_label': <property object at 0x7f13a815fc70>, 'get_id_type': <property object at 0x7f13a815fd60>, 'get_id_usage': <property object at 0x7f13a815fe50>, 'get_id_uuid': <property object at 0x7f13a815ff40>, 'get_id_version': <property object at 0x7f13a8160090>, 'get_preferred_device': <property object at 0x7f13a81601d0>, 'get_read_only': <property object at 0x7f13a81602c0>, 'get_size': <property object at 0x7f13a81603b0>, 'get_symlinks': <property object at 0x7f13a81604a0>, 'get_userspace_mount_options': <property object at 0x7f13a81605e0>, 'get_hint_symbolic_icon_name': <property object at 0x7f13a8160720>, 'get_id': <property object at 0x7f13a8160810>, 'get_mdraid': <property object at 0x7f13a8160900>, 'get_mdraid_member': <property object at 0x7f13a8160a40>, 'handle_open_device': <property object at 0x7f13a8160b80>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BlockIface)


