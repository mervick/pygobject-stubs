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


# Variables with simple values

_namespace = 'ICalGLib'

_version = '3.0'

__weakref__ = None

# functions

def bt(): # real signature unknown; restored from __doc__
    """ bt() """
    pass

def errno_return(): # real signature unknown; restored from __doc__
    """ errno_return() -> ICalGLib.ErrorEnum """
    pass

def error_clear_errno(): # real signature unknown; restored from __doc__
    """ error_clear_errno() """
    pass

def error_crash_here(): # real signature unknown; restored from __doc__
    """ error_crash_here() """
    pass

def error_get_error_state(error): # real signature unknown; restored from __doc__
    """ error_get_error_state(error:ICalGLib.ErrorEnum) -> ICalGLib.ErrorState """
    pass

def error_perror(): # real signature unknown; restored from __doc__
    """ error_perror() -> str """
    return ""

def error_restore(error, es): # real signature unknown; restored from __doc__
    """ error_restore(error:str, es:ICalGLib.ErrorState) """
    pass

def error_set_errno(x): # real signature unknown; restored from __doc__
    """ error_set_errno(x:ICalGLib.ErrorEnum) """
    pass

def error_set_error_state(error, state): # real signature unknown; restored from __doc__
    """ error_set_error_state(error:ICalGLib.ErrorEnum, state:ICalGLib.ErrorState) """
    pass

def error_stop_here(): # real signature unknown; restored from __doc__
    """ error_stop_here() """
    pass

def error_strerror(e): # real signature unknown; restored from __doc__
    """ error_strerror(e:ICalGLib.ErrorEnum) -> str """
    return ""

def error_supress(error): # real signature unknown; restored from __doc__
    """ error_supress(error:str) -> ICalGLib.ErrorState """
    pass

def get_unknown_token_handling_setting(): # real signature unknown; restored from __doc__
    """ get_unknown_token_handling_setting() -> ICalGLib.Unknowntokenhandling """
    pass

def memory_add_tmp_buffer(buf=None): # real signature unknown; restored from __doc__
    """ memory_add_tmp_buffer(buf=None) """
    pass

def memory_append_char(buf, pos, ch): # real signature unknown; restored from __doc__
    """ memory_append_char(buf:list, pos:list, ch:int) -> buf:list, pos:list """
    pass

def memory_append_string(buf, pos, p_str): # real signature unknown; restored from __doc__
    """ memory_append_string(buf:list, pos:list, str:str) -> buf:list, pos:list """
    pass

def memory_free_buffer(buf=None): # real signature unknown; restored from __doc__
    """ memory_free_buffer(buf=None) """
    pass

def memory_new_buffer(size): # real signature unknown; restored from __doc__
    """ memory_new_buffer(size:int) """
    pass

def memory_resize_buffer(buf=None, size): # real signature unknown; restored from __doc__
    """ memory_resize_buffer(buf=None, size:int) """
    pass

def memory_strdup(s): # real signature unknown; restored from __doc__
    """ memory_strdup(s:str) -> str """
    return ""

def memory_tmp_buffer(size): # real signature unknown; restored from __doc__
    """ memory_tmp_buffer(size:int) """
    pass

def memory_tmp_copy(p_str): # real signature unknown; restored from __doc__
    """ memory_tmp_copy(str:str) -> str """
    return ""

def mime_parse(func, user_data=None): # real signature unknown; restored from __doc__
    """ mime_parse(func:ICalGLib.MimeParseFunc, user_data=None) -> ICalGLib.Component """
    pass

def recur_expand_recurrence(rule, start, count): # real signature unknown; restored from __doc__
    """ recur_expand_recurrence(rule:str, start:int, count:int) -> list """
    return []

def request_status_code(stat): # real signature unknown; restored from __doc__
    """ request_status_code(stat:ICalGLib.RequestStatus) -> str """
    return ""

def request_status_desc(stat): # real signature unknown; restored from __doc__
    """ request_status_desc(stat:ICalGLib.RequestStatus) -> str """
    return ""

def request_status_from_num(major, minor): # real signature unknown; restored from __doc__
    """ request_status_from_num(major:int, minor:int) -> ICalGLib.RequestStatus """
    pass

def request_status_major(stat): # real signature unknown; restored from __doc__
    """ request_status_major(stat:ICalGLib.RequestStatus) -> int """
    return 0

def request_status_minor(stat): # real signature unknown; restored from __doc__
    """ request_status_minor(stat:ICalGLib.RequestStatus) -> int """
    return 0

def restriction_check(comp): # real signature unknown; restored from __doc__
    """ restriction_check(comp:ICalGLib.Component) -> int """
    return 0

def restriction_compare(restr, count): # real signature unknown; restored from __doc__
    """ restriction_compare(restr:ICalGLib.RestrictionKind, count:int) -> int """
    return 0

def set_unknown_token_handling_setting(newSetting): # real signature unknown; restored from __doc__
    """ set_unknown_token_handling_setting(newSetting:ICalGLib.Unknowntokenhandling) """
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

from .Object import Object
from .Array import Array
from .ArrayClass import ArrayClass
from .Attach import Attach
from .AttachClass import AttachClass
from .CompIter import CompIter
from .CompIterClass import CompIterClass
from .Component import Component
from .ComponentClass import ComponentClass
from .ComponentKind import ComponentKind
from .Datetimeperiod import Datetimeperiod
from .DatetimeperiodClass import DatetimeperiodClass
from .Duration import Duration
from .DurationClass import DurationClass
from .ErrorEnum import ErrorEnum
from .ErrorState import ErrorState
from .Geo import Geo
from .GeoClass import GeoClass
from .ObjectClass import ObjectClass
from .ObjectPrivate import ObjectPrivate
from .Parameter import Parameter
from .ParameterAction import ParameterAction
from .ParameterClass import ParameterClass
from .ParameterCutype import ParameterCutype
from .ParameterEnable import ParameterEnable
from .ParameterEncoding import ParameterEncoding
from .ParameterFbtype import ParameterFbtype
from .ParameterKind import ParameterKind
from .ParameterLocal import ParameterLocal
from .ParameterPartstat import ParameterPartstat
from .ParameterRange import ParameterRange
from .ParameterRelated import ParameterRelated
from .ParameterReltype import ParameterReltype
from .ParameterRequired import ParameterRequired
from .ParameterRole import ParameterRole
from .ParameterRsvp import ParameterRsvp
from .ParameterScheduleagent import ParameterScheduleagent
from .ParameterScheduleforcesend import ParameterScheduleforcesend
from .ParameterStayinformed import ParameterStayinformed
from .ParameterSubstate import ParameterSubstate
from .ParameterValue import ParameterValue
from .ParameterXliccomparetype import ParameterXliccomparetype
from .ParameterXlicerrortype import ParameterXlicerrortype
from .Parser import Parser
from .ParserClass import ParserClass
from .ParserState import ParserState
from .Period import Period
from .PeriodClass import PeriodClass
from .Property import Property
from .PropertyAction import PropertyAction
from .PropertyBusytype import PropertyBusytype
from .PropertyCarlevel import PropertyCarlevel
from .PropertyClass import PropertyClass
from .PropertyCmd import PropertyCmd
from .PropertyKind import PropertyKind
from .PropertyMethod import PropertyMethod
from .PropertyPollcompletion import PropertyPollcompletion
from .PropertyPollmode import PropertyPollmode
from .PropertyQuerylevel import PropertyQuerylevel
from .PropertyStatus import PropertyStatus
from .PropertyTaskmode import PropertyTaskmode
from .PropertyTransp import PropertyTransp
from .PropertyXlicclass import PropertyXlicclass
from .Property_Class import Property_Class
from .RecurIterator import RecurIterator
from .RecurIteratorClass import RecurIteratorClass
from .Recurrence import Recurrence
from .RecurrenceArrayMaxValues import RecurrenceArrayMaxValues
from .RecurrenceArraySizes import RecurrenceArraySizes
from .RecurrenceClass import RecurrenceClass
from .RecurrenceFrequency import RecurrenceFrequency
from .RecurrenceSkip import RecurrenceSkip
from .RecurrenceWeekday import RecurrenceWeekday
from .Reqstat import Reqstat
from .ReqstatClass import ReqstatClass
from .RequestStatus import RequestStatus
from .RestrictionKind import RestrictionKind
from .Time import Time
from .TimeClass import TimeClass
from .TimeSpan import TimeSpan
from .TimeSpanClass import TimeSpanClass
from .Timezone import Timezone
from .TimezoneClass import TimezoneClass
from .Trigger import Trigger
from .TriggerClass import TriggerClass
from .Unknowntokenhandling import Unknowntokenhandling
from .Value import Value
from .ValueClass import ValueClass
from .ValueKind import ValueKind
from ._Array import _Array
from ._Attach import _Attach
from ._CompIter import _CompIter
from ._Component import _Component
from ._Datetimeperiod import _Datetimeperiod
from ._Duration import _Duration
from ._Geo import _Geo
from ._Parameter import _Parameter
from ._Parser import _Parser
from ._Period import _Period
from ._Property import _Property
from ._RecurIterator import _RecurIterator
from ._Recurrence import _Recurrence
from ._Reqstat import _Reqstat
from ._Time import _Time
from ._TimeSpan import _TimeSpan
from ._Timezone import _Timezone
from ._Trigger import _Trigger
from ._Value import _Value
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f13551b1d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/ICalGLib-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.ICalGLib', loader=<gi.importer.DynamicImporter object at 0x7f13551b1d00>)"

