# encoding: utf-8
# module gi.repository.Atspi
# from /usr/lib64/girepository-1.0/Atspi-2.0.typelib
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


class Text(__gobject.GInterface):
    # no doc
    def add_selection(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ add_selection(self, start_offset:int, end_offset:int) -> bool """
        return False

    def get_attribute_run(self, offset, include_defaults): # real signature unknown; restored from __doc__
        """ get_attribute_run(self, offset:int, include_defaults:bool) -> dict, start_offset:int, end_offset:int """
        return {}

    def get_bounded_ranges(self, x, y, width, height, type, clipTypeX, clipTypeY): # real signature unknown; restored from __doc__
        """ get_bounded_ranges(self, x:int, y:int, width:int, height:int, type:Atspi.CoordType, clipTypeX:Atspi.TextClipType, clipTypeY:Atspi.TextClipType) -> list """
        return []

    def get_caret_offset(self): # real signature unknown; restored from __doc__
        """ get_caret_offset(self) -> int """
        return 0

    def get_character_at_offset(self, offset): # real signature unknown; restored from __doc__
        """ get_character_at_offset(self, offset:int) -> int """
        return 0

    def get_character_count(self): # real signature unknown; restored from __doc__
        """ get_character_count(self) -> int """
        return 0

    def get_character_extents(self, offset, type): # real signature unknown; restored from __doc__
        """ get_character_extents(self, offset:int, type:Atspi.CoordType) -> Atspi.Rect """
        pass

    def get_default_attributes(self): # real signature unknown; restored from __doc__
        """ get_default_attributes(self) -> dict """
        return {}

    def get_n_selections(self): # real signature unknown; restored from __doc__
        """ get_n_selections(self) -> int """
        return 0

    def get_offset_at_point(self, x, y, type): # real signature unknown; restored from __doc__
        """ get_offset_at_point(self, x:int, y:int, type:Atspi.CoordType) -> int """
        return 0

    def get_range_extents(self, start_offset, end_offset, type): # real signature unknown; restored from __doc__
        """ get_range_extents(self, start_offset:int, end_offset:int, type:Atspi.CoordType) -> Atspi.Rect """
        pass

    def get_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ get_selection(self, selection_num:int) -> Atspi.Range """
        pass

    def get_string_at_offset(self, offset, granularity): # real signature unknown; restored from __doc__
        """ get_string_at_offset(self, offset:int, granularity:Atspi.TextGranularity) -> Atspi.TextRange """
        pass

    def get_text(self, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ get_text(self, start_offset:int, end_offset:int) -> str """
        return ""

    def get_text_after_offset(self, offset, type): # real signature unknown; restored from __doc__
        """ get_text_after_offset(self, offset:int, type:Atspi.TextBoundaryType) -> Atspi.TextRange """
        pass

    def get_text_attributes(self, offset): # real signature unknown; restored from __doc__
        """ get_text_attributes(self, offset:int) -> dict, start_offset:int, end_offset:int """
        return {}

    def get_text_attribute_value(self, offset, attribute_name): # real signature unknown; restored from __doc__
        """ get_text_attribute_value(self, offset:int, attribute_name:str) -> str or None """
        return ""

    def get_text_at_offset(self, offset, type): # real signature unknown; restored from __doc__
        """ get_text_at_offset(self, offset:int, type:Atspi.TextBoundaryType) -> Atspi.TextRange """
        pass

    def get_text_before_offset(self, offset, type): # real signature unknown; restored from __doc__
        """ get_text_before_offset(self, offset:int, type:Atspi.TextBoundaryType) -> Atspi.TextRange """
        pass

    def remove_selection(self, selection_num): # real signature unknown; restored from __doc__
        """ remove_selection(self, selection_num:int) -> bool """
        return False

    def scroll_substring_to(self, start_offset, end_offset, type): # real signature unknown; restored from __doc__
        """ scroll_substring_to(self, start_offset:int, end_offset:int, type:Atspi.ScrollType) -> bool """
        return False

    def scroll_substring_to_point(self, start_offset, end_offset, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_substring_to_point(self, start_offset:int, end_offset:int, coords:Atspi.CoordType, x:int, y:int) -> bool """
        return False

    def set_caret_offset(self, new_offset): # real signature unknown; restored from __doc__
        """ set_caret_offset(self, new_offset:int) -> bool """
        return False

    def set_selection(self, selection_num, start_offset, end_offset): # real signature unknown; restored from __doc__
        """ set_selection(self, selection_num:int, start_offset:int, end_offset:int) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Text), '__module__': 'gi.repository.Atspi', '__gtype__': <GType AtspiText (94141573302816)>, '__dict__': <attribute '__dict__' of 'Text' objects>, '__weakref__': <attribute '__weakref__' of 'Text' objects>, '__doc__': None, '__gsignals__': {}, 'add_selection': gi.FunctionInfo(add_selection), 'get_attribute_run': gi.FunctionInfo(get_attribute_run), 'get_text_attribute_value': gi.FunctionInfo(get_text_attribute_value), 'get_text_attributes': gi.FunctionInfo(get_text_attributes), 'get_bounded_ranges': gi.FunctionInfo(get_bounded_ranges), 'get_caret_offset': gi.FunctionInfo(get_caret_offset), 'get_character_at_offset': gi.FunctionInfo(get_character_at_offset), 'get_character_count': gi.FunctionInfo(get_character_count), 'get_character_extents': gi.FunctionInfo(get_character_extents), 'get_default_attributes': gi.FunctionInfo(get_default_attributes), 'get_n_selections': gi.FunctionInfo(get_n_selections), 'get_offset_at_point': gi.FunctionInfo(get_offset_at_point), 'get_range_extents': gi.FunctionInfo(get_range_extents), 'get_selection': gi.FunctionInfo(get_selection), 'get_string_at_offset': gi.FunctionInfo(get_string_at_offset), 'get_text': gi.FunctionInfo(get_text), 'get_text_after_offset': gi.FunctionInfo(get_text_after_offset), 'get_text_at_offset': gi.FunctionInfo(get_text_at_offset), 'get_text_before_offset': gi.FunctionInfo(get_text_before_offset), 'remove_selection': gi.FunctionInfo(remove_selection), 'scroll_substring_to': gi.FunctionInfo(scroll_substring_to), 'scroll_substring_to_point': gi.FunctionInfo(scroll_substring_to_point), 'set_caret_offset': gi.FunctionInfo(set_caret_offset), 'set_selection': gi.FunctionInfo(set_selection)})"
    __gdoc__ = 'Interface AtspiText\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtspiText (94141573302816)>'
    __info__ = InterfaceInfo(Text)


