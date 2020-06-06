# encoding: utf-8
# module gi.repository.OSTree
# from /usr/lib64/girepository-1.0/OSTree-1.0.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

BUILT_FEATURES = 'libcurl libsoup gpgme ex-fsverity libarchive selinux openssl libmount systemd release p2p'

COMMIT_GVARIANT_STRING = '(a{sv}aya(say)sstayay)'

COMMIT_META_KEY_COLLECTION_BINDING = 'ostree.collection-binding'

COMMIT_META_KEY_ENDOFLIFE = 'ostree.endoflife'

COMMIT_META_KEY_ENDOFLIFE_REBASE = 'ostree.endoflife-rebase'

COMMIT_META_KEY_REF_BINDING = 'ostree.ref-binding'

COMMIT_META_KEY_SOURCE_TITLE = 'ostree.source-title'

COMMIT_META_KEY_VERSION = 'version'

DIRMETA_GVARIANT_STRING = '(uuua(ayay))'

FILEMETA_GVARIANT_STRING = '(uuua(ayay))'

MAX_METADATA_SIZE = 10485760

MAX_METADATA_WARN_SIZE = 7340032

META_KEY_DEPLOY_COLLECTION_ID = 'ostree.deploy-collection-id'

ORIGIN_TRANSIENT_GROUP = 'libostree-transient'

RELEASE_VERSION = 3

REPO_METADATA_REF = 'ostree-metadata'

SHA256_DIGEST_LEN = 32

SHA256_STRING_LEN = 64

SUMMARY_GVARIANT_STRING = '(a(s(taya{sv}))a{sv})'

SUMMARY_SIG_GVARIANT_STRING = 'a{sv}'

TIMESTAMP = 0

TREE_GVARIANT_STRING = '(a(say)a(sayay))'

VERSION = 2020.3

VERSION_S = '2020.3'

YEAR_VERSION = 2020

_namespace = 'OSTree'

_version = '1.0'

__weakref__ = None

# functions

def break_hardlink(dfd, path, skip_xattrs, cancellable=None): # real signature unknown; restored from __doc__
    """ break_hardlink(dfd:int, path:str, skip_xattrs:bool, cancellable:Gio.Cancellable=None) -> bool """
    return False

def checksum_b64_from_bytes(csum): # real signature unknown; restored from __doc__
    """ checksum_b64_from_bytes(csum:list) -> str """
    return ""

def checksum_b64_to_bytes(checksum): # real signature unknown; restored from __doc__
    """ checksum_b64_to_bytes(checksum:str) -> list """
    return []

def checksum_bytes_peek(bytes): # real signature unknown; restored from __doc__
    """ checksum_bytes_peek(bytes:GLib.Variant) -> list """
    return []

def checksum_bytes_peek_validate(bytes): # real signature unknown; restored from __doc__
    """ checksum_bytes_peek_validate(bytes:GLib.Variant) -> list """
    return []

def checksum_file(f, objtype, cancellable=None): # real signature unknown; restored from __doc__
    """ checksum_file(f:Gio.File, objtype:OSTree.ObjectType, cancellable:Gio.Cancellable=None) -> bool, out_csum:list """
    return False

def checksum_file_async(f, objtype, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ checksum_file_async(f:Gio.File, objtype:OSTree.ObjectType, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def checksum_file_async_finish(f, result): # real signature unknown; restored from __doc__
    """ checksum_file_async_finish(f:Gio.File, result:Gio.AsyncResult) -> bool, out_csum:list """
    return False

def checksum_file_at(dfd, path, stbuf=None, objtype, flags, out_checksum, cancellable=None): # real signature unknown; restored from __doc__
    """ checksum_file_at(dfd:int, path:str, stbuf=None, objtype:OSTree.ObjectType, flags:OSTree.ChecksumFlags, out_checksum:str, cancellable:Gio.Cancellable=None) -> bool """
    return False

def checksum_file_from_input(file_info, xattrs=None, in_=None, objtype, cancellable=None): # real signature unknown; restored from __doc__
    """ checksum_file_from_input(file_info:Gio.FileInfo, xattrs:GLib.Variant=None, in_:Gio.InputStream=None, objtype:OSTree.ObjectType, cancellable:Gio.Cancellable=None) -> bool, out_csum:list """
    return False

def checksum_from_bytes(csum): # real signature unknown; restored from __doc__
    """ checksum_from_bytes(csum:list) -> str """
    return ""

def checksum_from_bytes_v(csum_v): # real signature unknown; restored from __doc__
    """ checksum_from_bytes_v(csum_v:GLib.Variant) -> str """
    return ""

def checksum_inplace_to_bytes(checksum, buf): # real signature unknown; restored from __doc__
    """ checksum_inplace_to_bytes(checksum:str, buf:int) """
    pass

def checksum_to_bytes(checksum): # real signature unknown; restored from __doc__
    """ checksum_to_bytes(checksum:str) -> list """
    return []

def checksum_to_bytes_v(checksum): # real signature unknown; restored from __doc__
    """ checksum_to_bytes_v(checksum:str) -> GLib.Variant """
    pass

def check_version(required_year, required_release): # real signature unknown; restored from __doc__
    """ check_version(required_year:int, required_release:int) -> bool """
    return False

def cmd__private__(): # real signature unknown; restored from __doc__
    """ cmd__private__() -> OSTree.CmdPrivateVTable """
    pass

def cmp_checksum_bytes(a, b): # real signature unknown; restored from __doc__
    """ cmp_checksum_bytes(a:int, b:int) -> int """
    return 0

def collection_ref_dupv(refs): # real signature unknown; restored from __doc__
    """ collection_ref_dupv(refs:list) -> list """
    return []

def collection_ref_equal(ref1, ref2): # real signature unknown; restored from __doc__
    """ collection_ref_equal(ref1, ref2) -> bool """
    return False

def collection_ref_freev(refs): # real signature unknown; restored from __doc__
    """ collection_ref_freev(refs:list) """
    pass

def collection_ref_hash(ref): # real signature unknown; restored from __doc__
    """ collection_ref_hash(ref) -> int """
    return 0

def commit_get_content_checksum(commit_variant): # real signature unknown; restored from __doc__
    """ commit_get_content_checksum(commit_variant:GLib.Variant) -> str or None """
    return ""

def commit_get_object_sizes(commit_variant): # real signature unknown; restored from __doc__
    """ commit_get_object_sizes(commit_variant:GLib.Variant) -> bool, out_sizes_entries:list """
    return False

def commit_get_parent(commit_variant): # real signature unknown; restored from __doc__
    """ commit_get_parent(commit_variant:GLib.Variant) -> str """
    return ""

def commit_get_timestamp(commit_variant): # real signature unknown; restored from __doc__
    """ commit_get_timestamp(commit_variant:GLib.Variant) -> int """
    return 0

def content_file_parse(compressed, content_path, trusted, cancellable=None): # real signature unknown; restored from __doc__
    """ content_file_parse(compressed:bool, content_path:Gio.File, trusted:bool, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream, out_file_info:Gio.FileInfo, out_xattrs:GLib.Variant """
    return False

def content_file_parse_at(compressed, parent_dfd, path, trusted, cancellable=None): # real signature unknown; restored from __doc__
    """ content_file_parse_at(compressed:bool, parent_dfd:int, path:str, trusted:bool, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream, out_file_info:Gio.FileInfo, out_xattrs:GLib.Variant """
    return False

def content_stream_parse(compressed, input, input_length, trusted, cancellable=None): # real signature unknown; restored from __doc__
    """ content_stream_parse(compressed:bool, input:Gio.InputStream, input_length:int, trusted:bool, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream, out_file_info:Gio.FileInfo, out_xattrs:GLib.Variant """
    return False

def create_directory_metadata(dir_info, xattrs=None): # real signature unknown; restored from __doc__
    """ create_directory_metadata(dir_info:Gio.FileInfo, xattrs:GLib.Variant=None) -> GLib.Variant """
    pass

def diff_dirs(flags, a, b, modified, removed, added, cancellable=None): # real signature unknown; restored from __doc__
    """ diff_dirs(flags:OSTree.DiffFlags, a:Gio.File, b:Gio.File, modified:list, removed:list, added:list, cancellable:Gio.Cancellable=None) -> bool """
    return False

def diff_dirs_with_options(flags, a, b, modified, removed, added, options=None, cancellable=None): # real signature unknown; restored from __doc__
    """ diff_dirs_with_options(flags:OSTree.DiffFlags, a:Gio.File, b:Gio.File, modified:list, removed:list, added:list, options:OSTree.DiffDirsOptions=None, cancellable:Gio.Cancellable=None) -> bool """
    return False

def diff_print(a, b, modified, removed, added): # real signature unknown; restored from __doc__
    """ diff_print(a:Gio.File, b:Gio.File, modified:list, removed:list, added:list) """
    pass

def gpg_error_quark(): # real signature unknown; restored from __doc__
    """ gpg_error_quark() -> int """
    return 0

def hash_object_name(a=None): # real signature unknown; restored from __doc__
    """ hash_object_name(a=None) -> int """
    return 0

def kernel_args_cleanup(loc=None): # real signature unknown; restored from __doc__
    """ kernel_args_cleanup(loc=None) """
    pass

def metadata_variant_type(objtype): # real signature unknown; restored from __doc__
    """ metadata_variant_type(objtype:OSTree.ObjectType) -> GLib.VariantType """
    pass

def object_from_string(p_str): # real signature unknown; restored from __doc__
    """ object_from_string(str:str) -> out_checksum:str, out_objtype:OSTree.ObjectType """
    pass

def object_name_deserialize(variant): # real signature unknown; restored from __doc__
    """ object_name_deserialize(variant:GLib.Variant) -> out_checksum:str, out_objtype:OSTree.ObjectType """
    pass

def object_name_serialize(checksum, objtype): # real signature unknown; restored from __doc__
    """ object_name_serialize(checksum:str, objtype:OSTree.ObjectType) -> GLib.Variant """
    pass

def object_to_string(checksum, objtype): # real signature unknown; restored from __doc__
    """ object_to_string(checksum:str, objtype:OSTree.ObjectType) -> str """
    return ""

def object_type_from_string(p_str): # real signature unknown; restored from __doc__
    """ object_type_from_string(str:str) -> OSTree.ObjectType """
    pass

def object_type_to_string(objtype): # real signature unknown; restored from __doc__
    """ object_type_to_string(objtype:OSTree.ObjectType) -> str """
    return ""

def parse_refspec(refspec): # real signature unknown; restored from __doc__
    """ parse_refspec(refspec:str) -> bool, out_remote:str, out_ref:str """
    return False

def raw_file_to_archive_z2_stream(input, file_info, xattrs=None, cancellable=None): # real signature unknown; restored from __doc__
    """ raw_file_to_archive_z2_stream(input:Gio.InputStream, file_info:Gio.FileInfo, xattrs:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream """
    return False

def raw_file_to_archive_z2_stream_with_options(input, file_info, xattrs=None, options=None, cancellable=None): # real signature unknown; restored from __doc__
    """ raw_file_to_archive_z2_stream_with_options(input:Gio.InputStream, file_info:Gio.FileInfo, xattrs:GLib.Variant=None, options:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream """
    return False

def raw_file_to_content_stream(input, file_info, xattrs=None, cancellable=None): # real signature unknown; restored from __doc__
    """ raw_file_to_content_stream(input:Gio.InputStream, file_info:Gio.FileInfo, xattrs:GLib.Variant=None, cancellable:Gio.Cancellable=None) -> bool, out_input:Gio.InputStream, out_length:int """
    return False

def repo_commit_traverse_iter_cleanup(p=None): # real signature unknown; restored from __doc__
    """ repo_commit_traverse_iter_cleanup(p=None) """
    pass

def repo_finder_resolve_all_async(finders, refs, parent_repo, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ repo_finder_resolve_all_async(finders:list, refs:list, parent_repo:OSTree.Repo, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def repo_finder_resolve_all_finish(result): # real signature unknown; restored from __doc__
    """ repo_finder_resolve_all_finish(result:Gio.AsyncResult) -> list """
    return []

def repo_finder_result_freev(results): # real signature unknown; restored from __doc__
    """ repo_finder_result_freev(results:list) """
    pass

def validate_checksum_string(sha256): # real signature unknown; restored from __doc__
    """ validate_checksum_string(sha256:str) -> bool """
    return False

def validate_collection_id(collection_id=None): # real signature unknown; restored from __doc__
    """ validate_collection_id(collection_id:str=None) -> bool """
    return False

def validate_remote_name(remote_name): # real signature unknown; restored from __doc__
    """ validate_remote_name(remote_name:str) -> bool """
    return False

def validate_rev(rev): # real signature unknown; restored from __doc__
    """ validate_rev(rev:str) -> bool """
    return False

def validate_structureof_checksum_string(checksum): # real signature unknown; restored from __doc__
    """ validate_structureof_checksum_string(checksum:str) -> bool """
    return False

def validate_structureof_commit(commit): # real signature unknown; restored from __doc__
    """ validate_structureof_commit(commit:GLib.Variant) -> bool """
    return False

def validate_structureof_csum_v(checksum): # real signature unknown; restored from __doc__
    """ validate_structureof_csum_v(checksum:GLib.Variant) -> bool """
    return False

def validate_structureof_dirmeta(dirmeta): # real signature unknown; restored from __doc__
    """ validate_structureof_dirmeta(dirmeta:GLib.Variant) -> bool """
    return False

def validate_structureof_dirtree(dirtree): # real signature unknown; restored from __doc__
    """ validate_structureof_dirtree(dirtree:GLib.Variant) -> bool """
    return False

def validate_structureof_file_mode(mode): # real signature unknown; restored from __doc__
    """ validate_structureof_file_mode(mode:int) -> bool """
    return False

def validate_structureof_objtype(objtype): # real signature unknown; restored from __doc__
    """ validate_structureof_objtype(objtype:int) -> bool """
    return False

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

from .AsyncProgress import AsyncProgress
from .AsyncProgressClass import AsyncProgressClass
from .BootconfigParser import BootconfigParser
from .Bootloader import Bootloader
from .BootloaderGrub2 import BootloaderGrub2
from .BootloaderInterface import BootloaderInterface
from .BootloaderSyslinux import BootloaderSyslinux
from .BootloaderUboot import BootloaderUboot
from .BootloaderZipl import BootloaderZipl
from .ChecksumFlags import ChecksumFlags
from .ChecksumInputStream import ChecksumInputStream
from .ChecksumInputStreamClass import ChecksumInputStreamClass
from .ChecksumInputStreamPrivate import ChecksumInputStreamPrivate
from .CmdPrivateVTable import CmdPrivateVTable
from .CollectionRef import CollectionRef
from .CommitSizesEntry import CommitSizesEntry
from .Deployment import Deployment
from .DeploymentUnlockedState import DeploymentUnlockedState
from .DiffDirsOptions import DiffDirsOptions
from .DiffFlags import DiffFlags
from .DiffItem import DiffItem
from .GpgError import GpgError
from .GpgSignatureAttr import GpgSignatureAttr
from .GpgSignatureFormatFlags import GpgSignatureFormatFlags
from .GpgVerifier import GpgVerifier
from .GpgVerifyResult import GpgVerifyResult
from .KernelArgs import KernelArgs
from .KernelArgsEntry import KernelArgsEntry
from .LibarchiveInputStream import LibarchiveInputStream
from .LibarchiveInputStreamClass import LibarchiveInputStreamClass
from .LibarchiveInputStreamPrivate import LibarchiveInputStreamPrivate
from .LzmaCompressor import LzmaCompressor
from .LzmaCompressorClass import LzmaCompressorClass
from .LzmaDecompressor import LzmaDecompressor
from .LzmaDecompressorClass import LzmaDecompressorClass
from .MutableTree import MutableTree
from .MutableTreeClass import MutableTreeClass
from .MutableTreeIter import MutableTreeIter
from .ObjectType import ObjectType
from .Remote import Remote
from .Repo import Repo
from .RepoCheckoutAtOptions import RepoCheckoutAtOptions
from .RepoCheckoutFilterResult import RepoCheckoutFilterResult
from .RepoCheckoutMode import RepoCheckoutMode
from .RepoCheckoutOverwriteMode import RepoCheckoutOverwriteMode
from .RepoCommitFilterResult import RepoCommitFilterResult
from .RepoCommitIterResult import RepoCommitIterResult
from .RepoCommitModifier import RepoCommitModifier
from .RepoCommitModifierFlags import RepoCommitModifierFlags
from .RepoCommitState import RepoCommitState
from .RepoCommitTraverseFlags import RepoCommitTraverseFlags
from .RepoCommitTraverseIter import RepoCommitTraverseIter
from .RepoDevInoCache import RepoDevInoCache
from .RepoFile import RepoFile
from .RepoFileClass import RepoFileClass
from .RepoFileEnumerator import RepoFileEnumerator
from .RepoFileEnumeratorClass import RepoFileEnumeratorClass
from .RepoFinder import RepoFinder
from .RepoFinderAvahi import RepoFinderAvahi
from .RepoFinderAvahiClass import RepoFinderAvahiClass
from .RepoFinderConfig import RepoFinderConfig
from .RepoFinderConfigClass import RepoFinderConfigClass
from .RepoFinderInterface import RepoFinderInterface
from .RepoFinderMount import RepoFinderMount
from .RepoFinderMountClass import RepoFinderMountClass
from .RepoFinderOverride import RepoFinderOverride
from .RepoFinderOverrideClass import RepoFinderOverrideClass
from .RepoFinderResult import RepoFinderResult
from .RepoListObjectsFlags import RepoListObjectsFlags
from .RepoListRefsExtFlags import RepoListRefsExtFlags
from .RepoMode import RepoMode
from .RepoPruneFlags import RepoPruneFlags
from .RepoPruneOptions import RepoPruneOptions
from .RepoPullFlags import RepoPullFlags
from .RepoRemoteChange import RepoRemoteChange
from .RepoResolveRevExtFlags import RepoResolveRevExtFlags
from .RepoTransactionStats import RepoTransactionStats
from .RollsumMatches import RollsumMatches
from .SePolicy import SePolicy
from .SePolicyRestoreconFlags import SePolicyRestoreconFlags
from .StaticDeltaGenerateOpt import StaticDeltaGenerateOpt
from .Sysroot import Sysroot
from .SysrootSimpleWriteDeploymentFlags import SysrootSimpleWriteDeploymentFlags
from .SysrootUpgrader import SysrootUpgrader
from .SysrootUpgraderFlags import SysrootUpgraderFlags
from .SysrootUpgraderPullFlags import SysrootUpgraderPullFlags
from .SysrootWriteDeploymentsOpts import SysrootWriteDeploymentsOpts
from .TlsCertInteraction import TlsCertInteraction
from .TlsCertInteractionClass import TlsCertInteractionClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7feced122d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/OSTree-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.OSTree', loader=<gi.importer.DynamicImporter object at 0x7feced122d00>)"

