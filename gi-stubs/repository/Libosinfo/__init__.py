# encoding: utf-8
# module gi.repository.Libosinfo
# from /usr/lib64/girepository-1.0/Libosinfo-1.0.typelib
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

ARCHITECTURE_ALL = 'all'

AVATAR_FORMAT_PROP_ALPHA = 'alpha'
AVATAR_FORMAT_PROP_HEIGHT = 'height'

AVATAR_FORMAT_PROP_MIME_TYPE = 'mime-type'

AVATAR_FORMAT_PROP_WIDTH = 'width'

DEVICELINK_PROP_DRIVER = 'driver'
DEVICELINK_PROP_SUPPORTED = 'supported'

DEVICE_DRIVER_DEFAULT_PRIORITY = 50

DEVICE_DRIVER_PROP_ARCHITECTURE = 'arch'
DEVICE_DRIVER_PROP_DEVICE = 'device'
DEVICE_DRIVER_PROP_FILE = 'file'
DEVICE_DRIVER_PROP_LOCATION = 'location'

DEVICE_DRIVER_PROP_PRE_INSTALLABLE = 'pre-installable'

DEVICE_DRIVER_PROP_PRIORITY = 'priority'
DEVICE_DRIVER_PROP_SIGNED = 'signed'

DEVICE_PROP_BUS_TYPE = 'bus-type'

DEVICE_PROP_CLASS = 'class'
DEVICE_PROP_NAME = 'name'
DEVICE_PROP_PRODUCT = 'product'

DEVICE_PROP_PRODUCT_ID = 'product-id'

DEVICE_PROP_SUBSYSTEM = 'subsystem'
DEVICE_PROP_VENDOR = 'vendor'

DEVICE_PROP_VENDOR_ID = 'vendor-id'

ENTITY_PROP_ID = 'id'

FIRMWARE_PROP_ARCHITECTURE = 'architecture'
FIRMWARE_PROP_SUPPORTED = 'supported'
FIRMWARE_PROP_TYPE = 'type'

GIBIBYTES = 1073741824

IMAGE_PROP_ARCHITECTURE = 'architecture'

IMAGE_PROP_CLOUD_INIT = 'cloud-init'

IMAGE_PROP_FORMAT = 'format'
IMAGE_PROP_URL = 'url'
IMAGE_PROP_VARIANT = 'variant'

INSTALL_CONFIG_PARAM_PROP_DATAMAP = 'value-map'
INSTALL_CONFIG_PARAM_PROP_NAME = 'name'
INSTALL_CONFIG_PARAM_PROP_POLICY = 'policy'

INSTALL_CONFIG_PROP_ADMIN_PASSWORD = 'admin-password'

INSTALL_CONFIG_PROP_AVATAR_DISK = 'avatar-disk'
INSTALL_CONFIG_PROP_AVATAR_LOCATION = 'avatar-location'

INSTALL_CONFIG_PROP_DRIVER_SIGNING = 'driver-signing'

INSTALL_CONFIG_PROP_HARDWARE_ARCH = 'hardware-arch'

INSTALL_CONFIG_PROP_HOSTNAME = 'hostname'

INSTALL_CONFIG_PROP_INSTALLATION_URL = 'installation-url'

INSTALL_CONFIG_PROP_L10N_KEYBOARD = 'l10n-keyboard'
INSTALL_CONFIG_PROP_L10N_LANGUAGE = 'l10n-language'
INSTALL_CONFIG_PROP_L10N_TIMEZONE = 'l10n-timezone'

INSTALL_CONFIG_PROP_POST_INSTALL_DRIVERS_DISK = 'post-install-drivers-disk'
INSTALL_CONFIG_PROP_POST_INSTALL_DRIVERS_LOCATION = 'post-install-drivers-location'

INSTALL_CONFIG_PROP_PRE_INSTALL_DRIVERS_DISK = 'pre-install-drivers-disk'
INSTALL_CONFIG_PROP_PRE_INSTALL_DRIVERS_LOCATION = 'pre-install-drivers-location'

INSTALL_CONFIG_PROP_REG_LOGIN = 'reg-login'
INSTALL_CONFIG_PROP_REG_PASSWORD = 'reg-password'
INSTALL_CONFIG_PROP_REG_PRODUCTKEY = 'reg-product-key'

INSTALL_CONFIG_PROP_SCRIPT_DISK = 'script-disk'

INSTALL_CONFIG_PROP_TARGET_DISK = 'target-disk'

INSTALL_CONFIG_PROP_USER_ADMIN = 'user-admin'
INSTALL_CONFIG_PROP_USER_AUTOLOGIN = 'user-autologin'
INSTALL_CONFIG_PROP_USER_LOGIN = 'user-login'
INSTALL_CONFIG_PROP_USER_PASSWORD = 'user-password'
INSTALL_CONFIG_PROP_USER_REALNAME = 'user-realname'

INSTALL_SCRIPT_PROFILE_DESKTOP = 'desktop'
INSTALL_SCRIPT_PROFILE_JEOS = 'jeos'

INSTALL_SCRIPT_PROP_CAN_POST_INSTALL_DRIVERS = 'can-post-install-drivers'

INSTALL_SCRIPT_PROP_CAN_PRE_INSTALL_DRIVERS = 'can-pre-install-drivers'

INSTALL_SCRIPT_PROP_EXPECTED_FILENAME = 'expected-filename'

INSTALL_SCRIPT_PROP_INJECTION_METHOD = 'injection-method'

INSTALL_SCRIPT_PROP_INSTALLATION_SOURCE = 'installation-source'

INSTALL_SCRIPT_PROP_NEEDS_INTERNET = 'needs-internet'

INSTALL_SCRIPT_PROP_PATH_FORMAT = 'path-format'

INSTALL_SCRIPT_PROP_POST_INSTALL_DRIVERS_SIGNING_REQ = 'post-install-drivers-signing-req'

INSTALL_SCRIPT_PROP_PREFERRED_INJECTION_METHOD = 'preferred-injection-method'

INSTALL_SCRIPT_PROP_PRE_INSTALL_DRIVERS_SIGNING_REQ = 'pre-install-drivers-signing-req'

INSTALL_SCRIPT_PROP_PRODUCT_KEY_FORMAT = 'product-key-format'

INSTALL_SCRIPT_PROP_PROFILE = 'profile'

INSTALL_SCRIPT_PROP_TEMPLATE_DATA = 'template-data'
INSTALL_SCRIPT_PROP_TEMPLATE_URI = 'template-uri'

KIBIBYTES = 1024

MAJOR_VERSION = 1

MEBIBYTES = 1048576

MEDIA_PROP_APPLICATION_ID = 'application-id'

MEDIA_PROP_ARCHITECTURE = 'architecture'
MEDIA_PROP_BOOTABLE = 'bootable'

MEDIA_PROP_EJECT_AFTER_INSTALL = 'eject-after-install'

MEDIA_PROP_INITRD = 'initrd'
MEDIA_PROP_INSTALLER = 'installer'

MEDIA_PROP_INSTALLER_REBOOTS = 'installer-reboots'
MEDIA_PROP_INSTALLER_SCRIPT = 'installer-script'

MEDIA_PROP_KERNEL = 'kernel'
MEDIA_PROP_LANG = 'l10n-language'

MEDIA_PROP_LANG_MAP = 'l10n-language-map'
MEDIA_PROP_LANG_REGEX = 'l10n-language-regex'

MEDIA_PROP_LIVE = 'live'

MEDIA_PROP_PUBLISHER_ID = 'publisher-id'

MEDIA_PROP_SYSTEM_ID = 'system-id'

MEDIA_PROP_URL = 'url'
MEDIA_PROP_VARIANT = 'variant'

MEDIA_PROP_VOLUME_ID = 'volume-id'
MEDIA_PROP_VOLUME_SIZE = 'volume-size'

MEGAHERTZ = 1000000

MICRO_VERSION = 1

MINOR_VERSION = 7

OS_PROP_DISTRO = 'distro'
OS_PROP_FAMILY = 'family'

OS_PROP_KERNEL_URL_ARGUMENT = 'kernel-url-argument'

OS_PROP_RELEASE_STATUS = 'release-status'

OS_VARIANT_PROP_NAME = 'name'

PRODUCT_PROP_CODENAME = 'codename'

PRODUCT_PROP_EOL_DATE = 'eol-date'

PRODUCT_PROP_LOGO = 'logo'
PRODUCT_PROP_NAME = 'name'

PRODUCT_PROP_RELEASE_DATE = 'release-date'

PRODUCT_PROP_SHORT_ID = 'short-id'

PRODUCT_PROP_VENDOR = 'vendor'
PRODUCT_PROP_VERSION = 'version'

RESOURCES_PROP_ARCHITECTURE = 'architecture'
RESOURCES_PROP_CPU = 'cpu'

RESOURCES_PROP_N_CPUS = 'n-cpus'

RESOURCES_PROP_RAM = 'ram'
RESOURCES_PROP_STORAGE = 'storage'

TREE_PROP_ARCHITECTURE = 'architecture'

TREE_PROP_BOOT_ISO = 'boot-iso'

TREE_PROP_HAS_TREEINFO = 'has-treeinfo'

TREE_PROP_INITRD = 'initrd'
TREE_PROP_KERNEL = 'kernel'

TREE_PROP_TREEINFO_ARCH = 'treeinfo-arch'
TREE_PROP_TREEINFO_FAMILY = 'treeinfo-family'
TREE_PROP_TREEINFO_VARIANT = 'treeinfo-variant'
TREE_PROP_TREEINFO_VERSION = 'treeinfo-version'

TREE_PROP_URL = 'url'
TREE_PROP_VARIANT = 'variant'

_namespace = 'Libosinfo'

_version = '1.0'

__weakref__ = None

# functions

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def media_error_quark(): # real signature unknown; restored from __doc__
    """ media_error_quark() -> int """
    return 0

def tree_error_quark(): # real signature unknown; restored from __doc__
    """ tree_error_quark() -> int """
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

from .Entity import Entity
from .AvatarFormat import AvatarFormat
from .AvatarFormatClass import AvatarFormatClass
from .Datamap import Datamap
from .DatamapClass import DatamapClass
from .List import List
from .DatamapList import DatamapList
from .DatamapListClass import DatamapListClass
from .DatamapListPrivate import DatamapListPrivate
from .DatamapPrivate import DatamapPrivate
from .Db import Db
from .DbClass import DbClass
from .DbPrivate import DbPrivate
from .Deployment import Deployment
from .DeploymentClass import DeploymentClass
from .DeploymentList import DeploymentList
from .DeploymentListClass import DeploymentListClass
from .DeploymentListPrivate import DeploymentListPrivate
from .DeploymentPrivate import DeploymentPrivate
from .Device import Device
from .DeviceClass import DeviceClass
from .DeviceDriver import DeviceDriver
from .DeviceDriverClass import DeviceDriverClass
from .DeviceDriverList import DeviceDriverList
from .DeviceDriverListClass import DeviceDriverListClass
from .DeviceDriverListPrivate import DeviceDriverListPrivate
from .DeviceDriverPrivate import DeviceDriverPrivate
from .DeviceDriverSigningReq import DeviceDriverSigningReq
from .DeviceLink import DeviceLink
from .DeviceLinkClass import DeviceLinkClass
from .Filter import Filter
from .DeviceLinkFilter import DeviceLinkFilter
from .DeviceLinkFilterClass import DeviceLinkFilterClass
from .DeviceLinkFilterPrivate import DeviceLinkFilterPrivate
from .DeviceLinkList import DeviceLinkList
from .DeviceLinkListClass import DeviceLinkListClass
from .DeviceLinkListPrivate import DeviceLinkListPrivate
from .DeviceLinkPrivate import DeviceLinkPrivate
from .DeviceList import DeviceList
from .DeviceListClass import DeviceListClass
from .DeviceListPrivate import DeviceListPrivate
from .DevicePrivate import DevicePrivate
from .EntityClass import EntityClass
from .EntityPrivate import EntityPrivate
from .FilterClass import FilterClass
from .FilterPrivate import FilterPrivate
from .Firmware import Firmware
from .FirmwareClass import FirmwareClass
from .FirmwareList import FirmwareList
from .FirmwareListClass import FirmwareListClass
from .FirmwareListPrivate import FirmwareListPrivate
from .FirmwarePrivate import FirmwarePrivate
from .Image import Image
from .ImageClass import ImageClass
from .ImageList import ImageList
from .ImageListClass import ImageListClass
from .ImageListPrivate import ImageListPrivate
from .ImagePrivate import ImagePrivate
from .InstallConfig import InstallConfig
from .InstallConfigClass import InstallConfigClass
from .InstallConfigParam import InstallConfigParam
from .InstallConfigParamClass import InstallConfigParamClass
from .InstallConfigParamList import InstallConfigParamList
from .InstallConfigParamListClass import InstallConfigParamListClass
from .InstallConfigParamListPrivate import InstallConfigParamListPrivate
from .InstallConfigParamPolicy import InstallConfigParamPolicy
from .InstallConfigParamPrivate import InstallConfigParamPrivate
from .InstallConfigPrivate import InstallConfigPrivate
from .InstallScript import InstallScript
from .InstallScriptClass import InstallScriptClass
from .InstallScriptInjectionMethod import InstallScriptInjectionMethod
from .InstallScriptInstallationSource import InstallScriptInstallationSource
from .InstallScriptList import InstallScriptList
from .InstallScriptListClass import InstallScriptListClass
from .InstallScriptListPrivate import InstallScriptListPrivate
from .InstallScriptPrivate import InstallScriptPrivate
from .ListClass import ListClass
from .ListPrivate import ListPrivate
from .Loader import Loader
from .LoaderClass import LoaderClass
from .LoaderPrivate import LoaderPrivate
from .Media import Media
from .MediaClass import MediaClass
from .MediaDetectFlags import MediaDetectFlags
from .MediaError import MediaError
from .MediaList import MediaList
from .MediaListClass import MediaListClass
from .MediaListPrivate import MediaListPrivate
from .MediaPrivate import MediaPrivate
from .Product import Product
from .Os import Os
from .OsClass import OsClass
from .ProductList import ProductList
from .OsList import OsList
from .OsListClass import OsListClass
from .OsListPrivate import OsListPrivate
from .OsPrivate import OsPrivate
from .OsVariant import OsVariant
from .OsVariantClass import OsVariantClass
from .OsVariantList import OsVariantList
from .OsVariantListClass import OsVariantListClass
from .OsVariantListPrivate import OsVariantListPrivate
from .OsVariantPrivate import OsVariantPrivate
from .PathFormat import PathFormat
from .Platform import Platform
from .PlatformClass import PlatformClass
from .PlatformList import PlatformList
from .PlatformListClass import PlatformListClass
from .PlatformListPrivate import PlatformListPrivate
from .PlatformPrivate import PlatformPrivate
from .ProductClass import ProductClass
from .ProductFilter import ProductFilter
from .ProductFilterClass import ProductFilterClass
from .ProductFilterPrivate import ProductFilterPrivate
from .ProductListClass import ProductListClass
from .ProductListPrivate import ProductListPrivate
from .ProductPrivate import ProductPrivate
from .ProductRelationship import ProductRelationship
from .ReleaseStatus import ReleaseStatus
from .Resources import Resources
from .ResourcesClass import ResourcesClass
from .ResourcesList import ResourcesList
from .ResourcesListClass import ResourcesListClass
from .ResourcesListPrivate import ResourcesListPrivate
from .ResourcesPrivate import ResourcesPrivate
from .Tree import Tree
from .TreeClass import TreeClass
from .TreeError import TreeError
from .TreeList import TreeList
from .TreeListClass import TreeListClass
from .TreeListPrivate import TreeListPrivate
from .TreePrivate import TreePrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f715475fd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Libosinfo-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Libosinfo', loader=<gi.importer.DynamicImporter object at 0x7f715475fd00>)"

