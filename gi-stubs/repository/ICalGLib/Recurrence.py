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

class Recurrence(Object):
    """
    :Constructors:
    
    ::
    
        Recurrence(**properties)
        new() -> ICalGLib.Recurrence
        new_from_string(str:str) -> ICalGLib.Recurrence
    """
    def add_depender(self, depender): # real signature unknown; restored from __doc__
        """ add_depender(self, depender:GObject.Object) """
        pass

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

    def day_day_of_week(self, day): # real signature unknown; restored from __doc__
        """ day_day_of_week(day:int) -> ICalGLib.RecurrenceWeekday """
        pass

    def day_position(self, day): # real signature unknown; restored from __doc__
        """ day_position(day:int) -> int """
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

    def frequency_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ frequency_from_string(str:str) -> ICalGLib.RecurrenceFrequency """
        pass

    def frequency_to_string(self, kind): # real signature unknown; restored from __doc__
        """ frequency_to_string(kind:ICalGLib.RecurrenceFrequency) -> str """
        return ""

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_by_day(self, index): # real signature unknown; restored from __doc__
        """ get_by_day(self, index:int) -> int """
        return 0

    def get_by_day_array(self): # real signature unknown; restored from __doc__
        """ get_by_day_array(self) -> list """
        return []

    def get_by_hour(self, index): # real signature unknown; restored from __doc__
        """ get_by_hour(self, index:int) -> int """
        return 0

    def get_by_hour_array(self): # real signature unknown; restored from __doc__
        """ get_by_hour_array(self) -> list """
        return []

    def get_by_minute(self, index): # real signature unknown; restored from __doc__
        """ get_by_minute(self, index:int) -> int """
        return 0

    def get_by_minute_array(self): # real signature unknown; restored from __doc__
        """ get_by_minute_array(self) -> list """
        return []

    def get_by_month(self, index): # real signature unknown; restored from __doc__
        """ get_by_month(self, index:int) -> int """
        return 0

    def get_by_month_array(self): # real signature unknown; restored from __doc__
        """ get_by_month_array(self) -> list """
        return []

    def get_by_month_day(self, index): # real signature unknown; restored from __doc__
        """ get_by_month_day(self, index:int) -> int """
        return 0

    def get_by_month_day_array(self): # real signature unknown; restored from __doc__
        """ get_by_month_day_array(self) -> list """
        return []

    def get_by_second(self, index): # real signature unknown; restored from __doc__
        """ get_by_second(self, index:int) -> int """
        return 0

    def get_by_second_array(self): # real signature unknown; restored from __doc__
        """ get_by_second_array(self) -> list """
        return []

    def get_by_set_pos(self, index): # real signature unknown; restored from __doc__
        """ get_by_set_pos(self, index:int) -> int """
        return 0

    def get_by_set_pos_array(self): # real signature unknown; restored from __doc__
        """ get_by_set_pos_array(self) -> list """
        return []

    def get_by_week_no(self, index): # real signature unknown; restored from __doc__
        """ get_by_week_no(self, index:int) -> int """
        return 0

    def get_by_week_no_array(self): # real signature unknown; restored from __doc__
        """ get_by_week_no_array(self) -> list """
        return []

    def get_by_year_day(self, index): # real signature unknown; restored from __doc__
        """ get_by_year_day(self, index:int) -> int """
        return 0

    def get_by_year_day_array(self): # real signature unknown; restored from __doc__
        """ get_by_year_day_array(self) -> list """
        return []

    def get_count(self): # real signature unknown; restored from __doc__
        """ get_count(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_freq(self): # real signature unknown; restored from __doc__
        """ get_freq(self) -> ICalGLib.RecurrenceFrequency """
        pass

    def get_interval(self): # real signature unknown; restored from __doc__
        """ get_interval(self) -> int """
        return 0

    def get_is_global_memory(self): # real signature unknown; restored from __doc__
        """ get_is_global_memory(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_until(self): # real signature unknown; restored from __doc__
        """ get_until(self) -> ICalGLib.Time """
        pass

    def get_week_start(self): # real signature unknown; restored from __doc__
        """ get_week_start(self) -> ICalGLib.RecurrenceWeekday """
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

    def month_is_leap(self, month): # real signature unknown; restored from __doc__
        """ month_is_leap(month:int) -> bool """
        return False

    def month_month(self, month): # real signature unknown; restored from __doc__
        """ month_month(month:int) -> int """
        return 0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ICalGLib.Recurrence """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_from_string(str:str) -> ICalGLib.Recurrence """
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

    def rscale_is_supported(self): # real signature unknown; restored from __doc__
        """ rscale_is_supported() -> bool """
        return False

    def rscale_supported_calendars(self): # real signature unknown; restored from __doc__
        """ rscale_supported_calendars() -> ICalGLib.Array """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_by_day(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_day(self, index:int, value:int) """
        pass

    def set_by_day_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_day_array(self, values:list) """
        pass

    def set_by_hour(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_hour(self, index:int, value:int) """
        pass

    def set_by_hour_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_hour_array(self, values:list) """
        pass

    def set_by_minute(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_minute(self, index:int, value:int) """
        pass

    def set_by_minute_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_minute_array(self, values:list) """
        pass

    def set_by_month(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_month(self, index:int, value:int) """
        pass

    def set_by_month_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_month_array(self, values:list) """
        pass

    def set_by_month_day(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_month_day(self, index:int, value:int) """
        pass

    def set_by_month_day_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_month_day_array(self, values:list) """
        pass

    def set_by_second(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_second(self, index:int, value:int) """
        pass

    def set_by_second_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_second_array(self, values:list) """
        pass

    def set_by_set_pos(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_set_pos(self, index:int, value:int) """
        pass

    def set_by_set_pos_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_set_pos_array(self, values:list) """
        pass

    def set_by_week_no(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_week_no(self, index:int, value:int) """
        pass

    def set_by_week_no_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_week_no_array(self, values:list) """
        pass

    def set_by_year_day(self, index, value): # real signature unknown; restored from __doc__
        """ set_by_year_day(self, index:int, value:int) """
        pass

    def set_by_year_day_array(self, values): # real signature unknown; restored from __doc__
        """ set_by_year_day_array(self, values:list) """
        pass

    def set_count(self, count): # real signature unknown; restored from __doc__
        """ set_count(self, count:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_freq(self, freq): # real signature unknown; restored from __doc__
        """ set_freq(self, freq:ICalGLib.RecurrenceFrequency) """
        pass

    def set_interval(self, interval): # real signature unknown; restored from __doc__
        """ set_interval(self, interval:int) """
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

    def set_until(self, until): # real signature unknown; restored from __doc__
        """ set_until(self, until:ICalGLib.Time) """
        pass

    def set_week_start(self, week_start): # real signature unknown; restored from __doc__
        """ set_week_start(self, week_start:ICalGLib.RecurrenceWeekday) """
        pass

    def skip_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ skip_from_string(str:str) -> ICalGLib.RecurrenceSkip """
        pass

    def skip_to_string(self, kind): # real signature unknown; restored from __doc__
        """ skip_to_string(kind:ICalGLib.RecurrenceSkip) -> str """
        return ""

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

    def weekday_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ weekday_from_string(str:str) -> ICalGLib.RecurrenceWeekday """
        pass

    def weekday_to_string(self, kind): # real signature unknown; restored from __doc__
        """ weekday_to_string(kind:ICalGLib.RecurrenceWeekday) -> str """
        return ""

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1351fd4f70>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Recurrence), '__module__': 'gi.repository.ICalGLib', '__gtype__': <GType ICalRecurrence (94403188523872)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_string': gi.FunctionInfo(new_from_string), 'day_day_of_week': gi.FunctionInfo(day_day_of_week), 'day_position': gi.FunctionInfo(day_position), 'frequency_from_string': gi.FunctionInfo(frequency_from_string), 'frequency_to_string': gi.FunctionInfo(frequency_to_string), 'month_is_leap': gi.FunctionInfo(month_is_leap), 'month_month': gi.FunctionInfo(month_month), 'rscale_is_supported': gi.FunctionInfo(rscale_is_supported), 'rscale_supported_calendars': gi.FunctionInfo(rscale_supported_calendars), 'skip_from_string': gi.FunctionInfo(skip_from_string), 'skip_to_string': gi.FunctionInfo(skip_to_string), 'weekday_from_string': gi.FunctionInfo(weekday_from_string), 'weekday_to_string': gi.FunctionInfo(weekday_to_string), 'clear': gi.FunctionInfo(clear), 'get_by_day': gi.FunctionInfo(get_by_day), 'get_by_day_array': gi.FunctionInfo(get_by_day_array), 'get_by_hour': gi.FunctionInfo(get_by_hour), 'get_by_hour_array': gi.FunctionInfo(get_by_hour_array), 'get_by_minute': gi.FunctionInfo(get_by_minute), 'get_by_minute_array': gi.FunctionInfo(get_by_minute_array), 'get_by_month': gi.FunctionInfo(get_by_month), 'get_by_month_array': gi.FunctionInfo(get_by_month_array), 'get_by_month_day': gi.FunctionInfo(get_by_month_day), 'get_by_month_day_array': gi.FunctionInfo(get_by_month_day_array), 'get_by_second': gi.FunctionInfo(get_by_second), 'get_by_second_array': gi.FunctionInfo(get_by_second_array), 'get_by_set_pos': gi.FunctionInfo(get_by_set_pos), 'get_by_set_pos_array': gi.FunctionInfo(get_by_set_pos_array), 'get_by_week_no': gi.FunctionInfo(get_by_week_no), 'get_by_week_no_array': gi.FunctionInfo(get_by_week_no_array), 'get_by_year_day': gi.FunctionInfo(get_by_year_day), 'get_by_year_day_array': gi.FunctionInfo(get_by_year_day_array), 'get_count': gi.FunctionInfo(get_count), 'get_freq': gi.FunctionInfo(get_freq), 'get_interval': gi.FunctionInfo(get_interval), 'get_until': gi.FunctionInfo(get_until), 'get_week_start': gi.FunctionInfo(get_week_start), 'set_by_day': gi.FunctionInfo(set_by_day), 'set_by_day_array': gi.FunctionInfo(set_by_day_array), 'set_by_hour': gi.FunctionInfo(set_by_hour), 'set_by_hour_array': gi.FunctionInfo(set_by_hour_array), 'set_by_minute': gi.FunctionInfo(set_by_minute), 'set_by_minute_array': gi.FunctionInfo(set_by_minute_array), 'set_by_month': gi.FunctionInfo(set_by_month), 'set_by_month_array': gi.FunctionInfo(set_by_month_array), 'set_by_month_day': gi.FunctionInfo(set_by_month_day), 'set_by_month_day_array': gi.FunctionInfo(set_by_month_day_array), 'set_by_second': gi.FunctionInfo(set_by_second), 'set_by_second_array': gi.FunctionInfo(set_by_second_array), 'set_by_set_pos': gi.FunctionInfo(set_by_set_pos), 'set_by_set_pos_array': gi.FunctionInfo(set_by_set_pos_array), 'set_by_week_no': gi.FunctionInfo(set_by_week_no), 'set_by_week_no_array': gi.FunctionInfo(set_by_week_no_array), 'set_by_year_day': gi.FunctionInfo(set_by_year_day), 'set_by_year_day_array': gi.FunctionInfo(set_by_year_day_array), 'set_count': gi.FunctionInfo(set_count), 'set_freq': gi.FunctionInfo(set_freq), 'set_interval': gi.FunctionInfo(set_interval), 'set_until': gi.FunctionInfo(set_until), 'set_week_start': gi.FunctionInfo(set_week_start), 'to_string': gi.FunctionInfo(to_string)})"
    __gdoc__ = 'Object ICalRecurrence\n\nProperties from ICalObject:\n  native -> gpointer: Native\n    Native libical structure\n  native-destroy-func -> gpointer: Native-Destroy-Func\n    GDestroyNotify function to use to destroy the native libical structure\n  is-global-memory -> gboolean: Is-Global-Memory\n    Whether the native libical structure is from a global shared memory\n  owner -> GObject: Owner\n    The native libical structure owner\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ICalRecurrence (94403188523872)>'
    __info__ = ObjectInfo(Recurrence)


