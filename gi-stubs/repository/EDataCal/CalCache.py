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


class CalCache(__gi_repository_EBackend.Cache, __gi_repository_ECal.TimezoneCache, __gi_repository_EDataServer.Extensible):
    """
    :Constructors:
    
    ::
    
        CalCache(**properties)
        new(filename:str, cancellable:Gio.Cancellable=None) -> EDataCal.CalCache or None
    """
    def add_timezone(self, zone): # real signature unknown; restored from __doc__
        """ add_timezone(self, zone:ICalGLib.Timezone) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_revision(self): # real signature unknown; restored from __doc__
        """ change_revision(self) """
        pass

    def clear_offline_changes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ clear_offline_changes(self, cancellable:Gio.Cancellable=None) -> bool """
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

    def contains(self, uid, rid=None, deleted_flag): # real signature unknown; restored from __doc__
        """ contains(self, uid:str, rid:str=None, deleted_flag:EBackend.CacheDeletedFlag) -> bool """
        return False

    def copy_missing_to_column_values(self, column_names, column_values, other_columns): # real signature unknown; restored from __doc__
        """ copy_missing_to_column_values(self, column_names:list, column_values:list, other_columns:EBackend.CacheColumnValues) -> other_columns:EBackend.CacheColumnValues """
        pass

    def delete_attachments(self, component, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_attachments(self, component:ICalGLib.Component, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_before_put(self, *args, **kwargs): # real signature unknown
        """ before_put(self, uid:str, revision:str, object:str, other_columns:EBackend.CacheColumnValues, is_replace:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_before_remove(self, *args, **kwargs): # real signature unknown
        """ before_remove(self, uid:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_clear_offline_changes_locked(self, *args, **kwargs): # real signature unknown
        """ clear_offline_changes_locked(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_dup_component_revision(self, *args, **kwargs): # real signature unknown
        """ dup_component_revision(self, icomp:ICalGLib.Component) -> str """
        pass

    def do_erase(self, *args, **kwargs): # real signature unknown
        """ erase(self) """
        pass

    def do_put_locked(self, *args, **kwargs): # real signature unknown
        """ put_locked(self, uid:str, revision:str, object:str, other_columns:EBackend.CacheColumnValues, offline_state:EBackend.OfflineState, is_replace:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_remove_locked(self, *args, **kwargs): # real signature unknown
        """ remove_locked(self, uid:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_revision_changed(self, *args, **kwargs): # real signature unknown
        """ revision_changed(self) """
        pass

    def dup_component_revision(self, icomp): # real signature unknown; restored from __doc__
        """ dup_component_revision(self, icomp:ICalGLib.Component) -> str """
        return ""

    def dup_key(self, key): # real signature unknown; restored from __doc__
        """ dup_key(self, key:str) -> str """
        return ""

    def dup_revision(self): # real signature unknown; restored from __doc__
        """ dup_revision(self) -> str """
        return ""

    def dup_timezone_as_string(self, tzid, cancellable=None): # real signature unknown; restored from __doc__
        """ dup_timezone_as_string(self, tzid:str, cancellable:Gio.Cancellable=None) -> bool, out_zone_string:str """
        return False

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def erase(self): # real signature unknown; restored from __doc__
        """ erase(self) """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, deleted_flag, where_clause=None, func, user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ foreach(self, deleted_flag:EBackend.CacheDeletedFlag, where_clause:str=None, func:EBackend.CacheForeachFunc, user_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def foreach_update(self, deleted_flag, where_clause=None, func, user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ foreach_update(self, deleted_flag:EBackend.CacheDeletedFlag, where_clause:str=None, func:EBackend.CacheUpdateFunc, user_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def freeze_revision_change(self): # real signature unknown; restored from __doc__
        """ freeze_revision_change(self) """
        pass

    def get(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get(self, uid:str, cancellable:Gio.Cancellable=None) -> str or None, out_revision:str, out_other_columns:EBackend.CacheColumnValues """
        return ""

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_component(self, uid, rid=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_component(self, uid:str, rid:str=None, cancellable:Gio.Cancellable=None) -> bool, out_component:ECal.Component """
        return False

    def get_components_by_uid(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_components_by_uid(self, uid:str, cancellable:Gio.Cancellable=None) -> bool, out_components:list """
        return False

    def get_components_by_uid_as_string(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_components_by_uid_as_string(self, uid:str, cancellable:Gio.Cancellable=None) -> bool, out_icalstrings:list """
        return False

    def get_components_in_range(self, range_start, range_end, cancellable=None): # real signature unknown; restored from __doc__
        """ get_components_in_range(self, range_start:int, range_end:int, cancellable:Gio.Cancellable=None) -> bool, out_components:list """
        return False

    def get_components_in_range_as_strings(self, range_start, range_end, cancellable=None): # real signature unknown; restored from __doc__
        """ get_components_in_range_as_strings(self, range_start:int, range_end:int, cancellable:Gio.Cancellable=None) -> bool, out_icalstrings:list """
        return False

    def get_component_as_string(self, uid, rid=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_component_as_string(self, uid:str, rid:str=None, cancellable:Gio.Cancellable=None) -> bool, out_icalstring:str """
        return False

    def get_component_custom_flags(self, uid, rid=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_component_custom_flags(self, uid:str, rid:str=None, cancellable:Gio.Cancellable=None) -> bool, out_custom_flags:int """
        return False

    def get_component_extra(self, uid, rid=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_component_extra(self, uid:str, rid:str=None, cancellable:Gio.Cancellable=None) -> bool, out_extra:str """
        return False

    def get_count(self, deleted_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ get_count(self, deleted_flag:EBackend.CacheDeletedFlag, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_ids_with_extra(self, extra, cancellable=None): # real signature unknown; restored from __doc__
        """ get_ids_with_extra(self, extra:str, cancellable:Gio.Cancellable=None) -> bool, out_ids:list """
        return False

    def get_key_int(self, key): # real signature unknown; restored from __doc__
        """ get_key_int(self, key:str) -> int """
        return 0

    def get_objects(self, deleted_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ get_objects(self, deleted_flag:EBackend.CacheDeletedFlag, cancellable:Gio.Cancellable=None) -> bool, out_objects:list, out_revisions:list """
        return False

    def get_object_include_deleted(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_object_include_deleted(self, uid:str, cancellable:Gio.Cancellable=None) -> str or None, out_revision:str, out_other_columns:EBackend.CacheColumnValues """
        return ""

    def get_offline_changes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_offline_changes(self, cancellable:Gio.Cancellable=None) -> list """
        return []

    def get_offline_state(self, uid, rid=None, cancellable=None): # real signature unknown; restored from __doc__
        """ get_offline_state(self, uid:str, rid:str=None, cancellable:Gio.Cancellable=None) -> EBackend.OfflineState """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sqlitedb(self): # real signature unknown; restored from __doc__
        """ get_sqlitedb(self) """
        pass

    def get_timezone(self, tzid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_timezone(self, tzid:str, cancellable:Gio.Cancellable=None) -> bool, out_zone:ICalGLib.Timezone """
        return False

    def get_uids(self, deleted_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ get_uids(self, deleted_flag:EBackend.CacheDeletedFlag, cancellable:Gio.Cancellable=None) -> bool, out_uids:list, out_revisions:list """
        return False

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> int """
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

    def initialize_sync(self, filename, other_columns=None, cancellable=None): # real signature unknown; restored from __doc__
        """ initialize_sync(self, filename:str, other_columns:list=None, cancellable:Gio.Cancellable=None) -> bool """
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

    def is_revision_change_frozen(self): # real signature unknown; restored from __doc__
        """ is_revision_change_frozen(self) -> bool """
        return False

    def list_extensions(self, extension_type): # real signature unknown; restored from __doc__
        """ list_extensions(self, extension_type:GType) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_timezones(self, cancellable=None): # real signature unknown; restored from __doc__
        """ list_timezones(self, cancellable:Gio.Cancellable=None) -> bool, out_timezones:list """
        return False

    def load_extensions(self): # real signature unknown; restored from __doc__
        """ load_extensions(self) """
        pass

    def lock(self, lock_type): # real signature unknown; restored from __doc__
        """ lock(self, lock_type:EBackend.CacheLockType) """
        pass

    def new(self, filename, cancellable=None): # real signature unknown; restored from __doc__
        """ new(filename:str, cancellable:Gio.Cancellable=None) -> EDataCal.CalCache or None """
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

    def put(self, uid, revision=None, p_object, other_columns=None, offline_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ put(self, uid:str, revision:str=None, object:str, other_columns:EBackend.CacheColumnValues=None, offline_flag:EBackend.CacheOfflineFlag, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_component(self, component, extra=None, custom_flags, offline_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ put_component(self, component:ECal.Component, extra:str=None, custom_flags:int, offline_flag:EBackend.CacheOfflineFlag, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_components(self, components, extras=None, custom_flags=None, offline_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ put_components(self, components:list, extras:list=None, custom_flags:list=None, offline_flag:EBackend.CacheOfflineFlag, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_timezone(self, zone, inc_ref_counts, cancellable=None): # real signature unknown; restored from __doc__
        """ put_timezone(self, zone:ICalGLib.Timezone, inc_ref_counts:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self, uid, offline_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ remove(self, uid:str, offline_flag:EBackend.CacheOfflineFlag, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_all(self, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_all(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_component(self, uid, rid=None, custom_flags, offline_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_component(self, uid:str, rid:str=None, custom_flags:int, offline_flag:EBackend.CacheOfflineFlag, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_components(self, ids, custom_flags=None, offline_flag, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_components(self, ids:list, custom_flags:list=None, offline_flag:EBackend.CacheOfflineFlag, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_timezone(self, tzid, dec_ref_counts, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_timezone(self, tzid:str, dec_ref_counts:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_timezones(self, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_timezones(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def resolve_timezone_cb(self, tzid, cal_cache=None, cancellable=None): # real signature unknown; restored from __doc__
        """ resolve_timezone_cb(tzid:str, cal_cache=None, cancellable:Gio.Cancellable=None) -> ICalGLib.Timezone or None """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def search(self, sexp=None, cancellable=None): # real signature unknown; restored from __doc__
        """ search(self, sexp:str=None, cancellable:Gio.Cancellable=None) -> bool, out_data:list """
        return False

    def search_components(self, sexp=None, cancellable=None): # real signature unknown; restored from __doc__
        """ search_components(self, sexp:str=None, cancellable:Gio.Cancellable=None) -> bool, out_components:list """
        return False

    def search_ids(self, sexp=None, cancellable=None): # real signature unknown; restored from __doc__
        """ search_ids(self, sexp:str=None, cancellable:Gio.Cancellable=None) -> bool, out_ids:list """
        return False

    def search_with_callback(self, sexp=None, func=None, user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ search_with_callback(self, sexp:str=None, func:EDataCal.CalCacheSearchFunc=None, user_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_component_custom_flags(self, uid, rid=None, custom_flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_component_custom_flags(self, uid:str, rid:str=None, custom_flags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_component_extra(self, uid, rid=None, extra=None, cancellable=None): # real signature unknown; restored from __doc__
        """ set_component_extra(self, uid:str, rid:str=None, extra:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_key(self, key, value=None): # real signature unknown; restored from __doc__
        """ set_key(self, key:str, value:str=None) -> bool """
        return False

    def set_key_int(self, key, value): # real signature unknown; restored from __doc__
        """ set_key_int(self, key:str, value:int) -> bool """
        return False

    def set_offline_state(self, uid, state, cancellable=None): # real signature unknown; restored from __doc__
        """ set_offline_state(self, uid:str, state:EBackend.OfflineState, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_revision(self, revision=None): # real signature unknown; restored from __doc__
        """ set_revision(self, revision:str=None) """
        pass

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:int) """
        pass

    def sqlite_exec(self, sql_stmt, cancellable=None): # real signature unknown; restored from __doc__
        """ sqlite_exec(self, sql_stmt:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def sqlite_maybe_vacuum(self, cancellable=None): # real signature unknown; restored from __doc__
        """ sqlite_maybe_vacuum(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def sqlite_select(self, sql_stmt, func, user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ sqlite_select(self, sql_stmt:str, func:EBackend.CacheSelectFunc, user_data=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def sqlite_stmt_free(self, stmt): # real signature unknown; restored from __doc__
        """ sqlite_stmt_free(stmt:str) """
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

    def thaw_revision_change(self): # real signature unknown; restored from __doc__
        """ thaw_revision_change(self) """
        pass

    def unlock(self, action): # real signature unknown; restored from __doc__
        """ unlock(self, action:EBackend.CacheUnlockAction) """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb65e5ddaf0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CalCache), '__module__': 'gi.repository.EDataCal', '__gtype__': <GType ECalCache (94060045415648)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'resolve_timezone_cb': gi.FunctionInfo(resolve_timezone_cb), 'contains': gi.FunctionInfo(contains), 'delete_attachments': gi.FunctionInfo(delete_attachments), 'dup_component_revision': gi.FunctionInfo(dup_component_revision), 'dup_timezone_as_string': gi.FunctionInfo(dup_timezone_as_string), 'get_component': gi.FunctionInfo(get_component), 'get_component_as_string': gi.FunctionInfo(get_component_as_string), 'get_component_custom_flags': gi.FunctionInfo(get_component_custom_flags), 'get_component_extra': gi.FunctionInfo(get_component_extra), 'get_components_by_uid': gi.FunctionInfo(get_components_by_uid), 'get_components_by_uid_as_string': gi.FunctionInfo(get_components_by_uid_as_string), 'get_components_in_range': gi.FunctionInfo(get_components_in_range), 'get_components_in_range_as_strings': gi.FunctionInfo(get_components_in_range_as_strings), 'get_ids_with_extra': gi.FunctionInfo(get_ids_with_extra), 'get_offline_changes': gi.FunctionInfo(get_offline_changes), 'get_offline_state': gi.FunctionInfo(get_offline_state), 'get_timezone': gi.FunctionInfo(get_timezone), 'list_timezones': gi.FunctionInfo(list_timezones), 'put_component': gi.FunctionInfo(put_component), 'put_components': gi.FunctionInfo(put_components), 'put_timezone': gi.FunctionInfo(put_timezone), 'remove_component': gi.FunctionInfo(remove_component), 'remove_components': gi.FunctionInfo(remove_components), 'remove_timezone': gi.FunctionInfo(remove_timezone), 'remove_timezones': gi.FunctionInfo(remove_timezones), 'search': gi.FunctionInfo(search), 'search_components': gi.FunctionInfo(search_components), 'search_ids': gi.FunctionInfo(search_ids), 'search_with_callback': gi.FunctionInfo(search_with_callback), 'set_component_custom_flags': gi.FunctionInfo(set_component_custom_flags), 'set_component_extra': gi.FunctionInfo(set_component_extra), 'do_dup_component_revision': gi.VFuncInfo(dup_component_revision), 'parent': <property object at 0x7fb65e5fb090>, 'priv': <property object at 0x7fb65e5fb1d0>})"
    __gdoc__ = 'Object ECalCache\n\nSignals from ECalCache:\n  dup-component-revision (ICalComponent) -> gchararray\n  get-timezone (gchararray) -> ICalTimezone\n\nSignals from ETimezoneCache:\n  timezone-added (ICalTimezone)\n\nSignals from ECache:\n  before-put (gchararray, gchararray, gchararray, ECacheColumnValues, gboolean, GCancellable, gpointer) -> gboolean\n  before-remove (gchararray, GCancellable, gpointer) -> gboolean\n  revision-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ECalCache (94060045415648)>'
    __info__ = ObjectInfo(CalCache)


