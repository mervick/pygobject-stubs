# encoding: utf-8
# module gi.repository.IBus
# from /usr/lib64/girepository-1.0/IBus-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class PanelServiceClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PanelServiceClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    candidate_clicked_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    commit_text_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_down_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_up_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_in = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide_auxiliary_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide_language_bar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide_preedit_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_down_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_up_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    panel_extension_received = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pdummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    process_key_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    register_properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_content_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_cursor_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_cursor_location_relative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_auxiliary_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_language_bar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_preedit_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_setup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    update_auxiliary_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    update_lookup_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    update_preedit_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    update_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PanelServiceClass), '__module__': 'gi.repository.IBus', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PanelServiceClass' objects>, '__weakref__': <attribute '__weakref__' of 'PanelServiceClass' objects>, '__doc__': None, 'parent': <property object at 0x7f59b12cfa40>, 'focus_in': <property object at 0x7f59b12cfb30>, 'focus_out': <property object at 0x7f59b12cfc20>, 'register_properties': <property object at 0x7f59b12cfd60>, 'set_cursor_location': <property object at 0x7f59b12cfe50>, 'update_auxiliary_text': <property object at 0x7f59b12cff40>, 'update_lookup_table': <property object at 0x7f59b12d2090>, 'update_preedit_text': <property object at 0x7f59b12d2180>, 'update_property': <property object at 0x7f59b12d2220>, 'cursor_down_lookup_table': <property object at 0x7f59b12d2360>, 'cursor_up_lookup_table': <property object at 0x7f59b12d24a0>, 'hide_auxiliary_text': <property object at 0x7f59b12d25e0>, 'hide_language_bar': <property object at 0x7f59b12d26d0>, 'hide_lookup_table': <property object at 0x7f59b12d2810>, 'hide_preedit_text': <property object at 0x7f59b12d2900>, 'page_down_lookup_table': <property object at 0x7f59b12d29f0>, 'page_up_lookup_table': <property object at 0x7f59b12d2b30>, 'reset': <property object at 0x7f59b12d2c20>, 'show_auxiliary_text': <property object at 0x7f59b12d2d60>, 'show_language_bar': <property object at 0x7f59b12d2e50>, 'show_lookup_table': <property object at 0x7f59b12d2f90>, 'show_preedit_text': <property object at 0x7f59b12d30e0>, 'start_setup': <property object at 0x7f59b12d3180>, 'state_changed': <property object at 0x7f59b12d3270>, 'destroy_context': <property object at 0x7f59b12d3360>, 'set_content_type': <property object at 0x7f59b12d34a0>, 'set_cursor_location_relative': <property object at 0x7f59b12d3590>, 'panel_extension_received': <property object at 0x7f59b12d3680>, 'process_key_event': <property object at 0x7f59b12d37c0>, 'commit_text_received': <property object at 0x7f59b12d38b0>, 'candidate_clicked_lookup_table': <property object at 0x7f59b12d39f0>, 'pdummy': <property object at 0x7f59b12d3ae0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PanelServiceClass)


