# encoding: utf-8
# module gi.repository.GData
# from /usr/lib64/girepository-1.0/GData-0.0.typelib
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


class Commentable(__gobject.GInterface):
    # no doc
    def delete_comment(self, service, comment_, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_comment(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_comment_async(self, service, comment_, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_comment_async(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_comment_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_comment_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def insert_comment(self, service, comment_, cancellable=None): # real signature unknown; restored from __doc__
        """ insert_comment(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None) -> GData.Comment or None """
        pass

    def insert_comment_async(self, service, comment_, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ insert_comment_async(self, service:GData.Service, comment_:GData.Comment, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def insert_comment_finish(self, result): # real signature unknown; restored from __doc__
        """ insert_comment_finish(self, result:Gio.AsyncResult) -> GData.Comment or None """
        pass

    def query_comments(self, service, query=None, cancellable=None, progress_callback=None, progress_user_data=None): # real signature unknown; restored from __doc__
        """ query_comments(self, service:GData.Service, query:GData.Query=None, cancellable:Gio.Cancellable=None, progress_callback:GData.QueryProgressCallback=None, progress_user_data=None) -> GData.Feed or None """
        pass

    def query_comments_async(self, service, query=None, cancellable=None, progress_callback=None, progress_user_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_comments_async(self, service:GData.Service, query:GData.Query=None, cancellable:Gio.Cancellable=None, progress_callback:GData.QueryProgressCallback=None, progress_user_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_comments_finish(self, result): # real signature unknown; restored from __doc__
        """ query_comments_finish(self, result:Gio.AsyncResult) -> GData.Feed or None """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Commentable), '__module__': 'gi.repository.GData', '__gtype__': <GType GDataCommentable (94233464336656)>, '__dict__': <attribute '__dict__' of 'Commentable' objects>, '__weakref__': <attribute '__weakref__' of 'Commentable' objects>, '__doc__': None, '__gsignals__': {}, 'delete_comment': gi.FunctionInfo(delete_comment), 'delete_comment_async': gi.FunctionInfo(delete_comment_async), 'delete_comment_finish': gi.FunctionInfo(delete_comment_finish), 'insert_comment': gi.FunctionInfo(insert_comment), 'insert_comment_async': gi.FunctionInfo(insert_comment_async), 'insert_comment_finish': gi.FunctionInfo(insert_comment_finish), 'query_comments': gi.FunctionInfo(query_comments), 'query_comments_async': gi.FunctionInfo(query_comments_async), 'query_comments_finish': gi.FunctionInfo(query_comments_finish)})"
    __gdoc__ = 'Interface GDataCommentable\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataCommentable (94233464336656)>'
    __info__ = InterfaceInfo(Commentable)


