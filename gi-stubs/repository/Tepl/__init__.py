# encoding: utf-8
# module gi.repository.Tepl
# from /usr/lib64/girepository-1.0/Tepl-4.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gi.repository.GtkSource as __gi_repository_GtkSource
import gobject as __gobject


# Variables with simple values

_namespace = 'Tepl'

_version = '4'

__weakref__ = None

# functions

def encoding_get_all(): # real signature unknown; restored from __doc__
    """ encoding_get_all() -> list """
    return []

def encoding_get_default_candidates(): # real signature unknown; restored from __doc__
    """ encoding_get_default_candidates() -> list """
    return []

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

def iter_get_line_indentation(iter): # real signature unknown; restored from __doc__
    """ iter_get_line_indentation(iter:Gtk.TextIter) -> str """
    return ""

def menu_shell_append_edit_actions(menu_shell): # real signature unknown; restored from __doc__
    """ menu_shell_append_edit_actions(menu_shell:Gtk.MenuShell) """
    pass

def metadata_manager_init(metadata_path): # real signature unknown; restored from __doc__
    """ metadata_manager_init(metadata_path:str) """
    pass

def metadata_manager_shutdown(): # real signature unknown; restored from __doc__
    """ metadata_manager_shutdown() """
    pass

def utils_get_file_extension(filename): # real signature unknown; restored from __doc__
    """ utils_get_file_extension(filename:str) -> str """
    return ""

def utils_get_file_shortname(filename): # real signature unknown; restored from __doc__
    """ utils_get_file_shortname(filename:str) -> str """
    return ""

def utils_replace_home_dir_with_tilde(filename): # real signature unknown; restored from __doc__
    """ utils_replace_home_dir_with_tilde(filename:str) -> str """
    return ""

def utils_str_end_truncate(p_str, truncate_length): # real signature unknown; restored from __doc__
    """ utils_str_end_truncate(str:str, truncate_length:int) -> str """
    return ""

def utils_str_middle_truncate(p_str, truncate_length): # real signature unknown; restored from __doc__
    """ utils_str_middle_truncate(str:str, truncate_length:int) -> str """
    return ""

def utils_str_replace(string, search, replacement): # real signature unknown; restored from __doc__
    """ utils_str_replace(string:str, search:str, replacement:str) -> str """
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

from .AbstractFactory import AbstractFactory
from .AbstractFactoryClass import AbstractFactoryClass
from .AbstractFactoryVala import AbstractFactoryVala
from .AbstractFactoryValaClass import AbstractFactoryValaClass
from .Application import Application
from .ApplicationClass import ApplicationClass
from .ApplicationPrivate import ApplicationPrivate
from .TabGroup import TabGroup
from .ApplicationWindow import ApplicationWindow
from .ApplicationWindowClass import ApplicationWindowClass
from .ApplicationWindowPrivate import ApplicationWindowPrivate
from .Buffer import Buffer
from .BufferClass import BufferClass
from .CompressionType import CompressionType
from .Encoding import Encoding
from .File import File
from .FileClass import FileClass
from .FileLoader import FileLoader
from .FileLoaderClass import FileLoaderClass
from .FileLoaderError import FileLoaderError
from .FileMetadata import FileMetadata
from .FileMetadataClass import FileMetadataClass
from .FileSaver import FileSaver
from .FileSaverClass import FileSaverClass
from .FileSaverError import FileSaverError
from .FileSaverFlags import FileSaverFlags
from .FileSaverPrivate import FileSaverPrivate
from .FoldRegion import FoldRegion
from .FoldRegionClass import FoldRegionClass
from .GutterRendererFolds import GutterRendererFolds
from .GutterRendererFoldsClass import GutterRendererFoldsClass
from .GutterRendererFoldsState import GutterRendererFoldsState
from .InfoBar import InfoBar
from .InfoBarClass import InfoBarClass
from .NewlineType import NewlineType
from .Notebook import Notebook
from .NotebookClass import NotebookClass
from .NotebookPrivate import NotebookPrivate
from .SelectionType import SelectionType
from .Tab import Tab
from .TabClass import TabClass
from .TabGroupInterface import TabGroupInterface
from .TabLabel import TabLabel
from .TabLabelClass import TabLabelClass
from .TabLabelPrivate import TabLabelPrivate
from .TabPrivate import TabPrivate
from .View import View
from .ViewClass import ViewClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f3a987acd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Tepl-4.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Tepl', loader=<gi.importer.DynamicImporter object at 0x7f3a987acd00>)"

