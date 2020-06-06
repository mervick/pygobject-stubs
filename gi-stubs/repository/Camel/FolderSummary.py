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


class FolderSummary(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        FolderSummary(**properties)
        new(folder:Camel.Folder) -> Camel.FolderSummary
    """
    def add(self, info, force_keep_uid): # real signature unknown; restored from __doc__
        """ add(self, info:Camel.MessageInfo, force_keep_uid:bool) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_uid(self, uid): # real signature unknown; restored from __doc__
        """ check_uid(self, uid:str) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> bool """
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

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_message_info_from_uid(self, *args, **kwargs): # real signature unknown
        """ message_info_from_uid(self, uid:str) -> Camel.MessageInfo or None """
        pass

    def do_message_info_new_from_headers(self, *args, **kwargs): # real signature unknown
        """ message_info_new_from_headers(self, headers:Camel.NameValueArray) -> Camel.MessageInfo """
        pass

    def do_message_info_new_from_message(self, *args, **kwargs): # real signature unknown
        """ message_info_new_from_message(self, message:Camel.MimeMessage) -> Camel.MessageInfo """
        pass

    def do_message_info_new_from_parser(self, *args, **kwargs): # real signature unknown
        """ message_info_new_from_parser(self, parser:Camel.MimeParser) -> Camel.MessageInfo """
        pass

    def do_next_uid_string(self, *args, **kwargs): # real signature unknown
        """ next_uid_string(self) -> str """
        pass

    def do_prepare_fetch_all(self, *args, **kwargs): # real signature unknown
        """ prepare_fetch_all(self) """
        pass

    def do_summary_header_load(self, *args, **kwargs): # real signature unknown
        """ summary_header_load(self, fir=None) -> bool """
        pass

    def do_summary_header_save(self, *args, **kwargs): # real signature unknown
        """ summary_header_save(self) """
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

    def free_array(self, array): # real signature unknown; restored from __doc__
        """ free_array(array:list) """
        pass

    def get(self, uid): # real signature unknown; restored from __doc__
        """ get(self, uid:str) -> Camel.MessageInfo or None """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_array(self): # real signature unknown; restored from __doc__
        """ get_array(self) -> list """
        return []

    def get_changed(self): # real signature unknown; restored from __doc__
        """ get_changed(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_deleted_count(self): # real signature unknown; restored from __doc__
        """ get_deleted_count(self) -> int """
        return 0

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_folder(self): # real signature unknown; restored from __doc__
        """ get_folder(self) """
        pass

    def get_hash(self): # real signature unknown; restored from __doc__
        """ get_hash(self) -> dict """
        return {}

    def get_index(self): # real signature unknown; restored from __doc__
        """ get_index(self) -> Camel.Index """
        pass

    def get_info_flags(self, uid): # real signature unknown; restored from __doc__
        """ get_info_flags(self, uid:str) -> int """
        return 0

    def get_junk_count(self): # real signature unknown; restored from __doc__
        """ get_junk_count(self) -> int """
        return 0

    def get_junk_not_deleted_count(self): # real signature unknown; restored from __doc__
        """ get_junk_not_deleted_count(self) -> int """
        return 0

    def get_next_uid(self): # real signature unknown; restored from __doc__
        """ get_next_uid(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_saved_count(self): # real signature unknown; restored from __doc__
        """ get_saved_count(self) -> int """
        return 0

    def get_timestamp(self): # real signature unknown; restored from __doc__
        """ get_timestamp(self) -> int """
        return 0

    def get_unread_count(self): # real signature unknown; restored from __doc__
        """ get_unread_count(self) -> int """
        return 0

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> int """
        return 0

    def get_visible_count(self): # real signature unknown; restored from __doc__
        """ get_visible_count(self) -> int """
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

    def header_load(self, store=None, folder_name): # real signature unknown; restored from __doc__
        """ header_load(self, store=None, folder_name:str) -> bool """
        return False

    def header_save(self): # real signature unknown; restored from __doc__
        """ header_save(self) -> bool """
        return False

    def info_new_from_headers(self, headers): # real signature unknown; restored from __doc__
        """ info_new_from_headers(self, headers:Camel.NameValueArray) -> Camel.MessageInfo """
        pass

    def info_new_from_message(self, message): # real signature unknown; restored from __doc__
        """ info_new_from_message(self, message:Camel.MimeMessage) -> Camel.MessageInfo """
        pass

    def info_new_from_parser(self, parser): # real signature unknown; restored from __doc__
        """ info_new_from_parser(self, parser:Camel.MimeParser) -> Camel.MessageInfo """
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

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> bool """
        return False

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) """
        pass

    def new(self, folder): # real signature unknown; restored from __doc__
        """ new(folder:Camel.Folder) -> Camel.FolderSummary """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def next_uid(self): # real signature unknown; restored from __doc__
        """ next_uid(self) -> int """
        return 0

    def next_uid_string(self): # real signature unknown; restored from __doc__
        """ next_uid_string(self) -> str """
        return ""

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_loaded(self, uid): # real signature unknown; restored from __doc__
        """ peek_loaded(self, uid:str) -> Camel.MessageInfo or None """
        pass

    def prepare_fetch_all(self): # real signature unknown; restored from __doc__
        """ prepare_fetch_all(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self, info): # real signature unknown; restored from __doc__
        """ remove(self, info:Camel.MessageInfo) -> bool """
        return False

    def remove_uid(self, uid): # real signature unknown; restored from __doc__
        """ remove_uid(self, uid:str) -> bool """
        return False

    def remove_uids(self, uids): # real signature unknown; restored from __doc__
        """ remove_uids(self, uids:list) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_flags(self, info): # real signature unknown; restored from __doc__
        """ replace_flags(self, info:Camel.MessageInfo) -> bool """
        return False

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def save(self): # real signature unknown; restored from __doc__
        """ save(self) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:int) """
        pass

    def set_index(self, index): # real signature unknown; restored from __doc__
        """ set_index(self, index:Camel.Index) """
        pass

    def set_next_uid(self, uid): # real signature unknown; restored from __doc__
        """ set_next_uid(self, uid:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_timestamp(self, timestamp): # real signature unknown; restored from __doc__
        """ set_timestamp(self, timestamp:int) """
        pass

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:int) """
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

    def touch(self): # real signature unknown; restored from __doc__
        """ touch(self) """
        pass

    def unlock(self): # real signature unknown; restored from __doc__
        """ unlock(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7b34e2bd90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(FolderSummary), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelFolderSummary (94124523697216)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'free_array': gi.FunctionInfo(free_array), 'add': gi.FunctionInfo(add), 'check_uid': gi.FunctionInfo(check_uid), 'clear': gi.FunctionInfo(clear), 'count': gi.FunctionInfo(count), 'get': gi.FunctionInfo(get), 'get_array': gi.FunctionInfo(get_array), 'get_changed': gi.FunctionInfo(get_changed), 'get_deleted_count': gi.FunctionInfo(get_deleted_count), 'get_flags': gi.FunctionInfo(get_flags), 'get_folder': gi.FunctionInfo(get_folder), 'get_hash': gi.FunctionInfo(get_hash), 'get_index': gi.FunctionInfo(get_index), 'get_info_flags': gi.FunctionInfo(get_info_flags), 'get_junk_count': gi.FunctionInfo(get_junk_count), 'get_junk_not_deleted_count': gi.FunctionInfo(get_junk_not_deleted_count), 'get_next_uid': gi.FunctionInfo(get_next_uid), 'get_saved_count': gi.FunctionInfo(get_saved_count), 'get_timestamp': gi.FunctionInfo(get_timestamp), 'get_unread_count': gi.FunctionInfo(get_unread_count), 'get_version': gi.FunctionInfo(get_version), 'get_visible_count': gi.FunctionInfo(get_visible_count), 'header_load': gi.FunctionInfo(header_load), 'header_save': gi.FunctionInfo(header_save), 'info_new_from_headers': gi.FunctionInfo(info_new_from_headers), 'info_new_from_message': gi.FunctionInfo(info_new_from_message), 'info_new_from_parser': gi.FunctionInfo(info_new_from_parser), 'load': gi.FunctionInfo(load), 'lock': gi.FunctionInfo(lock), 'next_uid': gi.FunctionInfo(next_uid), 'next_uid_string': gi.FunctionInfo(next_uid_string), 'peek_loaded': gi.FunctionInfo(peek_loaded), 'prepare_fetch_all': gi.FunctionInfo(prepare_fetch_all), 'remove': gi.FunctionInfo(remove), 'remove_uid': gi.FunctionInfo(remove_uid), 'remove_uids': gi.FunctionInfo(remove_uids), 'replace_flags': gi.FunctionInfo(replace_flags), 'save': gi.FunctionInfo(save), 'set_flags': gi.FunctionInfo(set_flags), 'set_index': gi.FunctionInfo(set_index), 'set_next_uid': gi.FunctionInfo(set_next_uid), 'set_timestamp': gi.FunctionInfo(set_timestamp), 'set_version': gi.FunctionInfo(set_version), 'touch': gi.FunctionInfo(touch), 'unlock': gi.FunctionInfo(unlock), 'do_message_info_from_uid': gi.VFuncInfo(message_info_from_uid), 'do_message_info_new_from_headers': gi.VFuncInfo(message_info_new_from_headers), 'do_message_info_new_from_message': gi.VFuncInfo(message_info_new_from_message), 'do_message_info_new_from_parser': gi.VFuncInfo(message_info_new_from_parser), 'do_next_uid_string': gi.VFuncInfo(next_uid_string), 'do_prepare_fetch_all': gi.VFuncInfo(prepare_fetch_all), 'do_summary_header_load': gi.VFuncInfo(summary_header_load), 'do_summary_header_save': gi.VFuncInfo(summary_header_save), 'parent': <property object at 0x7f7b34fd69f0>, 'priv': <property object at 0x7f7b34fd6bd0>})"
    __gdoc__ = 'Object CamelFolderSummary\n\nSignals from CamelFolderSummary:\n  changed ()\n\nProperties from CamelFolderSummary:\n  folder -> CamelFolder: Folder\n    The folder to which the folder summary belongs\n  saved-count -> guint: Saved count\n    How many infos is savef in a summary\n  unread-count -> guint: Unread count\n    How many unread infos is saved in a summary\n  deleted-count -> guint: Deleted count\n    How many deleted infos is saved in a summary\n  junk-count -> guint: Junk count\n    How many junk infos is saved in a summary\n  junk-not-deleted-count -> guint: Junk not deleted count\n    How many junk and not deleted infos is saved in a summary\n  visible-count -> guint: Visible count\n    How many visible (not deleted and not junk) infos is saved in a summary\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelFolderSummary (94124523697216)>'
    __info__ = ObjectInfo(FolderSummary)


