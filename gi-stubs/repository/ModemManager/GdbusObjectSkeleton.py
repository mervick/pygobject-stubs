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


from .GdbusObject import GdbusObject

class GdbusObjectSkeleton(__gi_repository_Gio.DBusObjectSkeleton, GdbusObject):
    """
    :Constructors:
    
    ::
    
        GdbusObjectSkeleton(**properties)
        new(object_path:str) -> ModemManager.GdbusObjectSkeleton
    """
    def add_interface(self, interface_): # real signature unknown; restored from __doc__
        """ add_interface(self, interface_:Gio.DBusInterfaceSkeleton) """
        pass

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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authorize_method(self, *args, **kwargs): # real signature unknown
        """ authorize_method(self, interface_:Gio.DBusInterfaceSkeleton, invocation:Gio.DBusMethodInvocation) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_interface(self, interface_name): # real signature unknown; restored from __doc__
        """ get_interface(self, interface_name:str) -> Gio.DBusInterface """
        pass

    def get_interfaces(self): # real signature unknown; restored from __doc__
        """ get_interfaces(self) -> list """
        return []

    def get_modem(self): # real signature unknown; restored from __doc__
        """ get_modem(self) -> ModemManager.GdbusModem or None """
        pass

    def get_modem3gpp(self): # real signature unknown; restored from __doc__
        """ get_modem3gpp(self) -> ModemManager.GdbusModem3gpp or None """
        pass

    def get_modem3gpp_ussd(self): # real signature unknown; restored from __doc__
        """ get_modem3gpp_ussd(self) -> ModemManager.GdbusModem3gppUssd or None """
        pass

    def get_modem_cdma(self): # real signature unknown; restored from __doc__
        """ get_modem_cdma(self) -> ModemManager.GdbusModemCdma or None """
        pass

    def get_modem_firmware(self): # real signature unknown; restored from __doc__
        """ get_modem_firmware(self) -> ModemManager.GdbusModemFirmware or None """
        pass

    def get_modem_location(self): # real signature unknown; restored from __doc__
        """ get_modem_location(self) -> ModemManager.GdbusModemLocation or None """
        pass

    def get_modem_messaging(self): # real signature unknown; restored from __doc__
        """ get_modem_messaging(self) -> ModemManager.GdbusModemMessaging or None """
        pass

    def get_modem_oma(self): # real signature unknown; restored from __doc__
        """ get_modem_oma(self) -> ModemManager.GdbusModemOma or None """
        pass

    def get_modem_signal(self): # real signature unknown; restored from __doc__
        """ get_modem_signal(self) -> ModemManager.GdbusModemSignal or None """
        pass

    def get_modem_simple(self): # real signature unknown; restored from __doc__
        """ get_modem_simple(self) -> ModemManager.GdbusModemSimple or None """
        pass

    def get_modem_time(self): # real signature unknown; restored from __doc__
        """ get_modem_time(self) -> ModemManager.GdbusModemTime or None """
        pass

    def get_modem_voice(self): # real signature unknown; restored from __doc__
        """ get_modem_voice(self) -> ModemManager.GdbusModemVoice or None """
        pass

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
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

    def new(self, object_path): # real signature unknown; restored from __doc__
        """ new(object_path:str) -> ModemManager.GdbusObjectSkeleton """
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

    def remove_interface(self, interface_): # real signature unknown; restored from __doc__
        """ remove_interface(self, interface_:Gio.DBusInterfaceSkeleton) """
        pass

    def remove_interface_by_name(self, interface_name): # real signature unknown; restored from __doc__
        """ remove_interface_by_name(self, interface_name:str) """
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

    def set_modem(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem(self, interface_:ModemManager.GdbusModem=None) """
        pass

    def set_modem3gpp(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem3gpp(self, interface_:ModemManager.GdbusModem3gpp=None) """
        pass

    def set_modem3gpp_ussd(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem3gpp_ussd(self, interface_:ModemManager.GdbusModem3gppUssd=None) """
        pass

    def set_modem_cdma(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_cdma(self, interface_:ModemManager.GdbusModemCdma=None) """
        pass

    def set_modem_firmware(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_firmware(self, interface_:ModemManager.GdbusModemFirmware=None) """
        pass

    def set_modem_location(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_location(self, interface_:ModemManager.GdbusModemLocation=None) """
        pass

    def set_modem_messaging(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_messaging(self, interface_:ModemManager.GdbusModemMessaging=None) """
        pass

    def set_modem_oma(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_oma(self, interface_:ModemManager.GdbusModemOma=None) """
        pass

    def set_modem_signal(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_signal(self, interface_:ModemManager.GdbusModemSignal=None) """
        pass

    def set_modem_simple(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_simple(self, interface_:ModemManager.GdbusModemSimple=None) """
        pass

    def set_modem_time(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_time(self, interface_:ModemManager.GdbusModemTime=None) """
        pass

    def set_modem_voice(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_modem_voice(self, interface_:ModemManager.GdbusModemVoice=None) """
        pass

    def set_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ set_object_path(self, object_path:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f694351aaf0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(GdbusObjectSkeleton), '__module__': 'gi.repository.ModemManager', '__gtype__': <GType MmGdbusObjectSkeleton (94631948525904)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'set_modem': gi.FunctionInfo(set_modem), 'set_modem3gpp': gi.FunctionInfo(set_modem3gpp), 'set_modem3gpp_ussd': gi.FunctionInfo(set_modem3gpp_ussd), 'set_modem_cdma': gi.FunctionInfo(set_modem_cdma), 'set_modem_firmware': gi.FunctionInfo(set_modem_firmware), 'set_modem_location': gi.FunctionInfo(set_modem_location), 'set_modem_messaging': gi.FunctionInfo(set_modem_messaging), 'set_modem_oma': gi.FunctionInfo(set_modem_oma), 'set_modem_signal': gi.FunctionInfo(set_modem_signal), 'set_modem_simple': gi.FunctionInfo(set_modem_simple), 'set_modem_time': gi.FunctionInfo(set_modem_time), 'set_modem_voice': gi.FunctionInfo(set_modem_voice), 'parent_instance': <property object at 0x7f694388b860>, 'priv': <property object at 0x7f694388b950>})"
    __gdoc__ = 'Object MmGdbusObjectSkeleton\n\nSignals from GDBusObject:\n  interface-added (GDBusInterface)\n  interface-removed (GDBusInterface)\n\nSignals from GDBusObjectSkeleton:\n  authorize-method (GDBusInterfaceSkeleton, GDBusMethodInvocation) -> gboolean\n\nProperties from GDBusObjectSkeleton:\n  g-object-path -> gchararray: Object Path\n    The object path where the object is exported\n\nSignals from GDBusObject:\n  interface-added (GDBusInterface)\n  interface-removed (GDBusInterface)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType MmGdbusObjectSkeleton (94631948525904)>'
    __info__ = ObjectInfo(GdbusObjectSkeleton)


