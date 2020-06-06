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


class CompletionProvider(__gobject.GInterface):
    # no doc
    def activate_proposal(self, proposal, iter): # real signature unknown; restored from __doc__
        """ activate_proposal(self, proposal:GtkSource.CompletionProposal, iter:Gtk.TextIter) -> bool """
        return False

    def get_activation(self): # real signature unknown; restored from __doc__
        """ get_activation(self) -> GtkSource.CompletionActivation """
        pass

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon or None """
        pass

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str or None """
        return ""

    def get_info_widget(self, proposal): # real signature unknown; restored from __doc__
        """ get_info_widget(self, proposal:GtkSource.CompletionProposal) -> Gtk.Widget or None """
        pass

    def get_interactive_delay(self): # real signature unknown; restored from __doc__
        """ get_interactive_delay(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_start_iter(self, context, proposal): # real signature unknown; restored from __doc__
        """ get_start_iter(self, context:GtkSource.CompletionContext, proposal:GtkSource.CompletionProposal) -> bool, iter:Gtk.TextIter """
        return False

    def match(self, context): # real signature unknown; restored from __doc__
        """ match(self, context:GtkSource.CompletionContext) -> bool """
        return False

    def populate(self, context): # real signature unknown; restored from __doc__
        """ populate(self, context:GtkSource.CompletionContext) """
        pass

    def update_info(self, proposal, info): # real signature unknown; restored from __doc__
        """ update_info(self, proposal:GtkSource.CompletionProposal, info:GtkSource.CompletionInfo) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(CompletionProvider), '__module__': 'gi.repository.GtkSource', '__gtype__': <GType GtkSourceCompletionProvider (94260244479680)>, '__dict__': <attribute '__dict__' of 'CompletionProvider' objects>, '__weakref__': <attribute '__weakref__' of 'CompletionProvider' objects>, '__doc__': None, '__gsignals__': {}, 'activate_proposal': gi.FunctionInfo(activate_proposal), 'get_activation': gi.FunctionInfo(get_activation), 'get_gicon': gi.FunctionInfo(get_gicon), 'get_icon': gi.FunctionInfo(get_icon), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_info_widget': gi.FunctionInfo(get_info_widget), 'get_interactive_delay': gi.FunctionInfo(get_interactive_delay), 'get_name': gi.FunctionInfo(get_name), 'get_priority': gi.FunctionInfo(get_priority), 'get_start_iter': gi.FunctionInfo(get_start_iter), 'match': gi.FunctionInfo(match), 'populate': gi.FunctionInfo(populate), 'update_info': gi.FunctionInfo(update_info)})"
    __gdoc__ = 'Interface GtkSourceCompletionProvider\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkSourceCompletionProvider (94260244479680)>'
    __info__ = InterfaceInfo(CompletionProvider)


