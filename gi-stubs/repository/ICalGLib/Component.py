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

class Component(Object):
    """
    :Constructors:
    
    ::
    
        Component(**properties)
        new(kind:ICalGLib.ComponentKind) -> ICalGLib.Component
        new_from_string(str:str) -> ICalGLib.Component
        new_vagenda() -> ICalGLib.Component
        new_valarm() -> ICalGLib.Component
        new_vavailability() -> ICalGLib.Component
        new_vcalendar() -> ICalGLib.Component
        new_vevent() -> ICalGLib.Component
        new_vfreebusy() -> ICalGLib.Component
        new_vjournal() -> ICalGLib.Component
        new_vpoll() -> ICalGLib.Component
        new_vquery() -> ICalGLib.Component
        new_vtimezone() -> ICalGLib.Component
        new_vtodo() -> ICalGLib.Component
        new_vvoter() -> ICalGLib.Component
        new_x(x_name:str) -> ICalGLib.Component
        new_xavailable() -> ICalGLib.Component
        new_xdaylight() -> ICalGLib.Component
        new_xstandard() -> ICalGLib.Component
        new_xvote() -> ICalGLib.Component
    """
    def add_component(self, child): # real signature unknown; restored from __doc__
        """ add_component(self, child:ICalGLib.Component) """
        pass

    def add_depender(self, depender): # real signature unknown; restored from __doc__
        """ add_depender(self, depender:GObject.Object) """
        pass

    def add_property(self, property): # real signature unknown; restored from __doc__
        """ add_property(self, property:ICalGLib.Property) """
        pass

    def as_ical_string(self): # real signature unknown; restored from __doc__
        """ as_ical_string(self) -> str """
        return ""

    def begin_component(self, kind): # real signature unknown; restored from __doc__
        """ begin_component(self, kind:ICalGLib.ComponentKind) -> ICalGLib.CompIter """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_restrictions(self): # real signature unknown; restored from __doc__
        """ check_restrictions(self) -> int """
        return 0

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> ICalGLib.Component """
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

    def convert_errors(self): # real signature unknown; restored from __doc__
        """ convert_errors(self) """
        pass

    def count_components(self, kind): # real signature unknown; restored from __doc__
        """ count_components(self, kind:ICalGLib.ComponentKind) -> int """
        return 0

    def count_errors(self): # real signature unknown; restored from __doc__
        """ count_errors(self) -> int """
        return 0

    def count_properties(self, kind): # real signature unknown; restored from __doc__
        """ count_properties(self, kind:ICalGLib.PropertyKind) -> int """
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

    def end_component(self, kind): # real signature unknown; restored from __doc__
        """ end_component(self, kind:ICalGLib.ComponentKind) -> ICalGLib.CompIter """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach_recurrence(self, start, end, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_recurrence(self, start:ICalGLib.Time, end:ICalGLib.Time, callback:ICalGLib.ComponentForeachRecurrenceFunc=None, user_data=None) """
        pass

    def foreach_tzid(self, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_tzid(self, callback:ICalGLib.ComponentForeachTZIDFunc=None, user_data=None) """
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

    def get_comment(self): # real signature unknown; restored from __doc__
        """ get_comment(self) -> str """
        return ""

    def get_current_component(self): # real signature unknown; restored from __doc__
        """ get_current_component(self) -> ICalGLib.Component """
        pass

    def get_current_property(self): # real signature unknown; restored from __doc__
        """ get_current_property(self) -> ICalGLib.Property """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_dtend(self): # real signature unknown; restored from __doc__
        """ get_dtend(self) -> ICalGLib.Time """
        pass

    def get_dtstamp(self): # real signature unknown; restored from __doc__
        """ get_dtstamp(self) -> ICalGLib.Time """
        pass

    def get_dtstart(self): # real signature unknown; restored from __doc__
        """ get_dtstart(self) -> ICalGLib.Time """
        pass

    def get_due(self): # real signature unknown; restored from __doc__
        """ get_due(self) -> ICalGLib.Time """
        pass

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> ICalGLib.Duration """
        pass

    def get_first_component(self, kind): # real signature unknown; restored from __doc__
        """ get_first_component(self, kind:ICalGLib.ComponentKind) -> ICalGLib.Component or None """
        pass

    def get_first_property(self, kind): # real signature unknown; restored from __doc__
        """ get_first_property(self, kind:ICalGLib.PropertyKind) -> ICalGLib.Property or None """
        pass

    def get_first_real_component(self): # real signature unknown; restored from __doc__
        """ get_first_real_component(self) -> ICalGLib.Component """
        pass

    def get_inner(self): # real signature unknown; restored from __doc__
        """ get_inner(self) -> ICalGLib.Component or None """
        pass

    def get_is_global_memory(self): # real signature unknown; restored from __doc__
        """ get_is_global_memory(self) -> bool """
        return False

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> str """
        return ""

    def get_method(self): # real signature unknown; restored from __doc__
        """ get_method(self) -> ICalGLib.PropertyMethod """
        pass

    def get_next_component(self, kind): # real signature unknown; restored from __doc__
        """ get_next_component(self, kind:ICalGLib.ComponentKind) -> ICalGLib.Component or None """
        pass

    def get_next_property(self, kind): # real signature unknown; restored from __doc__
        """ get_next_property(self, kind:ICalGLib.PropertyKind) -> ICalGLib.Property or None """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> ICalGLib.Component or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_recurrenceid(self): # real signature unknown; restored from __doc__
        """ get_recurrenceid(self) -> ICalGLib.Time """
        pass

    def get_relcalid(self): # real signature unknown; restored from __doc__
        """ get_relcalid(self) -> str """
        return ""

    def get_sequence(self): # real signature unknown; restored from __doc__
        """ get_sequence(self) -> int """
        return 0

    def get_span(self): # real signature unknown; restored from __doc__
        """ get_span(self) -> ICalGLib.TimeSpan """
        pass

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> ICalGLib.PropertyStatus """
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_timezone(self, tzid): # real signature unknown; restored from __doc__
        """ get_timezone(self, tzid:str) -> ICalGLib.Timezone or None """
        pass

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
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

    def isa(self): # real signature unknown; restored from __doc__
        """ isa(self) -> ICalGLib.ComponentKind """
        pass

    def isa_component(self): # real signature unknown; restored from __doc__
        """ isa_component(self) -> int """
        return 0

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def kind_from_string(self, string): # real signature unknown; restored from __doc__
        """ kind_from_string(string:str) -> ICalGLib.ComponentKind """
        pass

    def kind_is_valid(self, kind): # real signature unknown; restored from __doc__
        """ kind_is_valid(kind:ICalGLib.ComponentKind) -> bool """
        return False

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:ICalGLib.ComponentKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def merge_component(self, comp_to_merge): # real signature unknown; restored from __doc__
        """ merge_component(self, comp_to_merge:ICalGLib.Component) """
        pass

    def new(self, kind): # real signature unknown; restored from __doc__
        """ new(kind:ICalGLib.ComponentKind) -> ICalGLib.Component """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_from_string(str:str) -> ICalGLib.Component """
        pass

    def new_vagenda(self): # real signature unknown; restored from __doc__
        """ new_vagenda() -> ICalGLib.Component """
        pass

    def new_valarm(self): # real signature unknown; restored from __doc__
        """ new_valarm() -> ICalGLib.Component """
        pass

    def new_vavailability(self): # real signature unknown; restored from __doc__
        """ new_vavailability() -> ICalGLib.Component """
        pass

    def new_vcalendar(self): # real signature unknown; restored from __doc__
        """ new_vcalendar() -> ICalGLib.Component """
        pass

    def new_vevent(self): # real signature unknown; restored from __doc__
        """ new_vevent() -> ICalGLib.Component """
        pass

    def new_vfreebusy(self): # real signature unknown; restored from __doc__
        """ new_vfreebusy() -> ICalGLib.Component """
        pass

    def new_vjournal(self): # real signature unknown; restored from __doc__
        """ new_vjournal() -> ICalGLib.Component """
        pass

    def new_vpoll(self): # real signature unknown; restored from __doc__
        """ new_vpoll() -> ICalGLib.Component """
        pass

    def new_vquery(self): # real signature unknown; restored from __doc__
        """ new_vquery() -> ICalGLib.Component """
        pass

    def new_vtimezone(self): # real signature unknown; restored from __doc__
        """ new_vtimezone() -> ICalGLib.Component """
        pass

    def new_vtodo(self): # real signature unknown; restored from __doc__
        """ new_vtodo() -> ICalGLib.Component """
        pass

    def new_vvoter(self): # real signature unknown; restored from __doc__
        """ new_vvoter() -> ICalGLib.Component """
        pass

    def new_x(self, x_name): # real signature unknown; restored from __doc__
        """ new_x(x_name:str) -> ICalGLib.Component """
        pass

    def new_xavailable(self): # real signature unknown; restored from __doc__
        """ new_xavailable() -> ICalGLib.Component """
        pass

    def new_xdaylight(self): # real signature unknown; restored from __doc__
        """ new_xdaylight() -> ICalGLib.Component """
        pass

    def new_xstandard(self): # real signature unknown; restored from __doc__
        """ new_xstandard() -> ICalGLib.Component """
        pass

    def new_xvote(self): # real signature unknown; restored from __doc__
        """ new_xvote() -> ICalGLib.Component """
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

    def remove_component(self, child): # real signature unknown; restored from __doc__
        """ remove_component(self, child:ICalGLib.Component) """
        pass

    def remove_depender(self, depender): # real signature unknown; restored from __doc__
        """ remove_depender(self, depender:GObject.Object) """
        pass

    def remove_owner(self): # real signature unknown; restored from __doc__
        """ remove_owner(self) """
        pass

    def remove_property(self, property): # real signature unknown; restored from __doc__
        """ remove_property(self, property:ICalGLib.Property) """
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

    def set_comment(self, v): # real signature unknown; restored from __doc__
        """ set_comment(self, v:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, v): # real signature unknown; restored from __doc__
        """ set_description(self, v:str) """
        pass

    def set_dtend(self, v): # real signature unknown; restored from __doc__
        """ set_dtend(self, v:ICalGLib.Time) """
        pass

    def set_dtstamp(self, v): # real signature unknown; restored from __doc__
        """ set_dtstamp(self, v:ICalGLib.Time) """
        pass

    def set_dtstart(self, v): # real signature unknown; restored from __doc__
        """ set_dtstart(self, v:ICalGLib.Time) """
        pass

    def set_due(self, v): # real signature unknown; restored from __doc__
        """ set_due(self, v:ICalGLib.Time) """
        pass

    def set_duration(self, v): # real signature unknown; restored from __doc__
        """ set_duration(self, v:ICalGLib.Duration) """
        pass

    def set_location(self, v): # real signature unknown; restored from __doc__
        """ set_location(self, v:str) """
        pass

    def set_method(self, method): # real signature unknown; restored from __doc__
        """ set_method(self, method:ICalGLib.PropertyMethod) """
        pass

    def set_native_destroy_func(self, native_destroy_func): # real signature unknown; restored from __doc__
        """ set_native_destroy_func(self, native_destroy_func:GLib.DestroyNotify) """
        pass

    def set_owner(self, owner): # real signature unknown; restored from __doc__
        """ set_owner(self, owner:GObject.Object) """
        pass

    def set_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:ICalGLib.Component=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_recurrenceid(self, v): # real signature unknown; restored from __doc__
        """ set_recurrenceid(self, v:ICalGLib.Time) """
        pass

    def set_relcalid(self, v): # real signature unknown; restored from __doc__
        """ set_relcalid(self, v:str) """
        pass

    def set_sequence(self, v): # real signature unknown; restored from __doc__
        """ set_sequence(self, v:int) """
        pass

    def set_status(self, status): # real signature unknown; restored from __doc__
        """ set_status(self, status:ICalGLib.PropertyStatus) """
        pass

    def set_summary(self, v): # real signature unknown; restored from __doc__
        """ set_summary(self, v:str) """
        pass

    def set_uid(self, v): # real signature unknown; restored from __doc__
        """ set_uid(self, v:str) """
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

    def strip_errors(self): # real signature unknown; restored from __doc__
        """ strip_errors(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1352080c70>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Component), '__module__': 'gi.repository.ICalGLib', '__gtype__': <GType ICalComponent (94403187911472)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_vagenda': gi.FunctionInfo(new_vagenda), 'new_valarm': gi.FunctionInfo(new_valarm), 'new_vavailability': gi.FunctionInfo(new_vavailability), 'new_vcalendar': gi.FunctionInfo(new_vcalendar), 'new_vevent': gi.FunctionInfo(new_vevent), 'new_vfreebusy': gi.FunctionInfo(new_vfreebusy), 'new_vjournal': gi.FunctionInfo(new_vjournal), 'new_vpoll': gi.FunctionInfo(new_vpoll), 'new_vquery': gi.FunctionInfo(new_vquery), 'new_vtimezone': gi.FunctionInfo(new_vtimezone), 'new_vtodo': gi.FunctionInfo(new_vtodo), 'new_vvoter': gi.FunctionInfo(new_vvoter), 'new_x': gi.FunctionInfo(new_x), 'new_xavailable': gi.FunctionInfo(new_xavailable), 'new_xdaylight': gi.FunctionInfo(new_xdaylight), 'new_xstandard': gi.FunctionInfo(new_xstandard), 'new_xvote': gi.FunctionInfo(new_xvote), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_is_valid': gi.FunctionInfo(kind_is_valid), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'add_component': gi.FunctionInfo(add_component), 'add_property': gi.FunctionInfo(add_property), 'as_ical_string': gi.FunctionInfo(as_ical_string), 'begin_component': gi.FunctionInfo(begin_component), 'check_restrictions': gi.FunctionInfo(check_restrictions), 'clone': gi.FunctionInfo(clone), 'convert_errors': gi.FunctionInfo(convert_errors), 'count_components': gi.FunctionInfo(count_components), 'count_errors': gi.FunctionInfo(count_errors), 'count_properties': gi.FunctionInfo(count_properties), 'end_component': gi.FunctionInfo(end_component), 'foreach_recurrence': gi.FunctionInfo(foreach_recurrence), 'foreach_tzid': gi.FunctionInfo(foreach_tzid), 'get_comment': gi.FunctionInfo(get_comment), 'get_current_component': gi.FunctionInfo(get_current_component), 'get_current_property': gi.FunctionInfo(get_current_property), 'get_description': gi.FunctionInfo(get_description), 'get_dtend': gi.FunctionInfo(get_dtend), 'get_dtstamp': gi.FunctionInfo(get_dtstamp), 'get_dtstart': gi.FunctionInfo(get_dtstart), 'get_due': gi.FunctionInfo(get_due), 'get_duration': gi.FunctionInfo(get_duration), 'get_first_component': gi.FunctionInfo(get_first_component), 'get_first_property': gi.FunctionInfo(get_first_property), 'get_first_real_component': gi.FunctionInfo(get_first_real_component), 'get_inner': gi.FunctionInfo(get_inner), 'get_location': gi.FunctionInfo(get_location), 'get_method': gi.FunctionInfo(get_method), 'get_next_component': gi.FunctionInfo(get_next_component), 'get_next_property': gi.FunctionInfo(get_next_property), 'get_parent': gi.FunctionInfo(get_parent), 'get_recurrenceid': gi.FunctionInfo(get_recurrenceid), 'get_relcalid': gi.FunctionInfo(get_relcalid), 'get_sequence': gi.FunctionInfo(get_sequence), 'get_span': gi.FunctionInfo(get_span), 'get_status': gi.FunctionInfo(get_status), 'get_summary': gi.FunctionInfo(get_summary), 'get_timezone': gi.FunctionInfo(get_timezone), 'get_uid': gi.FunctionInfo(get_uid), 'is_valid': gi.FunctionInfo(is_valid), 'isa': gi.FunctionInfo(isa), 'isa_component': gi.FunctionInfo(isa_component), 'merge_component': gi.FunctionInfo(merge_component), 'remove_component': gi.FunctionInfo(remove_component), 'remove_property': gi.FunctionInfo(remove_property), 'set_comment': gi.FunctionInfo(set_comment), 'set_description': gi.FunctionInfo(set_description), 'set_dtend': gi.FunctionInfo(set_dtend), 'set_dtstamp': gi.FunctionInfo(set_dtstamp), 'set_dtstart': gi.FunctionInfo(set_dtstart), 'set_due': gi.FunctionInfo(set_due), 'set_duration': gi.FunctionInfo(set_duration), 'set_location': gi.FunctionInfo(set_location), 'set_method': gi.FunctionInfo(set_method), 'set_parent': gi.FunctionInfo(set_parent), 'set_recurrenceid': gi.FunctionInfo(set_recurrenceid), 'set_relcalid': gi.FunctionInfo(set_relcalid), 'set_sequence': gi.FunctionInfo(set_sequence), 'set_status': gi.FunctionInfo(set_status), 'set_summary': gi.FunctionInfo(set_summary), 'set_uid': gi.FunctionInfo(set_uid), 'strip_errors': gi.FunctionInfo(strip_errors)})"
    __gdoc__ = 'Object ICalComponent\n\nProperties from ICalObject:\n  native -> gpointer: Native\n    Native libical structure\n  native-destroy-func -> gpointer: Native-Destroy-Func\n    GDestroyNotify function to use to destroy the native libical structure\n  is-global-memory -> gboolean: Is-Global-Memory\n    Whether the native libical structure is from a global shared memory\n  owner -> GObject: Owner\n    The native libical structure owner\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ICalComponent (94403187911472)>'
    __info__ = ObjectInfo(Component)


