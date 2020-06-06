# encoding: utf-8
# module gi.repository.Modulemd
# from /usr/lib64/girepository-1.0/Modulemd-1.0.typelib
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

_namespace = 'Modulemd'

_version = '2.0'

__weakref__ = None

# functions

def compression_type(name): # real signature unknown; restored from __doc__
    """ compression_type(name:str) -> Modulemd.CompressionTypeEnum """
    pass

def error_quark(): # real signature unknown; restored from __doc__
    """ error_quark() -> int """
    return 0

def get_version(): # real signature unknown; restored from __doc__
    """ get_version() -> str """
    return ""

def yaml_error_quark(): # real signature unknown; restored from __doc__
    """ yaml_error_quark() -> int """
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

from .Buildopts import Buildopts
from .BuildoptsClass import BuildoptsClass
from .Component import Component
from .ComponentClass import ComponentClass
from .ComponentModule import ComponentModule
from .ComponentModuleClass import ComponentModuleClass
from .ComponentRpm import ComponentRpm
from .ComponentRpmClass import ComponentRpmClass
from .CompressionTypeEnum import CompressionTypeEnum
from .Defaults import Defaults
from .DefaultsClass import DefaultsClass
from .DefaultsV1 import DefaultsV1
from .DefaultsV1Class import DefaultsV1Class
from .DefaultsVersionEnum import DefaultsVersionEnum
from .Dependencies import Dependencies
from .DependenciesClass import DependenciesClass
from .Error import Error
from .ErrorEnum import ErrorEnum
from .Module import Module
from .ModuleClass import ModuleClass
from .ModuleIndex import ModuleIndex
from .ModuleIndexClass import ModuleIndexClass
from .ModuleIndexMerger import ModuleIndexMerger
from .ModuleIndexMergerClass import ModuleIndexMergerClass
from .ModuleStream import ModuleStream
from .ModuleStreamClass import ModuleStreamClass
from .ModuleStreamV1 import ModuleStreamV1
from .ModuleStreamV1Class import ModuleStreamV1Class
from .ModuleStreamV2 import ModuleStreamV2
from .ModuleStreamV2Class import ModuleStreamV2Class
from .ModuleStreamVersionEnum import ModuleStreamVersionEnum
from .Profile import Profile
from .ProfileClass import ProfileClass
from .RpmMapEntry import RpmMapEntry
from .RpmMapEntryClass import RpmMapEntryClass
from .ServiceLevel import ServiceLevel
from .ServiceLevelClass import ServiceLevelClass
from .SubdocumentInfo import SubdocumentInfo
from .SubdocumentInfoClass import SubdocumentInfoClass
from .Translation import Translation
from .TranslationClass import TranslationClass
from .TranslationEntry import TranslationEntry
from .TranslationEntryClass import TranslationEntryClass
from .YamlError import YamlError
from .YamlErrorEnum import YamlErrorEnum
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f723ffe5d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Modulemd-2.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Modulemd', loader=<gi.importer.DynamicImporter object at 0x7f723ffe5d00>)"

