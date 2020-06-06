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


class Quaternion(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Quaternion()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Cogl.Quaternion """
        pass

    def dot_product(self, b): # real signature unknown; restored from __doc__
        """ dot_product(self, b:Cogl.Quaternion) -> float """
        return 0.0

    def equal(self, v1=None, v2=None): # real signature unknown; restored from __doc__
        """ equal(v1=None, v2=None) -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_rotation_angle(self): # real signature unknown; restored from __doc__
        """ get_rotation_angle(self) -> float """
        return 0.0

    def get_rotation_axis(self): # real signature unknown; restored from __doc__
        """ get_rotation_axis(self) -> vector3:float """
        pass

    def init(self, angle, x, y, z): # real signature unknown; restored from __doc__
        """ init(self, angle:float, x:float, y:float, z:float) """
        pass

    def init_from_angle_vector(self, angle, axis3f): # real signature unknown; restored from __doc__
        """ init_from_angle_vector(self, angle:float, axis3f:float) """
        pass

    def init_from_array(self, array): # real signature unknown; restored from __doc__
        """ init_from_array(self, array:float) """
        pass

    def init_from_euler(self, euler): # real signature unknown; restored from __doc__
        """ init_from_euler(self, euler:Cogl.Euler) """
        pass

    def init_from_matrix(self, matrix): # real signature unknown; restored from __doc__
        """ init_from_matrix(self, matrix:Cogl.Matrix) """
        pass

    def init_from_quaternion(self, src): # real signature unknown; restored from __doc__
        """ init_from_quaternion(self, src:Cogl.Quaternion) """
        pass

    def init_from_x_rotation(self, angle): # real signature unknown; restored from __doc__
        """ init_from_x_rotation(self, angle:float) """
        pass

    def init_from_y_rotation(self, angle): # real signature unknown; restored from __doc__
        """ init_from_y_rotation(self, angle:float) """
        pass

    def init_from_z_rotation(self, angle): # real signature unknown; restored from __doc__
        """ init_from_z_rotation(self, angle:float) """
        pass

    def init_identity(self): # real signature unknown; restored from __doc__
        """ init_identity(self) """
        pass

    def invert(self): # real signature unknown; restored from __doc__
        """ invert(self) """
        pass

    def multiply(self, left, right): # real signature unknown; restored from __doc__
        """ multiply(self, left:Cogl.Quaternion, right:Cogl.Quaternion) """
        pass

    def nlerp(self, a, b, t): # real signature unknown; restored from __doc__
        """ nlerp(self, a:Cogl.Quaternion, b:Cogl.Quaternion, t:float) """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) """
        pass

    def pow(self, exponent): # real signature unknown; restored from __doc__
        """ pow(self, exponent:float) """
        pass

    def slerp(self, a, b, t): # real signature unknown; restored from __doc__
        """ slerp(self, a:Cogl.Quaternion, b:Cogl.Quaternion, t:float) """
        pass

    def squad(self, prev, a, b, next, t): # real signature unknown; restored from __doc__
        """ squad(self, prev:Cogl.Quaternion, a:Cogl.Quaternion, b:Cogl.Quaternion, next:Cogl.Quaternion, t:float) """
        pass

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

    padding0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Quaternion), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglQuaternion (93970932252464)>, '__dict__': <attribute '__dict__' of 'Quaternion' objects>, '__weakref__': <attribute '__weakref__' of 'Quaternion' objects>, '__doc__': None, 'w': <property object at 0x7fba88d80040>, 'x': <property object at 0x7fba88d80130>, 'y': <property object at 0x7fba88d80220>, 'z': <property object at 0x7fba88d80310>, 'padding0': <property object at 0x7fba88d80400>, 'padding1': <property object at 0x7fba88d804f0>, 'padding2': <property object at 0x7fba88d805e0>, 'padding3': <property object at 0x7fba88d806d0>, 'copy': gi.FunctionInfo(copy), 'dot_product': gi.FunctionInfo(dot_product), 'free': gi.FunctionInfo(free), 'get_rotation_angle': gi.FunctionInfo(get_rotation_angle), 'get_rotation_axis': gi.FunctionInfo(get_rotation_axis), 'init': gi.FunctionInfo(init), 'init_from_angle_vector': gi.FunctionInfo(init_from_angle_vector), 'init_from_array': gi.FunctionInfo(init_from_array), 'init_from_euler': gi.FunctionInfo(init_from_euler), 'init_from_matrix': gi.FunctionInfo(init_from_matrix), 'init_from_quaternion': gi.FunctionInfo(init_from_quaternion), 'init_from_x_rotation': gi.FunctionInfo(init_from_x_rotation), 'init_from_y_rotation': gi.FunctionInfo(init_from_y_rotation), 'init_from_z_rotation': gi.FunctionInfo(init_from_z_rotation), 'init_identity': gi.FunctionInfo(init_identity), 'invert': gi.FunctionInfo(invert), 'multiply': gi.FunctionInfo(multiply), 'nlerp': gi.FunctionInfo(nlerp), 'normalize': gi.FunctionInfo(normalize), 'pow': gi.FunctionInfo(pow), 'slerp': gi.FunctionInfo(slerp), 'squad': gi.FunctionInfo(squad), 'equal': gi.FunctionInfo(equal)})"
    __gtype__ = None # (!) real value is '<GType CoglQuaternion (93970932252464)>'
    __info__ = StructInfo(Quaternion)


