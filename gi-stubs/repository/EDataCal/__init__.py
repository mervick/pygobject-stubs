# encoding: utf-8
# module gi.repository.EDataCal
# from /usr/lib64/girepository-1.0/EDataCal-2.0.typelib
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
import gi.repository.EBackend as __gi_repository_EBackend
import gi.repository.ECal as __gi_repository_ECal
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio


# Variables with simple values

EDS_CALENDAR_MODULES = 'EDS_CALENDAR_MODULES'

EDS_SUBPROCESS_CAL_PATH = 'EDS_SUBPROCESS_CAL_PATH'

INTERVALTREE_DEBUG = 1

LIBICAL_GLIB_UNSTABLE_API = 1

_namespace = 'EDataCal'

_version = '2.0'

__weakref__ = None

# functions

def cal_cache_offline_change_free(change=None): # real signature unknown; restored from __doc__
    """ cal_cache_offline_change_free(change=None) """
    pass

def cal_cache_search_data_free(ptr=None): # real signature unknown; restored from __doc__
    """ cal_cache_search_data_free(ptr=None) """
    pass

def cal_meta_backend_info_free(ptr=None): # real signature unknown; restored from __doc__
    """ cal_meta_backend_info_free(ptr=None) """
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

from .CalBackend import CalBackend
from .CalBackendClass import CalBackendClass
from .CalBackendFactory import CalBackendFactory
from .CalBackendFactoryClass import CalBackendFactoryClass
from .CalBackendFactoryPrivate import CalBackendFactoryPrivate
from .CalBackendPrivate import CalBackendPrivate
from .CalBackendSExp import CalBackendSExp
from .CalBackendSExpClass import CalBackendSExpClass
from .CalBackendSExpPrivate import CalBackendSExpPrivate
from .CalBackendSync import CalBackendSync
from .CalBackendSyncClass import CalBackendSyncClass
from .CalBackendSyncPrivate import CalBackendSyncPrivate
from .CalCache import CalCache
from .CalCacheClass import CalCacheClass
from .CalCacheOfflineChange import CalCacheOfflineChange
from .CalCachePrivate import CalCachePrivate
from .CalCacheSearchData import CalCacheSearchData
from .CalMetaBackend import CalMetaBackend
from .CalMetaBackendClass import CalMetaBackendClass
from .CalMetaBackendInfo import CalMetaBackendInfo
from .CalMetaBackendPrivate import CalMetaBackendPrivate
from .DataCal import DataCal
from .DataCalClass import DataCalClass
from .DataCalFactory import DataCalFactory
from .DataCalFactoryClass import DataCalFactoryClass
from .DataCalFactoryPrivate import DataCalFactoryPrivate
from .DataCalPrivate import DataCalPrivate
from .DataCalView import DataCalView
from .DataCalViewClass import DataCalViewClass
from .DataCalViewPrivate import DataCalViewPrivate
from .IntervalTree import IntervalTree
from .IntervalTreeClass import IntervalTreeClass
from .IntervalTreePrivate import IntervalTreePrivate
from .SubprocessCalFactory import SubprocessCalFactory
from .SubprocessCalFactoryClass import SubprocessCalFactoryClass
from .SubprocessCalFactoryPrivate import SubprocessCalFactoryPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fb65f50cd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/EDataCal-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.EDataCal', loader=<gi.importer.DynamicImporter object at 0x7fb65f50cd00>)"

