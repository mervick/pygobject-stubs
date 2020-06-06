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

class Time(Object):
    """
    :Constructors:
    
    ::
    
        Time(**properties)
        new() -> ICalGLib.Time
        new_current_with_zone(zone:ICalGLib.Timezone=None) -> ICalGLib.Time
        new_from_day_of_year(day:int, year:int) -> ICalGLib.Time
        new_from_string(str:str) -> ICalGLib.Time
        new_from_timet_with_zone(v:int, is_date:int, zone:ICalGLib.Timezone=None) -> ICalGLib.Time
        new_null_date() -> ICalGLib.Time
        new_null_time() -> ICalGLib.Time
        new_today() -> ICalGLib.Time
    """
    def add(self, d): # real signature unknown; restored from __doc__
        """ add(self, d:ICalGLib.Duration) -> ICalGLib.Time """
        pass

    def add_depender(self, depender): # real signature unknown; restored from __doc__
        """ add_depender(self, depender:GObject.Object) """
        pass

    def adjust(self, days, hours, minutes, seconds): # real signature unknown; restored from __doc__
        """ adjust(self, days:int, hours:int, minutes:int, seconds:int) """
        pass

    def as_ical_string(self): # real signature unknown; restored from __doc__
        """ as_ical_string(self) -> str """
        return ""

    def as_timet(self): # real signature unknown; restored from __doc__
        """ as_timet(self) -> int """
        return 0

    def as_timet_with_zone(self, zone=None): # real signature unknown; restored from __doc__
        """ as_timet_with_zone(self, zone:ICalGLib.Timezone=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> ICalGLib.Time """
        pass

    def compare(self, b): # real signature unknown; restored from __doc__
        """ compare(self, b:ICalGLib.Time) -> int """
        return 0

    def compare_date_only(self, b): # real signature unknown; restored from __doc__
        """ compare_date_only(self, b:ICalGLib.Time) -> int """
        return 0

    def compare_date_only_tz(self, b, zone=None): # real signature unknown; restored from __doc__
        """ compare_date_only_tz(self, b:ICalGLib.Time, zone:ICalGLib.Timezone=None) -> int """
        return 0

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

    def convert_timezone(self, from_zone=None, to_zone=None): # real signature unknown; restored from __doc__
        """ convert_timezone(self, from_zone:ICalGLib.Timezone=None, to_zone:ICalGLib.Timezone=None) """
        pass

    def convert_to_zone(self, zone=None): # real signature unknown; restored from __doc__
        """ convert_to_zone(self, zone:ICalGLib.Timezone=None) -> ICalGLib.Time """
        pass

    def convert_to_zone_inplace(self, zone=None): # real signature unknown; restored from __doc__
        """ convert_to_zone_inplace(self, zone:ICalGLib.Timezone=None) """
        pass

    def days_in_month(self, month, year): # real signature unknown; restored from __doc__
        """ days_in_month(month:int, year:int) -> int """
        return 0

    def days_in_year(self, year): # real signature unknown; restored from __doc__
        """ days_in_year(year:int) -> int """
        return 0

    def days_is_leap_year(self, year): # real signature unknown; restored from __doc__
        """ days_is_leap_year(year:int) -> bool """
        return False

    def day_of_week(self): # real signature unknown; restored from __doc__
        """ day_of_week(self) -> int """
        return 0

    def day_of_year(self): # real signature unknown; restored from __doc__
        """ day_of_year(self) -> int """
        return 0

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

    def free_global_objects(self): # real signature unknown; restored from __doc__
        """ free_global_objects() """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date(self): # real signature unknown; restored from __doc__
        """ get_date(self) -> year:int, month:int, day:int """
        pass

    def get_day(self): # real signature unknown; restored from __doc__
        """ get_day(self) -> int """
        return 0

    def get_hour(self): # real signature unknown; restored from __doc__
        """ get_hour(self) -> int """
        return 0

    def get_is_global_memory(self): # real signature unknown; restored from __doc__
        """ get_is_global_memory(self) -> bool """
        return False

    def get_minute(self): # real signature unknown; restored from __doc__
        """ get_minute(self) -> int """
        return 0

    def get_month(self): # real signature unknown; restored from __doc__
        """ get_month(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_second(self): # real signature unknown; restored from __doc__
        """ get_second(self) -> int """
        return 0

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> hour:int, minute:int, second:int """
        pass

    def get_timezone(self): # real signature unknown; restored from __doc__
        """ get_timezone(self) -> ICalGLib.Timezone """
        pass

    def get_tzid(self): # real signature unknown; restored from __doc__
        """ get_tzid(self) -> str or None """
        return ""

    def get_year(self): # real signature unknown; restored from __doc__
        """ get_year(self) -> int """
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

    def is_date(self): # real signature unknown; restored from __doc__
        """ is_date(self) -> bool """
        return False

    def is_daylight(self): # real signature unknown; restored from __doc__
        """ is_daylight(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_null_time(self): # real signature unknown; restored from __doc__
        """ is_null_time(self) -> bool """
        return False

    def is_utc(self): # real signature unknown; restored from __doc__
        """ is_utc(self) -> bool """
        return False

    def is_valid_time(self): # real signature unknown; restored from __doc__
        """ is_valid_time(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ICalGLib.Time """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_current_with_zone(self, zone=None): # real signature unknown; restored from __doc__
        """ new_current_with_zone(zone:ICalGLib.Timezone=None) -> ICalGLib.Time """
        pass

    def new_from_day_of_year(self, day, year): # real signature unknown; restored from __doc__
        """ new_from_day_of_year(day:int, year:int) -> ICalGLib.Time """
        pass

    def new_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_from_string(str:str) -> ICalGLib.Time """
        pass

    def new_from_timet_with_zone(self, v, is_date, zone=None): # real signature unknown; restored from __doc__
        """ new_from_timet_with_zone(v:int, is_date:int, zone:ICalGLib.Timezone=None) -> ICalGLib.Time """
        pass

    def new_null_date(self): # real signature unknown; restored from __doc__
        """ new_null_date() -> ICalGLib.Time """
        pass

    def new_null_time(self): # real signature unknown; restored from __doc__
        """ new_null_time() -> ICalGLib.Time """
        pass

    def new_today(self): # real signature unknown; restored from __doc__
        """ new_today() -> ICalGLib.Time """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> ICalGLib.Time """
        pass

    def normalize_inplace(self): # real signature unknown; restored from __doc__
        """ normalize_inplace(self) """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date(self, year, month, day): # real signature unknown; restored from __doc__
        """ set_date(self, year:int, month:int, day:int) """
        pass

    def set_day(self, day): # real signature unknown; restored from __doc__
        """ set_day(self, day:int) """
        pass

    def set_hour(self, hour): # real signature unknown; restored from __doc__
        """ set_hour(self, hour:int) """
        pass

    def set_is_date(self, is_date): # real signature unknown; restored from __doc__
        """ set_is_date(self, is_date:bool) """
        pass

    def set_is_daylight(self, is_daylight): # real signature unknown; restored from __doc__
        """ set_is_daylight(self, is_daylight:bool) """
        pass

    def set_minute(self, minute): # real signature unknown; restored from __doc__
        """ set_minute(self, minute:int) """
        pass

    def set_month(self, month): # real signature unknown; restored from __doc__
        """ set_month(self, month:int) """
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

    def set_second(self, second): # real signature unknown; restored from __doc__
        """ set_second(self, second:int) """
        pass

    def set_time(self, hour, minute, second): # real signature unknown; restored from __doc__
        """ set_time(self, hour:int, minute:int, second:int) """
        pass

    def set_timezone(self, zone=None): # real signature unknown; restored from __doc__
        """ set_timezone(self, zone:ICalGLib.Timezone=None) """
        pass

    def set_year(self, year): # real signature unknown; restored from __doc__
        """ set_year(self, year:int) """
        pass

    def start_doy_week(self, fdow): # real signature unknown; restored from __doc__
        """ start_doy_week(self, fdow:int) -> int """
        return 0

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

    def subtract(self, t2): # real signature unknown; restored from __doc__
        """ subtract(self, t2:ICalGLib.Time) -> ICalGLib.Duration """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def timezone_expand_vtimezone(self, comp, end_year, changes): # real signature unknown; restored from __doc__
        """ timezone_expand_vtimezone(comp:ICalGLib.Component, end_year:int, changes:ICalGLib.Array) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def week_number(self): # real signature unknown; restored from __doc__
        """ week_number(self) -> int """
        return 0

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1351fd4820>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Time), '__module__': 'gi.repository.ICalGLib', '__gtype__': <GType ICalTime (94403188538816)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_current_with_zone': gi.FunctionInfo(new_current_with_zone), 'new_from_day_of_year': gi.FunctionInfo(new_from_day_of_year), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_from_timet_with_zone': gi.FunctionInfo(new_from_timet_with_zone), 'new_null_date': gi.FunctionInfo(new_null_date), 'new_null_time': gi.FunctionInfo(new_null_time), 'new_today': gi.FunctionInfo(new_today), 'days_in_month': gi.FunctionInfo(days_in_month), 'days_in_year': gi.FunctionInfo(days_in_year), 'days_is_leap_year': gi.FunctionInfo(days_is_leap_year), 'timezone_expand_vtimezone': gi.FunctionInfo(timezone_expand_vtimezone), 'add': gi.FunctionInfo(add), 'adjust': gi.FunctionInfo(adjust), 'as_ical_string': gi.FunctionInfo(as_ical_string), 'as_timet': gi.FunctionInfo(as_timet), 'as_timet_with_zone': gi.FunctionInfo(as_timet_with_zone), 'clone': gi.FunctionInfo(clone), 'compare': gi.FunctionInfo(compare), 'compare_date_only': gi.FunctionInfo(compare_date_only), 'compare_date_only_tz': gi.FunctionInfo(compare_date_only_tz), 'convert_timezone': gi.FunctionInfo(convert_timezone), 'convert_to_zone': gi.FunctionInfo(convert_to_zone), 'convert_to_zone_inplace': gi.FunctionInfo(convert_to_zone_inplace), 'day_of_week': gi.FunctionInfo(day_of_week), 'day_of_year': gi.FunctionInfo(day_of_year), 'get_date': gi.FunctionInfo(get_date), 'get_day': gi.FunctionInfo(get_day), 'get_hour': gi.FunctionInfo(get_hour), 'get_minute': gi.FunctionInfo(get_minute), 'get_month': gi.FunctionInfo(get_month), 'get_second': gi.FunctionInfo(get_second), 'get_time': gi.FunctionInfo(get_time), 'get_timezone': gi.FunctionInfo(get_timezone), 'get_tzid': gi.FunctionInfo(get_tzid), 'get_year': gi.FunctionInfo(get_year), 'is_date': gi.FunctionInfo(is_date), 'is_daylight': gi.FunctionInfo(is_daylight), 'is_null_time': gi.FunctionInfo(is_null_time), 'is_utc': gi.FunctionInfo(is_utc), 'is_valid_time': gi.FunctionInfo(is_valid_time), 'normalize': gi.FunctionInfo(normalize), 'normalize_inplace': gi.FunctionInfo(normalize_inplace), 'set_date': gi.FunctionInfo(set_date), 'set_day': gi.FunctionInfo(set_day), 'set_hour': gi.FunctionInfo(set_hour), 'set_is_date': gi.FunctionInfo(set_is_date), 'set_is_daylight': gi.FunctionInfo(set_is_daylight), 'set_minute': gi.FunctionInfo(set_minute), 'set_month': gi.FunctionInfo(set_month), 'set_second': gi.FunctionInfo(set_second), 'set_time': gi.FunctionInfo(set_time), 'set_timezone': gi.FunctionInfo(set_timezone), 'set_year': gi.FunctionInfo(set_year), 'start_doy_week': gi.FunctionInfo(start_doy_week), 'subtract': gi.FunctionInfo(subtract), 'week_number': gi.FunctionInfo(week_number)})"
    __gdoc__ = 'Object ICalTime\n\nProperties from ICalObject:\n  native -> gpointer: Native\n    Native libical structure\n  native-destroy-func -> gpointer: Native-Destroy-Func\n    GDestroyNotify function to use to destroy the native libical structure\n  is-global-memory -> gboolean: Is-Global-Memory\n    Whether the native libical structure is from a global shared memory\n  owner -> GObject: Owner\n    The native libical structure owner\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ICalTime (94403188538816)>'
    __info__ = ObjectInfo(Time)


