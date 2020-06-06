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


class Units(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Units()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Clutter.Units """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_cm(self, cm): # real signature unknown; restored from __doc__
        """ from_cm(cm:float) -> units:Clutter.Units """
        pass

    def from_em(self, em): # real signature unknown; restored from __doc__
        """ from_em(em:float) -> units:Clutter.Units """
        pass

    def from_em_for_font(self, font_name=None, em): # real signature unknown; restored from __doc__
        """ from_em_for_font(font_name:str=None, em:float) -> units:Clutter.Units """
        pass

    def from_mm(self, mm): # real signature unknown; restored from __doc__
        """ from_mm(mm:float) -> units:Clutter.Units """
        pass

    def from_pixels(self, px): # real signature unknown; restored from __doc__
        """ from_pixels(px:int) -> units:Clutter.Units """
        pass

    def from_pt(self, pt): # real signature unknown; restored from __doc__
        """ from_pt(pt:float) -> units:Clutter.Units """
        pass

    def from_string(self, p_str): # real signature unknown; restored from __doc__
        """ from_string(str:str) -> bool, units:Clutter.Units """
        return False

    def get_unit_type(self): # real signature unknown; restored from __doc__
        """ get_unit_type(self) -> Clutter.UnitType """
        pass

    def get_unit_value(self): # real signature unknown; restored from __doc__
        """ get_unit_value(self) -> float """
        return 0.0

    def to_pixels(self): # real signature unknown; restored from __doc__
        """ to_pixels(self) -> float """
        return 0.0

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

    pixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixels_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __padding_1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __padding_2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Units), '__module__': 'gi.repository.Clutter', '__gtype__': <GType ClutterUnits (94911696241744)>, '__dict__': <attribute '__dict__' of 'Units' objects>, '__weakref__': <attribute '__weakref__' of 'Units' objects>, '__doc__': None, 'unit_type': <property object at 0x7f54134ed950>, 'value': <property object at 0x7f54134eda40>, 'pixels': <property object at 0x7f54134edb30>, 'pixels_set': <property object at 0x7f54134edc20>, 'serial': <property object at 0x7f54134edd10>, '__padding_1': <property object at 0x7f54134ede00>, '__padding_2': <property object at 0x7f54134edef0>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_unit_type': gi.FunctionInfo(get_unit_type), 'get_unit_value': gi.FunctionInfo(get_unit_value), 'to_pixels': gi.FunctionInfo(to_pixels), 'to_string': gi.FunctionInfo(to_string), 'from_cm': gi.FunctionInfo(from_cm), 'from_em': gi.FunctionInfo(from_em), 'from_em_for_font': gi.FunctionInfo(from_em_for_font), 'from_mm': gi.FunctionInfo(from_mm), 'from_pixels': gi.FunctionInfo(from_pixels), 'from_pt': gi.FunctionInfo(from_pt), 'from_string': gi.FunctionInfo(from_string)})"
    __gtype__ = None # (!) real value is '<GType ClutterUnits (94911696241744)>'
    __info__ = StructInfo(Units)


