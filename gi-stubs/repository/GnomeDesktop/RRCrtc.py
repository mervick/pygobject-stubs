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


class RRCrtc(__gi.Boxed):
    # no doc
    def can_drive_output(self, output): # real signature unknown; restored from __doc__
        """ can_drive_output(self, output:GnomeDesktop.RROutput) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_mode(self): # real signature unknown; restored from __doc__
        """ get_current_mode(self) -> GnomeDesktop.RRMode """
        pass

    def get_current_rotation(self): # real signature unknown; restored from __doc__
        """ get_current_rotation(self) -> GnomeDesktop.RRRotation """
        pass

    def get_gamma(self, size): # real signature unknown; restored from __doc__
        """ get_gamma(self, size:int) -> bool, red:int, green:int, blue:int """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> x:int, y:int """
        pass

    def get_rotations(self): # real signature unknown; restored from __doc__
        """ get_rotations(self) -> GnomeDesktop.RRRotation """
        pass

    def set_gamma(self, size, red, green, blue): # real signature unknown; restored from __doc__
        """ set_gamma(self, size:int, red:int, green:int, blue:int) -> bool """
        return False

    def supports_rotation(self, rotation): # real signature unknown; restored from __doc__
        """ supports_rotation(self, rotation:GnomeDesktop.RRRotation) -> bool """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RRCrtc), '__module__': 'gi.repository.GnomeDesktop', '__gtype__': <GType GnomeRRCrtc (93939703383296)>, '__dict__': <attribute '__dict__' of 'RRCrtc' objects>, '__weakref__': <attribute '__weakref__' of 'RRCrtc' objects>, '__doc__': None, 'can_drive_output': gi.FunctionInfo(can_drive_output), 'get_current_mode': gi.FunctionInfo(get_current_mode), 'get_current_rotation': gi.FunctionInfo(get_current_rotation), 'get_gamma': gi.FunctionInfo(get_gamma), 'get_id': gi.FunctionInfo(get_id), 'get_position': gi.FunctionInfo(get_position), 'get_rotations': gi.FunctionInfo(get_rotations), 'set_gamma': gi.FunctionInfo(set_gamma), 'supports_rotation': gi.FunctionInfo(supports_rotation)})"
    __gtype__ = None # (!) real value is '<GType GnomeRRCrtc (93939703383296)>'
    __info__ = StructInfo(RRCrtc)


