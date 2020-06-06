# encoding: utf-8
# module gi.repository.GMime
# from /usr/lib64/girepository-1.0/GMime-3.0.typelib
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

BINARY_AGE = 207

DISPOSITION_ATTACHMENT = 'attachment'
DISPOSITION_INLINE = 'inline'

FILTER_ENRICHED_IS_RICHTEXT = 1

FILTER_HTML_BLOCKQUOTE_CITATION = 256

FILTER_HTML_CITE = 128

FILTER_HTML_CONVERT_ADDRESSES = 32
FILTER_HTML_CONVERT_NL = 2
FILTER_HTML_CONVERT_SPACES = 4
FILTER_HTML_CONVERT_URLS = 8

FILTER_HTML_ESCAPE_8BIT = 64

FILTER_HTML_MARK_CITATION = 16

FILTER_HTML_PRE = 1

INTERFACE_AGE = 1

MAJOR_VERSION = 3

MICRO_VERSION = 7

MINOR_VERSION = 2

SIGNATURE_STATUS_ERROR_MASK = -8

UUDECODE_STATE_BEGIN = 65536
UUDECODE_STATE_END = 131072
UUDECODE_STATE_INIT = 0
UUDECODE_STATE_MASK = 0

YDECODE_STATE_BEGIN = 4096
YDECODE_STATE_DECODE = 16384
YDECODE_STATE_END = 32768
YDECODE_STATE_EOLN = 256
YDECODE_STATE_ESCAPE = 512
YDECODE_STATE_INIT = 0
YDECODE_STATE_PART = 8192

YENCODE_CRC_INIT = -1

YENCODE_STATE_INIT = 0

_namespace = 'GMime'

_version = '3.0'

__weakref__ = None

# functions

def charset_best(inbuf, inlen): # real signature unknown; restored from __doc__
    """ charset_best(inbuf:str, inlen:int) -> str or None """
    return ""

def charset_canon_name(charset): # real signature unknown; restored from __doc__
    """ charset_canon_name(charset:str) -> str """
    return ""

def charset_iconv_name(charset): # real signature unknown; restored from __doc__
    """ charset_iconv_name(charset:str) -> str """
    return ""

def charset_iso_to_windows(isocharset): # real signature unknown; restored from __doc__
    """ charset_iso_to_windows(isocharset:str) -> str """
    return ""

def charset_language(charset): # real signature unknown; restored from __doc__
    """ charset_language(charset:str) -> str or None """
    return ""

def charset_locale_name(): # real signature unknown; restored from __doc__
    """ charset_locale_name() -> str """
    return ""

def charset_map_init(): # real signature unknown; restored from __doc__
    """ charset_map_init() """
    pass

def charset_map_shutdown(): # real signature unknown; restored from __doc__
    """ charset_map_shutdown() """
    pass

def charset_name(charset): # real signature unknown; restored from __doc__
    """ charset_name(charset:str) -> str """
    return ""

def check_version(major, minor, micro): # real signature unknown; restored from __doc__
    """ check_version(major:int, minor:int, micro:int) -> bool """
    return False

def content_encoding_from_string(p_str): # real signature unknown; restored from __doc__
    """ content_encoding_from_string(str:str) -> GMime.ContentEncoding """
    pass

def content_encoding_to_string(encoding): # real signature unknown; restored from __doc__
    """ content_encoding_to_string(encoding:GMime.ContentEncoding) -> str """
    return ""

def encoding_base64_decode_step(inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_base64_decode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
    return 0

def encoding_base64_encode_close(inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_base64_encode_close(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
    return 0

def encoding_base64_encode_step(inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_base64_encode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
    return 0

def encoding_quoted_decode_step(inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_quoted_decode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
    return 0

def encoding_quoted_encode_close(inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_quoted_encode_close(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
    return 0

def encoding_quoted_encode_step(inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_quoted_encode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
    return 0

def encoding_uudecode_step(inbuf, inlen, outbuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_uudecode_step(inbuf:int, inlen:int, outbuf:int, state:int, save:int) -> int """
    return 0

def encoding_uuencode_close(inbuf, inlen, outbuf, uubuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_uuencode_close(inbuf:int, inlen:int, outbuf:int, uubuf:int, state:int, save:int) -> int """
    return 0

def encoding_uuencode_step(inbuf, inlen, outbuf, uubuf, state, save): # real signature unknown; restored from __doc__
    """ encoding_uuencode_step(inbuf:int, inlen:int, outbuf:int, uubuf:int, state:int, save:int) -> int """
    return 0

def format_options_get_default(): # real signature unknown; restored from __doc__
    """ format_options_get_default() -> GMime.FormatOptions """
    pass

def iconv_locale_to_utf8(p_str): # real signature unknown; restored from __doc__
    """ iconv_locale_to_utf8(str:str) -> str """
    return ""

def iconv_locale_to_utf8_length(p_str, n): # real signature unknown; restored from __doc__
    """ iconv_locale_to_utf8_length(str:str, n:int) -> str """
    return ""

def iconv_utf8_to_locale(p_str): # real signature unknown; restored from __doc__
    """ iconv_utf8_to_locale(str:str) -> str """
    return ""

def iconv_utf8_to_locale_length(p_str, n): # real signature unknown; restored from __doc__
    """ iconv_utf8_to_locale_length(str:str, n:int) -> str """
    return ""

def init(): # real signature unknown; restored from __doc__
    """ init() """
    pass

def locale_charset(): # real signature unknown; restored from __doc__
    """ locale_charset() -> str """
    return ""

def locale_language(): # real signature unknown; restored from __doc__
    """ locale_language() -> str or None """
    return ""

def parser_options_get_default(): # real signature unknown; restored from __doc__
    """ parser_options_get_default() -> GMime.ParserOptions """
    pass

def references_parse(options=None, text): # real signature unknown; restored from __doc__
    """ references_parse(options:GMime.ParserOptions=None, text:str) -> GMime.References """
    pass

def shutdown(): # real signature unknown; restored from __doc__
    """ shutdown() """
    pass

def utils_best_encoding(text): # real signature unknown; restored from __doc__
    """ utils_best_encoding(text:list) -> GMime.ContentEncoding """
    pass

def utils_decode_8bit(options=None, text): # real signature unknown; restored from __doc__
    """ utils_decode_8bit(options:GMime.ParserOptions=None, text:list) -> str """
    return ""

def utils_decode_message_id(message_id): # real signature unknown; restored from __doc__
    """ utils_decode_message_id(message_id:str) -> str """
    return ""

def utils_generate_message_id(fqdn): # real signature unknown; restored from __doc__
    """ utils_generate_message_id(fqdn:str) -> str """
    return ""

def utils_header_decode_date(p_str): # real signature unknown; restored from __doc__
    """ utils_header_decode_date(str:str) -> GLib.DateTime or None """
    pass

def utils_header_decode_phrase(options=None, phrase): # real signature unknown; restored from __doc__
    """ utils_header_decode_phrase(options:GMime.ParserOptions=None, phrase:str) -> str """
    return ""

def utils_header_decode_text(options=None, text): # real signature unknown; restored from __doc__
    """ utils_header_decode_text(options:GMime.ParserOptions=None, text:str) -> str """
    return ""

def utils_header_encode_phrase(options=None, phrase, charset=None): # real signature unknown; restored from __doc__
    """ utils_header_encode_phrase(options:GMime.FormatOptions=None, phrase:str, charset:str=None) -> str """
    return ""

def utils_header_encode_text(options=None, text, charset=None): # real signature unknown; restored from __doc__
    """ utils_header_encode_text(options:GMime.FormatOptions=None, text:str, charset:str=None) -> str """
    return ""

def utils_header_format_date(date): # real signature unknown; restored from __doc__
    """ utils_header_format_date(date:GLib.DateTime) -> str """
    return ""

def utils_header_unfold(value): # real signature unknown; restored from __doc__
    """ utils_header_unfold(value:str) -> str """
    return ""

def utils_quote_string(p_str): # real signature unknown; restored from __doc__
    """ utils_quote_string(str:str) -> str """
    return ""

def utils_structured_header_fold(options=None, format=None, header): # real signature unknown; restored from __doc__
    """ utils_structured_header_fold(options:GMime.ParserOptions=None, format:GMime.FormatOptions=None, header:str) -> str """
    return ""

def utils_text_is_8bit(text): # real signature unknown; restored from __doc__
    """ utils_text_is_8bit(text:list) -> bool """
    return False

def utils_unquote_string(p_str): # real signature unknown; restored from __doc__
    """ utils_unquote_string(str:str) """
    pass

def utils_unstructured_header_fold(options=None, format=None, header): # real signature unknown; restored from __doc__
    """ utils_unstructured_header_fold(options:GMime.ParserOptions=None, format:GMime.FormatOptions=None, header:str) -> str """
    return ""

def ydecode_step(inbuf, inlen, outbuf, state, pcrc, crc): # real signature unknown; restored from __doc__
    """ ydecode_step(inbuf:int, inlen:int, outbuf:int, state:int, pcrc:int, crc:int) -> int """
    return 0

def yencode_close(inbuf, inlen, outbuf, state, pcrc, crc): # real signature unknown; restored from __doc__
    """ yencode_close(inbuf:int, inlen:int, outbuf:int, state:int, pcrc:int, crc:int) -> int """
    return 0

def yencode_step(inbuf, inlen, outbuf, state, pcrc, crc): # real signature unknown; restored from __doc__
    """ yencode_step(inbuf:int, inlen:int, outbuf:int, state:int, pcrc:int, crc:int) -> int """
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

from .AddressType import AddressType
from .Object import Object
from .Part import Part
from .ApplicationPkcs7Mime import ApplicationPkcs7Mime
from .ApplicationPkcs7MimeClass import ApplicationPkcs7MimeClass
from .AutocryptHeader import AutocryptHeader
from .AutocryptHeaderClass import AutocryptHeaderClass
from .AutocryptHeaderList import AutocryptHeaderList
from .AutocryptHeaderListClass import AutocryptHeaderListClass
from .AutocryptPreferEncrypt import AutocryptPreferEncrypt
from .Certificate import Certificate
from .CertificateClass import CertificateClass
from .CertificateList import CertificateList
from .CertificateListClass import CertificateListClass
from .Charset import Charset
from .CipherAlgo import CipherAlgo
from .ContentDisposition import ContentDisposition
from .ContentDispositionClass import ContentDispositionClass
from .ContentEncoding import ContentEncoding
from .ContentType import ContentType
from .ContentTypeClass import ContentTypeClass
from .CryptoContext import CryptoContext
from .CryptoContextClass import CryptoContextClass
from .DataWrapper import DataWrapper
from .DataWrapperClass import DataWrapperClass
from .DecryptFlags import DecryptFlags
from .DecryptResult import DecryptResult
from .DecryptResultClass import DecryptResultClass
from .DigestAlgo import DigestAlgo
from .Encoding import Encoding
from .EncodingConstraint import EncodingConstraint
from .EncryptFlags import EncryptFlags
from .Filter import Filter
from .FilterBasic import FilterBasic
from .FilterBasicClass import FilterBasicClass
from .FilterBest import FilterBest
from .FilterBestClass import FilterBestClass
from .FilterBestFlags import FilterBestFlags
from .FilterCharset import FilterCharset
from .FilterCharsetClass import FilterCharsetClass
from .FilterChecksum import FilterChecksum
from .FilterChecksumClass import FilterChecksumClass
from .FilterClass import FilterClass
from .FilterDos2Unix import FilterDos2Unix
from .FilterDos2UnixClass import FilterDos2UnixClass
from .FilterEnriched import FilterEnriched
from .FilterEnrichedClass import FilterEnrichedClass
from .FilterFrom import FilterFrom
from .FilterFromClass import FilterFromClass
from .FilterFromMode import FilterFromMode
from .FilterGZip import FilterGZip
from .FilterGZipClass import FilterGZipClass
from .FilterGZipMode import FilterGZipMode
from .FilterHTML import FilterHTML
from .FilterHTMLClass import FilterHTMLClass
from .FilterOpenPGP import FilterOpenPGP
from .FilterOpenPGPClass import FilterOpenPGPClass
from .FilterSmtpData import FilterSmtpData
from .FilterSmtpDataClass import FilterSmtpDataClass
from .FilterStrip import FilterStrip
from .FilterStripClass import FilterStripClass
from .FilterUnix2Dos import FilterUnix2Dos
from .FilterUnix2DosClass import FilterUnix2DosClass
from .FilterWindows import FilterWindows
from .FilterWindowsClass import FilterWindowsClass
from .FilterYenc import FilterYenc
from .FilterYencClass import FilterYencClass
from .Format import Format
from .FormatOptions import FormatOptions
from .GpgContext import GpgContext
from .GpgContextClass import GpgContextClass
from .Header import Header
from .HeaderClass import HeaderClass
from .HeaderList import HeaderList
from .HeaderListClass import HeaderListClass
from .InternetAddress import InternetAddress
from .InternetAddressClass import InternetAddressClass
from .InternetAddressGroup import InternetAddressGroup
from .InternetAddressGroupClass import InternetAddressGroupClass
from .InternetAddressList import InternetAddressList
from .InternetAddressListClass import InternetAddressListClass
from .InternetAddressMailbox import InternetAddressMailbox
from .InternetAddressMailboxClass import InternetAddressMailboxClass
from .Message import Message
from .MessageClass import MessageClass
from .MessagePart import MessagePart
from .MessagePartClass import MessagePartClass
from .MessagePartial import MessagePartial
from .MessagePartialClass import MessagePartialClass
from .Multipart import Multipart
from .MultipartClass import MultipartClass
from .MultipartEncrypted import MultipartEncrypted
from .MultipartEncryptedClass import MultipartEncryptedClass
from .MultipartSigned import MultipartSigned
from .MultipartSignedClass import MultipartSignedClass
from .NewLineFormat import NewLineFormat
from .ObjectClass import ObjectClass
from .OpenPGPData import OpenPGPData
from .OpenPGPMarker import OpenPGPMarker
from .OpenPGPState import OpenPGPState
from .Param import Param
from .ParamClass import ParamClass
from .ParamEncodingMethod import ParamEncodingMethod
from .ParamList import ParamList
from .ParamListClass import ParamListClass
from .Parser import Parser
from .ParserClass import ParserClass
from .ParserOptions import ParserOptions
from .ParserWarning import ParserWarning
from .PartClass import PartClass
from .PartIter import PartIter
from .Pkcs7Context import Pkcs7Context
from .Pkcs7ContextClass import Pkcs7ContextClass
from .PubKeyAlgo import PubKeyAlgo
from .References import References
from .RfcComplianceMode import RfcComplianceMode
from .SecureMimeType import SecureMimeType
from .SeekWhence import SeekWhence
from .Signature import Signature
from .SignatureClass import SignatureClass
from .SignatureList import SignatureList
from .SignatureListClass import SignatureListClass
from .SignatureStatus import SignatureStatus
from .Stream import Stream
from .StreamBuffer import StreamBuffer
from .StreamBufferClass import StreamBufferClass
from .StreamBufferMode import StreamBufferMode
from .StreamCat import StreamCat
from .StreamCatClass import StreamCatClass
from .StreamClass import StreamClass
from .StreamFile import StreamFile
from .StreamFileClass import StreamFileClass
from .StreamFilter import StreamFilter
from .StreamFilterClass import StreamFilterClass
from .StreamFs import StreamFs
from .StreamFsClass import StreamFsClass
from .StreamGIO import StreamGIO
from .StreamGIOClass import StreamGIOClass
from .StreamIOVector import StreamIOVector
from .StreamMem import StreamMem
from .StreamMemClass import StreamMemClass
from .StreamMmap import StreamMmap
from .StreamMmapClass import StreamMmapClass
from .StreamNull import StreamNull
from .StreamNullClass import StreamNullClass
from .StreamPipe import StreamPipe
from .StreamPipeClass import StreamPipeClass
from .TextPart import TextPart
from .TextPartClass import TextPartClass
from .Trust import Trust
from .Validity import Validity
from .VerifyFlags import VerifyFlags
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fc97173ad00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GMime-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GMime', loader=<gi.importer.DynamicImporter object at 0x7fc97173ad00>)"

