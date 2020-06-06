# encoding: utf-8
# module gi.repository.LibvirtGObject
# from /usr/lib64/girepository-1.0/LibvirtGObject-1.0.typelib
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

_namespace = 'LibvirtGObject'

_version = '1.0'

__weakref__ = None

# functions

def init_object(argv=None): # real signature unknown; restored from __doc__
    """ init_object(argv:list=None) -> argv:list """
    pass

def init_object_check(argv=None): # real signature unknown; restored from __doc__
    """ init_object_check(argv:list=None) -> bool, argv:list """
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

from .Connection import Connection
from .ConnectionClass import ConnectionClass
from .ConnectionHandle import ConnectionHandle
from .ConnectionPrivate import ConnectionPrivate
from .Domain import Domain
from .DomainClass import DomainClass
from .DomainDeleteFlags import DomainDeleteFlags
from .DomainDevice import DomainDevice
from .DomainDeviceClass import DomainDeviceClass
from .DomainDevicePrivate import DomainDevicePrivate
from .DomainDisk import DomainDisk
from .DomainDiskClass import DomainDiskClass
from .DomainDiskPrivate import DomainDiskPrivate
from .DomainDiskStats import DomainDiskStats
from .DomainHandle import DomainHandle
from .DomainInfo import DomainInfo
from .DomainInterface import DomainInterface
from .DomainInterfaceClass import DomainInterfaceClass
from .DomainInterfacePrivate import DomainInterfacePrivate
from .DomainInterfaceStats import DomainInterfaceStats
from .DomainPrivate import DomainPrivate
from .DomainRebootFlags import DomainRebootFlags
from .DomainShutdownFlags import DomainShutdownFlags
from .DomainSnapshot import DomainSnapshot
from .DomainSnapshotClass import DomainSnapshotClass
from .DomainSnapshotCreateFlags import DomainSnapshotCreateFlags
from .DomainSnapshotDeleteFlags import DomainSnapshotDeleteFlags
from .DomainSnapshotHandle import DomainSnapshotHandle
from .DomainSnapshotListFlags import DomainSnapshotListFlags
from .DomainSnapshotPrivate import DomainSnapshotPrivate
from .DomainSnapshotRevertFlags import DomainSnapshotRevertFlags
from .DomainStartFlags import DomainStartFlags
from .DomainState import DomainState
from .DomainUpdateDeviceFlags import DomainUpdateDeviceFlags
from .DomainXMLFlags import DomainXMLFlags
from .Interface import Interface
from .InterfaceClass import InterfaceClass
from .InterfaceHandle import InterfaceHandle
from .InterfacePrivate import InterfacePrivate
from .IPAddrType import IPAddrType
from .Manager import Manager
from .ManagerClass import ManagerClass
from .ManagerPrivate import ManagerPrivate
from .Network import Network
from .NetworkClass import NetworkClass
from .NetworkDHCPLease import NetworkDHCPLease
from .NetworkDHCPLeaseClass import NetworkDHCPLeaseClass
from .NetworkDHCPLeasePrivate import NetworkDHCPLeasePrivate
from .NetworkFilter import NetworkFilter
from .NetworkFilterClass import NetworkFilterClass
from .NetworkFilterHandle import NetworkFilterHandle
from .NetworkFilterPrivate import NetworkFilterPrivate
from .NetworkHandle import NetworkHandle
from .NetworkPrivate import NetworkPrivate
from .NodeDevice import NodeDevice
from .NodeDeviceClass import NodeDeviceClass
from .NodeDeviceHandle import NodeDeviceHandle
from .NodeDevicePrivate import NodeDevicePrivate
from .NodeInfo import NodeInfo
from .Secret import Secret
from .SecretClass import SecretClass
from .SecretHandle import SecretHandle
from .SecretPrivate import SecretPrivate
from .StoragePool import StoragePool
from .StoragePoolClass import StoragePoolClass
from .StoragePoolHandle import StoragePoolHandle
from .StoragePoolInfo import StoragePoolInfo
from .StoragePoolPrivate import StoragePoolPrivate
from .StoragePoolState import StoragePoolState
from .StorageVol import StorageVol
from .StorageVolClass import StorageVolClass
from .StorageVolHandle import StorageVolHandle
from .StorageVolInfo import StorageVolInfo
from .StorageVolPrivate import StorageVolPrivate
from .StorageVolResizeFlags import StorageVolResizeFlags
from .StorageVolType import StorageVolType
from .Stream import Stream
from .StreamClass import StreamClass
from .StreamHandle import StreamHandle
from .StreamIOCondition import StreamIOCondition
from .StreamPrivate import StreamPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7ffa707edd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/LibvirtGObject-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.LibvirtGObject', loader=<gi.importer.DynamicImporter object at 0x7ffa707edd00>)"

