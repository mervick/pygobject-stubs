# encoding: utf-8
# module gi.repository.Gdm
# from /usr/lib64/girepository-1.0/Gdm-1.0.typelib
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


class GreeterIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GreeterIface()
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

    default_language_name_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_session_name_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_begin_auto_login = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_get_timed_login_details = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_select_session = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_select_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_start_session_when_ready = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reauthenticated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selected_user_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_opened = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timed_login_requested = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GreeterIface), '__module__': 'gi.repository.Gdm', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GreeterIface' objects>, '__weakref__': <attribute '__weakref__' of 'GreeterIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f26ef03bf40>, 'handle_begin_auto_login': <property object at 0x7f26ef03e0e0>, 'handle_get_timed_login_details': <property object at 0x7f26ef03e220>, 'handle_select_session': <property object at 0x7f26ef03e360>, 'handle_select_user': <property object at 0x7f26ef03e4a0>, 'handle_start_session_when_ready': <property object at 0x7f26ef03e5e0>, 'default_language_name_changed': <property object at 0x7f26ef03e720>, 'default_session_name_changed': <property object at 0x7f26ef03e860>, 'reauthenticated': <property object at 0x7f26ef03e950>, 'selected_user_changed': <property object at 0x7f26ef03ea90>, 'session_opened': <property object at 0x7f26ef03eb80>, 'timed_login_requested': <property object at 0x7f26ef03ecc0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GreeterIface)


