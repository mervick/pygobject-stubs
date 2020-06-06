# encoding: utf-8
# module gi.repository.Goa
# from /usr/lib64/girepository-1.0/Goa-1.0.typelib
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


from .Object import Object

class ObjectSkeleton(__gi_repository_Gio.DBusObjectSkeleton, Object):
    """
    :Constructors:
    
    ::
    
        ObjectSkeleton(**properties)
        new(object_path:str) -> Goa.ObjectSkeleton
    """
    def add_interface(self, interface_): # real signature unknown; restored from __doc__
        """ add_interface(self, interface_:Gio.DBusInterfaceSkeleton) """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authorize_method(self, *args, **kwargs): # real signature unknown
        """ authorize_method(self, interface_:Gio.DBusInterfaceSkeleton, invocation:Gio.DBusMethodInvocation) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
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

    def get_account(self): # real signature unknown; restored from __doc__
        """ get_account(self) -> Goa.Account or None """
        pass

    def get_calendar(self): # real signature unknown; restored from __doc__
        """ get_calendar(self) -> Goa.Calendar or None """
        pass

    def get_chat(self): # real signature unknown; restored from __doc__
        """ get_chat(self) -> Goa.Chat or None """
        pass

    def get_contacts(self): # real signature unknown; restored from __doc__
        """ get_contacts(self) -> Goa.Contacts or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_documents(self): # real signature unknown; restored from __doc__
        """ get_documents(self) -> Goa.Documents or None """
        pass

    def get_exchange(self): # real signature unknown; restored from __doc__
        """ get_exchange(self) -> Goa.Exchange or None """
        pass

    def get_files(self): # real signature unknown; restored from __doc__
        """ get_files(self) -> Goa.Files or None """
        pass

    def get_interface(self, interface_name): # real signature unknown; restored from __doc__
        """ get_interface(self, interface_name:str) -> Gio.DBusInterface """
        pass

    def get_interfaces(self): # real signature unknown; restored from __doc__
        """ get_interfaces(self) -> list """
        return []

    def get_mail(self): # real signature unknown; restored from __doc__
        """ get_mail(self) -> Goa.Mail or None """
        pass

    def get_manager(self): # real signature unknown; restored from __doc__
        """ get_manager(self) -> Goa.Manager or None """
        pass

    def get_maps(self): # real signature unknown; restored from __doc__
        """ get_maps(self) -> Goa.Maps or None """
        pass

    def get_media_server(self): # real signature unknown; restored from __doc__
        """ get_media_server(self) -> Goa.MediaServer or None """
        pass

    def get_music(self): # real signature unknown; restored from __doc__
        """ get_music(self) -> Goa.Music or None """
        pass

    def get_oauth2_based(self): # real signature unknown; restored from __doc__
        """ get_oauth2_based(self) -> Goa.OAuth2Based or None """
        pass

    def get_oauth_based(self): # real signature unknown; restored from __doc__
        """ get_oauth_based(self) -> Goa.OAuthBased or None """
        pass

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_password_based(self): # real signature unknown; restored from __doc__
        """ get_password_based(self) -> Goa.PasswordBased or None """
        pass

    def get_photos(self): # real signature unknown; restored from __doc__
        """ get_photos(self) -> Goa.Photos or None """
        pass

    def get_printers(self): # real signature unknown; restored from __doc__
        """ get_printers(self) -> Goa.Printers or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_read_later(self): # real signature unknown; restored from __doc__
        """ get_read_later(self) -> Goa.ReadLater or None """
        pass

    def get_ticketing(self): # real signature unknown; restored from __doc__
        """ get_ticketing(self) -> Goa.Ticketing or None """
        pass

    def get_todo(self): # real signature unknown; restored from __doc__
        """ get_todo(self) -> Goa.Todo or None """
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

    def new(self, object_path): # real signature unknown; restored from __doc__
        """ new(object_path:str) -> Goa.ObjectSkeleton """
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

    def remove_interface(self, interface_): # real signature unknown; restored from __doc__
        """ remove_interface(self, interface_:Gio.DBusInterfaceSkeleton) """
        pass

    def remove_interface_by_name(self, interface_name): # real signature unknown; restored from __doc__
        """ remove_interface_by_name(self, interface_name:str) """
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

    def set_account(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_account(self, interface_:Goa.Account=None) """
        pass

    def set_calendar(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_calendar(self, interface_:Goa.Calendar=None) """
        pass

    def set_chat(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_chat(self, interface_:Goa.Chat=None) """
        pass

    def set_contacts(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_contacts(self, interface_:Goa.Contacts=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_documents(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_documents(self, interface_:Goa.Documents=None) """
        pass

    def set_exchange(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_exchange(self, interface_:Goa.Exchange=None) """
        pass

    def set_files(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_files(self, interface_:Goa.Files=None) """
        pass

    def set_mail(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_mail(self, interface_:Goa.Mail=None) """
        pass

    def set_manager(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_manager(self, interface_:Goa.Manager=None) """
        pass

    def set_maps(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_maps(self, interface_:Goa.Maps=None) """
        pass

    def set_media_server(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_media_server(self, interface_:Goa.MediaServer=None) """
        pass

    def set_music(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_music(self, interface_:Goa.Music=None) """
        pass

    def set_oauth2_based(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_oauth2_based(self, interface_:Goa.OAuth2Based=None) """
        pass

    def set_oauth_based(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_oauth_based(self, interface_:Goa.OAuthBased=None) """
        pass

    def set_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ set_object_path(self, object_path:str) """
        pass

    def set_password_based(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_password_based(self, interface_:Goa.PasswordBased=None) """
        pass

    def set_photos(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_photos(self, interface_:Goa.Photos=None) """
        pass

    def set_printers(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_printers(self, interface_:Goa.Printers=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_read_later(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_read_later(self, interface_:Goa.ReadLater=None) """
        pass

    def set_ticketing(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_ticketing(self, interface_:Goa.Ticketing=None) """
        pass

    def set_todo(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_todo(self, interface_:Goa.Todo=None) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f37f4bc6d90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ObjectSkeleton), '__module__': 'gi.repository.Goa', '__gtype__': <GType GoaObjectSkeleton (94357271071632)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'set_account': gi.FunctionInfo(set_account), 'set_calendar': gi.FunctionInfo(set_calendar), 'set_chat': gi.FunctionInfo(set_chat), 'set_contacts': gi.FunctionInfo(set_contacts), 'set_documents': gi.FunctionInfo(set_documents), 'set_exchange': gi.FunctionInfo(set_exchange), 'set_files': gi.FunctionInfo(set_files), 'set_mail': gi.FunctionInfo(set_mail), 'set_manager': gi.FunctionInfo(set_manager), 'set_maps': gi.FunctionInfo(set_maps), 'set_media_server': gi.FunctionInfo(set_media_server), 'set_music': gi.FunctionInfo(set_music), 'set_oauth2_based': gi.FunctionInfo(set_oauth2_based), 'set_oauth_based': gi.FunctionInfo(set_oauth_based), 'set_password_based': gi.FunctionInfo(set_password_based), 'set_photos': gi.FunctionInfo(set_photos), 'set_printers': gi.FunctionInfo(set_printers), 'set_read_later': gi.FunctionInfo(set_read_later), 'set_ticketing': gi.FunctionInfo(set_ticketing), 'set_todo': gi.FunctionInfo(set_todo), 'parent_instance': <property object at 0x7f37f4c37400>, 'priv': <property object at 0x7f37f4c374f0>})"
    __gdoc__ = 'Object GoaObjectSkeleton\n\nSignals from GDBusObject:\n  interface-added (GDBusInterface)\n  interface-removed (GDBusInterface)\n\nSignals from GDBusObjectSkeleton:\n  authorize-method (GDBusInterfaceSkeleton, GDBusMethodInvocation) -> gboolean\n\nProperties from GDBusObjectSkeleton:\n  g-object-path -> gchararray: Object Path\n    The object path where the object is exported\n\nSignals from GDBusObject:\n  interface-added (GDBusInterface)\n  interface-removed (GDBusInterface)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GoaObjectSkeleton (94357271071632)>'
    __info__ = ObjectInfo(ObjectSkeleton)


