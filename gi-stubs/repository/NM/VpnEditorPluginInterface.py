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


class VpnEditorPluginInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VpnEditorPluginInterface()
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

    export_to_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_capabilities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_editor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_suggested_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_vt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    import_from_file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    notify_plugin_info_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VpnEditorPluginInterface), '__module__': 'gi.repository.NM', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VpnEditorPluginInterface' objects>, '__weakref__': <attribute '__weakref__' of 'VpnEditorPluginInterface' objects>, '__doc__': None, 'g_iface': <property object at 0x7fb9b84a76d0>, 'get_editor': <property object at 0x7fb9b84a77c0>, 'get_capabilities': <property object at 0x7fb9b84a7900>, 'import_from_file': <property object at 0x7fb9b84a79f0>, 'export_to_file': <property object at 0x7fb9b84a7ae0>, 'get_suggested_filename': <property object at 0x7fb9b84a7c20>, 'notify_plugin_info_set': <property object at 0x7fb9b84a7d10>, 'get_vt': <property object at 0x7fb9b84a7e00>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VpnEditorPluginInterface)


