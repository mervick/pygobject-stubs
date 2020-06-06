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


class FileIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        FileIface()
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

    append_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    append_to_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    append_to_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_file_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_mountable_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_children_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    equal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    find_enclosing_mount_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_basename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_child_for_display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_parse_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_relative_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri_scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_uri_scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_native = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_directory_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_symbolic_link = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    measure_disk_usage_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    monitor_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    monitor_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_enclosing_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_enclosing_volume_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    move = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prefix_matches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_filesystem_info_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_info_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_settable_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_writable_namespaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    read_fn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    replace_readwrite_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resolve_relative_path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_attributes_from_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_display_name_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_thread_contexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trash_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmount_mountable_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _make_symbolic_link_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _make_symbolic_link_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _move_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _move_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_settable_attributes_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_settable_attributes_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_writable_namespaces_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _query_writable_namespaces_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FileIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'FileIface' objects>, '__weakref__': <attribute '__weakref__' of 'FileIface' objects>, '__doc__': None, 'g_iface': <property object at 0x7f4b87fe00e0>, 'dup': <property object at 0x7f4b87fe01d0>, 'hash': <property object at 0x7f4b87fe02c0>, 'equal': <property object at 0x7f4b87fe03b0>, 'is_native': <property object at 0x7f4b87fe04a0>, 'has_uri_scheme': <property object at 0x7f4b87fe0590>, 'get_uri_scheme': <property object at 0x7f4b87fe0680>, 'get_basename': <property object at 0x7f4b87fe0770>, 'get_path': <property object at 0x7f4b87fe0860>, 'get_uri': <property object at 0x7f4b87fe0950>, 'get_parse_name': <property object at 0x7f4b87fe0a40>, 'get_parent': <property object at 0x7f4b87fe0b30>, 'prefix_matches': <property object at 0x7f4b87fe0c20>, 'get_relative_path': <property object at 0x7f4b87fe0d60>, 'resolve_relative_path': <property object at 0x7f4b87fe0e50>, 'get_child_for_display_name': <property object at 0x7f4b87fe0f40>, 'enumerate_children': <property object at 0x7f4b87fe2090>, 'enumerate_children_async': <property object at 0x7f4b87fe2180>, 'enumerate_children_finish': <property object at 0x7f4b87fe2270>, 'query_info': <property object at 0x7f4b87fe2310>, 'query_info_async': <property object at 0x7f4b87fe2450>, 'query_info_finish': <property object at 0x7f4b87fe2540>, 'query_filesystem_info': <property object at 0x7f4b87fe2630>, 'query_filesystem_info_async': <property object at 0x7f4b87fe2720>, 'query_filesystem_info_finish': <property object at 0x7f4b87fe2810>, 'find_enclosing_mount': <property object at 0x7f4b87fe2900>, 'find_enclosing_mount_async': <property object at 0x7f4b87fe29f0>, 'find_enclosing_mount_finish': <property object at 0x7f4b87fe2ae0>, 'set_display_name': <property object at 0x7f4b87fe2bd0>, 'set_display_name_async': <property object at 0x7f4b87fe2cc0>, 'set_display_name_finish': <property object at 0x7f4b87fe2db0>, 'query_settable_attributes': <property object at 0x7f4b87fe2ea0>, '_query_settable_attributes_async': <property object at 0x7f4b87fe2f40>, '_query_settable_attributes_finish': <property object at 0x7f4b87fe3090>, 'query_writable_namespaces': <property object at 0x7f4b87fe31d0>, '_query_writable_namespaces_async': <property object at 0x7f4b87fe3270>, '_query_writable_namespaces_finish': <property object at 0x7f4b87fe3360>, 'set_attribute': <property object at 0x7f4b87fe3450>, 'set_attributes_from_info': <property object at 0x7f4b87fe3590>, 'set_attributes_async': <property object at 0x7f4b87fe3680>, 'set_attributes_finish': <property object at 0x7f4b87fe3770>, 'read_fn': <property object at 0x7f4b87fe37c0>, 'read_async': <property object at 0x7f4b87fe38b0>, 'read_finish': <property object at 0x7f4b87fe39a0>, 'append_to': <property object at 0x7f4b87fe3a90>, 'append_to_async': <property object at 0x7f4b87fe3b80>, 'append_to_finish': <property object at 0x7f4b87fe3cc0>, 'create': <property object at 0x7f4b87fe3d60>, 'create_async': <property object at 0x7f4b87fe3e50>, 'create_finish': <property object at 0x7f4b87fe3f40>, 'replace': <property object at 0x7f4b87fe4090>, 'replace_async': <property object at 0x7f4b87fe4180>, 'replace_finish': <property object at 0x7f4b87fe4270>, 'delete_file': <property object at 0x7f4b87fe4360>, 'delete_file_async': <property object at 0x7f4b87fe44a0>, 'delete_file_finish': <property object at 0x7f4b87fe45e0>, 'trash': <property object at 0x7f4b87fe46d0>, 'trash_async': <property object at 0x7f4b87fe47c0>, 'trash_finish': <property object at 0x7f4b87fe48b0>, 'make_directory': <property object at 0x7f4b87fe49a0>, 'make_directory_async': <property object at 0x7f4b87fe4ae0>, 'make_directory_finish': <property object at 0x7f4b87fe4bd0>, 'make_symbolic_link': <property object at 0x7f4b87fe4cc0>, '_make_symbolic_link_async': <property object at 0x7f4b87fe4db0>, '_make_symbolic_link_finish': <property object at 0x7f4b87fe4ef0>, 'copy': <property object at 0x7f4b87fe5040>, 'copy_async': <property object at 0x7f4b87fe5130>, 'copy_finish': <property object at 0x7f4b87fe5220>, 'move': <property object at 0x7f4b87fe5310>, '_move_async': <property object at 0x7f4b87fe5400>, '_move_finish': <property object at 0x7f4b87fe54f0>, 'mount_mountable': <property object at 0x7f4b87fe55e0>, 'mount_mountable_finish': <property object at 0x7f4b87fe5720>, 'unmount_mountable': <property object at 0x7f4b87fe5810>, 'unmount_mountable_finish': <property object at 0x7f4b87fe5900>, 'eject_mountable': <property object at 0x7f4b87fe59a0>, 'eject_mountable_finish': <property object at 0x7f4b87fe5ae0>, 'mount_enclosing_volume': <property object at 0x7f4b87fe5bd0>, 'mount_enclosing_volume_finish': <property object at 0x7f4b87fe5cc0>, 'monitor_dir': <property object at 0x7f4b87fe5d60>, 'monitor_file': <property object at 0x7f4b87fe5e50>, 'open_readwrite': <property object at 0x7f4b87fe5ef0>, 'open_readwrite_async': <property object at 0x7f4b87fe6090>, 'open_readwrite_finish': <property object at 0x7f4b87fe6180>, 'create_readwrite': <property object at 0x7f4b87fe6270>, 'create_readwrite_async': <property object at 0x7f4b87fe6360>, 'create_readwrite_finish': <property object at 0x7f4b87fe6450>, 'replace_readwrite': <property object at 0x7f4b87fe6540>, 'replace_readwrite_async': <property object at 0x7f4b87fe6630>, 'replace_readwrite_finish': <property object at 0x7f4b87fe6720>, 'start_mountable': <property object at 0x7f4b87fe67c0>, 'start_mountable_finish': <property object at 0x7f4b87fe6900>, 'stop_mountable': <property object at 0x7f4b87fe69a0>, 'stop_mountable_finish': <property object at 0x7f4b87fe6ae0>, 'supports_thread_contexts': <property object at 0x7f4b87fe6bd0>, 'unmount_mountable_with_operation': <property object at 0x7f4b87fe6c70>, 'unmount_mountable_with_operation_finish': <property object at 0x7f4b87fe6d60>, 'eject_mountable_with_operation': <property object at 0x7f4b87fe6ea0>, 'eject_mountable_with_operation_finish': <property object at 0x7f4b87fe6ef0>, 'poll_mountable': <property object at 0x7f4b87fe7040>, 'poll_mountable_finish': <property object at 0x7f4b87fe7180>, 'measure_disk_usage': <property object at 0x7f4b87fe7270>, 'measure_disk_usage_async': <property object at 0x7f4b87fe73b0>, 'measure_disk_usage_finish': <property object at 0x7f4b87fe74f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(FileIface)


