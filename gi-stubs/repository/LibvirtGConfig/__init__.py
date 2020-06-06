# encoding: utf-8
# module gi.repository.LibvirtGConfig
# from /usr/lib64/girepository-1.0/LibvirtGConfig-1.0.typelib
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

_namespace = 'LibvirtGConfig'

_version = '1.0'

__weakref__ = None

# functions

def init(argv=None): # real signature unknown; restored from __doc__
    """ init(argv:list=None) -> argv:list """
    pass

def init_check(argv=None): # real signature unknown; restored from __doc__
    """ init_check(argv:list=None) -> bool, argv:list """
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

from .Object import Object
from .Capabilities import Capabilities
from .CapabilitiesClass import CapabilitiesClass
from .CapabilitiesCpu import CapabilitiesCpu
from .CapabilitiesCpuClass import CapabilitiesCpuClass
from .CapabilitiesCpuFeature import CapabilitiesCpuFeature
from .CapabilitiesCpuFeatureClass import CapabilitiesCpuFeatureClass
from .CapabilitiesCpuFeaturePrivate import CapabilitiesCpuFeaturePrivate
from .CapabilitiesCpuModel import CapabilitiesCpuModel
from .CapabilitiesCpuModelClass import CapabilitiesCpuModelClass
from .CapabilitiesCpuModelPrivate import CapabilitiesCpuModelPrivate
from .CapabilitiesCpuPrivate import CapabilitiesCpuPrivate
from .CapabilitiesCpuTopology import CapabilitiesCpuTopology
from .CapabilitiesCpuTopologyClass import CapabilitiesCpuTopologyClass
from .CapabilitiesCpuTopologyPrivate import CapabilitiesCpuTopologyPrivate
from .CapabilitiesGuest import CapabilitiesGuest
from .CapabilitiesGuestArch import CapabilitiesGuestArch
from .CapabilitiesGuestArchClass import CapabilitiesGuestArchClass
from .CapabilitiesGuestArchPrivate import CapabilitiesGuestArchPrivate
from .CapabilitiesGuestClass import CapabilitiesGuestClass
from .CapabilitiesGuestDomain import CapabilitiesGuestDomain
from .CapabilitiesGuestDomainClass import CapabilitiesGuestDomainClass
from .CapabilitiesGuestDomainPrivate import CapabilitiesGuestDomainPrivate
from .CapabilitiesGuestFeature import CapabilitiesGuestFeature
from .CapabilitiesGuestFeatureClass import CapabilitiesGuestFeatureClass
from .CapabilitiesGuestFeaturePrivate import CapabilitiesGuestFeaturePrivate
from .CapabilitiesGuestPrivate import CapabilitiesGuestPrivate
from .CapabilitiesHost import CapabilitiesHost
from .CapabilitiesHostClass import CapabilitiesHostClass
from .CapabilitiesHostPrivate import CapabilitiesHostPrivate
from .CapabilitiesHostSecModel import CapabilitiesHostSecModel
from .CapabilitiesHostSecModelClass import CapabilitiesHostSecModelClass
from .CapabilitiesHostSecModelPrivate import CapabilitiesHostSecModelPrivate
from .CapabilitiesPrivate import CapabilitiesPrivate
from .Domain import Domain
from .DomainAddress import DomainAddress
from .DomainAddressClass import DomainAddressClass
from .DomainAddressPci import DomainAddressPci
from .DomainAddressPciClass import DomainAddressPciClass
from .DomainAddressPciPrivate import DomainAddressPciPrivate
from .DomainAddressPrivate import DomainAddressPrivate
from .DomainAddressUsb import DomainAddressUsb
from .DomainAddressUsbClass import DomainAddressUsbClass
from .DomainAddressUsbPrivate import DomainAddressUsbPrivate
from .DomainCapabilities import DomainCapabilities
from .DomainCapabilitiesClass import DomainCapabilitiesClass
from .DomainCapabilitiesOs import DomainCapabilitiesOs
from .DomainCapabilitiesOsClass import DomainCapabilitiesOsClass
from .DomainCapabilitiesOsPrivate import DomainCapabilitiesOsPrivate
from .DomainCapabilitiesPrivate import DomainCapabilitiesPrivate
from .DomainDevice import DomainDevice
from .DomainChardev import DomainChardev
from .DomainChannel import DomainChannel
from .DomainChannelClass import DomainChannelClass
from .DomainChannelPrivate import DomainChannelPrivate
from .DomainChannelTargetType import DomainChannelTargetType
from .DomainChardevClass import DomainChardevClass
from .DomainChardevPrivate import DomainChardevPrivate
from .DomainChardevSource import DomainChardevSource
from .DomainChardevSourceClass import DomainChardevSourceClass
from .DomainChardevSourcePrivate import DomainChardevSourcePrivate
from .DomainChardevSourcePty import DomainChardevSourcePty
from .DomainChardevSourcePtyClass import DomainChardevSourcePtyClass
from .DomainChardevSourcePtyPrivate import DomainChardevSourcePtyPrivate
from .DomainChardevSourceSpicePort import DomainChardevSourceSpicePort
from .DomainChardevSourceSpicePortClass import DomainChardevSourceSpicePortClass
from .DomainChardevSourceSpicePortPrivate import DomainChardevSourceSpicePortPrivate
from .DomainChardevSourceSpiceVmc import DomainChardevSourceSpiceVmc
from .DomainChardevSourceSpiceVmcClass import DomainChardevSourceSpiceVmcClass
from .DomainChardevSourceSpiceVmcPrivate import DomainChardevSourceSpiceVmcPrivate
from .DomainChardevSourceUnix import DomainChardevSourceUnix
from .DomainChardevSourceUnixClass import DomainChardevSourceUnixClass
from .DomainChardevSourceUnixPrivate import DomainChardevSourceUnixPrivate
from .DomainClass import DomainClass
from .DomainClock import DomainClock
from .DomainClockClass import DomainClockClass
from .DomainClockOffset import DomainClockOffset
from .DomainClockPrivate import DomainClockPrivate
from .DomainConsole import DomainConsole
from .DomainConsoleClass import DomainConsoleClass
from .DomainConsolePrivate import DomainConsolePrivate
from .DomainConsoleTargetType import DomainConsoleTargetType
from .DomainController import DomainController
from .DomainControllerClass import DomainControllerClass
from .DomainControllerPrivate import DomainControllerPrivate
from .DomainControllerUsb import DomainControllerUsb
from .DomainControllerUsbClass import DomainControllerUsbClass
from .DomainControllerUsbModel import DomainControllerUsbModel
from .DomainControllerUsbPrivate import DomainControllerUsbPrivate
from .DomainCpu import DomainCpu
from .DomainCpuClass import DomainCpuClass
from .DomainCpuFeature import DomainCpuFeature
from .DomainCpuFeatureClass import DomainCpuFeatureClass
from .DomainCpuFeaturePolicy import DomainCpuFeaturePolicy
from .DomainCpuFeaturePrivate import DomainCpuFeaturePrivate
from .DomainCpuMatchPolicy import DomainCpuMatchPolicy
from .DomainCpuMode import DomainCpuMode
from .DomainCpuModel import DomainCpuModel
from .DomainCpuModelClass import DomainCpuModelClass
from .DomainCpuModelPrivate import DomainCpuModelPrivate
from .DomainCpuPrivate import DomainCpuPrivate
from .DomainDeviceClass import DomainDeviceClass
from .DomainDevicePrivate import DomainDevicePrivate
from .DomainDisk import DomainDisk
from .DomainDiskBus import DomainDiskBus
from .DomainDiskCacheType import DomainDiskCacheType
from .DomainDiskClass import DomainDiskClass
from .DomainDiskDriver import DomainDiskDriver
from .DomainDiskDriverClass import DomainDiskDriverClass
from .DomainDiskDriverDiscard import DomainDiskDriverDiscard
from .DomainDiskDriverErrorPolicy import DomainDiskDriverErrorPolicy
from .DomainDiskDriverIoPolicy import DomainDiskDriverIoPolicy
from .DomainDiskDriverPrivate import DomainDiskDriverPrivate
from .DomainDiskFormat import DomainDiskFormat
from .DomainDiskGuestDeviceType import DomainDiskGuestDeviceType
from .DomainDiskPrivate import DomainDiskPrivate
from .DomainDiskSnapshotType import DomainDiskSnapshotType
from .DomainDiskStartupPolicy import DomainDiskStartupPolicy
from .DomainDiskType import DomainDiskType
from .DomainFilesys import DomainFilesys
from .DomainFilesysAccessType import DomainFilesysAccessType
from .DomainFilesysClass import DomainFilesysClass
from .DomainFilesysDriverType import DomainFilesysDriverType
from .DomainFilesysPrivate import DomainFilesysPrivate
from .DomainFilesysType import DomainFilesysType
from .DomainGraphics import DomainGraphics
from .DomainGraphicsClass import DomainGraphicsClass
from .DomainGraphicsDesktop import DomainGraphicsDesktop
from .DomainGraphicsDesktopClass import DomainGraphicsDesktopClass
from .DomainGraphicsDesktopPrivate import DomainGraphicsDesktopPrivate
from .DomainGraphicsPrivate import DomainGraphicsPrivate
from .DomainGraphicsRdp import DomainGraphicsRdp
from .DomainGraphicsRdpClass import DomainGraphicsRdpClass
from .DomainGraphicsRdpPrivate import DomainGraphicsRdpPrivate
from .DomainGraphicsSdl import DomainGraphicsSdl
from .DomainGraphicsSdlClass import DomainGraphicsSdlClass
from .DomainGraphicsSdlPrivate import DomainGraphicsSdlPrivate
from .DomainGraphicsSpice import DomainGraphicsSpice
from .DomainGraphicsSpiceClass import DomainGraphicsSpiceClass
from .DomainGraphicsSpiceImageCompression import DomainGraphicsSpiceImageCompression
from .DomainGraphicsSpicePrivate import DomainGraphicsSpicePrivate
from .DomainGraphicsVnc import DomainGraphicsVnc
from .DomainGraphicsVncClass import DomainGraphicsVncClass
from .DomainGraphicsVncPrivate import DomainGraphicsVncPrivate
from .DomainHostdev import DomainHostdev
from .DomainHostdevClass import DomainHostdevClass
from .DomainHostdevPci import DomainHostdevPci
from .DomainHostdevPciClass import DomainHostdevPciClass
from .DomainHostdevPciPrivate import DomainHostdevPciPrivate
from .DomainHostdevPrivate import DomainHostdevPrivate
from .DomainInput import DomainInput
from .DomainInputBus import DomainInputBus
from .DomainInputClass import DomainInputClass
from .DomainInputDeviceType import DomainInputDeviceType
from .DomainInputPrivate import DomainInputPrivate
from .DomainInterface import DomainInterface
from .DomainInterfaceBridge import DomainInterfaceBridge
from .DomainInterfaceBridgeClass import DomainInterfaceBridgeClass
from .DomainInterfaceBridgePrivate import DomainInterfaceBridgePrivate
from .DomainInterfaceClass import DomainInterfaceClass
from .DomainInterfaceFilterref import DomainInterfaceFilterref
from .DomainInterfaceFilterrefClass import DomainInterfaceFilterrefClass
from .DomainInterfaceFilterrefParameter import DomainInterfaceFilterrefParameter
from .DomainInterfaceFilterrefParameterClass import DomainInterfaceFilterrefParameterClass
from .DomainInterfaceFilterrefParameterPrivate import DomainInterfaceFilterrefParameterPrivate
from .DomainInterfaceFilterrefPrivate import DomainInterfaceFilterrefPrivate
from .DomainInterfaceLinkState import DomainInterfaceLinkState
from .DomainInterfaceNetwork import DomainInterfaceNetwork
from .DomainInterfaceNetworkClass import DomainInterfaceNetworkClass
from .DomainInterfaceNetworkPrivate import DomainInterfaceNetworkPrivate
from .DomainInterfacePrivate import DomainInterfacePrivate
from .DomainInterfaceUser import DomainInterfaceUser
from .DomainInterfaceUserClass import DomainInterfaceUserClass
from .DomainInterfaceUserPrivate import DomainInterfaceUserPrivate
from .DomainLifecycleAction import DomainLifecycleAction
from .DomainLifecycleEvent import DomainLifecycleEvent
from .DomainMemballoon import DomainMemballoon
from .DomainMemballoonClass import DomainMemballoonClass
from .DomainMemballoonModel import DomainMemballoonModel
from .DomainMemballoonPrivate import DomainMemballoonPrivate
from .DomainOs import DomainOs
from .DomainOsBootDevice import DomainOsBootDevice
from .DomainOsClass import DomainOsClass
from .DomainOsFirmware import DomainOsFirmware
from .DomainOsPrivate import DomainOsPrivate
from .DomainOsSmBiosMode import DomainOsSmBiosMode
from .DomainOsType import DomainOsType
from .DomainParallel import DomainParallel
from .DomainParallelClass import DomainParallelClass
from .DomainParallelPrivate import DomainParallelPrivate
from .DomainPowerManagement import DomainPowerManagement
from .DomainPowerManagementClass import DomainPowerManagementClass
from .DomainPowerManagementPrivate import DomainPowerManagementPrivate
from .DomainPrivate import DomainPrivate
from .DomainRedirdev import DomainRedirdev
from .DomainRedirdevBus import DomainRedirdevBus
from .DomainRedirdevClass import DomainRedirdevClass
from .DomainRedirdevPrivate import DomainRedirdevPrivate
from .DomainSeclabel import DomainSeclabel
from .DomainSeclabelClass import DomainSeclabelClass
from .DomainSeclabelPrivate import DomainSeclabelPrivate
from .DomainSeclabelType import DomainSeclabelType
from .DomainSerial import DomainSerial
from .DomainSerialClass import DomainSerialClass
from .DomainSerialPrivate import DomainSerialPrivate
from .DomainSmartcard import DomainSmartcard
from .DomainSmartcardClass import DomainSmartcardClass
from .DomainSmartcardHost import DomainSmartcardHost
from .DomainSmartcardHostCertificates import DomainSmartcardHostCertificates
from .DomainSmartcardHostCertificatesClass import DomainSmartcardHostCertificatesClass
from .DomainSmartcardHostCertificatesPrivate import DomainSmartcardHostCertificatesPrivate
from .DomainSmartcardHostClass import DomainSmartcardHostClass
from .DomainSmartcardHostPrivate import DomainSmartcardHostPrivate
from .DomainSmartcardPassthrough import DomainSmartcardPassthrough
from .DomainSmartcardPassthroughClass import DomainSmartcardPassthroughClass
from .DomainSmartcardPassthroughPrivate import DomainSmartcardPassthroughPrivate
from .DomainSmartcardPrivate import DomainSmartcardPrivate
from .DomainSnapshot import DomainSnapshot
from .DomainSnapshotClass import DomainSnapshotClass
from .DomainSnapshotDisk import DomainSnapshotDisk
from .DomainSnapshotDiskClass import DomainSnapshotDiskClass
from .DomainSnapshotDiskPrivate import DomainSnapshotDiskPrivate
from .DomainSnapshotDomainState import DomainSnapshotDomainState
from .DomainSnapshotMemoryState import DomainSnapshotMemoryState
from .DomainSnapshotPrivate import DomainSnapshotPrivate
from .DomainSound import DomainSound
from .DomainSoundClass import DomainSoundClass
from .DomainSoundModel import DomainSoundModel
from .DomainSoundPrivate import DomainSoundPrivate
from .DomainTimer import DomainTimer
from .DomainTimerClass import DomainTimerClass
from .DomainTimerHpet import DomainTimerHpet
from .DomainTimerHpetClass import DomainTimerHpetClass
from .DomainTimerHpetPrivate import DomainTimerHpetPrivate
from .DomainTimerPit import DomainTimerPit
from .DomainTimerPitClass import DomainTimerPitClass
from .DomainTimerPitPrivate import DomainTimerPitPrivate
from .DomainTimerPrivate import DomainTimerPrivate
from .DomainTimerRtc import DomainTimerRtc
from .DomainTimerRtcClass import DomainTimerRtcClass
from .DomainTimerRtcPrivate import DomainTimerRtcPrivate
from .DomainTimerTickPolicy import DomainTimerTickPolicy
from .DomainVideo import DomainVideo
from .DomainVideoClass import DomainVideoClass
from .DomainVideoModel import DomainVideoModel
from .DomainVideoPrivate import DomainVideoPrivate
from .DomainVirtType import DomainVirtType
from .Interface import Interface
from .InterfaceClass import InterfaceClass
from .InterfacePrivate import InterfacePrivate
from .Network import Network
from .NetworkClass import NetworkClass
from .NetworkFilter import NetworkFilter
from .NetworkFilterClass import NetworkFilterClass
from .NetworkFilterPrivate import NetworkFilterPrivate
from .NetworkPrivate import NetworkPrivate
from .NodeDevice import NodeDevice
from .NodeDeviceClass import NodeDeviceClass
from .NodeDevicePrivate import NodeDevicePrivate
from .ObjectClass import ObjectClass
from .ObjectPrivate import ObjectPrivate
from .Secret import Secret
from .SecretClass import SecretClass
from .SecretPrivate import SecretPrivate
from .StoragePermissions import StoragePermissions
from .StoragePermissionsClass import StoragePermissionsClass
from .StoragePermissionsPrivate import StoragePermissionsPrivate
from .StoragePool import StoragePool
from .StoragePoolClass import StoragePoolClass
from .StoragePoolPrivate import StoragePoolPrivate
from .StoragePoolSource import StoragePoolSource
from .StoragePoolSourceClass import StoragePoolSourceClass
from .StoragePoolSourcePrivate import StoragePoolSourcePrivate
from .StoragePoolTarget import StoragePoolTarget
from .StoragePoolTargetClass import StoragePoolTargetClass
from .StoragePoolTargetPrivate import StoragePoolTargetPrivate
from .StoragePoolType import StoragePoolType
from .StorageVol import StorageVol
from .StorageVolBackingStore import StorageVolBackingStore
from .StorageVolBackingStoreClass import StorageVolBackingStoreClass
from .StorageVolBackingStorePrivate import StorageVolBackingStorePrivate
from .StorageVolClass import StorageVolClass
from .StorageVolPrivate import StorageVolPrivate
from .StorageVolTarget import StorageVolTarget
from .StorageVolTargetClass import StorageVolTargetClass
from .StorageVolTargetFeatures import StorageVolTargetFeatures
from .StorageVolTargetPrivate import StorageVolTargetPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fa8c01e7d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/LibvirtGConfig-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.LibvirtGConfig', loader=<gi.importer.DynamicImporter object at 0x7fa8c01e7d00>)"

