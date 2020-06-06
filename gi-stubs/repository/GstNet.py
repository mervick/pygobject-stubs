# encoding: utf-8
# module gi.repository.GstNet
# from /usr/lib64/girepository-1.0/GstNet-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.Gst as __gi_repository_Gst


# Variables with simple values

NET_TIME_PACKET_SIZE = 16

PTP_CLOCK_ID_NONE = 18446744073709551615

PTP_STATISTICS_BEST_MASTER_CLOCK_SELECTED = 'GstPtpStatisticsBestMasterClockSelected'

PTP_STATISTICS_NEW_DOMAIN_FOUND = 'GstPtpStatisticsNewDomainFound'

PTP_STATISTICS_PATH_DELAY_MEASURED = 'GstPtpStatisticsPathDelayMeasured'

PTP_STATISTICS_TIME_UPDATED = 'GstPtpStatisticsTimeUpdated'

_namespace = 'GstNet'

_version = '1.0'

__weakref__ = None

# functions

def buffer_add_net_address_meta(buffer, addr): # real signature unknown; restored from __doc__
    """ buffer_add_net_address_meta(buffer:Gst.Buffer, addr:Gio.SocketAddress) -> GstNet.NetAddressMeta """
    pass

def buffer_add_net_control_message_meta(buffer, message): # real signature unknown; restored from __doc__
    """ buffer_add_net_control_message_meta(buffer:Gst.Buffer, message:Gio.SocketControlMessage) -> GstNet.NetControlMessageMeta """
    pass

def buffer_get_net_address_meta(buffer): # real signature unknown; restored from __doc__
    """ buffer_get_net_address_meta(buffer:Gst.Buffer) -> GstNet.NetAddressMeta """
    pass

def net_address_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ net_address_meta_api_get_type() -> GType """
    pass

def net_address_meta_get_info(): # real signature unknown; restored from __doc__
    """ net_address_meta_get_info() -> Gst.MetaInfo """
    pass

def net_control_message_meta_api_get_type(): # real signature unknown; restored from __doc__
    """ net_control_message_meta_api_get_type() -> GType """
    pass

def net_control_message_meta_get_info(): # real signature unknown; restored from __doc__
    """ net_control_message_meta_get_info() -> Gst.MetaInfo """
    pass

def net_time_packet_receive(socket): # real signature unknown; restored from __doc__
    """ net_time_packet_receive(socket:Gio.Socket) -> GstNet.NetTimePacket, src_address:Gio.SocketAddress """
    pass

def ptp_deinit(): # real signature unknown; restored from __doc__
    """ ptp_deinit() """
    pass

def ptp_init(clock_id, interfaces=None): # real signature unknown; restored from __doc__
    """ ptp_init(clock_id:int, interfaces:list=None) -> bool """
    return False

def ptp_is_initialized(): # real signature unknown; restored from __doc__
    """ ptp_is_initialized() -> bool """
    return False

def ptp_is_supported(): # real signature unknown; restored from __doc__
    """ ptp_is_supported() -> bool """
    return False

def ptp_statistics_callback_add(callback, user_data=None): # real signature unknown; restored from __doc__
    """ ptp_statistics_callback_add(callback:GstNet.PtpStatisticsCallback, user_data=None) -> int """
    return 0

def ptp_statistics_callback_remove(id): # real signature unknown; restored from __doc__
    """ ptp_statistics_callback_remove(id:int) """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

class NetAddressMeta(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        NetAddressMeta()
    """
    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info() -> Gst.MetaInfo """
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

    addr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NetAddressMeta), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NetAddressMeta' objects>, '__weakref__': <attribute '__weakref__' of 'NetAddressMeta' objects>, '__doc__': None, 'meta': <property object at 0x7f795dd3df40>, 'addr': <property object at 0x7f795dd3df90>, 'get_info': gi.FunctionInfo(get_info)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NetAddressMeta)


class NetClientClock(__gi_repository_Gst.SystemClock):
    """
    :Constructors:
    
    ::
    
        NetClientClock(**properties)
        new(name:str, remote_address:str, remote_port:int, base_time:int) -> Gst.Clock
    """
    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_observation(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation(self, slave:int, master:int) -> bool, r_squared:float """
        return False

    def add_observation_unapplied(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation_unapplied(self, slave:int, master:int) -> bool, r_squared:float, internal:int, external:int, rate_num:int, rate_denom:int """
        return False

    def adjust_unlocked(self, internal): # real signature unknown; restored from __doc__
        """ adjust_unlocked(self, internal:int) -> int """
        return 0

    def adjust_with_calibration(self, internal_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ adjust_with_calibration(self, internal_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
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

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_change_resolution(self, *args, **kwargs): # real signature unknown
        """ change_resolution(self, old_resolution:int, new_resolution:int) -> int """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_get_internal_time(self, *args, **kwargs): # real signature unknown
        """ get_internal_time(self) -> int """
        pass

    def do_get_resolution(self, *args, **kwargs): # real signature unknown
        """ get_resolution(self) -> int """
        pass

    def do_unschedule(self, *args, **kwargs): # real signature unknown
        """ unschedule(self, entry:Gst.ClockEntry) """
        pass

    def do_wait(self, *args, **kwargs): # real signature unknown
        """ wait(self, entry:Gst.ClockEntry, jitter:int) -> Gst.ClockReturn """
        pass

    def do_wait_async(self, *args, **kwargs): # real signature unknown
        """ wait_async(self, entry:Gst.ClockEntry) -> Gst.ClockReturn """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
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

    def get_calibration(self): # real signature unknown; restored from __doc__
        """ get_calibration(self) -> internal:int, external:int, rate_num:int, rate_denom:int """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_internal_time(self): # real signature unknown; restored from __doc__
        """ get_internal_time(self) -> int """
        return 0

    def get_master(self): # real signature unknown; restored from __doc__
        """ get_master(self) -> Gst.Clock or None """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> int """
        return 0

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def get_timeout(self): # real signature unknown; restored from __doc__
        """ get_timeout(self) -> int """
        return 0

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
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

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
        return False

    def id_compare_func(self, id1=None, id2=None): # real signature unknown; restored from __doc__
        """ id_compare_func(id1=None, id2=None) -> int """
        return 0

    def id_get_clock(self, id): # real signature unknown; restored from __doc__
        """ id_get_clock(id) -> Gst.Clock or None """
        pass

    def id_get_time(self, id): # real signature unknown; restored from __doc__
        """ id_get_time(id) -> int """
        return 0

    def id_ref(self, id): # real signature unknown; restored from __doc__
        """ id_ref(id) """
        pass

    def id_unref(self, id): # real signature unknown; restored from __doc__
        """ id_unref(id) """
        pass

    def id_unschedule(self, id): # real signature unknown; restored from __doc__
        """ id_unschedule(id) """
        pass

    def id_uses_clock(self, id, clock): # real signature unknown; restored from __doc__
        """ id_uses_clock(id, clock:Gst.Clock) -> bool """
        return False

    def id_wait(self, id): # real signature unknown; restored from __doc__
        """ id_wait(id) -> Gst.ClockReturn, jitter:int """
        pass

    def id_wait_async(self, id, func, user_data=None): # real signature unknown; restored from __doc__
        """ id_wait_async(id, func:Gst.ClockCallback, user_data=None) -> Gst.ClockReturn """
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

    def is_synced(self): # real signature unknown; restored from __doc__
        """ is_synced(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, name, remote_address, remote_port, base_time): # real signature unknown; restored from __doc__
        """ new(name:str, remote_address:str, remote_port:int, base_time:int) -> Gst.Clock """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_periodic_id(self, start_time, interval): # real signature unknown; restored from __doc__
        """ new_periodic_id(self, start_time:int, interval:int) """
        pass

    def new_single_shot_id(self, time): # real signature unknown; restored from __doc__
        """ new_single_shot_id(self, time:int) """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def obtain(self): # real signature unknown; restored from __doc__
        """ obtain() -> Gst.Clock """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def periodic_id_reinit(self, id, start_time, interval): # real signature unknown; restored from __doc__
        """ periodic_id_reinit(self, id, start_time:int, interval:int) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
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

    def set_calibration(self, internal, external, rate_num, rate_denom): # real signature unknown; restored from __doc__
        """ set_calibration(self, internal:int, external:int, rate_num:int, rate_denom:int) """
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default(self, new_clock=None): # real signature unknown; restored from __doc__
        """ set_default(new_clock:Gst.Clock=None) """
        pass

    def set_master(self, master=None): # real signature unknown; restored from __doc__
        """ set_master(self, master:Gst.Clock=None) -> bool """
        return False

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, resolution): # real signature unknown; restored from __doc__
        """ set_resolution(self, resolution:int) -> int """
        return 0

    def set_synced(self, synced): # real signature unknown; restored from __doc__
        """ set_synced(self, synced:bool) """
        pass

    def set_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_timeout(self, timeout:int) """
        pass

    def single_shot_id_reinit(self, id, time): # real signature unknown; restored from __doc__
        """ single_shot_id_reinit(self, id, time:int) -> bool """
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

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unadjust_unlocked(self, external): # real signature unknown; restored from __doc__
        """ unadjust_unlocked(self, external:int) -> int """
        return 0

    def unadjust_with_calibration(self, external_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ unadjust_with_calibration(self, external_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait_for_sync(self, timeout): # real signature unknown; restored from __doc__
        """ wait_for_sync(self, timeout:int) -> bool """
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

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f795dca4b50>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(NetClientClock), '__module__': 'gi.repository.GstNet', '__gtype__': <GType GstNetClientClock (94234266514256)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'clock': <property object at 0x7f795dcd1590>, 'priv': <property object at 0x7f795dcd1680>, '_gst_reserved': <property object at 0x7f795dcd1770>})"
    __gdoc__ = 'Object GstNetClientClock\n\nProperties from GstNetClientClock:\n  address -> gchararray: address\n    The IP address of the machine providing a time server\n  port -> gint: port\n    The port on which the remote server is listening\n  round-trip-limit -> guint64: round-trip limit\n    Maximum tolerable round-trip interval for packets, in nanoseconds (0 = no limit)\n  minimum-update-interval -> guint64: minimum update interval\n    Minimum polling interval for packets, in nanoseconds(0 = no limit)\n  bus -> GstBus: bus\n    A GstBus on which to send clock status information\n  base-time -> guint64: Base Time\n    Initial time that is reported before synchronization\n  internal-clock -> GstClock: Internal Clock\n    Internal clock that directly slaved to the remote clock\n  qos-dscp -> gint: QoS diff srv code point\n    Quality of Service, differentiated services code point (-1 default)\n\nProperties from GstSystemClock:\n  clock-type -> GstClockType: Clock type\n    The type of underlying clock implementation used\n\nSignals from GstClock:\n  synced (gboolean)\n\nProperties from GstClock:\n  window-size -> gint: Window size\n    The size of the window used to calculate rate and offset\n  window-threshold -> gint: Window threshold\n    The threshold to start calculating rate and offset\n  timeout -> guint64: Timeout\n    The amount of time, in nanoseconds, to sample master and slave clocks\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstNetClientClock (94234266514256)>'
    __info__ = ObjectInfo(NetClientClock)


class NetClientClockClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        NetClientClockClass()
    """
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NetClientClockClass), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NetClientClockClass' objects>, '__weakref__': <attribute '__weakref__' of 'NetClientClockClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f795dcd18b0>, '_gst_reserved': <property object at 0x7f795dcd19a0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NetClientClockClass)


class NetClientClockPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NetClientClockPrivate), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NetClientClockPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'NetClientClockPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NetClientClockPrivate)


class NetControlMessageMeta(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        NetControlMessageMeta()
    """
    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info() -> Gst.MetaInfo """
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

    message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    meta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NetControlMessageMeta), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NetControlMessageMeta' objects>, '__weakref__': <attribute '__weakref__' of 'NetControlMessageMeta' objects>, '__doc__': None, 'meta': <property object at 0x7f795dcd1bd0>, 'message': <property object at 0x7f795dcd1cc0>, 'get_info': gi.FunctionInfo(get_info)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NetControlMessageMeta)


class NetTimePacket(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        NetTimePacket()
        new(buffer:list) -> GstNet.NetTimePacket
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GstNet.NetTimePacket """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self, buffer): # real signature unknown; restored from __doc__
        """ new(buffer:list) -> GstNet.NetTimePacket """
        pass

    def receive(self, socket): # real signature unknown; restored from __doc__
        """ receive(socket:Gio.Socket) -> GstNet.NetTimePacket, src_address:Gio.SocketAddress """
        pass

    def send(self, socket, dest_address): # real signature unknown; restored from __doc__
        """ send(self, socket:Gio.Socket, dest_address:Gio.SocketAddress) -> bool """
        return False

    def serialize(self): # real signature unknown; restored from __doc__
        """ serialize(self) -> int """
        return 0

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

    local_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remote_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NetTimePacket), '__module__': 'gi.repository.GstNet', '__gtype__': <GType GstNetTimePacket (94234266936816)>, '__dict__': <attribute '__dict__' of 'NetTimePacket' objects>, '__weakref__': <attribute '__weakref__' of 'NetTimePacket' objects>, '__doc__': None, 'local_time': <property object at 0x7f795dcd1e50>, 'remote_time': <property object at 0x7f795dcd1f40>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'send': gi.FunctionInfo(send), 'serialize': gi.FunctionInfo(serialize), 'receive': gi.FunctionInfo(receive)})"
    __gtype__ = None # (!) real value is '<GType GstNetTimePacket (94234266936816)>'
    __info__ = StructInfo(NetTimePacket)


class NetTimeProvider(__gi_repository_Gst.Object, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        NetTimeProvider(**properties)
        new(clock:Gst.Clock, address:str=None, port:int) -> GstNet.NetTimeProvider
    """
    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
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

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
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

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
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

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
        return False

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def new(self, clock, address=None, port): # real signature unknown; restored from __doc__
        """ new(clock:Gst.Clock, address:str=None, port:int) -> GstNet.NetTimeProvider """
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

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
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

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

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

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f795dcc1cd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(NetTimeProvider), '__module__': 'gi.repository.GstNet', '__gtype__': <GType GstNetTimeProvider (94234266911984)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'parent': <property object at 0x7f795dcd30e0>, 'priv': <property object at 0x7f795dcd3220>, '_gst_reserved': <property object at 0x7f795dcd3310>})"
    __gdoc__ = 'Object GstNetTimeProvider\n\nProperties from GstNetTimeProvider:\n  port -> gint: port\n    The port to receive the packets from, 0=allocate\n  address -> gchararray: address\n    The address to bind on, as a dotted quad (x.x.x.x)\n  clock -> GstClock: Clock\n    The clock to export over the network\n  active -> gboolean: Active\n    TRUE if the clock will respond to queries over the network\n  qos-dscp -> gint: QoS diff srv code point\n    Quality of Service, differentiated services code point (-1 default)\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstNetTimeProvider (94234266911984)>'
    __info__ = ObjectInfo(NetTimeProvider)


class NetTimeProviderClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        NetTimeProviderClass()
    """
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NetTimeProviderClass), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NetTimeProviderClass' objects>, '__weakref__': <attribute '__weakref__' of 'NetTimeProviderClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f795dcd34a0>, '_gst_reserved': <property object at 0x7f795dcd3590>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NetTimeProviderClass)


class NetTimeProviderPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NetTimeProviderPrivate), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NetTimeProviderPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'NetTimeProviderPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NetTimeProviderPrivate)


class NtpClock(NetClientClock):
    """
    :Constructors:
    
    ::
    
        NtpClock(**properties)
        new(name:str, remote_address:str, remote_port:int, base_time:int) -> Gst.Clock
    """
    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_observation(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation(self, slave:int, master:int) -> bool, r_squared:float """
        return False

    def add_observation_unapplied(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation_unapplied(self, slave:int, master:int) -> bool, r_squared:float, internal:int, external:int, rate_num:int, rate_denom:int """
        return False

    def adjust_unlocked(self, internal): # real signature unknown; restored from __doc__
        """ adjust_unlocked(self, internal:int) -> int """
        return 0

    def adjust_with_calibration(self, internal_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ adjust_with_calibration(self, internal_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
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

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_change_resolution(self, *args, **kwargs): # real signature unknown
        """ change_resolution(self, old_resolution:int, new_resolution:int) -> int """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_get_internal_time(self, *args, **kwargs): # real signature unknown
        """ get_internal_time(self) -> int """
        pass

    def do_get_resolution(self, *args, **kwargs): # real signature unknown
        """ get_resolution(self) -> int """
        pass

    def do_unschedule(self, *args, **kwargs): # real signature unknown
        """ unschedule(self, entry:Gst.ClockEntry) """
        pass

    def do_wait(self, *args, **kwargs): # real signature unknown
        """ wait(self, entry:Gst.ClockEntry, jitter:int) -> Gst.ClockReturn """
        pass

    def do_wait_async(self, *args, **kwargs): # real signature unknown
        """ wait_async(self, entry:Gst.ClockEntry) -> Gst.ClockReturn """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
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

    def get_calibration(self): # real signature unknown; restored from __doc__
        """ get_calibration(self) -> internal:int, external:int, rate_num:int, rate_denom:int """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_internal_time(self): # real signature unknown; restored from __doc__
        """ get_internal_time(self) -> int """
        return 0

    def get_master(self): # real signature unknown; restored from __doc__
        """ get_master(self) -> Gst.Clock or None """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> int """
        return 0

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def get_timeout(self): # real signature unknown; restored from __doc__
        """ get_timeout(self) -> int """
        return 0

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
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

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
        return False

    def id_compare_func(self, id1=None, id2=None): # real signature unknown; restored from __doc__
        """ id_compare_func(id1=None, id2=None) -> int """
        return 0

    def id_get_clock(self, id): # real signature unknown; restored from __doc__
        """ id_get_clock(id) -> Gst.Clock or None """
        pass

    def id_get_time(self, id): # real signature unknown; restored from __doc__
        """ id_get_time(id) -> int """
        return 0

    def id_ref(self, id): # real signature unknown; restored from __doc__
        """ id_ref(id) """
        pass

    def id_unref(self, id): # real signature unknown; restored from __doc__
        """ id_unref(id) """
        pass

    def id_unschedule(self, id): # real signature unknown; restored from __doc__
        """ id_unschedule(id) """
        pass

    def id_uses_clock(self, id, clock): # real signature unknown; restored from __doc__
        """ id_uses_clock(id, clock:Gst.Clock) -> bool """
        return False

    def id_wait(self, id): # real signature unknown; restored from __doc__
        """ id_wait(id) -> Gst.ClockReturn, jitter:int """
        pass

    def id_wait_async(self, id, func, user_data=None): # real signature unknown; restored from __doc__
        """ id_wait_async(id, func:Gst.ClockCallback, user_data=None) -> Gst.ClockReturn """
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

    def is_synced(self): # real signature unknown; restored from __doc__
        """ is_synced(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, name, remote_address, remote_port, base_time): # real signature unknown; restored from __doc__
        """ new(name:str, remote_address:str, remote_port:int, base_time:int) -> Gst.Clock """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_periodic_id(self, start_time, interval): # real signature unknown; restored from __doc__
        """ new_periodic_id(self, start_time:int, interval:int) """
        pass

    def new_single_shot_id(self, time): # real signature unknown; restored from __doc__
        """ new_single_shot_id(self, time:int) """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def obtain(self): # real signature unknown; restored from __doc__
        """ obtain() -> Gst.Clock """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def periodic_id_reinit(self, id, start_time, interval): # real signature unknown; restored from __doc__
        """ periodic_id_reinit(self, id, start_time:int, interval:int) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
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

    def set_calibration(self, internal, external, rate_num, rate_denom): # real signature unknown; restored from __doc__
        """ set_calibration(self, internal:int, external:int, rate_num:int, rate_denom:int) """
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default(self, new_clock=None): # real signature unknown; restored from __doc__
        """ set_default(new_clock:Gst.Clock=None) """
        pass

    def set_master(self, master=None): # real signature unknown; restored from __doc__
        """ set_master(self, master:Gst.Clock=None) -> bool """
        return False

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, resolution): # real signature unknown; restored from __doc__
        """ set_resolution(self, resolution:int) -> int """
        return 0

    def set_synced(self, synced): # real signature unknown; restored from __doc__
        """ set_synced(self, synced:bool) """
        pass

    def set_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_timeout(self, timeout:int) """
        pass

    def single_shot_id_reinit(self, id, time): # real signature unknown; restored from __doc__
        """ single_shot_id_reinit(self, id, time:int) -> bool """
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

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unadjust_unlocked(self, external): # real signature unknown; restored from __doc__
        """ unadjust_unlocked(self, external:int) -> int """
        return 0

    def unadjust_with_calibration(self, external_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ unadjust_with_calibration(self, external_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait_for_sync(self, timeout): # real signature unknown; restored from __doc__
        """ wait_for_sync(self, timeout:int) -> bool """
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

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f795dcdfd60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(NtpClock), '__module__': 'gi.repository.GstNet', '__gtype__': <GType GstNtpClock (94234266590816)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'clock': <property object at 0x7f795dcd3770>, 'priv': <property object at 0x7f795dcd38b0>, '_gst_reserved': <property object at 0x7f795dcd39a0>})"
    __gdoc__ = 'Object GstNtpClock\n\nProperties from GstNetClientClock:\n  address -> gchararray: address\n    The IP address of the machine providing a time server\n  port -> gint: port\n    The port on which the remote server is listening\n  round-trip-limit -> guint64: round-trip limit\n    Maximum tolerable round-trip interval for packets, in nanoseconds (0 = no limit)\n  minimum-update-interval -> guint64: minimum update interval\n    Minimum polling interval for packets, in nanoseconds(0 = no limit)\n  bus -> GstBus: bus\n    A GstBus on which to send clock status information\n  base-time -> guint64: Base Time\n    Initial time that is reported before synchronization\n  internal-clock -> GstClock: Internal Clock\n    Internal clock that directly slaved to the remote clock\n  qos-dscp -> gint: QoS diff srv code point\n    Quality of Service, differentiated services code point (-1 default)\n\nProperties from GstSystemClock:\n  clock-type -> GstClockType: Clock type\n    The type of underlying clock implementation used\n\nSignals from GstClock:\n  synced (gboolean)\n\nProperties from GstClock:\n  window-size -> gint: Window size\n    The size of the window used to calculate rate and offset\n  window-threshold -> gint: Window threshold\n    The threshold to start calculating rate and offset\n  timeout -> guint64: Timeout\n    The amount of time, in nanoseconds, to sample master and slave clocks\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstNtpClock (94234266590816)>'
    __info__ = ObjectInfo(NtpClock)


class NtpClockClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        NtpClockClass()
    """
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(NtpClockClass), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'NtpClockClass' objects>, '__weakref__': <attribute '__weakref__' of 'NtpClockClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f795dcd3b30>, '_gst_reserved': <property object at 0x7f795dcd3c20>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(NtpClockClass)


class PtpClock(__gi_repository_Gst.SystemClock):
    """
    :Constructors:
    
    ::
    
        PtpClock(**properties)
        new(name:str, domain:int) -> Gst.Clock
    """
    def add_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ add_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def add_observation(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation(self, slave:int, master:int) -> bool, r_squared:float """
        return False

    def add_observation_unapplied(self, slave, master): # real signature unknown; restored from __doc__
        """ add_observation_unapplied(self, slave:int, master:int) -> bool, r_squared:float, internal:int, external:int, rate_num:int, rate_denom:int """
        return False

    def adjust_unlocked(self, internal): # real signature unknown; restored from __doc__
        """ adjust_unlocked(self, internal:int) -> int """
        return 0

    def adjust_with_calibration(self, internal_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ adjust_with_calibration(self, internal_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_uniqueness(self, p_list, name): # real signature unknown; restored from __doc__
        """ check_uniqueness(list:list, name:str) -> bool """
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

    def default_deep_notify(self, p_object, orig, pspec, excluded_props=None): # real signature unknown; restored from __doc__
        """ default_deep_notify(object:GObject.Object, orig:Gst.Object, pspec:GObject.ParamSpec, excluded_props:list=None) """
        pass

    def default_error(self, error, debug=None): # real signature unknown; restored from __doc__
        """ default_error(self, error:error, debug:str=None) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_change_resolution(self, *args, **kwargs): # real signature unknown
        """ change_resolution(self, old_resolution:int, new_resolution:int) -> int """
        pass

    def do_deep_notify(self, *args, **kwargs): # real signature unknown
        """ deep_notify(self, orig:Gst.Object, pspec:GObject.ParamSpec) """
        pass

    def do_get_internal_time(self, *args, **kwargs): # real signature unknown
        """ get_internal_time(self) -> int """
        pass

    def do_get_resolution(self, *args, **kwargs): # real signature unknown
        """ get_resolution(self) -> int """
        pass

    def do_unschedule(self, *args, **kwargs): # real signature unknown
        """ unschedule(self, entry:Gst.ClockEntry) """
        pass

    def do_wait(self, *args, **kwargs): # real signature unknown
        """ wait(self, entry:Gst.ClockEntry, jitter:int) -> Gst.ClockReturn """
        pass

    def do_wait_async(self, *args, **kwargs): # real signature unknown
        """ wait_async(self, entry:Gst.ClockEntry) -> Gst.ClockReturn """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
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

    def get_calibration(self): # real signature unknown; restored from __doc__
        """ get_calibration(self) -> internal:int, external:int, rate_num:int, rate_denom:int """
        pass

    def get_control_binding(self, property_name): # real signature unknown; restored from __doc__
        """ get_control_binding(self, property_name:str) -> Gst.ControlBinding or None """
        pass

    def get_control_rate(self): # real signature unknown; restored from __doc__
        """ get_control_rate(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_g_value_array(self, property_name, timestamp, interval, values): # real signature unknown; restored from __doc__
        """ get_g_value_array(self, property_name:str, timestamp:int, interval:int, values:list) -> bool """
        return False

    def get_internal_time(self): # real signature unknown; restored from __doc__
        """ get_internal_time(self) -> int """
        return 0

    def get_master(self): # real signature unknown; restored from __doc__
        """ get_master(self) -> Gst.Clock or None """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gst.Object or None """
        pass

    def get_path_string(self): # real signature unknown; restored from __doc__
        """ get_path_string(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> int """
        return 0

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def get_timeout(self): # real signature unknown; restored from __doc__
        """ get_timeout(self) -> int """
        return 0

    def get_value(self, property_name, timestamp): # real signature unknown; restored from __doc__
        """ get_value(self, property_name:str, timestamp:int) -> GObject.Value or None """
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

    def has_active_control_bindings(self): # real signature unknown; restored from __doc__
        """ has_active_control_bindings(self) -> bool """
        return False

    def has_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ has_as_ancestor(self, ancestor:Gst.Object) -> bool """
        return False

    def has_as_parent(self, parent): # real signature unknown; restored from __doc__
        """ has_as_parent(self, parent:Gst.Object) -> bool """
        return False

    def id_compare_func(self, id1=None, id2=None): # real signature unknown; restored from __doc__
        """ id_compare_func(id1=None, id2=None) -> int """
        return 0

    def id_get_clock(self, id): # real signature unknown; restored from __doc__
        """ id_get_clock(id) -> Gst.Clock or None """
        pass

    def id_get_time(self, id): # real signature unknown; restored from __doc__
        """ id_get_time(id) -> int """
        return 0

    def id_ref(self, id): # real signature unknown; restored from __doc__
        """ id_ref(id) """
        pass

    def id_unref(self, id): # real signature unknown; restored from __doc__
        """ id_unref(id) """
        pass

    def id_unschedule(self, id): # real signature unknown; restored from __doc__
        """ id_unschedule(id) """
        pass

    def id_uses_clock(self, id, clock): # real signature unknown; restored from __doc__
        """ id_uses_clock(id, clock:Gst.Clock) -> bool """
        return False

    def id_wait(self, id): # real signature unknown; restored from __doc__
        """ id_wait(id) -> Gst.ClockReturn, jitter:int """
        pass

    def id_wait_async(self, id, func, user_data=None): # real signature unknown; restored from __doc__
        """ id_wait_async(id, func:Gst.ClockCallback, user_data=None) -> Gst.ClockReturn """
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

    def is_synced(self): # real signature unknown; restored from __doc__
        """ is_synced(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, name, domain): # real signature unknown; restored from __doc__
        """ new(name:str, domain:int) -> Gst.Clock """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_periodic_id(self, start_time, interval): # real signature unknown; restored from __doc__
        """ new_periodic_id(self, start_time:int, interval:int) """
        pass

    def new_single_shot_id(self, time): # real signature unknown; restored from __doc__
        """ new_single_shot_id(self, time:int) """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def obtain(self): # real signature unknown; restored from __doc__
        """ obtain() -> Gst.Clock """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def periodic_id_reinit(self, id, start_time, interval): # real signature unknown; restored from __doc__
        """ periodic_id_reinit(self, id, start_time:int, interval:int) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gst.Object """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_control_binding(self, binding): # real signature unknown; restored from __doc__
        """ remove_control_binding(self, binding:Gst.ControlBinding) -> bool """
        return False

    def replace(self, oldobj=None, newobj=None): # real signature unknown; restored from __doc__
        """ replace(oldobj:Gst.Object=None, newobj:Gst.Object=None) -> bool, oldobj:Gst.Object """
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

    def set_calibration(self, internal, external, rate_num, rate_denom): # real signature unknown; restored from __doc__
        """ set_calibration(self, internal:int, external:int, rate_num:int, rate_denom:int) """
        pass

    def set_control_bindings_disabled(self, disabled): # real signature unknown; restored from __doc__
        """ set_control_bindings_disabled(self, disabled:bool) """
        pass

    def set_control_binding_disabled(self, property_name, disabled): # real signature unknown; restored from __doc__
        """ set_control_binding_disabled(self, property_name:str, disabled:bool) """
        pass

    def set_control_rate(self, control_rate): # real signature unknown; restored from __doc__
        """ set_control_rate(self, control_rate:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default(self, new_clock=None): # real signature unknown; restored from __doc__
        """ set_default(new_clock:Gst.Clock=None) """
        pass

    def set_master(self, master=None): # real signature unknown; restored from __doc__
        """ set_master(self, master:Gst.Clock=None) -> bool """
        return False

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) -> bool """
        return False

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gst.Object) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, resolution): # real signature unknown; restored from __doc__
        """ set_resolution(self, resolution:int) -> int """
        return 0

    def set_synced(self, synced): # real signature unknown; restored from __doc__
        """ set_synced(self, synced:bool) """
        pass

    def set_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_timeout(self, timeout:int) """
        pass

    def single_shot_id_reinit(self, id, time): # real signature unknown; restored from __doc__
        """ single_shot_id_reinit(self, id, time:int) -> bool """
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

    def suggest_next_sync(self): # real signature unknown; restored from __doc__
        """ suggest_next_sync(self) -> int """
        return 0

    def sync_values(self, timestamp): # real signature unknown; restored from __doc__
        """ sync_values(self, timestamp:int) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unadjust_unlocked(self, external): # real signature unknown; restored from __doc__
        """ unadjust_unlocked(self, external:int) -> int """
        return 0

    def unadjust_with_calibration(self, external_target, cinternal, cexternal, cnum, cdenom): # real signature unknown; restored from __doc__
        """ unadjust_with_calibration(self, external_target:int, cinternal:int, cexternal:int, cnum:int, cdenom:int) -> int """
        return 0

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def wait_for_sync(self, timeout): # real signature unknown; restored from __doc__
        """ wait_for_sync(self, timeout:int) -> bool """
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

    clock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_bindings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    control_rate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    last_sync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f795da83d90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(PtpClock), '__module__': 'gi.repository.GstNet', '__gtype__': <GType GstPtpClock (94234266588544)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'clock': <property object at 0x7f795dcd3e00>, 'priv': <property object at 0x7f795dcd3f40>, '_gst_reserved': <property object at 0x7f795dcd5090>})"
    __gdoc__ = 'Object GstPtpClock\n\nProperties from GstPtpClock:\n  domain -> guint: Domain\n    The PTP domain\n  internal-clock -> GstClock: Internal Clock\n    Internal clock\n  master-clock-id -> guint64: Master Clock ID\n    Master Clock ID\n  grandmaster-clock-id -> guint64: Grand Master Clock ID\n    Grand Master Clock ID\n\nProperties from GstSystemClock:\n  clock-type -> GstClockType: Clock type\n    The type of underlying clock implementation used\n\nSignals from GstClock:\n  synced (gboolean)\n\nProperties from GstClock:\n  window-size -> gint: Window size\n    The size of the window used to calculate rate and offset\n  window-threshold -> gint: Window threshold\n    The threshold to start calculating rate and offset\n  timeout -> guint64: Timeout\n    The amount of time, in nanoseconds, to sample master and slave clocks\n\nSignals from GstObject:\n  deep-notify (GstObject, GParam)\n\nProperties from GstObject:\n  name -> gchararray: Name\n    The name of the object\n  parent -> GstObject: Parent\n    The parent of the object\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GstPtpClock (94234266588544)>'
    __info__ = ObjectInfo(PtpClock)


class PtpClockClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PtpClockClass()
    """
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

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gst_reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PtpClockClass), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PtpClockClass' objects>, '__weakref__': <attribute '__weakref__' of 'PtpClockClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f795dcd5220>, '_gst_reserved': <property object at 0x7f795dcd5310>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PtpClockClass)


class PtpClockPrivate(__gi.Struct):
    # no doc
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PtpClockPrivate), '__module__': 'gi.repository.GstNet', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PtpClockPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'PtpClockPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PtpClockPrivate)


class __class__(object):
    """
    An object which wraps an introspection typelib.
    
        This wrapping creates a python module like representation of the typelib
        using gi repository as a foundation. Accessing attributes of the module
        will dynamically pull them in and create wrappers for the members.
        These members are then cached on this introspection module.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # reliably restored by inspect
        # no doc
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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __init__(self, namespace, version=None): # reliably restored by inspect
        """ Might raise gi._gi.RepositoryError """
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

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f795df451f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f795df45280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f795df45310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f795df453a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f795eb81d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GstNet-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GstNet', loader=<gi.importer.DynamicImporter object at 0x7f795eb81d00>)"

