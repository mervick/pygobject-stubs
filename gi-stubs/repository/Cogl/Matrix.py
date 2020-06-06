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


class Matrix(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Matrix()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Cogl.Matrix """
        pass

    def equal(self, v1=None, v2=None): # real signature unknown; restored from __doc__
        """ equal(v1=None, v2=None) -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def frustum(self, left, right, bottom, top, z_near, z_far): # real signature unknown; restored from __doc__
        """ frustum(self, left:float, right:float, bottom:float, top:float, z_near:float, z_far:float) """
        pass

    def get_array(self): # real signature unknown; restored from __doc__
        """ get_array(self) -> float """
        return 0.0

    def get_inverse(self): # real signature unknown; restored from __doc__
        """ get_inverse(self) -> int, inverse:Cogl.Matrix """
        return 0

    def init_from_array(self, array): # real signature unknown; restored from __doc__
        """ init_from_array(self, array:float) """
        pass

    def init_from_euler(self, euler): # real signature unknown; restored from __doc__
        """ init_from_euler(self, euler:Cogl.Euler) """
        pass

    def init_from_quaternion(self, quaternion): # real signature unknown; restored from __doc__
        """ init_from_quaternion(self, quaternion:Cogl.Quaternion) """
        pass

    def init_identity(self): # real signature unknown; restored from __doc__
        """ init_identity(self) """
        pass

    def init_translation(self, tx, ty, tz): # real signature unknown; restored from __doc__
        """ init_translation(self, tx:float, ty:float, tz:float) """
        pass

    def is_identity(self): # real signature unknown; restored from __doc__
        """ is_identity(self) -> int """
        return 0

    def look_at(self, eye_position_x, eye_position_y, eye_position_z, object_x, object_y, object_z, world_up_x, world_up_y, world_up_z): # real signature unknown; restored from __doc__
        """ look_at(self, eye_position_x:float, eye_position_y:float, eye_position_z:float, object_x:float, object_y:float, object_z:float, world_up_x:float, world_up_y:float, world_up_z:float) """
        pass

    def multiply(self, a, b): # real signature unknown; restored from __doc__
        """ multiply(self, a:Cogl.Matrix, b:Cogl.Matrix) """
        pass

    def ortho(self, left, right, bottom, top, near, far): # real signature unknown; restored from __doc__
        """ ortho(self, left:float, right:float, bottom:float, top:float, near:float, far:float) """
        pass

    def orthographic(self, x_1, y_1, x_2, y_2, near, far): # real signature unknown; restored from __doc__
        """ orthographic(self, x_1:float, y_1:float, x_2:float, y_2:float, near:float, far:float) """
        pass

    def perspective(self, fov_y, aspect, z_near, z_far): # real signature unknown; restored from __doc__
        """ perspective(self, fov_y:float, aspect:float, z_near:float, z_far:float) """
        pass

    def project_points(self, n_components, stride_in, points_in=None, stride_out, points_out=None, n_points): # real signature unknown; restored from __doc__
        """ project_points(self, n_components:int, stride_in:int, points_in=None, stride_out:int, points_out=None, n_points:int) """
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

    def scale(self, sx, sy, sz): # real signature unknown; restored from __doc__
        """ scale(self, sx:float, sy:float, sz:float) """
        pass

    def transform_point(self, x, y, z, w): # real signature unknown; restored from __doc__
        """ transform_point(self, x:float, y:float, z:float, w:float) -> x:float, y:float, z:float, w:float """
        pass

    def transform_points(self, n_components, stride_in, points_in=None, stride_out, points_out=None, n_points): # real signature unknown; restored from __doc__
        """ transform_points(self, n_components:int, stride_in:int, points_in=None, stride_out:int, points_out=None, n_points:int) """
        pass

    def translate(self, x, y, z): # real signature unknown; restored from __doc__
        """ translate(self, x:float, y:float, z:float) """
        pass

    def transpose(self): # real signature unknown; restored from __doc__
        """ transpose(self) """
        pass

    def view_2d_in_frustum(self, left, right, bottom, top, z_near, z_2d, width_2d, height_2d): # real signature unknown; restored from __doc__
        """ view_2d_in_frustum(self, left:float, right:float, bottom:float, top:float, z_near:float, z_2d:float, width_2d:float, height_2d:float) """
        pass

    def view_2d_in_perspective(self, fov_y, aspect, z_near, z_2d, width_2d, height_2d): # real signature unknown; restored from __doc__
        """ view_2d_in_perspective(self, fov_y:float, aspect:float, z_near:float, z_2d:float, width_2d:float, height_2d:float) """
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

    private_member_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_inv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member__padding3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ww = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    yz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    zw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    zx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    zy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    zz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Matrix), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglMatrix (93970932179472)>, '__dict__': <attribute '__dict__' of 'Matrix' objects>, '__weakref__': <attribute '__weakref__' of 'Matrix' objects>, '__doc__': None, 'xx': <property object at 0x7fba89037f40>, 'yx': <property object at 0x7fba89039090>, 'zx': <property object at 0x7fba89039130>, 'wx': <property object at 0x7fba89039220>, 'xy': <property object at 0x7fba89039310>, 'yy': <property object at 0x7fba89039400>, 'zy': <property object at 0x7fba890394f0>, 'wy': <property object at 0x7fba890395e0>, 'xz': <property object at 0x7fba890396d0>, 'yz': <property object at 0x7fba890397c0>, 'zz': <property object at 0x7fba890398b0>, 'wz': <property object at 0x7fba890399a0>, 'xw': <property object at 0x7fba89039a90>, 'yw': <property object at 0x7fba89039b80>, 'zw': <property object at 0x7fba89039c70>, 'ww': <property object at 0x7fba89039d60>, 'private_member_inv': <property object at 0x7fba89039ea0>, 'private_member_type': <property object at 0x7fba8903a040>, 'private_member_flags': <property object at 0x7fba8903a180>, 'private_member__padding3': <property object at 0x7fba8903a2c0>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'frustum': gi.FunctionInfo(frustum), 'get_array': gi.FunctionInfo(get_array), 'get_inverse': gi.FunctionInfo(get_inverse), 'init_from_array': gi.FunctionInfo(init_from_array), 'init_from_euler': gi.FunctionInfo(init_from_euler), 'init_from_quaternion': gi.FunctionInfo(init_from_quaternion), 'init_identity': gi.FunctionInfo(init_identity), 'init_translation': gi.FunctionInfo(init_translation), 'is_identity': gi.FunctionInfo(is_identity), 'look_at': gi.FunctionInfo(look_at), 'multiply': gi.FunctionInfo(multiply), 'ortho': gi.FunctionInfo(ortho), 'orthographic': gi.FunctionInfo(orthographic), 'perspective': gi.FunctionInfo(perspective), 'project_points': gi.FunctionInfo(project_points), 'rotate': gi.FunctionInfo(rotate), 'rotate_euler': gi.FunctionInfo(rotate_euler), 'rotate_quaternion': gi.FunctionInfo(rotate_quaternion), 'scale': gi.FunctionInfo(scale), 'transform_point': gi.FunctionInfo(transform_point), 'transform_points': gi.FunctionInfo(transform_points), 'translate': gi.FunctionInfo(translate), 'transpose': gi.FunctionInfo(transpose), 'view_2d_in_frustum': gi.FunctionInfo(view_2d_in_frustum), 'view_2d_in_perspective': gi.FunctionInfo(view_2d_in_perspective), 'equal': gi.FunctionInfo(equal)})"
    __gtype__ = None # (!) real value is '<GType CoglMatrix (93970932179472)>'
    __info__ = StructInfo(Matrix)


