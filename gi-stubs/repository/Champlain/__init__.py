# encoding: utf-8
# module gi.repository.Champlain
# from /usr/lib64/girepository-1.0/Champlain-0.12.typelib
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
import gi.repository.Clutter as __gi_repository_Clutter
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


# Variables with simple values

MAJOR_VERSION = 0

MAP_SOURCE_MEMPHIS_LOCAL = 'memphis-local'
MAP_SOURCE_MEMPHIS_NETWORK = 'memphis-network'

MAP_SOURCE_MFF_RELIEF = 'mff-relief'

MAP_SOURCE_OAM = 'OpenAerialMap'

MAP_SOURCE_OSM_AERIAL_MAP = 'osm-aerialmap'

MAP_SOURCE_OSM_CYCLE_MAP = 'osm-cyclemap'

MAP_SOURCE_OSM_MAPNIK = 'osm-mapnik'
MAP_SOURCE_OSM_MAPQUEST = 'osm-mapquest'
MAP_SOURCE_OSM_OSMARENDER = 'osm-osmarender'

MAP_SOURCE_OSM_TRANSPORT_MAP = 'osm-transportmap'

MAP_SOURCE_OWM_CLOUDS = 'owm-clouds'
MAP_SOURCE_OWM_PRECIPITATION = 'owm-precipitation'
MAP_SOURCE_OWM_PRESSURE = 'owm-pressure'
MAP_SOURCE_OWM_TEMPERATURE = 'owm-temperature'
MAP_SOURCE_OWM_WIND = 'owm-wind'

MAX_LATITUDE = 85.051129
MAX_LONGITUDE = 180.0

MICRO_VERSION = 20

MINOR_VERSION = 12

MIN_LATITUDE = 85.051129
MIN_LONGITUDE = 180.0

VERSION = 0.12

VERSION_HEX = 0
VERSION_S = '0.12.20'

_namespace = 'Champlain'

_version = '0.12'

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

from .Adjustment import Adjustment
from .AdjustmentClass import AdjustmentClass
from .AdjustmentPrivate import AdjustmentPrivate
from .BoundingBox import BoundingBox
from .Location import Location
from .Coordinate import Coordinate
from .CoordinateClass import CoordinateClass
from .CoordinatePrivate import CoordinatePrivate
from .Marker import Marker
from .CustomMarker import CustomMarker
from .CustomMarkerClass import CustomMarkerClass
from .CustomMarkerPrivate import CustomMarkerPrivate
from .Renderer import Renderer
from .ErrorTileRenderer import ErrorTileRenderer
from .ErrorTileRendererClass import ErrorTileRendererClass
from .ErrorTileRendererPrivate import ErrorTileRendererPrivate
from .Exportable import Exportable
from .ExportableIface import ExportableIface
from .MapSource import MapSource
from .TileCache import TileCache
from .FileCache import FileCache
from .FileCacheClass import FileCacheClass
from .FileCachePrivate import FileCachePrivate
from .TileSource import TileSource
from .FileTileSource import FileTileSource
from .FileTileSourceClass import FileTileSourceClass
from .FileTileSourcePrivate import FileTileSourcePrivate
from .ImageRenderer import ImageRenderer
from .ImageRendererClass import ImageRendererClass
from .ImageRendererPrivate import ImageRendererPrivate
from .KineticScrollView import KineticScrollView
from .KineticScrollViewClass import KineticScrollViewClass
from .KineticScrollViewPrivate import KineticScrollViewPrivate
from .Label import Label
from .LabelClass import LabelClass
from .LabelPrivate import LabelPrivate
from .Layer import Layer
from .LayerClass import LayerClass
from .License import License
from .LicenseClass import LicenseClass
from .LicensePrivate import LicensePrivate
from .LocationIface import LocationIface
from .MapProjection import MapProjection
from .MapSourceChain import MapSourceChain
from .MapSourceChainClass import MapSourceChainClass
from .MapSourceChainPrivate import MapSourceChainPrivate
from .MapSourceClass import MapSourceClass
from .MapSourceDesc import MapSourceDesc
from .MapSourceDescClass import MapSourceDescClass
from .MapSourceDescPrivate import MapSourceDescPrivate
from .MapSourceFactory import MapSourceFactory
from .MapSourceFactoryClass import MapSourceFactoryClass
from .MapSourceFactoryPrivate import MapSourceFactoryPrivate
from .MapSourcePrivate import MapSourcePrivate
from .MarkerClass import MarkerClass
from .MarkerLayer import MarkerLayer
from .MarkerLayerClass import MarkerLayerClass
from .MarkerLayerPrivate import MarkerLayerPrivate
from .MarkerPrivate import MarkerPrivate
from .MemoryCache import MemoryCache
from .MemoryCacheClass import MemoryCacheClass
from .MemoryCachePrivate import MemoryCachePrivate
from .NetworkBboxTileSource import NetworkBboxTileSource
from .NetworkBboxTileSourceClass import NetworkBboxTileSourceClass
from .NetworkBboxTileSourcePrivate import NetworkBboxTileSourcePrivate
from .NetworkTileSource import NetworkTileSource
from .NetworkTileSourceClass import NetworkTileSourceClass
from .NetworkTileSourcePrivate import NetworkTileSourcePrivate
from .NullTileSource import NullTileSource
from .NullTileSourceClass import NullTileSourceClass
from .NullTileSourcePrivate import NullTileSourcePrivate
from .PathLayer import PathLayer
from .PathLayerClass import PathLayerClass
from .PathLayerPrivate import PathLayerPrivate
from .Point import Point
from .PointClass import PointClass
from .PointPrivate import PointPrivate
from .RendererClass import RendererClass
from .Scale import Scale
from .ScaleClass import ScaleClass
from .ScalePrivate import ScalePrivate
from .SelectionMode import SelectionMode
from .State import State
from .Tile import Tile
from .TileCacheClass import TileCacheClass
from .TileCachePrivate import TileCachePrivate
from .TileClass import TileClass
from .TilePrivate import TilePrivate
from .TileSourceClass import TileSourceClass
from .TileSourcePrivate import TileSourcePrivate
from .Unit import Unit
from .View import View
from .ViewClass import ViewClass
from .Viewport import Viewport
from .ViewportClass import ViewportClass
from .ViewportPrivate import ViewportPrivate
from .ViewPrivate import ViewPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f2e2ea84d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Champlain-0.12.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Champlain', loader=<gi.importer.DynamicImporter object at 0x7f2e2ea84d00>)"

