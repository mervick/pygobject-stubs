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


class SearchableContainer(__gobject.GInterface):
    # no doc
    def find_object(self, id, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ find_object(self, id:str, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def find_object_finish(self, _res_): # real signature unknown; restored from __doc__
        """ find_object_finish(self, _res_:Gio.AsyncResult) -> RygelServer.MediaObject """
        pass

    def get_search_classes(self): # real signature unknown; restored from __doc__
        """ get_search_classes(self) -> Gee.ArrayList """
        pass

    def search(self, expression=None, offset, max_count, sort_criteria, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ search(self, expression:RygelServer.SearchExpression=None, offset:int, max_count:int, sort_criteria:str, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def search_finish(self, _res_): # real signature unknown; restored from __doc__
        """ search_finish(self, _res_:Gio.AsyncResult) -> RygelServer.MediaObjects, total_matches:int """
        pass

    def set_search_classes(self, value): # real signature unknown; restored from __doc__
        """ set_search_classes(self, value:Gee.ArrayList) """
        pass

    def simple_search(self, expression=None, offset, max_count, sort_criteria, cancellable=None, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
        """ simple_search(self, expression:RygelServer.SearchExpression=None, offset:int, max_count:int, sort_criteria:str, cancellable:Gio.Cancellable=None, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
        pass

    def simple_search_finish(self, _res_): # real signature unknown; restored from __doc__
        """ simple_search_finish(self, _res_:Gio.AsyncResult) -> RygelServer.MediaObjects, total_matches:int """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(SearchableContainer), '__module__': 'gi.repository.RygelServer', '__gtype__': <GType RygelSearchableContainer (94219762691312)>, '__dict__': <attribute '__dict__' of 'SearchableContainer' objects>, '__weakref__': <attribute '__weakref__' of 'SearchableContainer' objects>, '__doc__': None, '__gsignals__': {}, 'search': gi.FunctionInfo(search), 'search_finish': gi.FunctionInfo(search_finish), 'simple_search': gi.FunctionInfo(simple_search), 'simple_search_finish': gi.FunctionInfo(simple_search_finish), 'find_object': gi.FunctionInfo(find_object), 'find_object_finish': gi.FunctionInfo(find_object_finish), 'get_search_classes': gi.FunctionInfo(get_search_classes), 'set_search_classes': gi.FunctionInfo(set_search_classes)})"
    __gdoc__ = 'Interface RygelSearchableContainer\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelSearchableContainer (94219762691312)>'
    __info__ = InterfaceInfo(SearchableContainer)


