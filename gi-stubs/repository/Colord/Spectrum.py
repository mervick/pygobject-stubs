# encoding: utf-8
# module gi.repository.Colord
# from /usr/lib64/girepository-1.0/Colord-1.0.typelib
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
import gobject as __gobject


class Spectrum(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Colord.Spectrum
        planckian_new(temperature:float) -> Colord.Spectrum
        planckian_new_full(temperature:float, start:float, end:float, resolution:float) -> Colord.Spectrum
        sized_new(reserved_size:int) -> Colord.Spectrum
    """
    def add_value(self, data): # real signature unknown; restored from __doc__
        """ add_value(self, data:float) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Colord.Spectrum """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> list """
        return []

    def get_end(self): # real signature unknown; restored from __doc__
        """ get_end(self) -> float """
        return 0.0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_norm(self): # real signature unknown; restored from __doc__
        """ get_norm(self) -> float """
        return 0.0

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> float """
        return 0.0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_start(self): # real signature unknown; restored from __doc__
        """ get_start(self) -> float """
        return 0.0

    def get_value(self, idx): # real signature unknown; restored from __doc__
        """ get_value(self, idx:int) -> float """
        return 0.0

    def get_value_for_nm(self, wavelength): # real signature unknown; restored from __doc__
        """ get_value_for_nm(self, wavelength:float) -> float """
        return 0.0

    def get_value_max(self): # real signature unknown; restored from __doc__
        """ get_value_max(self) -> float """
        return 0.0

    def get_value_min(self): # real signature unknown; restored from __doc__
        """ get_value_min(self) -> float """
        return 0.0

    def get_value_raw(self, idx): # real signature unknown; restored from __doc__
        """ get_value_raw(self, idx:int) -> float """
        return 0.0

    def get_wavelength(self, idx): # real signature unknown; restored from __doc__
        """ get_wavelength(self, idx:int) -> float """
        return 0.0

    def get_wavelength_cal(self, c1, c2, c3): # real signature unknown; restored from __doc__
        """ get_wavelength_cal(self, c1:float, c2:float, c3:float) """
        pass

    def limit_max(self, value): # real signature unknown; restored from __doc__
        """ limit_max(self, value:float) """
        pass

    def limit_min(self, value): # real signature unknown; restored from __doc__
        """ limit_min(self, value:float) """
        pass

    def multiply(self, s2, resolution): # real signature unknown; restored from __doc__
        """ multiply(self, s2:Colord.Spectrum, resolution:float) -> Colord.Spectrum """
        pass

    def multiply_scalar(self, value): # real signature unknown; restored from __doc__
        """ multiply_scalar(self, value:float) -> Colord.Spectrum """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Colord.Spectrum """
        pass

    def normalize(self, wavelength, value): # real signature unknown; restored from __doc__
        """ normalize(self, wavelength:float, value:float) """
        pass

    def normalize_max(self, value): # real signature unknown; restored from __doc__
        """ normalize_max(self, value:float) """
        pass

    def planckian_new(self, temperature): # real signature unknown; restored from __doc__
        """ planckian_new(temperature:float) -> Colord.Spectrum """
        pass

    def planckian_new_full(self, temperature, start, end, resolution): # real signature unknown; restored from __doc__
        """ planckian_new_full(temperature:float, start:float, end:float, resolution:float) -> Colord.Spectrum """
        pass

    def resample(self, start, end, resolution): # real signature unknown; restored from __doc__
        """ resample(self, start:float, end:float, resolution:float) -> Colord.Spectrum """
        pass

    def resample_to_size(self, size): # real signature unknown; restored from __doc__
        """ resample_to_size(self, size:int) -> Colord.Spectrum """
        pass

    def set_data(self, value): # real signature unknown; restored from __doc__
        """ set_data(self, value:list) """
        pass

    def set_end(self, end): # real signature unknown; restored from __doc__
        """ set_end(self, end:float) """
        pass

    def set_id(self, id): # real signature unknown; restored from __doc__
        """ set_id(self, id:str) """
        pass

    def set_norm(self, norm): # real signature unknown; restored from __doc__
        """ set_norm(self, norm:float) """
        pass

    def set_start(self, start): # real signature unknown; restored from __doc__
        """ set_start(self, start:float) """
        pass

    def set_value(self, idx, data): # real signature unknown; restored from __doc__
        """ set_value(self, idx:int, data:float) """
        pass

    def set_wavelength_cal(self, c1, c2, c3): # real signature unknown; restored from __doc__
        """ set_wavelength_cal(self, c1:float, c2:float, c3:float) """
        pass

    def sized_new(self, reserved_size): # real signature unknown; restored from __doc__
        """ sized_new(reserved_size:int) -> Colord.Spectrum """
        pass

    def subtract(self, s2, resolution): # real signature unknown; restored from __doc__
        """ subtract(self, s2:Colord.Spectrum, resolution:float) -> Colord.Spectrum """
        pass

    def to_string(self, max_width, max_height): # real signature unknown; restored from __doc__
        """ to_string(self, max_width:int, max_height:int) -> str """
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
        """ new() -> Colord.Spectrum """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Spectrum), '__module__': 'gi.repository.Colord', '__gtype__': <GType CdSpectrum (94892598901104)>, '__dict__': <attribute '__dict__' of 'Spectrum' objects>, '__weakref__': <attribute '__weakref__' of 'Spectrum' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'planckian_new': gi.FunctionInfo(planckian_new), 'planckian_new_full': gi.FunctionInfo(planckian_new_full), 'sized_new': gi.FunctionInfo(sized_new), 'add_value': gi.FunctionInfo(add_value), 'dup': gi.FunctionInfo(dup), 'free': gi.FunctionInfo(free), 'get_data': gi.FunctionInfo(get_data), 'get_end': gi.FunctionInfo(get_end), 'get_id': gi.FunctionInfo(get_id), 'get_norm': gi.FunctionInfo(get_norm), 'get_resolution': gi.FunctionInfo(get_resolution), 'get_size': gi.FunctionInfo(get_size), 'get_start': gi.FunctionInfo(get_start), 'get_value': gi.FunctionInfo(get_value), 'get_value_for_nm': gi.FunctionInfo(get_value_for_nm), 'get_value_max': gi.FunctionInfo(get_value_max), 'get_value_min': gi.FunctionInfo(get_value_min), 'get_value_raw': gi.FunctionInfo(get_value_raw), 'get_wavelength': gi.FunctionInfo(get_wavelength), 'get_wavelength_cal': gi.FunctionInfo(get_wavelength_cal), 'limit_max': gi.FunctionInfo(limit_max), 'limit_min': gi.FunctionInfo(limit_min), 'multiply': gi.FunctionInfo(multiply), 'multiply_scalar': gi.FunctionInfo(multiply_scalar), 'normalize': gi.FunctionInfo(normalize), 'normalize_max': gi.FunctionInfo(normalize_max), 'resample': gi.FunctionInfo(resample), 'resample_to_size': gi.FunctionInfo(resample_to_size), 'set_data': gi.FunctionInfo(set_data), 'set_end': gi.FunctionInfo(set_end), 'set_id': gi.FunctionInfo(set_id), 'set_norm': gi.FunctionInfo(set_norm), 'set_start': gi.FunctionInfo(set_start), 'set_value': gi.FunctionInfo(set_value), 'set_wavelength_cal': gi.FunctionInfo(set_wavelength_cal), 'subtract': gi.FunctionInfo(subtract), 'to_string': gi.FunctionInfo(to_string), '__new__': <staticmethod object at 0x7f09131e4190>, '__init__': <function nothing at 0x7f09135aaee0>})"
    __gtype__ = None # (!) real value is '<GType CdSpectrum (94892598901104)>'
    __info__ = StructInfo(Spectrum)


