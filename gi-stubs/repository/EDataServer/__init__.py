# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


# Variables with simple values

CLIENT_BACKEND_PROPERTY_CACHE_DIR = 'cache-dir'

CLIENT_BACKEND_PROPERTY_CAPABILITIES = 'capabilities'
CLIENT_BACKEND_PROPERTY_ONLINE = 'online'
CLIENT_BACKEND_PROPERTY_OPENED = 'opened'
CLIENT_BACKEND_PROPERTY_OPENING = 'opening'
CLIENT_BACKEND_PROPERTY_READONLY = 'readonly'
CLIENT_BACKEND_PROPERTY_REVISION = 'revision'

DEBUG_LOG_DOMAIN_CAL_QUERIES = 'CalQueries'

DEBUG_LOG_DOMAIN_GLOG = 'GLog'
DEBUG_LOG_DOMAIN_USER = 'USER'

EDS_MAJOR_VERSION = 3

EDS_MICRO_VERSION = 3

EDS_MINOR_VERSION = 36

NETWORK_MONITOR_ALWAYS_ONLINE_NAME = '"always-online"'

OAUTH2_SECRET_ACCESS_TOKEN = 'access_token'

OAUTH2_SECRET_EXPIRES_AFTER = 'expires_after'

OAUTH2_SECRET_REFRESH_TOKEN = 'refresh_token'

SOURCE_CREDENTIAL_PASSWORD = 'password'

SOURCE_CREDENTIAL_SSL_TRUST = 'ssl-trust'

SOURCE_CREDENTIAL_USERNAME = 'username'

SOURCE_EXTENSION_ADDRESS_BOOK = 'Address Book'

SOURCE_EXTENSION_ALARMS = 'Alarms'
SOURCE_EXTENSION_AUTHENTICATION = 'Authentication'
SOURCE_EXTENSION_AUTOCOMPLETE = 'Autocomplete'
SOURCE_EXTENSION_AUTOCONFIG = 'Autoconfig'
SOURCE_EXTENSION_CALENDAR = 'Calendar'
SOURCE_EXTENSION_COLLECTION = 'Collection'

SOURCE_EXTENSION_CONTACTS_BACKEND = 'Contacts Backend'

SOURCE_EXTENSION_GOA = 'GNOME Online Accounts'

SOURCE_EXTENSION_LDAP_BACKEND = 'LDAP Backend'

SOURCE_EXTENSION_LOCAL_BACKEND = 'Local Backend'

SOURCE_EXTENSION_MAIL_ACCOUNT = 'Mail Account'
SOURCE_EXTENSION_MAIL_COMPOSITION = 'Mail Composition'
SOURCE_EXTENSION_MAIL_IDENTITY = 'Mail Identity'
SOURCE_EXTENSION_MAIL_SIGNATURE = 'Mail Signature'
SOURCE_EXTENSION_MAIL_SUBMISSION = 'Mail Submission'
SOURCE_EXTENSION_MAIL_TRANSPORT = 'Mail Transport'

SOURCE_EXTENSION_MDN = 'Message Disposition Notifications'

SOURCE_EXTENSION_MEMO_LIST = 'Memo List'

SOURCE_EXTENSION_OFFLINE = 'Offline'
SOURCE_EXTENSION_OPENPGP = 'Pretty Good Privacy (OpenPGP)'
SOURCE_EXTENSION_PROXY = 'Proxy'
SOURCE_EXTENSION_REFRESH = 'Refresh'
SOURCE_EXTENSION_RESOURCE = 'Resource'

SOURCE_EXTENSION_REVISION_GUARDS = 'Revision Guards'

SOURCE_EXTENSION_SECURITY = 'Security'
SOURCE_EXTENSION_SMIME = 'Secure MIME (S/MIME)'

SOURCE_EXTENSION_TASK_LIST = 'Task List'

SOURCE_EXTENSION_UOA = 'Ubuntu Online Accounts'

SOURCE_EXTENSION_WEATHER_BACKEND = 'Weather Backend'

SOURCE_EXTENSION_WEBDAV_BACKEND = 'WebDAV Backend'

SOURCE_PARAM_SETTING = 1

WEBDAV_CAPABILITY_ACCESS_CONTROL = 'access-control'

WEBDAV_CAPABILITY_ADDRESSBOOK = 'addressbook'
WEBDAV_CAPABILITY_BIND = 'bind'

WEBDAV_CAPABILITY_CALENDAR_ACCESS = 'calendar-access'

WEBDAV_CAPABILITY_CALENDAR_AUTO_SCHEDULE = 'calendar-auto-schedule'

WEBDAV_CAPABILITY_CALENDAR_PROXY = 'calendar-proxy'
WEBDAV_CAPABILITY_CALENDAR_SCHEDULE = 'calendar-schedule'

WEBDAV_CAPABILITY_CLASS_1 = '1'
WEBDAV_CAPABILITY_CLASS_2 = '2'
WEBDAV_CAPABILITY_CLASS_3 = '3'

WEBDAV_CAPABILITY_EXTENDED_MKCOL = 'extended-mkcol'

WEBDAV_COLLATION_ASCII_CASEMAP = 'i;'

WEBDAV_COLLATION_ASCII_CASEMAP_SUFFIX = 'ascii-casemap'

WEBDAV_COLLATION_ASCII_NUMERIC = 'i;'

WEBDAV_COLLATION_ASCII_NUMERIC_SUFFIX = 'ascii-numeric'

WEBDAV_COLLATION_OCTET = 'i;'

WEBDAV_COLLATION_OCTET_SUFFIX = 'octet'

WEBDAV_COLLATION_UNICODE_CASEMAP = 'i;'

WEBDAV_COLLATION_UNICODE_CASEMAP_SUFFIX = 'unicode-casemap'

WEBDAV_CONTENT_TYPE_CALENDAR = 'text/calendar; charset="utf-8"'
WEBDAV_CONTENT_TYPE_VCARD = 'text/vcard; charset="utf-8"'
WEBDAV_CONTENT_TYPE_XML = 'application/xml; charset="utf-8"'

WEBDAV_DEPTH_INFINITY = 'infinity'
WEBDAV_DEPTH_THIS = '0'

WEBDAV_DEPTH_THIS_AND_CHILDREN = '1'

WEBDAV_NS_CALDAV = 'urn:ietf:params:xml:ns:caldav'
WEBDAV_NS_CALENDARSERVER = 'http://calendarserver.org/ns/'
WEBDAV_NS_CARDDAV = 'urn:ietf:params:xml:ns:carddav'
WEBDAV_NS_DAV = 'DAV:'
WEBDAV_NS_ICAL = 'http://apple.com/ns/ical/'

_namespace = 'EDataServer'

_version = '1.2'

__weakref__ = None

# functions

def binding_bind_property(source, source_property, target, target_property, flags): # real signature unknown; restored from __doc__
    """ binding_bind_property(source:GObject.Object, source_property:str, target:GObject.Object, target_property:str, flags:GObject.BindingFlags) -> GObject.Binding """
    pass

def binding_bind_property_full(source, source_property, target, target_property, flags, transform_to, transform_from): # real signature unknown; restored from __doc__
    """ binding_bind_property_full(source:GObject.Object, source_property:str, target:GObject.Object, target_property:str, flags:GObject.BindingFlags, transform_to:GObject.Closure, transform_from:GObject.Closure) -> GObject.Binding """
    pass

def binding_transform_enum_nick_to_value(binding, source_value, target_value, not_used=None): # real signature unknown; restored from __doc__
    """ binding_transform_enum_nick_to_value(binding:GObject.Binding, source_value:GObject.Value, target_value:GObject.Value, not_used=None) -> bool """
    return False

def binding_transform_enum_value_to_nick(binding, source_value, target_value, not_used=None): # real signature unknown; restored from __doc__
    """ binding_transform_enum_value_to_nick(binding:GObject.Binding, source_value:GObject.Value, target_value:GObject.Value, not_used=None) -> bool """
    return False

def categories_add(category, unused, icon_file, searchable): # real signature unknown; restored from __doc__
    """ categories_add(category:str, unused:str, icon_file:str, searchable:bool) """
    pass

def categories_dup_icon_file_for(category): # real signature unknown; restored from __doc__
    """ categories_dup_icon_file_for(category:str) -> str """
    return ""

def categories_dup_list(): # real signature unknown; restored from __doc__
    """ categories_dup_list() -> list """
    return []

def categories_exist(category): # real signature unknown; restored from __doc__
    """ categories_exist(category:str) -> bool """
    return False

def categories_get_icon_file_for(category): # real signature unknown; restored from __doc__
    """ categories_get_icon_file_for(category:str) -> str """
    return ""

def categories_get_list(): # real signature unknown; restored from __doc__
    """ categories_get_list() -> list """
    return []

def categories_is_searchable(category): # real signature unknown; restored from __doc__
    """ categories_is_searchable(category:str) -> bool """
    return False

def categories_register_change_listener(listener, user_data=None): # real signature unknown; restored from __doc__
    """ categories_register_change_listener(listener:GObject.Callback, user_data=None) """
    pass

def categories_remove(category): # real signature unknown; restored from __doc__
    """ categories_remove(category:str) """
    pass

def categories_set_icon_file_for(category, icon_file): # real signature unknown; restored from __doc__
    """ categories_set_icon_file_for(category:str, icon_file:str) """
    pass

def categories_unregister_change_listener(listener, user_data=None): # real signature unknown; restored from __doc__
    """ categories_unregister_change_listener(listener:GObject.Callback, user_data=None) """
    pass

def collator_error_quark(): # real signature unknown; restored from __doc__
    """ collator_error_quark() -> int """
    return 0

def data_server_util_get_dbus_call_timeout(): # real signature unknown; restored from __doc__
    """ data_server_util_get_dbus_call_timeout() -> int """
    return 0

def data_server_util_set_dbus_call_timeout(timeout_msec): # real signature unknown; restored from __doc__
    """ data_server_util_set_dbus_call_timeout(timeout_msec:int) """
    pass

def debug_log_clear(): # real signature unknown; restored from __doc__
    """ debug_log_clear() """
    pass

def debug_log_disable_domains(domains): # real signature unknown; restored from __doc__
    """ debug_log_disable_domains(domains:list) """
    pass

def debug_log_dump(filename): # real signature unknown; restored from __doc__
    """ debug_log_dump(filename:str) -> bool """
    return False

def debug_log_dump_to_dated_file(): # real signature unknown; restored from __doc__
    """ debug_log_dump_to_dated_file() -> bool """
    return False

def debug_log_enable_domains(domains): # real signature unknown; restored from __doc__
    """ debug_log_enable_domains(domains:list) """
    pass

def debug_log_get_max_lines(): # real signature unknown; restored from __doc__
    """ debug_log_get_max_lines() -> int """
    return 0

def debug_log_is_domain_enabled(domain): # real signature unknown; restored from __doc__
    """ debug_log_is_domain_enabled(domain:str) -> bool """
    return False

def debug_log_load_configuration(filename): # real signature unknown; restored from __doc__
    """ debug_log_load_configuration(filename:str) -> bool """
    return False

def debug_log_set_max_lines(num_lines): # real signature unknown; restored from __doc__
    """ debug_log_set_max_lines(num_lines:int) """
    pass

def eds_check_version(required_major, required_minor, required_micro): # real signature unknown; restored from __doc__
    """ eds_check_version(required_major:int, required_minor:int, required_micro:int) -> str """
    return ""

def enum_from_string(enum_type, string, enum_value): # real signature unknown; restored from __doc__
    """ enum_from_string(enum_type:GType, string:str, enum_value:int) -> bool """
    return False

def enum_to_string(enum_type, enum_value): # real signature unknown; restored from __doc__
    """ enum_to_string(enum_type:GType, enum_value:int) -> str """
    return ""

def filename_make_safe(string): # real signature unknown; restored from __doc__
    """ filename_make_safe(string:str) """
    pass

def filename_mkdir_encoded(basepath, fileprefix, filename, fileindex): # real signature unknown; restored from __doc__
    """ filename_mkdir_encoded(basepath:str, fileprefix:str, filename:str, fileindex:int) -> str """
    return ""

def file_recursive_delete(file, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ file_recursive_delete(file:Gio.File, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def file_recursive_delete_finish(file, result): # real signature unknown; restored from __doc__
    """ file_recursive_delete_finish(file:Gio.File, result:Gio.AsyncResult) -> bool """
    return False

def file_recursive_delete_sync(file, cancellable=None): # real signature unknown; restored from __doc__
    """ file_recursive_delete_sync(file:Gio.File, cancellable:Gio.Cancellable=None) -> bool """
    return False

def free_form_exp_to_sexp(free_form_exp, symbols): # real signature unknown; restored from __doc__
    """ free_form_exp_to_sexp(free_form_exp:str, symbols:EDataServer.FreeFormExpSymbol) -> str """
    return ""

def get_user_cache_dir(): # real signature unknown; restored from __doc__
    """ get_user_cache_dir() -> str """
    return ""

def get_user_config_dir(): # real signature unknown; restored from __doc__
    """ get_user_config_dir() -> str """
    return ""

def get_user_data_dir(): # real signature unknown; restored from __doc__
    """ get_user_data_dir() -> str """
    return ""

def localtime_with_offset(tt, tm=None, offset): # real signature unknown; restored from __doc__
    """ localtime_with_offset(tt:int, tm=None, offset:int) """
    pass

def mktime_utc(tm=None): # real signature unknown; restored from __doc__
    """ mktime_utc(tm=None) -> int """
    return 0

def oauth2_service_util_set_to_form(form, name, value=None): # real signature unknown; restored from __doc__
    """ oauth2_service_util_set_to_form(form:dict, name:str, value:str=None) """
    pass

def oauth2_service_util_take_to_form(form, name, value=None): # real signature unknown; restored from __doc__
    """ oauth2_service_util_take_to_form(form:dict, name:str, value:str=None) """
    pass

def queue_transfer(src_queue, dst_queue): # real signature unknown; restored from __doc__
    """ queue_transfer(src_queue:GLib.Queue, dst_queue:GLib.Queue) """
    pass

def secret_store_delete_sync(uid, cancellable=None): # real signature unknown; restored from __doc__
    """ secret_store_delete_sync(uid:str, cancellable:Gio.Cancellable=None) -> bool """
    return False

def secret_store_lookup_sync(uid, cancellable=None): # real signature unknown; restored from __doc__
    """ secret_store_lookup_sync(uid:str, cancellable:Gio.Cancellable=None) -> bool, out_secret:str """
    return False

def secret_store_store_sync(uid, secret, label, permanently, cancellable=None): # real signature unknown; restored from __doc__
    """ secret_store_store_sync(uid:str, secret:str, label:str, permanently:bool, cancellable:Gio.Cancellable=None) -> bool """
    return False

def soup_ssl_trust_connect(soup_message, source): # real signature unknown; restored from __doc__
    """ soup_ssl_trust_connect(soup_message:Soup.Message, source:EDataServer.Source) """
    pass

def strftime(string, max, fmt, tm=None): # real signature unknown; restored from __doc__
    """ strftime(string:str, max:int, fmt:str, tm=None) -> int """
    return 0

def timeout_add_seconds_with_name(priority, interval, name=None, function, data=None): # real signature unknown; restored from __doc__
    """ timeout_add_seconds_with_name(priority:int, interval:int, name:str=None, function:GLib.SourceFunc, data=None) -> int """
    return 0

def timeout_add_with_name(priority, interval, name=None, function, data=None): # real signature unknown; restored from __doc__
    """ timeout_add_with_name(priority:int, interval:int, name:str=None, function:GLib.SourceFunc, data=None) -> int """
    return 0

def time_format_date_and_time(date_tm=None, use_24_hour_format, show_midnight, show_zero_seconds, buffer, buffer_size): # real signature unknown; restored from __doc__
    """ time_format_date_and_time(date_tm=None, use_24_hour_format:bool, show_midnight:bool, show_zero_seconds:bool, buffer:str, buffer_size:int) """
    pass

def time_format_time(date_tm=None, use_24_hour_format, show_zero_seconds, buffer, buffer_size): # real signature unknown; restored from __doc__
    """ time_format_time(date_tm=None, use_24_hour_format:bool, show_zero_seconds:bool, buffer:str, buffer_size:int) """
    pass

def time_get_d_fmt_with_4digit_year(): # real signature unknown; restored from __doc__
    """ time_get_d_fmt_with_4digit_year() -> str """
    return ""

def time_parse_date(value, result=None): # real signature unknown; restored from __doc__
    """ time_parse_date(value:str, result=None) -> EDataServer.TimeParseStatus """
    pass

def time_parse_date_and_time(value, result=None): # real signature unknown; restored from __doc__
    """ time_parse_date_and_time(value:str, result=None) -> EDataServer.TimeParseStatus """
    pass

def time_parse_date_and_time_ex(value, result=None, two_digit_year): # real signature unknown; restored from __doc__
    """ time_parse_date_and_time_ex(value:str, result=None, two_digit_year:bool) -> EDataServer.TimeParseStatus """
    pass

def time_parse_date_ex(value, result=None, two_digit_year): # real signature unknown; restored from __doc__
    """ time_parse_date_ex(value:str, result=None, two_digit_year:bool) -> EDataServer.TimeParseStatus """
    pass

def time_parse_time(value, result=None): # real signature unknown; restored from __doc__
    """ time_parse_time(value:str, result=None) -> EDataServer.TimeParseStatus """
    pass

def type_traverse(parent_type, func, user_data=None): # real signature unknown; restored from __doc__
    """ type_traverse(parent_type:GType, func:EDataServer.TypeFunc, user_data=None) """
    pass

def uid_new(): # real signature unknown; restored from __doc__
    """ uid_new() -> str """
    return ""

def utf8_strftime(string, max, fmt, tm=None): # real signature unknown; restored from __doc__
    """ utf8_strftime(string:str, max:int, fmt:str, tm=None) -> int """
    return 0

def util_can_use_collection_as_credential_source(collection_source=None, child_source=None): # real signature unknown; restored from __doc__
    """ util_can_use_collection_as_credential_source(collection_source=None, child_source=None) -> bool """
    return False

def util_copy_object_slist(copy_to=None, objects): # real signature unknown; restored from __doc__
    """ util_copy_object_slist(copy_to:list=None, objects:list) -> list """
    return []

def util_copy_string_slist(copy_to=None, strings): # real signature unknown; restored from __doc__
    """ util_copy_string_slist(copy_to:list=None, strings:list) -> list """
    return []

def util_ensure_gdbus_string(p_str, gdbus_str): # real signature unknown; restored from __doc__
    """ util_ensure_gdbus_string(str:str, gdbus_str:str) -> str """
    return ""

def util_free_nullable_object_slist(objects): # real signature unknown; restored from __doc__
    """ util_free_nullable_object_slist(objects:list) """
    pass

def util_free_object_slist(objects): # real signature unknown; restored from __doc__
    """ util_free_object_slist(objects:list) """
    pass

def util_free_string_slist(strings): # real signature unknown; restored from __doc__
    """ util_free_string_slist(strings:list) """
    pass

def util_generate_uid(): # real signature unknown; restored from __doc__
    """ util_generate_uid() -> str """
    return ""

def util_get_source_full_name(registry=None, source=None): # real signature unknown; restored from __doc__
    """ util_get_source_full_name(registry=None, source=None) -> str """
    return ""

def util_gthread_id(thread): # real signature unknown; restored from __doc__
    """ util_gthread_id(thread:GLib.Thread) -> int """
    return 0

def util_identity_can_send(registry=None, identity_source=None): # real signature unknown; restored from __doc__
    """ util_identity_can_send(registry=None, identity_source=None) -> bool """
    return False

def util_safe_free_string(p_str): # real signature unknown; restored from __doc__
    """ util_safe_free_string(str:str) """
    pass

def util_slist_to_strv(strings): # real signature unknown; restored from __doc__
    """ util_slist_to_strv(strings:list) -> list """
    return []

def util_strcmp0(str1, str2): # real signature unknown; restored from __doc__
    """ util_strcmp0(str1:str, str2:str) -> int """
    return 0

def util_strdup_strip(string=None): # real signature unknown; restored from __doc__
    """ util_strdup_strip(string:str=None) -> str """
    return ""

def util_strstrcase(haystack, needle): # real signature unknown; restored from __doc__
    """ util_strstrcase(haystack:str, needle:str) -> str """
    return ""

def util_strv_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ util_strv_equal(v1=None, v2=None) -> bool """
    return False

def util_strv_to_slist(strv): # real signature unknown; restored from __doc__
    """ util_strv_to_slist(strv:str) -> list """
    return []

def util_unicode_get_utf8(text, out): # real signature unknown; restored from __doc__
    """ util_unicode_get_utf8(text:str, out:str) -> str """
    return ""

def util_unref_in_thread(p_object=None): # real signature unknown; restored from __doc__
    """ util_unref_in_thread(object=None) """
    pass

def util_utf8_data_make_valid(data, data_bytes): # real signature unknown; restored from __doc__
    """ util_utf8_data_make_valid(data:str, data_bytes:int) -> str """
    return ""

def util_utf8_decompose(text): # real signature unknown; restored from __doc__
    """ util_utf8_decompose(text:str) -> str """
    return ""

def util_utf8_make_valid(p_str): # real signature unknown; restored from __doc__
    """ util_utf8_make_valid(str:str) -> str """
    return ""

def util_utf8_normalize(p_str): # real signature unknown; restored from __doc__
    """ util_utf8_normalize(str:str) -> str """
    return ""

def util_utf8_remove_accents(p_str): # real signature unknown; restored from __doc__
    """ util_utf8_remove_accents(str:str) -> str """
    return ""

def util_utf8_strcasecmp(s1, s2): # real signature unknown; restored from __doc__
    """ util_utf8_strcasecmp(s1:str, s2:str) -> int """
    return 0

def util_utf8_strstrcase(haystack, needle): # real signature unknown; restored from __doc__
    """ util_utf8_strstrcase(haystack:str, needle:str) -> str """
    return ""

def util_utf8_strstrcasedecomp(haystack, needle): # real signature unknown; restored from __doc__
    """ util_utf8_strstrcasedecomp(haystack:str, needle:str) -> str """
    return ""

def webdav_access_control_entry_free(ptr=None): # real signature unknown; restored from __doc__
    """ webdav_access_control_entry_free(ptr=None) """
    pass

def webdav_discover_free_discovered_sources(discovered_sources): # real signature unknown; restored from __doc__
    """ webdav_discover_free_discovered_sources(discovered_sources:list) """
    pass

def webdav_discover_sources(source, url_use_path=None, only_supports, credentials=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ webdav_discover_sources(source:EDataServer.Source, url_use_path:str=None, only_supports:int, credentials:EDataServer.NamedParameters=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def webdav_discover_sources_finish(source, result): # real signature unknown; restored from __doc__
    """ webdav_discover_sources_finish(source:EDataServer.Source, result:Gio.AsyncResult) -> bool, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, out_discovered_sources:list, out_calendar_user_addresses:list """
    return False

def webdav_discover_sources_full(source, url_use_path=None, only_supports, credentials=None, ref_source_func=None, ref_source_func_user_data=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ webdav_discover_sources_full(source:EDataServer.Source, url_use_path:str=None, only_supports:int, credentials:EDataServer.NamedParameters=None, ref_source_func:EDataServer.WebDAVDiscoverRefSourceFunc=None, ref_source_func_user_data=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def webdav_discover_sources_full_sync(source, url_use_path=None, only_supports, credentials=None, ref_source_func=None, ref_source_func_user_data=None, cancellable=None): # real signature unknown; restored from __doc__
    """ webdav_discover_sources_full_sync(source:EDataServer.Source, url_use_path:str=None, only_supports:int, credentials:EDataServer.NamedParameters=None, ref_source_func:EDataServer.WebDAVDiscoverRefSourceFunc=None, ref_source_func_user_data=None, cancellable:Gio.Cancellable=None) -> bool, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, out_discovered_sources:list, out_calendar_user_addresses:list """
    return False

def webdav_discover_sources_sync(source, url_use_path=None, only_supports, credentials=None, cancellable=None): # real signature unknown; restored from __doc__
    """ webdav_discover_sources_sync(source:EDataServer.Source, url_use_path:str=None, only_supports:int, credentials:EDataServer.NamedParameters=None, cancellable:Gio.Cancellable=None) -> bool, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, out_discovered_sources:list, out_calendar_user_addresses:list """
    return False

def webdav_privilege_free(ptr=None): # real signature unknown; restored from __doc__
    """ webdav_privilege_free(ptr=None) """
    pass

def webdav_property_change_free(ptr=None): # real signature unknown; restored from __doc__
    """ webdav_property_change_free(ptr=None) """
    pass

def webdav_resource_free(ptr=None): # real signature unknown; restored from __doc__
    """ webdav_resource_free(ptr=None) """
    pass

def xmlhash_add(hash, key, data): # real signature unknown; restored from __doc__
    """ xmlhash_add(hash:EDataServer.XmlHash, key:str, data:str) """
    pass

def xmlhash_compare(hash, key, compare_data): # real signature unknown; restored from __doc__
    """ xmlhash_compare(hash:EDataServer.XmlHash, key:str, compare_data:str) -> EDataServer.XmlHashStatus """
    pass

def xmlhash_destroy(hash): # real signature unknown; restored from __doc__
    """ xmlhash_destroy(hash:EDataServer.XmlHash) """
    pass

def xmlhash_foreach_key(hash, func, user_data=None): # real signature unknown; restored from __doc__
    """ xmlhash_foreach_key(hash:EDataServer.XmlHash, func:EDataServer.XmlHashFunc, user_data=None) """
    pass

def xmlhash_foreach_key_remove(hash, func, user_data=None): # real signature unknown; restored from __doc__
    """ xmlhash_foreach_key_remove(hash:EDataServer.XmlHash, func:EDataServer.XmlHashRemoveFunc, user_data=None) """
    pass

def xmlhash_remove(hash, key): # real signature unknown; restored from __doc__
    """ xmlhash_remove(hash:EDataServer.XmlHash, key:str) """
    pass

def xmlhash_write(hash): # real signature unknown; restored from __doc__
    """ xmlhash_write(hash:EDataServer.XmlHash) """
    pass

def xml_destroy_hash(hash): # real signature unknown; restored from __doc__
    """ xml_destroy_hash(hash:dict) """
    pass

def xml_save_file(filename, doc): # real signature unknown; restored from __doc__
    """ xml_save_file(filename:str, doc:libxml2.Doc) -> int """
    return 0

def xml_to_hash(doc, type): # real signature unknown; restored from __doc__
    """ xml_to_hash(doc:libxml2.Doc, type:EDataServer.XmlHashType) -> dict """
    return {}

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

from .AsyncClosure import AsyncClosure
from .Client import Client
from .ClientClass import ClientClass
from .ClientError import ClientError
from .ClientErrorsList import ClientErrorsList
from .ClientPrivate import ClientPrivate
from .Collator import Collator
from .CollatorError import CollatorError
from .ConflictResolution import ConflictResolution
from .Extensible import Extensible
from .ExtensibleInterface import ExtensibleInterface
from .Extension import Extension
from .ExtensionClass import ExtensionClass
from .ExtensionPrivate import ExtensionPrivate
from .Flag import Flag
from .FreeFormExpSymbol import FreeFormExpSymbol
from .GDataOAuth2Authorizer import GDataOAuth2Authorizer
from .GDataOAuth2AuthorizerClass import GDataOAuth2AuthorizerClass
from .GDataOAuth2AuthorizerPrivate import GDataOAuth2AuthorizerPrivate
from .MdnResponsePolicy import MdnResponsePolicy
from .MemChunk import MemChunk
from .Module import Module
from .ModuleClass import ModuleClass
from .ModulePrivate import ModulePrivate
from .NamedParameters import NamedParameters
from .NetworkMonitor import NetworkMonitor
from .NetworkMonitorClass import NetworkMonitorClass
from .NetworkMonitorPrivate import NetworkMonitorPrivate
from .OAuth2Service import OAuth2Service
from .OAuth2ServiceBase import OAuth2ServiceBase
from .OAuth2ServiceBaseClass import OAuth2ServiceBaseClass
from .OAuth2ServiceFlags import OAuth2ServiceFlags
from .OAuth2ServiceGoogle import OAuth2ServiceGoogle
from .OAuth2ServiceGoogleClass import OAuth2ServiceGoogleClass
from .OAuth2ServiceInterface import OAuth2ServiceInterface
from .OAuth2ServiceNavigationPolicy import OAuth2ServiceNavigationPolicy
from .OAuth2ServiceOutlook import OAuth2ServiceOutlook
from .OAuth2ServiceOutlookClass import OAuth2ServiceOutlookClass
from .OAuth2Services import OAuth2Services
from .OAuth2ServicesClass import OAuth2ServicesClass
from .OAuth2ServicesPrivate import OAuth2ServicesPrivate
from .OperationPool import OperationPool
from .ProxyMethod import ProxyMethod
from .SoupAuthBearer import SoupAuthBearer
from .SoupAuthBearerClass import SoupAuthBearerClass
from .SoupAuthBearerPrivate import SoupAuthBearerPrivate
from .SoupSession import SoupSession
from .SoupSessionClass import SoupSessionClass
from .SoupSessionPrivate import SoupSessionPrivate
from .Source import Source
from .SourceExtension import SourceExtension
from .SourceBackend import SourceBackend
from .SourceAddressBook import SourceAddressBook
from .SourceAddressBookClass import SourceAddressBookClass
from .SourceAddressBookPrivate import SourceAddressBookPrivate
from .SourceAlarms import SourceAlarms
from .SourceAlarmsClass import SourceAlarmsClass
from .SourceAlarmsPrivate import SourceAlarmsPrivate
from .SourceAuthentication import SourceAuthentication
from .SourceAuthenticationClass import SourceAuthenticationClass
from .SourceAuthenticationPrivate import SourceAuthenticationPrivate
from .SourceAuthenticationResult import SourceAuthenticationResult
from .SourceAutocomplete import SourceAutocomplete
from .SourceAutocompleteClass import SourceAutocompleteClass
from .SourceAutocompletePrivate import SourceAutocompletePrivate
from .SourceAutoconfig import SourceAutoconfig
from .SourceAutoconfigClass import SourceAutoconfigClass
from .SourceAutoconfigPrivate import SourceAutoconfigPrivate
from .SourceBackendClass import SourceBackendClass
from .SourceBackendPrivate import SourceBackendPrivate
from .SourceSelectable import SourceSelectable
from .SourceCalendar import SourceCalendar
from .SourceCalendarClass import SourceCalendarClass
from .SourceCalendarPrivate import SourceCalendarPrivate
from .SourceCamel import SourceCamel
from .SourceCamelClass import SourceCamelClass
from .SourceCamelPrivate import SourceCamelPrivate
from .SourceClass import SourceClass
from .SourceCollection import SourceCollection
from .SourceCollectionClass import SourceCollectionClass
from .SourceCollectionPrivate import SourceCollectionPrivate
from .SourceConnectionStatus import SourceConnectionStatus
from .SourceContacts import SourceContacts
from .SourceContactsClass import SourceContactsClass
from .SourceContactsPrivate import SourceContactsPrivate
from .SourceCredentialsProvider import SourceCredentialsProvider
from .SourceCredentialsProviderClass import SourceCredentialsProviderClass
from .SourceCredentialsProviderImpl import SourceCredentialsProviderImpl
from .SourceCredentialsProviderImplClass import SourceCredentialsProviderImplClass
from .SourceCredentialsProviderImplOAuth2 import SourceCredentialsProviderImplOAuth2
from .SourceCredentialsProviderImplOAuth2Class import SourceCredentialsProviderImplOAuth2Class
from .SourceCredentialsProviderImplOAuth2Private import SourceCredentialsProviderImplOAuth2Private
from .SourceCredentialsProviderImplPassword import SourceCredentialsProviderImplPassword
from .SourceCredentialsProviderImplPasswordClass import SourceCredentialsProviderImplPasswordClass
from .SourceCredentialsProviderImplPasswordPrivate import SourceCredentialsProviderImplPasswordPrivate
from .SourceCredentialsProviderImplPrivate import SourceCredentialsProviderImplPrivate
from .SourceCredentialsProviderPrivate import SourceCredentialsProviderPrivate
from .SourceCredentialsReason import SourceCredentialsReason
from .SourceExtensionClass import SourceExtensionClass
from .SourceExtensionPrivate import SourceExtensionPrivate
from .SourceGoa import SourceGoa
from .SourceGoaClass import SourceGoaClass
from .SourceGoaPrivate import SourceGoaPrivate
from .SourceLDAP import SourceLDAP
from .SourceLDAPAuthentication import SourceLDAPAuthentication
from .SourceLDAPClass import SourceLDAPClass
from .SourceLDAPPrivate import SourceLDAPPrivate
from .SourceLDAPScope import SourceLDAPScope
from .SourceLDAPSecurity import SourceLDAPSecurity
from .SourceLocal import SourceLocal
from .SourceLocalClass import SourceLocalClass
from .SourceLocalPrivate import SourceLocalPrivate
from .SourceMailAccount import SourceMailAccount
from .SourceMailAccountClass import SourceMailAccountClass
from .SourceMailAccountPrivate import SourceMailAccountPrivate
from .SourceMailComposition import SourceMailComposition
from .SourceMailCompositionClass import SourceMailCompositionClass
from .SourceMailCompositionPrivate import SourceMailCompositionPrivate
from .SourceMailCompositionReplyStyle import SourceMailCompositionReplyStyle
from .SourceMailIdentity import SourceMailIdentity
from .SourceMailIdentityClass import SourceMailIdentityClass
from .SourceMailIdentityPrivate import SourceMailIdentityPrivate
from .SourceMailSignature import SourceMailSignature
from .SourceMailSignatureClass import SourceMailSignatureClass
from .SourceMailSignaturePrivate import SourceMailSignaturePrivate
from .SourceMailSubmission import SourceMailSubmission
from .SourceMailSubmissionClass import SourceMailSubmissionClass
from .SourceMailSubmissionPrivate import SourceMailSubmissionPrivate
from .SourceMailTransport import SourceMailTransport
from .SourceMailTransportClass import SourceMailTransportClass
from .SourceMailTransportPrivate import SourceMailTransportPrivate
from .SourceMDN import SourceMDN
from .SourceMDNClass import SourceMDNClass
from .SourceMDNPrivate import SourceMDNPrivate
from .SourceMemoList import SourceMemoList
from .SourceMemoListClass import SourceMemoListClass
from .SourceMemoListPrivate import SourceMemoListPrivate
from .SourceOffline import SourceOffline
from .SourceOfflineClass import SourceOfflineClass
from .SourceOfflinePrivate import SourceOfflinePrivate
from .SourceOpenPGP import SourceOpenPGP
from .SourceOpenPGPClass import SourceOpenPGPClass
from .SourceOpenPGPPrivate import SourceOpenPGPPrivate
from .SourcePrivate import SourcePrivate
from .SourceProxy import SourceProxy
from .SourceProxyClass import SourceProxyClass
from .SourceProxyPrivate import SourceProxyPrivate
from .SourceRefresh import SourceRefresh
from .SourceRefreshClass import SourceRefreshClass
from .SourceRefreshPrivate import SourceRefreshPrivate
from .SourceRegistry import SourceRegistry
from .SourceRegistryClass import SourceRegistryClass
from .SourceRegistryPrivate import SourceRegistryPrivate
from .SourceRegistryWatcher import SourceRegistryWatcher
from .SourceRegistryWatcherClass import SourceRegistryWatcherClass
from .SourceRegistryWatcherPrivate import SourceRegistryWatcherPrivate
from .SourceResource import SourceResource
from .SourceResourceClass import SourceResourceClass
from .SourceResourcePrivate import SourceResourcePrivate
from .SourceRevisionGuards import SourceRevisionGuards
from .SourceRevisionGuardsClass import SourceRevisionGuardsClass
from .SourceRevisionGuardsPrivate import SourceRevisionGuardsPrivate
from .SourceSecurity import SourceSecurity
from .SourceSecurityClass import SourceSecurityClass
from .SourceSecurityPrivate import SourceSecurityPrivate
from .SourceSelectableClass import SourceSelectableClass
from .SourceSelectablePrivate import SourceSelectablePrivate
from .SourceSMIME import SourceSMIME
from .SourceSMIMEClass import SourceSMIMEClass
from .SourceSMIMEPrivate import SourceSMIMEPrivate
from .SourceTaskList import SourceTaskList
from .SourceTaskListClass import SourceTaskListClass
from .SourceTaskListPrivate import SourceTaskListPrivate
from .SourceUoa import SourceUoa
from .SourceUoaClass import SourceUoaClass
from .SourceUoaPrivate import SourceUoaPrivate
from .SourceWeather import SourceWeather
from .SourceWeatherClass import SourceWeatherClass
from .SourceWeatherPrivate import SourceWeatherPrivate
from .SourceWeatherUnits import SourceWeatherUnits
from .SourceWebdav import SourceWebdav
from .SourceWebdavClass import SourceWebdavClass
from .SourceWebdavPrivate import SourceWebdavPrivate
from .ThreeState import ThreeState
from .TimeParseStatus import TimeParseStatus
from .TrustPromptResponse import TrustPromptResponse
from .WebDAVAccessControlEntry import WebDAVAccessControlEntry
from .WebDAVACEFlag import WebDAVACEFlag
from .WebDAVACEPrincipalKind import WebDAVACEPrincipalKind
from .WebDAVACLRestrictions import WebDAVACLRestrictions
from .WebDAVDiscoveredSource import WebDAVDiscoveredSource
from .WebDAVDiscoverSupports import WebDAVDiscoverSupports
from .WebDAVListFlags import WebDAVListFlags
from .WebDAVLockScope import WebDAVLockScope
from .WebDAVPrivilege import WebDAVPrivilege
from .WebDAVPrivilegeHint import WebDAVPrivilegeHint
from .WebDAVPrivilegeKind import WebDAVPrivilegeKind
from .WebDAVPropertyChange import WebDAVPropertyChange
from .WebDAVPropertyChangeKind import WebDAVPropertyChangeKind
from .WebDAVResource import WebDAVResource
from .WebDAVResourceKind import WebDAVResourceKind
from .WebDAVResourceSupports import WebDAVResourceSupports
from .WebDAVSession import WebDAVSession
from .WebDAVSessionClass import WebDAVSessionClass
from .WebDAVSessionPrivate import WebDAVSessionPrivate
from .XmlDocument import XmlDocument
from .XmlDocumentClass import XmlDocumentClass
from .XmlDocumentPrivate import XmlDocumentPrivate
from .XmlHash import XmlHash
from .XmlHashStatus import XmlHashStatus
from .XmlHashType import XmlHashType
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f6272aaed00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EDataServer-1.2.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EDataServer', loader=<gi.importer.DynamicImporter object at 0x7f6272aaed00>)"

