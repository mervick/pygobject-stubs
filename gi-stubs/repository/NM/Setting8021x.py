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

class Setting8021x(Setting):
    """
    :Constructors:
    
    ::
    
        Setting8021x(**properties)
        new() -> NM.Setting
    """
    def add_altsubject_match(self, altsubject_match): # real signature unknown; restored from __doc__
        """ add_altsubject_match(self, altsubject_match:str) -> bool """
        return False

    def add_eap_method(self, eap): # real signature unknown; restored from __doc__
        """ add_eap_method(self, eap:str) -> bool """
        return False

    def add_phase2_altsubject_match(self, phase2_altsubject_match): # real signature unknown; restored from __doc__
        """ add_phase2_altsubject_match(self, phase2_altsubject_match:str) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_cert_scheme(self, pdata=None, length): # real signature unknown; restored from __doc__
        """ check_cert_scheme(pdata=None, length:int) -> NM.Setting8021xCKScheme """
        pass

    def clear_altsubject_matches(self): # real signature unknown; restored from __doc__
        """ clear_altsubject_matches(self) """
        pass

    def clear_eap_methods(self): # real signature unknown; restored from __doc__
        """ clear_eap_methods(self) """
        pass

    def clear_phase2_altsubject_matches(self): # real signature unknown; restored from __doc__
        """ clear_phase2_altsubject_matches(self) """
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

    def get_altsubject_match(self, i): # real signature unknown; restored from __doc__
        """ get_altsubject_match(self, i:int) -> str """
        return ""

    def get_anonymous_identity(self): # real signature unknown; restored from __doc__
        """ get_anonymous_identity(self) -> str """
        return ""

    def get_auth_timeout(self): # real signature unknown; restored from __doc__
        """ get_auth_timeout(self) -> int """
        return 0

    def get_ca_cert_blob(self): # real signature unknown; restored from __doc__
        """ get_ca_cert_blob(self) -> GLib.Bytes """
        pass

    def get_ca_cert_password(self): # real signature unknown; restored from __doc__
        """ get_ca_cert_password(self) -> str """
        return ""

    def get_ca_cert_password_flags(self): # real signature unknown; restored from __doc__
        """ get_ca_cert_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_ca_cert_path(self): # real signature unknown; restored from __doc__
        """ get_ca_cert_path(self) -> str """
        return ""

    def get_ca_cert_scheme(self): # real signature unknown; restored from __doc__
        """ get_ca_cert_scheme(self) -> NM.Setting8021xCKScheme """
        pass

    def get_ca_cert_uri(self): # real signature unknown; restored from __doc__
        """ get_ca_cert_uri(self) -> str """
        return ""

    def get_ca_path(self): # real signature unknown; restored from __doc__
        """ get_ca_path(self) -> str """
        return ""

    def get_client_cert_blob(self): # real signature unknown; restored from __doc__
        """ get_client_cert_blob(self) -> GLib.Bytes """
        pass

    def get_client_cert_password(self): # real signature unknown; restored from __doc__
        """ get_client_cert_password(self) -> str """
        return ""

    def get_client_cert_password_flags(self): # real signature unknown; restored from __doc__
        """ get_client_cert_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_client_cert_path(self): # real signature unknown; restored from __doc__
        """ get_client_cert_path(self) -> str """
        return ""

    def get_client_cert_scheme(self): # real signature unknown; restored from __doc__
        """ get_client_cert_scheme(self) -> NM.Setting8021xCKScheme """
        pass

    def get_client_cert_uri(self): # real signature unknown; restored from __doc__
        """ get_client_cert_uri(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dbus_property_type(self, property_name): # real signature unknown; restored from __doc__
        """ get_dbus_property_type(self, property_name:str) -> GLib.VariantType """
        pass

    def get_domain_suffix_match(self): # real signature unknown; restored from __doc__
        """ get_domain_suffix_match(self) -> str """
        return ""

    def get_eap_method(self, i): # real signature unknown; restored from __doc__
        """ get_eap_method(self, i:int) -> str """
        return ""

    def get_identity(self): # real signature unknown; restored from __doc__
        """ get_identity(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_num_altsubject_matches(self): # real signature unknown; restored from __doc__
        """ get_num_altsubject_matches(self) -> int """
        return 0

    def get_num_eap_methods(self): # real signature unknown; restored from __doc__
        """ get_num_eap_methods(self) -> int """
        return 0

    def get_num_phase2_altsubject_matches(self): # real signature unknown; restored from __doc__
        """ get_num_phase2_altsubject_matches(self) -> int """
        return 0

    def get_optional(self): # real signature unknown; restored from __doc__
        """ get_optional(self) -> bool """
        return False

    def get_pac_file(self): # real signature unknown; restored from __doc__
        """ get_pac_file(self) -> str """
        return ""

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str """
        return ""

    def get_password_flags(self): # real signature unknown; restored from __doc__
        """ get_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_password_raw(self): # real signature unknown; restored from __doc__
        """ get_password_raw(self) -> GLib.Bytes """
        pass

    def get_password_raw_flags(self): # real signature unknown; restored from __doc__
        """ get_password_raw_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_phase1_auth_flags(self): # real signature unknown; restored from __doc__
        """ get_phase1_auth_flags(self) -> NM.Setting8021xAuthFlags """
        pass

    def get_phase1_fast_provisioning(self): # real signature unknown; restored from __doc__
        """ get_phase1_fast_provisioning(self) -> str """
        return ""

    def get_phase1_peaplabel(self): # real signature unknown; restored from __doc__
        """ get_phase1_peaplabel(self) -> str """
        return ""

    def get_phase1_peapver(self): # real signature unknown; restored from __doc__
        """ get_phase1_peapver(self) -> str """
        return ""

    def get_phase2_altsubject_match(self, i): # real signature unknown; restored from __doc__
        """ get_phase2_altsubject_match(self, i:int) -> str """
        return ""

    def get_phase2_auth(self): # real signature unknown; restored from __doc__
        """ get_phase2_auth(self) -> str """
        return ""

    def get_phase2_autheap(self): # real signature unknown; restored from __doc__
        """ get_phase2_autheap(self) -> str """
        return ""

    def get_phase2_ca_cert_blob(self): # real signature unknown; restored from __doc__
        """ get_phase2_ca_cert_blob(self) -> GLib.Bytes """
        pass

    def get_phase2_ca_cert_password(self): # real signature unknown; restored from __doc__
        """ get_phase2_ca_cert_password(self) -> str """
        return ""

    def get_phase2_ca_cert_password_flags(self): # real signature unknown; restored from __doc__
        """ get_phase2_ca_cert_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_phase2_ca_cert_path(self): # real signature unknown; restored from __doc__
        """ get_phase2_ca_cert_path(self) -> str """
        return ""

    def get_phase2_ca_cert_scheme(self): # real signature unknown; restored from __doc__
        """ get_phase2_ca_cert_scheme(self) -> NM.Setting8021xCKScheme """
        pass

    def get_phase2_ca_cert_uri(self): # real signature unknown; restored from __doc__
        """ get_phase2_ca_cert_uri(self) -> str """
        return ""

    def get_phase2_ca_path(self): # real signature unknown; restored from __doc__
        """ get_phase2_ca_path(self) -> str """
        return ""

    def get_phase2_client_cert_blob(self): # real signature unknown; restored from __doc__
        """ get_phase2_client_cert_blob(self) -> GLib.Bytes """
        pass

    def get_phase2_client_cert_password(self): # real signature unknown; restored from __doc__
        """ get_phase2_client_cert_password(self) -> str """
        return ""

    def get_phase2_client_cert_password_flags(self): # real signature unknown; restored from __doc__
        """ get_phase2_client_cert_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_phase2_client_cert_path(self): # real signature unknown; restored from __doc__
        """ get_phase2_client_cert_path(self) -> str """
        return ""

    def get_phase2_client_cert_scheme(self): # real signature unknown; restored from __doc__
        """ get_phase2_client_cert_scheme(self) -> NM.Setting8021xCKScheme """
        pass

    def get_phase2_client_cert_uri(self): # real signature unknown; restored from __doc__
        """ get_phase2_client_cert_uri(self) -> str """
        return ""

    def get_phase2_domain_suffix_match(self): # real signature unknown; restored from __doc__
        """ get_phase2_domain_suffix_match(self) -> str """
        return ""

    def get_phase2_private_key_blob(self): # real signature unknown; restored from __doc__
        """ get_phase2_private_key_blob(self) -> GLib.Bytes """
        pass

    def get_phase2_private_key_format(self): # real signature unknown; restored from __doc__
        """ get_phase2_private_key_format(self) -> NM.Setting8021xCKFormat """
        pass

    def get_phase2_private_key_password(self): # real signature unknown; restored from __doc__
        """ get_phase2_private_key_password(self) -> str """
        return ""

    def get_phase2_private_key_password_flags(self): # real signature unknown; restored from __doc__
        """ get_phase2_private_key_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_phase2_private_key_path(self): # real signature unknown; restored from __doc__
        """ get_phase2_private_key_path(self) -> str """
        return ""

    def get_phase2_private_key_scheme(self): # real signature unknown; restored from __doc__
        """ get_phase2_private_key_scheme(self) -> NM.Setting8021xCKScheme """
        pass

    def get_phase2_private_key_uri(self): # real signature unknown; restored from __doc__
        """ get_phase2_private_key_uri(self) -> str """
        return ""

    def get_phase2_subject_match(self): # real signature unknown; restored from __doc__
        """ get_phase2_subject_match(self) -> str """
        return ""

    def get_pin(self): # real signature unknown; restored from __doc__
        """ get_pin(self) -> str """
        return ""

    def get_pin_flags(self): # real signature unknown; restored from __doc__
        """ get_pin_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_private_key_blob(self): # real signature unknown; restored from __doc__
        """ get_private_key_blob(self) -> GLib.Bytes """
        pass

    def get_private_key_format(self): # real signature unknown; restored from __doc__
        """ get_private_key_format(self) -> NM.Setting8021xCKFormat """
        pass

    def get_private_key_password(self): # real signature unknown; restored from __doc__
        """ get_private_key_password(self) -> str """
        return ""

    def get_private_key_password_flags(self): # real signature unknown; restored from __doc__
        """ get_private_key_password_flags(self) -> NM.SettingSecretFlags """
        pass

    def get_private_key_path(self): # real signature unknown; restored from __doc__
        """ get_private_key_path(self) -> str """
        return ""

    def get_private_key_scheme(self): # real signature unknown; restored from __doc__
        """ get_private_key_scheme(self) -> NM.Setting8021xCKScheme """
        pass

    def get_private_key_uri(self): # real signature unknown; restored from __doc__
        """ get_private_key_uri(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_secret_flags(self, secret_name, out_flags): # real signature unknown; restored from __doc__
        """ get_secret_flags(self, secret_name:str, out_flags:NM.SettingSecretFlags) -> bool """
        return False

    def get_subject_match(self): # real signature unknown; restored from __doc__
        """ get_subject_match(self) -> str """
        return ""

    def get_system_ca_certs(self): # real signature unknown; restored from __doc__
        """ get_system_ca_certs(self) -> bool """
        return False

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

    def remove_altsubject_match(self, i): # real signature unknown; restored from __doc__
        """ remove_altsubject_match(self, i:int) """
        pass

    def remove_altsubject_match_by_value(self, altsubject_match): # real signature unknown; restored from __doc__
        """ remove_altsubject_match_by_value(self, altsubject_match:str) -> bool """
        return False

    def remove_eap_method(self, i): # real signature unknown; restored from __doc__
        """ remove_eap_method(self, i:int) """
        pass

    def remove_eap_method_by_value(self, eap): # real signature unknown; restored from __doc__
        """ remove_eap_method_by_value(self, eap:str) -> bool """
        return False

    def remove_phase2_altsubject_match(self, i): # real signature unknown; restored from __doc__
        """ remove_phase2_altsubject_match(self, i:int) """
        pass

    def remove_phase2_altsubject_match_by_value(self, phase2_altsubject_match): # real signature unknown; restored from __doc__
        """ remove_phase2_altsubject_match_by_value(self, phase2_altsubject_match:str) -> bool """
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

    def set_ca_cert(self, value, scheme, out_format): # real signature unknown; restored from __doc__
        """ set_ca_cert(self, value:str, scheme:NM.Setting8021xCKScheme, out_format:NM.Setting8021xCKFormat) -> bool """
        return False

    def set_client_cert(self, value, scheme, out_format): # real signature unknown; restored from __doc__
        """ set_client_cert(self, value:str, scheme:NM.Setting8021xCKScheme, out_format:NM.Setting8021xCKFormat) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_phase2_ca_cert(self, value, scheme, out_format): # real signature unknown; restored from __doc__
        """ set_phase2_ca_cert(self, value:str, scheme:NM.Setting8021xCKScheme, out_format:NM.Setting8021xCKFormat) -> bool """
        return False

    def set_phase2_client_cert(self, value, scheme, out_format): # real signature unknown; restored from __doc__
        """ set_phase2_client_cert(self, value:str, scheme:NM.Setting8021xCKScheme, out_format:NM.Setting8021xCKFormat) -> bool """
        return False

    def set_phase2_private_key(self, value, password, scheme, out_format): # real signature unknown; restored from __doc__
        """ set_phase2_private_key(self, value:str, password:str, scheme:NM.Setting8021xCKScheme, out_format:NM.Setting8021xCKFormat) -> bool """
        return False

    def set_private_key(self, value, password, scheme, out_format): # real signature unknown; restored from __doc__
        """ set_private_key(self, value:str, password:str, scheme:NM.Setting8021xCKScheme, out_format:NM.Setting8021xCKFormat) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_secret_flags(self, secret_name, flags): # real signature unknown; restored from __doc__
        """ set_secret_flags(self, secret_name:str, flags:NM.SettingSecretFlags) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b805a190>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Setting8021x), '__module__': 'gi.repository.NM', '__gtype__': <GType NMSetting8021x (94741104348304)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'check_cert_scheme': gi.FunctionInfo(check_cert_scheme), 'add_altsubject_match': gi.FunctionInfo(add_altsubject_match), 'add_eap_method': gi.FunctionInfo(add_eap_method), 'add_phase2_altsubject_match': gi.FunctionInfo(add_phase2_altsubject_match), 'clear_altsubject_matches': gi.FunctionInfo(clear_altsubject_matches), 'clear_eap_methods': gi.FunctionInfo(clear_eap_methods), 'clear_phase2_altsubject_matches': gi.FunctionInfo(clear_phase2_altsubject_matches), 'get_altsubject_match': gi.FunctionInfo(get_altsubject_match), 'get_anonymous_identity': gi.FunctionInfo(get_anonymous_identity), 'get_auth_timeout': gi.FunctionInfo(get_auth_timeout), 'get_ca_cert_blob': gi.FunctionInfo(get_ca_cert_blob), 'get_ca_cert_password': gi.FunctionInfo(get_ca_cert_password), 'get_ca_cert_password_flags': gi.FunctionInfo(get_ca_cert_password_flags), 'get_ca_cert_path': gi.FunctionInfo(get_ca_cert_path), 'get_ca_cert_scheme': gi.FunctionInfo(get_ca_cert_scheme), 'get_ca_cert_uri': gi.FunctionInfo(get_ca_cert_uri), 'get_ca_path': gi.FunctionInfo(get_ca_path), 'get_client_cert_blob': gi.FunctionInfo(get_client_cert_blob), 'get_client_cert_password': gi.FunctionInfo(get_client_cert_password), 'get_client_cert_password_flags': gi.FunctionInfo(get_client_cert_password_flags), 'get_client_cert_path': gi.FunctionInfo(get_client_cert_path), 'get_client_cert_scheme': gi.FunctionInfo(get_client_cert_scheme), 'get_client_cert_uri': gi.FunctionInfo(get_client_cert_uri), 'get_domain_suffix_match': gi.FunctionInfo(get_domain_suffix_match), 'get_eap_method': gi.FunctionInfo(get_eap_method), 'get_identity': gi.FunctionInfo(get_identity), 'get_num_altsubject_matches': gi.FunctionInfo(get_num_altsubject_matches), 'get_num_eap_methods': gi.FunctionInfo(get_num_eap_methods), 'get_num_phase2_altsubject_matches': gi.FunctionInfo(get_num_phase2_altsubject_matches), 'get_optional': gi.FunctionInfo(get_optional), 'get_pac_file': gi.FunctionInfo(get_pac_file), 'get_password': gi.FunctionInfo(get_password), 'get_password_flags': gi.FunctionInfo(get_password_flags), 'get_password_raw': gi.FunctionInfo(get_password_raw), 'get_password_raw_flags': gi.FunctionInfo(get_password_raw_flags), 'get_phase1_auth_flags': gi.FunctionInfo(get_phase1_auth_flags), 'get_phase1_fast_provisioning': gi.FunctionInfo(get_phase1_fast_provisioning), 'get_phase1_peaplabel': gi.FunctionInfo(get_phase1_peaplabel), 'get_phase1_peapver': gi.FunctionInfo(get_phase1_peapver), 'get_phase2_altsubject_match': gi.FunctionInfo(get_phase2_altsubject_match), 'get_phase2_auth': gi.FunctionInfo(get_phase2_auth), 'get_phase2_autheap': gi.FunctionInfo(get_phase2_autheap), 'get_phase2_ca_cert_blob': gi.FunctionInfo(get_phase2_ca_cert_blob), 'get_phase2_ca_cert_password': gi.FunctionInfo(get_phase2_ca_cert_password), 'get_phase2_ca_cert_password_flags': gi.FunctionInfo(get_phase2_ca_cert_password_flags), 'get_phase2_ca_cert_path': gi.FunctionInfo(get_phase2_ca_cert_path), 'get_phase2_ca_cert_scheme': gi.FunctionInfo(get_phase2_ca_cert_scheme), 'get_phase2_ca_cert_uri': gi.FunctionInfo(get_phase2_ca_cert_uri), 'get_phase2_ca_path': gi.FunctionInfo(get_phase2_ca_path), 'get_phase2_client_cert_blob': gi.FunctionInfo(get_phase2_client_cert_blob), 'get_phase2_client_cert_password': gi.FunctionInfo(get_phase2_client_cert_password), 'get_phase2_client_cert_password_flags': gi.FunctionInfo(get_phase2_client_cert_password_flags), 'get_phase2_client_cert_path': gi.FunctionInfo(get_phase2_client_cert_path), 'get_phase2_client_cert_scheme': gi.FunctionInfo(get_phase2_client_cert_scheme), 'get_phase2_client_cert_uri': gi.FunctionInfo(get_phase2_client_cert_uri), 'get_phase2_domain_suffix_match': gi.FunctionInfo(get_phase2_domain_suffix_match), 'get_phase2_private_key_blob': gi.FunctionInfo(get_phase2_private_key_blob), 'get_phase2_private_key_format': gi.FunctionInfo(get_phase2_private_key_format), 'get_phase2_private_key_password': gi.FunctionInfo(get_phase2_private_key_password), 'get_phase2_private_key_password_flags': gi.FunctionInfo(get_phase2_private_key_password_flags), 'get_phase2_private_key_path': gi.FunctionInfo(get_phase2_private_key_path), 'get_phase2_private_key_scheme': gi.FunctionInfo(get_phase2_private_key_scheme), 'get_phase2_private_key_uri': gi.FunctionInfo(get_phase2_private_key_uri), 'get_phase2_subject_match': gi.FunctionInfo(get_phase2_subject_match), 'get_pin': gi.FunctionInfo(get_pin), 'get_pin_flags': gi.FunctionInfo(get_pin_flags), 'get_private_key_blob': gi.FunctionInfo(get_private_key_blob), 'get_private_key_format': gi.FunctionInfo(get_private_key_format), 'get_private_key_password': gi.FunctionInfo(get_private_key_password), 'get_private_key_password_flags': gi.FunctionInfo(get_private_key_password_flags), 'get_private_key_path': gi.FunctionInfo(get_private_key_path), 'get_private_key_scheme': gi.FunctionInfo(get_private_key_scheme), 'get_private_key_uri': gi.FunctionInfo(get_private_key_uri), 'get_subject_match': gi.FunctionInfo(get_subject_match), 'get_system_ca_certs': gi.FunctionInfo(get_system_ca_certs), 'remove_altsubject_match': gi.FunctionInfo(remove_altsubject_match), 'remove_altsubject_match_by_value': gi.FunctionInfo(remove_altsubject_match_by_value), 'remove_eap_method': gi.FunctionInfo(remove_eap_method), 'remove_eap_method_by_value': gi.FunctionInfo(remove_eap_method_by_value), 'remove_phase2_altsubject_match': gi.FunctionInfo(remove_phase2_altsubject_match), 'remove_phase2_altsubject_match_by_value': gi.FunctionInfo(remove_phase2_altsubject_match_by_value), 'set_ca_cert': gi.FunctionInfo(set_ca_cert), 'set_client_cert': gi.FunctionInfo(set_client_cert), 'set_phase2_ca_cert': gi.FunctionInfo(set_phase2_ca_cert), 'set_phase2_client_cert': gi.FunctionInfo(set_phase2_client_cert), 'set_phase2_private_key': gi.FunctionInfo(set_phase2_private_key), 'set_private_key': gi.FunctionInfo(set_private_key), 'parent': <property object at 0x7fb9b84dcef0>})"
    __gdoc__ = 'Object NMSetting8021x\n\nProperties from NMSetting8021x:\n  eap -> GStrv: \n    \n  identity -> gchararray: \n    \n  anonymous-identity -> gchararray: \n    \n  pac-file -> gchararray: \n    \n  ca-cert -> GBytes: \n    \n  ca-cert-password -> gchararray: \n    \n  ca-cert-password-flags -> NMSettingSecretFlags: \n    \n  ca-path -> gchararray: \n    \n  subject-match -> gchararray: \n    \n  altsubject-matches -> GStrv: \n    \n  domain-suffix-match -> gchararray: \n    \n  client-cert -> GBytes: \n    \n  client-cert-password -> gchararray: \n    \n  client-cert-password-flags -> NMSettingSecretFlags: \n    \n  phase1-peapver -> gchararray: \n    \n  phase1-peaplabel -> gchararray: \n    \n  phase1-fast-provisioning -> gchararray: \n    \n  phase1-auth-flags -> guint: \n    \n  phase2-auth -> gchararray: \n    \n  phase2-autheap -> gchararray: \n    \n  phase2-ca-cert -> GBytes: \n    \n  phase2-ca-cert-password -> gchararray: \n    \n  phase2-ca-cert-password-flags -> NMSettingSecretFlags: \n    \n  phase2-ca-path -> gchararray: \n    \n  phase2-subject-match -> gchararray: \n    \n  phase2-altsubject-matches -> GStrv: \n    \n  phase2-domain-suffix-match -> gchararray: \n    \n  phase2-client-cert -> GBytes: \n    \n  phase2-client-cert-password -> gchararray: \n    \n  phase2-client-cert-password-flags -> NMSettingSecretFlags: \n    \n  password -> gchararray: \n    \n  password-flags -> NMSettingSecretFlags: \n    \n  password-raw -> GBytes: \n    \n  password-raw-flags -> NMSettingSecretFlags: \n    \n  private-key -> GBytes: \n    \n  private-key-password -> gchararray: \n    \n  private-key-password-flags -> NMSettingSecretFlags: \n    \n  phase2-private-key -> GBytes: \n    \n  phase2-private-key-password -> gchararray: \n    \n  phase2-private-key-password-flags -> NMSettingSecretFlags: \n    \n  pin -> gchararray: \n    \n  pin-flags -> NMSettingSecretFlags: \n    \n  system-ca-certs -> gboolean: \n    \n  optional -> gboolean: \n    \n  auth-timeout -> gint: \n    \n\nProperties from NMSetting:\n  name -> gchararray: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMSetting8021x (94741104348304)>'
    __info__ = ObjectInfo(Setting8021x)


