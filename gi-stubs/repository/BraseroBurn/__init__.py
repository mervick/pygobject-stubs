# encoding: utf-8
# module gi.repository.BraseroBurn
# from /usr/lib64/girepository-1.0/BraseroBurn-3.1.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

COVER_URI = 'session::art::cover'

DATA_TRACK_SIZE_TAG = 'track::data::estimated_size'

DND_TARGET_DATA_TRACK_REFERENCE_LIST = 'GTK_TREE_MODEL_ROW'

DVD_STREAM_FORMAT = 'session::DVD::stream::format'

MIN_STREAM_LENGTH = 1705032704

SESSION_STREAM_AUDIO_FORMAT = 'session::stream::audio::format'

STREAM_TRACK_SIZE_TAG = 'track::stream::estimated_size'

TRACK_MEDIUM_ADDRESS_END_TAG = 'track::medium::address::end'

TRACK_MEDIUM_ADDRESS_START_TAG = 'track::medium::address::start'

TRACK_MEDIUM_WRONG_CHECKSUM_TAG = 'track::medium::error::checksum::list'

TRACK_STREAM_ALBUM_TAG = 'track::stream::info::album'

TRACK_STREAM_ARTIST_TAG = 'track::stream::info::artist'

TRACK_STREAM_COMPOSER_TAG = 'track::stream::info::composer'

TRACK_STREAM_ISRC_TAG = 'track::stream::info::isrc'

TRACK_STREAM_MIME_TAG = 'track::stream::mime'

TRACK_STREAM_THUMBNAIL_TAG = 'track::stream::snapshot'

TRACK_STREAM_TITLE_TAG = 'track::stream::info::title'

VCD_TYPE = 'session::VCD::format'

VIDEO_OUTPUT_ASPECT = 'session::video::aspect'
VIDEO_OUTPUT_FRAMERATE = 'session::video::framerate'

_namespace = 'BraseroBurn'

_version = '3.1'

__weakref__ = None

# functions

def graft_point_free(graft): # real signature unknown; restored from __doc__
    """ graft_point_free(graft:BraseroBurn.GraftPt) """
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

from .Burn import Burn
from .BurnAction import BurnAction
from .BurnClass import BurnClass
from .BurnDialog import BurnDialog
from .BurnDialogClass import BurnDialogClass
from .BurnError import BurnError
from .BurnFlag import BurnFlag
from .BurnOptions import BurnOptions
from .BurnOptionsClass import BurnOptionsClass
from .BurnResult import BurnResult
from .BurnSession import BurnSession
from .BurnSessionClass import BurnSessionClass
from .ChecksumType import ChecksumType
from .GraftPt import GraftPt
from .ImageFormat import ImageFormat
from .ImageFS import ImageFS
from .PluginErrorType import PluginErrorType
from .SessionSpan import SessionSpan
from .SessionCfg import SessionCfg
from .SessionCfgClass import SessionCfgClass
from .SessionError import SessionError
from .SessionSpanClass import SessionSpanClass
from .Status import Status
from .StatusClass import StatusClass
from .StatusType import StatusType
from .StreamFormat import StreamFormat
from .ToolDialog import ToolDialog
from .SumDialog import SumDialog
from .SumDialogClass import SumDialogClass
from .ToolDialogClass import ToolDialogClass
from .Track import Track
from .TrackClass import TrackClass
from .TrackData import TrackData
from .TrackDataCfg import TrackDataCfg
from .TrackDataCfgClass import TrackDataCfgClass
from .TrackDataCfgColumn import TrackDataCfgColumn
from .TrackDataClass import TrackDataClass
from .TrackDisc import TrackDisc
from .TrackDiscClass import TrackDiscClass
from .TrackImage import TrackImage
from .TrackImageCfg import TrackImageCfg
from .TrackImageCfgClass import TrackImageCfgClass
from .TrackImageClass import TrackImageClass
from .TrackStream import TrackStream
from .TrackStreamCfg import TrackStreamCfg
from .TrackStreamCfgClass import TrackStreamCfgClass
from .TrackStreamClass import TrackStreamClass
from .TrackType import TrackType
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fdd633c5d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/BraseroBurn-3.1.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.BraseroBurn', loader=<gi.importer.DynamicImporter object at 0x7fdd633c5d00>)"

