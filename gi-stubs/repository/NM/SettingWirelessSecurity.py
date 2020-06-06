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


from .Setting import Setting

class SettingWirelessSecurity(Setting):
    """
    :Constructors:
    
    ::
    
        SettingWirelessSecurity(**properties)
        new() -> NM.Setting
    """
    def add_group(self, group): # real signature unknown; restored from __doc__
        """ add_group(self, group:str) -> bool """
        return False

    def add_pairwise(self, pairwise): # real signature unknown; restored from __doc__
        """ add_pairwise(self, pairwise:str) -> bool """
        return False

    def add_proto(self, proto): # real signature unknown; restored from __doc__
        """ add_proto(self, proto:str) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_groups(self): # real signature unknown; restored from __doc__
        """ clear_groups(self) """
        pass

    def clear_pairwise(self): # real signature unknown; restored from __doc__
        """ clear_pairwise(self) """
        pass

    def clear_protos(self): # real signature unknown; restored from __doc__
        """ clear_protos(self) """
        pass

    def compare(self, b, flags): # real signature unknown; restored from __doc__
        """ compare(self, b:NM.Setting, flags:NM.SettingCompareFlags) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def diff(self, b, flags, invert_results, results): # real signature unknown; restored from __doc__
        """ diff(self, b:NM.Setting, flags:NM.SettingCompareFlags, invert_results:bool, results:dict) -> bool, results:dict """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_aggregate(self, *args, **kwargs): # real signature unknown
        """ aggregate(self, type_i:int, arg=None) -> bool """
        pass

    def do_get_secret_flags(self, *args, **kwargs): # real signature unknown
        """ get_secret_flags(self, secret_name:str, out_flags:NM.SettingSecretFlags) -> bool """
        pass

    def do_init_from_dbus(self, *args, **kwargs): # real signature unknown
        """ init_from_dbus(self, keys:dict, setting_dict:GLib.Variant, connection_dict:GLib.Variant, parse_flags:int) -> bool """
        pass

    def do_set_secret_flags(self, *args, **kwargs): # real signature unknown
        """ set_secret_flags(self, secret_name:str, flags:NM.SettingSecretFlags) -> bool """
        pass

    def do_update_one_secret(self, *args, **kwargs): # real signature unknown
        """ update_one_secret(self, key:str, value:GLib.Variant) -> int """
        pass

    def do_verify(self, *args, **kwargs): # real signature unknown
        """ verify(self, connection:NM.Connection) -> int """
        pass

    def do_verify_secrets(self, *args, **kwargs): # real signature unknown
        """ verify_secrets(self, connection:NM.Connection=None) -> bool """
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) -> NM.Setting """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def enumerate_values(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_values(self, func:NM.SettingValueIterFn, user_data=None) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_auth_alg(self): # real signature unknown; restored from __doc__
        """ get_auth_alg(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dbus_property_type(self, property_name): # real signature unknown; restored from __doc__
        """ get_dbus_property_type(self, property_name:str) -> GLib.VariantType """
        pass

    def get_fils(self): # real signature unknown; restored from __doc__
        """ get_fils(self) -> NM.SettingWirelessSecurityFils """
        pass

    def get_group(self, i): # real signature unknown; restored from __doc__
        """ get_group(self, i:int) -> str """
        return ""

    def get_key_mgmt(self): # real signature unknown; restored from __doc__
        """ get_key_mgmt(self) -> str """
        return ""

    def get_leap_password(self): # real signature unknown; restored from __doc__
        """ get_leap_password(self) -> str """
        return ""

    def get_leap_password_flags(self): # real signature unknown; restored from __doc__
        """ get_leap_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_leap_username(self): # real signature unknown; restored from __doc__
        """ get_leap_username(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_num_groups(self): # real signature unknown; restored from __doc__
        """ get_num_groups(self) -> int """
        return 0

    def get_num_pairwise(self): # real signature unknown; restored from __doc__
        """ get_num_pairwise(self) -> int """
        return 0

    def get_num_protos(self): # real signature unknown; restored from __doc__
        """ get_num_protos(self) -> int """
        return 0

    def get_pairwise(self, i): # real signature unknown; restored from __doc__
        """ get_pairwise(self, i:int) -> str """
        return ""

    def get_pmf(self): # real signature unknown; restored from __doc__
        """ get_pmf(self) -> NM.SettingWirelessSecurityPmf """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_proto(self, i): # real signature unknown; restored from __doc__
        """ get_proto(self, i:int) -> str """
        return ""

    def get_psk(self): # real signature unknown; restored from __doc__
        """ get_psk(self) -> str """
        return ""

    def get_psk_flags(self): # real signature unknown; restored from __doc__
        """ get_psk_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_secret_flags(self, secret_name, out_flags): # real signature unknown; restored from __doc__
        """ get_secret_flags(self, secret_name:str, out_flags:NM.SettingSecretFlags) -> bool """
        return False

    def get_wep_key(self, idx): # real signature unknown; restored from __doc__
        """ get_wep_key(self, idx:int) -> str """
        return ""

    def get_wep_key_flags(self): # real signature unknown; restored from __doc__
        """ get_wep_key_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_wep_key_type(self): # real signature unknown; restored from __doc__
        """ get_wep_key_type(self) -> NM.WepKeyType """
        pass

    def get_wep_tx_keyidx(self): # real signature unknown; restored from __doc__
        """ get_wep_tx_keyidx(self) -> int """
        return 0

    def get_wps_method(self): # real signature unknown; restored from __doc__
        """ get_wps_method(self) -> NM.SettingWirelessSecurityWpsMethod """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lookup_type(self, name): # real signature unknown; restored from __doc__
        """ lookup_type(name:str) -> GType """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> NM.Setting """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_group(self, i): # real signature unknown; restored from __doc__
        """ remove_group(self, i:int) """
        pass

    def remove_group_by_value(self, group): # real signature unknown; restored from __doc__
        """ remove_group_by_value(self, group:str) -> bool """
        return False

    def remove_pairwise(self, i): # real signature unknown; restored from __doc__
        """ remove_pairwise(self, i:int) """
        pass

    def remove_pairwise_by_value(self, pairwise): # real signature unknown; restored from __doc__
        """ remove_pairwise_by_value(self, pairwise:str) -> bool """
        return False

    def remove_proto(self, i): # real signature unknown; restored from __doc__
        """ remove_proto(self, i:int) """
        pass

    def remove_proto_by_value(self, proto): # real signature unknown; restored from __doc__
        """ remove_proto_by_value(self, proto:str) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_secret_flags(self, secret_name, flags): # real signature unknown; restored from __doc__
        """ set_secret_flags(self, secret_name:str, flags:NM.SettingSecretFlags) -> bool """
        return False

    def set_wep_key(self, idx, key): # real signature unknown; restored from __doc__
        """ set_wep_key(self, idx:int, key:str) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def verify(self, connection=None): # real signature unknown; restored from __doc__
        """ verify(self, connection:NM.Connection=None) -> bool """
        return False

    def verify_secrets(self, connection=None): # real signature unknown; restored from __doc__
        """ verify_secrets(self, connection:NM.Connection=None) -> bool """
        return False

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b80c26a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SettingWirelessSecurity), '__module__': 'gi.repository.NM', '__gtype__': <GType NMSettingWirelessSecurity (94741104208544)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_group': gi.FunctionInfo(add_group), 'add_pairwise': gi.FunctionInfo(add_pairwise), 'add_proto': gi.FunctionInfo(add_proto), 'clear_groups': gi.FunctionInfo(clear_groups), 'clear_pairwise': gi.FunctionInfo(clear_pairwise), 'clear_protos': gi.FunctionInfo(clear_protos), 'get_auth_alg': gi.FunctionInfo(get_auth_alg), 'get_fils': gi.FunctionInfo(get_fils), 'get_group': gi.FunctionInfo(get_group), 'get_key_mgmt': gi.FunctionInfo(get_key_mgmt), 'get_leap_password': gi.FunctionInfo(get_leap_password), 'get_leap_password_flags': gi.FunctionInfo(get_leap_password_flags), 'get_leap_username': gi.FunctionInfo(get_leap_username), 'get_num_groups': gi.FunctionInfo(get_num_groups), 'get_num_pairwise': gi.FunctionInfo(get_num_pairwise), 'get_num_protos': gi.FunctionInfo(get_num_protos), 'get_pairwise': gi.FunctionInfo(get_pairwise), 'get_pmf': gi.FunctionInfo(get_pmf), 'get_proto': gi.FunctionInfo(get_proto), 'get_psk': gi.FunctionInfo(get_psk), 'get_psk_flags': gi.FunctionInfo(get_psk_flags), 'get_wep_key': gi.FunctionInfo(get_wep_key), 'get_wep_key_flags': gi.FunctionInfo(get_wep_key_flags), 'get_wep_key_type': gi.FunctionInfo(get_wep_key_type), 'get_wep_tx_keyidx': gi.FunctionInfo(get_wep_tx_keyidx), 'get_wps_method': gi.FunctionInfo(get_wps_method), 'remove_group': gi.FunctionInfo(remove_group), 'remove_group_by_value': gi.FunctionInfo(remove_group_by_value), 'remove_pairwise': gi.FunctionInfo(remove_pairwise), 'remove_pairwise_by_value': gi.FunctionInfo(remove_pairwise_by_value), 'remove_proto': gi.FunctionInfo(remove_proto), 'remove_proto_by_value': gi.FunctionInfo(remove_proto_by_value), 'set_wep_key': gi.FunctionInfo(set_wep_key), 'parent': <property object at 0x7fb9b8494900>})"
    __gdoc__ = 'Object NMSettingWirelessSecurity\n\nProperties from NMSettingWirelessSecurity:\n  key-mgmt -> gchararray: \n    \n  wep-tx-keyidx -> guint: \n    \n  auth-alg -> gchararray: \n    \n  proto -> GStrv: \n    \n  pairwise -> GStrv: \n    \n  group -> GStrv: \n    \n  pmf -> gint: \n    \n  leap-username -> gchararray: \n    \n  wep-key0 -> gchararray: \n    \n  wep-key1 -> gchararray: \n    \n  wep-key2 -> gchararray: \n    \n  wep-key3 -> gchararray: \n    \n  wep-key-flags -> NMSettingSecretFlags: \n    \n  wep-key-type -> NMWepKeyType: \n    \n  psk -> gchararray: \n    \n  psk-flags -> NMSettingSecretFlags: \n    \n  leap-password -> gchararray: \n    \n  leap-password-flags -> NMSettingSecretFlags: \n    \n  wps-method -> guint: \n    \n  fils -> gint: \n    \n\nProperties from NMSetting:\n  name -> gchararray: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMSettingWirelessSecurity (94741104208544)>'
    __info__ = ObjectInfo(SettingWirelessSecurity)


