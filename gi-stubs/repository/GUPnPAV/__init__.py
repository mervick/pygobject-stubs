# encoding: utf-8
# module gi.repository.GUPnPAV
# from /usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib
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

DIDL_LITE_WRITER_NAMESPACE_DC = 'dc'
DIDL_LITE_WRITER_NAMESPACE_DLNA = 'dlna'
DIDL_LITE_WRITER_NAMESPACE_PV = 'pv'
DIDL_LITE_WRITER_NAMESPACE_UPNP = 'upnp'

_namespace = 'GUPnPAV'

_version = '1.0'

__weakref__ = None

# functions

def protocol_error_quark(): # real signature unknown; restored from __doc__
    """ protocol_error_quark() -> int """
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

from .CDSLastChangeEntry import CDSLastChangeEntry
from .CDSLastChangeEvent import CDSLastChangeEvent
from .CDSLastChangeParser import CDSLastChangeParser
from .CDSLastChangeParserClass import CDSLastChangeParserClass
from .CDSLastChangeParserPrivate import CDSLastChangeParserPrivate
from .DIDLLiteObject import DIDLLiteObject
from .DIDLLiteContainer import DIDLLiteContainer
from .DIDLLiteContainerClass import DIDLLiteContainerClass
from .DIDLLiteContributor import DIDLLiteContributor
from .DIDLLiteContributorClass import DIDLLiteContributorClass
from .DIDLLiteContributorPrivate import DIDLLiteContributorPrivate
from .DIDLLiteCreateClass import DIDLLiteCreateClass
from .DIDLLiteCreateClassClass import DIDLLiteCreateClassClass
from .DIDLLiteCreateClassPrivate import DIDLLiteCreateClassPrivate
from .DIDLLiteDescriptor import DIDLLiteDescriptor
from .DIDLLiteDescriptorClass import DIDLLiteDescriptorClass
from .DIDLLiteDescriptorPrivate import DIDLLiteDescriptorPrivate
from .DIDLLiteFragmentResult import DIDLLiteFragmentResult
from .DIDLLiteItem import DIDLLiteItem
from .DIDLLiteItemClass import DIDLLiteItemClass
from .DIDLLiteObjectClass import DIDLLiteObjectClass
from .DIDLLiteObjectPrivate import DIDLLiteObjectPrivate
from .DIDLLiteParser import DIDLLiteParser
from .DIDLLiteParserClass import DIDLLiteParserClass
from .DIDLLiteResource import DIDLLiteResource
from .DIDLLiteResourceClass import DIDLLiteResourceClass
from .DIDLLiteResourcePrivate import DIDLLiteResourcePrivate
from .DIDLLiteWriter import DIDLLiteWriter
from .DIDLLiteWriterClass import DIDLLiteWriterClass
from .DIDLLiteWriterPrivate import DIDLLiteWriterPrivate
from .DLNAConversion import DLNAConversion
from .DLNAFlags import DLNAFlags
from .DLNAOperation import DLNAOperation
from .Feature import Feature
from .FeatureClass import FeatureClass
from .FeatureListParser import FeatureListParser
from .FeatureListParserClass import FeatureListParserClass
from .FeaturePrivate import FeaturePrivate
from .LastChangeParser import LastChangeParser
from .LastChangeParserClass import LastChangeParserClass
from .MediaCollection import MediaCollection
from .MediaCollectionClass import MediaCollectionClass
from .MediaCollectionPrivate import MediaCollectionPrivate
from .OCMFlags import OCMFlags
from .ProtocolError import ProtocolError
from .ProtocolInfo import ProtocolInfo
from .ProtocolInfoClass import ProtocolInfoClass
from .ProtocolInfoPrivate import ProtocolInfoPrivate
from .SearchCriteriaOp import SearchCriteriaOp
from .SearchCriteriaParser import SearchCriteriaParser
from .SearchCriteriaParserClass import SearchCriteriaParserClass
from .SearchCriteriaParserError import SearchCriteriaParserError
from .SearchCriteriaParserPrivate import SearchCriteriaParserPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fda4efb4d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.GUPnPAV', loader=<gi.importer.DynamicImporter object at 0x7fda4efb4d00>)"

