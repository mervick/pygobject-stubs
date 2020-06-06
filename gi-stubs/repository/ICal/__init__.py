# encoding: utf-8
# module gi.repository.ICal
# from /usr/lib64/girepository-1.0/ICal-3.0.typelib
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
import gobject as __gobject


# Variables with simple values

BOOLEAN_FALSE = 0
BOOLEAN_TRUE = 1

BY_DAY_SIZE = -6

BY_HOUR_SIZE = 25

BY_MINUTE_SIZE = 61

BY_MONTHDAY_SIZE = 32

BY_MONTH_SIZE = 14

BY_SECOND_SIZE = 62

BY_WEEKNO_SIZE = 56

BY_YEARDAY_SIZE = 386

ERRORS_ARE_FATAL = 0

ICALPARAMETER_FIRST_ENUM = 20000

ICALPARAMETER_LAST_ENUM = 22300

ICALPROPERTY_FIRST_ENUM = 10000

ICALPROPERTY_LAST_ENUM = 11300

MAJOR_VERSION = 3

MINOR_VERSION = 0

PACKAGE = 'libical'

PATCH_VERSION = 8

VERSION = '3.0'

ZONES_TAB_SYSTEM_FILENAME = 'tab/zone_sun.tab'

_namespace = 'ICal'

_version = '3.0'

__weakref__ = None

# functions

def bt(): # real signature unknown; restored from __doc__
    """ bt() """
    pass

def decode_base64(dest, src, size): # real signature unknown; restored from __doc__
    """ decode_base64(dest:str, src:str, size:int) -> str """
    return ""

def decode_quoted_printable(dest, src, size): # real signature unknown; restored from __doc__
    """ decode_quoted_printable(dest:str, src:str, size:int) -> str """
    return ""

def free_zone_directory(): # real signature unknown; restored from __doc__
    """ free_zone_directory() """
    pass

def get_unknown_token_handling_setting(): # real signature unknown; restored from __doc__
    """ get_unknown_token_handling_setting() -> ICal._unknown_token_handling """
    pass

def icalarray_append(array, element=None): # real signature unknown; restored from __doc__
    """ icalarray_append(array:ICal.array, element=None) """
    pass

def icalarray_element_at(array, position): # real signature unknown; restored from __doc__
    """ icalarray_element_at(array:ICal.array, position:int) """
    pass

def icalarray_free(array): # real signature unknown; restored from __doc__
    """ icalarray_free(array:ICal.array) """
    pass

def icalarray_remove_element_at(array, position): # real signature unknown; restored from __doc__
    """ icalarray_remove_element_at(array:ICal.array, position:int) """
    pass

def icalarray_sort(array, compare=None): # real signature unknown; restored from __doc__
    """ icalarray_sort(array:ICal.array, compare=None) """
    pass

def icalattach_get_data(attach): # real signature unknown; restored from __doc__
    """ icalattach_get_data(attach:ICal.attach) -> int """
    return 0

def icalattach_get_is_url(attach): # real signature unknown; restored from __doc__
    """ icalattach_get_is_url(attach:ICal.attach) -> int """
    return 0

def icalattach_get_url(attach): # real signature unknown; restored from __doc__
    """ icalattach_get_url(attach:ICal.attach) -> str """
    return ""

def icalattach_ref(attach): # real signature unknown; restored from __doc__
    """ icalattach_ref(attach:ICal.attach) """
    pass

def icalattach_unref(attach): # real signature unknown; restored from __doc__
    """ icalattach_unref(attach:ICal.attach) """
    pass

def icalcomponent_add_component(parent, child): # real signature unknown; restored from __doc__
    """ icalcomponent_add_component(parent:ICal.component, child:ICal.component) """
    pass

def icalcomponent_add_property(component, property): # real signature unknown; restored from __doc__
    """ icalcomponent_add_property(component:ICal.component, property:ICal.property) """
    pass

def icalcomponent_as_ical_string(component): # real signature unknown; restored from __doc__
    """ icalcomponent_as_ical_string(component:ICal.component) -> str """
    return ""

def icalcomponent_as_ical_string_r(component): # real signature unknown; restored from __doc__
    """ icalcomponent_as_ical_string_r(component:ICal.component) -> str """
    return ""

def icalcomponent_check_restrictions(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_check_restrictions(comp:ICal.component) -> int """
    return 0

def icalcomponent_convert_errors(component): # real signature unknown; restored from __doc__
    """ icalcomponent_convert_errors(component:ICal.component) """
    pass

def icalcomponent_count_components(component, kind): # real signature unknown; restored from __doc__
    """ icalcomponent_count_components(component:ICal.component, kind:ICal.component_kind) -> int """
    return 0

def icalcomponent_count_errors(component): # real signature unknown; restored from __doc__
    """ icalcomponent_count_errors(component:ICal.component) -> int """
    return 0

def icalcomponent_count_properties(component, kind): # real signature unknown; restored from __doc__
    """ icalcomponent_count_properties(component:ICal.component, kind:ICal.property_kind) -> int """
    return 0

def icalcomponent_foreach_recurrence(comp, start=None, end=None, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ icalcomponent_foreach_recurrence(comp:ICal.component, start=None, end=None, callback=None, callback_data=None) """
    pass

def icalcomponent_foreach_tzid(comp, callback=None, callback_data=None): # real signature unknown; restored from __doc__
    """ icalcomponent_foreach_tzid(comp:ICal.component, callback=None, callback_data=None) """
    pass

def icalcomponent_free(component): # real signature unknown; restored from __doc__
    """ icalcomponent_free(component:ICal.component) """
    pass

def icalcomponent_get_comment(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_comment(comp:ICal.component) -> str """
    return ""

def icalcomponent_get_description(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_description(comp:ICal.component) -> str """
    return ""

def icalcomponent_get_dtend(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_dtend(comp:ICal.component) """
    pass

def icalcomponent_get_dtstamp(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_dtstamp(comp:ICal.component) """
    pass

def icalcomponent_get_dtstart(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_dtstart(comp:ICal.component) """
    pass

def icalcomponent_get_due(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_due(comp:ICal.component) """
    pass

def icalcomponent_get_duration(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_duration(comp:ICal.component) """
    pass

def icalcomponent_get_location(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_location(comp:ICal.component) -> str """
    return ""

def icalcomponent_get_method(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_method(comp:ICal.component) -> ICal.property_method """
    pass

def icalcomponent_get_recurrenceid(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_recurrenceid(comp:ICal.component) """
    pass

def icalcomponent_get_relcalid(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_relcalid(comp:ICal.component) -> str """
    return ""

def icalcomponent_get_sequence(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_sequence(comp:ICal.component) -> int """
    return 0

def icalcomponent_get_span(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_span(comp:ICal.component) """
    pass

def icalcomponent_get_status(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_status(comp:ICal.component) """
    pass

def icalcomponent_get_summary(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_summary(comp:ICal.component) -> str """
    return ""

def icalcomponent_get_uid(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_get_uid(comp:ICal.component) -> str """
    return ""

def icalcomponent_isa(component): # real signature unknown; restored from __doc__
    """ icalcomponent_isa(component:ICal.component) -> ICal.component_kind """
    pass

def icalcomponent_isa_component(component=None): # real signature unknown; restored from __doc__
    """ icalcomponent_isa_component(component=None) -> int """
    return 0

def icalcomponent_is_valid(component): # real signature unknown; restored from __doc__
    """ icalcomponent_is_valid(component:ICal.component) -> int """
    return 0

def icalcomponent_kind_is_valid(kind): # real signature unknown; restored from __doc__
    """ icalcomponent_kind_is_valid(kind:ICal.component_kind) -> int """
    return 0

def icalcomponent_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ icalcomponent_kind_to_string(kind:ICal.component_kind) -> str """
    return ""

def icalcomponent_merge_component(comp, comp_to_merge): # real signature unknown; restored from __doc__
    """ icalcomponent_merge_component(comp:ICal.component, comp_to_merge:ICal.component) """
    pass

def icalcomponent_normalize(comp): # real signature unknown; restored from __doc__
    """ icalcomponent_normalize(comp:ICal.component) """
    pass

def icalcomponent_remove_component(parent, child): # real signature unknown; restored from __doc__
    """ icalcomponent_remove_component(parent:ICal.component, child:ICal.component) """
    pass

def icalcomponent_remove_property(component, property): # real signature unknown; restored from __doc__
    """ icalcomponent_remove_property(component:ICal.component, property:ICal.property) """
    pass

def icalcomponent_set_comment(comp, v): # real signature unknown; restored from __doc__
    """ icalcomponent_set_comment(comp:ICal.component, v:str) """
    pass

def icalcomponent_set_description(comp, v): # real signature unknown; restored from __doc__
    """ icalcomponent_set_description(comp:ICal.component, v:str) """
    pass

def icalcomponent_set_dtend(comp, v=None): # real signature unknown; restored from __doc__
    """ icalcomponent_set_dtend(comp:ICal.component, v=None) """
    pass

def icalcomponent_set_dtstamp(comp, v=None): # real signature unknown; restored from __doc__
    """ icalcomponent_set_dtstamp(comp:ICal.component, v=None) """
    pass

def icalcomponent_set_dtstart(comp, v=None): # real signature unknown; restored from __doc__
    """ icalcomponent_set_dtstart(comp:ICal.component, v=None) """
    pass

def icalcomponent_set_due(comp, v=None): # real signature unknown; restored from __doc__
    """ icalcomponent_set_due(comp:ICal.component, v=None) """
    pass

def icalcomponent_set_duration(comp, v=None): # real signature unknown; restored from __doc__
    """ icalcomponent_set_duration(comp:ICal.component, v=None) """
    pass

def icalcomponent_set_location(comp, v): # real signature unknown; restored from __doc__
    """ icalcomponent_set_location(comp:ICal.component, v:str) """
    pass

def icalcomponent_set_method(comp, method): # real signature unknown; restored from __doc__
    """ icalcomponent_set_method(comp:ICal.component, method:ICal.property_method) """
    pass

def icalcomponent_set_parent(component, parent): # real signature unknown; restored from __doc__
    """ icalcomponent_set_parent(component:ICal.component, parent:ICal.component) """
    pass

def icalcomponent_set_recurrenceid(comp, v=None): # real signature unknown; restored from __doc__
    """ icalcomponent_set_recurrenceid(comp:ICal.component, v=None) """
    pass

def icalcomponent_set_relcalid(comp, v): # real signature unknown; restored from __doc__
    """ icalcomponent_set_relcalid(comp:ICal.component, v:str) """
    pass

def icalcomponent_set_sequence(comp, v): # real signature unknown; restored from __doc__
    """ icalcomponent_set_sequence(comp:ICal.component, v:int) """
    pass

def icalcomponent_set_status(comp, v=None): # real signature unknown; restored from __doc__
    """ icalcomponent_set_status(comp:ICal.component, v=None) """
    pass

def icalcomponent_set_summary(comp, v): # real signature unknown; restored from __doc__
    """ icalcomponent_set_summary(comp:ICal.component, v:str) """
    pass

def icalcomponent_set_uid(comp, v): # real signature unknown; restored from __doc__
    """ icalcomponent_set_uid(comp:ICal.component, v:str) """
    pass

def icalcomponent_string_to_kind(string): # real signature unknown; restored from __doc__
    """ icalcomponent_string_to_kind(string:str) -> ICal.component_kind """
    pass

def icalcomponent_strip_errors(component): # real signature unknown; restored from __doc__
    """ icalcomponent_strip_errors(component:ICal.component) """
    pass

def icaldurationtype_as_ical_string(d=None): # real signature unknown; restored from __doc__
    """ icaldurationtype_as_ical_string(d=None) -> str """
    return ""

def icaldurationtype_as_ical_string_r(d=None): # real signature unknown; restored from __doc__
    """ icaldurationtype_as_ical_string_r(d=None) -> str """
    return ""

def icaldurationtype_as_int(duration=None): # real signature unknown; restored from __doc__
    """ icaldurationtype_as_int(duration=None) -> int """
    return 0

def icaldurationtype_bad_duration(): # real signature unknown; restored from __doc__
    """ icaldurationtype_bad_duration() """
    pass

def icaldurationtype_from_int(t): # real signature unknown; restored from __doc__
    """ icaldurationtype_from_int(t:int) """
    pass

def icaldurationtype_from_string(dur): # real signature unknown; restored from __doc__
    """ icaldurationtype_from_string(dur:str) """
    pass

def icaldurationtype_is_bad_duration(d=None): # real signature unknown; restored from __doc__
    """ icaldurationtype_is_bad_duration(d=None) -> int """
    return 0

def icaldurationtype_is_null_duration(d=None): # real signature unknown; restored from __doc__
    """ icaldurationtype_is_null_duration(d=None) -> int """
    return 0

def icaldurationtype_null_duration(): # real signature unknown; restored from __doc__
    """ icaldurationtype_null_duration() """
    pass

def icalenum_num_to_reqstat(major, minor): # real signature unknown; restored from __doc__
    """ icalenum_num_to_reqstat(major:int, minor:int) -> ICal.requeststatus """
    pass

def icalenum_reqstat_code(stat): # real signature unknown; restored from __doc__
    """ icalenum_reqstat_code(stat:ICal.requeststatus) -> str """
    return ""

def icalenum_reqstat_code_r(stat): # real signature unknown; restored from __doc__
    """ icalenum_reqstat_code_r(stat:ICal.requeststatus) -> str """
    return ""

def icalenum_reqstat_desc(stat): # real signature unknown; restored from __doc__
    """ icalenum_reqstat_desc(stat:ICal.requeststatus) -> str """
    return ""

def icalenum_reqstat_major(stat): # real signature unknown; restored from __doc__
    """ icalenum_reqstat_major(stat:ICal.requeststatus) -> int """
    return 0

def icalenum_reqstat_minor(stat): # real signature unknown; restored from __doc__
    """ icalenum_reqstat_minor(stat:ICal.requeststatus) -> int """
    return 0

def icalerrno_return(): # real signature unknown; restored from __doc__
    """ icalerrno_return() -> ICal.errorenum """
    pass

def icalerror_clear_errno(): # real signature unknown; restored from __doc__
    """ icalerror_clear_errno() """
    pass

def icalerror_crash_here(): # real signature unknown; restored from __doc__
    """ icalerror_crash_here() """
    pass

def icalerror_error_from_string(p_str): # real signature unknown; restored from __doc__
    """ icalerror_error_from_string(str:str) -> ICal.errorenum """
    pass

def icalerror_get_errors_are_fatal(): # real signature unknown; restored from __doc__
    """ icalerror_get_errors_are_fatal() -> int """
    return 0

def icalerror_get_error_state(error): # real signature unknown; restored from __doc__
    """ icalerror_get_error_state(error:ICal.errorenum) -> ICal.errorstate """
    pass

def icalerror_perror(): # real signature unknown; restored from __doc__
    """ icalerror_perror() -> str """
    return ""

def icalerror_restore(error, es): # real signature unknown; restored from __doc__
    """ icalerror_restore(error:str, es:ICal.errorstate) """
    pass

def icalerror_set_errno(x): # real signature unknown; restored from __doc__
    """ icalerror_set_errno(x:ICal.errorenum) """
    pass

def icalerror_set_errors_are_fatal(fatal): # real signature unknown; restored from __doc__
    """ icalerror_set_errors_are_fatal(fatal:int) """
    pass

def icalerror_set_error_state(error, state): # real signature unknown; restored from __doc__
    """ icalerror_set_error_state(error:ICal.errorenum, state:ICal.errorstate) """
    pass

def icalerror_stop_here(): # real signature unknown; restored from __doc__
    """ icalerror_stop_here() """
    pass

def icalerror_strerror(e): # real signature unknown; restored from __doc__
    """ icalerror_strerror(e:ICal.errorenum) -> str """
    return ""

def icalerror_supress(error): # real signature unknown; restored from __doc__
    """ icalerror_supress(error:str) -> ICal.errorstate """
    pass

def icallangbind_access_array(array, index): # real signature unknown; restored from __doc__
    """ icallangbind_access_array(array:int, index:int) -> int """
    return 0

def icallangbind_free_array(array): # real signature unknown; restored from __doc__
    """ icallangbind_free_array(array:int) """
    pass

def icallangbind_new_array(size): # real signature unknown; restored from __doc__
    """ icallangbind_new_array(size:int) -> int """
    return 0

def icallangbind_property_eval_string(prop, sep): # real signature unknown; restored from __doc__
    """ icallangbind_property_eval_string(prop:ICal.property, sep:str) -> str """
    return ""

def icallangbind_property_eval_string_r(prop, sep): # real signature unknown; restored from __doc__
    """ icallangbind_property_eval_string_r(prop:ICal.property, sep:str) -> str """
    return ""

def icallangbind_quote_as_ical(p_str): # real signature unknown; restored from __doc__
    """ icallangbind_quote_as_ical(str:str) -> str """
    return ""

def icallangbind_quote_as_ical_r(p_str): # real signature unknown; restored from __doc__
    """ icallangbind_quote_as_ical_r(str:str) -> str """
    return ""

def icallangbind_string_to_open_flag(p_str): # real signature unknown; restored from __doc__
    """ icallangbind_string_to_open_flag(str:str) -> int """
    return 0

def icalmemory_add_tmp_buffer(buf=None): # real signature unknown; restored from __doc__
    """ icalmemory_add_tmp_buffer(buf=None) """
    pass

def icalmemory_append_char(buf, pos, buf_size, ch): # real signature unknown; restored from __doc__
    """ icalmemory_append_char(buf:str, pos:str, buf_size:int, ch:int) """
    pass

def icalmemory_append_string(buf, pos, buf_size, string): # real signature unknown; restored from __doc__
    """ icalmemory_append_string(buf:str, pos:str, buf_size:int, string:str) """
    pass

def icalmemory_free_buffer(buf=None): # real signature unknown; restored from __doc__
    """ icalmemory_free_buffer(buf=None) """
    pass

def icalmemory_free_ring(): # real signature unknown; restored from __doc__
    """ icalmemory_free_ring() """
    pass

def icalmemory_new_buffer(size): # real signature unknown; restored from __doc__
    """ icalmemory_new_buffer(size:int) """
    pass

def icalmemory_resize_buffer(buf=None, size): # real signature unknown; restored from __doc__
    """ icalmemory_resize_buffer(buf=None, size:int) """
    pass

def icalmemory_strdup(s): # real signature unknown; restored from __doc__
    """ icalmemory_strdup(s:str) -> str """
    return ""

def icalmemory_tmp_buffer(size): # real signature unknown; restored from __doc__
    """ icalmemory_tmp_buffer(size:int) """
    pass

def icalmemory_tmp_copy(p_str): # real signature unknown; restored from __doc__
    """ icalmemory_tmp_copy(str:str) -> str """
    return ""

def icalparameter_as_ical_string(parameter): # real signature unknown; restored from __doc__
    """ icalparameter_as_ical_string(parameter:ICal.parameter) -> str """
    return ""

def icalparameter_as_ical_string_r(parameter): # real signature unknown; restored from __doc__
    """ icalparameter_as_ical_string_r(parameter:ICal.parameter) -> str """
    return ""

def icalparameter_enum_to_string(e): # real signature unknown; restored from __doc__
    """ icalparameter_enum_to_string(e:int) -> str """
    return ""

def icalparameter_free(parameter): # real signature unknown; restored from __doc__
    """ icalparameter_free(parameter:ICal.parameter) """
    pass

def icalparameter_get_actionparam(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_actionparam(value:ICal.parameter) -> ICal.parameter_action """
    pass

def icalparameter_get_altrep(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_altrep(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_charset(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_charset(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_cn(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_cn(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_cutype(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_cutype(value:ICal.parameter) -> ICal.parameter_cutype """
    pass

def icalparameter_get_delegatedfrom(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_delegatedfrom(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_delegatedto(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_delegatedto(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_dir(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_dir(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_display(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_display(value:ICal.parameter) -> ICal.parameter_display """
    pass

def icalparameter_get_email(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_email(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_enable(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_enable(value:ICal.parameter) -> ICal.parameter_enable """
    pass

def icalparameter_get_encoding(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_encoding(value:ICal.parameter) -> ICal.parameter_encoding """
    pass

def icalparameter_get_fbtype(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_fbtype(value:ICal.parameter) -> ICal.parameter_fbtype """
    pass

def icalparameter_get_feature(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_feature(value:ICal.parameter) -> ICal.parameter_feature """
    pass

def icalparameter_get_filename(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_filename(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_fmttype(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_fmttype(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_iana(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_iana(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_iana_name(param): # real signature unknown; restored from __doc__
    """ icalparameter_get_iana_name(param:ICal.parameter) -> str """
    return ""

def icalparameter_get_iana_value(param): # real signature unknown; restored from __doc__
    """ icalparameter_get_iana_value(param:ICal.parameter) -> str """
    return ""

def icalparameter_get_id(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_id(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_label(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_label(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_language(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_language(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_latency(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_latency(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_local(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_local(value:ICal.parameter) -> ICal.parameter_local """
    pass

def icalparameter_get_localize(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_localize(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_managedid(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_managedid(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_member(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_member(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_modified(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_modified(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_options(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_options(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_partstat(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_partstat(value:ICal.parameter) -> ICal.parameter_partstat """
    pass

def icalparameter_get_patchaction(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_patchaction(value:ICal.parameter) -> ICal.parameter_patchaction """
    pass

def icalparameter_get_publiccomment(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_publiccomment(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_range(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_range(value:ICal.parameter) -> ICal.parameter_range """
    pass

def icalparameter_get_reason(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_reason(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_related(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_related(value:ICal.parameter) -> ICal.parameter_related """
    pass

def icalparameter_get_reltype(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_reltype(value:ICal.parameter) -> ICal.parameter_reltype """
    pass

def icalparameter_get_required(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_required(value:ICal.parameter) -> ICal.parameter_required """
    pass

def icalparameter_get_response(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_response(value:ICal.parameter) -> int """
    return 0

def icalparameter_get_role(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_role(value:ICal.parameter) -> ICal.parameter_role """
    pass

def icalparameter_get_rsvp(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_rsvp(value:ICal.parameter) -> ICal.parameter_rsvp """
    pass

def icalparameter_get_scheduleagent(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_scheduleagent(value:ICal.parameter) -> ICal.parameter_scheduleagent """
    pass

def icalparameter_get_scheduleforcesend(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_scheduleforcesend(value:ICal.parameter) -> ICal.parameter_scheduleforcesend """
    pass

def icalparameter_get_schedulestatus(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_schedulestatus(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_sentby(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_sentby(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_size(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_size(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_stayinformed(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_stayinformed(value:ICal.parameter) -> ICal.parameter_stayinformed """
    pass

def icalparameter_get_substate(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_substate(value:ICal.parameter) -> ICal.parameter_substate """
    pass

def icalparameter_get_tzid(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_tzid(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_value(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_value(value:ICal.parameter) -> ICal.parameter_value """
    pass

def icalparameter_get_x(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_x(value:ICal.parameter) -> str """
    return ""

def icalparameter_get_xliccomparetype(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_xliccomparetype(value:ICal.parameter) -> ICal.parameter_xliccomparetype """
    pass

def icalparameter_get_xlicerrortype(value): # real signature unknown; restored from __doc__
    """ icalparameter_get_xlicerrortype(value:ICal.parameter) -> ICal.parameter_xlicerrortype """
    pass

def icalparameter_get_xname(param): # real signature unknown; restored from __doc__
    """ icalparameter_get_xname(param:ICal.parameter) -> str """
    return ""

def icalparameter_get_xvalue(param): # real signature unknown; restored from __doc__
    """ icalparameter_get_xvalue(param:ICal.parameter) -> str """
    return ""

def icalparameter_has_same_name(param1, param2): # real signature unknown; restored from __doc__
    """ icalparameter_has_same_name(param1:ICal.parameter, param2:ICal.parameter) -> int """
    return 0

def icalparameter_isa(parameter): # real signature unknown; restored from __doc__
    """ icalparameter_isa(parameter:ICal.parameter) -> ICal.parameter_kind """
    pass

def icalparameter_isa_parameter(param=None): # real signature unknown; restored from __doc__
    """ icalparameter_isa_parameter(param=None) -> int """
    return 0

def icalparameter_kind_is_valid(kind): # real signature unknown; restored from __doc__
    """ icalparameter_kind_is_valid(kind:ICal.parameter_kind) -> int """
    return 0

def icalparameter_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ icalparameter_kind_to_string(kind:ICal.parameter_kind) -> str """
    return ""

def icalparameter_set_actionparam(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_actionparam(value:ICal.parameter, v:ICal.parameter_action) """
    pass

def icalparameter_set_altrep(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_altrep(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_charset(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_charset(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_cn(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_cn(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_cutype(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_cutype(value:ICal.parameter, v:ICal.parameter_cutype) """
    pass

def icalparameter_set_delegatedfrom(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_delegatedfrom(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_delegatedto(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_delegatedto(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_dir(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_dir(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_display(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_display(value:ICal.parameter, v:ICal.parameter_display) """
    pass

def icalparameter_set_email(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_email(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_enable(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_enable(value:ICal.parameter, v:ICal.parameter_enable) """
    pass

def icalparameter_set_encoding(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_encoding(value:ICal.parameter, v:ICal.parameter_encoding) """
    pass

def icalparameter_set_fbtype(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_fbtype(value:ICal.parameter, v:ICal.parameter_fbtype) """
    pass

def icalparameter_set_feature(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_feature(value:ICal.parameter, v:ICal.parameter_feature) """
    pass

def icalparameter_set_filename(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_filename(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_fmttype(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_fmttype(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_iana(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_iana(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_iana_name(param, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_iana_name(param:ICal.parameter, v:str) """
    pass

def icalparameter_set_iana_value(param, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_iana_value(param:ICal.parameter, v:str) """
    pass

def icalparameter_set_id(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_id(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_label(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_label(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_language(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_language(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_latency(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_latency(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_local(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_local(value:ICal.parameter, v:ICal.parameter_local) """
    pass

def icalparameter_set_localize(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_localize(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_managedid(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_managedid(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_member(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_member(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_modified(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_modified(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_options(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_options(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_parent(param, property): # real signature unknown; restored from __doc__
    """ icalparameter_set_parent(param:ICal.parameter, property:ICal.property) """
    pass

def icalparameter_set_partstat(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_partstat(value:ICal.parameter, v:ICal.parameter_partstat) """
    pass

def icalparameter_set_patchaction(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_patchaction(value:ICal.parameter, v:ICal.parameter_patchaction) """
    pass

def icalparameter_set_publiccomment(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_publiccomment(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_range(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_range(value:ICal.parameter, v:ICal.parameter_range) """
    pass

def icalparameter_set_reason(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_reason(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_related(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_related(value:ICal.parameter, v:ICal.parameter_related) """
    pass

def icalparameter_set_reltype(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_reltype(value:ICal.parameter, v:ICal.parameter_reltype) """
    pass

def icalparameter_set_required(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_required(value:ICal.parameter, v:ICal.parameter_required) """
    pass

def icalparameter_set_response(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_response(value:ICal.parameter, v:int) """
    pass

def icalparameter_set_role(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_role(value:ICal.parameter, v:ICal.parameter_role) """
    pass

def icalparameter_set_rsvp(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_rsvp(value:ICal.parameter, v:ICal.parameter_rsvp) """
    pass

def icalparameter_set_scheduleagent(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_scheduleagent(value:ICal.parameter, v:ICal.parameter_scheduleagent) """
    pass

def icalparameter_set_scheduleforcesend(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_scheduleforcesend(value:ICal.parameter, v:ICal.parameter_scheduleforcesend) """
    pass

def icalparameter_set_schedulestatus(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_schedulestatus(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_sentby(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_sentby(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_size(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_size(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_stayinformed(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_stayinformed(value:ICal.parameter, v:ICal.parameter_stayinformed) """
    pass

def icalparameter_set_substate(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_substate(value:ICal.parameter, v:ICal.parameter_substate) """
    pass

def icalparameter_set_tzid(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_tzid(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_value(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_value(value:ICal.parameter, v:ICal.parameter_value) """
    pass

def icalparameter_set_x(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_x(value:ICal.parameter, v:str) """
    pass

def icalparameter_set_xliccomparetype(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_xliccomparetype(value:ICal.parameter, v:ICal.parameter_xliccomparetype) """
    pass

def icalparameter_set_xlicerrortype(value, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_xlicerrortype(value:ICal.parameter, v:ICal.parameter_xlicerrortype) """
    pass

def icalparameter_set_xname(param, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_xname(param:ICal.parameter, v:str) """
    pass

def icalparameter_set_xvalue(param, v): # real signature unknown; restored from __doc__
    """ icalparameter_set_xvalue(param:ICal.parameter, v:str) """
    pass

def icalparameter_string_to_enum(p_str): # real signature unknown; restored from __doc__
    """ icalparameter_string_to_enum(str:str) -> int """
    return 0

def icalparameter_string_to_kind(string): # real signature unknown; restored from __doc__
    """ icalparameter_string_to_kind(string:str) -> ICal.parameter_kind """
    pass

def icalparameter_value_to_value_kind(value): # real signature unknown; restored from __doc__
    """ icalparameter_value_to_value_kind(value:ICal.parameter_value) -> ICal.value_kind """
    pass

def icalparser_free(parser): # real signature unknown; restored from __doc__
    """ icalparser_free(parser:ICal.parser) """
    pass

def icalparser_get_state(parser): # real signature unknown; restored from __doc__
    """ icalparser_get_state(parser:ICal.parser) -> ICal.parser_state """
    pass

def icalparser_set_gen_data(parser, data=None): # real signature unknown; restored from __doc__
    """ icalparser_set_gen_data(parser:ICal.parser, data=None) """
    pass

def icalparser_string_line_generator(out, buf_size, d=None): # real signature unknown; restored from __doc__
    """ icalparser_string_line_generator(out:str, buf_size:int, d=None) -> str """
    return ""

def icalperiodtype_as_ical_string(p=None): # real signature unknown; restored from __doc__
    """ icalperiodtype_as_ical_string(p=None) -> str """
    return ""

def icalperiodtype_as_ical_string_r(p=None): # real signature unknown; restored from __doc__
    """ icalperiodtype_as_ical_string_r(p=None) -> str """
    return ""

def icalperiodtype_from_string(p_str): # real signature unknown; restored from __doc__
    """ icalperiodtype_from_string(str:str) """
    pass

def icalperiodtype_is_null_period(p=None): # real signature unknown; restored from __doc__
    """ icalperiodtype_is_null_period(p=None) -> int """
    return 0

def icalperiodtype_is_valid_period(p=None): # real signature unknown; restored from __doc__
    """ icalperiodtype_is_valid_period(p=None) -> int """
    return 0

def icalperiodtype_null_period(): # real signature unknown; restored from __doc__
    """ icalperiodtype_null_period() """
    pass

def icalproperty_add_parameter(prop, parameter): # real signature unknown; restored from __doc__
    """ icalproperty_add_parameter(prop:ICal.property, parameter:ICal.parameter) """
    pass

def icalproperty_as_ical_string(prop): # real signature unknown; restored from __doc__
    """ icalproperty_as_ical_string(prop:ICal.property) -> str """
    return ""

def icalproperty_as_ical_string_r(prop): # real signature unknown; restored from __doc__
    """ icalproperty_as_ical_string_r(prop:ICal.property) -> str """
    return ""

def icalproperty_count_parameters(prop): # real signature unknown; restored from __doc__
    """ icalproperty_count_parameters(prop:ICal.property) -> int """
    return 0

def icalproperty_enum_belongs_to_property(kind, e): # real signature unknown; restored from __doc__
    """ icalproperty_enum_belongs_to_property(kind:ICal.property_kind, e:int) -> int """
    return 0

def icalproperty_enum_to_string(e): # real signature unknown; restored from __doc__
    """ icalproperty_enum_to_string(e:int) -> str """
    return ""

def icalproperty_enum_to_string_r(e): # real signature unknown; restored from __doc__
    """ icalproperty_enum_to_string_r(e:int) -> str """
    return ""

def icalproperty_free(prop): # real signature unknown; restored from __doc__
    """ icalproperty_free(prop:ICal.property) """
    pass

def icalproperty_get_acceptresponse(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_acceptresponse(prop:ICal.property) -> str """
    return ""

def icalproperty_get_acknowledged(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_acknowledged(prop:ICal.property) """
    pass

def icalproperty_get_action(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_action(prop:ICal.property) """
    pass

def icalproperty_get_allowconflict(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_allowconflict(prop:ICal.property) -> str """
    return ""

def icalproperty_get_attendee(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_attendee(prop:ICal.property) -> str """
    return ""

def icalproperty_get_busytype(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_busytype(prop:ICal.property) """
    pass

def icalproperty_get_calid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_calid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_calmaster(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_calmaster(prop:ICal.property) -> str """
    return ""

def icalproperty_get_calscale(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_calscale(prop:ICal.property) -> str """
    return ""

def icalproperty_get_capversion(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_capversion(prop:ICal.property) -> str """
    return ""

def icalproperty_get_carid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_carid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_carlevel(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_carlevel(prop:ICal.property) """
    pass

def icalproperty_get_categories(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_categories(prop:ICal.property) -> str """
    return ""

def icalproperty_get_class(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_class(prop:ICal.property) """
    pass

def icalproperty_get_cmd(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_cmd(prop:ICal.property) """
    pass

def icalproperty_get_color(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_color(prop:ICal.property) -> str """
    return ""

def icalproperty_get_comment(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_comment(prop:ICal.property) -> str """
    return ""

def icalproperty_get_completed(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_completed(prop:ICal.property) """
    pass

def icalproperty_get_components(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_components(prop:ICal.property) -> str """
    return ""

def icalproperty_get_conference(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_conference(prop:ICal.property) -> str """
    return ""

def icalproperty_get_contact(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_contact(prop:ICal.property) -> str """
    return ""

def icalproperty_get_created(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_created(prop:ICal.property) """
    pass

def icalproperty_get_csid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_csid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_datemax(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_datemax(prop:ICal.property) """
    pass

def icalproperty_get_datemin(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_datemin(prop:ICal.property) """
    pass

def icalproperty_get_datetime_with_component(prop, comp): # real signature unknown; restored from __doc__
    """ icalproperty_get_datetime_with_component(prop:ICal.property, comp:ICal.component) """
    pass

def icalproperty_get_decreed(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_decreed(prop:ICal.property) -> str """
    return ""

def icalproperty_get_defaultcharset(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_defaultcharset(prop:ICal.property) -> str """
    return ""

def icalproperty_get_defaultlocale(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_defaultlocale(prop:ICal.property) -> str """
    return ""

def icalproperty_get_defaulttzid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_defaulttzid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_defaultvcars(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_defaultvcars(prop:ICal.property) -> str """
    return ""

def icalproperty_get_deny(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_deny(prop:ICal.property) -> str """
    return ""

def icalproperty_get_description(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_description(prop:ICal.property) -> str """
    return ""

def icalproperty_get_dtend(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_dtend(prop:ICal.property) """
    pass

def icalproperty_get_dtstamp(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_dtstamp(prop:ICal.property) """
    pass

def icalproperty_get_dtstart(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_dtstart(prop:ICal.property) """
    pass

def icalproperty_get_due(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_due(prop:ICal.property) """
    pass

def icalproperty_get_duration(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_duration(prop:ICal.property) """
    pass

def icalproperty_get_estimatedduration(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_estimatedduration(prop:ICal.property) """
    pass

def icalproperty_get_exdate(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_exdate(prop:ICal.property) """
    pass

def icalproperty_get_expand(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_expand(prop:ICal.property) -> int """
    return 0

def icalproperty_get_exrule(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_exrule(prop:ICal.property) """
    pass

def icalproperty_get_freebusy(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_freebusy(prop:ICal.property) """
    pass

def icalproperty_get_geo(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_geo(prop:ICal.property) """
    pass

def icalproperty_get_grant(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_grant(prop:ICal.property) -> str """
    return ""

def icalproperty_get_itipversion(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_itipversion(prop:ICal.property) -> str """
    return ""

def icalproperty_get_lastmodified(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_lastmodified(prop:ICal.property) """
    pass

def icalproperty_get_location(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_location(prop:ICal.property) -> str """
    return ""

def icalproperty_get_maxcomponentsize(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_maxcomponentsize(prop:ICal.property) -> int """
    return 0

def icalproperty_get_maxdate(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_maxdate(prop:ICal.property) """
    pass

def icalproperty_get_maxresults(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_maxresults(prop:ICal.property) -> int """
    return 0

def icalproperty_get_maxresultssize(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_maxresultssize(prop:ICal.property) -> int """
    return 0

def icalproperty_get_method(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_method(prop:ICal.property) """
    pass

def icalproperty_get_mindate(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_mindate(prop:ICal.property) """
    pass

def icalproperty_get_multipart(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_multipart(prop:ICal.property) -> str """
    return ""

def icalproperty_get_name(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_name(prop:ICal.property) -> str """
    return ""

def icalproperty_get_organizer(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_organizer(prop:ICal.property) -> str """
    return ""

def icalproperty_get_owner(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_owner(prop:ICal.property) -> str """
    return ""

def icalproperty_get_parameter_as_string(prop, name): # real signature unknown; restored from __doc__
    """ icalproperty_get_parameter_as_string(prop:ICal.property, name:str) -> str """
    return ""

def icalproperty_get_parameter_as_string_r(prop, name): # real signature unknown; restored from __doc__
    """ icalproperty_get_parameter_as_string_r(prop:ICal.property, name:str) -> str """
    return ""

def icalproperty_get_patchdelete(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_patchdelete(prop:ICal.property) -> str """
    return ""

def icalproperty_get_patchorder(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_patchorder(prop:ICal.property) -> int """
    return 0

def icalproperty_get_patchparameter(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_patchparameter(prop:ICal.property) -> str """
    return ""

def icalproperty_get_patchtarget(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_patchtarget(prop:ICal.property) -> str """
    return ""

def icalproperty_get_patchversion(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_patchversion(prop:ICal.property) -> str """
    return ""

def icalproperty_get_percentcomplete(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_percentcomplete(prop:ICal.property) -> int """
    return 0

def icalproperty_get_permission(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_permission(prop:ICal.property) -> str """
    return ""

def icalproperty_get_pollcompletion(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_pollcompletion(prop:ICal.property) """
    pass

def icalproperty_get_pollitemid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_pollitemid(prop:ICal.property) -> int """
    return 0

def icalproperty_get_pollmode(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_pollmode(prop:ICal.property) """
    pass

def icalproperty_get_pollproperties(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_pollproperties(prop:ICal.property) -> str """
    return ""

def icalproperty_get_pollwinner(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_pollwinner(prop:ICal.property) -> int """
    return 0

def icalproperty_get_priority(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_priority(prop:ICal.property) -> int """
    return 0

def icalproperty_get_prodid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_prodid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_property_name(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_property_name(prop:ICal.property) -> str """
    return ""

def icalproperty_get_property_name_r(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_property_name_r(prop:ICal.property) -> str """
    return ""

def icalproperty_get_query(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_query(prop:ICal.property) -> str """
    return ""

def icalproperty_get_queryid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_queryid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_querylevel(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_querylevel(prop:ICal.property) """
    pass

def icalproperty_get_queryname(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_queryname(prop:ICal.property) -> str """
    return ""

def icalproperty_get_rdate(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_rdate(prop:ICal.property) """
    pass

def icalproperty_get_recuraccepted(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_recuraccepted(prop:ICal.property) -> str """
    return ""

def icalproperty_get_recurexpand(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_recurexpand(prop:ICal.property) -> str """
    return ""

def icalproperty_get_recurlimit(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_recurlimit(prop:ICal.property) -> str """
    return ""

def icalproperty_get_recurrenceid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_recurrenceid(prop:ICal.property) """
    pass

def icalproperty_get_refreshinterval(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_refreshinterval(prop:ICal.property) """
    pass

def icalproperty_get_relatedto(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_relatedto(prop:ICal.property) -> str """
    return ""

def icalproperty_get_relcalid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_relcalid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_repeat(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_repeat(prop:ICal.property) -> int """
    return 0

def icalproperty_get_replyurl(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_replyurl(prop:ICal.property) -> str """
    return ""

def icalproperty_get_requeststatus(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_requeststatus(prop:ICal.property) """
    pass

def icalproperty_get_resources(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_resources(prop:ICal.property) -> str """
    return ""

def icalproperty_get_response(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_response(prop:ICal.property) -> int """
    return 0

def icalproperty_get_restriction(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_restriction(prop:ICal.property) -> str """
    return ""

def icalproperty_get_rrule(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_rrule(prop:ICal.property) """
    pass

def icalproperty_get_scope(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_scope(prop:ICal.property) -> str """
    return ""

def icalproperty_get_sequence(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_sequence(prop:ICal.property) -> int """
    return 0

def icalproperty_get_source(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_source(prop:ICal.property) -> str """
    return ""

def icalproperty_get_status(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_status(prop:ICal.property) """
    pass

def icalproperty_get_storesexpanded(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_storesexpanded(prop:ICal.property) -> str """
    return ""

def icalproperty_get_summary(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_summary(prop:ICal.property) -> str """
    return ""

def icalproperty_get_target(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_target(prop:ICal.property) -> str """
    return ""

def icalproperty_get_taskmode(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_taskmode(prop:ICal.property) """
    pass

def icalproperty_get_transp(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_transp(prop:ICal.property) """
    pass

def icalproperty_get_trigger(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_trigger(prop:ICal.property) """
    pass

def icalproperty_get_tzid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_tzid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_tzidaliasof(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_tzidaliasof(prop:ICal.property) -> str """
    return ""

def icalproperty_get_tzname(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_tzname(prop:ICal.property) -> str """
    return ""

def icalproperty_get_tzoffsetfrom(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_tzoffsetfrom(prop:ICal.property) -> int """
    return 0

def icalproperty_get_tzoffsetto(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_tzoffsetto(prop:ICal.property) -> int """
    return 0

def icalproperty_get_tzuntil(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_tzuntil(prop:ICal.property) """
    pass

def icalproperty_get_tzurl(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_tzurl(prop:ICal.property) -> str """
    return ""

def icalproperty_get_uid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_uid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_url(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_url(prop:ICal.property) -> str """
    return ""

def icalproperty_get_value_as_string(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_value_as_string(prop:ICal.property) -> str """
    return ""

def icalproperty_get_value_as_string_r(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_value_as_string_r(prop:ICal.property) -> str """
    return ""

def icalproperty_get_version(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_version(prop:ICal.property) -> str """
    return ""

def icalproperty_get_voter(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_voter(prop:ICal.property) -> str """
    return ""

def icalproperty_get_x(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_x(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicclass(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicclass(prop:ICal.property) """
    pass

def icalproperty_get_xlicclustercount(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicclustercount(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicerror(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicerror(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicmimecharset(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicmimecharset(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicmimecid(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicmimecid(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicmimecontenttype(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicmimecontenttype(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicmimeencoding(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicmimeencoding(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicmimefilename(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicmimefilename(prop:ICal.property) -> str """
    return ""

def icalproperty_get_xlicmimeoptinfo(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_xlicmimeoptinfo(prop:ICal.property) -> str """
    return ""

def icalproperty_get_x_name(prop): # real signature unknown; restored from __doc__
    """ icalproperty_get_x_name(prop:ICal.property) -> str """
    return ""

def icalproperty_isa(property): # real signature unknown; restored from __doc__
    """ icalproperty_isa(property:ICal.property) -> ICal.property_kind """
    pass

def icalproperty_isa_property(property=None): # real signature unknown; restored from __doc__
    """ icalproperty_isa_property(property=None) -> int """
    return 0

def icalproperty_kind_and_string_to_enum(kind, p_str): # real signature unknown; restored from __doc__
    """ icalproperty_kind_and_string_to_enum(kind:int, str:str) -> int """
    return 0

def icalproperty_kind_is_valid(kind): # real signature unknown; restored from __doc__
    """ icalproperty_kind_is_valid(kind:ICal.property_kind) -> int """
    return 0

def icalproperty_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ icalproperty_kind_to_string(kind:ICal.property_kind) -> str """
    return ""

def icalproperty_kind_to_value_kind(kind): # real signature unknown; restored from __doc__
    """ icalproperty_kind_to_value_kind(kind:ICal.property_kind) -> ICal.value_kind """
    pass

def icalproperty_method_to_string(method): # real signature unknown; restored from __doc__
    """ icalproperty_method_to_string(method:ICal.property_method) -> str """
    return ""

def icalproperty_normalize(prop): # real signature unknown; restored from __doc__
    """ icalproperty_normalize(prop:ICal.property) """
    pass

def icalproperty_recurrence_is_excluded(comp, dtstart=None, recurtime=None): # real signature unknown; restored from __doc__
    """ icalproperty_recurrence_is_excluded(comp:ICal.component, dtstart=None, recurtime=None) -> int """
    return 0

def icalproperty_remove_parameter_by_kind(prop, kind): # real signature unknown; restored from __doc__
    """ icalproperty_remove_parameter_by_kind(prop:ICal.property, kind:ICal.parameter_kind) """
    pass

def icalproperty_remove_parameter_by_name(prop, name): # real signature unknown; restored from __doc__
    """ icalproperty_remove_parameter_by_name(prop:ICal.property, name:str) """
    pass

def icalproperty_remove_parameter_by_ref(prop, param): # real signature unknown; restored from __doc__
    """ icalproperty_remove_parameter_by_ref(prop:ICal.property, param:ICal.parameter) """
    pass

def icalproperty_set_acceptresponse(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_acceptresponse(prop:ICal.property, v:str) """
    pass

def icalproperty_set_acknowledged(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_acknowledged(prop:ICal.property, v=None) """
    pass

def icalproperty_set_action(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_action(prop:ICal.property, v=None) """
    pass

def icalproperty_set_allowconflict(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_allowconflict(prop:ICal.property, v:str) """
    pass

def icalproperty_set_attach(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_attach(prop:ICal.property, v:ICal.attach) """
    pass

def icalproperty_set_attendee(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_attendee(prop:ICal.property, v:str) """
    pass

def icalproperty_set_busytype(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_busytype(prop:ICal.property, v=None) """
    pass

def icalproperty_set_calid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_calid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_calmaster(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_calmaster(prop:ICal.property, v:str) """
    pass

def icalproperty_set_calscale(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_calscale(prop:ICal.property, v:str) """
    pass

def icalproperty_set_capversion(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_capversion(prop:ICal.property, v:str) """
    pass

def icalproperty_set_carid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_carid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_carlevel(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_carlevel(prop:ICal.property, v=None) """
    pass

def icalproperty_set_categories(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_categories(prop:ICal.property, v:str) """
    pass

def icalproperty_set_class(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_class(prop:ICal.property, v=None) """
    pass

def icalproperty_set_cmd(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_cmd(prop:ICal.property, v=None) """
    pass

def icalproperty_set_color(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_color(prop:ICal.property, v:str) """
    pass

def icalproperty_set_comment(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_comment(prop:ICal.property, v:str) """
    pass

def icalproperty_set_completed(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_completed(prop:ICal.property, v=None) """
    pass

def icalproperty_set_components(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_components(prop:ICal.property, v:str) """
    pass

def icalproperty_set_conference(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_conference(prop:ICal.property, v:str) """
    pass

def icalproperty_set_contact(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_contact(prop:ICal.property, v:str) """
    pass

def icalproperty_set_created(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_created(prop:ICal.property, v=None) """
    pass

def icalproperty_set_csid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_csid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_datemax(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_datemax(prop:ICal.property, v=None) """
    pass

def icalproperty_set_datemin(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_datemin(prop:ICal.property, v=None) """
    pass

def icalproperty_set_decreed(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_decreed(prop:ICal.property, v:str) """
    pass

def icalproperty_set_defaultcharset(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_defaultcharset(prop:ICal.property, v:str) """
    pass

def icalproperty_set_defaultlocale(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_defaultlocale(prop:ICal.property, v:str) """
    pass

def icalproperty_set_defaulttzid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_defaulttzid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_defaultvcars(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_defaultvcars(prop:ICal.property, v:str) """
    pass

def icalproperty_set_deny(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_deny(prop:ICal.property, v:str) """
    pass

def icalproperty_set_description(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_description(prop:ICal.property, v:str) """
    pass

def icalproperty_set_dtend(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_dtend(prop:ICal.property, v=None) """
    pass

def icalproperty_set_dtstamp(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_dtstamp(prop:ICal.property, v=None) """
    pass

def icalproperty_set_dtstart(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_dtstart(prop:ICal.property, v=None) """
    pass

def icalproperty_set_due(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_due(prop:ICal.property, v=None) """
    pass

def icalproperty_set_duration(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_duration(prop:ICal.property, v=None) """
    pass

def icalproperty_set_estimatedduration(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_estimatedduration(prop:ICal.property, v=None) """
    pass

def icalproperty_set_exdate(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_exdate(prop:ICal.property, v=None) """
    pass

def icalproperty_set_expand(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_expand(prop:ICal.property, v:int) """
    pass

def icalproperty_set_exrule(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_exrule(prop:ICal.property, v=None) """
    pass

def icalproperty_set_freebusy(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_freebusy(prop:ICal.property, v=None) """
    pass

def icalproperty_set_geo(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_geo(prop:ICal.property, v=None) """
    pass

def icalproperty_set_grant(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_grant(prop:ICal.property, v:str) """
    pass

def icalproperty_set_image(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_image(prop:ICal.property, v:ICal.attach) """
    pass

def icalproperty_set_itipversion(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_itipversion(prop:ICal.property, v:str) """
    pass

def icalproperty_set_lastmodified(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_lastmodified(prop:ICal.property, v=None) """
    pass

def icalproperty_set_location(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_location(prop:ICal.property, v:str) """
    pass

def icalproperty_set_maxcomponentsize(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_maxcomponentsize(prop:ICal.property, v:int) """
    pass

def icalproperty_set_maxdate(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_maxdate(prop:ICal.property, v=None) """
    pass

def icalproperty_set_maxresults(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_maxresults(prop:ICal.property, v:int) """
    pass

def icalproperty_set_maxresultssize(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_maxresultssize(prop:ICal.property, v:int) """
    pass

def icalproperty_set_method(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_method(prop:ICal.property, v=None) """
    pass

def icalproperty_set_mindate(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_mindate(prop:ICal.property, v=None) """
    pass

def icalproperty_set_multipart(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_multipart(prop:ICal.property, v:str) """
    pass

def icalproperty_set_name(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_name(prop:ICal.property, v:str) """
    pass

def icalproperty_set_organizer(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_organizer(prop:ICal.property, v:str) """
    pass

def icalproperty_set_owner(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_owner(prop:ICal.property, v:str) """
    pass

def icalproperty_set_parameter(prop, parameter): # real signature unknown; restored from __doc__
    """ icalproperty_set_parameter(prop:ICal.property, parameter:ICal.parameter) """
    pass

def icalproperty_set_parameter_from_string(prop, name, value): # real signature unknown; restored from __doc__
    """ icalproperty_set_parameter_from_string(prop:ICal.property, name:str, value:str) """
    pass

def icalproperty_set_parent(property, component): # real signature unknown; restored from __doc__
    """ icalproperty_set_parent(property:ICal.property, component:ICal.component) """
    pass

def icalproperty_set_patchdelete(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_patchdelete(prop:ICal.property, v:str) """
    pass

def icalproperty_set_patchorder(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_patchorder(prop:ICal.property, v:int) """
    pass

def icalproperty_set_patchparameter(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_patchparameter(prop:ICal.property, v:str) """
    pass

def icalproperty_set_patchtarget(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_patchtarget(prop:ICal.property, v:str) """
    pass

def icalproperty_set_patchversion(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_patchversion(prop:ICal.property, v:str) """
    pass

def icalproperty_set_percentcomplete(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_percentcomplete(prop:ICal.property, v:int) """
    pass

def icalproperty_set_permission(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_permission(prop:ICal.property, v:str) """
    pass

def icalproperty_set_pollcompletion(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_pollcompletion(prop:ICal.property, v=None) """
    pass

def icalproperty_set_pollitemid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_pollitemid(prop:ICal.property, v:int) """
    pass

def icalproperty_set_pollmode(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_pollmode(prop:ICal.property, v=None) """
    pass

def icalproperty_set_pollproperties(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_pollproperties(prop:ICal.property, v:str) """
    pass

def icalproperty_set_pollwinner(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_pollwinner(prop:ICal.property, v:int) """
    pass

def icalproperty_set_priority(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_priority(prop:ICal.property, v:int) """
    pass

def icalproperty_set_prodid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_prodid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_query(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_query(prop:ICal.property, v:str) """
    pass

def icalproperty_set_queryid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_queryid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_querylevel(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_querylevel(prop:ICal.property, v=None) """
    pass

def icalproperty_set_queryname(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_queryname(prop:ICal.property, v:str) """
    pass

def icalproperty_set_rdate(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_rdate(prop:ICal.property, v=None) """
    pass

def icalproperty_set_recuraccepted(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_recuraccepted(prop:ICal.property, v:str) """
    pass

def icalproperty_set_recurexpand(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_recurexpand(prop:ICal.property, v:str) """
    pass

def icalproperty_set_recurlimit(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_recurlimit(prop:ICal.property, v:str) """
    pass

def icalproperty_set_recurrenceid(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_recurrenceid(prop:ICal.property, v=None) """
    pass

def icalproperty_set_refreshinterval(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_refreshinterval(prop:ICal.property, v=None) """
    pass

def icalproperty_set_relatedto(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_relatedto(prop:ICal.property, v:str) """
    pass

def icalproperty_set_relcalid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_relcalid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_repeat(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_repeat(prop:ICal.property, v:int) """
    pass

def icalproperty_set_replyurl(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_replyurl(prop:ICal.property, v:str) """
    pass

def icalproperty_set_requeststatus(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_requeststatus(prop:ICal.property, v=None) """
    pass

def icalproperty_set_resources(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_resources(prop:ICal.property, v:str) """
    pass

def icalproperty_set_response(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_response(prop:ICal.property, v:int) """
    pass

def icalproperty_set_restriction(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_restriction(prop:ICal.property, v:str) """
    pass

def icalproperty_set_rrule(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_rrule(prop:ICal.property, v=None) """
    pass

def icalproperty_set_scope(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_scope(prop:ICal.property, v:str) """
    pass

def icalproperty_set_sequence(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_sequence(prop:ICal.property, v:int) """
    pass

def icalproperty_set_source(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_source(prop:ICal.property, v:str) """
    pass

def icalproperty_set_status(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_status(prop:ICal.property, v=None) """
    pass

def icalproperty_set_storesexpanded(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_storesexpanded(prop:ICal.property, v:str) """
    pass

def icalproperty_set_summary(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_summary(prop:ICal.property, v:str) """
    pass

def icalproperty_set_target(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_target(prop:ICal.property, v:str) """
    pass

def icalproperty_set_taskmode(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_taskmode(prop:ICal.property, v=None) """
    pass

def icalproperty_set_transp(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_transp(prop:ICal.property, v=None) """
    pass

def icalproperty_set_trigger(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_trigger(prop:ICal.property, v=None) """
    pass

def icalproperty_set_tzid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_tzid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_tzidaliasof(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_tzidaliasof(prop:ICal.property, v:str) """
    pass

def icalproperty_set_tzname(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_tzname(prop:ICal.property, v:str) """
    pass

def icalproperty_set_tzoffsetfrom(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_tzoffsetfrom(prop:ICal.property, v:int) """
    pass

def icalproperty_set_tzoffsetto(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_tzoffsetto(prop:ICal.property, v:int) """
    pass

def icalproperty_set_tzuntil(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_tzuntil(prop:ICal.property, v=None) """
    pass

def icalproperty_set_tzurl(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_tzurl(prop:ICal.property, v:str) """
    pass

def icalproperty_set_uid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_uid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_url(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_url(prop:ICal.property, v:str) """
    pass

def icalproperty_set_value(prop, value): # real signature unknown; restored from __doc__
    """ icalproperty_set_value(prop:ICal.property, value:ICal.value) """
    pass

def icalproperty_set_value_from_string(prop, value, kind): # real signature unknown; restored from __doc__
    """ icalproperty_set_value_from_string(prop:ICal.property, value:str, kind:str) """
    pass

def icalproperty_set_version(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_version(prop:ICal.property, v:str) """
    pass

def icalproperty_set_voter(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_voter(prop:ICal.property, v:str) """
    pass

def icalproperty_set_x(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_x(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicclass(prop, v=None): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicclass(prop:ICal.property, v=None) """
    pass

def icalproperty_set_xlicclustercount(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicclustercount(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicerror(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicerror(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicmimecharset(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicmimecharset(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicmimecid(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicmimecid(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicmimecontenttype(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicmimecontenttype(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicmimeencoding(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicmimeencoding(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicmimefilename(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicmimefilename(prop:ICal.property, v:str) """
    pass

def icalproperty_set_xlicmimeoptinfo(prop, v): # real signature unknown; restored from __doc__
    """ icalproperty_set_xlicmimeoptinfo(prop:ICal.property, v:str) """
    pass

def icalproperty_set_x_name(prop, name): # real signature unknown; restored from __doc__
    """ icalproperty_set_x_name(prop:ICal.property, name:str) """
    pass

def icalproperty_status_to_string(arg0): # real signature unknown; restored from __doc__
    """ icalproperty_status_to_string(arg0:ICal.property_status) -> str """
    return ""

def icalproperty_string_to_kind(string): # real signature unknown; restored from __doc__
    """ icalproperty_string_to_kind(string:str) -> ICal.property_kind """
    pass

def icalproperty_string_to_method(p_str): # real signature unknown; restored from __doc__
    """ icalproperty_string_to_method(str:str) -> ICal.property_method """
    pass

def icalproperty_string_to_status(string): # real signature unknown; restored from __doc__
    """ icalproperty_string_to_status(string:str) -> ICal.property_status """
    pass

def icalproperty_value_kind_to_kind(kind): # real signature unknown; restored from __doc__
    """ icalproperty_value_kind_to_kind(kind:ICal.value_kind) -> ICal.property_kind """
    pass

def icalrecurrencetype_as_string(recur=None): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_as_string(recur=None) -> str """
    return ""

def icalrecurrencetype_as_string_r(recur=None): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_as_string_r(recur=None) -> str """
    return ""

def icalrecurrencetype_clear(r=None): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_clear(r=None) """
    pass

def icalrecurrencetype_day_day_of_week(day): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_day_day_of_week(day:int) """
    pass

def icalrecurrencetype_day_position(day): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_day_position(day:int) -> int """
    return 0

def icalrecurrencetype_from_string(p_str): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_from_string(str:str) """
    pass

def icalrecurrencetype_month_is_leap(month): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_month_is_leap(month:int) -> int """
    return 0

def icalrecurrencetype_month_month(month): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_month_month(month:int) -> int """
    return 0

def icalrecurrencetype_rscale_is_supported(): # real signature unknown; restored from __doc__
    """ icalrecurrencetype_rscale_is_supported() -> int """
    return 0

def icalrecur_expand_recurrence(rule, start, count, array): # real signature unknown; restored from __doc__
    """ icalrecur_expand_recurrence(rule:str, start:int, count:int, array:int) -> int """
    return 0

def icalrecur_freq_to_string(kind): # real signature unknown; restored from __doc__
    """ icalrecur_freq_to_string(kind:ICal.recurrencetype_frequency) -> str """
    return ""

def icalrecur_iterator_free(arg0): # real signature unknown; restored from __doc__
    """ icalrecur_iterator_free(arg0:ICal.recur_iterator) """
    pass

def icalrecur_iterator_next(arg0): # real signature unknown; restored from __doc__
    """ icalrecur_iterator_next(arg0:ICal.recur_iterator) """
    pass

def icalrecur_iterator_set_start(impl, start=None): # real signature unknown; restored from __doc__
    """ icalrecur_iterator_set_start(impl:ICal.recur_iterator, start=None) -> int """
    return 0

def icalrecur_skip_to_string(kind): # real signature unknown; restored from __doc__
    """ icalrecur_skip_to_string(kind:ICal.recurrencetype_skip) -> str """
    return ""

def icalrecur_string_to_freq(p_str): # real signature unknown; restored from __doc__
    """ icalrecur_string_to_freq(str:str) -> ICal.recurrencetype_frequency """
    pass

def icalrecur_string_to_skip(p_str): # real signature unknown; restored from __doc__
    """ icalrecur_string_to_skip(str:str) -> ICal.recurrencetype_skip """
    pass

def icalrecur_string_to_weekday(p_str): # real signature unknown; restored from __doc__
    """ icalrecur_string_to_weekday(str:str) -> ICal.recurrencetype_weekday """
    pass

def icalrecur_weekday_to_string(kind): # real signature unknown; restored from __doc__
    """ icalrecur_weekday_to_string(kind:ICal.recurrencetype_weekday) -> str """
    return ""

def icalreqstattype_as_string(arg0=None): # real signature unknown; restored from __doc__
    """ icalreqstattype_as_string(arg0=None) -> str """
    return ""

def icalreqstattype_as_string_r(arg0=None): # real signature unknown; restored from __doc__
    """ icalreqstattype_as_string_r(arg0=None) -> str """
    return ""

def icalreqstattype_from_string(p_str): # real signature unknown; restored from __doc__
    """ icalreqstattype_from_string(str:str) """
    pass

def icalrestriction_check(comp): # real signature unknown; restored from __doc__
    """ icalrestriction_check(comp:ICal.component) -> int """
    return 0

def icalrestriction_compare(restr, count): # real signature unknown; restored from __doc__
    """ icalrestriction_compare(restr:ICal.restriction_kind, count:int) -> int """
    return 0

def icaltimezone_array_append_from_vtimezone(timezones, child): # real signature unknown; restored from __doc__
    """ icaltimezone_array_append_from_vtimezone(timezones:ICal.array, child:ICal.component) """
    pass

def icaltimezone_array_free(timezones): # real signature unknown; restored from __doc__
    """ icaltimezone_array_free(timezones:ICal.array) """
    pass

def icaltimezone_convert_time(tt=None, from_zone, to_zone): # real signature unknown; restored from __doc__
    """ icaltimezone_convert_time(tt=None, from_zone:ICal.timezone, to_zone:ICal.timezone) """
    pass

def icaltimezone_dump_changes(zone, max_year, fp=None): # real signature unknown; restored from __doc__
    """ icaltimezone_dump_changes(zone:ICal.timezone, max_year:int, fp=None) -> int """
    return 0

def icaltimezone_expand_vtimezone(comp, end_year, changes): # real signature unknown; restored from __doc__
    """ icaltimezone_expand_vtimezone(comp:ICal.component, end_year:int, changes:ICal.array) """
    pass

def icaltimezone_free(zone, free_struct): # real signature unknown; restored from __doc__
    """ icaltimezone_free(zone:ICal.timezone, free_struct:int) """
    pass

def icaltimezone_free_builtin_timezones(): # real signature unknown; restored from __doc__
    """ icaltimezone_free_builtin_timezones() """
    pass

def icaltimezone_get_builtin_tzdata(): # real signature unknown; restored from __doc__
    """ icaltimezone_get_builtin_tzdata() -> int """
    return 0

def icaltimezone_get_display_name(zone): # real signature unknown; restored from __doc__
    """ icaltimezone_get_display_name(zone:ICal.timezone) -> str """
    return ""

def icaltimezone_get_latitude(zone): # real signature unknown; restored from __doc__
    """ icaltimezone_get_latitude(zone:ICal.timezone) -> float """
    return 0.0

def icaltimezone_get_location(zone): # real signature unknown; restored from __doc__
    """ icaltimezone_get_location(zone:ICal.timezone) -> str """
    return ""

def icaltimezone_get_location_from_vtimezone(component): # real signature unknown; restored from __doc__
    """ icaltimezone_get_location_from_vtimezone(component:ICal.component) -> str """
    return ""

def icaltimezone_get_longitude(zone): # real signature unknown; restored from __doc__
    """ icaltimezone_get_longitude(zone:ICal.timezone) -> float """
    return 0.0

def icaltimezone_get_tzid(zone): # real signature unknown; restored from __doc__
    """ icaltimezone_get_tzid(zone:ICal.timezone) -> str """
    return ""

def icaltimezone_get_tznames(zone): # real signature unknown; restored from __doc__
    """ icaltimezone_get_tznames(zone:ICal.timezone) -> str """
    return ""

def icaltimezone_get_tznames_from_vtimezone(component): # real signature unknown; restored from __doc__
    """ icaltimezone_get_tznames_from_vtimezone(component:ICal.component) -> str """
    return ""

def icaltimezone_get_utc_offset(zone, tt=None, is_daylight): # real signature unknown; restored from __doc__
    """ icaltimezone_get_utc_offset(zone:ICal.timezone, tt=None, is_daylight:int) -> int """
    return 0

def icaltimezone_get_utc_offset_of_utc_time(zone, tt=None, is_daylight): # real signature unknown; restored from __doc__
    """ icaltimezone_get_utc_offset_of_utc_time(zone:ICal.timezone, tt=None, is_daylight:int) -> int """
    return 0

def icaltimezone_release_zone_tab(): # real signature unknown; restored from __doc__
    """ icaltimezone_release_zone_tab() """
    pass

def icaltimezone_set_builtin_tzdata(set): # real signature unknown; restored from __doc__
    """ icaltimezone_set_builtin_tzdata(set:int) """
    pass

def icaltimezone_set_component(zone, comp): # real signature unknown; restored from __doc__
    """ icaltimezone_set_component(zone:ICal.timezone, comp:ICal.component) -> int """
    return 0

def icaltimezone_set_tzid_prefix(new_prefix): # real signature unknown; restored from __doc__
    """ icaltimezone_set_tzid_prefix(new_prefix:str) """
    pass

def icaltimezone_truncate_vtimezone(vtz, start, end, ms_compatible): # real signature unknown; restored from __doc__
    """ icaltimezone_truncate_vtimezone(vtz:ICal.component, start:ICal.timetype, end:ICal.timetype, ms_compatible:int) """
    pass

def icaltimezone_tzid_prefix(): # real signature unknown; restored from __doc__
    """ icaltimezone_tzid_prefix() -> str """
    return ""

def icaltime_add(t=None, d=None): # real signature unknown; restored from __doc__
    """ icaltime_add(t=None, d=None) """
    pass

def icaltime_adjust(tt=None, days, hours, minutes, seconds): # real signature unknown; restored from __doc__
    """ icaltime_adjust(tt=None, days:int, hours:int, minutes:int, seconds:int) """
    pass

def icaltime_as_ical_string(tt=None): # real signature unknown; restored from __doc__
    """ icaltime_as_ical_string(tt=None) -> str """
    return ""

def icaltime_as_ical_string_r(tt=None): # real signature unknown; restored from __doc__
    """ icaltime_as_ical_string_r(tt=None) -> str """
    return ""

def icaltime_as_timet(arg0=None): # real signature unknown; restored from __doc__
    """ icaltime_as_timet(arg0=None) -> int """
    return 0

def icaltime_as_timet_with_zone(tt=None, zone): # real signature unknown; restored from __doc__
    """ icaltime_as_timet_with_zone(tt=None, zone:ICal.timezone) -> int """
    return 0

def icaltime_compare(a=None, b=None): # real signature unknown; restored from __doc__
    """ icaltime_compare(a=None, b=None) -> int """
    return 0

def icaltime_compare_date_only(a=None, b=None): # real signature unknown; restored from __doc__
    """ icaltime_compare_date_only(a=None, b=None) -> int """
    return 0

def icaltime_compare_date_only_tz(a=None, b=None, tz): # real signature unknown; restored from __doc__
    """ icaltime_compare_date_only_tz(a=None, b=None, tz:ICal.timezone) -> int """
    return 0

def icaltime_convert_to_zone(tt=None, zone): # real signature unknown; restored from __doc__
    """ icaltime_convert_to_zone(tt=None, zone:ICal.timezone) """
    pass

def icaltime_current_time_with_zone(zone): # real signature unknown; restored from __doc__
    """ icaltime_current_time_with_zone(zone:ICal.timezone) """
    pass

def icaltime_days_in_month(month, year): # real signature unknown; restored from __doc__
    """ icaltime_days_in_month(month:int, year:int) -> int """
    return 0

def icaltime_days_in_year(year): # real signature unknown; restored from __doc__
    """ icaltime_days_in_year(year:int) -> int """
    return 0

def icaltime_day_of_week(t=None): # real signature unknown; restored from __doc__
    """ icaltime_day_of_week(t=None) -> int """
    return 0

def icaltime_day_of_year(t=None): # real signature unknown; restored from __doc__
    """ icaltime_day_of_year(t=None) -> int """
    return 0

def icaltime_from_day_of_year(doy, year): # real signature unknown; restored from __doc__
    """ icaltime_from_day_of_year(doy:int, year:int) """
    pass

def icaltime_from_string(p_str): # real signature unknown; restored from __doc__
    """ icaltime_from_string(str:str) """
    pass

def icaltime_from_timet_with_zone(tm, is_date, zone): # real signature unknown; restored from __doc__
    """ icaltime_from_timet_with_zone(tm:int, is_date:int, zone:ICal.timezone) """
    pass

def icaltime_get_timezone(t=None): # real signature unknown; restored from __doc__
    """ icaltime_get_timezone(t=None) -> ICal.timezone """
    pass

def icaltime_get_tzid(t=None): # real signature unknown; restored from __doc__
    """ icaltime_get_tzid(t=None) -> str """
    return ""

def icaltime_is_date(t=None): # real signature unknown; restored from __doc__
    """ icaltime_is_date(t=None) -> int """
    return 0

def icaltime_is_leap_year(year): # real signature unknown; restored from __doc__
    """ icaltime_is_leap_year(year:int) -> int """
    return 0

def icaltime_is_null_time(t=None): # real signature unknown; restored from __doc__
    """ icaltime_is_null_time(t=None) -> int """
    return 0

def icaltime_is_utc(t=None): # real signature unknown; restored from __doc__
    """ icaltime_is_utc(t=None) -> int """
    return 0

def icaltime_is_valid_time(t=None): # real signature unknown; restored from __doc__
    """ icaltime_is_valid_time(t=None) -> int """
    return 0

def icaltime_normalize(t=None): # real signature unknown; restored from __doc__
    """ icaltime_normalize(t=None) """
    pass

def icaltime_null_date(): # real signature unknown; restored from __doc__
    """ icaltime_null_date() """
    pass

def icaltime_null_time(): # real signature unknown; restored from __doc__
    """ icaltime_null_time() """
    pass

def icaltime_set_timezone(t=None, zone): # real signature unknown; restored from __doc__
    """ icaltime_set_timezone(t=None, zone:ICal.timezone) """
    pass

def icaltime_span_contains(s, container): # real signature unknown; restored from __doc__
    """ icaltime_span_contains(s:ICal.time_span, container:ICal.time_span) -> int """
    return 0

def icaltime_span_new(dtstart=None, dtend=None, is_busy): # real signature unknown; restored from __doc__
    """ icaltime_span_new(dtstart=None, dtend=None, is_busy:int) """
    pass

def icaltime_span_overlaps(s1, s2): # real signature unknown; restored from __doc__
    """ icaltime_span_overlaps(s1:ICal.time_span, s2:ICal.time_span) -> int """
    return 0

def icaltime_start_doy_week(t=None, fdow): # real signature unknown; restored from __doc__
    """ icaltime_start_doy_week(t=None, fdow:int) -> int """
    return 0

def icaltime_subtract(t1=None, t2=None): # real signature unknown; restored from __doc__
    """ icaltime_subtract(t1=None, t2=None) """
    pass

def icaltime_today(): # real signature unknown; restored from __doc__
    """ icaltime_today() """
    pass

def icaltime_week_number(t=None): # real signature unknown; restored from __doc__
    """ icaltime_week_number(t=None) -> int """
    return 0

def icaltriggertype_from_int(reltime): # real signature unknown; restored from __doc__
    """ icaltriggertype_from_int(reltime:int) """
    pass

def icaltriggertype_from_string(p_str): # real signature unknown; restored from __doc__
    """ icaltriggertype_from_string(str:str) """
    pass

def icaltriggertype_is_bad_trigger(tr=None): # real signature unknown; restored from __doc__
    """ icaltriggertype_is_bad_trigger(tr=None) -> int """
    return 0

def icaltriggertype_is_null_trigger(tr=None): # real signature unknown; restored from __doc__
    """ icaltriggertype_is_null_trigger(tr=None) -> int """
    return 0

def icaltzutil_get_zone_directory(): # real signature unknown; restored from __doc__
    """ icaltzutil_get_zone_directory() -> str """
    return ""

def icalvalue_as_ical_string(value): # real signature unknown; restored from __doc__
    """ icalvalue_as_ical_string(value:ICal.value) -> str """
    return ""

def icalvalue_as_ical_string_r(value): # real signature unknown; restored from __doc__
    """ icalvalue_as_ical_string_r(value:ICal.value) -> str """
    return ""

def icalvalue_compare(a, b): # real signature unknown; restored from __doc__
    """ icalvalue_compare(a:ICal.value, b:ICal.value) -> ICal.parameter_xliccomparetype """
    pass

def icalvalue_decode_ical_string(szText, szDecText, nMaxBufferLen): # real signature unknown; restored from __doc__
    """ icalvalue_decode_ical_string(szText:str, szDecText:str, nMaxBufferLen:int) -> int """
    return 0

def icalvalue_encode_ical_string(szText, szEncText, MaxBufferLen): # real signature unknown; restored from __doc__
    """ icalvalue_encode_ical_string(szText:str, szEncText:str, MaxBufferLen:int) -> int """
    return 0

def icalvalue_free(value): # real signature unknown; restored from __doc__
    """ icalvalue_free(value:ICal.value) """
    pass

def icalvalue_get_action(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_action(value:ICal.value) """
    pass

def icalvalue_get_binary(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_binary(value:ICal.value) -> str """
    return ""

def icalvalue_get_boolean(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_boolean(value:ICal.value) -> int """
    return 0

def icalvalue_get_busytype(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_busytype(value:ICal.value) """
    pass

def icalvalue_get_caladdress(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_caladdress(value:ICal.value) -> str """
    return ""

def icalvalue_get_carlevel(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_carlevel(value:ICal.value) """
    pass

def icalvalue_get_class(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_class(value:ICal.value) """
    pass

def icalvalue_get_cmd(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_cmd(value:ICal.value) """
    pass

def icalvalue_get_date(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_date(value:ICal.value) """
    pass

def icalvalue_get_datetime(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_datetime(value:ICal.value) """
    pass

def icalvalue_get_datetimedate(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_datetimedate(value:ICal.value) """
    pass

def icalvalue_get_datetimeperiod(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_datetimeperiod(value:ICal.value) """
    pass

def icalvalue_get_duration(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_duration(value:ICal.value) """
    pass

def icalvalue_get_float(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_float(value:ICal.value) -> float """
    return 0.0

def icalvalue_get_geo(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_geo(value:ICal.value) """
    pass

def icalvalue_get_integer(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_integer(value:ICal.value) -> int """
    return 0

def icalvalue_get_method(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_method(value:ICal.value) """
    pass

def icalvalue_get_period(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_period(value:ICal.value) """
    pass

def icalvalue_get_pollcompletion(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_pollcompletion(value:ICal.value) """
    pass

def icalvalue_get_pollmode(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_pollmode(value:ICal.value) """
    pass

def icalvalue_get_query(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_query(value:ICal.value) -> str """
    return ""

def icalvalue_get_querylevel(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_querylevel(value:ICal.value) """
    pass

def icalvalue_get_recur(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_recur(value:ICal.value) """
    pass

def icalvalue_get_requeststatus(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_requeststatus(value:ICal.value) """
    pass

def icalvalue_get_status(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_status(value:ICal.value) """
    pass

def icalvalue_get_string(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_string(value:ICal.value) -> str """
    return ""

def icalvalue_get_taskmode(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_taskmode(value:ICal.value) """
    pass

def icalvalue_get_text(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_text(value:ICal.value) -> str """
    return ""

def icalvalue_get_transp(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_transp(value:ICal.value) """
    pass

def icalvalue_get_trigger(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_trigger(value:ICal.value) """
    pass

def icalvalue_get_uri(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_uri(value:ICal.value) -> str """
    return ""

def icalvalue_get_utcoffset(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_utcoffset(value:ICal.value) -> int """
    return 0

def icalvalue_get_x(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_x(value:ICal.value) -> str """
    return ""

def icalvalue_get_xlicclass(value): # real signature unknown; restored from __doc__
    """ icalvalue_get_xlicclass(value:ICal.value) """
    pass

def icalvalue_isa(value): # real signature unknown; restored from __doc__
    """ icalvalue_isa(value:ICal.value) -> ICal.value_kind """
    pass

def icalvalue_isa_value(arg0=None): # real signature unknown; restored from __doc__
    """ icalvalue_isa_value(arg0=None) -> int """
    return 0

def icalvalue_is_valid(value): # real signature unknown; restored from __doc__
    """ icalvalue_is_valid(value:ICal.value) -> int """
    return 0

def icalvalue_kind_is_valid(kind): # real signature unknown; restored from __doc__
    """ icalvalue_kind_is_valid(kind:ICal.value_kind) -> int """
    return 0

def icalvalue_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ icalvalue_kind_to_string(kind:ICal.value_kind) -> str """
    return ""

def icalvalue_reset_kind(value): # real signature unknown; restored from __doc__
    """ icalvalue_reset_kind(value:ICal.value) """
    pass

def icalvalue_set_action(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_action(value:ICal.value, v=None) """
    pass

def icalvalue_set_attach(value, attach): # real signature unknown; restored from __doc__
    """ icalvalue_set_attach(value:ICal.value, attach:ICal.attach) """
    pass

def icalvalue_set_binary(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_binary(value:ICal.value, v:str) """
    pass

def icalvalue_set_boolean(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_boolean(value:ICal.value, v:int) """
    pass

def icalvalue_set_busytype(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_busytype(value:ICal.value, v=None) """
    pass

def icalvalue_set_caladdress(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_caladdress(value:ICal.value, v:str) """
    pass

def icalvalue_set_carlevel(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_carlevel(value:ICal.value, v=None) """
    pass

def icalvalue_set_class(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_class(value:ICal.value, v=None) """
    pass

def icalvalue_set_cmd(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_cmd(value:ICal.value, v=None) """
    pass

def icalvalue_set_date(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_date(value:ICal.value, v=None) """
    pass

def icalvalue_set_datetime(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_datetime(value:ICal.value, v=None) """
    pass

def icalvalue_set_datetimedate(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_datetimedate(value:ICal.value, v=None) """
    pass

def icalvalue_set_datetimeperiod(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_datetimeperiod(value:ICal.value, v=None) """
    pass

def icalvalue_set_duration(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_duration(value:ICal.value, v=None) """
    pass

def icalvalue_set_float(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_float(value:ICal.value, v:float) """
    pass

def icalvalue_set_geo(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_geo(value:ICal.value, v=None) """
    pass

def icalvalue_set_integer(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_integer(value:ICal.value, v:int) """
    pass

def icalvalue_set_method(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_method(value:ICal.value, v=None) """
    pass

def icalvalue_set_parent(value, property): # real signature unknown; restored from __doc__
    """ icalvalue_set_parent(value:ICal.value, property:ICal.property) """
    pass

def icalvalue_set_period(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_period(value:ICal.value, v=None) """
    pass

def icalvalue_set_pollcompletion(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_pollcompletion(value:ICal.value, v=None) """
    pass

def icalvalue_set_pollmode(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_pollmode(value:ICal.value, v=None) """
    pass

def icalvalue_set_query(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_query(value:ICal.value, v:str) """
    pass

def icalvalue_set_querylevel(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_querylevel(value:ICal.value, v=None) """
    pass

def icalvalue_set_recur(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_recur(value:ICal.value, v=None) """
    pass

def icalvalue_set_requeststatus(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_requeststatus(value:ICal.value, v=None) """
    pass

def icalvalue_set_status(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_status(value:ICal.value, v=None) """
    pass

def icalvalue_set_string(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_string(value:ICal.value, v:str) """
    pass

def icalvalue_set_taskmode(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_taskmode(value:ICal.value, v=None) """
    pass

def icalvalue_set_text(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_text(value:ICal.value, v:str) """
    pass

def icalvalue_set_transp(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_transp(value:ICal.value, v=None) """
    pass

def icalvalue_set_trigger(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_trigger(value:ICal.value, v=None) """
    pass

def icalvalue_set_uri(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_uri(value:ICal.value, v:str) """
    pass

def icalvalue_set_utcoffset(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_utcoffset(value:ICal.value, v:int) """
    pass

def icalvalue_set_x(value, v): # real signature unknown; restored from __doc__
    """ icalvalue_set_x(value:ICal.value, v:str) """
    pass

def icalvalue_set_xlicclass(value, v=None): # real signature unknown; restored from __doc__
    """ icalvalue_set_xlicclass(value:ICal.value, v=None) """
    pass

def icalvalue_string_to_kind(p_str): # real signature unknown; restored from __doc__
    """ icalvalue_string_to_kind(str:str) -> ICal.value_kind """
    pass

def print_datetime_to_string(p_str, data=None): # real signature unknown; restored from __doc__
    """ print_datetime_to_string(str:str, data=None) """
    pass

def print_date_to_string(p_str, data=None): # real signature unknown; restored from __doc__
    """ print_date_to_string(str:str, data=None) """
    pass

def pvl_clear(arg0): # real signature unknown; restored from __doc__
    """ pvl_clear(arg0:ICal.pvl_list) """
    pass

def pvl_count(arg0): # real signature unknown; restored from __doc__
    """ pvl_count(arg0:ICal.pvl_list) -> int """
    return 0

def pvl_data(arg0): # real signature unknown; restored from __doc__
    """ pvl_data(arg0:ICal.pvl_elem) """
    pass

def pvl_free(arg0): # real signature unknown; restored from __doc__
    """ pvl_free(arg0:ICal.pvl_list) """
    pass

def pvl_insert_after(l, e, d=None): # real signature unknown; restored from __doc__
    """ pvl_insert_after(l:ICal.pvl_list, e:ICal.pvl_elem, d=None) """
    pass

def pvl_insert_before(l, e, d=None): # real signature unknown; restored from __doc__
    """ pvl_insert_before(l:ICal.pvl_list, e:ICal.pvl_elem, d=None) """
    pass

def pvl_pop(l): # real signature unknown; restored from __doc__
    """ pvl_pop(l:ICal.pvl_list) """
    pass

def pvl_push(l, d=None): # real signature unknown; restored from __doc__
    """ pvl_push(l:ICal.pvl_list, d=None) """
    pass

def pvl_remove(arg0, arg1): # real signature unknown; restored from __doc__
    """ pvl_remove(arg0:ICal.pvl_list, arg1:ICal.pvl_elem) """
    pass

def pvl_shift(l): # real signature unknown; restored from __doc__
    """ pvl_shift(l:ICal.pvl_list) """
    pass

def pvl_unshift(l, d=None): # real signature unknown; restored from __doc__
    """ pvl_unshift(l:ICal.pvl_list, d=None) """
    pass

def set_unknown_token_handling_setting(newSetting): # real signature unknown; restored from __doc__
    """ set_unknown_token_handling_setting(newSetting:ICal._unknown_token_handling) """
    pass

def set_zone_directory(path): # real signature unknown; restored from __doc__
    """ set_zone_directory(path:str) """
    pass

def sspm_encoding_string(type=None): # real signature unknown; restored from __doc__
    """ sspm_encoding_string(type=None) -> str """
    return ""

def sspm_free_parts(parts=None, max_parts): # real signature unknown; restored from __doc__
    """ sspm_free_parts(parts=None, max_parts:int) """
    pass

def sspm_major_type_string(type=None): # real signature unknown; restored from __doc__
    """ sspm_major_type_string(type=None) -> str """
    return ""

def sspm_minor_type_string(type=None): # real signature unknown; restored from __doc__
    """ sspm_minor_type_string(type=None) -> str """
    return ""

def sspm_parse_mime(parts=None, max_parts, actions=None, get_string=None, get_string_data=None, first_header=None): # real signature unknown; restored from __doc__
    """ sspm_parse_mime(parts=None, max_parts:int, actions=None, get_string=None, get_string_data=None, first_header=None) -> int """
    return 0

def sspm_write_mime(parts=None, num_parts, output_string, header): # real signature unknown; restored from __doc__
    """ sspm_write_mime(parts=None, num_parts:int, output_string:str, header:str) -> int """
    return 0

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

from .array import array
from .attach import attach
from .compiter import compiter
from .component import component
from .component_kind import component_kind
from .datetimeperiodtype import datetimeperiodtype
from .durationtype import durationtype
from .errorenum import errorenum
from .errorstate import errorstate
from .geotype import geotype
from .parameter import parameter
from .parameter_action import parameter_action
from .parameter_cutype import parameter_cutype
from .parameter_display import parameter_display
from .parameter_enable import parameter_enable
from .parameter_encoding import parameter_encoding
from .parameter_fbtype import parameter_fbtype
from .parameter_feature import parameter_feature
from .parameter_kind import parameter_kind
from .parameter_local import parameter_local
from .parameter_partstat import parameter_partstat
from .parameter_patchaction import parameter_patchaction
from .parameter_range import parameter_range
from .parameter_related import parameter_related
from .parameter_reltype import parameter_reltype
from .parameter_required import parameter_required
from .parameter_role import parameter_role
from .parameter_rsvp import parameter_rsvp
from .parameter_scheduleagent import parameter_scheduleagent
from .parameter_scheduleforcesend import parameter_scheduleforcesend
from .parameter_stayinformed import parameter_stayinformed
from .parameter_substate import parameter_substate
from .parameter_value import parameter_value
from .parameter_xliccomparetype import parameter_xliccomparetype
from .parameter_xlicerrortype import parameter_xlicerrortype
from .parser import parser
from .parser_state import parser_state
from .periodtype import periodtype
from .property import property
from .property_action import property_action
from .property_busytype import property_busytype
from .property_carlevel import property_carlevel
from .property_class import property_class
from .property_cmd import property_cmd
from .property_kind import property_kind
from .property_method import property_method
from .property_pollcompletion import property_pollcompletion
from .property_pollmode import property_pollmode
from .property_querylevel import property_querylevel
from .property_status import property_status
from .property_taskmode import property_taskmode
from .property_transp import property_transp
from .property_xlicclass import property_xlicclass
from .pvl_elem import pvl_elem
from .pvl_elem_t import pvl_elem_t
from .pvl_list import pvl_list
from .recurrencetype import recurrencetype
from .recurrencetype_frequency import recurrencetype_frequency
from .recurrencetype_skip import recurrencetype_skip
from .recurrencetype_weekday import recurrencetype_weekday
from .recur_iterator import recur_iterator
from .reqstattype import reqstattype
from .requeststatus import requeststatus
from .restriction_kind import restriction_kind
from .sspm_action_map import sspm_action_map
from .sspm_header import sspm_header
from .sspm_part import sspm_part
from .timetype import timetype
from .timezone import timezone
from .timezonephase import timezonephase
from .timezonetype import timezonetype
from .time_span import time_span
from .triggertype import triggertype
from .value import value
from .value_kind import value_kind
from ._unknown_token_handling import _unknown_token_handling
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f384a972d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/ICal-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.ICal', loader=<gi.importer.DynamicImporter object at 0x7f384a972d00>)"

