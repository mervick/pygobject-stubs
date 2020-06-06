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


class VideoOverlay(__gobject.GInterface):
    # no doc
    def expose(self): # real signature unknown; restored from __doc__
        """ expose(self) """
        pass

    def got_window_handle(self, handle): # real signature unknown; restored from __doc__
        """ got_window_handle(self, handle:int) """
        pass

    def handle_events(self, handle_events): # real signature unknown; restored from __doc__
        """ handle_events(self, handle_events:bool) """
        pass

    def install_properties(self, oclass, last_prop_id): # real signature unknown; restored from __doc__
        """ install_properties(oclass:GObject.ObjectClass, last_prop_id:int) """
        pass

    def prepare_window_handle(self): # real signature unknown; restored from __doc__
        """ prepare_window_handle(self) """
        pass

    def set_property(self, p_object, last_prop_id, property_id, value): # real signature unknown; restored from __doc__
        """ set_property(object:GObject.Object, last_prop_id:int, property_id:int, value:GObject.Value) -> bool """
        return False

    def set_render_rectangle(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ set_render_rectangle(self, x:int, y:int, width:int, height:int) -> bool """
        return False

    def set_window_handle(self, handle): # real signature unknown; restored from __doc__
        """ set_window_handle(self, handle:int) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(VideoOverlay), '__module__': 'gi.repository.GstVideo', '__gtype__': <GType GstVideoOverlay (94743669531360)>, '__dict__': <attribute '__dict__' of 'VideoOverlay' objects>, '__weakref__': <attribute '__weakref__' of 'VideoOverlay' objects>, '__doc__': None, '__gsignals__': {}, 'install_properties': gi.FunctionInfo(install_properties), 'set_property': gi.FunctionInfo(set_property), 'expose': gi.FunctionInfo(expose), 'got_window_handle': gi.FunctionInfo(got_window_handle), 'handle_events': gi.FunctionInfo(handle_events), 'prepare_window_handle': gi.FunctionInfo(prepare_window_handle), 'set_render_rectangle': gi.FunctionInfo(set_render_rectangle), 'set_window_handle': gi.FunctionInfo(set_window_handle)})"
    __gdoc__ = 'Interface GstVideoOverlay\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstVideoOverlay (94743669531360)>'
    __info__ = InterfaceInfo(VideoOverlay)

