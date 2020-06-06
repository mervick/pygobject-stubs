# encoding: utf-8
# module gi.repository.GnomeDesktop
# from /usr/lib64/girepository-1.0/GnomeDesktop-3.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class RROutput(__gi.Boxed):
    # no doc
    def can_clone(self, clone): # real signature unknown; restored from __doc__
        """ can_clone(self, clone:GnomeDesktop.RROutput) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_backlight(self): # real signature unknown; restored from __doc__
        """ get_backlight(self) -> int """
        return 0

    def get_crtc(self): # real signature unknown; restored from __doc__
        """ get_crtc(self) -> GnomeDesktop.RRCrtc """
        pass

    def get_current_mode(self): # real signature unknown; restored from __doc__
        """ get_current_mode(self) -> GnomeDesktop.RRMode """
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_edid_data(self, size): # real signature unknown; restored from __doc__
        """ get_edid_data(self, size:int) -> int """
        return 0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_ids_from_edid(self): # real signature unknown; restored from __doc__
        """ get_ids_from_edid(self) -> vendor:str, product:str, serial:str """
        pass

    def get_is_primary(self): # real signature unknown; restored from __doc__
        """ get_is_primary(self) -> bool """
        return False

    def get_is_underscanning(self): # real signature unknown; restored from __doc__
        """ get_is_underscanning(self) -> bool """
        return False

    def get_min_backlight_step(self): # real signature unknown; restored from __doc__
        """ get_min_backlight_step(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_physical_size(self): # real signature unknown; restored from __doc__
        """ get_physical_size(self) -> width_mm:int, height_mm:int """
        pass

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> x:int, y:int """
        pass

    def get_possible_crtcs(self): # real signature unknown; restored from __doc__
        """ get_possible_crtcs(self) -> list """
        return []

    def get_preferred_mode(self): # real signature unknown; restored from __doc__
        """ get_preferred_mode(self) -> GnomeDesktop.RRMode """
        pass

    def is_builtin_display(self): # real signature unknown; restored from __doc__
        """ is_builtin_display(self) -> bool """
        return False

    def list_modes(self): # real signature unknown; restored from __doc__
        """ list_modes(self) -> list """
        return []

    def set_backlight(self, value): # real signature unknown; restored from __doc__
        """ set_backlight(self, value:int) -> bool """
        return False

    def supports_mode(self, mode): # real signature unknown; restored from __doc__
        """ supports_mode(self, mode:GnomeDesktop.RRMode) -> bool """
        return False

    def supports_underscanning(self): # real signature unknown; restored from __doc__
        """ supports_underscanning(self) -> bool """
        return False

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RROutput), '__module__': 'gi.repository.GnomeDesktop', '__gtype__': <GType GnomeRROutput (93939703628384)>, '__dict__': <attribute '__dict__' of 'RROutput' objects>, '__weakref__': <attribute '__weakref__' of 'RROutput' objects>, '__doc__': None, 'can_clone': gi.FunctionInfo(can_clone), 'get_backlight': gi.FunctionInfo(get_backlight), 'get_crtc': gi.FunctionInfo(get_crtc), 'get_current_mode': gi.FunctionInfo(get_current_mode), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_edid_data': gi.FunctionInfo(get_edid_data), 'get_id': gi.FunctionInfo(get_id), 'get_ids_from_edid': gi.FunctionInfo(get_ids_from_edid), 'get_is_primary': gi.FunctionInfo(get_is_primary), 'get_is_underscanning': gi.FunctionInfo(get_is_underscanning), 'get_min_backlight_step': gi.FunctionInfo(get_min_backlight_step), 'get_name': gi.FunctionInfo(get_name), 'get_physical_size': gi.FunctionInfo(get_physical_size), 'get_position': gi.FunctionInfo(get_position), 'get_possible_crtcs': gi.FunctionInfo(get_possible_crtcs), 'get_preferred_mode': gi.FunctionInfo(get_preferred_mode), 'is_builtin_display': gi.FunctionInfo(is_builtin_display), 'list_modes': gi.FunctionInfo(list_modes), 'set_backlight': gi.FunctionInfo(set_backlight), 'supports_mode': gi.FunctionInfo(supports_mode), 'supports_underscanning': gi.FunctionInfo(supports_underscanning)})"
    __gtype__ = None # (!) real value is '<GType GnomeRROutput (93939703628384)>'
    __info__ = StructInfo(RROutput)


