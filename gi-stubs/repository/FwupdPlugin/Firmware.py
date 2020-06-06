# encoding: utf-8
# module gi.repository.FwupdPlugin
# from /usr/lib64/girepository-1.0/FwupdPlugin-1.0.typelib
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
import gi.repository.Fwupd as __gi_repository_Fwupd
import gobject as __gobject


class Firmware(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Firmware(**properties)
        new() -> FwupdPlugin.Firmware
        new_from_bytes(fw:GLib.Bytes) -> FwupdPlugin.Firmware
    """
    def add_image(self, img): # real signature unknown; restored from __doc__
        """ add_image(self, img:FwupdPlugin.FirmwareImage) """
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

    def do_parse(self, *args, **kwargs): # real signature unknown
        """ parse(self, fw:GLib.Bytes, addr_start:int, addr_end:int, flags:Fwupd.InstallFlags) -> bool """
        pass

    def do_tokenize(self, *args, **kwargs): # real signature unknown
        """ tokenize(self, fw:GLib.Bytes, flags:Fwupd.InstallFlags) -> bool """
        pass

    def do_to_string(self, *args, **kwargs): # real signature unknown
        """ to_string(self, indent:int, str:GLib.String) """
        pass

    def do_write(self, *args, **kwargs): # real signature unknown
        """ write(self) -> GLib.Bytes """
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_images(self): # real signature unknown; restored from __doc__
        """ get_images(self) -> list """
        return []

    def get_image_by_id(self, id=None): # real signature unknown; restored from __doc__
        """ get_image_by_id(self, id:str=None) -> FwupdPlugin.FirmwareImage """
        pass

    def get_image_by_idx(self, idx): # real signature unknown; restored from __doc__
        """ get_image_by_idx(self, idx:int) -> FwupdPlugin.FirmwareImage """
        pass

    def get_image_by_idx_bytes(self, idx): # real signature unknown; restored from __doc__
        """ get_image_by_idx_bytes(self, idx:int) -> GLib.Bytes """
        pass

    def get_image_by_id_bytes(self, id=None): # real signature unknown; restored from __doc__
        """ get_image_by_id_bytes(self, id:str=None) -> GLib.Bytes """
        pass

    def get_image_default(self): # real signature unknown; restored from __doc__
        """ get_image_default(self) -> FwupdPlugin.FirmwareImage """
        pass

    def get_image_default_bytes(self): # real signature unknown; restored from __doc__
        """ get_image_default_bytes(self) -> GLib.Bytes """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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
        """ new() -> FwupdPlugin.Firmware """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_bytes(self, fw): # real signature unknown; restored from __doc__
        """ new_from_bytes(fw:GLib.Bytes) -> FwupdPlugin.Firmware """
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

    def parse(self, fw, flags): # real signature unknown; restored from __doc__
        """ parse(self, fw:GLib.Bytes, flags:Fwupd.InstallFlags) -> bool """
        return False

    def parse_file(self, file, flags): # real signature unknown; restored from __doc__
        """ parse_file(self, file:Gio.File, flags:Fwupd.InstallFlags) -> bool """
        return False

    def parse_full(self, fw, addr_start, addr_end, flags): # real signature unknown; restored from __doc__
        """ parse_full(self, fw:GLib.Bytes, addr_start:int, addr_end:int, flags:Fwupd.InstallFlags) -> bool """
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

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:str) """
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

    def strparse_uint16(self, data): # real signature unknown; restored from __doc__
        """ strparse_uint16(data:str) -> int """
        return 0

    def strparse_uint24(self, data): # real signature unknown; restored from __doc__
        """ strparse_uint24(data:str) -> int """
        return 0

    def strparse_uint32(self, data): # real signature unknown; restored from __doc__
        """ strparse_uint32(data:str) -> int """
        return 0

    def strparse_uint4(self, data): # real signature unknown; restored from __doc__
        """ strparse_uint4(data:str) -> int """
        return 0

    def strparse_uint8(self, data): # real signature unknown; restored from __doc__
        """ strparse_uint8(data:str) -> int """
        return 0

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def tokenize(self, fw, flags): # real signature unknown; restored from __doc__
        """ tokenize(self, fw:GLib.Bytes, flags:Fwupd.InstallFlags) -> bool """
        return False

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write(self): # real signature unknown; restored from __doc__
        """ write(self) -> GLib.Bytes """
        pass

    def write_file(self, file): # real signature unknown; restored from __doc__
        """ write_file(self, file:Gio.File) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7feb1a362370>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Firmware), '__module__': 'gi.repository.FwupdPlugin', '__gtype__': <GType void (4)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_bytes': gi.FunctionInfo(new_from_bytes), 'strparse_uint16': gi.FunctionInfo(strparse_uint16), 'strparse_uint24': gi.FunctionInfo(strparse_uint24), 'strparse_uint32': gi.FunctionInfo(strparse_uint32), 'strparse_uint4': gi.FunctionInfo(strparse_uint4), 'strparse_uint8': gi.FunctionInfo(strparse_uint8), 'add_image': gi.FunctionInfo(add_image), 'get_image_by_id': gi.FunctionInfo(get_image_by_id), 'get_image_by_id_bytes': gi.FunctionInfo(get_image_by_id_bytes), 'get_image_by_idx': gi.FunctionInfo(get_image_by_idx), 'get_image_by_idx_bytes': gi.FunctionInfo(get_image_by_idx_bytes), 'get_image_default': gi.FunctionInfo(get_image_default), 'get_image_default_bytes': gi.FunctionInfo(get_image_default_bytes), 'get_images': gi.FunctionInfo(get_images), 'get_version': gi.FunctionInfo(get_version), 'parse': gi.FunctionInfo(parse), 'parse_file': gi.FunctionInfo(parse_file), 'parse_full': gi.FunctionInfo(parse_full), 'set_version': gi.FunctionInfo(set_version), 'to_string': gi.FunctionInfo(to_string), 'tokenize': gi.FunctionInfo(tokenize), 'write': gi.FunctionInfo(write), 'write_file': gi.FunctionInfo(write_file), 'do_parse': gi.VFuncInfo(parse), 'do_to_string': gi.VFuncInfo(to_string), 'do_tokenize': gi.VFuncInfo(tokenize), 'do_write': gi.VFuncInfo(write), 'parent_instance': <property object at 0x7feb1afdf270>})"
    __gdoc__ = 'void\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = ObjectInfo(Firmware)


