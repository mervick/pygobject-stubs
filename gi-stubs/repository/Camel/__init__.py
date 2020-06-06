# encoding: utf-8
# module gi.repository.Camel
# from /usr/lib64/girepository-1.0/Camel-1.2.typelib
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
import gobject as __gobject


# Variables with simple values

AI_CANONNAME = 2
AI_NUMERICHOST = 4

BLOCK_SIZE = 1024

BLOCK_SIZE_BITS = 10

CIPHER_CERT_INFO_PROPERTY_PHOTO_FILENAME = 'photo-filename'

CIPHER_CERT_INFO_PROPERTY_SIGNERS_ALT_EMAILS = 'signers-alt-emails'

DB_FILE = 'folders.db'

DB_FREE_CACHE_SIZE = 2097152

DB_IN_MEMORY_DB = 'EVO_IN_meM_hAnDlE'
DB_IN_MEMORY_TABLE = 'EVO_IN_meM_hAnDlE.temp'

DB_IN_MEMORY_TABLE_LIMIT = 100000

DB_SLEEP_INTERVAL = 100

DEBUG_IMAP = 'imap'

DEBUG_IMAP_FOLDER = 'imap:folder'

DOT_LOCK_REFRESH = 30

EAI_ADDRFAMILY = -9
EAI_AGAIN = -3
EAI_BADFLAGS = -1
EAI_FAIL = -4
EAI_FAMILY = -6
EAI_MEMORY = -10
EAI_NODATA = -5
EAI_NONAME = -2
EAI_OVERFLOW = -12
EAI_SERVICE = -8
EAI_SOCKTYPE = -7
EAI_SYSTEM = -11

EDS_CAMEL_PROVIDER_DIR = 'EDS_CAMEL_PROVIDER_DIR'

FOLDER_TYPE_BIT = 10
FOLDER_TYPE_MASK = 64512

FOLD_MAX_SIZE = 998

FOLD_SIZE = 77

INDEX_DELETED = 1

KEY_TABLE_MAX_KEY = 128

LOCK_DELAY = 2

LOCK_DOT_DELAY = 2
LOCK_DOT_RETRY = 5
LOCK_DOT_STALE = 60

LOCK_RETRY = 5

MESSAGE_DATE_CURRENT = -1

MESSAGE_SYSTEM_MASK = -65536

MIME_FILTER_ENRICHED_IS_RICHTEXT = 1

MIME_YDECODE_STATE_BEGIN = 4096
MIME_YDECODE_STATE_DECODE = 16384
MIME_YDECODE_STATE_END = 32768
MIME_YDECODE_STATE_EOLN = 256
MIME_YDECODE_STATE_ESCAPE = 512
MIME_YDECODE_STATE_INIT = 0
MIME_YDECODE_STATE_PART = 8192

MIME_YENCODE_CRC_INIT = -1

MIME_YENCODE_STATE_INIT = 0

NI_DGRAM = 16
NI_NAMEREQD = 8
NI_NOFQDN = 4
NI_NUMERICHOST = 1
NI_NUMERICSERV = 2

O_BINARY = 0

RECIPIENT_TYPE_BCC = 'Bcc'
RECIPIENT_TYPE_CC = 'Cc'

RECIPIENT_TYPE_RESENT_BCC = 'Resent-Bcc'
RECIPIENT_TYPE_RESENT_CC = 'Resent-Cc'
RECIPIENT_TYPE_RESENT_TO = 'Resent-To'

RECIPIENT_TYPE_TO = 'To'

STORE_INFO_FOLDER_TYPE_BIT = 10
STORE_INFO_FOLDER_TYPE_MASK = 64512

STORE_INFO_FOLDER_UNKNOWN = -1

STORE_SETUP_ARCHIVE_FOLDER = 'Account:Mail Account:archive-folder:f'

STORE_SETUP_DRAFTS_FOLDER = 'Submission:Mail Composition:drafts-folder:f'

STORE_SETUP_SENT_FOLDER = 'Submission:Mail Submission:sent-folder:f'

STORE_SETUP_TEMPLATES_FOLDER = 'Submission:Mail Composition:templates-folder:f'

UNMATCHED_NAME = 'UNMATCHED'

URL_HIDE_ALL = 3

URL_PART_AUTH = 2
URL_PART_HIDDEN = 8
URL_PART_HOST = 8
URL_PART_NEED = 8
URL_PART_PASSWORD = 4
URL_PART_PATH = 32

URL_PART_PATH_DIR = 64

URL_PART_PORT = 16
URL_PART_USER = 1

UUDECODE_STATE_MASK = 196608

VJUNK_NAME = '.#evolution/Junk'

VTRASH_NAME = '.#evolution/Trash'

_namespace = 'Camel'

_version = '1.2'

__weakref__ = None

# functions

def binding_bind_property(source, source_property, target, target_property, flags): # real signature unknown; restored from __doc__
    """ binding_bind_property(source:GObject.Object, source_property:str, target:GObject.Object, target_property:str, flags:GObject.BindingFlags) -> GObject.Binding """
    pass

def binding_bind_property_full(source, source_property, target, target_property, flags, transform_to, transform_from): # real signature unknown; restored from __doc__
    """ binding_bind_property_full(source:GObject.Object, source_property:str, target:GObject.Object, target_property:str, flags:GObject.BindingFlags, transform_to:GObject.Closure, transform_from:GObject.Closure) -> GObject.Binding """
    pass

def charset_best(in_): # real signature unknown; restored from __doc__
    """ charset_best(in_:list) -> str or None """
    return ""

def charset_iso_to_windows(isocharset): # real signature unknown; restored from __doc__
    """ charset_iso_to_windows(isocharset:str) -> str """
    return ""

def cipher_canonical_to_stream(part, flags, ostream, cancellable=None): # real signature unknown; restored from __doc__
    """ cipher_canonical_to_stream(part:Camel.MimePart, flags:int, ostream:Camel.Stream, cancellable:Gio.Cancellable=None) -> int """
    return 0

def cipher_can_load_photos(): # real signature unknown; restored from __doc__
    """ cipher_can_load_photos() -> bool """
    return False

def cipher_certinfo_get_property(cert_info, name): # real signature unknown; restored from __doc__
    """ cipher_certinfo_get_property(cert_info:Camel.CipherCertInfo, name:str) """
    pass

def cipher_certinfo_set_property(cert_info, name, value=None, value_clone=None): # real signature unknown; restored from __doc__
    """ cipher_certinfo_set_property(cert_info:Camel.CipherCertInfo, name:str, value=None, value_clone:Camel.CipherCloneFunc=None) """
    pass

def content_disposition_decode(in_): # real signature unknown; restored from __doc__
    """ content_disposition_decode(in_:str) -> Camel.ContentDisposition """
    pass

def content_transfer_encoding_decode(in_): # real signature unknown; restored from __doc__
    """ content_transfer_encoding_decode(in_:str) -> str """
    return ""

def content_type_decode(in_): # real signature unknown; restored from __doc__
    """ content_type_decode(in_:str) -> Camel.ContentType """
    pass

def debug(mode): # real signature unknown; restored from __doc__
    """ debug(mode:str) -> bool """
    return False

def debug_demangle_backtrace(bt=None): # real signature unknown; restored from __doc__
    """ debug_demangle_backtrace(bt:GLib.String=None) -> bt:GLib.String """
    pass

def debug_end(): # real signature unknown; restored from __doc__
    """ debug_end() """
    pass

def debug_get_backtrace(): # real signature unknown; restored from __doc__
    """ debug_get_backtrace() -> GLib.String """
    pass

def debug_get_raw_backtrace(): # real signature unknown; restored from __doc__
    """ debug_get_raw_backtrace() -> GLib.String """
    pass

def debug_init(): # real signature unknown; restored from __doc__
    """ debug_init() """
    pass

def debug_ref_unref_dump_backtraces(): # real signature unknown; restored from __doc__
    """ debug_ref_unref_dump_backtraces() """
    pass

def debug_ref_unref_push_backtrace(backtrace, object_ref_count): # real signature unknown; restored from __doc__
    """ debug_ref_unref_push_backtrace(backtrace:GLib.String, object_ref_count:int) """
    pass

def debug_ref_unref_push_backtrace_for_object(_object=None): # real signature unknown; restored from __doc__
    """ debug_ref_unref_push_backtrace_for_object(_object=None) """
    pass

def debug_start(mode): # real signature unknown; restored from __doc__
    """ debug_start(mode:str) -> bool """
    return False

def enriched_to_html(in_, flags): # real signature unknown; restored from __doc__
    """ enriched_to_html(in_:str, flags:int) -> str """
    return ""

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def file_util_decode_fixed_int32(in_=None, dest): # real signature unknown; restored from __doc__
    """ file_util_decode_fixed_int32(in_=None, dest:int) -> int """
    return 0

def file_util_decode_fixed_string(in_=None, p_str, len): # real signature unknown; restored from __doc__
    """ file_util_decode_fixed_string(in_=None, str:str, len:int) -> int """
    return 0

def file_util_decode_gsize(in_=None, dest): # real signature unknown; restored from __doc__
    """ file_util_decode_gsize(in_=None, dest:int) -> int """
    return 0

def file_util_decode_off_t(in_=None, dest): # real signature unknown; restored from __doc__
    """ file_util_decode_off_t(in_=None, dest:int) -> int """
    return 0

def file_util_decode_string(in_=None, p_str): # real signature unknown; restored from __doc__
    """ file_util_decode_string(in_=None, str:str) -> int """
    return 0

def file_util_decode_time_t(in_=None, dest): # real signature unknown; restored from __doc__
    """ file_util_decode_time_t(in_=None, dest:int) -> int """
    return 0

def file_util_decode_uint32(in_=None, dest): # real signature unknown; restored from __doc__
    """ file_util_decode_uint32(in_=None, dest:int) -> int """
    return 0

def file_util_encode_fixed_int32(out=None, value): # real signature unknown; restored from __doc__
    """ file_util_encode_fixed_int32(out=None, value:int) -> int """
    return 0

def file_util_encode_fixed_string(out=None, p_str, len): # real signature unknown; restored from __doc__
    """ file_util_encode_fixed_string(out=None, str:str, len:int) -> int """
    return 0

def file_util_encode_gsize(out=None, value): # real signature unknown; restored from __doc__
    """ file_util_encode_gsize(out=None, value:int) -> int """
    return 0

def file_util_encode_off_t(out=None, value): # real signature unknown; restored from __doc__
    """ file_util_encode_off_t(out=None, value:int) -> int """
    return 0

def file_util_encode_string(out=None, p_str): # real signature unknown; restored from __doc__
    """ file_util_encode_string(out=None, str:str) -> int """
    return 0

def file_util_encode_time_t(out=None, value): # real signature unknown; restored from __doc__
    """ file_util_encode_time_t(out=None, value:int) -> int """
    return 0

def file_util_encode_uint32(out=None, value): # real signature unknown; restored from __doc__
    """ file_util_encode_uint32(out=None, value:int) -> int """
    return 0

def file_util_safe_filename(name): # real signature unknown; restored from __doc__
    """ file_util_safe_filename(name:str) -> str """
    return ""

def file_util_savename(filename): # real signature unknown; restored from __doc__
    """ file_util_savename(filename:str) -> str """
    return ""

def folder_info_build(folders, namespace_, separator, short_names): # real signature unknown; restored from __doc__
    """ folder_info_build(folders:list, namespace_:str, separator:int, short_names:bool) -> Camel.FolderInfo """
    pass

def freeaddrinfo(host=None): # real signature unknown; restored from __doc__
    """ freeaddrinfo(host=None) """
    pass

def getaddrinfo(name, service, hints=None, cancellable=None): # real signature unknown; restored from __doc__
    """ getaddrinfo(name:str, service:str, hints=None, cancellable:Gio.Cancellable=None) """
    pass

def headers_dup_mailing_list(headers): # real signature unknown; restored from __doc__
    """ headers_dup_mailing_list(headers:Camel.NameValueArray) -> str or None """
    return ""

def header_address_decode(in_, charset): # real signature unknown; restored from __doc__
    """ header_address_decode(in_:str, charset:str) -> Camel.HeaderAddress """
    pass

def header_address_fold(in_, headerlen): # real signature unknown; restored from __doc__
    """ header_address_fold(in_:str, headerlen:int) -> str """
    return ""

def header_address_list_append(addrlistp, addr): # real signature unknown; restored from __doc__
    """ header_address_list_append(addrlistp:list, addr:Camel.HeaderAddress) """
    pass

def header_address_list_append_list(addrlistp, addrs): # real signature unknown; restored from __doc__
    """ header_address_list_append_list(addrlistp:list, addrs:list) """
    pass

def header_address_list_clear(addrlistp): # real signature unknown; restored from __doc__
    """ header_address_list_clear(addrlistp:list) """
    pass

def header_address_list_encode(addrlist): # real signature unknown; restored from __doc__
    """ header_address_list_encode(addrlist:list) -> str """
    return ""

def header_address_list_format(addrlist): # real signature unknown; restored from __doc__
    """ header_address_list_format(addrlist:list) -> str """
    return ""

def header_contentid_decode(in_): # real signature unknown; restored from __doc__
    """ header_contentid_decode(in_:str) -> str """
    return ""

def header_decode_date(p_str, tz_offset): # real signature unknown; restored from __doc__
    """ header_decode_date(str:str, tz_offset:int) -> int """
    return 0

def header_decode_int(in_): # real signature unknown; restored from __doc__
    """ header_decode_int(in_:str) -> int """
    return 0

def header_decode_string(in_, default_charset): # real signature unknown; restored from __doc__
    """ header_decode_string(in_:str, default_charset:str) -> str """
    return ""

def header_encode_phrase(in_): # real signature unknown; restored from __doc__
    """ header_encode_phrase(in_:int) -> str """
    return ""

def header_encode_string(in_): # real signature unknown; restored from __doc__
    """ header_encode_string(in_:int) -> str """
    return ""

def header_fold(in_, headerlen): # real signature unknown; restored from __doc__
    """ header_fold(in_:str, headerlen:int) -> str """
    return ""

def header_format_ctext(in_, default_charset): # real signature unknown; restored from __doc__
    """ header_format_ctext(in_:str, default_charset:str) -> str """
    return ""

def header_format_date(date, tz_offset): # real signature unknown; restored from __doc__
    """ header_format_date(date:int, tz_offset:int) -> str """
    return ""

def header_location_decode(in_): # real signature unknown; restored from __doc__
    """ header_location_decode(in_:str) -> str """
    return ""

def header_mailbox_decode(in_, charset): # real signature unknown; restored from __doc__
    """ header_mailbox_decode(in_:str, charset:str) -> Camel.HeaderAddress """
    pass

def header_mime_decode(in_, maj, min): # real signature unknown; restored from __doc__
    """ header_mime_decode(in_:str, maj:int, min:int) """
    pass

def header_msgid_decode(in_): # real signature unknown; restored from __doc__
    """ header_msgid_decode(in_:str) -> str """
    return ""

def header_msgid_generate(domain): # real signature unknown; restored from __doc__
    """ header_msgid_generate(domain:str) -> str """
    return ""

def header_newsgroups_decode(in_): # real signature unknown; restored from __doc__
    """ header_newsgroups_decode(in_:str) -> list """
    return []

def header_param(params=None, name): # real signature unknown; restored from __doc__
    """ header_param(params=None, name:str) -> str """
    return ""

def header_param_list_decode(in_=None): # real signature unknown; restored from __doc__
    """ header_param_list_decode(in_:str=None) """
    pass

def header_param_list_format(params=None): # real signature unknown; restored from __doc__
    """ header_param_list_format(params=None) -> str """
    return ""

def header_param_list_format_append(out, params=None): # real signature unknown; restored from __doc__
    """ header_param_list_format_append(out:GLib.String, params=None) """
    pass

def header_param_list_free(params=None): # real signature unknown; restored from __doc__
    """ header_param_list_free(params=None) """
    pass

def header_references_decode(in_): # real signature unknown; restored from __doc__
    """ header_references_decode(in_:str) -> list """
    return []

def header_set_param(paramsp=None, name, value): # real signature unknown; restored from __doc__
    """ header_set_param(paramsp=None, name:str, value:str) """
    pass

def header_token_decode(in_): # real signature unknown; restored from __doc__
    """ header_token_decode(in_:str) -> str """
    return ""

def header_unfold(in_): # real signature unknown; restored from __doc__
    """ header_unfold(in_:str) -> str """
    return ""

def host_idna_to_ascii(host): # real signature unknown; restored from __doc__
    """ host_idna_to_ascii(host:str) -> str """
    return ""

def iconv_charset_language(charset): # real signature unknown; restored from __doc__
    """ iconv_charset_language(charset:str) -> str """
    return ""

def iconv_charset_name(charset): # real signature unknown; restored from __doc__
    """ iconv_charset_name(charset:str) -> str """
    return ""

def iconv_locale_charset(): # real signature unknown; restored from __doc__
    """ iconv_locale_charset() -> str """
    return ""

def iconv_locale_language(): # real signature unknown; restored from __doc__
    """ iconv_locale_language() -> str """
    return ""

def init(certdb_dir, nss_init): # real signature unknown; restored from __doc__
    """ init(certdb_dir:str, nss_init:bool) -> int """
    return 0

def localtime_with_offset(tt, tm=None, offset): # real signature unknown; restored from __doc__
    """ localtime_with_offset(tt:int, tm=None, offset:int) """
    pass

def lock_dot(path): # real signature unknown; restored from __doc__
    """ lock_dot(path:str) -> int """
    return 0

def lock_fcntl(fd, type): # real signature unknown; restored from __doc__
    """ lock_fcntl(fd:int, type:Camel.LockType) -> int """
    return 0

def lock_flock(fd, type): # real signature unknown; restored from __doc__
    """ lock_flock(fd:int, type:Camel.LockType) -> int """
    return 0

def lock_folder(path, fd, type): # real signature unknown; restored from __doc__
    """ lock_folder(path:str, fd:int, type:Camel.LockType) -> int """
    return 0

def lock_helper_lock(path): # real signature unknown; restored from __doc__
    """ lock_helper_lock(path:str) -> int """
    return 0

def lock_helper_unlock(lockid): # real signature unknown; restored from __doc__
    """ lock_helper_unlock(lockid:int) -> int """
    return 0

def mktime_utc(tm=None): # real signature unknown; restored from __doc__
    """ mktime_utc(tm=None) -> int """
    return 0

def movemail(source, dest): # real signature unknown; restored from __doc__
    """ movemail(source:str, dest:str) -> int """
    return 0

def pointer_tracker_dump(): # real signature unknown; restored from __doc__
    """ pointer_tracker_dump() """
    pass

def pointer_tracker_track_with_info(ptr=None, info): # real signature unknown; restored from __doc__
    """ pointer_tracker_track_with_info(ptr=None, info:str) """
    pass

def pointer_tracker_untrack(ptr=None): # real signature unknown; restored from __doc__
    """ pointer_tracker_untrack(ptr=None) """
    pass

def provider_get(protocol): # real signature unknown; restored from __doc__
    """ provider_get(protocol:str) -> Camel.Provider """
    pass

def provider_init(): # real signature unknown; restored from __doc__
    """ provider_init() """
    pass

def provider_list(load): # real signature unknown; restored from __doc__
    """ provider_list(load:bool) -> list """
    return []

def provider_load(path): # real signature unknown; restored from __doc__
    """ provider_load(path:str) -> bool """
    return False

def provider_module_init(): # real signature unknown; restored from __doc__
    """ provider_module_init() """
    pass

def pstring_add(string, own): # real signature unknown; restored from __doc__
    """ pstring_add(string:str, own:bool) -> str """
    return ""

def pstring_contains(string): # real signature unknown; restored from __doc__
    """ pstring_contains(string:str) -> bool """
    return False

def pstring_dump_stat(): # real signature unknown; restored from __doc__
    """ pstring_dump_stat() """
    pass

def pstring_free(string): # real signature unknown; restored from __doc__
    """ pstring_free(string:str) """
    pass

def pstring_peek(string): # real signature unknown; restored from __doc__
    """ pstring_peek(string:str) -> str """
    return ""

def pstring_strdup(string): # real signature unknown; restored from __doc__
    """ pstring_strdup(string:str) -> str """
    return ""

def quoted_decode_step(in_, out, saveme): # real signature unknown; restored from __doc__
    """ quoted_decode_step(in_:list, out:list, saveme:list) -> int, out:list, saveme:list """
    return 0

def quoted_encode_close(in_, out, save): # real signature unknown; restored from __doc__
    """ quoted_encode_close(in_:list, out:list, save:list) -> int, out:list, save:list """
    return 0

def quoted_encode_step(in_, out, save): # real signature unknown; restored from __doc__
    """ quoted_encode_step(in_:list, out:list, save:list) -> int, out:list, save:list """
    return 0

def read(fd, buf, n, cancellable=None): # real signature unknown; restored from __doc__
    """ read(fd:int, buf:str, n:int, cancellable:Gio.Cancellable=None) -> int """
    return 0

def search_camel_header_soundex(header, match): # real signature unknown; restored from __doc__
    """ search_camel_header_soundex(header:str, match:str) -> bool """
    return False

def search_get_all_headers_decoded(message): # real signature unknown; restored from __doc__
    """ search_get_all_headers_decoded(message:Camel.MimeMessage) -> str """
    return ""

def search_get_default_charset_from_headers(headers): # real signature unknown; restored from __doc__
    """ search_get_default_charset_from_headers(headers:Camel.NameValueArray) -> str """
    return ""

def search_get_default_charset_from_message(message): # real signature unknown; restored from __doc__
    """ search_get_default_charset_from_message(message:Camel.MimeMessage) -> str """
    return ""

def search_get_headers_decoded(headers, default_charset=None): # real signature unknown; restored from __doc__
    """ search_get_headers_decoded(headers:Camel.NameValueArray, default_charset:str=None) -> str """
    return ""

def search_get_header_decoded(header_name, header_value, default_charset=None): # real signature unknown; restored from __doc__
    """ search_get_header_decoded(header_name:str, header_value:str, default_charset:str=None) -> str """
    return ""

def search_header_is_address(header_name): # real signature unknown; restored from __doc__
    """ search_header_is_address(header_name:str) -> bool """
    return False

def search_header_match(value, match, how, type, default_charset): # real signature unknown; restored from __doc__
    """ search_header_match(value:str, match:str, how:Camel._search_match_t, type:Camel._search_t, default_charset:str) -> bool """
    return False

def search_words_free(words=None): # real signature unknown; restored from __doc__
    """ search_words_free(words=None) """
    pass

def search_words_simple(words=None): # real signature unknown; restored from __doc__
    """ search_words_simple(words=None) """
    pass

def search_words_split(in_): # real signature unknown; restored from __doc__
    """ search_words_split(in_:int) """
    pass

def shutdown(): # real signature unknown; restored from __doc__
    """ shutdown() """
    pass

def store_info_name(summary, info): # real signature unknown; restored from __doc__
    """ store_info_name(summary:Camel.StoreSummary, info:Camel.StoreInfo) -> str """
    return ""

def store_info_path(summary, info): # real signature unknown; restored from __doc__
    """ store_info_path(summary:Camel.StoreSummary, info:Camel.StoreInfo) -> str """
    return ""

def store_info_set_string(summary, info, type, value): # real signature unknown; restored from __doc__
    """ store_info_set_string(summary:Camel.StoreSummary, info:Camel.StoreInfo, type:int, value:str) """
    pass

def strcase_equal(a=None, b=None): # real signature unknown; restored from __doc__
    """ strcase_equal(a=None, b=None) -> int """
    return 0

def strcase_hash(v=None): # real signature unknown; restored from __doc__
    """ strcase_hash(v=None) -> int """
    return 0

def strdown(p_str): # real signature unknown; restored from __doc__
    """ strdown(str:str) -> str """
    return ""

def strstrcase(haystack, needle): # real signature unknown; restored from __doc__
    """ strstrcase(haystack:str, needle:str) -> str """
    return ""

def system_flag(name): # real signature unknown; restored from __doc__
    """ system_flag(name:str) -> Camel.MessageFlags """
    pass

def system_flag_get(flags, name): # real signature unknown; restored from __doc__
    """ system_flag_get(flags:Camel.MessageFlags, name:str) -> bool """
    return False

def text_to_html(in_, flags, color): # real signature unknown; restored from __doc__
    """ text_to_html(in_:str, flags:Camel.MimeFilterToHTMLFlags, color:int) -> str """
    return ""

def time_value_apply(src_time, unit, value): # real signature unknown; restored from __doc__
    """ time_value_apply(src_time:int, unit:Camel.TimeUnit, value:int) -> int """
    return 0

def transfer_encoding_from_string(string): # real signature unknown; restored from __doc__
    """ transfer_encoding_from_string(string:str) -> Camel.TransferEncoding """
    pass

def transfer_encoding_to_string(encoding): # real signature unknown; restored from __doc__
    """ transfer_encoding_to_string(encoding:Camel.TransferEncoding) -> str """
    return ""

def ucs2_utf8(ptr): # real signature unknown; restored from __doc__
    """ ucs2_utf8(ptr:str) -> str """
    return ""

def uid_cache_free_uids(uids): # real signature unknown; restored from __doc__
    """ uid_cache_free_uids(uids:list) """
    pass

def unlock_dot(path): # real signature unknown; restored from __doc__
    """ unlock_dot(path:str) """
    pass

def unlock_fcntl(fd): # real signature unknown; restored from __doc__
    """ unlock_fcntl(fd:int) """
    pass

def unlock_flock(fd): # real signature unknown; restored from __doc__
    """ unlock_flock(fd:int) """
    pass

def unlock_folder(path, fd): # real signature unknown; restored from __doc__
    """ unlock_folder(path:str, fd:int) """
    pass

def url_addrspec_end(in_, pos, inend, match): # real signature unknown; restored from __doc__
    """ url_addrspec_end(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
    return False

def url_addrspec_start(in_, pos, inend, match): # real signature unknown; restored from __doc__
    """ url_addrspec_start(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
    return False

def url_decode(part): # real signature unknown; restored from __doc__
    """ url_decode(part:str) """
    pass

def url_decode_path(path): # real signature unknown; restored from __doc__
    """ url_decode_path(path:str) -> str """
    return ""

def url_encode(part, escape_extra): # real signature unknown; restored from __doc__
    """ url_encode(part:str, escape_extra:str) -> str """
    return ""

def url_file_end(in_, pos, inend, match): # real signature unknown; restored from __doc__
    """ url_file_end(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
    return False

def url_file_start(in_, pos, inend, match): # real signature unknown; restored from __doc__
    """ url_file_start(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
    return False

def url_web_end(in_, pos, inend, match): # real signature unknown; restored from __doc__
    """ url_web_end(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
    return False

def url_web_start(in_, pos, inend, match): # real signature unknown; restored from __doc__
    """ url_web_start(in_:str, pos:str, inend:str, match:Camel.UrlMatch) -> bool """
    return False

def ustrstrcase(haystack, needle): # real signature unknown; restored from __doc__
    """ ustrstrcase(haystack:str, needle:str) -> str """
    return ""

def utf7_utf8(ptr): # real signature unknown; restored from __doc__
    """ utf7_utf8(ptr:str) -> str """
    return ""

def utf8_getc(ptr): # real signature unknown; restored from __doc__
    """ utf8_getc(ptr:int) -> int, ptr:int """
    return 0

def utf8_getc_limit(ptr, end): # real signature unknown; restored from __doc__
    """ utf8_getc_limit(ptr:int, end:int) -> int, ptr:int """
    return 0

def utf8_make_valid(text): # real signature unknown; restored from __doc__
    """ utf8_make_valid(text:str) -> str """
    return ""

def utf8_make_valid_len(text, text_len): # real signature unknown; restored from __doc__
    """ utf8_make_valid_len(text:str, text_len:int) -> str """
    return ""

def utf8_putc(ptr, c): # real signature unknown; restored from __doc__
    """ utf8_putc(ptr:int, c:int) -> ptr:int """
    pass

def utf8_ucs2(ptr): # real signature unknown; restored from __doc__
    """ utf8_ucs2(ptr:str) -> str """
    return ""

def utf8_utf7(ptr): # real signature unknown; restored from __doc__
    """ utf8_utf7(ptr:str) -> str """
    return ""

def util_bdata_get_number(bdata_ptr, default_value): # real signature unknown; restored from __doc__
    """ util_bdata_get_number(bdata_ptr:str, default_value:int) -> int """
    return 0

def util_bdata_get_string(bdata_ptr, default_value): # real signature unknown; restored from __doc__
    """ util_bdata_get_string(bdata_ptr:str, default_value:str) -> str """
    return ""

def util_bdata_put_number(bdata_str, value): # real signature unknown; restored from __doc__
    """ util_bdata_put_number(bdata_str:GLib.String, value:int) """
    pass

def util_bdata_put_string(bdata_str, value): # real signature unknown; restored from __doc__
    """ util_bdata_put_string(bdata_str:GLib.String, value:str) """
    pass

def uudecode_step(in_, out, save): # real signature unknown; restored from __doc__
    """ uudecode_step(in_:list, out:list, save:list) -> int, out:list, save:list """
    return 0

def uuencode_close(in_, out, uubuf, save): # real signature unknown; restored from __doc__
    """ uuencode_close(in_:list, out:list, uubuf:list, save:list) -> int, out:list, uubuf:list, save:list """
    return 0

def uuencode_step(in_, out, uubuf, save): # real signature unknown; restored from __doc__
    """ uuencode_step(in_:list, out:list, uubuf:list, save:list) -> int, out:list, uubuf:list, save:list """
    return 0

def write(fd, buf, n, cancellable=None): # real signature unknown; restored from __doc__
    """ write(fd:int, buf:str, n:int, cancellable:Gio.Cancellable=None) -> int """
    return 0

def ydecode_step(in_): # real signature unknown; restored from __doc__
    """ ydecode_step(in_:list) -> int, out:list, state:int, pcrc:int, crc:int """
    return 0

def yencode_close(in_): # real signature unknown; restored from __doc__
    """ yencode_close(in_:list) -> int, out:list, state:int, pcrc:int, crc:int """
    return 0

def yencode_step(in_): # real signature unknown; restored from __doc__
    """ yencode_step(in_:list) -> int, out:list, state:int, pcrc:int, crc:int """
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

from .Address import Address
from .AddressClass import AddressClass
from .AddressPrivate import AddressPrivate
from .AsyncClosure import AsyncClosure
from .AuthenticationResult import AuthenticationResult
from .BestencEncoding import BestencEncoding
from .BestencRequired import BestencRequired
from .Block import Block
from .BlockFile import BlockFile
from .BlockFileClass import BlockFileClass
from .BlockFileFlags import BlockFileFlags
from .BlockFilePrivate import BlockFilePrivate
from .BlockFlags import BlockFlags
from .BlockRoot import BlockRoot
from .Cert import Cert
from .CertDB import CertDB
from .CertDBClass import CertDBClass
from .CertDBPrivate import CertDBPrivate
from .CertTrust import CertTrust
from .Charset import Charset
from .CipherCertInfo import CipherCertInfo
from .CipherCertInfoProperty import CipherCertInfoProperty
from .CipherContext import CipherContext
from .CipherContextClass import CipherContextClass
from .CipherContextPrivate import CipherContextPrivate
from .CipherHash import CipherHash
from .CipherValidity import CipherValidity
from .CipherValidityEncrypt import CipherValidityEncrypt
from .CipherValidityMode import CipherValidityMode
from .CipherValiditySign import CipherValiditySign
from .CompareType import CompareType
from .ContentDisposition import ContentDisposition
from .ContentType import ContentType
from .DataCache import DataCache
from .DataCacheClass import DataCacheClass
from .DataCachePrivate import DataCachePrivate
from .DataWrapper import DataWrapper
from .DataWrapperClass import DataWrapperClass
from .DataWrapperPrivate import DataWrapperPrivate
from .DB import DB
from .DBClass import DBClass
from .DBKnownColumnNames import DBKnownColumnNames
from .DBPrivate import DBPrivate
from .Error import Error
from .FetchHeadersType import FetchHeadersType
from .FetchType import FetchType
from .FilterDriver import FilterDriver
from .FilterDriverClass import FilterDriverClass
from .FilterDriverPrivate import FilterDriverPrivate
from .FilterInputStream import FilterInputStream
from .FilterInputStreamClass import FilterInputStreamClass
from .FilterInputStreamPrivate import FilterInputStreamPrivate
from .FilterOutputStream import FilterOutputStream
from .FilterOutputStreamClass import FilterOutputStreamClass
from .FilterOutputStreamPrivate import FilterOutputStreamPrivate
from .FIRecord import FIRecord
from .Object import Object
from .Folder import Folder
from .FolderChangeInfo import FolderChangeInfo
from .FolderChangeInfoPrivate import FolderChangeInfoPrivate
from .FolderClass import FolderClass
from .FolderError import FolderError
from .FolderFlags import FolderFlags
from .FolderInfo import FolderInfo
from .FolderInfoFlags import FolderInfoFlags
from .FolderPrivate import FolderPrivate
from .FolderQuotaInfo import FolderQuotaInfo
from .FolderSearch import FolderSearch
from .FolderSearchClass import FolderSearchClass
from .FolderSearchPrivate import FolderSearchPrivate
from .FolderSummary import FolderSummary
from .FolderSummaryClass import FolderSummaryClass
from .FolderSummaryFlags import FolderSummaryFlags
from .FolderSummaryPrivate import FolderSummaryPrivate
from .FolderThread import FolderThread
from .FolderThreadNode import FolderThreadNode
from .GpgContext import GpgContext
from .GpgContextClass import GpgContextClass
from .GpgContextPrivate import GpgContextPrivate
from .HeaderAddress import HeaderAddress
from .HeaderAddressType import HeaderAddressType
from .HeaderParam import HeaderParam
from .HTMLParser import HTMLParser
from .HTMLParserClass import HTMLParserClass
from .HTMLParserPrivate import HTMLParserPrivate
from .HTMLParserState import HTMLParserState
from .Index import Index
from .IndexClass import IndexClass
from .IndexCursor import IndexCursor
from .IndexCursorClass import IndexCursorClass
from .IndexCursorPrivate import IndexCursorPrivate
from .IndexName import IndexName
from .IndexNameClass import IndexNameClass
from .IndexNamePrivate import IndexNamePrivate
from .IndexPrivate import IndexPrivate
from .InternetAddress import InternetAddress
from .InternetAddressClass import InternetAddressClass
from .InternetAddressPrivate import InternetAddressPrivate
from .JunkFilter import JunkFilter
from .JunkFilterInterface import JunkFilterInterface
from .JunkStatus import JunkStatus
from .KeyBlock import KeyBlock
from .KeyFile import KeyFile
from .KeyFileClass import KeyFileClass
from .KeyFilePrivate import KeyFilePrivate
from .KeyRootBlock import KeyRootBlock
from .KeyTable import KeyTable
from .KeyTableClass import KeyTableClass
from .KeyTablePrivate import KeyTablePrivate
from .Settings import Settings
from .StoreSettings import StoreSettings
from .LocalSettings import LocalSettings
from .LocalSettingsClass import LocalSettingsClass
from .LocalSettingsPrivate import LocalSettingsPrivate
from .LockType import LockType
from .Medium import Medium
from .MediumClass import MediumClass
from .MediumPrivate import MediumPrivate
from .MemChunk import MemChunk
from .MemPool import MemPool
from .MemPoolFlags import MemPoolFlags
from .MessageContentInfo import MessageContentInfo
from .MessageFlags import MessageFlags
from .MessageInfo import MessageInfo
from .MessageInfoBase import MessageInfoBase
from .MessageInfoBaseClass import MessageInfoBaseClass
from .MessageInfoBasePrivate import MessageInfoBasePrivate
from .MessageInfoClass import MessageInfoClass
from .MessageInfoPrivate import MessageInfoPrivate
from .MimeFilter import MimeFilter
from .MimeFilterBasic import MimeFilterBasic
from .MimeFilterBasicClass import MimeFilterBasicClass
from .MimeFilterBasicPrivate import MimeFilterBasicPrivate
from .MimeFilterBasicType import MimeFilterBasicType
from .MimeFilterBestenc import MimeFilterBestenc
from .MimeFilterBestencClass import MimeFilterBestencClass
from .MimeFilterBestencPrivate import MimeFilterBestencPrivate
from .MimeFilterCanon import MimeFilterCanon
from .MimeFilterCanonClass import MimeFilterCanonClass
from .MimeFilterCanonPrivate import MimeFilterCanonPrivate
from .MimeFilterCharset import MimeFilterCharset
from .MimeFilterCharsetClass import MimeFilterCharsetClass
from .MimeFilterCharsetPrivate import MimeFilterCharsetPrivate
from .MimeFilterClass import MimeFilterClass
from .MimeFilterCRLF import MimeFilterCRLF
from .MimeFilterCRLFClass import MimeFilterCRLFClass
from .MimeFilterCRLFDirection import MimeFilterCRLFDirection
from .MimeFilterCRLFMode import MimeFilterCRLFMode
from .MimeFilterCRLFPrivate import MimeFilterCRLFPrivate
from .MimeFilterEnriched import MimeFilterEnriched
from .MimeFilterEnrichedClass import MimeFilterEnrichedClass
from .MimeFilterEnrichedPrivate import MimeFilterEnrichedPrivate
from .MimeFilterFrom import MimeFilterFrom
from .MimeFilterFromClass import MimeFilterFromClass
from .MimeFilterFromPrivate import MimeFilterFromPrivate
from .MimeFilterGZip import MimeFilterGZip
from .MimeFilterGZipClass import MimeFilterGZipClass
from .MimeFilterGZipMode import MimeFilterGZipMode
from .MimeFilterGZipPrivate import MimeFilterGZipPrivate
from .MimeFilterHTML import MimeFilterHTML
from .MimeFilterHTMLClass import MimeFilterHTMLClass
from .MimeFilterHTMLPrivate import MimeFilterHTMLPrivate
from .MimeFilterIndex import MimeFilterIndex
from .MimeFilterIndexClass import MimeFilterIndexClass
from .MimeFilterIndexPrivate import MimeFilterIndexPrivate
from .MimeFilterLinewrap import MimeFilterLinewrap
from .MimeFilterLinewrapClass import MimeFilterLinewrapClass
from .MimeFilterLinewrapPrivate import MimeFilterLinewrapPrivate
from .MimeFilterPgp import MimeFilterPgp
from .MimeFilterPgpClass import MimeFilterPgpClass
from .MimeFilterPgpPrivate import MimeFilterPgpPrivate
from .MimeFilterPrivate import MimeFilterPrivate
from .MimeFilterProgress import MimeFilterProgress
from .MimeFilterProgressClass import MimeFilterProgressClass
from .MimeFilterProgressPrivate import MimeFilterProgressPrivate
from .MimeFilterToHTML import MimeFilterToHTML
from .MimeFilterToHTMLClass import MimeFilterToHTMLClass
from .MimeFilterToHTMLFlags import MimeFilterToHTMLFlags
from .MimeFilterToHTMLPrivate import MimeFilterToHTMLPrivate
from .MimeFilterWindows import MimeFilterWindows
from .MimeFilterWindowsClass import MimeFilterWindowsClass
from .MimeFilterWindowsPrivate import MimeFilterWindowsPrivate
from .MimeFilterYenc import MimeFilterYenc
from .MimeFilterYencClass import MimeFilterYencClass
from .MimeFilterYencDirection import MimeFilterYencDirection
from .MimeFilterYencPrivate import MimeFilterYencPrivate
from .MimePart import MimePart
from .MimeMessage import MimeMessage
from .MimeMessageClass import MimeMessageClass
from .MimeMessagePrivate import MimeMessagePrivate
from .MimeParser import MimeParser
from .MimeParserClass import MimeParserClass
from .MimeParserPrivate import MimeParserPrivate
from .MimeParserState import MimeParserState
from .MimePartClass import MimePartClass
from .MimePartPrivate import MimePartPrivate
from .MIRecord import MIRecord
from .Msg import Msg
from .MsgPort import MsgPort
from .Multipart import Multipart
from .MultipartClass import MultipartClass
from .MultipartEncrypted import MultipartEncrypted
from .MultipartEncryptedClass import MultipartEncryptedClass
from .MultipartEncryptedPrivate import MultipartEncryptedPrivate
from .MultipartPrivate import MultipartPrivate
from .MultipartSigned import MultipartSigned
from .MultipartSignedClass import MultipartSignedClass
from .MultipartSignedPrivate import MultipartSignedPrivate
from .NamedFlags import NamedFlags
from .NameValueArray import NameValueArray
from .NetworkSecurityMethod import NetworkSecurityMethod
from .NetworkService import NetworkService
from .NetworkServiceInterface import NetworkServiceInterface
from .NetworkSettings import NetworkSettings
from .NetworkSettingsInterface import NetworkSettingsInterface
from .NNTPAddress import NNTPAddress
from .NNTPAddressClass import NNTPAddressClass
from .NNTPAddressPrivate import NNTPAddressPrivate
from .NullOutputStream import NullOutputStream
from .NullOutputStreamClass import NullOutputStreamClass
from .NullOutputStreamPrivate import NullOutputStreamPrivate
from .ObjectBag import ObjectBag
from .ObjectClass import ObjectClass
from .ObjectPrivate import ObjectPrivate
from .OfflineFolder import OfflineFolder
from .OfflineFolderClass import OfflineFolderClass
from .OfflineFolderPrivate import OfflineFolderPrivate
from .OfflineSettings import OfflineSettings
from .OfflineSettingsClass import OfflineSettingsClass
from .OfflineSettingsPrivate import OfflineSettingsPrivate
from .Service import Service
from .Store import Store
from .OfflineStore import OfflineStore
from .OfflineStoreClass import OfflineStoreClass
from .OfflineStorePrivate import OfflineStorePrivate
from .Operation import Operation
from .OperationClass import OperationClass
from .OperationPrivate import OperationPrivate
from .ParamFlags import ParamFlags
from .PartitionKey import PartitionKey
from .PartitionKeyBlock import PartitionKeyBlock
from .PartitionMap import PartitionMap
from .PartitionMapBlock import PartitionMapBlock
from .PartitionTable import PartitionTable
from .PartitionTableClass import PartitionTableClass
from .PartitionTablePrivate import PartitionTablePrivate
from .Provider import Provider
from .ProviderConfEntry import ProviderConfEntry
from .ProviderConfType import ProviderConfType
from .ProviderFlags import ProviderFlags
from .ProviderModule import ProviderModule
from .ProviderPortEntry import ProviderPortEntry
from .ProviderType import ProviderType
from .ProviderURLFlags import ProviderURLFlags
from .RecipientCertificateFlags import RecipientCertificateFlags
from .Sasl import Sasl
from .SaslAnonTraceType import SaslAnonTraceType
from .SaslAnonymous import SaslAnonymous
from .SaslAnonymousClass import SaslAnonymousClass
from .SaslAnonymousPrivate import SaslAnonymousPrivate
from .SaslClass import SaslClass
from .SaslCramMd5 import SaslCramMd5
from .SaslCramMd5Class import SaslCramMd5Class
from .SaslCramMd5Private import SaslCramMd5Private
from .SaslDigestMd5 import SaslDigestMd5
from .SaslDigestMd5Class import SaslDigestMd5Class
from .SaslDigestMd5Private import SaslDigestMd5Private
from .SaslGssapi import SaslGssapi
from .SaslGssapiClass import SaslGssapiClass
from .SaslGssapiPrivate import SaslGssapiPrivate
from .SaslLogin import SaslLogin
from .SaslLoginClass import SaslLoginClass
from .SaslLoginPrivate import SaslLoginPrivate
from .SaslNTLM import SaslNTLM
from .SaslNTLMClass import SaslNTLMClass
from .SaslNTLMPrivate import SaslNTLMPrivate
from .SaslPlain import SaslPlain
from .SaslPlainClass import SaslPlainClass
from .SaslPlainPrivate import SaslPlainPrivate
from .SaslPOPB4SMTP import SaslPOPB4SMTP
from .SaslPOPB4SMTPClass import SaslPOPB4SMTPClass
from .SaslPOPB4SMTPPrivate import SaslPOPB4SMTPPrivate
from .SaslPrivate import SaslPrivate
from .SaslXOAuth2 import SaslXOAuth2
from .SaslXOAuth2Class import SaslXOAuth2Class
from .SaslXOAuth2Google import SaslXOAuth2Google
from .SaslXOAuth2GoogleClass import SaslXOAuth2GoogleClass
from .SaslXOAuth2GooglePrivate import SaslXOAuth2GooglePrivate
from .SaslXOAuth2Outlook import SaslXOAuth2Outlook
from .SaslXOAuth2OutlookClass import SaslXOAuth2OutlookClass
from .SaslXOAuth2OutlookPrivate import SaslXOAuth2OutlookPrivate
from .SaslXOAuth2Private import SaslXOAuth2Private
from .ServiceAuthType import ServiceAuthType
from .ServiceClass import ServiceClass
from .ServiceConnectionStatus import ServiceConnectionStatus
from .ServiceError import ServiceError
from .ServicePrivate import ServicePrivate
from .Session import Session
from .SessionAlertType import SessionAlertType
from .SessionClass import SessionClass
from .SessionPrivate import SessionPrivate
from .SettingsClass import SettingsClass
from .SettingsPrivate import SettingsPrivate
from .SExp import SExp
from .SExpClass import SExpClass
from .SExpPrivate import SExpPrivate
from .SExpResult import SExpResult
from .SExpResultType import SExpResultType
from .SExpSymbol import SExpSymbol
from .SExpTerm import SExpTerm
from .SExpTermType import SExpTermType
from .SMIMEContext import SMIMEContext
from .SMIMEContextClass import SMIMEContextClass
from .SMIMEContextPrivate import SMIMEContextPrivate
from .SMIMEDescribe import SMIMEDescribe
from .SMIMESign import SMIMESign
from .SortType import SortType
from .StoreClass import StoreClass
from .StoreError import StoreError
from .StoreFlags import StoreFlags
from .StoreGetFolderFlags import StoreGetFolderFlags
from .StoreGetFolderInfoFlags import StoreGetFolderInfoFlags
from .StoreInfo import StoreInfo
from .StoreInfoFlags import StoreInfoFlags
from .StorePermissionFlags import StorePermissionFlags
from .StorePrivate import StorePrivate
from .StoreSettingsClass import StoreSettingsClass
from .StoreSettingsPrivate import StoreSettingsPrivate
from .StoreSummary import StoreSummary
from .StoreSummaryClass import StoreSummaryClass
from .StoreSummaryPrivate import StoreSummaryPrivate
from .Stream import Stream
from .StreamBuffer import StreamBuffer
from .StreamBufferClass import StreamBufferClass
from .StreamBufferMode import StreamBufferMode
from .StreamBufferPrivate import StreamBufferPrivate
from .StreamClass import StreamClass
from .StreamFilter import StreamFilter
from .StreamFilterClass import StreamFilterClass
from .StreamFilterPrivate import StreamFilterPrivate
from .StreamFs import StreamFs
from .StreamFsClass import StreamFsClass
from .StreamFsPrivate import StreamFsPrivate
from .StreamMem import StreamMem
from .StreamMemClass import StreamMemClass
from .StreamMemPrivate import StreamMemPrivate
from .StreamNull import StreamNull
from .StreamNullClass import StreamNullClass
from .StreamNullPrivate import StreamNullPrivate
from .StreamPrivate import StreamPrivate
from .StreamProcess import StreamProcess
from .StreamProcessClass import StreamProcessClass
from .StreamProcessPrivate import StreamProcessPrivate
from .Subscribable import Subscribable
from .SubscribableInterface import SubscribableInterface
from .SummaryMessageID import SummaryMessageID
from .TextIndex import TextIndex
from .TextIndexClass import TextIndexClass
from .TextIndexCursor import TextIndexCursor
from .TextIndexCursorClass import TextIndexCursorClass
from .TextIndexCursorPrivate import TextIndexCursorPrivate
from .TextIndexKeyCursor import TextIndexKeyCursor
from .TextIndexKeyCursorClass import TextIndexKeyCursorClass
from .TextIndexKeyCursorPrivate import TextIndexKeyCursorPrivate
from .TextIndexName import TextIndexName
from .TextIndexNameClass import TextIndexNameClass
from .TextIndexNamePrivate import TextIndexNamePrivate
from .TextIndexPrivate import TextIndexPrivate
from .ThreeState import ThreeState
from .TimeUnit import TimeUnit
from .TransferEncoding import TransferEncoding
from .Transport import Transport
from .TransportClass import TransportClass
from .TransportPrivate import TransportPrivate
from .Trie import Trie
from .UIDCache import UIDCache
from .URL import URL
from .URLFlags import URLFlags
from .UrlMatch import UrlMatch
from .UrlPattern import UrlPattern
from .UrlScanner import UrlScanner
from .UUDecodeState import UUDecodeState
from .VeeDataCache import VeeDataCache
from .VeeDataCacheClass import VeeDataCacheClass
from .VeeDataCachePrivate import VeeDataCachePrivate
from .VeeFolder import VeeFolder
from .VeeFolderClass import VeeFolderClass
from .VeeFolderPrivate import VeeFolderPrivate
from .VeeMessageInfo import VeeMessageInfo
from .VeeMessageInfoClass import VeeMessageInfoClass
from .VeeMessageInfoData import VeeMessageInfoData
from .VeeMessageInfoDataClass import VeeMessageInfoDataClass
from .VeeMessageInfoDataPrivate import VeeMessageInfoDataPrivate
from .VeeMessageInfoPrivate import VeeMessageInfoPrivate
from .VeeStore import VeeStore
from .VeeStoreClass import VeeStoreClass
from .VeeStorePrivate import VeeStorePrivate
from .VeeSubfolderData import VeeSubfolderData
from .VeeSubfolderDataClass import VeeSubfolderDataClass
from .VeeSubfolderDataPrivate import VeeSubfolderDataPrivate
from .VeeSummary import VeeSummary
from .VeeSummaryClass import VeeSummaryClass
from .VeeSummaryPrivate import VeeSummaryPrivate
from .VTrashFolder import VTrashFolder
from .VTrashFolderClass import VTrashFolderClass
from .VTrashFolderPrivate import VTrashFolderPrivate
from .VTrashFolderType import VTrashFolderType
from .WeakRefGroup import WeakRefGroup
from ._encrypt import _encrypt
from ._KeyKey import _KeyKey
from ._LockHelperMsg import _LockHelperMsg
from ._search_flags_t import _search_flags_t
from ._search_match_t import _search_match_t
from ._search_t import _search_t
from ._search_word_t import _search_word_t
from ._sign import _sign
from .__class__ import __class__
from .__search_word import __search_word
from .__search_words import __search_words
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f7b383d5d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Camel-1.2.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Camel', loader=<gi.importer.DynamicImporter object at 0x7f7b383d5d00>)"

