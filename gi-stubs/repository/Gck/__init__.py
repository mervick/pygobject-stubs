# encoding: utf-8
# module gi.repository.Gck
# from /usr/lib64/girepository-1.0/Gck-1.typelib
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

INVALID = 18446744073709551615

MAJOR_VERSION = 1

MICRO_VERSION = 0

MINOR_VERSION = 0

URI_FOR_MODULE_WITH_VERSION = 24

URI_FOR_OBJECT_ON_TOKEN = 6

URI_FOR_OBJECT_ON_TOKEN_AND_MODULE = 8

VENDOR_CODE = 1195592448

_namespace = 'Gck'

_version = '1'

__weakref__ = None

# functions

def builder_unref(builder=None): # real signature unknown; restored from __doc__
    """ builder_unref(builder=None) """
    pass

def error_get_quark(): # real signature unknown; restored from __doc__
    """ error_get_quark() -> int """
    return 0

def list_get_boxed_type(): # real signature unknown; restored from __doc__
    """ list_get_boxed_type() -> GType """
    pass

def message_from_rv(rv): # real signature unknown; restored from __doc__
    """ message_from_rv(rv:int) -> str """
    return ""

def modules_enumerate_objects(modules, attrs, session_options): # real signature unknown; restored from __doc__
    """ modules_enumerate_objects(modules:list, attrs:Gck.Attributes, session_options:Gck.SessionOptions) -> Gck.Enumerator """
    pass

def modules_enumerate_uri(modules, uri, session_options): # real signature unknown; restored from __doc__
    """ modules_enumerate_uri(modules:list, uri:str, session_options:Gck.SessionOptions) -> Gck.Enumerator """
    pass

def modules_get_slots(modules, token_present): # real signature unknown; restored from __doc__
    """ modules_get_slots(modules:list, token_present:bool) -> list """
    return []

def modules_initialize_registered(cancellable=None): # real signature unknown; restored from __doc__
    """ modules_initialize_registered(cancellable:Gio.Cancellable=None) -> list """
    return []

def modules_initialize_registered_async(cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ modules_initialize_registered_async(cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def modules_initialize_registered_finish(result): # real signature unknown; restored from __doc__
    """ modules_initialize_registered_finish(result:Gio.AsyncResult) -> list """
    return []

def modules_objects_for_uri(modules, uri, session_options): # real signature unknown; restored from __doc__
    """ modules_objects_for_uri(modules:list, uri:str, session_options:Gck.SessionOptions) -> list """
    return []

def modules_object_for_uri(modules, uri, session_options): # real signature unknown; restored from __doc__
    """ modules_object_for_uri(modules:list, uri:str, session_options:Gck.SessionOptions) -> Gck.Object or None """
    pass

def modules_tokens_for_uri(modules, uri): # real signature unknown; restored from __doc__
    """ modules_tokens_for_uri(modules:list, uri:str) -> list """
    return []

def modules_token_for_uri(modules, uri): # real signature unknown; restored from __doc__
    """ modules_token_for_uri(modules:list, uri:str) -> Gck.Slot """
    pass

def objects_from_handle_array(session, object_handles): # real signature unknown; restored from __doc__
    """ objects_from_handle_array(session:Gck.Session, object_handles:list) -> list """
    return []

def slots_enumerate_objects(slots, match, options): # real signature unknown; restored from __doc__
    """ slots_enumerate_objects(slots:list, match:Gck.Attributes, options:Gck.SessionOptions) -> Gck.Enumerator """
    pass

def uri_build(uri_data, flags): # real signature unknown; restored from __doc__
    """ uri_build(uri_data:Gck.UriData, flags:Gck.UriFlags) -> str """
    return ""

def uri_error_get_quark(): # real signature unknown; restored from __doc__
    """ uri_error_get_quark() -> int """
    return 0

def uri_parse(string, flags): # real signature unknown; restored from __doc__
    """ uri_parse(string:str, flags:Gck.UriFlags) -> Gck.UriData """
    pass

def value_to_boolean(value, result): # real signature unknown; restored from __doc__
    """ value_to_boolean(value:list, result:bool) -> bool """
    return False

def value_to_ulong(value, result): # real signature unknown; restored from __doc__
    """ value_to_ulong(value:list, result:int) -> bool """
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

from .Attribute import Attribute
from .Attributes import Attributes
from .Builder import Builder
from .BuilderFlags import BuilderFlags
from .Enumerator import Enumerator
from .EnumeratorClass import EnumeratorClass
from .EnumeratorPrivate import EnumeratorPrivate
from .Error import Error
from .Mechanism import Mechanism
from .MechanismInfo import MechanismInfo
from .Module import Module
from .ModuleClass import ModuleClass
from .ModuleInfo import ModuleInfo
from .ModulePrivate import ModulePrivate
from .Object import Object
from .ObjectCache import ObjectCache
from .ObjectCacheIface import ObjectCacheIface
from .ObjectClass import ObjectClass
from .ObjectPrivate import ObjectPrivate
from .Password import Password
from .PasswordClass import PasswordClass
from .PasswordPrivate import PasswordPrivate
from .Session import Session
from .SessionClass import SessionClass
from .SessionInfo import SessionInfo
from .SessionOptions import SessionOptions
from .SessionPrivate import SessionPrivate
from .Slot import Slot
from .SlotClass import SlotClass
from .SlotInfo import SlotInfo
from .SlotPrivate import SlotPrivate
from .TokenInfo import TokenInfo
from .UriData import UriData
from .UriError import UriError
from .UriFlags import UriFlags
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fc2e6fc0d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Gck-1.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Gck', loader=<gi.importer.DynamicImporter object at 0x7fc2e6fc0d00>)"

