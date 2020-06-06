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


# Variables with simple values

BACKEND_PROPERTY_ALARM_EMAIL_ADDRESS = 'alarm-email-address'

BACKEND_PROPERTY_CAL_EMAIL_ADDRESS = 'cal-email-address'

BACKEND_PROPERTY_DEFAULT_OBJECT = 'default-object'

BACKEND_PROPERTY_REVISION = 'revision'

EVOLUTION_ALARM_UID_PROPERTY = 'X-EVOLUTION-ALARM-UID'

EVOLUTION_ENDDATE_PARAMETER = 'X-EVOLUTION-ENDDATE'

LIBICAL_GLIB_UNSTABLE_API = 1

STATIC_CAPABILITY_ALARM_DESCRIPTION = 'alarm-description'

STATIC_CAPABILITY_ALL_DAY_EVENT_AS_TIME = 'all-day-event-as-time'

STATIC_CAPABILITY_BULK_ADDS = 'bulk-adds'
STATIC_CAPABILITY_BULK_MODIFIES = 'bulk-modifies'
STATIC_CAPABILITY_BULK_REMOVES = 'bulk-removes'

STATIC_CAPABILITY_COMPONENT_COLOR = 'component-color'

STATIC_CAPABILITY_CREATE_MESSAGES = 'create-messages'

STATIC_CAPABILITY_DELEGATE_SUPPORTED = 'delegate-support'

STATIC_CAPABILITY_DELEGATE_TO_MANY = 'delegate-to-many'

STATIC_CAPABILITY_HAS_UNACCEPTED_MEETING = 'has-unaccepted-meeting'

STATIC_CAPABILITY_NO_ALARM_AFTER_START = 'no-alarm-after-start'

STATIC_CAPABILITY_NO_ALARM_REPEAT = 'no-alarm-repeat'

STATIC_CAPABILITY_NO_AUDIO_ALARMS = 'no-audio-alarms'

STATIC_CAPABILITY_NO_CONV_TO_ASSIGN_TASK = 'no-conv-to-assign-task'

STATIC_CAPABILITY_NO_CONV_TO_RECUR = 'no-conv-to-recur'

STATIC_CAPABILITY_NO_DISPLAY_ALARMS = 'no-display-alarms'

STATIC_CAPABILITY_NO_EMAIL_ALARMS = 'no-email-alarms'

STATIC_CAPABILITY_NO_GEN_OPTIONS = 'no-general-options'

STATIC_CAPABILITY_NO_MEMO_START_DATE = 'no-memo-start-date'

STATIC_CAPABILITY_NO_ORGANIZER = 'no-organizer'

STATIC_CAPABILITY_NO_PROCEDURE_ALARMS = 'no-procedure-alarms'

STATIC_CAPABILITY_NO_TASK_ASSIGNMENT = 'no-task-assignment'

STATIC_CAPABILITY_NO_THISANDFUTURE = 'no-thisandfuture'
STATIC_CAPABILITY_NO_THISANDPRIOR = 'no-thisandprior'
STATIC_CAPABILITY_NO_TRANSPARENCY = 'no-transparency'

STATIC_CAPABILITY_ONE_ALARM_ONLY = 'one-alarm-only'

STATIC_CAPABILITY_ORGANIZER_MUST_ACCEPT = 'organizer-must-accept'
STATIC_CAPABILITY_ORGANIZER_MUST_ATTEND = 'organizer-must-attend'

STATIC_CAPABILITY_ORGANIZER_NOT_EMAIL_ADDRESS = 'organizer-not-email-address'

STATIC_CAPABILITY_RECURRENCES_NO_MASTER = 'recurrences-no-master-object'

STATIC_CAPABILITY_REFRESH_SUPPORTED = 'refresh-supported'

STATIC_CAPABILITY_REMOVE_ALARMS = 'remove-alarms'

STATIC_CAPABILITY_REMOVE_ONLY_THIS = 'remove-only-this'

STATIC_CAPABILITY_REQ_SEND_OPTIONS = 'require-send-options'

STATIC_CAPABILITY_SAVE_SCHEDULES = 'save-schedules'

STATIC_CAPABILITY_TASK_CAN_RECUR = 'task-can-recur'

STATIC_CAPABILITY_TASK_DATE_ONLY = 'task-date-only'

STATIC_CAPABILITY_TASK_HANDLE_RECUR = 'task-handle-recur'

STATIC_CAPABILITY_TASK_NO_ALARM = 'task-no-alarm'

_namespace = 'ECal'

_version = '2.0'

__weakref__ = None

# functions

def isodate_from_time_t(t): # real signature unknown; restored from __doc__
    """ isodate_from_time_t(t:int) -> str """
    return ""

def match_tzid(tzid): # real signature unknown; restored from __doc__
    """ match_tzid(tzid:str) -> str """
    return ""

def recur_describe_recurrence(icalcomp, week_start_day, flags): # real signature unknown; restored from __doc__
    """ recur_describe_recurrence(icalcomp:ICalGLib.Component, week_start_day:GLib.DateWeekday, flags:int) -> str or None """
    return ""

def recur_ensure_end_dates(comp, refresh, tz_cb, tz_cb_data=None, cancellable=None): # real signature unknown; restored from __doc__
    """ recur_ensure_end_dates(comp:ECal.Component, refresh:bool, tz_cb:ECal.RecurResolveTimezoneCb, tz_cb_data=None, cancellable:Gio.Cancellable=None) -> bool """
    return False

def recur_generate_instances_sync(icalcomp, interval_start, interval_end, callback=None, callback_user_data=None, get_tz_callback=None, get_tz_callback_user_data=None, default_timezone, cancellable=None): # real signature unknown; restored from __doc__
    """ recur_generate_instances_sync(icalcomp:ICalGLib.Component, interval_start:ICalGLib.Time, interval_end:ICalGLib.Time, callback:ECal.RecurInstanceCb=None, callback_user_data=None, get_tz_callback:ECal.RecurResolveTimezoneCb=None, get_tz_callback_user_data=None, default_timezone:ICalGLib.Timezone, cancellable:Gio.Cancellable=None) -> bool """
    return False

def recur_get_localized_nth(nth): # real signature unknown; restored from __doc__
    """ recur_get_localized_nth(nth:int) -> str """
    return ""

def recur_obtain_enddate(ir, prop, zone, convert_end_date): # real signature unknown; restored from __doc__
    """ recur_obtain_enddate(ir:ICalGLib.Recurrence, prop:ICalGLib.Property, zone:ICalGLib.Timezone, convert_end_date:bool) -> int """
    return 0

def reminder_data_free(rd=None): # real signature unknown; restored from __doc__
    """ reminder_data_free(rd=None) """
    pass

def system_timezone_get_location(): # real signature unknown; restored from __doc__
    """ system_timezone_get_location() -> str """
    return ""

def time_add_day(time, days): # real signature unknown; restored from __doc__
    """ time_add_day(time:int, days:int) -> int """
    return 0

def time_add_day_with_zone(time, days, zone): # real signature unknown; restored from __doc__
    """ time_add_day_with_zone(time:int, days:int, zone:ICalGLib.Timezone) -> int """
    return 0

def time_add_month_with_zone(time, months, zone): # real signature unknown; restored from __doc__
    """ time_add_month_with_zone(time:int, months:int, zone:ICalGLib.Timezone) -> int """
    return 0

def time_add_week(time, weeks): # real signature unknown; restored from __doc__
    """ time_add_week(time:int, weeks:int) -> int """
    return 0

def time_add_week_with_zone(time, weeks, zone): # real signature unknown; restored from __doc__
    """ time_add_week_with_zone(time:int, weeks:int, zone:ICalGLib.Timezone) -> int """
    return 0

def time_days_in_month(year, month): # real signature unknown; restored from __doc__
    """ time_days_in_month(year:int, month:int) -> int """
    return 0

def time_day_begin(t): # real signature unknown; restored from __doc__
    """ time_day_begin(t:int) -> int """
    return 0

def time_day_begin_with_zone(time, zone): # real signature unknown; restored from __doc__
    """ time_day_begin_with_zone(time:int, zone:ICalGLib.Timezone) -> int """
    return 0

def time_day_end(t): # real signature unknown; restored from __doc__
    """ time_day_end(t:int) -> int """
    return 0

def time_day_end_with_zone(time, zone): # real signature unknown; restored from __doc__
    """ time_day_end_with_zone(time:int, zone:ICalGLib.Timezone) -> int """
    return 0

def time_day_of_week(day, month, year): # real signature unknown; restored from __doc__
    """ time_day_of_week(day:int, month:int, year:int) -> int """
    return 0

def time_day_of_year(day, month, year): # real signature unknown; restored from __doc__
    """ time_day_of_year(day:int, month:int, year:int) -> int """
    return 0

def time_from_isodate(p_str): # real signature unknown; restored from __doc__
    """ time_from_isodate(str:str) -> int """
    return 0

def time_is_leap_year(year): # real signature unknown; restored from __doc__
    """ time_is_leap_year(year:int) -> bool """
    return False

def time_leap_years_up_to(year): # real signature unknown; restored from __doc__
    """ time_leap_years_up_to(year:int) -> int """
    return 0

def time_month_begin_with_zone(time, zone): # real signature unknown; restored from __doc__
    """ time_month_begin_with_zone(time:int, zone:ICalGLib.Timezone) -> int """
    return 0

def time_to_gdate_with_zone(date, time, zone=None): # real signature unknown; restored from __doc__
    """ time_to_gdate_with_zone(date:GLib.Date, time:int, zone:ICalGLib.Timezone=None) """
    pass

def time_week_begin_with_zone(time, week_start_day, zone): # real signature unknown; restored from __doc__
    """ time_week_begin_with_zone(time:int, week_start_day:int, zone:ICalGLib.Timezone) -> int """
    return 0

def time_year_begin_with_zone(time, zone): # real signature unknown; restored from __doc__
    """ time_year_begin_with_zone(time:int, zone:ICalGLib.Timezone) -> int """
    return 0

def util_add_timezones_from_component(vcal_comp, icalcomp): # real signature unknown; restored from __doc__
    """ util_add_timezones_from_component(vcal_comp:ICalGLib.Component, icalcomp:ICalGLib.Component) """
    pass

def util_component_dup_x_property(icalcomp, x_name): # real signature unknown; restored from __doc__
    """ util_component_dup_x_property(icalcomp:ICalGLib.Component, x_name:str) -> str or None """
    return ""

def util_component_find_x_property(icalcomp, x_name): # real signature unknown; restored from __doc__
    """ util_component_find_x_property(icalcomp:ICalGLib.Component, x_name:str) -> ICalGLib.Property or None """
    pass

def util_component_get_recurid_as_string(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_get_recurid_as_string(icalcomp:ICalGLib.Component) -> str or None """
    return ""

def util_component_has_alarms(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_has_alarms(icalcomp:ICalGLib.Component) -> bool """
    return False

def util_component_has_attendee(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_has_attendee(icalcomp:ICalGLib.Component) -> bool """
    return False

def util_component_has_organizer(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_has_organizer(icalcomp:ICalGLib.Component) -> bool """
    return False

def util_component_has_property(icalcomp, prop_kind): # real signature unknown; restored from __doc__
    """ util_component_has_property(icalcomp:ICalGLib.Component, prop_kind:ICalGLib.PropertyKind) -> bool """
    return False

def util_component_has_rdates(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_has_rdates(icalcomp:ICalGLib.Component) -> bool """
    return False

def util_component_has_recurrences(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_has_recurrences(icalcomp:ICalGLib.Component) -> bool """
    return False

def util_component_has_rrules(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_has_rrules(icalcomp:ICalGLib.Component) -> bool """
    return False

def util_component_has_x_property(icalcomp, x_name): # real signature unknown; restored from __doc__
    """ util_component_has_x_property(icalcomp:ICalGLib.Component, x_name:str) -> bool """
    return False

def util_component_is_instance(icalcomp): # real signature unknown; restored from __doc__
    """ util_component_is_instance(icalcomp:ICalGLib.Component) -> bool """
    return False

def util_component_remove_property_by_kind(icalcomp, kind, all): # real signature unknown; restored from __doc__
    """ util_component_remove_property_by_kind(icalcomp:ICalGLib.Component, kind:ICalGLib.PropertyKind, all:bool) -> int """
    return 0

def util_component_remove_x_property(icalcomp, x_name): # real signature unknown; restored from __doc__
    """ util_component_remove_x_property(icalcomp:ICalGLib.Component, x_name:str) -> bool """
    return False

def util_component_set_x_property(icalcomp, x_name, value=None): # real signature unknown; restored from __doc__
    """ util_component_set_x_property(icalcomp:ICalGLib.Component, x_name:str, value:str=None) """
    pass

def util_conflict_resolution_to_operation_flags(conflict_resolution): # real signature unknown; restored from __doc__
    """ util_conflict_resolution_to_operation_flags(conflict_resolution:EDataServer.ConflictResolution) -> int """
    return 0

def util_construct_instance(icalcomp, rid): # real signature unknown; restored from __doc__
    """ util_construct_instance(icalcomp:ICalGLib.Component, rid:ICalGLib.Time) -> ICalGLib.Component or None """
    pass

def util_copy_timezone(zone): # real signature unknown; restored from __doc__
    """ util_copy_timezone(zone:ICalGLib.Timezone) -> ICalGLib.Timezone """
    pass

def util_generate_alarms_for_comp(comp, start, end, omit, resolve_tzid, user_data=None, default_timezone): # real signature unknown; restored from __doc__
    """ util_generate_alarms_for_comp(comp:ECal.Component, start:int, end:int, omit:ECal.ComponentAlarmAction, resolve_tzid:ECal.RecurResolveTimezoneCb, user_data=None, default_timezone:ICalGLib.Timezone) -> ECal.ComponentAlarms or None """
    pass

def util_generate_alarms_for_list(comps, start, end, omit, resolve_tzid, user_data=None, default_timezone): # real signature unknown; restored from __doc__
    """ util_generate_alarms_for_list(comps:list, start:int, end:int, omit:ECal.ComponentAlarmAction, resolve_tzid:ECal.RecurResolveTimezoneCb, user_data=None, default_timezone:ICalGLib.Timezone) -> int, comp_alarms:list """
    return 0

def util_get_component_occur_times(comp, tz_cb, tz_cb_data=None, default_timezone, kind): # real signature unknown; restored from __doc__
    """ util_get_component_occur_times(comp:ECal.Component, tz_cb:ECal.RecurResolveTimezoneCb, tz_cb_data=None, default_timezone:ICalGLib.Timezone, kind:ICalGLib.ComponentKind) -> out_start:int, out_end:int """
    pass

def util_get_system_timezone(): # real signature unknown; restored from __doc__
    """ util_get_system_timezone() -> ICalGLib.Timezone or None """
    pass

def util_get_system_timezone_location(): # real signature unknown; restored from __doc__
    """ util_get_system_timezone_location() -> str """
    return ""

def util_icaltime_to_tm(itt): # real signature unknown; restored from __doc__
    """ util_icaltime_to_tm(itt:ICalGLib.Time) """
    pass

def util_icaltime_to_tm_with_zone(itt, from_zone, to_zone): # real signature unknown; restored from __doc__
    """ util_icaltime_to_tm_with_zone(itt:ICalGLib.Time, from_zone:ICalGLib.Timezone, to_zone:ICalGLib.Timezone) """
    pass

def util_init_recur_task_sync(vtodo, cal_client=None, cancellable=None): # real signature unknown; restored from __doc__
    """ util_init_recur_task_sync(vtodo:ICalGLib.Component, cal_client=None, cancellable:Gio.Cancellable=None) -> bool """
    return False

def util_is_first_instance(comp, rid, tz_cb, tz_cb_data=None): # real signature unknown; restored from __doc__
    """ util_is_first_instance(comp:ECal.Component, rid:ICalGLib.Time, tz_cb:ECal.RecurResolveTimezoneCb, tz_cb_data=None) -> bool """
    return False

def util_mark_task_complete_sync(vtodo, completed_time, cal_client=None, cancellable=None): # real signature unknown; restored from __doc__
    """ util_mark_task_complete_sync(vtodo:ICalGLib.Component, completed_time:int, cal_client=None, cancellable:Gio.Cancellable=None) -> bool """
    return False

def util_new_component(kind): # real signature unknown; restored from __doc__
    """ util_new_component(kind:ICalGLib.ComponentKind) -> ICalGLib.Component """
    pass

def util_new_top_level(): # real signature unknown; restored from __doc__
    """ util_new_top_level() -> ICalGLib.Component """
    pass

def util_operation_flags_to_conflict_resolution(flags): # real signature unknown; restored from __doc__
    """ util_operation_flags_to_conflict_resolution(flags:int) -> EDataServer.ConflictResolution """
    pass

def util_parse_ics_file(filename): # real signature unknown; restored from __doc__
    """ util_parse_ics_file(filename:str) -> ICalGLib.Component or None """
    pass

def util_parse_ics_string(string): # real signature unknown; restored from __doc__
    """ util_parse_ics_string(string:str) -> ICalGLib.Component or None """
    pass

def util_priority_from_string(string): # real signature unknown; restored from __doc__
    """ util_priority_from_string(string:str) -> int """
    return 0

def util_priority_to_string(priority): # real signature unknown; restored from __doc__
    """ util_priority_to_string(priority:int) -> str """
    return ""

def util_property_has_parameter(prop, param_kind): # real signature unknown; restored from __doc__
    """ util_property_has_parameter(prop:ICalGLib.Property, param_kind:ICalGLib.ParameterKind) -> bool """
    return False

def util_remove_instances(icalcomp, rid, mod): # real signature unknown; restored from __doc__
    """ util_remove_instances(icalcomp:ICalGLib.Component, rid:ICalGLib.Time, mod:ECal.ObjModType) """
    pass

def util_seconds_to_string(seconds): # real signature unknown; restored from __doc__
    """ util_seconds_to_string(seconds:int) -> str """
    return ""

def util_split_at_instance(icalcomp, rid, master_dtstart=None): # real signature unknown; restored from __doc__
    """ util_split_at_instance(icalcomp:ICalGLib.Component, rid:ICalGLib.Time, master_dtstart:ICalGLib.Time=None) -> ICalGLib.Component or None """
    pass

def util_tm_to_icaltime(tm=None, is_date): # real signature unknown; restored from __doc__
    """ util_tm_to_icaltime(tm=None, is_date:bool) -> ICalGLib.Time """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ Default object formatter. """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ Helper for pickle. """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(*args, **kwargs): # real signature unknown
    """ Size of object in memory, in bytes. """
    pass

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .TimezoneCache import TimezoneCache
from .Client import Client
from .ClientClass import ClientClass
from .ClientError import ClientError
from .ClientPrivate import ClientPrivate
from .ClientSourceType import ClientSourceType
from .ClientTzlookupICalCompData import ClientTzlookupICalCompData
from .ClientView import ClientView
from .ClientViewClass import ClientViewClass
from .ClientViewFlags import ClientViewFlags
from .ClientViewPrivate import ClientViewPrivate
from .Component import Component
from .ComponentAlarm import ComponentAlarm
from .ComponentAlarmAction import ComponentAlarmAction
from .ComponentAlarmInstance import ComponentAlarmInstance
from .ComponentAlarmRepeat import ComponentAlarmRepeat
from .ComponentAlarms import ComponentAlarms
from .ComponentAlarmTrigger import ComponentAlarmTrigger
from .ComponentAlarmTriggerKind import ComponentAlarmTriggerKind
from .ComponentAttendee import ComponentAttendee
from .ComponentClass import ComponentClass
from .ComponentClassification import ComponentClassification
from .ComponentDateTime import ComponentDateTime
from .ComponentId import ComponentId
from .ComponentOrganizer import ComponentOrganizer
from .ComponentParameterBag import ComponentParameterBag
from .ComponentPeriod import ComponentPeriod
from .ComponentPeriodKind import ComponentPeriodKind
from .ComponentPrivate import ComponentPrivate
from .ComponentPropertyBag import ComponentPropertyBag
from .ComponentRange import ComponentRange
from .ComponentRangeKind import ComponentRangeKind
from .ComponentText import ComponentText
from .ComponentTransparency import ComponentTransparency
from .ComponentVType import ComponentVType
from .ObjModType import ObjModType
from .OperationFlags import OperationFlags
from .RecurDescribeRecurrenceFlags import RecurDescribeRecurrenceFlags
from .ReminderData import ReminderData
from .ReminderWatcher import ReminderWatcher
from .ReminderWatcherClass import ReminderWatcherClass
from .ReminderWatcherDescribeFlags import ReminderWatcherDescribeFlags
from .ReminderWatcherPrivate import ReminderWatcherPrivate
from .TimezoneCacheInterface import TimezoneCacheInterface
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fe5cdd15d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/ECal-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.ECal', loader=<gi.importer.DynamicImporter object at 0x7fe5cdd15d00>)"

