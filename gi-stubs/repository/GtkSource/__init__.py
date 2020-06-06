# encoding: utf-8
# module gi.repository.GtkSource
# from /usr/lib64/girepository-1.0/GtkSource-3.0.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

_namespace = 'GtkSource'

_version = '4'

__weakref__ = None

# functions

def completion_error_quark(): # real signature unknown; restored from __doc__
    """ completion_error_quark() -> int """
    return 0

def encoding_get_all(): # real signature unknown; restored from __doc__
    """ encoding_get_all() -> list """
    return []

def encoding_get_current(): # real signature unknown; restored from __doc__
    """ encoding_get_current() -> GtkSource.Encoding """
    pass

def encoding_get_default_candidates(): # real signature unknown; restored from __doc__
    """ encoding_get_default_candidates() -> list """
    return []

def encoding_get_from_charset(charset): # real signature unknown; restored from __doc__
    """ encoding_get_from_charset(charset:str) -> GtkSource.Encoding or None """
    pass

def encoding_get_utf8(): # real signature unknown; restored from __doc__
    """ encoding_get_utf8() -> GtkSource.Encoding """
    pass

def file_loader_error_quark(): # real signature unknown; restored from __doc__
    """ file_loader_error_quark() -> int """
    return 0

def file_saver_error_quark(): # real signature unknown; restored from __doc__
    """ file_saver_error_quark() -> int """
    return 0

def finalize(): # real signature unknown; restored from __doc__
    """ finalize() """
    pass

def init(): # real signature unknown; restored from __doc__
    """ init() """
    pass

def utils_escape_search_text(text): # real signature unknown; restored from __doc__
    """ utils_escape_search_text(text:str) -> str """
    return ""

def utils_unescape_search_text(text): # real signature unknown; restored from __doc__
    """ utils_unescape_search_text(text:str) -> str """
    return ""

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

from .BackgroundPatternType import BackgroundPatternType
from .BracketMatchType import BracketMatchType
from .Buffer import Buffer
from .BufferClass import BufferClass
from .BufferPrivate import BufferPrivate
from .ChangeCaseType import ChangeCaseType
from .Completion import Completion
from .CompletionActivation import CompletionActivation
from .CompletionClass import CompletionClass
from .CompletionContext import CompletionContext
from .CompletionContextClass import CompletionContextClass
from .CompletionContextPrivate import CompletionContextPrivate
from .CompletionError import CompletionError
from .CompletionInfo import CompletionInfo
from .CompletionInfoClass import CompletionInfoClass
from .CompletionInfoPrivate import CompletionInfoPrivate
from .CompletionProposal import CompletionProposal
from .CompletionItem import CompletionItem
from .CompletionItemClass import CompletionItemClass
from .CompletionItemPrivate import CompletionItemPrivate
from .CompletionPrivate import CompletionPrivate
from .CompletionProposalIface import CompletionProposalIface
from .CompletionProvider import CompletionProvider
from .CompletionProviderIface import CompletionProviderIface
from .CompletionWords import CompletionWords
from .CompletionWordsClass import CompletionWordsClass
from .CompletionWordsPrivate import CompletionWordsPrivate
from .CompressionType import CompressionType
from .Encoding import Encoding
from .File import File
from .FileClass import FileClass
from .FileLoader import FileLoader
from .FileLoaderClass import FileLoaderClass
from .FileLoaderError import FileLoaderError
from .FileLoaderPrivate import FileLoaderPrivate
from .FilePrivate import FilePrivate
from .FileSaver import FileSaver
from .FileSaverClass import FileSaverClass
from .FileSaverError import FileSaverError
from .FileSaverFlags import FileSaverFlags
from .FileSaverPrivate import FileSaverPrivate
from .Gutter import Gutter
from .GutterClass import GutterClass
from .GutterPrivate import GutterPrivate
from .GutterRenderer import GutterRenderer
from .GutterRendererAlignmentMode import GutterRendererAlignmentMode
from .GutterRendererClass import GutterRendererClass
from .GutterRendererPixbuf import GutterRendererPixbuf
from .GutterRendererPixbufClass import GutterRendererPixbufClass
from .GutterRendererPixbufPrivate import GutterRendererPixbufPrivate
from .GutterRendererPrivate import GutterRendererPrivate
from .GutterRendererState import GutterRendererState
from .GutterRendererText import GutterRendererText
from .GutterRendererTextClass import GutterRendererTextClass
from .GutterRendererTextPrivate import GutterRendererTextPrivate
from .Language import Language
from .LanguageClass import LanguageClass
from .LanguageManager import LanguageManager
from .LanguageManagerClass import LanguageManagerClass
from .LanguageManagerPrivate import LanguageManagerPrivate
from .LanguagePrivate import LanguagePrivate
from .View import View
from .Map import Map
from .MapClass import MapClass
from .Mark import Mark
from .MarkAttributes import MarkAttributes
from .MarkAttributesClass import MarkAttributesClass
from .MarkAttributesPrivate import MarkAttributesPrivate
from .MarkClass import MarkClass
from .MarkPrivate import MarkPrivate
from .NewlineType import NewlineType
from .PrintCompositor import PrintCompositor
from .PrintCompositorClass import PrintCompositorClass
from .PrintCompositorPrivate import PrintCompositorPrivate
from .Region import Region
from .RegionClass import RegionClass
from .RegionIter import RegionIter
from .SearchContext import SearchContext
from .SearchContextClass import SearchContextClass
from .SearchContextPrivate import SearchContextPrivate
from .SearchSettings import SearchSettings
from .SearchSettingsClass import SearchSettingsClass
from .SearchSettingsPrivate import SearchSettingsPrivate
from .SmartHomeEndType import SmartHomeEndType
from .SortFlags import SortFlags
from .SpaceDrawer import SpaceDrawer
from .SpaceDrawerClass import SpaceDrawerClass
from .SpaceDrawerPrivate import SpaceDrawerPrivate
from .SpaceLocationFlags import SpaceLocationFlags
from .SpaceTypeFlags import SpaceTypeFlags
from .Style import Style
from .StyleClass import StyleClass
from .StyleScheme import StyleScheme
from .StyleSchemeChooser import StyleSchemeChooser
from .StyleSchemeChooserButton import StyleSchemeChooserButton
from .StyleSchemeChooserButtonClass import StyleSchemeChooserButtonClass
from .StyleSchemeChooserInterface import StyleSchemeChooserInterface
from .StyleSchemeChooserWidget import StyleSchemeChooserWidget
from .StyleSchemeChooserWidgetClass import StyleSchemeChooserWidgetClass
from .StyleSchemeClass import StyleSchemeClass
from .StyleSchemeManager import StyleSchemeManager
from .StyleSchemeManagerClass import StyleSchemeManagerClass
from .StyleSchemeManagerPrivate import StyleSchemeManagerPrivate
from .StyleSchemePrivate import StyleSchemePrivate
from .Tag import Tag
from .TagClass import TagClass
from .UndoManager import UndoManager
from .UndoManagerIface import UndoManagerIface
from .ViewClass import ViewClass
from .ViewGutterPosition import ViewGutterPosition
from .ViewPrivate import ViewPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f77cc73fd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GtkSource-4.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GtkSource', loader=<gi.importer.DynamicImporter object at 0x7f77cc73fd00>)"

