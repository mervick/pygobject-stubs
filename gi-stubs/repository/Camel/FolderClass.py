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


class FolderClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        FolderClass()
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

    append_message_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cmp_uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    count_by_expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    delete_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expunge_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freeze = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free_summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free_uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_cached = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_user_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_message_user_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_permanent_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_quota_info_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uncached_uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_search_capability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_frozen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prepare_content_refresh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    purge_message_cache_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refresh_info_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    renamed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved_methods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved_signals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    search_by_expression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    search_by_uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    search_free = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_message_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_message_user_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_message_user_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sort_uids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    synchronize_message_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    synchronize_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thaw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transfer_messages_to_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FolderClass), '__module__': 'gi.repository.Camel', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'FolderClass' objects>, '__weakref__': <attribute '__weakref__' of 'FolderClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f7b34fc7b30>, 'get_message_count': <property object at 0x7f7b34fc7c70>, 'get_permanent_flags': <property object at 0x7f7b34fc7d60>, 'get_message_flags': <property object at 0x7f7b34fc7e50>, 'set_message_flags': <property object at 0x7f7b34fc7f40>, 'get_message_user_flag': <property object at 0x7f7b34fc9090>, 'set_message_user_flag': <property object at 0x7f7b34fc9180>, 'get_message_user_tag': <property object at 0x7f7b34fc9270>, 'set_message_user_tag': <property object at 0x7f7b34fc9360>, 'get_uids': <property object at 0x7f7b34fc9400>, 'free_uids': <property object at 0x7f7b34fc94f0>, 'cmp_uids': <property object at 0x7f7b34fc95e0>, 'sort_uids': <property object at 0x7f7b34fc96d0>, 'get_summary': <property object at 0x7f7b34fc97c0>, 'free_summary': <property object at 0x7f7b34fc98b0>, 'has_search_capability': <property object at 0x7f7b34fc99f0>, 'search_by_expression': <property object at 0x7f7b34fc9b30>, 'search_by_uids': <property object at 0x7f7b34fc9bd0>, 'search_free': <property object at 0x7f7b34fc9cc0>, 'get_message_info': <property object at 0x7f7b34fc9e00>, 'delete_': <property object at 0x7f7b34fc9ea0>, 'rename': <property object at 0x7f7b34fc9f90>, 'freeze': <property object at 0x7f7b34fcc0e0>, 'thaw': <property object at 0x7f7b34fcc1d0>, 'is_frozen': <property object at 0x7f7b34fcc2c0>, 'count_by_expression': <property object at 0x7f7b34fcc400>, 'get_uncached_uids': <property object at 0x7f7b34fcc4f0>, 'get_filename': <property object at 0x7f7b34fcc590>, 'get_message_cached': <property object at 0x7f7b34fcc6d0>, 'append_message_sync': <property object at 0x7f7b34fcc7c0>, 'expunge_sync': <property object at 0x7f7b34fcc860>, 'get_message_sync': <property object at 0x7f7b34fcc9a0>, 'get_quota_info_sync': <property object at 0x7f7b34fcca90>, 'purge_message_cache_sync': <property object at 0x7f7b34fccb80>, 'refresh_info_sync': <property object at 0x7f7b34fccc70>, 'synchronize_sync': <property object at 0x7f7b34fccd60>, 'synchronize_message_sync': <property object at 0x7f7b34fcce50>, 'transfer_messages_to_sync': <property object at 0x7f7b34fccf40>, 'prepare_content_refresh': <property object at 0x7f7b34fcd090>, 'reserved_methods': <property object at 0x7f7b34fcd180>, 'changed': <property object at 0x7f7b34fcd270>, 'deleted': <property object at 0x7f7b34fcd360>, 'renamed': <property object at 0x7f7b34fcd450>, 'reserved_signals': <property object at 0x7f7b34fcd590>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(FolderClass)


