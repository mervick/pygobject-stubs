# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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


class DB(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        DB(**properties)
        new(filename:str) -> Camel.DB
    """
    def abort_transaction(self): # real signature unknown; restored from __doc__
        """ abort_transaction(self) -> int """
        return 0

    def add_to_transaction(self, query): # real signature unknown; restored from __doc__
        """ add_to_transaction(self, query:str) -> int """
        return 0

    def begin_transaction(self): # real signature unknown; restored from __doc__
        """ begin_transaction(self) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def camel_mir_free(self, record=None): # real signature unknown; restored from __doc__
        """ camel_mir_free(record:Camel.MIRecord=None) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_folder_summary(self, folder_name): # real signature unknown; restored from __doc__
        """ clear_folder_summary(self, folder_name:str) -> int """
        return 0

    def command(self, stmt): # real signature unknown; restored from __doc__
        """ command(self, stmt:str) -> int """
        return 0

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

    def count_deleted_message_info(self, table_name): # real signature unknown; restored from __doc__
        """ count_deleted_message_info(self, table_name:str) -> int, count:int """
        return 0

    def count_junk_message_info(self, table_name): # real signature unknown; restored from __doc__
        """ count_junk_message_info(self, table_name:str) -> int, count:int """
        return 0

    def count_junk_not_deleted_message_info(self, table_name, count): # real signature unknown; restored from __doc__
        """ count_junk_not_deleted_message_info(self, table_name:str, count:int) -> int """
        return 0

    def count_message_info(self, query): # real signature unknown; restored from __doc__
        """ count_message_info(self, query:str) -> int, count:int """
        return 0

    def count_total_message_info(self, table_name): # real signature unknown; restored from __doc__
        """ count_total_message_info(self, table_name:str) -> int, count:int """
        return 0

    def count_unread_message_info(self, table_name): # real signature unknown; restored from __doc__
        """ count_unread_message_info(self, table_name:str) -> int, count:int """
        return 0

    def count_visible_message_info(self, table_name): # real signature unknown; restored from __doc__
        """ count_visible_message_info(self, table_name:str) -> int, count:int """
        return 0

    def count_visible_unread_message_info(self, table_name): # real signature unknown; restored from __doc__
        """ count_visible_unread_message_info(self, table_name:str) -> int, count:int """
        return 0

    def create_folders_table(self): # real signature unknown; restored from __doc__
        """ create_folders_table(self) -> int """
        return 0

    def delete_folder(self, folder_name): # real signature unknown; restored from __doc__
        """ delete_folder(self, folder_name:str) -> int """
        return 0

    def delete_uid(self, folder_name, uid): # real signature unknown; restored from __doc__
        """ delete_uid(self, folder_name:str, uid:str) -> int """
        return 0

    def delete_uids(self, folder_name, uids): # real signature unknown; restored from __doc__
        """ delete_uids(self, folder_name:str, uids:list) -> int """
        return 0

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

    def end_transaction(self): # real signature unknown; restored from __doc__
        """ end_transaction(self) -> int """
        return 0

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush_in_memory_transactions(self, folder_name): # real signature unknown; restored from __doc__
        """ flush_in_memory_transactions(self, folder_name:str) -> int """
        return 0

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

    def free_sqlized_string(self, string=None): # real signature unknown; restored from __doc__
        """ free_sqlized_string(string:str=None) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_column_ident(self, hash, index, col_names): # real signature unknown; restored from __doc__
        """ get_column_ident(hash:dict, index:int, col_names:list) -> Camel.DBKnownColumnNames, hash:dict """
        pass

    def get_column_name(self, raw_name): # real signature unknown; restored from __doc__
        """ get_column_name(raw_name:str) -> str or None """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_folder_deleted_uids(self, folder_name): # real signature unknown; restored from __doc__
        """ get_folder_deleted_uids(self, folder_name:str) -> list or None """
        return []

    def get_folder_junk_uids(self, folder_name): # real signature unknown; restored from __doc__
        """ get_folder_junk_uids(self, folder_name:str) -> list or None """
        return []

    def get_folder_uids(self, folder_name, sort_by=None, collate=None, hash): # real signature unknown; restored from __doc__
        """ get_folder_uids(self, folder_name:str, sort_by:str=None, collate:str=None, hash:dict) -> int """
        return 0

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

    def maybe_run_maintenance(self): # real signature unknown; restored from __doc__
        """ maybe_run_maintenance(self) -> bool """
        return False

    def new(self, filename): # real signature unknown; restored from __doc__
        """ new(filename:str) -> Camel.DB """
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

    def prepare_message_info_table(self, folder_name): # real signature unknown; restored from __doc__
        """ prepare_message_info_table(self, folder_name:str) -> int """
        return 0

    def read_folder_info_record(self, folder_name): # real signature unknown; restored from __doc__
        """ read_folder_info_record(self, folder_name:str) -> int, record:Camel.FIRecord """
        return 0

    def read_message_info_records(self, folder_name, user_data=None, callback): # real signature unknown; restored from __doc__
        """ read_message_info_records(self, folder_name:str, user_data=None, callback:Camel.DBSelectCB) -> int """
        return 0

    def read_message_info_record_with_uid(self, folder_name, uid, user_data=None, callback): # real signature unknown; restored from __doc__
        """ read_message_info_record_with_uid(self, folder_name:str, uid:str, user_data=None, callback:Camel.DBSelectCB) -> int """
        return 0

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def release_cache_memory(self): # real signature unknown; restored from __doc__
        """ release_cache_memory() """
        pass

    def rename_folder(self, old_folder_name, new_folder_name): # real signature unknown; restored from __doc__
        """ rename_folder(self, old_folder_name:str, new_folder_name:str) -> int """
        return 0

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_folder_version(self, folder_name, reset_version): # real signature unknown; restored from __doc__
        """ reset_folder_version(self, folder_name:str, reset_version:int) -> int """
        return 0

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def select(self, stmt, callback, user_data=None): # real signature unknown; restored from __doc__
        """ select(self, stmt:str, callback:Camel.DBSelectCB, user_data=None) -> int """
        return 0

    def set_collate(self, col, collate, func): # real signature unknown; restored from __doc__
        """ set_collate(self, col:str, collate:str, func:Camel.DBCollate) -> int """
        return 0

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def sqlize_string(self, string): # real signature unknown; restored from __doc__
        """ sqlize_string(string:str) -> str """
        return ""

    def start_in_memory_transactions(self): # real signature unknown; restored from __doc__
        """ start_in_memory_transactions(self) -> int """
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

    def transaction_command(self, qry_list): # real signature unknown; restored from __doc__
        """ transaction_command(self, qry_list:list) -> int """
        return 0

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write_folder_info_record(self, record): # real signature unknown; restored from __doc__
        """ write_folder_info_record(self, record:Camel.FIRecord) -> int """
        return 0

    def write_message_info_record(self, folder_name, record): # real signature unknown; restored from __doc__
        """ write_message_info_record(self, folder_name:str, record:Camel.MIRecord) -> int """
        return 0

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7b34f295b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DB), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelDB (94124523588480)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'camel_mir_free': gi.FunctionInfo(camel_mir_free), 'free_sqlized_string': gi.FunctionInfo(free_sqlized_string), 'get_column_ident': gi.FunctionInfo(get_column_ident), 'get_column_name': gi.FunctionInfo(get_column_name), 'release_cache_memory': gi.FunctionInfo(release_cache_memory), 'sqlize_string': gi.FunctionInfo(sqlize_string), 'abort_transaction': gi.FunctionInfo(abort_transaction), 'add_to_transaction': gi.FunctionInfo(add_to_transaction), 'begin_transaction': gi.FunctionInfo(begin_transaction), 'clear_folder_summary': gi.FunctionInfo(clear_folder_summary), 'command': gi.FunctionInfo(command), 'count_deleted_message_info': gi.FunctionInfo(count_deleted_message_info), 'count_junk_message_info': gi.FunctionInfo(count_junk_message_info), 'count_junk_not_deleted_message_info': gi.FunctionInfo(count_junk_not_deleted_message_info), 'count_message_info': gi.FunctionInfo(count_message_info), 'count_total_message_info': gi.FunctionInfo(count_total_message_info), 'count_unread_message_info': gi.FunctionInfo(count_unread_message_info), 'count_visible_message_info': gi.FunctionInfo(count_visible_message_info), 'count_visible_unread_message_info': gi.FunctionInfo(count_visible_unread_message_info), 'create_folders_table': gi.FunctionInfo(create_folders_table), 'delete_folder': gi.FunctionInfo(delete_folder), 'delete_uid': gi.FunctionInfo(delete_uid), 'delete_uids': gi.FunctionInfo(delete_uids), 'end_transaction': gi.FunctionInfo(end_transaction), 'flush_in_memory_transactions': gi.FunctionInfo(flush_in_memory_transactions), 'get_filename': gi.FunctionInfo(get_filename), 'get_folder_deleted_uids': gi.FunctionInfo(get_folder_deleted_uids), 'get_folder_junk_uids': gi.FunctionInfo(get_folder_junk_uids), 'get_folder_uids': gi.FunctionInfo(get_folder_uids), 'maybe_run_maintenance': gi.FunctionInfo(maybe_run_maintenance), 'prepare_message_info_table': gi.FunctionInfo(prepare_message_info_table), 'read_folder_info_record': gi.FunctionInfo(read_folder_info_record), 'read_message_info_record_with_uid': gi.FunctionInfo(read_message_info_record_with_uid), 'read_message_info_records': gi.FunctionInfo(read_message_info_records), 'rename_folder': gi.FunctionInfo(rename_folder), 'reset_folder_version': gi.FunctionInfo(reset_folder_version), 'select': gi.FunctionInfo(select), 'set_collate': gi.FunctionInfo(set_collate), 'start_in_memory_transactions': gi.FunctionInfo(start_in_memory_transactions), 'transaction_command': gi.FunctionInfo(transaction_command), 'write_folder_info_record': gi.FunctionInfo(write_folder_info_record), 'write_message_info_record': gi.FunctionInfo(write_message_info_record), 'parent': <property object at 0x7f7b34fafcc0>, 'priv': <property object at 0x7f7b34fafdb0>})"
    __gdoc__ = 'Object CamelDB\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelDB (94124523588480)>'
    __info__ = ObjectInfo(DB)


