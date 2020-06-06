# encoding: utf-8
# module gi.repository.Gcr
# from /usr/lib64/girepository-1.0/Gcr-3.typelib
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
import gi.repository.Gck as __gi_repository_Gck
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


# Variables with simple values

ICON_CERTIFICATE = 'application-certificate'
ICON_GNUPG = 'gcr-gnupg'

ICON_HOME_DIRECTORY = 'user-home'

ICON_KEY = 'gcr-key'

ICON_KEY_PAIR = 'gcr-key-pair'

ICON_PASSWORD = 'gcr-password'

ICON_SMART_CARD = 'gcr-smart-card'

MAJOR_VERSION = 3

MICRO_VERSION = 0

MINOR_VERSION = 36

PURPOSE_CLIENT_AUTH = '1.3.6.1.5.5.7.3.2'

PURPOSE_CODE_SIGNING = '1.3.6.1.5.5.7.3.3'

PURPOSE_EMAIL = '1.3.6.1.5.5.7.3.4'

PURPOSE_SERVER_AUTH = '1.3.6.1.5.5.7.3.1'

SECRET_EXCHANGE_PROTOCOL_1 = 'sx-aes-1'

UNLOCK_OPTION_ALWAYS = 'always'
UNLOCK_OPTION_IDLE = 'idle'
UNLOCK_OPTION_SESSION = 'session'
UNLOCK_OPTION_TIMEOUT = 'timeout'

_namespace = 'Gcr'

_version = '3'

__weakref__ = None

# functions

def certificate_compare(first=None, other=None): # real signature unknown; restored from __doc__
    """ certificate_compare(first:Gcr.Comparable=None, other:Gcr.Comparable=None) -> int """
    return 0

def data_error_get_domain(): # real signature unknown; restored from __doc__
    """ data_error_get_domain() -> int """
    return 0

def fingerprint_from_attributes(attrs, checksum_type): # real signature unknown; restored from __doc__
    """ fingerprint_from_attributes(attrs:Gck.Attributes, checksum_type:GLib.ChecksumType) -> list or None, n_fingerprint:int """
    return []

def fingerprint_from_subject_public_key_info(key_info, checksum_type): # real signature unknown; restored from __doc__
    """ fingerprint_from_subject_public_key_info(key_info:list, checksum_type:GLib.ChecksumType) -> list or None, n_fingerprint:int """
    return []

def icon_for_token(token_info): # real signature unknown; restored from __doc__
    """ icon_for_token(token_info:Gck.TokenInfo) -> Gio.Icon """
    pass

def importer_create_for_parsed(parsed): # real signature unknown; restored from __doc__
    """ importer_create_for_parsed(parsed:Gcr.Parsed) -> list """
    return []

def importer_queue_and_filter_for_parsed(importers, parsed): # real signature unknown; restored from __doc__
    """ importer_queue_and_filter_for_parsed(importers:list, parsed:Gcr.Parsed) -> list """
    return []

def importer_register(importer_type, attrs): # real signature unknown; restored from __doc__
    """ importer_register(importer_type:GType, attrs:Gck.Attributes) """
    pass

def importer_register_well_known(): # real signature unknown; restored from __doc__
    """ importer_register_well_known() """
    pass

def mock_prompter_disconnect(): # real signature unknown; restored from __doc__
    """ mock_prompter_disconnect() """
    pass

def mock_prompter_expect_close(): # real signature unknown; restored from __doc__
    """ mock_prompter_expect_close() """
    pass

def mock_prompter_expect_confirm_cancel(): # real signature unknown; restored from __doc__
    """ mock_prompter_expect_confirm_cancel() """
    pass

def mock_prompter_expect_password_cancel(): # real signature unknown; restored from __doc__
    """ mock_prompter_expect_password_cancel() """
    pass

def mock_prompter_get_delay_msec(): # real signature unknown; restored from __doc__
    """ mock_prompter_get_delay_msec() -> int """
    return 0

def mock_prompter_is_expecting(): # real signature unknown; restored from __doc__
    """ mock_prompter_is_expecting() -> bool """
    return False

def mock_prompter_is_prompting(): # real signature unknown; restored from __doc__
    """ mock_prompter_is_prompting() -> bool """
    return False

def mock_prompter_set_delay_msec(delay_msec): # real signature unknown; restored from __doc__
    """ mock_prompter_set_delay_msec(delay_msec:int) """
    pass

def mock_prompter_start(): # real signature unknown; restored from __doc__
    """ mock_prompter_start() -> str """
    return ""

def mock_prompter_stop(): # real signature unknown; restored from __doc__
    """ mock_prompter_stop() """
    pass

def parsed_unref(parsed=None): # real signature unknown; restored from __doc__
    """ parsed_unref(parsed=None) """
    pass

def pkcs11_add_module(module): # real signature unknown; restored from __doc__
    """ pkcs11_add_module(module:Gck.Module) """
    pass

def pkcs11_add_module_from_file(module_path, unused=None): # real signature unknown; restored from __doc__
    """ pkcs11_add_module_from_file(module_path:str, unused=None) -> bool """
    return False

def pkcs11_get_modules(): # real signature unknown; restored from __doc__
    """ pkcs11_get_modules() -> list """
    return []

def pkcs11_get_trust_lookup_slots(): # real signature unknown; restored from __doc__
    """ pkcs11_get_trust_lookup_slots() -> list """
    return []

def pkcs11_get_trust_lookup_uris(): # real signature unknown; restored from __doc__
    """ pkcs11_get_trust_lookup_uris() -> list or None """
    return []

def pkcs11_get_trust_store_slot(): # real signature unknown; restored from __doc__
    """ pkcs11_get_trust_store_slot() -> Gck.Slot or None """
    pass

def pkcs11_get_trust_store_uri(): # real signature unknown; restored from __doc__
    """ pkcs11_get_trust_store_uri() -> str or None """
    return ""

def pkcs11_initialize(cancellable=None): # real signature unknown; restored from __doc__
    """ pkcs11_initialize(cancellable:Gio.Cancellable=None) -> bool """
    return False

def pkcs11_initialize_async(cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ pkcs11_initialize_async(cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def pkcs11_initialize_finish(result): # real signature unknown; restored from __doc__
    """ pkcs11_initialize_finish(result:Gio.AsyncResult) -> bool """
    return False

def pkcs11_set_modules(modules): # real signature unknown; restored from __doc__
    """ pkcs11_set_modules(modules:list) """
    pass

def pkcs11_set_trust_lookup_uris(pkcs11_uris=None): # real signature unknown; restored from __doc__
    """ pkcs11_set_trust_lookup_uris(pkcs11_uris:str=None) """
    pass

def pkcs11_set_trust_store_uri(pkcs11_uri=None): # real signature unknown; restored from __doc__
    """ pkcs11_set_trust_store_uri(pkcs11_uri:str=None) """
    pass

def trust_add_pinned_certificate(certificate, purpose, peer, cancellable=None): # real signature unknown; restored from __doc__
    """ trust_add_pinned_certificate(certificate:Gcr.Certificate, purpose:str, peer:str, cancellable:Gio.Cancellable=None) -> bool """
    return False

def trust_add_pinned_certificate_async(certificate, purpose, peer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ trust_add_pinned_certificate_async(certificate:Gcr.Certificate, purpose:str, peer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def trust_add_pinned_certificate_finish(result): # real signature unknown; restored from __doc__
    """ trust_add_pinned_certificate_finish(result:Gio.AsyncResult) -> bool """
    return False

def trust_is_certificate_anchored(certificate, purpose, cancellable=None): # real signature unknown; restored from __doc__
    """ trust_is_certificate_anchored(certificate:Gcr.Certificate, purpose:str, cancellable:Gio.Cancellable=None) -> bool """
    return False

def trust_is_certificate_anchored_async(certificate, purpose, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ trust_is_certificate_anchored_async(certificate:Gcr.Certificate, purpose:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def trust_is_certificate_anchored_finish(result): # real signature unknown; restored from __doc__
    """ trust_is_certificate_anchored_finish(result:Gio.AsyncResult) -> bool """
    return False

def trust_is_certificate_pinned(certificate, purpose, peer, cancellable=None): # real signature unknown; restored from __doc__
    """ trust_is_certificate_pinned(certificate:Gcr.Certificate, purpose:str, peer:str, cancellable:Gio.Cancellable=None) -> bool """
    return False

def trust_is_certificate_pinned_async(certificate, purpose, peer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ trust_is_certificate_pinned_async(certificate:Gcr.Certificate, purpose:str, peer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def trust_is_certificate_pinned_finish(result): # real signature unknown; restored from __doc__
    """ trust_is_certificate_pinned_finish(result:Gio.AsyncResult) -> bool """
    return False

def trust_remove_pinned_certificate(certificate, purpose, peer, cancellable=None): # real signature unknown; restored from __doc__
    """ trust_remove_pinned_certificate(certificate:Gcr.Certificate, purpose:str, peer:str, cancellable:Gio.Cancellable=None) -> bool """
    return False

def trust_remove_pinned_certificate_async(certificate, purpose, peer, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ trust_remove_pinned_certificate_async(certificate:Gcr.Certificate, purpose:str, peer:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def trust_remove_pinned_certificate_finish(result): # real signature unknown; restored from __doc__
    """ trust_remove_pinned_certificate_finish(result:Gio.AsyncResult) -> bool """
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

from .Certificate import Certificate
from .CertificateChain import CertificateChain
from .CertificateChainClass import CertificateChainClass
from .CertificateChainFlags import CertificateChainFlags
from .CertificateChainPrivate import CertificateChainPrivate
from .CertificateChainStatus import CertificateChainStatus
from .CertificateIface import CertificateIface
from .CertificateRequest import CertificateRequest
from .CertificateRequestClass import CertificateRequestClass
from .CertificateRequestFormat import CertificateRequestFormat
from .Collection import Collection
from .CollectionIface import CollectionIface
from .Column import Column
from .ColumnFlags import ColumnFlags
from .Comparable import Comparable
from .ComparableIface import ComparableIface
from .DataError import DataError
from .DataFormat import DataFormat
from .FilterCollection import FilterCollection
from .FilterCollectionClass import FilterCollectionClass
from .FilterCollectionPrivate import FilterCollectionPrivate
from .Importer import Importer
from .ImporterIface import ImporterIface
from .ImportInteraction import ImportInteraction
from .ImportInteractionIface import ImportInteractionIface
from .Parsed import Parsed
from .Parser import Parser
from .ParserClass import ParserClass
from .ParserPrivate import ParserPrivate
from .Pkcs11Certificate import Pkcs11Certificate
from .Pkcs11CertificateClass import Pkcs11CertificateClass
from .Pkcs11CertificatePrivate import Pkcs11CertificatePrivate
from .Prompt import Prompt
from .PromptIface import PromptIface
from .PromptReply import PromptReply
from .SecretExchange import SecretExchange
from .SecretExchangeClass import SecretExchangeClass
from .SecretExchangePrivate import SecretExchangePrivate
from .SimpleCertificate import SimpleCertificate
from .SimpleCertificateClass import SimpleCertificateClass
from .SimpleCertificatePrivate import SimpleCertificatePrivate
from .SimpleCollection import SimpleCollection
from .SimpleCollectionClass import SimpleCollectionClass
from .SimpleCollectionPrivate import SimpleCollectionPrivate
from .SshAskpass import SshAskpass
from .SshAskpassClass import SshAskpassClass
from .SystemPrompt import SystemPrompt
from .SystemPromptClass import SystemPromptClass
from .SystemPrompter import SystemPrompter
from .SystemPrompterClass import SystemPrompterClass
from .SystemPrompterMode import SystemPrompterMode
from .SystemPrompterPrivate import SystemPrompterPrivate
from .SystemPromptError import SystemPromptError
from .SystemPromptPrivate import SystemPromptPrivate
from .UnionCollection import UnionCollection
from .UnionCollectionClass import UnionCollectionClass
from .UnionCollectionPrivate import UnionCollectionPrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7eff9de1fd00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gcr-3.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gcr', loader=<gi.importer.DynamicImporter object at 0x7eff9de1fd00>)"

