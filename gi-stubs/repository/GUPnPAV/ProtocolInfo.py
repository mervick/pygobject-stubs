# encoding: utf-8
# module gi.repository.GUPnPAV
# from /usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib
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


class ProtocolInfo(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        ProtocolInfo(**properties)
        new() -> GUPnPAV.ProtocolInfo
        new_from_string(protocol_info:str) -> GUPnPAV.ProtocolInfo
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

    def get_dlna_conversion(self): # real signature unknown; restored from __doc__
        """ get_dlna_conversion(self) -> GUPnPAV.DLNAConversion """
        pass

    def get_dlna_flags(self): # real signature unknown; restored from __doc__
        """ get_dlna_flags(self) -> GUPnPAV.DLNAFlags """
        pass

    def get_dlna_operation(self): # real signature unknown; restored from __doc__
        """ get_dlna_operation(self) -> GUPnPAV.DLNAOperation """
        pass

    def get_dlna_profile(self): # real signature unknown; restored from __doc__
        """ get_dlna_profile(self) -> str """
        return ""

    def get_mime_type(self): # real signature unknown; restored from __doc__
        """ get_mime_type(self) -> str """
        return ""

    def get_network(self): # real signature unknown; restored from __doc__
        """ get_network(self) -> str """
        return ""

    def get_play_speeds(self): # real signature unknown; restored from __doc__
        """ get_play_speeds(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def is_compatible(self, info2): # real signature unknown; restored from __doc__
        """ is_compatible(self, info2:GUPnPAV.ProtocolInfo) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> GUPnPAV.ProtocolInfo """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_string(self, protocol_info): # real signature unknown; restored from __doc__
        """ new_from_string(protocol_info:str) -> GUPnPAV.ProtocolInfo """
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

    def set_dlna_conversion(self, conversion): # real signature unknown; restored from __doc__
        """ set_dlna_conversion(self, conversion:GUPnPAV.DLNAConversion) """
        pass

    def set_dlna_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_dlna_flags(self, flags:GUPnPAV.DLNAFlags) """
        pass

    def set_dlna_operation(self, operation): # real signature unknown; restored from __doc__
        """ set_dlna_operation(self, operation:GUPnPAV.DLNAOperation) """
        pass

    def set_dlna_profile(self, profile): # real signature unknown; restored from __doc__
        """ set_dlna_profile(self, profile:str) """
        pass

    def set_mime_type(self, mime_type): # real signature unknown; restored from __doc__
        """ set_mime_type(self, mime_type:str) """
        pass

    def set_network(self, network): # real signature unknown; restored from __doc__
        """ set_network(self, network:str) """
        pass

    def set_play_speeds(self, speeds): # real signature unknown; restored from __doc__
        """ set_play_speeds(self, speeds:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ set_protocol(self, protocol:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fda4df67a90>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ProtocolInfo), '__module__': 'gi.repository.GUPnPAV', '__gtype__': <GType GUPnPProtocolInfo (94653145952816)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_string': gi.FunctionInfo(new_from_string), 'get_dlna_conversion': gi.FunctionInfo(get_dlna_conversion), 'get_dlna_flags': gi.FunctionInfo(get_dlna_flags), 'get_dlna_operation': gi.FunctionInfo(get_dlna_operation), 'get_dlna_profile': gi.FunctionInfo(get_dlna_profile), 'get_mime_type': gi.FunctionInfo(get_mime_type), 'get_network': gi.FunctionInfo(get_network), 'get_play_speeds': gi.FunctionInfo(get_play_speeds), 'get_protocol': gi.FunctionInfo(get_protocol), 'is_compatible': gi.FunctionInfo(is_compatible), 'set_dlna_conversion': gi.FunctionInfo(set_dlna_conversion), 'set_dlna_flags': gi.FunctionInfo(set_dlna_flags), 'set_dlna_operation': gi.FunctionInfo(set_dlna_operation), 'set_dlna_profile': gi.FunctionInfo(set_dlna_profile), 'set_mime_type': gi.FunctionInfo(set_mime_type), 'set_network': gi.FunctionInfo(set_network), 'set_play_speeds': gi.FunctionInfo(set_play_speeds), 'set_protocol': gi.FunctionInfo(set_protocol), 'to_string': gi.FunctionInfo(to_string), 'parent': <property object at 0x7fda4e18dbd0>, 'priv': <property object at 0x7fda4e18dcc0>})"
    __gdoc__ = 'Object GUPnPProtocolInfo\n\nProperties from GUPnPProtocolInfo:\n  protocol -> gchararray: Protocol\n    The protocol of this info.\n  network -> gchararray: Network\n    The network this info is associated with.\n  mime-type -> gchararray: MIMEType\n    The MIME-type of this info.\n  dlna-profile -> gchararray: DLNAProfile\n    The DLNA profile of this info.\n  play-speeds -> GStrv: PlaySpeeds\n    The allowed play speeds on this info in the form of array of strings.\n  dlna-conversion -> GUPnPDLNAConversion: DLNAConversion\n    The DLNA conversion flags.\n  dlna-operation -> GUPnPDLNAOperation: DLNAOperation\n    The DLNA operation flags.\n  dlna-flags -> GUPnPDLNAFlags: DLNAFlags\n    Various generic DLNA flags.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GUPnPProtocolInfo (94653145952816)>'
    __info__ = ObjectInfo(ProtocolInfo)


