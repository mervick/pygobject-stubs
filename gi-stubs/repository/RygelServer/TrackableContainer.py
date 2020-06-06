# encoding: utf-8
# module gi.repository.RygelServer
# from /usr/lib64/girepository-1.0/RygelServer-2.6.typelib
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
import gi.repository.Gee as __gi_repository_Gee
import gi.repository.GUPnP as __gi_repository_GUPnP
import gi.repository.RygelCore as __gi_repository_RygelCore
import gobject as __gobject


class TrackableContainer(__gobject.GInterface):
    # no doc
    def add_child(self, p_object, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ add_child(self, object:RygelServer.MediaObject, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def add_child_finish(self, _res_): # real signature unknown; restored from __doc__
        """ add_child_finish(self, _res_:Gio.AsyncResult) """
        pass

    def add_child_tracked(self, p_object, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ add_child_tracked(self, object:RygelServer.MediaObject, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def add_child_tracked_finish(self, _res_): # real signature unknown; restored from __doc__
        """ add_child_tracked_finish(self, _res_:Gio.AsyncResult) """
        pass

    def clear(self, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ clear(self, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def clear_finish(self, _res_): # real signature unknown; restored from __doc__
        """ clear_finish(self, _res_:Gio.AsyncResult) """
        pass

    def get_service_reset_token(self): # real signature unknown; restored from __doc__
        """ get_service_reset_token(self) -> str """
        return ""

    def get_system_update_id(self): # real signature unknown; restored from __doc__
        """ get_system_update_id(self) -> int """
        return 0

    def remove_child(self, p_object, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ remove_child(self, object:RygelServer.MediaObject, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def remove_child_finish(self, _res_): # real signature unknown; restored from __doc__
        """ remove_child_finish(self, _res_:Gio.AsyncResult) """
        pass

    def remove_child_tracked(self, p_object, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ remove_child_tracked(self, object:RygelServer.MediaObject, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def remove_child_tracked_finish(self, _res_): # real signature unknown; restored from __doc__
        """ remove_child_tracked_finish(self, _res_:Gio.AsyncResult) """
        pass

    def set_service_reset_token(self, token): # real signature unknown; restored from __doc__
        """ set_service_reset_token(self, token:str) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(TrackableContainer), '__module__': 'gi.repository.RygelServer', '__gtype__': <GType RygelTrackableContainer (94219762696000)>, '__dict__': <attribute '__dict__' of 'TrackableContainer' objects>, '__weakref__': <attribute '__weakref__' of 'TrackableContainer' objects>, '__doc__': None, '__gsignals__': {}, 'clear': gi.FunctionInfo(clear), 'clear_finish': gi.FunctionInfo(clear_finish), 'add_child': gi.FunctionInfo(add_child), 'add_child_finish': gi.FunctionInfo(add_child_finish), 'add_child_tracked': gi.FunctionInfo(add_child_tracked), 'add_child_tracked_finish': gi.FunctionInfo(add_child_tracked_finish), 'remove_child': gi.FunctionInfo(remove_child), 'remove_child_finish': gi.FunctionInfo(remove_child_finish), 'remove_child_tracked': gi.FunctionInfo(remove_child_tracked), 'remove_child_tracked_finish': gi.FunctionInfo(remove_child_tracked_finish), 'get_service_reset_token': gi.FunctionInfo(get_service_reset_token), 'set_service_reset_token': gi.FunctionInfo(set_service_reset_token), 'get_system_update_id': gi.FunctionInfo(get_system_update_id)})"
    __gdoc__ = 'Interface RygelTrackableContainer\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelTrackableContainer (94219762696000)>'
    __info__ = InterfaceInfo(TrackableContainer)


