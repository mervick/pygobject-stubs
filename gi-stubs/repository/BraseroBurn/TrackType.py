# encoding: utf-8
# module gi.repository.BraseroBurn
# from /usr/lib64/girepository-1.0/BraseroBurn-3.1.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class TrackType(__gi.Struct):
    # no doc
    def equal(self, type_B): # real signature unknown; restored from __doc__
        """ equal(self, type_B:BraseroBurn.TrackType) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_data_fs(self): # real signature unknown; restored from __doc__
        """ get_data_fs(self) -> BraseroBurn.ImageFS """
        pass

    def get_has_data(self): # real signature unknown; restored from __doc__
        """ get_has_data(self) -> bool """
        return False

    def get_has_image(self): # real signature unknown; restored from __doc__
        """ get_has_image(self) -> bool """
        return False

    def get_has_medium(self): # real signature unknown; restored from __doc__
        """ get_has_medium(self) -> bool """
        return False

    def get_has_stream(self): # real signature unknown; restored from __doc__
        """ get_has_stream(self) -> bool """
        return False

    def get_image_format(self): # real signature unknown; restored from __doc__
        """ get_image_format(self) -> BraseroBurn.ImageFormat """
        pass

    def get_stream_format(self): # real signature unknown; restored from __doc__
        """ get_stream_format(self) -> BraseroBurn.StreamFormat """
        pass

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def set_data_fs(self, fs_type): # real signature unknown; restored from __doc__
        """ set_data_fs(self, fs_type:BraseroBurn.ImageFS) """
        pass

    def set_has_data(self): # real signature unknown; restored from __doc__
        """ set_has_data(self) """
        pass

    def set_has_image(self): # real signature unknown; restored from __doc__
        """ set_has_image(self) """
        pass

    def set_has_medium(self): # real signature unknown; restored from __doc__
        """ set_has_medium(self) """
        pass

    def set_has_stream(self): # real signature unknown; restored from __doc__
        """ set_has_stream(self) """
        pass

    def set_image_format(self, format): # real signature unknown; restored from __doc__
        """ set_image_format(self, format:BraseroBurn.ImageFormat) """
        pass

    def set_stream_format(self, format): # real signature unknown; restored from __doc__
        """ set_stream_format(self, format:BraseroBurn.StreamFormat) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TrackType), '__module__': 'gi.repository.BraseroBurn', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TrackType' objects>, '__weakref__': <attribute '__weakref__' of 'TrackType' objects>, '__doc__': None, 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_data_fs': gi.FunctionInfo(get_data_fs), 'get_has_data': gi.FunctionInfo(get_has_data), 'get_has_image': gi.FunctionInfo(get_has_image), 'get_has_medium': gi.FunctionInfo(get_has_medium), 'get_has_stream': gi.FunctionInfo(get_has_stream), 'get_image_format': gi.FunctionInfo(get_image_format), 'get_stream_format': gi.FunctionInfo(get_stream_format), 'is_empty': gi.FunctionInfo(is_empty), 'set_data_fs': gi.FunctionInfo(set_data_fs), 'set_has_data': gi.FunctionInfo(set_has_data), 'set_has_image': gi.FunctionInfo(set_has_image), 'set_has_medium': gi.FunctionInfo(set_has_medium), 'set_has_stream': gi.FunctionInfo(set_has_stream), 'set_image_format': gi.FunctionInfo(set_image_format), 'set_stream_format': gi.FunctionInfo(set_stream_format)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TrackType)


