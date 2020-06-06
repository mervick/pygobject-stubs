# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
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
import gobject as __gobject


from .Object import Object

class Renderer(Object):
    """
    :Constructors:
    
    ::
    
        Renderer(**properties)
        new() -> Cogl.Renderer
    """
    def add_constraint(self, constraint): # real signature unknown; restored from __doc__
        """ add_constraint(self, constraint:Cogl.RendererConstraint) """
        pass

    def check_onscreen_template(self, onscreen_template): # real signature unknown; restored from __doc__
        """ check_onscreen_template(self, onscreen_template:Cogl.OnscreenTemplate) -> int """
        return 0

    def connect(self): # real signature unknown; restored from __doc__
        """ connect(self) -> int """
        return 0

    def foreach_output(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_output(self, callback:Cogl.OutputCallback, user_data=None) """
        pass

    def get_driver(self): # real signature unknown; restored from __doc__
        """ get_driver(self) -> Cogl.Driver """
        pass

    def get_n_fragment_texture_units(self): # real signature unknown; restored from __doc__
        """ get_n_fragment_texture_units(self) -> int """
        return 0

    def get_winsys_id(self): # real signature unknown; restored from __doc__
        """ get_winsys_id(self) -> Cogl.WinsysID """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Cogl.Renderer """
        pass

    def remove_constraint(self, constraint): # real signature unknown; restored from __doc__
        """ remove_constraint(self, constraint:Cogl.RendererConstraint) """
        pass

    def set_driver(self, driver): # real signature unknown; restored from __doc__
        """ set_driver(self, driver:Cogl.Driver) """
        pass

    def set_winsys_id(self, winsys_id): # real signature unknown; restored from __doc__
        """ set_winsys_id(self, winsys_id:Cogl.WinsysID) """
        pass

    def value_get_object(self, value): # real signature unknown; restored from __doc__
        """ value_get_object(value:GObject.Value) """
        pass

    def value_set_object(self, value, p_object=None): # real signature unknown; restored from __doc__
        """ value_set_object(value:GObject.Value, object=None) """
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Renderer), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglRenderer (93970932266256)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_constraint': gi.FunctionInfo(add_constraint), 'check_onscreen_template': gi.FunctionInfo(check_onscreen_template), 'connect': gi.FunctionInfo(connect), 'foreach_output': gi.FunctionInfo(foreach_output), 'get_driver': gi.FunctionInfo(get_driver), 'get_n_fragment_texture_units': gi.FunctionInfo(get_n_fragment_texture_units), 'get_winsys_id': gi.FunctionInfo(get_winsys_id), 'remove_constraint': gi.FunctionInfo(remove_constraint), 'set_driver': gi.FunctionInfo(set_driver), 'set_winsys_id': gi.FunctionInfo(set_winsys_id)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglRenderer (93970932266256)>'
    __info__ = ObjectInfo(Renderer)


