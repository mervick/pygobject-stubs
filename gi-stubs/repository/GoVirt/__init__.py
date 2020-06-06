# encoding: utf-8
# module gi.repository.GoVirt
# from /usr/lib64/girepository-1.0/GoVirt-1.0.typelib
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
import gi.repository.Rest as __gi_repository_Rest
import gobject as __gobject


# Variables with simple values

_namespace = 'GoVirt'

_version = '1.0'

__weakref__ = None

# functions

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def rest_call_error_quark(): # real signature unknown; restored from __doc__
    """ rest_call_error_quark() -> int """
    return 0

def set_proxy_options(proxy): # real signature unknown; restored from __doc__
    """ set_proxy_options(proxy:GoVirt.Proxy) """
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

from .Resource import Resource
from .Api import Api
from .ApiClass import ApiClass
from .ApiPrivate import ApiPrivate
from .Cdrom import Cdrom
from .CdromClass import CdromClass
from .CdromPrivate import CdromPrivate
from .Cluster import Cluster
from .ClusterClass import ClusterClass
from .ClusterPrivate import ClusterPrivate
from .Collection import Collection
from .CollectionClass import CollectionClass
from .CollectionPrivate import CollectionPrivate
from .DataCenter import DataCenter
from .DataCenterClass import DataCenterClass
from .DataCenterPrivate import DataCenterPrivate
from .Error import Error
from .Host import Host
from .HostClass import HostClass
from .HostPrivate import HostPrivate
from .Proxy import Proxy
from .ProxyClass import ProxyClass
from .ProxyPrivate import ProxyPrivate
from .ResourceClass import ResourceClass
from .ResourcePrivate import ResourcePrivate
from .RestCallError import RestCallError
from .StorageDomain import StorageDomain
from .StorageDomainClass import StorageDomainClass
from .StorageDomainFormatVersion import StorageDomainFormatVersion
from .StorageDomainPrivate import StorageDomainPrivate
from .StorageDomainState import StorageDomainState
from .StorageDomainType import StorageDomainType
from .Vm import Vm
from .VmClass import VmClass
from .VmDisplay import VmDisplay
from .VmDisplayClass import VmDisplayClass
from .VmDisplayPrivate import VmDisplayPrivate
from .VmDisplayType import VmDisplayType
from .VmPool import VmPool
from .VmPoolClass import VmPoolClass
from .VmPoolPrivate import VmPoolPrivate
from .VmPrivate import VmPrivate
from .VmState import VmState
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f5430925d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GoVirt-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GoVirt', loader=<gi.importer.DynamicImporter object at 0x7f5430925d00>)"

