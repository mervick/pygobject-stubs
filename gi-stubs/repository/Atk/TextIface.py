# encoding: utf-8
# module gi.repository.Atk
# from /usr/lib64/girepository-1.0/Atk-1.0.typelib
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
import gobject as __gobject


class TextIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TextIface()
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

    add_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_bounded_ranges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_caret_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_character_at_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_character_extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_default_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_selections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_offset_at_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_range_extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_run_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_string_at_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text_after_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text_at_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_text_before_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_substring_to = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll_substring_to_point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_caret_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_attributes_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_caret_moved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_selection_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextIface), '__module__': 'gi.repository.Atk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TextIface' objects>, '__weakref__': <attribute '__weakref__' of 'TextIface' objects>, '__doc__': None, 'parent': <property object at 0x7f0cd81c0590>, 'get_text': <property object at 0x7f0cd81c0680>, 'get_text_after_offset': <property object at 0x7f0cd81c07c0>, 'get_text_at_offset': <property object at 0x7f0cd81c08b0>, 'get_character_at_offset': <property object at 0x7f0cd81c09a0>, 'get_text_before_offset': <property object at 0x7f0cd81c0a90>, 'get_caret_offset': <property object at 0x7f0cd81c0b80>, 'get_run_attributes': <property object at 0x7f0cd81c0c70>, 'get_default_attributes': <property object at 0x7f0cd81c0d60>, 'get_character_extents': <property object at 0x7f0cd81c0e50>, 'get_character_count': <property object at 0x7f0cd81c0f40>, 'get_offset_at_point': <property object at 0x7f0cd81c4090>, 'get_n_selections': <property object at 0x7f0cd81c4180>, 'get_selection': <property object at 0x7f0cd81c4220>, 'add_selection': <property object at 0x7f0cd81c4310>, 'remove_selection': <property object at 0x7f0cd81c4450>, 'set_selection': <property object at 0x7f0cd81c44f0>, 'set_caret_offset': <property object at 0x7f0cd81c4630>, 'text_changed': <property object at 0x7f0cd81c46d0>, 'text_caret_moved': <property object at 0x7f0cd81c4810>, 'text_selection_changed': <property object at 0x7f0cd81c4950>, 'text_attributes_changed': <property object at 0x7f0cd81c4a90>, 'get_range_extents': <property object at 0x7f0cd81c4bd0>, 'get_bounded_ranges': <property object at 0x7f0cd81c4cc0>, 'get_string_at_offset': <property object at 0x7f0cd81c4db0>, 'scroll_substring_to': <property object at 0x7f0cd81c4ea0>, 'scroll_substring_to_point': <property object at 0x7f0cd81c4f90>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TextIface)


