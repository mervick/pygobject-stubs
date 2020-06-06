# encoding: utf-8
# module gi.repository.ICalGLib
# from /usr/lib64/girepository-1.0/ICalGLib-3.0.typelib
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


from .Object import Object

class Timezone(Object):
    """
    :Constructors:
    
    ::
    
        Timezone(**properties)
        array_new() -> ICalGLib.Array
        new() -> ICalGLib.Timezone or None
    """
    def add_depender(self, depender): # real signature unknown; restored from __doc__
        """ add_depender(self, depender:GObject.Object) """
        pass

    def array_append_from_vtimezone(self, timezones, child): # real signature unknown; restored from __doc__
        """ array_append_from_vtimezone(timezones:ICalGLib.Array, child:ICalGLib.Component) """
        pass

    def array_element_at(self, timezones, index): # real signature unknown; restored from __doc__
        """ array_element_at(timezones:ICalGLib.Array, index:int) -> ICalGLib.Timezone """
        pass

    def array_new(self): # real signature unknown; restored from __doc__
        """ array_new() -> ICalGLib.Array """
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

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ICalGLib.Timezone """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dump_changes(self, max_year, fp=None): # real signature unknown; restored from __doc__
        """ dump_changes(self, max_year:int, fp=None) -> int """
        return 0

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

    def free_builtin_timezones(self): # real signature unknown; restored from __doc__
        """ free_builtin_timezones() """
        pass

    def free_global_objects(self): # real signature unknown; restored from __doc__
        """ free_global_objects() """
        pass

    def free_zone_directory(self): # real signature unknown; restored from __doc__
        """ free_zone_directory() """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_builtin_timezone(self, location=None): # real signature unknown; restored from __doc__
        """ get_builtin_timezone(location:str=None) -> ICalGLib.Timezone or None """
        pass

    def get_builtin_timezones(self): # real signature unknown; restored from __doc__
        """ get_builtin_timezones() -> ICalGLib.Array """
        pass

    def get_builtin_timezone_from_offset(self, offset, tzname=None): # real signature unknown; restored from __doc__
        """ get_builtin_timezone_from_offset(offset:int, tzname:str=None) -> ICalGLib.Timezone """
        pass

    def get_builtin_timezone_from_tzid(self, tzid=None): # real signature unknown; restored from __doc__
        """ get_builtin_timezone_from_tzid(tzid:str=None) -> ICalGLib.Timezone """
        pass

    def get_builtin_tzdata(self): # real signature unknown; restored from __doc__
        """ get_builtin_tzdata() -> bool """
        return False

    def get_component(self): # real signature unknown; restored from __doc__
        """ get_component(self) -> ICalGLib.Component """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_is_global_memory(self): # real signature unknown; restored from __doc__
        """ get_is_global_memory(self) -> bool """
        return False

    def get_latitude(self): # real signature unknown; restored from __doc__
        """ get_latitude(self) -> float """
        return 0.0

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> str or None """
        return ""

    def get_location_from_vtimezone(self, component): # real signature unknown; restored from __doc__
        """ get_location_from_vtimezone(component:ICalGLib.Component) -> str """
        return ""

    def get_longitude(self): # real signature unknown; restored from __doc__
        """ get_longitude(self) -> float """
        return 0.0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_tzid(self): # real signature unknown; restored from __doc__
        """ get_tzid(self) -> str or None """
        return ""

    def get_tznames(self): # real signature unknown; restored from __doc__
        """ get_tznames(self) -> str or None """
        return ""

    def get_tznames_from_vtimezone(self, component): # real signature unknown; restored from __doc__
        """ get_tznames_from_vtimezone(component:ICalGLib.Component) -> str """
        return ""

    def get_utc_offset(self, tt=None): # real signature unknown; restored from __doc__
        """ get_utc_offset(self, tt:ICalGLib.Time=None) -> int, is_daylight:int """
        return 0

    def get_utc_offset_of_utc_time(self, tt): # real signature unknown; restored from __doc__
        """ get_utc_offset_of_utc_time(self, tt:ICalGLib.Time) -> int, is_daylight:int """
        return 0

    def get_utc_timezone(self): # real signature unknown; restored from __doc__
        """ get_utc_timezone() -> ICalGLib.Timezone """
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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ICalGLib.Timezone or None """
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

    def ref_owner(self): # real signature unknown; restored from __doc__
        """ ref_owner(self) -> GObject.Object or None """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def release_zone_tab(self): # real signature unknown; restored from __doc__
        """ release_zone_tab() """
        pass

    def remove_depender(self, depender): # real signature unknown; restored from __doc__
        """ remove_depender(self, depender:GObject.Object) """
        pass

    def remove_owner(self): # real signature unknown; restored from __doc__
        """ remove_owner(self) """
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

    def set_builtin_tzdata(self, set): # real signature unknown; restored from __doc__
        """ set_builtin_tzdata(set:bool) """
        pass

    def set_component(self, comp): # real signature unknown; restored from __doc__
        """ set_component(self, comp:ICalGLib.Component) -> int """
        return 0

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_native_destroy_func(self, native_destroy_func): # real signature unknown; restored from __doc__
        """ set_native_destroy_func(self, native_destroy_func:GLib.DestroyNotify) """
        pass

    def set_owner(self, owner): # real signature unknown; restored from __doc__
        """ set_owner(self, owner:GObject.Object) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_tzid_prefix(self, new_prefix): # real signature unknown; restored from __doc__
        """ set_tzid_prefix(new_prefix:str) """
        pass

    def set_zone_directory(self, path): # real signature unknown; restored from __doc__
        """ set_zone_directory(path:str) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_native(self): # real signature unknown; restored from __doc__
        """ steal_native(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1351ed1bb0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Timezone), '__module__': 'gi.repository.ICalGLib', '__gtype__': <GType ICalTimezone (94403188540432)>, '__doc__': None, '__gsignals__': {}, 'array_new': gi.FunctionInfo(array_new), 'new': gi.FunctionInfo(new), 'array_append_from_vtimezone': gi.FunctionInfo(array_append_from_vtimezone), 'array_element_at': gi.FunctionInfo(array_element_at), 'free_builtin_timezones': gi.FunctionInfo(free_builtin_timezones), 'free_zone_directory': gi.FunctionInfo(free_zone_directory), 'get_builtin_timezone': gi.FunctionInfo(get_builtin_timezone), 'get_builtin_timezone_from_offset': gi.FunctionInfo(get_builtin_timezone_from_offset), 'get_builtin_timezone_from_tzid': gi.FunctionInfo(get_builtin_timezone_from_tzid), 'get_builtin_timezones': gi.FunctionInfo(get_builtin_timezones), 'get_builtin_tzdata': gi.FunctionInfo(get_builtin_tzdata), 'get_location_from_vtimezone': gi.FunctionInfo(get_location_from_vtimezone), 'get_tznames_from_vtimezone': gi.FunctionInfo(get_tznames_from_vtimezone), 'get_utc_timezone': gi.FunctionInfo(get_utc_timezone), 'release_zone_tab': gi.FunctionInfo(release_zone_tab), 'set_builtin_tzdata': gi.FunctionInfo(set_builtin_tzdata), 'set_tzid_prefix': gi.FunctionInfo(set_tzid_prefix), 'set_zone_directory': gi.FunctionInfo(set_zone_directory), 'copy': gi.FunctionInfo(copy), 'dump_changes': gi.FunctionInfo(dump_changes), 'get_component': gi.FunctionInfo(get_component), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_latitude': gi.FunctionInfo(get_latitude), 'get_location': gi.FunctionInfo(get_location), 'get_longitude': gi.FunctionInfo(get_longitude), 'get_tzid': gi.FunctionInfo(get_tzid), 'get_tznames': gi.FunctionInfo(get_tznames), 'get_utc_offset': gi.FunctionInfo(get_utc_offset), 'get_utc_offset_of_utc_time': gi.FunctionInfo(get_utc_offset_of_utc_time), 'set_component': gi.FunctionInfo(set_component)})"
    __gdoc__ = 'Object ICalTimezone\n\nProperties from ICalObject:\n  native -> gpointer: Native\n    Native libical structure\n  native-destroy-func -> gpointer: Native-Destroy-Func\n    GDestroyNotify function to use to destroy the native libical structure\n  is-global-memory -> gboolean: Is-Global-Memory\n    Whether the native libical structure is from a global shared memory\n  owner -> GObject: Owner\n    The native libical structure owner\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ICalTimezone (94403188540432)>'
    __info__ = ObjectInfo(Timezone)


