# encoding: utf-8
# module gi.repository.GtkSource
# from /usr/lib64/girepository-1.0/GtkSource-3.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class CompletionProposal(__gobject.GInterface):
    # no doc
    def changed(self): # real signature unknown; restored from __doc__
        """ changed(self) """
        pass

    def equal(self, other): # real signature unknown; restored from __doc__
        """ equal(self, other:GtkSource.CompletionProposal) -> bool """
        return False

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon or None """
        pass

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str or None """
        return ""

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> str or None """
        return ""

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_markup(self): # real signature unknown; restored from __doc__
        """ get_markup(self) -> str """
        return ""

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str """
        return ""

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(CompletionProposal), '__module__': 'gi.repository.GtkSource', '__gtype__': <GType GtkSourceCompletionProposal (94260244419744)>, '__dict__': <attribute '__dict__' of 'CompletionProposal' objects>, '__weakref__': <attribute '__weakref__' of 'CompletionProposal' objects>, '__doc__': None, '__gsignals__': {}, 'changed': gi.FunctionInfo(changed), 'equal': gi.FunctionInfo(equal), 'get_gicon': gi.FunctionInfo(get_gicon), 'get_icon': gi.FunctionInfo(get_icon), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_info': gi.FunctionInfo(get_info), 'get_label': gi.FunctionInfo(get_label), 'get_markup': gi.FunctionInfo(get_markup), 'get_text': gi.FunctionInfo(get_text), 'hash': gi.FunctionInfo(hash)})"
    __gdoc__ = 'Interface GtkSourceCompletionProposal\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkSourceCompletionProposal (94260244419744)>'
    __info__ = InterfaceInfo(CompletionProposal)


