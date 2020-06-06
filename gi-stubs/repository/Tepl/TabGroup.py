# encoding: utf-8
# module gi.repository.Tepl
# from /usr/lib64/girepository-1.0/Tepl-4.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gi.repository.GtkSource as __gi_repository_GtkSource
import gobject as __gobject


class TabGroup(__gobject.GInterface):
    # no doc
    def append_tab(self, tab, jump_to): # real signature unknown; restored from __doc__
        """ append_tab(self, tab:Tepl.Tab, jump_to:bool) """
        pass

    def get_active_buffer(self): # real signature unknown; restored from __doc__
        """ get_active_buffer(self) -> Tepl.Buffer or None """
        pass

    def get_active_tab(self): # real signature unknown; restored from __doc__
        """ get_active_tab(self) -> Tepl.Tab or None """
        pass

    def get_active_view(self): # real signature unknown; restored from __doc__
        """ get_active_view(self) -> Tepl.View or None """
        pass

    def get_buffers(self): # real signature unknown; restored from __doc__
        """ get_buffers(self) -> list """
        return []

    def get_tabs(self): # real signature unknown; restored from __doc__
        """ get_tabs(self) -> list """
        return []

    def get_views(self): # real signature unknown; restored from __doc__
        """ get_views(self) -> list """
        return []

    def set_active_tab(self, tab): # real signature unknown; restored from __doc__
        """ set_active_tab(self, tab:Tepl.Tab) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(TabGroup), '__module__': 'gi.repository.Tepl', '__gtype__': <GType TeplTabGroup (93942770047440)>, '__dict__': <attribute '__dict__' of 'TabGroup' objects>, '__weakref__': <attribute '__weakref__' of 'TabGroup' objects>, '__doc__': None, '__gsignals__': {}, 'append_tab': gi.FunctionInfo(append_tab), 'get_active_buffer': gi.FunctionInfo(get_active_buffer), 'get_active_tab': gi.FunctionInfo(get_active_tab), 'get_active_view': gi.FunctionInfo(get_active_view), 'get_buffers': gi.FunctionInfo(get_buffers), 'get_tabs': gi.FunctionInfo(get_tabs), 'get_views': gi.FunctionInfo(get_views), 'set_active_tab': gi.FunctionInfo(set_active_tab)})"
    __gdoc__ = 'Interface TeplTabGroup\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType TeplTabGroup (93942770047440)>'
    __info__ = InterfaceInfo(TabGroup)


