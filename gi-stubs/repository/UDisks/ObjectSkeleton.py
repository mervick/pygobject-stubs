# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .Object import Object

class ObjectSkeleton(__gi_repository_Gio.DBusObjectSkeleton, Object):
    """
    :Constructors:
    
    ::
    
        ObjectSkeleton(**properties)
        new(object_path:str) -> UDisks.ObjectSkeleton
    """
    def add_interface(self, interface_): # real signature unknown; restored from __doc__
        """ add_interface(self, interface_:Gio.DBusInterfaceSkeleton) """
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

    def do_authorize_method(self, *args, **kwargs): # real signature unknown
        """ authorize_method(self, interface_:Gio.DBusInterfaceSkeleton, invocation:Gio.DBusMethodInvocation) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
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

    def get_block(self): # real signature unknown; restored from __doc__
        """ get_block(self) -> UDisks.Block or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_drive(self): # real signature unknown; restored from __doc__
        """ get_drive(self) -> UDisks.Drive or None """
        pass

    def get_drive_ata(self): # real signature unknown; restored from __doc__
        """ get_drive_ata(self) -> UDisks.DriveAta or None """
        pass

    def get_encrypted(self): # real signature unknown; restored from __doc__
        """ get_encrypted(self) -> UDisks.Encrypted or None """
        pass

    def get_filesystem(self): # real signature unknown; restored from __doc__
        """ get_filesystem(self) -> UDisks.Filesystem or None """
        pass

    def get_interface(self, interface_name): # real signature unknown; restored from __doc__
        """ get_interface(self, interface_name:str) -> Gio.DBusInterface """
        pass

    def get_interfaces(self): # real signature unknown; restored from __doc__
        """ get_interfaces(self) -> list """
        return []

    def get_job(self): # real signature unknown; restored from __doc__
        """ get_job(self) -> UDisks.Job or None """
        pass

    def get_loop(self): # real signature unknown; restored from __doc__
        """ get_loop(self) -> UDisks.Loop or None """
        pass

    def get_manager(self): # real signature unknown; restored from __doc__
        """ get_manager(self) -> UDisks.Manager or None """
        pass

    def get_mdraid(self): # real signature unknown; restored from __doc__
        """ get_mdraid(self) -> UDisks.MDRaid or None """
        pass

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_partition(self): # real signature unknown; restored from __doc__
        """ get_partition(self) -> UDisks.Partition or None """
        pass

    def get_partition_table(self): # real signature unknown; restored from __doc__
        """ get_partition_table(self) -> UDisks.PartitionTable or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_swapspace(self): # real signature unknown; restored from __doc__
        """ get_swapspace(self) -> UDisks.Swapspace or None """
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

    def new(self, object_path): # real signature unknown; restored from __doc__
        """ new(object_path:str) -> UDisks.ObjectSkeleton """
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

    def remove_interface(self, interface_): # real signature unknown; restored from __doc__
        """ remove_interface(self, interface_:Gio.DBusInterfaceSkeleton) """
        pass

    def remove_interface_by_name(self, interface_name): # real signature unknown; restored from __doc__
        """ remove_interface_by_name(self, interface_name:str) """
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

    def set_block(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_block(self, interface_:UDisks.Block=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_drive(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_drive(self, interface_:UDisks.Drive=None) """
        pass

    def set_drive_ata(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_drive_ata(self, interface_:UDisks.DriveAta=None) """
        pass

    def set_encrypted(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_encrypted(self, interface_:UDisks.Encrypted=None) """
        pass

    def set_filesystem(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_filesystem(self, interface_:UDisks.Filesystem=None) """
        pass

    def set_job(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_job(self, interface_:UDisks.Job=None) """
        pass

    def set_loop(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_loop(self, interface_:UDisks.Loop=None) """
        pass

    def set_manager(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_manager(self, interface_:UDisks.Manager=None) """
        pass

    def set_mdraid(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_mdraid(self, interface_:UDisks.MDRaid=None) """
        pass

    def set_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ set_object_path(self, object_path:str) """
        pass

    def set_partition(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_partition(self, interface_:UDisks.Partition=None) """
        pass

    def set_partition_table(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_partition_table(self, interface_:UDisks.PartitionTable=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_swapspace(self, interface_=None): # real signature unknown; restored from __doc__
        """ set_swapspace(self, interface_:UDisks.Swapspace=None) """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f13a7e9fee0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ObjectSkeleton), '__module__': 'gi.repository.UDisks', '__gtype__': <GType UDisksObjectSkeleton (93969722803872)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'set_block': gi.FunctionInfo(set_block), 'set_drive': gi.FunctionInfo(set_drive), 'set_drive_ata': gi.FunctionInfo(set_drive_ata), 'set_encrypted': gi.FunctionInfo(set_encrypted), 'set_filesystem': gi.FunctionInfo(set_filesystem), 'set_job': gi.FunctionInfo(set_job), 'set_loop': gi.FunctionInfo(set_loop), 'set_manager': gi.FunctionInfo(set_manager), 'set_mdraid': gi.FunctionInfo(set_mdraid), 'set_partition': gi.FunctionInfo(set_partition), 'set_partition_table': gi.FunctionInfo(set_partition_table), 'set_swapspace': gi.FunctionInfo(set_swapspace), 'parent_instance': <property object at 0x7f13a806d450>, 'priv': <property object at 0x7f13a806d540>})"
    __gdoc__ = 'Object UDisksObjectSkeleton\n\nSignals from GDBusObject:\n  interface-added (GDBusInterface)\n  interface-removed (GDBusInterface)\n\nSignals from GDBusObjectSkeleton:\n  authorize-method (GDBusInterfaceSkeleton, GDBusMethodInvocation) -> gboolean\n\nProperties from GDBusObjectSkeleton:\n  g-object-path -> gchararray: Object Path\n    The object path where the object is exported\n\nSignals from GDBusObject:\n  interface-added (GDBusInterface)\n  interface-removed (GDBusInterface)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType UDisksObjectSkeleton (93969722803872)>'
    __info__ = ObjectInfo(ObjectSkeleton)


