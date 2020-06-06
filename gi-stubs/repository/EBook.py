# encoding: utf-8
# module gi.repository.EBook
# from /usr/lib64/girepository-1.0/EBook-1.2.typelib
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


# Variables with simple values

_namespace = 'EBook'

_version = '1.2'

__weakref__ = None

# functions

def book_error_quark(): # real signature unknown; restored from __doc__
    """ book_error_quark() -> int """
    return 0

def book_utils_get_recipient_certificates_sync(registry, only_clients=None, flags, recipients, cancellable=None): # real signature unknown; restored from __doc__
    """ book_utils_get_recipient_certificates_sync(registry:EDataServer.SourceRegistry, only_clients:list=None, flags:int, recipients:list, cancellable:Gio.Cancellable=None) -> bool, out_certificates:list """
    return False

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

class BookClient(__gi_repository_EDataServer.Client, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        BookClient(**properties)
        new(source:EDataServer.Source) -> EBook.BookClient
    """
    def add_contact(self, contact, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_contact(self, contact:EBookContacts.Contact, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_contacts(self, contacts, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ add_contacts(self, contacts:list, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def add_contacts_finish(self, result): # real signature unknown; restored from __doc__
        """ add_contacts_finish(self, result:Gio.AsyncResult) -> bool, out_added_uids:list """
        return False

    def add_contacts_sync(self, contacts, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ add_contacts_sync(self, contacts:list, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_added_uids:list """
        return False

    def add_contact_finish(self, result): # real signature unknown; restored from __doc__
        """ add_contact_finish(self, result:Gio.AsyncResult) -> bool, out_added_uid:str """
        return False

    def add_contact_sync(self, contact, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ add_contact_sync(self, contact:EBookContacts.Contact, opflags:int, cancellable:Gio.Cancellable=None) -> bool, out_added_uid:str """
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

    def check_refresh_supported(self): # real signature unknown; restored from __doc__
        """ check_refresh_supported(self) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, source, wait_for_connected_seconds, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect(source:EDataServer.Source, wait_for_connected_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def connect_direct(self, source, wait_for_connected_seconds, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect_direct(source:EDataServer.Source, wait_for_connected_seconds:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def connect_direct_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_direct_finish(result:Gio.AsyncResult) -> EBook.BookClient """
        pass

    def connect_direct_sync(self, registry, source, wait_for_connected_seconds, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_direct_sync(registry:EDataServer.SourceRegistry, source:EDataServer.Source, wait_for_connected_seconds:int, cancellable:Gio.Cancellable=None) -> EBook.BookClient """
        pass

    def connect_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_finish(result:Gio.AsyncResult) -> EBook.BookClient """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_sync(self, source, wait_for_connected_seconds, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(source:EDataServer.Source, wait_for_connected_seconds:int, cancellable:Gio.Cancellable=None) -> EBook.BookClient """
        pass

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
        """ error_create(code:EDataServer.ClientError, custom_msg:str=None) -> error """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def error_to_string(self, code): # real signature unknown; restored from __doc__
        """ error_to_string(code:EDataServer.ClientError) -> str """
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

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

    def get_contact(self, uid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_contact(self, uid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_contacts(self, sexp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_contacts(self, sexp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_contacts_finish(self, result): # real signature unknown; restored from __doc__
        """ get_contacts_finish(self, result:Gio.AsyncResult) -> bool, out_contacts:list """
        return False

    def get_contacts_sync(self, sexp, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contacts_sync(self, sexp:str, cancellable:Gio.Cancellable=None) -> bool, out_contacts:list """
        return False

    def get_contacts_uids(self, sexp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_contacts_uids(self, sexp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_contacts_uids_finish(self, result): # real signature unknown; restored from __doc__
        """ get_contacts_uids_finish(self, result:Gio.AsyncResult) -> bool, out_contact_uids:list """
        return False

    def get_contacts_uids_sync(self, sexp, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contacts_uids_sync(self, sexp:str, cancellable:Gio.Cancellable=None) -> bool, out_contact_uids:list """
        return False

    def get_contact_finish(self, result): # real signature unknown; restored from __doc__
        """ get_contact_finish(self, result:Gio.AsyncResult) -> bool, out_contact:EBookContacts.Contact """
        return False

    def get_contact_sync(self, uid, cancellable=None): # real signature unknown; restored from __doc__
        """ get_contact_sync(self, uid:str, cancellable:Gio.Cancellable=None) -> bool, out_contact:EBookContacts.Contact """
        return False

    def get_cursor(self, sexp, sort_fields, sort_types, n_fields, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_cursor(self, sexp:str, sort_fields:EBookContacts.ContactField, sort_types:EBookContacts.BookCursorSortType, n_fields:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_cursor_finish(self, result): # real signature unknown; restored from __doc__
        """ get_cursor_finish(self, result:Gio.AsyncResult) -> bool, out_cursor:EBook.BookClientCursor """
        return False

    def get_cursor_sync(self, sexp, sort_fields, sort_types, n_fields, cancellable=None): # real signature unknown; restored from __doc__
        """ get_cursor_sync(self, sexp:str, sort_fields:EBookContacts.ContactField, sort_types:EBookContacts.BookCursorSortType, n_fields:int, cancellable:Gio.Cancellable=None) -> bool, out_cursor:EBook.BookClientCursor """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_locale(self): # real signature unknown; restored from __doc__
        """ get_locale(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_self(self, registry): # real signature unknown; restored from __doc__
        """ get_self(registry:EDataServer.SourceRegistry) -> bool, out_contact:EBookContacts.Contact, out_client:EBook.BookClient """
        return False

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_view(self, sexp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_view(self, sexp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_view_finish(self, result): # real signature unknown; restored from __doc__
        """ get_view_finish(self, result:Gio.AsyncResult) -> bool, out_view:EBook.BookClientView """
        return False

    def get_view_sync(self, sexp, cancellable=None): # real signature unknown; restored from __doc__
        """ get_view_sync(self, sexp:str, cancellable:Gio.Cancellable=None) -> bool, out_view:EBook.BookClientView """
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

    def is_self(self, contact): # real signature unknown; restored from __doc__
        """ is_self(contact:EBookContacts.Contact) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def modify_contact(self, contact, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ modify_contact(self, contact:EBookContacts.Contact, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def modify_contacts(self, contacts, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ modify_contacts(self, contacts:list, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def modify_contacts_finish(self, result): # real signature unknown; restored from __doc__
        """ modify_contacts_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def modify_contacts_sync(self, contacts, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_contacts_sync(self, contacts:list, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def modify_contact_finish(self, result): # real signature unknown; restored from __doc__
        """ modify_contact_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def modify_contact_sync(self, contact, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ modify_contact_sync(self, contact:EBookContacts.Contact, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def new(self, source): # real signature unknown; restored from __doc__
        """ new(source:EDataServer.Source) -> EBook.BookClient """
        pass

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

    def remove_contact(self, contact, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_contact(self, contact:EBookContacts.Contact, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_contacts(self, uids, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_contacts(self, uids:list, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_contacts_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_contacts_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_contacts_sync(self, uids, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contacts_sync(self, uids:list, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_contact_by_uid(self, uid, opflags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ remove_contact_by_uid(self, uid:str, opflags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def remove_contact_by_uid_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_contact_by_uid_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_contact_by_uid_sync(self, uid, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contact_by_uid_sync(self, uid:str, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_contact_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_contact_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def remove_contact_sync(self, contact, opflags, cancellable=None): # real signature unknown; restored from __doc__
        """ remove_contact_sync(self, contact:EBookContacts.Contact, opflags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def remove_finish(self, result): # real signature unknown; restored from __doc__
        """ remove_finish(self, result:Gio.AsyncResult) -> bool """
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

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_self(self, contact): # real signature unknown; restored from __doc__
        """ set_self(self, contact:EBookContacts.Contact) -> bool """
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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f298c28d640>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BookClient), '__module__': 'gi.repository.EBook', '__gtype__': <GType EBookClient (94072263458224)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'connect': gi.FunctionInfo(connect), 'connect_direct': gi.FunctionInfo(connect_direct), 'connect_direct_finish': gi.FunctionInfo(connect_direct_finish), 'connect_direct_sync': gi.FunctionInfo(connect_direct_sync), 'connect_finish': gi.FunctionInfo(connect_finish), 'connect_sync': gi.FunctionInfo(connect_sync), 'get_self': gi.FunctionInfo(get_self), 'is_self': gi.FunctionInfo(is_self), 'add_contact': gi.FunctionInfo(add_contact), 'add_contact_finish': gi.FunctionInfo(add_contact_finish), 'add_contact_sync': gi.FunctionInfo(add_contact_sync), 'add_contacts': gi.FunctionInfo(add_contacts), 'add_contacts_finish': gi.FunctionInfo(add_contacts_finish), 'add_contacts_sync': gi.FunctionInfo(add_contacts_sync), 'get_contact': gi.FunctionInfo(get_contact), 'get_contact_finish': gi.FunctionInfo(get_contact_finish), 'get_contact_sync': gi.FunctionInfo(get_contact_sync), 'get_contacts': gi.FunctionInfo(get_contacts), 'get_contacts_finish': gi.FunctionInfo(get_contacts_finish), 'get_contacts_sync': gi.FunctionInfo(get_contacts_sync), 'get_contacts_uids': gi.FunctionInfo(get_contacts_uids), 'get_contacts_uids_finish': gi.FunctionInfo(get_contacts_uids_finish), 'get_contacts_uids_sync': gi.FunctionInfo(get_contacts_uids_sync), 'get_cursor': gi.FunctionInfo(get_cursor), 'get_cursor_finish': gi.FunctionInfo(get_cursor_finish), 'get_cursor_sync': gi.FunctionInfo(get_cursor_sync), 'get_locale': gi.FunctionInfo(get_locale), 'get_view': gi.FunctionInfo(get_view), 'get_view_finish': gi.FunctionInfo(get_view_finish), 'get_view_sync': gi.FunctionInfo(get_view_sync), 'modify_contact': gi.FunctionInfo(modify_contact), 'modify_contact_finish': gi.FunctionInfo(modify_contact_finish), 'modify_contact_sync': gi.FunctionInfo(modify_contact_sync), 'modify_contacts': gi.FunctionInfo(modify_contacts), 'modify_contacts_finish': gi.FunctionInfo(modify_contacts_finish), 'modify_contacts_sync': gi.FunctionInfo(modify_contacts_sync), 'remove_contact': gi.FunctionInfo(remove_contact), 'remove_contact_by_uid': gi.FunctionInfo(remove_contact_by_uid), 'remove_contact_by_uid_finish': gi.FunctionInfo(remove_contact_by_uid_finish), 'remove_contact_by_uid_sync': gi.FunctionInfo(remove_contact_by_uid_sync), 'remove_contact_finish': gi.FunctionInfo(remove_contact_finish), 'remove_contact_sync': gi.FunctionInfo(remove_contact_sync), 'remove_contacts': gi.FunctionInfo(remove_contacts), 'remove_contacts_finish': gi.FunctionInfo(remove_contacts_finish), 'remove_contacts_sync': gi.FunctionInfo(remove_contacts_sync), 'set_self': gi.FunctionInfo(set_self), 'parent': <property object at 0x7f298c256770>, 'priv': <property object at 0x7f298c2567c0>})"
    __gdoc__ = "Object EBookClient\n\nProperties from EBookClient:\n  locale -> gchararray: Locale\n    The currently active locale for this addressbook\n\nSignals from EClient:\n  opened (GError)\n  backend-error (gchararray)\n  backend-died ()\n  backend-property-changed (gchararray, gchararray)\n\nProperties from EClient:\n  capabilities -> gpointer: Capabilities\n    The capabilities of this client\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  online -> gboolean: Online\n    Whether this client is online\n  opened -> gboolean: Opened\n    Whether this client is open and ready to use\n  readonly -> gboolean: Read only\n    Whether this client's backing data is readonly\n  source -> ESource: Source\n    The ESource for which this client was created\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EBookClient (94072263458224)>'
    __info__ = ObjectInfo(BookClient)


class BookClientClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BookClientClass()
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


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookClientClass), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BookClientClass' objects>, '__weakref__': <attribute '__weakref__' of 'BookClientClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f298c256950>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BookClientClass)


class BookClientCursor(__gi_overrides_GObject.Object, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        BookClientCursor(**properties)
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

    def do_refresh(self, *args, **kwargs): # real signature unknown
        """ refresh(self) """
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

    def get_alphabet(self): # real signature unknown; restored from __doc__
        """ get_alphabet(self) -> list, n_labels:int, underflow:int, inflow:int, overflow:int """
        return []

    def get_contact_alphabetic_index(self, contact): # real signature unknown; restored from __doc__
        """ get_contact_alphabetic_index(self, contact:EBookContacts.Contact) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_total(self): # real signature unknown; restored from __doc__
        """ get_total(self) -> int """
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

    def ref_client(self): # real signature unknown; restored from __doc__
        """ ref_client(self) """
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

    def set_alphabetic_index(self, index, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_alphabetic_index(self, index:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_alphabetic_index_finish(self, result): # real signature unknown; restored from __doc__
        """ set_alphabetic_index_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_alphabetic_index_sync(self, index, cancellable=None): # real signature unknown; restored from __doc__
        """ set_alphabetic_index_sync(self, index:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sexp(self, sexp, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_sexp(self, sexp:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_sexp_finish(self, result): # real signature unknown; restored from __doc__
        """ set_sexp_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def set_sexp_sync(self, sexp, cancellable=None): # real signature unknown; restored from __doc__
        """ set_sexp_sync(self, sexp:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def step(self, flags, origin, count, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ step(self, flags:EBookContacts.BookCursorStepFlags, origin:EBookContacts.BookCursorOrigin, count:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def step_finish(self, result): # real signature unknown; restored from __doc__
        """ step_finish(self, result:Gio.AsyncResult) -> int, out_contacts:list """
        return 0

    def step_sync(self, flags, origin, count, cancellable=None): # real signature unknown; restored from __doc__
        """ step_sync(self, flags:EBookContacts.BookCursorStepFlags, origin:EBookContacts.BookCursorOrigin, count:int, cancellable:Gio.Cancellable=None) -> int, out_contacts:list """
        return 0

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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f2988c91b20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BookClientCursor), '__module__': 'gi.repository.EBook', '__gtype__': <GType EBookClientCursor (94072263478192)>, '__doc__': None, '__gsignals__': {}, 'get_alphabet': gi.FunctionInfo(get_alphabet), 'get_contact_alphabetic_index': gi.FunctionInfo(get_contact_alphabetic_index), 'get_position': gi.FunctionInfo(get_position), 'get_total': gi.FunctionInfo(get_total), 'ref_client': gi.FunctionInfo(ref_client), 'set_alphabetic_index': gi.FunctionInfo(set_alphabetic_index), 'set_alphabetic_index_finish': gi.FunctionInfo(set_alphabetic_index_finish), 'set_alphabetic_index_sync': gi.FunctionInfo(set_alphabetic_index_sync), 'set_sexp': gi.FunctionInfo(set_sexp), 'set_sexp_finish': gi.FunctionInfo(set_sexp_finish), 'set_sexp_sync': gi.FunctionInfo(set_sexp_sync), 'step': gi.FunctionInfo(step), 'step_finish': gi.FunctionInfo(step_finish), 'step_sync': gi.FunctionInfo(step_sync), 'do_refresh': gi.VFuncInfo(refresh), 'parent': <property object at 0x7f298c256c20>, 'priv': <property object at 0x7f298c256d10>})"
    __gdoc__ = "Object EBookClientCursor\n\nSignals from EBookClientCursor:\n  refresh ()\n\nProperties from EBookClientCursor:\n  sort-fields -> GStrv: Sort Fields\n    The #EContactField names to sort this cursor with\n  client -> EBookClient: Client\n    The EBookClient for the cursor\n  context -> GMainContext: Context\n    The GMainContext in which this cursor was created\n  connection -> GDBusConnection: Connection\n    The GDBusConnection used to create the D-Bus proxy\n  object-path -> gchararray: Object Path\n    The object path used to create the D-Bus proxy\n  direct-cursor -> EDataBookCursor: Direct Cursor\n    The EDataBookCursor for direct read access\n  alphabet -> GStrv: Alphabet\n    The active alphabet\n  total -> gint: Total\n    The total contacts for this cursor's query\n  position -> gint: Position\n    The current cursor position\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EBookClientCursor (94072263478192)>'
    __info__ = ObjectInfo(BookClientCursor)


class BookClientCursorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BookClientCursorClass()
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

    refresh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookClientCursorClass), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BookClientCursorClass' objects>, '__weakref__': <attribute '__weakref__' of 'BookClientCursorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f298c256ea0>, 'refresh': <property object at 0x7f298c256f90>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BookClientCursorClass)


class BookClientCursorPrivate(__gi.Struct):
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookClientCursorPrivate), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BookClientCursorPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'BookClientCursorPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BookClientCursorPrivate)


class BookClientPrivate(__gi.Struct):
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookClientPrivate), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BookClientPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'BookClientPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BookClientPrivate)


class BookClientView(__gi_overrides_GObject.Object, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        BookClientView(**properties)
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

    def do_complete(self, *args, **kwargs): # real signature unknown
        """ complete(self, error:error) """
        pass

    def do_progress(self, *args, **kwargs): # real signature unknown
        """ progress(self, percent:int, message:str) """
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

    def get_client(self): # real signature unknown; restored from __doc__
        """ get_client(self) """
        pass

    def get_connection(self): # real signature unknown; restored from __doc__
        """ get_connection(self) -> Gio.DBusConnection """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

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

    def is_running(self): # real signature unknown; restored from __doc__
        """ is_running(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

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

    def ref_client(self): # real signature unknown; restored from __doc__
        """ ref_client(self) """
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

    def set_fields_of_interest(self, fields_of_interest): # real signature unknown; restored from __doc__
        """ set_fields_of_interest(self, fields_of_interest:list) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:EBookContacts.BookClientViewFlags) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f298c2528e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BookClientView), '__module__': 'gi.repository.EBook', '__gtype__': <GType EBookClientView (94072263487808)>, '__doc__': None, '__gsignals__': {}, 'get_client': gi.FunctionInfo(get_client), 'get_connection': gi.FunctionInfo(get_connection), 'get_object_path': gi.FunctionInfo(get_object_path), 'is_running': gi.FunctionInfo(is_running), 'ref_client': gi.FunctionInfo(ref_client), 'set_fields_of_interest': gi.FunctionInfo(set_fields_of_interest), 'set_flags': gi.FunctionInfo(set_flags), 'start': gi.FunctionInfo(start), 'stop': gi.FunctionInfo(stop), 'do_complete': gi.VFuncInfo(complete), 'do_progress': gi.VFuncInfo(progress), 'parent': <property object at 0x7f298c257310>, 'priv': <property object at 0x7f298c257400>})"
    __gdoc__ = 'Object EBookClientView\n\nSignals from EBookClientView:\n  objects-added (gpointer)\n  objects-modified (gpointer)\n  objects-removed (gpointer)\n  progress (guint, gchararray)\n  complete (GError)\n\nProperties from EBookClientView:\n  client -> EBookClient: Client\n    The EBookClient for the view\n  connection -> GDBusConnection: Connection\n    The GDBusConnection used to create the D-Bus proxy\n  direct-backend -> EBookBackend: Direct Backend\n    The EBookBackend to fetch contact data from, if direct read access is enabled\n  object-path -> gchararray: Object Path\n    The object path used to create the D-Bus proxy\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EBookClientView (94072263487808)>'
    __info__ = ObjectInfo(BookClientView)


class BookClientViewClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BookClientViewClass()
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

    complete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    objects_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    objects_modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    objects_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookClientViewClass), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BookClientViewClass' objects>, '__weakref__': <attribute '__weakref__' of 'BookClientViewClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f298c257590>, 'objects_added': <property object at 0x7f298c257680>, 'objects_modified': <property object at 0x7f298c2577c0>, 'objects_removed': <property object at 0x7f298c2578b0>, 'progress': <property object at 0x7f298c2579a0>, 'complete': <property object at 0x7f298c257a90>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BookClientViewClass)


class BookClientViewPrivate(__gi.Struct):
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BookClientViewPrivate), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BookClientViewPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'BookClientViewPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BookClientViewPrivate)


class BookStatus(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    AUTHENTICATION_FAILED = 14
    AUTHENTICATION_REQUIRED = 15
    BUSY = 2
    CANCELLED = 12
    CONTACT_ID_ALREADY_EXISTS = 10
    CONTACT_NOT_FOUND = 9
    COULD_NOT_CANCEL = 13
    DBUS_EXCEPTION = 17
    INVALID_ARG = 1
    INVALID_SERVER_VERSION = 21
    NOT_SUPPORTED = 24
    NO_SELF_CONTACT = 5
    NO_SPACE = 23
    NO_SUCH_BOOK = 4
    NO_SUCH_SOURCE = 18
    OFFLINE_UNAVAILABLE = 19
    OK = 0
    OTHER_ERROR = 20
    PERMISSION_DENIED = 8
    PROTOCOL_NOT_SUPPORTED = 11
    REPOSITORY_OFFLINE = 3
    SOURCE_ALREADY_LOADED = 7
    SOURCE_NOT_LOADED = 6
    TLS_NOT_AVAILABLE = 16
    UNSUPPORTED_AUTHENTICATION_METHOD = 22
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.EBook', '__dict__': <attribute '__dict__' of 'BookStatus' objects>, '__doc__': None, '__gtype__': <GType EBookStatus (94072263496928)>, '__enum_values__': {0: <enum E_BOOK_ERROR_OK of type EBook.BookStatus>, 1: <enum E_BOOK_ERROR_INVALID_ARG of type EBook.BookStatus>, 2: <enum E_BOOK_ERROR_BUSY of type EBook.BookStatus>, 3: <enum E_BOOK_ERROR_REPOSITORY_OFFLINE of type EBook.BookStatus>, 4: <enum E_BOOK_ERROR_NO_SUCH_BOOK of type EBook.BookStatus>, 5: <enum E_BOOK_ERROR_NO_SELF_CONTACT of type EBook.BookStatus>, 6: <enum E_BOOK_ERROR_SOURCE_NOT_LOADED of type EBook.BookStatus>, 7: <enum E_BOOK_ERROR_SOURCE_ALREADY_LOADED of type EBook.BookStatus>, 8: <enum E_BOOK_ERROR_PERMISSION_DENIED of type EBook.BookStatus>, 9: <enum E_BOOK_ERROR_CONTACT_NOT_FOUND of type EBook.BookStatus>, 10: <enum E_BOOK_ERROR_CONTACT_ID_ALREADY_EXISTS of type EBook.BookStatus>, 11: <enum E_BOOK_ERROR_PROTOCOL_NOT_SUPPORTED of type EBook.BookStatus>, 12: <enum E_BOOK_ERROR_CANCELLED of type EBook.BookStatus>, 13: <enum E_BOOK_ERROR_COULD_NOT_CANCEL of type EBook.BookStatus>, 14: <enum E_BOOK_ERROR_AUTHENTICATION_FAILED of type EBook.BookStatus>, 15: <enum E_BOOK_ERROR_AUTHENTICATION_REQUIRED of type EBook.BookStatus>, 16: <enum E_BOOK_ERROR_TLS_NOT_AVAILABLE of type EBook.BookStatus>, 17: <enum E_BOOK_ERROR_DBUS_EXCEPTION of type EBook.BookStatus>, 18: <enum E_BOOK_ERROR_NO_SUCH_SOURCE of type EBook.BookStatus>, 19: <enum E_BOOK_ERROR_OFFLINE_UNAVAILABLE of type EBook.BookStatus>, 20: <enum E_BOOK_ERROR_OTHER_ERROR of type EBook.BookStatus>, 21: <enum E_BOOK_ERROR_INVALID_SERVER_VERSION of type EBook.BookStatus>, 22: <enum E_BOOK_ERROR_UNSUPPORTED_AUTHENTICATION_METHOD of type EBook.BookStatus>, 23: <enum E_BOOK_ERROR_NO_SPACE of type EBook.BookStatus>, 24: <enum E_BOOK_ERROR_NOT_SUPPORTED of type EBook.BookStatus>}, '__info__': gi.EnumInfo(BookStatus), 'OK': <enum E_BOOK_ERROR_OK of type EBook.BookStatus>, 'INVALID_ARG': <enum E_BOOK_ERROR_INVALID_ARG of type EBook.BookStatus>, 'BUSY': <enum E_BOOK_ERROR_BUSY of type EBook.BookStatus>, 'REPOSITORY_OFFLINE': <enum E_BOOK_ERROR_REPOSITORY_OFFLINE of type EBook.BookStatus>, 'NO_SUCH_BOOK': <enum E_BOOK_ERROR_NO_SUCH_BOOK of type EBook.BookStatus>, 'NO_SELF_CONTACT': <enum E_BOOK_ERROR_NO_SELF_CONTACT of type EBook.BookStatus>, 'SOURCE_NOT_LOADED': <enum E_BOOK_ERROR_SOURCE_NOT_LOADED of type EBook.BookStatus>, 'SOURCE_ALREADY_LOADED': <enum E_BOOK_ERROR_SOURCE_ALREADY_LOADED of type EBook.BookStatus>, 'PERMISSION_DENIED': <enum E_BOOK_ERROR_PERMISSION_DENIED of type EBook.BookStatus>, 'CONTACT_NOT_FOUND': <enum E_BOOK_ERROR_CONTACT_NOT_FOUND of type EBook.BookStatus>, 'CONTACT_ID_ALREADY_EXISTS': <enum E_BOOK_ERROR_CONTACT_ID_ALREADY_EXISTS of type EBook.BookStatus>, 'PROTOCOL_NOT_SUPPORTED': <enum E_BOOK_ERROR_PROTOCOL_NOT_SUPPORTED of type EBook.BookStatus>, 'CANCELLED': <enum E_BOOK_ERROR_CANCELLED of type EBook.BookStatus>, 'COULD_NOT_CANCEL': <enum E_BOOK_ERROR_COULD_NOT_CANCEL of type EBook.BookStatus>, 'AUTHENTICATION_FAILED': <enum E_BOOK_ERROR_AUTHENTICATION_FAILED of type EBook.BookStatus>, 'AUTHENTICATION_REQUIRED': <enum E_BOOK_ERROR_AUTHENTICATION_REQUIRED of type EBook.BookStatus>, 'TLS_NOT_AVAILABLE': <enum E_BOOK_ERROR_TLS_NOT_AVAILABLE of type EBook.BookStatus>, 'DBUS_EXCEPTION': <enum E_BOOK_ERROR_DBUS_EXCEPTION of type EBook.BookStatus>, 'NO_SUCH_SOURCE': <enum E_BOOK_ERROR_NO_SUCH_SOURCE of type EBook.BookStatus>, 'OFFLINE_UNAVAILABLE': <enum E_BOOK_ERROR_OFFLINE_UNAVAILABLE of type EBook.BookStatus>, 'OTHER_ERROR': <enum E_BOOK_ERROR_OTHER_ERROR of type EBook.BookStatus>, 'INVALID_SERVER_VERSION': <enum E_BOOK_ERROR_INVALID_SERVER_VERSION of type EBook.BookStatus>, 'UNSUPPORTED_AUTHENTICATION_METHOD': <enum E_BOOK_ERROR_UNSUPPORTED_AUTHENTICATION_METHOD of type EBook.BookStatus>, 'NO_SPACE': <enum E_BOOK_ERROR_NO_SPACE of type EBook.BookStatus>, 'NOT_SUPPORTED': <enum E_BOOK_ERROR_NOT_SUPPORTED of type EBook.BookStatus>})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
    }
    __gtype__ = None # (!) real value is '<GType EBookStatus (94072263496928)>'
    __info__ = gi.EnumInfo(BookStatus)


class Destination(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Destination(**properties)
        new() -> EBook.Destination
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

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> EBook.Destination """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """ empty(self) -> bool """
        return False

    def equal(self, b): # real signature unknown; restored from __doc__
        """ equal(self, b:EBook.Destination) -> bool """
        return False

    def export(self): # real signature unknown; restored from __doc__
        """ export(self) -> str """
        return ""

    def exportv(self, destv): # real signature unknown; restored from __doc__
        """ exportv(destv:list) -> str """
        return ""

    def export_to_vcard_attribute(self, attr): # real signature unknown; restored from __doc__
        """ export_to_vcard_attribute(self, attr:EBookContacts.VCardAttribute) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freev(self, destv): # real signature unknown; restored from __doc__
        """ freev(destv:list) """
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

    def get_address(self): # real signature unknown; restored from __doc__
        """ get_address(self) -> str or None """
        return ""

    def get_contact(self): # real signature unknown; restored from __doc__
        """ get_contact(self) -> EBookContacts.Contact or None """
        pass

    def get_contact_uid(self): # real signature unknown; restored from __doc__
        """ get_contact_uid(self) -> str or None """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_email(self): # real signature unknown; restored from __doc__
        """ get_email(self) -> str """
        return ""

    def get_email_num(self): # real signature unknown; restored from __doc__
        """ get_email_num(self) -> int """
        return 0

    def get_html_mail_pref(self): # real signature unknown; restored from __doc__
        """ get_html_mail_pref(self) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_source_uid(self): # real signature unknown; restored from __doc__
        """ get_source_uid(self) -> str or None """
        return ""

    def get_textrep(self, include_email): # real signature unknown; restored from __doc__
        """ get_textrep(self, include_email:bool) -> str """
        return ""

    def get_textrepv(self, destv): # real signature unknown; restored from __doc__
        """ get_textrepv(destv:list) -> str """
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

    def importv(self, p_str): # real signature unknown; restored from __doc__
        """ importv(str:str) -> list """
        return []

    def import_(self, p_str): # real signature unknown; restored from __doc__
        """ import_(str:str) -> EBook.Destination or None """
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

    def is_auto_recipient(self): # real signature unknown; restored from __doc__
        """ is_auto_recipient(self) -> bool """
        return False

    def is_evolution_list(self): # real signature unknown; restored from __doc__
        """ is_evolution_list(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_ignored(self): # real signature unknown; restored from __doc__
        """ is_ignored(self) -> bool """
        return False

    def list_get_dests(self): # real signature unknown; restored from __doc__
        """ list_get_dests(self) -> list """
        return []

    def list_get_root_dests(self): # real signature unknown; restored from __doc__
        """ list_get_root_dests(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_show_addresses(self): # real signature unknown; restored from __doc__
        """ list_show_addresses(self) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> EBook.Destination """
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

    def set_auto_recipient(self, value): # real signature unknown; restored from __doc__
        """ set_auto_recipient(self, value:bool) """
        pass

    def set_client(self, client): # real signature unknown; restored from __doc__
        """ set_client(self, client:EBook.BookClient) """
        pass

    def set_contact(self, contact, email_num): # real signature unknown; restored from __doc__
        """ set_contact(self, contact:EBookContacts.Contact, email_num:int) """
        pass

    def set_contact_uid(self, uid, email_num): # real signature unknown; restored from __doc__
        """ set_contact_uid(self, uid:str, email_num:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_email(self, email): # real signature unknown; restored from __doc__
        """ set_email(self, email:str) """
        pass

    def set_html_mail_pref(self, flag): # real signature unknown; restored from __doc__
        """ set_html_mail_pref(self, flag:bool) """
        pass

    def set_ignored(self, ignored): # real signature unknown; restored from __doc__
        """ set_ignored(self, ignored:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_raw(self, raw): # real signature unknown; restored from __doc__
        """ set_raw(self, raw:str) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f298c23c940>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Destination), '__module__': 'gi.repository.EBook', '__gtype__': <GType EDestination (94072263505056)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'exportv': gi.FunctionInfo(exportv), 'freev': gi.FunctionInfo(freev), 'get_textrepv': gi.FunctionInfo(get_textrepv), 'import_': gi.FunctionInfo(import), 'importv': gi.FunctionInfo(importv), 'copy': gi.FunctionInfo(copy), 'empty': gi.FunctionInfo(empty), 'equal': gi.FunctionInfo(equal), 'export': gi.FunctionInfo(export), 'export_to_vcard_attribute': gi.FunctionInfo(export_to_vcard_attribute), 'get_address': gi.FunctionInfo(get_address), 'get_contact': gi.FunctionInfo(get_contact), 'get_contact_uid': gi.FunctionInfo(get_contact_uid), 'get_email': gi.FunctionInfo(get_email), 'get_email_num': gi.FunctionInfo(get_email_num), 'get_html_mail_pref': gi.FunctionInfo(get_html_mail_pref), 'get_name': gi.FunctionInfo(get_name), 'get_source_uid': gi.FunctionInfo(get_source_uid), 'get_textrep': gi.FunctionInfo(get_textrep), 'is_auto_recipient': gi.FunctionInfo(is_auto_recipient), 'is_evolution_list': gi.FunctionInfo(is_evolution_list), 'is_ignored': gi.FunctionInfo(is_ignored), 'list_get_dests': gi.FunctionInfo(list_get_dests), 'list_get_root_dests': gi.FunctionInfo(list_get_root_dests), 'list_show_addresses': gi.FunctionInfo(list_show_addresses), 'set_auto_recipient': gi.FunctionInfo(set_auto_recipient), 'set_client': gi.FunctionInfo(set_client), 'set_contact': gi.FunctionInfo(set_contact), 'set_contact_uid': gi.FunctionInfo(set_contact_uid), 'set_email': gi.FunctionInfo(set_email), 'set_html_mail_pref': gi.FunctionInfo(set_html_mail_pref), 'set_ignored': gi.FunctionInfo(set_ignored), 'set_name': gi.FunctionInfo(set_name), 'set_raw': gi.FunctionInfo(set_raw), 'do_changed': gi.VFuncInfo(changed), 'object': <property object at 0x7f298c25ac20>, 'priv': <property object at 0x7f298c25ad10>})"
    __gdoc__ = 'Object EDestination\n\nSignals from EDestination:\n  changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType EDestination (94072263505056)>'
    __info__ = ObjectInfo(Destination)


class DestinationClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DestinationClass()
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

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ebook_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ebook_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ebook_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ebook_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DestinationClass), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DestinationClass' objects>, '__weakref__': <attribute '__weakref__' of 'DestinationClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f298c25aea0>, 'changed': <property object at 0x7f298c25af90>, '_ebook_reserved1': <property object at 0x7f298c25d130>, '_ebook_reserved2': <property object at 0x7f298c25d270>, '_ebook_reserved3': <property object at 0x7f298c25d3b0>, '_ebook_reserved4': <property object at 0x7f298c25d4f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DestinationClass)


class DestinationPrivate(__gi.Struct):
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DestinationPrivate), '__module__': 'gi.repository.EBook', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DestinationPrivate' objects>, '__weakref__': <attribute '__weakref__' of 'DestinationPrivate' objects>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DestinationPrivate)


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.module', '__doc__': 'An object which wraps an introspection typelib.\\n\\n    This wrapping creates a python module like representation of the typelib\\n    using gi repository as a foundation. Accessing attributes of the module\\n    will dynamically pull them in and create wrappers for the members.\\n    These members are then cached on this introspection module.\\n    ', '__init__': <function IntrospectionModule.__init__ at 0x7f298c5081f0>, '__getattr__': <function IntrospectionModule.__getattr__ at 0x7f298c508280>, '__repr__': <function IntrospectionModule.__repr__ at 0x7f298c508310>, '__dir__': <function IntrospectionModule.__dir__ at 0x7f298c5083a0>, '__dict__': <attribute '__dict__' of 'IntrospectionModule' objects>, '__weakref__': <attribute '__weakref__' of 'IntrospectionModule' objects>})"


# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f298d144d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EBook-1.2.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EBook', loader=<gi.importer.DynamicImporter object at 0x7f298d144d00>)"

