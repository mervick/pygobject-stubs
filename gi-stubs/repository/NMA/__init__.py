# encoding: utf-8
# module gi.repository.NMA
# from /usr/lib64/girepository-1.0/NMA-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

BAR_CODE_SIZE = 'size'
BAR_CODE_TEXT = 'text'

BAR_CODE_WIDGET_CONNECTION = 'connection'

MAJOR_VERSION = 1

MICRO_VERSION = 28

MINOR_VERSION = 8

_namespace = 'NMA'

_version = '1.0'

__weakref__ = None

# functions

def mobile_providers_split_3gpp_mcc_mnc(mccmnc): # real signature unknown; restored from __doc__
    """ mobile_providers_split_3gpp_mcc_mnc(mccmnc:str) -> bool, mcc:str, mnc:str """
    return False

def utils_menu_to_secret_flags(passwd_entry): # real signature unknown; restored from __doc__
    """ utils_menu_to_secret_flags(passwd_entry:Gtk.Widget) -> NM.SettingSecretFlags """
    pass

def utils_setup_password_storage(passwd_entry, initial_flags, setting, password_flags_name, with_not_required, ask_mode): # real signature unknown; restored from __doc__
    """ utils_setup_password_storage(passwd_entry:Gtk.Widget, initial_flags:NM.SettingSecretFlags, setting:NM.Setting, password_flags_name:str, with_not_required:bool, ask_mode:bool) """
    pass

def utils_update_password_storage(passwd_entry, secret_flags, setting, password_flags_name): # real signature unknown; restored from __doc__
    """ utils_update_password_storage(passwd_entry:Gtk.Widget, secret_flags:NM.SettingSecretFlags, setting:NM.Setting, password_flags_name:str) """
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

from .BarCode import BarCode
from .BarCodeClass import BarCodeClass
from .BarCodeWidget import BarCodeWidget
from .BarCodeWidgetClass import BarCodeWidgetClass
from .CertChooser import CertChooser
from .CertChooserClass import CertChooserClass
from .CertChooserFlags import CertChooserFlags
from .CountryInfo import CountryInfo
from .MobileAccessMethod import MobileAccessMethod
from .MobileFamily import MobileFamily
from .MobileProvider import MobileProvider
from .MobileProvidersDatabase import MobileProvidersDatabase
from .MobileProvidersDatabaseClass import MobileProvidersDatabaseClass
from .MobileProvidersDatabasePrivate import MobileProvidersDatabasePrivate
from .MobileWizard import MobileWizard
from .MobileWizardAccessMethod import MobileWizardAccessMethod
from .MobileWizardClass import MobileWizardClass
from .VpnPasswordDialog import VpnPasswordDialog
from .VpnPasswordDialogClass import VpnPasswordDialogClass
from .WifiDialog import WifiDialog
from .WifiDialogClass import WifiDialogClass
from .Ws import Ws
from .Ws8021x import Ws8021x
from .Ws8021xClass import Ws8021xClass
from .WsDynamicWep import WsDynamicWep
from .WsDynamicWepClass import WsDynamicWepClass
from .WsInterface import WsInterface
from .WsLeap import WsLeap
from .WsLeapClass import WsLeapClass
from .WsSae import WsSae
from .WsSaeClass import WsSaeClass
from .WsWepKey import WsWepKey
from .WsWepKeyClass import WsWepKeyClass
from .WsWpaEap import WsWpaEap
from .WsWpaEapClass import WsWpaEapClass
from .WsWpaPsk import WsWpaPsk
from .WsWpaPskClass import WsWpaPskClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f9b254a4d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/NMA-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.NMA', loader=<gi.importer.DynamicImporter object at 0x7f9b254a4d00>)"

