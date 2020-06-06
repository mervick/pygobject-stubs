# encoding: utf-8
# module gi.repository.EBackend
# from /usr/lib64/girepository-1.0/EBackend-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

CACHE_COLUMN_OBJECT = 'ECacheOBJ'
CACHE_COLUMN_REVISION = 'ECacheREV'
CACHE_COLUMN_STATE = 'ECacheState'
CACHE_COLUMN_UID = 'ECacheUID'

CACHE_TABLE_KEYS = 'ECacheKeys'
CACHE_TABLE_OBJECTS = 'ECacheObjects'

EDS_REGISTRY_MODULES = 'EDS_REGISTRY_MODULES'

SOURCE_REGISTRY_SERVER_OBJECT_PATH = '/org/gnome/evolution/dataserver/SourceManager'

USER_PROMPTER_SERVER_OBJECT_PATH = '/org/gnome/evolution/dataserver/UserPrompter'

_namespace = 'EBackend'

_version = '1.2'

__weakref__ = None

# functions

def cache_column_info_free(info=None): # real signature unknown; restored from __doc__
    """ cache_column_info_free(info=None) """
    pass

def cache_offline_change_free(change=None): # real signature unknown; restored from __doc__
    """ cache_offline_change_free(change=None) """
    pass

def sqlite3_vfs_init(): # real signature unknown; restored from __doc__
    """ sqlite3_vfs_init() """
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

from .AuthenticationSessionResult import AuthenticationSessionResult
from .Backend import Backend
from .BackendClass import BackendClass
from .BackendFactory import BackendFactory
from .BackendFactoryClass import BackendFactoryClass
from .BackendFactoryPrivate import BackendFactoryPrivate
from .BackendPrivate import BackendPrivate
from .Cache import Cache
from .CacheClass import CacheClass
from .CacheColumnInfo import CacheColumnInfo
from .CacheColumnValues import CacheColumnValues
from .CacheDeletedFlag import CacheDeletedFlag
from .CacheError import CacheError
from .CacheLockType import CacheLockType
from .CacheOfflineChange import CacheOfflineChange
from .CacheOfflineFlag import CacheOfflineFlag
from .CachePrivate import CachePrivate
from .CacheReaper import CacheReaper
from .CacheReaperClass import CacheReaperClass
from .CacheUnlockAction import CacheUnlockAction
from .CollectionBackend import CollectionBackend
from .CollectionBackendClass import CollectionBackendClass
from .CollectionBackendFactory import CollectionBackendFactory
from .CollectionBackendFactoryClass import CollectionBackendFactoryClass
from .CollectionBackendFactoryPrivate import CollectionBackendFactoryPrivate
from .CollectionBackendPrivate import CollectionBackendPrivate
from .DBusServer import DBusServer
from .DataFactory import DataFactory
from .DataFactoryClass import DataFactoryClass
from .DataFactoryPrivate import DataFactoryPrivate
from .DBusServerClass import DBusServerClass
from .DBusServerExitCode import DBusServerExitCode
from .DBusServerPrivate import DBusServerPrivate
from .FileCache import FileCache
from .FileCacheClass import FileCacheClass
from .FileCachePrivate import FileCachePrivate
from .OAuth2Support import OAuth2Support
from .OAuth2SupportInterface import OAuth2SupportInterface
from .OfflineState import OfflineState
from .ServerSideSource import ServerSideSource
from .ServerSideSourceClass import ServerSideSourceClass
from .ServerSideSourceCredentialsProvider import ServerSideSourceCredentialsProvider
from .ServerSideSourceCredentialsProviderClass import ServerSideSourceCredentialsProviderClass
from .ServerSideSourceCredentialsProviderPrivate import ServerSideSourceCredentialsProviderPrivate
from .ServerSideSourcePrivate import ServerSideSourcePrivate
from .SourcePermissionFlags import SourcePermissionFlags
from .SourceRegistryServer import SourceRegistryServer
from .SourceRegistryServerClass import SourceRegistryServerClass
from .SourceRegistryServerPrivate import SourceRegistryServerPrivate
from .SubprocessFactory import SubprocessFactory
from .SubprocessFactoryClass import SubprocessFactoryClass
from .SubprocessFactoryPrivate import SubprocessFactoryPrivate
from .UserPrompter import UserPrompter
from .UserPrompterClass import UserPrompterClass
from .UserPrompterPrivate import UserPrompterPrivate
from .UserPrompterServer import UserPrompterServer
from .UserPrompterServerClass import UserPrompterServerClass
from .UserPrompterServerExtension import UserPrompterServerExtension
from .UserPrompterServerExtensionClass import UserPrompterServerExtensionClass
from .UserPrompterServerExtensionPrivate import UserPrompterServerExtensionPrivate
from .UserPrompterServerPrivate import UserPrompterServerPrivate
from .WebDAVCollectionBackend import WebDAVCollectionBackend
from .WebDAVCollectionBackendClass import WebDAVCollectionBackendClass
from .WebDAVCollectionBackendPrivate import WebDAVCollectionBackendPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f9dc3c5dd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EBackend-1.2.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EBackend', loader=<gi.importer.DynamicImporter object at 0x7f9dc3c5dd00>)"

