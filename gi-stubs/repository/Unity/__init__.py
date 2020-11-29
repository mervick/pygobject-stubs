# encoding: utf-8
# module gi.repository.Unity
# from /usr/lib/girepository-1.0/Unity-7.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Unity as __gi_overrides_Unity
import gi.repository.Dee as __gi_repository_Dee
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


# Variables with simple values

SCOPE_API_VERSION = 7

_namespace = 'Unity'

_version = '7.0'

__path__ = '/usr/lib/girepository-1.0/Unity-7.0.typelib'

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
    """ default object formatter """
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
    """ helper for pickle """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ helper for pickle """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(): # real signature unknown; restored from __doc__
    """
    __sizeof__() -> int
    size of object in memory, in bytes
    """
    return 0

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

from .AbstractPreview import AbstractPreview
from .AbstractPreviewClass import AbstractPreviewClass
from .AbstractPreviewPrivate import AbstractPreviewPrivate
from .AbstractScope import AbstractScope
from .AbstractScopeClass import AbstractScopeClass
from .AbstractScopePrivate import AbstractScopePrivate
from .ActivationResponse import ActivationResponse
from .ActivationResponseClass import ActivationResponseClass
from .ActivationResponsePrivate import ActivationResponsePrivate
from .ActivePlaylistContainer import ActivePlaylistContainer
from .ScopeSearchBase import ScopeSearchBase
from .DeprecatedScopeSearch import DeprecatedScopeSearch
from .AggregatedScopeSearch import AggregatedScopeSearch
from .AggregatedScopeSearchClass import AggregatedScopeSearchClass
from .AggregatedScopeSearchPrivate import AggregatedScopeSearchPrivate
from .AggregatorActivation import AggregatorActivation
from .AggregatorActivationClass import AggregatorActivationClass
from .AggregatorActivationPrivate import AggregatorActivationPrivate
from .DeprecatedScopeBase import DeprecatedScopeBase
from .AggregatorScope import AggregatorScope
from .AggregatorScopeClass import AggregatorScopeClass
from .AggregatorScopeMergeMode import AggregatorScopeMergeMode
from .AggregatorScopePrivate import AggregatorScopePrivate
from .AggregatorScopeSortFlags import AggregatorScopeSortFlags
from .AnnotatedIcon import AnnotatedIcon
from .AnnotatedIconClass import AnnotatedIconClass
from .AnnotatedIconPrivate import AnnotatedIconPrivate
from .AppInfoManager import AppInfoManager
from .AppInfoManagerClass import AppInfoManagerClass
from .AppInfoManagerPrivate import AppInfoManagerPrivate
from .Preview import Preview
from .ApplicationPreview import ApplicationPreview
from .ApplicationPreviewClass import ApplicationPreviewClass
from .ApplicationPreviewPrivate import ApplicationPreviewPrivate
from .Cancellable import Cancellable
from .CancellableClass import CancellableClass
from .CancellablePrivate import CancellablePrivate
from .Category import Category
from .CategoryClass import CategoryClass
from .CategoryContentType import CategoryContentType
from .CategoryPrivate import CategoryPrivate
from .CategoryRenderer import CategoryRenderer
from .CategorySet import CategorySet
from .CategorySetClass import CategorySetClass
from .CategorySetPrivate import CategorySetPrivate
from .CategoryType import CategoryType
from .Filter import Filter
from .OptionsFilter import OptionsFilter
from .CheckOptionFilter import CheckOptionFilter
from .CheckOptionFilterClass import CheckOptionFilterClass
from .CheckOptionFilterCompact import CheckOptionFilterCompact
from .CheckOptionFilterCompactClass import CheckOptionFilterCompactClass
from .CheckOptionFilterCompactPrivate import CheckOptionFilterCompactPrivate
from .CheckOptionFilterPrivate import CheckOptionFilterPrivate
from .DeprecatedScope import DeprecatedScope
from .DeprecatedScopeBaseClass import DeprecatedScopeBaseClass
from .DeprecatedScopeBasePrivate import DeprecatedScopeBasePrivate
from .DeprecatedScopeClass import DeprecatedScopeClass
from .DeprecatedScopePrivate import DeprecatedScopePrivate
from .DeprecatedScopeSearchClass import DeprecatedScopeSearchClass
from .DeprecatedScopeSearchPrivate import DeprecatedScopeSearchPrivate
from .FilterClass import FilterClass
from .FilterOption import FilterOption
from .FilterOptionClass import FilterOptionClass
from .FilterOptionPrivate import FilterOptionPrivate
from .FilterPrivate import FilterPrivate
from .FilterRenderer import FilterRenderer
from .FilterSet import FilterSet
from .FilterSetClass import FilterSetClass
from .FilterSetPrivate import FilterSetPrivate
from .GenericPreview import GenericPreview
from .GenericPreviewClass import GenericPreviewClass
from .GenericPreviewPrivate import GenericPreviewPrivate
from .GeoCoordinate import GeoCoordinate
from .GeoCoordinateClass import GeoCoordinateClass
from .GeoCoordinatePrivate import GeoCoordinatePrivate
from .HandledType import HandledType
from .IconSizeHint import IconSizeHint
from .InfoHint import InfoHint
from .InfoHintClass import InfoHintClass
from .InfoHintPrivate import InfoHintPrivate
from .Inspector import Inspector
from .InspectorClass import InspectorClass
from .InspectorPrivate import InspectorPrivate
from .LauncherEntry import LauncherEntry
from .LauncherEntryClass import LauncherEntryClass
from .LauncherEntryPrivate import LauncherEntryPrivate
from .LauncherFavorites import LauncherFavorites
from .LauncherFavoritesClass import LauncherFavoritesClass
from .LauncherFavoritesPrivate import LauncherFavoritesPrivate
from .LayoutHint import LayoutHint
from .MasterScope import MasterScope
from .MasterScopeClass import MasterScopeClass
from .MasterScopePrivate import MasterScopePrivate
from .MetadataProvider import MetadataProvider
from .MetadataProviderClass import MetadataProviderClass
from .MetadataProviderPrivate import MetadataProviderPrivate
from .MoviePreview import MoviePreview
from .MoviePreviewClass import MoviePreviewClass
from .MoviePreviewPrivate import MoviePreviewPrivate
from .MultiRangeFilter import MultiRangeFilter
from .MultiRangeFilterClass import MultiRangeFilterClass
from .MultiRangeFilterPrivate import MultiRangeFilterPrivate
from .MusicPlayer import MusicPlayer
from .MusicPlayerClass import MusicPlayerClass
from .MusicPlayerPrivate import MusicPlayerPrivate
from .MusicPreview import MusicPreview
from .MusicPreviewClass import MusicPreviewClass
from .MusicPreviewPrivate import MusicPreviewPrivate
from .MusicPreviewTrackState import MusicPreviewTrackState
from .OptionsFilterClass import OptionsFilterClass
from .OptionsFilterPrivate import OptionsFilterPrivate
from .OptionsFilterSortType import OptionsFilterSortType
from .PaymentPreview import PaymentPreview
from .PaymentPreviewClass import PaymentPreviewClass
from .PaymentPreviewPrivate import PaymentPreviewPrivate
from .PaymentPreviewType import PaymentPreviewType
from .PlaybackState import PlaybackState
from .Playlist import Playlist
from .PlaylistClass import PlaylistClass
from .PlaylistDetails import PlaylistDetails
from .PlaylistPrivate import PlaylistPrivate
from .PreferencesManager import PreferencesManager
from .PreferencesManagerClass import PreferencesManagerClass
from .PreferencesManagerPrivate import PreferencesManagerPrivate
from .PreferencesManagerRemoteContent import PreferencesManagerRemoteContent
from .PreviewAction import PreviewAction
from .PreviewActionClass import PreviewActionClass
from .PreviewActionPrivate import PreviewActionPrivate
from .PreviewClass import PreviewClass
from .PreviewPrivate import PreviewPrivate
from .ProgressSourceProvider import ProgressSourceProvider
from .ProgressSourceProviderClass import ProgressSourceProviderClass
from .ProgressSourceProviderPrivate import ProgressSourceProviderPrivate
from .RadioOptionFilter import RadioOptionFilter
from .RadioOptionFilterClass import RadioOptionFilterClass
from .RadioOptionFilterPrivate import RadioOptionFilterPrivate
from .RatingsFilter import RatingsFilter
from .RatingsFilterClass import RatingsFilterClass
from .RatingsFilterPrivate import RatingsFilterPrivate
from .ResultPreviewer import ResultPreviewer
from .ResultPreviewerClass import ResultPreviewerClass
from .ResultPreviewerPrivate import ResultPreviewerPrivate
from .ResultSet import ResultSet
from .ResultSetClass import ResultSetClass
from .ResultSetPrivate import ResultSetPrivate
from .ResultType import ResultType
from .Schema import Schema
from .SchemaClass import SchemaClass
from .SchemaFieldInfo import SchemaFieldInfo
from .SchemaFieldType import SchemaFieldType
from .SchemaPrivate import SchemaPrivate
from .ScopeDBusConnector import ScopeDBusConnector
from .ScopeDBusConnectorClass import ScopeDBusConnectorClass
from .ScopeDBusConnectorPrivate import ScopeDBusConnectorPrivate
from .ScopeLoader import ScopeLoader
from .ScopeLoaderClass import ScopeLoaderClass
from .ScopeLoaderPrivate import ScopeLoaderPrivate
from .ScopeResult import ScopeResult
from .ScopeSearchBaseClass import ScopeSearchBaseClass
from .ScopeSearchBasePrivate import ScopeSearchBasePrivate
from .SearchContext import SearchContext
from .SearchMetadata import SearchMetadata
from .SearchMetadataClass import SearchMetadataClass
from .SearchMetadataPrivate import SearchMetadataPrivate
from .SearchType import SearchType
from .SerializationType import SerializationType
from .SimpleScope import SimpleScope
from .SimpleScopeClass import SimpleScopeClass
from .SimpleScopePrivate import SimpleScopePrivate
from .SocialPreview import SocialPreview
from .SocialPreviewClass import SocialPreviewClass
from .SocialPreviewComment import SocialPreviewComment
from .SocialPreviewCommentClass import SocialPreviewCommentClass
from .SocialPreviewCommentPrivate import SocialPreviewCommentPrivate
from .SocialPreviewPrivate import SocialPreviewPrivate
from .TrackMetadata import TrackMetadata
from .TrackMetadataClass import TrackMetadataClass
from .TrackMetadataPrivate import TrackMetadataPrivate
from .__class__ import __class__
# variables with complex values

category_content_type_from_string = gi.FunctionInfo(category_content_type_from_string)

category_content_type_to_string = gi.FunctionInfo(category_content_type_to_string)

category_renderer_from_string = gi.FunctionInfo(category_renderer_from_string)

category_renderer_to_string = gi.FunctionInfo(category_renderer_to_string)

filter_renderer_from_string = gi.FunctionInfo(filter_renderer_from_string)

filter_renderer_to_string = gi.FunctionInfo(filter_renderer_to_string)

object_unref = gi.FunctionInfo(object_unref)

scope_module_get_version = gi.FunctionInfo(scope_module_get_version)

scope_module_load_scopes = gi.FunctionInfo(scope_module_load_scopes)

_introspection_module = None # (!) real value is "<IntrospectionModule 'Unity' from '/usr/lib/girepository-1.0/Unity-7.0.typelib'>"

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f0cf67da550>'

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Unity', loader=<gi.importer.DynamicImporter object at 0x7f0cf67da550>)"

