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


class MIKEYMessage(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        MIKEYMessage()
        new() -> GstSdp.MIKEYMessage
        new_from_bytes(bytes:GLib.Bytes, info:GstSdp.MIKEYDecryptInfo) -> GstSdp.MIKEYMessage
        new_from_caps(caps:Gst.Caps) -> GstSdp.MIKEYMessage
        new_from_data(data:list, info:GstSdp.MIKEYDecryptInfo) -> GstSdp.MIKEYMessage
    """
    def add_cs_srtp(self, policy, ssrc, roc): # real signature unknown; restored from __doc__
        """ add_cs_srtp(self, policy:int, ssrc:int, roc:int) -> bool """
        return False

    def add_payload(self, payload): # real signature unknown; restored from __doc__
        """ add_payload(self, payload:GstSdp.MIKEYPayload) -> bool """
        return False

    def add_pke(self, C, data): # real signature unknown; restored from __doc__
        """ add_pke(self, C:GstSdp.MIKEYCacheType, data:list) -> bool """
        return False

    def add_rand(self, rand): # real signature unknown; restored from __doc__
        """ add_rand(self, rand:list) -> bool """
        return False

    def add_rand_len(self, len): # real signature unknown; restored from __doc__
        """ add_rand_len(self, len:int) -> bool """
        return False

    def add_t(self, type, ts_value): # real signature unknown; restored from __doc__
        """ add_t(self, type:GstSdp.MIKEYTSType, ts_value:list) -> bool """
        return False

    def add_t_now_ntp_utc(self): # real signature unknown; restored from __doc__
        """ add_t_now_ntp_utc(self) -> bool """
        return False

    def base64_encode(self): # real signature unknown; restored from __doc__
        """ base64_encode(self) -> str """
        return ""

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def find_payload(self, type, nth): # real signature unknown; restored from __doc__
        """ find_payload(self, type:GstSdp.MIKEYPayloadType, nth:int) -> GstSdp.MIKEYPayload """
        pass

    def get_cs_srtp(self, idx): # real signature unknown; restored from __doc__
        """ get_cs_srtp(self, idx:int) -> GstSdp.MIKEYMapSRTP """
        pass

    def get_n_cs(self): # real signature unknown; restored from __doc__
        """ get_n_cs(self) -> int """
        return 0

    def get_n_payloads(self): # real signature unknown; restored from __doc__
        """ get_n_payloads(self) -> int """
        return 0

    def get_payload(self, idx): # real signature unknown; restored from __doc__
        """ get_payload(self, idx:int) -> GstSdp.MIKEYPayload """
        pass

    def insert_cs_srtp(self, idx, map): # real signature unknown; restored from __doc__
        """ insert_cs_srtp(self, idx:int, map:GstSdp.MIKEYMapSRTP) -> bool """
        return False

    def insert_payload(self, idx, payload): # real signature unknown; restored from __doc__
        """ insert_payload(self, idx:int, payload:GstSdp.MIKEYPayload) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GstSdp.MIKEYMessage """
        pass

    def new_from_bytes(self, bytes, info): # real signature unknown; restored from __doc__
        """ new_from_bytes(bytes:GLib.Bytes, info:GstSdp.MIKEYDecryptInfo) -> GstSdp.MIKEYMessage """
        pass

    def new_from_caps(self, caps): # real signature unknown; restored from __doc__
        """ new_from_caps(caps:Gst.Caps) -> GstSdp.MIKEYMessage """
        pass

    def new_from_data(self, data, info): # real signature unknown; restored from __doc__
        """ new_from_data(data:list, info:GstSdp.MIKEYDecryptInfo) -> GstSdp.MIKEYMessage """
        pass

    def remove_cs_srtp(self, idx): # real signature unknown; restored from __doc__
        """ remove_cs_srtp(self, idx:int) -> bool """
        return False

    def remove_payload(self, idx): # real signature unknown; restored from __doc__
        """ remove_payload(self, idx:int) -> bool """
        return False

    def replace_cs_srtp(self, idx, map): # real signature unknown; restored from __doc__
        """ replace_cs_srtp(self, idx:int, map:GstSdp.MIKEYMapSRTP) -> bool """
        return False

    def replace_payload(self, idx, payload): # real signature unknown; restored from __doc__
        """ replace_payload(self, idx:int, payload:GstSdp.MIKEYPayload) -> bool """
        return False

    def set_info(self, version, type, V, prf_func, CSB_id, map_type): # real signature unknown; restored from __doc__
        """ set_info(self, version:int, type:GstSdp.MIKEYType, V:bool, prf_func:GstSdp.MIKEYPRFFunc, CSB_id:int, map_type:GstSdp.MIKEYMapType) -> bool """
        return False

    def to_bytes(self, info): # real signature unknown; restored from __doc__
        """ to_bytes(self, info:GstSdp.MIKEYEncryptInfo) -> GLib.Bytes """
        pass

    def to_caps(self, caps): # real signature unknown; restored from __doc__
        """ to_caps(self, caps:Gst.Caps) -> bool """
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
        """ new() -> GstSdp.MIKEYMessage """
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

    CSB_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    map_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mini_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    payloads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prf_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MIKEYMessage), '__module__': 'gi.repository.GstSdp', '__gtype__': <GType GstMIKEYMessage (94778371161664)>, '__dict__': <attribute '__dict__' of 'MIKEYMessage' objects>, '__weakref__': <attribute '__weakref__' of 'MIKEYMessage' objects>, '__doc__': None, 'mini_object': <property object at 0x7f89a6027180>, 'version': <property object at 0x7f89a6027270>, 'type': <property object at 0x7f89a6027360>, 'V': <property object at 0x7f89a6027450>, 'prf_func': <property object at 0x7f89a6027540>, 'CSB_id': <property object at 0x7f89a6027630>, 'map_type': <property object at 0x7f89a6027720>, 'map_info': <property object at 0x7f89a6027810>, 'payloads': <property object at 0x7f89a6027900>, 'new': gi.FunctionInfo(new), 'new_from_bytes': gi.FunctionInfo(new_from_bytes), 'new_from_caps': gi.FunctionInfo(new_from_caps), 'new_from_data': gi.FunctionInfo(new_from_data), 'add_cs_srtp': gi.FunctionInfo(add_cs_srtp), 'add_payload': gi.FunctionInfo(add_payload), 'add_pke': gi.FunctionInfo(add_pke), 'add_rand': gi.FunctionInfo(add_rand), 'add_rand_len': gi.FunctionInfo(add_rand_len), 'add_t': gi.FunctionInfo(add_t), 'add_t_now_ntp_utc': gi.FunctionInfo(add_t_now_ntp_utc), 'base64_encode': gi.FunctionInfo(base64_encode), 'find_payload': gi.FunctionInfo(find_payload), 'get_cs_srtp': gi.FunctionInfo(get_cs_srtp), 'get_n_cs': gi.FunctionInfo(get_n_cs), 'get_n_payloads': gi.FunctionInfo(get_n_payloads), 'get_payload': gi.FunctionInfo(get_payload), 'insert_cs_srtp': gi.FunctionInfo(insert_cs_srtp), 'insert_payload': gi.FunctionInfo(insert_payload), 'remove_cs_srtp': gi.FunctionInfo(remove_cs_srtp), 'remove_payload': gi.FunctionInfo(remove_payload), 'replace_cs_srtp': gi.FunctionInfo(replace_cs_srtp), 'replace_payload': gi.FunctionInfo(replace_payload), 'set_info': gi.FunctionInfo(set_info), 'to_bytes': gi.FunctionInfo(to_bytes), 'to_caps': gi.FunctionInfo(to_caps), '__new__': <staticmethod object at 0x7f89a60263a0>, '__init__': <function nothing at 0x7f89a625cee0>})"
    __gtype__ = None # (!) real value is '<GType GstMIKEYMessage (94778371161664)>'
    __info__ = StructInfo(MIKEYMessage)


