# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

ERROR_NUM_ENTRIES = 27

MAJOR_VERSION = 2

MICRO_VERSION = 4

MINOR_VERSION = 8

_namespace = 'UDisks'

_version = '2.0'

__weakref__ = None

# functions

def block_interface_info(): # real signature unknown; restored from __doc__
    """ block_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def block_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ block_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def drive_ata_interface_info(): # real signature unknown; restored from __doc__
    """ drive_ata_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def drive_ata_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ drive_ata_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def drive_interface_info(): # real signature unknown; restored from __doc__
    """ drive_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def drive_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ drive_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def encrypted_interface_info(): # real signature unknown; restored from __doc__
    """ encrypted_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def encrypted_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ encrypted_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def filesystem_interface_info(): # real signature unknown; restored from __doc__
    """ filesystem_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def filesystem_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ filesystem_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def job_interface_info(): # real signature unknown; restored from __doc__
    """ job_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def job_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ job_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def loop_interface_info(): # real signature unknown; restored from __doc__
    """ loop_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def loop_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ loop_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def manager_interface_info(): # real signature unknown; restored from __doc__
    """ manager_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def manager_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ manager_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def mdraid_interface_info(): # real signature unknown; restored from __doc__
    """ mdraid_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def mdraid_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ mdraid_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def partition_interface_info(): # real signature unknown; restored from __doc__
    """ partition_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def partition_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ partition_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def partition_table_interface_info(): # real signature unknown; restored from __doc__
    """ partition_table_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def partition_table_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ partition_table_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
    return 0

def swapspace_interface_info(): # real signature unknown; restored from __doc__
    """ swapspace_interface_info() -> Gio.DBusInterfaceInfo """
    pass

def swapspace_override_properties(klass, property_id_begin): # real signature unknown; restored from __doc__
    """ swapspace_override_properties(klass:GObject.ObjectClass, property_id_begin:int) -> int """
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

from .Block import Block
from .BlockIface import BlockIface
from .BlockProxy import BlockProxy
from .BlockProxyClass import BlockProxyClass
from .BlockProxyPrivate import BlockProxyPrivate
from .BlockSkeleton import BlockSkeleton
from .BlockSkeletonClass import BlockSkeletonClass
from .BlockSkeletonPrivate import BlockSkeletonPrivate
from .Client import Client
from .Drive import Drive
from .DriveAta import DriveAta
from .DriveAtaIface import DriveAtaIface
from .DriveAtaProxy import DriveAtaProxy
from .DriveAtaProxyClass import DriveAtaProxyClass
from .DriveAtaProxyPrivate import DriveAtaProxyPrivate
from .DriveAtaSkeleton import DriveAtaSkeleton
from .DriveAtaSkeletonClass import DriveAtaSkeletonClass
from .DriveAtaSkeletonPrivate import DriveAtaSkeletonPrivate
from .DriveIface import DriveIface
from .DriveProxy import DriveProxy
from .DriveProxyClass import DriveProxyClass
from .DriveProxyPrivate import DriveProxyPrivate
from .DriveSkeleton import DriveSkeleton
from .DriveSkeletonClass import DriveSkeletonClass
from .DriveSkeletonPrivate import DriveSkeletonPrivate
from .Encrypted import Encrypted
from .EncryptedIface import EncryptedIface
from .EncryptedProxy import EncryptedProxy
from .EncryptedProxyClass import EncryptedProxyClass
from .EncryptedProxyPrivate import EncryptedProxyPrivate
from .EncryptedSkeleton import EncryptedSkeleton
from .EncryptedSkeletonClass import EncryptedSkeletonClass
from .EncryptedSkeletonPrivate import EncryptedSkeletonPrivate
from .Error import Error
from .Filesystem import Filesystem
from .FilesystemIface import FilesystemIface
from .FilesystemProxy import FilesystemProxy
from .FilesystemProxyClass import FilesystemProxyClass
from .FilesystemProxyPrivate import FilesystemProxyPrivate
from .FilesystemSkeleton import FilesystemSkeleton
from .FilesystemSkeletonClass import FilesystemSkeletonClass
from .FilesystemSkeletonPrivate import FilesystemSkeletonPrivate
from .Job import Job
from .JobIface import JobIface
from .JobProxy import JobProxy
from .JobProxyClass import JobProxyClass
from .JobProxyPrivate import JobProxyPrivate
from .JobSkeleton import JobSkeleton
from .JobSkeletonClass import JobSkeletonClass
from .JobSkeletonPrivate import JobSkeletonPrivate
from .Loop import Loop
from .LoopIface import LoopIface
from .LoopProxy import LoopProxy
from .LoopProxyClass import LoopProxyClass
from .LoopProxyPrivate import LoopProxyPrivate
from .LoopSkeleton import LoopSkeleton
from .LoopSkeletonClass import LoopSkeletonClass
from .LoopSkeletonPrivate import LoopSkeletonPrivate
from .Manager import Manager
from .ManagerIface import ManagerIface
from .ManagerProxy import ManagerProxy
from .ManagerProxyClass import ManagerProxyClass
from .ManagerProxyPrivate import ManagerProxyPrivate
from .ManagerSkeleton import ManagerSkeleton
from .ManagerSkeletonClass import ManagerSkeletonClass
from .ManagerSkeletonPrivate import ManagerSkeletonPrivate
from .MDRaid import MDRaid
from .MDRaidIface import MDRaidIface
from .MDRaidProxy import MDRaidProxy
from .MDRaidProxyClass import MDRaidProxyClass
from .MDRaidProxyPrivate import MDRaidProxyPrivate
from .MDRaidSkeleton import MDRaidSkeleton
from .MDRaidSkeletonClass import MDRaidSkeletonClass
from .MDRaidSkeletonPrivate import MDRaidSkeletonPrivate
from .Object import Object
from .ObjectIface import ObjectIface
from .ObjectInfo import ObjectInfo
from .ObjectManagerClient import ObjectManagerClient
from .ObjectManagerClientClass import ObjectManagerClientClass
from .ObjectManagerClientPrivate import ObjectManagerClientPrivate
from .ObjectProxy import ObjectProxy
from .ObjectProxyClass import ObjectProxyClass
from .ObjectProxyPrivate import ObjectProxyPrivate
from .ObjectSkeleton import ObjectSkeleton
from .ObjectSkeletonClass import ObjectSkeletonClass
from .ObjectSkeletonPrivate import ObjectSkeletonPrivate
from .Partition import Partition
from .PartitionIface import PartitionIface
from .PartitionProxy import PartitionProxy
from .PartitionProxyClass import PartitionProxyClass
from .PartitionProxyPrivate import PartitionProxyPrivate
from .PartitionSkeleton import PartitionSkeleton
from .PartitionSkeletonClass import PartitionSkeletonClass
from .PartitionSkeletonPrivate import PartitionSkeletonPrivate
from .PartitionTable import PartitionTable
from .PartitionTableIface import PartitionTableIface
from .PartitionTableProxy import PartitionTableProxy
from .PartitionTableProxyClass import PartitionTableProxyClass
from .PartitionTableProxyPrivate import PartitionTableProxyPrivate
from .PartitionTableSkeleton import PartitionTableSkeleton
from .PartitionTableSkeletonClass import PartitionTableSkeletonClass
from .PartitionTableSkeletonPrivate import PartitionTableSkeletonPrivate
from .PartitionTypeInfo import PartitionTypeInfo
from .PartitionTypeInfoFlags import PartitionTypeInfoFlags
from .Swapspace import Swapspace
from .SwapspaceIface import SwapspaceIface
from .SwapspaceProxy import SwapspaceProxy
from .SwapspaceProxyClass import SwapspaceProxyClass
from .SwapspaceProxyPrivate import SwapspaceProxyPrivate
from .SwapspaceSkeleton import SwapspaceSkeleton
from .SwapspaceSkeletonClass import SwapspaceSkeletonClass
from .SwapspaceSkeletonPrivate import SwapspaceSkeletonPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f13a8fd8d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/UDisks-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.UDisks', loader=<gi.importer.DynamicImporter object at 0x7f13a8fd8d00>)"

