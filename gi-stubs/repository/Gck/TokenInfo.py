# encoding: utf-8
# module gi.repository.Gck
# from /usr/lib64/girepository-1.0/Gck-1.typelib
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


class TokenInfo(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        TokenInfo()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gck.TokenInfo """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

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

    firmware_version_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    firmware_version_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free_private_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    free_public_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hardware_version_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hardware_version_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    manufacturer_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_pin_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_rw_session_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_session_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_pin_len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rw_session_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    serial_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    session_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_private_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    total_public_memory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    utc_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TokenInfo), '__module__': 'gi.repository.Gck', '__gtype__': <GType GckTokenInfo (94702127946800)>, '__dict__': <attribute '__dict__' of 'TokenInfo' objects>, '__weakref__': <attribute '__weakref__' of 'TokenInfo' objects>, '__doc__': None, 'label': <property object at 0x7fc2e61562c0>, 'manufacturer_id': <property object at 0x7fc2e61563b0>, 'model': <property object at 0x7fc2e61564a0>, 'serial_number': <property object at 0x7fc2e6156590>, 'flags': <property object at 0x7fc2e6156680>, 'max_session_count': <property object at 0x7fc2e61567c0>, 'session_count': <property object at 0x7fc2e61568b0>, 'max_rw_session_count': <property object at 0x7fc2e61569f0>, 'rw_session_count': <property object at 0x7fc2e6156b30>, 'max_pin_len': <property object at 0x7fc2e6156c20>, 'min_pin_len': <property object at 0x7fc2e6156d10>, 'total_public_memory': <property object at 0x7fc2e6156e50>, 'free_public_memory': <property object at 0x7fc2e6156f90>, 'total_private_memory': <property object at 0x7fc2e6157130>, 'free_private_memory': <property object at 0x7fc2e6157270>, 'hardware_version_major': <property object at 0x7fc2e61573b0>, 'hardware_version_minor': <property object at 0x7fc2e61574a0>, 'firmware_version_major': <property object at 0x7fc2e6157590>, 'firmware_version_minor': <property object at 0x7fc2e6157680>, 'utc_time': <property object at 0x7fc2e6157720>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free)})"
    __gtype__ = None # (!) real value is '<GType GckTokenInfo (94702127946800)>'
    __info__ = StructInfo(TokenInfo)


