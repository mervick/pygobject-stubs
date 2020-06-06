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


class FolderSearchClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        FolderSearchClass()
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

    and_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_contains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_regex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compare_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_current_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_received_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_relative_months = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sent_date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_contains = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_ends_with = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_full_regex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_matches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_regex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_soundex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    header_starts_with = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    make_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    match_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    match_threads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    message_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    not_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    or_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    system_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FolderSearchClass), '__module__': 'gi.repository.Camel', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'FolderSearchClass' objects>, '__weakref__': <attribute '__weakref__' of 'FolderSearchClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f7b34fd34a0>, 'and_': <property object at 0x7f7b34fd3590>, 'or_': <property object at 0x7f7b34fd3680>, 'not_': <property object at 0x7f7b34fd3770>, 'lt': <property object at 0x7f7b34fd3810>, 'gt': <property object at 0x7f7b34fd3900>, 'eq': <property object at 0x7f7b34fd39f0>, 'match_all': <property object at 0x7f7b34fd3ae0>, 'match_threads': <property object at 0x7f7b34fd3bd0>, 'body_contains': <property object at 0x7f7b34fd3cc0>, 'body_regex': <property object at 0x7f7b34fd3db0>, 'header_contains': <property object at 0x7f7b34fd3ea0>, 'header_matches': <property object at 0x7f7b34fd3f90>, 'header_starts_with': <property object at 0x7f7b34fd5130>, 'header_ends_with': <property object at 0x7f7b34fd5270>, 'header_exists': <property object at 0x7f7b34fd5360>, 'header_soundex': <property object at 0x7f7b34fd5450>, 'header_regex': <property object at 0x7f7b34fd5540>, 'header_full_regex': <property object at 0x7f7b34fd5680>, 'user_flag': <property object at 0x7f7b34fd5770>, 'user_tag': <property object at 0x7f7b34fd5860>, 'system_flag': <property object at 0x7f7b34fd5950>, 'get_sent_date': <property object at 0x7f7b34fd5a40>, 'get_received_date': <property object at 0x7f7b34fd5b80>, 'get_current_date': <property object at 0x7f7b34fd5cc0>, 'get_relative_months': <property object at 0x7f7b34fd5e00>, 'get_size': <property object at 0x7f7b34fd5ef0>, 'uid': <property object at 0x7f7b34fd6040>, 'message_location': <property object at 0x7f7b34fd6180>, 'make_time': <property object at 0x7f7b34fd6270>, 'compare_date': <property object at 0x7f7b34fd6360>, 'reserved': <property object at 0x7f7b34fd6450>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(FolderSearchClass)


