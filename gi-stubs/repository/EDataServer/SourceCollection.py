# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


from .SourceBackend import SourceBackend

class SourceCollection(SourceBackend):
    """
    :Constructors:
    
    ::
    
        SourceCollection(**properties)
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

    def dup_backend_name(self): # real signature unknown; restored from __doc__
        """ dup_backend_name(self) -> str """
        return ""

    def dup_calendar_url(self): # real signature unknown; restored from __doc__
        """ dup_calendar_url(self) -> str """
        return ""

    def dup_contacts_url(self): # real signature unknown; restored from __doc__
        """ dup_contacts_url(self) -> str """
        return ""

    def dup_identity(self): # real signature unknown; restored from __doc__
        """ dup_identity(self) -> str """
        return ""

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

    def get_allow_sources_rename(self): # real signature unknown; restored from __doc__
        """ get_allow_sources_rename(self) -> bool """
        return False

    def get_backend_name(self): # real signature unknown; restored from __doc__
        """ get_backend_name(self) -> str """
        return ""

    def get_calendar_enabled(self): # real signature unknown; restored from __doc__
        """ get_calendar_enabled(self) -> bool """
        return False

    def get_calendar_url(self): # real signature unknown; restored from __doc__
        """ get_calendar_url(self) -> str or None """
        return ""

    def get_contacts_enabled(self): # real signature unknown; restored from __doc__
        """ get_contacts_enabled(self) -> bool """
        return False

    def get_contacts_url(self): # real signature unknown; restored from __doc__
        """ get_contacts_url(self) -> str or None """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_identity(self): # real signature unknown; restored from __doc__
        """ get_identity(self) -> str """
        return ""

    def get_mail_enabled(self): # real signature unknown; restored from __doc__
        """ get_mail_enabled(self) -> bool """
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

    def ref_source(self): # real signature unknown; restored from __doc__
        """ ref_source(self) -> EDataServer.Source """
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

    def set_allow_sources_rename(self, allow_sources_rename): # real signature unknown; restored from __doc__
        """ set_allow_sources_rename(self, allow_sources_rename:bool) """
        pass

    def set_backend_name(self, backend_name=None): # real signature unknown; restored from __doc__
        """ set_backend_name(self, backend_name:str=None) """
        pass

    def set_calendar_enabled(self, calendar_enabled): # real signature unknown; restored from __doc__
        """ set_calendar_enabled(self, calendar_enabled:bool) """
        pass

    def set_calendar_url(self, calendar_url=None): # real signature unknown; restored from __doc__
        """ set_calendar_url(self, calendar_url:str=None) """
        pass

    def set_contacts_enabled(self, contacts_enabled): # real signature unknown; restored from __doc__
        """ set_contacts_enabled(self, contacts_enabled:bool) """
        pass

    def set_contacts_url(self, contacts_url=None): # real signature unknown; restored from __doc__
        """ set_contacts_url(self, contacts_url:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_identity(self, identity=None): # real signature unknown; restored from __doc__
        """ set_identity(self, identity:str=None) """
        pass

    def set_mail_enabled(self, mail_enabled): # real signature unknown; restored from __doc__
        """ set_mail_enabled(self, mail_enabled:bool) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f626e8dbdf0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SourceCollection), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ESourceCollection (94877537017040)>, '__doc__': None, '__gsignals__': {}, 'dup_calendar_url': gi.FunctionInfo(dup_calendar_url), 'dup_contacts_url': gi.FunctionInfo(dup_contacts_url), 'dup_identity': gi.FunctionInfo(dup_identity), 'get_allow_sources_rename': gi.FunctionInfo(get_allow_sources_rename), 'get_calendar_enabled': gi.FunctionInfo(get_calendar_enabled), 'get_calendar_url': gi.FunctionInfo(get_calendar_url), 'get_contacts_enabled': gi.FunctionInfo(get_contacts_enabled), 'get_contacts_url': gi.FunctionInfo(get_contacts_url), 'get_identity': gi.FunctionInfo(get_identity), 'get_mail_enabled': gi.FunctionInfo(get_mail_enabled), 'set_allow_sources_rename': gi.FunctionInfo(set_allow_sources_rename), 'set_calendar_enabled': gi.FunctionInfo(set_calendar_enabled), 'set_calendar_url': gi.FunctionInfo(set_calendar_url), 'set_contacts_enabled': gi.FunctionInfo(set_contacts_enabled), 'set_contacts_url': gi.FunctionInfo(set_contacts_url), 'set_identity': gi.FunctionInfo(set_identity), 'set_mail_enabled': gi.FunctionInfo(set_mail_enabled), 'parent': <property object at 0x7f626e922a40>, 'priv': <property object at 0x7f626e922b30>})"
    __gdoc__ = 'Object ESourceCollection\n\nProperties from ESourceCollection:\n  calendar-enabled -> gboolean: Calendar Enabled\n    Whether calendar resources are enabled\n  contacts-enabled -> gboolean: Contacts Enabled\n    Whether contact resources are enabled\n  identity -> gchararray: Identity\n    Uniquely identifies the account at the service provider\n  mail-enabled -> gboolean: Mail Enabled\n    Whether mail resources are enabled\n  allow-sources-rename -> gboolean: Allow Sources Rename\n    Set to TRUE when the collection source allows user rename the child sources\n  calendar-url -> gchararray: Calendar URL\n    Calendar top URL\n  contacts-url -> gchararray: Contacts URL\n    Contacts top URL\n\nProperties from ESourceBackend:\n  backend-name -> gchararray: Backend Name\n    The name of the backend handling the data source\n\nProperties from ESourceExtension:\n  source -> ESource: Source\n    The ESource being extended\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ESourceCollection (94877537017040)>'
    __info__ = ObjectInfo(SourceCollection)


