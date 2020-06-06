# encoding: utf-8
# module gi.repository.LibvirtGObject
# from /usr/lib64/girepository-1.0/LibvirtGObject-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Domain(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Domain(**properties)
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

    def create_snapshot(self, custom_conf=None, flags): # real signature unknown; restored from __doc__
        """ create_snapshot(self, custom_conf:LibvirtGConfig.DomainSnapshot=None, flags:int) -> LibvirtGObject.DomainSnapshot """
        pass

    def create_snapshot_async(self, custom_conf=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_snapshot_async(self, custom_conf:LibvirtGConfig.DomainSnapshot=None, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_snapshot_finish(self, result): # real signature unknown; restored from __doc__
        """ create_snapshot_finish(self, result:Gio.AsyncResult) -> LibvirtGObject.DomainSnapshot """
        pass

    def delete(self, flags): # real signature unknown; restored from __doc__
        """ delete(self, flags:int) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_pmsuspended(self, *args, **kwargs): # real signature unknown
        """ pmsuspended(self) """
        pass

    def do_resumed(self, *args, **kwargs): # real signature unknown
        """ resumed(self) """
        pass

    def do_started(self, *args, **kwargs): # real signature unknown
        """ started(self) """
        pass

    def do_stopped(self, *args, **kwargs): # real signature unknown
        """ stopped(self) """
        pass

    def do_suspended(self, *args, **kwargs): # real signature unknown
        """ suspended(self) """
        pass

    def do_updated(self, *args, **kwargs): # real signature unknown
        """ updated(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def fetch_snapshots(self, list_flags, cancellable=None): # real signature unknown; restored from __doc__
        """ fetch_snapshots(self, list_flags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def fetch_snapshots_async(self, list_flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ fetch_snapshots_async(self, list_flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def fetch_snapshots_finish(self, res): # real signature unknown; restored from __doc__
        """ fetch_snapshots_finish(self, res:Gio.AsyncResult) -> bool """
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

    def get_config(self, flags): # real signature unknown; restored from __doc__
        """ get_config(self, flags:int) -> LibvirtGConfig.Domain """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_devices(self): # real signature unknown; restored from __doc__
        """ get_devices(self) -> list """
        return []

    def get_has_current_snapshot(self, flags): # real signature unknown; restored from __doc__
        """ get_has_current_snapshot(self, flags:int) -> bool, has_current_snapshot:bool """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_info(self): # real signature unknown; restored from __doc__
        """ get_info(self) -> LibvirtGObject.DomainInfo """
        pass

    def get_info_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ get_info_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def get_info_finish(self, result): # real signature unknown; restored from __doc__
        """ get_info_finish(self, result:Gio.AsyncResult) -> LibvirtGObject.DomainInfo """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_persistent(self): # real signature unknown; restored from __doc__
        """ get_persistent(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_saved(self): # real signature unknown; restored from __doc__
        """ get_saved(self) -> bool """
        return False

    def get_snapshots(self): # real signature unknown; restored from __doc__
        """ get_snapshots(self) -> list """
        return []

    def get_uuid(self): # real signature unknown; restored from __doc__
        """ get_uuid(self) -> str """
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

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open_console(self, stream, devname=None, flags): # real signature unknown; restored from __doc__
        """ open_console(self, stream:LibvirtGObject.Stream, devname:str=None, flags:int) -> bool """
        return False

    def open_graphics(self, idx, fd, flags): # real signature unknown; restored from __doc__
        """ open_graphics(self, idx:int, fd:int, flags:int) -> bool """
        return False

    def open_graphics_fd(self, idx, flags): # real signature unknown; restored from __doc__
        """ open_graphics_fd(self, idx:int, flags:int) -> int """
        return 0

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def reboot(self, flags): # real signature unknown; restored from __doc__
        """ reboot(self, flags:int) -> bool """
        return False

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

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> bool """
        return False

    def resume_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ resume_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def resume_finish(self, result): # real signature unknown; restored from __doc__
        """ resume_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def save(self, flags): # real signature unknown; restored from __doc__
        """ save(self, flags:int) -> bool """
        return False

    def save_async(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ save_async(self, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def save_finish(self, result): # real signature unknown; restored from __doc__
        """ save_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def save_to_file(self, filename, custom_conf=None, flags): # real signature unknown; restored from __doc__
        """ save_to_file(self, filename:str, custom_conf:LibvirtGConfig.Domain=None, flags:int) -> bool """
        return False

    def save_to_file_async(self, filename, custom_conf=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ save_to_file_async(self, filename:str, custom_conf:LibvirtGConfig.Domain=None, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def save_to_file_finish(self, result): # real signature unknown; restored from __doc__
        """ save_to_file_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def screenshot(self, stream, monitor_id, flags): # real signature unknown; restored from __doc__
        """ screenshot(self, stream:LibvirtGObject.Stream, monitor_id:int, flags:int) -> str """
        return ""

    def set_config(self, conf): # real signature unknown; restored from __doc__
        """ set_config(self, conf:LibvirtGConfig.Domain) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_time(self, date_time=None, flags): # real signature unknown; restored from __doc__
        """ set_time(self, date_time:GLib.DateTime=None, flags:int) -> bool """
        return False

    def set_time_async(self, date_time=None, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_time_async(self, date_time:GLib.DateTime=None, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_time_finish(self, result): # real signature unknown; restored from __doc__
        """ set_time_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def shutdown(self, flags): # real signature unknown; restored from __doc__
        """ shutdown(self, flags:int) -> bool """
        return False

    def start(self, flags): # real signature unknown; restored from __doc__
        """ start(self, flags:int) -> bool """
        return False

    def start_async(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ start_async(self, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def start_finish(self, result): # real signature unknown; restored from __doc__
        """ start_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop(self, flags): # real signature unknown; restored from __doc__
        """ stop(self, flags:int) -> bool """
        return False

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def suspend(self): # real signature unknown; restored from __doc__
        """ suspend(self) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def update_device(self, device, flags): # real signature unknown; restored from __doc__
        """ update_device(self, device:LibvirtGConfig.DomainDevice, flags:int) -> bool """
        return False

    def wakeup(self, flags): # real signature unknown; restored from __doc__
        """ wakeup(self, flags:int) -> bool """
        return False

    def wakeup_async(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ wakeup_async(self, flags:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def wakeup_finish(self, result): # real signature unknown; restored from __doc__
        """ wakeup_finish(self, result:Gio.AsyncResult) -> bool """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7ffa6e34daf0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Domain), '__module__': 'gi.repository.LibvirtGObject', '__gtype__': <GType GVirDomain (94394875749952)>, '__doc__': None, '__gsignals__': {}, 'create_snapshot': gi.FunctionInfo(create_snapshot), 'create_snapshot_async': gi.FunctionInfo(create_snapshot_async), 'create_snapshot_finish': gi.FunctionInfo(create_snapshot_finish), 'delete': gi.FunctionInfo(delete), 'fetch_snapshots': gi.FunctionInfo(fetch_snapshots), 'fetch_snapshots_async': gi.FunctionInfo(fetch_snapshots_async), 'fetch_snapshots_finish': gi.FunctionInfo(fetch_snapshots_finish), 'get_config': gi.FunctionInfo(get_config), 'get_devices': gi.FunctionInfo(get_devices), 'get_has_current_snapshot': gi.FunctionInfo(get_has_current_snapshot), 'get_id': gi.FunctionInfo(get_id), 'get_info': gi.FunctionInfo(get_info), 'get_info_async': gi.FunctionInfo(get_info_async), 'get_info_finish': gi.FunctionInfo(get_info_finish), 'get_name': gi.FunctionInfo(get_name), 'get_persistent': gi.FunctionInfo(get_persistent), 'get_saved': gi.FunctionInfo(get_saved), 'get_snapshots': gi.FunctionInfo(get_snapshots), 'get_uuid': gi.FunctionInfo(get_uuid), 'open_console': gi.FunctionInfo(open_console), 'open_graphics': gi.FunctionInfo(open_graphics), 'open_graphics_fd': gi.FunctionInfo(open_graphics_fd), 'reboot': gi.FunctionInfo(reboot), 'resume': gi.FunctionInfo(resume), 'resume_async': gi.FunctionInfo(resume_async), 'resume_finish': gi.FunctionInfo(resume_finish), 'save': gi.FunctionInfo(save), 'save_async': gi.FunctionInfo(save_async), 'save_finish': gi.FunctionInfo(save_finish), 'save_to_file': gi.FunctionInfo(save_to_file), 'save_to_file_async': gi.FunctionInfo(save_to_file_async), 'save_to_file_finish': gi.FunctionInfo(save_to_file_finish), 'screenshot': gi.FunctionInfo(screenshot), 'set_config': gi.FunctionInfo(set_config), 'set_time': gi.FunctionInfo(set_time), 'set_time_async': gi.FunctionInfo(set_time_async), 'set_time_finish': gi.FunctionInfo(set_time_finish), 'shutdown': gi.FunctionInfo(shutdown), 'start': gi.FunctionInfo(start), 'start_async': gi.FunctionInfo(start_async), 'start_finish': gi.FunctionInfo(start_finish), 'stop': gi.FunctionInfo(stop), 'suspend': gi.FunctionInfo(suspend), 'update_device': gi.FunctionInfo(update_device), 'wakeup': gi.FunctionInfo(wakeup), 'wakeup_async': gi.FunctionInfo(wakeup_async), 'wakeup_finish': gi.FunctionInfo(wakeup_finish), 'do_pmsuspended': gi.VFuncInfo(pmsuspended), 'do_resumed': gi.VFuncInfo(resumed), 'do_started': gi.VFuncInfo(started), 'do_stopped': gi.VFuncInfo(stopped), 'do_suspended': gi.VFuncInfo(suspended), 'do_updated': gi.VFuncInfo(updated), 'parent': <property object at 0x7ffa6f9688b0>, 'priv': <property object at 0x7ffa6f9689a0>})"
    __gdoc__ = 'Object GVirDomain\n\nSignals from GVirDomain:\n  started ()\n  suspended ()\n  resumed ()\n  stopped ()\n  updated ()\n  pmsuspended ()\n\nProperties from GVirDomain:\n  handle -> GVirDomainHandle: Handle\n    The domain handle\n  persistent -> gboolean: Persistent\n    If domain is persistent\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GVirDomain (94394875749952)>'
    __info__ = ObjectInfo(Domain)


