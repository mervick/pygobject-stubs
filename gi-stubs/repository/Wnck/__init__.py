# encoding: utf-8
# module gi.repository.Wnck
# from /usr/lib64/girepository-1.0/Wnck-3.0.typelib
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

DEFAULT_ICON_SIZE = 32

DEFAULT_MINI_ICON_SIZE = 16

MAJOR_VERSION = 3

MICRO_VERSION = 0

MINOR_VERSION = 36

_namespace = 'Wnck'

_version = '3.0'

__weakref__ = None

# functions

def pid_read_resource_usage(gdk_display, pid, usage): # real signature unknown; restored from __doc__
    """ pid_read_resource_usage(gdk_display:Gdk.Display, pid:int, usage:Wnck.ResourceUsage) """
    pass

def set_client_type(ewmh_sourceindication_client_type): # real signature unknown; restored from __doc__
    """ set_client_type(ewmh_sourceindication_client_type:Wnck.ClientType) """
    pass

def set_default_icon_size(size): # real signature unknown; restored from __doc__
    """ set_default_icon_size(size:int) """
    pass

def set_default_mini_icon_size(size): # real signature unknown; restored from __doc__
    """ set_default_mini_icon_size(size:int) """
    pass

def shutdown(): # real signature unknown; restored from __doc__
    """ shutdown() """
    pass

def xid_read_resource_usage(gdk_display, xid, usage): # real signature unknown; restored from __doc__
    """ xid_read_resource_usage(gdk_display:Gdk.Display, xid:int, usage:Wnck.ResourceUsage) """
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

from .ActionMenu import ActionMenu
from .ActionMenuClass import ActionMenuClass
from .ActionMenuPrivate import ActionMenuPrivate
from .Application import Application
from .ApplicationClass import ApplicationClass
from .ApplicationPrivate import ApplicationPrivate
from .ClassGroup import ClassGroup
from .ClassGroupClass import ClassGroupClass
from .ClassGroupPrivate import ClassGroupPrivate
from .ClientType import ClientType
from .ImageMenuItem import ImageMenuItem
from .ImageMenuItemClass import ImageMenuItemClass
from .MotionDirection import MotionDirection
from .Pager import Pager
from .PagerClass import PagerClass
from .PagerDisplayMode import PagerDisplayMode
from .PagerPrivate import PagerPrivate
from .PagerScrollMode import PagerScrollMode
from .ResourceUsage import ResourceUsage
from .Screen import Screen
from .ScreenClass import ScreenClass
from .ScreenPrivate import ScreenPrivate
from .Selector import Selector
from .SelectorClass import SelectorClass
from .SelectorPrivate import SelectorPrivate
from .Tasklist import Tasklist
from .TasklistClass import TasklistClass
from .TasklistGroupingType import TasklistGroupingType
from .TasklistPrivate import TasklistPrivate
from .Window import Window
from .WindowActions import WindowActions
from .WindowClass import WindowClass
from .WindowGravity import WindowGravity
from .WindowMoveResizeMask import WindowMoveResizeMask
from .WindowPrivate import WindowPrivate
from .WindowState import WindowState
from .WindowType import WindowType
from .Workspace import Workspace
from .WorkspaceClass import WorkspaceClass
from .WorkspaceLayout import WorkspaceLayout
from .WorkspacePrivate import WorkspacePrivate
from ._LayoutCorner import _LayoutCorner
from ._LayoutOrientation import _LayoutOrientation
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f75c529bd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Wnck-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Wnck', loader=<gi.importer.DynamicImporter object at 0x7f75c529bd00>)"

