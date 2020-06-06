# encoding: utf-8
# module gi.repository.GUPnPDLNA
# from /usr/lib64/girepository-1.0/GUPnPDLNA-2.0.typelib
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
import gobject as __gobject


class AudioInformationClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AudioInformationClass()
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

    get_bitrate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mpeg_audio_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mpeg_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_stream_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_wma_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AudioInformationClass), '__module__': 'gi.repository.GUPnPDLNA', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AudioInformationClass' objects>, '__weakref__': <attribute '__weakref__' of 'AudioInformationClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f67847e01d0>, 'get_bitrate': <property object at 0x7f67847c5f40>, 'get_channels': <property object at 0x7f67847c5e50>, 'get_depth': <property object at 0x7f67847c5c70>, 'get_layer': <property object at 0x7f67847c5a40>, 'get_level': <property object at 0x7f6785ac9180>, 'get_mpeg_audio_version': <property object at 0x7f6784764810>, 'get_mpeg_version': <property object at 0x7f6784764950>, 'get_profile': <property object at 0x7f6784764a40>, 'get_rate': <property object at 0x7f6784764b30>, 'get_stream_format': <property object at 0x7f6784764c70>, 'get_wma_version': <property object at 0x7f6784764d60>, 'get_mime': <property object at 0x7f6784764e50>, '_reserved': <property object at 0x7f6784764f40>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AudioInformationClass)


