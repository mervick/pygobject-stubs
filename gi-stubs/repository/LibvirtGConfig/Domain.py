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


from .Object import Object

class Domain(Object):
    """
    :Constructors:
    
    ::
    
        Domain(**properties)
        new() -> LibvirtGConfig.Domain
        new_from_xml(xml:str) -> LibvirtGConfig.Domain
    """
    def add_device(self, device): # real signature unknown; restored from __doc__
        """ add_device(self, device:LibvirtGConfig.DomainDevice) """
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

    def get_clock(self): # real signature unknown; restored from __doc__
        """ get_clock(self) -> LibvirtGConfig.DomainClock """
        pass

    def get_cpu(self): # real signature unknown; restored from __doc__
        """ get_cpu(self) -> LibvirtGConfig.DomainCpu """
        pass

    def get_current_memory(self): # real signature unknown; restored from __doc__
        """ get_current_memory(self) -> int """
        return 0

    def get_custom_xml(self, ns_uri): # real signature unknown; restored from __doc__
        """ get_custom_xml(self, ns_uri:str) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_devices(self): # real signature unknown; restored from __doc__
        """ get_devices(self) -> list """
        return []

    def get_features(self): # real signature unknown; restored from __doc__
        """ get_features(self) -> list """
        return []

    def get_memory(self): # real signature unknown; restored from __doc__
        """ get_memory(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_os(self): # real signature unknown; restored from __doc__
        """ get_os(self) -> LibvirtGConfig.DomainOs """
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

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_uuid(self): # real signature unknown; restored from __doc__
        """ get_uuid(self) -> str """
        return ""

    def get_vcpus(self): # real signature unknown; restored from __doc__
        """ get_vcpus(self) -> int """
        return 0

    def get_virt_type(self): # real signature unknown; restored from __doc__
        """ get_virt_type(self) -> LibvirtGConfig.DomainVirtType """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> LibvirtGConfig.Domain """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_xml(self, xml): # real signature unknown; restored from __doc__
        """ new_from_xml(xml:str) -> LibvirtGConfig.Domain """
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

    def set_clock(self, klock=None): # real signature unknown; restored from __doc__
        """ set_clock(self, klock:LibvirtGConfig.DomainClock=None) """
        pass

    def set_cpu(self, cpu=None): # real signature unknown; restored from __doc__
        """ set_cpu(self, cpu:LibvirtGConfig.DomainCpu=None) """
        pass

    def set_current_memory(self, memory): # real signature unknown; restored from __doc__
        """ set_current_memory(self, memory:int) """
        pass

    def set_custom_xml(self, xml, ns, ns_uri): # real signature unknown; restored from __doc__
        """ set_custom_xml(self, xml:str, ns:str, ns_uri:str) -> bool """
        return False

    def set_custom_xml_ns_children(self, xml, ns, ns_uri): # real signature unknown; restored from __doc__
        """ set_custom_xml_ns_children(self, xml:str, ns:str, ns_uri:str) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description=None): # real signature unknown; restored from __doc__
        """ set_description(self, description:str=None) """
        pass

    def set_devices(self, devices): # real signature unknown; restored from __doc__
        """ set_devices(self, devices:list) """
        pass

    def set_features(self, features): # real signature unknown; restored from __doc__
        """ set_features(self, features:list) """
        pass

    def set_lifecycle(self, event, action): # real signature unknown; restored from __doc__
        """ set_lifecycle(self, event:LibvirtGConfig.DomainLifecycleEvent, action:LibvirtGConfig.DomainLifecycleAction) """
        pass

    def set_memory(self, memory): # real signature unknown; restored from __doc__
        """ set_memory(self, memory:int) """
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) """
        pass

    def set_os(self, os=None): # real signature unknown; restored from __doc__
        """ set_os(self, os:LibvirtGConfig.DomainOs=None) """
        pass

    def set_power_management(self, pm=None): # real signature unknown; restored from __doc__
        """ set_power_management(self, pm:LibvirtGConfig.DomainPowerManagement=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_seclabel(self, seclabel=None): # real signature unknown; restored from __doc__
        """ set_seclabel(self, seclabel:LibvirtGConfig.DomainSeclabel=None) """
        pass

    def set_title(self, title=None): # real signature unknown; restored from __doc__
        """ set_title(self, title:str=None) """
        pass

    def set_uuid(self, uuid=None): # real signature unknown; restored from __doc__
        """ set_uuid(self, uuid:str=None) """
        pass

    def set_vcpus(self, vcpu_count): # real signature unknown; restored from __doc__
        """ set_vcpus(self, vcpu_count:int) """
        pass

    def set_virt_type(self, type): # real signature unknown; restored from __doc__
        """ set_virt_type(self, type:LibvirtGConfig.DomainVirtType) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa8bf0cb850>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Domain), '__module__': 'gi.repository.LibvirtGConfig', '__gtype__': <GType GVirConfigDomain (94643613216048)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_xml': gi.FunctionInfo(new_from_xml), 'add_device': gi.FunctionInfo(add_device), 'get_clock': gi.FunctionInfo(get_clock), 'get_cpu': gi.FunctionInfo(get_cpu), 'get_current_memory': gi.FunctionInfo(get_current_memory), 'get_custom_xml': gi.FunctionInfo(get_custom_xml), 'get_description': gi.FunctionInfo(get_description), 'get_devices': gi.FunctionInfo(get_devices), 'get_features': gi.FunctionInfo(get_features), 'get_memory': gi.FunctionInfo(get_memory), 'get_name': gi.FunctionInfo(get_name), 'get_os': gi.FunctionInfo(get_os), 'get_title': gi.FunctionInfo(get_title), 'get_uuid': gi.FunctionInfo(get_uuid), 'get_vcpus': gi.FunctionInfo(get_vcpus), 'get_virt_type': gi.FunctionInfo(get_virt_type), 'set_clock': gi.FunctionInfo(set_clock), 'set_cpu': gi.FunctionInfo(set_cpu), 'set_current_memory': gi.FunctionInfo(set_current_memory), 'set_custom_xml': gi.FunctionInfo(set_custom_xml), 'set_custom_xml_ns_children': gi.FunctionInfo(set_custom_xml_ns_children), 'set_description': gi.FunctionInfo(set_description), 'set_devices': gi.FunctionInfo(set_devices), 'set_features': gi.FunctionInfo(set_features), 'set_lifecycle': gi.FunctionInfo(set_lifecycle), 'set_memory': gi.FunctionInfo(set_memory), 'set_name': gi.FunctionInfo(set_name), 'set_os': gi.FunctionInfo(set_os), 'set_power_management': gi.FunctionInfo(set_power_management), 'set_seclabel': gi.FunctionInfo(set_seclabel), 'set_title': gi.FunctionInfo(set_title), 'set_uuid': gi.FunctionInfo(set_uuid), 'set_vcpus': gi.FunctionInfo(set_vcpus), 'set_virt_type': gi.FunctionInfo(set_virt_type), 'parent': <property object at 0x7fa8bf3bc180>, 'priv': <property object at 0x7fa8bf3bc270>})"
    __gdoc__ = 'Object GVirConfigDomain\n\nProperties from GVirConfigDomain:\n  name -> gchararray: Name\n    Domain Name\n  uuid -> gchararray: UUID\n    Domain UUID\n  title -> gchararray: Title\n    A short description - title - of the domain\n  description -> gchararray: Description\n    Some human readable description (could be anything).\n  memory -> guint64: Memory\n    Maximum Guest Memory (in kilobytes)\n  vcpu -> guint64: Virtual CPUs\n    Maximum Number of Guest Virtual CPUs\n  features -> GStrv: Features\n    Hypervisor Features\n  current-memory -> guint64: Current memory\n    Current Guest Memory (in kilobytes)\n\nProperties from GVirConfigObject:\n  schema -> gchararray: Schema\n    The doc RNG schema\n  node -> gpointer: XML Node\n    The XML node this config object corresponds to\n  doc -> GVirConfigXmlDoc: XML Doc\n    The XML doc this config object corresponds to\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GVirConfigDomain (94643613216048)>'
    __info__ = ObjectInfo(Domain)


