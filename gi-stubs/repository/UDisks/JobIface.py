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


class JobIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        JobIface()
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

    completed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_bytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_cancelable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_expected_end_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_objects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_progress_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_started_by_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(JobIface), '__module__': 'gi.repository.UDisks', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'JobIface' objects>, '__weakref__': <attribute '__weakref__' of 'JobIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f13a80548b0>, 'handle_cancel': <property object at 0x7f13a80549a0>, 'get_cancelable': <property object at 0x7f13a8054a90>, 'get_expected_end_time': <property object at 0x7f13a8054bd0>, 'get_objects': <property object at 0x7f13a8054cc0>, 'get_operation': <property object at 0x7f13a8054db0>, 'get_progress': <property object at 0x7f13a8054ea0>, 'get_progress_valid': <property object at 0x7f13a8057040>, 'get_start_time': <property object at 0x7f13a8057130>, 'get_started_by_uid': <property object at 0x7f13a8057270>, 'completed': <property object at 0x7f13a8057360>, 'get_bytes': <property object at 0x7f13a8057450>, 'get_rate': <property object at 0x7f13a8057540>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(JobIface)


