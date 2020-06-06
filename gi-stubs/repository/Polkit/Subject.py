# encoding: utf-8
# module gi.repository.Polkit
# from /usr/lib64/girepository-1.0/Polkit-1.0.typelib
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


class Subject(__gobject.GInterface):
    # no doc
    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Polkit.Subject) -> bool """
        return False

    def exists(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ exists(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def exists_finish(self, res): # real signature unknown; restored from __doc__
        """ exists_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def exists_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ exists_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def from_string(self, p_str): # real signature unknown; restored from __doc__
        """ from_string(str:str) -> Polkit.Subject """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Subject), '__module__': 'gi.repository.Polkit', '__gtype__': <GType PolkitSubject (94810843387664)>, '__dict__': <attribute '__dict__' of 'Subject' objects>, '__weakref__': <attribute '__weakref__' of 'Subject' objects>, '__doc__': None, '__gsignals__': {}, 'from_string': gi.FunctionInfo(from_string), 'equal': gi.FunctionInfo(equal), 'exists': gi.FunctionInfo(exists), 'exists_finish': gi.FunctionInfo(exists_finish), 'exists_sync': gi.FunctionInfo(exists_sync), 'hash': gi.FunctionInfo(hash), 'to_string': gi.FunctionInfo(to_string)})"
    __gdoc__ = 'Interface PolkitSubject\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PolkitSubject (94810843387664)>'
    __info__ = InterfaceInfo(Subject)


