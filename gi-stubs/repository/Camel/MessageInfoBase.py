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


from .MessageInfo import MessageInfo

class MessageInfoBase(MessageInfo):
    """
    :Constructors:
    
    ::
    
        MessageInfoBase(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clone(self, assign_summary=None): # real signature unknown; restored from __doc__
        """ clone(self, assign_summary:Camel.FolderSummary=None) -> Camel.MessageInfo """
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

    def do_clone(self, *args, **kwargs): # real signature unknown
        """ clone(self, assign_summary:Camel.FolderSummary=None) -> Camel.MessageInfo """
        pass

    def do_dup_user_flags(self, *args, **kwargs): # real signature unknown
        """ dup_user_flags(self) -> Camel.NamedFlags """
        pass

    def do_dup_user_tags(self, *args, **kwargs): # real signature unknown
        """ dup_user_tags(self) -> Camel.NameValueArray or None """
        pass

    def do_get_cc(self, *args, **kwargs): # real signature unknown
        """ get_cc(self) -> str """
        pass

    def do_get_date_received(self, *args, **kwargs): # real signature unknown
        """ get_date_received(self) -> int """
        pass

    def do_get_date_sent(self, *args, **kwargs): # real signature unknown
        """ get_date_sent(self) -> int """
        pass

    def do_get_flags(self, *args, **kwargs): # real signature unknown
        """ get_flags(self) -> int """
        pass

    def do_get_from(self, *args, **kwargs): # real signature unknown
        """ get_from(self) -> str """
        pass

    def do_get_headers(self, *args, **kwargs): # real signature unknown
        """ get_headers(self) -> Camel.NameValueArray or None """
        pass

    def do_get_message_id(self, *args, **kwargs): # real signature unknown
        """ get_message_id(self) -> int """
        pass

    def do_get_mlist(self, *args, **kwargs): # real signature unknown
        """ get_mlist(self) -> str """
        pass

    def do_get_references(self, *args, **kwargs): # real signature unknown
        """ get_references(self) -> list or None """
        pass

    def do_get_size(self, *args, **kwargs): # real signature unknown
        """ get_size(self) -> int """
        pass

    def do_get_subject(self, *args, **kwargs): # real signature unknown
        """ get_subject(self) -> str """
        pass

    def do_get_to(self, *args, **kwargs): # real signature unknown
        """ get_to(self) -> str """
        pass

    def do_get_user_flag(self, *args, **kwargs): # real signature unknown
        """ get_user_flag(self, name:str) -> bool """
        pass

    def do_get_user_flags(self, *args, **kwargs): # real signature unknown
        """ get_user_flags(self) -> Camel.NamedFlags or None """
        pass

    def do_get_user_tag(self, *args, **kwargs): # real signature unknown
        """ get_user_tag(self, name:str) -> str or None """
        pass

    def do_get_user_tags(self, *args, **kwargs): # real signature unknown
        """ get_user_tags(self) -> Camel.NameValueArray or None """
        pass

    def do_load(self, *args, **kwargs): # real signature unknown
        """ load(self, record:Camel.MIRecord=None, bdata_ptr:str) -> bool """
        pass

    def do_save(self, *args, **kwargs): # real signature unknown
        """ save(self, record:Camel.MIRecord=None, bdata_str:GLib.String) -> bool """
        pass

    def do_set_cc(self, *args, **kwargs): # real signature unknown
        """ set_cc(self, cc:str=None) -> bool """
        pass

    def do_set_date_received(self, *args, **kwargs): # real signature unknown
        """ set_date_received(self, date_received:int) -> bool """
        pass

    def do_set_date_sent(self, *args, **kwargs): # real signature unknown
        """ set_date_sent(self, date_sent:int) -> bool """
        pass

    def do_set_flags(self, *args, **kwargs): # real signature unknown
        """ set_flags(self, mask:int, set:int) -> bool """
        pass

    def do_set_from(self, *args, **kwargs): # real signature unknown
        """ set_from(self, from_:str=None) -> bool """
        pass

    def do_set_message_id(self, *args, **kwargs): # real signature unknown
        """ set_message_id(self, message_id:int) -> bool """
        pass

    def do_set_mlist(self, *args, **kwargs): # real signature unknown
        """ set_mlist(self, mlist:str=None) -> bool """
        pass

    def do_set_size(self, *args, **kwargs): # real signature unknown
        """ set_size(self, size:int) -> bool """
        pass

    def do_set_subject(self, *args, **kwargs): # real signature unknown
        """ set_subject(self, subject:str=None) -> bool """
        pass

    def do_set_to(self, *args, **kwargs): # real signature unknown
        """ set_to(self, to:str=None) -> bool """
        pass

    def do_set_user_flag(self, *args, **kwargs): # real signature unknown
        """ set_user_flag(self, name:str, state:bool) -> bool """
        pass

    def do_set_user_tag(self, *args, **kwargs): # real signature unknown
        """ set_user_tag(self, name:str, value:str=None) -> bool """
        pass

    def do_take_headers(self, *args, **kwargs): # real signature unknown
        """ take_headers(self, headers:Camel.NameValueArray=None) -> bool """
        pass

    def do_take_references(self, *args, **kwargs): # real signature unknown
        """ take_references(self, references:list=None) -> bool """
        pass

    def do_take_user_flags(self, *args, **kwargs): # real signature unknown
        """ take_user_flags(self, user_flags:Camel.NamedFlags=None) -> bool """
        pass

    def do_take_user_tags(self, *args, **kwargs): # real signature unknown
        """ take_user_tags(self, user_tags:Camel.NameValueArray=None) -> bool """
        pass

    def dump(self): # real signature unknown; restored from __doc__
        """ dump(self) """
        pass

    def dup_headers(self): # real signature unknown; restored from __doc__
        """ dup_headers(self) -> Camel.NameValueArray or None """
        pass

    def dup_references(self): # real signature unknown; restored from __doc__
        """ dup_references(self) -> list or None """
        return []

    def dup_user_flags(self): # real signature unknown; restored from __doc__
        """ dup_user_flags(self) -> Camel.NamedFlags """
        pass

    def dup_user_tag(self, name): # real signature unknown; restored from __doc__
        """ dup_user_tag(self, name:str) -> str or None """
        return ""

    def dup_user_tags(self): # real signature unknown; restored from __doc__
        """ dup_user_tags(self) -> Camel.NameValueArray or None """
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

    def freeze_notifications(self): # real signature unknown; restored from __doc__
        """ freeze_notifications(self) """
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

    def get_abort_notifications(self): # real signature unknown; restored from __doc__
        """ get_abort_notifications(self) -> bool """
        return False

    def get_cc(self): # real signature unknown; restored from __doc__
        """ get_cc(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date_received(self): # real signature unknown; restored from __doc__
        """ get_date_received(self) -> int """
        return 0

    def get_date_sent(self): # real signature unknown; restored from __doc__
        """ get_date_sent(self) -> int """
        return 0

    def get_dirty(self): # real signature unknown; restored from __doc__
        """ get_dirty(self) -> bool """
        return False

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_folder_flagged(self): # real signature unknown; restored from __doc__
        """ get_folder_flagged(self) -> bool """
        return False

    def get_folder_flagged_stamp(self): # real signature unknown; restored from __doc__
        """ get_folder_flagged_stamp(self) -> int """
        return 0

    def get_from(self): # real signature unknown; restored from __doc__
        """ get_from(self) -> str """
        return ""

    def get_headers(self): # real signature unknown; restored from __doc__
        """ get_headers(self) -> Camel.NameValueArray or None """
        pass

    def get_message_id(self): # real signature unknown; restored from __doc__
        """ get_message_id(self) -> int """
        return 0

    def get_mlist(self): # real signature unknown; restored from __doc__
        """ get_mlist(self) -> str """
        return ""

    def get_notifications_frozen(self): # real signature unknown; restored from __doc__
        """ get_notifications_frozen(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_references(self): # real signature unknown; restored from __doc__
        """ get_references(self) -> list or None """
        return []

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_subject(self): # real signature unknown; restored from __doc__
        """ get_subject(self) -> str """
        return ""

    def get_to(self): # real signature unknown; restored from __doc__
        """ get_to(self) -> str """
        return ""

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def get_user_flag(self, name): # real signature unknown; restored from __doc__
        """ get_user_flag(self, name:str) -> bool """
        return False

    def get_user_flags(self): # real signature unknown; restored from __doc__
        """ get_user_flags(self) -> Camel.NamedFlags or None """
        pass

    def get_user_tag(self, name): # real signature unknown; restored from __doc__
        """ get_user_tag(self, name:str) -> str or None """
        return ""

    def get_user_tags(self): # real signature unknown; restored from __doc__
        """ get_user_tags(self) -> Camel.NameValueArray or None """
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

    def load(self, record, bdata_ptr): # real signature unknown; restored from __doc__
        """ load(self, record:Camel.MIRecord, bdata_ptr:str) -> bool """
        return False

    def new(self, summary=None): # real signature unknown; restored from __doc__
        """ new(summary:Camel.FolderSummary=None) -> Camel.MessageInfo """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_headers(self, summary, headers): # real signature unknown; restored from __doc__
        """ new_from_headers(summary:Camel.FolderSummary, headers:Camel.NameValueArray) -> Camel.MessageInfo """
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

    def pooldup_uid(self): # real signature unknown; restored from __doc__
        """ pooldup_uid(self) -> str """
        return ""

    def property_lock(self): # real signature unknown; restored from __doc__
        """ property_lock(self) """
        pass

    def property_unlock(self): # real signature unknown; restored from __doc__
        """ property_unlock(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_summary(self): # real signature unknown; restored from __doc__
        """ ref_summary(self) """
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

    def save(self, record, bdata_str): # real signature unknown; restored from __doc__
        """ save(self, record:Camel.MIRecord, bdata_str:GLib.String) -> bool """
        return False

    def set_abort_notifications(self, abort_notifications): # real signature unknown; restored from __doc__
        """ set_abort_notifications(self, abort_notifications:bool) """
        pass

    def set_cc(self, cc=None): # real signature unknown; restored from __doc__
        """ set_cc(self, cc:str=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date_received(self, date_received): # real signature unknown; restored from __doc__
        """ set_date_received(self, date_received:int) -> bool """
        return False

    def set_date_sent(self, date_sent): # real signature unknown; restored from __doc__
        """ set_date_sent(self, date_sent:int) -> bool """
        return False

    def set_dirty(self, dirty): # real signature unknown; restored from __doc__
        """ set_dirty(self, dirty:bool) """
        pass

    def set_flags(self, mask, set): # real signature unknown; restored from __doc__
        """ set_flags(self, mask:int, set:int) -> bool """
        return False

    def set_folder_flagged(self, folder_flagged): # real signature unknown; restored from __doc__
        """ set_folder_flagged(self, folder_flagged:bool) -> bool """
        return False

    def set_from(self, from_=None): # real signature unknown; restored from __doc__
        """ set_from(self, from_:str=None) -> bool """
        return False

    def set_message_id(self, message_id): # real signature unknown; restored from __doc__
        """ set_message_id(self, message_id:int) -> bool """
        return False

    def set_mlist(self, mlist=None): # real signature unknown; restored from __doc__
        """ set_mlist(self, mlist:str=None) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) -> bool """
        return False

    def set_subject(self, subject=None): # real signature unknown; restored from __doc__
        """ set_subject(self, subject:str=None) -> bool """
        return False

    def set_to(self, to=None): # real signature unknown; restored from __doc__
        """ set_to(self, to:str=None) -> bool """
        return False

    def set_uid(self, uid): # real signature unknown; restored from __doc__
        """ set_uid(self, uid:str) -> bool """
        return False

    def set_user_flag(self, name, state): # real signature unknown; restored from __doc__
        """ set_user_flag(self, name:str, state:bool) -> bool """
        return False

    def set_user_tag(self, name, value=None): # real signature unknown; restored from __doc__
        """ set_user_tag(self, name:str, value:str=None) -> bool """
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

    def take_headers(self, headers=None): # real signature unknown; restored from __doc__
        """ take_headers(self, headers:Camel.NameValueArray=None) -> bool """
        return False

    def take_references(self, references=None): # real signature unknown; restored from __doc__
        """ take_references(self, references:list=None) -> bool """
        return False

    def take_user_flags(self, user_flags=None): # real signature unknown; restored from __doc__
        """ take_user_flags(self, user_flags:Camel.NamedFlags=None) -> bool """
        return False

    def take_user_tags(self, user_tags=None): # real signature unknown; restored from __doc__
        """ take_user_tags(self, user_tags:Camel.NameValueArray=None) -> bool """
        return False

    def thaw_notifications(self): # real signature unknown; restored from __doc__
        """ thaw_notifications(self) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7b34c2d400>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MessageInfoBase), '__module__': 'gi.repository.Camel', '__gtype__': <GType CamelMessageInfoBase (94124523857968)>, '__doc__': None, '__gsignals__': {}, 'parent': <property object at 0x7f7b34f794f0>, 'priv': <property object at 0x7f7b34f79630>})"
    __gdoc__ = 'Object CamelMessageInfoBase\n\nProperties from CamelMessageInfo:\n  summary -> CamelFolderSummary: Summary\n  dirty -> gboolean: Dirty\n  folder-flagged -> gboolean: Folder Flagged\n  folder-flagged-stamp -> guint: Folder Flagged Stamp\n  abort-notifications -> gboolean: Abort Notifications\n  uid -> gchararray: UID\n  flags -> guint: Flags\n  user-flags -> CamelNamedFlags: User Flags\n  user-tags -> CamelNameValueArray: User tags\n  subject -> gchararray: Subject\n  from -> gchararray: From\n  to -> gchararray: To\n  cc -> gchararray: CC\n  mlist -> gchararray: mlist\n  size -> guint: Size\n  date-sent -> gint64: Date Sent\n  date-received -> gint64: Date Received\n  message-id -> guint64: Message ID\n  references -> GArray: References\n  headers -> CamelNameValueArray: Headers\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CamelMessageInfoBase (94124523857968)>'
    __info__ = ObjectInfo(MessageInfoBase)


