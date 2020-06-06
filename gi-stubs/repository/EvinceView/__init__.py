# encoding: utf-8
# module gi.repository.EvinceView
# from /usr/lib64/girepository-1.0/EvinceView-3.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

STOCK_ANNOT_SQUIGGLY = 'annotations-squiggly-symbolic'
STOCK_ANNOT_TEXT = 'annotations-text-symbolic'

STOCK_ATTACHMENT = 'mail-attachment'
STOCK_CLOSE = 'close'

STOCK_FIND_UNSUPPORTED = 'find-unsupported-symbolic'

STOCK_INVERTED_COLORS = 'inverted'

STOCK_OUTLINE = 'outline-symbolic'

STOCK_RESIZE_SE = 'resize-se'
STOCK_RESIZE_SW = 'resize-sw'

STOCK_ROTATE_LEFT = 'object-rotate-left'
STOCK_ROTATE_RIGHT = 'object-rotate-right'

STOCK_RUN_PRESENTATION = 'x-office-presentation'

STOCK_SEND_TO = 'document-send'

STOCK_VIEW_CONTINUOUS = 'view-page-continuous'
STOCK_VIEW_DUAL = 'view-page-facing'
STOCK_VIEW_SIDEBAR = 'view-sidebar-symbolic'

STOCK_VISIBLE = 'visible-symbolic'
STOCK_ZOOM = 'zoom'

STOCK_ZOOM_PAGE = 'zoom-fit-height'
STOCK_ZOOM_WIDTH = 'zoom-fit-width'

_namespace = 'EvinceView'

_version = '3.0'

__weakref__ = None

# functions

def stock_icons_init(): # real signature unknown; restored from __doc__
    """ stock_icons_init() """
    pass

def stock_icons_set_screen(screen): # real signature unknown; restored from __doc__
    """ stock_icons_set_screen(screen:Gdk.Screen) """
    pass

def stock_icons_shutdown(): # real signature unknown; restored from __doc__
    """ stock_icons_shutdown() """
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

from .DocumentModel import DocumentModel
from .DocumentModelClass import DocumentModelClass
from .Job import Job
from .JobAnnots import JobAnnots
from .JobAnnotsClass import JobAnnotsClass
from .JobAttachments import JobAttachments
from .JobAttachmentsClass import JobAttachmentsClass
from .JobClass import JobClass
from .JobExport import JobExport
from .JobExportClass import JobExportClass
from .JobFind import JobFind
from .JobFindClass import JobFindClass
from .JobFonts import JobFonts
from .JobFontsClass import JobFontsClass
from .JobLayers import JobLayers
from .JobLayersClass import JobLayersClass
from .JobLinks import JobLinks
from .JobLinksClass import JobLinksClass
from .JobLoad import JobLoad
from .JobLoadClass import JobLoadClass
from .JobLoadGFile import JobLoadGFile
from .JobLoadGFileClass import JobLoadGFileClass
from .JobLoadStream import JobLoadStream
from .JobLoadStreamClass import JobLoadStreamClass
from .JobPageData import JobPageData
from .JobPageDataClass import JobPageDataClass
from .JobPageDataFlags import JobPageDataFlags
from .JobPrint import JobPrint
from .JobPrintClass import JobPrintClass
from .JobPriority import JobPriority
from .JobRender import JobRender
from .JobRenderClass import JobRenderClass
from .JobRunMode import JobRunMode
from .JobSave import JobSave
from .JobSaveClass import JobSaveClass
from .JobThumbnail import JobThumbnail
from .JobThumbnailClass import JobThumbnailClass
from .JobThumbnailFormat import JobThumbnailFormat
from .PageLayout import PageLayout
from .PrintOperation import PrintOperation
from .PrintOperationClass import PrintOperationClass
from .SizingMode import SizingMode
from .View import View
from .ViewClass import ViewClass
from .ViewPresentation import ViewPresentation
from .ViewPresentationClass import ViewPresentationClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fb1d85fbd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EvinceView-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EvinceView', loader=<gi.importer.DynamicImporter object at 0x7fb1d85fbd00>)"

