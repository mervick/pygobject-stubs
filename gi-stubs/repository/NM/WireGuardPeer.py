# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class WireGuardPeer(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> NM.WireGuardPeer
    """
    def append_allowed_ip(self, allowed_ip, accept_invalid): # real signature unknown; restored from __doc__
        """ append_allowed_ip(self, allowed_ip:str, accept_invalid:bool) -> bool """
        return False

    def clear_allowed_ips(self): # real signature unknown; restored from __doc__
        """ clear_allowed_ips(self) """
        pass

    def cmp(self, b=None, compare_flags): # real signature unknown; restored from __doc__
        """ cmp(self, b:NM.WireGuardPeer=None, compare_flags:NM.SettingCompareFlags) -> int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_allowed_ip(self, idx, out_is_valid=None): # real signature unknown; restored from __doc__
        """ get_allowed_ip(self, idx:int, out_is_valid:bool=None) -> str """
        return ""

    def get_allowed_ips_len(self): # real signature unknown; restored from __doc__
        """ get_allowed_ips_len(self) -> int """
        return 0

    def get_endpoint(self): # real signature unknown; restored from __doc__
        """ get_endpoint(self) -> str """
        return ""

    def get_persistent_keepalive(self): # real signature unknown; restored from __doc__
        """ get_persistent_keepalive(self) -> int """
        return 0

    def get_preshared_key(self): # real signature unknown; restored from __doc__
        """ get_preshared_key(self) -> str """
        return ""

    def get_preshared_key_flags(self): # real signature unknown; restored from __doc__
        """ get_preshared_key_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_public_key(self): # real signature unknown; restored from __doc__
        """ get_public_key(self) -> str """
        return ""

    def is_sealed(self): # real signature unknown; restored from __doc__
        """ is_sealed(self) -> bool """
        return False

    def is_valid(self, check_non_secrets, check_secrets): # real signature unknown; restored from __doc__
        """ is_valid(self, check_non_secrets:bool, check_secrets:bool) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> NM.WireGuardPeer """
        pass

    def new_clone(self, with_secrets): # real signature unknown; restored from __doc__
        """ new_clone(self, with_secrets:bool) -> NM.WireGuardPeer """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> NM.WireGuardPeer """
        pass

    def remove_allowed_ip(self, idx): # real signature unknown; restored from __doc__
        """ remove_allowed_ip(self, idx:int) -> bool """
        return False

    def seal(self): # real signature unknown; restored from __doc__
        """ seal(self) """
        pass

    def set_endpoint(self, endpoint, allow_invalid): # real signature unknown; restored from __doc__
        """ set_endpoint(self, endpoint:str, allow_invalid:bool) -> bool """
        return False

    def set_persistent_keepalive(self, persistent_keepalive): # real signature unknown; restored from __doc__
        """ set_persistent_keepalive(self, persistent_keepalive:int) """
        pass

    def set_preshared_key(self, preshared_key=None, accept_invalid): # real signature unknown; restored from __doc__
        """ set_preshared_key(self, preshared_key:str=None, accept_invalid:bool) -> bool """
        return False

    def set_preshared_key_flags(self, preshared_key_flags): # real signature unknown; restored from __doc__
        """ set_preshared_key_flags(self, preshared_key_flags:NM.SettingSecretFlags) """
        pass

    def set_public_key(self, public_key=None, accept_invalid): # real signature unknown; restored from __doc__
        """ set_public_key(self, public_key:str=None, accept_invalid:bool) -> bool """
        return False

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
        """ new() -> NM.WireGuardPeer """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(WireGuardPeer), '__module__': 'gi.repository.NM', '__gtype__': <GType NMWireGuardPeer (94741104748864)>, '__dict__': <attribute '__dict__' of 'WireGuardPeer' objects>, '__weakref__': <attribute '__weakref__' of 'WireGuardPeer' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'append_allowed_ip': gi.FunctionInfo(append_allowed_ip), 'clear_allowed_ips': gi.FunctionInfo(clear_allowed_ips), 'cmp': gi.FunctionInfo(cmp), 'get_allowed_ip': gi.FunctionInfo(get_allowed_ip), 'get_allowed_ips_len': gi.FunctionInfo(get_allowed_ips_len), 'get_endpoint': gi.FunctionInfo(get_endpoint), 'get_persistent_keepalive': gi.FunctionInfo(get_persistent_keepalive), 'get_preshared_key': gi.FunctionInfo(get_preshared_key), 'get_preshared_key_flags': gi.FunctionInfo(get_preshared_key_flags), 'get_public_key': gi.FunctionInfo(get_public_key), 'is_sealed': gi.FunctionInfo(is_sealed), 'is_valid': gi.FunctionInfo(is_valid), 'new_clone': gi.FunctionInfo(new_clone), 'ref': gi.FunctionInfo(ref), 'remove_allowed_ip': gi.FunctionInfo(remove_allowed_ip), 'seal': gi.FunctionInfo(seal), 'set_endpoint': gi.FunctionInfo(set_endpoint), 'set_persistent_keepalive': gi.FunctionInfo(set_persistent_keepalive), 'set_preshared_key': gi.FunctionInfo(set_preshared_key), 'set_preshared_key_flags': gi.FunctionInfo(set_preshared_key_flags), 'set_public_key': gi.FunctionInfo(set_public_key), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7fb9b84a8be0>, '__init__': <function nothing at 0x7fb9b8f70ee0>})"
    __gtype__ = None # (!) real value is '<GType NMWireGuardPeer (94741104748864)>'
    __info__ = StructInfo(WireGuardPeer)


