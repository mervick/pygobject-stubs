# encoding: utf-8
# module gi.repository.EDataCal
# from /usr/lib64/girepository-1.0/EDataCal-2.0.typelib
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
import gi.repository.EBackend as __gi_repository_EBackend
import gi.repository.ECal as __gi_repository_ECal
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio


class CalBackend(__gi_repository_EBackend.Backend, __gi_repository_ECal.TimezoneCache):
    """
    :Constructors:
    
    ::
    
        CalBackend(**properties)
    """
    def add_timezone(self, tzobject, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_timezone(self, tzobject:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_timezone_finish(self, result): # real signature unknown; restored from __doc__
        """ add_timezone_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def add_timezone_sync(self, tzobject, cancellable=None): # real signature unknown; restored from __doc__
        """ add_timezone_sync(self, tzobject:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def add_view(self, view): # real signature unknown; restored from __doc__
        """ add_view(self, view:EDataCal.DataCalView) """
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

    def create_cache_filename(self, uid, filename, fileindex): # real signature unknown; restored from __doc__
        """ create_cache_filename(self, uid:str, filename:str, fileindex:int) -> str """
        return ""

    def create_objects(self, calobjs, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_objects(self, calobjs:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_objects_finish(self, result, out_uids): # real signature unknown; restored from __doc__
        """ create_objects_finish(self, result:Gio.AsyncResult, out_uids:GLib.Queue) -> bool """
        return False

    def create_objects_sync(self, calobjs, opflags, out_uids, cancellable=None): # real signature unknown; restored from __doc__
        """ create_objects_sync(self, calobjs:str, opflags:int, out_uids:GLib.Queue, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def credentials_required_finish(self, result): # real signature unknown; restored from __doc__
        """ credentials_required_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def credentials_required_sync(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None): # real signature unknown; restored from __doc__
        """ credentials_required_sync(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def discard_alarm(self, uid, rid, alarm_uid, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ discard_alarm(self, uid:str, rid:str, alarm_uid:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def discard_alarm_finish(self, result): # real signature unknown; restored from __doc__
        """ discard_alarm_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def discard_alarm_sync(self, uid, rid, alarm_uid, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ discard_alarm_sync(self, uid:str, rid:str, alarm_uid:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authenticate_sync(self, *args, **kwargs): # real signature unknown
        """ authenticate_sync(self, credentials:EDataServer.NamedParameters, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, cancellable:Gio.Cancellable=None) -> EDataServer.SourceAuthenticationResult """
        pass

    def do_closed(self, *args, **kwargs): # real signature unknown
        """ closed(self, sender:str) """
        pass

    def do_get_destination_address(self, *args, **kwargs): # real signature unknown
        """ get_destination_address(self) -> bool, host:str, port:int """
        pass

    def do_impl_add_timezone(self, *args, **kwargs): # real signature unknown
        """ impl_add_timezone(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, tzobject:str) """
        pass

    def do_impl_discard_alarm(self, *args, **kwargs): # real signature unknown
        """ impl_discard_alarm(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, uid:str, rid:str, auid:str, opflags:int) """
        pass

    def do_impl_get_attachment_uris(self, *args, **kwargs): # real signature unknown
        """ impl_get_attachment_uris(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, uid:str, rid:str) """
        pass

    def do_impl_get_backend_property(self, *args, **kwargs): # real signature unknown
        """ impl_get_backend_property(self, prop_name:str) -> str """
        pass

    def do_impl_get_object(self, *args, **kwargs): # real signature unknown
        """ impl_get_object(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, uid:str, rid:str) """
        pass

    def do_impl_get_object_list(self, *args, **kwargs): # real signature unknown
        """ impl_get_object_list(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, sexp:str) """
        pass

    def do_impl_get_timezone(self, *args, **kwargs): # real signature unknown
        """ impl_get_timezone(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, tzid:str) """
        pass

    def do_impl_open(self, *args, **kwargs): # real signature unknown
        """ impl_open(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None) """
        pass

    def do_impl_receive_objects(self, *args, **kwargs): # real signature unknown
        """ impl_receive_objects(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, calobj:str, opflags:int) """
        pass

    def do_impl_refresh(self, *args, **kwargs): # real signature unknown
        """ impl_refresh(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None) """
        pass

    def do_impl_send_objects(self, *args, **kwargs): # real signature unknown
        """ impl_send_objects(self, cal:EDataCal.DataCal, opid:int, cancellable:Gio.Cancellable=None, calobj:str, opflags:int) """
        pass

    def do_impl_start_view(self, *args, **kwargs): # real signature unknown
        """ impl_start_view(self, view:EDataCal.DataCalView) """
        pass

    def do_impl_stop_view(self, *args, **kwargs): # real signature unknown
        """ impl_stop_view(self, view:EDataCal.DataCalView) """
        pass

    def do_prepare_shutdown(self, *args, **kwargs): # real signature unknown
        """ prepare_shutdown(self) """
        pass

    def do_shutdown(self, *args, **kwargs): # real signature unknown
        """ shutdown(self) """
        pass

    def dup_cache_dir(self): # real signature unknown; restored from __doc__
        """ dup_cache_dir(self) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_online_state_updated(self, cancellable=None): # real signature unknown; restored from __doc__
        """ ensure_online_state_updated(self, cancellable:Gio.Cancellable=None) """
        pass

    def ensure_source_status_connected(self): # real signature unknown; restored from __doc__
        """ ensure_source_status_connected(self) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach_view(self, func=None, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_view(self, func:EDataCal.CalBackendForeachViewFunc=None, user_data=None) -> bool """
        return False

    def foreach_view_notify_progress(self, only_completed_views, percent, message=None): # real signature unknown; restored from __doc__
        """ foreach_view_notify_progress(self, only_completed_views:bool, percent:int, message:str=None) """
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

    def get_attachment_uris(self, uid, rid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_attachment_uris(self, uid:str, rid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_attachment_uris_finish(self, result, out_attachment_uris): # real signature unknown; restored from __doc__
        """ get_attachment_uris_finish(self, result:Gio.AsyncResult, out_attachment_uris:GLib.Queue) -> bool """
        return False

    def get_attachment_uris_sync(self, uid, rid, out_attachment_uris, cancellable=None): # real signature unknown; restored from __doc__
        """ get_attachment_uris_sync(self, uid:str, rid:str, out_attachment_uris:GLib.Queue, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_backend_property(self, prop_name): # real signature unknown; restored from __doc__
        """ get_backend_property(self, prop_name:str) -> str """
        return ""

    def get_cache_dir(self): # real signature unknown; restored from __doc__
        """ get_cache_dir(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_destination_address(self): # real signature unknown; restored from __doc__
        """ get_destination_address(self) -> bool, host:str, port:int """
        return False

    def get_free_busy(self, start, end, users, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_free_busy(self, start:int, end:int, users:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_free_busy_finish(self, result, out_freebusy): # real signature unknown; restored from __doc__
        """ get_free_busy_finish(self, result:Gio.AsyncResult, out_freebusy:list) -> bool """
        return False

    def get_free_busy_sync(self, start, end, users, out_freebusy, cancellable=None): # real signature unknown; restored from __doc__
        """ get_free_busy_sync(self, start:int, end:int, users:list, out_freebusy:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> ICalGLib.ComponentKind """
        pass

    def get_object(self, uid, rid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_object(self, uid:str, rid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_object_finish(self, result): # real signature unknown; restored from __doc__
        """ get_object_finish(self, result:Gio.AsyncResult) -> str """
        return ""

    def get_object_list(self, query, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_object_list(self, query:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_object_list_finish(self, result, out_objects): # real signature unknown; restored from __doc__
        """ get_object_list_finish(self, result:Gio.AsyncResult, out_objects:GLib.Queue) -> bool """
        return False

    def get_object_list_sync(self, query, out_objects, cancellable=None): # real signature unknown; restored from __doc__
        """ get_object_list_sync(self, query:str, out_objects:GLib.Queue, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_object_sync(self, uid, rid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_object_sync(self, uid:str, rid:str, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def get_online(self): # real signature unknown; restored from __doc__
        """ get_online(self) -> bool """
        return False

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

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_timezone(self, tzid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_timezone(self, tzid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_timezone_finish(self, result): # real signature unknown; restored from __doc__
        """ get_timezone_finish(self, result:Gio.AsyncResult) -> str """
        return ""

    def get_timezone_sync(self, tzid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_timezone_sync(self, tzid:str, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def get_user_prompter(self): # real signature unknown; restored from __doc__
        """ get_user_prompter(self) """
        pass

    def get_writable(self): # real signature unknown; restored from __doc__
        """ get_writable(self) -> bool """
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

    def is_destination_reachable(self, cancellable=None): # real signature unknown; restored from __doc__
        """ is_destination_reachable(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
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

    def list_views(self): # real signature unknown; restored from __doc__
        """ list_views(self) -> list """
        return []

    def mail_account_get_default(self, registry, address, name): # real signature unknown; restored from __doc__
        """ mail_account_get_default(registry:EDataServer.SourceRegistry, address:str, name:str) -> bool """
        return False

    def mail_account_is_valid(self, registry, user, name): # real signature unknown; restored from __doc__
        """ mail_account_is_valid(registry:EDataServer.SourceRegistry, user:str, name:str) -> bool """
        return False

    def modify_objects(self, calobjs, mod, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ modify_objects(self, calobjs:str, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def modify_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ modify_objects_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def modify_objects_sync(self, calobjs, mod, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_objects_sync(self, calobjs:str, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_component_created(self, component): # real signature unknown; restored from __doc__
        """ notify_component_created(self, component:ECal.Component) """
        pass

    def notify_component_modified(self, old_component, new_component): # real signature unknown; restored from __doc__
        """ notify_component_modified(self, old_component:ECal.Component, new_component:ECal.Component) """
        pass

    def notify_component_removed(self, id, old_component, new_component): # real signature unknown; restored from __doc__
        """ notify_component_removed(self, id:ECal.ComponentId, old_component:ECal.Component, new_component:ECal.Component) """
        pass

    def notify_error(self, message): # real signature unknown; restored from __doc__
        """ notify_error(self, message:str) """
        pass

    def notify_property_changed(self, prop_name, prop_value=None): # real signature unknown; restored from __doc__
        """ notify_property_changed(self, prop_name:str, prop_value:str=None) """
        pass

    def open(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_finish(self, result): # real signature unknown; restored from __doc__
        """ open_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def open_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def prepare_for_completion(self, opid, result_queue): # real signature unknown; restored from __doc__
        """ prepare_for_completion(self, opid:int, result_queue:GLib.Queue) -> Gio.SimpleAsyncResult """
        pass

    def prepare_shutdown(self): # real signature unknown; restored from __doc__
        """ prepare_shutdown(self) """
        pass

    def receive_objects(self, calobj, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ receive_objects(self, calobj:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def receive_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ receive_objects_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def receive_objects_sync(self, calobj, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ receive_objects_sync(self, calobj:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
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

    def ref_connectable(self): # real signature unknown; restored from __doc__
        """ ref_connectable(self) -> Gio.SocketConnectable or None """
        pass

    def ref_data_cal(self): # real signature unknown; restored from __doc__
        """ ref_data_cal(self) -> EDataCal.DataCal """
        pass

    def ref_main_context(self): # real signature unknown; restored from __doc__
        """ ref_main_context(self) -> GLib.MainContext """
        pass

    def ref_proxy_resolver(self): # real signature unknown; restored from __doc__
        """ ref_proxy_resolver(self) -> Gio.ProxyResolver or None """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_objects(self, component_ids, mod, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_objects(self, component_ids:list, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_objects_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_objects_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_objects_sync(self, component_ids, mod, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_objects_sync(self, component_ids:list, mod:ECal.ObjModType, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_view(self, view): # real signature unknown; restored from __doc__
        """ remove_view(self, view:EDataCal.DataCalView) """
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

    def schedule_authenticate(self, credentials=None): # real signature unknown; restored from __doc__
        """ schedule_authenticate(self, credentials:EDataServer.NamedParameters=None) """
        pass

    def schedule_credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, who_calls=None): # real signature unknown; restored from __doc__
        """ schedule_credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, who_calls:str=None) """
        pass

    def schedule_custom_operation(self, use_cancellable=None, func, user_data=None): # real signature unknown; restored from __doc__
        """ schedule_custom_operation(self, use_cancellable:Gio.Cancellable=None, func:EDataCal.CalBackendCustomOpFunc, user_data=None) """
        pass

    def send_objects(self, calobj, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ send_objects(self, calobj:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def send_objects_finish(self, result, out_users): # real signature unknown; restored from __doc__
        """ send_objects_finish(self, result:Gio.AsyncResult, out_users:GLib.Queue) -> str """
        return ""

    def send_objects_sync(self, calobj, opflags, out_users, cancellable=None): # real signature unknown; restored from __doc__
        """ send_objects_sync(self, calobj:str, opflags:int, out_users:GLib.Queue, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def set_cache_dir(self, cache_dir): # real signature unknown; restored from __doc__
        """ set_cache_dir(self, cache_dir:str) """
        pass

    def set_connectable(self, connectable): # real signature unknown; restored from __doc__
        """ set_connectable(self, connectable:Gio.SocketConnectable) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data_cal(self, data_cal): # real signature unknown; restored from __doc__
        """ set_data_cal(self, data_cal:EDataCal.DataCal) """
        pass

    def set_online(self, online): # real signature unknown; restored from __doc__
        """ set_online(self, online:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_writable(self, writable): # real signature unknown; restored from __doc__
        """ set_writable(self, writable:bool) """
        pass

    def start_view(self, view): # real signature unknown; restored from __doc__
        """ start_view(self, view:EDataCal.DataCalView) """
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

    def stop_view(self, view): # real signature unknown; restored from __doc__
        """ stop_view(self, view:EDataCal.DataCalView) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def trust_prompt(self, parameters, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ trust_prompt(self, parameters:EDataServer.NamedParameters, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def trust_prompt_finish(self, result): # real signature unknown; restored from __doc__
        """ trust_prompt_finish(self, result:Gio.AsyncResult) -> EDataServer.TrustPromptResponse """
        pass

    def trust_prompt_sync(self, parameters, cancellable=None): # real signature unknown; restored from __doc__
        """ trust_prompt_sync(self, parameters:EDataServer.NamedParameters, cancellable:Gio.Cancellable=None) -> EDataServer.TrustPromptResponse """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def user_declined(self, registry, icalcomp): # real signature unknown; restored from __doc__
        """ user_declined(registry:EDataServer.SourceRegistry, icalcomp:ICalGLib.Component) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb65af4a940>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CalBackend), '__module__': 'gi.repository.EDataCal', '__gtype__': <GType ECalBackend (94060045360192)>, '__doc__': None, '__gsignals__': {}, 'mail_account_get_default': gi.FunctionInfo(mail_account_get_default), 'mail_account_is_valid': gi.FunctionInfo(mail_account_is_valid), 'user_declined': gi.FunctionInfo(user_declined), 'add_timezone': gi.FunctionInfo(add_timezone), 'add_timezone_finish': gi.FunctionInfo(add_timezone_finish), 'add_timezone_sync': gi.FunctionInfo(add_timezone_sync), 'add_view': gi.FunctionInfo(add_view), 'create_cache_filename': gi.FunctionInfo(create_cache_filename), 'create_objects': gi.FunctionInfo(create_objects), 'create_objects_finish': gi.FunctionInfo(create_objects_finish), 'create_objects_sync': gi.FunctionInfo(create_objects_sync), 'discard_alarm': gi.FunctionInfo(discard_alarm), 'discard_alarm_finish': gi.FunctionInfo(discard_alarm_finish), 'discard_alarm_sync': gi.FunctionInfo(discard_alarm_sync), 'dup_cache_dir': gi.FunctionInfo(dup_cache_dir), 'foreach_view': gi.FunctionInfo(foreach_view), 'foreach_view_notify_progress': gi.FunctionInfo(foreach_view_notify_progress), 'get_attachment_uris': gi.FunctionInfo(get_attachment_uris), 'get_attachment_uris_finish': gi.FunctionInfo(get_attachment_uris_finish), 'get_attachment_uris_sync': gi.FunctionInfo(get_attachment_uris_sync), 'get_backend_property': gi.FunctionInfo(get_backend_property), 'get_cache_dir': gi.FunctionInfo(get_cache_dir), 'get_free_busy': gi.FunctionInfo(get_free_busy), 'get_free_busy_finish': gi.FunctionInfo(get_free_busy_finish), 'get_free_busy_sync': gi.FunctionInfo(get_free_busy_sync), 'get_kind': gi.FunctionInfo(get_kind), 'get_object': gi.FunctionInfo(get_object), 'get_object_finish': gi.FunctionInfo(get_object_finish), 'get_object_list': gi.FunctionInfo(get_object_list), 'get_object_list_finish': gi.FunctionInfo(get_object_list_finish), 'get_object_list_sync': gi.FunctionInfo(get_object_list_sync), 'get_object_sync': gi.FunctionInfo(get_object_sync), 'get_registry': gi.FunctionInfo(get_registry), 'get_timezone': gi.FunctionInfo(get_timezone), 'get_timezone_finish': gi.FunctionInfo(get_timezone_finish), 'get_timezone_sync': gi.FunctionInfo(get_timezone_sync), 'get_writable': gi.FunctionInfo(get_writable), 'is_opened': gi.FunctionInfo(is_opened), 'is_readonly': gi.FunctionInfo(is_readonly), 'list_views': gi.FunctionInfo(list_views), 'modify_objects': gi.FunctionInfo(modify_objects), 'modify_objects_finish': gi.FunctionInfo(modify_objects_finish), 'modify_objects_sync': gi.FunctionInfo(modify_objects_sync), 'notify_component_created': gi.FunctionInfo(notify_component_created), 'notify_component_modified': gi.FunctionInfo(notify_component_modified), 'notify_component_removed': gi.FunctionInfo(notify_component_removed), 'notify_error': gi.FunctionInfo(notify_error), 'notify_property_changed': gi.FunctionInfo(notify_property_changed), 'open': gi.FunctionInfo(open), 'open_finish': gi.FunctionInfo(open_finish), 'open_sync': gi.FunctionInfo(open_sync), 'prepare_for_completion': gi.FunctionInfo(prepare_for_completion), 'receive_objects': gi.FunctionInfo(receive_objects), 'receive_objects_finish': gi.FunctionInfo(receive_objects_finish), 'receive_objects_sync': gi.FunctionInfo(receive_objects_sync), 'ref_data_cal': gi.FunctionInfo(ref_data_cal), 'ref_proxy_resolver': gi.FunctionInfo(ref_proxy_resolver), 'refresh': gi.FunctionInfo(refresh), 'refresh_finish': gi.FunctionInfo(refresh_finish), 'refresh_sync': gi.FunctionInfo(refresh_sync), 'remove_objects': gi.FunctionInfo(remove_objects), 'remove_objects_finish': gi.FunctionInfo(remove_objects_finish), 'remove_objects_sync': gi.FunctionInfo(remove_objects_sync), 'remove_view': gi.FunctionInfo(remove_view), 'schedule_custom_operation': gi.FunctionInfo(schedule_custom_operation), 'send_objects': gi.FunctionInfo(send_objects), 'send_objects_finish': gi.FunctionInfo(send_objects_finish), 'send_objects_sync': gi.FunctionInfo(send_objects_sync), 'set_cache_dir': gi.FunctionInfo(set_cache_dir), 'set_data_cal': gi.FunctionInfo(set_data_cal), 'set_writable': gi.FunctionInfo(set_writable), 'start_view': gi.FunctionInfo(start_view), 'stop_view': gi.FunctionInfo(stop_view), 'do_closed': gi.VFuncInfo(closed), 'do_impl_add_timezone': gi.VFuncInfo(impl_add_timezone), 'do_impl_discard_alarm': gi.VFuncInfo(impl_discard_alarm), 'do_impl_get_attachment_uris': gi.VFuncInfo(impl_get_attachment_uris), 'do_impl_get_backend_property': gi.VFuncInfo(impl_get_backend_property), 'do_impl_get_object': gi.VFuncInfo(impl_get_object), 'do_impl_get_object_list': gi.VFuncInfo(impl_get_object_list), 'do_impl_get_timezone': gi.VFuncInfo(impl_get_timezone), 'do_impl_open': gi.VFuncInfo(impl_open), 'do_impl_receive_objects': gi.VFuncInfo(impl_receive_objects), 'do_impl_refresh': gi.VFuncInfo(impl_refresh), 'do_impl_send_objects': gi.VFuncInfo(impl_send_objects), 'do_impl_start_view': gi.VFuncInfo(impl_start_view), 'do_impl_stop_view': gi.VFuncInfo(impl_stop_view), 'do_shutdown': gi.VFuncInfo(shutdown), 'parent': <property object at 0x7fb65e5edf40>, 'priv': <property object at 0x7fb65e5edf90>})"
    __gdoc__ = "Object ECalBackend\n\nSignals from ECalBackend:\n  closed (gchararray)\n  shutdown ()\n\nProperties from ECalBackend:\n  cache-dir -> gchararray: Cache Dir\n    The backend's cache directory\n  kind -> gulong: Kind\n    The kind of iCalendar components this backend manages\n  proxy-resolver -> GProxyResolver: Proxy Resolver\n    The proxy resolver for this backend\n  registry -> ESourceRegistry: Registry\n    Data source registry\n  writable -> gboolean: Writable\n    Whether the backend will accept changes\n\nSignals from ETimezoneCache:\n  timezone-added (ICalTimezone)\n\nProperties from EBackend:\n  connectable -> GSocketConnectable: Connectable\n    Socket endpoint of a network service\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  online -> gboolean: Online\n    Whether the backend is online\n  source -> ESource: Source\n    The data source being acted upon\n  user-prompter -> EUserPrompter: User Prompter\n    User prompter instance\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ECalBackend (94060045360192)>'
    __info__ = ObjectInfo(CalBackend)


