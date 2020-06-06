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


from .TimezoneCache import TimezoneCache

class Client(__gi_repository_EDataServer.Client, TimezoneCache, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        Client(**properties)
    """
    def add_timezone(self, zone, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_timezone(self, zone:ICalGLib.Timezone, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_timezone_finish(self, result): # real signature unknown; restored from __doc__
        """ add_timezone_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def add_timezone_sync(self, zone, cancellable=None): # real signature unknown; restored from __doc__
        """ add_timezone_sync(self, zone:ICalGLib.Timezone, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cancel_all(self): # real signature unknown; restored from __doc__
        """ cancel_all(self) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_capability(self, capability): # real signature unknown; restored from __doc__
        """ check_capability(self, capability:str) -> bool """
        return False

    def check_one_alarm_only(self): # real signature unknown; restored from __doc__
        """ check_one_alarm_only(self) -> bool """
        return False

    def check_organizer_must_accept(self): # real signature unknown; restored from __doc__
        """ check_organizer_must_accept(self) -> bool """
        return False

    def check_organizer_must_attend(self): # real signature unknown; restored from __doc__
        """ check_organizer_must_attend(self) -> bool """
        return False

    def check_recurrences_no_master(self): # real signature unknown; restored from __doc__
        """ check_recurrences_no_master(self) -> bool """
        return False

    def check_refresh_supported(self): # real signature unknown; restored from __doc__
        """ check_refresh_supported(self) -> bool """
        return False

    def check_save_schedules(self): # real signature unknown; restored from __doc__
        """ check_save_schedules(self) -> bool """
        return False

    def check_timezones_sync(self, vcalendar, icalcomps=None, tzlookup=None, tzlookup_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ check_timezones_sync(vcalendar:ICalGLib.Component, icalcomps:list=None, tzlookup:ECal.RecurResolveTimezoneCb=None, tzlookup_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, source, source_type, wait_for_connected_seconds, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect(source:EDataServer.Source, source_type:ECal.ClientSourceType, wait_for_connected_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def connect_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_finish(result:Gio.AsyncResult) -> EDataServer.Client """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_sync(self, source, source_type, wait_for_connected_seconds, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(source:EDataServer.Source, source_type:ECal.ClientSourceType, wait_for_connected_seconds:int, cancellable:Gio.Cancellable=None) -> EDataServer.Client """
        pass

    def create_object(self, icalcomp, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_object(self, icalcomp:ICalGLib.Component, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_objects(self, icalcomps, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_objects(self, icalcomps:list, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ create_objects_finish(self, result:Gio.AsyncResult) -> bool, out_uids:list """
        return False

    def create_objects_sync(self, icalcomps, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ create_objects_sync(self, icalcomps:list, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_uids:list """
        return False

    def create_object_finish(self, result): # real signature unknown; restored from __doc__
        """ create_object_finish(self, result:Gio.AsyncResult) -> bool, out_uid:str """
        return False

    def create_object_sync(self, icalcomp, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ create_object_sync(self, icalcomp:ICalGLib.Component, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_uid:str """
        return False

    def discard_alarm(self, uid, rid, auid, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ discard_alarm(self, uid:str, rid:str, auid:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def discard_alarm_finish(self, result): # real signature unknown; restored from __doc__
        """ discard_alarm_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def discard_alarm_sync(self, uid, rid, auid, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ discard_alarm_sync(self, uid:str, rid:str, auid:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_backend_died(self, *args, **kwargs): # real signature unknown
        """ backend_died(self) """
        pass

    def do_backend_error(self, *args, **kwargs): # real signature unknown
        """ backend_error(self, error_msg:str) """
        pass

    def do_backend_property_changed(self, *args, **kwargs): # real signature unknown
        """ backend_property_changed(self, prop_name:str, prop_value:str) """
        pass

    def do_get_backend_property(self, *args, **kwargs): # real signature unknown
        """ get_backend_property(self, prop_name:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_get_backend_property_finish(self, *args, **kwargs): # real signature unknown
        """ get_backend_property_finish(self, result:Gio.AsyncResult) -> bool, prop_value:str """
        pass

    def do_get_backend_property_sync(self, *args, **kwargs): # real signature unknown
        """ get_backend_property_sync(self, prop_name:str, cancellable:Gio.Cancellable=None) -> bool, prop_value:str """
        pass

    def do_open(self, *args, **kwargs): # real signature unknown
        """ open(self, only_if_exists:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_opened(self, *args, **kwargs): # real signature unknown
        """ opened(self, error:error) """
        pass

    def do_open_finish(self, *args, **kwargs): # real signature unknown
        """ open_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_open_sync(self, *args, **kwargs): # real signature unknown
        """ open_sync(self, only_if_exists:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_refresh(self, *args, **kwargs): # real signature unknown
        """ refresh(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_refresh_finish(self, *args, **kwargs): # real signature unknown
        """ refresh_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_refresh_sync(self, *args, **kwargs): # real signature unknown
        """ refresh_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_remove_finish(self, *args, **kwargs): # real signature unknown
        """ remove_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_remove_sync(self, *args, **kwargs): # real signature unknown
        """ remove_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_retrieve_capabilities(self, *args, **kwargs): # real signature unknown
        """ retrieve_capabilities(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_retrieve_capabilities_finish(self, *args, **kwargs): # real signature unknown
        """ retrieve_capabilities_finish(self, result:Gio.AsyncResult) -> bool, capabilities:str """
        pass

    def do_retrieve_capabilities_sync(self, *args, **kwargs): # real signature unknown
        """ retrieve_capabilities_sync(self, cancellable:Gio.Cancellable=None) -> bool, capabilities:str """
        pass

    def do_retrieve_properties_sync(self, *args, **kwargs): # real signature unknown
        """ retrieve_properties_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_set_backend_property(self, *args, **kwargs): # real signature unknown
        """ set_backend_property(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_set_backend_property_finish(self, *args, **kwargs): # real signature unknown
        """ set_backend_property_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_set_backend_property_sync(self, *args, **kwargs): # real signature unknown
        """ set_backend_property_sync(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_unwrap_dbus_error(self, *args, **kwargs): # real signature unknown
        """ unwrap_dbus_error(self, dbus_error:error) """
        pass

    def dup_bus_name(self): # real signature unknown; restored from __doc__
        """ dup_bus_name(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_create(self, code, custom_msg=None): # real signature unknown; restored from __doc__
        """ error_create(code:ECal.ClientError, custom_msg:str=None) -> error """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def error_to_string(self, code): # real signature unknown; restored from __doc__
        """ error_to_string(code:ECal.ClientError) -> str """
        return ""

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

    def generate_instances(self, start, end, cancellable=None, cb, cb_data=None): # real signature unknown; restored from __doc__
        """ generate_instances(self, start:int, end:int, cancellable:Gio.Cancellable=None, cb:ECal.RecurInstanceCb, cb_data=None) """
        pass

    def generate_instances_for_object(self, icalcomp, start, end, cancellable=None, cb, cb_data=None): # real signature unknown; restored from __doc__
        """ generate_instances_for_object(self, icalcomp:ICalGLib.Component, start:int, end:int, cancellable:Gio.Cancellable=None, cb:ECal.RecurInstanceCb, cb_data=None) """
        pass

    def generate_instances_for_object_sync(self, icalcomp, start, end, cancellable=None, cb, cb_data=None): # real signature unknown; restored from __doc__
        """ generate_instances_for_object_sync(self, icalcomp:ICalGLib.Component, start:int, end:int, cancellable:Gio.Cancellable=None, cb:ECal.RecurInstanceCb, cb_data=None) """
        pass

    def generate_instances_sync(self, start, end, cancellable=None, cb, cb_data=None): # real signature unknown; restored from __doc__
        """ generate_instances_sync(self, start:int, end:int, cancellable:Gio.Cancellable=None, cb:ECal.RecurInstanceCb, cb_data=None) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_attachment_uris(self, uid, rid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_attachment_uris(self, uid:str, rid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_attachment_uris_finish(self, result): # real signature unknown; restored from __doc__
        """ get_attachment_uris_finish(self, result:Gio.AsyncResult) -> bool, out_attachment_uris:list """
        return False

    def get_attachment_uris_sync(self, uid, rid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_attachment_uris_sync(self, uid:str, rid:str, cancellable:Gio.Cancellable=None) -> bool, out_attachment_uris:list """
        return False

    def get_backend_property(self, prop_name, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_backend_property(self, prop_name:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_backend_property_finish(self, result): # real signature unknown; restored from __doc__
        """ get_backend_property_finish(self, result:Gio.AsyncResult) -> bool, prop_value:str """
        return False

    def get_backend_property_sync(self, prop_name, cancellable=None): # real signature unknown; restored from __doc__
        """ get_backend_property_sync(self, prop_name:str, cancellable:Gio.Cancellable=None) -> bool, prop_value:str """
        return False

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> list """
        return []

    def get_component_as_string(self, icalcomp): # real signature unknown; restored from __doc__
        """ get_component_as_string(self, icalcomp:ICalGLib.Component) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_object(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_default_object(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_default_object_finish(self, result): # real signature unknown; restored from __doc__
        """ get_default_object_finish(self, result:Gio.AsyncResult) -> bool, out_icalcomp:ICalGLib.Component """
        return False

    def get_default_object_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_default_object_sync(self, cancellable:Gio.Cancellable=None) -> bool, out_icalcomp:ICalGLib.Component """
        return False

    def get_default_timezone(self): # real signature unknown; restored from __doc__
        """ get_default_timezone(self) -> ICalGLib.Timezone """
        pass

    def get_free_busy(self, start, end, users, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_free_busy(self, start:int, end:int, users:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_free_busy_finish(self, result, out_freebusy): # real signature unknown; restored from __doc__
        """ get_free_busy_finish(self, result:Gio.AsyncResult, out_freebusy:list) -> bool """
        return False

    def get_free_busy_sync(self, start, end, users, out_freebusy, cancellable=None): # real signature unknown; restored from __doc__
        """ get_free_busy_sync(self, start:int, end:int, users:list, out_freebusy:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_local_attachment_store(self): # real signature unknown; restored from __doc__
        """ get_local_attachment_store(self) -> str """
        return ""

    def get_object(self, uid, rid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_object(self, uid:str, rid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_objects_for_uid(self, uid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_objects_for_uid(self, uid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_objects_for_uid_finish(self, result): # real signature unknown; restored from __doc__
        """ get_objects_for_uid_finish(self, result:Gio.AsyncResult) -> bool, out_ecalcomps:list """
        return False

    def get_objects_for_uid_sync(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_objects_for_uid_sync(self, uid:str, cancellable:Gio.Cancellable=None) -> bool, out_ecalcomps:list """
        return False

    def get_object_finish(self, result): # real signature unknown; restored from __doc__
        """ get_object_finish(self, result:Gio.AsyncResult) -> bool, out_icalcomp:ICalGLib.Component """
        return False

    def get_object_list(self, sexp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_object_list(self, sexp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_object_list_as_comps(self, sexp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_object_list_as_comps(self, sexp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_object_list_as_comps_finish(self, result): # real signature unknown; restored from __doc__
        """ get_object_list_as_comps_finish(self, result:Gio.AsyncResult) -> bool, out_ecalcomps:list """
        return False

    def get_object_list_as_comps_sync(self, sexp, cancellable=None): # real signature unknown; restored from __doc__
        """ get_object_list_as_comps_sync(self, sexp:str, cancellable:Gio.Cancellable=None) -> bool, out_ecalcomps:list """
        return False

    def get_object_list_finish(self, result): # real signature unknown; restored from __doc__
        """ get_object_list_finish(self, result:Gio.AsyncResult) -> bool, out_icalcomps:list """
        return False

    def get_object_list_sync(self, sexp, cancellable=None): # real signature unknown; restored from __doc__
        """ get_object_list_sync(self, sexp:str, cancellable:Gio.Cancellable=None) -> bool, out_icalcomps:list """
        return False

    def get_object_sync(self, uid, rid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_object_sync(self, uid:str, rid:str, cancellable:Gio.Cancellable=None) -> bool, out_icalcomp:ICalGLib.Component """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_source_type(self): # real signature unknown; restored from __doc__
        """ get_source_type(self) -> ECal.ClientSourceType """
        pass

    def get_timezone(self, tzid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_timezone(self, tzid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_timezone_finish(self, result): # real signature unknown; restored from __doc__
        """ get_timezone_finish(self, result:Gio.AsyncResult) -> bool, out_zone:ICalGLib.Timezone """
        return False

    def get_timezone_sync(self, tzid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_timezone_sync(self, tzid:str, cancellable:Gio.Cancellable=None) -> bool, out_zone:ICalGLib.Timezone """
        return False

    def get_view(self, sexp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_view(self, sexp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_view_finish(self, result): # real signature unknown; restored from __doc__
        """ get_view_finish(self, result:Gio.AsyncResult) -> bool, out_view:ECal.ClientView """
        return False

    def get_view_sync(self, sexp, cancellable=None): # real signature unknown; restored from __doc__
        """ get_view_sync(self, sexp:str, cancellable:Gio.Cancellable=None) -> bool, out_view:ECal.ClientView """
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

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_finish(self, res): # real signature unknown; restored from __doc__
        """ init_finish(self, res:Gio.AsyncResult) -> bool """
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

    def is_online(self): # real signature unknown; restored from __doc__
        """ is_online(self) -> bool """
        return False

    def is_opened(self): # real signature unknown; restored from __doc__
        """ is_opened(self) -> bool """
        return False

    def is_readonly(self): # real signature unknown; restored from __doc__
        """ is_readonly(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_timezones(self): # real signature unknown; restored from __doc__
        """ list_timezones(self) -> list """
        return []

    def modify_object(self, icalcomp, mod, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ modify_object(self, icalcomp:ICalGLib.Component, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def modify_objects(self, icalcomps, mod, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ modify_objects(self, icalcomps:list, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def modify_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ modify_objects_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def modify_objects_sync(self, icalcomps, mod, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_objects_sync(self, icalcomps:list, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def modify_object_finish(self, result): # real signature unknown; restored from __doc__
        """ modify_object_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def modify_object_sync(self, icalcomp, mod, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_object_sync(self, icalcomp:ICalGLib.Component, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
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

    def open(self, only_if_exists, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open(self, only_if_exists:bool, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def open_sync(self, only_if_exists, cancellable=None): # real signature unknown; restored from __doc__
        """ open_sync(self, only_if_exists:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def receive_objects(self, icalcomp, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ receive_objects(self, icalcomp:ICalGLib.Component, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def receive_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ receive_objects_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def receive_objects_sync(self, icalcomp, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ receive_objects_sync(self, icalcomp:ICalGLib.Component, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def refresh(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ refresh(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def refresh_finish(self, result): # real signature unknown; restored from __doc__
        """ refresh_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def refresh_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref_main_context(self): # real signature unknown; restored from __doc__
        """ ref_main_context(self) -> GLib.MainContext """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_object(self, uid, rid, mod, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_object(self, uid:str, rid:str, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_objects(self, ids, mod, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_objects(self, ids:list, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_objects_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_objects_sync(self, ids, mod, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_objects_sync(self, ids:list, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_object_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_object_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_object_sync(self, uid, rid, mod, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_object_sync(self, uid:str, rid:str, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def retrieve_capabilities(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ retrieve_capabilities(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def retrieve_capabilities_finish(self, result): # real signature unknown; restored from __doc__
        """ retrieve_capabilities_finish(self, result:Gio.AsyncResult) -> bool, capabilities:str """
        return False

    def retrieve_capabilities_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ retrieve_capabilities_sync(self, cancellable:Gio.Cancellable=None) -> bool, capabilities:str """
        return False

    def retrieve_properties(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ retrieve_properties(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def retrieve_properties_finish(self, result): # real signature unknown; restored from __doc__
        """ retrieve_properties_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def retrieve_properties_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ retrieve_properties_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_objects(self, icalcomp, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ send_objects(self, icalcomp:ICalGLib.Component, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def send_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ send_objects_finish(self, result:Gio.AsyncResult) -> bool, out_users:list, out_modified_icalcomp:ICalGLib.Component """
        return False

    def send_objects_sync(self, icalcomp, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ send_objects_sync(self, icalcomp:ICalGLib.Component, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_users:list, out_modified_icalcomp:ICalGLib.Component """
        return False

    def set_backend_property(self, prop_name, prop_value, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_backend_property(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_backend_property_finish(self, result): # real signature unknown; restored from __doc__
        """ set_backend_property_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_backend_property_sync(self, prop_name, prop_value, cancellable=None): # real signature unknown; restored from __doc__
        """ set_backend_property_sync(self, prop_name:str, prop_value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_bus_name(self, bus_name): # real signature unknown; restored from __doc__
        """ set_bus_name(self, bus_name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_timezone(self, zone): # real signature unknown; restored from __doc__
        """ set_default_timezone(self, zone:ICalGLib.Timezone) """
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

    def tzlookup_cb(self, tzid, ecalclient, cancellable=None): # real signature unknown; restored from __doc__
        """ tzlookup_cb(tzid:str, ecalclient:ECal.Client, cancellable:Gio.Cancellable=None) -> ICalGLib.Timezone or None """
        pass

    def tzlookup_icalcomp_cb(self, tzid, lookup_data, cancellable=None): # real signature unknown; restored from __doc__
        """ tzlookup_icalcomp_cb(tzid:str, lookup_data:ECal.ClientTzlookupICalCompData, cancellable:Gio.Cancellable=None) -> ICalGLib.Timezone or None """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unwrap_dbus_error(self, dbus_error): # real signature unknown; restored from __doc__
        """ unwrap_dbus_error(self, dbus_error:error) """
        pass

    def util_copy_object_slist(self, copy_to=None, objects): # real signature unknown; restored from __doc__
        """ util_copy_object_slist(copy_to:list=None, objects:list) -> list """
        return []

    def util_copy_string_slist(self, copy_to=None, strings): # real signature unknown; restored from __doc__
        """ util_copy_string_slist(copy_to:list=None, strings:list) -> list """
        return []

    def util_free_object_slist(self, objects): # real signature unknown; restored from __doc__
        """ util_free_object_slist(objects:list) """
        pass

    def util_free_string_slist(self, strings): # real signature unknown; restored from __doc__
        """ util_free_string_slist(strings:list) """
        pass

    def util_parse_comma_strings(self, strings): # real signature unknown; restored from __doc__
        """ util_parse_comma_strings(strings:str) -> list """
        return []

    def util_slist_to_strv(self, strings): # real signature unknown; restored from __doc__
        """ util_slist_to_strv(strings:list) -> list """
        return []

    def util_strv_to_slist(self, strv): # real signature unknown; restored from __doc__
        """ util_strv_to_slist(strv:str) -> list """
        return []

    def util_unwrap_dbus_error(self, dbus_error, known_errors, known_errors_count, known_errors_domain, fail_when_none_matched): # real signature unknown; restored from __doc__
        """ util_unwrap_dbus_error(dbus_error:error, known_errors:EDataServer.ClientErrorsList, known_errors_count:int, known_errors_domain:int, fail_when_none_matched:bool) -> bool, client_error:error """
        return False

    def wait_for_connected(self, timeout_seconds, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ wait_for_connected(self, timeout_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def wait_for_connected_finish(self, result): # real signature unknown; restored from __doc__
        """ wait_for_connected_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def wait_for_connected_sync(self, timeout_seconds, cancellable=None): # real signature unknown; restored from __doc__
        """ wait_for_connected_sync(self, timeout_seconds:int, cancellable:Gio.Cancellable=None) -> bool """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fe5ccdf7400>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Client), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalClient (94764814789616)>, '__doc__': None, '__gsignals__': {}, 'check_timezones_sync': gi.FunctionInfo(check_timezones_sync), 'connect': gi.FunctionInfo(connect), 'connect_finish': gi.FunctionInfo(connect_finish), 'connect_sync': gi.FunctionInfo(connect_sync), 'error_create': gi.FunctionInfo(error_create), 'error_quark': gi.FunctionInfo(error_quark), 'error_to_string': gi.FunctionInfo(error_to_string), 'tzlookup_cb': gi.FunctionInfo(tzlookup_cb), 'tzlookup_icalcomp_cb': gi.FunctionInfo(tzlookup_icalcomp_cb), 'add_timezone': gi.FunctionInfo(add_timezone), 'add_timezone_finish': gi.FunctionInfo(add_timezone_finish), 'add_timezone_sync': gi.FunctionInfo(add_timezone_sync), 'check_one_alarm_only': gi.FunctionInfo(check_one_alarm_only), 'check_organizer_must_accept': gi.FunctionInfo(check_organizer_must_accept), 'check_organizer_must_attend': gi.FunctionInfo(check_organizer_must_attend), 'check_recurrences_no_master': gi.FunctionInfo(check_recurrences_no_master), 'check_save_schedules': gi.FunctionInfo(check_save_schedules), 'create_object': gi.FunctionInfo(create_object), 'create_object_finish': gi.FunctionInfo(create_object_finish), 'create_object_sync': gi.FunctionInfo(create_object_sync), 'create_objects': gi.FunctionInfo(create_objects), 'create_objects_finish': gi.FunctionInfo(create_objects_finish), 'create_objects_sync': gi.FunctionInfo(create_objects_sync), 'discard_alarm': gi.FunctionInfo(discard_alarm), 'discard_alarm_finish': gi.FunctionInfo(discard_alarm_finish), 'discard_alarm_sync': gi.FunctionInfo(discard_alarm_sync), 'generate_instances': gi.FunctionInfo(generate_instances), 'generate_instances_for_object': gi.FunctionInfo(generate_instances_for_object), 'generate_instances_for_object_sync': gi.FunctionInfo(generate_instances_for_object_sync), 'generate_instances_sync': gi.FunctionInfo(generate_instances_sync), 'get_attachment_uris': gi.FunctionInfo(get_attachment_uris), 'get_attachment_uris_finish': gi.FunctionInfo(get_attachment_uris_finish), 'get_attachment_uris_sync': gi.FunctionInfo(get_attachment_uris_sync), 'get_component_as_string': gi.FunctionInfo(get_component_as_string), 'get_default_object': gi.FunctionInfo(get_default_object), 'get_default_object_finish': gi.FunctionInfo(get_default_object_finish), 'get_default_object_sync': gi.FunctionInfo(get_default_object_sync), 'get_default_timezone': gi.FunctionInfo(get_default_timezone), 'get_free_busy': gi.FunctionInfo(get_free_busy), 'get_free_busy_finish': gi.FunctionInfo(get_free_busy_finish), 'get_free_busy_sync': gi.FunctionInfo(get_free_busy_sync), 'get_local_attachment_store': gi.FunctionInfo(get_local_attachment_store), 'get_object': gi.FunctionInfo(get_object), 'get_object_finish': gi.FunctionInfo(get_object_finish), 'get_object_list': gi.FunctionInfo(get_object_list), 'get_object_list_as_comps': gi.FunctionInfo(get_object_list_as_comps), 'get_object_list_as_comps_finish': gi.FunctionInfo(get_object_list_as_comps_finish), 'get_object_list_as_comps_sync': gi.FunctionInfo(get_object_list_as_comps_sync), 'get_object_list_finish': gi.FunctionInfo(get_object_list_finish), 'get_object_list_sync': gi.FunctionInfo(get_object_list_sync), 'get_object_sync': gi.FunctionInfo(get_object_sync), 'get_objects_for_uid': gi.FunctionInfo(get_objects_for_uid), 'get_objects_for_uid_finish': gi.FunctionInfo(get_objects_for_uid_finish), 'get_objects_for_uid_sync': gi.FunctionInfo(get_objects_for_uid_sync), 'get_source_type': gi.FunctionInfo(get_source_type), 'get_timezone': gi.FunctionInfo(get_timezone), 'get_timezone_finish': gi.FunctionInfo(get_timezone_finish), 'get_timezone_sync': gi.FunctionInfo(get_timezone_sync), 'get_view': gi.FunctionInfo(get_view), 'get_view_finish': gi.FunctionInfo(get_view_finish), 'get_view_sync': gi.FunctionInfo(get_view_sync), 'modify_object': gi.FunctionInfo(modify_object), 'modify_object_finish': gi.FunctionInfo(modify_object_finish), 'modify_object_sync': gi.FunctionInfo(modify_object_sync), 'modify_objects': gi.FunctionInfo(modify_objects), 'modify_objects_finish': gi.FunctionInfo(modify_objects_finish), 'modify_objects_sync': gi.FunctionInfo(modify_objects_sync), 'receive_objects': gi.FunctionInfo(receive_objects), 'receive_objects_finish': gi.FunctionInfo(receive_objects_finish), 'receive_objects_sync': gi.FunctionInfo(receive_objects_sync), 'remove_object': gi.FunctionInfo(remove_object), 'remove_object_finish': gi.FunctionInfo(remove_object_finish), 'remove_object_sync': gi.FunctionInfo(remove_object_sync), 'remove_objects': gi.FunctionInfo(remove_objects), 'remove_objects_finish': gi.FunctionInfo(remove_objects_finish), 'remove_objects_sync': gi.FunctionInfo(remove_objects_sync), 'send_objects': gi.FunctionInfo(send_objects), 'send_objects_finish': gi.FunctionInfo(send_objects_finish), 'send_objects_sync': gi.FunctionInfo(send_objects_sync), 'set_default_timezone': gi.FunctionInfo(set_default_timezone), 'parent': <property object at 0x7fe5cce08770>, 'priv': <property object at 0x7fe5cce087c0>})"
    __gdoc__ = "Object ECalClient\n\nSignals from ECalClient:\n  free-busy-data (gpointer)\n\nProperties from ECalClient:\n  default-timezone -> ICalTimezone: Default Timezone\n    Timezone used to resolve DATE and floating DATE-TIME values\n  source-type -> ECalClientSourceType: Source Type\n    The iCalendar data type\n\nSignals from ETimezoneCache:\n  timezone-added (ICalTimezone)\n\nSignals from EClient:\n  opened (GError)\n  backend-error (gchararray)\n  backend-died ()\n  backend-property-changed (gchararray, gchararray)\n\nProperties from EClient:\n  capabilities -> gpointer: Capabilities\n    The capabilities of this client\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  online -> gboolean: Online\n    Whether this client is online\n  opened -> gboolean: Opened\n    Whether this client is open and ready to use\n  readonly -> gboolean: Read only\n    Whether this client's backing data is readonly\n  source -> ESource: Source\n    The ESource for which this client was created\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ECalClient (94764814789616)>'
    __info__ = ObjectInfo(Client)


