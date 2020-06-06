# encoding: utf-8
# module gi.repository.GstVideo
# from /usr/lib64/girepository-1.0/GstVideo-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class VideoFormatInfo(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VideoFormatInfo()
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

    bits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    h_sub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_planes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pack_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pack_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixel_stride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shift = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tile_hs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tile_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tile_ws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unpack_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unpack_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    w_sub = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoFormatInfo), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VideoFormatInfo' objects>, '__weakref__': <attribute '__weakref__' of 'VideoFormatInfo' objects>, '__doc__': None, 'format': <property object at 0x7f930d283bd0>, 'name': <property object at 0x7f930d283cc0>, 'description': <property object at 0x7f930d283db0>, 'flags': <property object at 0x7f930d283ea0>, 'bits': <property object at 0x7f930d283f90>, 'n_components': <property object at 0x7f930d2890e0>, 'shift': <property object at 0x7f930d2891d0>, 'depth': <property object at 0x7f930d2892c0>, 'pixel_stride': <property object at 0x7f930d2893b0>, 'n_planes': <property object at 0x7f930d2894a0>, 'plane': <property object at 0x7f930d289590>, 'poffset': <property object at 0x7f930d289680>, 'w_sub': <property object at 0x7f930d289770>, 'h_sub': <property object at 0x7f930d289860>, 'unpack_format': <property object at 0x7f930d289950>, 'unpack_func': <property object at 0x7f930d289a40>, 'pack_lines': <property object at 0x7f930d289b30>, 'pack_func': <property object at 0x7f930d289c20>, 'tile_mode': <property object at 0x7f930d289d10>, 'tile_ws': <property object at 0x7f930d289e00>, 'tile_hs': <property object at 0x7f930d289ef0>, '_gst_reserved': <property object at 0x7f930d28a040>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VideoFormatInfo)


