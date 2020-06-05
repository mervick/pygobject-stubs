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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FileIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'FileIface' objects>, '__weakref__': <attribute '__weakref__' of 'FileIface' objects>, '__doc__': None, 'g_iface': <property object at 0x7f28ddefce00>, 'dup': <property object at 0x7f28ddefcef0>, 'hash': <property object at 0x7f28dde7f040>, 'equal': <property object at 0x7f28dde7f130>, 'is_native': <property object at 0x7f28dde7f220>, 'has_uri_scheme': <property object at 0x7f28dde7f310>, 'get_uri_scheme': <property object at 0x7f28dde7f400>, 'get_basename': <property object at 0x7f28dde7f4f0>, 'get_path': <property object at 0x7f28dde7f5e0>, 'get_uri': <property object at 0x7f28dde7f6d0>, 'get_parse_name': <property object at 0x7f28dde7f7c0>, 'get_parent': <property object at 0x7f28dde7f8b0>, 'prefix_matches': <property object at 0x7f28dde7f9a0>, 'get_relative_path': <property object at 0x7f28dde7fae0>, 'resolve_relative_path': <property object at 0x7f28dde7fbd0>, 'get_child_for_display_name': <property object at 0x7f28dde7fcc0>, 'enumerate_children': <property object at 0x7f28dde7fdb0>, 'enumerate_children_async': <property object at 0x7f28dde7fea0>, 'enumerate_children_finish': <property object at 0x7f28dde7ff90>, 'query_info': <property object at 0x7f28dde80090>, 'query_info_async': <property object at 0x7f28dde801d0>, 'query_info_finish': <property object at 0x7f28dde802c0>, 'query_filesystem_info': <property object at 0x7f28dde803b0>, 'query_filesystem_info_async': <property object at 0x7f28dde804a0>, 'query_filesystem_info_finish': <property object at 0x7f28dde80590>, 'find_enclosing_mount': <property object at 0x7f28dde80680>, 'find_enclosing_mount_async': <property object at 0x7f28dde80770>, 'find_enclosing_mount_finish': <property object at 0x7f28dde80860>, 'set_display_name': <property object at 0x7f28dde80950>, 'set_display_name_async': <property object at 0x7f28dde80a40>, 'set_display_name_finish': <property object at 0x7f28dde80b30>, 'query_settable_attributes': <property object at 0x7f28dde80c20>, '_query_settable_attributes_async': <property object at 0x7f28dde80cc0>, '_query_settable_attributes_finish': <property object at 0x7f28dde80db0>, 'query_writable_namespaces': <property object at 0x7f28dde80ef0>, '_query_writable_namespaces_async': <property object at 0x7f28dde80f90>, '_query_writable_namespaces_finish': <property object at 0x7f28dde810e0>, 'set_attribute': <property object at 0x7f28dde811d0>, 'set_attributes_from_info': <property object at 0x7f28dde81310>, 'set_attributes_async': <property object at 0x7f28dde81400>, 'set_attributes_finish': <property object at 0x7f28dde814f0>, 'read_fn': <property object at 0x7f28dde81590>, 'read_async': <property object at 0x7f28dde81680>, 'read_finish': <property object at 0x7f28dde81770>, 'append_to': <property object at 0x7f28dde81860>, 'append_to_async': <property object at 0x7f28dde81950>, 'append_to_finish': <property object at 0x7f28dde81a90>, 'create': <property object at 0x7f28dde81b30>, 'create_async': <property object at 0x7f28dde81c20>, 'create_finish': <property object at 0x7f28dde81d10>, 'replace': <property object at 0x7f28dde81e00>, 'replace_async': <property object at 0x7f28dde81ef0>, 'replace_finish': <property object at 0x7f28dde82040>, 'delete_file': <property object at 0x7f28dde82130>, 'delete_file_async': <property object at 0x7f28dde82270>, 'delete_file_finish': <property object at 0x7f28dde823b0>, 'trash': <property object at 0x7f28dde824a0>, 'trash_async': <property object at 0x7f28dde82590>, 'trash_finish': <property object at 0x7f28dde82680>, 'make_directory': <property object at 0x7f28dde82770>, 'make_directory_async': <property object at 0x7f28dde828b0>, 'make_directory_finish': <property object at 0x7f28dde829a0>, 'make_symbolic_link': <property object at 0x7f28dde82a90>, '_make_symbolic_link_async': <property object at 0x7f28dde82b80>, '_make_symbolic_link_finish': <property object at 0x7f28dde82cc0>, 'copy': <property object at 0x7f28dde82db0>, 'copy_async': <property object at 0x7f28dde82ea0>, 'copy_finish': <property object at 0x7f28dde82f90>, 'move': <property object at 0x7f28dde830e0>, '_move_async': <property object at 0x7f28dde831d0>, '_move_finish': <property object at 0x7f28dde832c0>, 'mount_mountable': <property object at 0x7f28dde833b0>, 'mount_mountable_finish': <property object at 0x7f28dde834f0>, 'unmount_mountable': <property object at 0x7f28dde835e0>, 'unmount_mountable_finish': <property object at 0x7f28dde836d0>, 'eject_mountable': <property object at 0x7f28dde83770>, 'eject_mountable_finish': <property object at 0x7f28dde838b0>, 'mount_enclosing_volume': <property object at 0x7f28dde839a0>, 'mount_enclosing_volume_finish': <property object at 0x7f28dde83a90>, 'monitor_dir': <property object at 0x7f28dde83b30>, 'monitor_file': <property object at 0x7f28dde83c20>, 'open_readwrite': <property object at 0x7f28dde83d10>, 'open_readwrite_async': <property object at 0x7f28dde83e50>, 'open_readwrite_finish': <property object at 0x7f28dde83f40>, 'create_readwrite': <property object at 0x7f28dde84090>, 'create_readwrite_async': <property object at 0x7f28dde84180>, 'create_readwrite_finish': <property object at 0x7f28dde84270>, 'replace_readwrite': <property object at 0x7f28dde84360>, 'replace_readwrite_async': <property object at 0x7f28dde84450>, 'replace_readwrite_finish': <property object at 0x7f28dde84540>, 'start_mountable': <property object at 0x7f28dde845e0>, 'start_mountable_finish': <property object at 0x7f28dde846d0>, 'stop_mountable': <property object at 0x7f28dde84770>, 'stop_mountable_finish': <property object at 0x7f28dde848b0>, 'supports_thread_contexts': <property object at 0x7f28dde849a0>, 'unmount_mountable_with_operation': <property object at 0x7f28dde84a40>, 'unmount_mountable_with_operation_finish': <property object at 0x7f28dde84b30>, 'eject_mountable_with_operation': <property object at 0x7f28dde84c70>, 'eject_mountable_with_operation_finish': <property object at 0x7f28dde84d10>, 'poll_mountable': <property object at 0x7f28dde84e00>, 'poll_mountable_finish': <property object at 0x7f28dde84f40>, 'measure_disk_usage': <property object at 0x7f28dde85090>, 'measure_disk_usage_async': <property object at 0x7f28dde851d0>, 'measure_disk_usage_finish': <property object at 0x7f28dde85310>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(FileIface)


