# encoding: utf-8
# module gi.repository.PackageKitGlib
# from /usr/lib64/girepository-1.0/PackageKitGlib-1.0.typelib
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

DBUS_INTERFACE = 'org.freedesktop.PackageKit'

DBUS_INTERFACE_OFFLINE = 'org.freedesktop.PackageKit.Offline'
DBUS_INTERFACE_TRANSACTION = 'org.freedesktop.PackageKit.Transaction'

DBUS_PATH = '/org/freedesktop/PackageKit'
DBUS_SERVICE = 'org.freedesktop.PackageKit'

DESKTOP_DEFAULT_APPLICATION_DIR = '/usr/share/applications'

MAJOR_VERSION = 1

MICRO_VERSION = 13

MINOR_VERSION = 1

OFFLINE_DESTDIR = ''

OFFLINE_RESULTS_GROUP = 'PackageKit Offline Update Results'

PACKAGE_IDS_DELIM = '&'

PACKAGE_ID_ARCH = 2
PACKAGE_ID_DATA = 3
PACKAGE_ID_NAME = 0
PACKAGE_ID_VERSION = 1

SYSTEM_PACKAGE_CACHE_FILENAME = '/var/lib/PackageKit/package-cache.db'

SYSTEM_PACKAGE_LIST_FILENAME = '/var/lib/PackageKit/system.package-list'

_namespace = 'PackageKitGlib'

_version = '1.0'

__weakref__ = None

# functions

def authorize_type_enum_from_string(authorize_type): # real signature unknown; restored from __doc__
    """ authorize_type_enum_from_string(authorize_type:str) -> PackageKitGlib.AuthorizeEnum """
    pass

def authorize_type_enum_to_string(authorize_type): # real signature unknown; restored from __doc__
    """ authorize_type_enum_to_string(authorize_type:PackageKitGlib.AuthorizeEnum) -> str """
    return ""

def client_error_quark(): # real signature unknown; restored from __doc__
    """ client_error_quark() -> int """
    return 0

def control_error_quark(): # real signature unknown; restored from __doc__
    """ control_error_quark() -> int """
    return 0

def debug_add_log_domain(log_domain): # real signature unknown; restored from __doc__
    """ debug_add_log_domain(log_domain:str) """
    pass

def debug_is_verbose(): # real signature unknown; restored from __doc__
    """ debug_is_verbose() -> bool """
    return False

def debug_set_verbose(verbose): # real signature unknown; restored from __doc__
    """ debug_set_verbose(verbose:bool) """
    pass

def distro_upgrade_enum_from_string(upgrade): # real signature unknown; restored from __doc__
    """ distro_upgrade_enum_from_string(upgrade:str) -> PackageKitGlib.DistroUpgradeEnum """
    pass

def distro_upgrade_enum_to_string(upgrade): # real signature unknown; restored from __doc__
    """ distro_upgrade_enum_to_string(upgrade:PackageKitGlib.DistroUpgradeEnum) -> str """
    return ""

def enum_find_string(table, value): # real signature unknown; restored from __doc__
    """ enum_find_string(table:PackageKitGlib.EnumMatch, value:int) -> str """
    return ""

def enum_find_value(table, string): # real signature unknown; restored from __doc__
    """ enum_find_value(table:PackageKitGlib.EnumMatch, string:str) -> int """
    return 0

def error_enum_from_string(code): # real signature unknown; restored from __doc__
    """ error_enum_from_string(code:str) -> PackageKitGlib.ErrorEnum """
    pass

def error_enum_to_string(code): # real signature unknown; restored from __doc__
    """ error_enum_to_string(code:PackageKitGlib.ErrorEnum) -> str """
    return ""

def exit_enum_from_string(exit): # real signature unknown; restored from __doc__
    """ exit_enum_from_string(exit:str) -> PackageKitGlib.ExitEnum """
    pass

def exit_enum_to_string(exit): # real signature unknown; restored from __doc__
    """ exit_enum_to_string(exit:PackageKitGlib.ExitEnum) -> str """
    return ""

def filter_bitfield_from_string(filters): # real signature unknown; restored from __doc__
    """ filter_bitfield_from_string(filters:str) -> int """
    return 0

def filter_bitfield_to_string(filters): # real signature unknown; restored from __doc__
    """ filter_bitfield_to_string(filters:int) -> str """
    return ""

def filter_enum_from_string(filter): # real signature unknown; restored from __doc__
    """ filter_enum_from_string(filter:str) -> PackageKitGlib.FilterEnum """
    pass

def filter_enum_to_string(filter): # real signature unknown; restored from __doc__
    """ filter_enum_to_string(filter:PackageKitGlib.FilterEnum) -> str """
    return ""

def get_distro_id(): # real signature unknown; restored from __doc__
    """ get_distro_id() -> str """
    return ""

def group_bitfield_from_string(groups): # real signature unknown; restored from __doc__
    """ group_bitfield_from_string(groups:str) -> int """
    return 0

def group_bitfield_to_string(groups): # real signature unknown; restored from __doc__
    """ group_bitfield_to_string(groups:int) -> str """
    return ""

def group_enum_from_string(group): # real signature unknown; restored from __doc__
    """ group_enum_from_string(group:str) -> PackageKitGlib.GroupEnum """
    pass

def group_enum_to_string(group): # real signature unknown; restored from __doc__
    """ group_enum_to_string(group:PackageKitGlib.GroupEnum) -> str """
    return ""

def info_enum_from_string(info): # real signature unknown; restored from __doc__
    """ info_enum_from_string(info:str) -> PackageKitGlib.InfoEnum """
    pass

def info_enum_to_localised_past(info): # real signature unknown; restored from __doc__
    """ info_enum_to_localised_past(info:PackageKitGlib.InfoEnum) -> str """
    return ""

def info_enum_to_localised_present(info): # real signature unknown; restored from __doc__
    """ info_enum_to_localised_present(info:PackageKitGlib.InfoEnum) -> str """
    return ""

def info_enum_to_string(info): # real signature unknown; restored from __doc__
    """ info_enum_to_string(info:PackageKitGlib.InfoEnum) -> str """
    return ""

def iso8601_from_date(date): # real signature unknown; restored from __doc__
    """ iso8601_from_date(date:GLib.Date) -> str """
    return ""

def iso8601_present(): # real signature unknown; restored from __doc__
    """ iso8601_present() -> str """
    return ""

def media_type_enum_from_string(media_type): # real signature unknown; restored from __doc__
    """ media_type_enum_from_string(media_type:str) -> PackageKitGlib.MediaTypeEnum """
    pass

def media_type_enum_to_string(media_type): # real signature unknown; restored from __doc__
    """ media_type_enum_to_string(media_type:PackageKitGlib.MediaTypeEnum) -> str """
    return ""

def network_enum_from_string(network): # real signature unknown; restored from __doc__
    """ network_enum_from_string(network:str) -> PackageKitGlib.NetworkEnum """
    pass

def network_enum_to_string(network): # real signature unknown; restored from __doc__
    """ network_enum_to_string(network:PackageKitGlib.NetworkEnum) -> str """
    return ""

def offline_action_from_string(action): # real signature unknown; restored from __doc__
    """ offline_action_from_string(action:str) -> PackageKitGlib.OfflineAction """
    pass

def offline_action_to_string(action): # real signature unknown; restored from __doc__
    """ offline_action_to_string(action:PackageKitGlib.OfflineAction) -> str """
    return ""

def offline_auth_cancel(): # real signature unknown; restored from __doc__
    """ offline_auth_cancel() -> bool """
    return False

def offline_auth_clear_results(): # real signature unknown; restored from __doc__
    """ offline_auth_clear_results() -> bool """
    return False

def offline_auth_invalidate(): # real signature unknown; restored from __doc__
    """ offline_auth_invalidate() -> bool """
    return False

def offline_auth_set_action(action): # real signature unknown; restored from __doc__
    """ offline_auth_set_action(action:PackageKitGlib.OfflineAction) -> bool """
    return False

def offline_auth_set_prepared_ids(package_ids): # real signature unknown; restored from __doc__
    """ offline_auth_set_prepared_ids(package_ids:str) -> bool """
    return False

def offline_auth_set_prepared_upgrade(name, release_ver): # real signature unknown; restored from __doc__
    """ offline_auth_set_prepared_upgrade(name:str, release_ver:str) -> bool """
    return False

def offline_auth_set_results(results): # real signature unknown; restored from __doc__
    """ offline_auth_set_results(results:PackageKitGlib.Results) -> bool """
    return False

def offline_auth_trigger(action): # real signature unknown; restored from __doc__
    """ offline_auth_trigger(action:PackageKitGlib.OfflineAction) -> bool """
    return False

def offline_auth_trigger_upgrade(action): # real signature unknown; restored from __doc__
    """ offline_auth_trigger_upgrade(action:PackageKitGlib.OfflineAction) -> bool """
    return False

def offline_cancel(cancellable=None): # real signature unknown; restored from __doc__
    """ offline_cancel(cancellable:Gio.Cancellable=None) -> bool """
    return False

def offline_clear_results(cancellable=None): # real signature unknown; restored from __doc__
    """ offline_clear_results(cancellable:Gio.Cancellable=None) -> bool """
    return False

def offline_error_quark(): # real signature unknown; restored from __doc__
    """ offline_error_quark() -> int """
    return 0

def offline_get_action(): # real signature unknown; restored from __doc__
    """ offline_get_action() -> PackageKitGlib.OfflineAction """
    pass

def offline_get_action_monitor(cancellable=None): # real signature unknown; restored from __doc__
    """ offline_get_action_monitor(cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
    pass

def offline_get_prepared_ids(): # real signature unknown; restored from __doc__
    """ offline_get_prepared_ids() -> list """
    return []

def offline_get_prepared_monitor(cancellable=None): # real signature unknown; restored from __doc__
    """ offline_get_prepared_monitor(cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
    pass

def offline_get_prepared_sack(): # real signature unknown; restored from __doc__
    """ offline_get_prepared_sack() -> PackageKitGlib.PackageSack """
    pass

def offline_get_prepared_upgrade(name, release_ver): # real signature unknown; restored from __doc__
    """ offline_get_prepared_upgrade(name:str, release_ver:str) -> bool """
    return False

def offline_get_prepared_upgrade_monitor(cancellable=None): # real signature unknown; restored from __doc__
    """ offline_get_prepared_upgrade_monitor(cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
    pass

def offline_get_prepared_upgrade_name(): # real signature unknown; restored from __doc__
    """ offline_get_prepared_upgrade_name() -> str """
    return ""

def offline_get_prepared_upgrade_version(): # real signature unknown; restored from __doc__
    """ offline_get_prepared_upgrade_version() -> str """
    return ""

def offline_get_results(): # real signature unknown; restored from __doc__
    """ offline_get_results() -> PackageKitGlib.Results """
    pass

def offline_get_results_mtime(): # real signature unknown; restored from __doc__
    """ offline_get_results_mtime() -> int """
    return 0

def offline_trigger(action, cancellable=None): # real signature unknown; restored from __doc__
    """ offline_trigger(action:PackageKitGlib.OfflineAction, cancellable:Gio.Cancellable=None) -> bool """
    return False

def offline_trigger_upgrade(action, cancellable=None): # real signature unknown; restored from __doc__
    """ offline_trigger_upgrade(action:PackageKitGlib.OfflineAction, cancellable:Gio.Cancellable=None) -> bool """
    return False

def polkit_agent_close(): # real signature unknown; restored from __doc__
    """ polkit_agent_close() """
    pass

def polkit_agent_open(): # real signature unknown; restored from __doc__
    """ polkit_agent_open() -> int """
    return 0

def ptr_array_to_strv(array): # real signature unknown; restored from __doc__
    """ ptr_array_to_strv(array:list) -> list """
    return []

def restart_enum_from_string(restart): # real signature unknown; restored from __doc__
    """ restart_enum_from_string(restart:str) -> PackageKitGlib.RestartEnum """
    pass

def restart_enum_to_string(restart): # real signature unknown; restored from __doc__
    """ restart_enum_to_string(restart:PackageKitGlib.RestartEnum) -> str """
    return ""

def role_bitfield_from_string(roles): # real signature unknown; restored from __doc__
    """ role_bitfield_from_string(roles:str) -> int """
    return 0

def role_bitfield_to_string(roles): # real signature unknown; restored from __doc__
    """ role_bitfield_to_string(roles:int) -> str """
    return ""

def role_enum_from_string(role): # real signature unknown; restored from __doc__
    """ role_enum_from_string(role:str) -> PackageKitGlib.RoleEnum """
    pass

def role_enum_to_localised_present(role): # real signature unknown; restored from __doc__
    """ role_enum_to_localised_present(role:PackageKitGlib.RoleEnum) -> str """
    return ""

def role_enum_to_string(role): # real signature unknown; restored from __doc__
    """ role_enum_to_string(role:PackageKitGlib.RoleEnum) -> str """
    return ""

def sig_type_enum_from_string(sig_type): # real signature unknown; restored from __doc__
    """ sig_type_enum_from_string(sig_type:str) -> PackageKitGlib.SigTypeEnum """
    pass

def sig_type_enum_to_string(sig_type): # real signature unknown; restored from __doc__
    """ sig_type_enum_to_string(sig_type:PackageKitGlib.SigTypeEnum) -> str """
    return ""

def status_enum_from_string(status): # real signature unknown; restored from __doc__
    """ status_enum_from_string(status:str) -> PackageKitGlib.StatusEnum """
    pass

def status_enum_to_localised_text(status): # real signature unknown; restored from __doc__
    """ status_enum_to_localised_text(status:PackageKitGlib.StatusEnum) -> str """
    return ""

def status_enum_to_string(status): # real signature unknown; restored from __doc__
    """ status_enum_to_string(status:PackageKitGlib.StatusEnum) -> str """
    return ""

def transaction_flag_bitfield_from_string(transaction_flags): # real signature unknown; restored from __doc__
    """ transaction_flag_bitfield_from_string(transaction_flags:str) -> int """
    return 0

def transaction_flag_bitfield_to_string(transaction_flags): # real signature unknown; restored from __doc__
    """ transaction_flag_bitfield_to_string(transaction_flags:int) -> str """
    return ""

def transaction_flag_enum_from_string(transaction_flag): # real signature unknown; restored from __doc__
    """ transaction_flag_enum_from_string(transaction_flag:str) -> PackageKitGlib.TransactionFlagEnum """
    pass

def transaction_flag_enum_to_string(transaction_flag): # real signature unknown; restored from __doc__
    """ transaction_flag_enum_to_string(transaction_flag:PackageKitGlib.TransactionFlagEnum) -> str """
    return ""

def update_state_enum_from_string(update_state): # real signature unknown; restored from __doc__
    """ update_state_enum_from_string(update_state:str) -> PackageKitGlib.UpdateStateEnum """
    pass

def update_state_enum_to_string(update_state): # real signature unknown; restored from __doc__
    """ update_state_enum_to_string(update_state:PackageKitGlib.UpdateStateEnum) -> str """
    return ""

def upgrade_kind_enum_from_string(upgrade_kind): # real signature unknown; restored from __doc__
    """ upgrade_kind_enum_from_string(upgrade_kind:str) -> PackageKitGlib.UpgradeKindEnum """
    pass

def upgrade_kind_enum_to_string(upgrade_kind): # real signature unknown; restored from __doc__
    """ upgrade_kind_enum_to_string(upgrade_kind:PackageKitGlib.UpgradeKindEnum) -> str """
    return ""

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

from .AuthorizeEnum import AuthorizeEnum
from .Source import Source
from .Category import Category
from .CategoryClass import CategoryClass
from .CategoryPrivate import CategoryPrivate
from .Client import Client
from .ClientClass import ClientClass
from .ClientError import ClientError
from .ClientHelper import ClientHelper
from .ClientHelperClass import ClientHelperClass
from .ClientHelperPrivate import ClientHelperPrivate
from .ClientPrivate import ClientPrivate
from .Control import Control
from .ControlClass import ControlClass
from .ControlError import ControlError
from .ControlPrivate import ControlPrivate
from .Desktop import Desktop
from .DesktopClass import DesktopClass
from .DesktopPrivate import DesktopPrivate
from .Details import Details
from .DetailsClass import DetailsClass
from .DetailsPrivate import DetailsPrivate
from .DistroUpgrade import DistroUpgrade
from .DistroUpgradeClass import DistroUpgradeClass
from .DistroUpgradeEnum import DistroUpgradeEnum
from .DistroUpgradePrivate import DistroUpgradePrivate
from .EnumMatch import EnumMatch
from .Error import Error
from .ErrorClass import ErrorClass
from .ErrorEnum import ErrorEnum
from .ErrorPrivate import ErrorPrivate
from .EulaRequired import EulaRequired
from .EulaRequiredClass import EulaRequiredClass
from .EulaRequiredPrivate import EulaRequiredPrivate
from .ExitEnum import ExitEnum
from .Files import Files
from .FilesClass import FilesClass
from .FilesPrivate import FilesPrivate
from .FilterEnum import FilterEnum
from .GroupEnum import GroupEnum
from .InfoEnum import InfoEnum
from .ItemProgress import ItemProgress
from .ItemProgressClass import ItemProgressClass
from .ItemProgressPrivate import ItemProgressPrivate
from .MediaChangeRequired import MediaChangeRequired
from .MediaChangeRequiredClass import MediaChangeRequiredClass
from .MediaChangeRequiredPrivate import MediaChangeRequiredPrivate
from .MediaTypeEnum import MediaTypeEnum
from .NetworkEnum import NetworkEnum
from .OfflineAction import OfflineAction
from .OfflineError import OfflineError
from .Package import Package
from .PackageClass import PackageClass
from .PackagePrivate import PackagePrivate
from .PackageSack import PackageSack
from .PackageSackClass import PackageSackClass
from .PackageSackPrivate import PackageSackPrivate
from .PackageSackResults import PackageSackResults
from .PackageSackSortType import PackageSackSortType
from .Progress import Progress
from .ProgressClass import ProgressClass
from .ProgressPrivate import ProgressPrivate
from .ProgressType import ProgressType
from .RepoDetail import RepoDetail
from .RepoDetailClass import RepoDetailClass
from .RepoDetailPrivate import RepoDetailPrivate
from .RepoSignatureRequired import RepoSignatureRequired
from .RepoSignatureRequiredClass import RepoSignatureRequiredClass
from .RepoSignatureRequiredPrivate import RepoSignatureRequiredPrivate
from .RequireRestart import RequireRestart
from .RequireRestartClass import RequireRestartClass
from .RequireRestartPrivate import RequireRestartPrivate
from .RestartEnum import RestartEnum
from .Results import Results
from .ResultsClass import ResultsClass
from .ResultsPrivate import ResultsPrivate
from .RoleEnum import RoleEnum
from .SigTypeEnum import SigTypeEnum
from .SourceClass import SourceClass
from .SourcePrivate import SourcePrivate
from .StatusEnum import StatusEnum
from .Task import Task
from .TaskClass import TaskClass
from .TaskPrivate import TaskPrivate
from .TransactionFlagEnum import TransactionFlagEnum
from .TransactionList import TransactionList
from .TransactionListClass import TransactionListClass
from .TransactionListPrivate import TransactionListPrivate
from .TransactionPast import TransactionPast
from .TransactionPastClass import TransactionPastClass
from .TransactionPastPrivate import TransactionPastPrivate
from .UpdateDetail import UpdateDetail
from .UpdateDetailClass import UpdateDetailClass
from .UpdateDetailPrivate import UpdateDetailPrivate
from .UpdateStateEnum import UpdateStateEnum
from .UpgradeKindEnum import UpgradeKindEnum
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f12209a5d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/PackageKitGlib-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.PackageKitGlib', loader=<gi.importer.DynamicImporter object at 0x7f12209a5d00>)"

