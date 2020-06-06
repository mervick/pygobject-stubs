# encoding: utf-8
# module gi.repository.RygelCore
# from /usr/lib64/girepository-1.0/RygelCore-2.6.typelib
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
import gi.repository.GUPnP as __gi_repository_GUPnP
import gobject as __gobject


# Variables with simple values

_namespace = 'RygelCore'

_version = '2.6'

__weakref__ = None

# functions

def get_pretty_host_name(): # real signature unknown; restored from __doc__
    """ get_pretty_host_name() -> str """
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

from .Configuration import Configuration
from .BaseConfiguration import BaseConfiguration
from .BaseConfigurationClass import BaseConfigurationClass
from .BaseConfigurationPrivate import BaseConfigurationPrivate
from .BasicManagement import BasicManagement
from .BasicManagementClass import BasicManagementClass
from .BasicManagementPrivate import BasicManagementPrivate
from .CmdlineConfig import CmdlineConfig
from .CmdlineConfigClass import CmdlineConfigClass
from .CmdlineConfigError import CmdlineConfigError
from .CmdlineConfigPrivate import CmdlineConfigPrivate
from .ConfigurationEntry import ConfigurationEntry
from .ConfigurationError import ConfigurationError
from .ConfigurationIface import ConfigurationIface
from .ConnectionManager import ConnectionManager
from .ConnectionManagerClass import ConnectionManagerClass
from .ConnectionManagerPrivate import ConnectionManagerPrivate
from .DBusAclProvider import DBusAclProvider
from .DBusAclProviderIface import DBusAclProviderIface
from .DBusInterface import DBusInterface
from .DBusInterfaceIface import DBusInterfaceIface
from .DescriptionFile import DescriptionFile
from .DescriptionFileClass import DescriptionFileClass
from .DescriptionFilePrivate import DescriptionFilePrivate
from .DLNAProfile import DLNAProfile
from .EnergyManagement import EnergyManagement
from .EnergyManagementClass import EnergyManagementClass
from .EnergyManagementPrivate import EnergyManagementPrivate
from .EnvironmentConfig import EnvironmentConfig
from .EnvironmentConfigClass import EnvironmentConfigClass
from .EnvironmentConfigPrivate import EnvironmentConfigPrivate
from .IconInfo import IconInfo
from .LogHandler import LogHandler
from .LogHandlerClass import LogHandlerClass
from .LogHandlerPrivate import LogHandlerPrivate
from .LogLevel import LogLevel
from .MediaDevice import MediaDevice
from .MediaDeviceClass import MediaDeviceClass
from .MediaDevicePrivate import MediaDevicePrivate
from .MetaConfig import MetaConfig
from .MetaConfigClass import MetaConfigClass
from .MetaConfigPrivate import MetaConfigPrivate
from .Plugin import Plugin
from .PluginCapabilities import PluginCapabilities
from .PluginClass import PluginClass
from .PluginInformation import PluginInformation
from .PluginInformationClass import PluginInformationClass
from .PluginInformationPrivate import PluginInformationPrivate
from .RecursiveModuleLoader import RecursiveModuleLoader
from .PluginLoader import PluginLoader
from .PluginLoaderClass import PluginLoaderClass
from .PluginLoaderPrivate import PluginLoaderPrivate
from .PluginPrivate import PluginPrivate
from .RecursiveModuleLoaderClass import RecursiveModuleLoaderClass
from .RecursiveModuleLoaderPrivate import RecursiveModuleLoaderPrivate
from .ResourceInfo import ResourceInfo
from .RootDevice import RootDevice
from .RootDeviceClass import RootDeviceClass
from .RootDeviceFactory import RootDeviceFactory
from .RootDeviceFactoryClass import RootDeviceFactoryClass
from .RootDeviceFactoryPrivate import RootDeviceFactoryPrivate
from .RootDevicePrivate import RootDevicePrivate
from .SectionEntry import SectionEntry
from .StateMachine import StateMachine
from .StateMachineIface import StateMachineIface
from .UserConfig import UserConfig
from .UserConfigClass import UserConfigClass
from .UserConfigPrivate import UserConfigPrivate
from .V1Hacks import V1Hacks
from .V1HacksClass import V1HacksClass
from .V1HacksPrivate import V1HacksPrivate
from .XMLUtils import XMLUtils
from .XMLUtilsChildIterator import XMLUtilsChildIterator
from .XMLUtilsIterator import XMLUtilsIterator
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f3821470d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/RygelCore-2.6.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.RygelCore', loader=<gi.importer.DynamicImporter object at 0x7f3821470d00>)"

