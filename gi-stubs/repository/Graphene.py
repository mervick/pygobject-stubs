# encoding: utf-8
# module gi.repository.Graphene
# from /usr/lib64/girepository-1.0/Graphene-1.0.typelib
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


# Variables with simple values

false = 0

HAS_GCC = 1
HAS_SCALAR = 1
HAS_SSE = 1

PI = 3.141593
PI_2 = 1.570796

SIMD_S = 'sse'

true = 1

VEC2_LEN = 2

VEC3_LEN = 3

VEC4_LEN = 4

_namespace = 'Graphene'

_version = '1.0'

__weakref__ = None

# functions

def box_empty(): # real signature unknown; restored from __doc__
    """ box_empty() -> Graphene.Box """
    pass

def box_infinite(): # real signature unknown; restored from __doc__
    """ box_infinite() -> Graphene.Box """
    pass

def box_minus_one(): # real signature unknown; restored from __doc__
    """ box_minus_one() -> Graphene.Box """
    pass

def box_one(): # real signature unknown; restored from __doc__
    """ box_one() -> Graphene.Box """
    pass

def box_one_minus_one(): # real signature unknown; restored from __doc__
    """ box_one_minus_one() -> Graphene.Box """
    pass

def box_zero(): # real signature unknown; restored from __doc__
    """ box_zero() -> Graphene.Box """
    pass

def point3d_zero(): # real signature unknown; restored from __doc__
    """ point3d_zero() -> Graphene.Point3D """
    pass

def point_zero(): # real signature unknown; restored from __doc__
    """ point_zero() -> Graphene.Point """
    pass

def rect_alloc(): # real signature unknown; restored from __doc__
    """ rect_alloc() -> Graphene.Rect """
    pass

def rect_zero(): # real signature unknown; restored from __doc__
    """ rect_zero() -> Graphene.Rect """
    pass

def size_zero(): # real signature unknown; restored from __doc__
    """ size_zero() -> Graphene.Size """
    pass

def vec2_one(): # real signature unknown; restored from __doc__
    """ vec2_one() -> Graphene.Vec2 """
    pass

def vec2_x_axis(): # real signature unknown; restored from __doc__
    """ vec2_x_axis() -> Graphene.Vec2 """
    pass

def vec2_y_axis(): # real signature unknown; restored from __doc__
    """ vec2_y_axis() -> Graphene.Vec2 """
    pass

def vec2_zero(): # real signature unknown; restored from __doc__
    """ vec2_zero() -> Graphene.Vec2 """
    pass

def vec3_one(): # real signature unknown; restored from __doc__
    """ vec3_one() -> Graphene.Vec3 """
    pass

def vec3_x_axis(): # real signature unknown; restored from __doc__
    """ vec3_x_axis() -> Graphene.Vec3 """
    pass

def vec3_y_axis(): # real signature unknown; restored from __doc__
    """ vec3_y_axis() -> Graphene.Vec3 """
    pass

def vec3_zero(): # real signature unknown; restored from __doc__
    """ vec3_zero() -> Graphene.Vec3 """
    pass

def vec3_z_axis(): # real signature unknown; restored from __doc__
    """ vec3_z_axis() -> Graphene.Vec3 """
    pass

def vec4_one(): # real signature unknown; restored from __doc__
    """ vec4_one() -> Graphene.Vec4 """
    pass

def vec4_w_axis(): # real signature unknown; restored from __doc__
    """ vec4_w_axis() -> Graphene.Vec4 """
    pass

def vec4_x_axis(): # real signature unknown; restored from __doc__
    """ vec4_x_axis() -> Graphene.Vec4 """
    pass

def vec4_y_axis(): # real signature unknown; restored from __doc__
    """ vec4_y_axis() -> Graphene.Vec4 """
    pass

def vec4_zero(): # real signature unknown; restored from __doc__
    """ vec4_zero() -> Graphene.Vec4 """
    pass

def vec4_z_axis(): # real signature unknown; restored from __doc__
    """ vec4_z_axis() -> Graphene.Vec4 """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class Box(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Box()
        alloc() -> Graphene.Box
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Box """
        pass

    def contains_box(self, b): # real signature unknown; restored from __doc__
        """ contains_box(self, b:Graphene.Box) -> bool """
        return False

    def contains_point(self, point): # real signature unknown; restored from __doc__
        """ contains_point(self, point:Graphene.Point3D) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """ empty() -> Graphene.Box """
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Box) -> bool """
        return False

    def expand(self, point): # real signature unknown; restored from __doc__
        """ expand(self, point:Graphene.Point3D) -> res:Graphene.Box """
        pass

    def expand_scalar(self, scalar): # real signature unknown; restored from __doc__
        """ expand_scalar(self, scalar:float) -> res:Graphene.Box """
        pass

    def expand_vec3(self, vec): # real signature unknown; restored from __doc__
        """ expand_vec3(self, vec:Graphene.Vec3) -> res:Graphene.Box """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_bounding_sphere(self): # real signature unknown; restored from __doc__
        """ get_bounding_sphere(self) -> sphere:Graphene.Sphere """
        pass

    def get_center(self): # real signature unknown; restored from __doc__
        """ get_center(self) -> center:Graphene.Point3D """
        pass

    def get_depth(self): # real signature unknown; restored from __doc__
        """ get_depth(self) -> float """
        return 0.0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> float """
        return 0.0

    def get_max(self): # real signature unknown; restored from __doc__
        """ get_max(self) -> max:Graphene.Point3D """
        pass

    def get_min(self): # real signature unknown; restored from __doc__
        """ get_min(self) -> min:Graphene.Point3D """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> size:Graphene.Vec3 """
        pass

    def get_vertices(self): # real signature unknown; restored from __doc__
        """ get_vertices(self) -> vertices:list """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> float """
        return 0.0

    def infinite(self): # real signature unknown; restored from __doc__
        """ infinite() -> Graphene.Box """
        pass

    def init(self, min=None, max=None): # real signature unknown; restored from __doc__
        """ init(self, min:Graphene.Point3D=None, max:Graphene.Point3D=None) -> Graphene.Box """
        pass

    def init_from_box(self, src): # real signature unknown; restored from __doc__
        """ init_from_box(self, src:Graphene.Box) -> Graphene.Box """
        pass

    def init_from_points(self, points): # real signature unknown; restored from __doc__
        """ init_from_points(self, points:list) -> Graphene.Box """
        pass

    def init_from_vec3(self, min=None, max=None): # real signature unknown; restored from __doc__
        """ init_from_vec3(self, min:Graphene.Vec3=None, max:Graphene.Vec3=None) -> Graphene.Box """
        pass

    def init_from_vectors(self, vectors): # real signature unknown; restored from __doc__
        """ init_from_vectors(self, vectors:list) -> Graphene.Box """
        pass

    def intersection(self, b): # real signature unknown; restored from __doc__
        """ intersection(self, b:Graphene.Box) -> bool, res:Graphene.Box """
        return False

    def minus_one(self): # real signature unknown; restored from __doc__
        """ minus_one() -> Graphene.Box """
        pass

    def one(self): # real signature unknown; restored from __doc__
        """ one() -> Graphene.Box """
        pass

    def one_minus_one(self): # real signature unknown; restored from __doc__
        """ one_minus_one() -> Graphene.Box """
        pass

    def union(self, b): # real signature unknown; restored from __doc__
        """ union(self, b:Graphene.Box) -> res:Graphene.Box """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Box """
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

    max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Box), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneBox (94782570741760)>, '__dict__': <attribute '__dict__' of 'Box' objects>, '__weakref__': <attribute '__weakref__' of 'Box' objects>, '__doc__': None, 'min': <property object at 0x7fa3eccf7900>, 'max': <property object at 0x7fa3eccf7950>, 'alloc': gi.FunctionInfo(alloc), 'contains_box': gi.FunctionInfo(contains_box), 'contains_point': gi.FunctionInfo(contains_point), 'equal': gi.FunctionInfo(equal), 'expand': gi.FunctionInfo(expand), 'expand_scalar': gi.FunctionInfo(expand_scalar), 'expand_vec3': gi.FunctionInfo(expand_vec3), 'free': gi.FunctionInfo(free), 'get_bounding_sphere': gi.FunctionInfo(get_bounding_sphere), 'get_center': gi.FunctionInfo(get_center), 'get_depth': gi.FunctionInfo(get_depth), 'get_height': gi.FunctionInfo(get_height), 'get_max': gi.FunctionInfo(get_max), 'get_min': gi.FunctionInfo(get_min), 'get_size': gi.FunctionInfo(get_size), 'get_vertices': gi.FunctionInfo(get_vertices), 'get_width': gi.FunctionInfo(get_width), 'init': gi.FunctionInfo(init), 'init_from_box': gi.FunctionInfo(init_from_box), 'init_from_points': gi.FunctionInfo(init_from_points), 'init_from_vec3': gi.FunctionInfo(init_from_vec3), 'init_from_vectors': gi.FunctionInfo(init_from_vectors), 'intersection': gi.FunctionInfo(intersection), 'union': gi.FunctionInfo(union), 'empty': gi.FunctionInfo(empty), 'infinite': gi.FunctionInfo(infinite), 'minus_one': gi.FunctionInfo(minus_one), 'one': gi.FunctionInfo(one), 'one_minus_one': gi.FunctionInfo(one_minus_one), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GrapheneBox (94782570741760)>'
    __info__ = StructInfo(Box)


class Euler(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Euler()
        alloc() -> Graphene.Euler
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Euler """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Euler) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_beta(self): # real signature unknown; restored from __doc__
        """ get_beta(self) -> float """
        return 0.0

    def get_gamma(self): # real signature unknown; restored from __doc__
        """ get_gamma(self) -> float """
        return 0.0

    def get_order(self): # real signature unknown; restored from __doc__
        """ get_order(self) -> Graphene.EulerOrder """
        pass

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def get_z(self): # real signature unknown; restored from __doc__
        """ get_z(self) -> float """
        return 0.0

    def init(self, x, y, z): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float, z:float) -> Graphene.Euler """
        pass

    def init_from_euler(self, src=None): # real signature unknown; restored from __doc__
        """ init_from_euler(self, src:Graphene.Euler=None) -> Graphene.Euler """
        pass

    def init_from_matrix(self, m=None, order): # real signature unknown; restored from __doc__
        """ init_from_matrix(self, m:Graphene.Matrix=None, order:Graphene.EulerOrder) -> Graphene.Euler """
        pass

    def init_from_quaternion(self, q=None, order): # real signature unknown; restored from __doc__
        """ init_from_quaternion(self, q:Graphene.Quaternion=None, order:Graphene.EulerOrder) -> Graphene.Euler """
        pass

    def init_from_radians(self, x, y, z, order): # real signature unknown; restored from __doc__
        """ init_from_radians(self, x:float, y:float, z:float, order:Graphene.EulerOrder) -> Graphene.Euler """
        pass

    def init_from_vec3(self, v=None, order): # real signature unknown; restored from __doc__
        """ init_from_vec3(self, v:Graphene.Vec3=None, order:Graphene.EulerOrder) -> Graphene.Euler """
        pass

    def init_with_order(self, x, y, z, order): # real signature unknown; restored from __doc__
        """ init_with_order(self, x:float, y:float, z:float, order:Graphene.EulerOrder) -> Graphene.Euler """
        pass

    def reorder(self, order): # real signature unknown; restored from __doc__
        """ reorder(self, order:Graphene.EulerOrder) -> res:Graphene.Euler """
        pass

    def to_matrix(self): # real signature unknown; restored from __doc__
        """ to_matrix(self) -> res:Graphene.Matrix """
        pass

    def to_quaternion(self): # real signature unknown; restored from __doc__
        """ to_quaternion(self) -> res:Graphene.Quaternion """
        pass

    def to_vec3(self): # real signature unknown; restored from __doc__
        """ to_vec3(self) -> res:Graphene.Vec3 """
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

    angles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Euler), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneEuler (94782570768432)>, '__dict__': <attribute '__dict__' of 'Euler' objects>, '__weakref__': <attribute '__weakref__' of 'Euler' objects>, '__doc__': None, 'angles': <property object at 0x7fa3eccf7b30>, 'order': <property object at 0x7fa3ecd2f0e0>, 'alloc': gi.FunctionInfo(alloc), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_alpha': gi.FunctionInfo(get_alpha), 'get_beta': gi.FunctionInfo(get_beta), 'get_gamma': gi.FunctionInfo(get_gamma), 'get_order': gi.FunctionInfo(get_order), 'get_x': gi.FunctionInfo(get_x), 'get_y': gi.FunctionInfo(get_y), 'get_z': gi.FunctionInfo(get_z), 'init': gi.FunctionInfo(init), 'init_from_euler': gi.FunctionInfo(init_from_euler), 'init_from_matrix': gi.FunctionInfo(init_from_matrix), 'init_from_quaternion': gi.FunctionInfo(init_from_quaternion), 'init_from_radians': gi.FunctionInfo(init_from_radians), 'init_from_vec3': gi.FunctionInfo(init_from_vec3), 'init_with_order': gi.FunctionInfo(init_with_order), 'reorder': gi.FunctionInfo(reorder), 'to_matrix': gi.FunctionInfo(to_matrix), 'to_quaternion': gi.FunctionInfo(to_quaternion), 'to_vec3': gi.FunctionInfo(to_vec3)})"
    __gtype__ = None # (!) real value is '<GType GrapheneEuler (94782570768432)>'
    __info__ = StructInfo(Euler)


class EulerOrder(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DEFAULT = -1
    RXYX = 19
    RXYZ = 28
    RXZX = 21
    RXZY = 22
    RYXY = 25
    RYXZ = 26
    RYZX = 20
    RYZY = 23
    RZXY = 24
    RZXZ = 27
    RZYX = 18
    RZYZ = 29
    SXYX = 7
    SXYZ = 6
    SXZX = 9
    SXZY = 8
    SYXY = 13
    SYXZ = 12
    SYZX = 10
    SYZY = 11
    SZXY = 14
    SZXZ = 15
    SZYX = 16
    SZYZ = 17
    XYZ = 0
    XZY = 3
    YXZ = 4
    YZX = 1
    ZXY = 2
    ZYX = 5
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Graphene', '__dict__': <attribute '__dict__' of 'EulerOrder' objects>, '__doc__': None, '__gtype__': <GType PyGrapheneEulerOrder (94782570691568)>, '__enum_values__': {-1: <enum GRAPHENE_EULER_ORDER_DEFAULT of type Graphene.EulerOrder>, 0: <enum GRAPHENE_EULER_ORDER_XYZ of type Graphene.EulerOrder>, 1: <enum GRAPHENE_EULER_ORDER_YZX of type Graphene.EulerOrder>, 2: <enum GRAPHENE_EULER_ORDER_ZXY of type Graphene.EulerOrder>, 3: <enum GRAPHENE_EULER_ORDER_XZY of type Graphene.EulerOrder>, 4: <enum GRAPHENE_EULER_ORDER_YXZ of type Graphene.EulerOrder>, 5: <enum GRAPHENE_EULER_ORDER_ZYX of type Graphene.EulerOrder>, 6: <enum GRAPHENE_EULER_ORDER_SXYZ of type Graphene.EulerOrder>, 7: <enum GRAPHENE_EULER_ORDER_SXYX of type Graphene.EulerOrder>, 8: <enum GRAPHENE_EULER_ORDER_SXZY of type Graphene.EulerOrder>, 9: <enum GRAPHENE_EULER_ORDER_SXZX of type Graphene.EulerOrder>, 10: <enum GRAPHENE_EULER_ORDER_SYZX of type Graphene.EulerOrder>, 11: <enum GRAPHENE_EULER_ORDER_SYZY of type Graphene.EulerOrder>, 12: <enum GRAPHENE_EULER_ORDER_SYXZ of type Graphene.EulerOrder>, 13: <enum GRAPHENE_EULER_ORDER_SYXY of type Graphene.EulerOrder>, 14: <enum GRAPHENE_EULER_ORDER_SZXY of type Graphene.EulerOrder>, 15: <enum GRAPHENE_EULER_ORDER_SZXZ of type Graphene.EulerOrder>, 16: <enum GRAPHENE_EULER_ORDER_SZYX of type Graphene.EulerOrder>, 17: <enum GRAPHENE_EULER_ORDER_SZYZ of type Graphene.EulerOrder>, 18: <enum GRAPHENE_EULER_ORDER_RZYX of type Graphene.EulerOrder>, 19: <enum GRAPHENE_EULER_ORDER_RXYX of type Graphene.EulerOrder>, 20: <enum GRAPHENE_EULER_ORDER_RYZX of type Graphene.EulerOrder>, 21: <enum GRAPHENE_EULER_ORDER_RXZX of type Graphene.EulerOrder>, 22: <enum GRAPHENE_EULER_ORDER_RXZY of type Graphene.EulerOrder>, 23: <enum GRAPHENE_EULER_ORDER_RYZY of type Graphene.EulerOrder>, 24: <enum GRAPHENE_EULER_ORDER_RZXY of type Graphene.EulerOrder>, 25: <enum GRAPHENE_EULER_ORDER_RYXY of type Graphene.EulerOrder>, 26: <enum GRAPHENE_EULER_ORDER_RYXZ of type Graphene.EulerOrder>, 27: <enum GRAPHENE_EULER_ORDER_RZXZ of type Graphene.EulerOrder>, 28: <enum GRAPHENE_EULER_ORDER_RXYZ of type Graphene.EulerOrder>, 29: <enum GRAPHENE_EULER_ORDER_RZYZ of type Graphene.EulerOrder>}, '__info__': gi.EnumInfo(EulerOrder), 'DEFAULT': <enum GRAPHENE_EULER_ORDER_DEFAULT of type Graphene.EulerOrder>, 'XYZ': <enum GRAPHENE_EULER_ORDER_XYZ of type Graphene.EulerOrder>, 'YZX': <enum GRAPHENE_EULER_ORDER_YZX of type Graphene.EulerOrder>, 'ZXY': <enum GRAPHENE_EULER_ORDER_ZXY of type Graphene.EulerOrder>, 'XZY': <enum GRAPHENE_EULER_ORDER_XZY of type Graphene.EulerOrder>, 'YXZ': <enum GRAPHENE_EULER_ORDER_YXZ of type Graphene.EulerOrder>, 'ZYX': <enum GRAPHENE_EULER_ORDER_ZYX of type Graphene.EulerOrder>, 'SXYZ': <enum GRAPHENE_EULER_ORDER_SXYZ of type Graphene.EulerOrder>, 'SXYX': <enum GRAPHENE_EULER_ORDER_SXYX of type Graphene.EulerOrder>, 'SXZY': <enum GRAPHENE_EULER_ORDER_SXZY of type Graphene.EulerOrder>, 'SXZX': <enum GRAPHENE_EULER_ORDER_SXZX of type Graphene.EulerOrder>, 'SYZX': <enum GRAPHENE_EULER_ORDER_SYZX of type Graphene.EulerOrder>, 'SYZY': <enum GRAPHENE_EULER_ORDER_SYZY of type Graphene.EulerOrder>, 'SYXZ': <enum GRAPHENE_EULER_ORDER_SYXZ of type Graphene.EulerOrder>, 'SYXY': <enum GRAPHENE_EULER_ORDER_SYXY of type Graphene.EulerOrder>, 'SZXY': <enum GRAPHENE_EULER_ORDER_SZXY of type Graphene.EulerOrder>, 'SZXZ': <enum GRAPHENE_EULER_ORDER_SZXZ of type Graphene.EulerOrder>, 'SZYX': <enum GRAPHENE_EULER_ORDER_SZYX of type Graphene.EulerOrder>, 'SZYZ': <enum GRAPHENE_EULER_ORDER_SZYZ of type Graphene.EulerOrder>, 'RZYX': <enum GRAPHENE_EULER_ORDER_RZYX of type Graphene.EulerOrder>, 'RXYX': <enum GRAPHENE_EULER_ORDER_RXYX of type Graphene.EulerOrder>, 'RYZX': <enum GRAPHENE_EULER_ORDER_RYZX of type Graphene.EulerOrder>, 'RXZX': <enum GRAPHENE_EULER_ORDER_RXZX of type Graphene.EulerOrder>, 'RXZY': <enum GRAPHENE_EULER_ORDER_RXZY of type Graphene.EulerOrder>, 'RYZY': <enum GRAPHENE_EULER_ORDER_RYZY of type Graphene.EulerOrder>, 'RZXY': <enum GRAPHENE_EULER_ORDER_RZXY of type Graphene.EulerOrder>, 'RYXY': <enum GRAPHENE_EULER_ORDER_RYXY of type Graphene.EulerOrder>, 'RYXZ': <enum GRAPHENE_EULER_ORDER_RYXZ of type Graphene.EulerOrder>, 'RZXZ': <enum GRAPHENE_EULER_ORDER_RZXZ of type Graphene.EulerOrder>, 'RXYZ': <enum GRAPHENE_EULER_ORDER_RXYZ of type Graphene.EulerOrder>, 'RZYZ': <enum GRAPHENE_EULER_ORDER_RZYZ of type Graphene.EulerOrder>})"
    __enum_values__ = {
        -1: -1,
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
    }
    __gtype__ = None # (!) real value is '<GType PyGrapheneEulerOrder (94782570691568)>'
    __info__ = gi.EnumInfo(EulerOrder)


class Frustum(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Frustum()
        alloc() -> Graphene.Frustum
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Frustum """
        pass

    def contains_point(self, point): # real signature unknown; restored from __doc__
        """ contains_point(self, point:Graphene.Point3D) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Frustum) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_planes(self): # real signature unknown; restored from __doc__
        """ get_planes(self) -> planes:list """
        pass

    def init(self, p0, p1, p2, p3, p4, p5): # real signature unknown; restored from __doc__
        """ init(self, p0:Graphene.Plane, p1:Graphene.Plane, p2:Graphene.Plane, p3:Graphene.Plane, p4:Graphene.Plane, p5:Graphene.Plane) -> Graphene.Frustum """
        pass

    def init_from_frustum(self, src): # real signature unknown; restored from __doc__
        """ init_from_frustum(self, src:Graphene.Frustum) -> Graphene.Frustum """
        pass

    def init_from_matrix(self, matrix): # real signature unknown; restored from __doc__
        """ init_from_matrix(self, matrix:Graphene.Matrix) -> Graphene.Frustum """
        pass

    def intersects_box(self, box): # real signature unknown; restored from __doc__
        """ intersects_box(self, box:Graphene.Box) -> bool """
        return False

    def intersects_sphere(self, sphere): # real signature unknown; restored from __doc__
        """ intersects_sphere(self, sphere:Graphene.Sphere) -> bool """
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

    planes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Frustum), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneFrustum (94782570828384)>, '__dict__': <attribute '__dict__' of 'Frustum' objects>, '__weakref__': <attribute '__weakref__' of 'Frustum' objects>, '__doc__': None, 'planes': <property object at 0x7fa3eccb5db0>, 'alloc': gi.FunctionInfo(alloc), 'contains_point': gi.FunctionInfo(contains_point), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_planes': gi.FunctionInfo(get_planes), 'init': gi.FunctionInfo(init), 'init_from_frustum': gi.FunctionInfo(init_from_frustum), 'init_from_matrix': gi.FunctionInfo(init_from_matrix), 'intersects_box': gi.FunctionInfo(intersects_box), 'intersects_sphere': gi.FunctionInfo(intersects_sphere)})"
    __gtype__ = None # (!) real value is '<GType GrapheneFrustum (94782570828384)>'
    __info__ = StructInfo(Frustum)


class Matrix(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Matrix()
        alloc() -> Graphene.Matrix
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Matrix """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def decompose(self): # real signature unknown; restored from __doc__
        """ decompose(self) -> bool, translate:Graphene.Vec3, scale:Graphene.Vec3, rotate:Graphene.Quaternion, shear:Graphene.Vec3, perspective:Graphene.Vec4 """
        return False

    def determinant(self): # real signature unknown; restored from __doc__
        """ determinant(self) -> float """
        return 0.0

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Matrix) -> bool """
        return False

    def equal_fast(self, b): # real signature unknown; restored from __doc__
        """ equal_fast(self, b:Graphene.Matrix) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_row(self, index_): # real signature unknown; restored from __doc__
        """ get_row(self, index_:int) -> res:Graphene.Vec4 """
        pass

    def get_value(self, row, col): # real signature unknown; restored from __doc__
        """ get_value(self, row:int, col:int) -> float """
        return 0.0

    def get_x_scale(self): # real signature unknown; restored from __doc__
        """ get_x_scale(self) -> float """
        return 0.0

    def get_x_translation(self): # real signature unknown; restored from __doc__
        """ get_x_translation(self) -> float """
        return 0.0

    def get_y_scale(self): # real signature unknown; restored from __doc__
        """ get_y_scale(self) -> float """
        return 0.0

    def get_y_translation(self): # real signature unknown; restored from __doc__
        """ get_y_translation(self) -> float """
        return 0.0

    def get_z_scale(self): # real signature unknown; restored from __doc__
        """ get_z_scale(self) -> float """
        return 0.0

    def get_z_translation(self): # real signature unknown; restored from __doc__
        """ get_z_translation(self) -> float """
        return 0.0

    def init_from_2d(self, xx, yx, xy, yy, x_0, y_0): # real signature unknown; restored from __doc__
        """ init_from_2d(self, xx:float, yx:float, xy:float, yy:float, x_0:float, y_0:float) -> Graphene.Matrix """
        pass

    def init_from_float(self, v): # real signature unknown; restored from __doc__
        """ init_from_float(self, v:list) -> Graphene.Matrix """
        pass

    def init_from_matrix(self, src): # real signature unknown; restored from __doc__
        """ init_from_matrix(self, src:Graphene.Matrix) -> Graphene.Matrix """
        pass

    def init_from_vec4(self, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ init_from_vec4(self, v0:Graphene.Vec4, v1:Graphene.Vec4, v2:Graphene.Vec4, v3:Graphene.Vec4) -> Graphene.Matrix """
        pass

    def init_frustum(self, left, right, bottom, top, z_near, z_far): # real signature unknown; restored from __doc__
        """ init_frustum(self, left:float, right:float, bottom:float, top:float, z_near:float, z_far:float) -> Graphene.Matrix """
        pass

    def init_identity(self): # real signature unknown; restored from __doc__
        """ init_identity(self) -> Graphene.Matrix """
        pass

    def init_look_at(self, eye, center, up): # real signature unknown; restored from __doc__
        """ init_look_at(self, eye:Graphene.Vec3, center:Graphene.Vec3, up:Graphene.Vec3) -> Graphene.Matrix """
        pass

    def init_ortho(self, left, right, top, bottom, z_near, z_far): # real signature unknown; restored from __doc__
        """ init_ortho(self, left:float, right:float, top:float, bottom:float, z_near:float, z_far:float) -> Graphene.Matrix """
        pass

    def init_perspective(self, fovy, aspect, z_near, z_far): # real signature unknown; restored from __doc__
        """ init_perspective(self, fovy:float, aspect:float, z_near:float, z_far:float) -> Graphene.Matrix """
        pass

    def init_rotate(self, angle, axis): # real signature unknown; restored from __doc__
        """ init_rotate(self, angle:float, axis:Graphene.Vec3) -> Graphene.Matrix """
        pass

    def init_scale(self, x, y, z): # real signature unknown; restored from __doc__
        """ init_scale(self, x:float, y:float, z:float) -> Graphene.Matrix """
        pass

    def init_skew(self, x_skew, y_skew): # real signature unknown; restored from __doc__
        """ init_skew(self, x_skew:float, y_skew:float) -> Graphene.Matrix """
        pass

    def init_translate(self, p): # real signature unknown; restored from __doc__
        """ init_translate(self, p:Graphene.Point3D) -> Graphene.Matrix """
        pass

    def interpolate(self, b, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, b:Graphene.Matrix, factor:float) -> res:Graphene.Matrix """
        pass

    def inverse(self): # real signature unknown; restored from __doc__
        """ inverse(self) -> bool, res:Graphene.Matrix """
        return False

    def is_2d(self): # real signature unknown; restored from __doc__
        """ is_2d(self) -> bool """
        return False

    def is_backface_visible(self): # real signature unknown; restored from __doc__
        """ is_backface_visible(self) -> bool """
        return False

    def is_identity(self): # real signature unknown; restored from __doc__
        """ is_identity(self) -> bool """
        return False

    def is_singular(self): # real signature unknown; restored from __doc__
        """ is_singular(self) -> bool """
        return False

    def multiply(self, b): # real signature unknown; restored from __doc__
        """ multiply(self, b:Graphene.Matrix) -> res:Graphene.Matrix """
        pass

    def near(self, b, epsilon): # real signature unknown; restored from __doc__
        """ near(self, b:Graphene.Matrix, epsilon:float) -> bool """
        return False

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> res:Graphene.Matrix """
        pass

    def perspective(self, depth): # real signature unknown; restored from __doc__
        """ perspective(self, depth:float) -> res:Graphene.Matrix """
        pass

    def print_(self): # real signature unknown; restored from __doc__
        """ print_(self) """
        pass

    def project_point(self, p): # real signature unknown; restored from __doc__
        """ project_point(self, p:Graphene.Point) -> res:Graphene.Point """
        pass

    def project_rect(self, r): # real signature unknown; restored from __doc__
        """ project_rect(self, r:Graphene.Rect) -> res:Graphene.Quad """
        pass

    def project_rect_bounds(self, r): # real signature unknown; restored from __doc__
        """ project_rect_bounds(self, r:Graphene.Rect) -> res:Graphene.Rect """
        pass

    def rotate(self, angle, axis): # real signature unknown; restored from __doc__
        """ rotate(self, angle:float, axis:Graphene.Vec3) """
        pass

    def rotate_euler(self, e): # real signature unknown; restored from __doc__
        """ rotate_euler(self, e:Graphene.Euler) """
        pass

    def rotate_quaternion(self, q): # real signature unknown; restored from __doc__
        """ rotate_quaternion(self, q:Graphene.Quaternion) """
        pass

    def rotate_x(self, angle): # real signature unknown; restored from __doc__
        """ rotate_x(self, angle:float) """
        pass

    def rotate_y(self, angle): # real signature unknown; restored from __doc__
        """ rotate_y(self, angle:float) """
        pass

    def rotate_z(self, angle): # real signature unknown; restored from __doc__
        """ rotate_z(self, angle:float) """
        pass

    def scale(self, factor_x, factor_y, factor_z): # real signature unknown; restored from __doc__
        """ scale(self, factor_x:float, factor_y:float, factor_z:float) """
        pass

    def skew_xy(self, factor): # real signature unknown; restored from __doc__
        """ skew_xy(self, factor:float) """
        pass

    def skew_xz(self, factor): # real signature unknown; restored from __doc__
        """ skew_xz(self, factor:float) """
        pass

    def skew_yz(self, factor): # real signature unknown; restored from __doc__
        """ skew_yz(self, factor:float) """
        pass

    def to_2d(self): # real signature unknown; restored from __doc__
        """ to_2d(self) -> bool, xx:float, yx:float, xy:float, yy:float, x_0:float, y_0:float """
        return False

    def to_float(self): # real signature unknown; restored from __doc__
        """ to_float(self) -> v:list """
        pass

    def transform_bounds(self, r): # real signature unknown; restored from __doc__
        """ transform_bounds(self, r:Graphene.Rect) -> res:Graphene.Rect """
        pass

    def transform_box(self, b): # real signature unknown; restored from __doc__
        """ transform_box(self, b:Graphene.Box) -> res:Graphene.Box """
        pass

    def transform_point(self, p): # real signature unknown; restored from __doc__
        """ transform_point(self, p:Graphene.Point) -> res:Graphene.Point """
        pass

    def transform_point3d(self, p): # real signature unknown; restored from __doc__
        """ transform_point3d(self, p:Graphene.Point3D) -> res:Graphene.Point3D """
        pass

    def transform_ray(self, r): # real signature unknown; restored from __doc__
        """ transform_ray(self, r:Graphene.Ray) -> res:Graphene.Ray """
        pass

    def transform_rect(self, r): # real signature unknown; restored from __doc__
        """ transform_rect(self, r:Graphene.Rect) -> res:Graphene.Quad """
        pass

    def transform_sphere(self, s): # real signature unknown; restored from __doc__
        """ transform_sphere(self, s:Graphene.Sphere) -> res:Graphene.Sphere """
        pass

    def transform_vec3(self, v): # real signature unknown; restored from __doc__
        """ transform_vec3(self, v:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def transform_vec4(self, v): # real signature unknown; restored from __doc__
        """ transform_vec4(self, v:Graphene.Vec4) -> res:Graphene.Vec4 """
        pass

    def translate(self, pos): # real signature unknown; restored from __doc__
        """ translate(self, pos:Graphene.Point3D) """
        pass

    def transpose(self): # real signature unknown; restored from __doc__
        """ transpose(self) -> res:Graphene.Matrix """
        pass

    def unproject_point3d(self, modelview, point): # real signature unknown; restored from __doc__
        """ unproject_point3d(self, modelview:Graphene.Matrix, point:Graphene.Point3D) -> res:Graphene.Point3D """
        pass

    def untransform_bounds(self, r, bounds): # real signature unknown; restored from __doc__
        """ untransform_bounds(self, r:Graphene.Rect, bounds:Graphene.Rect) -> res:Graphene.Rect """
        pass

    def untransform_point(self, p, bounds): # real signature unknown; restored from __doc__
        """ untransform_point(self, p:Graphene.Point, bounds:Graphene.Rect) -> bool, res:Graphene.Point """
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

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Matrix), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneMatrix (94782571181680)>, '__dict__': <attribute '__dict__' of 'Matrix' objects>, '__weakref__': <attribute '__weakref__' of 'Matrix' objects>, '__doc__': None, 'value': <property object at 0x7fa3ecc85040>, 'alloc': gi.FunctionInfo(alloc), 'decompose': gi.FunctionInfo(decompose), 'determinant': gi.FunctionInfo(determinant), 'equal': gi.FunctionInfo(equal), 'equal_fast': gi.FunctionInfo(equal_fast), 'free': gi.FunctionInfo(free), 'get_row': gi.FunctionInfo(get_row), 'get_value': gi.FunctionInfo(get_value), 'get_x_scale': gi.FunctionInfo(get_x_scale), 'get_x_translation': gi.FunctionInfo(get_x_translation), 'get_y_scale': gi.FunctionInfo(get_y_scale), 'get_y_translation': gi.FunctionInfo(get_y_translation), 'get_z_scale': gi.FunctionInfo(get_z_scale), 'get_z_translation': gi.FunctionInfo(get_z_translation), 'init_from_2d': gi.FunctionInfo(init_from_2d), 'init_from_float': gi.FunctionInfo(init_from_float), 'init_from_matrix': gi.FunctionInfo(init_from_matrix), 'init_from_vec4': gi.FunctionInfo(init_from_vec4), 'init_frustum': gi.FunctionInfo(init_frustum), 'init_identity': gi.FunctionInfo(init_identity), 'init_look_at': gi.FunctionInfo(init_look_at), 'init_ortho': gi.FunctionInfo(init_ortho), 'init_perspective': gi.FunctionInfo(init_perspective), 'init_rotate': gi.FunctionInfo(init_rotate), 'init_scale': gi.FunctionInfo(init_scale), 'init_skew': gi.FunctionInfo(init_skew), 'init_translate': gi.FunctionInfo(init_translate), 'interpolate': gi.FunctionInfo(interpolate), 'inverse': gi.FunctionInfo(inverse), 'is_2d': gi.FunctionInfo(is_2d), 'is_backface_visible': gi.FunctionInfo(is_backface_visible), 'is_identity': gi.FunctionInfo(is_identity), 'is_singular': gi.FunctionInfo(is_singular), 'multiply': gi.FunctionInfo(multiply), 'near': gi.FunctionInfo(near), 'normalize': gi.FunctionInfo(normalize), 'perspective': gi.FunctionInfo(perspective), 'print_': gi.FunctionInfo(print), 'project_point': gi.FunctionInfo(project_point), 'project_rect': gi.FunctionInfo(project_rect), 'project_rect_bounds': gi.FunctionInfo(project_rect_bounds), 'rotate': gi.FunctionInfo(rotate), 'rotate_euler': gi.FunctionInfo(rotate_euler), 'rotate_quaternion': gi.FunctionInfo(rotate_quaternion), 'rotate_x': gi.FunctionInfo(rotate_x), 'rotate_y': gi.FunctionInfo(rotate_y), 'rotate_z': gi.FunctionInfo(rotate_z), 'scale': gi.FunctionInfo(scale), 'skew_xy': gi.FunctionInfo(skew_xy), 'skew_xz': gi.FunctionInfo(skew_xz), 'skew_yz': gi.FunctionInfo(skew_yz), 'to_2d': gi.FunctionInfo(to_2d), 'to_float': gi.FunctionInfo(to_float), 'transform_bounds': gi.FunctionInfo(transform_bounds), 'transform_box': gi.FunctionInfo(transform_box), 'transform_point': gi.FunctionInfo(transform_point), 'transform_point3d': gi.FunctionInfo(transform_point3d), 'transform_ray': gi.FunctionInfo(transform_ray), 'transform_rect': gi.FunctionInfo(transform_rect), 'transform_sphere': gi.FunctionInfo(transform_sphere), 'transform_vec3': gi.FunctionInfo(transform_vec3), 'transform_vec4': gi.FunctionInfo(transform_vec4), 'translate': gi.FunctionInfo(translate), 'transpose': gi.FunctionInfo(transpose), 'unproject_point3d': gi.FunctionInfo(unproject_point3d), 'untransform_bounds': gi.FunctionInfo(untransform_bounds), 'untransform_point': gi.FunctionInfo(untransform_point)})"
    __gtype__ = None # (!) real value is '<GType GrapheneMatrix (94782571181680)>'
    __info__ = StructInfo(Matrix)


class Plane(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Plane()
        alloc() -> Graphene.Plane
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Plane """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def distance(self, point): # real signature unknown; restored from __doc__
        """ distance(self, point:Graphene.Point3D) -> float """
        return 0.0

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Plane) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_constant(self): # real signature unknown; restored from __doc__
        """ get_constant(self) -> float """
        return 0.0

    def get_normal(self): # real signature unknown; restored from __doc__
        """ get_normal(self) -> normal:Graphene.Vec3 """
        pass

    def init(self, normal=None, constant): # real signature unknown; restored from __doc__
        """ init(self, normal:Graphene.Vec3=None, constant:float) -> Graphene.Plane """
        pass

    def init_from_plane(self, src): # real signature unknown; restored from __doc__
        """ init_from_plane(self, src:Graphene.Plane) -> Graphene.Plane """
        pass

    def init_from_point(self, normal, point): # real signature unknown; restored from __doc__
        """ init_from_point(self, normal:Graphene.Vec3, point:Graphene.Point3D) -> Graphene.Plane """
        pass

    def init_from_points(self, a, b, c): # real signature unknown; restored from __doc__
        """ init_from_points(self, a:Graphene.Point3D, b:Graphene.Point3D, c:Graphene.Point3D) -> Graphene.Plane """
        pass

    def init_from_vec4(self, src): # real signature unknown; restored from __doc__
        """ init_from_vec4(self, src:Graphene.Vec4) -> Graphene.Plane """
        pass

    def negate(self): # real signature unknown; restored from __doc__
        """ negate(self) -> res:Graphene.Plane """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> res:Graphene.Plane """
        pass

    def transform(self, matrix, normal_matrix=None): # real signature unknown; restored from __doc__
        """ transform(self, matrix:Graphene.Matrix, normal_matrix:Graphene.Matrix=None) -> res:Graphene.Plane """
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

    constant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Plane), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GraphenePlane (94782570883712)>, '__dict__': <attribute '__dict__' of 'Plane' objects>, '__weakref__': <attribute '__weakref__' of 'Plane' objects>, '__doc__': None, 'normal': <property object at 0x7fa3ecc855e0>, 'constant': <property object at 0x7fa3ecc856d0>, 'alloc': gi.FunctionInfo(alloc), 'distance': gi.FunctionInfo(distance), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_constant': gi.FunctionInfo(get_constant), 'get_normal': gi.FunctionInfo(get_normal), 'init': gi.FunctionInfo(init), 'init_from_plane': gi.FunctionInfo(init_from_plane), 'init_from_point': gi.FunctionInfo(init_from_point), 'init_from_points': gi.FunctionInfo(init_from_points), 'init_from_vec4': gi.FunctionInfo(init_from_vec4), 'negate': gi.FunctionInfo(negate), 'normalize': gi.FunctionInfo(normalize), 'transform': gi.FunctionInfo(transform)})"
    __gtype__ = None # (!) real value is '<GType GraphenePlane (94782570883712)>'
    __info__ = StructInfo(Plane)


class Point(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Point()
        alloc() -> Graphene.Point
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Point """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def distance(self, b): # real signature unknown; restored from __doc__
        """ distance(self, b:Graphene.Point) -> float, d_x:float, d_y:float """
        return 0.0

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Point) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self, x, y): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float) -> Graphene.Point """
        pass

    def init_from_point(self, src): # real signature unknown; restored from __doc__
        """ init_from_point(self, src:Graphene.Point) -> Graphene.Point """
        pass

    def init_from_vec2(self, src): # real signature unknown; restored from __doc__
        """ init_from_vec2(self, src:Graphene.Vec2) -> Graphene.Point """
        pass

    def interpolate(self, b, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, b:Graphene.Point, factor:float) -> res:Graphene.Point """
        pass

    def near(self, b, epsilon): # real signature unknown; restored from __doc__
        """ near(self, b:Graphene.Point, epsilon:float) -> bool """
        return False

    def to_vec2(self): # real signature unknown; restored from __doc__
        """ to_vec2(self) -> v:Graphene.Vec2 """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Point """
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

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Point), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GraphenePoint (94782571197712)>, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None, 'x': <property object at 0x7fa3ecc85860>, 'y': <property object at 0x7fa3ecc85950>, 'alloc': gi.FunctionInfo(alloc), 'distance': gi.FunctionInfo(distance), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init), 'init_from_point': gi.FunctionInfo(init_from_point), 'init_from_vec2': gi.FunctionInfo(init_from_vec2), 'interpolate': gi.FunctionInfo(interpolate), 'near': gi.FunctionInfo(near), 'to_vec2': gi.FunctionInfo(to_vec2), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GraphenePoint (94782571197712)>'
    __info__ = StructInfo(Point)


class Point3D(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Point3D()
        alloc() -> Graphene.Point3D
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Point3D """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def cross(self, b): # real signature unknown; restored from __doc__
        """ cross(self, b:Graphene.Point3D) -> res:Graphene.Point3D """
        pass

    def distance(self, b): # real signature unknown; restored from __doc__
        """ distance(self, b:Graphene.Point3D) -> float, delta:Graphene.Vec3 """
        return 0.0

    def dot(self, b): # real signature unknown; restored from __doc__
        """ dot(self, b:Graphene.Point3D) -> float """
        return 0.0

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Point3D) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self, x, y, z): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float, z:float) -> Graphene.Point3D """
        pass

    def init_from_point(self, src): # real signature unknown; restored from __doc__
        """ init_from_point(self, src:Graphene.Point3D) -> Graphene.Point3D """
        pass

    def init_from_vec3(self, v): # real signature unknown; restored from __doc__
        """ init_from_vec3(self, v:Graphene.Vec3) -> Graphene.Point3D """
        pass

    def interpolate(self, b, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, b:Graphene.Point3D, factor:float) -> res:Graphene.Point3D """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def near(self, b, epsilon): # real signature unknown; restored from __doc__
        """ near(self, b:Graphene.Point3D, epsilon:float) -> bool """
        return False

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> res:Graphene.Point3D """
        pass

    def normalize_viewport(self, viewport, z_near, z_far): # real signature unknown; restored from __doc__
        """ normalize_viewport(self, viewport:Graphene.Rect, z_near:float, z_far:float) -> res:Graphene.Point3D """
        pass

    def scale(self, factor): # real signature unknown; restored from __doc__
        """ scale(self, factor:float) -> res:Graphene.Point3D """
        pass

    def to_vec3(self): # real signature unknown; restored from __doc__
        """ to_vec3(self) -> v:Graphene.Vec3 """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Point3D """
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

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Point3D), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GraphenePoint3D (94782570945040)>, '__dict__': <attribute '__dict__' of 'Point3D' objects>, '__weakref__': <attribute '__weakref__' of 'Point3D' objects>, '__doc__': None, 'x': <property object at 0x7fa3ecc85ae0>, 'y': <property object at 0x7fa3ecc85bd0>, 'z': <property object at 0x7fa3ecc85cc0>, 'alloc': gi.FunctionInfo(alloc), 'cross': gi.FunctionInfo(cross), 'distance': gi.FunctionInfo(distance), 'dot': gi.FunctionInfo(dot), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init), 'init_from_point': gi.FunctionInfo(init_from_point), 'init_from_vec3': gi.FunctionInfo(init_from_vec3), 'interpolate': gi.FunctionInfo(interpolate), 'length': gi.FunctionInfo(length), 'near': gi.FunctionInfo(near), 'normalize': gi.FunctionInfo(normalize), 'normalize_viewport': gi.FunctionInfo(normalize_viewport), 'scale': gi.FunctionInfo(scale), 'to_vec3': gi.FunctionInfo(to_vec3), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GraphenePoint3D (94782570945040)>'
    __info__ = StructInfo(Point3D)


class Quad(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Quad()
        alloc() -> Graphene.Quad
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Quad """
        pass

    def bounds(self): # real signature unknown; restored from __doc__
        """ bounds(self) -> r:Graphene.Rect """
        pass

    def contains(self, p): # real signature unknown; restored from __doc__
        """ contains(self, p:Graphene.Point) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_point(self, index_): # real signature unknown; restored from __doc__
        """ get_point(self, index_:int) -> Graphene.Point """
        pass

    def init(self, p1, p2, p3, p4): # real signature unknown; restored from __doc__
        """ init(self, p1:Graphene.Point, p2:Graphene.Point, p3:Graphene.Point, p4:Graphene.Point) -> Graphene.Quad """
        pass

    def init_from_points(self, points): # real signature unknown; restored from __doc__
        """ init_from_points(self, points:list) -> Graphene.Quad """
        pass

    def init_from_rect(self, r): # real signature unknown; restored from __doc__
        """ init_from_rect(self, r:Graphene.Rect) -> Graphene.Quad """
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

    points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Quad), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneQuad (94782570945152)>, '__dict__': <attribute '__dict__' of 'Quad' objects>, '__weakref__': <attribute '__weakref__' of 'Quad' objects>, '__doc__': None, 'points': <property object at 0x7fa3ecc85e50>, 'alloc': gi.FunctionInfo(alloc), 'bounds': gi.FunctionInfo(bounds), 'contains': gi.FunctionInfo(contains), 'free': gi.FunctionInfo(free), 'get_point': gi.FunctionInfo(get_point), 'init': gi.FunctionInfo(init), 'init_from_points': gi.FunctionInfo(init_from_points), 'init_from_rect': gi.FunctionInfo(init_from_rect)})"
    __gtype__ = None # (!) real value is '<GType GrapheneQuad (94782570945152)>'
    __info__ = StructInfo(Quad)


class Quaternion(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Quaternion()
        alloc() -> Graphene.Quaternion
    """
    def add(self, b): # real signature unknown; restored from __doc__
        """ add(self, b:Graphene.Quaternion) -> res:Graphene.Quaternion """
        pass

    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Quaternion """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dot(self, b): # real signature unknown; restored from __doc__
        """ dot(self, b:Graphene.Quaternion) -> float """
        return 0.0

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Quaternion) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self, x, y, z, w): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float, z:float, w:float) -> Graphene.Quaternion """
        pass

    def init_from_angles(self, deg_x, deg_y, deg_z): # real signature unknown; restored from __doc__
        """ init_from_angles(self, deg_x:float, deg_y:float, deg_z:float) -> Graphene.Quaternion """
        pass

    def init_from_angle_vec3(self, angle, axis): # real signature unknown; restored from __doc__
        """ init_from_angle_vec3(self, angle:float, axis:Graphene.Vec3) -> Graphene.Quaternion """
        pass

    def init_from_euler(self, e): # real signature unknown; restored from __doc__
        """ init_from_euler(self, e:Graphene.Euler) -> Graphene.Quaternion """
        pass

    def init_from_matrix(self, m): # real signature unknown; restored from __doc__
        """ init_from_matrix(self, m:Graphene.Matrix) -> Graphene.Quaternion """
        pass

    def init_from_quaternion(self, src): # real signature unknown; restored from __doc__
        """ init_from_quaternion(self, src:Graphene.Quaternion) -> Graphene.Quaternion """
        pass

    def init_from_radians(self, rad_x, rad_y, rad_z): # real signature unknown; restored from __doc__
        """ init_from_radians(self, rad_x:float, rad_y:float, rad_z:float) -> Graphene.Quaternion """
        pass

    def init_from_vec4(self, src): # real signature unknown; restored from __doc__
        """ init_from_vec4(self, src:Graphene.Vec4) -> Graphene.Quaternion """
        pass

    def init_identity(self): # real signature unknown; restored from __doc__
        """ init_identity(self) -> Graphene.Quaternion """
        pass

    def invert(self): # real signature unknown; restored from __doc__
        """ invert(self) -> res:Graphene.Quaternion """
        pass

    def multiply(self, b): # real signature unknown; restored from __doc__
        """ multiply(self, b:Graphene.Quaternion) -> res:Graphene.Quaternion """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> res:Graphene.Quaternion """
        pass

    def scale(self, factor): # real signature unknown; restored from __doc__
        """ scale(self, factor:float) -> res:Graphene.Quaternion """
        pass

    def slerp(self, b, factor): # real signature unknown; restored from __doc__
        """ slerp(self, b:Graphene.Quaternion, factor:float) -> res:Graphene.Quaternion """
        pass

    def to_angles(self): # real signature unknown; restored from __doc__
        """ to_angles(self) -> deg_x:float, deg_y:float, deg_z:float """
        pass

    def to_angle_vec3(self): # real signature unknown; restored from __doc__
        """ to_angle_vec3(self) -> angle:float, axis:Graphene.Vec3 """
        pass

    def to_matrix(self): # real signature unknown; restored from __doc__
        """ to_matrix(self) -> m:Graphene.Matrix """
        pass

    def to_radians(self): # real signature unknown; restored from __doc__
        """ to_radians(self) -> rad_x:float, rad_y:float, rad_z:float """
        pass

    def to_vec4(self): # real signature unknown; restored from __doc__
        """ to_vec4(self) -> res:Graphene.Vec4 """
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

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Quaternion), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneQuaternion (94782570808128)>, '__dict__': <attribute '__dict__' of 'Quaternion' objects>, '__weakref__': <attribute '__weakref__' of 'Quaternion' objects>, '__doc__': None, 'x': <property object at 0x7fa3ecc8c040>, 'y': <property object at 0x7fa3ecc8c130>, 'z': <property object at 0x7fa3ecc8c220>, 'w': <property object at 0x7fa3ecc8c310>, 'alloc': gi.FunctionInfo(alloc), 'add': gi.FunctionInfo(add), 'dot': gi.FunctionInfo(dot), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init), 'init_from_angle_vec3': gi.FunctionInfo(init_from_angle_vec3), 'init_from_angles': gi.FunctionInfo(init_from_angles), 'init_from_euler': gi.FunctionInfo(init_from_euler), 'init_from_matrix': gi.FunctionInfo(init_from_matrix), 'init_from_quaternion': gi.FunctionInfo(init_from_quaternion), 'init_from_radians': gi.FunctionInfo(init_from_radians), 'init_from_vec4': gi.FunctionInfo(init_from_vec4), 'init_identity': gi.FunctionInfo(init_identity), 'invert': gi.FunctionInfo(invert), 'multiply': gi.FunctionInfo(multiply), 'normalize': gi.FunctionInfo(normalize), 'scale': gi.FunctionInfo(scale), 'slerp': gi.FunctionInfo(slerp), 'to_angle_vec3': gi.FunctionInfo(to_angle_vec3), 'to_angles': gi.FunctionInfo(to_angles), 'to_matrix': gi.FunctionInfo(to_matrix), 'to_radians': gi.FunctionInfo(to_radians), 'to_vec4': gi.FunctionInfo(to_vec4)})"
    __gtype__ = None # (!) real value is '<GType GrapheneQuaternion (94782570808128)>'
    __info__ = StructInfo(Quaternion)


class Ray(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Ray()
        alloc() -> Graphene.Ray
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Ray """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Ray) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_closest_point_to_point(self, p): # real signature unknown; restored from __doc__
        """ get_closest_point_to_point(self, p:Graphene.Point3D) -> res:Graphene.Point3D """
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> direction:Graphene.Vec3 """
        pass

    def get_distance_to_plane(self, p): # real signature unknown; restored from __doc__
        """ get_distance_to_plane(self, p:Graphene.Plane) -> float """
        return 0.0

    def get_distance_to_point(self, p): # real signature unknown; restored from __doc__
        """ get_distance_to_point(self, p:Graphene.Point3D) -> float """
        return 0.0

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> origin:Graphene.Point3D """
        pass

    def get_position_at(self, t): # real signature unknown; restored from __doc__
        """ get_position_at(self, t:float) -> position:Graphene.Point3D """
        pass

    def init(self, origin=None, direction=None): # real signature unknown; restored from __doc__
        """ init(self, origin:Graphene.Point3D=None, direction:Graphene.Vec3=None) -> Graphene.Ray """
        pass

    def init_from_ray(self, src): # real signature unknown; restored from __doc__
        """ init_from_ray(self, src:Graphene.Ray) -> Graphene.Ray """
        pass

    def init_from_vec3(self, origin=None, direction=None): # real signature unknown; restored from __doc__
        """ init_from_vec3(self, origin:Graphene.Vec3=None, direction:Graphene.Vec3=None) -> Graphene.Ray """
        pass

    def intersects_box(self, b): # real signature unknown; restored from __doc__
        """ intersects_box(self, b:Graphene.Box) -> bool """
        return False

    def intersects_sphere(self, s): # real signature unknown; restored from __doc__
        """ intersects_sphere(self, s:Graphene.Sphere) -> bool """
        return False

    def intersects_triangle(self, t): # real signature unknown; restored from __doc__
        """ intersects_triangle(self, t:Graphene.Triangle) -> bool """
        return False

    def intersect_box(self, b): # real signature unknown; restored from __doc__
        """ intersect_box(self, b:Graphene.Box) -> Graphene.RayIntersectionKind, t_out:float """
        pass

    def intersect_sphere(self, s): # real signature unknown; restored from __doc__
        """ intersect_sphere(self, s:Graphene.Sphere) -> Graphene.RayIntersectionKind, t_out:float """
        pass

    def intersect_triangle(self, t): # real signature unknown; restored from __doc__
        """ intersect_triangle(self, t:Graphene.Triangle) -> Graphene.RayIntersectionKind, t_out:float """
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

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Ray), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneRay (94782570985952)>, '__dict__': <attribute '__dict__' of 'Ray' objects>, '__weakref__': <attribute '__weakref__' of 'Ray' objects>, '__doc__': None, 'origin': <property object at 0x7fa3ecc8c540>, 'direction': <property object at 0x7fa3ecc8c630>, 'alloc': gi.FunctionInfo(alloc), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_closest_point_to_point': gi.FunctionInfo(get_closest_point_to_point), 'get_direction': gi.FunctionInfo(get_direction), 'get_distance_to_plane': gi.FunctionInfo(get_distance_to_plane), 'get_distance_to_point': gi.FunctionInfo(get_distance_to_point), 'get_origin': gi.FunctionInfo(get_origin), 'get_position_at': gi.FunctionInfo(get_position_at), 'init': gi.FunctionInfo(init), 'init_from_ray': gi.FunctionInfo(init_from_ray), 'init_from_vec3': gi.FunctionInfo(init_from_vec3), 'intersect_box': gi.FunctionInfo(intersect_box), 'intersect_sphere': gi.FunctionInfo(intersect_sphere), 'intersect_triangle': gi.FunctionInfo(intersect_triangle), 'intersects_box': gi.FunctionInfo(intersects_box), 'intersects_sphere': gi.FunctionInfo(intersects_sphere), 'intersects_triangle': gi.FunctionInfo(intersects_triangle)})"
    __gtype__ = None # (!) real value is '<GType GrapheneRay (94782570985952)>'
    __info__ = StructInfo(Ray)


class RayIntersectionKind(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ENTER = 1
    LEAVE = 2
    NONE = 0
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Graphene', '__dict__': <attribute '__dict__' of 'RayIntersectionKind' objects>, '__doc__': None, '__gtype__': <GType PyGrapheneRayIntersectionKind (94782570775552)>, '__enum_values__': {0: <enum GRAPHENE_RAY_INTERSECTION_KIND_NONE of type Graphene.RayIntersectionKind>, 1: <enum GRAPHENE_RAY_INTERSECTION_KIND_ENTER of type Graphene.RayIntersectionKind>, 2: <enum GRAPHENE_RAY_INTERSECTION_KIND_LEAVE of type Graphene.RayIntersectionKind>}, '__info__': gi.EnumInfo(RayIntersectionKind), 'NONE': <enum GRAPHENE_RAY_INTERSECTION_KIND_NONE of type Graphene.RayIntersectionKind>, 'ENTER': <enum GRAPHENE_RAY_INTERSECTION_KIND_ENTER of type Graphene.RayIntersectionKind>, 'LEAVE': <enum GRAPHENE_RAY_INTERSECTION_KIND_LEAVE of type Graphene.RayIntersectionKind>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is '<GType PyGrapheneRayIntersectionKind (94782570775552)>'
    __info__ = gi.EnumInfo(RayIntersectionKind)


class Rect(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Rect()
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Rect """
        pass

    def contains_point(self, p): # real signature unknown; restored from __doc__
        """ contains_point(self, p:Graphene.Point) -> bool """
        return False

    def contains_rect(self, b): # real signature unknown; restored from __doc__
        """ contains_rect(self, b:Graphene.Rect) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Rect) -> bool """
        return False

    def expand(self, p): # real signature unknown; restored from __doc__
        """ expand(self, p:Graphene.Point) -> res:Graphene.Rect """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_area(self): # real signature unknown; restored from __doc__
        """ get_area(self) -> float """
        return 0.0

    def get_bottom_left(self): # real signature unknown; restored from __doc__
        """ get_bottom_left(self) -> p:Graphene.Point """
        pass

    def get_bottom_right(self): # real signature unknown; restored from __doc__
        """ get_bottom_right(self) -> p:Graphene.Point """
        pass

    def get_center(self): # real signature unknown; restored from __doc__
        """ get_center(self) -> p:Graphene.Point """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> float """
        return 0.0

    def get_top_left(self): # real signature unknown; restored from __doc__
        """ get_top_left(self) -> p:Graphene.Point """
        pass

    def get_top_right(self): # real signature unknown; restored from __doc__
        """ get_top_right(self) -> p:Graphene.Point """
        pass

    def get_vertices(self): # real signature unknown; restored from __doc__
        """ get_vertices(self) -> vertices:list """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> float """
        return 0.0

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def init(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float, width:float, height:float) -> Graphene.Rect """
        pass

    def init_from_rect(self, src): # real signature unknown; restored from __doc__
        """ init_from_rect(self, src:Graphene.Rect) -> Graphene.Rect """
        pass

    def inset(self, d_x, d_y): # real signature unknown; restored from __doc__
        """ inset(self, d_x:float, d_y:float) -> Graphene.Rect """
        pass

    def inset_r(self, d_x, d_y): # real signature unknown; restored from __doc__
        """ inset_r(self, d_x:float, d_y:float) -> res:Graphene.Rect """
        pass

    def interpolate(self, b, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, b:Graphene.Rect, factor:float) -> res:Graphene.Rect """
        pass

    def intersection(self, b): # real signature unknown; restored from __doc__
        """ intersection(self, b:Graphene.Rect) -> bool, res:Graphene.Rect """
        return False

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> Graphene.Rect """
        pass

    def normalize_r(self): # real signature unknown; restored from __doc__
        """ normalize_r(self) -> res:Graphene.Rect """
        pass

    def offset(self, d_x, d_y): # real signature unknown; restored from __doc__
        """ offset(self, d_x:float, d_y:float) -> Graphene.Rect """
        pass

    def offset_r(self, d_x, d_y): # real signature unknown; restored from __doc__
        """ offset_r(self, d_x:float, d_y:float) -> res:Graphene.Rect """
        pass

    def round(self): # real signature unknown; restored from __doc__
        """ round(self) -> res:Graphene.Rect """
        pass

    def round_extents(self): # real signature unknown; restored from __doc__
        """ round_extents(self) -> res:Graphene.Rect """
        pass

    def round_to_pixel(self): # real signature unknown; restored from __doc__
        """ round_to_pixel(self) -> Graphene.Rect """
        pass

    def scale(self, s_h, s_v): # real signature unknown; restored from __doc__
        """ scale(self, s_h:float, s_v:float) -> res:Graphene.Rect """
        pass

    def union(self, b): # real signature unknown; restored from __doc__
        """ union(self, b:Graphene.Rect) -> res:Graphene.Rect """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Rect """
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

    origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Rect), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneRect (94782570688704)>, '__dict__': <attribute '__dict__' of 'Rect' objects>, '__weakref__': <attribute '__weakref__' of 'Rect' objects>, '__doc__': None, 'origin': <property object at 0x7fa3ecc8cb80>, 'size': <property object at 0x7fa3ecc8cc70>, 'contains_point': gi.FunctionInfo(contains_point), 'contains_rect': gi.FunctionInfo(contains_rect), 'equal': gi.FunctionInfo(equal), 'expand': gi.FunctionInfo(expand), 'free': gi.FunctionInfo(free), 'get_area': gi.FunctionInfo(get_area), 'get_bottom_left': gi.FunctionInfo(get_bottom_left), 'get_bottom_right': gi.FunctionInfo(get_bottom_right), 'get_center': gi.FunctionInfo(get_center), 'get_height': gi.FunctionInfo(get_height), 'get_top_left': gi.FunctionInfo(get_top_left), 'get_top_right': gi.FunctionInfo(get_top_right), 'get_vertices': gi.FunctionInfo(get_vertices), 'get_width': gi.FunctionInfo(get_width), 'get_x': gi.FunctionInfo(get_x), 'get_y': gi.FunctionInfo(get_y), 'init': gi.FunctionInfo(init), 'init_from_rect': gi.FunctionInfo(init_from_rect), 'inset': gi.FunctionInfo(inset), 'inset_r': gi.FunctionInfo(inset_r), 'interpolate': gi.FunctionInfo(interpolate), 'intersection': gi.FunctionInfo(intersection), 'normalize': gi.FunctionInfo(normalize), 'normalize_r': gi.FunctionInfo(normalize_r), 'offset': gi.FunctionInfo(offset), 'offset_r': gi.FunctionInfo(offset_r), 'round': gi.FunctionInfo(round), 'round_extents': gi.FunctionInfo(round_extents), 'round_to_pixel': gi.FunctionInfo(round_to_pixel), 'scale': gi.FunctionInfo(scale), 'union': gi.FunctionInfo(union), 'alloc': gi.FunctionInfo(alloc), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GrapheneRect (94782570688704)>'
    __info__ = StructInfo(Rect)


class Simd4F(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Simd4F()
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

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Simd4F), '__module__': 'gi.repository.Graphene', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Simd4F' objects>, '__weakref__': <attribute '__weakref__' of 'Simd4F' objects>, '__doc__': None, 'x': <property object at 0x7fa3ecc8ce00>, 'y': <property object at 0x7fa3ecc8cef0>, 'z': <property object at 0x7fa3ecc90040>, 'w': <property object at 0x7fa3ecc90130>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Simd4F)


class Simd4X4F(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Simd4X4F()
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

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Simd4X4F), '__module__': 'gi.repository.Graphene', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Simd4X4F' objects>, '__weakref__': <attribute '__weakref__' of 'Simd4X4F' objects>, '__doc__': None, 'x': <property object at 0x7fa3ecc902c0>, 'y': <property object at 0x7fa3ecc903b0>, 'z': <property object at 0x7fa3ecc904a0>, 'w': <property object at 0x7fa3ecc90590>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Simd4X4F)


class Size(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Size()
        alloc() -> Graphene.Size
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Size """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Size) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init(self, width, height): # real signature unknown; restored from __doc__
        """ init(self, width:float, height:float) -> Graphene.Size """
        pass

    def init_from_size(self, src): # real signature unknown; restored from __doc__
        """ init_from_size(self, src:Graphene.Size) -> Graphene.Size """
        pass

    def interpolate(self, b, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, b:Graphene.Size, factor:float) -> res:Graphene.Size """
        pass

    def scale(self, factor): # real signature unknown; restored from __doc__
        """ scale(self, factor:float) -> res:Graphene.Size """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Size """
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

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Size), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneSize (94782570688816)>, '__dict__': <attribute '__dict__' of 'Size' objects>, '__weakref__': <attribute '__weakref__' of 'Size' objects>, '__doc__': None, 'width': <property object at 0x7fa3ecc906d0>, 'height': <property object at 0x7fa3ecc907c0>, 'alloc': gi.FunctionInfo(alloc), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'init': gi.FunctionInfo(init), 'init_from_size': gi.FunctionInfo(init_from_size), 'interpolate': gi.FunctionInfo(interpolate), 'scale': gi.FunctionInfo(scale), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GrapheneSize (94782570688816)>'
    __info__ = StructInfo(Size)


class Sphere(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Sphere()
        alloc() -> Graphene.Sphere
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Sphere """
        pass

    def contains_point(self, point): # real signature unknown; restored from __doc__
        """ contains_point(self, point:Graphene.Point3D) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def distance(self, point): # real signature unknown; restored from __doc__
        """ distance(self, point:Graphene.Point3D) -> float """
        return 0.0

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Sphere) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_bounding_box(self): # real signature unknown; restored from __doc__
        """ get_bounding_box(self) -> box:Graphene.Box """
        pass

    def get_center(self): # real signature unknown; restored from __doc__
        """ get_center(self) -> center:Graphene.Point3D """
        pass

    def get_radius(self): # real signature unknown; restored from __doc__
        """ get_radius(self) -> float """
        return 0.0

    def init(self, center=None, radius): # real signature unknown; restored from __doc__
        """ init(self, center:Graphene.Point3D=None, radius:float) -> Graphene.Sphere """
        pass

    def init_from_points(self, points, center=None): # real signature unknown; restored from __doc__
        """ init_from_points(self, points:list, center:Graphene.Point3D=None) -> Graphene.Sphere """
        pass

    def init_from_vectors(self, vectors, center=None): # real signature unknown; restored from __doc__
        """ init_from_vectors(self, vectors:list, center:Graphene.Point3D=None) -> Graphene.Sphere """
        pass

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def translate(self, point): # real signature unknown; restored from __doc__
        """ translate(self, point:Graphene.Point3D) -> res:Graphene.Sphere """
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

    center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Sphere), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneSphere (94782571062432)>, '__dict__': <attribute '__dict__' of 'Sphere' objects>, '__weakref__': <attribute '__weakref__' of 'Sphere' objects>, '__doc__': None, 'center': <property object at 0x7fa3ecc90950>, 'radius': <property object at 0x7fa3ecc90a40>, 'alloc': gi.FunctionInfo(alloc), 'contains_point': gi.FunctionInfo(contains_point), 'distance': gi.FunctionInfo(distance), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_bounding_box': gi.FunctionInfo(get_bounding_box), 'get_center': gi.FunctionInfo(get_center), 'get_radius': gi.FunctionInfo(get_radius), 'init': gi.FunctionInfo(init), 'init_from_points': gi.FunctionInfo(init_from_points), 'init_from_vectors': gi.FunctionInfo(init_from_vectors), 'is_empty': gi.FunctionInfo(is_empty), 'translate': gi.FunctionInfo(translate)})"
    __gtype__ = None # (!) real value is '<GType GrapheneSphere (94782571062432)>'
    __info__ = StructInfo(Sphere)


class Triangle(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Triangle()
        alloc() -> Graphene.Triangle
    """
    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Triangle """
        pass

    def contains_point(self, p): # real signature unknown; restored from __doc__
        """ contains_point(self, p:Graphene.Point3D) -> bool """
        return False

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:Graphene.Triangle) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_area(self): # real signature unknown; restored from __doc__
        """ get_area(self) -> float """
        return 0.0

    def get_barycoords(self, p=None): # real signature unknown; restored from __doc__
        """ get_barycoords(self, p:Graphene.Point3D=None) -> bool, res:Graphene.Vec2 """
        return False

    def get_bounding_box(self): # real signature unknown; restored from __doc__
        """ get_bounding_box(self) -> res:Graphene.Box """
        pass

    def get_midpoint(self): # real signature unknown; restored from __doc__
        """ get_midpoint(self) -> res:Graphene.Point3D """
        pass

    def get_normal(self): # real signature unknown; restored from __doc__
        """ get_normal(self) -> res:Graphene.Vec3 """
        pass

    def get_plane(self): # real signature unknown; restored from __doc__
        """ get_plane(self) -> res:Graphene.Plane """
        pass

    def get_points(self): # real signature unknown; restored from __doc__
        """ get_points(self) -> a:Graphene.Point3D, b:Graphene.Point3D, c:Graphene.Point3D """
        pass

    def get_uv(self, p=None, uv_a, uv_b, uv_c): # real signature unknown; restored from __doc__
        """ get_uv(self, p:Graphene.Point3D=None, uv_a:Graphene.Vec2, uv_b:Graphene.Vec2, uv_c:Graphene.Vec2) -> bool, res:Graphene.Vec2 """
        return False

    def get_vertices(self): # real signature unknown; restored from __doc__
        """ get_vertices(self) -> a:Graphene.Vec3, b:Graphene.Vec3, c:Graphene.Vec3 """
        pass

    def init_from_float(self, a, b, c): # real signature unknown; restored from __doc__
        """ init_from_float(self, a:list, b:list, c:list) -> Graphene.Triangle """
        pass

    def init_from_point3d(self, a=None, b=None, c=None): # real signature unknown; restored from __doc__
        """ init_from_point3d(self, a:Graphene.Point3D=None, b:Graphene.Point3D=None, c:Graphene.Point3D=None) -> Graphene.Triangle """
        pass

    def init_from_vec3(self, a=None, b=None, c=None): # real signature unknown; restored from __doc__
        """ init_from_vec3(self, a:Graphene.Vec3=None, b:Graphene.Vec3=None, c:Graphene.Vec3=None) -> Graphene.Triangle """
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

    a = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    b = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    c = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Triangle), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneTriangle (94782571071696)>, '__dict__': <attribute '__dict__' of 'Triangle' objects>, '__weakref__': <attribute '__weakref__' of 'Triangle' objects>, '__doc__': None, 'a': <property object at 0x7fa3ecc90c20>, 'b': <property object at 0x7fa3ecc90d10>, 'c': <property object at 0x7fa3ecc90e00>, 'alloc': gi.FunctionInfo(alloc), 'contains_point': gi.FunctionInfo(contains_point), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_area': gi.FunctionInfo(get_area), 'get_barycoords': gi.FunctionInfo(get_barycoords), 'get_bounding_box': gi.FunctionInfo(get_bounding_box), 'get_midpoint': gi.FunctionInfo(get_midpoint), 'get_normal': gi.FunctionInfo(get_normal), 'get_plane': gi.FunctionInfo(get_plane), 'get_points': gi.FunctionInfo(get_points), 'get_uv': gi.FunctionInfo(get_uv), 'get_vertices': gi.FunctionInfo(get_vertices), 'init_from_float': gi.FunctionInfo(init_from_float), 'init_from_point3d': gi.FunctionInfo(init_from_point3d), 'init_from_vec3': gi.FunctionInfo(init_from_vec3)})"
    __gtype__ = None # (!) real value is '<GType GrapheneTriangle (94782571071696)>'
    __info__ = StructInfo(Triangle)


class Vec2(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Vec2()
        alloc() -> Graphene.Vec2
    """
    def add(self, b): # real signature unknown; restored from __doc__
        """ add(self, b:Graphene.Vec2) -> res:Graphene.Vec2 """
        pass

    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Vec2 """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def divide(self, b): # real signature unknown; restored from __doc__
        """ divide(self, b:Graphene.Vec2) -> res:Graphene.Vec2 """
        pass

    def dot(self, b): # real signature unknown; restored from __doc__
        """ dot(self, b:Graphene.Vec2) -> float """
        return 0.0

    def equal(self, v2): # real signature unknown; restored from __doc__
        """ equal(self, v2:Graphene.Vec2) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def init(self, x, y): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float) -> Graphene.Vec2 """
        pass

    def init_from_float(self, src): # real signature unknown; restored from __doc__
        """ init_from_float(self, src:list) -> Graphene.Vec2 """
        pass

    def init_from_vec2(self, src): # real signature unknown; restored from __doc__
        """ init_from_vec2(self, src:Graphene.Vec2) -> Graphene.Vec2 """
        pass

    def interpolate(self, v2, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, v2:Graphene.Vec2, factor:float) -> res:Graphene.Vec2 """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def max(self, b): # real signature unknown; restored from __doc__
        """ max(self, b:Graphene.Vec2) -> res:Graphene.Vec2 """
        pass

    def min(self, b): # real signature unknown; restored from __doc__
        """ min(self, b:Graphene.Vec2) -> res:Graphene.Vec2 """
        pass

    def multiply(self, b): # real signature unknown; restored from __doc__
        """ multiply(self, b:Graphene.Vec2) -> res:Graphene.Vec2 """
        pass

    def near(self, v2, epsilon): # real signature unknown; restored from __doc__
        """ near(self, v2:Graphene.Vec2, epsilon:float) -> bool """
        return False

    def negate(self): # real signature unknown; restored from __doc__
        """ negate(self) -> res:Graphene.Vec2 """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> res:Graphene.Vec2 """
        pass

    def one(self): # real signature unknown; restored from __doc__
        """ one() -> Graphene.Vec2 """
        pass

    def scale(self, factor): # real signature unknown; restored from __doc__
        """ scale(self, factor:float) -> res:Graphene.Vec2 """
        pass

    def subtract(self, b): # real signature unknown; restored from __doc__
        """ subtract(self, b:Graphene.Vec2) -> res:Graphene.Vec2 """
        pass

    def to_float(self): # real signature unknown; restored from __doc__
        """ to_float(self) -> dest:list """
        pass

    def x_axis(self): # real signature unknown; restored from __doc__
        """ x_axis() -> Graphene.Vec2 """
        pass

    def y_axis(self): # real signature unknown; restored from __doc__
        """ y_axis() -> Graphene.Vec2 """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Vec2 """
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

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Vec2), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneVec2 (94782571087728)>, '__dict__': <attribute '__dict__' of 'Vec2' objects>, '__weakref__': <attribute '__weakref__' of 'Vec2' objects>, '__doc__': None, 'value': <property object at 0x7fa3ecc93040>, 'alloc': gi.FunctionInfo(alloc), 'add': gi.FunctionInfo(add), 'divide': gi.FunctionInfo(divide), 'dot': gi.FunctionInfo(dot), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_x': gi.FunctionInfo(get_x), 'get_y': gi.FunctionInfo(get_y), 'init': gi.FunctionInfo(init), 'init_from_float': gi.FunctionInfo(init_from_float), 'init_from_vec2': gi.FunctionInfo(init_from_vec2), 'interpolate': gi.FunctionInfo(interpolate), 'length': gi.FunctionInfo(length), 'max': gi.FunctionInfo(max), 'min': gi.FunctionInfo(min), 'multiply': gi.FunctionInfo(multiply), 'near': gi.FunctionInfo(near), 'negate': gi.FunctionInfo(negate), 'normalize': gi.FunctionInfo(normalize), 'scale': gi.FunctionInfo(scale), 'subtract': gi.FunctionInfo(subtract), 'to_float': gi.FunctionInfo(to_float), 'one': gi.FunctionInfo(one), 'x_axis': gi.FunctionInfo(x_axis), 'y_axis': gi.FunctionInfo(y_axis), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GrapheneVec2 (94782571087728)>'
    __info__ = StructInfo(Vec2)


class Vec3(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Vec3()
        alloc() -> Graphene.Vec3
    """
    def add(self, b): # real signature unknown; restored from __doc__
        """ add(self, b:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Vec3 """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def cross(self, b): # real signature unknown; restored from __doc__
        """ cross(self, b:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def divide(self, b): # real signature unknown; restored from __doc__
        """ divide(self, b:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def dot(self, b): # real signature unknown; restored from __doc__
        """ dot(self, b:Graphene.Vec3) -> float """
        return 0.0

    def equal(self, v2): # real signature unknown; restored from __doc__
        """ equal(self, v2:Graphene.Vec3) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_xy(self): # real signature unknown; restored from __doc__
        """ get_xy(self) -> res:Graphene.Vec2 """
        pass

    def get_xy0(self): # real signature unknown; restored from __doc__
        """ get_xy0(self) -> res:Graphene.Vec3 """
        pass

    def get_xyz0(self): # real signature unknown; restored from __doc__
        """ get_xyz0(self) -> res:Graphene.Vec4 """
        pass

    def get_xyz1(self): # real signature unknown; restored from __doc__
        """ get_xyz1(self) -> res:Graphene.Vec4 """
        pass

    def get_xyzw(self, w): # real signature unknown; restored from __doc__
        """ get_xyzw(self, w:float) -> res:Graphene.Vec4 """
        pass

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def get_z(self): # real signature unknown; restored from __doc__
        """ get_z(self) -> float """
        return 0.0

    def init(self, x, y, z): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float, z:float) -> Graphene.Vec3 """
        pass

    def init_from_float(self, src): # real signature unknown; restored from __doc__
        """ init_from_float(self, src:list) -> Graphene.Vec3 """
        pass

    def init_from_vec3(self, src): # real signature unknown; restored from __doc__
        """ init_from_vec3(self, src:Graphene.Vec3) -> Graphene.Vec3 """
        pass

    def interpolate(self, v2, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, v2:Graphene.Vec3, factor:float) -> res:Graphene.Vec3 """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def max(self, b): # real signature unknown; restored from __doc__
        """ max(self, b:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def min(self, b): # real signature unknown; restored from __doc__
        """ min(self, b:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def multiply(self, b): # real signature unknown; restored from __doc__
        """ multiply(self, b:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def near(self, v2, epsilon): # real signature unknown; restored from __doc__
        """ near(self, v2:Graphene.Vec3, epsilon:float) -> bool """
        return False

    def negate(self): # real signature unknown; restored from __doc__
        """ negate(self) -> res:Graphene.Vec3 """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> res:Graphene.Vec3 """
        pass

    def one(self): # real signature unknown; restored from __doc__
        """ one() -> Graphene.Vec3 """
        pass

    def scale(self, factor): # real signature unknown; restored from __doc__
        """ scale(self, factor:float) -> res:Graphene.Vec3 """
        pass

    def subtract(self, b): # real signature unknown; restored from __doc__
        """ subtract(self, b:Graphene.Vec3) -> res:Graphene.Vec3 """
        pass

    def to_float(self): # real signature unknown; restored from __doc__
        """ to_float(self) -> dest:list """
        pass

    def x_axis(self): # real signature unknown; restored from __doc__
        """ x_axis() -> Graphene.Vec3 """
        pass

    def y_axis(self): # real signature unknown; restored from __doc__
        """ y_axis() -> Graphene.Vec3 """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Vec3 """
        pass

    def z_axis(self): # real signature unknown; restored from __doc__
        """ z_axis() -> Graphene.Vec3 """
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

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Vec3), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneVec3 (94782571062592)>, '__dict__': <attribute '__dict__' of 'Vec3' objects>, '__weakref__': <attribute '__weakref__' of 'Vec3' objects>, '__doc__': None, 'value': <property object at 0x7fa3ecc931d0>, 'alloc': gi.FunctionInfo(alloc), 'add': gi.FunctionInfo(add), 'cross': gi.FunctionInfo(cross), 'divide': gi.FunctionInfo(divide), 'dot': gi.FunctionInfo(dot), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_x': gi.FunctionInfo(get_x), 'get_xy': gi.FunctionInfo(get_xy), 'get_xy0': gi.FunctionInfo(get_xy0), 'get_xyz0': gi.FunctionInfo(get_xyz0), 'get_xyz1': gi.FunctionInfo(get_xyz1), 'get_xyzw': gi.FunctionInfo(get_xyzw), 'get_y': gi.FunctionInfo(get_y), 'get_z': gi.FunctionInfo(get_z), 'init': gi.FunctionInfo(init), 'init_from_float': gi.FunctionInfo(init_from_float), 'init_from_vec3': gi.FunctionInfo(init_from_vec3), 'interpolate': gi.FunctionInfo(interpolate), 'length': gi.FunctionInfo(length), 'max': gi.FunctionInfo(max), 'min': gi.FunctionInfo(min), 'multiply': gi.FunctionInfo(multiply), 'near': gi.FunctionInfo(near), 'negate': gi.FunctionInfo(negate), 'normalize': gi.FunctionInfo(normalize), 'scale': gi.FunctionInfo(scale), 'subtract': gi.FunctionInfo(subtract), 'to_float': gi.FunctionInfo(to_float), 'one': gi.FunctionInfo(one), 'x_axis': gi.FunctionInfo(x_axis), 'y_axis': gi.FunctionInfo(y_axis), 'z_axis': gi.FunctionInfo(z_axis), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GrapheneVec3 (94782571062592)>'
    __info__ = StructInfo(Vec3)


class Vec4(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Vec4()
        alloc() -> Graphene.Vec4
    """
    def add(self, b): # real signature unknown; restored from __doc__
        """ add(self, b:Graphene.Vec4) -> res:Graphene.Vec4 """
        pass

    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Graphene.Vec4 """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def divide(self, b): # real signature unknown; restored from __doc__
        """ divide(self, b:Graphene.Vec4) -> res:Graphene.Vec4 """
        pass

    def dot(self, b): # real signature unknown; restored from __doc__
        """ dot(self, b:Graphene.Vec4) -> float """
        return 0.0

    def equal(self, v2): # real signature unknown; restored from __doc__
        """ equal(self, v2:Graphene.Vec4) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_w(self): # real signature unknown; restored from __doc__
        """ get_w(self) -> float """
        return 0.0

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> float """
        return 0.0

    def get_xy(self): # real signature unknown; restored from __doc__
        """ get_xy(self) -> res:Graphene.Vec2 """
        pass

    def get_xyz(self): # real signature unknown; restored from __doc__
        """ get_xyz(self) -> res:Graphene.Vec3 """
        pass

    def get_y(self): # real signature unknown; restored from __doc__
        """ get_y(self) -> float """
        return 0.0

    def get_z(self): # real signature unknown; restored from __doc__
        """ get_z(self) -> float """
        return 0.0

    def init(self, x, y, z, w): # real signature unknown; restored from __doc__
        """ init(self, x:float, y:float, z:float, w:float) -> Graphene.Vec4 """
        pass

    def init_from_float(self, src): # real signature unknown; restored from __doc__
        """ init_from_float(self, src:list) -> Graphene.Vec4 """
        pass

    def init_from_vec2(self, src, z, w): # real signature unknown; restored from __doc__
        """ init_from_vec2(self, src:Graphene.Vec2, z:float, w:float) -> Graphene.Vec4 """
        pass

    def init_from_vec3(self, src, w): # real signature unknown; restored from __doc__
        """ init_from_vec3(self, src:Graphene.Vec3, w:float) -> Graphene.Vec4 """
        pass

    def init_from_vec4(self, src): # real signature unknown; restored from __doc__
        """ init_from_vec4(self, src:Graphene.Vec4) -> Graphene.Vec4 """
        pass

    def interpolate(self, v2, factor): # real signature unknown; restored from __doc__
        """ interpolate(self, v2:Graphene.Vec4, factor:float) -> res:Graphene.Vec4 """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> float """
        return 0.0

    def max(self, b): # real signature unknown; restored from __doc__
        """ max(self, b:Graphene.Vec4) -> res:Graphene.Vec4 """
        pass

    def min(self, b): # real signature unknown; restored from __doc__
        """ min(self, b:Graphene.Vec4) -> res:Graphene.Vec4 """
        pass

    def multiply(self, b): # real signature unknown; restored from __doc__
        """ multiply(self, b:Graphene.Vec4) -> res:Graphene.Vec4 """
        pass

    def near(self, v2, epsilon): # real signature unknown; restored from __doc__
        """ near(self, v2:Graphene.Vec4, epsilon:float) -> bool """
        return False

    def negate(self): # real signature unknown; restored from __doc__
        """ negate(self) -> res:Graphene.Vec4 """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> res:Graphene.Vec4 """
        pass

    def one(self): # real signature unknown; restored from __doc__
        """ one() -> Graphene.Vec4 """
        pass

    def scale(self, factor): # real signature unknown; restored from __doc__
        """ scale(self, factor:float) -> res:Graphene.Vec4 """
        pass

    def subtract(self, b): # real signature unknown; restored from __doc__
        """ subtract(self, b:Graphene.Vec4) -> res:Graphene.Vec4 """
        pass

    def to_float(self): # real signature unknown; restored from __doc__
        """ to_float(self) -> dest:list """
        pass

    def w_axis(self): # real signature unknown; restored from __doc__
        """ w_axis() -> Graphene.Vec4 """
        pass

    def x_axis(self): # real signature unknown; restored from __doc__
        """ x_axis() -> Graphene.Vec4 """
        pass

    def y_axis(self): # real signature unknown; restored from __doc__
        """ y_axis() -> Graphene.Vec4 """
        pass

    def zero(self): # real signature unknown; restored from __doc__
        """ zero() -> Graphene.Vec4 """
        pass

    def z_axis(self): # real signature unknown; restored from __doc__
        """ z_axis() -> Graphene.Vec4 """
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

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Vec4), '__module__': 'gi.repository.Graphene', '__gtype__': <GType GrapheneVec4 (94782571256704)>, '__dict__': <attribute '__dict__' of 'Vec4' objects>, '__weakref__': <attribute '__weakref__' of 'Vec4' objects>, '__doc__': None, 'value': <property object at 0x7fa3ecc93360>, 'alloc': gi.FunctionInfo(alloc), 'add': gi.FunctionInfo(add), 'divide': gi.FunctionInfo(divide), 'dot': gi.FunctionInfo(dot), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'get_w': gi.FunctionInfo(get_w), 'get_x': gi.FunctionInfo(get_x), 'get_xy': gi.FunctionInfo(get_xy), 'get_xyz': gi.FunctionInfo(get_xyz), 'get_y': gi.FunctionInfo(get_y), 'get_z': gi.FunctionInfo(get_z), 'init': gi.FunctionInfo(init), 'init_from_float': gi.FunctionInfo(init_from_float), 'init_from_vec2': gi.FunctionInfo(init_from_vec2), 'init_from_vec3': gi.FunctionInfo(init_from_vec3), 'init_from_vec4': gi.FunctionInfo(init_from_vec4), 'interpolate': gi.FunctionInfo(interpolate), 'length': gi.FunctionInfo(length), 'max': gi.FunctionInfo(max), 'min': gi.FunctionInfo(min), 'multiply': gi.FunctionInfo(multiply), 'near': gi.FunctionInfo(near), 'negate': gi.FunctionInfo(negate), 'normalize': gi.FunctionInfo(normalize), 'scale': gi.FunctionInfo(scale), 'subtract': gi.FunctionInfo(subtract), 'to_float': gi.FunctionInfo(to_float), 'one': gi.FunctionInfo(one), 'w_axis': gi.FunctionInfo(w_axis), 'x_axis': gi.FunctionInfo(x_axis), 'y_axis': gi.FunctionInfo(y_axis), 'z_axis': gi.FunctionInfo(z_axis), 'zero': gi.FunctionInfo(zero)})"
    __gtype__ = None # (!) real value is '<GType GrapheneVec4 (94782571256704)>'
    __info__ = StructInfo(Vec4)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7fa3ece861f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7fa3ece86280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7fa3ece86310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7fa3ece863a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fa3edac2d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Graphene-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Graphene', loader=<gi.importer.DynamicImporter object at 0x7fa3edac2d00>)"

