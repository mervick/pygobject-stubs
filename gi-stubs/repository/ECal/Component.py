# encoding: utf-8
# module gi.repository.ECal
# from /usr/lib64/girepository-1.0/ECal-2.0.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class Component(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Component(**properties)
        new() -> ECal.Component
        new_from_icalcomponent(icalcomp:ICalGLib.Component) -> ECal.Component
        new_from_string(calobj:str) -> ECal.Component
        new_vtype(vtype:ECal.ComponentVType) -> ECal.Component
    """
    def abort_sequence(self): # real signature unknown; restored from __doc__
        """ abort_sequence(self) """
        pass

    def add_alarm(self, alarm): # real signature unknown; restored from __doc__
        """ add_alarm(self, alarm:ECal.ComponentAlarm) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> ECal.Component """
        pass

    def commit_sequence(self): # real signature unknown; restored from __doc__
        """ commit_sequence(self) """
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_alarm(self, auid): # real signature unknown; restored from __doc__
        """ get_alarm(self, auid:str) -> ECal.ComponentAlarm or None """
        pass

    def get_alarm_uids(self): # real signature unknown; restored from __doc__
        """ get_alarm_uids(self) -> list or None """
        return []

    def get_all_alarms(self): # real signature unknown; restored from __doc__
        """ get_all_alarms(self) -> list or None """
        return []

    def get_as_string(self): # real signature unknown; restored from __doc__
        """ get_as_string(self) -> str """
        return ""

    def get_attachments(self): # real signature unknown; restored from __doc__
        """ get_attachments(self) -> list or None """
        return []

    def get_attendees(self): # real signature unknown; restored from __doc__
        """ get_attendees(self) -> list or None """
        return []

    def get_categories(self): # real signature unknown; restored from __doc__
        """ get_categories(self) -> str or None """
        return ""

    def get_categories_list(self): # real signature unknown; restored from __doc__
        """ get_categories_list(self) -> list or None """
        return []

    def get_classification(self): # real signature unknown; restored from __doc__
        """ get_classification(self) -> ECal.ComponentClassification """
        pass

    def get_comments(self): # real signature unknown; restored from __doc__
        """ get_comments(self) -> list or None """
        return []

    def get_completed(self): # real signature unknown; restored from __doc__
        """ get_completed(self) -> ICalGLib.Time """
        pass

    def get_contacts(self): # real signature unknown; restored from __doc__
        """ get_contacts(self) -> list """
        return []

    def get_created(self): # real signature unknown; restored from __doc__
        """ get_created(self) -> ICalGLib.Time """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_descriptions(self): # real signature unknown; restored from __doc__
        """ get_descriptions(self) -> list or None """
        return []

    def get_dtend(self): # real signature unknown; restored from __doc__
        """ get_dtend(self) -> ECal.ComponentDateTime or None """
        pass

    def get_dtstamp(self): # real signature unknown; restored from __doc__
        """ get_dtstamp(self) -> ICalGLib.Time or None """
        pass

    def get_dtstart(self): # real signature unknown; restored from __doc__
        """ get_dtstart(self) -> ECal.ComponentDateTime or None """
        pass

    def get_due(self): # real signature unknown; restored from __doc__
        """ get_due(self) -> ECal.ComponentDateTime or None """
        pass

    def get_exdates(self): # real signature unknown; restored from __doc__
        """ get_exdates(self) -> list or None """
        return []

    def get_exrules(self): # real signature unknown; restored from __doc__
        """ get_exrules(self) -> list or None """
        return []

    def get_exrule_properties(self): # real signature unknown; restored from __doc__
        """ get_exrule_properties(self) -> list or None """
        return []

    def get_geo(self): # real signature unknown; restored from __doc__
        """ get_geo(self) -> ICalGLib.Geo or None """
        pass

    def get_icalcomponent(self): # real signature unknown; restored from __doc__
        """ get_icalcomponent(self) -> ICalGLib.Component or None """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> ECal.ComponentId """
        pass

    def get_last_modified(self): # real signature unknown; restored from __doc__
        """ get_last_modified(self) -> ICalGLib.Time """
        pass

    def get_location(self): # real signature unknown; restored from __doc__
        """ get_location(self) -> str or None """
        return ""

    def get_organizer(self): # real signature unknown; restored from __doc__
        """ get_organizer(self) -> ECal.ComponentOrganizer or None """
        pass

    def get_percent_complete(self): # real signature unknown; restored from __doc__
        """ get_percent_complete(self) -> int """
        return 0

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rdates(self): # real signature unknown; restored from __doc__
        """ get_rdates(self) -> list or None """
        return []

    def get_recurid(self): # real signature unknown; restored from __doc__
        """ get_recurid(self) -> ECal.ComponentRange or None """
        pass

    def get_recurid_as_string(self): # real signature unknown; restored from __doc__
        """ get_recurid_as_string(self) -> str """
        return ""

    def get_rrules(self): # real signature unknown; restored from __doc__
        """ get_rrules(self) -> list or None """
        return []

    def get_rrule_properties(self): # real signature unknown; restored from __doc__
        """ get_rrule_properties(self) -> list or None """
        return []

    def get_sequence(self): # real signature unknown; restored from __doc__
        """ get_sequence(self) -> int """
        return 0

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> ICalGLib.PropertyStatus """
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> ECal.ComponentText or None """
        pass

    def get_transparency(self): # real signature unknown; restored from __doc__
        """ get_transparency(self) -> ECal.ComponentTransparency """
        pass

    def get_uid(self): # real signature unknown; restored from __doc__
        """ get_uid(self) -> str """
        return ""

    def get_url(self): # real signature unknown; restored from __doc__
        """ get_url(self) -> str or None """
        return ""

    def get_vtype(self): # real signature unknown; restored from __doc__
        """ get_vtype(self) -> ECal.ComponentVType """
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

    def has_alarms(self): # real signature unknown; restored from __doc__
        """ has_alarms(self) -> bool """
        return False

    def has_attachments(self): # real signature unknown; restored from __doc__
        """ has_attachments(self) -> bool """
        return False

    def has_attendees(self): # real signature unknown; restored from __doc__
        """ has_attendees(self) -> bool """
        return False

    def has_exceptions(self): # real signature unknown; restored from __doc__
        """ has_exceptions(self) -> bool """
        return False

    def has_exdates(self): # real signature unknown; restored from __doc__
        """ has_exdates(self) -> bool """
        return False

    def has_exrules(self): # real signature unknown; restored from __doc__
        """ has_exrules(self) -> bool """
        return False

    def has_organizer(self): # real signature unknown; restored from __doc__
        """ has_organizer(self) -> bool """
        return False

    def has_rdates(self): # real signature unknown; restored from __doc__
        """ has_rdates(self) -> bool """
        return False

    def has_recurrences(self): # real signature unknown; restored from __doc__
        """ has_recurrences(self) -> bool """
        return False

    def has_rrules(self): # real signature unknown; restored from __doc__
        """ has_rrules(self) -> bool """
        return False

    def has_simple_recurrence(self): # real signature unknown; restored from __doc__
        """ has_simple_recurrence(self) -> bool """
        return False

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

    def is_instance(self): # real signature unknown; restored from __doc__
        """ is_instance(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ECal.Component """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_from_icalcomponent(self, icalcomp): # real signature unknown; restored from __doc__
        """ new_from_icalcomponent(icalcomp:ICalGLib.Component) -> ECal.Component """
        pass

    def new_from_string(self, calobj): # real signature unknown; restored from __doc__
        """ new_from_string(calobj:str) -> ECal.Component """
        pass

    def new_vtype(self, vtype): # real signature unknown; restored from __doc__
        """ new_vtype(vtype:ECal.ComponentVType) -> ECal.Component """
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

    def remove_alarm(self, auid): # real signature unknown; restored from __doc__
        """ remove_alarm(self, auid:str) """
        pass

    def remove_all_alarms(self): # real signature unknown; restored from __doc__
        """ remove_all_alarms(self) """
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

    def set_attachments(self, attachments=None): # real signature unknown; restored from __doc__
        """ set_attachments(self, attachments:list=None) """
        pass

    def set_attendees(self, attendee_list=None): # real signature unknown; restored from __doc__
        """ set_attendees(self, attendee_list:list=None) """
        pass

    def set_categories(self, categories): # real signature unknown; restored from __doc__
        """ set_categories(self, categories:str) """
        pass

    def set_categories_list(self, categ_list): # real signature unknown; restored from __doc__
        """ set_categories_list(self, categ_list:list) """
        pass

    def set_classification(self, classif): # real signature unknown; restored from __doc__
        """ set_classification(self, classif:ECal.ComponentClassification) """
        pass

    def set_comments(self, text_list): # real signature unknown; restored from __doc__
        """ set_comments(self, text_list:list) """
        pass

    def set_completed(self, tt=None): # real signature unknown; restored from __doc__
        """ set_completed(self, tt:ICalGLib.Time=None) """
        pass

    def set_contacts(self, text_list): # real signature unknown; restored from __doc__
        """ set_contacts(self, text_list:list) """
        pass

    def set_created(self, tt=None): # real signature unknown; restored from __doc__
        """ set_created(self, tt:ICalGLib.Time=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_descriptions(self, text_list): # real signature unknown; restored from __doc__
        """ set_descriptions(self, text_list:list) """
        pass

    def set_dtend(self, dt=None): # real signature unknown; restored from __doc__
        """ set_dtend(self, dt:ECal.ComponentDateTime=None) """
        pass

    def set_dtstamp(self, tt): # real signature unknown; restored from __doc__
        """ set_dtstamp(self, tt:ICalGLib.Time) """
        pass

    def set_dtstart(self, dt=None): # real signature unknown; restored from __doc__
        """ set_dtstart(self, dt:ECal.ComponentDateTime=None) """
        pass

    def set_due(self, dt=None): # real signature unknown; restored from __doc__
        """ set_due(self, dt:ECal.ComponentDateTime=None) """
        pass

    def set_exdates(self, exdate_list=None): # real signature unknown; restored from __doc__
        """ set_exdates(self, exdate_list:list=None) """
        pass

    def set_exrules(self, recur_list=None): # real signature unknown; restored from __doc__
        """ set_exrules(self, recur_list:list=None) """
        pass

    def set_geo(self, geo=None): # real signature unknown; restored from __doc__
        """ set_geo(self, geo:ICalGLib.Geo=None) """
        pass

    def set_icalcomponent(self, icalcomp=None): # real signature unknown; restored from __doc__
        """ set_icalcomponent(self, icalcomp:ICalGLib.Component=None) -> bool """
        return False

    def set_last_modified(self, tt=None): # real signature unknown; restored from __doc__
        """ set_last_modified(self, tt:ICalGLib.Time=None) """
        pass

    def set_location(self, location=None): # real signature unknown; restored from __doc__
        """ set_location(self, location:str=None) """
        pass

    def set_new_vtype(self, type): # real signature unknown; restored from __doc__
        """ set_new_vtype(self, type:ECal.ComponentVType) """
        pass

    def set_organizer(self, organizer=None): # real signature unknown; restored from __doc__
        """ set_organizer(self, organizer:ECal.ComponentOrganizer=None) """
        pass

    def set_percent_complete(self, percent): # real signature unknown; restored from __doc__
        """ set_percent_complete(self, percent:int) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rdates(self, rdate_list=None): # real signature unknown; restored from __doc__
        """ set_rdates(self, rdate_list:list=None) """
        pass

    def set_recurid(self, recur_id=None): # real signature unknown; restored from __doc__
        """ set_recurid(self, recur_id:ECal.ComponentRange=None) """
        pass

    def set_rrules(self, recur_list=None): # real signature unknown; restored from __doc__
        """ set_rrules(self, recur_list:list=None) """
        pass

    def set_sequence(self, sequence): # real signature unknown; restored from __doc__
        """ set_sequence(self, sequence:int) """
        pass

    def set_status(self, status): # real signature unknown; restored from __doc__
        """ set_status(self, status:ICalGLib.PropertyStatus) """
        pass

    def set_summary(self, summary): # real signature unknown; restored from __doc__
        """ set_summary(self, summary:ECal.ComponentText) """
        pass

    def set_transparency(self, transp): # real signature unknown; restored from __doc__
        """ set_transparency(self, transp:ECal.ComponentTransparency) """
        pass

    def set_uid(self, uid): # real signature unknown; restored from __doc__
        """ set_uid(self, uid:str) """
        pass

    def set_url(self, url=None): # real signature unknown; restored from __doc__
        """ set_url(self, url:str=None) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fe5cce51c10>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Component), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponent (94764814821424)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_from_icalcomponent': gi.FunctionInfo(new_from_icalcomponent), 'new_from_string': gi.FunctionInfo(new_from_string), 'new_vtype': gi.FunctionInfo(new_vtype), 'abort_sequence': gi.FunctionInfo(abort_sequence), 'add_alarm': gi.FunctionInfo(add_alarm), 'clone': gi.FunctionInfo(clone), 'commit_sequence': gi.FunctionInfo(commit_sequence), 'get_alarm': gi.FunctionInfo(get_alarm), 'get_alarm_uids': gi.FunctionInfo(get_alarm_uids), 'get_all_alarms': gi.FunctionInfo(get_all_alarms), 'get_as_string': gi.FunctionInfo(get_as_string), 'get_attachments': gi.FunctionInfo(get_attachments), 'get_attendees': gi.FunctionInfo(get_attendees), 'get_categories': gi.FunctionInfo(get_categories), 'get_categories_list': gi.FunctionInfo(get_categories_list), 'get_classification': gi.FunctionInfo(get_classification), 'get_comments': gi.FunctionInfo(get_comments), 'get_completed': gi.FunctionInfo(get_completed), 'get_contacts': gi.FunctionInfo(get_contacts), 'get_created': gi.FunctionInfo(get_created), 'get_descriptions': gi.FunctionInfo(get_descriptions), 'get_dtend': gi.FunctionInfo(get_dtend), 'get_dtstamp': gi.FunctionInfo(get_dtstamp), 'get_dtstart': gi.FunctionInfo(get_dtstart), 'get_due': gi.FunctionInfo(get_due), 'get_exdates': gi.FunctionInfo(get_exdates), 'get_exrule_properties': gi.FunctionInfo(get_exrule_properties), 'get_exrules': gi.FunctionInfo(get_exrules), 'get_geo': gi.FunctionInfo(get_geo), 'get_icalcomponent': gi.FunctionInfo(get_icalcomponent), 'get_id': gi.FunctionInfo(get_id), 'get_last_modified': gi.FunctionInfo(get_last_modified), 'get_location': gi.FunctionInfo(get_location), 'get_organizer': gi.FunctionInfo(get_organizer), 'get_percent_complete': gi.FunctionInfo(get_percent_complete), 'get_priority': gi.FunctionInfo(get_priority), 'get_rdates': gi.FunctionInfo(get_rdates), 'get_recurid': gi.FunctionInfo(get_recurid), 'get_recurid_as_string': gi.FunctionInfo(get_recurid_as_string), 'get_rrule_properties': gi.FunctionInfo(get_rrule_properties), 'get_rrules': gi.FunctionInfo(get_rrules), 'get_sequence': gi.FunctionInfo(get_sequence), 'get_status': gi.FunctionInfo(get_status), 'get_summary': gi.FunctionInfo(get_summary), 'get_transparency': gi.FunctionInfo(get_transparency), 'get_uid': gi.FunctionInfo(get_uid), 'get_url': gi.FunctionInfo(get_url), 'get_vtype': gi.FunctionInfo(get_vtype), 'has_alarms': gi.FunctionInfo(has_alarms), 'has_attachments': gi.FunctionInfo(has_attachments), 'has_attendees': gi.FunctionInfo(has_attendees), 'has_exceptions': gi.FunctionInfo(has_exceptions), 'has_exdates': gi.FunctionInfo(has_exdates), 'has_exrules': gi.FunctionInfo(has_exrules), 'has_organizer': gi.FunctionInfo(has_organizer), 'has_rdates': gi.FunctionInfo(has_rdates), 'has_recurrences': gi.FunctionInfo(has_recurrences), 'has_rrules': gi.FunctionInfo(has_rrules), 'has_simple_recurrence': gi.FunctionInfo(has_simple_recurrence), 'is_instance': gi.FunctionInfo(is_instance), 'remove_alarm': gi.FunctionInfo(remove_alarm), 'remove_all_alarms': gi.FunctionInfo(remove_all_alarms), 'set_attachments': gi.FunctionInfo(set_attachments), 'set_attendees': gi.FunctionInfo(set_attendees), 'set_categories': gi.FunctionInfo(set_categories), 'set_categories_list': gi.FunctionInfo(set_categories_list), 'set_classification': gi.FunctionInfo(set_classification), 'set_comments': gi.FunctionInfo(set_comments), 'set_completed': gi.FunctionInfo(set_completed), 'set_contacts': gi.FunctionInfo(set_contacts), 'set_created': gi.FunctionInfo(set_created), 'set_descriptions': gi.FunctionInfo(set_descriptions), 'set_dtend': gi.FunctionInfo(set_dtend), 'set_dtstamp': gi.FunctionInfo(set_dtstamp), 'set_dtstart': gi.FunctionInfo(set_dtstart), 'set_due': gi.FunctionInfo(set_due), 'set_exdates': gi.FunctionInfo(set_exdates), 'set_exrules': gi.FunctionInfo(set_exrules), 'set_geo': gi.FunctionInfo(set_geo), 'set_icalcomponent': gi.FunctionInfo(set_icalcomponent), 'set_last_modified': gi.FunctionInfo(set_last_modified), 'set_location': gi.FunctionInfo(set_location), 'set_new_vtype': gi.FunctionInfo(set_new_vtype), 'set_organizer': gi.FunctionInfo(set_organizer), 'set_percent_complete': gi.FunctionInfo(set_percent_complete), 'set_priority': gi.FunctionInfo(set_priority), 'set_rdates': gi.FunctionInfo(set_rdates), 'set_recurid': gi.FunctionInfo(set_recurid), 'set_rrules': gi.FunctionInfo(set_rrules), 'set_sequence': gi.FunctionInfo(set_sequence), 'set_status': gi.FunctionInfo(set_status), 'set_summary': gi.FunctionInfo(set_summary), 'set_transparency': gi.FunctionInfo(set_transparency), 'set_uid': gi.FunctionInfo(set_uid), 'set_url': gi.FunctionInfo(set_url), 'strip_errors': gi.FunctionInfo(strip_errors), 'parent': <property object at 0x7fe5cce0f4f0>, 'priv': <property object at 0x7fe5cce0f5e0>})"
    __gdoc__ = 'Object ECalComponent\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ECalComponent (94764814821424)>'
    __info__ = ObjectInfo(Component)


