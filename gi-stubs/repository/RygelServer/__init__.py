# encoding: utf-8
# module gi.repository.RygelServer
# from /usr/lib64/girepository-1.0/RygelServer-2.6.typelib
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
import gi.repository.Gee as __gi_repository_Gee
import gi.repository.GUPnP as __gi_repository_GUPnP
import gi.repository.RygelCore as __gi_repository_RygelCore
import gobject as __gobject


# Variables with simple values

_namespace = 'RygelServer'

_version = '2.6'

__weakref__ = None

# functions

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

from .MediaObject import MediaObject
from .MediaItem import MediaItem
from .MediaFileItem import MediaFileItem
from .AudioItem import AudioItem
from .AudioItemClass import AudioItemClass
from .AudioItemPrivate import AudioItemPrivate
from .ContentDirectory import ContentDirectory
from .ContentDirectoryClass import ContentDirectoryClass
from .ContentDirectoryPrivate import ContentDirectoryPrivate
from .DataSource import DataSource
from .DataSourceError import DataSourceError
from .DataSourceIface import DataSourceIface
from .HTTPSeekRequest import HTTPSeekRequest
from .DLNAAvailableSeekRangeRequest import DLNAAvailableSeekRangeRequest
from .DLNAAvailableSeekRangeRequestClass import DLNAAvailableSeekRangeRequestClass
from .DLNAAvailableSeekRangeRequestPrivate import DLNAAvailableSeekRangeRequestPrivate
from .HTTPResponseElement import HTTPResponseElement
from .DLNAAvailableSeekRangeResponse import DLNAAvailableSeekRangeResponse
from .DLNAAvailableSeekRangeResponseClass import DLNAAvailableSeekRangeResponseClass
from .DLNAAvailableSeekRangeResponsePrivate import DLNAAvailableSeekRangeResponsePrivate
from .DTCPCleartextRequest import DTCPCleartextRequest
from .DTCPCleartextRequestClass import DTCPCleartextRequestClass
from .DTCPCleartextRequestPrivate import DTCPCleartextRequestPrivate
from .DTCPCleartextResponse import DTCPCleartextResponse
from .DTCPCleartextResponseClass import DTCPCleartextResponseClass
from .DTCPCleartextResponsePrivate import DTCPCleartextResponsePrivate
from .HTTPByteSeekRequest import HTTPByteSeekRequest
from .HTTPByteSeekRequestClass import HTTPByteSeekRequestClass
from .HTTPByteSeekRequestPrivate import HTTPByteSeekRequestPrivate
from .HTTPByteSeekResponse import HTTPByteSeekResponse
from .HTTPByteSeekResponseClass import HTTPByteSeekResponseClass
from .HTTPByteSeekResponsePrivate import HTTPByteSeekResponsePrivate
from .HTTPGetClass import HTTPGetClass
from .HTTPGetHandler import HTTPGetHandler
from .HTTPGetHandlerClass import HTTPGetHandlerClass
from .HTTPGetHandlerPrivate import HTTPGetHandlerPrivate
from .HTTPGetPrivate import HTTPGetPrivate
from .HTTPItemURI import HTTPItemURI
from .HTTPItemURIClass import HTTPItemURIClass
from .HTTPItemURIPrivate import HTTPItemURIPrivate
from .HTTPRequestClass import HTTPRequestClass
from .HTTPRequestError import HTTPRequestError
from .HTTPRequestPrivate import HTTPRequestPrivate
from .HTTPResponseClass import HTTPResponseClass
from .HTTPResponseElementClass import HTTPResponseElementClass
from .HTTPResponseElementPrivate import HTTPResponseElementPrivate
from .HTTPResponsePrivate import HTTPResponsePrivate
from .HTTPSeekRequestClass import HTTPSeekRequestClass
from .HTTPSeekRequestError import HTTPSeekRequestError
from .HTTPSeekRequestPrivate import HTTPSeekRequestPrivate
from .HTTPServerClass import HTTPServerClass
from .HTTPServerPrivate import HTTPServerPrivate
from .HTTPTimeSeekRequest import HTTPTimeSeekRequest
from .HTTPTimeSeekRequestClass import HTTPTimeSeekRequestClass
from .HTTPTimeSeekRequestPrivate import HTTPTimeSeekRequestPrivate
from .HTTPTimeSeekResponse import HTTPTimeSeekResponse
from .HTTPTimeSeekResponseClass import HTTPTimeSeekResponseClass
from .HTTPTimeSeekResponsePrivate import HTTPTimeSeekResponsePrivate
from .VisualItem import VisualItem
from .ImageItem import ImageItem
from .ImageItemClass import ImageItemClass
from .ImageItemPrivate import ImageItemPrivate
from .LogicalExpression import LogicalExpression
from .LogicalOperator import LogicalOperator
from .MediaArtStore import MediaArtStore
from .MediaArtStoreClass import MediaArtStoreClass
from .MediaArtStorePrivate import MediaArtStorePrivate
from .MediaContainer import MediaContainer
from .MediaContainerClass import MediaContainerClass
from .MediaContainerPrivate import MediaContainerPrivate
from .MediaEngine import MediaEngine
from .MediaEngineClass import MediaEngineClass
from .MediaEngineError import MediaEngineError
from .MediaEnginePrivate import MediaEnginePrivate
from .MediaFileItemClass import MediaFileItemClass
from .MediaFileItemPrivate import MediaFileItemPrivate
from .MediaItemClass import MediaItemClass
from .MediaItemPrivate import MediaItemPrivate
from .MediaObjectClass import MediaObjectClass
from .MediaObjectPrivate import MediaObjectPrivate
from .MediaObjects import MediaObjects
from .MediaObjectsClass import MediaObjectsClass
from .MediaObjectsPrivate import MediaObjectsPrivate
from .MediaResource import MediaResource
from .MediaResourceClass import MediaResourceClass
from .MediaResourcePrivate import MediaResourcePrivate
from .MediaServer import MediaServer
from .MediaServerClass import MediaServerClass
from .MediaServerPlugin import MediaServerPlugin
from .MediaServerPluginClass import MediaServerPluginClass
from .MediaServerPluginPrivate import MediaServerPluginPrivate
from .MediaServerPrivate import MediaServerPrivate
from .MusicItem import MusicItem
from .MusicItemClass import MusicItemClass
from .MusicItemPrivate import MusicItemPrivate
from .ObjectEventType import ObjectEventType
from .PhotoItem import PhotoItem
from .PhotoItemClass import PhotoItemClass
from .PhotoItemPrivate import PhotoItemPrivate
from .PlaylistItem import PlaylistItem
from .PlaylistItemClass import PlaylistItemClass
from .PlaylistItemPrivate import PlaylistItemPrivate
from .PlaySpeed import PlaySpeed
from .PlaySpeedError import PlaySpeedError
from .PlaySpeedRequest import PlaySpeedRequest
from .PlaySpeedRequestClass import PlaySpeedRequestClass
from .PlaySpeedRequestPrivate import PlaySpeedRequestPrivate
from .PlaySpeedResponse import PlaySpeedResponse
from .PlaySpeedResponseClass import PlaySpeedResponseClass
from .PlaySpeedResponsePrivate import PlaySpeedResponsePrivate
from .RelationalExpression import RelationalExpression
from .SearchableContainer import SearchableContainer
from .SearchableContainerIface import SearchableContainerIface
from .SearchExpression import SearchExpression
from .Serializer import Serializer
from .SerializerClass import SerializerClass
from .SerializerPrivate import SerializerPrivate
from .SerializerType import SerializerType
from .SimpleContainer import SimpleContainer
from .SimpleContainerClass import SimpleContainerClass
from .SimpleContainerPrivate import SimpleContainerPrivate
from .Subtitle import Subtitle
from .Thumbnail import Thumbnail
from .TrackableContainer import TrackableContainer
from .TrackableContainerIface import TrackableContainerIface
from .TrackableItem import TrackableItem
from .TrackableItemIface import TrackableItemIface
from .UpdatableObject import UpdatableObject
from .UpdatableObjectIface import UpdatableObjectIface
from .VideoItem import VideoItem
from .VideoItemClass import VideoItemClass
from .VideoItemPrivate import VideoItemPrivate
from .VisualItemIface import VisualItemIface
from .WritableContainer import WritableContainer
from .WritableContainerError import WritableContainerError
from .WritableContainerIface import WritableContainerIface
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fe1d2ef7d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/RygelServer-2.6.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.RygelServer', loader=<gi.importer.DynamicImporter object at 0x7fe1d2ef7d00>)"

