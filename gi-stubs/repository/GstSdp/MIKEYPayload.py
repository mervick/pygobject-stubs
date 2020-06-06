# encoding: utf-8
# module gi.repository.GstSdp
# from /usr/lib64/girepository-1.0/GstSdp-1.0.typelib
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


class MIKEYPayload(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        MIKEYPayload()
        new(type:GstSdp.MIKEYPayloadType) -> GstSdp.MIKEYPayload or None
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def kemac_add_sub(self, newpay): # real signature unknown; restored from __doc__
        """ kemac_add_sub(self, newpay:GstSdp.MIKEYPayload) -> bool """
        return False

    def kemac_get_n_sub(self): # real signature unknown; restored from __doc__
        """ kemac_get_n_sub(self) -> int """
        return 0

    def kemac_get_sub(self, idx): # real signature unknown; restored from __doc__
        """ kemac_get_sub(self, idx:int) -> GstSdp.MIKEYPayload """
        pass

    def kemac_remove_sub(self, idx): # real signature unknown; restored from __doc__
        """ kemac_remove_sub(self, idx:int) -> bool """
        return False

    def kemac_set(self, enc_alg, mac_alg): # real signature unknown; restored from __doc__
        """ kemac_set(self, enc_alg:GstSdp.MIKEYEncAlg, mac_alg:GstSdp.MIKEYMacAlg) -> bool """
        return False

    def key_data_set_interval(self, vf_len, vt_data): # real signature unknown; restored from __doc__
        """ key_data_set_interval(self, vf_len:int, vt_data:list) -> bool """
        return False

    def key_data_set_key(self, key_type, key_data): # real signature unknown; restored from __doc__
        """ key_data_set_key(self, key_type:GstSdp.MIKEYKeyDataType, key_data:list) -> bool """
        return False

    def key_data_set_salt(self, salt_data=None): # real signature unknown; restored from __doc__
        """ key_data_set_salt(self, salt_data:list=None) -> bool """
        return False

    def key_data_set_spi(self, spi_data): # real signature unknown; restored from __doc__
        """ key_data_set_spi(self, spi_data:list) -> bool """
        return False

    def new(self, type): # real signature unknown; restored from __doc__
        """ new(type:GstSdp.MIKEYPayloadType) -> GstSdp.MIKEYPayload or None """
        pass

    def pke_set(self, C, data): # real signature unknown; restored from __doc__
        """ pke_set(self, C:GstSdp.MIKEYCacheType, data:list) -> bool """
        return False

    def rand_set(self, rand): # real signature unknown; restored from __doc__
        """ rand_set(self, rand:list) -> bool """
        return False

    def sp_add_param(self, type, val): # real signature unknown; restored from __doc__
        """ sp_add_param(self, type:int, val:list) -> bool """
        return False

    def sp_get_n_params(self): # real signature unknown; restored from __doc__
        """ sp_get_n_params(self) -> int """
        return 0

    def sp_get_param(self, idx): # real signature unknown; restored from __doc__
        """ sp_get_param(self, idx:int) -> GstSdp.MIKEYPayloadSPParam """
        pass

    def sp_remove_param(self, idx): # real signature unknown; restored from __doc__
        """ sp_remove_param(self, idx:int) -> bool """
        return False

    def sp_set(self, policy, proto): # real signature unknown; restored from __doc__
        """ sp_set(self, policy:int, proto:GstSdp.MIKEYSecProto) -> bool """
        return False

    def t_set(self, type, ts_value): # real signature unknown; restored from __doc__
        """ t_set(self, type:GstSdp.MIKEYTSType, ts_value:list) -> bool """
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

    len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mini_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MIKEYPayload), '__module__': 'gi.repository.GstSdp', '__gtype__': <GType GstMIKEYPayload (94778371226464)>, '__dict__': <attribute '__dict__' of 'MIKEYPayload' objects>, '__weakref__': <attribute '__weakref__' of 'MIKEYPayload' objects>, '__doc__': None, 'mini_object': <property object at 0x7f89a6027c20>, 'type': <property object at 0x7f89a6027d10>, 'len': <property object at 0x7f89a6027e00>, 'new': gi.FunctionInfo(new), 'kemac_add_sub': gi.FunctionInfo(kemac_add_sub), 'kemac_get_n_sub': gi.FunctionInfo(kemac_get_n_sub), 'kemac_get_sub': gi.FunctionInfo(kemac_get_sub), 'kemac_remove_sub': gi.FunctionInfo(kemac_remove_sub), 'kemac_set': gi.FunctionInfo(kemac_set), 'key_data_set_interval': gi.FunctionInfo(key_data_set_interval), 'key_data_set_key': gi.FunctionInfo(key_data_set_key), 'key_data_set_salt': gi.FunctionInfo(key_data_set_salt), 'key_data_set_spi': gi.FunctionInfo(key_data_set_spi), 'pke_set': gi.FunctionInfo(pke_set), 'rand_set': gi.FunctionInfo(rand_set), 'sp_add_param': gi.FunctionInfo(sp_add_param), 'sp_get_n_params': gi.FunctionInfo(sp_get_n_params), 'sp_get_param': gi.FunctionInfo(sp_get_param), 'sp_remove_param': gi.FunctionInfo(sp_remove_param), 'sp_set': gi.FunctionInfo(sp_set), 't_set': gi.FunctionInfo(t_set)})"
    __gtype__ = None # (!) real value is '<GType GstMIKEYPayload (94778371226464)>'
    __info__ = StructInfo(MIKEYPayload)


