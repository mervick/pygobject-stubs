# encoding: utf-8
# module gi.repository.Libosinfo
# from /usr/lib64/girepository-1.0/Libosinfo-1.0.typelib
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


from .Entity import Entity

class InstallConfig(Entity):
    """
    :Constructors:
    
    ::
    
        InstallConfig(**properties)
        new(id:str) -> Libosinfo.InstallConfig
    """
    def add_param(self, key, value): # real signature unknown; restored from __doc__
        """ add_param(self, key:str, value:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_param(self, key): # real signature unknown; restored from __doc__
        """ clear_param(self, key:str) """
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

    def get_admin_password(self): # real signature unknown; restored from __doc__
        """ get_admin_password(self) -> str """
        return ""

    def get_avatar_disk(self): # real signature unknown; restored from __doc__
        """ get_avatar_disk(self) -> str """
        return ""

    def get_avatar_location(self): # real signature unknown; restored from __doc__
        """ get_avatar_location(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_driver_signing(self): # real signature unknown; restored from __doc__
        """ get_driver_signing(self) -> bool """
        return False

    def get_hardware_arch(self): # real signature unknown; restored from __doc__
        """ get_hardware_arch(self) -> str """
        return ""

    def get_hostname(self): # real signature unknown; restored from __doc__
        """ get_hostname(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_installation_url(self): # real signature unknown; restored from __doc__
        """ get_installation_url(self) -> str """
        return ""

    def get_l10n_keyboard(self): # real signature unknown; restored from __doc__
        """ get_l10n_keyboard(self) -> str """
        return ""

    def get_l10n_language(self): # real signature unknown; restored from __doc__
        """ get_l10n_language(self) -> str """
        return ""

    def get_l10n_timezone(self): # real signature unknown; restored from __doc__
        """ get_l10n_timezone(self) -> str """
        return ""

    def get_param_keys(self): # real signature unknown; restored from __doc__
        """ get_param_keys(self) -> list """
        return []

    def get_param_value(self, key): # real signature unknown; restored from __doc__
        """ get_param_value(self, key:str) -> str """
        return ""

    def get_param_value_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_param_value_boolean(self, key:str) -> bool """
        return False

    def get_param_value_boolean_with_default(self, key, default_value): # real signature unknown; restored from __doc__
        """ get_param_value_boolean_with_default(self, key:str, default_value:bool) -> bool """
        return False

    def get_param_value_enum(self, key, enum_type, default_value): # real signature unknown; restored from __doc__
        """ get_param_value_enum(self, key:str, enum_type:GType, default_value:int) -> int """
        return 0

    def get_param_value_int64(self, key): # real signature unknown; restored from __doc__
        """ get_param_value_int64(self, key:str) -> int """
        return 0

    def get_param_value_int64_with_default(self, key, default_value): # real signature unknown; restored from __doc__
        """ get_param_value_int64_with_default(self, key:str, default_value:int) -> int """
        return 0

    def get_param_value_list(self, key): # real signature unknown; restored from __doc__
        """ get_param_value_list(self, key:str) -> list """
        return []

    def get_post_install_drivers_disk(self): # real signature unknown; restored from __doc__
        """ get_post_install_drivers_disk(self) -> str """
        return ""

    def get_post_install_drivers_location(self): # real signature unknown; restored from __doc__
        """ get_post_install_drivers_location(self) -> str """
        return ""

    def get_pre_install_drivers_disk(self): # real signature unknown; restored from __doc__
        """ get_pre_install_drivers_disk(self) -> str """
        return ""

    def get_pre_install_drivers_location(self): # real signature unknown; restored from __doc__
        """ get_pre_install_drivers_location(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_reg_login(self): # real signature unknown; restored from __doc__
        """ get_reg_login(self) -> str """
        return ""

    def get_reg_password(self): # real signature unknown; restored from __doc__
        """ get_reg_password(self) -> str """
        return ""

    def get_reg_product_key(self): # real signature unknown; restored from __doc__
        """ get_reg_product_key(self) -> str """
        return ""

    def get_script_disk(self): # real signature unknown; restored from __doc__
        """ get_script_disk(self) -> str """
        return ""

    def get_target_disk(self): # real signature unknown; restored from __doc__
        """ get_target_disk(self) -> str """
        return ""

    def get_user_administrator(self): # real signature unknown; restored from __doc__
        """ get_user_administrator(self) -> bool """
        return False

    def get_user_autologin(self): # real signature unknown; restored from __doc__
        """ get_user_autologin(self) -> bool """
        return False

    def get_user_login(self): # real signature unknown; restored from __doc__
        """ get_user_login(self) -> str """
        return ""

    def get_user_password(self): # real signature unknown; restored from __doc__
        """ get_user_password(self) -> str """
        return ""

    def get_user_realname(self): # real signature unknown; restored from __doc__
        """ get_user_realname(self) -> str """
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

    def new(self, id): # real signature unknown; restored from __doc__
        """ new(id:str) -> Libosinfo.InstallConfig """
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

    def set_admin_password(self, password): # real signature unknown; restored from __doc__
        """ set_admin_password(self, password:str) """
        pass

    def set_avatar_disk(self, disk): # real signature unknown; restored from __doc__
        """ set_avatar_disk(self, disk:str) """
        pass

    def set_avatar_location(self, location): # real signature unknown; restored from __doc__
        """ set_avatar_location(self, location:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_driver_signing(self, signing): # real signature unknown; restored from __doc__
        """ set_driver_signing(self, signing:bool) """
        pass

    def set_hardware_arch(self, arch): # real signature unknown; restored from __doc__
        """ set_hardware_arch(self, arch:str) """
        pass

    def set_hostname(self, hostname): # real signature unknown; restored from __doc__
        """ set_hostname(self, hostname:str) """
        pass

    def set_installation_url(self, url): # real signature unknown; restored from __doc__
        """ set_installation_url(self, url:str) """
        pass

    def set_l10n_keyboard(self, keyboard): # real signature unknown; restored from __doc__
        """ set_l10n_keyboard(self, keyboard:str) """
        pass

    def set_l10n_language(self, language): # real signature unknown; restored from __doc__
        """ set_l10n_language(self, language:str) """
        pass

    def set_l10n_timezone(self, timezone): # real signature unknown; restored from __doc__
        """ set_l10n_timezone(self, timezone:str) """
        pass

    def set_param(self, key, value): # real signature unknown; restored from __doc__
        """ set_param(self, key:str, value:str) """
        pass

    def set_param_boolean(self, key, value): # real signature unknown; restored from __doc__
        """ set_param_boolean(self, key:str, value:bool) """
        pass

    def set_param_enum(self, key, value, enum_type): # real signature unknown; restored from __doc__
        """ set_param_enum(self, key:str, value:int, enum_type:GType) """
        pass

    def set_param_int64(self, key, value): # real signature unknown; restored from __doc__
        """ set_param_int64(self, key:str, value:int) """
        pass

    def set_post_install_drivers_disk(self, disk): # real signature unknown; restored from __doc__
        """ set_post_install_drivers_disk(self, disk:str) """
        pass

    def set_post_install_drivers_location(self, location): # real signature unknown; restored from __doc__
        """ set_post_install_drivers_location(self, location:str) """
        pass

    def set_pre_install_drivers_disk(self, disk): # real signature unknown; restored from __doc__
        """ set_pre_install_drivers_disk(self, disk:str) """
        pass

    def set_pre_install_drivers_location(self, location): # real signature unknown; restored from __doc__
        """ set_pre_install_drivers_location(self, location:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_reg_login(self, name): # real signature unknown; restored from __doc__
        """ set_reg_login(self, name:str) """
        pass

    def set_reg_password(self, password): # real signature unknown; restored from __doc__
        """ set_reg_password(self, password:str) """
        pass

    def set_reg_product_key(self, key): # real signature unknown; restored from __doc__
        """ set_reg_product_key(self, key:str) """
        pass

    def set_script_disk(self, disk): # real signature unknown; restored from __doc__
        """ set_script_disk(self, disk:str) """
        pass

    def set_target_disk(self, disk): # real signature unknown; restored from __doc__
        """ set_target_disk(self, disk:str) """
        pass

    def set_user_administrator(self, admin): # real signature unknown; restored from __doc__
        """ set_user_administrator(self, admin:bool) """
        pass

    def set_user_autologin(self, autologin): # real signature unknown; restored from __doc__
        """ set_user_autologin(self, autologin:bool) """
        pass

    def set_user_login(self, username): # real signature unknown; restored from __doc__
        """ set_user_login(self, username:str) """
        pass

    def set_user_password(self, password): # real signature unknown; restored from __doc__
        """ set_user_password(self, password:str) """
        pass

    def set_user_realname(self, name): # real signature unknown; restored from __doc__
        """ set_user_realname(self, name:str) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f715306ca90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(InstallConfig), '__module__': 'gi.repository.Libosinfo', '__gtype__': <GType OsinfoInstallConfig (94407636349856)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_admin_password': gi.FunctionInfo(get_admin_password), 'get_avatar_disk': gi.FunctionInfo(get_avatar_disk), 'get_avatar_location': gi.FunctionInfo(get_avatar_location), 'get_driver_signing': gi.FunctionInfo(get_driver_signing), 'get_hardware_arch': gi.FunctionInfo(get_hardware_arch), 'get_hostname': gi.FunctionInfo(get_hostname), 'get_installation_url': gi.FunctionInfo(get_installation_url), 'get_l10n_keyboard': gi.FunctionInfo(get_l10n_keyboard), 'get_l10n_language': gi.FunctionInfo(get_l10n_language), 'get_l10n_timezone': gi.FunctionInfo(get_l10n_timezone), 'get_post_install_drivers_disk': gi.FunctionInfo(get_post_install_drivers_disk), 'get_post_install_drivers_location': gi.FunctionInfo(get_post_install_drivers_location), 'get_pre_install_drivers_disk': gi.FunctionInfo(get_pre_install_drivers_disk), 'get_pre_install_drivers_location': gi.FunctionInfo(get_pre_install_drivers_location), 'get_reg_login': gi.FunctionInfo(get_reg_login), 'get_reg_password': gi.FunctionInfo(get_reg_password), 'get_reg_product_key': gi.FunctionInfo(get_reg_product_key), 'get_script_disk': gi.FunctionInfo(get_script_disk), 'get_target_disk': gi.FunctionInfo(get_target_disk), 'get_user_administrator': gi.FunctionInfo(get_user_administrator), 'get_user_autologin': gi.FunctionInfo(get_user_autologin), 'get_user_login': gi.FunctionInfo(get_user_login), 'get_user_password': gi.FunctionInfo(get_user_password), 'get_user_realname': gi.FunctionInfo(get_user_realname), 'set_admin_password': gi.FunctionInfo(set_admin_password), 'set_avatar_disk': gi.FunctionInfo(set_avatar_disk), 'set_avatar_location': gi.FunctionInfo(set_avatar_location), 'set_driver_signing': gi.FunctionInfo(set_driver_signing), 'set_hardware_arch': gi.FunctionInfo(set_hardware_arch), 'set_hostname': gi.FunctionInfo(set_hostname), 'set_installation_url': gi.FunctionInfo(set_installation_url), 'set_l10n_keyboard': gi.FunctionInfo(set_l10n_keyboard), 'set_l10n_language': gi.FunctionInfo(set_l10n_language), 'set_l10n_timezone': gi.FunctionInfo(set_l10n_timezone), 'set_post_install_drivers_disk': gi.FunctionInfo(set_post_install_drivers_disk), 'set_post_install_drivers_location': gi.FunctionInfo(set_post_install_drivers_location), 'set_pre_install_drivers_disk': gi.FunctionInfo(set_pre_install_drivers_disk), 'set_pre_install_drivers_location': gi.FunctionInfo(set_pre_install_drivers_location), 'set_reg_login': gi.FunctionInfo(set_reg_login), 'set_reg_password': gi.FunctionInfo(set_reg_password), 'set_reg_product_key': gi.FunctionInfo(set_reg_product_key), 'set_script_disk': gi.FunctionInfo(set_script_disk), 'set_target_disk': gi.FunctionInfo(set_target_disk), 'set_user_administrator': gi.FunctionInfo(set_user_administrator), 'set_user_autologin': gi.FunctionInfo(set_user_autologin), 'set_user_login': gi.FunctionInfo(set_user_login), 'set_user_password': gi.FunctionInfo(set_user_password), 'set_user_realname': gi.FunctionInfo(set_user_realname), 'parent_instance': <property object at 0x7f715312cc70>, 'priv': <property object at 0x7f715312cd60>})"
    __gdoc__ = 'Object OsinfoInstallConfig\n\nProperties from OsinfoEntity:\n  id -> gchararray: ID\n    Unique identifier\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OsinfoInstallConfig (94407636349856)>'
    __info__ = ObjectInfo(InstallConfig)


