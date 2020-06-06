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

class Media(Entity):
    """
    :Constructors:
    
    ::
    
        Media(**properties)
        new(id:str, architecture:str) -> Libosinfo.Media
    """
    def add_install_script(self, script): # real signature unknown; restored from __doc__
        """ add_install_script(self, script:Libosinfo.InstallScript) """
        pass

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

    def create_from_location(self, location, cancellable=None): # real signature unknown; restored from __doc__
        """ create_from_location(location:str, cancellable:Gio.Cancellable=None) -> Libosinfo.Media """
        pass

    def create_from_location_async(self, location, priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_from_location_async(location:str, priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_from_location_finish(self, res): # real signature unknown; restored from __doc__
        """ create_from_location_finish(res:Gio.AsyncResult) -> Libosinfo.Media """
        pass

    def create_from_location_with_flags(self, location, cancellable=None, flags): # real signature unknown; restored from __doc__
        """ create_from_location_with_flags(location:str, cancellable:Gio.Cancellable=None, flags:int) -> Libosinfo.Media """
        pass

    def create_from_location_with_flags_async(self, location, priority, cancellable=None, callback=None, flags, user_data=None): # real signature unknown; restored from __doc__
        """ create_from_location_with_flags_async(location:str, priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, flags:int, user_data=None) """
        pass

    def create_from_location_with_flags_finish(self, res): # real signature unknown; restored from __doc__
        """ create_from_location_with_flags_finish(res:Gio.AsyncResult) -> Libosinfo.Media """
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

    def get_application_id(self): # real signature unknown; restored from __doc__
        """ get_application_id(self) -> str """
        return ""

    def get_architecture(self): # real signature unknown; restored from __doc__
        """ get_architecture(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_eject_after_install(self): # real signature unknown; restored from __doc__
        """ get_eject_after_install(self) -> bool """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_initrd_path(self): # real signature unknown; restored from __doc__
        """ get_initrd_path(self) -> str """
        return ""

    def get_installer(self): # real signature unknown; restored from __doc__
        """ get_installer(self) -> bool """
        return False

    def get_installer_reboots(self): # real signature unknown; restored from __doc__
        """ get_installer_reboots(self) -> int """
        return 0

    def get_install_script_list(self): # real signature unknown; restored from __doc__
        """ get_install_script_list(self) -> Libosinfo.InstallScriptList """
        pass

    def get_kernel_path(self): # real signature unknown; restored from __doc__
        """ get_kernel_path(self) -> str """
        return ""

    def get_languages(self): # real signature unknown; restored from __doc__
        """ get_languages(self) -> list """
        return []

    def get_live(self): # real signature unknown; restored from __doc__
        """ get_live(self) -> bool """
        return False

    def get_os(self): # real signature unknown; restored from __doc__
        """ get_os(self) -> Libosinfo.Os """
        pass

    def get_os_variants(self): # real signature unknown; restored from __doc__
        """ get_os_variants(self) -> Libosinfo.OsVariantList """
        pass

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

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_publisher_id(self): # real signature unknown; restored from __doc__
        """ get_publisher_id(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_system_id(self): # real signature unknown; restored from __doc__
        """ get_system_id(self) -> str """
        return ""

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> str """
        return ""

    def get_volume_id(self): # real signature unknown; restored from __doc__
        """ get_volume_id(self) -> str """
        return ""

    def get_volume_size(self): # real signature unknown; restored from __doc__
        """ get_volume_size(self) -> int """
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

    def is_bootable(self): # real signature unknown; restored from __doc__
        """ is_bootable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, id, architecture): # real signature unknown; restored from __doc__
        """ new(id:str, architecture:str) -> Libosinfo.Media """
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

    def supports_installer_script(self): # real signature unknown; restored from __doc__
        """ supports_installer_script(self) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f7153165dc0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Media), '__module__': 'gi.repository.Libosinfo', '__gtype__': <GType OsinfoMedia (94407636465824)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'create_from_location': gi.FunctionInfo(create_from_location), 'create_from_location_async': gi.FunctionInfo(create_from_location_async), 'create_from_location_finish': gi.FunctionInfo(create_from_location_finish), 'create_from_location_with_flags': gi.FunctionInfo(create_from_location_with_flags), 'create_from_location_with_flags_async': gi.FunctionInfo(create_from_location_with_flags_async), 'create_from_location_with_flags_finish': gi.FunctionInfo(create_from_location_with_flags_finish), 'add_install_script': gi.FunctionInfo(add_install_script), 'get_application_id': gi.FunctionInfo(get_application_id), 'get_architecture': gi.FunctionInfo(get_architecture), 'get_eject_after_install': gi.FunctionInfo(get_eject_after_install), 'get_initrd_path': gi.FunctionInfo(get_initrd_path), 'get_install_script_list': gi.FunctionInfo(get_install_script_list), 'get_installer': gi.FunctionInfo(get_installer), 'get_installer_reboots': gi.FunctionInfo(get_installer_reboots), 'get_kernel_path': gi.FunctionInfo(get_kernel_path), 'get_languages': gi.FunctionInfo(get_languages), 'get_live': gi.FunctionInfo(get_live), 'get_os': gi.FunctionInfo(get_os), 'get_os_variants': gi.FunctionInfo(get_os_variants), 'get_publisher_id': gi.FunctionInfo(get_publisher_id), 'get_system_id': gi.FunctionInfo(get_system_id), 'get_url': gi.FunctionInfo(get_url), 'get_volume_id': gi.FunctionInfo(get_volume_id), 'get_volume_size': gi.FunctionInfo(get_volume_size), 'is_bootable': gi.FunctionInfo(is_bootable), 'supports_installer_script': gi.FunctionInfo(supports_installer_script), 'parent_instance': <property object at 0x7f7153139900>, 'priv': <property object at 0x7f71531399f0>})"
    __gdoc__ = 'Object OsinfoMedia\n\nProperties from OsinfoMedia:\n  architecture -> gchararray: ARCHITECTURE\n    CPU Architecture\n  url -> gchararray: URL\n    The URL to this media\n  volume-id -> gchararray: VolumeID\n    The expected ISO9660 volume ID\n  publisher-id -> gchararray: PublisherID\n    The expected ISO9660 publisher ID\n  application-id -> gchararray: ApplicationID\n    The expected ISO9660 application ID\n  system-id -> gchararray: SystemID\n    The expected ISO9660 system ID\n  kernel-path -> gchararray: KernelPath\n    The path to the kernel image\n  initrd-path -> gchararray: InitrdPath\n    The path to the initrd image\n  installer -> gboolean: Installer\n    Media provides an installer\n  live -> gboolean: Live\n    Media can boot directly w/o installation\n  installer-reboots -> gint: InstallerReboots\n    Number of installer reboots\n  os -> OsinfoOs: Os\n    Information about the operating system on this media\n  languages -> gpointer: Languages\n    Supported languages\n  volume-size -> gint64: VolumeSize\n    Expected ISO9660 volume size, in bytes\n  eject-after-install -> gboolean: EjectAfterInstall\n    Whether the media should be ejected after the installtion process\n  installer-script -> gboolean: InstallerScript\n    Whether the media should be used for an installation using install scripts\n\nProperties from OsinfoEntity:\n  id -> gchararray: ID\n    Unique identifier\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OsinfoMedia (94407636465824)>'
    __info__ = ObjectInfo(Media)


