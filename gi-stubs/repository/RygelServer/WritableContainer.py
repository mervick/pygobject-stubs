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


class WritableContainer(__gobject.GInterface):
    # no doc
    def add_container(self, container, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ add_container(self, container:RygelServer.MediaContainer, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def add_container_finish(self, _res_): # real signature unknown; restored from __doc__
        """ add_container_finish(self, _res_:Gio.AsyncResult) """
        pass

    def add_item(self, item, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ add_item(self, item:RygelServer.MediaFileItem, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def add_item_finish(self, _res_): # real signature unknown; restored from __doc__
        """ add_item_finish(self, _res_:Gio.AsyncResult) """
        pass

    def add_reference(self, p_object, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ add_reference(self, object:RygelServer.MediaObject, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def add_reference_finish(self, _res_): # real signature unknown; restored from __doc__
        """ add_reference_finish(self, _res_:Gio.AsyncResult) -> str """
        return ""

    def can_create(self, upnp_class): # real signature unknown; restored from __doc__
        """ can_create(self, upnp_class:str) -> bool """
        return False

    def get_create_classes(self): # real signature unknown; restored from __doc__
        """ get_create_classes(self) -> Gee.ArrayList """
        pass

    def remove_container(self, id, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ remove_container(self, id:str, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def remove_container_finish(self, _res_): # real signature unknown; restored from __doc__
        """ remove_container_finish(self, _res_:Gio.AsyncResult) """
        pass

    def remove_item(self, id, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ remove_item(self, id:str, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def remove_item_finish(self, _res_): # real signature unknown; restored from __doc__
        """ remove_item_finish(self, _res_:Gio.AsyncResult) """
        pass

    def set_create_classes(self, value): # real signature unknown; restored from __doc__
        """ set_create_classes(self, value:Gee.ArrayList) """
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

    WRITABLE_SCHEME = 'rygel-writable://'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(WritableContainer), '__module__': 'gi.repository.RygelServer', '__gtype__': <GType RygelWritableContainer (94219762531344)>, '__dict__': <attribute '__dict__' of 'WritableContainer' objects>, '__weakref__': <attribute '__weakref__' of 'WritableContainer' objects>, '__doc__': None, '__gsignals__': {}, 'can_create': gi.FunctionInfo(can_create), 'add_item': gi.FunctionInfo(add_item), 'add_item_finish': gi.FunctionInfo(add_item_finish), 'add_container': gi.FunctionInfo(add_container), 'add_container_finish': gi.FunctionInfo(add_container_finish), 'add_reference': gi.FunctionInfo(add_reference), 'add_reference_finish': gi.FunctionInfo(add_reference_finish), 'remove_item': gi.FunctionInfo(remove_item), 'remove_item_finish': gi.FunctionInfo(remove_item_finish), 'remove_container': gi.FunctionInfo(remove_container), 'remove_container_finish': gi.FunctionInfo(remove_container_finish), 'get_create_classes': gi.FunctionInfo(get_create_classes), 'set_create_classes': gi.FunctionInfo(set_create_classes), 'WRITABLE_SCHEME': 'rygel-writable://'})"
    __gdoc__ = 'Interface RygelWritableContainer\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelWritableContainer (94219762531344)>'
    __info__ = InterfaceInfo(WritableContainer)


