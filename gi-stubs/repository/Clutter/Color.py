# encoding: utf-8
# module gi.repository.Clutter
# from /usr/lib64/girepository-1.0/Clutter-1.0.typelib
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
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class Color(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Color()
        alloc() -> Clutter.Color
        new(red:int, green:int, blue:int, alpha:int) -> Clutter.Color
    """
    def add(self, b): # real signature unknown; restored from __doc__
        """ add(self, b:Clutter.Color) -> result:Clutter.Color """
        pass

    def alloc(self): # real signature unknown; restored from __doc__
        """ alloc() -> Clutter.Color """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Clutter.Color """
        pass

    def darken(self): # real signature unknown; restored from __doc__
        """ darken(self) -> result:Clutter.Color """
        pass

    def equal(self, v2): # real signature unknown; restored from __doc__
        """ equal(self, v2:Clutter.Color) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_hls(self, hue, luminance, saturation): # real signature unknown; restored from __doc__
        """ from_hls(hue:float, luminance:float, saturation:float) -> color:Clutter.Color """
        pass

    def from_pixel(self, pixel): # real signature unknown; restored from __doc__
        """ from_pixel(pixel:int) -> color:Clutter.Color """
        pass

    def from_string(self, p_str): # real signature unknown; restored from __doc__
        """ from_string(str:str) -> bool, color:Clutter.Color """
        return False

    def get_static(self, color): # real signature unknown; restored from __doc__
        """ get_static(color:Clutter.StaticColor) -> Clutter.Color """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def init(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ init(self, red:int, green:int, blue:int, alpha:int) -> Clutter.Color """
        pass

    def interpolate(self, final, progress): # real signature unknown; restored from __doc__
        """ interpolate(self, final:Clutter.Color, progress:float) -> result:Clutter.Color """
        pass

    def lighten(self): # real signature unknown; restored from __doc__
        """ lighten(self) -> result:Clutter.Color """
        pass

    def new(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ new(red:int, green:int, blue:int, alpha:int) -> Clutter.Color """
        pass

    def shade(self, factor): # real signature unknown; restored from __doc__
        """ shade(self, factor:float) -> result:Clutter.Color """
        pass

    def subtract(self, b): # real signature unknown; restored from __doc__
        """ subtract(self, b:Clutter.Color) -> result:Clutter.Color """
        pass

    def to_hls(self): # real signature unknown; restored from __doc__
        """ to_hls(self) -> hue:float, luminance:float, saturation:float """
        pass

    def to_pixel(self): # real signature unknown; restored from __doc__
        """ to_pixel(self) -> int """
        return 0

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Color), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterColor (94911696074912)>, '__dict__': <attribute '__dict__' of 'Color' objects>, '__weakref__': <attribute '__weakref__' of 'Color' objects>, '__doc__': None, 'red': <property object at 0x7f5413c9a950>, 'green': <property object at 0x7f5413c9aa40>, 'blue': <property object at 0x7f5413c9ab30>, 'alpha': <property object at 0x7f5413c9ac20>, 'alloc': gi.FunctionInfo(alloc), 'new': gi.FunctionInfo(new), 'add': gi.FunctionInfo(add), 'copy': gi.FunctionInfo(copy), 'darken': gi.FunctionInfo(darken), 'equal': gi.FunctionInfo(equal), 'free': gi.FunctionInfo(free), 'hash': gi.FunctionInfo(hash), 'init': gi.FunctionInfo(init), 'interpolate': gi.FunctionInfo(interpolate), 'lighten': gi.FunctionInfo(lighten), 'shade': gi.FunctionInfo(shade), 'subtract': gi.FunctionInfo(subtract), 'to_hls': gi.FunctionInfo(to_hls), 'to_pixel': gi.FunctionInfo(to_pixel), 'to_string': gi.FunctionInfo(to_string), 'from_hls': gi.FunctionInfo(from_hls), 'from_pixel': gi.FunctionInfo(from_pixel), 'from_string': gi.FunctionInfo(from_string), 'get_static': gi.FunctionInfo(get_static)})"
    __gtype__ = None # (!) real value is '<GType ClutterColor (94911696074912)>'
    __info__ = StructInfo(Color)


