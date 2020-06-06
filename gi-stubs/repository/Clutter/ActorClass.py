# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class ActorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ActorClass()
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

    allocate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    apply_transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button_press_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button_release_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    captured_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    destroy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enter_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_accessible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_paint_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_overlaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hide_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_focus_in = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_focus_out = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_press_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_release_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    leave_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    motion_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    paint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    paint_node = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue_redraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue_relayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    realize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touch_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unrealize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _padding_dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ActorClass), '__module__': 'gi.repository.Clutter', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ActorClass' objects>, '__weakref__': <attribute '__weakref__' of 'ActorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f5413e13310>, 'show': <property object at 0x7f5413e13400>, 'show_all': <property object at 0x7f5413e134f0>, 'hide': <property object at 0x7f5413e135e0>, 'hide_all': <property object at 0x7f5413e136d0>, 'realize': <property object at 0x7f5413e137c0>, 'unrealize': <property object at 0x7f5413e138b0>, 'map': <property object at 0x7f5413e139a0>, 'unmap': <property object at 0x7f5413e13a90>, 'paint': <property object at 0x7f5413e13b80>, 'parent_set': <property object at 0x7f5413e13c70>, 'destroy': <property object at 0x7f5413e13d60>, 'pick': <property object at 0x7f5413e13e50>, 'queue_redraw': <property object at 0x7f5413e13f40>, 'get_preferred_width': <property object at 0x7f5413d950e0>, 'get_preferred_height': <property object at 0x7f5413d951d0>, 'allocate': <property object at 0x7f5413d95270>, 'apply_transform': <property object at 0x7f5413d95360>, 'event': <property object at 0x7f5413d95450>, 'button_press_event': <property object at 0x7f5413d95590>, 'button_release_event': <property object at 0x7f5413d956d0>, 'scroll_event': <property object at 0x7f5413d957c0>, 'key_press_event': <property object at 0x7f5413d958b0>, 'key_release_event': <property object at 0x7f5413d959f0>, 'motion_event': <property object at 0x7f5413d95ae0>, 'enter_event': <property object at 0x7f5413d95bd0>, 'leave_event': <property object at 0x7f5413d95cc0>, 'captured_event': <property object at 0x7f5413d95db0>, 'key_focus_in': <property object at 0x7f5413d95ea0>, 'key_focus_out': <property object at 0x7f5413d95f90>, 'queue_relayout': <property object at 0x7f5413d970e0>, 'get_accessible': <property object at 0x7f5413d971d0>, 'get_paint_volume': <property object at 0x7f5413d97310>, 'has_overlaps': <property object at 0x7f5413d973b0>, 'paint_node': <property object at 0x7f5413d974a0>, 'touch_event': <property object at 0x7f5413d97590>, '_padding_dummy': <property object at 0x7f5413d97680>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ActorClass)


