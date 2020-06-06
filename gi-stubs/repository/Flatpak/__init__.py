# encoding: utf-8
# module gi.repository.Flatpak
# from /usr/lib64/girepository-1.0/Flatpak-1.0.typelib
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

MAJOR_VERSION = 1

MICRO_VERSION = 3

MINOR_VERSION = 6

_namespace = 'Flatpak'

_version = '1.0'

__weakref__ = None

# functions

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def get_default_arch(): # real signature unknown; restored from __doc__
    """ get_default_arch() -> str """
    return ""

def get_supported_arches(): # real signature unknown; restored from __doc__
    """ get_supported_arches() -> list """
    return []

def get_system_installations(cancellable=None): # real signature unknown; restored from __doc__
    """ get_system_installations(cancellable:Gio.Cancellable=None) -> list """
    return []

def portal_error_quark(): # real signature unknown; restored from __doc__
    """ portal_error_quark() -> int """
    return 0

def transaction_operation_type_to_string(kind): # real signature unknown; restored from __doc__
    """ transaction_operation_type_to_string(kind:Flatpak.TransactionOperationType) -> str """
    return ""

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

from .Ref import Ref
from .BundleRef import BundleRef
from .BundleRefClass import BundleRefClass
from .Error import Error
from .Installation import Installation
from .InstallationClass import InstallationClass
from .InstalledRef import InstalledRef
from .InstalledRefClass import InstalledRefClass
from .InstallFlags import InstallFlags
from .Instance import Instance
from .InstanceClass import InstanceClass
from .LaunchFlags import LaunchFlags
from .PortalError import PortalError
from .QueryFlags import QueryFlags
from .RefClass import RefClass
from .RefKind import RefKind
from .RelatedRef import RelatedRef
from .RelatedRefClass import RelatedRefClass
from .Remote import Remote
from .RemoteClass import RemoteClass
from .RemoteRef import RemoteRef
from .RemoteRefClass import RemoteRefClass
from .RemoteType import RemoteType
from .StorageType import StorageType
from .Transaction import Transaction
from .TransactionClass import TransactionClass
from .TransactionErrorDetails import TransactionErrorDetails
from .TransactionOperation import TransactionOperation
from .TransactionOperationClass import TransactionOperationClass
from .TransactionOperationType import TransactionOperationType
from .TransactionProgress import TransactionProgress
from .TransactionProgressClass import TransactionProgressClass
from .TransactionRemoteReason import TransactionRemoteReason
from .TransactionResult import TransactionResult
from .UninstallFlags import UninstallFlags
from .UpdateFlags import UpdateFlags
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f295435fd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Flatpak-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Flatpak', loader=<gi.importer.DynamicImporter object at 0x7f295435fd00>)"

