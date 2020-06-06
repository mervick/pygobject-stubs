# encoding: utf-8
# module gi.repository.EvinceDocument
# from /usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib
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

MAJOR_VERSION = 3

MICRO_VERSION = 3

MINOR_VERSION = 36

_namespace = 'EvinceDocument'

_version = '3.0'

__weakref__ = None

# functions

def backends_manager_get_document(mime_type): # real signature unknown; restored from __doc__
    """ backends_manager_get_document(mime_type:str) -> EvinceDocument.Document """
    pass

def backends_manager_get_document_module_name(document): # real signature unknown; restored from __doc__
    """ backends_manager_get_document_module_name(document:EvinceDocument.Document) -> str """
    return ""

def document_error_quark(): # real signature unknown; restored from __doc__
    """ document_error_quark() -> int """
    return 0

def file_compress(uri, type): # real signature unknown; restored from __doc__
    """ file_compress(uri:str, type:EvinceDocument.CompressionType) -> str """
    return ""

def file_copy_metadata(from_, to): # real signature unknown; restored from __doc__
    """ file_copy_metadata(from_:str, to:str) -> bool """
    return False

def file_get_mime_type(uri, fast): # real signature unknown; restored from __doc__
    """ file_get_mime_type(uri:str, fast:bool) -> str """
    return ""

def file_is_temp(file): # real signature unknown; restored from __doc__
    """ file_is_temp(file:Gio.File) -> bool """
    return False

def file_uncompress(uri, type): # real signature unknown; restored from __doc__
    """ file_uncompress(uri:str, type:EvinceDocument.CompressionType) -> str """
    return ""

def get_locale_dir(): # real signature unknown; restored from __doc__
    """ get_locale_dir() -> str """
    return ""

def init(): # real signature unknown; restored from __doc__
    """ init() -> bool """
    return False

def mkdtemp(tmpl): # real signature unknown; restored from __doc__
    """ mkdtemp(tmpl:str) -> str """
    return ""

def mkstemp(tmpl, file_name): # real signature unknown; restored from __doc__
    """ mkstemp(tmpl:str, file_name:str) -> int """
    return 0

def mkstemp_file(tmpl): # real signature unknown; restored from __doc__
    """ mkstemp_file(tmpl:str) -> Gio.File """
    pass

def rect_cmp(a, b): # real signature unknown; restored from __doc__
    """ rect_cmp(a:EvinceDocument.Rectangle, b:EvinceDocument.Rectangle) -> int """
    return 0

def shutdown(): # real signature unknown; restored from __doc__
    """ shutdown() """
    pass

def tmp_filename_unlink(filename): # real signature unknown; restored from __doc__
    """ tmp_filename_unlink(filename:str) """
    pass

def tmp_file_unlink(file): # real signature unknown; restored from __doc__
    """ tmp_file_unlink(file:Gio.File) """
    pass

def tmp_uri_unlink(uri): # real signature unknown; restored from __doc__
    """ tmp_uri_unlink(uri:str) """
    pass

def xfer_uri_simple(from_, to): # real signature unknown; restored from __doc__
    """ xfer_uri_simple(from_:str, to:str) -> bool """
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

from .Annotation import Annotation
from .AnnotationMarkup import AnnotationMarkup
from .AnnotationAttachment import AnnotationAttachment
from .AnnotationAttachmentClass import AnnotationAttachmentClass
from .AnnotationClass import AnnotationClass
from .AnnotationMarkupInterface import AnnotationMarkupInterface
from .AnnotationsSaveMask import AnnotationsSaveMask
from .AnnotationText import AnnotationText
from .AnnotationTextClass import AnnotationTextClass
from .AnnotationTextIcon import AnnotationTextIcon
from .AnnotationTextMarkup import AnnotationTextMarkup
from .AnnotationTextMarkupClass import AnnotationTextMarkupClass
from .AnnotationTextMarkupType import AnnotationTextMarkupType
from .AnnotationType import AnnotationType
from .AsyncRenderer import AsyncRenderer
from .AsyncRendererInterface import AsyncRendererInterface
from .Attachment import Attachment
from .AttachmentClass import AttachmentClass
from .CompressionType import CompressionType
from .Document import Document
from .DocumentAnnotations import DocumentAnnotations
from .DocumentAnnotationsInterface import DocumentAnnotationsInterface
from .DocumentAttachments import DocumentAttachments
from .DocumentAttachmentsInterface import DocumentAttachmentsInterface
from .DocumentBackendInfo import DocumentBackendInfo
from .DocumentClass import DocumentClass
from .DocumentError import DocumentError
from .DocumentFind import DocumentFind
from .DocumentFindInterface import DocumentFindInterface
from .DocumentFonts import DocumentFonts
from .DocumentFontsInterface import DocumentFontsInterface
from .DocumentForms import DocumentForms
from .DocumentFormsInterface import DocumentFormsInterface
from .DocumentImages import DocumentImages
from .DocumentImagesInterface import DocumentImagesInterface
from .DocumentInfo import DocumentInfo
from .DocumentInfoFields import DocumentInfoFields
from .DocumentLayers import DocumentLayers
from .DocumentLayersInterface import DocumentLayersInterface
from .DocumentLayout import DocumentLayout
from .DocumentLicense import DocumentLicense
from .DocumentLinks import DocumentLinks
from .DocumentLinksInterface import DocumentLinksInterface
from .DocumentLoadFlags import DocumentLoadFlags
from .DocumentMedia import DocumentMedia
from .DocumentMediaInterface import DocumentMediaInterface
from .DocumentMode import DocumentMode
from .DocumentPermissions import DocumentPermissions
from .DocumentPrint import DocumentPrint
from .DocumentPrintInterface import DocumentPrintInterface
from .DocumentPrivate import DocumentPrivate
from .DocumentSecurity import DocumentSecurity
from .DocumentSecurityInterface import DocumentSecurityInterface
from .DocumentText import DocumentText
from .DocumentTextInterface import DocumentTextInterface
from .DocumentTransition import DocumentTransition
from .DocumentTransitionInterface import DocumentTransitionInterface
from .DocumentUIHints import DocumentUIHints
from .FileExporter import FileExporter
from .FileExporterCapabilities import FileExporterCapabilities
from .FileExporterContext import FileExporterContext
from .FileExporterFormat import FileExporterFormat
from .FileExporterInterface import FileExporterInterface
from .FindOptions import FindOptions
from .FormField import FormField
from .FormFieldButton import FormFieldButton
from .FormFieldButtonClass import FormFieldButtonClass
from .FormFieldButtonType import FormFieldButtonType
from .FormFieldChoice import FormFieldChoice
from .FormFieldChoiceClass import FormFieldChoiceClass
from .FormFieldChoiceType import FormFieldChoiceType
from .FormFieldClass import FormFieldClass
from .FormFieldSignature import FormFieldSignature
from .FormFieldSignatureClass import FormFieldSignatureClass
from .FormFieldText import FormFieldText
from .FormFieldTextClass import FormFieldTextClass
from .FormFieldTextType import FormFieldTextType
from .Image import Image
from .ImageClass import ImageClass
from .ImagePrivate import ImagePrivate
from .Layer import Layer
from .LayerClass import LayerClass
from .LayerPrivate import LayerPrivate
from .Link import Link
from .LinkAction import LinkAction
from .LinkActionClass import LinkActionClass
from .LinkActionPrivate import LinkActionPrivate
from .LinkActionType import LinkActionType
from .LinkClass import LinkClass
from .LinkDest import LinkDest
from .LinkDestClass import LinkDestClass
from .LinkDestPrivate import LinkDestPrivate
from .LinkDestType import LinkDestType
from .LinkPrivate import LinkPrivate
from .Mapping import Mapping
from .MappingList import MappingList
from .Media import Media
from .MediaClass import MediaClass
from .MediaPrivate import MediaPrivate
from .Page import Page
from .PageClass import PageClass
from .Point import Point
from .Rectangle import Rectangle
from .RenderContext import RenderContext
from .RenderContextClass import RenderContextClass
from .Selection import Selection
from .SelectionInterface import SelectionInterface
from .SelectionStyle import SelectionStyle
from .SourceLink import SourceLink
from .TransitionEffect import TransitionEffect
from .TransitionEffectAlignment import TransitionEffectAlignment
from .TransitionEffectClass import TransitionEffectClass
from .TransitionEffectDirection import TransitionEffectDirection
from .TransitionEffectType import TransitionEffectType
from .TypeInfo import TypeInfo
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f6ab36c7d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EvinceDocument-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EvinceDocument', loader=<gi.importer.DynamicImporter object at 0x7f6ab36c7d00>)"

