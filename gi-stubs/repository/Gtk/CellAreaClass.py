# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class CellAreaClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CellAreaClass()
    """
    def find_cell_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_cell_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def install_cell_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_cell_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def list_cell_properties(self): # real signature unknown; restored from __doc__
        """ list_cell_properties(self) -> list, n_properties:int """
        return []

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

    activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    apply_attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    create_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    foreach = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    foreach_alloc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_cell_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height_for_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width_for_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_request_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_activatable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_cell_property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CellAreaClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CellAreaClass' objects>, '__weakref__': <attribute '__weakref__' of 'CellAreaClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fe8310b95e0>, 'add': <property object at 0x7fe8310b96d0>, 'remove': <property object at 0x7fe8310b97c0>, 'foreach': <property object at 0x7fe8310b98b0>, 'foreach_alloc': <property object at 0x7fe8310b99a0>, 'event': <property object at 0x7fe8310b9a90>, 'render': <property object at 0x7fe8310b9b80>, 'apply_attributes': <property object at 0x7fe8310b9cc0>, 'create_context': <property object at 0x7fe8310b9d60>, 'copy_context': <property object at 0x7fe8310b9e50>, 'get_request_mode': <property object at 0x7fe8310b9f90>, 'get_preferred_width': <property object at 0x7fe8310ba0e0>, 'get_preferred_height_for_width': <property object at 0x7fe8310ba1d0>, 'get_preferred_height': <property object at 0x7fe8310ba2c0>, 'get_preferred_width_for_height': <property object at 0x7fe8310ba3b0>, 'set_cell_property': <property object at 0x7fe8310ba4a0>, 'get_cell_property': <property object at 0x7fe8310ba5e0>, 'focus': <property object at 0x7fe8310ba6d0>, 'is_activatable': <property object at 0x7fe8310ba7c0>, 'activate': <property object at 0x7fe8310ba8b0>, '_gtk_reserved1': <property object at 0x7fe8310ba9a0>, '_gtk_reserved2': <property object at 0x7fe8310baa90>, '_gtk_reserved3': <property object at 0x7fe8310bab80>, '_gtk_reserved4': <property object at 0x7fe8310bac70>, '_gtk_reserved5': <property object at 0x7fe8310bad60>, '_gtk_reserved6': <property object at 0x7fe8310bae50>, '_gtk_reserved7': <property object at 0x7fe8310baf40>, '_gtk_reserved8': <property object at 0x7fe8310bb090>, 'find_cell_property': gi.FunctionInfo(find_cell_property), 'install_cell_property': gi.FunctionInfo(install_cell_property), 'list_cell_properties': gi.FunctionInfo(list_cell_properties)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CellAreaClass)


