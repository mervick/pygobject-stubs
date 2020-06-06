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


class Db(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Db(**properties)
        new() -> Libosinfo.Db
    """
    def add_datamap(self, datamap): # real signature unknown; restored from __doc__
        """ add_datamap(self, datamap:Libosinfo.Datamap) """
        pass

    def add_deployment(self, deployment): # real signature unknown; restored from __doc__
        """ add_deployment(self, deployment:Libosinfo.Deployment) """
        pass

    def add_device(self, device): # real signature unknown; restored from __doc__
        """ add_device(self, device:Libosinfo.Device) """
        pass

    def add_install_script(self, script): # real signature unknown; restored from __doc__
        """ add_install_script(self, script:Libosinfo.InstallScript) """
        pass

    def add_os(self, os): # real signature unknown; restored from __doc__
        """ add_os(self, os:Libosinfo.Os) """
        pass

    def add_platform(self, platform): # real signature unknown; restored from __doc__
        """ add_platform(self, platform:Libosinfo.Platform) """
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

    def find_deployment(self, os, platform): # real signature unknown; restored from __doc__
        """ find_deployment(self, os:Libosinfo.Os, platform:Libosinfo.Platform) -> Libosinfo.Deployment """
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_datamap(self, id): # real signature unknown; restored from __doc__
        """ get_datamap(self, id:str) -> Libosinfo.Datamap """
        pass

    def get_datamap_list(self): # real signature unknown; restored from __doc__
        """ get_datamap_list(self) -> Libosinfo.DatamapList """
        pass

    def get_deployment(self, id): # real signature unknown; restored from __doc__
        """ get_deployment(self, id:str) -> Libosinfo.Deployment """
        pass

    def get_deployment_list(self): # real signature unknown; restored from __doc__
        """ get_deployment_list(self) -> Libosinfo.DeploymentList """
        pass

    def get_device(self, id): # real signature unknown; restored from __doc__
        """ get_device(self, id:str) -> Libosinfo.Device """
        pass

    def get_device_list(self): # real signature unknown; restored from __doc__
        """ get_device_list(self) -> Libosinfo.DeviceList """
        pass

    def get_install_script(self, id): # real signature unknown; restored from __doc__
        """ get_install_script(self, id:str) -> Libosinfo.InstallScript """
        pass

    def get_install_script_list(self): # real signature unknown; restored from __doc__
        """ get_install_script_list(self) -> Libosinfo.InstallScriptList """
        pass

    def get_os(self, id): # real signature unknown; restored from __doc__
        """ get_os(self, id:str) -> Libosinfo.Os """
        pass

    def get_os_list(self): # real signature unknown; restored from __doc__
        """ get_os_list(self) -> Libosinfo.OsList """
        pass

    def get_platform(self, id): # real signature unknown; restored from __doc__
        """ get_platform(self, id:str) -> Libosinfo.Platform """
        pass

    def get_platform_list(self): # real signature unknown; restored from __doc__
        """ get_platform_list(self) -> Libosinfo.PlatformList """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def guess_os_from_media(self, media): # real signature unknown; restored from __doc__
        """ guess_os_from_media(self, media:Libosinfo.Media) -> Libosinfo.Os, matched_media:Libosinfo.Media """
        pass

    def guess_os_from_tree(self, tree): # real signature unknown; restored from __doc__
        """ guess_os_from_tree(self, tree:Libosinfo.Tree) -> Libosinfo.Os, matched_tree:Libosinfo.Tree """
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

    def identify_media(self, media): # real signature unknown; restored from __doc__
        """ identify_media(self, media:Libosinfo.Media) -> bool """
        return False

    def identify_tree(self, tree): # real signature unknown; restored from __doc__
        """ identify_tree(self, tree:Libosinfo.Tree) -> bool """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Libosinfo.Db """
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

    def unique_values_for_os_relationship(self, relshp): # real signature unknown; restored from __doc__
        """ unique_values_for_os_relationship(self, relshp:Libosinfo.ProductRelationship) -> Libosinfo.OsList """
        pass

    def unique_values_for_platform_relationship(self, relshp): # real signature unknown; restored from __doc__
        """ unique_values_for_platform_relationship(self, relshp:Libosinfo.ProductRelationship) -> Libosinfo.PlatformList """
        pass

    def unique_values_for_property_in_deployment(self, propName): # real signature unknown; restored from __doc__
        """ unique_values_for_property_in_deployment(self, propName:str) -> list """
        return []

    def unique_values_for_property_in_device(self, propName): # real signature unknown; restored from __doc__
        """ unique_values_for_property_in_device(self, propName:str) -> list """
        return []

    def unique_values_for_property_in_os(self, propName): # real signature unknown; restored from __doc__
        """ unique_values_for_property_in_os(self, propName:str) -> list """
        return []

    def unique_values_for_property_in_platform(self, propName): # real signature unknown; restored from __doc__
        """ unique_values_for_property_in_platform(self, propName:str) -> list """
        return []

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f71538bccd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Db), '__module__': 'gi.repository.Libosinfo', '__gtype__': <GType OsinfoDb (94407636173472)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_datamap': gi.FunctionInfo(add_datamap), 'add_deployment': gi.FunctionInfo(add_deployment), 'add_device': gi.FunctionInfo(add_device), 'add_install_script': gi.FunctionInfo(add_install_script), 'add_os': gi.FunctionInfo(add_os), 'add_platform': gi.FunctionInfo(add_platform), 'find_deployment': gi.FunctionInfo(find_deployment), 'get_datamap': gi.FunctionInfo(get_datamap), 'get_datamap_list': gi.FunctionInfo(get_datamap_list), 'get_deployment': gi.FunctionInfo(get_deployment), 'get_deployment_list': gi.FunctionInfo(get_deployment_list), 'get_device': gi.FunctionInfo(get_device), 'get_device_list': gi.FunctionInfo(get_device_list), 'get_install_script': gi.FunctionInfo(get_install_script), 'get_install_script_list': gi.FunctionInfo(get_install_script_list), 'get_os': gi.FunctionInfo(get_os), 'get_os_list': gi.FunctionInfo(get_os_list), 'get_platform': gi.FunctionInfo(get_platform), 'get_platform_list': gi.FunctionInfo(get_platform_list), 'guess_os_from_media': gi.FunctionInfo(guess_os_from_media), 'guess_os_from_tree': gi.FunctionInfo(guess_os_from_tree), 'identify_media': gi.FunctionInfo(identify_media), 'identify_tree': gi.FunctionInfo(identify_tree), 'unique_values_for_os_relationship': gi.FunctionInfo(unique_values_for_os_relationship), 'unique_values_for_platform_relationship': gi.FunctionInfo(unique_values_for_platform_relationship), 'unique_values_for_property_in_deployment': gi.FunctionInfo(unique_values_for_property_in_deployment), 'unique_values_for_property_in_device': gi.FunctionInfo(unique_values_for_property_in_device), 'unique_values_for_property_in_os': gi.FunctionInfo(unique_values_for_property_in_os), 'unique_values_for_property_in_platform': gi.FunctionInfo(unique_values_for_property_in_platform), 'parent_instance': <property object at 0x7f71538ea630>, 'priv': <property object at 0x7f71538ea720>})"
    __gdoc__ = 'Object OsinfoDb\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OsinfoDb (94407636173472)>'
    __info__ = ObjectInfo(Db)


