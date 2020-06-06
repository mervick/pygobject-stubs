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

class Parameter(Object):
    """
    :Constructors:
    
    ::
    
        Parameter(**properties)
        new(v:ICalGLib.ParameterKind) -> ICalGLib.Parameter
        new_actionparam(v:ICalGLib.ParameterAction) -> ICalGLib.Parameter
        new_altrep(v:str) -> ICalGLib.Parameter
        new_charset(v:str) -> ICalGLib.Parameter
        new_cn(v:str) -> ICalGLib.Parameter
        new_cutype(v:ICalGLib.ParameterCutype) -> ICalGLib.Parameter
        new_delegatedfrom(v:str) -> ICalGLib.Parameter
        new_delegatedto(v:str) -> ICalGLib.Parameter
        new_dir(v:str) -> ICalGLib.Parameter
        new_enable(v:ICalGLib.ParameterEnable) -> ICalGLib.Parameter
        new_encoding(v:ICalGLib.ParameterEncoding) -> ICalGLib.Parameter
        new_fbtype(v:ICalGLib.ParameterFbtype) -> ICalGLib.Parameter
        new_filename(v:str) -> ICalGLib.Parameter
        new_fmttype(v:str) -> ICalGLib.Parameter
        new_from_string(value:str) -> ICalGLib.Parameter
        new_from_value_string(kind:ICalGLib.ParameterKind, value:str) -> ICalGLib.Parameter
        new_iana(v:str) -> ICalGLib.Parameter
        new_id(v:str) -> ICalGLib.Parameter
        new_language(v:str) -> ICalGLib.Parameter
        new_latency(v:str) -> ICalGLib.Parameter
        new_local(v:ICalGLib.ParameterLocal) -> ICalGLib.Parameter
        new_localize(v:str) -> ICalGLib.Parameter
        new_managedid(v:str) -> ICalGLib.Parameter
        new_member(v:str) -> ICalGLib.Parameter
        new_modified(v:str) -> ICalGLib.Parameter
        new_options(v:str) -> ICalGLib.Parameter
        new_partstat(v:ICalGLib.ParameterPartstat) -> ICalGLib.Parameter
        new_publiccomment(v:str) -> ICalGLib.Parameter
        new_range(v:ICalGLib.ParameterRange) -> ICalGLib.Parameter
        new_reason(v:str) -> ICalGLib.Parameter
        new_related(v:ICalGLib.ParameterRelated) -> ICalGLib.Parameter
        new_reltype(v:ICalGLib.ParameterReltype) -> ICalGLib.Parameter
        new_required(v:ICalGLib.ParameterRequired) -> ICalGLib.Parameter
        new_response(v:int) -> ICalGLib.Parameter
        new_role(v:ICalGLib.ParameterRole) -> ICalGLib.Parameter
        new_rsvp(v:ICalGLib.ParameterRsvp) -> ICalGLib.Parameter
        new_scheduleagent(v:ICalGLib.ParameterScheduleagent) -> ICalGLib.Parameter
        new_scheduleforcesend(v:ICalGLib.ParameterScheduleforcesend) -> ICalGLib.Parameter
        new_schedulestatus(v:str) -> ICalGLib.Parameter
        new_sentby(v:str) -> ICalGLib.Parameter
        new_size(v:str) -> ICalGLib.Parameter
        new_stayinformed(v:ICalGLib.ParameterStayinformed) -> ICalGLib.Parameter
        new_substate(v:ICalGLib.ParameterSubstate) -> ICalGLib.Parameter
        new_tzid(v:str) -> ICalGLib.Parameter
        new_value(v:ICalGLib.ParameterValue) -> ICalGLib.Parameter
        new_x(v:str) -> ICalGLib.Parameter
        new_xliccomparetype(v:ICalGLib.ParameterXliccomparetype) -> ICalGLib.Parameter
        new_xlicerrortype(v:ICalGLib.ParameterXlicerrortype) -> ICalGLib.Parameter
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
        """ clone(self) -> ICalGLib.Parameter """
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

    def free_global_objects(self): # real signature unknown; restored from __doc__
        """ free_global_objects() """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_actionparam(self): # real signature unknown; restored from __doc__
        """ get_actionparam(self) -> ICalGLib.ParameterAction """
        pass

    def get_altrep(self): # real signature unknown; restored from __doc__
        """ get_altrep(self) -> str or None """
        return ""

    def get_charset(self): # real signature unknown; restored from __doc__
        """ get_charset(self) -> str or None """
        return ""

    def get_cn(self): # real signature unknown; restored from __doc__
        """ get_cn(self) -> str or None """
        return ""

    def get_cutype(self): # real signature unknown; restored from __doc__
        """ get_cutype(self) -> ICalGLib.ParameterCutype or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_delegatedfrom(self): # real signature unknown; restored from __doc__
        """ get_delegatedfrom(self) -> str or None """
        return ""

    def get_delegatedto(self): # real signature unknown; restored from __doc__
        """ get_delegatedto(self) -> str or None """
        return ""

    def get_dir(self): # real signature unknown; restored from __doc__
        """ get_dir(self) -> str or None """
        return ""

    def get_enable(self): # real signature unknown; restored from __doc__
        """ get_enable(self) -> ICalGLib.ParameterEnable """
        pass

    def get_encoding(self): # real signature unknown; restored from __doc__
        """ get_encoding(self) -> ICalGLib.ParameterEncoding """
        pass

    def get_fbtype(self): # real signature unknown; restored from __doc__
        """ get_fbtype(self) -> ICalGLib.ParameterFbtype """
        pass

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str or None """
        return ""

    def get_fmttype(self): # real signature unknown; restored from __doc__
        """ get_fmttype(self) -> str or None """
        return ""

    def get_iana(self): # real signature unknown; restored from __doc__
        """ get_iana(self) -> str or None """
        return ""

    def get_iana_name(self): # real signature unknown; restored from __doc__
        """ get_iana_name(self) -> str or None """
        return ""

    def get_iana_value(self): # real signature unknown; restored from __doc__
        """ get_iana_value(self) -> str or None """
        return ""

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str or None """
        return ""

    def get_is_global_memory(self): # real signature unknown; restored from __doc__
        """ get_is_global_memory(self) -> bool """
        return False

    def get_language(self): # real signature unknown; restored from __doc__
        """ get_language(self) -> str or None """
        return ""

    def get_latency(self): # real signature unknown; restored from __doc__
        """ get_latency(self) -> str or None """
        return ""

    def get_local(self): # real signature unknown; restored from __doc__
        """ get_local(self) -> ICalGLib.ParameterLocal """
        pass

    def get_localize(self): # real signature unknown; restored from __doc__
        """ get_localize(self) -> str or None """
        return ""

    def get_managedid(self): # real signature unknown; restored from __doc__
        """ get_managedid(self) -> str or None """
        return ""

    def get_member(self): # real signature unknown; restored from __doc__
        """ get_member(self) -> str or None """
        return ""

    def get_modified(self): # real signature unknown; restored from __doc__
        """ get_modified(self) -> str or None """
        return ""

    def get_options(self): # real signature unknown; restored from __doc__
        """ get_options(self) -> str or None """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> ICalGLib.Property or None """
        pass

    def get_partstat(self): # real signature unknown; restored from __doc__
        """ get_partstat(self) -> ICalGLib.ParameterPartstat """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_publiccomment(self): # real signature unknown; restored from __doc__
        """ get_publiccomment(self) -> str or None """
        return ""

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_range(self): # real signature unknown; restored from __doc__
        """ get_range(self) -> ICalGLib.ParameterRange """
        pass

    def get_reason(self): # real signature unknown; restored from __doc__
        """ get_reason(self) -> str or None """
        return ""

    def get_related(self): # real signature unknown; restored from __doc__
        """ get_related(self) -> ICalGLib.ParameterRelated """
        pass

    def get_reltype(self): # real signature unknown; restored from __doc__
        """ get_reltype(self) -> ICalGLib.ParameterReltype """
        pass

    def get_required(self): # real signature unknown; restored from __doc__
        """ get_required(self) -> ICalGLib.ParameterRequired """
        pass

    def get_response(self): # real signature unknown; restored from __doc__
        """ get_response(self) -> int """
        return 0

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> ICalGLib.ParameterRole """
        pass

    def get_rsvp(self): # real signature unknown; restored from __doc__
        """ get_rsvp(self) -> ICalGLib.ParameterRsvp """
        pass

    def get_scheduleagent(self): # real signature unknown; restored from __doc__
        """ get_scheduleagent(self) -> ICalGLib.ParameterScheduleagent """
        pass

    def get_scheduleforcesend(self): # real signature unknown; restored from __doc__
        """ get_scheduleforcesend(self) -> ICalGLib.ParameterScheduleforcesend """
        pass

    def get_schedulestatus(self): # real signature unknown; restored from __doc__
        """ get_schedulestatus(self) -> str or None """
        return ""

    def get_sentby(self): # real signature unknown; restored from __doc__
        """ get_sentby(self) -> str or None """
        return ""

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> str or None """
        return ""

    def get_stayinformed(self): # real signature unknown; restored from __doc__
        """ get_stayinformed(self) -> ICalGLib.ParameterStayinformed """
        pass

    def get_substate(self): # real signature unknown; restored from __doc__
        """ get_substate(self) -> ICalGLib.ParameterSubstate """
        pass

    def get_tzid(self): # real signature unknown; restored from __doc__
        """ get_tzid(self) -> str or None """
        return ""

    def get_value(self): # real signature unknown; restored from __doc__
        """ get_value(self) -> ICalGLib.ParameterValue """
        pass

    def get_x(self): # real signature unknown; restored from __doc__
        """ get_x(self) -> str or None """
        return ""

    def get_xliccomparetype(self): # real signature unknown; restored from __doc__
        """ get_xliccomparetype(self) -> ICalGLib.ParameterXliccomparetype """
        pass

    def get_xlicerrortype(self): # real signature unknown; restored from __doc__
        """ get_xlicerrortype(self) -> ICalGLib.ParameterXlicerrortype """
        pass

    def get_xname(self): # real signature unknown; restored from __doc__
        """ get_xname(self) -> str or None """
        return ""

    def get_xvalue(self): # real signature unknown; restored from __doc__
        """ get_xvalue(self) -> str or None """
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

    def has_same_name(self, param2): # real signature unknown; restored from __doc__
        """ has_same_name(self, param2:ICalGLib.Parameter) -> int """
        return 0

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
        """ isa(self) -> ICalGLib.ParameterKind """
        pass

    def isa_parameter(self): # real signature unknown; restored from __doc__
        """ isa_parameter(self) -> int """
        return 0

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def kind_from_string(self, string): # real signature unknown; restored from __doc__
        """ kind_from_string(string:str) -> ICalGLib.ParameterKind """
        pass

    def kind_is_valid(self, kind): # real signature unknown; restored from __doc__
        """ kind_is_valid(kind:ICalGLib.ParameterKind) -> bool """
        return False

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:ICalGLib.ParameterKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, v): # real signature unknown; restored from __doc__
        """ new(v:ICalGLib.ParameterKind) -> ICalGLib.Parameter """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_actionparam(self, v): # real signature unknown; restored from __doc__
        """ new_actionparam(v:ICalGLib.ParameterAction) -> ICalGLib.Parameter """
        pass

    def new_altrep(self, v): # real signature unknown; restored from __doc__
        """ new_altrep(v:str) -> ICalGLib.Parameter """
        pass

    def new_charset(self, v): # real signature unknown; restored from __doc__
        """ new_charset(v:str) -> ICalGLib.Parameter """
        pass

    def new_cn(self, v): # real signature unknown; restored from __doc__
        """ new_cn(v:str) -> ICalGLib.Parameter """
        pass

    def new_cutype(self, v): # real signature unknown; restored from __doc__
        """ new_cutype(v:ICalGLib.ParameterCutype) -> ICalGLib.Parameter """
        pass

    def new_delegatedfrom(self, v): # real signature unknown; restored from __doc__
        """ new_delegatedfrom(v:str) -> ICalGLib.Parameter """
        pass

    def new_delegatedto(self, v): # real signature unknown; restored from __doc__
        """ new_delegatedto(v:str) -> ICalGLib.Parameter """
        pass

    def new_dir(self, v): # real signature unknown; restored from __doc__
        """ new_dir(v:str) -> ICalGLib.Parameter """
        pass

    def new_enable(self, v): # real signature unknown; restored from __doc__
        """ new_enable(v:ICalGLib.ParameterEnable) -> ICalGLib.Parameter """
        pass

    def new_encoding(self, v): # real signature unknown; restored from __doc__
        """ new_encoding(v:ICalGLib.ParameterEncoding) -> ICalGLib.Parameter """
        pass

    def new_fbtype(self, v): # real signature unknown; restored from __doc__
        """ new_fbtype(v:ICalGLib.ParameterFbtype) -> ICalGLib.Parameter """
        pass

    def new_filename(self, v): # real signature unknown; restored from __doc__
        """ new_filename(v:str) -> ICalGLib.Parameter """
        pass

    def new_fmttype(self, v): # real signature unknown; restored from __doc__
        """ new_fmttype(v:str) -> ICalGLib.Parameter """
        pass

    def new_from_string(self, value): # real signature unknown; restored from __doc__
        """ new_from_string(value:str) -> ICalGLib.Parameter """
        pass

    def new_from_value_string(self, kind, value): # real signature unknown; restored from __doc__
        """ new_from_value_string(kind:ICalGLib.ParameterKind, value:str) -> ICalGLib.Parameter """
        pass

    def new_iana(self, v): # real signature unknown; restored from __doc__
        """ new_iana(v:str) -> ICalGLib.Parameter """
        pass

    def new_id(self, v): # real signature unknown; restored from __doc__
        """ new_id(v:str) -> ICalGLib.Parameter """
        pass

    def new_language(self, v): # real signature unknown; restored from __doc__
        """ new_language(v:str) -> ICalGLib.Parameter """
        pass

    def new_latency(self, v): # real signature unknown; restored from __doc__
        """ new_latency(v:str) -> ICalGLib.Parameter """
        pass

    def new_local(self, v): # real signature unknown; restored from __doc__
        """ new_local(v:ICalGLib.ParameterLocal) -> ICalGLib.Parameter """
        pass

    def new_localize(self, v): # real signature unknown; restored from __doc__
        """ new_localize(v:str) -> ICalGLib.Parameter """
        pass

    def new_managedid(self, v): # real signature unknown; restored from __doc__
        """ new_managedid(v:str) -> ICalGLib.Parameter """
        pass

    def new_member(self, v): # real signature unknown; restored from __doc__
        """ new_member(v:str) -> ICalGLib.Parameter """
        pass

    def new_modified(self, v): # real signature unknown; restored from __doc__
        """ new_modified(v:str) -> ICalGLib.Parameter """
        pass

    def new_options(self, v): # real signature unknown; restored from __doc__
        """ new_options(v:str) -> ICalGLib.Parameter """
        pass

    def new_partstat(self, v): # real signature unknown; restored from __doc__
        """ new_partstat(v:ICalGLib.ParameterPartstat) -> ICalGLib.Parameter """
        pass

    def new_publiccomment(self, v): # real signature unknown; restored from __doc__
        """ new_publiccomment(v:str) -> ICalGLib.Parameter """
        pass

    def new_range(self, v): # real signature unknown; restored from __doc__
        """ new_range(v:ICalGLib.ParameterRange) -> ICalGLib.Parameter """
        pass

    def new_reason(self, v): # real signature unknown; restored from __doc__
        """ new_reason(v:str) -> ICalGLib.Parameter """
        pass

    def new_related(self, v): # real signature unknown; restored from __doc__
        """ new_related(v:ICalGLib.ParameterRelated) -> ICalGLib.Parameter """
        pass

    def new_reltype(self, v): # real signature unknown; restored from __doc__
        """ new_reltype(v:ICalGLib.ParameterReltype) -> ICalGLib.Parameter """
        pass

    def new_required(self, v): # real signature unknown; restored from __doc__
        """ new_required(v:ICalGLib.ParameterRequired) -> ICalGLib.Parameter """
        pass

    def new_response(self, v): # real signature unknown; restored from __doc__
        """ new_response(v:int) -> ICalGLib.Parameter """
        pass

    def new_role(self, v): # real signature unknown; restored from __doc__
        """ new_role(v:ICalGLib.ParameterRole) -> ICalGLib.Parameter """
        pass

    def new_rsvp(self, v): # real signature unknown; restored from __doc__
        """ new_rsvp(v:ICalGLib.ParameterRsvp) -> ICalGLib.Parameter """
        pass

    def new_scheduleagent(self, v): # real signature unknown; restored from __doc__
        """ new_scheduleagent(v:ICalGLib.ParameterScheduleagent) -> ICalGLib.Parameter """
        pass

    def new_scheduleforcesend(self, v): # real signature unknown; restored from __doc__
        """ new_scheduleforcesend(v:ICalGLib.ParameterScheduleforcesend) -> ICalGLib.Parameter """
        pass

    def new_schedulestatus(self, v): # real signature unknown; restored from __doc__
        """ new_schedulestatus(v:str) -> ICalGLib.Parameter """
        pass

    def new_sentby(self, v): # real signature unknown; restored from __doc__
        """ new_sentby(v:str) -> ICalGLib.Parameter """
        pass

    def new_size(self, v): # real signature unknown; restored from __doc__
        """ new_size(v:str) -> ICalGLib.Parameter """
        pass

    def new_stayinformed(self, v): # real signature unknown; restored from __doc__
        """ new_stayinformed(v:ICalGLib.ParameterStayinformed) -> ICalGLib.Parameter """
        pass

    def new_substate(self, v): # real signature unknown; restored from __doc__
        """ new_substate(v:ICalGLib.ParameterSubstate) -> ICalGLib.Parameter """
        pass

    def new_tzid(self, v): # real signature unknown; restored from __doc__
        """ new_tzid(v:str) -> ICalGLib.Parameter """
        pass

    def new_value(self, v): # real signature unknown; restored from __doc__
        """ new_value(v:ICalGLib.ParameterValue) -> ICalGLib.Parameter """
        pass

    def new_x(self, v): # real signature unknown; restored from __doc__
        """ new_x(v:str) -> ICalGLib.Parameter """
        pass

    def new_xliccomparetype(self, v): # real signature unknown; restored from __doc__
        """ new_xliccomparetype(v:ICalGLib.ParameterXliccomparetype) -> ICalGLib.Parameter """
        pass

    def new_xlicerrortype(self, v): # real signature unknown; restored from __doc__
        """ new_xlicerrortype(v:ICalGLib.ParameterXlicerrortype) -> ICalGLib.Parameter """
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

    def set_actionparam(self, v): # real signature unknown; restored from __doc__
        """ set_actionparam(self, v:ICalGLib.ParameterAction) """
        pass

    def set_altrep(self, v): # real signature unknown; restored from __doc__
        """ set_altrep(self, v:str) """
        pass

    def set_charset(self, v): # real signature unknown; restored from __doc__
        """ set_charset(self, v:str) """
        pass

    def set_cn(self, v): # real signature unknown; restored from __doc__
        """ set_cn(self, v:str) """
        pass

    def set_cutype(self, v): # real signature unknown; restored from __doc__
        """ set_cutype(self, v:ICalGLib.ParameterCutype) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_delegatedfrom(self, v): # real signature unknown; restored from __doc__
        """ set_delegatedfrom(self, v:str) """
        pass

    def set_delegatedto(self, v): # real signature unknown; restored from __doc__
        """ set_delegatedto(self, v:str) """
        pass

    def set_dir(self, v): # real signature unknown; restored from __doc__
        """ set_dir(self, v:str) """
        pass

    def set_enable(self, v): # real signature unknown; restored from __doc__
        """ set_enable(self, v:ICalGLib.ParameterEnable) """
        pass

    def set_encoding(self, v): # real signature unknown; restored from __doc__
        """ set_encoding(self, v:ICalGLib.ParameterEncoding) """
        pass

    def set_fbtype(self, v): # real signature unknown; restored from __doc__
        """ set_fbtype(self, v:ICalGLib.ParameterFbtype) """
        pass

    def set_filename(self, v): # real signature unknown; restored from __doc__
        """ set_filename(self, v:str) """
        pass

    def set_fmttype(self, v): # real signature unknown; restored from __doc__
        """ set_fmttype(self, v:str) """
        pass

    def set_iana(self, v): # real signature unknown; restored from __doc__
        """ set_iana(self, v:str) """
        pass

    def set_iana_name(self, v): # real signature unknown; restored from __doc__
        """ set_iana_name(self, v:str) """
        pass

    def set_iana_value(self, v): # real signature unknown; restored from __doc__
        """ set_iana_value(self, v:str) """
        pass

    def set_id(self, v): # real signature unknown; restored from __doc__
        """ set_id(self, v:str) """
        pass

    def set_language(self, v): # real signature unknown; restored from __doc__
        """ set_language(self, v:str) """
        pass

    def set_latency(self, v): # real signature unknown; restored from __doc__
        """ set_latency(self, v:str) """
        pass

    def set_local(self, v): # real signature unknown; restored from __doc__
        """ set_local(self, v:ICalGLib.ParameterLocal) """
        pass

    def set_localize(self, v): # real signature unknown; restored from __doc__
        """ set_localize(self, v:str) """
        pass

    def set_managedid(self, v): # real signature unknown; restored from __doc__
        """ set_managedid(self, v:str) """
        pass

    def set_member(self, v): # real signature unknown; restored from __doc__
        """ set_member(self, v:str) """
        pass

    def set_modified(self, v): # real signature unknown; restored from __doc__
        """ set_modified(self, v:str) """
        pass

    def set_native_destroy_func(self, native_destroy_func): # real signature unknown; restored from __doc__
        """ set_native_destroy_func(self, native_destroy_func:GLib.DestroyNotify) """
        pass

    def set_options(self, v): # real signature unknown; restored from __doc__
        """ set_options(self, v:str) """
        pass

    def set_owner(self, owner): # real signature unknown; restored from __doc__
        """ set_owner(self, owner:GObject.Object) """
        pass

    def set_parent(self, property=None): # real signature unknown; restored from __doc__
        """ set_parent(self, property:ICalGLib.Property=None) """
        pass

    def set_partstat(self, v): # real signature unknown; restored from __doc__
        """ set_partstat(self, v:ICalGLib.ParameterPartstat) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_publiccomment(self, v): # real signature unknown; restored from __doc__
        """ set_publiccomment(self, v:str) """
        pass

    def set_range(self, v): # real signature unknown; restored from __doc__
        """ set_range(self, v:ICalGLib.ParameterRange) """
        pass

    def set_reason(self, v): # real signature unknown; restored from __doc__
        """ set_reason(self, v:str) """
        pass

    def set_related(self, v): # real signature unknown; restored from __doc__
        """ set_related(self, v:ICalGLib.ParameterRelated) """
        pass

    def set_reltype(self, v): # real signature unknown; restored from __doc__
        """ set_reltype(self, v:ICalGLib.ParameterReltype) """
        pass

    def set_required(self, v): # real signature unknown; restored from __doc__
        """ set_required(self, v:ICalGLib.ParameterRequired) """
        pass

    def set_response(self, v): # real signature unknown; restored from __doc__
        """ set_response(self, v:int) """
        pass

    def set_role(self, v): # real signature unknown; restored from __doc__
        """ set_role(self, v:ICalGLib.ParameterRole) """
        pass

    def set_rsvp(self, v): # real signature unknown; restored from __doc__
        """ set_rsvp(self, v:ICalGLib.ParameterRsvp) """
        pass

    def set_scheduleagent(self, v): # real signature unknown; restored from __doc__
        """ set_scheduleagent(self, v:ICalGLib.ParameterScheduleagent) """
        pass

    def set_scheduleforcesend(self, v): # real signature unknown; restored from __doc__
        """ set_scheduleforcesend(self, v:ICalGLib.ParameterScheduleforcesend) """
        pass

    def set_schedulestatus(self, v): # real signature unknown; restored from __doc__
        """ set_schedulestatus(self, v:str) """
        pass

    def set_sentby(self, v): # real signature unknown; restored from __doc__
        """ set_sentby(self, v:str) """
        pass

    def set_size(self, v): # real signature unknown; restored from __doc__
        """ set_size(self, v:str) """
        pass

    def set_stayinformed(self, v): # real signature unknown; restored from __doc__
        """ set_stayinformed(self, v:ICalGLib.ParameterStayinformed) """
        pass

    def set_substate(self, v): # real signature unknown; restored from __doc__
        """ set_substate(self, v:ICalGLib.ParameterSubstate) """
        pass

    def set_tzid(self, v): # real signature unknown; restored from __doc__
        """ set_tzid(self, v:str) """
        pass

    def set_value(self, v): # real signature unknown; restored from __doc__
        """ set_value(self, v:ICalGLib.ParameterValue) """
        pass

    def set_x(self, v): # real signature unknown; restored from __doc__
        """ set_x(self, v:str) """
        pass

    def set_xliccomparetype(self, v): # real signature unknown; restored from __doc__
        """ set_xliccomparetype(self, v:ICalGLib.ParameterXliccomparetype) """
        pass

    def set_xlicerrortype(self, v): # real signature unknown; restored from __doc__
        """ set_xlicerrortype(self, v:ICalGLib.ParameterXlicerrortype) """
        pass

    def set_xname(self, v): # real signature unknown; restored from __doc__
        """ set_xname(self, v:str) """
        pass

    def set_xvalue(self, v): # real signature unknown; restored from __doc__
        """ set_xvalue(self, v:str) """
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

    def value_to_value_kind(self, value): # real signature unknown; restored from __doc__
        """ value_to_value_kind(value:ICalGLib.ParameterValue) -> ICalGLib.ValueKind """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f1352080700>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Parameter), '__module__': 'gi.repository.ICalGLib', '__gtype__': <GType ICalParameter (94403187916288)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_actionparam': gi.FunctionInfo(new_actionparam), 'new_altrep': gi.FunctionInfo(new_altrep), 'new_charset': gi.FunctionInfo(new_charset), 'new_cn': gi.FunctionInfo(new_cn), 'new_cutype': gi.FunctionInfo(new_cutype), 'new_delegatedfrom': gi.FunctionInfo(new_delegatedfrom), 'new_delegatedto': gi.FunctionInfo(new_delegatedto), 'new_dir': gi.FunctionInfo(new_dir), 'new_enable': gi.FunctionInfo(new_enable), 'new_encoding': gi.FunctionInfo(new_encoding), 'new_fbtype': gi.FunctionInfo(new_fbtype), 'new_filename': gi.FunctionInfo(new_filename), 'new_fmttype': gi.FunctionInfo(new_fmttype), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_from_value_string': gi.FunctionInfo(new_from_value_string), 'new_iana': gi.FunctionInfo(new_iana), 'new_id': gi.FunctionInfo(new_id), 'new_language': gi.FunctionInfo(new_language), 'new_latency': gi.FunctionInfo(new_latency), 'new_local': gi.FunctionInfo(new_local), 'new_localize': gi.FunctionInfo(new_localize), 'new_managedid': gi.FunctionInfo(new_managedid), 'new_member': gi.FunctionInfo(new_member), 'new_modified': gi.FunctionInfo(new_modified), 'new_options': gi.FunctionInfo(new_options), 'new_partstat': gi.FunctionInfo(new_partstat), 'new_publiccomment': gi.FunctionInfo(new_publiccomment), 'new_range': gi.FunctionInfo(new_range), 'new_reason': gi.FunctionInfo(new_reason), 'new_related': gi.FunctionInfo(new_related), 'new_reltype': gi.FunctionInfo(new_reltype), 'new_required': gi.FunctionInfo(new_required), 'new_response': gi.FunctionInfo(new_response), 'new_role': gi.FunctionInfo(new_role), 'new_rsvp': gi.FunctionInfo(new_rsvp), 'new_scheduleagent': gi.FunctionInfo(new_scheduleagent), 'new_scheduleforcesend': gi.FunctionInfo(new_scheduleforcesend), 'new_schedulestatus': gi.FunctionInfo(new_schedulestatus), 'new_sentby': gi.FunctionInfo(new_sentby), 'new_size': gi.FunctionInfo(new_size), 'new_stayinformed': gi.FunctionInfo(new_stayinformed), 'new_substate': gi.FunctionInfo(new_substate), 'new_tzid': gi.FunctionInfo(new_tzid), 'new_value': gi.FunctionInfo(new_value), 'new_x': gi.FunctionInfo(new_x), 'new_xliccomparetype': gi.FunctionInfo(new_xliccomparetype), 'new_xlicerrortype': gi.FunctionInfo(new_xlicerrortype), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_is_valid': gi.FunctionInfo(kind_is_valid), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'value_to_value_kind': gi.FunctionInfo(value_to_value_kind), 'as_ical_string': gi.FunctionInfo(as_ical_string), 'clone': gi.FunctionInfo(clone), 'get_actionparam': gi.FunctionInfo(get_actionparam), 'get_altrep': gi.FunctionInfo(get_altrep), 'get_charset': gi.FunctionInfo(get_charset), 'get_cn': gi.FunctionInfo(get_cn), 'get_cutype': gi.FunctionInfo(get_cutype), 'get_delegatedfrom': gi.FunctionInfo(get_delegatedfrom), 'get_delegatedto': gi.FunctionInfo(get_delegatedto), 'get_dir': gi.FunctionInfo(get_dir), 'get_enable': gi.FunctionInfo(get_enable), 'get_encoding': gi.FunctionInfo(get_encoding), 'get_fbtype': gi.FunctionInfo(get_fbtype), 'get_filename': gi.FunctionInfo(get_filename), 'get_fmttype': gi.FunctionInfo(get_fmttype), 'get_iana': gi.FunctionInfo(get_iana), 'get_iana_name': gi.FunctionInfo(get_iana_name), 'get_iana_value': gi.FunctionInfo(get_iana_value), 'get_id': gi.FunctionInfo(get_id), 'get_language': gi.FunctionInfo(get_language), 'get_latency': gi.FunctionInfo(get_latency), 'get_local': gi.FunctionInfo(get_local), 'get_localize': gi.FunctionInfo(get_localize), 'get_managedid': gi.FunctionInfo(get_managedid), 'get_member': gi.FunctionInfo(get_member), 'get_modified': gi.FunctionInfo(get_modified), 'get_options': gi.FunctionInfo(get_options), 'get_parent': gi.FunctionInfo(get_parent), 'get_partstat': gi.FunctionInfo(get_partstat), 'get_publiccomment': gi.FunctionInfo(get_publiccomment), 'get_range': gi.FunctionInfo(get_range), 'get_reason': gi.FunctionInfo(get_reason), 'get_related': gi.FunctionInfo(get_related), 'get_reltype': gi.FunctionInfo(get_reltype), 'get_required': gi.FunctionInfo(get_required), 'get_response': gi.FunctionInfo(get_response), 'get_role': gi.FunctionInfo(get_role), 'get_rsvp': gi.FunctionInfo(get_rsvp), 'get_scheduleagent': gi.FunctionInfo(get_scheduleagent), 'get_scheduleforcesend': gi.FunctionInfo(get_scheduleforcesend), 'get_schedulestatus': gi.FunctionInfo(get_schedulestatus), 'get_sentby': gi.FunctionInfo(get_sentby), 'get_size': gi.FunctionInfo(get_size), 'get_stayinformed': gi.FunctionInfo(get_stayinformed), 'get_substate': gi.FunctionInfo(get_substate), 'get_tzid': gi.FunctionInfo(get_tzid), 'get_value': gi.FunctionInfo(get_value), 'get_x': gi.FunctionInfo(get_x), 'get_xliccomparetype': gi.FunctionInfo(get_xliccomparetype), 'get_xlicerrortype': gi.FunctionInfo(get_xlicerrortype), 'get_xname': gi.FunctionInfo(get_xname), 'get_xvalue': gi.FunctionInfo(get_xvalue), 'has_same_name': gi.FunctionInfo(has_same_name), 'isa': gi.FunctionInfo(isa), 'isa_parameter': gi.FunctionInfo(isa_parameter), 'set_actionparam': gi.FunctionInfo(set_actionparam), 'set_altrep': gi.FunctionInfo(set_altrep), 'set_charset': gi.FunctionInfo(set_charset), 'set_cn': gi.FunctionInfo(set_cn), 'set_cutype': gi.FunctionInfo(set_cutype), 'set_delegatedfrom': gi.FunctionInfo(set_delegatedfrom), 'set_delegatedto': gi.FunctionInfo(set_delegatedto), 'set_dir': gi.FunctionInfo(set_dir), 'set_enable': gi.FunctionInfo(set_enable), 'set_encoding': gi.FunctionInfo(set_encoding), 'set_fbtype': gi.FunctionInfo(set_fbtype), 'set_filename': gi.FunctionInfo(set_filename), 'set_fmttype': gi.FunctionInfo(set_fmttype), 'set_iana': gi.FunctionInfo(set_iana), 'set_iana_name': gi.FunctionInfo(set_iana_name), 'set_iana_value': gi.FunctionInfo(set_iana_value), 'set_id': gi.FunctionInfo(set_id), 'set_language': gi.FunctionInfo(set_language), 'set_latency': gi.FunctionInfo(set_latency), 'set_local': gi.FunctionInfo(set_local), 'set_localize': gi.FunctionInfo(set_localize), 'set_managedid': gi.FunctionInfo(set_managedid), 'set_member': gi.FunctionInfo(set_member), 'set_modified': gi.FunctionInfo(set_modified), 'set_options': gi.FunctionInfo(set_options), 'set_parent': gi.FunctionInfo(set_parent), 'set_partstat': gi.FunctionInfo(set_partstat), 'set_publiccomment': gi.FunctionInfo(set_publiccomment), 'set_range': gi.FunctionInfo(set_range), 'set_reason': gi.FunctionInfo(set_reason), 'set_related': gi.FunctionInfo(set_related), 'set_reltype': gi.FunctionInfo(set_reltype), 'set_required': gi.FunctionInfo(set_required), 'set_response': gi.FunctionInfo(set_response), 'set_role': gi.FunctionInfo(set_role), 'set_rsvp': gi.FunctionInfo(set_rsvp), 'set_scheduleagent': gi.FunctionInfo(set_scheduleagent), 'set_scheduleforcesend': gi.FunctionInfo(set_scheduleforcesend), 'set_schedulestatus': gi.FunctionInfo(set_schedulestatus), 'set_sentby': gi.FunctionInfo(set_sentby), 'set_size': gi.FunctionInfo(set_size), 'set_stayinformed': gi.FunctionInfo(set_stayinformed), 'set_substate': gi.FunctionInfo(set_substate), 'set_tzid': gi.FunctionInfo(set_tzid), 'set_value': gi.FunctionInfo(set_value), 'set_x': gi.FunctionInfo(set_x), 'set_xliccomparetype': gi.FunctionInfo(set_xliccomparetype), 'set_xlicerrortype': gi.FunctionInfo(set_xlicerrortype), 'set_xname': gi.FunctionInfo(set_xname), 'set_xvalue': gi.FunctionInfo(set_xvalue)})"
    __gdoc__ = 'Object ICalParameter\n\nProperties from ICalObject:\n  native -> gpointer: Native\n    Native libical structure\n  native-destroy-func -> gpointer: Native-Destroy-Func\n    GDestroyNotify function to use to destroy the native libical structure\n  is-global-memory -> gboolean: Is-Global-Memory\n    Whether the native libical structure is from a global shared memory\n  owner -> GObject: Owner\n    The native libical structure owner\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ICalParameter (94403187916288)>'
    __info__ = ObjectInfo(Parameter)


