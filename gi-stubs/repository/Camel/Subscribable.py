# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class Subscribable(__gobject.GInterface):
    # no doc
    def folder_is_subscribed(self, folder_name): # real signature unknown; restored from __doc__
        """ folder_is_subscribed(self, folder_name:str) -> bool """
        return False

    def folder_subscribed(self, folder_info): # real signature unknown; restored from __doc__
        """ folder_subscribed(self, folder_info:Camel.FolderInfo) """
        pass

    def folder_unsubscribed(self, folder_info): # real signature unknown; restored from __doc__
        """ folder_unsubscribed(self, folder_info:Camel.FolderInfo) """
        pass

    def subscribe_folder(self, folder_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ subscribe_folder(self, folder_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def subscribe_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ subscribe_folder_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def subscribe_folder_sync(self, folder_name, cancellable=None): # real signature unknown; restored from __doc__
        """ subscribe_folder_sync(self, folder_name:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def unsubscribe_folder(self, folder_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unsubscribe_folder(self, folder_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unsubscribe_folder_finish(self, result): # real signature unknown; restored from __doc__
        """ unsubscribe_folder_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unsubscribe_folder_sync(self, folder_name, cancellable=None): # real signature unknown; restored from __doc__
        """ unsubscribe_folder_sync(self, folder_name:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Subscribable), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelSubscribable (94124524330704)>, '__dict__': <attribute '__dict__' of 'Subscribable' objects>, '__weakref__': <attribute '__weakref__' of 'Subscribable' objects>, '__doc__': None, '__gsignals__': {}, 'folder_is_subscribed': gi.FunctionInfo(folder_is_subscribed), 'folder_subscribed': gi.FunctionInfo(folder_subscribed), 'folder_unsubscribed': gi.FunctionInfo(folder_unsubscribed), 'subscribe_folder': gi.FunctionInfo(subscribe_folder), 'subscribe_folder_finish': gi.FunctionInfo(subscribe_folder_finish), 'subscribe_folder_sync': gi.FunctionInfo(subscribe_folder_sync), 'unsubscribe_folder': gi.FunctionInfo(unsubscribe_folder), 'unsubscribe_folder_finish': gi.FunctionInfo(unsubscribe_folder_finish), 'unsubscribe_folder_sync': gi.FunctionInfo(unsubscribe_folder_sync)})"
    __gdoc__ = 'Interface CamelSubscribable\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelSubscribable (94124524330704)>'
    __info__ = InterfaceInfo(Subscribable)


