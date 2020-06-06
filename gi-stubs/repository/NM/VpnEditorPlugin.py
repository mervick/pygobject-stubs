# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


class VpnEditorPlugin(__gobject.GInterface):
    # no doc
    def export(self, path, connection): # real signature unknown; restored from __doc__
        """ export(self, path:str, connection:NM.Connection) -> bool """
        return False

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> NM.VpnEditorPluginCapability """
        pass

    def get_editor(self, connection): # real signature unknown; restored from __doc__
        """ get_editor(self, connection:NM.Connection) -> NM.VpnEditor """
        pass

    def get_plugin_info(self): # real signature unknown; restored from __doc__
        """ get_plugin_info(self) -> NM.VpnPluginInfo """
        pass

    def get_suggested_filename(self, connection): # real signature unknown; restored from __doc__
        """ get_suggested_filename(self, connection:NM.Connection) -> str """
        return ""

    def get_vt(self, vt_size): # real signature unknown; restored from __doc__
        """ get_vt(self, vt_size:int) -> int, vt:NM.VpnEditorPluginVT """
        return 0

    def import_(self, path): # real signature unknown; restored from __doc__
        """ import_(self, path:str) -> NM.Connection """
        pass

    def load(self, plugin_name, check_service): # real signature unknown; restored from __doc__
        """ load(plugin_name:str, check_service:str) -> NM.VpnEditorPlugin """
        pass

    def load_from_file(self, plugin_name, check_service, check_owner, check_file, user_data=None): # real signature unknown; restored from __doc__
        """ load_from_file(plugin_name:str, check_service:str, check_owner:int, check_file:NM.UtilsCheckFilePredicate, user_data=None) -> NM.VpnEditorPlugin """
        pass

    def set_plugin_info(self, plugin_info=None): # real signature unknown; restored from __doc__
        """ set_plugin_info(self, plugin_info:NM.VpnPluginInfo=None) """
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(VpnEditorPlugin), '__module__': 'gi.repository.NM', '__gtype__': <GType NMVpnEditorPlugin (94741104697664)>, '__dict__': <attribute '__dict__' of 'VpnEditorPlugin' objects>, '__weakref__': <attribute '__weakref__' of 'VpnEditorPlugin' objects>, '__doc__': None, '__gsignals__': {}, 'load': gi.FunctionInfo(load), 'load_from_file': gi.FunctionInfo(load_from_file), 'export': gi.FunctionInfo(export), 'get_capabilities': gi.FunctionInfo(get_capabilities), 'get_editor': gi.FunctionInfo(get_editor), 'get_plugin_info': gi.FunctionInfo(get_plugin_info), 'get_suggested_filename': gi.FunctionInfo(get_suggested_filename), 'get_vt': gi.FunctionInfo(get_vt), 'import_': gi.FunctionInfo(import), 'set_plugin_info': gi.FunctionInfo(set_plugin_info)})"
    __gdoc__ = 'Interface NMVpnEditorPlugin\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMVpnEditorPlugin (94741104697664)>'
    __info__ = InterfaceInfo(VpnEditorPlugin)


