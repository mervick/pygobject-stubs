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


class Results(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Results(**properties)
        new() -> PackageKitGlib.Results
    """
    def add_category(self, item): # real signature unknown; restored from __doc__
        """ add_category(self, item:PackageKitGlib.Category) -> bool """
        return False

    def add_details(self, item): # real signature unknown; restored from __doc__
        """ add_details(self, item:PackageKitGlib.Details) -> bool """
        return False

    def add_distro_upgrade(self, item): # real signature unknown; restored from __doc__
        """ add_distro_upgrade(self, item:PackageKitGlib.DistroUpgrade) -> bool """
        return False

    def add_eula_required(self, item): # real signature unknown; restored from __doc__
        """ add_eula_required(self, item:PackageKitGlib.EulaRequired) -> bool """
        return False

    def add_files(self, item): # real signature unknown; restored from __doc__
        """ add_files(self, item:PackageKitGlib.Files) -> bool """
        return False

    def add_media_change_required(self, item): # real signature unknown; restored from __doc__
        """ add_media_change_required(self, item:PackageKitGlib.MediaChangeRequired) -> bool """
        return False

    def add_package(self, item): # real signature unknown; restored from __doc__
        """ add_package(self, item:PackageKitGlib.Package) -> bool """
        return False

    def add_repo_detail(self, item): # real signature unknown; restored from __doc__
        """ add_repo_detail(self, item:PackageKitGlib.RepoDetail) -> bool """
        return False

    def add_repo_signature_required(self, item): # real signature unknown; restored from __doc__
        """ add_repo_signature_required(self, item:PackageKitGlib.RepoSignatureRequired) -> bool """
        return False

    def add_require_restart(self, item): # real signature unknown; restored from __doc__
        """ add_require_restart(self, item:PackageKitGlib.RequireRestart) -> bool """
        return False

    def add_transaction(self, item): # real signature unknown; restored from __doc__
        """ add_transaction(self, item:PackageKitGlib.TransactionPast) -> bool """
        return False

    def add_update_detail(self, item): # real signature unknown; restored from __doc__
        """ add_update_detail(self, item:PackageKitGlib.UpdateDetail) -> bool """
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

    def get_category_array(self): # real signature unknown; restored from __doc__
        """ get_category_array(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_details_array(self): # real signature unknown; restored from __doc__
        """ get_details_array(self) -> list """
        return []

    def get_distro_upgrade_array(self): # real signature unknown; restored from __doc__
        """ get_distro_upgrade_array(self) -> list """
        return []

    def get_error_code(self): # real signature unknown; restored from __doc__
        """ get_error_code(self) -> PackageKitGlib.Error """
        pass

    def get_eula_required_array(self): # real signature unknown; restored from __doc__
        """ get_eula_required_array(self) -> list """
        return []

    def get_exit_code(self): # real signature unknown; restored from __doc__
        """ get_exit_code(self) -> PackageKitGlib.ExitEnum """
        pass

    def get_files_array(self): # real signature unknown; restored from __doc__
        """ get_files_array(self) -> list """
        return []

    def get_media_change_required_array(self): # real signature unknown; restored from __doc__
        """ get_media_change_required_array(self) -> list """
        return []

    def get_package_array(self): # real signature unknown; restored from __doc__
        """ get_package_array(self) -> list """
        return []

    def get_package_sack(self): # real signature unknown; restored from __doc__
        """ get_package_sack(self) -> PackageKitGlib.PackageSack """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_repo_detail_array(self): # real signature unknown; restored from __doc__
        """ get_repo_detail_array(self) -> list """
        return []

    def get_repo_signature_required_array(self): # real signature unknown; restored from __doc__
        """ get_repo_signature_required_array(self) -> list """
        return []

    def get_require_restart_array(self): # real signature unknown; restored from __doc__
        """ get_require_restart_array(self) -> list """
        return []

    def get_require_restart_worst(self): # real signature unknown; restored from __doc__
        """ get_require_restart_worst(self) -> PackageKitGlib.RestartEnum """
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> PackageKitGlib.RoleEnum """
        pass

    def get_transaction_array(self): # real signature unknown; restored from __doc__
        """ get_transaction_array(self) -> list """
        return []

    def get_transaction_flags(self): # real signature unknown; restored from __doc__
        """ get_transaction_flags(self) -> int """
        return 0

    def get_update_detail_array(self): # real signature unknown; restored from __doc__
        """ get_update_detail_array(self) -> list """
        return []

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
        """ new() -> PackageKitGlib.Results """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_error_code(self, item): # real signature unknown; restored from __doc__
        """ set_error_code(self, item:PackageKitGlib.Error) -> bool """
        return False

    def set_exit_code(self, exit_enum): # real signature unknown; restored from __doc__
        """ set_exit_code(self, exit_enum:PackageKitGlib.ExitEnum) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:PackageKitGlib.RoleEnum) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f121f8dd0d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Results), '__module__': 'gi.repository.PackageKitGlib', '__gtype__': <GType PkResults (94016447460128)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_category': gi.FunctionInfo(add_category), 'add_details': gi.FunctionInfo(add_details), 'add_distro_upgrade': gi.FunctionInfo(add_distro_upgrade), 'add_eula_required': gi.FunctionInfo(add_eula_required), 'add_files': gi.FunctionInfo(add_files), 'add_media_change_required': gi.FunctionInfo(add_media_change_required), 'add_package': gi.FunctionInfo(add_package), 'add_repo_detail': gi.FunctionInfo(add_repo_detail), 'add_repo_signature_required': gi.FunctionInfo(add_repo_signature_required), 'add_require_restart': gi.FunctionInfo(add_require_restart), 'add_transaction': gi.FunctionInfo(add_transaction), 'add_update_detail': gi.FunctionInfo(add_update_detail), 'get_category_array': gi.FunctionInfo(get_category_array), 'get_details_array': gi.FunctionInfo(get_details_array), 'get_distro_upgrade_array': gi.FunctionInfo(get_distro_upgrade_array), 'get_error_code': gi.FunctionInfo(get_error_code), 'get_eula_required_array': gi.FunctionInfo(get_eula_required_array), 'get_exit_code': gi.FunctionInfo(get_exit_code), 'get_files_array': gi.FunctionInfo(get_files_array), 'get_media_change_required_array': gi.FunctionInfo(get_media_change_required_array), 'get_package_array': gi.FunctionInfo(get_package_array), 'get_package_sack': gi.FunctionInfo(get_package_sack), 'get_repo_detail_array': gi.FunctionInfo(get_repo_detail_array), 'get_repo_signature_required_array': gi.FunctionInfo(get_repo_signature_required_array), 'get_require_restart_array': gi.FunctionInfo(get_require_restart_array), 'get_require_restart_worst': gi.FunctionInfo(get_require_restart_worst), 'get_role': gi.FunctionInfo(get_role), 'get_transaction_array': gi.FunctionInfo(get_transaction_array), 'get_transaction_flags': gi.FunctionInfo(get_transaction_flags), 'get_update_detail_array': gi.FunctionInfo(get_update_detail_array), 'set_error_code': gi.FunctionInfo(set_error_code), 'set_exit_code': gi.FunctionInfo(set_exit_code), 'set_role': gi.FunctionInfo(set_role), 'parent': <property object at 0x7f121f8fb950>, 'priv': <property object at 0x7f121f8fba40>})"
    __gdoc__ = 'Object PkResults\n\nProperties from PkResults:\n  role -> PkRoleEnum: role\n  transaction-flags -> guint64: transaction-flags\n  inputs -> guint: inputs\n  progress -> PkProgress: progress\n    The progress instance\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PkResults (94016447460128)>'
    __info__ = ObjectInfo(Results)


