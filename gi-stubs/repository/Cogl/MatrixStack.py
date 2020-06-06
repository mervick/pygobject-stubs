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

class MatrixStack(Object):
    """
    :Constructors:
    
    ::
    
        MatrixStack(**properties)
        new(ctx:Cogl.Context) -> Cogl.MatrixStack
    """
    def frustum(self, left, right, bottom, top, z_near, z_far): # real signature unknown; restored from __doc__
        """ frustum(self, left:float, right:float, bottom:float, top:float, z_near:float, z_far:float) """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get(self) -> Cogl.Matrix, matrix:Cogl.Matrix """
        pass

    def get_entry(self): # real signature unknown; restored from __doc__
        """ get_entry(self) -> Cogl.MatrixEntry """
        pass

    def get_inverse(self): # real signature unknown; restored from __doc__
        """ get_inverse(self) -> int, inverse:Cogl.Matrix """
        return 0

    def load_identity(self): # real signature unknown; restored from __doc__
        """ load_identity(self) """
        pass

    def multiply(self, matrix): # real signature unknown; restored from __doc__
        """ multiply(self, matrix:Cogl.Matrix) """
        pass

    def new(self, ctx): # real signature unknown; restored from __doc__
        """ new(ctx:Cogl.Context) -> Cogl.MatrixStack """
        pass

    def orthographic(self, x_1, y_1, x_2, y_2, near, far): # real signature unknown; restored from __doc__
        """ orthographic(self, x_1:float, y_1:float, x_2:float, y_2:float, near:float, far:float) """
        pass

    def perspective(self, fov_y, aspect, z_near, z_far): # real signature unknown; restored from __doc__
        """ perspective(self, fov_y:float, aspect:float, z_near:float, z_far:float) """
        pass

    def pop(self): # real signature unknown; restored from __doc__
        """ pop(self) """
        pass

    def push(self): # real signature unknown; restored from __doc__
        """ push(self) """
        pass

    def rotate(self, angle, x, y, z): # real signature unknown; restored from __doc__
        """ rotate(self, angle:float, x:float, y:float, z:float) """
        pass

    def rotate_euler(self, euler): # real signature unknown; restored from __doc__
        """ rotate_euler(self, euler:Cogl.Euler) """
        pass

    def rotate_quaternion(self, quaternion): # real signature unknown; restored from __doc__
        """ rotate_quaternion(self, quaternion:Cogl.Quaternion) """
        pass

    def scale(self, x, y, z): # real signature unknown; restored from __doc__
        """ scale(self, x:float, y:float, z:float) """
        pass

    def set(self, matrix): # real signature unknown; restored from __doc__
        """ set(self, matrix:Cogl.Matrix) """
        pass

    def translate(self, x, y, z): # real signature unknown; restored from __doc__
        """ translate(self, x:float, y:float, z:float) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MatrixStack), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglMatrixStack (93970932181184)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'frustum': gi.FunctionInfo(frustum), 'get': gi.FunctionInfo(get), 'get_entry': gi.FunctionInfo(get_entry), 'get_inverse': gi.FunctionInfo(get_inverse), 'load_identity': gi.FunctionInfo(load_identity), 'multiply': gi.FunctionInfo(multiply), 'orthographic': gi.FunctionInfo(orthographic), 'perspective': gi.FunctionInfo(perspective), 'pop': gi.FunctionInfo(pop), 'push': gi.FunctionInfo(push), 'rotate': gi.FunctionInfo(rotate), 'rotate_euler': gi.FunctionInfo(rotate_euler), 'rotate_quaternion': gi.FunctionInfo(rotate_quaternion), 'scale': gi.FunctionInfo(scale), 'set': gi.FunctionInfo(set), 'translate': gi.FunctionInfo(translate)})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CoglMatrixStack (93970932181184)>'
    __info__ = ObjectInfo(MatrixStack)


