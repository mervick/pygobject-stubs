# encoding: utf-8
# module gi.repository.Atspi
# from /usr/lib64/girepository-1.0/Atspi-2.0.typelib
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

COMPONENTLAYER_COUNT = 9

COORD_TYPE_COUNT = 3

DBUS_INTERFACE_ACCESSIBLE = 'org.a11y.atspi.Accessible'
DBUS_INTERFACE_ACTION = 'org.a11y.atspi.Action'
DBUS_INTERFACE_APPLICATION = 'org.a11y.atspi.Application'
DBUS_INTERFACE_CACHE = 'org.a11y.atspi.Cache'
DBUS_INTERFACE_COLLECTION = 'org.a11y.atspi.Collection'
DBUS_INTERFACE_COMPONENT = 'org.a11y.atspi.Component'
DBUS_INTERFACE_DEC = 'org.a11y.atspi.DeviceEventController'

DBUS_INTERFACE_DEVICE_EVENT_LISTENER = 'org.a11y.atspi.DeviceEventListener'

DBUS_INTERFACE_DOCUMENT = 'org.a11y.atspi.Document'

DBUS_INTERFACE_EDITABLE_TEXT = 'org.a11y.atspi.EditableText'

DBUS_INTERFACE_EVENT_KEYBOARD = 'org.a11y.atspi.Event.Keyboard'
DBUS_INTERFACE_EVENT_MOUSE = 'org.a11y.atspi.Event.Mouse'
DBUS_INTERFACE_EVENT_OBJECT = 'org.a11y.atspi.Event.Object'

DBUS_INTERFACE_EVENT_SCREEN_READER = 'org.a11y.atspi.Event.ScreenReader'

DBUS_INTERFACE_HYPERLINK = 'org.a11y.atspi.Hyperlink'
DBUS_INTERFACE_HYPERTEXT = 'org.a11y.atspi.Hypertext'
DBUS_INTERFACE_IMAGE = 'org.a11y.atspi.Image'
DBUS_INTERFACE_REGISTRY = 'org.a11y.atspi.Registry'
DBUS_INTERFACE_SELECTION = 'org.a11y.atspi.Selection'
DBUS_INTERFACE_SOCKET = 'org.a11y.atspi.Socket'
DBUS_INTERFACE_TABLE = 'org.a11y.atspi.Table'

DBUS_INTERFACE_TABLE_CELL = 'org.a11y.atspi.TableCell'

DBUS_INTERFACE_TEXT = 'org.a11y.atspi.Text'
DBUS_INTERFACE_VALUE = 'org.a11y.atspi.Value'

DBUS_NAME_REGISTRY = 'org.a11y.atspi.Registry'

DBUS_PATH_DEC = '/org/a11y/atspi/registry/deviceeventcontroller'
DBUS_PATH_NULL = '/org/a11y/atspi/null'
DBUS_PATH_REGISTRY = '/org/a11y/atspi/registry'
DBUS_PATH_ROOT = '/org/a11y/atspi/accessible/root'

DBUS_PATH_SCREEN_READER = '/org/a11y/atspi/screenreader'

EVENTTYPE_COUNT = 4

KEYEVENTTYPE_COUNT = 2

KEYSYNTHTYPE_COUNT = 5

MATCHTYPES_COUNT = 6

MODIFIERTYPE_COUNT = 8

RELATIONTYPE_COUNT = 24

ROLE_COUNT = 130

SCROLLTYPE_COUNT = 7

SORTORDER_COUNT = 8

STATETYPE_COUNT = 42

TEXT_BOUNDARY_TYPE_COUNT = 7

TEXT_CLIP_TYPE_COUNT = 4

_namespace = 'Atspi'

_version = '2.0'

__weakref__ = None

# functions

def deregister_device_event_listener(listener, filter=None): # real signature unknown; restored from __doc__
    """ deregister_device_event_listener(listener:Atspi.DeviceListener, filter=None) -> bool """
    return False

def deregister_keystroke_listener(listener, key_set=None, modmask, event_types): # real signature unknown; restored from __doc__
    """ deregister_keystroke_listener(listener:Atspi.DeviceListener, key_set:list=None, modmask:int, event_types:int) -> bool """
    return False

def event_main(): # real signature unknown; restored from __doc__
    """ event_main() """
    pass

def event_quit(): # real signature unknown; restored from __doc__
    """ event_quit() """
    pass

def exit(): # real signature unknown; restored from __doc__
    """ exit() -> int """
    return 0

def generate_keyboard_event(keyval, keystring=None, synth_type): # real signature unknown; restored from __doc__
    """ generate_keyboard_event(keyval:int, keystring:str=None, synth_type:Atspi.KeySynthType) -> bool """
    return False

def generate_mouse_event(x, y, name): # real signature unknown; restored from __doc__
    """ generate_mouse_event(x:int, y:int, name:str) -> bool """
    return False

def get_desktop(i): # real signature unknown; restored from __doc__
    """ get_desktop(i:int) -> Atspi.Accessible """
    pass

def get_desktop_count(): # real signature unknown; restored from __doc__
    """ get_desktop_count() -> int """
    return 0

def get_desktop_list(): # real signature unknown; restored from __doc__
    """ get_desktop_list() -> list """
    return []

def init(): # real signature unknown; restored from __doc__
    """ init() -> int """
    return 0

def is_initialized(): # real signature unknown; restored from __doc__
    """ is_initialized() -> bool """
    return False

def register_device_event_listener(listener, event_types, filter=None): # real signature unknown; restored from __doc__
    """ register_device_event_listener(listener:Atspi.DeviceListener, event_types:int, filter=None) -> bool """
    return False

def register_keystroke_listener(listener, key_set=None, modmask, event_types, sync_type): # real signature unknown; restored from __doc__
    """ register_keystroke_listener(listener:Atspi.DeviceListener, key_set:list=None, modmask:int, event_types:int, sync_type:Atspi.KeyListenerSyncType) -> bool """
    return False

def role_get_name(role): # real signature unknown; restored from __doc__
    """ role_get_name(role:Atspi.Role) -> str """
    return ""

def set_main_context(cnx): # real signature unknown; restored from __doc__
    """ set_main_context(cnx:GLib.MainContext) """
    pass

def set_reference_window(accessible): # real signature unknown; restored from __doc__
    """ set_reference_window(accessible:Atspi.Accessible) """
    pass

def set_timeout(val, startup_time): # real signature unknown; restored from __doc__
    """ set_timeout(val:int, startup_time:int) """
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

from .Action import Action
from .Collection import Collection
from .Component import Component
from .Document import Document
from .EditableText import EditableText
from .Hypertext import Hypertext
from .Image import Image
from .Object import Object
from .Selection import Selection
from .Table import Table
from .TableCell import TableCell
from .Text import Text
from .Value import Value
from .Accessible import Accessible
from .AccessibleClass import AccessibleClass
from .AccessiblePrivate import AccessiblePrivate
from .Application import Application
from .ApplicationClass import ApplicationClass
from .Cache import Cache
from .CollectionMatchType import CollectionMatchType
from .CollectionSortOrder import CollectionSortOrder
from .CollectionTreeTraversalType import CollectionTreeTraversalType
from .ComponentLayer import ComponentLayer
from .CoordType import CoordType
from .DeviceEvent import DeviceEvent
from .DeviceListener import DeviceListener
from .DeviceListenerClass import DeviceListenerClass
from .Event import Event
from .EventListener import EventListener
from .EventListenerClass import EventListenerClass
from .EventListenerMode import EventListenerMode
from .EventType import EventType
from .Hyperlink import Hyperlink
from .HyperlinkClass import HyperlinkClass
from .KeyDefinition import KeyDefinition
from .KeyEventType import KeyEventType
from .KeyListenerSyncType import KeyListenerSyncType
from .KeySet import KeySet
from .KeySynthType import KeySynthType
from .LocaleType import LocaleType
from .MatchRule import MatchRule
from .MatchRuleClass import MatchRuleClass
from .ModifierType import ModifierType
from .ObjectClass import ObjectClass
from .Point import Point
from .Range import Range
from .Rect import Rect
from .Relation import Relation
from .RelationClass import RelationClass
from .RelationType import RelationType
from .Role import Role
from .ScrollType import ScrollType
from .StateSet import StateSet
from .StateSetClass import StateSetClass
from .StateType import StateType
from .TextBoundaryType import TextBoundaryType
from .TextClipType import TextClipType
from .TextGranularity import TextGranularity
from .TextRange import TextRange
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f9873ccad00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Atspi-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Atspi', loader=<gi.importer.DynamicImporter object at 0x7f9873ccad00>)"

