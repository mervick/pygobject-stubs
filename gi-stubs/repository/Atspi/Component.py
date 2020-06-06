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


class Component(__gobject.GInterface):
    # no doc
    def contains(self, x, y, ctype): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, ctype:Atspi.CoordType) -> bool """
        return False

    def get_accessible_at_point(self, x, y, ctype): # real signature unknown; restored from __doc__
        """ get_accessible_at_point(self, x:int, y:int, ctype:Atspi.CoordType) -> Atspi.Accessible or None """
        pass

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_extents(self, ctype): # real signature unknown; restored from __doc__
        """ get_extents(self, ctype:Atspi.CoordType) -> Atspi.Rect """
        pass

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atspi.ComponentLayer """
        pass

    def get_mdi_z_order(self): # real signature unknown; restored from __doc__
        """ get_mdi_z_order(self) -> int """
        return 0

    def get_position(self, ctype): # real signature unknown; restored from __doc__
        """ get_position(self, ctype:Atspi.CoordType) -> Atspi.Point """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> Atspi.Point """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
        return False

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atspi.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atspi.CoordType, x:int, y:int) -> bool """
        return False

    def set_extents(self, x, y, width, height, ctype): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, ctype:Atspi.CoordType) -> bool """
        return False

    def set_position(self, x, y, ctype): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, ctype:Atspi.CoordType) -> bool """
        return False

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Component), '__module__': 'gi.repository.Atspi', '__gtype__': <GType AtspiComponent (94141573505904)>, '__dict__': <attribute '__dict__' of 'Component' objects>, '__weakref__': <attribute '__weakref__' of 'Component' objects>, '__doc__': None, '__gsignals__': {}, 'contains': gi.FunctionInfo(contains), 'get_accessible_at_point': gi.FunctionInfo(get_accessible_at_point), 'get_alpha': gi.FunctionInfo(get_alpha), 'get_extents': gi.FunctionInfo(get_extents), 'get_layer': gi.FunctionInfo(get_layer), 'get_mdi_z_order': gi.FunctionInfo(get_mdi_z_order), 'get_position': gi.FunctionInfo(get_position), 'get_size': gi.FunctionInfo(get_size), 'grab_focus': gi.FunctionInfo(grab_focus), 'scroll_to': gi.FunctionInfo(scroll_to), 'scroll_to_point': gi.FunctionInfo(scroll_to_point), 'set_extents': gi.FunctionInfo(set_extents), 'set_position': gi.FunctionInfo(set_position), 'set_size': gi.FunctionInfo(set_size)})"
    __gdoc__ = 'Interface AtspiComponent\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AtspiComponent (94141573505904)>'
    __info__ = InterfaceInfo(Component)


