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


class VideoScaler(__gi.Struct):
    # no doc
    def 2d(self, vscale, format, src=None, src_stride, dest=None, dest_stride, x, y, width, height): # real signature unknown; restored from __doc__
        """ 2d(self, vscale:GstVideo.VideoScaler, format:GstVideo.VideoFormat, src=None, src_stride:int, dest=None, dest_stride:int, x:int, y:int, width:int, height:int) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_coeff(self, out_offset, in_offset, n_taps): # real signature unknown; restored from __doc__
        """ get_coeff(self, out_offset:int, in_offset:int, n_taps:int) -> float """
        return 0.0

    def get_max_taps(self): # real signature unknown; restored from __doc__
        """ get_max_taps(self) -> int """
        return 0

    def horizontal(self, format, src=None, dest=None, dest_offset, width): # real signature unknown; restored from __doc__
        """ horizontal(self, format:GstVideo.VideoFormat, src=None, dest=None, dest_offset:int, width:int) """
        pass

    def vertical(self, format, src_lines=None, dest=None, dest_offset, width): # real signature unknown; restored from __doc__
        """ vertical(self, format:GstVideo.VideoFormat, src_lines=None, dest=None, dest_offset:int, width:int) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VideoScaler), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VideoScaler' objects>, '__weakref__': <attribute '__weakref__' of 'VideoScaler' objects>, '__doc__': None, '2d': gi.FunctionInfo(2d), 'free': gi.FunctionInfo(free), 'get_coeff': gi.FunctionInfo(get_coeff), 'get_max_taps': gi.FunctionInfo(get_max_taps), 'horizontal': gi.FunctionInfo(horizontal), 'vertical': gi.FunctionInfo(vertical)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VideoScaler)


