# encoding: utf-8
# module gi.repository.EvinceDocument
# from /usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib
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


class AnnotationMarkup(__gobject.GInterface):
    # no doc
    def can_have_popup(self): # real signature unknown; restored from __doc__
        """ can_have_popup(self) -> bool """
        return False

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_opacity(self): # real signature unknown; restored from __doc__
        """ get_opacity(self) -> float """
        return 0.0

    def get_popup_is_open(self): # real signature unknown; restored from __doc__
        """ get_popup_is_open(self) -> bool """
        return False

    def get_rectangle(self, ev_rect): # real signature unknown; restored from __doc__
        """ get_rectangle(self, ev_rect:EvinceDocument.Rectangle) """
        pass

    def has_popup(self): # real signature unknown; restored from __doc__
        """ has_popup(self) -> bool """
        return False

    def set_has_popup(self, has_popup): # real signature unknown; restored from __doc__
        """ set_has_popup(self, has_popup:bool) -> bool """
        return False

    def set_label(self, label): # real signature unknown; restored from __doc__
        """ set_label(self, label:str) -> bool """
        return False

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:float) -> bool """
        return False

    def set_popup_is_open(self, is_open): # real signature unknown; restored from __doc__
        """ set_popup_is_open(self, is_open:bool) -> bool """
        return False

    def set_rectangle(self, ev_rect): # real signature unknown; restored from __doc__
        """ set_rectangle(self, ev_rect:EvinceDocument.Rectangle) -> bool """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(AnnotationMarkup), '__module__': 'gi.repository.EvinceDocument', '__gtype__': <GType EvAnnotationMarkup (94742333671312)>, '__dict__': <attribute '__dict__' of 'AnnotationMarkup' objects>, '__weakref__': <attribute '__weakref__' of 'AnnotationMarkup' objects>, '__doc__': None, '__gsignals__': {}, 'can_have_popup': gi.FunctionInfo(can_have_popup), 'get_label': gi.FunctionInfo(get_label), 'get_opacity': gi.FunctionInfo(get_opacity), 'get_popup_is_open': gi.FunctionInfo(get_popup_is_open), 'get_rectangle': gi.FunctionInfo(get_rectangle), 'has_popup': gi.FunctionInfo(has_popup), 'set_has_popup': gi.FunctionInfo(set_has_popup), 'set_label': gi.FunctionInfo(set_label), 'set_opacity': gi.FunctionInfo(set_opacity), 'set_popup_is_open': gi.FunctionInfo(set_popup_is_open), 'set_rectangle': gi.FunctionInfo(set_rectangle)})"
    __gdoc__ = 'Interface EvAnnotationMarkup\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EvAnnotationMarkup (94742333671312)>'
    __info__ = InterfaceInfo(AnnotationMarkup)


