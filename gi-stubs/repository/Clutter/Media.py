# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Media(__gobject.GInterface):
    # no doc
    def get_audio_volume(self): # real signature unknown; restored from __doc__
        """ get_audio_volume(self) -> float """
        return 0.0

    def get_buffer_fill(self): # real signature unknown; restored from __doc__
        """ get_buffer_fill(self) -> float """
        return 0.0

    def get_can_seek(self): # real signature unknown; restored from __doc__
        """ get_can_seek(self) -> bool """
        return False

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> float """
        return 0.0

    def get_playing(self): # real signature unknown; restored from __doc__
        """ get_playing(self) -> bool """
        return False

    def get_progress(self): # real signature unknown; restored from __doc__
        """ get_progress(self) -> float """
        return 0.0

    def get_subtitle_font_name(self): # real signature unknown; restored from __doc__
        """ get_subtitle_font_name(self) -> str """
        return ""

    def get_subtitle_uri(self): # real signature unknown; restored from __doc__
        """ get_subtitle_uri(self) -> str """
        return ""

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def set_audio_volume(self, volume): # real signature unknown; restored from __doc__
        """ set_audio_volume(self, volume:float) """
        pass

    def set_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_filename(self, filename:str) """
        pass

    def set_playing(self, playing): # real signature unknown; restored from __doc__
        """ set_playing(self, playing:bool) """
        pass

    def set_progress(self, progress): # real signature unknown; restored from __doc__
        """ set_progress(self, progress:float) """
        pass

    def set_subtitle_font_name(self, font_name): # real signature unknown; restored from __doc__
        """ set_subtitle_font_name(self, font_name:str) """
        pass

    def set_subtitle_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_subtitle_uri(self, uri:str) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Media), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterMedia (94911696072320)>, '__dict__': <attribute '__dict__' of 'Media' objects>, '__weakref__': <attribute '__weakref__' of 'Media' objects>, '__doc__': None, '__gsignals__': {}, 'get_audio_volume': gi.FunctionInfo(get_audio_volume), 'get_buffer_fill': gi.FunctionInfo(get_buffer_fill), 'get_can_seek': gi.FunctionInfo(get_can_seek), 'get_duration': gi.FunctionInfo(get_duration), 'get_playing': gi.FunctionInfo(get_playing), 'get_progress': gi.FunctionInfo(get_progress), 'get_subtitle_font_name': gi.FunctionInfo(get_subtitle_font_name), 'get_subtitle_uri': gi.FunctionInfo(get_subtitle_uri), 'get_uri': gi.FunctionInfo(get_uri), 'set_audio_volume': gi.FunctionInfo(set_audio_volume), 'set_filename': gi.FunctionInfo(set_filename), 'set_playing': gi.FunctionInfo(set_playing), 'set_progress': gi.FunctionInfo(set_progress), 'set_subtitle_font_name': gi.FunctionInfo(set_subtitle_font_name), 'set_subtitle_uri': gi.FunctionInfo(set_subtitle_uri), 'set_uri': gi.FunctionInfo(set_uri)})"
    __gdoc__ = 'Interface ClutterMedia\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ClutterMedia (94911696072320)>'
    __info__ = InterfaceInfo(Media)


