# encoding: utf-8
# module gi.repository.Soup
# from /usr/lib64/girepository-1.0/Soup-2.4.typelib
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

ADDRESS_ANY_PORT = 0

ADDRESS_FAMILY = 'family'
ADDRESS_NAME = 'name'
ADDRESS_PHYSICAL = 'physical'
ADDRESS_PORT = 'port'
ADDRESS_PROTOCOL = 'protocol'
ADDRESS_SOCKADDR = 'sockaddr'

AUTH_DOMAIN_ADD_PATH = 'add-path'

AUTH_DOMAIN_BASIC_AUTH_CALLBACK = 'auth-callback'
AUTH_DOMAIN_BASIC_AUTH_DATA = 'auth-data'

AUTH_DOMAIN_DIGEST_AUTH_CALLBACK = 'auth-callback'
AUTH_DOMAIN_DIGEST_AUTH_DATA = 'auth-data'

AUTH_DOMAIN_FILTER = 'filter'

AUTH_DOMAIN_FILTER_DATA = 'filter-data'

AUTH_DOMAIN_GENERIC_AUTH_CALLBACK = 'generic-auth-callback'
AUTH_DOMAIN_GENERIC_AUTH_DATA = 'generic-auth-data'

AUTH_DOMAIN_PROXY = 'proxy'
AUTH_DOMAIN_REALM = 'realm'

AUTH_DOMAIN_REMOVE_PATH = 'remove-path'

AUTH_HOST = 'host'

AUTH_IS_AUTHENTICATED = 'is-authenticated'

AUTH_IS_FOR_PROXY = 'is-for-proxy'

AUTH_REALM = 'realm'

AUTH_SCHEME_NAME = 'scheme-name'

CHAR_HTTP_CTL = 16
CHAR_HTTP_SEPARATOR = 8

CHAR_URI_GEN_DELIMS = 2

CHAR_URI_PERCENT_ENCODED = 1

CHAR_URI_SUB_DELIMS = 4

COOKIE_JAR_ACCEPT_POLICY = 'accept-policy'

COOKIE_JAR_DB_FILENAME = 'filename'

COOKIE_JAR_READ_ONLY = 'read-only'

COOKIE_JAR_TEXT_FILENAME = 'filename'

COOKIE_MAX_AGE_ONE_DAY = 0
COOKIE_MAX_AGE_ONE_HOUR = 3600
COOKIE_MAX_AGE_ONE_WEEK = 0
COOKIE_MAX_AGE_ONE_YEAR = 0

FORM_MIME_TYPE_MULTIPART = 'multipart/form-data'
FORM_MIME_TYPE_URLENCODED = 'application/x-www-form-urlencoded'

HSTS_ENFORCER_DB_FILENAME = 'filename'

HSTS_POLICY_MAX_AGE_PAST = 0

LOGGER_LEVEL = 'level'

LOGGER_MAX_BODY_SIZE = 'max-body-size'

MAJOR_VERSION = 2

MESSAGE_FIRST_PARTY = 'first-party'

MESSAGE_FLAGS = 'flags'

MESSAGE_HTTP_VERSION = 'http-version'

MESSAGE_IS_TOP_LEVEL_NAVIGATION = 'is-top-level-navigation'

MESSAGE_METHOD = 'method'
MESSAGE_PRIORITY = 'priority'

MESSAGE_REASON_PHRASE = 'reason-phrase'

MESSAGE_REQUEST_BODY = 'request-body'

MESSAGE_REQUEST_BODY_DATA = 'request-body-data'

MESSAGE_REQUEST_HEADERS = 'request-headers'

MESSAGE_RESPONSE_BODY = 'response-body'

MESSAGE_RESPONSE_BODY_DATA = 'response-body-data'

MESSAGE_RESPONSE_HEADERS = 'response-headers'

MESSAGE_SERVER_SIDE = 'server-side'

MESSAGE_SITE_FOR_COOKIES = 'site-for-cookies'

MESSAGE_STATUS_CODE = 'status-code'

MESSAGE_TLS_CERTIFICATE = 'tls-certificate'
MESSAGE_TLS_ERRORS = 'tls-errors'

MESSAGE_URI = 'uri'

MICRO_VERSION = 0

MINOR_VERSION = 70

REQUEST_SESSION = 'session'
REQUEST_URI = 'uri'

SERVER_ASYNC_CONTEXT = 'async-context'

SERVER_HTTPS_ALIASES = 'https-aliases'

SERVER_HTTP_ALIASES = 'http-aliases'

SERVER_INTERFACE = 'interface'
SERVER_PORT = 'port'

SERVER_RAW_PATHS = 'raw-paths'

SERVER_SERVER_HEADER = 'server-header'

SERVER_SSL_CERT_FILE = 'ssl-cert-file'

SERVER_SSL_KEY_FILE = 'ssl-key-file'

SERVER_TLS_CERTIFICATE = 'tls-certificate'

SESSION_ACCEPT_LANGUAGE = 'accept-language'

SESSION_ACCEPT_LANGUAGE_AUTO = 'accept-language-auto'

SESSION_ASYNC_CONTEXT = 'async-context'

SESSION_HTTPS_ALIASES = 'https-aliases'

SESSION_HTTP_ALIASES = 'http-aliases'

SESSION_IDLE_TIMEOUT = 'idle-timeout'

SESSION_LOCAL_ADDRESS = 'local-address'

SESSION_MAX_CONNS = 'max-conns'

SESSION_MAX_CONNS_PER_HOST = 'max-conns-per-host'

SESSION_PROXY_RESOLVER = 'proxy-resolver'
SESSION_PROXY_URI = 'proxy-uri'

SESSION_SSL_CA_FILE = 'ssl-ca-file'

SESSION_SSL_STRICT = 'ssl-strict'

SESSION_SSL_USE_SYSTEM_CA_FILE = 'ssl-use-system-ca-file'

SESSION_TIMEOUT = 'timeout'

SESSION_TLS_DATABASE = 'tls-database'
SESSION_TLS_INTERACTION = 'tls-interaction'

SESSION_USER_AGENT = 'user-agent'

SESSION_USE_NTLM = 'use-ntlm'

SESSION_USE_THREAD_CONTEXT = 'use-thread-context'

SOCKET_ASYNC_CONTEXT = 'async-context'

SOCKET_FLAG_NONBLOCKING = 'non-blocking'

SOCKET_IS_SERVER = 'is-server'

SOCKET_LOCAL_ADDRESS = 'local-address'

SOCKET_REMOTE_ADDRESS = 'remote-address'

SOCKET_SSL_CREDENTIALS = 'ssl-creds'
SOCKET_SSL_FALLBACK = 'ssl-fallback'
SOCKET_SSL_STRICT = 'ssl-strict'

SOCKET_TIMEOUT = 'timeout'

SOCKET_TLS_CERTIFICATE = 'tls-certificate'
SOCKET_TLS_ERRORS = 'tls-errors'

SOCKET_TRUSTED_CERTIFICATE = 'trusted-certificate'

SOCKET_USE_THREAD_CONTEXT = 'use-thread-context'

VERSION_MIN_REQUIRED = 2

_namespace = 'Soup'

_version = '2.4'

__weakref__ = None

# functions

def check_version(major, minor, micro): # real signature unknown; restored from __doc__
    """ check_version(major:int, minor:int, micro:int) -> bool """
    return False

def cookies_from_request(msg): # real signature unknown; restored from __doc__
    """ cookies_from_request(msg:Soup.Message) -> list """
    return []

def cookies_from_response(msg): # real signature unknown; restored from __doc__
    """ cookies_from_response(msg:Soup.Message) -> list """
    return []

def cookies_to_cookie_header(cookies): # real signature unknown; restored from __doc__
    """ cookies_to_cookie_header(cookies:list) -> str """
    return ""

def cookies_to_request(cookies, msg): # real signature unknown; restored from __doc__
    """ cookies_to_request(cookies:list, msg:Soup.Message) """
    pass

def cookies_to_response(cookies, msg): # real signature unknown; restored from __doc__
    """ cookies_to_response(cookies:list, msg:Soup.Message) """
    pass

def cookie_parse(header, origin): # real signature unknown; restored from __doc__
    """ cookie_parse(header:str, origin:Soup.URI) -> Soup.Cookie or None """
    pass

def form_decode(encoded_form): # real signature unknown; restored from __doc__
    """ form_decode(encoded_form:str) -> dict """
    return {}

def form_decode_multipart(msg, file_control_name=None): # real signature unknown; restored from __doc__
    """ form_decode_multipart(msg:Soup.Message, file_control_name:str=None) -> dict or None, filename:str, content_type:str, file:Soup.Buffer """
    return {}

def form_encode_datalist(form_data_set): # real signature unknown; restored from __doc__
    """ form_encode_datalist(form_data_set:GLib.Data) -> str """
    return ""

def form_encode_hash(form_data_set): # real signature unknown; restored from __doc__
    """ form_encode_hash(form_data_set:dict) -> str """
    return ""

def form_request_new_from_datalist(method, uri, form_data_set): # real signature unknown; restored from __doc__
    """ form_request_new_from_datalist(method:str, uri:str, form_data_set:GLib.Data) -> Soup.Message """
    pass

def form_request_new_from_hash(method, uri, form_data_set): # real signature unknown; restored from __doc__
    """ form_request_new_from_hash(method:str, uri:str, form_data_set:dict) -> Soup.Message """
    pass

def form_request_new_from_multipart(uri, multipart): # real signature unknown; restored from __doc__
    """ form_request_new_from_multipart(uri:str, multipart:Soup.Multipart) -> Soup.Message """
    pass

def get_major_version(): # real signature unknown; restored from __doc__
    """ get_major_version() -> int """
    return 0

def get_micro_version(): # real signature unknown; restored from __doc__
    """ get_micro_version() -> int """
    return 0

def get_minor_version(): # real signature unknown; restored from __doc__
    """ get_minor_version() -> int """
    return 0

def headers_parse(p_str, len, dest): # real signature unknown; restored from __doc__
    """ headers_parse(str:str, len:int, dest:Soup.MessageHeaders) -> bool """
    return False

def headers_parse_request(p_str, len, req_headers): # real signature unknown; restored from __doc__
    """ headers_parse_request(str:str, len:int, req_headers:Soup.MessageHeaders) -> int, req_method:str, req_path:str, ver:Soup.HTTPVersion """
    return 0

def headers_parse_response(p_str, len, headers): # real signature unknown; restored from __doc__
    """ headers_parse_response(str:str, len:int, headers:Soup.MessageHeaders) -> bool, ver:Soup.HTTPVersion, status_code:int, reason_phrase:str """
    return False

def headers_parse_status_line(status_line): # real signature unknown; restored from __doc__
    """ headers_parse_status_line(status_line:str) -> bool, ver:Soup.HTTPVersion, status_code:int, reason_phrase:str """
    return False

def header_contains(header, token): # real signature unknown; restored from __doc__
    """ header_contains(header:str, token:str) -> bool """
    return False

def header_free_param_list(param_list): # real signature unknown; restored from __doc__
    """ header_free_param_list(param_list:dict) """
    pass

def header_g_string_append_param(string, name, value): # real signature unknown; restored from __doc__
    """ header_g_string_append_param(string:GLib.String, name:str, value:str) """
    pass

def header_g_string_append_param_quoted(string, name, value): # real signature unknown; restored from __doc__
    """ header_g_string_append_param_quoted(string:GLib.String, name:str, value:str) """
    pass

def header_parse_list(header): # real signature unknown; restored from __doc__
    """ header_parse_list(header:str) -> list """
    return []

def header_parse_param_list(header): # real signature unknown; restored from __doc__
    """ header_parse_param_list(header:str) -> dict """
    return {}

def header_parse_param_list_strict(header): # real signature unknown; restored from __doc__
    """ header_parse_param_list_strict(header:str) -> dict or None """
    return {}

def header_parse_quality_list(header): # real signature unknown; restored from __doc__
    """ header_parse_quality_list(header:str) -> list, unacceptable:list """
    return []

def header_parse_semi_param_list(header): # real signature unknown; restored from __doc__
    """ header_parse_semi_param_list(header:str) -> dict """
    return {}

def header_parse_semi_param_list_strict(header): # real signature unknown; restored from __doc__
    """ header_parse_semi_param_list_strict(header:str) -> dict or None """
    return {}

def http_error_quark(): # real signature unknown; restored from __doc__
    """ http_error_quark() -> int """
    return 0

def message_headers_iter_init(hdrs): # real signature unknown; restored from __doc__
    """ message_headers_iter_init(hdrs:Soup.MessageHeaders) -> iter:Soup.MessageHeadersIter """
    pass

def requester_error_quark(): # real signature unknown; restored from __doc__
    """ requester_error_quark() -> int """
    return 0

def request_error_quark(): # real signature unknown; restored from __doc__
    """ request_error_quark() -> int """
    return 0

def status_get_phrase(status_code): # real signature unknown; restored from __doc__
    """ status_get_phrase(status_code:int) -> str """
    return ""

def status_proxify(status_code): # real signature unknown; restored from __doc__
    """ status_proxify(status_code:int) -> int """
    return 0

def str_case_equal(v1=None, v2=None): # real signature unknown; restored from __doc__
    """ str_case_equal(v1=None, v2=None) -> bool """
    return False

def str_case_hash(key=None): # real signature unknown; restored from __doc__
    """ str_case_hash(key=None) -> int """
    return 0

def tld_domain_is_public_suffix(domain): # real signature unknown; restored from __doc__
    """ tld_domain_is_public_suffix(domain:str) -> bool """
    return False

def tld_error_quark(): # real signature unknown; restored from __doc__
    """ tld_error_quark() -> int """
    return 0

def tld_get_base_domain(hostname): # real signature unknown; restored from __doc__
    """ tld_get_base_domain(hostname:str) -> str """
    return ""

def uri_decode(part): # real signature unknown; restored from __doc__
    """ uri_decode(part:str) -> str """
    return ""

def uri_encode(part, escape_extra=None): # real signature unknown; restored from __doc__
    """ uri_encode(part:str, escape_extra:str=None) -> str """
    return ""

def uri_normalize(part, unescape_extra=None): # real signature unknown; restored from __doc__
    """ uri_normalize(part:str, unescape_extra:str=None) -> str """
    return ""

def value_array_new(): # real signature unknown; restored from __doc__
    """ value_array_new() -> GObject.ValueArray """
    pass

def value_hash_insert_value(hash, key, value): # real signature unknown; restored from __doc__
    """ value_hash_insert_value(hash:dict, key:str, value:GObject.Value) """
    pass

def value_hash_new(): # real signature unknown; restored from __doc__
    """ value_hash_new() -> dict """
    return {}

def websocket_client_prepare_handshake(msg, origin=None, protocols=None): # real signature unknown; restored from __doc__
    """ websocket_client_prepare_handshake(msg:Soup.Message, origin:str=None, protocols:list=None) """
    pass

def websocket_client_prepare_handshake_with_extensions(msg, origin=None, protocols=None, supported_extensions=None): # real signature unknown; restored from __doc__
    """ websocket_client_prepare_handshake_with_extensions(msg:Soup.Message, origin:str=None, protocols:list=None, supported_extensions:list=None) """
    pass

def websocket_client_verify_handshake(msg): # real signature unknown; restored from __doc__
    """ websocket_client_verify_handshake(msg:Soup.Message) -> bool """
    return False

def websocket_client_verify_handshake_with_extensions(msg, supported_extensions=None): # real signature unknown; restored from __doc__
    """ websocket_client_verify_handshake_with_extensions(msg:Soup.Message, supported_extensions:list=None) -> bool, accepted_extensions:list """
    return False

def websocket_error_get_quark(): # real signature unknown; restored from __doc__
    """ websocket_error_get_quark() -> int """
    return 0

def websocket_server_check_handshake(msg, origin=None, protocols=None): # real signature unknown; restored from __doc__
    """ websocket_server_check_handshake(msg:Soup.Message, origin:str=None, protocols:list=None) -> bool """
    return False

def websocket_server_check_handshake_with_extensions(msg, origin=None, protocols=None, supported_extensions=None): # real signature unknown; restored from __doc__
    """ websocket_server_check_handshake_with_extensions(msg:Soup.Message, origin:str=None, protocols:list=None, supported_extensions:list=None) -> bool """
    return False

def websocket_server_process_handshake(msg, expected_origin=None, protocols=None): # real signature unknown; restored from __doc__
    """ websocket_server_process_handshake(msg:Soup.Message, expected_origin:str=None, protocols:list=None) -> bool """
    return False

def websocket_server_process_handshake_with_extensions(msg, expected_origin=None, protocols=None, supported_extensions=None): # real signature unknown; restored from __doc__
    """ websocket_server_process_handshake_with_extensions(msg:Soup.Message, expected_origin:str=None, protocols:list=None, supported_extensions:list=None) -> bool, accepted_extensions:list """
    return False

def xmlrpc_build_method_call(method_name, params): # real signature unknown; restored from __doc__
    """ xmlrpc_build_method_call(method_name:str, params:list) -> str or None """
    return ""

def xmlrpc_build_method_response(value): # real signature unknown; restored from __doc__
    """ xmlrpc_build_method_response(value:GObject.Value) -> str or None """
    return ""

def xmlrpc_build_request(method_name, params): # real signature unknown; restored from __doc__
    """ xmlrpc_build_request(method_name:str, params:GLib.Variant) -> str """
    return ""

def xmlrpc_build_response(value): # real signature unknown; restored from __doc__
    """ xmlrpc_build_response(value:GLib.Variant) -> str """
    return ""

def xmlrpc_error_quark(): # real signature unknown; restored from __doc__
    """ xmlrpc_error_quark() -> int """
    return 0

def xmlrpc_fault_quark(): # real signature unknown; restored from __doc__
    """ xmlrpc_fault_quark() -> int """
    return 0

def xmlrpc_message_new(uri, method_name, params): # real signature unknown; restored from __doc__
    """ xmlrpc_message_new(uri:str, method_name:str, params:GLib.Variant) -> Soup.Message """
    pass

def xmlrpc_message_set_response(msg, value): # real signature unknown; restored from __doc__
    """ xmlrpc_message_set_response(msg:Soup.Message, value:GLib.Variant) -> bool """
    return False

def xmlrpc_parse_method_call(method_call, length): # real signature unknown; restored from __doc__
    """ xmlrpc_parse_method_call(method_call:str, length:int) -> bool, method_name:str, params:GObject.ValueArray """
    return False

def xmlrpc_parse_method_response(method_response, length): # real signature unknown; restored from __doc__
    """ xmlrpc_parse_method_response(method_response:str, length:int) -> bool, value:GObject.Value """
    return False

def xmlrpc_parse_request(method_call, length): # real signature unknown; restored from __doc__
    """ xmlrpc_parse_request(method_call:str, length:int) -> str, params:Soup.XMLRPCParams """
    return ""

def xmlrpc_parse_response(method_response, length, signature=None): # real signature unknown; restored from __doc__
    """ xmlrpc_parse_response(method_response:str, length:int, signature:str=None) -> GLib.Variant """
    pass

def xmlrpc_variant_get_datetime(variant): # real signature unknown; restored from __doc__
    """ xmlrpc_variant_get_datetime(variant:GLib.Variant) -> Soup.Date """
    pass

def xmlrpc_variant_new_datetime(date): # real signature unknown; restored from __doc__
    """ xmlrpc_variant_new_datetime(date:Soup.Date) -> GLib.Variant """
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

from .Address import Address
from .AddressClass import AddressClass
from .AddressFamily import AddressFamily
from .Auth import Auth
from .AuthBasic import AuthBasic
from .AuthClass import AuthClass
from .AuthDigest import AuthDigest
from .AuthDomain import AuthDomain
from .AuthDomainBasic import AuthDomainBasic
from .AuthDomainBasicClass import AuthDomainBasicClass
from .AuthDomainClass import AuthDomainClass
from .AuthDomainDigest import AuthDomainDigest
from .AuthDomainDigestClass import AuthDomainDigestClass
from .SessionFeature import SessionFeature
from .AuthManager import AuthManager
from .AuthManagerClass import AuthManagerClass
from .AuthManagerPrivate import AuthManagerPrivate
from .AuthNegotiate import AuthNegotiate
from .AuthNTLM import AuthNTLM
from .Buffer import Buffer
from .ByteArray import ByteArray
from .Cache import Cache
from .Cacheability import Cacheability
from .CacheClass import CacheClass
from .CachePrivate import CachePrivate
from .CacheResponse import CacheResponse
from .CacheType import CacheType
from .ClientContext import ClientContext
from .Connection import Connection
from .ConnectionState import ConnectionState
from .ContentDecoder import ContentDecoder
from .ContentDecoderClass import ContentDecoderClass
from .ContentDecoderPrivate import ContentDecoderPrivate
from .ContentSniffer import ContentSniffer
from .ContentSnifferClass import ContentSnifferClass
from .ContentSnifferPrivate import ContentSnifferPrivate
from .Cookie import Cookie
from .CookieJar import CookieJar
from .CookieJarAcceptPolicy import CookieJarAcceptPolicy
from .CookieJarClass import CookieJarClass
from .CookieJarDB import CookieJarDB
from .CookieJarDBClass import CookieJarDBClass
from .CookieJarText import CookieJarText
from .CookieJarTextClass import CookieJarTextClass
from .Date import Date
from .DateFormat import DateFormat
from .Encoding import Encoding
from .Expectation import Expectation
from .HSTSEnforcer import HSTSEnforcer
from .HSTSEnforcerClass import HSTSEnforcerClass
from .HSTSEnforcerDB import HSTSEnforcerDB
from .HSTSEnforcerDBClass import HSTSEnforcerDBClass
from .HSTSEnforcerDBPrivate import HSTSEnforcerDBPrivate
from .HSTSEnforcerPrivate import HSTSEnforcerPrivate
from .HSTSPolicy import HSTSPolicy
from .HTTPVersion import HTTPVersion
from .KnownStatusCode import KnownStatusCode
from .Logger import Logger
from .LoggerClass import LoggerClass
from .LoggerLogLevel import LoggerLogLevel
from .MemoryUse import MemoryUse
from .Message import Message
from .MessageBody import MessageBody
from .MessageClass import MessageClass
from .MessageFlags import MessageFlags
from .MessageHeaders import MessageHeaders
from .MessageHeadersIter import MessageHeadersIter
from .MessageHeadersType import MessageHeadersType
from .MessagePriority import MessagePriority
from .MessageQueue import MessageQueue
from .MessageQueueItem import MessageQueueItem
from .Multipart import Multipart
from .MultipartInputStream import MultipartInputStream
from .MultipartInputStreamClass import MultipartInputStreamClass
from .MultipartInputStreamPrivate import MultipartInputStreamPrivate
from .PasswordManager import PasswordManager
from .PasswordManagerInterface import PasswordManagerInterface
from .ProxyResolver import ProxyResolver
from .ProxyURIResolver import ProxyURIResolver
from .ProxyResolverDefault import ProxyResolverDefault
from .ProxyResolverDefaultClass import ProxyResolverDefaultClass
from .ProxyResolverInterface import ProxyResolverInterface
from .ProxyURIResolverInterface import ProxyURIResolverInterface
from .Range import Range
from .Request import Request
from .RequestClass import RequestClass
from .RequestData import RequestData
from .RequestDataClass import RequestDataClass
from .RequestDataPrivate import RequestDataPrivate
from .Requester import Requester
from .RequesterClass import RequesterClass
from .RequesterError import RequesterError
from .RequesterPrivate import RequesterPrivate
from .RequestError import RequestError
from .RequestFile import RequestFile
from .RequestFileClass import RequestFileClass
from .RequestFilePrivate import RequestFilePrivate
from .RequestHTTP import RequestHTTP
from .RequestHTTPClass import RequestHTTPClass
from .RequestHTTPPrivate import RequestHTTPPrivate
from .RequestPrivate import RequestPrivate
from .SameSitePolicy import SameSitePolicy
from .Server import Server
from .ServerClass import ServerClass
from .ServerListenOptions import ServerListenOptions
from .Session import Session
from .SessionAsync import SessionAsync
from .SessionAsyncClass import SessionAsyncClass
from .SessionClass import SessionClass
from .SessionFeatureInterface import SessionFeatureInterface
from .SessionSync import SessionSync
from .SessionSyncClass import SessionSyncClass
from .Socket import Socket
from .SocketClass import SocketClass
from .SocketIOStatus import SocketIOStatus
from .Status import Status
from .TLDError import TLDError
from .URI import URI
from .WebsocketCloseCode import WebsocketCloseCode
from .WebsocketConnection import WebsocketConnection
from .WebsocketConnectionClass import WebsocketConnectionClass
from .WebsocketConnectionPrivate import WebsocketConnectionPrivate
from .WebsocketConnectionType import WebsocketConnectionType
from .WebsocketDataType import WebsocketDataType
from .WebsocketError import WebsocketError
from .WebsocketExtension import WebsocketExtension
from .WebsocketExtensionClass import WebsocketExtensionClass
from .WebsocketExtensionDeflate import WebsocketExtensionDeflate
from .WebsocketExtensionDeflateClass import WebsocketExtensionDeflateClass
from .WebsocketExtensionManager import WebsocketExtensionManager
from .WebsocketExtensionManagerClass import WebsocketExtensionManagerClass
from .WebsocketState import WebsocketState
from .XMLRPCError import XMLRPCError
from .XMLRPCFault import XMLRPCFault
from .XMLRPCParams import XMLRPCParams
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f8e4948bd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Soup-2.4.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Soup', loader=<gi.importer.DynamicImporter object at 0x7f8e4948bd00>)"

