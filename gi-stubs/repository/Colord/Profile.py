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


class Profile(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Profile(**properties)
        new() -> Colord.Profile
        new_with_object_path(object_path:str) -> Colord.Profile
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

    def connect(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
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

    def connect_finish(self, res): # real signature unknown; restored from __doc__
        """ connect_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def equal(self, profile2): # real signature unknown; restored from __doc__
        """ equal(self, profile2:Colord.Profile) -> bool """
        return False

    def error_from_string(self, error_desc): # real signature unknown; restored from __doc__
        """ error_from_string(error_desc:str) -> Colord.ProfileError """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def error_to_string(self, error_enum): # real signature unknown; restored from __doc__
        """ error_to_string(error_enum:Colord.ProfileError) -> str """
        return ""

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

    def get_age(self): # real signature unknown; restored from __doc__
        """ get_age(self) -> int """
        return 0

    def get_colorspace(self): # real signature unknown; restored from __doc__
        """ get_colorspace(self) -> Colord.Colorspace """
        pass

    def get_connected(self): # real signature unknown; restored from __doc__
        """ get_connected(self) -> bool """
        return False

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str """
        return ""

    def get_format(self): # real signature unknown; restored from __doc__
        """ get_format(self) -> str """
        return ""

    def get_has_vcgt(self): # real signature unknown; restored from __doc__
        """ get_has_vcgt(self) -> bool """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_is_system_wide(self): # real signature unknown; restored from __doc__
        """ get_is_system_wide(self) -> bool """
        return False

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> Colord.ProfileKind """
        pass

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> dict """
        return {}

    def get_metadata_item(self, key): # real signature unknown; restored from __doc__
        """ get_metadata_item(self, key:str) -> str """
        return ""

    def get_object_path(self): # real signature unknown; restored from __doc__
        """ get_object_path(self) -> str """
        return ""

    def get_owner(self): # real signature unknown; restored from __doc__
        """ get_owner(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_qualifier(self): # real signature unknown; restored from __doc__
        """ get_qualifier(self) -> str """
        return ""

    def get_scope(self): # real signature unknown; restored from __doc__
        """ get_scope(self) -> Colord.ObjectScope """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_warnings(self): # real signature unknown; restored from __doc__
        """ get_warnings(self) -> list """
        return []

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

    def has_access(self): # real signature unknown; restored from __doc__
        """ has_access(self) -> bool """
        return False

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_system_wide(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ install_system_wide(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def install_system_wide_finish(self, res): # real signature unknown; restored from __doc__
        """ install_system_wide_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def install_system_wide_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ install_system_wide_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def kind_from_string(self, profile_kind): # real signature unknown; restored from __doc__
        """ kind_from_string(profile_kind:str) -> Colord.ProfileKind """
        pass

    def kind_to_string(self, profile_kind): # real signature unknown; restored from __doc__
        """ kind_to_string(profile_kind:Colord.ProfileKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load_icc(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ load_icc(self, flags:Colord.IccLoadFlags, cancellable:Gio.Cancellable=None) -> Colord.Icc """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Colord.Profile """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ new_with_object_path(object_path:str) -> Colord.Profile """
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

    def quality_from_string(self, quality): # real signature unknown; restored from __doc__
        """ quality_from_string(quality:str) -> Colord.ProfileQuality """
        pass

    def quality_to_string(self, quality_enum): # real signature unknown; restored from __doc__
        """ quality_to_string(quality_enum:Colord.ProfileQuality) -> str """
        return ""

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

    def set_object_path(self, object_path): # real signature unknown; restored from __doc__
        """ set_object_path(self, object_path:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, key, value, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_property(self, key:str, value:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_property_finish(self, res): # real signature unknown; restored from __doc__
        """ set_property_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def set_property_sync(self, key, value, cancellable=None): # real signature unknown; restored from __doc__
        """ set_property_sync(self, key:str, value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def warning_from_string(self, type): # real signature unknown; restored from __doc__
        """ warning_from_string(type:str) -> Colord.ProfileWarning """
        pass

    def warning_to_string(self, kind_enum): # real signature unknown; restored from __doc__
        """ warning_to_string(kind_enum:Colord.ProfileWarning) -> str """
        return ""

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f091334d7c0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Profile), '__module__': 'gi.repository.Colord', '__gtype__': <GType CdProfile (94892598918624)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_with_object_path': gi.FunctionInfo(new_with_object_path), 'error_from_string': gi.FunctionInfo(error_from_string), 'error_quark': gi.FunctionInfo(error_quark), 'error_to_string': gi.FunctionInfo(error_to_string), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'quality_from_string': gi.FunctionInfo(quality_from_string), 'quality_to_string': gi.FunctionInfo(quality_to_string), 'warning_from_string': gi.FunctionInfo(warning_from_string), 'warning_to_string': gi.FunctionInfo(warning_to_string), 'connect': gi.FunctionInfo(connect), 'connect_finish': gi.FunctionInfo(connect_finish), 'connect_sync': gi.FunctionInfo(connect_sync), 'equal': gi.FunctionInfo(equal), 'get_age': gi.FunctionInfo(get_age), 'get_colorspace': gi.FunctionInfo(get_colorspace), 'get_connected': gi.FunctionInfo(get_connected), 'get_created': gi.FunctionInfo(get_created), 'get_filename': gi.FunctionInfo(get_filename), 'get_format': gi.FunctionInfo(get_format), 'get_has_vcgt': gi.FunctionInfo(get_has_vcgt), 'get_id': gi.FunctionInfo(get_id), 'get_is_system_wide': gi.FunctionInfo(get_is_system_wide), 'get_kind': gi.FunctionInfo(get_kind), 'get_metadata': gi.FunctionInfo(get_metadata), 'get_metadata_item': gi.FunctionInfo(get_metadata_item), 'get_object_path': gi.FunctionInfo(get_object_path), 'get_owner': gi.FunctionInfo(get_owner), 'get_qualifier': gi.FunctionInfo(get_qualifier), 'get_scope': gi.FunctionInfo(get_scope), 'get_title': gi.FunctionInfo(get_title), 'get_warnings': gi.FunctionInfo(get_warnings), 'has_access': gi.FunctionInfo(has_access), 'install_system_wide': gi.FunctionInfo(install_system_wide), 'install_system_wide_finish': gi.FunctionInfo(install_system_wide_finish), 'install_system_wide_sync': gi.FunctionInfo(install_system_wide_sync), 'load_icc': gi.FunctionInfo(load_icc), 'set_object_path': gi.FunctionInfo(set_object_path), 'set_property': gi.FunctionInfo(set_property), 'set_property_finish': gi.FunctionInfo(set_property_finish), 'set_property_sync': gi.FunctionInfo(set_property_sync), 'to_string': gi.FunctionInfo(to_string), 'do_changed': gi.VFuncInfo(changed), 'parent_instance': <property object at 0x7f09131dca90>})"
    __gdoc__ = 'Object CdProfile\n\nSignals from CdProfile:\n  changed ()\n\nProperties from CdProfile:\n  object-path -> gchararray: object-path\n  connected -> gchararray: connected\n  id -> gchararray: id\n  filename -> gchararray: filename\n  qualifier -> gchararray: qualifier\n  format -> gchararray: format\n  title -> gchararray: title\n  kind -> gchararray: kind\n  colorspace -> gchararray: colorspace\n  created -> gint64: created\n  has-vcgt -> gchararray: has-vcgt\n  is-system-wide -> gchararray: is-system-wide\n  scope -> guint: scope\n  owner -> guint: owner\n  warnings -> GStrv: warnings\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType CdProfile (94892598918624)>'
    __info__ = ObjectInfo(Profile)


