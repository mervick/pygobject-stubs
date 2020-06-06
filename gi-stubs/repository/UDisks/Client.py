# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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


class Client(__gi_overrides_GObject.Object, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        Client(**properties)
        new_finish(res:Gio.AsyncResult) -> UDisks.Client
        new_sync(cancellable:Gio.Cancellable=None) -> UDisks.Client
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

    def get_all_blocks_for_mdraid(self, raid): # real signature unknown; restored from __doc__
        """ get_all_blocks_for_mdraid(self, raid:UDisks.MDRaid) -> list """
        return []

    def get_block_for_dev(self, block_device_number): # real signature unknown; restored from __doc__
        """ get_block_for_dev(self, block_device_number:int) -> UDisks.Block """
        pass

    def get_block_for_drive(self, drive, get_physical): # real signature unknown; restored from __doc__
        """ get_block_for_drive(self, drive:UDisks.Drive, get_physical:bool) -> UDisks.Block """
        pass

    def get_block_for_label(self, label): # real signature unknown; restored from __doc__
        """ get_block_for_label(self, label:str) -> list """
        return []

    def get_block_for_mdraid(self, raid): # real signature unknown; restored from __doc__
        """ get_block_for_mdraid(self, raid:UDisks.MDRaid) -> UDisks.Block """
        pass

    def get_block_for_uuid(self, uuid): # real signature unknown; restored from __doc__
        """ get_block_for_uuid(self, uuid:str) -> list """
        return []

    def get_cleartext_block(self, block): # real signature unknown; restored from __doc__
        """ get_cleartext_block(self, block:UDisks.Block) -> UDisks.Block """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_drive_for_block(self, block): # real signature unknown; restored from __doc__
        """ get_drive_for_block(self, block:UDisks.Block) -> UDisks.Drive """
        pass

    def get_drive_info(self, drive): # real signature unknown; restored from __doc__
        """ get_drive_info(self, drive:UDisks.Drive) -> out_name:str, out_description:str, out_drive_icon:Gio.Icon, out_media_description:str, out_media_icon:Gio.Icon """
        pass

    def get_drive_siblings(self, drive): # real signature unknown; restored from __doc__
        """ get_drive_siblings(self, drive:UDisks.Drive) -> list """
        return []

    def get_id_for_display(self, usage, type, version, long_string): # real signature unknown; restored from __doc__
        """ get_id_for_display(self, usage:str, type:str, version:str, long_string:bool) -> str """
        return ""

    def get_jobs_for_object(self, p_object): # real signature unknown; restored from __doc__
        """ get_jobs_for_object(self, object:UDisks.Object) -> list """
        return []

    def get_job_description(self, job): # real signature unknown; restored from __doc__
        """ get_job_description(self, job:UDisks.Job) -> str """
        return ""

    def get_job_description_from_operation(self, operation): # real signature unknown; restored from __doc__
        """ get_job_description_from_operation(operation:str) -> str """
        return ""

    def get_loop_for_block(self, block): # real signature unknown; restored from __doc__
        """ get_loop_for_block(self, block:UDisks.Block) -> UDisks.Loop """
        pass

    def get_manager(self): # real signature unknown; restored from __doc__
        """ get_manager(self) -> UDisks.Manager """
        pass

    def get_mdraid_for_block(self, block): # real signature unknown; restored from __doc__
        """ get_mdraid_for_block(self, block:UDisks.Block) -> UDisks.MDRaid """
        pass

    def get_media_compat_for_display(self, media_compat): # real signature unknown; restored from __doc__
        """ get_media_compat_for_display(self, media_compat:str) -> str """
        return ""

    def get_members_for_mdraid(self, raid): # real signature unknown; restored from __doc__
        """ get_members_for_mdraid(self, raid:UDisks.MDRaid) -> list """
        return []

    def get_object(self, object_path): # real signature unknown; restored from __doc__
        """ get_object(self, object_path:str) -> UDisks.Object """
        pass

    def get_object_info(self, p_object): # real signature unknown; restored from __doc__
        """ get_object_info(self, object:UDisks.Object) -> UDisks.ObjectInfo """
        pass

    def get_object_manager(self): # real signature unknown; restored from __doc__
        """ get_object_manager(self) -> Gio.DBusObjectManager """
        pass

    def get_partitions(self, table): # real signature unknown; restored from __doc__
        """ get_partitions(self, table:UDisks.PartitionTable) -> list """
        return []

    def get_partition_info(self, partition): # real signature unknown; restored from __doc__
        """ get_partition_info(self, partition:UDisks.Partition) -> str """
        return ""

    def get_partition_table(self, partition): # real signature unknown; restored from __doc__
        """ get_partition_table(self, partition:UDisks.Partition) -> UDisks.PartitionTable """
        pass

    def get_partition_table_subtypes(self, partition_table_type): # real signature unknown; restored from __doc__
        """ get_partition_table_subtypes(self, partition_table_type:str) -> list """
        return []

    def get_partition_table_subtype_for_display(self, partition_table_type, partition_table_subtype): # real signature unknown; restored from __doc__
        """ get_partition_table_subtype_for_display(self, partition_table_type:str, partition_table_subtype:str) -> str """
        return ""

    def get_partition_table_type_for_display(self, partition_table_type): # real signature unknown; restored from __doc__
        """ get_partition_table_type_for_display(self, partition_table_type:str) -> str """
        return ""

    def get_partition_type_and_subtype_for_display(self, partition_table_type, partition_table_subtype, partition_type): # real signature unknown; restored from __doc__
        """ get_partition_type_and_subtype_for_display(self, partition_table_type:str, partition_table_subtype:str, partition_type:str) -> str """
        return ""

    def get_partition_type_for_display(self, partition_table_type, partition_type): # real signature unknown; restored from __doc__
        """ get_partition_type_for_display(self, partition_table_type:str, partition_type:str) -> str """
        return ""

    def get_partition_type_infos(self, partition_table_type, partition_table_subtype=None): # real signature unknown; restored from __doc__
        """ get_partition_type_infos(self, partition_table_type:str, partition_table_subtype:str=None) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_size_for_display(self, size, use_pow2, long_string): # real signature unknown; restored from __doc__
        """ get_size_for_display(self, size:int, use_pow2:bool, long_string:bool) -> str """
        return ""

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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new(cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, res): # real signature unknown; restored from __doc__
        """ new_finish(res:Gio.AsyncResult) -> UDisks.Client """
        pass

    def new_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ new_sync(cancellable:Gio.Cancellable=None) -> UDisks.Client """
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

    def peek_object(self, object_path): # real signature unknown; restored from __doc__
        """ peek_object(self, object_path:str) -> UDisks.Object """
        pass

    def queue_changed(self): # real signature unknown; restored from __doc__
        """ queue_changed(self) """
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

    def settle(self): # real signature unknown; restored from __doc__
        """ settle(self) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f13a81539d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Client), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksClient (93969722163792)>, '__doc__': None, '__gsignals__': {}, 'new_finish': gi.FunctionInfo(new_finish), 'new_sync': gi.FunctionInfo(new_sync), 'get_job_description_from_operation': gi.FunctionInfo(get_job_description_from_operation), 'new': gi.FunctionInfo(new), 'get_all_blocks_for_mdraid': gi.FunctionInfo(get_all_blocks_for_mdraid), 'get_block_for_dev': gi.FunctionInfo(get_block_for_dev), 'get_block_for_drive': gi.FunctionInfo(get_block_for_drive), 'get_block_for_label': gi.FunctionInfo(get_block_for_label), 'get_block_for_mdraid': gi.FunctionInfo(get_block_for_mdraid), 'get_block_for_uuid': gi.FunctionInfo(get_block_for_uuid), 'get_cleartext_block': gi.FunctionInfo(get_cleartext_block), 'get_drive_for_block': gi.FunctionInfo(get_drive_for_block), 'get_drive_info': gi.FunctionInfo(get_drive_info), 'get_drive_siblings': gi.FunctionInfo(get_drive_siblings), 'get_id_for_display': gi.FunctionInfo(get_id_for_display), 'get_job_description': gi.FunctionInfo(get_job_description), 'get_jobs_for_object': gi.FunctionInfo(get_jobs_for_object), 'get_loop_for_block': gi.FunctionInfo(get_loop_for_block), 'get_manager': gi.FunctionInfo(get_manager), 'get_mdraid_for_block': gi.FunctionInfo(get_mdraid_for_block), 'get_media_compat_for_display': gi.FunctionInfo(get_media_compat_for_display), 'get_members_for_mdraid': gi.FunctionInfo(get_members_for_mdraid), 'get_object': gi.FunctionInfo(get_object), 'get_object_info': gi.FunctionInfo(get_object_info), 'get_object_manager': gi.FunctionInfo(get_object_manager), 'get_partition_info': gi.FunctionInfo(get_partition_info), 'get_partition_table': gi.FunctionInfo(get_partition_table), 'get_partition_table_subtype_for_display': gi.FunctionInfo(get_partition_table_subtype_for_display), 'get_partition_table_subtypes': gi.FunctionInfo(get_partition_table_subtypes), 'get_partition_table_type_for_display': gi.FunctionInfo(get_partition_table_type_for_display), 'get_partition_type_and_subtype_for_display': gi.FunctionInfo(get_partition_type_and_subtype_for_display), 'get_partition_type_for_display': gi.FunctionInfo(get_partition_type_for_display), 'get_partition_type_infos': gi.FunctionInfo(get_partition_type_infos), 'get_partitions': gi.FunctionInfo(get_partitions), 'get_size_for_display': gi.FunctionInfo(get_size_for_display), 'peek_object': gi.FunctionInfo(peek_object), 'queue_changed': gi.FunctionInfo(queue_changed), 'settle': gi.FunctionInfo(settle)})"
    __gdoc__ = 'Object UDisksClient\n\nSignals from UDisksClient:\n  changed ()\n\nProperties from UDisksClient:\n  object-manager -> GDBusObjectManager: Object Manager\n    The GDBusObjectManager used by the UDisksClient\n  manager -> UDisksManager: Manager\n    The UDisksManager\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksClient (93969722163792)>'
    __info__ = ObjectInfo(Client)


