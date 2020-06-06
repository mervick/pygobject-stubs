# encoding: utf-8
# module gi.repository.RygelServer
# from /usr/lib64/girepository-1.0/RygelServer-2.6.typelib
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
import gi.repository.Gee as __gi_repository_Gee
import gi.repository.GUPnP as __gi_repository_GUPnP
import gi.repository.RygelCore as __gi_repository_RygelCore
import gobject as __gobject


class MediaResource(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        MediaResource(**properties)
        new(name:str) -> RygelServer.MediaResource
        from_resource(name:str, that:RygelServer.MediaResource) -> RygelServer.MediaResource
        from_didl_lite_resource(name:str, didl_resource:GUPnPAV.DIDLLiteResource) -> RygelServer.MediaResource
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

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> RygelServer.MediaResource """
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

    def from_didl_lite_resource(self, name, didl_resource): # real signature unknown; restored from __doc__
        """ from_didl_lite_resource(name:str, didl_resource:GUPnPAV.DIDLLiteResource) -> RygelServer.MediaResource """
        pass

    def from_resource(self, name, that): # real signature unknown; restored from __doc__
        """ from_resource(name:str, that:RygelServer.MediaResource) -> RygelServer.MediaResource """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_audio_channels(self): # real signature unknown; restored from __doc__
        """ get_audio_channels(self) -> int """
        return 0

    def get_bitrate(self): # real signature unknown; restored from __doc__
        """ get_bitrate(self) -> int """
        return 0

    def get_bits_per_sample(self): # real signature unknown; restored from __doc__
        """ get_bits_per_sample(self) -> int """
        return 0

    def get_cleartext_size(self): # real signature unknown; restored from __doc__
        """ get_cleartext_size(self) -> int """
        return 0

    def get_color_depth(self): # real signature unknown; restored from __doc__
        """ get_color_depth(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_transfer_mode(self): # real signature unknown; restored from __doc__
        """ get_default_transfer_mode(self) -> str """
        return ""

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

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> int """
        return 0

    def get_extension(self): # real signature unknown; restored from __doc__
        """ get_extension(self) -> str """
        return ""

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_import_uri(self): # real signature unknown; restored from __doc__
        """ get_import_uri(self) -> str """
        return ""

    def get_mime_type(self): # real signature unknown; restored from __doc__
        """ get_mime_type(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_network(self): # real signature unknown; restored from __doc__
        """ get_network(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> str """
        return ""

    def get_protocol_info(self, replacements=None): # real signature unknown; restored from __doc__
        """ get_protocol_info(self, replacements:dict=None) -> GUPnPAV.ProtocolInfo """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sample_freq(self): # real signature unknown; restored from __doc__
        """ get_sample_freq(self) -> int """
        return 0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

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

    def is_cleartext_range_support_enabled(self): # real signature unknown; restored from __doc__
        """ is_cleartext_range_support_enabled(self) -> bool """
        return False

    def is_dlna_content(self): # real signature unknown; restored from __doc__
        """ is_dlna_content(self) -> bool """
        return False

    def is_dlna_operation_mode_set(self, flags): # real signature unknown; restored from __doc__
        """ is_dlna_operation_mode_set(self, flags:int) -> bool """
        return False

    def is_dlna_protocol_flag_set(self, flags): # real signature unknown; restored from __doc__
        """ is_dlna_protocol_flag_set(self, flags:int) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_link_protection_enabled(self): # real signature unknown; restored from __doc__
        """ is_link_protection_enabled(self) -> bool """
        return False

    def is_streamable(self): # real signature unknown; restored from __doc__
        """ is_streamable(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, name): # real signature unknown; restored from __doc__
        """ new(name:str) -> RygelServer.MediaResource """
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

    def serialize(self, didl_resource, replacements=None): # real signature unknown; restored from __doc__
        """ serialize(self, didl_resource:GUPnPAV.DIDLLiteResource, replacements:dict=None) -> GUPnPAV.DIDLLiteResource """
        pass

    def set_audio_channels(self, value): # real signature unknown; restored from __doc__
        """ set_audio_channels(self, value:int) """
        pass

    def set_bitrate(self, value): # real signature unknown; restored from __doc__
        """ set_bitrate(self, value:int) """
        pass

    def set_bits_per_sample(self, value): # real signature unknown; restored from __doc__
        """ set_bits_per_sample(self, value:int) """
        pass

    def set_cleartext_size(self, value): # real signature unknown; restored from __doc__
        """ set_cleartext_size(self, value:int) """
        pass

    def set_color_depth(self, value): # real signature unknown; restored from __doc__
        """ set_color_depth(self, value:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_dlna_conversion(self, value): # real signature unknown; restored from __doc__
        """ set_dlna_conversion(self, value:GUPnPAV.DLNAConversion) """
        pass

    def set_dlna_flags(self, value): # real signature unknown; restored from __doc__
        """ set_dlna_flags(self, value:GUPnPAV.DLNAFlags) """
        pass

    def set_dlna_operation(self, value): # real signature unknown; restored from __doc__
        """ set_dlna_operation(self, value:GUPnPAV.DLNAOperation) """
        pass

    def set_dlna_profile(self, value): # real signature unknown; restored from __doc__
        """ set_dlna_profile(self, value:str) """
        pass

    def set_duration(self, value): # real signature unknown; restored from __doc__
        """ set_duration(self, value:int) """
        pass

    def set_extension(self, value): # real signature unknown; restored from __doc__
        """ set_extension(self, value:str) """
        pass

    def set_height(self, value): # real signature unknown; restored from __doc__
        """ set_height(self, value:int) """
        pass

    def set_import_uri(self, value): # real signature unknown; restored from __doc__
        """ set_import_uri(self, value:str) """
        pass

    def set_mime_type(self, value): # real signature unknown; restored from __doc__
        """ set_mime_type(self, value:str) """
        pass

    def set_network(self, value): # real signature unknown; restored from __doc__
        """ set_network(self, value:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_protocol(self, value): # real signature unknown; restored from __doc__
        """ set_protocol(self, value:str) """
        pass

    def set_protocol_info(self, pi): # real signature unknown; restored from __doc__
        """ set_protocol_info(self, pi:GUPnPAV.ProtocolInfo) """
        pass

    def set_sample_freq(self, value): # real signature unknown; restored from __doc__
        """ set_sample_freq(self, value:int) """
        pass

    def set_size(self, value): # real signature unknown; restored from __doc__
        """ set_size(self, value:int) """
        pass

    def set_uri(self, value): # real signature unknown; restored from __doc__
        """ set_uri(self, value:str) """
        pass

    def set_width(self, value): # real signature unknown; restored from __doc__
        """ set_width(self, value:int) """
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

    def supports_arbitrary_byte_seek(self): # real signature unknown; restored from __doc__
        """ supports_arbitrary_byte_seek(self) -> bool """
        return False

    def supports_arbitrary_time_seek(self): # real signature unknown; restored from __doc__
        """ supports_arbitrary_time_seek(self) -> bool """
        return False

    def supports_full_cleartext_byte_seek(self): # real signature unknown; restored from __doc__
        """ supports_full_cleartext_byte_seek(self) -> bool """
        return False

    def supports_limited_byte_seek(self): # real signature unknown; restored from __doc__
        """ supports_limited_byte_seek(self) -> bool """
        return False

    def supports_limited_cleartext_byte_seek(self): # real signature unknown; restored from __doc__
        """ supports_limited_cleartext_byte_seek(self) -> bool """
        return False

    def supports_limited_time_seek(self): # real signature unknown; restored from __doc__
        """ supports_limited_time_seek(self) -> bool """
        return False

    def supports_playspeed(self): # real signature unknown; restored from __doc__
        """ supports_playspeed(self) -> bool """
        return False

    def supports_transfer_mode(self, transfer_mode): # real signature unknown; restored from __doc__
        """ supports_transfer_mode(self, transfer_mode:str) -> bool """
        return False

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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    play_speeds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fe1d16939a0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MediaResource), '__module__': 'gi.repository.RygelServer', '__gtype__': <GType RygelMediaResource (94219762608432)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'from_resource': gi.FunctionInfo(from_resource), 'from_didl_lite_resource': gi.FunctionInfo(from_didl_lite_resource), 'dup': gi.FunctionInfo(dup), 'get_name': gi.FunctionInfo(get_name), 'serialize': gi.FunctionInfo(serialize), 'set_protocol_info': gi.FunctionInfo(set_protocol_info), 'get_protocol_info': gi.FunctionInfo(get_protocol_info), 'supports_arbitrary_byte_seek': gi.FunctionInfo(supports_arbitrary_byte_seek), 'supports_arbitrary_time_seek': gi.FunctionInfo(supports_arbitrary_time_seek), 'supports_limited_byte_seek': gi.FunctionInfo(supports_limited_byte_seek), 'supports_limited_time_seek': gi.FunctionInfo(supports_limited_time_seek), 'supports_limited_cleartext_byte_seek': gi.FunctionInfo(supports_limited_cleartext_byte_seek), 'supports_full_cleartext_byte_seek': gi.FunctionInfo(supports_full_cleartext_byte_seek), 'is_link_protection_enabled': gi.FunctionInfo(is_link_protection_enabled), 'is_dlna_content': gi.FunctionInfo(is_dlna_content), 'get_default_transfer_mode': gi.FunctionInfo(get_default_transfer_mode), 'supports_transfer_mode': gi.FunctionInfo(supports_transfer_mode), 'is_streamable': gi.FunctionInfo(is_streamable), 'is_cleartext_range_support_enabled': gi.FunctionInfo(is_cleartext_range_support_enabled), 'supports_playspeed': gi.FunctionInfo(supports_playspeed), 'is_dlna_protocol_flag_set': gi.FunctionInfo(is_dlna_protocol_flag_set), 'is_dlna_operation_mode_set': gi.FunctionInfo(is_dlna_operation_mode_set), 'to_string': gi.FunctionInfo(to_string), 'get_uri': gi.FunctionInfo(get_uri), 'set_uri': gi.FunctionInfo(set_uri), 'get_import_uri': gi.FunctionInfo(get_import_uri), 'set_import_uri': gi.FunctionInfo(set_import_uri), 'get_extension': gi.FunctionInfo(get_extension), 'set_extension': gi.FunctionInfo(set_extension), 'get_size': gi.FunctionInfo(get_size), 'set_size': gi.FunctionInfo(set_size), 'get_cleartext_size': gi.FunctionInfo(get_cleartext_size), 'set_cleartext_size': gi.FunctionInfo(set_cleartext_size), 'get_duration': gi.FunctionInfo(get_duration), 'set_duration': gi.FunctionInfo(set_duration), 'get_bitrate': gi.FunctionInfo(get_bitrate), 'set_bitrate': gi.FunctionInfo(set_bitrate), 'get_bits_per_sample': gi.FunctionInfo(get_bits_per_sample), 'set_bits_per_sample': gi.FunctionInfo(set_bits_per_sample), 'get_color_depth': gi.FunctionInfo(get_color_depth), 'set_color_depth': gi.FunctionInfo(set_color_depth), 'get_width': gi.FunctionInfo(get_width), 'set_width': gi.FunctionInfo(set_width), 'get_height': gi.FunctionInfo(get_height), 'set_height': gi.FunctionInfo(set_height), 'get_audio_channels': gi.FunctionInfo(get_audio_channels), 'set_audio_channels': gi.FunctionInfo(set_audio_channels), 'get_sample_freq': gi.FunctionInfo(get_sample_freq), 'set_sample_freq': gi.FunctionInfo(set_sample_freq), 'get_protocol': gi.FunctionInfo(get_protocol), 'set_protocol': gi.FunctionInfo(set_protocol), 'get_mime_type': gi.FunctionInfo(get_mime_type), 'set_mime_type': gi.FunctionInfo(set_mime_type), 'get_dlna_profile': gi.FunctionInfo(get_dlna_profile), 'set_dlna_profile': gi.FunctionInfo(set_dlna_profile), 'get_network': gi.FunctionInfo(get_network), 'set_network': gi.FunctionInfo(set_network), 'get_dlna_conversion': gi.FunctionInfo(get_dlna_conversion), 'set_dlna_conversion': gi.FunctionInfo(set_dlna_conversion), 'get_dlna_flags': gi.FunctionInfo(get_dlna_flags), 'set_dlna_flags': gi.FunctionInfo(set_dlna_flags), 'get_dlna_operation': gi.FunctionInfo(get_dlna_operation), 'set_dlna_operation': gi.FunctionInfo(set_dlna_operation), 'parent_instance': <property object at 0x7fe1d1679c20>, 'priv': <property object at 0x7fe1d1679d10>, 'play_speeds': <property object at 0x7fe1d1679e00>})"
    __gdoc__ = 'Object RygelMediaResource\n\nProperties from RygelMediaResource:\n  uri -> gchararray: uri\n    uri\n  import-uri -> gchararray: import-uri\n    import-uri\n  extension -> gchararray: extension\n    extension\n  size -> gint64: size\n    size\n  cleartext-size -> gint64: cleartext-size\n    cleartext-size\n  duration -> glong: duration\n    duration\n  bitrate -> gint: bitrate\n    bitrate\n  bits-per-sample -> gint: bits-per-sample\n    bits-per-sample\n  color-depth -> gint: color-depth\n    color-depth\n  width -> gint: width\n    width\n  height -> gint: height\n    height\n  audio-channels -> gint: audio-channels\n    audio-channels\n  sample-freq -> gint: sample-freq\n    sample-freq\n  protocol -> gchararray: protocol\n    protocol\n  mime-type -> gchararray: mime-type\n    mime-type\n  dlna-profile -> gchararray: dlna-profile\n    dlna-profile\n  network -> gchararray: network\n    network\n  dlna-conversion -> GUPnPDLNAConversion: dlna-conversion\n    dlna-conversion\n  dlna-flags -> GUPnPDLNAFlags: dlna-flags\n    dlna-flags\n  dlna-operation -> GUPnPDLNAOperation: dlna-operation\n    dlna-operation\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType RygelMediaResource (94219762608432)>'
    __info__ = ObjectInfo(MediaResource)


