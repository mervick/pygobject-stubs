# encoding: utf-8
# module gi.repository.Gsf
# from /usr/lib64/girepository-1.0/Gsf-1.typelib
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

META_NAME_BYTE_COUNT = 'gsf:byte-count'

META_NAME_CASE_SENSITIVE = 'gsf:case-sensitivity'

META_NAME_CATEGORY = 'gsf:category'

META_NAME_CELL_COUNT = 'gsf:cell-count'

META_NAME_CHARACTER_COUNT = 'gsf:character-count'

META_NAME_CODEPAGE = 'msole:codepage'
META_NAME_COMPANY = 'dc:publisher'
META_NAME_CREATOR = 'dc:creator'

META_NAME_DATE_CREATED = 'meta:creation-date'
META_NAME_DATE_MODIFIED = 'dc:date'

META_NAME_DESCRIPTION = 'dc:description'
META_NAME_DICTIONARY = 'gsf:dictionary'

META_NAME_DOCUMENT_PARTS = 'gsf:document-parts'

META_NAME_EDITING_DURATION = 'meta:editing-duration'

META_NAME_GENERATOR = 'meta:generator'

META_NAME_HEADING_PAIRS = 'gsf:heading-pairs'

META_NAME_HIDDEN_SLIDE_COUNT = 'gsf:hidden-slide-count'

META_NAME_IMAGE_COUNT = 'gsf:image-count'

META_NAME_INITIAL_CREATOR = 'meta:initial-creator'

META_NAME_KEYWORD = 'meta:keyword'
META_NAME_KEYWORDS = 'dc:keywords'
META_NAME_LANGUAGE = 'dc:language'

META_NAME_LAST_PRINTED = 'gsf:last-printed'

META_NAME_LAST_SAVED_BY = 'gsf:last-saved-by'

META_NAME_LINE_COUNT = 'gsf:line-count'

META_NAME_LINKS_DIRTY = 'gsf:links-dirty'

META_NAME_LOCALE_SYSTEM_DEFAULT = 'gsf:default-locale'

META_NAME_MANAGER = 'gsf:manager'

META_NAME_MM_CLIP_COUNT = 'gsf:MM-clip-count'

META_NAME_MSOLE_UNKNOWN_17 = 'msole:unknown-doc-17'
META_NAME_MSOLE_UNKNOWN_18 = 'msole:unknown-doc-18'
META_NAME_MSOLE_UNKNOWN_19 = 'msole:unknown-doc-19'
META_NAME_MSOLE_UNKNOWN_20 = 'msole:unknown-doc-20'
META_NAME_MSOLE_UNKNOWN_21 = 'msole:unknown-doc-21'
META_NAME_MSOLE_UNKNOWN_22 = 'msole:unknown-doc-22'
META_NAME_MSOLE_UNKNOWN_23 = 'msole:unknown-doc-23'

META_NAME_NOTE_COUNT = 'gsf:note-count'

META_NAME_OBJECT_COUNT = 'gsf:object-count'

META_NAME_PAGE_COUNT = 'gsf:page-count'

META_NAME_PARAGRAPH_COUNT = 'gsf:paragraph-count'

META_NAME_PRESENTATION_FORMAT = 'gsf:presentation-format'

META_NAME_PRINTED_BY = 'meta:printed-by'

META_NAME_PRINT_DATE = 'meta:print-date'

META_NAME_REVISION_COUNT = 'meta:editing-cycles'

META_NAME_SCALE = 'gsf:scale'
META_NAME_SECURITY = 'gsf:security'

META_NAME_SLIDE_COUNT = 'gsf:slide-count'

META_NAME_SPREADSHEET_COUNT = 'gsf:spreadsheet-count'

META_NAME_SUBJECT = 'dc:subject'

META_NAME_TABLE_COUNT = 'gsf:table-count'

META_NAME_TEMPLATE = 'meta:template'
META_NAME_THUMBNAIL = 'gsf:thumbnail'
META_NAME_TITLE = 'dc:title'

META_NAME_WORD_COUNT = 'gsf:word-count'

_namespace = 'Gsf'

_version = '1'

__weakref__ = None

# functions

def base64_decode_simple(data, len): # real signature unknown; restored from __doc__
    """ base64_decode_simple(data:list, len:int) -> int """
    return 0

def base64_decode_step(in_, len, out, state, save): # real signature unknown; restored from __doc__
    """ base64_decode_step(in_:list, len:int, out:list, state:int, save:int) -> int, state:int, save:int """
    return 0

def base64_encode_close(in_, break_lines, out, state, save): # real signature unknown; restored from __doc__
    """ base64_encode_close(in_:list, break_lines:bool, out:list, state:int, save:int) -> int, state:int, save:int """
    return 0

def base64_encode_simple(data, len): # real signature unknown; restored from __doc__
    """ base64_encode_simple(data:list, len:int) -> int """
    return 0

def base64_encode_step(in_, len, break_lines, out, state, save): # real signature unknown; restored from __doc__
    """ base64_encode_step(in_:list, len:int, break_lines:bool, out:list, state:int, save:int) -> int, state:int, save:int """
    return 0

def debug_flag(flag): # real signature unknown; restored from __doc__
    """ debug_flag(flag:str) -> bool """
    return False

def doc_meta_dump(meta): # real signature unknown; restored from __doc__
    """ doc_meta_dump(meta:Gsf.DocMetaData) """
    pass

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def extension_pointer(path): # real signature unknown; restored from __doc__
    """ extension_pointer(path:str) -> str """
    return ""

def filename_to_utf8(filename, quoted): # real signature unknown; restored from __doc__
    """ filename_to_utf8(filename:str, quoted:bool) -> str """
    return ""

def init(): # real signature unknown; restored from __doc__
    """ init() """
    pass

def init_dynamic(module): # real signature unknown; restored from __doc__
    """ init_dynamic(module:GObject.TypeModule) """
    pass

def le_get_double(p=None): # real signature unknown; restored from __doc__
    """ le_get_double(p=None) -> float """
    return 0.0

def le_get_float(p=None): # real signature unknown; restored from __doc__
    """ le_get_float(p=None) -> float """
    return 0.0

def le_get_guint64(p=None): # real signature unknown; restored from __doc__
    """ le_get_guint64(p=None) -> int """
    return 0

def le_set_double(p=None, d): # real signature unknown; restored from __doc__
    """ le_set_double(p=None, d:float) """
    pass

def le_set_float(p=None, f): # real signature unknown; restored from __doc__
    """ le_set_float(p=None, f:float) """
    pass

def mem_dump(ptr, len): # real signature unknown; restored from __doc__
    """ mem_dump(ptr:int, len:int) """
    pass

def msole_codepage_to_lid(codepage): # real signature unknown; restored from __doc__
    """ msole_codepage_to_lid(codepage:int) -> int """
    return 0

def msole_iconv_win_codepage(): # real signature unknown; restored from __doc__
    """ msole_iconv_win_codepage() -> int """
    return 0

def msole_inflate(input, offset): # real signature unknown; restored from __doc__
    """ msole_inflate(input:Gsf.Input, offset:int) -> list """
    return []

def msole_language_for_lid(lid): # real signature unknown; restored from __doc__
    """ msole_language_for_lid(lid:int) -> str """
    return ""

def msole_lid_for_language(lang=None): # real signature unknown; restored from __doc__
    """ msole_lid_for_language(lang:str=None) -> int """
    return 0

def msole_lid_to_codepage(lid): # real signature unknown; restored from __doc__
    """ msole_lid_to_codepage(lid:int) -> int """
    return 0

def msole_lid_to_codepage_str(lid): # real signature unknown; restored from __doc__
    """ msole_lid_to_codepage_str(lid:int) -> str """
    return ""

def odf_get_ns(): # real signature unknown; restored from __doc__
    """ odf_get_ns() -> Gsf.XMLInNS """
    pass

def odf_get_version(): # real signature unknown; restored from __doc__
    """ odf_get_version() -> int """
    return 0

def odf_get_version_string(): # real signature unknown; restored from __doc__
    """ odf_get_version_string() -> str """
    return ""

def open_pkg_error_id(): # real signature unknown; restored from __doc__
    """ open_pkg_error_id() -> int """
    return 0

def open_pkg_foreach_rel(opkg, func, user_data=None): # real signature unknown; restored from __doc__
    """ open_pkg_foreach_rel(opkg:Gsf.Input, func:Gsf.OpenPkgIter, user_data=None) """
    pass

def open_pkg_open_rel(opkg, rel): # real signature unknown; restored from __doc__
    """ open_pkg_open_rel(opkg:Gsf.Input, rel:Gsf.OpenPkgRel) -> Gsf.Input """
    pass

def open_pkg_open_rel_by_id(opkg, id): # real signature unknown; restored from __doc__
    """ open_pkg_open_rel_by_id(opkg:Gsf.Input, id:str) -> Gsf.Input """
    pass

def open_pkg_open_rel_by_type(opkg, type): # real signature unknown; restored from __doc__
    """ open_pkg_open_rel_by_type(opkg:Gsf.Input, type:str) -> Gsf.Input """
    pass

def open_pkg_parse_rel_by_id(xin, id, dtd, ns): # real signature unknown; restored from __doc__
    """ open_pkg_parse_rel_by_id(xin:Gsf.XMLIn, id:str, dtd:Gsf.XMLInNode, ns:Gsf.XMLInNS) -> error """
    pass

def property_settings_find(name, params): # real signature unknown; restored from __doc__
    """ property_settings_find(name:str, params:list) -> GObject.Parameter """
    pass

def property_settings_free(params): # real signature unknown; restored from __doc__
    """ property_settings_free(params:list) """
    pass

def shutdown(): # real signature unknown; restored from __doc__
    """ shutdown() """
    pass

def shutdown_dynamic(module): # real signature unknown; restored from __doc__
    """ shutdown_dynamic(module:GObject.TypeModule) """
    pass

def value_get_docprop_array(value): # real signature unknown; restored from __doc__
    """ value_get_docprop_array(value:GObject.Value) -> list or None """
    return []

def value_get_docprop_varray(value): # real signature unknown; restored from __doc__
    """ value_get_docprop_varray(value:GObject.Value) -> GObject.ValueArray """
    pass

def value_get_docprop_vector(value): # real signature unknown; restored from __doc__
    """ value_get_docprop_vector(value:GObject.Value) -> Gsf.DocPropVector """
    pass

def vba_inflate(input, offset, size, add_null_terminator): # real signature unknown; restored from __doc__
    """ vba_inflate(input:Gsf.Input, offset:int, size:int, add_null_terminator:bool) -> int """
    return 0

def xmlDocFormatDump(output, cur, encoding=None, format): # real signature unknown; restored from __doc__
    """ xmlDocFormatDump(output:Gsf.Output, cur:libxml2.Doc, encoding:str=None, format:bool) -> int """
    return 0

def xml_gvalue_from_str(res, t, p_str): # real signature unknown; restored from __doc__
    """ xml_gvalue_from_str(res:GObject.Value, t:GType, str:str) -> bool """
    return False

def xml_probe(input, func): # real signature unknown; restored from __doc__
    """ xml_probe(input:Gsf.Input, func:Gsf.XMLProbeFunc) -> bool """
    return False

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

from .Blob import Blob
from .BlobClass import BlobClass
from .BlobPrivate import BlobPrivate
from .ClipData import ClipData
from .ClipDataClass import ClipDataClass
from .ClipDataPrivate import ClipDataPrivate
from .ClipFormat import ClipFormat
from .ClipFormatWindows import ClipFormatWindows
from .DocMetaData import DocMetaData
from .DocProp import DocProp
from .DocPropVector import DocPropVector
from .Error import Error
from .Input import Input
from .Infile import Infile
from .InfileClass import InfileClass
from .InfileMSOle import InfileMSOle
from .InfileMSVBA import InfileMSVBA
from .InfileStdio import InfileStdio
from .InfileTar import InfileTar
from .InfileZip import InfileZip
from .InputClass import InputClass
from .InputGio import InputGio
from .InputGZip import InputGZip
from .InputHTTP import InputHTTP
from .InputMemory import InputMemory
from .InputProxy import InputProxy
from .InputStdio import InputStdio
from .InputTextline import InputTextline
from .MSOleSortingKey import MSOleSortingKey
from .XMLOut import XMLOut
from .ODFOut import ODFOut
from .ODFOutClass import ODFOutClass
from .OpenPkgRel import OpenPkgRel
from .OpenPkgRels import OpenPkgRels
from .Output import Output
from .Outfile import Outfile
from .OutfileClass import OutfileClass
from .OutfileMSOle import OutfileMSOle
from .OutfileOpenPkg import OutfileOpenPkg
from .OutfileStdio import OutfileStdio
from .OutfileZip import OutfileZip
from .OutputBzip import OutputBzip
from .OutputClass import OutputClass
from .OutputCsv import OutputCsv
from .OutputCsvClass import OutputCsvClass
from .OutputCsvQuotingMode import OutputCsvQuotingMode
from .OutputGio import OutputGio
from .OutputGZip import OutputGZip
from .OutputIconv import OutputIconv
from .OutputIconvClass import OutputIconvClass
from .OutputIOChannel import OutputIOChannel
from .OutputMemory import OutputMemory
from .OutputStdio import OutputStdio
from .SharedMemory import SharedMemory
from .StructuredBlob import StructuredBlob
from .Timestamp import Timestamp
from .XMLBlob import XMLBlob
from .XMLContent import XMLContent
from .XMLIn import XMLIn
from .XMLInDoc import XMLInDoc
from .XMLInNode import XMLInNode
from .XMLInNS import XMLInNS
from .XMLOutClass import XMLOutClass
from .ZipCompressionMethod import ZipCompressionMethod
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f95c5809d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gsf-1.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gsf', loader=<gi.importer.DynamicImporter object at 0x7f95c5809d00>)"

