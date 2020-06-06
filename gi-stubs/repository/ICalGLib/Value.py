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

class Value(Object):
    """
    :Constructors:
    
    ::
    
        Value(**properties)
        new(kind:ICalGLib.ValueKind) -> ICalGLib.Value
        new_action(v:ICalGLib.PropertyAction) -> ICalGLib.Value
        new_attach(v:ICalGLib.Attach) -> ICalGLib.Value
        new_binary(v:str) -> ICalGLib.Value
        new_boolean(v:int) -> ICalGLib.Value
        new_busytype(v:ICalGLib.PropertyBusytype) -> ICalGLib.Value
        new_caladdress(v:str) -> ICalGLib.Value
        new_carlevel(v:ICalGLib.PropertyCarlevel) -> ICalGLib.Value
        new_class(v:ICalGLib.Property_Class) -> ICalGLib.Value
        new_cmd(v:ICalGLib.PropertyCmd) -> ICalGLib.Value
        new_date(v:ICalGLib.Time) -> ICalGLib.Value
        new_datetime(v:ICalGLib.Time) -> ICalGLib.Value
        new_datetimedate(v:ICalGLib.Time) -> ICalGLib.Value
        new_datetimeperiod(v:ICalGLib.Datetimeperiod) -> ICalGLib.Value
        new_duration(v:ICalGLib.Duration) -> ICalGLib.Value
        new_float(v:float) -> ICalGLib.Value
        new_from_string(kind:ICalGLib.ValueKind, str:str) -> ICalGLib.Value
        new_geo(v:ICalGLib.Geo) -> ICalGLib.Value
        new_integer(v:int) -> ICalGLib.Value
        new_method(v:ICalGLib.PropertyMethod) -> ICalGLib.Value
        new_period(v:ICalGLib.Period) -> ICalGLib.Value
        new_pollcompletion(v:ICalGLib.PropertyPollcompletion) -> ICalGLib.Value
        new_pollmode(v:ICalGLib.PropertyPollmode) -> ICalGLib.Value
        new_query(v:str) -> ICalGLib.Value
        new_querylevel(v:ICalGLib.PropertyQuerylevel) -> ICalGLib.Value
        new_recur(v:ICalGLib.Recurrence) -> ICalGLib.Value
        new_requeststatus(v:ICalGLib.Reqstat) -> ICalGLib.Value
        new_status(v:ICalGLib.PropertyStatus) -> ICalGLib.Value
        new_string(v:str) -> ICalGLib.Value
        new_taskmode(v:ICalGLib.PropertyTaskmode) -> ICalGLib.Value
        new_text(v:str) -> ICalGLib.Value
        new_transp(v:ICalGLib.PropertyTransp) -> ICalGLib.Value
        new_trigger(v:ICalGLib.Trigger) -> ICalGLib.Value
        new_uri(v:str) -> ICalGLib.Value
        new_utcoffset(v:int) -> ICalGLib.Value
        new_x(v:str) -> ICalGLib.Value
        new_xlicclass(v:ICalGLib.PropertyXlicclass) -> ICalGLib.Value
    """
    def add_depender(self, depender): # real signature unknown; restored from __doc__
        """ add_depender(self, depender:GObject.Object) """
        pass

    def as_ical_string(self): # real signature unknown; restored from __doc__
        """ as_ical_string(self) -> str """
        return ""

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> ICalGLib.Value """
        pass

    def compare(self, b): # real signature unknown; restored from __doc__
        """ compare(self, b:ICalGLib.Value) -> ICalGLib.ParameterXliccomparetype """
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

    def decode_ical_string(self, szText): # real signature unknown; restored from __doc__
        """ decode_ical_string(szText:str) -> str or None """
        return ""

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

    def encode_ical_string(self, szText): # real signature unknown; restored from __doc__
        """ encode_ical_string(szText:str) -> str or None """
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

    def free_global_objects(self): # real signature unknown; restored from __doc__
        """ free_global_objects() """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> ICalGLib.PropertyAction """
        pass

    def get_attach(self): # real signature unknown; restored from __doc__
        """ get_attach(self) -> ICalGLib.Attach or None """
        pass

    def get_binary(self): # real signature unknown; restored from __doc__
        """ get_binary(self) -> str or None """
        return ""

    def get_boolean(self): # real signature unknown; restored from __doc__
        """ get_boolean(self) -> int """
        return 0

    def get_busytype(self): # real signature unknown; restored from __doc__
        """ get_busytype(self) -> ICalGLib.PropertyBusytype """
        pass

    def get_caladdress(self): # real signature unknown; restored from __doc__
        """ get_caladdress(self) -> str or None """
        return ""

    def get_carlevel(self): # real signature unknown; restored from __doc__
        """ get_carlevel(self) -> ICalGLib.PropertyCarlevel """
        pass

    def get_class(self): # real signature unknown; restored from __doc__
        """ get_class(self) -> ICalGLib.Property_Class """
        pass

    def get_cmd(self): # real signature unknown; restored from __doc__
        """ get_cmd(self) -> ICalGLib.PropertyCmd """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date(self): # real signature unknown; restored from __doc__
        """ get_date(self) -> ICalGLib.Time or None """
        pass

    def get_datetime(self): # real signature unknown; restored from __doc__
        """ get_datetime(self) -> ICalGLib.Time or None """
        pass

    def get_datetimedate(self): # real signature unknown; restored from __doc__
        """ get_datetimedate(self) -> ICalGLib.Time or None """
        pass

    def get_datetimeperiod(self): # real signature unknown; restored from __doc__
        """ get_datetimeperiod(self) -> ICalGLib.Datetimeperiod or None """
        pass

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> ICalGLib.Duration or None """
        pass

    def get_float(self): # real signature unknown; restored from __doc__
        """ get_float(self) -> float """
        return 0.0

    def get_geo(self): # real signature unknown; restored from __doc__
        """ get_geo(self) -> ICalGLib.Geo or None """
        pass

    def get_integer(self): # real signature unknown; restored from __doc__
        """ get_integer(self) -> int """
        return 0

    def get_is_global_memory(self): # real signature unknown; restored from __doc__
        """ get_is_global_memory(self) -> bool """
        return False

    def get_method(self): # real signature unknown; restored from __doc__
        """ get_method(self) -> ICalGLib.PropertyMethod """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> ICalGLib.Property or None """
        pass

    def get_period(self): # real signature unknown; restored from __doc__
        """ get_period(self) -> ICalGLib.Period or None """
        pass

    def get_pollcompletion(self): # real signature unknown; restored from __doc__
        """ get_pollcompletion(self) -> ICalGLib.PropertyPollcompletion """
        pass

    def get_pollmode(self): # real signature unknown; restored from __doc__
        """ get_pollmode(self) -> ICalGLib.PropertyPollmode """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_query(self): # real signature unknown; restored from __doc__
        """ get_query(self) -> str or None """
        return ""

    def get_querylevel(self): # real signature unknown; restored from __doc__
        """ get_querylevel(self) -> ICalGLib.PropertyQuerylevel """
        pass

    def get_recur(self): # real signature unknown; restored from __doc__
        """ get_recur(self) -> ICalGLib.Recurrence or None """
        pass

    def get_requeststatus(self): # real signature unknown; restored from __doc__
        """ get_requeststatus(self) -> ICalGLib.Reqstat or None """
        pass

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> ICalGLib.PropertyStatus """
        pass

    def get_string(self): # real signature unknown; restored from __doc__
        """ get_string(self) -> str or None """
        return ""

    def get_taskmode(self): # real signature unknown; restored from __doc__
        """ get_taskmode(self) -> ICalGLib.PropertyTaskmode """
        pass

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str or None """
        return ""

    def get_transp(self): # real signature unknown; restored from __doc__
        """ get_transp(self) -> ICalGLib.PropertyTransp """
        pass

    def get_trigger(self): # real signature unknown; restored from __doc__
        """ get_trigger(self) -> ICalGLib.Trigger or None """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str or None """
        return ""

    def get_utcoffset(self): # real signature unknown; restored from __doc__
        """ get_utcoffset(self) -> int """
        return 0

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> str or None """
        return ""

    def get_xlicclass(self): # real signature unknown; restored from __doc__
        """ get_xlicclass(self) -> ICalGLib.PropertyXlicclass """
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

    def isa(self): # real signature unknown; restored from __doc__
        """ isa(self) -> ICalGLib.ValueKind """
        pass

    def isa_value(self): # real signature unknown; restored from __doc__
        """ isa_value(self) -> int """
        return 0

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def kind_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ kind_from_string(str:str) -> ICalGLib.ValueKind """
        pass

    def kind_is_valid(self, kind): # real signature unknown; restored from __doc__
        """ kind_is_valid(kind:ICalGLib.ValueKind) -> bool """
        return False

    def kind_to_property_kind(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_property_kind(kind:ICalGLib.ValueKind) -> ICalGLib.PropertyKind """
        pass

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:ICalGLib.ValueKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, kind): # real signature unknown; restored from __doc__
        """ new(kind:ICalGLib.ValueKind) -> ICalGLib.Value """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_action(self, v): # real signature unknown; restored from __doc__
        """ new_action(v:ICalGLib.PropertyAction) -> ICalGLib.Value """
        pass

    def new_attach(self, v): # real signature unknown; restored from __doc__
        """ new_attach(v:ICalGLib.Attach) -> ICalGLib.Value """
        pass

    def new_binary(self, v): # real signature unknown; restored from __doc__
        """ new_binary(v:str) -> ICalGLib.Value """
        pass

    def new_boolean(self, v): # real signature unknown; restored from __doc__
        """ new_boolean(v:int) -> ICalGLib.Value """
        pass

    def new_busytype(self, v): # real signature unknown; restored from __doc__
        """ new_busytype(v:ICalGLib.PropertyBusytype) -> ICalGLib.Value """
        pass

    def new_caladdress(self, v): # real signature unknown; restored from __doc__
        """ new_caladdress(v:str) -> ICalGLib.Value """
        pass

    def new_carlevel(self, v): # real signature unknown; restored from __doc__
        """ new_carlevel(v:ICalGLib.PropertyCarlevel) -> ICalGLib.Value """
        pass

    def new_class(self, v): # real signature unknown; restored from __doc__
        """ new_class(v:ICalGLib.Property_Class) -> ICalGLib.Value """
        pass

    def new_cmd(self, v): # real signature unknown; restored from __doc__
        """ new_cmd(v:ICalGLib.PropertyCmd) -> ICalGLib.Value """
        pass

    def new_date(self, v): # real signature unknown; restored from __doc__
        """ new_date(v:ICalGLib.Time) -> ICalGLib.Value """
        pass

    def new_datetime(self, v): # real signature unknown; restored from __doc__
        """ new_datetime(v:ICalGLib.Time) -> ICalGLib.Value """
        pass

    def new_datetimedate(self, v): # real signature unknown; restored from __doc__
        """ new_datetimedate(v:ICalGLib.Time) -> ICalGLib.Value """
        pass

    def new_datetimeperiod(self, v): # real signature unknown; restored from __doc__
        """ new_datetimeperiod(v:ICalGLib.Datetimeperiod) -> ICalGLib.Value """
        pass

    def new_duration(self, v): # real signature unknown; restored from __doc__
        """ new_duration(v:ICalGLib.Duration) -> ICalGLib.Value """
        pass

    def new_float(self, v): # real signature unknown; restored from __doc__
        """ new_float(v:float) -> ICalGLib.Value """
        pass

    def new_from_string(self, kind, p_str): # real signature unknown; restored from __doc__
        """ new_from_string(kind:ICalGLib.ValueKind, str:str) -> ICalGLib.Value """
        pass

    def new_geo(self, v): # real signature unknown; restored from __doc__
        """ new_geo(v:ICalGLib.Geo) -> ICalGLib.Value """
        pass

    def new_integer(self, v): # real signature unknown; restored from __doc__
        """ new_integer(v:int) -> ICalGLib.Value """
        pass

    def new_method(self, v): # real signature unknown; restored from __doc__
        """ new_method(v:ICalGLib.PropertyMethod) -> ICalGLib.Value """
        pass

    def new_period(self, v): # real signature unknown; restored from __doc__
        """ new_period(v:ICalGLib.Period) -> ICalGLib.Value """
        pass

    def new_pollcompletion(self, v): # real signature unknown; restored from __doc__
        """ new_pollcompletion(v:ICalGLib.PropertyPollcompletion) -> ICalGLib.Value """
        pass

    def new_pollmode(self, v): # real signature unknown; restored from __doc__
        """ new_pollmode(v:ICalGLib.PropertyPollmode) -> ICalGLib.Value """
        pass

    def new_query(self, v): # real signature unknown; restored from __doc__
        """ new_query(v:str) -> ICalGLib.Value """
        pass

    def new_querylevel(self, v): # real signature unknown; restored from __doc__
        """ new_querylevel(v:ICalGLib.PropertyQuerylevel) -> ICalGLib.Value """
        pass

    def new_recur(self, v): # real signature unknown; restored from __doc__
        """ new_recur(v:ICalGLib.Recurrence) -> ICalGLib.Value """
        pass

    def new_requeststatus(self, v): # real signature unknown; restored from __doc__
        """ new_requeststatus(v:ICalGLib.Reqstat) -> ICalGLib.Value """
        pass

    def new_status(self, v): # real signature unknown; restored from __doc__
        """ new_status(v:ICalGLib.PropertyStatus) -> ICalGLib.Value """
        pass

    def new_string(self, v): # real signature unknown; restored from __doc__
        """ new_string(v:str) -> ICalGLib.Value """
        pass

    def new_taskmode(self, v): # real signature unknown; restored from __doc__
        """ new_taskmode(v:ICalGLib.PropertyTaskmode) -> ICalGLib.Value """
        pass

    def new_text(self, v): # real signature unknown; restored from __doc__
        """ new_text(v:str) -> ICalGLib.Value """
        pass

    def new_transp(self, v): # real signature unknown; restored from __doc__
        """ new_transp(v:ICalGLib.PropertyTransp) -> ICalGLib.Value """
        pass

    def new_trigger(self, v): # real signature unknown; restored from __doc__
        """ new_trigger(v:ICalGLib.Trigger) -> ICalGLib.Value """
        pass

    def new_uri(self, v): # real signature unknown; restored from __doc__
        """ new_uri(v:str) -> ICalGLib.Value """
        pass

    def new_utcoffset(self, v): # real signature unknown; restored from __doc__
        """ new_utcoffset(v:int) -> ICalGLib.Value """
        pass

    def new_x(self, v): # real signature unknown; restored from __doc__
        """ new_x(v:str) -> ICalGLib.Value """
        pass

    def new_xlicclass(self, v): # real signature unknown; restored from __doc__
        """ new_xlicclass(v:ICalGLib.PropertyXlicclass) -> ICalGLib.Value """
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

    def reset_kind(self): # real signature unknown; restored from __doc__
        """ reset_kind(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_action(self, v): # real signature unknown; restored from __doc__
        """ set_action(self, v:ICalGLib.PropertyAction) """
        pass

    def set_attach(self, v): # real signature unknown; restored from __doc__
        """ set_attach(self, v:ICalGLib.Attach) """
        pass

    def set_binary(self, v): # real signature unknown; restored from __doc__
        """ set_binary(self, v:str) """
        pass

    def set_boolean(self, v): # real signature unknown; restored from __doc__
        """ set_boolean(self, v:int) """
        pass

    def set_busytype(self, v): # real signature unknown; restored from __doc__
        """ set_busytype(self, v:ICalGLib.PropertyBusytype) """
        pass

    def set_caladdress(self, v): # real signature unknown; restored from __doc__
        """ set_caladdress(self, v:str) """
        pass

    def set_carlevel(self, v): # real signature unknown; restored from __doc__
        """ set_carlevel(self, v:ICalGLib.PropertyCarlevel) """
        pass

    def set_class(self, v): # real signature unknown; restored from __doc__
        """ set_class(self, v:ICalGLib.Property_Class) """
        pass

    def set_cmd(self, v): # real signature unknown; restored from __doc__
        """ set_cmd(self, v:ICalGLib.PropertyCmd) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date(self, v): # real signature unknown; restored from __doc__
        """ set_date(self, v:ICalGLib.Time) """
        pass

    def set_datetime(self, v): # real signature unknown; restored from __doc__
        """ set_datetime(self, v:ICalGLib.Time) """
        pass

    def set_datetimedate(self, v): # real signature unknown; restored from __doc__
        """ set_datetimedate(self, v:ICalGLib.Time) """
        pass

    def set_datetimeperiod(self, v): # real signature unknown; restored from __doc__
        """ set_datetimeperiod(self, v:ICalGLib.Datetimeperiod) """
        pass

    def set_duration(self, v): # real signature unknown; restored from __doc__
        """ set_duration(self, v:ICalGLib.Duration) """
        pass

    def set_float(self, v): # real signature unknown; restored from __doc__
        """ set_float(self, v:float) """
        pass

    def set_geo(self, v): # real signature unknown; restored from __doc__
        """ set_geo(self, v:ICalGLib.Geo) """
        pass

    def set_integer(self, v): # real signature unknown; restored from __doc__
        """ set_integer(self, v:int) """
        pass

    def set_method(self, v): # real signature unknown; restored from __doc__
        """ set_method(self, v:ICalGLib.PropertyMethod) """
        pass

    def set_native_destroy_func(self, native_destroy_func): # real signature unknown; restored from __doc__
        """ set_native_destroy_func(self, native_destroy_func:GLib.DestroyNotify) """
        pass

    def set_owner(self, owner): # real signature unknown; restored from __doc__
        """ set_owner(self, owner:GObject.Object) """
        pass

    def set_parent(self, property=None): # real signature unknown; restored from __doc__
        """ set_parent(self, property:ICalGLib.Property=None) """
        pass

    def set_period(self, v): # real signature unknown; restored from __doc__
        """ set_period(self, v:ICalGLib.Period) """
        pass

    def set_pollcompletion(self, v): # real signature unknown; restored from __doc__
        """ set_pollcompletion(self, v:ICalGLib.PropertyPollcompletion) """
        pass

    def set_pollmode(self, v): # real signature unknown; restored from __doc__
        """ set_pollmode(self, v:ICalGLib.PropertyPollmode) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_query(self, v): # real signature unknown; restored from __doc__
        """ set_query(self, v:str) """
        pass

    def set_querylevel(self, v): # real signature unknown; restored from __doc__
        """ set_querylevel(self, v:ICalGLib.PropertyQuerylevel) """
        pass

    def set_recur(self, v): # real signature unknown; restored from __doc__
        """ set_recur(self, v:ICalGLib.Recurrence) """
        pass

    def set_requeststatus(self, v): # real signature unknown; restored from __doc__
        """ set_requeststatus(self, v:ICalGLib.Reqstat) """
        pass

    def set_status(self, v): # real signature unknown; restored from __doc__
        """ set_status(self, v:ICalGLib.PropertyStatus) """
        pass

    def set_string(self, v): # real signature unknown; restored from __doc__
        """ set_string(self, v:str) """
        pass

    def set_taskmode(self, v): # real signature unknown; restored from __doc__
        """ set_taskmode(self, v:ICalGLib.PropertyTaskmode) """
        pass

    def set_text(self, v): # real signature unknown; restored from __doc__
        """ set_text(self, v:str) """
        pass

    def set_transp(self, v): # real signature unknown; restored from __doc__
        """ set_transp(self, v:ICalGLib.PropertyTransp) """
        pass

    def set_trigger(self, v): # real signature unknown; restored from __doc__
        """ set_trigger(self, v:ICalGLib.Trigger) """
        pass

    def set_uri(self, v): # real signature unknown; restored from __doc__
        """ set_uri(self, v:str) """
        pass

    def set_utcoffset(self, v): # real signature unknown; restored from __doc__
        """ set_utcoffset(self, v:int) """
        pass

    def set_x(self, v): # real signature unknown; restored from __doc__
        """ set_x(self, v:str) """
        pass

    def set_xlicclass(self, v): # real signature unknown; restored from __doc__
        """ set_xlicclass(self, v:ICalGLib.PropertyXlicclass) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1351fd4460>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Value), '__module__': 'gi.repository.ICalGLib', '__gtype__': <GType ICalValue (94403188371776)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_action': gi.FunctionInfo(new_action), 'new_attach': gi.FunctionInfo(new_attach), 'new_binary': gi.FunctionInfo(new_binary), 'new_boolean': gi.FunctionInfo(new_boolean), 'new_busytype': gi.FunctionInfo(new_busytype), 'new_caladdress': gi.FunctionInfo(new_caladdress), 'new_carlevel': gi.FunctionInfo(new_carlevel), 'new_class': gi.FunctionInfo(new_class), 'new_cmd': gi.FunctionInfo(new_cmd), 'new_date': gi.FunctionInfo(new_date), 'new_datetime': gi.FunctionInfo(new_datetime), 'new_datetimedate': gi.FunctionInfo(new_datetimedate), 'new_datetimeperiod': gi.FunctionInfo(new_datetimeperiod), 'new_duration': gi.FunctionInfo(new_duration), 'new_float': gi.FunctionInfo(new_float), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_geo': gi.FunctionInfo(new_geo), 'new_integer': gi.FunctionInfo(new_integer), 'new_method': gi.FunctionInfo(new_method), 'new_period': gi.FunctionInfo(new_period), 'new_pollcompletion': gi.FunctionInfo(new_pollcompletion), 'new_pollmode': gi.FunctionInfo(new_pollmode), 'new_query': gi.FunctionInfo(new_query), 'new_querylevel': gi.FunctionInfo(new_querylevel), 'new_recur': gi.FunctionInfo(new_recur), 'new_requeststatus': gi.FunctionInfo(new_requeststatus), 'new_status': gi.FunctionInfo(new_status), 'new_string': gi.FunctionInfo(new_string), 'new_taskmode': gi.FunctionInfo(new_taskmode), 'new_text': gi.FunctionInfo(new_text), 'new_transp': gi.FunctionInfo(new_transp), 'new_trigger': gi.FunctionInfo(new_trigger), 'new_uri': gi.FunctionInfo(new_uri), 'new_utcoffset': gi.FunctionInfo(new_utcoffset), 'new_x': gi.FunctionInfo(new_x), 'new_xlicclass': gi.FunctionInfo(new_xlicclass), 'decode_ical_string': gi.FunctionInfo(decode_ical_string), 'encode_ical_string': gi.FunctionInfo(encode_ical_string), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_is_valid': gi.FunctionInfo(kind_is_valid), 'kind_to_property_kind': gi.FunctionInfo(kind_to_property_kind), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'as_ical_string': gi.FunctionInfo(as_ical_string), 'clone': gi.FunctionInfo(clone), 'compare': gi.FunctionInfo(compare), 'get_action': gi.FunctionInfo(get_action), 'get_attach': gi.FunctionInfo(get_attach), 'get_binary': gi.FunctionInfo(get_binary), 'get_boolean': gi.FunctionInfo(get_boolean), 'get_busytype': gi.FunctionInfo(get_busytype), 'get_caladdress': gi.FunctionInfo(get_caladdress), 'get_carlevel': gi.FunctionInfo(get_carlevel), 'get_class': gi.FunctionInfo(get_class), 'get_cmd': gi.FunctionInfo(get_cmd), 'get_date': gi.FunctionInfo(get_date), 'get_datetime': gi.FunctionInfo(get_datetime), 'get_datetimedate': gi.FunctionInfo(get_datetimedate), 'get_datetimeperiod': gi.FunctionInfo(get_datetimeperiod), 'get_duration': gi.FunctionInfo(get_duration), 'get_float': gi.FunctionInfo(get_float), 'get_geo': gi.FunctionInfo(get_geo), 'get_integer': gi.FunctionInfo(get_integer), 'get_method': gi.FunctionInfo(get_method), 'get_parent': gi.FunctionInfo(get_parent), 'get_period': gi.FunctionInfo(get_period), 'get_pollcompletion': gi.FunctionInfo(get_pollcompletion), 'get_pollmode': gi.FunctionInfo(get_pollmode), 'get_query': gi.FunctionInfo(get_query), 'get_querylevel': gi.FunctionInfo(get_querylevel), 'get_recur': gi.FunctionInfo(get_recur), 'get_requeststatus': gi.FunctionInfo(get_requeststatus), 'get_status': gi.FunctionInfo(get_status), 'get_string': gi.FunctionInfo(get_string), 'get_taskmode': gi.FunctionInfo(get_taskmode), 'get_text': gi.FunctionInfo(get_text), 'get_transp': gi.FunctionInfo(get_transp), 'get_trigger': gi.FunctionInfo(get_trigger), 'get_uri': gi.FunctionInfo(get_uri), 'get_utcoffset': gi.FunctionInfo(get_utcoffset), 'get_x': gi.FunctionInfo(get_x), 'get_xlicclass': gi.FunctionInfo(get_xlicclass), 'is_valid': gi.FunctionInfo(is_valid), 'isa': gi.FunctionInfo(isa), 'isa_value': gi.FunctionInfo(isa_value), 'reset_kind': gi.FunctionInfo(reset_kind), 'set_action': gi.FunctionInfo(set_action), 'set_attach': gi.FunctionInfo(set_attach), 'set_binary': gi.FunctionInfo(set_binary), 'set_boolean': gi.FunctionInfo(set_boolean), 'set_busytype': gi.FunctionInfo(set_busytype), 'set_caladdress': gi.FunctionInfo(set_caladdress), 'set_carlevel': gi.FunctionInfo(set_carlevel), 'set_class': gi.FunctionInfo(set_class), 'set_cmd': gi.FunctionInfo(set_cmd), 'set_date': gi.FunctionInfo(set_date), 'set_datetime': gi.FunctionInfo(set_datetime), 'set_datetimedate': gi.FunctionInfo(set_datetimedate), 'set_datetimeperiod': gi.FunctionInfo(set_datetimeperiod), 'set_duration': gi.FunctionInfo(set_duration), 'set_float': gi.FunctionInfo(set_float), 'set_geo': gi.FunctionInfo(set_geo), 'set_integer': gi.FunctionInfo(set_integer), 'set_method': gi.FunctionInfo(set_method), 'set_parent': gi.FunctionInfo(set_parent), 'set_period': gi.FunctionInfo(set_period), 'set_pollcompletion': gi.FunctionInfo(set_pollcompletion), 'set_pollmode': gi.FunctionInfo(set_pollmode), 'set_query': gi.FunctionInfo(set_query), 'set_querylevel': gi.FunctionInfo(set_querylevel), 'set_recur': gi.FunctionInfo(set_recur), 'set_requeststatus': gi.FunctionInfo(set_requeststatus), 'set_status': gi.FunctionInfo(set_status), 'set_string': gi.FunctionInfo(set_string), 'set_taskmode': gi.FunctionInfo(set_taskmode), 'set_text': gi.FunctionInfo(set_text), 'set_transp': gi.FunctionInfo(set_transp), 'set_trigger': gi.FunctionInfo(set_trigger), 'set_uri': gi.FunctionInfo(set_uri), 'set_utcoffset': gi.FunctionInfo(set_utcoffset), 'set_x': gi.FunctionInfo(set_x), 'set_xlicclass': gi.FunctionInfo(set_xlicclass)})"
    __gdoc__ = 'Object ICalValue\n\nProperties from ICalObject:\n  native -> gpointer: Native\n    Native libical structure\n  native-destroy-func -> gpointer: Native-Destroy-Func\n    GDestroyNotify function to use to destroy the native libical structure\n  is-global-memory -> gboolean: Is-Global-Memory\n    Whether the native libical structure is from a global shared memory\n  owner -> GObject: Owner\n    The native libical structure owner\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ICalValue (94403188371776)>'
    __info__ = ObjectInfo(Value)


