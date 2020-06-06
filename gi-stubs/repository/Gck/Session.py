# encoding: utf-8
# module gi.repository.Gck
# from /usr/lib64/girepository-1.0/Gck-1.typelib
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


class Session(__gi_overrides_GObject.Object, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        Session(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

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

    def create_object(self, attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ create_object(self, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> Gck.Object """
        pass

    def create_object_async(self, attrs, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_object_async(self, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_object_finish(self, result): # real signature unknown; restored from __doc__
        """ create_object_finish(self, result:Gio.AsyncResult) -> Gck.Object """
        pass

    def decrypt(self, key, mech_type, input, cancellable=None): # real signature unknown; restored from __doc__
        """ decrypt(self, key:Gck.Object, mech_type:int, input:list, cancellable:Gio.Cancellable=None) -> list, n_result:int """
        return []

    def decrypt_async(self, key, mechanism, input, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ decrypt_async(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def decrypt_finish(self, result): # real signature unknown; restored from __doc__
        """ decrypt_finish(self, result:Gio.AsyncResult) -> list, n_result:int """
        return []

    def decrypt_full(self, key, mechanism, input, cancellable=None): # real signature unknown; restored from __doc__
        """ decrypt_full(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, cancellable:Gio.Cancellable=None) -> list, n_result:int """
        return []

    def derive_key(self, base, mech_type, attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ derive_key(self, base:Gck.Object, mech_type:int, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> Gck.Object """
        pass

    def derive_key_async(self, base, mechanism, attrs, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ derive_key_async(self, base:Gck.Object, mechanism:Gck.Mechanism, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def derive_key_finish(self, result): # real signature unknown; restored from __doc__
        """ derive_key_finish(self, result:Gio.AsyncResult) -> Gck.Object """
        pass

    def derive_key_full(self, base, mechanism, attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ derive_key_full(self, base:Gck.Object, mechanism:Gck.Mechanism, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> Gck.Object """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def encrypt(self, key, mech_type, input, cancellable=None): # real signature unknown; restored from __doc__
        """ encrypt(self, key:Gck.Object, mech_type:int, input:list, cancellable:Gio.Cancellable=None) -> list, n_result:int """
        return []

    def encrypt_async(self, key, mechanism, input, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ encrypt_async(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def encrypt_finish(self, result): # real signature unknown; restored from __doc__
        """ encrypt_finish(self, result:Gio.AsyncResult) -> list, n_result:int """
        return []

    def encrypt_full(self, key, mechanism, input, cancellable=None): # real signature unknown; restored from __doc__
        """ encrypt_full(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, cancellable:Gio.Cancellable=None) -> list, n_result:int """
        return []

    def enumerate_objects(self, match): # real signature unknown; restored from __doc__
        """ enumerate_objects(self, match:Gck.Attributes) -> Gck.Enumerator """
        pass

    def find_handles(self, match, cancellable=None): # real signature unknown; restored from __doc__
        """ find_handles(self, match:Gck.Attributes, cancellable:Gio.Cancellable=None) -> list or None, n_handles:int """
        return []

    def find_handles_async(self, match, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_handles_async(self, match:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_handles_finish(self, result): # real signature unknown; restored from __doc__
        """ find_handles_finish(self, result:Gio.AsyncResult) -> list or None, n_handles:int """
        return []

    def find_objects(self, match, cancellable=None): # real signature unknown; restored from __doc__
        """ find_objects(self, match:Gck.Attributes, cancellable:Gio.Cancellable=None) -> list """
        return []

    def find_objects_async(self, match, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_objects_async(self, match:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ find_objects_finish(self, result:Gio.AsyncResult) -> list """
        return []

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

    def from_handle(self, slot, session_handle, options): # real signature unknown; restored from __doc__
        """ from_handle(slot:Gck.Slot, session_handle:int, options:Gck.SessionOptions) -> Gck.Session """
        pass

    def generate_key_pair(self, mech_type, public_attrs, private_attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ generate_key_pair(self, mech_type:int, public_attrs:Gck.Attributes, private_attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> bool, public_key:Gck.Object, private_key:Gck.Object """
        return False

    def generate_key_pair_async(self, mechanism, public_attrs, private_attrs, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ generate_key_pair_async(self, mechanism:Gck.Mechanism, public_attrs:Gck.Attributes, private_attrs:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def generate_key_pair_finish(self, result): # real signature unknown; restored from __doc__
        """ generate_key_pair_finish(self, result:Gio.AsyncResult) -> bool, public_key:Gck.Object, private_key:Gck.Object """
        return False

    def generate_key_pair_full(self, mechanism, public_attrs, private_attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ generate_key_pair_full(self, mechanism:Gck.Mechanism, public_attrs:Gck.Attributes, private_attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> bool, public_key:Gck.Object, private_key:Gck.Object """
        return False

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_handle(self): # real signature unknown; restored from __doc__
        """ get_handle(self) -> int """
        return 0

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> Gck.SessionInfo """
        pass

    def get_interaction(self): # real signature unknown; restored from __doc__
        """ get_interaction(self) -> Gio.TlsInteraction or None """
        pass

    def get_module(self): # real signature unknown; restored from __doc__
        """ get_module(self) -> Gck.Module """
        pass

    def get_options(self): # real signature unknown; restored from __doc__
        """ get_options(self) -> Gck.SessionOptions """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_slot(self): # real signature unknown; restored from __doc__
        """ get_slot(self) -> Gck.Slot """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> int """
        return 0

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

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_finish(self, res): # real signature unknown; restored from __doc__
        """ init_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def init_pin(self, pin=None, cancellable=None): # real signature unknown; restored from __doc__
        """ init_pin(self, pin:list=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_pin_async(self, pin=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_pin_async(self, pin:list=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_pin_finish(self, result): # real signature unknown; restored from __doc__
        """ init_pin_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    def login(self, user_type, pin=None, cancellable=None): # real signature unknown; restored from __doc__
        """ login(self, user_type:int, pin:list=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def login_async(self, user_type, pin=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ login_async(self, user_type:int, pin:list=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def login_finish(self, result): # real signature unknown; restored from __doc__
        """ login_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def login_interactive(self, user_type, interaction=None, cancellable=None): # real signature unknown; restored from __doc__
        """ login_interactive(self, user_type:int, interaction:Gio.TlsInteraction=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def login_interactive_async(self, user_type, interaction=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ login_interactive_async(self, user_type:int, interaction:Gio.TlsInteraction=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def login_interactive_finish(self, result): # real signature unknown; restored from __doc__
        """ login_interactive_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def logout(self, cancellable=None): # real signature unknown; restored from __doc__
        """ logout(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def logout_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ logout_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def logout_finish(self, result): # real signature unknown; restored from __doc__
        """ logout_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, res): # real signature unknown; restored from __doc__
        """ new_finish(self, res:Gio.AsyncResult) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open(self, slot, options, interaction=None, cancellable=None): # real signature unknown; restored from __doc__
        """ open(slot:Gck.Slot, options:Gck.SessionOptions, interaction:Gio.TlsInteraction=None, cancellable:Gio.Cancellable=None) -> Gck.Session """
        pass

    def open_async(self, slot, options, interaction=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_async(slot:Gck.Slot, options:Gck.SessionOptions, interaction:Gio.TlsInteraction=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(result:Gio.AsyncResult) -> Gck.Session """
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

    def set_interaction(self, interaction=None): # real signature unknown; restored from __doc__
        """ set_interaction(self, interaction:Gio.TlsInteraction=None) """
        pass

    def set_pin(self, old_pin=None, new_pin=None, cancellable=None): # real signature unknown; restored from __doc__
        """ set_pin(self, old_pin:list=None, new_pin:list=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_pin_async(self, old_pin=None, n_old_pin, new_pin=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_pin_async(self, old_pin:list=None, n_old_pin:int, new_pin:list=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_pin_finish(self, result): # real signature unknown; restored from __doc__
        """ set_pin_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def sign(self, key, mech_type, input, cancellable=None): # real signature unknown; restored from __doc__
        """ sign(self, key:Gck.Object, mech_type:int, input:list, cancellable:Gio.Cancellable=None) -> list, n_result:int """
        return []

    def sign_async(self, key, mechanism, input, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ sign_async(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def sign_finish(self, result): # real signature unknown; restored from __doc__
        """ sign_finish(self, result:Gio.AsyncResult) -> list, n_result:int """
        return []

    def sign_full(self, key, mechanism, input, n_result, cancellable=None): # real signature unknown; restored from __doc__
        """ sign_full(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, n_result:int, cancellable:Gio.Cancellable=None) -> int """
        return 0

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

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unwrap_key(self, wrapper, mech_type, input, attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ unwrap_key(self, wrapper:Gck.Object, mech_type:int, input:list, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> Gck.Object """
        pass

    def unwrap_key_async(self, wrapper, mechanism, input, attrs, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unwrap_key_async(self, wrapper:Gck.Object, mechanism:Gck.Mechanism, input:list, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unwrap_key_finish(self, result): # real signature unknown; restored from __doc__
        """ unwrap_key_finish(self, result:Gio.AsyncResult) -> Gck.Object """
        pass

    def unwrap_key_full(self, wrapper, mechanism, input, attrs, cancellable=None): # real signature unknown; restored from __doc__
        """ unwrap_key_full(self, wrapper:Gck.Object, mechanism:Gck.Mechanism, input:list, attrs:Gck.Attributes, cancellable:Gio.Cancellable=None) -> Gck.Object """
        pass

    def verify(self, key, mech_type, input, signature, cancellable=None): # real signature unknown; restored from __doc__
        """ verify(self, key:Gck.Object, mech_type:int, input:list, signature:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def verify_async(self, key, mechanism, input, signature, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ verify_async(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, signature:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def verify_finish(self, result): # real signature unknown; restored from __doc__
        """ verify_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def verify_full(self, key, mechanism, input, signature, cancellable=None): # real signature unknown; restored from __doc__
        """ verify_full(self, key:Gck.Object, mechanism:Gck.Mechanism, input:list, signature:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def wrap_key(self, wrapper, mech_type, wrapped, cancellable=None): # real signature unknown; restored from __doc__
        """ wrap_key(self, wrapper:Gck.Object, mech_type:int, wrapped:Gck.Object, cancellable:Gio.Cancellable=None) -> list, n_result:int """
        return []

    def wrap_key_async(self, wrapper, mechanism, wrapped, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ wrap_key_async(self, wrapper:Gck.Object, mechanism:Gck.Mechanism, wrapped:Gck.Object, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def wrap_key_finish(self, result): # real signature unknown; restored from __doc__
        """ wrap_key_finish(self, result:Gio.AsyncResult) -> list, n_result:int """
        return []

    def wrap_key_full(self, wrapper, mechanism, wrapped, cancellable=None): # real signature unknown; restored from __doc__
        """ wrap_key_full(self, wrapper:Gck.Object, mechanism:Gck.Mechanism, wrapped:Gck.Object, cancellable:Gio.Cancellable=None) -> list, n_result:int """
        return []

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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc2e611e400>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Session), '__module__': 'gi.repository.Gck', '__gtype__': <GType GckSession (94702128037216)>, '__doc__': None, '__gsignals__': {}, 'from_handle': gi.FunctionInfo(from_handle), 'open': gi.FunctionInfo(open), 'open_async': gi.FunctionInfo(open_async), 'open_finish': gi.FunctionInfo(open_finish), 'create_object': gi.FunctionInfo(create_object), 'create_object_async': gi.FunctionInfo(create_object_async), 'create_object_finish': gi.FunctionInfo(create_object_finish), 'decrypt': gi.FunctionInfo(decrypt), 'decrypt_async': gi.FunctionInfo(decrypt_async), 'decrypt_finish': gi.FunctionInfo(decrypt_finish), 'decrypt_full': gi.FunctionInfo(decrypt_full), 'derive_key': gi.FunctionInfo(derive_key), 'derive_key_async': gi.FunctionInfo(derive_key_async), 'derive_key_finish': gi.FunctionInfo(derive_key_finish), 'derive_key_full': gi.FunctionInfo(derive_key_full), 'encrypt': gi.FunctionInfo(encrypt), 'encrypt_async': gi.FunctionInfo(encrypt_async), 'encrypt_finish': gi.FunctionInfo(encrypt_finish), 'encrypt_full': gi.FunctionInfo(encrypt_full), 'enumerate_objects': gi.FunctionInfo(enumerate_objects), 'find_handles': gi.FunctionInfo(find_handles), 'find_handles_async': gi.FunctionInfo(find_handles_async), 'find_handles_finish': gi.FunctionInfo(find_handles_finish), 'find_objects': gi.FunctionInfo(find_objects), 'find_objects_async': gi.FunctionInfo(find_objects_async), 'find_objects_finish': gi.FunctionInfo(find_objects_finish), 'generate_key_pair': gi.FunctionInfo(generate_key_pair), 'generate_key_pair_async': gi.FunctionInfo(generate_key_pair_async), 'generate_key_pair_finish': gi.FunctionInfo(generate_key_pair_finish), 'generate_key_pair_full': gi.FunctionInfo(generate_key_pair_full), 'get_handle': gi.FunctionInfo(get_handle), 'get_info': gi.FunctionInfo(get_info), 'get_interaction': gi.FunctionInfo(get_interaction), 'get_module': gi.FunctionInfo(get_module), 'get_options': gi.FunctionInfo(get_options), 'get_slot': gi.FunctionInfo(get_slot), 'get_state': gi.FunctionInfo(get_state), 'init_pin': gi.FunctionInfo(init_pin), 'init_pin_async': gi.FunctionInfo(init_pin_async), 'init_pin_finish': gi.FunctionInfo(init_pin_finish), 'login': gi.FunctionInfo(login), 'login_async': gi.FunctionInfo(login_async), 'login_finish': gi.FunctionInfo(login_finish), 'login_interactive': gi.FunctionInfo(login_interactive), 'login_interactive_async': gi.FunctionInfo(login_interactive_async), 'login_interactive_finish': gi.FunctionInfo(login_interactive_finish), 'logout': gi.FunctionInfo(logout), 'logout_async': gi.FunctionInfo(logout_async), 'logout_finish': gi.FunctionInfo(logout_finish), 'set_interaction': gi.FunctionInfo(set_interaction), 'set_pin': gi.FunctionInfo(set_pin), 'set_pin_async': gi.FunctionInfo(set_pin_async), 'set_pin_finish': gi.FunctionInfo(set_pin_finish), 'sign': gi.FunctionInfo(sign), 'sign_async': gi.FunctionInfo(sign_async), 'sign_finish': gi.FunctionInfo(sign_finish), 'sign_full': gi.FunctionInfo(sign_full), 'unwrap_key': gi.FunctionInfo(unwrap_key), 'unwrap_key_async': gi.FunctionInfo(unwrap_key_async), 'unwrap_key_finish': gi.FunctionInfo(unwrap_key_finish), 'unwrap_key_full': gi.FunctionInfo(unwrap_key_full), 'verify': gi.FunctionInfo(verify), 'verify_async': gi.FunctionInfo(verify_async), 'verify_finish': gi.FunctionInfo(verify_finish), 'verify_full': gi.FunctionInfo(verify_full), 'wrap_key': gi.FunctionInfo(wrap_key), 'wrap_key_async': gi.FunctionInfo(wrap_key_async), 'wrap_key_finish': gi.FunctionInfo(wrap_key_finish), 'wrap_key_full': gi.FunctionInfo(wrap_key_full), 'parent': <property object at 0x7fc2e6151090>, 'pv': <property object at 0x7fc2e6151180>, 'reserved': <property object at 0x7fc2e6151270>})"
    __gdoc__ = 'Object GckSession\n\nSignals from GckSession:\n  discard-handle (gulong) -> gboolean\n\nProperties from GckSession:\n  module -> GckModule: Module\n    PKCS11 Module\n  handle -> gulong: Session Handle\n    PKCS11 Session Handle\n  interaction -> GTlsInteraction: Interaction\n    Interaction asking for pins\n  slot -> GckSlot: Slot that this session uses\n    PKCS11 Slot\n  options -> GckSessionOptions: Session Options\n    Session Options\n  opening-flags -> gulong: Opening flags\n    PKCS#11 open session flags\n  app-data -> gpointer: App data\n    PKCS#11 application data\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GckSession (94702128037216)>'
    __info__ = ObjectInfo(Session)


