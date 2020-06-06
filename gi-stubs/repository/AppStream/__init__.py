# encoding: utf-8
# module gi.repository.AppStream
# from /usr/lib64/girepository-1.0/AppStream-1.0.typelib
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

_namespace = 'AppStream'

_version = '1.0'

__weakref__ = None

# functions

def component_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ component_kind_from_string(kind_str:str) -> AppStream.ComponentKind """
    pass

def component_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ component_kind_to_string(kind:AppStream.ComponentKind) -> str """
    return ""

def format_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ format_kind_from_string(kind_str:str) -> AppStream.FormatKind """
    pass

def format_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ format_kind_to_string(kind:AppStream.FormatKind) -> str """
    return ""

def format_version_from_string(version_str): # real signature unknown; restored from __doc__
    """ format_version_from_string(version_str:str) -> AppStream.FormatVersion """
    pass

def format_version_to_string(version): # real signature unknown; restored from __doc__
    """ format_version_to_string(version:AppStream.FormatVersion) -> str """
    return ""

def get_appstream_version(): # real signature unknown; restored from __doc__
    """ get_appstream_version() -> str """
    return ""

def get_current_distro_component_id(): # real signature unknown; restored from __doc__
    """ get_current_distro_component_id() -> str """
    return ""

def get_default_categories(with_special): # real signature unknown; restored from __doc__
    """ get_default_categories(with_special:bool) -> list """
    return []

def get_license_url(license): # real signature unknown; restored from __doc__
    """ get_license_url(license:str) -> str """
    return ""

def is_spdx_license_exception_id(exception_id): # real signature unknown; restored from __doc__
    """ is_spdx_license_exception_id(exception_id:str) -> bool """
    return False

def is_spdx_license_expression(license): # real signature unknown; restored from __doc__
    """ is_spdx_license_expression(license:str) -> bool """
    return False

def is_spdx_license_id(license_id): # real signature unknown; restored from __doc__
    """ is_spdx_license_id(license_id:str) -> bool """
    return False

def license_is_free_license(license): # real signature unknown; restored from __doc__
    """ license_is_free_license(license:str) -> bool """
    return False

def license_is_metadata_license(license): # real signature unknown; restored from __doc__
    """ license_is_metadata_license(license:str) -> bool """
    return False

def license_to_spdx_id(license): # real signature unknown; restored from __doc__
    """ license_to_spdx_id(license:str) -> str """
    return ""

def markup_convert_simple(markup): # real signature unknown; restored from __doc__
    """ markup_convert_simple(markup:str) -> str """
    return ""

def merge_kind_from_string(kind_str): # real signature unknown; restored from __doc__
    """ merge_kind_from_string(kind_str:str) -> AppStream.MergeKind """
    pass

def merge_kind_to_string(kind): # real signature unknown; restored from __doc__
    """ merge_kind_to_string(kind:AppStream.MergeKind) -> str """
    return ""

def size_kind_from_string(size_kind): # real signature unknown; restored from __doc__
    """ size_kind_from_string(size_kind:str) -> AppStream.SizeKind """
    pass

def size_kind_to_string(size_kind): # real signature unknown; restored from __doc__
    """ size_kind_to_string(size_kind:AppStream.SizeKind) -> str """
    return ""

def spdx_license_detokenize(license_tokens): # real signature unknown; restored from __doc__
    """ spdx_license_detokenize(license_tokens:str) -> str or None """
    return ""

def spdx_license_tokenize(license): # real signature unknown; restored from __doc__
    """ spdx_license_tokenize(license:str) -> list or None """
    return []

def urgency_kind_from_string(urgency_kind): # real signature unknown; restored from __doc__
    """ urgency_kind_from_string(urgency_kind:str) -> AppStream.UrgencyKind """
    pass

def urgency_kind_to_string(urgency_kind): # real signature unknown; restored from __doc__
    """ urgency_kind_to_string(urgency_kind:AppStream.UrgencyKind) -> str """
    return ""

def url_kind_from_string(url_kind): # real signature unknown; restored from __doc__
    """ url_kind_from_string(url_kind:str) -> AppStream.UrlKind """
    pass

def url_kind_to_string(url_kind): # real signature unknown; restored from __doc__
    """ url_kind_to_string(url_kind:AppStream.UrlKind) -> str """
    return ""

def utils_compare_versions(a, b): # real signature unknown; restored from __doc__
    """ utils_compare_versions(a:str, b:str) -> int """
    return 0

def utils_is_category_name(category_name): # real signature unknown; restored from __doc__
    """ utils_is_category_name(category_name:str) -> bool """
    return False

def utils_is_desktop_environment(desktop): # real signature unknown; restored from __doc__
    """ utils_is_desktop_environment(desktop:str) -> bool """
    return False

def utils_is_tld(tld): # real signature unknown; restored from __doc__
    """ utils_is_tld(tld:str) -> bool """
    return False

def utils_locale_is_compatible(locale1, locale2): # real signature unknown; restored from __doc__
    """ utils_locale_is_compatible(locale1:str, locale2:str) -> bool """
    return False

def utils_sort_components_into_categories(cpts, categories, check_duplicates): # real signature unknown; restored from __doc__
    """ utils_sort_components_into_categories(cpts:list, categories:list, check_duplicates:bool) """
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

from .Agreement import Agreement
from .AgreementClass import AgreementClass
from .AgreementKind import AgreementKind
from .AgreementSection import AgreementSection
from .AgreementSectionClass import AgreementSectionClass
from .Artifact import Artifact
from .ArtifactClass import ArtifactClass
from .ArtifactKind import ArtifactKind
from .Bundle import Bundle
from .BundleClass import BundleClass
from .BundleKind import BundleKind
from .CacheFlags import CacheFlags
from .Category import Category
from .CategoryClass import CategoryClass
from .Checksum import Checksum
from .ChecksumClass import ChecksumClass
from .ChecksumKind import ChecksumKind
from .Component import Component
from .ComponentClass import ComponentClass
from .ComponentKind import ComponentKind
from .ComponentScope import ComponentScope
from .ContentRating import ContentRating
from .ContentRatingClass import ContentRatingClass
from .ContentRatingValue import ContentRatingValue
from .Context import Context
from .ContextClass import ContextClass
from .DistroDetails import DistroDetails
from .DistroDetailsClass import DistroDetailsClass
from .FormatKind import FormatKind
from .FormatStyle import FormatStyle
from .FormatVersion import FormatVersion
from .Icon import Icon
from .IconClass import IconClass
from .IconKind import IconKind
from .Image import Image
from .ImageClass import ImageClass
from .ImageKind import ImageKind
from .Issue import Issue
from .IssueClass import IssueClass
from .IssueKind import IssueKind
from .IssueSeverity import IssueSeverity
from .Launchable import Launchable
from .LaunchableClass import LaunchableClass
from .LaunchableKind import LaunchableKind
from .MergeKind import MergeKind
from .Metadata import Metadata
from .MetadataClass import MetadataClass
from .MetadataError import MetadataError
from .ParseFlags import ParseFlags
from .Pool import Pool
from .PoolClass import PoolClass
from .PoolError import PoolError
from .PoolFlags import PoolFlags
from .Provided import Provided
from .ProvidedClass import ProvidedClass
from .ProvidedKind import ProvidedKind
from .Relation import Relation
from .RelationClass import RelationClass
from .RelationCompare import RelationCompare
from .RelationItemKind import RelationItemKind
from .RelationKind import RelationKind
from .Release import Release
from .ReleaseClass import ReleaseClass
from .ReleaseKind import ReleaseKind
from .ReleaseUrlKind import ReleaseUrlKind
from .Screenshot import Screenshot
from .ScreenshotClass import ScreenshotClass
from .ScreenshotKind import ScreenshotKind
from .ScreenshotMediaKind import ScreenshotMediaKind
from .SizeKind import SizeKind
from .Suggested import Suggested
from .SuggestedClass import SuggestedClass
from .SuggestedKind import SuggestedKind
from .Translation import Translation
from .TranslationClass import TranslationClass
from .TranslationKind import TranslationKind
from .UrgencyKind import UrgencyKind
from .UrlKind import UrlKind
from .Validator import Validator
from .ValidatorClass import ValidatorClass
from .ValidatorIssue import ValidatorIssue
from .ValidatorIssueClass import ValidatorIssueClass
from .ValueFlags import ValueFlags
from .Video import Video
from .VideoClass import VideoClass
from .VideoCodecKind import VideoCodecKind
from .VideoContainerKind import VideoContainerKind
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f7543853d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/AppStream-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.AppStream', loader=<gi.importer.DynamicImporter object at 0x7f7543853d00>)"

