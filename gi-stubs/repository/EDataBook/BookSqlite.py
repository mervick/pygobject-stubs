# encoding: utf-8
# module gi.repository.EDataBook
# from /usr/lib64/girepository-1.0/EDataBook-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class BookSqlite(__gi_overrides_GObject.Object, __gi_repository_EDataServer.Extensible):
    """
    :Constructors:
    
    ::
    
        BookSqlite(**properties)
        new(path:str, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> EDataBook.BookSqlite
        new_full(path:str, source:EDataServer.Source, setup:EBookContacts.SourceBackendSummarySetup=None, vcard_callback:EDataBook.bSqlVCardCallback=None, change_callback:EDataBook.bSqlChangeCallback=None, user_data=None, cancellable:Gio.Cancellable=None) -> EDataBook.BookSqlite
    """
    def add_contact(self, contact, extra, replace, cancellable=None): # real signature unknown; restored from __doc__
        """ add_contact(self, contact:EBookContacts.Contact, extra:str, replace:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def add_contacts(self, contacts, extra=None, replace, cancellable=None): # real signature unknown; restored from __doc__
        """ add_contacts(self, contacts:list, extra:list=None, replace:bool, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def do_before_insert_contact(self, *args, **kwargs): # real signature unknown
        """ before_insert_contact(self, db=None, contact:EBookContacts.Contact, extra:str, replace:bool, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_before_remove_contact(self, *args, **kwargs): # real signature unknown
        """ before_remove_contact(self, db=None, contact_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
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

    def get_contact(self, uid, meta_contact): # real signature unknown; restored from __doc__
        """ get_contact(self, uid:str, meta_contact:bool) -> bool, ret_contact:EBookContacts.Contact """
        return False

    def get_contact_extra(self, uid): # real signature unknown; restored from __doc__
        """ get_contact_extra(self, uid:str) -> bool, ret_extra:str """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_key_value(self, key): # real signature unknown; restored from __doc__
        """ get_key_value(self, key:str) -> bool, value:str """
        return False

    def get_key_value_int(self, key): # real signature unknown; restored from __doc__
        """ get_key_value_int(self, key:str) -> bool, value:int """
        return False

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> bool, locale_out:str """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_vcard(self, uid, meta_contact): # real signature unknown; restored from __doc__
        """ get_vcard(self, uid:str, meta_contact:bool) -> bool, ret_vcard:str """
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

    def has_contact(self, uid): # real signature unknown; restored from __doc__
        """ has_contact(self, uid:str) -> bool, exists:bool """
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

    def list_extensions(self, extension_type): # real signature unknown; restored from __doc__
        """ list_extensions(self, extension_type:GType) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load_extensions(self): # real signature unknown; restored from __doc__
        """ load_extensions(self) """
        pass

    def lock(self, lock_type, cancellable=None): # real signature unknown; restored from __doc__
        """ lock(self, lock_type:EDataBook.bSqlLockType, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def new(self, path, source, cancellable=None): # real signature unknown; restored from __doc__
        """ new(path:str, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> EDataBook.BookSqlite """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_full(self, path, source, setup=None, vcard_callback=None, change_callback=None, user_data=None, cancellable=None): # real signature unknown; restored from __doc__
        """ new_full(path:str, source:EDataServer.Source, setup:EBookContacts.SourceBackendSummarySetup=None, vcard_callback:EDataBook.bSqlVCardCallback=None, change_callback:EDataBook.bSqlChangeCallback=None, user_data=None, cancellable:Gio.Cancellable=None) -> EDataBook.BookSqlite """
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

    def ref_collator(self): # real signature unknown; restored from __doc__
        """ ref_collator(self) -> EDataServer.Collator """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_source(self): # real signature unknown; restored from __doc__
        """ ref_source(self) -> EDataServer.Source """
        pass

    def remove_contact(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contact(self, uid:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_contacts(self, uids, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contacts(self, uids:list, cancellable:Gio.Cancellable=None) -> bool """
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

    def search(self, sexp=None, meta_contacts, cancellable=None): # real signature unknown; restored from __doc__
        """ search(self, sexp:str=None, meta_contacts:bool, cancellable:Gio.Cancellable=None) -> bool, ret_list:list """
        return False

    def search_data_free(self, data): # real signature unknown; restored from __doc__
        """ search_data_free(data:EDataBook.bSqlSearchData) """
        pass

    def search_uids(self, sexp=None, cancellable=None): # real signature unknown; restored from __doc__
        """ search_uids(self, sexp:str=None, cancellable:Gio.Cancellable=None) -> bool, ret_list:list """
        return False

    def set_contact_extra(self, uid, extra=None): # real signature unknown; restored from __doc__
        """ set_contact_extra(self, uid:str, extra:str=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_key_value(self, key, value): # real signature unknown; restored from __doc__
        """ set_key_value(self, key:str, value:str) -> bool """
        return False

    def set_key_value_int(self, key, value): # real signature unknown; restored from __doc__
        """ set_key_value_int(self, key:str, value:int) -> bool """
        return False

    def set_locale(self, lc_collate, cancellable=None): # real signature unknown; restored from __doc__
        """ set_locale(self, lc_collate:str, cancellable:Gio.Cancellable=None) -> bool """
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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unlock(self, action): # real signature unknown; restored from __doc__
        """ unlock(self, action:EDataBook.bSqlUnlockAction) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f09d0c21dc0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BookSqlite), '__module__': 'gi.repository.EDataBook', '__gtype__': <GType EBookSqlite (94654337922528)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_full': gi.FunctionInfo(new_full), 'error_quark': gi.FunctionInfo(error_quark), 'search_data_free': gi.FunctionInfo(search_data_free), 'add_contact': gi.FunctionInfo(add_contact), 'add_contacts': gi.FunctionInfo(add_contacts), 'get_contact': gi.FunctionInfo(get_contact), 'get_contact_extra': gi.FunctionInfo(get_contact_extra), 'get_key_value': gi.FunctionInfo(get_key_value), 'get_key_value_int': gi.FunctionInfo(get_key_value_int), 'get_locale': gi.FunctionInfo(get_locale), 'get_vcard': gi.FunctionInfo(get_vcard), 'has_contact': gi.FunctionInfo(has_contact), 'lock': gi.FunctionInfo(lock), 'ref_collator': gi.FunctionInfo(ref_collator), 'ref_source': gi.FunctionInfo(ref_source), 'remove_contact': gi.FunctionInfo(remove_contact), 'remove_contacts': gi.FunctionInfo(remove_contacts), 'search': gi.FunctionInfo(search), 'search_uids': gi.FunctionInfo(search_uids), 'set_contact_extra': gi.FunctionInfo(set_contact_extra), 'set_key_value': gi.FunctionInfo(set_key_value), 'set_key_value_int': gi.FunctionInfo(set_key_value_int), 'set_locale': gi.FunctionInfo(set_locale), 'unlock': gi.FunctionInfo(unlock), 'do_before_insert_contact': gi.VFuncInfo(before_insert_contact), 'do_before_remove_contact': gi.VFuncInfo(before_remove_contact), 'parent': <property object at 0x7f09d41b9450>, 'priv': <property object at 0x7f09d41b95e0>})"
    __gdoc__ = 'Object EBookSqlite\n\nSignals from EBookSqlite:\n  before-insert-contact (gpointer, EContact, gchararray, gboolean, GObject, gpointer) -> gboolean\n  before-remove-contact (gpointer, gchararray, GCancellable, gpointer) -> gboolean\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EBookSqlite (94654337922528)>'
    __info__ = ObjectInfo(BookSqlite)


