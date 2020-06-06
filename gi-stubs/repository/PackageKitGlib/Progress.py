# encoding: utf-8
# module gi.repository.PackageKitGlib
# from /usr/lib64/girepository-1.0/PackageKitGlib-1.0.typelib
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
import gobject as __gobject


class Progress(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Progress(**properties)
        new() -> PackageKitGlib.Progress
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

    def get_allow_cancel(self): # real signature unknown; restored from __doc__
        """ get_allow_cancel(self) -> bool """
        return False

    def get_caller_active(self): # real signature unknown; restored from __doc__
        """ get_caller_active(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_download_size_remaining(self): # real signature unknown; restored from __doc__
        """ get_download_size_remaining(self) -> int """
        return 0

    def get_elapsed_time(self): # real signature unknown; restored from __doc__
        """ get_elapsed_time(self) -> int """
        return 0

    def get_item_progress(self): # real signature unknown; restored from __doc__
        """ get_item_progress(self) -> PackageKitGlib.ItemProgress """
        pass

    def get_package(self): # real signature unknown; restored from __doc__
        """ get_package(self) -> PackageKitGlib.Package """
        pass

    def get_package_id(self): # real signature unknown; restored from __doc__
        """ get_package_id(self) -> str """
        return ""

    def get_percentage(self): # real signature unknown; restored from __doc__
        """ get_percentage(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remaining_time(self): # real signature unknown; restored from __doc__
        """ get_remaining_time(self) -> int """
        return 0

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> PackageKitGlib.RoleEnum """
        pass

    def get_speed(self): # real signature unknown; restored from __doc__
        """ get_speed(self) -> int """
        return 0

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> PackageKitGlib.StatusEnum """
        pass

    def get_transaction_flags(self): # real signature unknown; restored from __doc__
        """ get_transaction_flags(self) -> int """
        return 0

    def get_transaction_id(self): # real signature unknown; restored from __doc__
        """ get_transaction_id(self) -> str """
        return ""

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> int """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> PackageKitGlib.Progress """
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

    def set_allow_cancel(self, allow_cancel): # real signature unknown; restored from __doc__
        """ set_allow_cancel(self, allow_cancel:bool) -> bool """
        return False

    def set_caller_active(self, caller_active): # real signature unknown; restored from __doc__
        """ set_caller_active(self, caller_active:bool) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_download_size_remaining(self, download_size_remaining): # real signature unknown; restored from __doc__
        """ set_download_size_remaining(self, download_size_remaining:int) -> bool """
        return False

    def set_elapsed_time(self, elapsed_time): # real signature unknown; restored from __doc__
        """ set_elapsed_time(self, elapsed_time:int) -> bool """
        return False

    def set_item_progress(self, item_progress): # real signature unknown; restored from __doc__
        """ set_item_progress(self, item_progress:PackageKitGlib.ItemProgress) -> bool """
        return False

    def set_package(self, package): # real signature unknown; restored from __doc__
        """ set_package(self, package:PackageKitGlib.Package) -> bool """
        return False

    def set_package_id(self, package_id): # real signature unknown; restored from __doc__
        """ set_package_id(self, package_id:str) -> bool """
        return False

    def set_percentage(self, percentage): # real signature unknown; restored from __doc__
        """ set_percentage(self, percentage:int) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_remaining_time(self, remaining_time): # real signature unknown; restored from __doc__
        """ set_remaining_time(self, remaining_time:int) -> bool """
        return False

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:PackageKitGlib.RoleEnum) -> bool """
        return False

    def set_speed(self, speed): # real signature unknown; restored from __doc__
        """ set_speed(self, speed:int) -> bool """
        return False

    def set_status(self, status): # real signature unknown; restored from __doc__
        """ set_status(self, status:PackageKitGlib.StatusEnum) -> bool """
        return False

    def set_transaction_flags(self, transaction_flags): # real signature unknown; restored from __doc__
        """ set_transaction_flags(self, transaction_flags:int) -> bool """
        return False

    def set_transaction_id(self, transaction_id): # real signature unknown; restored from __doc__
        """ set_transaction_id(self, transaction_id:str) -> bool """
        return False

    def set_uid(self, uid): # real signature unknown; restored from __doc__
        """ set_uid(self, uid:int) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f121fb155e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Progress), '__module__': 'gi.repository.PackageKitGlib', '__gtype__': <GType PkProgress (94016447411904)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_allow_cancel': gi.FunctionInfo(get_allow_cancel), 'get_caller_active': gi.FunctionInfo(get_caller_active), 'get_download_size_remaining': gi.FunctionInfo(get_download_size_remaining), 'get_elapsed_time': gi.FunctionInfo(get_elapsed_time), 'get_item_progress': gi.FunctionInfo(get_item_progress), 'get_package': gi.FunctionInfo(get_package), 'get_package_id': gi.FunctionInfo(get_package_id), 'get_percentage': gi.FunctionInfo(get_percentage), 'get_remaining_time': gi.FunctionInfo(get_remaining_time), 'get_role': gi.FunctionInfo(get_role), 'get_speed': gi.FunctionInfo(get_speed), 'get_status': gi.FunctionInfo(get_status), 'get_transaction_flags': gi.FunctionInfo(get_transaction_flags), 'get_transaction_id': gi.FunctionInfo(get_transaction_id), 'get_uid': gi.FunctionInfo(get_uid), 'set_allow_cancel': gi.FunctionInfo(set_allow_cancel), 'set_caller_active': gi.FunctionInfo(set_caller_active), 'set_download_size_remaining': gi.FunctionInfo(set_download_size_remaining), 'set_elapsed_time': gi.FunctionInfo(set_elapsed_time), 'set_item_progress': gi.FunctionInfo(set_item_progress), 'set_package': gi.FunctionInfo(set_package), 'set_package_id': gi.FunctionInfo(set_package_id), 'set_percentage': gi.FunctionInfo(set_percentage), 'set_remaining_time': gi.FunctionInfo(set_remaining_time), 'set_role': gi.FunctionInfo(set_role), 'set_speed': gi.FunctionInfo(set_speed), 'set_status': gi.FunctionInfo(set_status), 'set_transaction_flags': gi.FunctionInfo(set_transaction_flags), 'set_transaction_id': gi.FunctionInfo(set_transaction_id), 'set_uid': gi.FunctionInfo(set_uid), 'parent': <property object at 0x7f121f8f0f90>, 'priv': <property object at 0x7f121f8f40e0>})"
    __gdoc__ = "Object PkProgress\n\nProperties from PkProgress:\n  package-id -> gchararray: package-id\n    The full package_id, e.g. 'gnome-power-manager;0.1.2;i386;fedora'\n  transaction-id -> gchararray: transaction-id\n    The transaction_id, e.g. '/892_deabbbdb_data'\n  percentage -> gint: percentage\n  allow-cancel -> gboolean: allow-cancel\n  role -> guint: role\n  status -> guint: status\n  caller-active -> gboolean: caller-active\n  elapsed-time -> guint: elapsed-time\n  remaining-time -> guint: remaining-time\n  speed -> guint: speed\n  download-size-remaining -> guint64: download-size-remaining\n  transaction-flags -> guint64: transaction-flags\n  uid -> guint: uid\n  package -> PkPackage: package\n  item-progress -> PkItemProgress: item-progress\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PkProgress (94016447411904)>'
    __info__ = ObjectInfo(Progress)


