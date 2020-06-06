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

class Property(Object):
    """
    :Constructors:
    
    ::
    
        Property(**properties)
        new(kind:ICalGLib.PropertyKind) -> ICalGLib.Property
        new_acceptresponse(v:str) -> ICalGLib.Property
        new_acknowledged(v:ICalGLib.Time) -> ICalGLib.Property
        new_action(v:ICalGLib.PropertyAction) -> ICalGLib.Property
        new_allowconflict(v:str) -> ICalGLib.Property
        new_attach(v:ICalGLib.Attach) -> ICalGLib.Property
        new_attendee(v:str) -> ICalGLib.Property
        new_busytype(v:ICalGLib.PropertyBusytype) -> ICalGLib.Property
        new_calid(v:str) -> ICalGLib.Property
        new_calmaster(v:str) -> ICalGLib.Property
        new_calscale(v:str) -> ICalGLib.Property
        new_capversion(v:str) -> ICalGLib.Property
        new_carid(v:str) -> ICalGLib.Property
        new_carlevel(v:ICalGLib.PropertyCarlevel) -> ICalGLib.Property
        new_categories(v:str) -> ICalGLib.Property
        new_class(v:ICalGLib.Property_Class) -> ICalGLib.Property
        new_cmd(v:ICalGLib.PropertyCmd) -> ICalGLib.Property
        new_color(v:str) -> ICalGLib.Property
        new_comment(v:str) -> ICalGLib.Property
        new_completed(v:ICalGLib.Time) -> ICalGLib.Property
        new_components(v:str) -> ICalGLib.Property
        new_contact(v:str) -> ICalGLib.Property
        new_created(v:ICalGLib.Time) -> ICalGLib.Property
        new_csid(v:str) -> ICalGLib.Property
        new_datemax(v:ICalGLib.Time) -> ICalGLib.Property
        new_datemin(v:ICalGLib.Time) -> ICalGLib.Property
        new_decreed(v:str) -> ICalGLib.Property
        new_defaultcharset(v:str) -> ICalGLib.Property
        new_defaultlocale(v:str) -> ICalGLib.Property
        new_defaulttzid(v:str) -> ICalGLib.Property
        new_defaultvcars(v:str) -> ICalGLib.Property
        new_deny(v:str) -> ICalGLib.Property
        new_description(v:str) -> ICalGLib.Property
        new_dtend(v:ICalGLib.Time) -> ICalGLib.Property
        new_dtstamp(v:ICalGLib.Time) -> ICalGLib.Property
        new_dtstart(v:ICalGLib.Time) -> ICalGLib.Property
        new_due(v:ICalGLib.Time) -> ICalGLib.Property
        new_duration(v:ICalGLib.Duration) -> ICalGLib.Property
        new_estimatedduration(v:ICalGLib.Duration) -> ICalGLib.Property
        new_exdate(v:ICalGLib.Time) -> ICalGLib.Property
        new_expand(v:int) -> ICalGLib.Property
        new_exrule(v:ICalGLib.Recurrence) -> ICalGLib.Property
        new_freebusy(v:ICalGLib.Period) -> ICalGLib.Property
        new_from_string(str:str) -> ICalGLib.Property
        new_geo(v:ICalGLib.Geo) -> ICalGLib.Property
        new_grant(v:str) -> ICalGLib.Property
        new_itipversion(v:str) -> ICalGLib.Property
        new_lastmodified(v:ICalGLib.Time) -> ICalGLib.Property
        new_location(v:str) -> ICalGLib.Property
        new_maxcomponentsize(v:int) -> ICalGLib.Property
        new_maxdate(v:ICalGLib.Time) -> ICalGLib.Property
        new_maxresults(v:int) -> ICalGLib.Property
        new_maxresultssize(v:int) -> ICalGLib.Property
        new_method(v:ICalGLib.PropertyMethod) -> ICalGLib.Property
        new_mindate(v:ICalGLib.Time) -> ICalGLib.Property
        new_multipart(v:str) -> ICalGLib.Property
        new_name(v:str) -> ICalGLib.Property
        new_organizer(v:str) -> ICalGLib.Property
        new_owner(v:str) -> ICalGLib.Property
        new_percentcomplete(v:int) -> ICalGLib.Property
        new_permission(v:str) -> ICalGLib.Property
        new_pollcompletion(v:ICalGLib.PropertyPollcompletion) -> ICalGLib.Property
        new_pollitemid(v:int) -> ICalGLib.Property
        new_pollmode(v:ICalGLib.PropertyPollmode) -> ICalGLib.Property
        new_pollproperties(v:str) -> ICalGLib.Property
        new_pollwinner(v:int) -> ICalGLib.Property
        new_priority(v:int) -> ICalGLib.Property
        new_prodid(v:str) -> ICalGLib.Property
        new_query(v:str) -> ICalGLib.Property
        new_queryid(v:str) -> ICalGLib.Property
        new_querylevel(v:ICalGLib.PropertyQuerylevel) -> ICalGLib.Property
        new_queryname(v:str) -> ICalGLib.Property
        new_rdate(v:ICalGLib.Datetimeperiod) -> ICalGLib.Property
        new_recuraccepted(v:str) -> ICalGLib.Property
        new_recurexpand(v:str) -> ICalGLib.Property
        new_recurlimit(v:str) -> ICalGLib.Property
        new_recurrenceid(v:ICalGLib.Time) -> ICalGLib.Property
        new_relatedto(v:str) -> ICalGLib.Property
        new_relcalid(v:str) -> ICalGLib.Property
        new_repeat(v:int) -> ICalGLib.Property
        new_replyurl(v:str) -> ICalGLib.Property
        new_requeststatus(v:ICalGLib.Reqstat) -> ICalGLib.Property
        new_resources(v:str) -> ICalGLib.Property
        new_response(v:int) -> ICalGLib.Property
        new_restriction(v:str) -> ICalGLib.Property
        new_rrule(v:ICalGLib.Recurrence) -> ICalGLib.Property
        new_scope(v:str) -> ICalGLib.Property
        new_sequence(v:int) -> ICalGLib.Property
        new_status(v:ICalGLib.PropertyStatus) -> ICalGLib.Property
        new_storesexpanded(v:str) -> ICalGLib.Property
        new_summary(v:str) -> ICalGLib.Property
        new_target(v:str) -> ICalGLib.Property
        new_taskmode(v:ICalGLib.PropertyTaskmode) -> ICalGLib.Property
        new_transp(v:ICalGLib.PropertyTransp) -> ICalGLib.Property
        new_trigger(v:ICalGLib.Trigger) -> ICalGLib.Property
        new_tzid(v:str) -> ICalGLib.Property
        new_tzidaliasof(v:str) -> ICalGLib.Property
        new_tzname(v:str) -> ICalGLib.Property
        new_tzoffsetfrom(v:int) -> ICalGLib.Property
        new_tzoffsetto(v:int) -> ICalGLib.Property
        new_tzuntil(v:ICalGLib.Time) -> ICalGLib.Property
        new_tzurl(v:str) -> ICalGLib.Property
        new_uid(v:str) -> ICalGLib.Property
        new_url(v:str) -> ICalGLib.Property
        new_version(v:str) -> ICalGLib.Property
        new_voter(v:str) -> ICalGLib.Property
        new_x(v:str) -> ICalGLib.Property
        new_xlicclass(v:ICalGLib.PropertyXlicclass) -> ICalGLib.Property
        new_xlicclustercount(v:str) -> ICalGLib.Property
        new_xlicerror(v:str) -> ICalGLib.Property
        new_xlicmimecharset(v:str) -> ICalGLib.Property
        new_xlicmimecid(v:str) -> ICalGLib.Property
        new_xlicmimecontenttype(v:str) -> ICalGLib.Property
        new_xlicmimeencoding(v:str) -> ICalGLib.Property
        new_xlicmimefilename(v:str) -> ICalGLib.Property
        new_xlicmimeoptinfo(v:str) -> ICalGLib.Property
    """
    def add_depender(self, depender): # real signature unknown; restored from __doc__
        """ add_depender(self, depender:GObject.Object) """
        pass

    def add_parameter(self, parameter): # real signature unknown; restored from __doc__
        """ add_parameter(self, parameter:ICalGLib.Parameter) """
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
        """ clone(self) -> ICalGLib.Property """
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

    def count_parameters(self): # real signature unknown; restored from __doc__
        """ count_parameters(self) -> int """
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

    def enum_to_string(self, e): # real signature unknown; restored from __doc__
        """ enum_to_string(e:int) -> str """
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

    def get_acceptresponse(self): # real signature unknown; restored from __doc__
        """ get_acceptresponse(self) -> str """
        return ""

    def get_acknowledged(self): # real signature unknown; restored from __doc__
        """ get_acknowledged(self) -> ICalGLib.Time """
        pass

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> ICalGLib.PropertyAction """
        pass

    def get_allowconflict(self): # real signature unknown; restored from __doc__
        """ get_allowconflict(self) -> str """
        return ""

    def get_attach(self): # real signature unknown; restored from __doc__
        """ get_attach(self) -> ICalGLib.Attach """
        pass

    def get_attendee(self): # real signature unknown; restored from __doc__
        """ get_attendee(self) -> str """
        return ""

    def get_busytype(self): # real signature unknown; restored from __doc__
        """ get_busytype(self) -> ICalGLib.PropertyBusytype """
        pass

    def get_calid(self): # real signature unknown; restored from __doc__
        """ get_calid(self) -> str """
        return ""

    def get_calmaster(self): # real signature unknown; restored from __doc__
        """ get_calmaster(self) -> str """
        return ""

    def get_calscale(self): # real signature unknown; restored from __doc__
        """ get_calscale(self) -> str """
        return ""

    def get_capversion(self): # real signature unknown; restored from __doc__
        """ get_capversion(self) -> str """
        return ""

    def get_carid(self): # real signature unknown; restored from __doc__
        """ get_carid(self) -> str """
        return ""

    def get_carlevel(self): # real signature unknown; restored from __doc__
        """ get_carlevel(self) -> ICalGLib.PropertyCarlevel """
        pass

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> str """
        return ""

    def get_class(self): # real signature unknown; restored from __doc__
        """ get_class(self) -> ICalGLib.Property_Class """
        pass

    def get_cmd(self): # real signature unknown; restored from __doc__
        """ get_cmd(self) -> ICalGLib.PropertyCmd """
        pass

    def get_color(self): # real signature unknown; restored from __doc__
        """ get_color(self) -> str """
        return ""

    def get_comment(self): # real signature unknown; restored from __doc__
        """ get_comment(self) -> str """
        return ""

    def get_completed(self): # real signature unknown; restored from __doc__
        """ get_completed(self) -> ICalGLib.Time """
        pass

    def get_components(self): # real signature unknown; restored from __doc__
        """ get_components(self) -> str """
        return ""

    def get_contact(self): # real signature unknown; restored from __doc__
        """ get_contact(self) -> str """
        return ""

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> ICalGLib.Time """
        pass

    def get_csid(self): # real signature unknown; restored from __doc__
        """ get_csid(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_datemax(self): # real signature unknown; restored from __doc__
        """ get_datemax(self) -> ICalGLib.Time """
        pass

    def get_datemin(self): # real signature unknown; restored from __doc__
        """ get_datemin(self) -> ICalGLib.Time """
        pass

    def get_datetime_with_component(self, comp=None): # real signature unknown; restored from __doc__
        """ get_datetime_with_component(self, comp:ICalGLib.Component=None) -> ICalGLib.Time """
        pass

    def get_decreed(self): # real signature unknown; restored from __doc__
        """ get_decreed(self) -> str """
        return ""

    def get_defaultcharset(self): # real signature unknown; restored from __doc__
        """ get_defaultcharset(self) -> str """
        return ""

    def get_defaultlocale(self): # real signature unknown; restored from __doc__
        """ get_defaultlocale(self) -> str """
        return ""

    def get_defaulttzid(self): # real signature unknown; restored from __doc__
        """ get_defaulttzid(self) -> str """
        return ""

    def get_defaultvcars(self): # real signature unknown; restored from __doc__
        """ get_defaultvcars(self) -> str """
        return ""

    def get_deny(self): # real signature unknown; restored from __doc__
        """ get_deny(self) -> str """
        return ""

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

    def get_estimatedduration(self): # real signature unknown; restored from __doc__
        """ get_estimatedduration(self) -> ICalGLib.Duration """
        pass

    def get_exdate(self): # real signature unknown; restored from __doc__
        """ get_exdate(self) -> ICalGLib.Time """
        pass

    def get_expand(self): # real signature unknown; restored from __doc__
        """ get_expand(self) -> int """
        return 0

    def get_exrule(self): # real signature unknown; restored from __doc__
        """ get_exrule(self) -> ICalGLib.Recurrence """
        pass

    def get_first_parameter(self, kind): # real signature unknown; restored from __doc__
        """ get_first_parameter(self, kind:ICalGLib.ParameterKind) -> ICalGLib.Parameter """
        pass

    def get_freebusy(self): # real signature unknown; restored from __doc__
        """ get_freebusy(self) -> ICalGLib.Period """
        pass

    def get_geo(self): # real signature unknown; restored from __doc__
        """ get_geo(self) -> ICalGLib.Geo """
        pass

    def get_grant(self): # real signature unknown; restored from __doc__
        """ get_grant(self) -> str """
        return ""

    def get_is_global_memory(self): # real signature unknown; restored from __doc__
        """ get_is_global_memory(self) -> bool """
        return False

    def get_itipversion(self): # real signature unknown; restored from __doc__
        """ get_itipversion(self) -> str """
        return ""

    def get_lastmodified(self): # real signature unknown; restored from __doc__
        """ get_lastmodified(self) -> ICalGLib.Time """
        pass

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> str """
        return ""

    def get_maxcomponentsize(self): # real signature unknown; restored from __doc__
        """ get_maxcomponentsize(self) -> int """
        return 0

    def get_maxdate(self): # real signature unknown; restored from __doc__
        """ get_maxdate(self) -> ICalGLib.Time """
        pass

    def get_maxresults(self): # real signature unknown; restored from __doc__
        """ get_maxresults(self) -> int """
        return 0

    def get_maxresultssize(self): # real signature unknown; restored from __doc__
        """ get_maxresultssize(self) -> int """
        return 0

    def get_method(self): # real signature unknown; restored from __doc__
        """ get_method(self) -> ICalGLib.PropertyMethod """
        pass

    def get_mindate(self): # real signature unknown; restored from __doc__
        """ get_mindate(self) -> ICalGLib.Time """
        pass

    def get_multipart(self): # real signature unknown; restored from __doc__
        """ get_multipart(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_next_parameter(self, kind): # real signature unknown; restored from __doc__
        """ get_next_parameter(self, kind:ICalGLib.ParameterKind) -> ICalGLib.Parameter """
        pass

    def get_organizer(self): # real signature unknown; restored from __doc__
        """ get_organizer(self) -> str """
        return ""

    def get_owner(self): # real signature unknown; restored from __doc__
        """ get_owner(self) -> str """
        return ""

    def get_parameter_as_string(self, name): # real signature unknown; restored from __doc__
        """ get_parameter_as_string(self, name:str) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> ICalGLib.Component or None """
        pass

    def get_percentcomplete(self): # real signature unknown; restored from __doc__
        """ get_percentcomplete(self) -> int """
        return 0

    def get_permission(self): # real signature unknown; restored from __doc__
        """ get_permission(self) -> str """
        return ""

    def get_pollcompletion(self): # real signature unknown; restored from __doc__
        """ get_pollcompletion(self) -> ICalGLib.PropertyPollcompletion """
        pass

    def get_pollitemid(self): # real signature unknown; restored from __doc__
        """ get_pollitemid(self) -> int """
        return 0

    def get_pollmode(self): # real signature unknown; restored from __doc__
        """ get_pollmode(self) -> ICalGLib.PropertyPollmode """
        pass

    def get_pollproperties(self): # real signature unknown; restored from __doc__
        """ get_pollproperties(self) -> str """
        return ""

    def get_pollwinner(self): # real signature unknown; restored from __doc__
        """ get_pollwinner(self) -> int """
        return 0

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_prodid(self): # real signature unknown; restored from __doc__
        """ get_prodid(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_property_name(self): # real signature unknown; restored from __doc__
        """ get_property_name(self) -> str """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_query(self): # real signature unknown; restored from __doc__
        """ get_query(self) -> str """
        return ""

    def get_queryid(self): # real signature unknown; restored from __doc__
        """ get_queryid(self) -> str """
        return ""

    def get_querylevel(self): # real signature unknown; restored from __doc__
        """ get_querylevel(self) -> ICalGLib.PropertyQuerylevel """
        pass

    def get_queryname(self): # real signature unknown; restored from __doc__
        """ get_queryname(self) -> str """
        return ""

    def get_rdate(self): # real signature unknown; restored from __doc__
        """ get_rdate(self) -> ICalGLib.Datetimeperiod """
        pass

    def get_recuraccepted(self): # real signature unknown; restored from __doc__
        """ get_recuraccepted(self) -> str """
        return ""

    def get_recurexpand(self): # real signature unknown; restored from __doc__
        """ get_recurexpand(self) -> str """
        return ""

    def get_recurlimit(self): # real signature unknown; restored from __doc__
        """ get_recurlimit(self) -> str """
        return ""

    def get_recurrenceid(self): # real signature unknown; restored from __doc__
        """ get_recurrenceid(self) -> ICalGLib.Time """
        pass

    def get_relatedto(self): # real signature unknown; restored from __doc__
        """ get_relatedto(self) -> str """
        return ""

    def get_relcalid(self): # real signature unknown; restored from __doc__
        """ get_relcalid(self) -> str """
        return ""

    def get_repeat(self): # real signature unknown; restored from __doc__
        """ get_repeat(self) -> int """
        return 0

    def get_replyurl(self): # real signature unknown; restored from __doc__
        """ get_replyurl(self) -> str """
        return ""

    def get_requeststatus(self): # real signature unknown; restored from __doc__
        """ get_requeststatus(self) -> ICalGLib.Reqstat """
        pass

    def get_resources(self): # real signature unknown; restored from __doc__
        """ get_resources(self) -> str """
        return ""

    def get_response(self): # real signature unknown; restored from __doc__
        """ get_response(self) -> int """
        return 0

    def get_restriction(self): # real signature unknown; restored from __doc__
        """ get_restriction(self) -> str """
        return ""

    def get_rrule(self): # real signature unknown; restored from __doc__
        """ get_rrule(self) -> ICalGLib.Recurrence """
        pass

    def get_scope(self): # real signature unknown; restored from __doc__
        """ get_scope(self) -> str """
        return ""

    def get_sequence(self): # real signature unknown; restored from __doc__
        """ get_sequence(self) -> int """
        return 0

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> ICalGLib.PropertyStatus """
        pass

    def get_storesexpanded(self): # real signature unknown; restored from __doc__
        """ get_storesexpanded(self) -> str """
        return ""

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

    def get_target(self): # real signature unknown; restored from __doc__
        """ get_target(self) -> str """
        return ""

    def get_taskmode(self): # real signature unknown; restored from __doc__
        """ get_taskmode(self) -> ICalGLib.PropertyTaskmode """
        pass

    def get_transp(self): # real signature unknown; restored from __doc__
        """ get_transp(self) -> ICalGLib.PropertyTransp """
        pass

    def get_trigger(self): # real signature unknown; restored from __doc__
        """ get_trigger(self) -> ICalGLib.Trigger """
        pass

    def get_tzid(self): # real signature unknown; restored from __doc__
        """ get_tzid(self) -> str """
        return ""

    def get_tzidaliasof(self): # real signature unknown; restored from __doc__
        """ get_tzidaliasof(self) -> str """
        return ""

    def get_tzname(self): # real signature unknown; restored from __doc__
        """ get_tzname(self) -> str """
        return ""

    def get_tzoffsetfrom(self): # real signature unknown; restored from __doc__
        """ get_tzoffsetfrom(self) -> int """
        return 0

    def get_tzoffsetto(self): # real signature unknown; restored from __doc__
        """ get_tzoffsetto(self) -> int """
        return 0

    def get_tzuntil(self): # real signature unknown; restored from __doc__
        """ get_tzuntil(self) -> ICalGLib.Time """
        pass

    def get_tzurl(self): # real signature unknown; restored from __doc__
        """ get_tzurl(self) -> str """
        return ""

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> str """
        return ""

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) -> ICalGLib.Value """
        pass

    def get_value_as_string(self): # real signature unknown; restored from __doc__
        """ get_value_as_string(self) -> str """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str """
        return ""

    def get_voter(self): # real signature unknown; restored from __doc__
        """ get_voter(self) -> str """
        return ""

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> str """
        return ""

    def get_xlicclass(self): # real signature unknown; restored from __doc__
        """ get_xlicclass(self) -> ICalGLib.PropertyXlicclass """
        pass

    def get_xlicclustercount(self): # real signature unknown; restored from __doc__
        """ get_xlicclustercount(self) -> str """
        return ""

    def get_xlicerror(self): # real signature unknown; restored from __doc__
        """ get_xlicerror(self) -> str """
        return ""

    def get_xlicmimecharset(self): # real signature unknown; restored from __doc__
        """ get_xlicmimecharset(self) -> str """
        return ""

    def get_xlicmimecid(self): # real signature unknown; restored from __doc__
        """ get_xlicmimecid(self) -> str """
        return ""

    def get_xlicmimecontenttype(self): # real signature unknown; restored from __doc__
        """ get_xlicmimecontenttype(self) -> str """
        return ""

    def get_xlicmimeencoding(self): # real signature unknown; restored from __doc__
        """ get_xlicmimeencoding(self) -> str """
        return ""

    def get_xlicmimefilename(self): # real signature unknown; restored from __doc__
        """ get_xlicmimefilename(self) -> str """
        return ""

    def get_xlicmimeoptinfo(self): # real signature unknown; restored from __doc__
        """ get_xlicmimeoptinfo(self) -> str """
        return ""

    def get_x_name(self): # real signature unknown; restored from __doc__
        """ get_x_name(self) -> str or None """
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
        """ isa(self) -> ICalGLib.PropertyKind """
        pass

    def isa_property(self): # real signature unknown; restored from __doc__
        """ isa_property(self) -> int """
        return 0

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def kind_and_string_to_enum(self, kind, p_str): # real signature unknown; restored from __doc__
        """ kind_and_string_to_enum(kind:int, str:str) -> int """
        return 0

    def kind_from_string(self, string): # real signature unknown; restored from __doc__
        """ kind_from_string(string:str) -> ICalGLib.PropertyKind """
        pass

    def kind_has_property(self, kind, e): # real signature unknown; restored from __doc__
        """ kind_has_property(kind:ICalGLib.PropertyKind, e:int) -> int """
        return 0

    def kind_is_valid(self, kind): # real signature unknown; restored from __doc__
        """ kind_is_valid(kind:ICalGLib.PropertyKind) -> bool """
        return False

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:ICalGLib.PropertyKind) -> str """
        return ""

    def kind_to_value_kind(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_value_kind(kind:ICalGLib.PropertyKind) -> ICalGLib.ValueKind """
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def method_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ method_from_string(str:str) -> ICalGLib.PropertyMethod """
        pass

    def method_to_string(self, method): # real signature unknown; restored from __doc__
        """ method_to_string(method:ICalGLib.PropertyMethod) -> str """
        return ""

    def new(self, kind): # real signature unknown; restored from __doc__
        """ new(kind:ICalGLib.PropertyKind) -> ICalGLib.Property """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_acceptresponse(self, v): # real signature unknown; restored from __doc__
        """ new_acceptresponse(v:str) -> ICalGLib.Property """
        pass

    def new_acknowledged(self, v): # real signature unknown; restored from __doc__
        """ new_acknowledged(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_action(self, v): # real signature unknown; restored from __doc__
        """ new_action(v:ICalGLib.PropertyAction) -> ICalGLib.Property """
        pass

    def new_allowconflict(self, v): # real signature unknown; restored from __doc__
        """ new_allowconflict(v:str) -> ICalGLib.Property """
        pass

    def new_attach(self, v): # real signature unknown; restored from __doc__
        """ new_attach(v:ICalGLib.Attach) -> ICalGLib.Property """
        pass

    def new_attendee(self, v): # real signature unknown; restored from __doc__
        """ new_attendee(v:str) -> ICalGLib.Property """
        pass

    def new_busytype(self, v): # real signature unknown; restored from __doc__
        """ new_busytype(v:ICalGLib.PropertyBusytype) -> ICalGLib.Property """
        pass

    def new_calid(self, v): # real signature unknown; restored from __doc__
        """ new_calid(v:str) -> ICalGLib.Property """
        pass

    def new_calmaster(self, v): # real signature unknown; restored from __doc__
        """ new_calmaster(v:str) -> ICalGLib.Property """
        pass

    def new_calscale(self, v): # real signature unknown; restored from __doc__
        """ new_calscale(v:str) -> ICalGLib.Property """
        pass

    def new_capversion(self, v): # real signature unknown; restored from __doc__
        """ new_capversion(v:str) -> ICalGLib.Property """
        pass

    def new_carid(self, v): # real signature unknown; restored from __doc__
        """ new_carid(v:str) -> ICalGLib.Property """
        pass

    def new_carlevel(self, v): # real signature unknown; restored from __doc__
        """ new_carlevel(v:ICalGLib.PropertyCarlevel) -> ICalGLib.Property """
        pass

    def new_categories(self, v): # real signature unknown; restored from __doc__
        """ new_categories(v:str) -> ICalGLib.Property """
        pass

    def new_class(self, v): # real signature unknown; restored from __doc__
        """ new_class(v:ICalGLib.Property_Class) -> ICalGLib.Property """
        pass

    def new_cmd(self, v): # real signature unknown; restored from __doc__
        """ new_cmd(v:ICalGLib.PropertyCmd) -> ICalGLib.Property """
        pass

    def new_color(self, v): # real signature unknown; restored from __doc__
        """ new_color(v:str) -> ICalGLib.Property """
        pass

    def new_comment(self, v): # real signature unknown; restored from __doc__
        """ new_comment(v:str) -> ICalGLib.Property """
        pass

    def new_completed(self, v): # real signature unknown; restored from __doc__
        """ new_completed(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_components(self, v): # real signature unknown; restored from __doc__
        """ new_components(v:str) -> ICalGLib.Property """
        pass

    def new_contact(self, v): # real signature unknown; restored from __doc__
        """ new_contact(v:str) -> ICalGLib.Property """
        pass

    def new_created(self, v): # real signature unknown; restored from __doc__
        """ new_created(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_csid(self, v): # real signature unknown; restored from __doc__
        """ new_csid(v:str) -> ICalGLib.Property """
        pass

    def new_datemax(self, v): # real signature unknown; restored from __doc__
        """ new_datemax(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_datemin(self, v): # real signature unknown; restored from __doc__
        """ new_datemin(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_decreed(self, v): # real signature unknown; restored from __doc__
        """ new_decreed(v:str) -> ICalGLib.Property """
        pass

    def new_defaultcharset(self, v): # real signature unknown; restored from __doc__
        """ new_defaultcharset(v:str) -> ICalGLib.Property """
        pass

    def new_defaultlocale(self, v): # real signature unknown; restored from __doc__
        """ new_defaultlocale(v:str) -> ICalGLib.Property """
        pass

    def new_defaulttzid(self, v): # real signature unknown; restored from __doc__
        """ new_defaulttzid(v:str) -> ICalGLib.Property """
        pass

    def new_defaultvcars(self, v): # real signature unknown; restored from __doc__
        """ new_defaultvcars(v:str) -> ICalGLib.Property """
        pass

    def new_deny(self, v): # real signature unknown; restored from __doc__
        """ new_deny(v:str) -> ICalGLib.Property """
        pass

    def new_description(self, v): # real signature unknown; restored from __doc__
        """ new_description(v:str) -> ICalGLib.Property """
        pass

    def new_dtend(self, v): # real signature unknown; restored from __doc__
        """ new_dtend(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_dtstamp(self, v): # real signature unknown; restored from __doc__
        """ new_dtstamp(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_dtstart(self, v): # real signature unknown; restored from __doc__
        """ new_dtstart(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_due(self, v): # real signature unknown; restored from __doc__
        """ new_due(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_duration(self, v): # real signature unknown; restored from __doc__
        """ new_duration(v:ICalGLib.Duration) -> ICalGLib.Property """
        pass

    def new_estimatedduration(self, v): # real signature unknown; restored from __doc__
        """ new_estimatedduration(v:ICalGLib.Duration) -> ICalGLib.Property """
        pass

    def new_exdate(self, v): # real signature unknown; restored from __doc__
        """ new_exdate(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_expand(self, v): # real signature unknown; restored from __doc__
        """ new_expand(v:int) -> ICalGLib.Property """
        pass

    def new_exrule(self, v): # real signature unknown; restored from __doc__
        """ new_exrule(v:ICalGLib.Recurrence) -> ICalGLib.Property """
        pass

    def new_freebusy(self, v): # real signature unknown; restored from __doc__
        """ new_freebusy(v:ICalGLib.Period) -> ICalGLib.Property """
        pass

    def new_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ new_from_string(str:str) -> ICalGLib.Property """
        pass

    def new_geo(self, v): # real signature unknown; restored from __doc__
        """ new_geo(v:ICalGLib.Geo) -> ICalGLib.Property """
        pass

    def new_grant(self, v): # real signature unknown; restored from __doc__
        """ new_grant(v:str) -> ICalGLib.Property """
        pass

    def new_itipversion(self, v): # real signature unknown; restored from __doc__
        """ new_itipversion(v:str) -> ICalGLib.Property """
        pass

    def new_lastmodified(self, v): # real signature unknown; restored from __doc__
        """ new_lastmodified(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_location(self, v): # real signature unknown; restored from __doc__
        """ new_location(v:str) -> ICalGLib.Property """
        pass

    def new_maxcomponentsize(self, v): # real signature unknown; restored from __doc__
        """ new_maxcomponentsize(v:int) -> ICalGLib.Property """
        pass

    def new_maxdate(self, v): # real signature unknown; restored from __doc__
        """ new_maxdate(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_maxresults(self, v): # real signature unknown; restored from __doc__
        """ new_maxresults(v:int) -> ICalGLib.Property """
        pass

    def new_maxresultssize(self, v): # real signature unknown; restored from __doc__
        """ new_maxresultssize(v:int) -> ICalGLib.Property """
        pass

    def new_method(self, v): # real signature unknown; restored from __doc__
        """ new_method(v:ICalGLib.PropertyMethod) -> ICalGLib.Property """
        pass

    def new_mindate(self, v): # real signature unknown; restored from __doc__
        """ new_mindate(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_multipart(self, v): # real signature unknown; restored from __doc__
        """ new_multipart(v:str) -> ICalGLib.Property """
        pass

    def new_name(self, v): # real signature unknown; restored from __doc__
        """ new_name(v:str) -> ICalGLib.Property """
        pass

    def new_organizer(self, v): # real signature unknown; restored from __doc__
        """ new_organizer(v:str) -> ICalGLib.Property """
        pass

    def new_owner(self, v): # real signature unknown; restored from __doc__
        """ new_owner(v:str) -> ICalGLib.Property """
        pass

    def new_percentcomplete(self, v): # real signature unknown; restored from __doc__
        """ new_percentcomplete(v:int) -> ICalGLib.Property """
        pass

    def new_permission(self, v): # real signature unknown; restored from __doc__
        """ new_permission(v:str) -> ICalGLib.Property """
        pass

    def new_pollcompletion(self, v): # real signature unknown; restored from __doc__
        """ new_pollcompletion(v:ICalGLib.PropertyPollcompletion) -> ICalGLib.Property """
        pass

    def new_pollitemid(self, v): # real signature unknown; restored from __doc__
        """ new_pollitemid(v:int) -> ICalGLib.Property """
        pass

    def new_pollmode(self, v): # real signature unknown; restored from __doc__
        """ new_pollmode(v:ICalGLib.PropertyPollmode) -> ICalGLib.Property """
        pass

    def new_pollproperties(self, v): # real signature unknown; restored from __doc__
        """ new_pollproperties(v:str) -> ICalGLib.Property """
        pass

    def new_pollwinner(self, v): # real signature unknown; restored from __doc__
        """ new_pollwinner(v:int) -> ICalGLib.Property """
        pass

    def new_priority(self, v): # real signature unknown; restored from __doc__
        """ new_priority(v:int) -> ICalGLib.Property """
        pass

    def new_prodid(self, v): # real signature unknown; restored from __doc__
        """ new_prodid(v:str) -> ICalGLib.Property """
        pass

    def new_query(self, v): # real signature unknown; restored from __doc__
        """ new_query(v:str) -> ICalGLib.Property """
        pass

    def new_queryid(self, v): # real signature unknown; restored from __doc__
        """ new_queryid(v:str) -> ICalGLib.Property """
        pass

    def new_querylevel(self, v): # real signature unknown; restored from __doc__
        """ new_querylevel(v:ICalGLib.PropertyQuerylevel) -> ICalGLib.Property """
        pass

    def new_queryname(self, v): # real signature unknown; restored from __doc__
        """ new_queryname(v:str) -> ICalGLib.Property """
        pass

    def new_rdate(self, v): # real signature unknown; restored from __doc__
        """ new_rdate(v:ICalGLib.Datetimeperiod) -> ICalGLib.Property """
        pass

    def new_recuraccepted(self, v): # real signature unknown; restored from __doc__
        """ new_recuraccepted(v:str) -> ICalGLib.Property """
        pass

    def new_recurexpand(self, v): # real signature unknown; restored from __doc__
        """ new_recurexpand(v:str) -> ICalGLib.Property """
        pass

    def new_recurlimit(self, v): # real signature unknown; restored from __doc__
        """ new_recurlimit(v:str) -> ICalGLib.Property """
        pass

    def new_recurrenceid(self, v): # real signature unknown; restored from __doc__
        """ new_recurrenceid(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_relatedto(self, v): # real signature unknown; restored from __doc__
        """ new_relatedto(v:str) -> ICalGLib.Property """
        pass

    def new_relcalid(self, v): # real signature unknown; restored from __doc__
        """ new_relcalid(v:str) -> ICalGLib.Property """
        pass

    def new_repeat(self, v): # real signature unknown; restored from __doc__
        """ new_repeat(v:int) -> ICalGLib.Property """
        pass

    def new_replyurl(self, v): # real signature unknown; restored from __doc__
        """ new_replyurl(v:str) -> ICalGLib.Property """
        pass

    def new_requeststatus(self, v): # real signature unknown; restored from __doc__
        """ new_requeststatus(v:ICalGLib.Reqstat) -> ICalGLib.Property """
        pass

    def new_resources(self, v): # real signature unknown; restored from __doc__
        """ new_resources(v:str) -> ICalGLib.Property """
        pass

    def new_response(self, v): # real signature unknown; restored from __doc__
        """ new_response(v:int) -> ICalGLib.Property """
        pass

    def new_restriction(self, v): # real signature unknown; restored from __doc__
        """ new_restriction(v:str) -> ICalGLib.Property """
        pass

    def new_rrule(self, v): # real signature unknown; restored from __doc__
        """ new_rrule(v:ICalGLib.Recurrence) -> ICalGLib.Property """
        pass

    def new_scope(self, v): # real signature unknown; restored from __doc__
        """ new_scope(v:str) -> ICalGLib.Property """
        pass

    def new_sequence(self, v): # real signature unknown; restored from __doc__
        """ new_sequence(v:int) -> ICalGLib.Property """
        pass

    def new_status(self, v): # real signature unknown; restored from __doc__
        """ new_status(v:ICalGLib.PropertyStatus) -> ICalGLib.Property """
        pass

    def new_storesexpanded(self, v): # real signature unknown; restored from __doc__
        """ new_storesexpanded(v:str) -> ICalGLib.Property """
        pass

    def new_summary(self, v): # real signature unknown; restored from __doc__
        """ new_summary(v:str) -> ICalGLib.Property """
        pass

    def new_target(self, v): # real signature unknown; restored from __doc__
        """ new_target(v:str) -> ICalGLib.Property """
        pass

    def new_taskmode(self, v): # real signature unknown; restored from __doc__
        """ new_taskmode(v:ICalGLib.PropertyTaskmode) -> ICalGLib.Property """
        pass

    def new_transp(self, v): # real signature unknown; restored from __doc__
        """ new_transp(v:ICalGLib.PropertyTransp) -> ICalGLib.Property """
        pass

    def new_trigger(self, v): # real signature unknown; restored from __doc__
        """ new_trigger(v:ICalGLib.Trigger) -> ICalGLib.Property """
        pass

    def new_tzid(self, v): # real signature unknown; restored from __doc__
        """ new_tzid(v:str) -> ICalGLib.Property """
        pass

    def new_tzidaliasof(self, v): # real signature unknown; restored from __doc__
        """ new_tzidaliasof(v:str) -> ICalGLib.Property """
        pass

    def new_tzname(self, v): # real signature unknown; restored from __doc__
        """ new_tzname(v:str) -> ICalGLib.Property """
        pass

    def new_tzoffsetfrom(self, v): # real signature unknown; restored from __doc__
        """ new_tzoffsetfrom(v:int) -> ICalGLib.Property """
        pass

    def new_tzoffsetto(self, v): # real signature unknown; restored from __doc__
        """ new_tzoffsetto(v:int) -> ICalGLib.Property """
        pass

    def new_tzuntil(self, v): # real signature unknown; restored from __doc__
        """ new_tzuntil(v:ICalGLib.Time) -> ICalGLib.Property """
        pass

    def new_tzurl(self, v): # real signature unknown; restored from __doc__
        """ new_tzurl(v:str) -> ICalGLib.Property """
        pass

    def new_uid(self, v): # real signature unknown; restored from __doc__
        """ new_uid(v:str) -> ICalGLib.Property """
        pass

    def new_url(self, v): # real signature unknown; restored from __doc__
        """ new_url(v:str) -> ICalGLib.Property """
        pass

    def new_version(self, v): # real signature unknown; restored from __doc__
        """ new_version(v:str) -> ICalGLib.Property """
        pass

    def new_voter(self, v): # real signature unknown; restored from __doc__
        """ new_voter(v:str) -> ICalGLib.Property """
        pass

    def new_x(self, v): # real signature unknown; restored from __doc__
        """ new_x(v:str) -> ICalGLib.Property """
        pass

    def new_xlicclass(self, v): # real signature unknown; restored from __doc__
        """ new_xlicclass(v:ICalGLib.PropertyXlicclass) -> ICalGLib.Property """
        pass

    def new_xlicclustercount(self, v): # real signature unknown; restored from __doc__
        """ new_xlicclustercount(v:str) -> ICalGLib.Property """
        pass

    def new_xlicerror(self, v): # real signature unknown; restored from __doc__
        """ new_xlicerror(v:str) -> ICalGLib.Property """
        pass

    def new_xlicmimecharset(self, v): # real signature unknown; restored from __doc__
        """ new_xlicmimecharset(v:str) -> ICalGLib.Property """
        pass

    def new_xlicmimecid(self, v): # real signature unknown; restored from __doc__
        """ new_xlicmimecid(v:str) -> ICalGLib.Property """
        pass

    def new_xlicmimecontenttype(self, v): # real signature unknown; restored from __doc__
        """ new_xlicmimecontenttype(v:str) -> ICalGLib.Property """
        pass

    def new_xlicmimeencoding(self, v): # real signature unknown; restored from __doc__
        """ new_xlicmimeencoding(v:str) -> ICalGLib.Property """
        pass

    def new_xlicmimefilename(self, v): # real signature unknown; restored from __doc__
        """ new_xlicmimefilename(v:str) -> ICalGLib.Property """
        pass

    def new_xlicmimeoptinfo(self, v): # real signature unknown; restored from __doc__
        """ new_xlicmimeoptinfo(v:str) -> ICalGLib.Property """
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

    def recurrence_is_excluded(self, comp, dtstart, recurtime): # real signature unknown; restored from __doc__
        """ recurrence_is_excluded(comp:ICalGLib.Component, dtstart:ICalGLib.Time, recurtime:ICalGLib.Time) -> bool """
        return False

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

    def remove_parameter_by_kind(self, kind): # real signature unknown; restored from __doc__
        """ remove_parameter_by_kind(self, kind:ICalGLib.ParameterKind) """
        pass

    def remove_parameter_by_name(self, name): # real signature unknown; restored from __doc__
        """ remove_parameter_by_name(self, name:str) """
        pass

    def remove_parameter_by_ref(self, param): # real signature unknown; restored from __doc__
        """ remove_parameter_by_ref(self, param:ICalGLib.Parameter) """
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

    def set_acceptresponse(self, v): # real signature unknown; restored from __doc__
        """ set_acceptresponse(self, v:str) """
        pass

    def set_acknowledged(self, v): # real signature unknown; restored from __doc__
        """ set_acknowledged(self, v:ICalGLib.Time) """
        pass

    def set_action(self, v): # real signature unknown; restored from __doc__
        """ set_action(self, v:ICalGLib.PropertyAction) """
        pass

    def set_allowconflict(self, v): # real signature unknown; restored from __doc__
        """ set_allowconflict(self, v:str) """
        pass

    def set_attach(self, v): # real signature unknown; restored from __doc__
        """ set_attach(self, v:ICalGLib.Attach) """
        pass

    def set_attendee(self, v): # real signature unknown; restored from __doc__
        """ set_attendee(self, v:str) """
        pass

    def set_busytype(self, v): # real signature unknown; restored from __doc__
        """ set_busytype(self, v:ICalGLib.PropertyBusytype) """
        pass

    def set_calid(self, v): # real signature unknown; restored from __doc__
        """ set_calid(self, v:str) """
        pass

    def set_calmaster(self, v): # real signature unknown; restored from __doc__
        """ set_calmaster(self, v:str) """
        pass

    def set_calscale(self, v): # real signature unknown; restored from __doc__
        """ set_calscale(self, v:str) """
        pass

    def set_capversion(self, v): # real signature unknown; restored from __doc__
        """ set_capversion(self, v:str) """
        pass

    def set_carid(self, v): # real signature unknown; restored from __doc__
        """ set_carid(self, v:str) """
        pass

    def set_carlevel(self, v): # real signature unknown; restored from __doc__
        """ set_carlevel(self, v:ICalGLib.PropertyCarlevel) """
        pass

    def set_categories(self, v): # real signature unknown; restored from __doc__
        """ set_categories(self, v:str) """
        pass

    def set_class(self, v): # real signature unknown; restored from __doc__
        """ set_class(self, v:ICalGLib.Property_Class) """
        pass

    def set_cmd(self, v): # real signature unknown; restored from __doc__
        """ set_cmd(self, v:ICalGLib.PropertyCmd) """
        pass

    def set_color(self, v): # real signature unknown; restored from __doc__
        """ set_color(self, v:str) """
        pass

    def set_comment(self, v): # real signature unknown; restored from __doc__
        """ set_comment(self, v:str) """
        pass

    def set_completed(self, v): # real signature unknown; restored from __doc__
        """ set_completed(self, v:ICalGLib.Time) """
        pass

    def set_components(self, v): # real signature unknown; restored from __doc__
        """ set_components(self, v:str) """
        pass

    def set_contact(self, v): # real signature unknown; restored from __doc__
        """ set_contact(self, v:str) """
        pass

    def set_created(self, v): # real signature unknown; restored from __doc__
        """ set_created(self, v:ICalGLib.Time) """
        pass

    def set_csid(self, v): # real signature unknown; restored from __doc__
        """ set_csid(self, v:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_datemax(self, v): # real signature unknown; restored from __doc__
        """ set_datemax(self, v:ICalGLib.Time) """
        pass

    def set_datemin(self, v): # real signature unknown; restored from __doc__
        """ set_datemin(self, v:ICalGLib.Time) """
        pass

    def set_decreed(self, v): # real signature unknown; restored from __doc__
        """ set_decreed(self, v:str) """
        pass

    def set_defaultcharset(self, v): # real signature unknown; restored from __doc__
        """ set_defaultcharset(self, v:str) """
        pass

    def set_defaultlocale(self, v): # real signature unknown; restored from __doc__
        """ set_defaultlocale(self, v:str) """
        pass

    def set_defaulttzid(self, v): # real signature unknown; restored from __doc__
        """ set_defaulttzid(self, v:str) """
        pass

    def set_defaultvcars(self, v): # real signature unknown; restored from __doc__
        """ set_defaultvcars(self, v:str) """
        pass

    def set_deny(self, v): # real signature unknown; restored from __doc__
        """ set_deny(self, v:str) """
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

    def set_estimatedduration(self, v): # real signature unknown; restored from __doc__
        """ set_estimatedduration(self, v:ICalGLib.Duration) """
        pass

    def set_exdate(self, v): # real signature unknown; restored from __doc__
        """ set_exdate(self, v:ICalGLib.Time) """
        pass

    def set_expand(self, v): # real signature unknown; restored from __doc__
        """ set_expand(self, v:int) """
        pass

    def set_exrule(self, v): # real signature unknown; restored from __doc__
        """ set_exrule(self, v:ICalGLib.Recurrence) """
        pass

    def set_freebusy(self, v): # real signature unknown; restored from __doc__
        """ set_freebusy(self, v:ICalGLib.Period) """
        pass

    def set_geo(self, v): # real signature unknown; restored from __doc__
        """ set_geo(self, v:ICalGLib.Geo) """
        pass

    def set_grant(self, v): # real signature unknown; restored from __doc__
        """ set_grant(self, v:str) """
        pass

    def set_itipversion(self, v): # real signature unknown; restored from __doc__
        """ set_itipversion(self, v:str) """
        pass

    def set_lastmodified(self, v): # real signature unknown; restored from __doc__
        """ set_lastmodified(self, v:ICalGLib.Time) """
        pass

    def set_location(self, v): # real signature unknown; restored from __doc__
        """ set_location(self, v:str) """
        pass

    def set_maxcomponentsize(self, v): # real signature unknown; restored from __doc__
        """ set_maxcomponentsize(self, v:int) """
        pass

    def set_maxdate(self, v): # real signature unknown; restored from __doc__
        """ set_maxdate(self, v:ICalGLib.Time) """
        pass

    def set_maxresults(self, v): # real signature unknown; restored from __doc__
        """ set_maxresults(self, v:int) """
        pass

    def set_maxresultssize(self, v): # real signature unknown; restored from __doc__
        """ set_maxresultssize(self, v:int) """
        pass

    def set_method(self, v): # real signature unknown; restored from __doc__
        """ set_method(self, v:ICalGLib.PropertyMethod) """
        pass

    def set_mindate(self, v): # real signature unknown; restored from __doc__
        """ set_mindate(self, v:ICalGLib.Time) """
        pass

    def set_multipart(self, v): # real signature unknown; restored from __doc__
        """ set_multipart(self, v:str) """
        pass

    def set_name(self, v): # real signature unknown; restored from __doc__
        """ set_name(self, v:str) """
        pass

    def set_native_destroy_func(self, native_destroy_func): # real signature unknown; restored from __doc__
        """ set_native_destroy_func(self, native_destroy_func:GLib.DestroyNotify) """
        pass

    def set_organizer(self, v): # real signature unknown; restored from __doc__
        """ set_organizer(self, v:str) """
        pass

    def set_owner(self, v): # real signature unknown; restored from __doc__
        """ set_owner(self, v:str) """
        pass

    def set_parameter(self, parameter): # real signature unknown; restored from __doc__
        """ set_parameter(self, parameter:ICalGLib.Parameter) """
        pass

    def set_parameter_from_string(self, name, value): # real signature unknown; restored from __doc__
        """ set_parameter_from_string(self, name:str, value:str) """
        pass

    def set_parent(self, component=None): # real signature unknown; restored from __doc__
        """ set_parent(self, component:ICalGLib.Component=None) """
        pass

    def set_percentcomplete(self, v): # real signature unknown; restored from __doc__
        """ set_percentcomplete(self, v:int) """
        pass

    def set_permission(self, v): # real signature unknown; restored from __doc__
        """ set_permission(self, v:str) """
        pass

    def set_pollcompletion(self, v): # real signature unknown; restored from __doc__
        """ set_pollcompletion(self, v:ICalGLib.PropertyPollcompletion) """
        pass

    def set_pollitemid(self, v): # real signature unknown; restored from __doc__
        """ set_pollitemid(self, v:int) """
        pass

    def set_pollmode(self, v): # real signature unknown; restored from __doc__
        """ set_pollmode(self, v:ICalGLib.PropertyPollmode) """
        pass

    def set_pollproperties(self, v): # real signature unknown; restored from __doc__
        """ set_pollproperties(self, v:str) """
        pass

    def set_pollwinner(self, v): # real signature unknown; restored from __doc__
        """ set_pollwinner(self, v:int) """
        pass

    def set_priority(self, v): # real signature unknown; restored from __doc__
        """ set_priority(self, v:int) """
        pass

    def set_prodid(self, v): # real signature unknown; restored from __doc__
        """ set_prodid(self, v:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_query(self, v): # real signature unknown; restored from __doc__
        """ set_query(self, v:str) """
        pass

    def set_queryid(self, v): # real signature unknown; restored from __doc__
        """ set_queryid(self, v:str) """
        pass

    def set_querylevel(self, v): # real signature unknown; restored from __doc__
        """ set_querylevel(self, v:ICalGLib.PropertyQuerylevel) """
        pass

    def set_queryname(self, v): # real signature unknown; restored from __doc__
        """ set_queryname(self, v:str) """
        pass

    def set_rdate(self, v): # real signature unknown; restored from __doc__
        """ set_rdate(self, v:ICalGLib.Datetimeperiod) """
        pass

    def set_recuraccepted(self, v): # real signature unknown; restored from __doc__
        """ set_recuraccepted(self, v:str) """
        pass

    def set_recurexpand(self, v): # real signature unknown; restored from __doc__
        """ set_recurexpand(self, v:str) """
        pass

    def set_recurlimit(self, v): # real signature unknown; restored from __doc__
        """ set_recurlimit(self, v:str) """
        pass

    def set_recurrenceid(self, v): # real signature unknown; restored from __doc__
        """ set_recurrenceid(self, v:ICalGLib.Time) """
        pass

    def set_relatedto(self, v): # real signature unknown; restored from __doc__
        """ set_relatedto(self, v:str) """
        pass

    def set_relcalid(self, v): # real signature unknown; restored from __doc__
        """ set_relcalid(self, v:str) """
        pass

    def set_repeat(self, v): # real signature unknown; restored from __doc__
        """ set_repeat(self, v:int) """
        pass

    def set_replyurl(self, v): # real signature unknown; restored from __doc__
        """ set_replyurl(self, v:str) """
        pass

    def set_requeststatus(self, v): # real signature unknown; restored from __doc__
        """ set_requeststatus(self, v:ICalGLib.Reqstat) """
        pass

    def set_resources(self, v): # real signature unknown; restored from __doc__
        """ set_resources(self, v:str) """
        pass

    def set_response(self, v): # real signature unknown; restored from __doc__
        """ set_response(self, v:int) """
        pass

    def set_restriction(self, v): # real signature unknown; restored from __doc__
        """ set_restriction(self, v:str) """
        pass

    def set_rrule(self, v): # real signature unknown; restored from __doc__
        """ set_rrule(self, v:ICalGLib.Recurrence) """
        pass

    def set_scope(self, v): # real signature unknown; restored from __doc__
        """ set_scope(self, v:str) """
        pass

    def set_sequence(self, v): # real signature unknown; restored from __doc__
        """ set_sequence(self, v:int) """
        pass

    def set_status(self, v): # real signature unknown; restored from __doc__
        """ set_status(self, v:ICalGLib.PropertyStatus) """
        pass

    def set_storesexpanded(self, v): # real signature unknown; restored from __doc__
        """ set_storesexpanded(self, v:str) """
        pass

    def set_summary(self, v): # real signature unknown; restored from __doc__
        """ set_summary(self, v:str) """
        pass

    def set_target(self, v): # real signature unknown; restored from __doc__
        """ set_target(self, v:str) """
        pass

    def set_taskmode(self, v): # real signature unknown; restored from __doc__
        """ set_taskmode(self, v:ICalGLib.PropertyTaskmode) """
        pass

    def set_transp(self, v): # real signature unknown; restored from __doc__
        """ set_transp(self, v:ICalGLib.PropertyTransp) """
        pass

    def set_trigger(self, v): # real signature unknown; restored from __doc__
        """ set_trigger(self, v:ICalGLib.Trigger) """
        pass

    def set_tzid(self, v): # real signature unknown; restored from __doc__
        """ set_tzid(self, v:str) """
        pass

    def set_tzidaliasof(self, v): # real signature unknown; restored from __doc__
        """ set_tzidaliasof(self, v:str) """
        pass

    def set_tzname(self, v): # real signature unknown; restored from __doc__
        """ set_tzname(self, v:str) """
        pass

    def set_tzoffsetfrom(self, v): # real signature unknown; restored from __doc__
        """ set_tzoffsetfrom(self, v:int) """
        pass

    def set_tzoffsetto(self, v): # real signature unknown; restored from __doc__
        """ set_tzoffsetto(self, v:int) """
        pass

    def set_tzuntil(self, v): # real signature unknown; restored from __doc__
        """ set_tzuntil(self, v:ICalGLib.Time) """
        pass

    def set_tzurl(self, v): # real signature unknown; restored from __doc__
        """ set_tzurl(self, v:str) """
        pass

    def set_uid(self, v): # real signature unknown; restored from __doc__
        """ set_uid(self, v:str) """
        pass

    def set_url(self, v): # real signature unknown; restored from __doc__
        """ set_url(self, v:str) """
        pass

    def set_value(self, value): # real signature unknown; restored from __doc__
        """ set_value(self, value:ICalGLib.Value) """
        pass

    def set_value_from_string(self, value, kind): # real signature unknown; restored from __doc__
        """ set_value_from_string(self, value:str, kind:str) """
        pass

    def set_version(self, v): # real signature unknown; restored from __doc__
        """ set_version(self, v:str) """
        pass

    def set_voter(self, v): # real signature unknown; restored from __doc__
        """ set_voter(self, v:str) """
        pass

    def set_x(self, v): # real signature unknown; restored from __doc__
        """ set_x(self, v:str) """
        pass

    def set_xlicclass(self, v): # real signature unknown; restored from __doc__
        """ set_xlicclass(self, v:ICalGLib.PropertyXlicclass) """
        pass

    def set_xlicclustercount(self, v): # real signature unknown; restored from __doc__
        """ set_xlicclustercount(self, v:str) """
        pass

    def set_xlicerror(self, v): # real signature unknown; restored from __doc__
        """ set_xlicerror(self, v:str) """
        pass

    def set_xlicmimecharset(self, v): # real signature unknown; restored from __doc__
        """ set_xlicmimecharset(self, v:str) """
        pass

    def set_xlicmimecid(self, v): # real signature unknown; restored from __doc__
        """ set_xlicmimecid(self, v:str) """
        pass

    def set_xlicmimecontenttype(self, v): # real signature unknown; restored from __doc__
        """ set_xlicmimecontenttype(self, v:str) """
        pass

    def set_xlicmimeencoding(self, v): # real signature unknown; restored from __doc__
        """ set_xlicmimeencoding(self, v:str) """
        pass

    def set_xlicmimefilename(self, v): # real signature unknown; restored from __doc__
        """ set_xlicmimefilename(self, v:str) """
        pass

    def set_xlicmimeoptinfo(self, v): # real signature unknown; restored from __doc__
        """ set_xlicmimeoptinfo(self, v:str) """
        pass

    def set_x_name(self, name): # real signature unknown; restored from __doc__
        """ set_x_name(self, name:str) """
        pass

    def status_from_string(self, p_str): # real signature unknown; restored from __doc__
        """ status_from_string(str:str) -> ICalGLib.PropertyStatus """
        pass

    def status_to_string(self, method): # real signature unknown; restored from __doc__
        """ status_to_string(method:ICalGLib.PropertyStatus) -> str """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1352080bb0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Property), '__module__': 'gi.repository.ICalGLib', '__gtype__': <GType ICalProperty (94403188380912)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_acceptresponse': gi.FunctionInfo(new_acceptresponse), 'new_acknowledged': gi.FunctionInfo(new_acknowledged), 'new_action': gi.FunctionInfo(new_action), 'new_allowconflict': gi.FunctionInfo(new_allowconflict), 'new_attach': gi.FunctionInfo(new_attach), 'new_attendee': gi.FunctionInfo(new_attendee), 'new_busytype': gi.FunctionInfo(new_busytype), 'new_calid': gi.FunctionInfo(new_calid), 'new_calmaster': gi.FunctionInfo(new_calmaster), 'new_calscale': gi.FunctionInfo(new_calscale), 'new_capversion': gi.FunctionInfo(new_capversion), 'new_carid': gi.FunctionInfo(new_carid), 'new_carlevel': gi.FunctionInfo(new_carlevel), 'new_categories': gi.FunctionInfo(new_categories), 'new_class': gi.FunctionInfo(new_class), 'new_cmd': gi.FunctionInfo(new_cmd), 'new_color': gi.FunctionInfo(new_color), 'new_comment': gi.FunctionInfo(new_comment), 'new_completed': gi.FunctionInfo(new_completed), 'new_components': gi.FunctionInfo(new_components), 'new_contact': gi.FunctionInfo(new_contact), 'new_created': gi.FunctionInfo(new_created), 'new_csid': gi.FunctionInfo(new_csid), 'new_datemax': gi.FunctionInfo(new_datemax), 'new_datemin': gi.FunctionInfo(new_datemin), 'new_decreed': gi.FunctionInfo(new_decreed), 'new_defaultcharset': gi.FunctionInfo(new_defaultcharset), 'new_defaultlocale': gi.FunctionInfo(new_defaultlocale), 'new_defaulttzid': gi.FunctionInfo(new_defaulttzid), 'new_defaultvcars': gi.FunctionInfo(new_defaultvcars), 'new_deny': gi.FunctionInfo(new_deny), 'new_description': gi.FunctionInfo(new_description), 'new_dtend': gi.FunctionInfo(new_dtend), 'new_dtstamp': gi.FunctionInfo(new_dtstamp), 'new_dtstart': gi.FunctionInfo(new_dtstart), 'new_due': gi.FunctionInfo(new_due), 'new_duration': gi.FunctionInfo(new_duration), 'new_estimatedduration': gi.FunctionInfo(new_estimatedduration), 'new_exdate': gi.FunctionInfo(new_exdate), 'new_expand': gi.FunctionInfo(new_expand), 'new_exrule': gi.FunctionInfo(new_exrule), 'new_freebusy': gi.FunctionInfo(new_freebusy), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_geo': gi.FunctionInfo(new_geo), 'new_grant': gi.FunctionInfo(new_grant), 'new_itipversion': gi.FunctionInfo(new_itipversion), 'new_lastmodified': gi.FunctionInfo(new_lastmodified), 'new_location': gi.FunctionInfo(new_location), 'new_maxcomponentsize': gi.FunctionInfo(new_maxcomponentsize), 'new_maxdate': gi.FunctionInfo(new_maxdate), 'new_maxresults': gi.FunctionInfo(new_maxresults), 'new_maxresultssize': gi.FunctionInfo(new_maxresultssize), 'new_method': gi.FunctionInfo(new_method), 'new_mindate': gi.FunctionInfo(new_mindate), 'new_multipart': gi.FunctionInfo(new_multipart), 'new_name': gi.FunctionInfo(new_name), 'new_organizer': gi.FunctionInfo(new_organizer), 'new_owner': gi.FunctionInfo(new_owner), 'new_percentcomplete': gi.FunctionInfo(new_percentcomplete), 'new_permission': gi.FunctionInfo(new_permission), 'new_pollcompletion': gi.FunctionInfo(new_pollcompletion), 'new_pollitemid': gi.FunctionInfo(new_pollitemid), 'new_pollmode': gi.FunctionInfo(new_pollmode), 'new_pollproperties': gi.FunctionInfo(new_pollproperties), 'new_pollwinner': gi.FunctionInfo(new_pollwinner), 'new_priority': gi.FunctionInfo(new_priority), 'new_prodid': gi.FunctionInfo(new_prodid), 'new_query': gi.FunctionInfo(new_query), 'new_queryid': gi.FunctionInfo(new_queryid), 'new_querylevel': gi.FunctionInfo(new_querylevel), 'new_queryname': gi.FunctionInfo(new_queryname), 'new_rdate': gi.FunctionInfo(new_rdate), 'new_recuraccepted': gi.FunctionInfo(new_recuraccepted), 'new_recurexpand': gi.FunctionInfo(new_recurexpand), 'new_recurlimit': gi.FunctionInfo(new_recurlimit), 'new_recurrenceid': gi.FunctionInfo(new_recurrenceid), 'new_relatedto': gi.FunctionInfo(new_relatedto), 'new_relcalid': gi.FunctionInfo(new_relcalid), 'new_repeat': gi.FunctionInfo(new_repeat), 'new_replyurl': gi.FunctionInfo(new_replyurl), 'new_requeststatus': gi.FunctionInfo(new_requeststatus), 'new_resources': gi.FunctionInfo(new_resources), 'new_response': gi.FunctionInfo(new_response), 'new_restriction': gi.FunctionInfo(new_restriction), 'new_rrule': gi.FunctionInfo(new_rrule), 'new_scope': gi.FunctionInfo(new_scope), 'new_sequence': gi.FunctionInfo(new_sequence), 'new_status': gi.FunctionInfo(new_status), 'new_storesexpanded': gi.FunctionInfo(new_storesexpanded), 'new_summary': gi.FunctionInfo(new_summary), 'new_target': gi.FunctionInfo(new_target), 'new_taskmode': gi.FunctionInfo(new_taskmode), 'new_transp': gi.FunctionInfo(new_transp), 'new_trigger': gi.FunctionInfo(new_trigger), 'new_tzid': gi.FunctionInfo(new_tzid), 'new_tzidaliasof': gi.FunctionInfo(new_tzidaliasof), 'new_tzname': gi.FunctionInfo(new_tzname), 'new_tzoffsetfrom': gi.FunctionInfo(new_tzoffsetfrom), 'new_tzoffsetto': gi.FunctionInfo(new_tzoffsetto), 'new_tzuntil': gi.FunctionInfo(new_tzuntil), 'new_tzurl': gi.FunctionInfo(new_tzurl), 'new_uid': gi.FunctionInfo(new_uid), 'new_url': gi.FunctionInfo(new_url), 'new_version': gi.FunctionInfo(new_version), 'new_voter': gi.FunctionInfo(new_voter), 'new_x': gi.FunctionInfo(new_x), 'new_xlicclass': gi.FunctionInfo(new_xlicclass), 'new_xlicclustercount': gi.FunctionInfo(new_xlicclustercount), 'new_xlicerror': gi.FunctionInfo(new_xlicerror), 'new_xlicmimecharset': gi.FunctionInfo(new_xlicmimecharset), 'new_xlicmimecid': gi.FunctionInfo(new_xlicmimecid), 'new_xlicmimecontenttype': gi.FunctionInfo(new_xlicmimecontenttype), 'new_xlicmimeencoding': gi.FunctionInfo(new_xlicmimeencoding), 'new_xlicmimefilename': gi.FunctionInfo(new_xlicmimefilename), 'new_xlicmimeoptinfo': gi.FunctionInfo(new_xlicmimeoptinfo), 'enum_to_string': gi.FunctionInfo(enum_to_string), 'kind_and_string_to_enum': gi.FunctionInfo(kind_and_string_to_enum), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_has_property': gi.FunctionInfo(kind_has_property), 'kind_is_valid': gi.FunctionInfo(kind_is_valid), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'kind_to_value_kind': gi.FunctionInfo(kind_to_value_kind), 'method_from_string': gi.FunctionInfo(method_from_string), 'method_to_string': gi.FunctionInfo(method_to_string), 'recurrence_is_excluded': gi.FunctionInfo(recurrence_is_excluded), 'status_from_string': gi.FunctionInfo(status_from_string), 'status_to_string': gi.FunctionInfo(status_to_string), 'add_parameter': gi.FunctionInfo(add_parameter), 'as_ical_string': gi.FunctionInfo(as_ical_string), 'clone': gi.FunctionInfo(clone), 'count_parameters': gi.FunctionInfo(count_parameters), 'get_acceptresponse': gi.FunctionInfo(get_acceptresponse), 'get_acknowledged': gi.FunctionInfo(get_acknowledged), 'get_action': gi.FunctionInfo(get_action), 'get_allowconflict': gi.FunctionInfo(get_allowconflict), 'get_attach': gi.FunctionInfo(get_attach), 'get_attendee': gi.FunctionInfo(get_attendee), 'get_busytype': gi.FunctionInfo(get_busytype), 'get_calid': gi.FunctionInfo(get_calid), 'get_calmaster': gi.FunctionInfo(get_calmaster), 'get_calscale': gi.FunctionInfo(get_calscale), 'get_capversion': gi.FunctionInfo(get_capversion), 'get_carid': gi.FunctionInfo(get_carid), 'get_carlevel': gi.FunctionInfo(get_carlevel), 'get_categories': gi.FunctionInfo(get_categories), 'get_class': gi.FunctionInfo(get_class), 'get_cmd': gi.FunctionInfo(get_cmd), 'get_color': gi.FunctionInfo(get_color), 'get_comment': gi.FunctionInfo(get_comment), 'get_completed': gi.FunctionInfo(get_completed), 'get_components': gi.FunctionInfo(get_components), 'get_contact': gi.FunctionInfo(get_contact), 'get_created': gi.FunctionInfo(get_created), 'get_csid': gi.FunctionInfo(get_csid), 'get_datemax': gi.FunctionInfo(get_datemax), 'get_datemin': gi.FunctionInfo(get_datemin), 'get_datetime_with_component': gi.FunctionInfo(get_datetime_with_component), 'get_decreed': gi.FunctionInfo(get_decreed), 'get_defaultcharset': gi.FunctionInfo(get_defaultcharset), 'get_defaultlocale': gi.FunctionInfo(get_defaultlocale), 'get_defaulttzid': gi.FunctionInfo(get_defaulttzid), 'get_defaultvcars': gi.FunctionInfo(get_defaultvcars), 'get_deny': gi.FunctionInfo(get_deny), 'get_description': gi.FunctionInfo(get_description), 'get_dtend': gi.FunctionInfo(get_dtend), 'get_dtstamp': gi.FunctionInfo(get_dtstamp), 'get_dtstart': gi.FunctionInfo(get_dtstart), 'get_due': gi.FunctionInfo(get_due), 'get_duration': gi.FunctionInfo(get_duration), 'get_estimatedduration': gi.FunctionInfo(get_estimatedduration), 'get_exdate': gi.FunctionInfo(get_exdate), 'get_expand': gi.FunctionInfo(get_expand), 'get_exrule': gi.FunctionInfo(get_exrule), 'get_first_parameter': gi.FunctionInfo(get_first_parameter), 'get_freebusy': gi.FunctionInfo(get_freebusy), 'get_geo': gi.FunctionInfo(get_geo), 'get_grant': gi.FunctionInfo(get_grant), 'get_itipversion': gi.FunctionInfo(get_itipversion), 'get_lastmodified': gi.FunctionInfo(get_lastmodified), 'get_location': gi.FunctionInfo(get_location), 'get_maxcomponentsize': gi.FunctionInfo(get_maxcomponentsize), 'get_maxdate': gi.FunctionInfo(get_maxdate), 'get_maxresults': gi.FunctionInfo(get_maxresults), 'get_maxresultssize': gi.FunctionInfo(get_maxresultssize), 'get_method': gi.FunctionInfo(get_method), 'get_mindate': gi.FunctionInfo(get_mindate), 'get_multipart': gi.FunctionInfo(get_multipart), 'get_name': gi.FunctionInfo(get_name), 'get_next_parameter': gi.FunctionInfo(get_next_parameter), 'get_organizer': gi.FunctionInfo(get_organizer), 'get_owner': gi.FunctionInfo(get_owner), 'get_parameter_as_string': gi.FunctionInfo(get_parameter_as_string), 'get_parent': gi.FunctionInfo(get_parent), 'get_percentcomplete': gi.FunctionInfo(get_percentcomplete), 'get_permission': gi.FunctionInfo(get_permission), 'get_pollcompletion': gi.FunctionInfo(get_pollcompletion), 'get_pollitemid': gi.FunctionInfo(get_pollitemid), 'get_pollmode': gi.FunctionInfo(get_pollmode), 'get_pollproperties': gi.FunctionInfo(get_pollproperties), 'get_pollwinner': gi.FunctionInfo(get_pollwinner), 'get_priority': gi.FunctionInfo(get_priority), 'get_prodid': gi.FunctionInfo(get_prodid), 'get_property_name': gi.FunctionInfo(get_property_name), 'get_query': gi.FunctionInfo(get_query), 'get_queryid': gi.FunctionInfo(get_queryid), 'get_querylevel': gi.FunctionInfo(get_querylevel), 'get_queryname': gi.FunctionInfo(get_queryname), 'get_rdate': gi.FunctionInfo(get_rdate), 'get_recuraccepted': gi.FunctionInfo(get_recuraccepted), 'get_recurexpand': gi.FunctionInfo(get_recurexpand), 'get_recurlimit': gi.FunctionInfo(get_recurlimit), 'get_recurrenceid': gi.FunctionInfo(get_recurrenceid), 'get_relatedto': gi.FunctionInfo(get_relatedto), 'get_relcalid': gi.FunctionInfo(get_relcalid), 'get_repeat': gi.FunctionInfo(get_repeat), 'get_replyurl': gi.FunctionInfo(get_replyurl), 'get_requeststatus': gi.FunctionInfo(get_requeststatus), 'get_resources': gi.FunctionInfo(get_resources), 'get_response': gi.FunctionInfo(get_response), 'get_restriction': gi.FunctionInfo(get_restriction), 'get_rrule': gi.FunctionInfo(get_rrule), 'get_scope': gi.FunctionInfo(get_scope), 'get_sequence': gi.FunctionInfo(get_sequence), 'get_status': gi.FunctionInfo(get_status), 'get_storesexpanded': gi.FunctionInfo(get_storesexpanded), 'get_summary': gi.FunctionInfo(get_summary), 'get_target': gi.FunctionInfo(get_target), 'get_taskmode': gi.FunctionInfo(get_taskmode), 'get_transp': gi.FunctionInfo(get_transp), 'get_trigger': gi.FunctionInfo(get_trigger), 'get_tzid': gi.FunctionInfo(get_tzid), 'get_tzidaliasof': gi.FunctionInfo(get_tzidaliasof), 'get_tzname': gi.FunctionInfo(get_tzname), 'get_tzoffsetfrom': gi.FunctionInfo(get_tzoffsetfrom), 'get_tzoffsetto': gi.FunctionInfo(get_tzoffsetto), 'get_tzuntil': gi.FunctionInfo(get_tzuntil), 'get_tzurl': gi.FunctionInfo(get_tzurl), 'get_uid': gi.FunctionInfo(get_uid), 'get_url': gi.FunctionInfo(get_url), 'get_value': gi.FunctionInfo(get_value), 'get_value_as_string': gi.FunctionInfo(get_value_as_string), 'get_version': gi.FunctionInfo(get_version), 'get_voter': gi.FunctionInfo(get_voter), 'get_x': gi.FunctionInfo(get_x), 'get_x_name': gi.FunctionInfo(get_x_name), 'get_xlicclass': gi.FunctionInfo(get_xlicclass), 'get_xlicclustercount': gi.FunctionInfo(get_xlicclustercount), 'get_xlicerror': gi.FunctionInfo(get_xlicerror), 'get_xlicmimecharset': gi.FunctionInfo(get_xlicmimecharset), 'get_xlicmimecid': gi.FunctionInfo(get_xlicmimecid), 'get_xlicmimecontenttype': gi.FunctionInfo(get_xlicmimecontenttype), 'get_xlicmimeencoding': gi.FunctionInfo(get_xlicmimeencoding), 'get_xlicmimefilename': gi.FunctionInfo(get_xlicmimefilename), 'get_xlicmimeoptinfo': gi.FunctionInfo(get_xlicmimeoptinfo), 'isa': gi.FunctionInfo(isa), 'isa_property': gi.FunctionInfo(isa_property), 'remove_parameter_by_kind': gi.FunctionInfo(remove_parameter_by_kind), 'remove_parameter_by_name': gi.FunctionInfo(remove_parameter_by_name), 'remove_parameter_by_ref': gi.FunctionInfo(remove_parameter_by_ref), 'set_acceptresponse': gi.FunctionInfo(set_acceptresponse), 'set_acknowledged': gi.FunctionInfo(set_acknowledged), 'set_action': gi.FunctionInfo(set_action), 'set_allowconflict': gi.FunctionInfo(set_allowconflict), 'set_attach': gi.FunctionInfo(set_attach), 'set_attendee': gi.FunctionInfo(set_attendee), 'set_busytype': gi.FunctionInfo(set_busytype), 'set_calid': gi.FunctionInfo(set_calid), 'set_calmaster': gi.FunctionInfo(set_calmaster), 'set_calscale': gi.FunctionInfo(set_calscale), 'set_capversion': gi.FunctionInfo(set_capversion), 'set_carid': gi.FunctionInfo(set_carid), 'set_carlevel': gi.FunctionInfo(set_carlevel), 'set_categories': gi.FunctionInfo(set_categories), 'set_class': gi.FunctionInfo(set_class), 'set_cmd': gi.FunctionInfo(set_cmd), 'set_color': gi.FunctionInfo(set_color), 'set_comment': gi.FunctionInfo(set_comment), 'set_completed': gi.FunctionInfo(set_completed), 'set_components': gi.FunctionInfo(set_components), 'set_contact': gi.FunctionInfo(set_contact), 'set_created': gi.FunctionInfo(set_created), 'set_csid': gi.FunctionInfo(set_csid), 'set_datemax': gi.FunctionInfo(set_datemax), 'set_datemin': gi.FunctionInfo(set_datemin), 'set_decreed': gi.FunctionInfo(set_decreed), 'set_defaultcharset': gi.FunctionInfo(set_defaultcharset), 'set_defaultlocale': gi.FunctionInfo(set_defaultlocale), 'set_defaulttzid': gi.FunctionInfo(set_defaulttzid), 'set_defaultvcars': gi.FunctionInfo(set_defaultvcars), 'set_deny': gi.FunctionInfo(set_deny), 'set_description': gi.FunctionInfo(set_description), 'set_dtend': gi.FunctionInfo(set_dtend), 'set_dtstamp': gi.FunctionInfo(set_dtstamp), 'set_dtstart': gi.FunctionInfo(set_dtstart), 'set_due': gi.FunctionInfo(set_due), 'set_duration': gi.FunctionInfo(set_duration), 'set_estimatedduration': gi.FunctionInfo(set_estimatedduration), 'set_exdate': gi.FunctionInfo(set_exdate), 'set_expand': gi.FunctionInfo(set_expand), 'set_exrule': gi.FunctionInfo(set_exrule), 'set_freebusy': gi.FunctionInfo(set_freebusy), 'set_geo': gi.FunctionInfo(set_geo), 'set_grant': gi.FunctionInfo(set_grant), 'set_itipversion': gi.FunctionInfo(set_itipversion), 'set_lastmodified': gi.FunctionInfo(set_lastmodified), 'set_location': gi.FunctionInfo(set_location), 'set_maxcomponentsize': gi.FunctionInfo(set_maxcomponentsize), 'set_maxdate': gi.FunctionInfo(set_maxdate), 'set_maxresults': gi.FunctionInfo(set_maxresults), 'set_maxresultssize': gi.FunctionInfo(set_maxresultssize), 'set_method': gi.FunctionInfo(set_method), 'set_mindate': gi.FunctionInfo(set_mindate), 'set_multipart': gi.FunctionInfo(set_multipart), 'set_name': gi.FunctionInfo(set_name), 'set_organizer': gi.FunctionInfo(set_organizer), 'set_owner': gi.FunctionInfo(set_owner), 'set_parameter': gi.FunctionInfo(set_parameter), 'set_parameter_from_string': gi.FunctionInfo(set_parameter_from_string), 'set_parent': gi.FunctionInfo(set_parent), 'set_percentcomplete': gi.FunctionInfo(set_percentcomplete), 'set_permission': gi.FunctionInfo(set_permission), 'set_pollcompletion': gi.FunctionInfo(set_pollcompletion), 'set_pollitemid': gi.FunctionInfo(set_pollitemid), 'set_pollmode': gi.FunctionInfo(set_pollmode), 'set_pollproperties': gi.FunctionInfo(set_pollproperties), 'set_pollwinner': gi.FunctionInfo(set_pollwinner), 'set_priority': gi.FunctionInfo(set_priority), 'set_prodid': gi.FunctionInfo(set_prodid), 'set_query': gi.FunctionInfo(set_query), 'set_queryid': gi.FunctionInfo(set_queryid), 'set_querylevel': gi.FunctionInfo(set_querylevel), 'set_queryname': gi.FunctionInfo(set_queryname), 'set_rdate': gi.FunctionInfo(set_rdate), 'set_recuraccepted': gi.FunctionInfo(set_recuraccepted), 'set_recurexpand': gi.FunctionInfo(set_recurexpand), 'set_recurlimit': gi.FunctionInfo(set_recurlimit), 'set_recurrenceid': gi.FunctionInfo(set_recurrenceid), 'set_relatedto': gi.FunctionInfo(set_relatedto), 'set_relcalid': gi.FunctionInfo(set_relcalid), 'set_repeat': gi.FunctionInfo(set_repeat), 'set_replyurl': gi.FunctionInfo(set_replyurl), 'set_requeststatus': gi.FunctionInfo(set_requeststatus), 'set_resources': gi.FunctionInfo(set_resources), 'set_response': gi.FunctionInfo(set_response), 'set_restriction': gi.FunctionInfo(set_restriction), 'set_rrule': gi.FunctionInfo(set_rrule), 'set_scope': gi.FunctionInfo(set_scope), 'set_sequence': gi.FunctionInfo(set_sequence), 'set_status': gi.FunctionInfo(set_status), 'set_storesexpanded': gi.FunctionInfo(set_storesexpanded), 'set_summary': gi.FunctionInfo(set_summary), 'set_target': gi.FunctionInfo(set_target), 'set_taskmode': gi.FunctionInfo(set_taskmode), 'set_transp': gi.FunctionInfo(set_transp), 'set_trigger': gi.FunctionInfo(set_trigger), 'set_tzid': gi.FunctionInfo(set_tzid), 'set_tzidaliasof': gi.FunctionInfo(set_tzidaliasof), 'set_tzname': gi.FunctionInfo(set_tzname), 'set_tzoffsetfrom': gi.FunctionInfo(set_tzoffsetfrom), 'set_tzoffsetto': gi.FunctionInfo(set_tzoffsetto), 'set_tzuntil': gi.FunctionInfo(set_tzuntil), 'set_tzurl': gi.FunctionInfo(set_tzurl), 'set_uid': gi.FunctionInfo(set_uid), 'set_url': gi.FunctionInfo(set_url), 'set_value': gi.FunctionInfo(set_value), 'set_value_from_string': gi.FunctionInfo(set_value_from_string), 'set_version': gi.FunctionInfo(set_version), 'set_voter': gi.FunctionInfo(set_voter), 'set_x': gi.FunctionInfo(set_x), 'set_x_name': gi.FunctionInfo(set_x_name), 'set_xlicclass': gi.FunctionInfo(set_xlicclass), 'set_xlicclustercount': gi.FunctionInfo(set_xlicclustercount), 'set_xlicerror': gi.FunctionInfo(set_xlicerror), 'set_xlicmimecharset': gi.FunctionInfo(set_xlicmimecharset), 'set_xlicmimecid': gi.FunctionInfo(set_xlicmimecid), 'set_xlicmimecontenttype': gi.FunctionInfo(set_xlicmimecontenttype), 'set_xlicmimeencoding': gi.FunctionInfo(set_xlicmimeencoding), 'set_xlicmimefilename': gi.FunctionInfo(set_xlicmimefilename), 'set_xlicmimeoptinfo': gi.FunctionInfo(set_xlicmimeoptinfo)})"
    __gdoc__ = 'Object ICalProperty\n\nProperties from ICalObject:\n  native -> gpointer: Native\n    Native libical structure\n  native-destroy-func -> gpointer: Native-Destroy-Func\n    GDestroyNotify function to use to destroy the native libical structure\n  is-global-memory -> gboolean: Is-Global-Memory\n    Whether the native libical structure is from a global shared memory\n  owner -> GObject: Owner\n    The native libical structure owner\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ICalProperty (94403188380912)>'
    __info__ = ObjectInfo(Property)


