# encoding: utf-8
# module gi.repository.Dazzle
# from /usr/lib64/girepository-1.0/Dazzle-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class Preferences(__gobject.GInterface):
    # no doc
    def add_custom(self, page_name, group_name, widget, keywords=None, priority): # real signature unknown; restored from __doc__
        """ add_custom(self, page_name:str, group_name:str, widget:Gtk.Widget, keywords:str=None, priority:int) -> int """
        return 0

    def add_file_chooser(self, page_name, group_name, schema_id, key, path, title, subtitle, action, keywords, priority): # real signature unknown; restored from __doc__
        """ add_file_chooser(self, page_name:str, group_name:str, schema_id:str, key:str, path:str, title:str, subtitle:str, action:Gtk.FileChooserAction, keywords:str, priority:int) -> int """
        return 0

    def add_font_button(self, page_name, group_name, schema_id, key, title, keywords, priority): # real signature unknown; restored from __doc__
        """ add_font_button(self, page_name:str, group_name:str, schema_id:str, key:str, title:str, keywords:str, priority:int) -> int """
        return 0

    def add_group(self, page_name, group_name, title, priority): # real signature unknown; restored from __doc__
        """ add_group(self, page_name:str, group_name:str, title:str, priority:int) """
        pass

    def add_list_group(self, page_name, group_name, title, mode, priority): # real signature unknown; restored from __doc__
        """ add_list_group(self, page_name:str, group_name:str, title:str, mode:Gtk.SelectionMode, priority:int) """
        pass

    def add_page(self, page_name, title, priority): # real signature unknown; restored from __doc__
        """ add_page(self, page_name:str, title:str, priority:int) """
        pass

    def add_radio(self, page_name, group_name, schema_id, key, path=None, variant_string=None, title=None, subtitle=None, keywords=None, priority): # real signature unknown; restored from __doc__
        """ add_radio(self, page_name:str, group_name:str, schema_id:str, key:str, path:str=None, variant_string:str=None, title:str=None, subtitle:str=None, keywords:str=None, priority:int) -> int """
        return 0

    def add_spin_button(self, page_name, group_name, schema_id, key, path, title, subtitle, keywords, priority): # real signature unknown; restored from __doc__
        """ add_spin_button(self, page_name:str, group_name:str, schema_id:str, key:str, path:str, title:str, subtitle:str, keywords:str, priority:int) -> int """
        return 0

    def add_switch(self, page_name, group_name, schema_id, key, path=None, variant_string=None, title=None, subtitle=None, keywords=None, priority): # real signature unknown; restored from __doc__
        """ add_switch(self, page_name:str, group_name:str, schema_id:str, key:str, path:str=None, variant_string:str=None, title:str=None, subtitle:str=None, keywords:str=None, priority:int) -> int """
        return 0

    def get_widget(self, widget_id): # real signature unknown; restored from __doc__
        """ get_widget(self, widget_id:int) -> Gtk.Widget or None """
        pass

    def remove_id(self, widget_id): # real signature unknown; restored from __doc__
        """ remove_id(self, widget_id:int) -> bool """
        return False

    def set_page(self, page_name, map): # real signature unknown; restored from __doc__
        """ set_page(self, page_name:str, map:dict) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Preferences), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType DzlPreferences (93962411574320)>, '__dict__': <attribute '__dict__' of 'Preferences' objects>, '__weakref__': <attribute '__weakref__' of 'Preferences' objects>, '__doc__': None, '__gsignals__': {}, 'add_custom': gi.FunctionInfo(add_custom), 'add_file_chooser': gi.FunctionInfo(add_file_chooser), 'add_font_button': gi.FunctionInfo(add_font_button), 'add_group': gi.FunctionInfo(add_group), 'add_list_group': gi.FunctionInfo(add_list_group), 'add_page': gi.FunctionInfo(add_page), 'add_radio': gi.FunctionInfo(add_radio), 'add_spin_button': gi.FunctionInfo(add_spin_button), 'add_switch': gi.FunctionInfo(add_switch), 'get_widget': gi.FunctionInfo(get_widget), 'remove_id': gi.FunctionInfo(remove_id), 'set_page': gi.FunctionInfo(set_page)})"
    __gdoc__ = 'Interface DzlPreferences\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DzlPreferences (93962411574320)>'
    __info__ = InterfaceInfo(Preferences)


