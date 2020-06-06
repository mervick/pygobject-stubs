# encoding: utf-8
# module gi.repository.LibvirtGConfig
# from /usr/lib64/girepository-1.0/LibvirtGConfig-1.0.typelib
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


from .DomainDevice import DomainDevice

class DomainDisk(DomainDevice):
    """
    :Constructors:
    
    ::
    
        DomainDisk(**properties)
        new() -> LibvirtGConfig.DomainDisk
        new_from_xml(xml:str) -> LibvirtGConfig.DomainDisk
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

    def get_alias(self): # real signature unknown; restored from __doc__
        """ get_alias(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_disk_type(self): # real signature unknown; restored from __doc__
        """ get_disk_type(self) -> LibvirtGConfig.DomainDiskType """
        pass

    def get_driver(self): # real signature unknown; restored from __doc__
        """ get_driver(self) -> LibvirtGConfig.DomainDiskDriver """
        pass

    def get_driver_cache(self): # real signature unknown; restored from __doc__
        """ get_driver_cache(self) -> LibvirtGConfig.DomainDiskCacheType """
        pass

    def get_driver_format(self): # real signature unknown; restored from __doc__
        """ get_driver_format(self) -> LibvirtGConfig.DomainDiskFormat """
        pass

    def get_driver_name(self): # real signature unknown; restored from __doc__
        """ get_driver_name(self) -> str """
        return ""

    def get_driver_type(self): # real signature unknown; restored from __doc__
        """ get_driver_type(self) -> str """
        return ""

    def get_guest_device_type(self): # real signature unknown; restored from __doc__
        """ get_guest_device_type(self) -> LibvirtGConfig.DomainDiskGuestDeviceType """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_schema(self): # real signature unknown; restored from __doc__
        """ get_schema(self) -> str """
        return ""

    def get_snapshot_type(self): # real signature unknown; restored from __doc__
        """ get_snapshot_type(self) -> LibvirtGConfig.DomainDiskSnapshotType """
        pass

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> str """
        return ""

    def get_startup_policy(self): # real signature unknown; restored from __doc__
        """ get_startup_policy(self) -> LibvirtGConfig.DomainDiskStartupPolicy """
        pass

    def get_target_bus(self): # real signature unknown; restored from __doc__
        """ get_target_bus(self) -> LibvirtGConfig.DomainDiskBus """
        pass

    def get_target_dev(self): # real signature unknown; restored from __doc__
        """ get_target_dev(self) -> str """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> LibvirtGConfig.DomainDisk """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_xml(self, xml): # real signature unknown; restored from __doc__
        """ new_from_xml(xml:str) -> LibvirtGConfig.DomainDisk """
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

    def set_driver(self, driver=None): # real signature unknown; restored from __doc__
        """ set_driver(self, driver:LibvirtGConfig.DomainDiskDriver=None) """
        pass

    def set_driver_cache(self, cache_type): # real signature unknown; restored from __doc__
        """ set_driver_cache(self, cache_type:LibvirtGConfig.DomainDiskCacheType) """
        pass

    def set_driver_format(self, format): # real signature unknown; restored from __doc__
        """ set_driver_format(self, format:LibvirtGConfig.DomainDiskFormat) """
        pass

    def set_driver_name(self, driver_name): # real signature unknown; restored from __doc__
        """ set_driver_name(self, driver_name:str) """
        pass

    def set_driver_type(self, driver_type): # real signature unknown; restored from __doc__
        """ set_driver_type(self, driver_type:str) """
        pass

    def set_guest_device_type(self, type): # real signature unknown; restored from __doc__
        """ set_guest_device_type(self, type:LibvirtGConfig.DomainDiskGuestDeviceType) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_readonly(self, readonly): # real signature unknown; restored from __doc__
        """ set_readonly(self, readonly:bool) """
        pass

    def set_snapshot_type(self, type): # real signature unknown; restored from __doc__
        """ set_snapshot_type(self, type:LibvirtGConfig.DomainDiskSnapshotType) """
        pass

    def set_source(self, source): # real signature unknown; restored from __doc__
        """ set_source(self, source:str) """
        pass

    def set_startup_policy(self, policy): # real signature unknown; restored from __doc__
        """ set_startup_policy(self, policy:LibvirtGConfig.DomainDiskStartupPolicy) """
        pass

    def set_target_bus(self, bus): # real signature unknown; restored from __doc__
        """ set_target_bus(self, bus:LibvirtGConfig.DomainDiskBus) """
        pass

    def set_target_dev(self, dev): # real signature unknown; restored from __doc__
        """ set_target_dev(self, dev:str) """
        pass

    def set_type(self, type): # real signature unknown; restored from __doc__
        """ set_type(self, type:LibvirtGConfig.DomainDiskType) """
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

    def to_xml(self): # real signature unknown; restored from __doc__
        """ to_xml(self) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """ validate(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa8bf0cbe80>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DomainDisk), '__module__': 'gi.repository.LibvirtGConfig', '__gtype__': <GType GVirConfigDomainDisk (94643613730832)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_xml': gi.FunctionInfo(new_from_xml), 'get_disk_type': gi.FunctionInfo(get_disk_type), 'get_driver': gi.FunctionInfo(get_driver), 'get_driver_cache': gi.FunctionInfo(get_driver_cache), 'get_driver_format': gi.FunctionInfo(get_driver_format), 'get_driver_name': gi.FunctionInfo(get_driver_name), 'get_driver_type': gi.FunctionInfo(get_driver_type), 'get_guest_device_type': gi.FunctionInfo(get_guest_device_type), 'get_snapshot_type': gi.FunctionInfo(get_snapshot_type), 'get_source': gi.FunctionInfo(get_source), 'get_startup_policy': gi.FunctionInfo(get_startup_policy), 'get_target_bus': gi.FunctionInfo(get_target_bus), 'get_target_dev': gi.FunctionInfo(get_target_dev), 'set_driver': gi.FunctionInfo(set_driver), 'set_driver_cache': gi.FunctionInfo(set_driver_cache), 'set_driver_format': gi.FunctionInfo(set_driver_format), 'set_driver_name': gi.FunctionInfo(set_driver_name), 'set_driver_type': gi.FunctionInfo(set_driver_type), 'set_guest_device_type': gi.FunctionInfo(set_guest_device_type), 'set_readonly': gi.FunctionInfo(set_readonly), 'set_snapshot_type': gi.FunctionInfo(set_snapshot_type), 'set_source': gi.FunctionInfo(set_source), 'set_startup_policy': gi.FunctionInfo(set_startup_policy), 'set_target_bus': gi.FunctionInfo(set_target_bus), 'set_target_dev': gi.FunctionInfo(set_target_dev), 'set_type': gi.FunctionInfo(set_type), 'parent': <property object at 0x7fa8bf3d8180>, 'priv': <property object at 0x7fa8bf3d8270>})"
    __gdoc__ = 'Object GVirConfigDomainDisk\n\nProperties from GVirConfigObject:\n  schema -> gchararray: Schema\n    The doc RNG schema\n  node -> gpointer: XML Node\n    The XML node this config object corresponds to\n  doc -> GVirConfigXmlDoc: XML Doc\n    The XML doc this config object corresponds to\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GVirConfigDomainDisk (94643613730832)>'
    __info__ = ObjectInfo(DomainDisk)


