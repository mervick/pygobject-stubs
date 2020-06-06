# encoding: utf-8
# module gi.repository.WebKit2
# from /usr/lib64/girepository-1.0/WebKit2-4.0.typelib
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
import gobject as __gobject


# Variables with simple values

EDITING_COMMAND_COPY = 'Copy'

EDITING_COMMAND_CREATE_LINK = 'CreateLink'

EDITING_COMMAND_CUT = 'Cut'

EDITING_COMMAND_INSERT_IMAGE = 'InsertImage'

EDITING_COMMAND_PASTE = 'Paste'
EDITING_COMMAND_REDO = 'Redo'

EDITING_COMMAND_SELECT_ALL = 'SelectAll'

EDITING_COMMAND_UNDO = 'Undo'

MAJOR_VERSION = 2

MICRO_VERSION = 2

MINOR_VERSION = 28

_namespace = 'WebKit2'

_version = '4.0'

__weakref__ = None

# functions

def download_error_quark(): # real signature unknown; restored from __doc__
    """ download_error_quark() -> int """
    return 0

def favicon_database_error_quark(): # real signature unknown; restored from __doc__
    """ favicon_database_error_quark() -> int """
    return 0

def get_major_version(): # real signature unknown; restored from __doc__
    """ get_major_version() -> int """
    return 0

def get_micro_version(): # real signature unknown; restored from __doc__
    """ get_micro_version() -> int """
    return 0

def get_minor_version(): # real signature unknown; restored from __doc__
    """ get_minor_version() -> int """
    return 0

def javascript_error_quark(): # real signature unknown; restored from __doc__
    """ javascript_error_quark() -> int """
    return 0

def network_error_quark(): # real signature unknown; restored from __doc__
    """ network_error_quark() -> int """
    return 0

def plugin_error_quark(): # real signature unknown; restored from __doc__
    """ plugin_error_quark() -> int """
    return 0

def policy_error_quark(): # real signature unknown; restored from __doc__
    """ policy_error_quark() -> int """
    return 0

def print_error_quark(): # real signature unknown; restored from __doc__
    """ print_error_quark() -> int """
    return 0

def snapshot_error_quark(): # real signature unknown; restored from __doc__
    """ snapshot_error_quark() -> int """
    return 0

def uri_for_display(uri): # real signature unknown; restored from __doc__
    """ uri_for_display(uri:str) -> str or None """
    return ""

def user_content_filter_error_quark(): # real signature unknown; restored from __doc__
    """ user_content_filter_error_quark() -> int """
    return 0

def user_media_permission_is_for_audio_device(request): # real signature unknown; restored from __doc__
    """ user_media_permission_is_for_audio_device(request:WebKit2.UserMediaPermissionRequest) -> bool """
    return False

def user_media_permission_is_for_video_device(request): # real signature unknown; restored from __doc__
    """ user_media_permission_is_for_video_device(request:WebKit2.UserMediaPermissionRequest) -> bool """
    return False

def user_message_error_quark(): # real signature unknown; restored from __doc__
    """ user_message_error_quark() -> int """
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

from .ApplicationInfo import ApplicationInfo
from .AuthenticationRequest import AuthenticationRequest
from .AuthenticationRequestClass import AuthenticationRequestClass
from .AuthenticationRequestPrivate import AuthenticationRequestPrivate
from .AuthenticationScheme import AuthenticationScheme
from .AutomationBrowsingContextPresentation import AutomationBrowsingContextPresentation
from .AutomationSession import AutomationSession
from .AutomationSessionClass import AutomationSessionClass
from .AutomationSessionPrivate import AutomationSessionPrivate
from .BackForwardList import BackForwardList
from .BackForwardListClass import BackForwardListClass
from .BackForwardListItem import BackForwardListItem
from .BackForwardListItemClass import BackForwardListItemClass
from .BackForwardListItemPrivate import BackForwardListItemPrivate
from .BackForwardListPrivate import BackForwardListPrivate
from .CacheModel import CacheModel
from .ColorChooserRequest import ColorChooserRequest
from .ColorChooserRequestClass import ColorChooserRequestClass
from .ColorChooserRequestPrivate import ColorChooserRequestPrivate
from .ContextMenu import ContextMenu
from .ContextMenuAction import ContextMenuAction
from .ContextMenuClass import ContextMenuClass
from .ContextMenuItem import ContextMenuItem
from .ContextMenuItemClass import ContextMenuItemClass
from .ContextMenuItemPrivate import ContextMenuItemPrivate
from .ContextMenuPrivate import ContextMenuPrivate
from .CookieAcceptPolicy import CookieAcceptPolicy
from .CookieManager import CookieManager
from .CookieManagerClass import CookieManagerClass
from .CookieManagerPrivate import CookieManagerPrivate
from .CookiePersistentStorage import CookiePersistentStorage
from .Credential import Credential
from .CredentialPersistence import CredentialPersistence
from .PermissionRequest import PermissionRequest
from .DeviceInfoPermissionRequest import DeviceInfoPermissionRequest
from .DeviceInfoPermissionRequestClass import DeviceInfoPermissionRequestClass
from .DeviceInfoPermissionRequestPrivate import DeviceInfoPermissionRequestPrivate
from .Download import Download
from .DownloadClass import DownloadClass
from .DownloadError import DownloadError
from .DownloadPrivate import DownloadPrivate
from .EditorState import EditorState
from .EditorStateClass import EditorStateClass
from .EditorStatePrivate import EditorStatePrivate
from .EditorTypingAttributes import EditorTypingAttributes
from .FaviconDatabase import FaviconDatabase
from .FaviconDatabaseClass import FaviconDatabaseClass
from .FaviconDatabaseError import FaviconDatabaseError
from .FaviconDatabasePrivate import FaviconDatabasePrivate
from .FileChooserRequest import FileChooserRequest
from .FileChooserRequestClass import FileChooserRequestClass
from .FileChooserRequestPrivate import FileChooserRequestPrivate
from .FindController import FindController
from .FindControllerClass import FindControllerClass
from .FindControllerPrivate import FindControllerPrivate
from .FindOptions import FindOptions
from .FormSubmissionRequest import FormSubmissionRequest
from .FormSubmissionRequestClass import FormSubmissionRequestClass
from .FormSubmissionRequestPrivate import FormSubmissionRequestPrivate
from .GeolocationManager import GeolocationManager
from .GeolocationManagerClass import GeolocationManagerClass
from .GeolocationManagerPrivate import GeolocationManagerPrivate
from .GeolocationPermissionRequest import GeolocationPermissionRequest
from .GeolocationPermissionRequestClass import GeolocationPermissionRequestClass
from .GeolocationPermissionRequestPrivate import GeolocationPermissionRequestPrivate
from .GeolocationPosition import GeolocationPosition
from .HardwareAccelerationPolicy import HardwareAccelerationPolicy
from .HitTestResult import HitTestResult
from .HitTestResultClass import HitTestResultClass
from .HitTestResultContext import HitTestResultContext
from .HitTestResultPrivate import HitTestResultPrivate
from .InputHints import InputHints
from .InputMethodContext import InputMethodContext
from .InputMethodContextClass import InputMethodContextClass
from .InputMethodContextPrivate import InputMethodContextPrivate
from .InputMethodUnderline import InputMethodUnderline
from .InputPurpose import InputPurpose
from .InsecureContentEvent import InsecureContentEvent
from .InstallMissingMediaPluginsPermissionRequest import InstallMissingMediaPluginsPermissionRequest
from .InstallMissingMediaPluginsPermissionRequestClass import InstallMissingMediaPluginsPermissionRequestClass
from .InstallMissingMediaPluginsPermissionRequestPrivate import InstallMissingMediaPluginsPermissionRequestPrivate
from .JavascriptError import JavascriptError
from .JavascriptResult import JavascriptResult
from .LoadEvent import LoadEvent
from .MimeInfo import MimeInfo
from .NavigationAction import NavigationAction
from .PolicyDecision import PolicyDecision
from .NavigationPolicyDecision import NavigationPolicyDecision
from .NavigationPolicyDecisionClass import NavigationPolicyDecisionClass
from .NavigationPolicyDecisionPrivate import NavigationPolicyDecisionPrivate
from .NavigationType import NavigationType
from .NetworkError import NetworkError
from .NetworkProxyMode import NetworkProxyMode
from .NetworkProxySettings import NetworkProxySettings
from .Notification import Notification
from .NotificationClass import NotificationClass
from .NotificationPermissionRequest import NotificationPermissionRequest
from .NotificationPermissionRequestClass import NotificationPermissionRequestClass
from .NotificationPermissionRequestPrivate import NotificationPermissionRequestPrivate
from .NotificationPrivate import NotificationPrivate
from .OptionMenu import OptionMenu
from .OptionMenuClass import OptionMenuClass
from .OptionMenuItem import OptionMenuItem
from .OptionMenuPrivate import OptionMenuPrivate
from .PermissionRequestIface import PermissionRequestIface
from .Plugin import Plugin
from .PluginClass import PluginClass
from .PluginError import PluginError
from .PluginPrivate import PluginPrivate
from .PointerLockPermissionRequest import PointerLockPermissionRequest
from .PointerLockPermissionRequestClass import PointerLockPermissionRequestClass
from .PointerLockPermissionRequestPrivate import PointerLockPermissionRequestPrivate
from .PolicyDecisionClass import PolicyDecisionClass
from .PolicyDecisionPrivate import PolicyDecisionPrivate
from .PolicyDecisionType import PolicyDecisionType
from .PolicyError import PolicyError
from .PrintCustomWidget import PrintCustomWidget
from .PrintCustomWidgetClass import PrintCustomWidgetClass
from .PrintCustomWidgetPrivate import PrintCustomWidgetPrivate
from .PrintError import PrintError
from .PrintOperation import PrintOperation
from .PrintOperationClass import PrintOperationClass
from .PrintOperationPrivate import PrintOperationPrivate
from .PrintOperationResponse import PrintOperationResponse
from .ProcessModel import ProcessModel
from .ResponsePolicyDecision import ResponsePolicyDecision
from .ResponsePolicyDecisionClass import ResponsePolicyDecisionClass
from .ResponsePolicyDecisionPrivate import ResponsePolicyDecisionPrivate
from .SaveMode import SaveMode
from .ScriptDialog import ScriptDialog
from .ScriptDialogType import ScriptDialogType
from .SecurityManager import SecurityManager
from .SecurityManagerClass import SecurityManagerClass
from .SecurityManagerPrivate import SecurityManagerPrivate
from .SecurityOrigin import SecurityOrigin
from .Settings import Settings
from .SettingsClass import SettingsClass
from .SettingsPrivate import SettingsPrivate
from .SnapshotError import SnapshotError
from .SnapshotOptions import SnapshotOptions
from .SnapshotRegion import SnapshotRegion
from .TLSErrorsPolicy import TLSErrorsPolicy
from .URIRequest import URIRequest
from .URIRequestClass import URIRequestClass
from .URIRequestPrivate import URIRequestPrivate
from .URIResponse import URIResponse
from .URIResponseClass import URIResponseClass
from .URIResponsePrivate import URIResponsePrivate
from .URISchemeRequest import URISchemeRequest
from .URISchemeRequestClass import URISchemeRequestClass
from .URISchemeRequestPrivate import URISchemeRequestPrivate
from .UserContentFilter import UserContentFilter
from .UserContentFilterError import UserContentFilterError
from .UserContentFilterStore import UserContentFilterStore
from .UserContentFilterStoreClass import UserContentFilterStoreClass
from .UserContentFilterStorePrivate import UserContentFilterStorePrivate
from .UserContentInjectedFrames import UserContentInjectedFrames
from .UserContentManager import UserContentManager
from .UserContentManagerClass import UserContentManagerClass
from .UserContentManagerPrivate import UserContentManagerPrivate
from .UserMediaPermissionRequest import UserMediaPermissionRequest
from .UserMediaPermissionRequestClass import UserMediaPermissionRequestClass
from .UserMediaPermissionRequestPrivate import UserMediaPermissionRequestPrivate
from .UserMessage import UserMessage
from .UserMessageClass import UserMessageClass
from .UserMessageError import UserMessageError
from .UserMessagePrivate import UserMessagePrivate
from .UserScript import UserScript
from .UserScriptInjectionTime import UserScriptInjectionTime
from .UserStyleLevel import UserStyleLevel
from .UserStyleSheet import UserStyleSheet
from .WebContext import WebContext
from .WebContextClass import WebContextClass
from .WebContextPrivate import WebContextPrivate
from .WebInspector import WebInspector
from .WebInspectorClass import WebInspectorClass
from .WebInspectorPrivate import WebInspectorPrivate
from .WebProcessTerminationReason import WebProcessTerminationReason
from .WebResource import WebResource
from .WebResourceClass import WebResourceClass
from .WebResourcePrivate import WebResourcePrivate
from .WebsiteData import WebsiteData
from .WebsiteDataManager import WebsiteDataManager
from .WebsiteDataManagerClass import WebsiteDataManagerClass
from .WebsiteDataManagerPrivate import WebsiteDataManagerPrivate
from .WebsiteDataTypes import WebsiteDataTypes
from .WebViewBase import WebViewBase
from .WebView import WebView
from .WebViewBaseClass import WebViewBaseClass
from .WebViewBasePrivate import WebViewBasePrivate
from .WebViewClass import WebViewClass
from .WebViewPrivate import WebViewPrivate
from .WebViewSessionState import WebViewSessionState
from .WindowProperties import WindowProperties
from .WindowPropertiesClass import WindowPropertiesClass
from .WindowPropertiesPrivate import WindowPropertiesPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fc3f0c9bd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/WebKit2-4.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.WebKit2', loader=<gi.importer.DynamicImporter object at 0x7fc3f0c9bd00>)"

