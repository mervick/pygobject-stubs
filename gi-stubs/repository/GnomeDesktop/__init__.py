# encoding: utf-8
# module gi.repository.GnomeDesktop
# from /usr/lib64/girepository-1.0/GnomeDesktop-3.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

RR_CONNECTOR_TYPE_PANEL = 'Panel'

_namespace = 'GnomeDesktop'

_version = '3.0'

__weakref__ = None

# functions

def desktop_thumbnail_is_valid(pixbuf, uri, mtime): # real signature unknown; restored from __doc__
    """ desktop_thumbnail_is_valid(pixbuf:GdkPixbuf.Pixbuf, uri:str, mtime:int) -> bool """
    return False

def desktop_thumbnail_path_for_uri(uri, size): # real signature unknown; restored from __doc__
    """ desktop_thumbnail_path_for_uri(uri:str, size:GnomeDesktop.DesktopThumbnailSize) -> str """
    return ""

def get_all_locales(): # real signature unknown; restored from __doc__
    """ get_all_locales() -> list """
    return []

def get_country_from_code(code, translation=None): # real signature unknown; restored from __doc__
    """ get_country_from_code(code:str, translation:str=None) -> str """
    return ""

def get_country_from_locale(locale, translation=None): # real signature unknown; restored from __doc__
    """ get_country_from_locale(locale:str, translation:str=None) -> str """
    return ""

def get_input_source_from_locale(locale): # real signature unknown; restored from __doc__
    """ get_input_source_from_locale(locale:str) -> bool, type:str, id:str """
    return False

def get_language_from_code(code, translation=None): # real signature unknown; restored from __doc__
    """ get_language_from_code(code:str, translation:str=None) -> str """
    return ""

def get_language_from_locale(locale, translation=None): # real signature unknown; restored from __doc__
    """ get_language_from_locale(locale:str, translation:str=None) -> str """
    return ""

def get_translated_modifier(modifier, translation=None): # real signature unknown; restored from __doc__
    """ get_translated_modifier(modifier:str, translation:str=None) -> str """
    return ""

def language_has_translations(code): # real signature unknown; restored from __doc__
    """ language_has_translations(code:str) -> bool """
    return False

def normalize_locale(locale): # real signature unknown; restored from __doc__
    """ normalize_locale(locale:str) -> str """
    return ""

def parse_locale(locale): # real signature unknown; restored from __doc__
    """ parse_locale(locale:str) -> bool, language_codep:str, country_codep:str, codesetp:str, modifierp:str """
    return False

def rr_error_quark(): # real signature unknown; restored from __doc__
    """ rr_error_quark() -> int """
    return 0

def start_systemd_scope(name, pid, description=None, connection=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ start_systemd_scope(name:str, pid:int, description:str=None, connection:Gio.DBusConnection=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def start_systemd_scope_finish(res): # real signature unknown; restored from __doc__
    """ start_systemd_scope_finish(res:Gio.AsyncResult) -> bool """
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

from .BG import BG
from .BGClass import BGClass
from .BGCrossfade import BGCrossfade
from .BGCrossfadeClass import BGCrossfadeClass
from .BGCrossfadePrivate import BGCrossfadePrivate
from .BGSlideShow import BGSlideShow
from .BGSlideShowClass import BGSlideShowClass
from .BGSlideShowPrivate import BGSlideShowPrivate
from .DesktopThumbnailFactory import DesktopThumbnailFactory
from .DesktopThumbnailFactoryClass import DesktopThumbnailFactoryClass
from .DesktopThumbnailFactoryPrivate import DesktopThumbnailFactoryPrivate
from .DesktopThumbnailSize import DesktopThumbnailSize
from .IdleMonitor import IdleMonitor
from .IdleMonitorClass import IdleMonitorClass
from .IdleMonitorPrivate import IdleMonitorPrivate
from .PnpIds import PnpIds
from .PnpIdsClass import PnpIdsClass
from .PnpIdsPrivate import PnpIdsPrivate
from .RRConfig import RRConfig
from .RRConfigClass import RRConfigClass
from .RRConfigPrivate import RRConfigPrivate
from .RRCrtc import RRCrtc
from .RRDpmsMode import RRDpmsMode
from .RRDpmsModeType import RRDpmsModeType
from .RRError import RRError
from .RRMode import RRMode
from .RROutput import RROutput
from .RROutputInfo import RROutputInfo
from .RROutputInfoClass import RROutputInfoClass
from .RROutputInfoPrivate import RROutputInfoPrivate
from .RRRotation import RRRotation
from .RRScreen import RRScreen
from .RRScreenClass import RRScreenClass
from .RRScreenPrivate import RRScreenPrivate
from .WallClock import WallClock
from .WallClockClass import WallClockClass
from .WallClockPrivate import WallClockPrivate
from .XkbInfo import XkbInfo
from .XkbInfoClass import XkbInfoClass
from .XkbInfoPrivate import XkbInfoPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fc62f614d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GnomeDesktop-3.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GnomeDesktop', loader=<gi.importer.DynamicImporter object at 0x7fc62f614d00>)"

