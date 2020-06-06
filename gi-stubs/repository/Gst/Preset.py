# encoding: utf-8
# module gi.repository.Gst
# from /usr/lib64/girepository-1.0/Gst-1.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Preset(__gobject.GInterface):
    # no doc
    def delete_preset(self, name): # real signature unknown; restored from __doc__
        """ delete_preset(self, name:str) -> bool """
        return False

    def get_app_dir(self): # real signature unknown; restored from __doc__
        """ get_app_dir() -> str or None """
        return ""

    def get_meta(self, name, tag): # real signature unknown; restored from __doc__
        """ get_meta(self, name:str, tag:str) -> bool, value:str """
        return False

    def get_preset_names(self): # real signature unknown; restored from __doc__
        """ get_preset_names(self) -> list """
        return []

    def get_property_names(self): # real signature unknown; restored from __doc__
        """ get_property_names(self) -> list """
        return []

    def is_editable(self): # real signature unknown; restored from __doc__
        """ is_editable(self) -> bool """
        return False

    def load_preset(self, name): # real signature unknown; restored from __doc__
        """ load_preset(self, name:str) -> bool """
        return False

    def rename_preset(self, old_name, new_name): # real signature unknown; restored from __doc__
        """ rename_preset(self, old_name:str, new_name:str) -> bool """
        return False

    def save_preset(self, name): # real signature unknown; restored from __doc__
        """ save_preset(self, name:str) -> bool """
        return False

    def set_app_dir(self, app_dir): # real signature unknown; restored from __doc__
        """ set_app_dir(app_dir:str) -> bool """
        return False

    def set_meta(self, name, tag, value=None): # real signature unknown; restored from __doc__
        """ set_meta(self, name:str, tag:str, value:str=None) -> bool """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Preset), '__module__': 'gi.repository.Gst', '__gtype__': <GType GstPreset (94058977876992)>, '__dict__': <attribute '__dict__' of 'Preset' objects>, '__weakref__': <attribute '__weakref__' of 'Preset' objects>, '__doc__': None, '__gsignals__': {}, 'get_app_dir': gi.FunctionInfo(get_app_dir), 'set_app_dir': gi.FunctionInfo(set_app_dir), 'delete_preset': gi.FunctionInfo(delete_preset), 'get_meta': gi.FunctionInfo(get_meta), 'get_preset_names': gi.FunctionInfo(get_preset_names), 'get_property_names': gi.FunctionInfo(get_property_names), 'is_editable': gi.FunctionInfo(is_editable), 'load_preset': gi.FunctionInfo(load_preset), 'rename_preset': gi.FunctionInfo(rename_preset), 'save_preset': gi.FunctionInfo(save_preset), 'set_meta': gi.FunctionInfo(set_meta)})"
    __gdoc__ = 'Interface GstPreset\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstPreset (94058977876992)>'
    __info__ = InterfaceInfo(Preset)


