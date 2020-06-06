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


from .Source import Source

class Package(Source):
    """
    :Constructors:
    
    ::
    
        Package(**properties)
        new() -> PackageKitGlib.Package
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

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equal(self, package2): # real signature unknown; restored from __doc__
        """ equal(self, package2:PackageKitGlib.Package) -> bool """
        return False

    def equal_id(self, package2): # real signature unknown; restored from __doc__
        """ equal_id(self, package2:PackageKitGlib.Package) -> bool """
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

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> str """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> PackageKitGlib.InfoEnum """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
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

    def ids_add_id(self, package_ids, package_id): # real signature unknown; restored from __doc__
        """ ids_add_id(package_ids:str, package_id:str) -> list """
        return []

    def ids_add_ids(self, package_ids, package_ids_new): # real signature unknown; restored from __doc__
        """ ids_add_ids(package_ids:str, package_ids_new:str) -> list """
        return []

    def ids_check(self, package_ids): # real signature unknown; restored from __doc__
        """ ids_check(package_ids:str) -> bool """
        return False

    def ids_from_id(self, package_id): # real signature unknown; restored from __doc__
        """ ids_from_id(package_id:str) -> list """
        return []

    def ids_from_string(self, package_id): # real signature unknown; restored from __doc__
        """ ids_from_string(package_id:str) -> list """
        return []

    def ids_present_id(self, package_ids, package_id): # real signature unknown; restored from __doc__
        """ ids_present_id(package_ids:str, package_id:str) -> bool """
        return False

    def ids_remove_id(self, package_ids, package_id): # real signature unknown; restored from __doc__
        """ ids_remove_id(package_ids:str, package_id:str) -> list """
        return []

    def ids_to_string(self, package_ids): # real signature unknown; restored from __doc__
        """ ids_to_string(package_ids:str) -> str """
        return ""

    def id_build(self, name, version, arch, data): # real signature unknown; restored from __doc__
        """ id_build(name:str, version:str, arch:str, data:str) -> str """
        return ""

    def id_check(self, package_id): # real signature unknown; restored from __doc__
        """ id_check(package_id:str) -> bool """
        return False

    def id_equal_fuzzy_arch(self, package_id1, package_id2): # real signature unknown; restored from __doc__
        """ id_equal_fuzzy_arch(package_id1:str, package_id2:str) -> bool """
        return False

    def id_split(self, package_id): # real signature unknown; restored from __doc__
        """ id_split(package_id:str) -> list """
        return []

    def id_to_printable(self, package_id): # real signature unknown; restored from __doc__
        """ id_to_printable(package_id:str) -> str """
        return ""

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
        """ new() -> PackageKitGlib.Package """
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

    def parse(self, data): # real signature unknown; restored from __doc__
        """ parse(self, data:str) -> bool """
        return False

    def print_(self): # real signature unknown; restored from __doc__
        """ print_(self) """
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

    def set_id(self, package_id): # real signature unknown; restored from __doc__
        """ set_id(self, package_id:str) -> bool """
        return False

    def set_info(self, info): # real signature unknown; restored from __doc__
        """ set_info(self, info:PackageKitGlib.InfoEnum) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_summary(self, summary): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f121f8aa4c0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Package), '__module__': 'gi.repository.PackageKitGlib', '__gtype__': <GType PkPackage (94016447175440)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'id_build': gi.FunctionInfo(id_build), 'id_check': gi.FunctionInfo(id_check), 'id_equal_fuzzy_arch': gi.FunctionInfo(id_equal_fuzzy_arch), 'id_split': gi.FunctionInfo(id_split), 'id_to_printable': gi.FunctionInfo(id_to_printable), 'ids_add_id': gi.FunctionInfo(ids_add_id), 'ids_add_ids': gi.FunctionInfo(ids_add_ids), 'ids_check': gi.FunctionInfo(ids_check), 'ids_from_id': gi.FunctionInfo(ids_from_id), 'ids_from_string': gi.FunctionInfo(ids_from_string), 'ids_present_id': gi.FunctionInfo(ids_present_id), 'ids_remove_id': gi.FunctionInfo(ids_remove_id), 'ids_to_string': gi.FunctionInfo(ids_to_string), 'equal': gi.FunctionInfo(equal), 'equal_id': gi.FunctionInfo(equal_id), 'get_arch': gi.FunctionInfo(get_arch), 'get_data': gi.FunctionInfo(get_data), 'get_id': gi.FunctionInfo(get_id), 'get_info': gi.FunctionInfo(get_info), 'get_name': gi.FunctionInfo(get_name), 'get_summary': gi.FunctionInfo(get_summary), 'get_version': gi.FunctionInfo(get_version), 'parse': gi.FunctionInfo(parse), 'print_': gi.FunctionInfo(print), 'set_id': gi.FunctionInfo(set_id), 'set_info': gi.FunctionInfo(set_info), 'set_summary': gi.FunctionInfo(set_summary), 'do_changed': gi.VFuncInfo(changed), 'parent': <property object at 0x7f121f8ebe50>, 'priv': <property object at 0x7f121f8ebf40>})"
    __gdoc__ = "Object PkPackage\n\nSignals from PkPackage:\n  changed ()\n\nProperties from PkPackage:\n  info -> PkInfoEnum: info\n    The PkInfoEnum package type, e.g. PK_INFO_ENUM_NORMAL\n  package-id -> gchararray: package-id\n    The full package_id, e.g. 'gnome-power-manager;0.1.2;i386;fedora'\n  summary -> gchararray: summary\n    The package summary\n  license -> gchararray: license\n    The package license\n  group -> PkGroupEnum: group\n    The package group\n  description -> gchararray: description\n    The package description\n  url -> gchararray: url\n    The package homepage URL\n  size -> guint64: size\n    The package size\n  update-updates -> gchararray: update-updates\n    The update packages\n  update-obsoletes -> gchararray: update-obsoletes\n    The update packages that are obsoleted\n  update-vendor-urls -> GStrv: update-vendor-urls\n    The update vendor URLs\n  update-bugzilla-urls -> GStrv: update-bugzilla-urls\n    The update bugzilla URLs\n  update-cve-urls -> GStrv: update-cve-urls\n    The update CVE URLs\n  update-restart -> PkRestartEnum: update-restart\n    The update restart type\n  update-text -> gchararray: update-text\n    The update description\n  update-changelog -> gchararray: update-changelog\n    The update ChangeLog\n  update-state -> PkUpdateStateEnum: update-state\n    The update state\n  update-issued -> gchararray: update-issued\n    When the update was issued\n  update-updated -> gchararray: update-updated\n    When the update was last updated\n\nProperties from PkSource:\n  role -> PkRoleEnum: role\n  transaction-id -> gchararray: transaction-id\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PkPackage (94016447175440)>'
    __info__ = ObjectInfo(Package)


