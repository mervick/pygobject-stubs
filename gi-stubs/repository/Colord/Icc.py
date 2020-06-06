# encoding: utf-8
# module gi.repository.Colord
# from /usr/lib64/girepository-1.0/Colord-1.0.typelib
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


class Icc(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Icc(**properties)
        new() -> Colord.Icc
    """
    def add_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ add_metadata(self, key:str, value:str) """
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

    def create_default(self): # real signature unknown; restored from __doc__
        """ create_default(self) -> bool """
        return False

    def create_from_edid(self, gamma_value, red, green, blue, white): # real signature unknown; restored from __doc__
        """ create_from_edid(self, gamma_value:float, red:Colord.ColorYxy, green:Colord.ColorYxy, blue:Colord.ColorYxy, white:Colord.ColorYxy) -> bool """
        return False

    def create_from_edid_data(self, edid): # real signature unknown; restored from __doc__
        """ create_from_edid_data(self, edid:Colord.Edid) -> bool """
        return False

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

    def get_blue(self): # real signature unknown; restored from __doc__
        """ get_blue(self) -> Colord.ColorXYZ """
        pass

    def get_can_delete(self): # real signature unknown; restored from __doc__
        """ get_can_delete(self) -> bool """
        return False

    def get_characterization_data(self): # real signature unknown; restored from __doc__
        """ get_characterization_data(self) -> str """
        return ""

    def get_checksum(self): # real signature unknown; restored from __doc__
        """ get_checksum(self) -> str """
        return ""

    def get_colorspace(self): # real signature unknown; restored from __doc__
        """ get_colorspace(self) -> Colord.Colorspace """
        pass

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) """
        pass

    def get_copyright(self, locale): # real signature unknown; restored from __doc__
        """ get_copyright(self, locale:str) -> str """
        return ""

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> GLib.DateTime """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self, locale): # real signature unknown; restored from __doc__
        """ get_description(self, locale:str) -> str """
        return ""

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_green(self): # real signature unknown; restored from __doc__
        """ get_green(self) -> Colord.ColorXYZ """
        pass

    def get_handle(self): # real signature unknown; restored from __doc__
        """ get_handle(self) """
        pass

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> Colord.ProfileKind """
        pass

    def get_manufacturer(self, locale): # real signature unknown; restored from __doc__
        """ get_manufacturer(self, locale:str) -> str """
        return ""

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> dict """
        return {}

    def get_metadata_item(self, key): # real signature unknown; restored from __doc__
        """ get_metadata_item(self, key:str) -> str """
        return ""

    def get_model(self, locale): # real signature unknown; restored from __doc__
        """ get_model(self, locale:str) -> str """
        return ""

    def get_named_colors(self): # real signature unknown; restored from __doc__
        """ get_named_colors(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_red(self): # real signature unknown; restored from __doc__
        """ get_red(self) -> Colord.ColorXYZ """
        pass

    def get_response(self, size): # real signature unknown; restored from __doc__
        """ get_response(self, size:int) -> list """
        return []

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_tags(self): # real signature unknown; restored from __doc__
        """ get_tags(self) -> list """
        return []

    def get_tag_data(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_data(self, tag:str) -> GLib.Bytes """
        pass

    def get_temperature(self): # real signature unknown; restored from __doc__
        """ get_temperature(self) -> int """
        return 0

    def get_vcgt(self, size): # real signature unknown; restored from __doc__
        """ get_vcgt(self, size:int) -> list """
        return []

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> float """
        return 0.0

    def get_warnings(self): # real signature unknown; restored from __doc__
        """ get_warnings(self) -> list """
        return []

    def get_white(self): # real signature unknown; restored from __doc__
        """ get_white(self) -> Colord.ColorXYZ """
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

    def load_data(self, data, data_len, flags): # real signature unknown; restored from __doc__
        """ load_data(self, data:int, data_len:int, flags:Colord.IccLoadFlags) -> bool """
        return False

    def load_fd(self, fd, flags): # real signature unknown; restored from __doc__
        """ load_fd(self, fd:int, flags:Colord.IccLoadFlags) -> bool """
        return False

    def load_file(self, file, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ load_file(self, file:Gio.File, flags:Colord.IccLoadFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def load_handle(self, handle=None, flags): # real signature unknown; restored from __doc__
        """ load_handle(self, handle=None, flags:Colord.IccLoadFlags) -> bool """
        return False

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Colord.Icc """
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

    def remove_metadata(self, key): # real signature unknown; restored from __doc__
        """ remove_metadata(self, key:str) """
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

    def save_data(self, flags): # real signature unknown; restored from __doc__
        """ save_data(self, flags:Colord.IccSaveFlags) -> GLib.Bytes """
        pass

    def save_default(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ save_default(self, flags:Colord.IccSaveFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def save_file(self, file, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ save_file(self, file:Gio.File, flags:Colord.IccSaveFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_characterization_data(self, data): # real signature unknown; restored from __doc__
        """ set_characterization_data(self, data:str) """
        pass

    def set_colorspace(self, colorspace): # real signature unknown; restored from __doc__
        """ set_colorspace(self, colorspace:Colord.Colorspace) """
        pass

    def set_copyright(self, locale, value=None): # real signature unknown; restored from __doc__
        """ set_copyright(self, locale:str, value:str=None) """
        pass

    def set_copyright_items(self, values): # real signature unknown; restored from __doc__
        """ set_copyright_items(self, values:dict) """
        pass

    def set_created(self, creation_time): # real signature unknown; restored from __doc__
        """ set_created(self, creation_time:GLib.DateTime) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, locale, value=None): # real signature unknown; restored from __doc__
        """ set_description(self, locale:str, value:str=None) """
        pass

    def set_description_items(self, values): # real signature unknown; restored from __doc__
        """ set_description_items(self, values:dict) """
        pass

    def set_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_filename(self, filename:str) """
        pass

    def set_kind(self, kind): # real signature unknown; restored from __doc__
        """ set_kind(self, kind:Colord.ProfileKind) """
        pass

    def set_manufacturer(self, locale, value=None): # real signature unknown; restored from __doc__
        """ set_manufacturer(self, locale:str, value:str=None) """
        pass

    def set_manufacturer_items(self, values): # real signature unknown; restored from __doc__
        """ set_manufacturer_items(self, values:dict) """
        pass

    def set_model(self, locale, value=None): # real signature unknown; restored from __doc__
        """ set_model(self, locale:str, value:str=None) """
        pass

    def set_model_items(self, values): # real signature unknown; restored from __doc__
        """ set_model_items(self, values:dict) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_tag_data(self, tag, data): # real signature unknown; restored from __doc__
        """ set_tag_data(self, tag:str, data:GLib.Bytes) -> bool """
        return False

    def set_vcgt(self, vcgt): # real signature unknown; restored from __doc__
        """ set_vcgt(self, vcgt:list) -> bool """
        return False

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:float) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f091320ceb0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Icc), '__module__': 'gi.repository.Colord', '__gtype__': <GType CdIcc (94892598885392)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'error_quark': gi.FunctionInfo(error_quark), 'add_metadata': gi.FunctionInfo(add_metadata), 'create_default': gi.FunctionInfo(create_default), 'create_from_edid': gi.FunctionInfo(create_from_edid), 'create_from_edid_data': gi.FunctionInfo(create_from_edid_data), 'get_blue': gi.FunctionInfo(get_blue), 'get_can_delete': gi.FunctionInfo(get_can_delete), 'get_characterization_data': gi.FunctionInfo(get_characterization_data), 'get_checksum': gi.FunctionInfo(get_checksum), 'get_colorspace': gi.FunctionInfo(get_colorspace), 'get_context': gi.FunctionInfo(get_context), 'get_copyright': gi.FunctionInfo(get_copyright), 'get_created': gi.FunctionInfo(get_created), 'get_description': gi.FunctionInfo(get_description), 'get_filename': gi.FunctionInfo(get_filename), 'get_green': gi.FunctionInfo(get_green), 'get_handle': gi.FunctionInfo(get_handle), 'get_kind': gi.FunctionInfo(get_kind), 'get_manufacturer': gi.FunctionInfo(get_manufacturer), 'get_metadata': gi.FunctionInfo(get_metadata), 'get_metadata_item': gi.FunctionInfo(get_metadata_item), 'get_model': gi.FunctionInfo(get_model), 'get_named_colors': gi.FunctionInfo(get_named_colors), 'get_red': gi.FunctionInfo(get_red), 'get_response': gi.FunctionInfo(get_response), 'get_size': gi.FunctionInfo(get_size), 'get_tag_data': gi.FunctionInfo(get_tag_data), 'get_tags': gi.FunctionInfo(get_tags), 'get_temperature': gi.FunctionInfo(get_temperature), 'get_vcgt': gi.FunctionInfo(get_vcgt), 'get_version': gi.FunctionInfo(get_version), 'get_warnings': gi.FunctionInfo(get_warnings), 'get_white': gi.FunctionInfo(get_white), 'load_data': gi.FunctionInfo(load_data), 'load_fd': gi.FunctionInfo(load_fd), 'load_file': gi.FunctionInfo(load_file), 'load_handle': gi.FunctionInfo(load_handle), 'remove_metadata': gi.FunctionInfo(remove_metadata), 'save_data': gi.FunctionInfo(save_data), 'save_default': gi.FunctionInfo(save_default), 'save_file': gi.FunctionInfo(save_file), 'set_characterization_data': gi.FunctionInfo(set_characterization_data), 'set_colorspace': gi.FunctionInfo(set_colorspace), 'set_copyright': gi.FunctionInfo(set_copyright), 'set_copyright_items': gi.FunctionInfo(set_copyright_items), 'set_created': gi.FunctionInfo(set_created), 'set_description': gi.FunctionInfo(set_description), 'set_description_items': gi.FunctionInfo(set_description_items), 'set_filename': gi.FunctionInfo(set_filename), 'set_kind': gi.FunctionInfo(set_kind), 'set_manufacturer': gi.FunctionInfo(set_manufacturer), 'set_manufacturer_items': gi.FunctionInfo(set_manufacturer_items), 'set_model': gi.FunctionInfo(set_model), 'set_model_items': gi.FunctionInfo(set_model_items), 'set_tag_data': gi.FunctionInfo(set_tag_data), 'set_vcgt': gi.FunctionInfo(set_vcgt), 'set_version': gi.FunctionInfo(set_version), 'to_string': gi.FunctionInfo(to_string), 'parent_instance': <property object at 0x7f091337dcc0>})"
    __gdoc__ = 'Object CdIcc\n\nProperties from CdIcc:\n  size -> guint: size\n  filename -> gchararray: filename\n  version -> gdouble: version\n  kind -> guint: kind\n  colorspace -> guint: colorspace\n  can-delete -> gboolean: can-delete\n  checksum -> gchararray: checksum\n  red -> CdColorXYZ: red\n  green -> CdColorXYZ: green\n  blue -> CdColorXYZ: blue\n  white -> CdColorXYZ: white\n  temperature -> guint: temperature\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CdIcc (94892598885392)>'
    __info__ = ObjectInfo(Icc)


