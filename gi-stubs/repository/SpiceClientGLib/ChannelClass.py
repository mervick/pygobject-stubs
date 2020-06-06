# encoding: utf-8
# module gi.repository.SpiceClientGLib
# from /usr/lib64/girepository-1.0/SpiceClientGLib-2.0.typelib
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


class ChannelClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ChannelClass()
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

    channel_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    channel_reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    channel_send_migration_handshake = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    channel_up = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deprecated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    deprecated2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_msg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterate_read = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterate_write = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open_fd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _spice_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ChannelClass), '__module__': 'gi.repository.SpiceClientGLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ChannelClass' objects>, '__weakref__': <attribute '__weakref__' of 'ChannelClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f9dce6d57c0>, 'channel_event': <property object at 0x7f9dce6d58b0>, 'open_fd': <property object at 0x7f9dce6d59a0>, 'handle_msg': <property object at 0x7f9dce6d5a90>, 'channel_up': <property object at 0x7f9dce6d5b80>, 'iterate_write': <property object at 0x7f9dce6d5c70>, 'iterate_read': <property object at 0x7f9dce6d5d60>, 'deprecated': <property object at 0x7f9dce6d5e50>, 'channel_reset': <property object at 0x7f9dce6d5f40>, 'deprecated2': <property object at 0x7f9dce6d6090>, 'channel_send_migration_handshake': <property object at 0x7f9dce6d6180>, 'priv': <property object at 0x7f9dce6d6270>, '_spice_reserved': <property object at 0x7f9dce6d6360>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ChannelClass)


