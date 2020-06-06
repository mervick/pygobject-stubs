# encoding: utf-8
# module gi.repository.Grl
# from /usr/lib64/girepository-1.0/Grl-0.3.typelib
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

CONFIG_KEY_APIKEY = 'api-key'

CONFIG_KEY_APIKEY_BLOB = 'api-key-blob'

CONFIG_KEY_APISECRET = 'api-secret'
CONFIG_KEY_APITOKEN = 'api-token'

CONFIG_KEY_APITOKEN_SECRET = 'api-token-secret'

CONFIG_KEY_PASSWORD = 'password'
CONFIG_KEY_PLUGIN = 'target-plugin'
CONFIG_KEY_SOURCE = 'target-source'
CONFIG_KEY_USERNAME = 'username'

COUNT_INFINITY = -1

KEYID_FORMAT = 'u'

METADATA_KEY_ALBUM = 1

METADATA_KEY_ALBUM_ARTIST = 60

METADATA_KEY_ALBUM_DISC_NUMBER = 58

METADATA_KEY_ARTIST = 2

METADATA_KEY_AUDIO_TRACK = 57

METADATA_KEY_AUTHOR = 3
METADATA_KEY_BITRATE = 4

METADATA_KEY_CAMERA_MODEL = 35

METADATA_KEY_CERTIFICATE = 5
METADATA_KEY_CHILDCOUNT = 6

METADATA_KEY_CHILDCOUNT_UNKNOWN = -1

METADATA_KEY_COMPOSER = 59

METADATA_KEY_CREATION_DATE = 34

METADATA_KEY_DESCRIPTION = 8
METADATA_KEY_DIRECTOR = 48
METADATA_KEY_DURATION = 9
METADATA_KEY_EPISODE = 32

METADATA_KEY_EPISODE_TITLE = 56

METADATA_KEY_EXPOSURE_TIME = 38

METADATA_KEY_EXTERNAL_PLAYER = 10
METADATA_KEY_EXTERNAL_URL = 11

METADATA_KEY_FAVOURITE = 43

METADATA_KEY_FLASH_USED = 37

METADATA_KEY_FRAMERATE = 12
METADATA_KEY_GENRE = 13
METADATA_KEY_HEIGHT = 14
METADATA_KEY_ID = 15
METADATA_KEY_INVALID = 0

METADATA_KEY_ISO_SPEED = 39

METADATA_KEY_KEYWORD = 45

METADATA_KEY_LAST_PLAYED = 16
METADATA_KEY_LAST_POSITION = 17

METADATA_KEY_LICENSE = 18
METADATA_KEY_LYRICS = 19

METADATA_KEY_MB_ALBUM_ID = 52

METADATA_KEY_MB_ARTIST_ID = 54

METADATA_KEY_MB_RECORDING_ID = 55

METADATA_KEY_MB_RELEASE_GROUP_ID = 62

METADATA_KEY_MB_RELEASE_ID = 61

METADATA_KEY_MB_TRACK_ID = 53

METADATA_KEY_MIME = 20

METADATA_KEY_MODIFICATION_DATE = 41

METADATA_KEY_ORIENTATION = 36

METADATA_KEY_ORIGINAL_TITLE = 49

METADATA_KEY_PERFORMER = 46

METADATA_KEY_PLAY_COUNT = 21

METADATA_KEY_PRODUCER = 47

METADATA_KEY_PUBLICATION_DATE = 7

METADATA_KEY_RATING = 22
METADATA_KEY_REGION = 44
METADATA_KEY_SEASON = 31
METADATA_KEY_SHOW = 33
METADATA_KEY_SITE = 23
METADATA_KEY_SIZE = 50
METADATA_KEY_SOURCE = 24

METADATA_KEY_START_TIME = 42

METADATA_KEY_STUDIO = 25
METADATA_KEY_THUMBNAIL = 26

METADATA_KEY_THUMBNAIL_BINARY = 27

METADATA_KEY_TITLE = 28

METADATA_KEY_TITLE_FROM_FILENAME = 51

METADATA_KEY_TRACK_NUMBER = 40

METADATA_KEY_URL = 29
METADATA_KEY_WIDTH = 30

PADDING = 16

PADDING_SMALL = 8

PLUGIN_AUTHOR = 'author'
PLUGIN_DESCRIPTION = 'description'
PLUGIN_LICENSE = 'license'

PLUGIN_LIST_VAR = 'GRL_PLUGIN_LIST'

PLUGIN_NAME = 'name'

PLUGIN_PATH_VAR = 'GRL_PLUGIN_PATH'

PLUGIN_RANKS_VAR = 'GRL_PLUGIN_RANKS'

PLUGIN_SITE = 'site'
PLUGIN_VERSION = 'version'

SOURCE_REMAINING_UNKNOWN = -1

_namespace = 'Grl'

_version = '0.3'

__weakref__ = None

# functions

def date_time_from_iso8601(date): # real signature unknown; restored from __doc__
    """ date_time_from_iso8601(date:str) -> GLib.DateTime """
    pass

def deinit(): # real signature unknown; restored from __doc__
    """ deinit() """
    pass

def g_value_dup(value): # real signature unknown; restored from __doc__
    """ g_value_dup(value:GObject.Value) -> GObject.Value """
    pass

def g_value_free(value): # real signature unknown; restored from __doc__
    """ g_value_free(value:GObject.Value) """
    pass

def g_value_hashtable_new(): # real signature unknown; restored from __doc__
    """ g_value_hashtable_new() -> dict """
    return {}

def g_value_hashtable_new_direct(): # real signature unknown; restored from __doc__
    """ g_value_hashtable_new_direct() -> dict """
    return {}

def g_value_new(g_type): # real signature unknown; restored from __doc__
    """ g_value_new(g_type:GType) -> GObject.Value """
    pass

def init(argv=None): # real signature unknown; restored from __doc__
    """ init(argv:list=None) -> argv:list """
    pass

def init_get_option_group(): # real signature unknown; restored from __doc__
    """ init_get_option_group() -> GLib.OptionGroup """
    pass

def log_configure(config): # real signature unknown; restored from __doc__
    """ log_configure(config:str) """
    pass

def metadata_key_get_desc(key): # real signature unknown; restored from __doc__
    """ metadata_key_get_desc(key:int) -> str """
    return ""

def metadata_key_get_name(key): # real signature unknown; restored from __doc__
    """ metadata_key_get_name(key:int) -> str """
    return ""

def metadata_key_get_type(key): # real signature unknown; restored from __doc__
    """ metadata_key_get_type(key:int) -> GType """
    pass

def multiple_get_media_from_uri(uri, keys, options, callback, user_data=None): # real signature unknown; restored from __doc__
    """ multiple_get_media_from_uri(uri:str, keys:list, options:Grl.OperationOptions, callback:Grl.SourceResolveCb, user_data=None) """
    pass

def multiple_search(sources=None, text, keys, options, callback, user_data=None): # real signature unknown; restored from __doc__
    """ multiple_search(sources:list=None, text:str, keys:list, options:Grl.OperationOptions, callback:Grl.SourceResultCb, user_data=None) -> int """
    return 0

def multiple_search_sync(sources=None, text, keys, options): # real signature unknown; restored from __doc__
    """ multiple_search_sync(sources:list=None, text:str, keys:list, options:Grl.OperationOptions) -> list """
    return []

def operation_cancel(operation_id): # real signature unknown; restored from __doc__
    """ operation_cancel(operation_id:int) """
    pass

def operation_get_data(operation_id): # real signature unknown; restored from __doc__
    """ operation_get_data(operation_id:int) """
    pass

def operation_set_data(operation_id, user_data=None): # real signature unknown; restored from __doc__
    """ operation_set_data(operation_id:int, user_data=None) """
    pass

def operation_set_data_full(operation_id, user_data=None, destroy_func=None): # real signature unknown; restored from __doc__
    """ operation_set_data_full(operation_id:int, user_data=None, destroy_func:GLib.DestroyNotify=None) """
    pass

def paging_translate(skip, count, max_page_size, page_size, page_number, internal_offset): # real signature unknown; restored from __doc__
    """ paging_translate(skip:int, count:int, max_page_size:int, page_size:int, page_number:int, internal_offset:int) """
    pass

def range_value_hashtable_insert(hash_table, key=None, min, max): # real signature unknown; restored from __doc__
    """ range_value_hashtable_insert(hash_table:dict, key=None, min:GObject.Value, max:GObject.Value) """
    pass

def range_value_hashtable_new(): # real signature unknown; restored from __doc__
    """ range_value_hashtable_new() -> dict """
    return {}

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

from .Caps import Caps
from .CapsClass import CapsClass
from .CapsPrivate import CapsPrivate
from .Config import Config
from .ConfigClass import ConfigClass
from .ConfigPrivate import ConfigPrivate
from .CoreError import CoreError
from .Data import Data
from .DataClass import DataClass
from .DataPrivate import DataPrivate
from .LogDomain import LogDomain
from .LogLevel import LogLevel
from .Media import Media
from .MediaClass import MediaClass
from .MediaPrivate import MediaPrivate
from .MediaSerializeType import MediaSerializeType
from .MediaType import MediaType
from .OperationOptions import OperationOptions
from .OperationOptionsClass import OperationOptionsClass
from .OperationOptionsPrivate import OperationOptionsPrivate
from .Plugin import Plugin
from .PluginClass import PluginClass
from .PluginDescriptor import PluginDescriptor
from .PluginPrivate import PluginPrivate
from .RangeValue import RangeValue
from .Rank import Rank
from .Registry import Registry
from .RegistryClass import RegistryClass
from .RegistryPrivate import RegistryPrivate
from .RelatedKeys import RelatedKeys
from .RelatedKeysClass import RelatedKeysClass
from .RelatedKeysPrivate import RelatedKeysPrivate
from .ResolutionFlags import ResolutionFlags
from .Source import Source
from .SourceBrowseSpec import SourceBrowseSpec
from .SourceChangeType import SourceChangeType
from .SourceClass import SourceClass
from .SourceMediaFromUriSpec import SourceMediaFromUriSpec
from .SourcePrivate import SourcePrivate
from .SourceQuerySpec import SourceQuerySpec
from .SourceRemoveSpec import SourceRemoveSpec
from .SourceResolveSpec import SourceResolveSpec
from .SourceSearchSpec import SourceSearchSpec
from .SourceStoreMetadataSpec import SourceStoreMetadataSpec
from .SourceStoreSpec import SourceStoreSpec
from .SupportedMedia import SupportedMedia
from .SupportedOps import SupportedOps
from .TypeFilter import TypeFilter
from .WriteFlags import WriteFlags
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fa04130ad00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Grl-0.3.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Grl', loader=<gi.importer.DynamicImporter object at 0x7fa04130ad00>)"

