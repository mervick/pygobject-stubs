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


class EngineClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        EngineClass()
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

    cancel_hand_writing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    candidate_clicked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_down = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cursor_up = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_in = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_down = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    page_up = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pdummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    process_hand_writing_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    process_key_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property_activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property_hide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property_show = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_content_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_cursor_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_surrounding_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(EngineClass), '__module__': 'gi.repository.IBus', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'EngineClass' objects>, '__weakref__': <attribute '__weakref__' of 'EngineClass' objects>, '__doc__': None, 'parent': <property object at 0x7f59b12ae9f0>, 'process_key_event': <property object at 0x7f59b12aeb30>, 'focus_in': <property object at 0x7f59b12aec20>, 'focus_out': <property object at 0x7f59b12aed10>, 'reset': <property object at 0x7f59b12aee00>, 'enable': <property object at 0x7f59b12aeef0>, 'disable': <property object at 0x7f59b12b0040>, 'set_cursor_location': <property object at 0x7f59b12b0180>, 'set_capabilities': <property object at 0x7f59b12b02c0>, 'page_up': <property object at 0x7f59b12b03b0>, 'page_down': <property object at 0x7f59b12b04a0>, 'cursor_up': <property object at 0x7f59b12b0590>, 'cursor_down': <property object at 0x7f59b12b0680>, 'property_activate': <property object at 0x7f59b12b07c0>, 'property_show': <property object at 0x7f59b12b08b0>, 'property_hide': <property object at 0x7f59b12b09a0>, 'candidate_clicked': <property object at 0x7f59b12b0ae0>, 'set_surrounding_text': <property object at 0x7f59b12b0c20>, 'process_hand_writing_event': <property object at 0x7f59b12b0d60>, 'cancel_hand_writing': <property object at 0x7f59b12b0ea0>, 'set_content_type': <property object at 0x7f59b12b0f90>, 'pdummy': <property object at 0x7f59b12b10e0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(EngineClass)


