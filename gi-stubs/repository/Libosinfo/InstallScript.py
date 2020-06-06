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

class InstallScript(Entity):
    """
    :Constructors:
    
    ::
    
        InstallScript(**properties)
        new(id:str) -> Libosinfo.InstallScript
        new_data(id:str, profile:str, templateData:str) -> Libosinfo.InstallScript
        new_uri(id:str, profile:str, templateUri:str) -> Libosinfo.InstallScript
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

    def generate(self, os, config, cancellable=None): # real signature unknown; restored from __doc__
        """ generate(self, os:Libosinfo.Os, config:Libosinfo.InstallConfig, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def generate_async(self, os, config, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ generate_async(self, os:Libosinfo.Os, config:Libosinfo.InstallConfig, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def generate_command_line(self, os, config): # real signature unknown; restored from __doc__
        """ generate_command_line(self, os:Libosinfo.Os, config:Libosinfo.InstallConfig) -> str """
        return ""

    def generate_command_line_for_media(self, media, config): # real signature unknown; restored from __doc__
        """ generate_command_line_for_media(self, media:Libosinfo.Media, config:Libosinfo.InstallConfig) -> str """
        return ""

    def generate_command_line_for_tree(self, tree, config): # real signature unknown; restored from __doc__
        """ generate_command_line_for_tree(self, tree:Libosinfo.Tree, config:Libosinfo.InstallConfig) -> str """
        return ""

    def generate_finish(self, res): # real signature unknown; restored from __doc__
        """ generate_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def generate_for_media(self, media, config, cancellable=None): # real signature unknown; restored from __doc__
        """ generate_for_media(self, media:Libosinfo.Media, config:Libosinfo.InstallConfig, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def generate_for_media_async(self, media, config, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ generate_for_media_async(self, media:Libosinfo.Media, config:Libosinfo.InstallConfig, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def generate_for_media_finish(self, res): # real signature unknown; restored from __doc__
        """ generate_for_media_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def generate_for_tree(self, tree, config, cancellable=None): # real signature unknown; restored from __doc__
        """ generate_for_tree(self, tree:Libosinfo.Tree, config:Libosinfo.InstallConfig, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def generate_for_tree_async(self, tree, config, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ generate_for_tree_async(self, tree:Libosinfo.Tree, config:Libosinfo.InstallConfig, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def generate_for_tree_finish(self, res): # real signature unknown; restored from __doc__
        """ generate_for_tree_finish(self, res:Gio.AsyncResult) -> str """
        return ""

    def generate_output(self, os, config, output_dir, cancellable=None): # real signature unknown; restored from __doc__
        """ generate_output(self, os:Libosinfo.Os, config:Libosinfo.InstallConfig, output_dir:Gio.File, cancellable:Gio.Cancellable=None) -> Gio.File """
        pass

    def generate_output_async(self, os, config, output_dir, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ generate_output_async(self, os:Libosinfo.Os, config:Libosinfo.InstallConfig, output_dir:Gio.File, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def generate_output_finish(self, res): # real signature unknown; restored from __doc__
        """ generate_output_finish(self, res:Gio.AsyncResult) -> Gio.File """
        pass

    def generate_output_for_media(self, media, config, output_dir, cancellable=None): # real signature unknown; restored from __doc__
        """ generate_output_for_media(self, media:Libosinfo.Media, config:Libosinfo.InstallConfig, output_dir:Gio.File, cancellable:Gio.Cancellable=None) -> Gio.File """
        pass

    def generate_output_for_media_async(self, media, config, output_dir, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ generate_output_for_media_async(self, media:Libosinfo.Media, config:Libosinfo.InstallConfig, output_dir:Gio.File, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def generate_output_for_media_finish(self, res): # real signature unknown; restored from __doc__
        """ generate_output_for_media_finish(self, res:Gio.AsyncResult) -> Gio.File """
        pass

    def generate_output_for_tree(self, tree, config, output_dir, cancellable=None): # real signature unknown; restored from __doc__
        """ generate_output_for_tree(self, tree:Libosinfo.Tree, config:Libosinfo.InstallConfig, output_dir:Gio.File, cancellable:Gio.Cancellable=None) -> Gio.File """
        pass

    def generate_output_for_tree_async(self, tree, config, output_dir, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ generate_output_for_tree_async(self, tree:Libosinfo.Tree, config:Libosinfo.InstallConfig, output_dir:Gio.File, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def generate_output_for_tree_finish(self, res): # real signature unknown; restored from __doc__
        """ generate_output_for_tree_finish(self, res:Gio.AsyncResult) -> Gio.File """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_avatar_format(self): # real signature unknown; restored from __doc__
        """ get_avatar_format(self) -> Libosinfo.AvatarFormat """
        pass

    def get_can_post_install_drivers(self): # real signature unknown; restored from __doc__
        """ get_can_post_install_drivers(self) -> bool """
        return False

    def get_can_pre_install_drivers(self): # real signature unknown; restored from __doc__
        """ get_can_pre_install_drivers(self) -> bool """
        return False

    def get_config_param(self, name): # real signature unknown; restored from __doc__
        """ get_config_param(self, name:str) -> Libosinfo.InstallConfigParam """
        pass

    def get_config_params(self): # real signature unknown; restored from __doc__
        """ get_config_params(self) -> Libosinfo.InstallConfigParamList """
        pass

    def get_config_param_list(self): # real signature unknown; restored from __doc__
        """ get_config_param_list(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_expected_filename(self): # real signature unknown; restored from __doc__
        """ get_expected_filename(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_injection_methods(self): # real signature unknown; restored from __doc__
        """ get_injection_methods(self) -> Libosinfo.InstallScriptInjectionMethod """
        pass

    def get_installation_source(self): # real signature unknown; restored from __doc__
        """ get_installation_source(self) -> Libosinfo.InstallScriptInstallationSource """
        pass

    def get_needs_internet(self): # real signature unknown; restored from __doc__
        """ get_needs_internet(self) -> bool """
        return False

    def get_output_filename(self): # real signature unknown; restored from __doc__
        """ get_output_filename(self) -> str """
        return ""

    def get_output_prefix(self): # real signature unknown; restored from __doc__
        """ get_output_prefix(self) -> str """
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

    def get_path_format(self): # real signature unknown; restored from __doc__
        """ get_path_format(self) -> Libosinfo.PathFormat """
        pass

    def get_post_install_drivers_signing_req(self): # real signature unknown; restored from __doc__
        """ get_post_install_drivers_signing_req(self) -> Libosinfo.DeviceDriverSigningReq """
        pass

    def get_preferred_injection_method(self): # real signature unknown; restored from __doc__
        """ get_preferred_injection_method(self) -> Libosinfo.InstallScriptInjectionMethod """
        pass

    def get_pre_install_drivers_signing_req(self): # real signature unknown; restored from __doc__
        """ get_pre_install_drivers_signing_req(self) -> Libosinfo.DeviceDriverSigningReq """
        pass

    def get_product_key_format(self): # real signature unknown; restored from __doc__
        """ get_product_key_format(self) -> str """
        return ""

    def get_profile(self): # real signature unknown; restored from __doc__
        """ get_profile(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_template_data(self): # real signature unknown; restored from __doc__
        """ get_template_data(self) -> str """
        return ""

    def get_template_uri(self): # real signature unknown; restored from __doc__
        """ get_template_uri(self) -> str """
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

    def has_config_param(self, config_param): # real signature unknown; restored from __doc__
        """ has_config_param(self, config_param:Libosinfo.InstallConfigParam) -> bool """
        return False

    def has_config_param_name(self, name): # real signature unknown; restored from __doc__
        """ has_config_param_name(self, name:str) -> bool """
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

    def new(self, id): # real signature unknown; restored from __doc__
        """ new(id:str) -> Libosinfo.InstallScript """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_data(self, id, profile, templateData): # real signature unknown; restored from __doc__
        """ new_data(id:str, profile:str, templateData:str) -> Libosinfo.InstallScript """
        pass

    def new_uri(self, id, profile, templateUri): # real signature unknown; restored from __doc__
        """ new_uri(id:str, profile:str, templateUri:str) -> Libosinfo.InstallScript """
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

    def set_installation_source(self, source): # real signature unknown; restored from __doc__
        """ set_installation_source(self, source:Libosinfo.InstallScriptInstallationSource) """
        pass

    def set_output_prefix(self, prefix): # real signature unknown; restored from __doc__
        """ set_output_prefix(self, prefix:str) """
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

    def set_preferred_injection_method(self, method): # real signature unknown; restored from __doc__
        """ set_preferred_injection_method(self, method:Libosinfo.InstallScriptInjectionMethod) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f715306c580>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(InstallScript), '__module__': 'gi.repository.Libosinfo', '__gtype__': <GType OsinfoInstallScript (94407636378320)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_data': gi.FunctionInfo(new_data), 'new_uri': gi.FunctionInfo(new_uri), 'generate': gi.FunctionInfo(generate), 'generate_async': gi.FunctionInfo(generate_async), 'generate_command_line': gi.FunctionInfo(generate_command_line), 'generate_command_line_for_media': gi.FunctionInfo(generate_command_line_for_media), 'generate_command_line_for_tree': gi.FunctionInfo(generate_command_line_for_tree), 'generate_finish': gi.FunctionInfo(generate_finish), 'generate_for_media': gi.FunctionInfo(generate_for_media), 'generate_for_media_async': gi.FunctionInfo(generate_for_media_async), 'generate_for_media_finish': gi.FunctionInfo(generate_for_media_finish), 'generate_for_tree': gi.FunctionInfo(generate_for_tree), 'generate_for_tree_async': gi.FunctionInfo(generate_for_tree_async), 'generate_for_tree_finish': gi.FunctionInfo(generate_for_tree_finish), 'generate_output': gi.FunctionInfo(generate_output), 'generate_output_async': gi.FunctionInfo(generate_output_async), 'generate_output_finish': gi.FunctionInfo(generate_output_finish), 'generate_output_for_media': gi.FunctionInfo(generate_output_for_media), 'generate_output_for_media_async': gi.FunctionInfo(generate_output_for_media_async), 'generate_output_for_media_finish': gi.FunctionInfo(generate_output_for_media_finish), 'generate_output_for_tree': gi.FunctionInfo(generate_output_for_tree), 'generate_output_for_tree_async': gi.FunctionInfo(generate_output_for_tree_async), 'generate_output_for_tree_finish': gi.FunctionInfo(generate_output_for_tree_finish), 'get_avatar_format': gi.FunctionInfo(get_avatar_format), 'get_can_post_install_drivers': gi.FunctionInfo(get_can_post_install_drivers), 'get_can_pre_install_drivers': gi.FunctionInfo(get_can_pre_install_drivers), 'get_config_param': gi.FunctionInfo(get_config_param), 'get_config_param_list': gi.FunctionInfo(get_config_param_list), 'get_config_params': gi.FunctionInfo(get_config_params), 'get_expected_filename': gi.FunctionInfo(get_expected_filename), 'get_injection_methods': gi.FunctionInfo(get_injection_methods), 'get_installation_source': gi.FunctionInfo(get_installation_source), 'get_needs_internet': gi.FunctionInfo(get_needs_internet), 'get_output_filename': gi.FunctionInfo(get_output_filename), 'get_output_prefix': gi.FunctionInfo(get_output_prefix), 'get_path_format': gi.FunctionInfo(get_path_format), 'get_post_install_drivers_signing_req': gi.FunctionInfo(get_post_install_drivers_signing_req), 'get_pre_install_drivers_signing_req': gi.FunctionInfo(get_pre_install_drivers_signing_req), 'get_preferred_injection_method': gi.FunctionInfo(get_preferred_injection_method), 'get_product_key_format': gi.FunctionInfo(get_product_key_format), 'get_profile': gi.FunctionInfo(get_profile), 'get_template_data': gi.FunctionInfo(get_template_data), 'get_template_uri': gi.FunctionInfo(get_template_uri), 'has_config_param': gi.FunctionInfo(has_config_param), 'has_config_param_name': gi.FunctionInfo(has_config_param_name), 'set_installation_source': gi.FunctionInfo(set_installation_source), 'set_output_prefix': gi.FunctionInfo(set_output_prefix), 'set_preferred_injection_method': gi.FunctionInfo(set_preferred_injection_method), 'parent_instance': <property object at 0x7f7153134a90>, 'priv': <property object at 0x7f7153134b80>})"
    __gdoc__ = 'Object OsinfoInstallScript\n\nProperties from OsinfoInstallScript:\n  template-uri -> gchararray: TemplateURI\n    URI for install script template\n  template-data -> gchararray: TemplateData\n    Data for install script template\n  profile -> gchararray: Profile\n    Install script profile name\n  product-key-format -> gchararray: Product Key Format\n    Product key format mask\n  path-format -> OsinfoPathFormat: Path Format\n    Expected path format\n  avatar-format -> OsinfoAvatarFormat: Avatar Format\n    Expected avatar format\n  preferred-injection-method -> OsinfoInstallScriptInjectionMethod: Preferred Injection Method\n    The preferred injection method\n  installation-source -> OsinfoInstallScriptInstallationSource: Installation Source\n    The installation source to be used\n\nProperties from OsinfoEntity:\n  id -> gchararray: ID\n    Unique identifier\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OsinfoInstallScript (94407636378320)>'
    __info__ = ObjectInfo(InstallScript)


