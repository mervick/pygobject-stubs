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


class PackageSack(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        PackageSack(**properties)
        new() -> PackageKitGlib.PackageSack
    """
    def add_package(self, package): # real signature unknown; restored from __doc__
        """ add_package(self, package:PackageKitGlib.Package) -> bool """
        return False

    def add_packages_from_file(self, file): # real signature unknown; restored from __doc__
        """ add_packages_from_file(self, file:Gio.File) -> bool """
        return False

    def add_package_by_id(self, package_id): # real signature unknown; restored from __doc__
        """ add_package_by_id(self, package_id:str) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
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

    def filter(self, filter_cb, user_data=None): # real signature unknown; restored from __doc__
        """ filter(self, filter_cb:PackageKitGlib.PackageSackFilterFunc, user_data=None) -> PackageKitGlib.PackageSack """
        pass

    def filter_by_info(self, info): # real signature unknown; restored from __doc__
        """ filter_by_info(self, info:PackageKitGlib.InfoEnum) -> PackageKitGlib.PackageSack """
        pass

    def find_by_id(self, package_id): # real signature unknown; restored from __doc__
        """ find_by_id(self, package_id:str) -> PackageKitGlib.Package """
        pass

    def find_by_id_name_arch(self, package_id): # real signature unknown; restored from __doc__
        """ find_by_id_name_arch(self, package_id:str) -> PackageKitGlib.Package """
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

    def get_array(self): # real signature unknown; restored from __doc__
        """ get_array(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_details(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_details(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_details_async(self, cancellable=None, progress_callback, progress_user_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_details_async(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_ids(self): # real signature unknown; restored from __doc__
        """ get_ids(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_total_bytes(self): # real signature unknown; restored from __doc__
        """ get_total_bytes(self) -> int """
        return 0

    def get_update_detail(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_update_detail(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def get_update_detail_async(self, cancellable=None, progress_callback, progress_user_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_update_detail_async(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def merge_generic_finish(self, res): # real signature unknown; restored from __doc__
        """ merge_generic_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> PackageKitGlib.PackageSack """
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

    def remove_by_filter(self, filter_cb, user_data=None): # real signature unknown; restored from __doc__
        """ remove_by_filter(self, filter_cb:PackageKitGlib.PackageSackFilterFunc, user_data=None) -> bool """
        return False

    def remove_package(self, package): # real signature unknown; restored from __doc__
        """ remove_package(self, package:PackageKitGlib.Package) -> bool """
        return False

    def remove_package_by_id(self, package_id): # real signature unknown; restored from __doc__
        """ remove_package_by_id(self, package_id:str) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def resolve(self, cancellable=None): # real signature unknown; restored from __doc__
        """ resolve(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def resolve_async(self, cancellable=None, progress_callback, progress_user_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ resolve_async(self, cancellable:Gio.Cancellable=None, progress_callback:PackageKitGlib.ProgressCallback, progress_user_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def sort(self, type): # real signature unknown; restored from __doc__
        """ sort(self, type:PackageKitGlib.PackageSackSortType) """
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

    def to_file(self, file): # real signature unknown; restored from __doc__
        """ to_file(self, file:Gio.File) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f121f8dd4c0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(PackageSack), '__module__': 'gi.repository.PackageKitGlib', '__gtype__': <GType PkPackageSack (94016446607376)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_package': gi.FunctionInfo(add_package), 'add_package_by_id': gi.FunctionInfo(add_package_by_id), 'add_packages_from_file': gi.FunctionInfo(add_packages_from_file), 'clear': gi.FunctionInfo(clear), 'filter': gi.FunctionInfo(filter), 'filter_by_info': gi.FunctionInfo(filter_by_info), 'find_by_id': gi.FunctionInfo(find_by_id), 'find_by_id_name_arch': gi.FunctionInfo(find_by_id_name_arch), 'get_array': gi.FunctionInfo(get_array), 'get_details': gi.FunctionInfo(get_details), 'get_details_async': gi.FunctionInfo(get_details_async), 'get_ids': gi.FunctionInfo(get_ids), 'get_size': gi.FunctionInfo(get_size), 'get_total_bytes': gi.FunctionInfo(get_total_bytes), 'get_update_detail': gi.FunctionInfo(get_update_detail), 'get_update_detail_async': gi.FunctionInfo(get_update_detail_async), 'merge_generic_finish': gi.FunctionInfo(merge_generic_finish), 'remove_by_filter': gi.FunctionInfo(remove_by_filter), 'remove_package': gi.FunctionInfo(remove_package), 'remove_package_by_id': gi.FunctionInfo(remove_package_by_id), 'resolve': gi.FunctionInfo(resolve), 'resolve_async': gi.FunctionInfo(resolve_async), 'sort': gi.FunctionInfo(sort), 'to_file': gi.FunctionInfo(to_file), 'do_changed': gi.VFuncInfo(changed), 'parent': <property object at 0x7f121f8eeb80>, 'priv': <property object at 0x7f121f8eec70>})"
    __gdoc__ = 'Object PkPackageSack\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PkPackageSack (94016446607376)>'
    __info__ = ObjectInfo(PackageSack)


