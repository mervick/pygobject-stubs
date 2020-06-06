# encoding: utf-8
# module gi.repository.GcrUi
# from /usr/lib64/girepository-1.0/GcrUi-3.typelib
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
import gi.repository.Gcr as __gi_repository_Gcr
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

_namespace = 'GcrUi'

_version = '3'

__weakref__ = None

# functions

def renderer_create(label=None, attrs): # real signature unknown; restored from __doc__
    """ renderer_create(label:str=None, attrs:Gck.Attributes) -> GcrUi.Renderer or None """
    pass

def renderer_register(renderer_type, attrs): # real signature unknown; restored from __doc__
    """ renderer_register(renderer_type:GType, attrs:Gck.Attributes) """
    pass

def renderer_register_well_known(): # real signature unknown; restored from __doc__
    """ renderer_register_well_known() """
    pass

def viewer_new(): # real signature unknown; restored from __doc__
    """ viewer_new() -> GcrUi.Viewer """
    pass

def viewer_new_scrolled(): # real signature unknown; restored from __doc__
    """ viewer_new_scrolled() -> GcrUi.Viewer """
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

from .Renderer import Renderer
from .CertificateRenderer import CertificateRenderer
from .CertificateRendererClass import CertificateRendererClass
from .CertificateRendererPrivate import CertificateRendererPrivate
from .CertificateWidget import CertificateWidget
from .CertificateWidgetClass import CertificateWidgetClass
from .CertificateWidgetPrivate import CertificateWidgetPrivate
from .CollectionModel import CollectionModel
from .CollectionModelClass import CollectionModelClass
from .CollectionModelMode import CollectionModelMode
from .CollectionModelPrivate import CollectionModelPrivate
from .ComboSelector import ComboSelector
from .ComboSelectorClass import ComboSelectorClass
from .ComboSelectorPrivate import ComboSelectorPrivate
from .FailureRenderer import FailureRenderer
from .FailureRendererClass import FailureRendererClass
from .FailureRendererPrivate import FailureRendererPrivate
from .ImportButton import ImportButton
from .ImportButtonClass import ImportButtonClass
from .ImportButtonPrivate import ImportButtonPrivate
from .KeyRenderer import KeyRenderer
from .KeyRendererClass import KeyRendererClass
from .KeyRendererPrivate import KeyRendererPrivate
from .KeyWidget import KeyWidget
from .KeyWidgetClass import KeyWidgetClass
from .KeyWidgetPrivate import KeyWidgetPrivate
from .ListSelector import ListSelector
from .ListSelectorClass import ListSelectorClass
from .ListSelectorPrivate import ListSelectorPrivate
from .PromptDialog import PromptDialog
from .PromptDialogClass import PromptDialogClass
from .PromptDialogPrivate import PromptDialogPrivate
from .RendererIface import RendererIface
from .SecureEntryBuffer import SecureEntryBuffer
from .SecureEntryBufferClass import SecureEntryBufferClass
from .SecureEntryBufferPrivate import SecureEntryBufferPrivate
from .TreeSelector import TreeSelector
from .TreeSelectorClass import TreeSelectorClass
from .TreeSelectorPrivate import TreeSelectorPrivate
from .UnlockOptionsWidget import UnlockOptionsWidget
from .UnlockOptionsWidgetClass import UnlockOptionsWidgetClass
from .UnlockOptionsWidgetPrivate import UnlockOptionsWidgetPrivate
from .Viewer import Viewer
from .ViewerIface import ViewerIface
from .ViewerWidget import ViewerWidget
from .ViewerWidgetClass import ViewerWidgetClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fa32b972d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GcrUi-3.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GcrUi', loader=<gi.importer.DynamicImporter object at 0x7fa32b972d00>)"

