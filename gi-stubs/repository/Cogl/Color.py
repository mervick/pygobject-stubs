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


class Color(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Color()
        new() -> Cogl.Color
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Cogl.Color """
        pass

    def equal(self, v1=None, v2=None): # real signature unknown; restored from __doc__
        """ equal(v1=None, v2=None) -> int """
        return 0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_alpha_byte(self): # real signature unknown; restored from __doc__
        """ get_alpha_byte(self) -> int """
        return 0

    def get_alpha_float(self): # real signature unknown; restored from __doc__
        """ get_alpha_float(self) -> float """
        return 0.0

    def get_blue(self): # real signature unknown; restored from __doc__
        """ get_blue(self) -> float """
        return 0.0

    def get_blue_byte(self): # real signature unknown; restored from __doc__
        """ get_blue_byte(self) -> int """
        return 0

    def get_blue_float(self): # real signature unknown; restored from __doc__
        """ get_blue_float(self) -> float """
        return 0.0

    def get_green(self): # real signature unknown; restored from __doc__
        """ get_green(self) -> float """
        return 0.0

    def get_green_byte(self): # real signature unknown; restored from __doc__
        """ get_green_byte(self) -> int """
        return 0

    def get_green_float(self): # real signature unknown; restored from __doc__
        """ get_green_float(self) -> float """
        return 0.0

    def get_red(self): # real signature unknown; restored from __doc__
        """ get_red(self) -> float """
        return 0.0

    def get_red_byte(self): # real signature unknown; restored from __doc__
        """ get_red_byte(self) -> int """
        return 0

    def get_red_float(self): # real signature unknown; restored from __doc__
        """ get_red_float(self) -> float """
        return 0.0

    def init_from_4f(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ init_from_4f(self, red:float, green:float, blue:float, alpha:float) """
        pass

    def init_from_4fv(self, color_array): # real signature unknown; restored from __doc__
        """ init_from_4fv(self, color_array:float) """
        pass

    def init_from_4ub(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ init_from_4ub(self, red:int, green:int, blue:int, alpha:int) """
        pass

    def init_from_hsl(self, hue, saturation, luminance): # real signature unknown; restored from __doc__
        """ init_from_hsl(hue:float, saturation:float, luminance:float) -> color:Cogl.Color """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Cogl.Color """
        pass

    def premultiply(self): # real signature unknown; restored from __doc__
        """ premultiply(self) """
        pass

    def set_alpha(self, alpha): # real signature unknown; restored from __doc__
        """ set_alpha(self, alpha:float) """
        pass

    def set_alpha_byte(self, alpha): # real signature unknown; restored from __doc__
        """ set_alpha_byte(self, alpha:int) """
        pass

    def set_alpha_float(self, alpha): # real signature unknown; restored from __doc__
        """ set_alpha_float(self, alpha:float) """
        pass

    def set_blue(self, blue): # real signature unknown; restored from __doc__
        """ set_blue(self, blue:float) """
        pass

    def set_blue_byte(self, blue): # real signature unknown; restored from __doc__
        """ set_blue_byte(self, blue:int) """
        pass

    def set_blue_float(self, blue): # real signature unknown; restored from __doc__
        """ set_blue_float(self, blue:float) """
        pass

    def set_from_4f(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ set_from_4f(self, red:float, green:float, blue:float, alpha:float) """
        pass

    def set_from_4ub(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ set_from_4ub(self, red:int, green:int, blue:int, alpha:int) """
        pass

    def set_green(self, green): # real signature unknown; restored from __doc__
        """ set_green(self, green:float) """
        pass

    def set_green_byte(self, green): # real signature unknown; restored from __doc__
        """ set_green_byte(self, green:int) """
        pass

    def set_green_float(self, green): # real signature unknown; restored from __doc__
        """ set_green_float(self, green:float) """
        pass

    def set_red(self, red): # real signature unknown; restored from __doc__
        """ set_red(self, red:float) """
        pass

    def set_red_byte(self, red): # real signature unknown; restored from __doc__
        """ set_red_byte(self, red:int) """
        pass

    def set_red_float(self, red): # real signature unknown; restored from __doc__
        """ set_red_float(self, red:float) """
        pass

    def to_hsl(self): # real signature unknown; restored from __doc__
        """ to_hsl(self) -> hue:float, saturation:float, luminance:float """
        pass

    def unpremultiply(self): # real signature unknown; restored from __doc__
        """ unpremultiply(self) """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Cogl.Color """
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

    private_member_alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_padding2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_member_red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Color), '__module__': 'gi.repository.Cogl', '__gtype__': <GType CoglColor (93970931931504)>, '__dict__': <attribute '__dict__' of 'Color' objects>, '__weakref__': <attribute '__weakref__' of 'Color' objects>, '__doc__': None, 'private_member_red': <property object at 0x7fba8900dbd0>, 'private_member_green': <property object at 0x7fba8900dc70>, 'private_member_blue': <property object at 0x7fba8900dd10>, 'private_member_alpha': <property object at 0x7fba8900ddb0>, 'private_member_padding0': <property object at 0x7fba8900def0>, 'private_member_padding1': <property object at 0x7fba89016090>, 'private_member_padding2': <property object at 0x7fba890161d0>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_alpha': gi.FunctionInfo(get_alpha), 'get_alpha_byte': gi.FunctionInfo(get_alpha_byte), 'get_alpha_float': gi.FunctionInfo(get_alpha_float), 'get_blue': gi.FunctionInfo(get_blue), 'get_blue_byte': gi.FunctionInfo(get_blue_byte), 'get_blue_float': gi.FunctionInfo(get_blue_float), 'get_green': gi.FunctionInfo(get_green), 'get_green_byte': gi.FunctionInfo(get_green_byte), 'get_green_float': gi.FunctionInfo(get_green_float), 'get_red': gi.FunctionInfo(get_red), 'get_red_byte': gi.FunctionInfo(get_red_byte), 'get_red_float': gi.FunctionInfo(get_red_float), 'init_from_4f': gi.FunctionInfo(init_from_4f), 'init_from_4fv': gi.FunctionInfo(init_from_4fv), 'init_from_4ub': gi.FunctionInfo(init_from_4ub), 'premultiply': gi.FunctionInfo(premultiply), 'set_alpha': gi.FunctionInfo(set_alpha), 'set_alpha_byte': gi.FunctionInfo(set_alpha_byte), 'set_alpha_float': gi.FunctionInfo(set_alpha_float), 'set_blue': gi.FunctionInfo(set_blue), 'set_blue_byte': gi.FunctionInfo(set_blue_byte), 'set_blue_float': gi.FunctionInfo(set_blue_float), 'set_from_4f': gi.FunctionInfo(set_from_4f), 'set_from_4ub': gi.FunctionInfo(set_from_4ub), 'set_green': gi.FunctionInfo(set_green), 'set_green_byte': gi.FunctionInfo(set_green_byte), 'set_green_float': gi.FunctionInfo(set_green_float), 'set_red': gi.FunctionInfo(set_red), 'set_red_byte': gi.FunctionInfo(set_red_byte), 'set_red_float': gi.FunctionInfo(set_red_float), 'to_hsl': gi.FunctionInfo(to_hsl), 'unpremultiply': gi.FunctionInfo(unpremultiply), 'equal': gi.FunctionInfo(equal), 'init_from_hsl': gi.FunctionInfo(init_from_hsl), '__new__': <staticmethod object at 0x7fba89013430>, '__init__': <function nothing at 0x7fba8921cee0>})"
    __gtype__ = None # (!) real value is '<GType CoglColor (93970931931504)>'
    __info__ = StructInfo(Color)


