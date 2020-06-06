# encoding: utf-8
# module gi.repository.ECal
# from /usr/lib64/girepository-1.0/ECal-2.0.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ReminderWatcher(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        ReminderWatcher(**properties)
        new(registry:EDataServer.SourceRegistry) -> ECal.ReminderWatcher
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

    def describe_data(self, rd, flags): # real signature unknown; restored from __doc__
        """ describe_data(self, rd:ECal.ReminderData, flags:int) -> str """
        return ""

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dismiss(self, rd, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ dismiss(self, rd:ECal.ReminderData, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def dismiss_all(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ dismiss_all(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def dismiss_all_finish(self, result): # real signature unknown; restored from __doc__
        """ dismiss_all_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def dismiss_all_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ dismiss_all_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def dismiss_finish(self, result): # real signature unknown; restored from __doc__
        """ dismiss_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def dismiss_sync(self, rd, cancellable=None): # real signature unknown; restored from __doc__
        """ dismiss_sync(self, rd:ECal.ReminderData, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def do_cal_client_connect(self, *args, **kwargs): # real signature unknown
        """ cal_client_connect(self, source:EDataServer.Source, source_type:ECal.ClientSourceType, wait_for_connected_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_format_time(self, *args, **kwargs): # real signature unknown
        """ format_time(self, rd:ECal.ReminderData, itt:ICalGLib.Time, inout_buffer:str, buffer_size:int) """
        pass

    def do_schedule_timer(self, *args, **kwargs): # real signature unknown
        """ schedule_timer(self, at_time:int) """
        pass

    def dup_default_zone(self): # real signature unknown; restored from __doc__
        """ dup_default_zone(self) -> ICalGLib.Timezone """
        pass

    def dup_past(self): # real signature unknown; restored from __doc__
        """ dup_past(self) -> list or None """
        return []

    def dup_snoozed(self): # real signature unknown; restored from __doc__
        """ dup_snoozed(self) -> list or None """
        return []

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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_registry(self): # real signature unknown; restored from __doc__
        """ get_registry(self) -> EDataServer.SourceRegistry """
        pass

    def get_timers_enabled(self): # real signature unknown; restored from __doc__
        """ get_timers_enabled(self) -> bool """
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

    def new(self, registry): # real signature unknown; restored from __doc__
        """ new(registry:EDataServer.SourceRegistry) -> ECal.ReminderWatcher """
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

    def ref_opened_client(self, source_uid): # real signature unknown; restored from __doc__
        """ ref_opened_client(self, source_uid:str) -> ECal.Client or None """
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

    def set_default_zone(self, zone=None): # real signature unknown; restored from __doc__
        """ set_default_zone(self, zone:ICalGLib.Timezone=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_timers_enabled(self, enabled): # real signature unknown; restored from __doc__
        """ set_timers_enabled(self, enabled:bool) """
        pass

    def snooze(self, rd, until): # real signature unknown; restored from __doc__
        """ snooze(self, rd:ECal.ReminderData, until:int) """
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

    def timer_elapsed(self): # real signature unknown; restored from __doc__
        """ timer_elapsed(self) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fe5c99d6880>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ReminderWatcher), '__module__': 'gi.repository.ECal', '__gtype__': <GType EReminderWatcher (94764814939936)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'describe_data': gi.FunctionInfo(describe_data), 'dismiss': gi.FunctionInfo(dismiss), 'dismiss_all': gi.FunctionInfo(dismiss_all), 'dismiss_all_finish': gi.FunctionInfo(dismiss_all_finish), 'dismiss_all_sync': gi.FunctionInfo(dismiss_all_sync), 'dismiss_finish': gi.FunctionInfo(dismiss_finish), 'dismiss_sync': gi.FunctionInfo(dismiss_sync), 'dup_default_zone': gi.FunctionInfo(dup_default_zone), 'dup_past': gi.FunctionInfo(dup_past), 'dup_snoozed': gi.FunctionInfo(dup_snoozed), 'get_registry': gi.FunctionInfo(get_registry), 'get_timers_enabled': gi.FunctionInfo(get_timers_enabled), 'ref_opened_client': gi.FunctionInfo(ref_opened_client), 'set_default_zone': gi.FunctionInfo(set_default_zone), 'set_timers_enabled': gi.FunctionInfo(set_timers_enabled), 'snooze': gi.FunctionInfo(snooze), 'timer_elapsed': gi.FunctionInfo(timer_elapsed), 'do_cal_client_connect': gi.VFuncInfo(cal_client_connect), 'do_changed': gi.VFuncInfo(changed), 'do_format_time': gi.VFuncInfo(format_time), 'do_schedule_timer': gi.VFuncInfo(schedule_timer), 'parent': <property object at 0x7fe5c99dcf40>, 'priv': <property object at 0x7fe5c99de090>})"
    __gdoc__ = 'Object EReminderWatcher\n\nSignals from EReminderWatcher:\n  format-time (gpointer, gpointer, gpointer, gint)\n  triggered (gpointer, gboolean)\n  changed ()\n\nProperties from EReminderWatcher:\n  registry -> ESourceRegistry: Registry\n    Data source registry\n  default-zone -> ICalTimezone: Default Zone\n    The default time zone\n  timers-enabled -> gboolean: Timers Enabled\n    Whether can schedule timers\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EReminderWatcher (94764814939936)>'
    __info__ = ObjectInfo(ReminderWatcher)


