# encoding: utf-8
# module gi.repository.Secret
# from /usr/lib64/girepository-1.0/Secret-1.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gobject as __gobject


# Variables with simple values

BACKEND_EXTENSION_POINT_NAME = 'secret-backend'

COLLECTION_DEFAULT = 'default'
COLLECTION_SESSION = 'session'

MAJOR_VERSION = 0

MICRO_VERSION = 3

MINOR_VERSION = 20

_namespace = 'Secret'

_version = '1'

__weakref__ = None

# functions

def backend_get(flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ backend_get(flags:Secret.BackendFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def backend_get_finish(result): # real signature unknown; restored from __doc__
    """ backend_get_finish(result:Gio.AsyncResult) -> Secret.Backend """
    pass

def error_get_quark(): # real signature unknown; restored from __doc__
    """ error_get_quark() -> int """
    return 0

def get_schema(type): # real signature unknown; restored from __doc__
    """ get_schema(type:Secret.SchemaType) -> Secret.Schema """
    pass

def password_clear(schema=None, attributes, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ password_clear(schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def password_clear_finish(result): # real signature unknown; restored from __doc__
    """ password_clear_finish(result:Gio.AsyncResult) -> bool """
    return False

def password_clear_sync(schema=None, attributes, cancellable=None): # real signature unknown; restored from __doc__
    """ password_clear_sync(schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None) -> bool """
    return False

def password_lookup(schema=None, attributes, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ password_lookup(schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def password_lookup_finish(result): # real signature unknown; restored from __doc__
    """ password_lookup_finish(result:Gio.AsyncResult) -> str """
    return ""

def password_lookup_sync(schema=None, attributes, cancellable=None): # real signature unknown; restored from __doc__
    """ password_lookup_sync(schema:Secret.Schema=None, attributes:dict, cancellable:Gio.Cancellable=None) -> str """
    return ""

def password_search(schema=None, attributes, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ password_search(schema:Secret.Schema=None, attributes:dict, flags:Secret.SearchFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def password_search_finish(result): # real signature unknown; restored from __doc__
    """ password_search_finish(result:Gio.AsyncResult) -> list """
    return []

def password_search_sync(schema=None, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
    """ password_search_sync(schema:Secret.Schema=None, attributes:dict, flags:Secret.SearchFlags, cancellable:Gio.Cancellable=None) -> list """
    return []

def password_store(schema=None, attributes, collection=None, label, password, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ password_store(schema:Secret.Schema=None, attributes:dict, collection:str=None, label:str, password:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def password_store_binary(schema=None, attributes, collection=None, label, value, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
    """ password_store_binary(schema:Secret.Schema=None, attributes:dict, collection:str=None, label:str, value:Secret.Value, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
    pass

def password_store_binary_sync(schema=None, attributes, collection=None, label, value, cancellable=None): # real signature unknown; restored from __doc__
    """ password_store_binary_sync(schema:Secret.Schema=None, attributes:dict, collection:str=None, label:str, value:Secret.Value, cancellable:Gio.Cancellable=None) -> bool """
    return False

def password_store_finish(result): # real signature unknown; restored from __doc__
    """ password_store_finish(result:Gio.AsyncResult) -> bool """
    return False

def password_store_sync(schema=None, attributes, collection=None, label, password, cancellable=None): # real signature unknown; restored from __doc__
    """ password_store_sync(schema:Secret.Schema=None, attributes:dict, collection:str=None, label:str, password:str, cancellable:Gio.Cancellable=None) -> bool """
    return False

def password_wipe(password=None): # real signature unknown; restored from __doc__
    """ password_wipe(password:str=None) """
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

from .Backend import Backend
from .BackendFlags import BackendFlags
from .BackendInterface import BackendInterface
from .Collection import Collection
from .CollectionClass import CollectionClass
from .CollectionCreateFlags import CollectionCreateFlags
from .CollectionFlags import CollectionFlags
from .CollectionPrivate import CollectionPrivate
from .Error import Error
from .Retrievable import Retrievable
from .Item import Item
from .ItemClass import ItemClass
from .ItemCreateFlags import ItemCreateFlags
from .ItemFlags import ItemFlags
from .ItemPrivate import ItemPrivate
from .Prompt import Prompt
from .PromptClass import PromptClass
from .PromptPrivate import PromptPrivate
from .RetrievableInterface import RetrievableInterface
from .Schema import Schema
from .SchemaAttribute import SchemaAttribute
from .SchemaAttributeType import SchemaAttributeType
from .SchemaFlags import SchemaFlags
from .SchemaType import SchemaType
from .SearchFlags import SearchFlags
from .Service import Service
from .ServiceClass import ServiceClass
from .ServiceFlags import ServiceFlags
from .ServicePrivate import ServicePrivate
from .Value import Value
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7fa0c67f3d00>'

__path__ = [
    '/usr/lib64/girepository-1.0/Secret-1.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Secret', loader=<gi.importer.DynamicImporter object at 0x7fa0c67f3d00>)"

