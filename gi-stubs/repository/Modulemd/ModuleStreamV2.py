# encoding: utf-8
# module gi.repository.Modulemd
# from /usr/lib64/girepository-1.0/Modulemd-1.0.typelib
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


from .ModuleStream import ModuleStream

class ModuleStreamV2(ModuleStream):
    """
    :Constructors:
    
    ::
    
        ModuleStreamV2(**properties)
        new(module_name:str=None, module_stream:str=None) -> Modulemd.ModuleStreamV2
    """
    def add_component(self, component): # real signature unknown; restored from __doc__
        """ add_component(self, component:Modulemd.Component) """
        pass

    def add_content_license(self, license): # real signature unknown; restored from __doc__
        """ add_content_license(self, license:str) """
        pass

    def add_dependencies(self, deps): # real signature unknown; restored from __doc__
        """ add_dependencies(self, deps:Modulemd.Dependencies) """
        pass

    def add_module_license(self, license): # real signature unknown; restored from __doc__
        """ add_module_license(self, license:str) """
        pass

    def add_profile(self, profile): # real signature unknown; restored from __doc__
        """ add_profile(self, profile:Modulemd.Profile) """
        pass

    def add_rpm_api(self, rpm): # real signature unknown; restored from __doc__
        """ add_rpm_api(self, rpm:str) """
        pass

    def add_rpm_artifact(self, nevr): # real signature unknown; restored from __doc__
        """ add_rpm_artifact(self, nevr:str) """
        pass

    def add_rpm_filter(self, rpm): # real signature unknown; restored from __doc__
        """ add_rpm_filter(self, rpm:str) """
        pass

    def add_servicelevel(self, servicelevel): # real signature unknown; restored from __doc__
        """ add_servicelevel(self, servicelevel:Modulemd.ServiceLevel) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def build_depends_on_stream(self, module_name, stream_name): # real signature unknown; restored from __doc__
        """ build_depends_on_stream(self, module_name:str, stream_name:str) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_content_licenses(self): # real signature unknown; restored from __doc__
        """ clear_content_licenses(self) """
        pass

    def clear_dependencies(self): # real signature unknown; restored from __doc__
        """ clear_dependencies(self) """
        pass

    def clear_module_components(self): # real signature unknown; restored from __doc__
        """ clear_module_components(self) """
        pass

    def clear_module_licenses(self): # real signature unknown; restored from __doc__
        """ clear_module_licenses(self) """
        pass

    def clear_profiles(self): # real signature unknown; restored from __doc__
        """ clear_profiles(self) """
        pass

    def clear_rpm_api(self): # real signature unknown; restored from __doc__
        """ clear_rpm_api(self) """
        pass

    def clear_rpm_artifacts(self): # real signature unknown; restored from __doc__
        """ clear_rpm_artifacts(self) """
        pass

    def clear_rpm_components(self): # real signature unknown; restored from __doc__
        """ clear_rpm_components(self) """
        pass

    def clear_rpm_filters(self): # real signature unknown; restored from __doc__
        """ clear_rpm_filters(self) """
        pass

    def clear_servicelevels(self): # real signature unknown; restored from __doc__
        """ clear_servicelevels(self) """
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

    def copy(self, module_name=None, module_stream=None): # real signature unknown; restored from __doc__
        """ copy(self, module_name:str=None, module_stream:str=None) -> Modulemd.ModuleStream """
        pass

    def depends_on_stream(self, module_name, stream_name): # real signature unknown; restored from __doc__
        """ depends_on_stream(self, module_name:str, stream_name:str) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_build_depends_on_stream(self, *args, **kwargs): # real signature unknown
        """ build_depends_on_stream(self, module_name:str, stream_name:str) -> bool """
        pass

    def do_copy(self, *args, **kwargs): # real signature unknown
        """ copy(self, module_name:str=None, module_stream:str=None) -> Modulemd.ModuleStream """
        pass

    def do_depends_on_stream(self, *args, **kwargs): # real signature unknown
        """ depends_on_stream(self, module_name:str, stream_name:str) -> bool """
        pass

    def do_equals(self, *args, **kwargs): # real signature unknown
        """ equals(self, self_2:Modulemd.ModuleStream) -> bool """
        pass

    def do_get_mdversion(self, *args, **kwargs): # real signature unknown
        """ get_mdversion(self) -> int """
        pass

    def do_validate(self, *args, **kwargs): # real signature unknown
        """ validate(self) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equals(self, self_2): # real signature unknown; restored from __doc__
        """ equals(self, self_2:Modulemd.ModuleStream) -> bool """
        return False

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

    def get_arch(self): # real signature unknown; restored from __doc__
        """ get_arch(self) -> str """
        return ""

    def get_buildopts(self): # real signature unknown; restored from __doc__
        """ get_buildopts(self) -> Modulemd.Buildopts """
        pass

    def get_community(self): # real signature unknown; restored from __doc__
        """ get_community(self) -> str """
        return ""

    def get_content_licenses(self): # real signature unknown; restored from __doc__
        """ get_content_licenses(self) -> list """
        return []

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dependencies(self): # real signature unknown; restored from __doc__
        """ get_dependencies(self) -> list """
        return []

    def get_description(self, locale=None): # real signature unknown; restored from __doc__
        """ get_description(self, locale:str=None) -> str """
        return ""

    def get_documentation(self): # real signature unknown; restored from __doc__
        """ get_documentation(self) -> str """
        return ""

    def get_mdversion(self): # real signature unknown; restored from __doc__
        """ get_mdversion(self) -> int """
        return 0

    def get_module_component(self, component_name): # real signature unknown; restored from __doc__
        """ get_module_component(self, component_name:str) -> Modulemd.ComponentModule """
        pass

    def get_module_component_names(self): # real signature unknown; restored from __doc__
        """ get_module_component_names(self) -> list """
        return []

    def get_module_licenses(self): # real signature unknown; restored from __doc__
        """ get_module_licenses(self) -> list """
        return []

    def get_module_name(self): # real signature unknown; restored from __doc__
        """ get_module_name(self) -> str """
        return ""

    def get_nsvc(self): # real signature unknown; restored from __doc__
        """ get_nsvc(self) -> str """
        return ""

    def get_NSVCA(self): # real signature unknown; restored from __doc__
        """ get_NSVCA(self) -> str """
        return ""

    def get_profile(self, profile_name): # real signature unknown; restored from __doc__
        """ get_profile(self, profile_name:str) -> Modulemd.Profile """
        pass

    def get_profile_names(self): # real signature unknown; restored from __doc__
        """ get_profile_names(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rpm_api(self): # real signature unknown; restored from __doc__
        """ get_rpm_api(self) -> list """
        return []

    def get_rpm_artifacts(self): # real signature unknown; restored from __doc__
        """ get_rpm_artifacts(self) -> list """
        return []

    def get_rpm_artifact_map_entry(self, digest, checksum): # real signature unknown; restored from __doc__
        """ get_rpm_artifact_map_entry(self, digest:str, checksum:str) -> Modulemd.RpmMapEntry """
        pass

    def get_rpm_component(self, component_name): # real signature unknown; restored from __doc__
        """ get_rpm_component(self, component_name:str) -> Modulemd.ComponentRpm """
        pass

    def get_rpm_component_names(self): # real signature unknown; restored from __doc__
        """ get_rpm_component_names(self) -> list """
        return []

    def get_rpm_filters(self): # real signature unknown; restored from __doc__
        """ get_rpm_filters(self) -> list """
        return []

    def get_servicelevel(self, servicelevel_name): # real signature unknown; restored from __doc__
        """ get_servicelevel(self, servicelevel_name:str) -> Modulemd.ServiceLevel """
        pass

    def get_servicelevel_names(self): # real signature unknown; restored from __doc__
        """ get_servicelevel_names(self) -> list """
        return []

    def get_stream_name(self): # real signature unknown; restored from __doc__
        """ get_stream_name(self) -> str """
        return ""

    def get_summary(self, locale=None): # real signature unknown; restored from __doc__
        """ get_summary(self, locale:str=None) -> str """
        return ""

    def get_tracker(self): # real signature unknown; restored from __doc__
        """ get_tracker(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> int """
        return 0

    def get_xmd(self): # real signature unknown; restored from __doc__
        """ get_xmd(self) -> GLib.Variant """
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

    def new(self, module_name=None, module_stream=None): # real signature unknown; restored from __doc__
        """ new(module_name:str=None, module_stream:str=None) -> Modulemd.ModuleStreamV2 """
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

    def read_file(self, path, strict, module_name=None, module_stream=None): # real signature unknown; restored from __doc__
        """ read_file(path:str, strict:bool, module_name:str=None, module_stream:str=None) -> Modulemd.ModuleStream """
        pass

    def read_string(self, yaml_string, strict, module_name=None, module_stream=None): # real signature unknown; restored from __doc__
        """ read_string(yaml_string:str, strict:bool, module_name:str=None, module_stream:str=None) -> Modulemd.ModuleStream """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_content_license(self, license): # real signature unknown; restored from __doc__
        """ remove_content_license(self, license:str) """
        pass

    def remove_dependencies(self, deps): # real signature unknown; restored from __doc__
        """ remove_dependencies(self, deps:Modulemd.Dependencies) """
        pass

    def remove_module_component(self, component_name): # real signature unknown; restored from __doc__
        """ remove_module_component(self, component_name:str) """
        pass

    def remove_module_license(self, license): # real signature unknown; restored from __doc__
        """ remove_module_license(self, license:str) """
        pass

    def remove_rpm_api(self, rpm): # real signature unknown; restored from __doc__
        """ remove_rpm_api(self, rpm:str) """
        pass

    def remove_rpm_artifact(self, nevr): # real signature unknown; restored from __doc__
        """ remove_rpm_artifact(self, nevr:str) """
        pass

    def remove_rpm_component(self, component_name): # real signature unknown; restored from __doc__
        """ remove_rpm_component(self, component_name:str) """
        pass

    def remove_rpm_filter(self, rpm): # real signature unknown; restored from __doc__
        """ remove_rpm_filter(self, rpm:str) """
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

    def search_profiles(self, profile_pattern=None): # real signature unknown; restored from __doc__
        """ search_profiles(self, profile_pattern:str=None) -> list """
        return []

    def set_arch(self, arch): # real signature unknown; restored from __doc__
        """ set_arch(self, arch:str) """
        pass

    def set_buildopts(self, buildopts): # real signature unknown; restored from __doc__
        """ set_buildopts(self, buildopts:Modulemd.Buildopts) """
        pass

    def set_community(self, community): # real signature unknown; restored from __doc__
        """ set_community(self, community:str) """
        pass

    def set_context(self, context=None): # real signature unknown; restored from __doc__
        """ set_context(self, context:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description=None): # real signature unknown; restored from __doc__
        """ set_description(self, description:str=None) """
        pass

    def set_documentation(self, documentation): # real signature unknown; restored from __doc__
        """ set_documentation(self, documentation:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rpm_artifact_map_entry(self, entry, digest, checksum): # real signature unknown; restored from __doc__
        """ set_rpm_artifact_map_entry(self, entry:Modulemd.RpmMapEntry, digest:str, checksum:str) """
        pass

    def set_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str=None) """
        pass

    def set_tracker(self, tracker): # real signature unknown; restored from __doc__
        """ set_tracker(self, tracker:str) """
        pass

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:int) """
        pass

    def set_xmd(self, xmd): # real signature unknown; restored from __doc__
        """ set_xmd(self, xmd:GLib.Variant) """
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

    def upgrade(self, mdversion): # real signature unknown; restored from __doc__
        """ upgrade(self, mdversion:int) -> Modulemd.ModuleStream """
        pass

    def validate(self): # real signature unknown; restored from __doc__
        """ validate(self) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f723f1bbd00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ModuleStreamV2), '__module__': 'gi.repository.Modulemd', '__gtype__': <GType ModulemdModuleStreamV2 (94446540506032)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_component': gi.FunctionInfo(add_component), 'add_content_license': gi.FunctionInfo(add_content_license), 'add_dependencies': gi.FunctionInfo(add_dependencies), 'add_module_license': gi.FunctionInfo(add_module_license), 'add_profile': gi.FunctionInfo(add_profile), 'add_rpm_api': gi.FunctionInfo(add_rpm_api), 'add_rpm_artifact': gi.FunctionInfo(add_rpm_artifact), 'add_rpm_filter': gi.FunctionInfo(add_rpm_filter), 'add_servicelevel': gi.FunctionInfo(add_servicelevel), 'clear_content_licenses': gi.FunctionInfo(clear_content_licenses), 'clear_dependencies': gi.FunctionInfo(clear_dependencies), 'clear_module_components': gi.FunctionInfo(clear_module_components), 'clear_module_licenses': gi.FunctionInfo(clear_module_licenses), 'clear_profiles': gi.FunctionInfo(clear_profiles), 'clear_rpm_api': gi.FunctionInfo(clear_rpm_api), 'clear_rpm_artifacts': gi.FunctionInfo(clear_rpm_artifacts), 'clear_rpm_components': gi.FunctionInfo(clear_rpm_components), 'clear_rpm_filters': gi.FunctionInfo(clear_rpm_filters), 'clear_servicelevels': gi.FunctionInfo(clear_servicelevels), 'get_arch': gi.FunctionInfo(get_arch), 'get_buildopts': gi.FunctionInfo(get_buildopts), 'get_community': gi.FunctionInfo(get_community), 'get_content_licenses': gi.FunctionInfo(get_content_licenses), 'get_dependencies': gi.FunctionInfo(get_dependencies), 'get_description': gi.FunctionInfo(get_description), 'get_documentation': gi.FunctionInfo(get_documentation), 'get_module_component': gi.FunctionInfo(get_module_component), 'get_module_component_names': gi.FunctionInfo(get_module_component_names), 'get_module_licenses': gi.FunctionInfo(get_module_licenses), 'get_profile': gi.FunctionInfo(get_profile), 'get_profile_names': gi.FunctionInfo(get_profile_names), 'get_rpm_api': gi.FunctionInfo(get_rpm_api), 'get_rpm_artifact_map_entry': gi.FunctionInfo(get_rpm_artifact_map_entry), 'get_rpm_artifacts': gi.FunctionInfo(get_rpm_artifacts), 'get_rpm_component': gi.FunctionInfo(get_rpm_component), 'get_rpm_component_names': gi.FunctionInfo(get_rpm_component_names), 'get_rpm_filters': gi.FunctionInfo(get_rpm_filters), 'get_servicelevel': gi.FunctionInfo(get_servicelevel), 'get_servicelevel_names': gi.FunctionInfo(get_servicelevel_names), 'get_summary': gi.FunctionInfo(get_summary), 'get_tracker': gi.FunctionInfo(get_tracker), 'get_xmd': gi.FunctionInfo(get_xmd), 'remove_content_license': gi.FunctionInfo(remove_content_license), 'remove_dependencies': gi.FunctionInfo(remove_dependencies), 'remove_module_component': gi.FunctionInfo(remove_module_component), 'remove_module_license': gi.FunctionInfo(remove_module_license), 'remove_rpm_api': gi.FunctionInfo(remove_rpm_api), 'remove_rpm_artifact': gi.FunctionInfo(remove_rpm_artifact), 'remove_rpm_component': gi.FunctionInfo(remove_rpm_component), 'remove_rpm_filter': gi.FunctionInfo(remove_rpm_filter), 'search_profiles': gi.FunctionInfo(search_profiles), 'set_arch': gi.FunctionInfo(set_arch), 'set_buildopts': gi.FunctionInfo(set_buildopts), 'set_community': gi.FunctionInfo(set_community), 'set_description': gi.FunctionInfo(set_description), 'set_documentation': gi.FunctionInfo(set_documentation), 'set_rpm_artifact_map_entry': gi.FunctionInfo(set_rpm_artifact_map_entry), 'set_summary': gi.FunctionInfo(set_summary), 'set_tracker': gi.FunctionInfo(set_tracker), 'set_xmd': gi.FunctionInfo(set_xmd)})"
    __gdoc__ = 'Object ModulemdModuleStreamV2\n\nProperties from ModulemdModuleStreamV2:\n  arch -> gchararray: Module Artifact Architecture\n    The architecture of the produced artifacts\n  buildopts -> ModulemdBuildopts: Module Build Options\n    Build options for module components\n  community -> gchararray: Module Community Website\n    The website address of the upstream community for this module\n  documentation -> gchararray: Module Documentation Website\n    The website address of the upstream documentation for this module\n  tracker -> gchararray: Module Bug Tracker Website\n    The website address of the upstream bug tracker for this module\n\nProperties from ModulemdModuleStream:\n  mdversion -> guint64: Metadata Version\n    The metadata version of this ModuleStream object. Read-only.\n  module-name -> gchararray: Module Name\n    The name of the module providing this stream.\n  stream-name -> gchararray: Stream Name\n    The name of this module stream.\n  version -> guint64: Module Stream Version\n    The version of this module stream\n  context -> gchararray: Module Stream Context\n    The context of this module stream. Distinguishes between streams with the same version but different dependencies due to module stream expansion.\n  arch -> gchararray: Module Stream Architecture\n    The processor architecture of this module stream.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ModulemdModuleStreamV2 (94446540506032)>'
    __info__ = ObjectInfo(ModuleStreamV2)


