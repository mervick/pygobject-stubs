# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


class SettingClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        SettingClass()
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

    aggregate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    clear_secrets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    compare_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    duplicate_copy_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    for_each_secret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_secret_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    init_from_dbus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    need_secrets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    setting_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_secret_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    update_one_secret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verify_secrets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SettingClass), '__module__': 'gi.repository.NM', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'SettingClass' objects>, '__weakref__': <attribute '__weakref__' of 'SettingClass' objects>, '__doc__': None, 'parent': <property object at 0x7fb9b84e4a90>, 'verify': <property object at 0x7fb9b84e4b80>, 'verify_secrets': <property object at 0x7fb9b84e4c70>, 'need_secrets': <property object at 0x7fb9b84e4d60>, 'update_one_secret': <property object at 0x7fb9b84e4ea0>, 'get_secret_flags': <property object at 0x7fb9b84e6040>, 'set_secret_flags': <property object at 0x7fb9b84e6130>, 'clear_secrets': <property object at 0x7fb9b84e61d0>, 'compare_property': <property object at 0x7fb9b84e6310>, 'duplicate_copy_properties': <property object at 0x7fb9b84e6450>, 'enumerate_values': <property object at 0x7fb9b84e6590>, 'aggregate': <property object at 0x7fb9b84e6630>, 'for_each_secret': <property object at 0x7fb9b84e6720>, 'init_from_dbus': <property object at 0x7fb9b84e6810>, 'padding': <property object at 0x7fb9b84e6900>, 'setting_info': <property object at 0x7fb9b84e69f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(SettingClass)


