# encoding: utf-8
# module gi.repository.ModemManager
# from /usr/lib64/girepository-1.0/ModemManager-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .GdbusModem import GdbusModem

class GdbusModemSkeleton(__gi_repository_Gio.DBusInterfaceSkeleton, GdbusModem):
    """
    :Constructors:
    
    ::
    
        GdbusModemSkeleton(**properties)
        new() -> ModemManager.GdbusModemSkeleton
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def call_command(self, arg_cmd, arg_timeout, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_command(self, arg_cmd:str, arg_timeout:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_command_finish(self, res): # real signature unknown; restored from __doc__
        """ call_command_finish(self, res:Gio.AsyncResult) -> out_response:str """
        pass

    def call_command_sync(self, arg_cmd, arg_timeout, cancellable=None): # real signature unknown; restored from __doc__
        """ call_command_sync(self, arg_cmd:str, arg_timeout:int, cancellable:Gio.Cancellable=None) -> out_response:str """
        pass

    def call_create_bearer(self, arg_properties, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_create_bearer(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_create_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ call_create_bearer_finish(self, res:Gio.AsyncResult) -> out_path:str """
        pass

    def call_create_bearer_sync(self, arg_properties, cancellable=None): # real signature unknown; restored from __doc__
        """ call_create_bearer_sync(self, arg_properties:GLib.Variant, cancellable:Gio.Cancellable=None) -> out_path:str """
        pass

    def call_delete_bearer(self, arg_bearer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_delete_bearer(self, arg_bearer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_delete_bearer_finish(self, res): # real signature unknown; restored from __doc__
        """ call_delete_bearer_finish(self, res:Gio.AsyncResult) """
        pass

    def call_delete_bearer_sync(self, arg_bearer, cancellable=None): # real signature unknown; restored from __doc__
        """ call_delete_bearer_sync(self, arg_bearer:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_enable(self, arg_enable, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_enable(self, arg_enable:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_enable_finish(self, res): # real signature unknown; restored from __doc__
        """ call_enable_finish(self, res:Gio.AsyncResult) """
        pass

    def call_enable_sync(self, arg_enable, cancellable=None): # real signature unknown; restored from __doc__
        """ call_enable_sync(self, arg_enable:bool, cancellable:Gio.Cancellable=None) """
        pass

    def call_factory_reset(self, arg_code, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_factory_reset(self, arg_code:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_factory_reset_finish(self, res): # real signature unknown; restored from __doc__
        """ call_factory_reset_finish(self, res:Gio.AsyncResult) """
        pass

    def call_factory_reset_sync(self, arg_code, cancellable=None): # real signature unknown; restored from __doc__
        """ call_factory_reset_sync(self, arg_code:str, cancellable:Gio.Cancellable=None) """
        pass

    def call_list_bearers(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_list_bearers(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_list_bearers_finish(self, res): # real signature unknown; restored from __doc__
        """ call_list_bearers_finish(self, res:Gio.AsyncResult) -> out_bearers:list """
        pass

    def call_list_bearers_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_list_bearers_sync(self, cancellable:Gio.Cancellable=None) -> out_bearers:list """
        pass

    def call_reset(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_reset(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_reset_finish(self, res): # real signature unknown; restored from __doc__
        """ call_reset_finish(self, res:Gio.AsyncResult) """
        pass

    def call_reset_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ call_reset_sync(self, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_bands(self, arg_bands, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_bands(self, arg_bands:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_bands_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_bands_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_bands_sync(self, arg_bands, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_bands_sync(self, arg_bands:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_capabilities(self, arg_capabilities, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities(self, arg_capabilities:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_capabilities_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_capabilities_sync(self, arg_capabilities, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_capabilities_sync(self, arg_capabilities:int, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_current_modes(self, arg_modes, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_current_modes(self, arg_modes:GLib.Variant, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_current_modes_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_current_modes_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_current_modes_sync(self, arg_modes, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_current_modes_sync(self, arg_modes:GLib.Variant, cancellable:Gio.Cancellable=None) """
        pass

    def call_set_power_state(self, arg_state, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call_set_power_state(self, arg_state:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_set_power_state_finish(self, res): # real signature unknown; restored from __doc__
        """ call_set_power_state_finish(self, res:Gio.AsyncResult) """
        pass

    def call_set_power_state_sync(self, arg_state, cancellable=None): # real signature unknown; restored from __doc__
        """ call_set_power_state_sync(self, arg_state:int, cancellable:Gio.Cancellable=None) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def complete_command(self, invocation, response): # real signature unknown; restored from __doc__
        """ complete_command(self, invocation:Gio.DBusMethodInvocation, response:str) """
        pass

    def complete_create_bearer(self, invocation, path): # real signature unknown; restored from __doc__
        """ complete_create_bearer(self, invocation:Gio.DBusMethodInvocation, path:str) """
        pass

    def complete_delete_bearer(self, invocation): # real signature unknown; restored from __doc__
        """ complete_delete_bearer(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_enable(self, invocation): # real signature unknown; restored from __doc__
        """ complete_enable(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_factory_reset(self, invocation): # real signature unknown; restored from __doc__
        """ complete_factory_reset(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_list_bearers(self, invocation, bearers): # real signature unknown; restored from __doc__
        """ complete_list_bearers(self, invocation:Gio.DBusMethodInvocation, bearers:str) """
        pass

    def complete_reset(self, invocation): # real signature unknown; restored from __doc__
        """ complete_reset(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_bands(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_bands(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_capabilities(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_capabilities(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_current_modes(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_current_modes(self, invocation:Gio.DBusMethodInvocation) """
        pass

    def complete_set_power_state(self, invocation): # real signature unknown; restored from __doc__
        """ complete_set_power_state(self, invocation:Gio.DBusMethodInvocation) """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_flush(self, *args, **kwargs): # real signature unknown
        """ flush(self) """
        pass

    def do_get_info(self, *args, **kwargs): # real signature unknown
        """ get_info(self) -> Gio.DBusInterfaceInfo """
        pass

    def do_get_properties(self, *args, **kwargs): # real signature unknown
        """ get_properties(self) -> GLib.Variant """
        pass

    def do_g_authorize_method(self, *args, **kwargs): # real signature unknown
        """ g_authorize_method(self, invocation:Gio.DBusMethodInvocation) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_state_changed(self, arg_old, arg_new, arg_reason): # real signature unknown; restored from __doc__
        """ emit_state_changed(self, arg_old:int, arg_new:int, arg_reason:int) """
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def export(self, connection, object_path): # real signature unknown; restored from __doc__
        """ export(self, connection:Gio.DBusConnection, object_path:str) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
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

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_connections(self): # real signature unknown; restored from __doc__
        """ get_connections(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.DBusInterfaceSkeletonFlags """
        pass

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> Gio.DBusInterfaceInfo """
        pass

    def get_object(self): # real signature unknown; restored from __doc__
        """ get_object(self) -> Gio.DBusObject """
        pass

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_properties(self): # real signature unknown; restored from __doc__
        """ get_properties(self) -> GLib.Variant """
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def has_connection(self, connection): # real signature unknown; restored from __doc__
        """ has_connection(self, connection:Gio.DBusConnection) -> bool """
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

    def interface_info(self): # real signature unknown; restored from __doc__
        """ interface_info() -> Gio.DBusInterfaceInfo """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ModemManager.GdbusModemSkeleton """
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

    def override_properties(self, klass, property_id_begin): # real signature unknown; restored from __doc__
        """ override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
        return 0

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

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Gio.DBusInterfaceSkeletonFlags) """
        pass

    def set_object(self, p_object=None): # real signature unknown; restored from __doc__
        """ set_object(self, object:Gio.DBusObject=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    def unexport(self): # real signature unknown; restored from __doc__
        """ unexport(self) """
        pass

    def unexport_from_connection(self, connection): # real signature unknown; restored from __doc__
        """ unexport_from_connection(self, connection:Gio.DBusConnection) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f6943588a90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(GdbusModemSkeleton), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusModemSkeleton (94631948449504)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent_instance': <property object at 0x7f69438fcbd0>, 'priv': <property object at 0x7f69438fcd10>})"
    __gdoc__ = 'Object MmGdbusModemSkeleton\n\nSignals from MmGdbusModem:\n  state-changed (gint, gint, guint)\n  handle-enable (GDBusMethodInvocation, gboolean) -> gboolean\n  handle-list-bearers (GDBusMethodInvocation) -> gboolean\n  handle-create-bearer (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-delete-bearer (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-reset (GDBusMethodInvocation) -> gboolean\n  handle-factory-reset (GDBusMethodInvocation, gchararray) -> gboolean\n  handle-set-power-state (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-current-capabilities (GDBusMethodInvocation, guint) -> gboolean\n  handle-set-current-modes (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-set-current-bands (GDBusMethodInvocation, GVariant) -> gboolean\n  handle-command (GDBusMethodInvocation, gchararray, guint) -> gboolean\n\nSignals from GDBusInterfaceSkeleton:\n  g-authorize-method (GDBusMethodInvocation) -> gboolean\n\nProperties from GDBusInterfaceSkeleton:\n  g-flags -> GDBusInterfaceSkeletonFlags: g-flags\n    Flags for the interface skeleton\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusModemSkeleton (94631948449504)>'
    __info__ = ObjectInfo(GdbusModemSkeleton)


